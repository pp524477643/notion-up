import os

import requests


class NotionToken:

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def getNotionToken(email, password):
        if not email:
            raise Exception('Email is not presented!')
        if not password:
            raise Exception('Password is not presented!')

        loginData = {
            'email': email,
            'password': password
        }
        headers = {
            # Notion obviously check this as some kind of (bad) test of CSRF
            'host': 'www.notion.so'
        }
        response = requests.post(
            'https://notion.so/api/v3/loginWithEmail',
            json=loginData,
            headers=headers
        )
        response.raise_for_status()
        return response.cookies['v02%3Auser_token_or_cookies%3A3QQi1pRtxSjineW8TaEPuuGzTXB5DFBziCLUlyBMQuBKavGBlWAaCf2BRSVKFfQH3XtMlBEiJbOmLZ99WOwm9ciQabo-t1OuYCjyAazItpGmWp-8U4Qekrp-_kR5n8dZvxj8;']
