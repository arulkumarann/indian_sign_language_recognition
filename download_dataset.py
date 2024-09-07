import requests
import os
from urllib.parse import urlparse, parse_qs

def get_file_id_from_url(url):
    """Extract file ID from Google Drive shareable URL."""
    parsed_url = urlparse(url)
    file_id = parse_qs(parsed_url.query).get('id')
    if file_id:
        return file_id[0]
    return None

def download_file_from_google_drive(url, dest_folder):
    """Download file from Google Drive."""
    file_id = get_file_id_from_url(url)
    if not file_id:
        print(f"Invalid URL: {url}")
        return
    
    # Request the file
    request_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = requests.get(request_url, stream=True)
    if response.status_code == 200:
        # Get the file name
        file_name = response.headers.get('Content-Disposition')
        if file_name:
            file_name = file_name.split('filename=')[1].strip('"')
        else:
            file_name = file_id + ".tmp"
        
        # Save file
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        file_path = os.path.join(dest_folder, file_name)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {file_path}")
    else:
        print(f"Failed to download: {url}")

# List of Google Drive file links
file_links = [
  "https://drive.google.com/open?id=1-BaN8zsEOtGLQ2JU37zAMtT7GTXcYpGL&usp=drive_copy",
  "https://drive.google.com/open?id=1-DgCkKh0wckhi80N5j_EO5nCHh-YLsxH&usp=drive_copy",
  "https://drive.google.com/open?id=1-EczkZLoqHgwSq2YGTMcOqz0fLDL3zhP&usp=drive_copy",
  "https://drive.google.com/open?id=1-IDOBYX7K6ekJcw2lyh7l5ttfCuLh2bL&usp=drive_copy",
  "https://drive.google.com/open?id=1-OYUFM2XyTjGu1GmvmGwfFrBEtQfrWij&usp=drive_copy",
  "https://drive.google.com/open?id=1-RBEQl7c2pdxMVEjcc14hL_gApmMRcfb&usp=drive_copy",
  "https://drive.google.com/open?id=1-UL7q6HsHaMPsAhqW9pIj5dQST2BHIL2&usp=drive_copy",
  "https://drive.google.com/open?id=1-ZHGp9FMrnUc372stP-mX9IY3TyScnk7&usp=drive_copy",
  "https://drive.google.com/open?id=1-_APAh291dTOAROhJrex8nXmE5tLsAAM&usp=drive_copy",
  "https://drive.google.com/open?id=1-_bS1CGFrVtUdU-dH3jfh-dEkNoeE_Wj&usp=drive_copy",
  "https://drive.google.com/open?id=1-cQb8wkuKA1ElaPxRSmq1QcfQxlKRWmm&usp=drive_copy",
  "https://drive.google.com/open?id=1-fvUZdGx8fMtRwqk31CBVHvzr3HKxzpy&usp=drive_copy",
  "https://drive.google.com/open?id=1-qOnFOhvvd-wlinLtbpttFh_nh7ntJPb&usp=drive_copy",
  "https://drive.google.com/open?id=101fQu_FLlVB0-5zkC75d8OB9p5Z-YmKG&usp=drive_copy",
  "https://drive.google.com/open?id=1080jM1WvRYrnNS2tbxq2ENi20Ua-6pT8&usp=drive_copy",
  "https://drive.google.com/open?id=109vCwar_exv0hp0p3gtzX2x7H9lymKgM&usp=drive_copy",
  "https://drive.google.com/open?id=10AXisyIhDcvXcNLLLRYn2JCrFnYQZDTh&usp=drive_copy",
  "https://drive.google.com/open?id=10Fo2B9xbso0N1bPlcumhntDD61oUh0kN&usp=drive_copy",
  "https://drive.google.com/open?id=10JXjBMH9wAlJpdNbExaE0-zu0byvV8-9&usp=drive_copy",
  "https://drive.google.com/open?id=10Wjo8VYEj_esgtiWAamF6AYBCw2no8LJ&usp=drive_copy",
  "https://drive.google.com/open?id=10_diYZP27DZM6z-7deoK6pw5XJG8-IPj&usp=drive_copy",
  "https://drive.google.com/open?id=10bMC2QHfvdnC18rRCRRpjcSdeCwaQDZH&usp=drive_copy",
  "https://drive.google.com/open?id=10d1gOH9chSewiutaKkHtjEb2MXL57xDB&usp=drive_copy",
  "https://drive.google.com/open?id=10m8vvI2_bt-m943E4dWDdSn6KJdATaec&usp=drive_copy",
  "https://drive.google.com/open?id=10sJ4t1OABH16joB4FwiWi9qtZujsCNgP&usp=drive_copy",
  "https://drive.google.com/open?id=10uM78MYI8gwnBpJYs6TnSPSZm7mipc-k&usp=drive_copy",
  "https://drive.google.com/open?id=10zzDpQ0nzH3F1F8aJ541oqzce_wL_OZ4&usp=drive_copy",
  "https://drive.google.com/open?id=11Hp4CxXERcKRahQSloSR-vPQAhx4fSIs&usp=drive_copy",
  "https://drive.google.com/open?id=11IQDaupyPqPFDvf8hNkCu1GPGsjfPE_R&usp=drive_copy",
  "https://drive.google.com/open?id=11IZU-Rx4cV-luTT3mqcoMqBfH2Lj0rQM&usp=drive_copy",
  "https://drive.google.com/open?id=11MIzy9Ox5Y5Sdz1vrFXtJ6GIPghY5iSM&usp=drive_copy",
  "https://drive.google.com/open?id=11NKSp1taJ3EJmY_pykXfSrQh0a7MVVWW&usp=drive_copy",
  "https://drive.google.com/open?id=11Pyj9NOKvAOsKdzviYn6PbrCuHxSTSJ1&usp=drive_copy",
  "https://drive.google.com/open?id=11W3atRxmplyTrBOIpv44GNcLZMri9MMm&usp=drive_copy",
  "https://drive.google.com/open?id=11W_DH4S_sYAyEw1ZwDLofTsvDKfBy_dJ&usp=drive_copy",
  "https://drive.google.com/open?id=11cEcruZo8zVispMhj0RAxK78JAKblQYh&usp=drive_copy",
  "https://drive.google.com/open?id=11hLNZ30UP67uOBzhYhPoXXHLS0BaQJRR&usp=drive_copy",
  "https://drive.google.com/open?id=11oqiJf4B7n-K7FepJwoOc9NGoVjXycNh&usp=drive_copy",
  "https://drive.google.com/open?id=11ox6TA9BGKfv0cN8Lz1ncM9YButotpBH&usp=drive_copy",
  "https://drive.google.com/open?id=11qjblMm21HHACioAqVvMPmuo8E09NDeF&usp=drive_copy",
  "https://drive.google.com/open?id=126HmUWM4qAV9_CTMcoNhhvpWfOHf0KaK&usp=drive_copy",
  "https://drive.google.com/open?id=127nukAv5W9iYh1mmGYPCHa3GfVcJ7w77&usp=drive_copy",
  "https://drive.google.com/open?id=12FujkWNSEXjNZ5yrNprmvglNrqjUJ-Ez&usp=drive_copy",
  "https://drive.google.com/open?id=12Weag1TfuQDAmt8OnwyvAtDolVggwBVQ&usp=drive_copy",
  "https://drive.google.com/open?id=12ZtTMWHKiA3x2-PWSwDcTzQmHri32-kn&usp=drive_copy",
  "https://drive.google.com/open?id=12gKbNY0PTP4XzNNSuOLfzHf4rPdu4N8n&usp=drive_copy",
  "https://drive.google.com/open?id=12iF9aQNOg-LhsLXKyaTUexpPWBI9SyK0&usp=drive_copy",
  "https://drive.google.com/open?id=12pAtFjlpTh8AmH6A_v9373mv1VTv4x0_&usp=drive_copy",
  "https://drive.google.com/open?id=12r3YpL61zQ2q8tgRGGFLtZvgyKFEOlu1&usp=drive_copy",
  "https://drive.google.com/open?id=12u3QQVuJVwKiqGAP7v5cHtzyiGL6N9i6&usp=drive_copy",
  "https://drive.google.com/open?id=1323zoIvsZj8zo3fQVEeMVNvREisPIBpl&usp=drive_copy",
  "https://drive.google.com/open?id=135nCChhkfGJiIC7d2auMH5ep_ur4Ssep&usp=drive_copy",
  "https://drive.google.com/open?id=136CMPcH0avHPwLS0RhfXKbJVXEQ2PDK9&usp=drive_copy",
  "https://drive.google.com/open?id=13BhKXwOqjT8sJ7xhhgFfpS5UQkHHlL7r&usp=drive_copy",
  "https://drive.google.com/open?id=13I5X8kK6uFZtwWl53GgJMPiWk5KbL4zL&usp=drive_copy",
  "https://drive.google.com/open?id=13MKoUowHn-TS8hRQFI4j0HD54osz6NW0&usp=drive_copy",
  "https://drive.google.com/open?id=13NeEg0Xw8iV3ZBv1jwrBr0M6G9Bohjci&usp=drive_copy",
  "https://drive.google.com/open?id=13j2ucO5MlTXyA7gP-7_cJTLtOWy7jsEH&usp=drive_copy",
  "https://drive.google.com/open?id=13uG4WzP2BY29q2WqTn_CaqT8VVdVr6FY&usp=drive_copy",
  "https://drive.google.com/open?id=1410pyTh6ySJ_L60kZ4Yc0UmhoVd5zI90&usp=drive_copy",
  "https://drive.google.com/open?id=142jVmoaML4QUo1x80O1VNS0N4LCsf6Y5&usp=drive_copy",
  "https://drive.google.com/open?id=14Dr8S2hoCqa8T9ZGKPZK71Kp8k2xayov&usp=drive_copy",
  "https://drive.google.com/open?id=14Fo_gwZZZY36Q7F3zvh5ZGu_VexI4wPq&usp=drive_copy",
  "https://drive.google.com/open?id=14KZ5xEY2v4bVv_HdsHwaPS_i9Rgiir7m&usp=drive_copy",
  "https://drive.google.com/open?id=14LY4P1yGE88gPRyFjl5U1oOjVyu1tD43&usp=drive_copy",
  "https://drive.google.com/open?id=14Vo4LKYj79yFzp2QPGjJKzuAhuc3mL7m&usp=drive_copy",
  "https://drive.google.com/open?id=14h4JcMy05DT1M4_H7N7-QnJgbLl5pYdj&usp=drive_copy",
  "https://drive.google.com/open?id=14qsdTz3H4_jZV8IBh-tELfb07Wg2a-QK&usp=drive_copy",
  "https://drive.google.com/open?id=14ssG0YYyXUgMdcqUNhvxL4TiBBmT5Xsu&usp=drive_copy",
  "https://drive.google.com/open?id=14tkRKrTOfGy02HMW4m8ybWwiQQEYUL7B&usp=drive_copy",
  "https://drive.google.com/open?id=14vGQff6X5bRgOdYwOxsRzTFhr_xbBepZ&usp=drive_copy",
  "https://drive.google.com/open?id=14z0P_HCF0BaY4oea1JIT_lFx_q0A-Z1G&usp=drive_copy",
  "https://drive.google.com/open?id=15ELk2BhApW2P5yl0EFo1TyUl6-9VsJdY&usp=drive_copy",
  "https://drive.google.com/open?id=15QhKT-p2d8FzB8dGlKljY8TZmFCQKmA7&usp=drive_copy",
  "https://drive.google.com/open?id=15aXDAFjtV9J4oEb2M_tMyf09g67WaZ24&usp=drive_copy",
  "https://drive.google.com/open?id=15jUBcPSMT2x1ByuXUmoN0aOG9jwQHRfF&usp=drive_copy",
  "https://drive.google.com/open?id=15mz4OE7u8HufGpZZ8EZEvutQy5uJxkMv&usp=drive_copy",
  "https://drive.google.com/open?id=15uIg9LQzx9abHwPjxqntZzBDNse0b2Hz&usp=drive_copy",
  "https://drive.google.com/open?id=16DAgyPsm2vsW0z_YcU4lz6XOSGBggrUJ&usp=drive_copy",
  "https://drive.google.com/open?id=16G6T2WyNLzeEyLZ6ij2_fzvx6SaAbFCT&usp=drive_copy",
  "https://drive.google.com/open?id=16KAt6dEdapIGRVmY8Z_F8cZneI90FBeC&usp=drive_copy",
  "https://drive.google.com/open?id=16QS2QL1rHoOkWmX0NxahbtFdA7m7HwBR&usp=drive_copy",
  "https://drive.google.com/open?id=16aG_6GEmR5o3-LrLTF_HXg1z7rYsv4O2&usp=drive_copy",
  "https://drive.google.com/open?id=16bD7m6KBbNIS1El6qa9SyG2Noh-vhHjb&usp=drive_copy",
  "https://drive.google.com/open?id=16fdkS8nRzVpkbuP-7du4ZHE9EqrUuBf7&usp=drive_copy",
  "https://drive.google.com/open?id=16l-xTR1TLgTkt1y1y5eWfYd4l8Ba4rMk&usp=drive_copy",
  "https://drive.google.com/open?id=16o6s6SZ5V4F6gAtWkzEci7hspmX9Z4-J&usp=drive_copy",
  "https://drive.google.com/open?id=16r7NllFES8ucy64SkhJmA0VEabkDkCrC&usp=drive_copy",
  "https://drive.google.com/open?id=16wOp5q0kwOmW06toYPscmUOeDB0Zoy2r&usp=drive_copy",
  "https://drive.google.com/open?id=17-2-q77Xep7DdjlsLFp0URyEjp73pq0J&usp=drive_copy",
  "https://drive.google.com/open?id=17GJv6UD6WrLzhqn_wX6fRLoH2xgA1U9c&usp=drive_copy",
  "https://drive.google.com/open?id=17L8WixLFSsTCgHG2M7r0eH3vl73uHlGh&usp=drive_copy",
  "https://drive.google.com/open?id=17WJL9_Vy-SCLwGCRPfjynRvD0_U5oH-4&usp=drive_copy",
  "https://drive.google.com/open?id=17gDMXb_13ybG1KX6Oaq2TWW2j1Oi3I1q&usp=drive_copy",
  "https://drive.google.com/open?id=17iZsm9DhfW7AFtWEr9ykK2k3FYNh_zO0&usp=drive_copy",
  "https://drive.google.com/open?id=17s8lQO5jqU0pYP0wrp4Zp6bqQUkDFA-M&usp=drive_copy",
  "https://drive.google.com/open?id=17uImFk0urPKrohsK92sUO4dIRHuy_dXp&usp=drive_copy",
  "https://drive.google.com/open?id=17zUQflH88oD_h4A3wAFWpBOsqbHDoZPB&usp=drive_copy",
  "https://drive.google.com/open?id=18CnU1usl7pDAW2WjSOwXq16HSWkjjX4z&usp=drive_copy",
  "https://drive.google.com/open?id=18NV3g1DNh67-d2pl7eT_Bztt6k0A-2Sa&usp=drive_copy",
  "https://drive.google.com/open?id=18NYkN0MsqdVbV9xyznL1do26cgfpY_lF&usp=drive_copy",
  "https://drive.google.com/open?id=18R6aSPt2DOxPDeBlUN70lOgyV-VfiN_I&usp=drive_copy",
  "https://drive.google.com/open?id=18k79xewY2mEesnXtXELlcHtj8mMY_1eT&usp=drive_copy",
  "https://drive.google.com/open?id=18t-a06mUtSx8uG1L3mZKn2ziSZK4Rk8b&usp=drive_copy",
  "https://drive.google.com/open?id=18zhwTcWZ9OwCkKmS0mOXlq4X_8MJpBKo&usp=drive_copy",
  "https://drive.google.com/open?id=19D3D_Xa0rCk2LN9NL5irihxa5xv_yLO9&usp=drive_copy",
  "https://drive.google.com/open?id=19Hk5J47CkF0qecTyvs86jfT_kYpylUBs&usp=drive_copy",
  "https://drive.google.com/open?id=19IHHX1GRLBaTy4FDVq92InKnSQ-k0vC5&usp=drive_copy",
  "https://drive.google.com/open?id=19Kw3bV7h8xaEv9WcHWazsZw1zJ9MtnNC&usp=drive_copy",
  "https://drive.google.com/open?id=19Np9W9n0Y5tOXAyK5pE6pu4f1H3d5Dme&usp=drive_copy",
  "https://drive.google.com/open?id=19VMK8P6hW8f6qVQ_P9mAdDPVjHo9ST6C&usp=drive_copy",
  "https://drive.google.com/open?id=19_sKTc2t7W0hnkDt6nCEpyJDxbhMOZ5N&usp=drive_copy",
  "https://drive.google.com/open?id=19ixkvx8U-QxUy9eM9KxeMLrLh9D88bU7&usp=drive_copy",
  "https://drive.google.com/open?id=19mCrZK2KMf2Xbcv8yT2x1w5q6F6gQfMM&usp=drive_copy",
  "https://drive.google.com/open?id=19nxE8i2JYklm0pfDS0dtYmg_zlN9lIQU&usp=drive_copy",
  "https://drive.google.com/open?id=19qIGCz7cA6gakx_pfwLmqK0CRnQe7OYB&usp=drive_copy",
  "https://drive.google.com/open?id=19wBqf8VVylWgB6E6OEBIRln-tyLVUp4m&usp=drive_copy",
  "https://drive.google.com/open?id=19z9rHVsniVWodB2xlvu78Jdm7OeAfCr1&usp=drive_copy",
  "https://drive.google.com/open?id=1A-wyxkE2sgz_F3dD19B8oyxRAZ6W8Kjf&usp=drive_copy",
  "https://drive.google.com/open?id=1A0LQshRtTo-YuRylTXwNHMrqjvsB-MGZ&usp=drive_copy",
  "https://drive.google.com/open?id=1A9_oK4OSKQhK89T_8vE9C8m5PYKfG7mS&usp=drive_copy",
  "https://drive.google.com/open?id=1AAJ8SYGH0c1tRtS-0az8fgjFzhQH1fLo2&usp=drive_copy",
  "https://drive.google.com/open?id=1ABG6HRzR_Fqg9Nwq6HL2H5GzErJibH6z&usp=drive_copy",
  "https://drive.google.com/open?id=1AFCUJHOMH6BrHgQXM1Z7XrA6fAqO-Qa4&usp=drive_copy",
  "https://drive.google.com/open?id=1AG26bA0U6OKMmoXHMEUVjICVeVV5CC-M&usp=drive_copy",
  "https://drive.google.com/open?id=1AGItH6cQJYhpl9xwX0GyWYoKstNpKfF0&usp=drive_copy",
  "https://drive.google.com/open?id=1AJZlLb4OHANHRZJ8h0El8WE-KjCLqpIK&usp=drive_copy",
  "https://drive.google.com/open?id=1AL39hRmT22k1FQYcYmuj8bkwrYdPlTdw&usp=drive_copy",
  "https://drive.google.com/open?id=1ALOVH0eGH9-MN_ScCdI0-ES49k6Yjxh9&usp=drive_copy",
  "https://drive.google.com/open?id=1AO3x2XNcW8b0qv-MPEvxl3RrTwABqOAt&usp=drive_copy",
  "https://drive.google.com/open?id=1AOmh73rO_F8HpD8sDOglkPOMo0xO9UMd&usp=drive_copy",
  "https://drive.google.com/open?id=1AP9eXTxLJpt36pa2-pGR09moY39edxK8&usp=drive_copy",
  "https://drive.google.com/open?id=1AQsJ93w7Uu5rsKb6Wf0Eu45xcs-NVnF1&usp=drive_copy",
  "https://drive.google.com/open?id=1ARexEEL7ge2m5q4rA5fWoei1ggXzRO2m&usp=drive_copy",
  "https://drive.google.com/open?id=1ASikUOIT7dr0VXB1ik9sw9bU3JlzhV7E&usp=drive_copy",
  "https://drive.google.com/open?id=1AThn4RlcsBAlvPxwdp4gMsFc2VdxuZt1&usp=drive_copy",
  "https://drive.google.com/open?id=1AU5IQsQZRD97DNMK6ZYejRtkixg2Wg4h&usp=drive_copy",
  "https://drive.google.com/open?id=1AWAWyDqDgbtrGnKRnR7sRY8n-LFc8JJK&usp=drive_copy",
  "https://drive.google.com/open?id=1AXfPvZewmWcuYGLwX_jc7cs6fGuJdZTQ&usp=drive_copy",
  "https://drive.google.com/open?id=1AZ90VZWz43i2FQWXUpiFkMLreE71Su2g&usp=drive_copy",
  "https://drive.google.com/open?id=1B7A0ho0s-4C09hZ2AjhEqe6Lmh8NEFGT&usp=drive_copy",
  "https://drive.google.com/open?id=1B8KY9TZVzry5r-cCBxlZ6sw9H1WbHBrB&usp=drive_copy",
  "https://drive.google.com/open?id=1B9d5-ROxkF3rfjtn5NzPA1b4s6ycywA1&usp=drive_copy",
  "https://drive.google.com/open?id=1BAUbhk3CFIlO1KIdhMsYGW9seX1tz8P4D&usp=drive_copy",
  "https://drive.google.com/open?id=1BDW27l3Jdks8dmix_PswlsMfB0QO_iM4&usp=drive_copy",
  "https://drive.google.com/open?id=1BFbFFRzNd-Lc0NhM4TTxJvTnlG-8T8D0&usp=drive_copy",
  "https://drive.google.com/open?id=1BGyB3V-KJgV2uf9KD6lKzFdvDJOGJcPv&usp=drive_copy",
  "https://drive.google.com/open?id=1BJ6pYqx7iUOMM4w_WjRny5MI2RUVivf3&usp=drive_copy",
  "https://drive.google.com/open?id=1BKnOr6T48uz7bDegh3XzGgL4r1SztplK&usp=drive_copy",
  "https://drive.google.com/open?id=1BL8G7jQw3hTOdHq8xS9t3XxO8Id9Yw30&usp=drive_copy",
  "https://drive.google.com/open?id=1BMJ1ehbF4TI_Df9C9_G_eE2eLFkHZWmc&usp=drive_copy",
  "https://drive.google.com/open?id=1BP-YobNo6HMyG5lqDRv2ReSLOpaM_Cm4&usp=drive_copy",
  "https://drive.google.com/open?id=1BQb60Nk1lo6FDFXqshNVUCRAZhhrNcQb&usp=drive_copy",
  "https://drive.google.com/open?id=1BRDlhF5uLUedrp9YgrsI1G62F2c5jK5U&usp=drive_copy"]

# Create a directory to save the downloaded files
download_dir = "downloads"

# Download files
for link in file_links:
    download_file_from_google_drive(link, download_dir)

print("All files downloaded.")
