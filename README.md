# dongle-lte-api

API For Dongle LAN/WAN LTE USB Modems, you can use this to simply get information about your internet usage, signal, and tons of other stuff
## Tested on:
* [4GDONG001](https://vi.aliexpress.com/item/1005004866748209.html?spm=a2g0o.productlist.main.11.10422d56VuClBS&algo_pvid=33188637-bff3-45b6-a248-57357591a4d9&algo_exp_id=33188637-bff3-45b6-a248-57357591a4d9-6&pdp_npi=3%40dis%21VND%211642643.0%211642643.0%21%21%21%21%21%40212279a216846025974963651d07dc%2112000030808142367%21sea%21VN%210&curPageLogUid=BmSEcUVU6U0L) 4G LTE UBS Dongle Wireless WIFI Modem Stick:
<img src="https://github.com/bxdoan/dongle-lte-api/blob/master/imgs/dongle-lte-usb.jpeg" width=40% height=40%>

* [Dongle](https://shopee.vn/Thi%E1%BA%BFt-B%E1%BB%8B-Ph%C3%A1t-WiFi-Kh%C3%B4ng-D%C3%A2y-4G-LTE-150Mbps-i.141578331.22717436016) 4G LTE USB Modem Stick:

<img src="https://github.com/bxdoan/dongle-lte-api/blob/master/imgs/dongle_stick.jpeg" width=40% height=40%>

## Install
```shell
pip3 install git+https://github.com/bxdoan/dongle-lte-api.git
```

## Usage
<details>
  <summary>📚 Click to see some basic examples</summary>

```python3
from dongle_lte_api import Dongle

info = Dongle().get_data()

print(info)
```

Result dict

```python3
{
   "ssidName":"DonHandsome",
   "signalStrength":-74,
   "sn":"1000000051E834",
   "simCardState":"valid",
   "systemVersion":"UFI103_V02_ZX_DD_230306",
   "appVersion":"WEB_V1.0.311#",
   "imei":"861323063168235",
   "basebandVersion":"UFI103_CT 20220801",
   "mac":"5c:a0:00:7b:05:3f",
   "wanIpAddress":"10.188.47.213",
   "imsi":"452021123670828",
   "iccId":"89840200011236708283",
   "hardwareVersion":"HW1.3"
}
```

Reboot network

```python3
from dongle_lte_api import Dongle

Dongle().reboot()
```

Change SSID

```python3
from dongle_lte_api import Dongle

Dongle().change_ssid(ssid="Don123")
```

Change password

```python3
from dongle_lte_api import Dongle

Dongle().change_password(password="12344321")
```

NOTE : change password/change ssid/reboot action will automate restart the modems
</details>

## Contact

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/bxdoan)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/bxdoan)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hi@bxdoan.com)

## Thanks for use
Buy me a coffee

[![buymecoffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/bxdoan)
[![bxdoan.eth](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)](https://etherscan.io/address/0x610322AeF748238C52E920a15Dd9A8845C9c0318)
[![paypal](	https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/bxdoan)
