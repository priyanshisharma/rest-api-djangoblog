# learning-rest-api-django

REST APIs have been created in a blog similar to https://github.com/priyanshisharma/DjangoBlogProject

The following functions are performed
* List
* Get Detail
* Create
* Delete
* Update


## Installation
Install using pip...

```bash
pip install requirements.txt
```
Add 'rest_framework' to your INSTALLED_APPS setting.
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Testing the APIs

Look into the API folder i.e. `../reddjan/reddjaapp/api` to have a deeper understanding, and go to 

* `..api/posts/` for Postlist
* `..api/posts/post/<post-id>` for Post Detail of Post with id post-id
* `..api/posts/post/new/` to create Post
* `..api/posts/post/<post-id>/remove/` to Delete Post with id post-id
* `..api/posts/post/<post-id>/remove/` to Update Post with id post-id
