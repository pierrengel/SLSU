import streamlit as st

# ---- Page Setup ----
st.set_page_config(layout="wide")

# ---- Page Navigation via Session State ----
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ---- Custom CSS Styling ----
st.markdown("""
<style>
body {
    background-color: #FFFFF3;
    color: #111;
}
[data-testid="stAppViewContainer"] {
    background-color: #FFFFF3;
    color: #111;
}
.card {
    background-color: #F7F6F3;  /* etwas helleres, dezentes Grau */
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
}
button[kind="secondary"], div[data-baseweb="select"] {
    background-color: #134e4a !important;
    color: white !important;
    border-radius: 8px !important;
    height: 42px !important;
    font-size: 0.95rem !important;  /* Dropdown-Font etwas größer */
}
button[kind="secondary"]:hover {
    background-color: #0f3e3a !important;
}
.stButton>button {
    height: 42px !important;
    margin-top: 20px !important;
    font-size: 0.8rem !important;
}
.stSelectbox > div {
    height: 42px !important;
    margin-top: 20px !important;
}
#MainMenu, footer, header {
    visibility: hidden;
}
a { text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ---- HEADER: Logo / Spacer / Dropdown / To-Do / Home ----
col1, col2, col3, col4, col5 = st.columns([2, 4, 1, 1, 1], gap="small")
with col1:
    st.image("LOGOBODO.jpg", width=140)
with col2:
    st.write("")  # spacer
with col3:
    category_map = {"Auswahl": "C0", "Gurke": "C2", "Paprika": "C3"}
    choice = st.selectbox("", list(category_map.keys()), label_visibility="collapsed")
    category = category_map[choice]
with col4:
    if st.button("To-Do"):
        st.session_state.page = "Recommendations"
with col5:
    if st.button("Home"):
        st.session_state.page = "Dashboard"

# ---- PAGE 1: DASHBOARD ----
if st.session_state.page == "Dashboard":
    c1, c2, c3 = st.columns(3)

    if category == "C0":
        wasser_data = [("Hier werden Ihre sensorbasierten Wasserdaten angezeigt.", "", "", "")]
        boden_data  = [("Hier werden Ihre sensorbasierten Produktdaten angezeigt.", "", "", "")]
        klima_data  = [("Hier werden Ihre sensorbasierten Klimadaten angezeigt.",   "", "", "")]
    elif category == "C2":
        wasser_data = [("Wasserqualität (NTU)", "1.0 NTU", "0–2 NTU", "🟢 OK")]
        boden_data = [
            ("Bodenfeuchte", "32.5 %", "25–40 %", "🟢 OK"),
            ("EC-Wert (Düngesalze)", "1.5 mS/cm", "1.0–2.0 mS/cm", "🟢 OK"),
            ("pH-Wert (Wasser)", "6.15", "5.8–6.5", "🟢 OK")
        ]
        klima_data = [
            ("Temperatur (Luft)", "21.0 °C", "18–24 °C", "🟢 OK"),
            ("Luftfeuchtigkeit", "70.0 %", "60–80 %", "🟢 OK"),
            ("CO₂-Konzentration", "800 ppm", "600–1000 ppm", "🟢 OK"),
            ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "22.0 °C", "18–26 °C", "🟢 OK")
        ]
    else:  # Paprika C3
        wasser_data = [("Wasserqualität (NTU)", "5.0 NTU", "0–2 NTU", "🔴 Kritisch – Wasser evtl. gekippt")]
        boden_data = [
            ("Bodenfeuchte", "41 %", "25–40 %", "🟠 Leicht erhöht"),
            ("EC-Wert (Düngesalze)", "3.0 mS/cm", "1.0–2.0 mS/cm", "🔴 Deutlich zu hoch"),
            ("pH-Wert (Wasser)", "7.5", "5.8–6.5", "🔴 Zu basisch")
        ]
        klima_data = [
            ("Temperatur (Luft)", "25 °C", "18–24 °C", "🔴 Zu hoch"),
            ("Luftfeuchtigkeit", "81 %", "60–80 %", "🟠 Grenzwertig"),
            ("CO₂-Konzentration", "1001 ppm", "600–1000 ppm", "🟠 Grenzwertig"),
            ("Lichtintensität", "225 µmol/m²/s", "150–300 µmol/m²/s", "🟢 OK"),
            ("Blatt-Temperatur", "27 °C", "18–26 °C", "🔴 Zu hoch")
        ]

    with c1:
        st.markdown("### Wassermanagement")
        for p, i, s, stt in wasser_data:
            st.markdown(f"""
            <div class='card'>
              <strong>{p}</strong><br>
              {('Ist-Wert: ' + i + '<br>') if i else ''}
              {('Sollbereich: <span style="color:#555;">' + s + '</span><br>') if s else ''}
              {('Status: <span style="font-weight:bold;">' + stt + '</span>') if stt else ''}
            </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown("### Produktüberwachung")
        for p, i, s, stt in boden_data:
            st.markdown(f"""
            <div class='card'>
              <strong>{p}</strong><br>
              {('Ist-Wert: ' + i + '<br>') if i else ''}
              {('Sollbereich: <span style="color:#555;">' + s + '</span><br>') if s else ''}
              {('Status: <span style="font-weight:bold;">' + stt + '</span>') if stt else ''}
            </div>""", unsafe_allow_html=True)

    with c3:
        st.markdown("### Klimaüberwachung")
        for p, i, s, stt in klima_data:
            st.markdown(f"""
            <div class='card'>
              <strong>{p}</strong><br>
              {('Ist-Wert: ' + i + '<br>') if i else ''}
              {('Sollbereich: <span style="color:#555;">' + s + '</span><br>') if s else ''}
              {('Status: <span style="font-weight:bold;">' + stt + '</span>') if stt else ''}
            </div>""", unsafe_allow_html=True)

# ---- PAGE 2: HANDLUNGSEMPFEHLUNGEN ----
elif st.session_state.page == "Recommendations":
    st.markdown("### 📋 Handlungsempfehlungen")
    st.markdown("Hier erscheinen Ihre individuellen Empfehlungen basierend auf aktuellen Messwerten.")

    colA, colB = st.columns(2, gap="large")

    with colA:
        st.markdown("#### Vom System erledigt")
        if category == "C0":
            st.markdown("Hier wird Ihnen ein Überblick gezeigt über die Aufgaben, die Bodo bereits erledigt hat.")
        elif category == "C2":
            st.markdown("""
🟢 Die Bodenfeuchtigkeit liegt mit 32,5 % im optimalen Bereich. Die Bewässerung wurde erfolgreich abgeschlossen.

🟢 Die Luftfeuchtigkeit beträgt 70 % und liegt im Zielbereich. Die Lüftung läuft im Standardbetrieb.

🟢 Die Temperaturregelung ist stabil. Lufttemperatur (21 °C) und Blatttemperatur (22 °C) sind optimal.

🟢 Der CO₂-Wert liegt mit 800 ppm im Idealbereich. Die CO₂-Zufuhr ist aktiv.

🟢 Es wurden keine kritischen Abweichungen festgestellt. Systemstatus: stabil.
""")
        else:
            st.markdown("""
🔴 Die Grenzwerte der Wasserqualität wurden überschritten (5 NTU statt max. 2 NTU). Die Bewässerung wurde deshalb automatisch gestoppt.

🔴 Die Luftfeuchtigkeit liegt mit 81 % über dem optimalen Bereich. Die Lüftung wurde automatisch aktiviert.

🔴 Die Lufttemperatur beträgt 25 °C, die Blatttemperatur liegt zwischen 27 und 29,5 °C. Das Kühlsystem wurde zur Temperatursenkung eingeschaltet.

🔴 Der CO₂-Wert liegt bei 1001 ppm und damit über dem Grenzwert. Die CO₂-Zufuhr wurde automatisch deaktiviert.

🔴 Mehrere kritische Werte wurden gleichzeitig festgestellt. Eine Alarmmeldung wurde an den Betreiber gesendet.
""")
    with colB:
        st.markdown("#### Handlungsempfehlungen")
        if category == "C0":
            st.markdown("Hier wird Ihnen ein Überblick gegeben über die Handlungsempfehlungen. Bodo hat diese für Sie nach Priorität sortiert.")
        elif category == "C2":
            st.markdown("""
🟢 🔍 **Routinekontrolle Wassertank**  
Wasserqualität gut (1.0 NTU), aber regelmäßige Sichtprüfung empfehlenswert.

🟢 🧴 **Filterwartung (alle X Wochen)**  
Wasserfilter in gutem Zustand, aber Reinigung gemäß Wartungsplan prüfen.

🟢 📈 **Düngermenge protokollieren**  
EC-Wert (1.5 mS/cm) gut, aber Protokollierung hilft bei Langzeitoptimierung.

🟢 📋 **Allgemeine Sichtprüfung der Pflanzen**  
Keine Auffälligkeiten, aber regelmäßige Kontrolle auf Blattveränderungen sinnvoll.

🟢 🪴 **Testweise Blattproben für Labor (optional)**  
Zur Optimierung der Nährstoffstrategie bei empfindlicher Sorte.
""")
        else:
            st.markdown("""
🔴 🧪 **Wassertank prüfen und ggf. reinigen**  
NTU-Wert stark erhöht – kann auf Algen, Sedimente oder Bakterien im Tank hinweisen.

🟠 🧴 **Frischwasser oder Filter tauschen**  
Wasserqualität außerhalb Toleranz → evtl. Wasserquelle kontaminiert.

🟠 ⚖️ **Düngergabe unterbrechen/anpassen**  
EC-Wert bei 3.0–5.5 mS/cm = Überdüngung möglich → Nährstoffbrand vermeiden.

🟠 🧫 **Blätter auf Schimmel / Schädlinge prüfen**  
Hohe Luftfeuchte + Wärme = optimales Milieu für Pilze.

🟡 🧯 **Manuelle Schattierung aktivieren**  
Licht in Kombination mit hoher Temperatur kann Verbrennungen fördern.

🟢 🌡️ **Zusätzliche Thermomatten entfernen (falls vorhanden)**  
Zu hohe Temperaturen → Verdacht auf interne Wärmequellen.

🟢 📋 **Daten manuell protokollieren**  
Ggf. ergänzen, ob zusätzliche Beobachtungen gemacht wurden (Geruch, Trübung, Geräusche etc.).
""")
