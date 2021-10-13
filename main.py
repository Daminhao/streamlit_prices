import streamlit as st # modulo para frond-end
import requests
from bs4 import BeautifulSoup as bs

def html(body):
    st.markdown(body, unsafe_allow_html=True)

def card_begin_str(header):
    return (
        "<style>div.card{background-color:DarkOrange;border-radius: 5px;box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);transition: 0.3s;}</style>"
        '<div class="card">'
        '<div class="container">'
        "<p>"
        f"<h3><b>Bitcoin</b></h3>"
        f"<h3><b>Price: {header}</b></h3>"

    )

url = "https://coinmarketcap.com/currencies/bitcoin"
        
r = requests.get(url)
soup = bs(r.content, "html.parser")

price = soup.find("div", {"class":"priceValue"})
        
price_text = (price.text)

html(card_begin_str(price_text))

st.info("Fonte: https://coinmarketcap.com/currencies/bitcoin")

