from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class LeadView(TemplateView):
    template_name = "html/base.html"

    def get(self, request, *args, **kwargs):
        pixel_id = request.GET.get('pixel', None)
        if pixel_id:
            return render(request, self.template_name, {'pixel_id': pixel_id})
        else:
            return HttpResponse('Pixel ID is not provided')
