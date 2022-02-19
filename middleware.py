
from utils.Database import Database


class HandleRequest():
	def __init__(self) -> None:
		self.data = Database("address.db")
		pass

	def ip_get(self):
		ip = self.data.getLastIP("ip")
		return {"ip":ip}

	def ip_post(self, req):
		day = req['day']
		month = req["month"]
		ip = req["ip"]
		try: 
			self.data.insertIP("ip", day, month, ip)
			return 200
		except Exception as e:
			return 400