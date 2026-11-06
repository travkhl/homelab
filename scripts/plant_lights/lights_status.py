import pywemo

ips = ['10.0.128.26', '10.0.128.45']

urls = [pywemo.setup_url_for_address(ip) for ip in ips]

#print(urls)

devices = [pywemo.discovery.device_from_description(url) for url in urls]

for device in devices:
	print(f"Device @ {device.host} is {'ON' if device.get_state() else 'OFF'}")

