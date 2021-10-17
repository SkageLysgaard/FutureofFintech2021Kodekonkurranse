import streamlit as sl
import requests
sl.sidebar.header("Menu")
#made a selectbox so it's easy to scale
endpoint = sl.sidebar.selectbox("Endpoints", ['Assets'])
sl.header("Future of Fintech 2021 Kodekonkurranse")
sl.subheader(f"OpenSea NFT API Explorer - {endpoint}")

sl.sidebar.subheader("Filters")
sl.sidebar.write("Collections to try: giphy, monkeybet")

collection = sl.sidebar.text_input("Collections")
owner = sl.sidebar.text_input("Owner")
#just to make it easy to scale. but not neccesarry when my endpoint only contains one item
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
        if asset['image_url'].endswith('mp4') or asset['image_url'].endswith('mov'):
            sl.video(asset['image_url'])
        else:
            sl.image(asset['image_url'])

    
