import streamlit as st

# ---- 1) Page setup must come first ----
st.set_page_config(layout="wide")

# ---- 2) Global CSS (scoped under the main app container) ----
st.markdown(
    """
    <style>
    /* overall background and text color */
    [data-testid="stAppViewContainer"] {
        background-color: #FFFFF3;
        color: #111;
    }

    /* card styles */
    [data-testid="stAppViewContainer"] .card {
        background-color: #F7F6F3;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        font-size: 0.9rem;
        text-decoration: none;
        color: inherit;
        transition: background-color 0.2s ease;
    }
    [data-testid="stAppViewContainer"] .card:hover {
        background-color: #E8E6E2;
    }

    /* secondary buttons & selects */
    [data-testid="stAppViewContainer"] button[kind="secondary"],
    [data-testid="stAppViewContainer"] div[data-baseweb="select"] {
        background-color: #134e4a !important;
        color: white !important;
        border-radius: 8px !important;
        height: 42px !important;
        font-size: 0.95rem !important;
    }
    [data-testid="stAppViewContainer"] button[kind="secondary"]:hover {
        background-color: #0f3e3a !important;
    }

    /* default stButton */
    [data-testid="stAppViewContainer"] .stButton > button {
        height: 42px !important;
        margin-top: 20px !important;
        font-size: 0.8rem !important;
    }

    /* selectbox height */
    [data-testid="stAppViewContainer"] .stSelectbox > div {
        height: 42px !important;
        margin-top: 20px !important;
    }

    /* hide the default menu, footer, header */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* remove link underlines */
    a {
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- 3) Read query-params using the new API ----
params = st.query_params
page   = params.get("page", ["Dashboard"])[0]

# ---- 4) HEADER: Logo / Dropdown / To-Do / Home ----
col1, col2, col3, col4 = st.columns([2, 5, 1, 1], gap="small")
with col1:
    # make sure LOGOBODO.jpg is in your repo (same folder or correct subfolder)
    st.image("LOGOBODO.jpg", width=140)
with col2:
    category_map = {"Auswahl": "C0", "Gurke": "C2", "Paprika": "C3"}
    choice       = st.selectbox("", list(category_map.keys()), label_visibility="collapsed")
    category     = category_map[choice]
with col3:
    if st.button("To-Do"):
        st.experimental_set_query_params(page="Recommendations")
with col4:
    if st.button("Home"):
        st.experimental_set_query_params(page="Dashboard")

# ---- DASHBOARD page ----
if page == "Dashboard":
    c1, c2, c3 = st.columns(3)
    # Daten je Kategorie
    if category == "C0":
        wasser_data = [("Hier werden Ihre sensorbasierten Wasserdaten angezeigt.", "", "", "")]
        boden_data  = [("Hier werden Ihre sensorbasierten Produktdaten angezeigt.", "", "", "")]
        klima_data  = [("Hier werden Ihre sensorbasierten Klimadaten angezeigt.",   "", "", "")]
    elif category == "C2":
        wasser_data = [("Wasserqualität (NTU)", "1.0 NTU", "0–2 NTU", "🟢 OK")]
        boden_data = [
            ("Bodenfeuchte", "32.5 %", "25–40 %", "🟢 OK"),
            ("EC-Wert (Düngesalze)", "1.5 mS/cm", "1.0–2.0 mS/cm", "🟢 OK"),
            ("pH-Wert (Wasser)", "6.15", "5.8–6.5", "🟢 OK"),
        ]
        klima_data = [
            ("Temperatur (Luft)", "21.0 °C", "18–24 °C", "🟢 OK"),
            ("Luftfeuchtigkeit", "70 %", "60–80 %", "🟢 OK"),
            ("CO₂-Konzentration", "800 ppm", "600–1000 ppm", "🟢 OK"),
            ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "22 °C", "18–26 °C", "🟢 OK"),
        ]
    else:  # Paprika
        wasser_data = [("Wasserqualität (NTU)", "5.0 NTU", "0–2 NTU", "🔴 Kritisch")]
        boden_data = [
            ("Bodenfeuchte", "41 %", "25–40 %", "🟠 Leicht erhöht"),
            ("EC-Wert (Düngesalze)", "3.0 mS/cm", "1.0–2.0 mS/cm", "🔴 Deutlich zu hoch"),
            ("pH-Wert (Wasser)", "7.5", "5.8–6.5", "🔴 Zu basisch"),
        ]
        klima_data = [
            ("Temperatur (Luft)", "25 °C", "18–24 °C", "🔴 Zu hoch"),
            ("Luftfeuchtigkeit", "81 %", "60–80 %", "🟠 Grenzwertig"),
            ("CO₂-Konzentration", "1001 ppm", "600–1000 ppm", "🟠 Grenzwertig"),
            ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "27 °C", "18–26 °C", "🔴 Zu hoch"),
        ]

    # Wassermanagement
    with c1:
        st.markdown("### Wassermanagement")
        for p, i, s, stt in wasser_data:
            st.markdown(
                f"""
                <a href="?page=Wassermanagement">
                  <div class="card">
                    <strong>{p}</strong><br>
                    {('Ist-Wert: ' + i + '<br>') if i else ''}
                    {('Sollbereich: <span style="color:#555;">' + s + '</span><br>') if s else ''}
                    {('Status: <span style="font-weight:bold;">' + stt + '</span>') if stt else ''}
                  </div>
                </a>
                """,
                unsafe_allow_html=True
            )

    # Produktüberwachung
    with c2:
        st.markdown("### Produktüberwachung")
        for p, i, s, stt in boden_data:
            st.markdown(
                f"""
                <a href="?page=Produktüberwachung">
                  <div class="card">
                    <strong>{p}</strong><br>
                    {('Ist-Wert: ' + i + '<br>') if i else ''}
                    {('Sollbereich: <span style="color:#555;">' + s + '</span><br>') if s else ''}
                    {('Status: <span style="font-weight:bold;">' + stt + '</span>') if stt else ''}
                  </div>
                </a>
                """,
                unsafe_allow_html=True
            )

    # Klimaüberwachung
    with c3:
        st.markdown("### Klimaüberwachung")
        for p, i, s, stt in klima_data:
            st.markdown(
                f"""
                <a href="?page=Klimaüberwachung">
                  <div class="card">
                    <strong>{p}</strong><br>
                    {('Ist-Wert: ' + i + '<br>') if i else ''}
                    {('Sollbereich: <span style="color:#555;">' + s + '</span><br>') if s else ''}
                    {('Status: <span style="font-weight:bold;">' + stt + '</span>') if stt else ''}
                  </div>
                </a>
                """,
                unsafe_allow_html=True
            )

# ---- TO-DO page ----
elif page == "Recommendations":
    st.markdown("### 📋 Handlungsempfehlungen")
    st.markdown("Hier erscheinen Ihre individuellen Empfehlungen basierend auf aktuellen Messwerten.")
    colA, colB = st.columns(2, gap="large")
    # … your recommendations content …

# ---- Detail pages per card ----
elif page in ["Wassermanagement", "Produktüberwachung", "Klimaüberwachung"]:
    st.markdown(f"## {page}")
    st.markdown("Hier kommt der spezifische Inhalt für diese Kategorie.")
    if st.button("Zurück zur Übersicht"):
        st.experimental_set_query_params(page="Dashboard")
