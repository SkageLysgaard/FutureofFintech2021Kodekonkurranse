import streamlit as sl
import requests, json
sl.sidebar.write("Menu")
endpoint = sl.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])
sl.header("Future of Fintech 2021 Kodekonkurranse")
sl.subheader(f"OpenSea NFT API Explorer - {endpoint}")

sl.sidebar.subheader("Filters")

collection = sl.sidebar.text_input("Collections")
owner = sl.sidebar.text_input("Owner")

if endpoint == 'Assets':
    params = {}

    if collection:
        params['collection'] = collection
    if owner:
        params['owner'] = owner
    
    url = requests.get("https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20", params=params)

    response = url.json()

    for asset in response['assets']:
        if asset['name']:
            sl.write(asset['name'])
        else:
            sl.write(f"{asset['collection']['name']} #{asset['token_id']}")
        if asset['image_url'].endswith('mp4'):
            sl.video(asset['image_url'])
        else:
            sl.image(asset['image_url'])

    sl.write(url.json())
