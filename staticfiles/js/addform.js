//hide & slugify input field 
const title = document.querySelector('#id_bgbuild_title');
const slug = document.querySelector('#id_slug');
const slug_div = document.getElementById("div_id_slug");

slug_div.style.display = ("none");

title.onkeyup = () => {
    slug.value = slugify(title.value);
};

function slugify(input) {
    if (!input) return '';
    let slug = input.toLowerCase().trim();
    slug = slug.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    slug = slug.replace(/[đĐ]/g, 'd');
    slug = slug.replace(/[^a-z0-9\s-]/g, '');
    slug = slug.replace(/[\s-]+/g, '-');
    slug = slug.replace(/^-+|-+$/g, '');
    return slug;
}

// fetch initial fields
const bgbase_class = document.getElementById("id_bgbase_class");
const multiclass = document.getElementById("id_multiclass");
const multiclass_one = document.getElementById("div_id_multiclass_one");
const multiclass_two = document.getElementById("div_id_multiclass_two");

// fetch subclass fields
const barbarian_subclass = document.getElementById("div_id_barbarian_subclass");
const bard_subclass = document.getElementById("div_id_bard_subclass");
const cleric_domain = document.getElementById("div_id_cleric_domain");
const druid_subclass = document.getElementById("div_id_druid_subclass");
const fighter_subclass = document.getElementById("div_id_fighter_subclass");
const monk_subclass = document.getElementById("div_id_monk_subclass");
const paladin_oath = document.getElementById("div_id_paladin_oath");
const ranger_subclass = document.getElementById("div_id_ranger_subclass");
const rogue_subclass = document.getElementById("div_id_rogue_subclass");
const sorcerer_subclass = document.getElementById("div_id_sorcerer_subclass");
const warlock_subclass = document.getElementById("div_id_warlock_subclass");
const wizard_school = document.getElementById("div_id_wizard_school");

// hide fields on DOM load
multiclass_one.style.display = ("none");
multiclass_two.style.display = ("none");

barbarian_subclass.style.display = ("none");
bard_subclass.style.display = ("none");
cleric_domain.style.display = ("none");
druid_subclass.style.display = ("none");
fighter_subclass.style.display = ("none");
monk_subclass.style.display = ("none");
paladin_oath.style.display = ("none");
ranger_subclass.style.display = ("none");
rogue_subclass.style.display = ("none");
sorcerer_subclass.style.display = ("none");
warlock_subclass.style.display = ("none");
wizard_school.style.display = ("none");

// event listener for dynamic class selection
bgbase_class.addEventListener("click", function() {
    if (bgbase_class.value === 'barbarian'){
        barbarian_subclass.style.display = ("block");
    } else {
        barbarian_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'bard'){
        bard_subclass.style.display = ("block");
    } else {
        bard_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'cleric'){
        cleric_domain.style.display = ("block");
    } else {
        cleric_domain.style.display = ("none");
    }
    if (bgbase_class.value === 'druid'){
        druid_subclass.style.display = ("block");
    } else {
        druid_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'fighter'){
        fighter_subclass.style.display = ("block");
    } else {
        fighter_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'monk'){
        monk_subclass.style.display = ("block");
    } else {
        monk_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'paladin'){
        paladin_oath.style.display = ("block");
    } else {
        paladin_oath.style.display = ("none");
    }
    if (bgbase_class.value === 'ranger'){
        ranger_subclass.style.display = ("block");
    } else {
        ranger_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'rogue'){
        rogue_subclass.style.display = ("block");
    } else {
        rogue_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'sorcerer'){
        sorcerer_subclass.style.display = ("block");
    } else {
        sorcerer_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'warlock'){
        warlock_subclass.style.display = ("block");
    } else {
        warlock_subclass.style.display = ("none");
    }
    if (bgbase_class.value === 'wizard'){
        wizard_school.style.display = ("block");
    } else {
        wizard_school.style.display = ("none");
    }
});

multiclass.addEventListener("click", function(){
    if (multiclass.value === 'yes'){
        multiclass_one.style.display = ("block");
    } else {
        multiclass_one.style.display = ("none");
    }
});