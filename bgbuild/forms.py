from .models import Bgcomment, Bgreply, Bgbuild
from django import forms


class BgcommentForm(forms.ModelForm):
    class Meta:
        model = Bgcomment
        fields = ('body',)


class BgreplyForm(forms.ModelForm):
    class Meta:
        model = Bgreply
        fields = ('body',)


class BgbuildForm(forms.ModelForm):
    """
    A form for creating and updating lego build posts.

    """
    class Meta:
        model = Bgbuild
        fields = ['bgbuild_title', 'slug', 'bgbuild_image',
                  'bgbuild_role', 'bgbase_class', 'barbarian_subclass',
                  'bard_subclass', 'cleric_domain', 'druid_subclass',
                  'fighter_subclass', 'monk_subclass', 'paladin_oath',
                  'ranger_subclass', 'rogue_subclass', 'sorcerer_subclass',
                  'warlock_subclass', 'wizard_school', 'multiclass', 'multiclass_one',
                  'multiclass_two', 'level_split', 'main_key_ability', 'secondary_key_ability',
                  'suggested_skill', 'suggested_skill', 'difficulty', 'excerpt', 'content']
        labels = {
            'bgbuild_title': "Build Title",
            'slug': "Slug (Title lowercase, and spaces replaced with '-')",
            'bgbuild_image': "Build Image",
            'bgbuild_role': "Build role",
            'bgbase_class': "Base class",
            'barbarian_subclass': "Barbarian subclass",
            'bard_subclass': "Bard subclass",
            'cleric_domain': "Cleric domain",
            'druid_subclass': "Druid subclass",
            'fighter_subclass': "Fighter subclass",
            'monk_subclass': "Monk subclass",
            'paladin_oath': "Paladin oath",
            'ranger_subclass': "Ranger subclass",
            'rogue_subclass': "Rogue subclass",
            'sorcerer_subclass': "Sorcerer subclass",
            'warlock_subclass': "Warlock subclass",
            'wizard_school': "Wizard school",
            'multiclass': "Multiclass?",
            "multiclass_one": "Additional class",
            "multiclass_two": "Class",
            "excerpt": "Build Headline",
            "content": "Write something about the build"
        }
