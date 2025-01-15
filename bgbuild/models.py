from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Dropdown fields
BUILD_ROLES = [
    ('melee', 'Melee'),
    ('ranged', 'Ranged'),
    ('support', 'Support'),
]

BASE_CLASS = [
    ('n/a', 'N/A'),
    ('barbarian', 'Barbarian'),
    ('bard', 'Bard'),
    ('cleric', 'Cleric'),
    ('druid', 'Druid'),
    ('fighter', 'Fighter'),
    ('monk', 'Monk'),
    ('paladin', 'Paladin'),
    ('ranger', 'Ranger'),
    ('rogue', 'Rogue'),
    ('sorcerer', 'Sorcerer'),
    ('warlock', 'Warlock'),
    ('wizard', 'Wizard')
]

BARBARIAN_SUBCLASS = [
    ('berserker', 'Berserker'),
    ('wild magic', 'Wild Magic'),
    ('wildheart', 'Wildheart')
]

BARD_SUBCLASS = [
    ('college of lore', 'College of Lore'),
    ('college of valour', 'College of Valour'),
    ('college of swords', 'College of Swords')
]

CLERIC_DOMAIN = [
    ('life', 'Life'),
    ('light', 'Light'),
    ('trickery', 'trickery'),
    ('knowledge', 'Knowledge'),
    ('nature', 'Nature'),
    ('tempest', 'Tempest'),
    ('war', 'War')
]

DRUID_SUBCLASS = [
    ('circle of the land', 'Circle of the Land'),
    ('circle of the moon', 'Circle of the Moon'),
    ('circle of the spores', 'Circle of the Spores'),
]

FIGHTER_SUBCLASS = [
    ('battle master', 'Battle Master'),
    ('eldritch knight', 'Eldritch Knight'),
    ('champion', 'Champion')
]

MONK_SUBCLASS = [
    ('way of the four elements', 'Way of the Four Elements'),
    ('way of the open hand', 'Way of the Open Hand'),
    ('way of shadow', 'Way of Shadow'),
]

PALADIN_OATH = [
    ('oath of the ancients', 'Oath of the Ancients'),
    ('oath of devotion', 'Oath of Devotion'),
    ('oath of vengeance', 'Oath of Vengeance'),
    ('oathbreaker', 'Oathbreaker'),
]

RANGER_SUBCLASS = [
    ('hunter', 'Hunter'),
    ('beast master', 'Beast Master'),
    ('gloom stalker', 'Gloom Stalker')
]

ROGUE_SUBCLASS = [
    ('thief', 'Thief'),
    ('arcane trickster', 'Arcane Trickster'),
    ('assassin', 'Assassin')
]

SORCERER_SUBCLASS = [
    ('wild magic', 'Wild Magic'),
    ('draconic bloodline', 'Draconic Bloodline'),
    ('storm sorcery', 'Storm Sorcery')
]

WARLOCK_SUBCLASS = [
    ('the fiend', 'The Fiend'),
    ('the great old one', 'The Great Old One'),
    ('the archfey', 'The Archfey')
]

WIZARD_SCHOOL = [
    ('abjuration', 'Abjuration'),
    ('evocation', 'Evocation'),
    ('necromancy', 'Necromancy'),
    ('conjuration', 'Conjuration'),
    ('enchantment', 'Enchantment'),
    ('divination', 'Divination'),
    ('illusion', 'Illusion'),
    ('transmutation', 'Transmutation')
]

MULTICLASS = [
    ('no', 'No'),
    ('yes', 'Yes'),
]

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Bgbuild(models.Model):
    """
    A model to create Baldur's Gate 3 build posts.
    """
    user = models.ForeignKey(
        User, related_name='build_owner', on_delete=models.CASCADE)
    bgbuild_title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=250, unique=True)
    bgbuild_role = models.CharField(
        max_length=50, choices=BUILD_ROLES, default='Melee')
    bgbase_class = models.CharField(
        max_length=10, choices=BASE_CLASS, default='N/A')
    
    barbarian_subclass = models.CharField(
        max_length=50, choices=BARBARIAN_SUBCLASS, default='Beserker'
    )
    bard_subclass = models.CharField(
        max_length=50, choices=BARD_SUBCLASS, default='College of Lore'
    )
    cleric_domain = models.CharField(
        max_length=50, choices=CLERIC_DOMAIN, default='Life'
    )
    druid_subclass = models.CharField(
        max_length=50, choices=DRUID_SUBCLASS, default='Circle of the Land'
    )
    druid_subclass = models.CharField(
        max_length=50, choices=DRUID_SUBCLASS, default='Circle of the Land'
    )
    fighter_subclass = models.CharField(
        max_length=50, choices=FIGHTER_SUBCLASS, default='Champion'
    )
    monk_subclass = models.CharField(
        max_length=50, choices=MONK_SUBCLASS, default='Way of the Four Elements'
    )
    paladin_oath = models.CharField(
        max_length=50, choices=PALADIN_OATH, default='Oath of the Ancients'
    )
    ranger_subclass = models.CharField(
        max_length=50, choices=RANGER_SUBCLASS, default='Hunter'
    )
    rogue_subclass = models.CharField(
        max_length=50, choices=ROGUE_SUBCLASS, default='Thief'
    )
    sorcerer_subclass = models.CharField(
        max_length=50, choices=SORCERER_SUBCLASS, default='Wild Magic'
    )
    warlock_subclass = models.CharField(
        max_length=50, choices=WARLOCK_SUBCLASS, default='The Fiend'
    )
    wizard_school = models.CharField(
        max_length=50, choices=WIZARD_SCHOOL, default='Abjuration'
    )
    
    multiclass = models.CharField(
        max_length=3, choices=MULTICLASS, default='No')    
    multiclass_one = models.CharField(
        max_length=10, choices=BASE_CLASS, default='N/A')    
    multiclass_two = models.CharField(
        max_length=10, choices=BASE_CLASS, default='N/A')
    classone_level = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
    )
    
    excerpt = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.build_title} | Posted by {self.user}"
    