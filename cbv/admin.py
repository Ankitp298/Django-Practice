from django.contrib import admin
from cbv.models import Student,Contact,Teacher,Author, Book
from django.utils.html import format_html
from django.db.models import Count
from django.urls import reverse
from urllib.parse import urlencode
# Register your models here.



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','address_color',]

    list_display_links= ['name']
    list_editable = ['age',]

    def address_color(self,obj):
        return format_html("<p style='color:red'> {} </p>",obj.address)
    address_color.short_description = "Address Status"



class Studentline(admin.StackedInline):
    model = Student
    extra = 2

class TeacherAdmin(admin.ModelAdmin):
    inlines = [Studentline]
    list_display=['name','address','age','age_group','mobile','salary_color','student_count']
    list_editable = ['age','mobile']
    list_filter = ['age',]
   
    fieldsets = (
        ("Personal info", {
            'fields': ("name","age","address"),
        }),
        ("Professional info",{
            'fields': ('salary','mobile')
        }),
    )

    def salary_color(self,obj):
        salary = obj.salary
        if salary > 10000:
            color = 'green'
        else:
            color = 'red'
        return format_html("<p style= 'color:{}'>{} </p>",color,salary)
    
    def student_count(self,obj):
        # return obj.student_set.count()
        count = obj.student_set.count()
        url = (
            reverse("admin:cbv_student_changelist")
            # + f"?teacher__id__exact={obj.id}"
            +'?'+ urlencode({'teacher__id__exact': obj.id})
        )

        return format_html('<a href="{}">{}</a>', url, count)

    def age_group(self,obj):  
        if obj.age < 25:
            return "young"
        elif obj.age <40:
            return "Middle"
        return "Old"

class BookInline(admin.TabularInline):
    model = Book
    extra = 2
    fields = ['title','publication_date']
    readonly_fields = ['publication_date']

    def some_custom_method(self,obj):
        return self.title

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ('id','name', 'book_count')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(total_books=Count('book'))
    
    # def books(self,obj):
    #     return obj.book_set.count()

    def book_count(self, obj):
        url = (
            reverse("admin:cbv_book_changelist")
            + f"?author__id__exact={obj.id}"
        )
        return format_html('<a href="{}">{}</a>', url, obj.total_books)

    book_count.short_description = "Total Books"

class ContactAdmin(admin.ModelAdmin):
    list_display = ("to","subject","message")

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj = ...):
        return False

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','publication_date','author_link')

    def author_link(self,obj):
        url = reverse("admin:cbv_author_changelist") + '?' + urlencode({'id':obj.author.id})
        return format_html("<a href='{}'>{} </a>",url,obj.author)

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Book,BookAdmin)    
admin.site.register(Author,AuthorAdmin)
admin.site.register(Contact,ContactAdmin)