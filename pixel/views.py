from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

from pixel.models import CountModel


class LeadView(TemplateView):
    template_name = "html/base.html"

    def get(self, request, *args, **kwargs):
        pixel_id = request.GET.get('pixel', '910583330092128')
        CountModel.objects.create(team='Светлая')
        if pixel_id:
            return render(request, self.template_name, {'pixel_id': pixel_id})
        else:
            return HttpResponse('Pixel ID is not provided')


class LeadDarkView(TemplateView):
    template_name = "html/base_dark.html"

    def get(self, request, *args, **kwargs):
        pixel_id = request.GET.get('pixel', '910583330092128')
        CountModel.objects.create(team='Темная')
        if pixel_id:
            return render(request, self.template_name, {'pixel_id': pixel_id})
        else:
            return HttpResponse('Pixel ID is not provided')


def re_dark(request):
    CountModel.objects.create(team='Нажатие Темная')
    return HttpResponseRedirect('https://t.me/+doGCw_WqWhNhZTNh')


def re_white(request):
    CountModel.objects.create(team='Нажатие Светлая')
    return HttpResponseRedirect('https://t.me/+h3viYl2cRS4yNmNi')
