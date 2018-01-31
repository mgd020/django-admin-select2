# django-admin-select2

Enable select2 for Django admin `select` inputs.

Automatically applies to all `select`s, excluding filtered selects (e.g. `auth.User.groups`).

Tested with Django versions 1.11 and 2.0.

## Installation

```shell
pip install django-admin-select2
```

Update `settings.py`:

```python
INSTALLED_APPS = [
    ...
    # must go before django.contrib.admin
    'django_admin_select2',
    ...
]
```

## How it works

This app adds an overriding template for `admin/base_site.html`, adding the required css and js to `extrahead` and `footer` blocks respectively.
