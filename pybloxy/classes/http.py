import logging
import requests

class Http:
	def sendRequest(url):
		payload = requests.get(str(url))
		statusCode = payload.status_code
		content = payload.content

		if statusCode != 200:
			return logging.error(f"[Pybloxy - GET] Something went wrong! Error Code: {statusCode}")
		
		return content

	def postRequest(url, payload):
		payload = requests.post(str(url), data = payload)
		statusCode = payload.status_code
		content = payload.content

		if statusCode != 200:
			return logging.error(f"[Pybloxy - POST] Something went wrong! Error Code: {statusCode}")
		
		return content

	def patchRequest(url, payload):
		payload = requests.patch(str(url), data = payload)
		statusCode = payload.status_code
		content = payload.content

		if statusCode != 200:
			return logging.error(f"[Pybloxy - PATCH] Something went wrong! Error Code: {statusCode}")
		
		return content

	def deleteRequest(url, payload):
		payload = requests.delete(str(url))
		statusCode = payload.status_code
		content = payload.content

		if statusCode != 200:
			return logging.error(f"[Pybloxy - DELETE] Something went wrong! Error Code: {statusCode}")
		
		return content