import pywemo

ips = ['10.0.128.26', '10.0.128.45']

urls = [pywemo.setup_url_for_address(ip) for ip in ips]

#print(urls)

devices = [pywemo.discovery.device_from_description(url) for url in urls]

for device in devices:
	device.on()

print(f"lights turned on for ips {ips}")
