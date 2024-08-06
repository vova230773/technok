from django import forms
from core.models import Counterparts
from operation.models import oper_mod
from technological_card.models import tk_mod
from product.models import product_mod

class KontrForm(forms.ModelForm):

    class Meta:
        model = Counterparts
        fields = '__all__'
#         fields = (
#             "name",
#             "slug",
#             "country",
#             "city",
#             "street",
#             "number",
#             "letter",
#             "full_name",
#             "okpo_cod",
#             "inn",
#             "director",
#             "phone",
#   )
        
class TkForm(forms.ModelForm):

    class Meta:
        model = tk_mod
        fields = '__all__'

class TMCForm(forms.ModelForm):

    class Meta:
        model = product_mod
        fields = '__all__'

class OPERForm(forms.ModelForm):

    class Meta:
        model = oper_mod
        fields = '__all__'