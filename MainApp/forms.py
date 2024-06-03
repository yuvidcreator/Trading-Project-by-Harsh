from django import forms  
class TradingForm(forms.Form):    
    file      = forms.FileField() # for creating file input  
    candle = forms.IntegerField(min_value=0)