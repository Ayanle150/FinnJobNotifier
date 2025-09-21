# Jobbvarsling System

Et lite Python-prosjekt som sender deg e-post når det dukker opp nye relevante stillinger på FINN.no.

## Hvordan fungerer det?

- **[`finn_scrapper.py`](finn_scrapper.py):** Skraper finn.no etter stillinger basert på dine søkeord.
- **[`config.py`](config.py):** Lagrer e-postadresser og søkeord.
- **[`send_email.py`](send_email.py):** Sender e-post via SendGrid når en relevant stilling blir funnet.
- **[`requirements.txt`](requirements.txt):** Holder oversikt over nødvendige Python-pakker.

## Kom i gang

1. **Klon repoet og installer avhengigheter:**
   ```bash
   git clone <repo-url>
   cd Jobbvarsling-System
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Opprett en SendGrid API-nøkkel og legg den til som miljøvariabel:**

   **macOS/Linux:**
   ```bash
   export SENDGRID_API_KEY="din_api_nokkel"
   ```

   **Windows PowerShell:**
   ```powershell
   $env:SENDGRID_API_KEY="din_api_nokkel"
   ```

3. **Oppdater [`config.py`](config.py):**
   - Sett din SendGrid-verifiserte avsenderadresse
   - Sett mottakeradresse
   - Legg inn ønskede søkeord

4. **Test e-postutsending:**
   ```bash
   python send_email.py
   ```

5. **Kjør skraperen for å finne relevante stillinger:**
   ```bash
   python finn_scrapper.py
   ```

## Automatisering

- **Linux/macOS:** Bruk `cron` for å kjøre skriptet automatisk, f.eks. hver time.
- **Windows:** Bruk Oppgaveplanlegging (Task Scheduler).

## Tips

- Du kan endre søkeordene i `config.py` for å tilpasse hvilke stillinger du får varsel om.
- Husk å holde SendGrid API-nøkkelen hemmelig og aldri legg den direkte i kode!
- Sjekk spam-filteret hvis du ikke mottar e-post.

---

**Spørsmål eller problemer?**  
Opprett en issue eller kontakt repo-eier.
