from pprint import pprint
import requests
import os


def get_current_waifu(waifu="neko"):

    request_url = f'https://api.waifu.pics/sfw/{waifu}'

    waifu_type = requests.get(request_url).json()

    return waifu_type


if __name__ == "__main__":
    print('\n Получи свой типаж \n')

    waifu = input("\nПожалуйста, введи свой типаж : ")

    waifu_type = get_current_waifu(waifu)

    print("\n")
    pprint(waifu_type)