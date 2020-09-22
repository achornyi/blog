from django.contrib.admin import AdminSite


class EditorAdminSite(AdminSite):
    site_header = 'Editor admin'


editor_admin = EditorAdminSite(name='editor_admin')
