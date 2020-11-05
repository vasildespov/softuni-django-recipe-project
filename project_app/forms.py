from project_app.models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""



class DisabledRecipeForm():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class DeleteRecipeForm(RecipeForm, DisabledRecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledRecipeForm.__init__(self)
