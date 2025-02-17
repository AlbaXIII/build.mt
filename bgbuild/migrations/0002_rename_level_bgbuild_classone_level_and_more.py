# Generated by Django 4.2.17 on 2025-01-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgbuild', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bgbuild',
            old_name='level',
            new_name='classone_level',
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='barbarian_subclass',
            field=models.CharField(choices=[('berserker', 'Berserker'), ('wild magic', 'Wild Magic'), ('wildheart', 'Wildheart')], default='Beserker', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='bard_subclass',
            field=models.CharField(choices=[('college of lore', 'College of Lore'), ('college of valour', 'College of Valour'), ('college of swords', 'College of Swords')], default='College of Lore', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='cleric_domain',
            field=models.CharField(choices=[('life', 'Life'), ('light', 'Light'), ('trickery', 'trickery'), ('knowledge', 'Knowledge'), ('nature', 'Nature'), ('tempest', 'Tempest'), ('war', 'War')], default='Life', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='druid_subclass',
            field=models.CharField(choices=[('circle of the land', 'Circle of the Land'), ('circle of the moon', 'Circle of the Moon'), ('circle of the spores', 'Circle of the Spores')], default='Circle of the Land', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='fighter_subclass',
            field=models.CharField(choices=[('battle master', 'Battle Master'), ('eldritch knight', 'Eldritch Knight'), ('champion', 'Champion')], default='Champion', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='monk_subclass',
            field=models.CharField(choices=[('way of the four elements', 'Way of the Four Elements'), ('way of the open hand', 'Way of the Open Hand'), ('way of shadow', 'Way of Shadow')], default='Way of the Four Elements', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='multiclass_one',
            field=models.CharField(choices=[('n/a', 'N/A'), ('barbarian', 'Barbarian'), ('bard', 'Bard'), ('cleric', 'Cleric'), ('druid', 'Druid'), ('fighter', 'Fighter'), ('monk', 'Monk'), ('paladin', 'Paladin'), ('ranger', 'Ranger'), ('rogue', 'Rogue'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'), ('wizard', 'Wizard')], default='N/A', max_length=10),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='multiclass_two',
            field=models.CharField(choices=[('n/a', 'N/A'), ('barbarian', 'Barbarian'), ('bard', 'Bard'), ('cleric', 'Cleric'), ('druid', 'Druid'), ('fighter', 'Fighter'), ('monk', 'Monk'), ('paladin', 'Paladin'), ('ranger', 'Ranger'), ('rogue', 'Rogue'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'), ('wizard', 'Wizard')], default='N/A', max_length=10),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='paladin_oath',
            field=models.CharField(choices=[('oath of the ancients', 'Oath of the Ancients'), ('oath of devotion', 'Oath of Devotion'), ('oath of vengeance', 'Oath of Vengeance'), ('oathbreaker', 'Oathbreaker')], default='Oath of the Ancients', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='ranger_subclass',
            field=models.CharField(choices=[('hunter', 'Hunter'), ('beast master', 'Beast Master'), ('gloom stalker', 'Gloom Stalker')], default='Hunter', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='rogue_subclass',
            field=models.CharField(choices=[('thief', 'Thief'), ('arcane trickster', 'Arcane Trickster'), ('assassin', 'Assassin')], default='Thief', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='sorcerer_subclass',
            field=models.CharField(choices=[('wild magic', 'Wild Magic'), ('draconic bloodline', 'Draconic Bloodline'), ('storm sorcery', 'Storm Sorcery')], default='Wild Magic', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='warlock_subclass',
            field=models.CharField(choices=[('the fiend', 'The Fiend'), ('the great old one', 'The Great Old One'), ('the archfey', 'The Archfey')], default='The Fiend', max_length=50),
        ),
        migrations.AddField(
            model_name='bgbuild',
            name='wizard_school',
            field=models.CharField(choices=[('abjuration', 'Abjuration'), ('evocation', 'Evocation'), ('necromancy', 'Necromancy'), ('conjuration', 'Conjuration'), ('enchantment', 'Enchantment'), ('divination', 'Divination'), ('illusion', 'Illusion'), ('transmutation', 'Transmutation')], default='Abjuration', max_length=50),
        ),
    ]
