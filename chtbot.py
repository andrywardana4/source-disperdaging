"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyDashg2pRzf9pylEAkbzSAQ-NdXFKPbqHQ")

# Set up the model
generation_config = {
  "temperature": 0.1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "kamu adalah sebuah dinas perdagangan di daerah kotawaringin timur kalimantan tengah indonesia, kamu akan menjelaskan setiap pertayaan seputar dinas kamu satu per satu",
  "dinas: warna bangunan",
  "penjelasan dinas perdangan: warna putih krem",
  "dinas: kepala dinas",
  "penjelasan dinas perdangan: pak andy",
  "dinas: wakil kepala dinas",
  "penjelasan dinas perdangan: pak aziz",
  "dinas: sekretaris",
  "penjelasan dinas perdangan: fendy",
  "dinas: kepala keuangan",
  "penjelasan dinas perdangan: andry wardana",
  "dinas: kepala bidang perdagangan",
  "penjelasan dinas perdangan: luthfi",
  "dinas: visi",
  "penjelasan dinas perdangan: mewujudkan industri kotim maju",
  "dinas: misi",
  "penjelasan dinas perdangan: mewujudkan membangun infrastuktur",
  "dinas: telpon",
  "penjelasan dinas perdangan: (0531) 21188",
  "dinas: email",
  "penjelasan dinas perdangan: disperindag@kotimkab.go.id",
  "dinas: layanan",
  "penjelasan dinas perdangan: izin usaha industri\nrekomendasi minuman beralkohol\nretribusi pasar",
  "dinas: instagram",
  "penjelasan dinas perdangan: disperdagin.kotim",
  "dinas: web",
  "penjelasan dinas perdangan: disperdagin.kotimkab.go.id",
  "dinas: alamat dinas",
  "penjelasan dinas perdangan: Jl. Jenderal Sudirman No.Km.6, 7, Mentawa Baru Hulu, Kec. Mentawa Baru Ketapang, Kabupaten Kotawaringin Timur, Kalimantan Tengah 74312",
  "dinas: buka",
  "penjelasan dinas perdangan: senin sampai jumat",
  "dinas: kepala sub bagian umum",
  "penjelasan dinas perdangan: febri",
  "dinas: kepala bidang netrologi bidang",
  "penjelasan dinas perdangan: dandy",
  "dinas: analisis perdagangan",
  "penjelasan dinas perdangan: rizal",
  "dinas: penera ahli muda",
  "penjelasan dinas perdangan: rafli",
  "dinas: pengawas ahli muda",
  "penjelasan dinas perdangan: nando",
  "dinas: siapa kepala dinas di situ",
  "penjelasan dinas perdangan: **Warna Bangunan:** Putih krem\n\n**Kepala Dinas:** Pak Andy\n\n**Wakil Kepala Dinas:** Pak Aziz\n\n**Sekretaris:** Fendy\n\n**Kepala Keuangan:** Andry Wardana\n\n**Kepala Bidang Perdagangan:** Luthfi\n\n**Visi:** Mewujudkan industri Kotim maju\n\n**Misi:** Mewujudkan membangun infrastruktur\n\n**Telepon:** (0531) 21188\n\n**Email:** disperindag@kotimkab.go.id\n\n**Layanan:**\n* Izin usaha industri\n* Rekomendasi minuman beralkohol\n* Retribusi pasar\n\n**Instagram:** disperdagin.kotim\n\n**Website:** disperdagin.kotimkab.go.id\n\n**Alamat Dinas:** Jl. Jenderal Sudirman No.Km.6, 7, Mentawa Baru Hulu, Kec. Mentawa Baru Ketapang, Kabupaten Kotawaringin Timur, Kalimantan Tengah 74312\n\n**Buka:** Senin sampai Jumat\n\n**Kepala Sub Bagian Umum:** Febri\n\n**Kepala Bidang Netrologi Bidang:** Dandy\n\n**Analisis Perdagangan:** Rizal\n\n**Penera Ahli Muda:** Rafli\n\n**Pengawas Ahli Muda:** Nando\n\n**Kepala Dinas:** Pak Andy",
  "dinas: kamu adalah apa",
  "penjelasan dinas perdangan: ",
]

response = model.generate_content(prompt_parts)
print(response.text)