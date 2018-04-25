from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from servers.models import Server1C, Port
from .forms import Server1CForm


def index(request):
    # return HttpResponse("index page")
    return render(request, 'servers/index.html')

def servers1c(request):
	base_list =[]
	server_list = []
	servers1c = Server1C.objects.order_by('name')
	for server in servers1c:
		for port in server.port.all():
			server_list.append(str(server.name) + ':' + str(port.number))

	ports = server.port.all()

	context = {'servers': servers1c, 'ports': ports, 'server_list': server_list}
	return render(request, 'servers/servers1c.html', context)

def new_server1c(request):
	if request.method != 'POST':
		form = Server1CForm()
	else:
		form = Server1CForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('servers:servers1c'))
	context = {'form': form}
	return render(request, 'servers/new_server1c.html', context)