from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Character(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL)

    name = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    char_class = models.CharField(max_length=30)
    created_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

class Stats(models.Model):
    belongs_to = models.ForeignKey('Character')

    str = models.SmallIntegerField(blank=True, null=True)
    dex = models.SmallIntegerField(blank=True, null=True)
    con = models.SmallIntegerField(blank=True, null=True)
    int = models.SmallIntegerField(blank=True, null=True)
    wis = models.SmallIntegerField(blank=True, null=True)
    cha = models.SmallIntegerField(blank=True, null=True)

    str_mod = models.SmallIntegerField(blank=True, null=True)
    dex_mod = models.SmallIntegerField(blank=True, null=True)
    con_mod = models.SmallIntegerField(blank=True, null=True)
    int_mod = models.SmallIntegerField(blank=True, null=True)
    wis_mod = models.SmallIntegerField(blank=True, null=True)
    cha_mod = models.SmallIntegerField(blank=True, null=True)

class Misc(models.Model):
    belongs_to = models.ForeignKey('Character')

    hp = models.SmallIntegerField(blank=True, null=True)
    ac = models.SmallIntegerField(blank=True, null=True)
    flatfooted_ac = models.SmallIntegerField(blank=True, null=True)
    touch_ac = models.SmallIntegerField(blank=True, null=True)
    init = models.SmallIntegerField(blank=True, null=True)
    speed = models.SmallIntegerField(blank=True, null=True)
    damage_resistance = models.SmallIntegerField(blank=True, null=True)
    languages = models.TextField(blank=True)

class Skills(models.Model):
    belongs_to = models.ForeignKey('Character')

    skill_name = models.CharField(max_length=30)
    ranks = models.SmallIntegerField(blank=True, null=True)

class Saves(models.Model):
    belongs_to = models.ForeignKey('Character')

    fort = models.SmallIntegerField(blank=True, null=True)
    reflex = models.SmallIntegerField(blank=True, null=True)
    will = models.SmallIntegerField(blank=True, null=True)

class Maneuvers(models.Model):
    belongs_to = models.ForeignKey('Character')

    cmb = models.SmallIntegerField(blank=True, null=True)
    cmd = models.SmallIntegerField(blank=True, null=True)

class Attacks(models.Model):
    belongs_to = models.ForeignKey('Character')

    attack_name = models.CharField(max_length=30)
    atk_bonus = models.SmallIntegerField(blank=True, null=True)
    crit = models.CharField(blank=True, max_length=30)
    damage = models.CharField(blank=True, max_length=30)
    range = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(blank=True, max_length=5)

class Armor(models.Model):
    belongs_to = models.ForeignKey('Character')

    armor_name = models.CharField(blank=True, max_length=30)
    ac_bonus = models.SmallIntegerField(blank=True, null=True)
    max_dex = models.SmallIntegerField(blank=True, null=True)
    armor_penalty = models.SmallIntegerField(blank=True, null=True)

class Spells(models.Model):
    belongs_to = models.ForeignKey('Character')

    spell_name = models.CharField(blank=True, max_length=100)
    spell_desc = models.TextField(blank=True)
    spell_lvl = models.SmallIntegerField(blank=True, null=True)

class Money(models.Model):
    belongs_to = models.ForeignKey('Character')

    gold = models.SmallIntegerField(blank=True, null=True)
    silver = models.SmallIntegerField(blank=True, null=True)
    copper = models.SmallIntegerField(blank=True, null=True)

class Gear(models.Model):
    belongs_to = models.ForeignKey('Character')

    item_name = models.CharField(blank=True, max_length=30)
    item_weight = models.SmallIntegerField(blank=True, null=True)

class Feats(models.Model):
    belongs_to = models.ForeignKey('Character')

    feat_name = models.CharField(blank=True, max_length=30)
    feat_desc = models.TextField(blank=True)

class Links(models.Model):
    belongs_to = models.ForeignKey('Character')

    link_name = models.CharField(blank=True, max_length=100)
    link_url = models.URLField(blank=True)
