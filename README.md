# Admin Search Plus

Admin Search Plus is a AdminMixin for Django that limits searches to specific fields which greatly enhances performance when working on large datasets.


## Installation

`$ pip install admin-search-plus`

## Usage

1. Add `admin_search_plus` to your `INSTALLED_APPS` before `django.contrib.admin`:
    
    ```
    INSTALLED_APPS = [
        'admin_search_plus',
        ...
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

2. In `admin.py` import `AdminSearchPlusMixin` to add search functions to `ModelAdmin`. 

    ```
    from admin_search_plus import AdminSearchPlusMixin

    class YourModelAdmin(AdminSearchPlusMixin, admin.ModelAdmin):
        search_fields = ['field_1', 'field_2', 'field_3']

    admin.site.register(YourModel, YourModelAdmin)

    ```

