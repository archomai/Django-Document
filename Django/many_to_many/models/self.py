from django.db import models

__all__ = (
    'FacebookUser',
)

class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # name 이 '이한영'이며
        # 친구로 '박보영', '아이유'를 가지는 경우
        # -> 이한영 (친구 : 박보영, 아이유)
        # __str__의 결과가 위처름 출력될 수 있도록 작성

        # list comprehension 사용
        # friends_string = ', '.join([f.name for f in self.friends.all()])

        # Manager의 values_list를 사용
        friends_string = ', '.join(self.friends.value_list('name', flat=True))

        return '{name} (친구 : {friends})'.format(
            name=self.name,
            friends=friends_string,
        )
