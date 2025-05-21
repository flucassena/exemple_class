from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=False,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
    )

    class Meta:
        abstract = True
        managed = True


class Author(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=255,
        null=False,
    )

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Album(ModelBase):
    title = models.CharField(
        db_column='tx_title',
        max_length=255,
        null=False,
    )

    date = models.DateField(
        db_column='dt_date',
        null=False,
    )

    author = models.ForeignKey(
        Author,
        db_column='id_author',
        on_delete=models.CASCADE,
        null=False,
    )

    class Meta:
        db_table = 'album'
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'


class Music(ModelBase):
    title = models.CharField(
        db_column='tx_title',
        max_length=255,
        null=False,
    )

    duration = models.DurationField(
        db_column='tm_duration',
        null=False,
    )

    album = models.ForeignKey(
        Album,
        db_column='id_album',
        on_delete=models.CASCADE,
        null=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'music'
        verbose_name = 'Music'
        verbose_name_plural = 'Musics'
