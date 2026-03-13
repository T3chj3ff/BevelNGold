import urllib.request
import os

urls = [
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/469778901_122168672444252990_5116974659896427671_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=104&ccb=1-7&_nc_sid=2a1932&_nc_ohc=sJZiLHfchZYQ7kNvwGKwH9P&_nc_oc=Adl4hfV_Oy5mV0v1ciW1qtrC8kihHx6ZiRD9A0kSzX3XqBcXcJmYyj6Fp7TCBXmvjgw&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_AfyTqPnl-47K96tDYzBZBA55ptz8wtIZUMyKW9UljgfQWw&oe=69B9B367",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/538266150_122213467346252990_952125302843893295_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=101&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=zMPfncmQ1J4Q7kNvwGVjKOJ&_nc_oc=Adm4LZCN2kngJZjdYp6EdRYLkmxvpM_tcnRgHc-2XekhJxDz933WPZVbmlk5quMDmQ4&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_AfwReR7PeQeWUrRfnVXw1V94MkDk8_APJLzv7vW_IGYp-w&oe=69B9A35D",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/536703291_122213462786252990_7765405815960254825_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=100&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=fcMzrZd-zgMQ7kNvwG5L3Ic&_nc_oc=AdkOP-qHhMSvElEWjgf-iGVG9_He4e3Z2bkDIlIDd-r9ElD3beDLfCdgKyh4wr4Ly4g&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_AfwlqS4T99d1kIORPgZXLZfu3y6bmdEdmjG3R-QGKrqabg&oe=69B98BD4",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/536711118_122213462834252990_1388626378579659044_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=101&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=w9kZnq6HrDUQ7kNvwFjnrZg&_nc_oc=AdneIZLYuOoniqJQix13vu1yG2yJjP5vcB4d_eEI9yHuKQzO-jlXB2I2FiAQxMvAGIw&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_Afw3iT5etao7bW6t772h3UvRiH8l7Hix7z4qJroTpaUM-g&oe=69B9A16E",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/537166575_122213462750252990_1878360330614538937_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=107&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=cqJHuEyC5-cQ7kNvwFcdKgG&_nc_oc=AdkuW1xRU0OrXzEjQk8zDjEgkZp4-3IQgOijA6-TelsOOjWJ898iUgO3o2AwEm9kgng&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_AfyELp_lPxqUyZ9QIYNhWoEIVxmqDaE2UOyVSmMlDRdiEA&oe=69B98999",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/536035886_122213344790252990_1499738737820641754_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=105&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=NBYtsCxtL-MQ7kNvwEVpxZD&_nc_oc=Adlktjba5uhwDeMqi_rSu7GL1D3BbayH5PfUaThLh5YDtQ0o-VLmcC0c-FMIYBTvdMw&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_AfxX3cEKYDP8_ieABxe8PQ6kMRICUdH_lntlCV2Q7r1lLQ&oe=69B9B88D",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/472062673_122173059302252990_4189508065497414921_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=103&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=ZquQ1DkPT9QQ7kNvwG0V7OI&_nc_oc=AdkJYf2dc-tHAgpNaLuvJyDYbCE1upIDu-aYT3bCHLfYqqT9w-NqxftAoHnMXsNnOXw&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_Afzk0L0hsH1WE9mLgDYCsF-Fjeb1z1MfTT_-W0yNNdMsYw&oe=69B987C5",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/472107370_122173058642252990_1045783088428520643_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=101&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=VQNEqULzRxQQ7kNvwGgofiF&_nc_oc=AdnZclI1IMeXvkpD6lzHcChXDWR2KP6tVaCGjpL2MmoaetCpeAK-m7iujzoqSRdtWs4&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_AfzMwmM9WMGpClkICock8ALcA2VOS98oTu9nxENDcb060Q&oe=69B99BAA",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/538142253_122213467388252990_8697726043526766515_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=106&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=SfNUvy0mBUEQ7kNvwEXh30u&_nc_oc=AdlKDBQEXHaNW1FJ6UukpTfT2W8Ntj5uZcyccA_MtEKePb_HPnz13JITXnpmwsC8VyE&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=fj4dTijJwcUb_JAw8D3rrQ&_nc_ss=8&oh=00_AfwmnqAnOoCIxAjhCsdUUjATNAQJPojcwr4CHv-J7XP0lA&oe=69B98C4A",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/470209456_122170251842252990_3046750778192941550_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=103&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=5FL3O2EyrfoQ7kNvwEUEOZz&_nc_oc=Adl_v-0000dp1o_EfwlPGnXd3znxi8ti4q0UYOkha_48R4z3SHp46W25Zac2u1zklw4&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=K0kW6N3KKKyAb91XcDmYBQ&_nc_ss=8&oh=00_Afz6eap2yIZMuK7bgOmYLuhqOaLg1eTamlxFmEaeYucoMA&oe=69B9B526",
    "https://scontent-den2-1.xx.fbcdn.net/v/t39.30808-6/472065972_122173058576252990_1212679529512105218_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=106&ccb=1-7&_nc_sid=5df8b4&_nc_ohc=scwP10w1M-oQ7kNvwFpLUxu&_nc_oc=Adnf30i9ezpP8KlE3QuGdl2whYfHrXWl2MIz5VFLhenAa1WYhqluhwSjUuCY1Qcmlug&_nc_zt=23&_nc_ht=scontent-den2-1.xx&_nc_gid=K0kW6N3KKKyAb91XcDmYBQ&_nc_ss=8&oh=00_Afx1fTfROm7qk4dgOzMh3_IQR9CNTWniOccTHpxgJu6uOA&oe=69B986D9"
]

output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.facebook.com/"
}

for i, url in enumerate(urls):
    if i < 8:
        filename = f"portfolio-{i+1}.webp"
    else:
        filename = f"showcase-{i-7}.webp"
    
    filepath = os.path.join(output_dir, filename)
    print(f"Downloading {url} to {filepath}")
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            print(f"Successfully downloaded {filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
