# filepath: /Users/ayanlemohamed/Documents/Jobbvarsling System/send_email.py

import os
import sendgrid
from sendgrid.helpers.mail import Mail
from config import EMAIL_ADDRESS, TO_EMAIL

def send_job_email(title, link, source):
    """
    Sender meg en e-post med informasjon om en ny stilling jeg har funnet.
    Jeg bruker SendGrid sin API-nøkkel som jeg har lagret som miljøvariabel.
    """

    # Henter API-nøkkelen fra miljøvariabel (jeg må sette denne lokalt)
    api_key = os.getenv("SENDGRID_API_KEY")

    if not api_key:
        print("Fant ingen SendGrid API-nøkkel i miljøvariabler.")
        return

    sg = sendgrid.SendGridAPIClient(api_key)

    subject = f"Ny jobb funnet på {source}"
    body = f"Tittel: {title}\nKilde: {source}\nLenke: {link}\n\nLykke til med søknaden!"

    # Lager e-postmeldingen
    message = Mail(
        from_email=EMAIL_ADDRESS,
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=body
    )

    try:
        response = sg.send(message)
        print(f" E-post sendt! Statuskode: {response.status_code}")
    except Exception as e:
        print(f" Klarte ikke å sende e-post: {e}")


if __name__ == "__main__":
    # Kjapp test for å sjekke at utsending fungerer
    send_job_email("Teststilling", "https://eksempel.no", "TestKilde")
