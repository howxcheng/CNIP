import os
import httpx

url = "https://raw.githubusercontent.com/Hackl0us/GeoIP2-CN/release/CN-ip-cidr.txt"
rsc_file = r"/opt/compose/caddy/www/cnip.rsc"

with open(rsc_file, "w", encoding="utf-8") as f:
    f.write("/ip firewall address-list\nremove [find list=CN_IP]\n")
    with httpx.Client() as client:
        response = client.get(url)

        # 检查响应状态码是否为 200（OK）
        if response.status_code == 200:

            # 将响应内容按行分割并打印每一行
            for line in response.text.splitlines():
                f.write("add address=" + line + " list=CN_IP\n")
        else:
            print(f"请求失败，状态码: {response.status_code}")
