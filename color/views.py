from django.shortcuts     import redirect
from django.views.generic import ListView
from color.models   import Color
 
MIN_SEARCH_CHARS = 2

class ColorList(ListView):
   
    model = Color
    context_object_name = "colors"
 
    def dispatch(self, request, *args, **kwargs):
        self.request = request     #So get_context_data can access it.
        return super(ColorList, self).dispatch(request, *args, **kwargs)
 
    def get_queryset(self):
        
        return  super(ColorList, self).get_queryset()
 
    def get_context_data(self, **kwargs):
        #The current context.
        context = super(ColorList, self).get_context_data(**kwargs)
 
        global  MIN_SEARCH_CHARS
 
        search_text = ""  
        if(self.request.method == "GET"):
           
            search_text = self.request.GET.get("search_text", "").strip().lower()
            if(len(search_text) < MIN_SEARCH_CHARS):
                search_text = ""   
 
        if(search_text != ""):
            color_search_results = Color.objects.filter(name__contains=search_text)
        else:
            color_search_results = []
 
        context["search_text"] = search_text
        context["color_search_results"] = color_search_results
 

        context["MIN_SEARCH_CHARS"] = MIN_SEARCH_CHARS
 
        return  context
 
def toggle_color_like(request, color_id):

    color = None
    try:
       
        color = Color.objects.filter(id=color_id)[0]
    except Color.DoesNotExist as e:
        raise  ValueError("Unknown color.id=" + str(color_id) + ". Original error: " + str(e))
 

    color.is_favorited = not color.is_favorited
    color.save()  
    return  redirect("color_list")  #See urls.py
