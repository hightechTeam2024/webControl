from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from serial import Serial
import json

s = Serial('COM4', baudrate=9600)

# Create your views here.
@ensure_csrf_cookie
def index(request):
	if request.method == 'POST':
		jsonData = json.loads(request.body)
		joy1PosX = jsonData.get('joy1PosX')
		joy1PosY = jsonData.get('joy1PosY')
		joy2PosX = jsonData.get('joy2PosX')
		joy2PosY = jsonData.get('joy2PosY')
		print(joy1PosX, joy1PosY, joy2PosX, joy2PosY)
		# buffer = [bytes(it) for it in [joy1PosX, joy1PosY, joy2PosX, joy2PosY, 0, 0, 0, 0]]
		s.write(f'{joy1PosX} {joy1PosY} {joy2PosX} {joy2PosY}\n'.encode('utf-8'))
		print(f'{joy1PosX} {joy1PosY} {joy2PosX} {joy2PosY}')
	return render(request, 'control/index.html')

def silent(request):
	print(f'silent')
	# s.write('0/n'.encode('utf-8'))
	return HttpResponse(200)

def dir(request, dir):
	print(f'dir = {dir}')
	# # print(s.read_all())
	# if (dir == 'forward'): s.write('1/n'.encode('utf-8'))
	# elif (dir == 'left'): s.write('2/n'.encode('utf-8'))
	# elif (dir == 'backward'): s.write('3/n'.encode('utf-8'))
	# elif (dir == 'right'): s.write('4/n'.encode('utf-8'))
	return HttpResponse(200)