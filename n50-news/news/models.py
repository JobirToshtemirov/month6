from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category name", unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class TagModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tag name", unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


def property(args):
    pass


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='news/authors/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    # slug = models.SlugField()
    image = models.ImageField(upload_to="news/")
    description = models.TextField()
    status = models.BooleanField(default=False)

    author = models.ForeignKey(AuthorModel,
                               on_delete=models.SET_NULL,
                               related_name="news",
                               null=True)

    categories = models.ManyToManyField(CategoryModel, related_name="news")
    tags = models.ManyToManyField(TagModel, related_name="news")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
