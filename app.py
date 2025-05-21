import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mengatur konfigurasi halaman Streamlit
st.set_page_config(layout="wide", page_title="Dashboard APBD Indonesia")
st.title("📊 Dashboard Perbandingan APBD Provinsi se-Indonesia")

# Upload file CSV
uploaded_file = st.file_uploader("Unggah data APBD (.csv)", type="csv")

if uploaded_file is not None:
    # Membaca file CSV yang diunggah
    df = pd.read_csv(uploaded_file)

    # Mengatasi typo pada nama kolom 'Pendpatan' menjadi 'Pendapatan'
    if "Pendpatan" in df.columns:
        df.rename(columns={"Pendpatan": "Pendapatan"}, inplace=True)

    # Memastikan kolom-kolom wajib ada dalam data
    required_columns = {"Provinsi", "Tahun", "Bulan", "Pendapatan", "Belanja"}
    if not required_columns.issubset(df.columns):
        st.error("❌ Kolom harus mencakup: Provinsi, Tahun, Bulan, Pendapatan, Belanja")
    else:
        # Mengubah format angka lokal (dengan titik sebagai ribuan dan koma sebagai desimal) menjadi float
        for kolom in ["Pendapatan", "Belanja"]:
            df[kolom] = (
                df[kolom]
                .astype(str)
                .str.replace(".", "", regex=False)  # Menghapus tanda titik ribuan
                .str.replace(",", ".", regex=False)  # Mengganti koma desimal menjadi titik
                .astype(float)
            )

        # Mengubah nama bulan dari teks ke angka (1-12)
        bulan_mapping = {
            "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
            "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
            "September": 9, "Oktober": 10, "November": 11, "Desember": 12
        }
        df["Bulan"] = df["Bulan"].replace(bulan_mapping)
        df["Bulan"] = df["Bulan"].astype(int)
        df["Tahun"] = df["Tahun"].astype(int)

        # Membuat filter di sidebar untuk memilih tahun dan provinsi
        st.sidebar.header("Filter")
        tahun_terpilih = st.sidebar.multiselect("Pilih Tahun", sorted(df["Tahun"].unique()), default=sorted(df["Tahun"].unique()))
        provinsi_terpilih = st.sidebar.multiselect("Pilih Provinsi", sorted(df["Provinsi"].unique()), default=sorted(df["Provinsi"].unique()))

        # Memfilter data berdasarkan pilihan tahun dan provinsi
        df_filtered = df[df["Tahun"].isin(tahun_terpilih) & df["Provinsi"].isin(provinsi_terpilih)]

        # Menampilkan statistik ringkas total pendapatan dan belanja
        st.subheader("📌 Statistik Ringkas")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Pendapatan (Rp)", f"{df_filtered['Pendapatan'].sum():,.0f}")
        with col2:
            st.metric("Total Belanja (Rp)", f"{df_filtered['Belanja'].sum():,.0f}")

        # ===== Tambahan: Grafik batang =====
        st.subheader("📈 Grafik Pendapatan dan Belanja per Provinsi")

        # Mengelompokkan data berdasarkan provinsi dan menjumlahkan pendapatan dan belanja
        df_grouped = df_filtered.groupby("Provinsi").agg({"Pendapatan": "sum", "Belanja": "sum"}).reset_index()

        # Membuat grafik batang perbandingan pendapatan dan belanja
        fig, ax = plt.subplots(figsize=(10, 6))
        bar_width = 0.4
        index = np.arange(len(df_grouped))

        ax.bar(index, df_grouped["Pendapatan"], bar_width, label="Pendapatan")
        ax.bar(index + bar_width, df_grouped["Belanja"], bar_width, label="Belanja")

        ax.set_xlabel("Provinsi")
        ax.set_ylabel("Jumlah (Rp)")
        ax.set_title("Perbandingan Total Pendapatan dan Belanja per Provinsi")
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(df_grouped["Provinsi"], rotation=45, ha="right")
        ax.legend()
        ax.grid(axis="y")

        # Menampilkan grafik di Streamlit
        st.pyplot(fig)

        # ===== Tambahan: Tabel dinamis =====
        st.subheader("📋 Tabel Data Filtered")
        st.dataframe(df_filtered.reset_index(drop=True))
