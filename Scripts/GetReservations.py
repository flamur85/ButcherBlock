import requests


def set_headers():
    cookies = {
        'csrftoken': 'YckgqWntI1PUyIxGPwiGlLKZazjwYyjl',
        '_gcl_au': '1.1.1192839833.1658545293',
        '_ga': 'GA1.2.1905695610.1658545293',
        'G_ENABLED_IDPS': 'google',
        '__stripe_mid': 'f05120ac-8222-4796-9d52-b5b42e7e8c1f3b14d5',
        '_gid': 'GA1.2.918030254.1658706413',
        '_gat': '1',
        '__stripe_sid': '10a0cd45-a53c-420a-96dd-4f3fe40aca4772a62e',
    }

    headers = {
        'authority': 'www.sevenrooms.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'csrftoken=YckgqWntI1PUyIxGPwiGlLKZazjwYyjl; _gcl_au=1.1.1192839833.1658545293; _ga=GA1.2.1905695610.1658545293; G_ENABLED_IDPS=google; __stripe_mid=f05120ac-8222-4796-9d52-b5b42e7e8c1f3b14d5; _gid=GA1.2.918030254.1658706413; _gat=1; __stripe_sid=10a0cd45-a53c-420a-96dd-4f3fe40aca4772a62e',
        'dnt': '1',
        'referer': 'https://www.sevenrooms.com/reservations/thebutchersblock',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    return cookies, headers


def get_reservations():
    try:
        cookies, headers = set_headers()
        response = requests.get('https://www.sevenrooms.com/api-yoa/availability/widget/range?venue=thebutchersblock&time_slot=14:00&party_size=2&halo_size_interval=24&start_date=07-30-2022&num_days=1&channel=SEVENROOMS_WIDGET', cookies=cookies, headers=headers)
        print(response.text)
        json_array_response = response.json()
        print(json_array_response['data'])
    except:
        print('something went wrong')


def main():
    print('|************************* - SCRIPT START - *************************|')
    get_reservations()


if __name__ == "__main__":
    main()