from django.db import models


class TwitterUser(models.Model):
    """
    내가 A를 팔로우함
        나는 A의 follwer
        A는 나의 followee

    A와 내가 서로 follo함
        나와 A는 friend

    Block기능이 있어야 함
    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',
    )

class Relation(models.Model):
    """
    유저간의 관계를 정의하는 모델
    단순히 자신의 MTM이 아닌 중개모델의 역할을 함
    추가적으로 받는 정보는 관계의 타입(팔로인 또는 차단)
    """
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로인'),
        (RELATION_TYPE_BLOCK, '차단'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)