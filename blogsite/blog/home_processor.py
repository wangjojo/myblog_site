from .models import Category,Blog
 
#home_display_categorys = Category.objects.filter(home_display=True)# 设置是否显示栏目
home_display_categorys = Category.objects.all()

def home_category(request):
    return {'home_display_categorys': home_display_categorys}