from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportMixin, ExportMixin , ImportMixin
from import_export.formats import base_formats
from import_export import fields
from import_export.widgets import ManyToManyWidget
from import_export.admin import ExportActionModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('pk','name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('pk','name')


class BookResource(resources.ModelResource):

    #many to manyフィールドのカテゴリ名でExport
    categories = fields.Field(attribute='categories', widget=ManyToManyWidget(Category, field="name"))

    class Meta:
        model = Book
        skip_unchanged = True
        fields = [ 'name', 'author','categories']
        export_order = ['author', 'name','categories']


    def get_export_headers(self):
        #Exportデータのヘッダをモデルのverbose_nameに変更する関数
        headers = []
        for field in self.get_fields():
            model_fields = self.Meta.model._meta.get_fields()
            header = next((
                str(x.verbose_name) for x in model_fields
                if x.name == field.column_name
            ), field.column_name)
            headers.append(header)
        return headers

    def dehydrate_author(self, book):
        #外部テーブル(authoor）の値でExportする
        return '%s' % (book.author)


@admin.register(Book)
class BookAdmin(ImportExportMixin, ExportActionModelAdmin, admin.ModelAdmin):
    list_display=('pk','name', 'author')
    resource_class = BookResource
    formats = [base_formats.XLSX]
