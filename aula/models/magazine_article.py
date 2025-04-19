from .magazine import *
from .article import *

class MagazineArticle(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)

    def __str__(self):
        return self.article