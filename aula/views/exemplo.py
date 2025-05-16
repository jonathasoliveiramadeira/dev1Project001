from .base_model import BaseModel

class Exemplo(BaseModel):

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.cod is None or self.cod =='':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kwargs)

    def clean(self):
        if not isinstance(str(self.nome), str):
            raise ValidationError({
                "nome": "Nome informado é do tipo errado"},
            code="error001")
        elif self.nome == "Teste":
            raise ValidationError(
                {"nome": "Não é possivel salvar testes!"},
                code="error002")
        elif self.cod == "1111111111" and self.nome == "IFRS Restinga":
            raise ValidationError(
                {"nome": "Combinação de nome e código errada!",
                 "cod": "Combinação de nome e código errada"},
                code="error0101")