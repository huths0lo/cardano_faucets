#!/usr/bin/python3

import os
import requests
from dotenv import load_dotenv
from time import sleep
import json

load_dotenv()

api_key = os.getenv('preprod_api_key')
test_wallet_1 = os.getenv('test_wallet_1')
test_wallet_2 = os.getenv('test_wallet_2')


def pull_from_faucet(wallet_addr):
    headers = {"Content-Type": "application/json"}
    url = f'https://faucet.mixed.world.dev.cardano.org/basic-faucet/{wallet_addr}?api_key={api_key}'
    response = requests.post(url=url, headers=headers)
    return response
	


def run_puller():
    total_pulls = 0
    while True:
        pull_from_faucet(test_wallet_1)
        sleep(60)
        pull_from_faucet(test_wallet_2)
        total_pulls += 1
        print(f'Total Pulls = {total_pulls}')
        sleep(600)


def get_delegation(pool_id)
    url = f'https://faucet.preprod.world.dev.cardano.org/delegate/{pool_id}?api_key=ooseiteiquo7Wie9oochooyiequi4ooc'
    response = requests.post(url=url)
    print(response.json())

run_puller()
