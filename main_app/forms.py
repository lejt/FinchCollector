from django.forms import ModelForm
from .models import Feeding

# custom form 
class FeedingForm(ModelForm):
    # meta class declared to indicate fields for input
    class Meta:
        model = Feeding
        fields = ['date', 'meal']