from django.shortcuts import render

class CreateOperation(CustomHtmxMixin, TemplateView):
    template_name = "oper_list.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Список oper"
        return super().get_context_data(**kwargs)
