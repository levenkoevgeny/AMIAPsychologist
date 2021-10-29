from django.forms import ModelForm
from .models import Adaptation, Tension
from django import forms


POSITIONS = [
    ('1', 'курсант'),
    ('2', 'командир отделения'),
    ('3', 'командир группы'),
    ('4', 'старшина курса')
]

ANSWERS_GROUP_1 = [
    ('1', 'очень плохое'),
    ('2', 'плохое'),
    ('3', 'удовлетворительное'),
    ('4', 'хорошее'),
    ('5', 'отличное'),
]

ANSWERS_GROUP_1_1 = [
    ('1', 'очень плохой'),
    ('2', 'плохой'),
    ('3', 'удовлетворительный'),
    ('4', 'хороший'),
    ('5', 'отличный'),
]

ANSWERS_GROUP_2 = [
    ('1', 'постоянно'),
    ('2', 'часто'),
    ('3', 'редко'),
    ('4', 'очень редко'),
    ('5', 'никогда'),
]

ANSWERS_GROUP_3 = [
    ('1', 'полностью согласен'),
    ('2', 'согласен'),
    ('3', 'сложно ответить'),
    ('4', 'не согласен'),
    ('5', 'полностью не согласен'),
]

ANSWERS_GROUP_4 = [
    ('1', 'сплю мало, часто не высыпаюсь'),
    ('2', 'с трудом засыпаю и просыпаюсь'),
    ('3', 'засыпаю с трудом, но легко просыпаюсь в установленное время'),
    ('4', 'быстро засыпаю, но просыпаюсь раньше положенного времени'),
    ('5', 'быстро засыпаю, и легко просыпаюсь в установленное режимом время'),
]

ANSWERS_GROUP_5 = [
    ('1', 'аппетит отсутствует, нет желания принимать пищу'),
    ('2', 'аппетит пониженный (съедаю меньше обычного, чувствую, что недоедаю)'),
    ('3', 'аппетит повышенный (съедаю больше обычного, чувствую, что переедаю)'),
    ('4', 'аппетит хороший, питаюсь как обычно'),
]

ANSWERS_GROUP_6 = [
    ('1', 'у нас каждый сам по себе'),
    ('2', 'коллектив состоит из небольших групп, в основном по интересам'),
    ('3', 'группа дружная и сплоченная'),
    ('4', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_7 = [
    ('1', 'Да'),
    ('0', 'Нет'),
]

ANSWERS_GROUP_8 = [
    ('1', 'с курсантами своей учебной группы, проживающими с вами в одном спальном помещении'),
    ('2', 'с курсантами своей учебной группы, не проживающими с вами в одном спальном помещении'),
    ('3', 'с курсантами другой учебной группы'),
    ('4', 'с младшими командирами'),
    ('5', 'с офицерами'),
    ('6', 'преподавателями'),
]

ANSWERS_GROUP_9 = [
    ('1', 'неблагоприятный'),
    ('2', 'средний'),
    ('3', 'благоприятный'),
]

ANSWERS_GROUP_10 = [
    ('1', 'нет'),
    ('2', 'скорее нет'),
    ('3', 'скорее да'),
    ('4', 'да'),
    ('5', 'не знаю'),
]

ANSWERS_GROUP_11 = [
    ('1', 'Да'),
    ('0', 'Нет'),
    ('2', 'Затрудняюсь ответить'),
]

ANSWERS_GROUP_12 = [
    ('1', 'не чувствую, что являюсь членом группы'),
    ('2', 'чувствую себя частью группы'),
    ('3', 'не знаю'),
]

ANSWERS_GROUP_13 = [
    ('1', 'в улучшении не нуждается'),
    ('2', 'хотелось бы некоторого улучшения'),
    ('3', 'нуждается в коренном улучшении'),
    ('4', 'любые перемены бессмысленны'),
    ('5', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_14 = [
    ('1', 'непомерно высокая'),
    ('2', 'высокая, но выполнимая'),
    ('3', 'умеренная'),
    ('4', 'низкая'),
    ('5', 'очень низкая'),
    ('6', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_15 = [
    ('1', 'полностью не удовлетворен'),
    ('2', 'скорее нет'),
    ('3', 'и да и нет'),
    ('4', 'скорее да'),
    ('5', 'полностью удовлетворен'),
]

ANSWERS_GROUP_16 = [
    ('1', 'нет'),
    ('2', 'скорее нет'),
    ('3', 'скорее да'),
    ('4', 'да'),
    ('5', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_17 = [
    ('1', 'Да'),
    ('0', 'Нет'),
    ('2', 'Не знаю'),
]

ANSWERS_GROUP_18 = [
    ('1', 'полностью не оправдались'),
    ('2', 'скорее нет'),
    ('3', 'наполовину'),
    ('4', 'скорее да'),
    ('5', 'полностью оправдались'),
]

ANSWERS_GROUP_19 = [
    ('1', 'ничего не ожидал от обучения'),
    ('2', 'рассчитывал, что будет лучше'),
    ('3', 'думал, что будет хуже'),
    ('4', 'оправдались полностью'),
    ('5', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_20 = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]

ANSWERS_GROUP_21 = [
    ('1', 'всегда'),
    ('2', 'часто'),
    ('3', 'никогда'),
    ('4', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_22 = [
    ('1', 'твердо решил отчислиться из Академии МВД'),
    ('2', 'убежден в том, что не хочу продолжать обучение'),
    ('3', 'задумывался об отчислении из Академии МВД, но конкретных шагов пока не предпринимаю'),
    ('4', 'намерен продолжать обучение'),
    ('5', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_23 = [
    ('1', 'медленно'),
    ('2', 'обычно'),
    ('3', 'быстро'),
    ('4', 'затрудняюсь ответить'),
]

ANSWERS_GROUP_24 = [
    ('1', 'с плохим'),
    ('2', 'чаще с плохим'),
    ('3', 'с обычным (нейтральным)'),
    ('4', 'чаще с хорошим'),
    ('5', 'с хорошим'),
]

ANSWERS_GROUP_25 = [
    ('1', 'погружаюсь в свои мысли, пытаюсь разобраться в себе и сохранить внутренний баланс'),
    ('2', 'стараюсь приспособиться к трудностям, возможно, спокойно перенес эти требования (вплоть до привыкания), пробую что-то изменить в себе'),
    ('3', 'становлюсь более активным, стараюсь устранить препятствия, решить проблему сразу, обращаюсь за помощь к окружающим либо пытаюсь найти иной вариант решения'),
]

ANSWERS_GROUP_26 = [
    ('1', 'чувствую себя не на своем месте, испытываю дискомфорт, если бы не ряд обстоятельств, то уже бы отчислился'),
    ('2', 'пока не могу здесь полностью освоиться, мне еще необходимо время чтобы привыкнуть к условиям и требованиям'),
    ('3', 'привык к требованиям, но еще привыкаю к условиям'),
    ('4', 'к условиям привык, но еще привыкаю к требованиям'),
    ('5', 'привык к условиям и требованиям'),
]

ANSWERS_GROUP_27 = [
    ('1', 'без интереса'),
    ('2', 'настороженно'),
    ('3', 'спокойно'),
    ('4', 'с интересом'),
]

ANSWERS_GROUP_28 = [
    ('1', 'в беседе не нуждаюсь. Я проинформирован, что при необходимости могу обратиться к психологу, работающему на факультете'),
    ('2', 'хотелось бы побеседовать (укажите, что конкретно вы хотите обсудить)'),
]


class AdaptationForm(ModelForm):

    class Meta:
        model = Adaptation
        fields = '__all__'

        widgets = {
            'position': forms.Select(choices=POSITIONS),
            'physical_well_being': forms.RadioSelect(choices=ANSWERS_GROUP_1, attrs={'class': 'form-check-input'}),
            'hard_to_concentrate': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'remember_information': forms.RadioSelect(choices=ANSWERS_GROUP_3, attrs={'class': 'form-check-input'}),
            'more_hard_to_concentrate': forms.RadioSelect(choices=ANSWERS_GROUP_3, attrs={'class': 'form-check-input'}),
            'sleep': forms.RadioSelect(choices=ANSWERS_GROUP_1_1, attrs={'class': 'form-check-input'}),
            'sleep_last_time': forms.RadioSelect(choices=ANSWERS_GROUP_4, attrs={'class': 'form-check-input'}),
            'sleep_morning': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'sleep_in_daytime': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'headache': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'appetite_as_a_rule': forms.RadioSelect(choices=ANSWERS_GROUP_5, attrs={'class': 'form-check-input'}),
            'fast_fatiguability': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'tell_about_the_study_group': forms.RadioSelect(choices=ANSWERS_GROUP_6, attrs={'class': 'form-check-input'}),
            'conflicts_in_group': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input '}),
            'significant_unresolved_issues': forms.RadioSelect(choices=ANSWERS_GROUP_7, attrs={'class': 'form-check-input'}),
            'go_through_a_conflict': forms.RadioSelect(choices=ANSWERS_GROUP_8, attrs={'class': 'form-check-input '}),
            'climate_in_group': forms.RadioSelect(choices=ANSWERS_GROUP_9, attrs={'class': 'form-check-input '}),
            'satisfied_with_the_relationship': forms.RadioSelect(choices=ANSWERS_GROUP_10, attrs={'class': 'form-check-input'}),
            'team_cohesion': forms.RadioSelect(choices=ANSWERS_GROUP_10, attrs={'class': 'form-check-input '}),
            'impression_of_not_understanding': forms.RadioSelect(choices=ANSWERS_GROUP_3, attrs={'class': 'form-check-input'}),
            'opinion_does_not_match': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'others_do_not_fair': forms.RadioSelect(choices=ANSWERS_GROUP_3, attrs={'class': 'form-check-input'}),
            'strained_relationship': forms.RadioSelect(choices=ANSWERS_GROUP_11, attrs={'class': 'form-check-input'}),
            'group_membership': forms.RadioSelect(choices=ANSWERS_GROUP_12, attrs={'class': 'form-check-input'}),
            'safe_trust_no_one': forms.RadioSelect(choices=ANSWERS_GROUP_3, attrs={'class': 'form-check-input'}),
            'attitude_needs_improvement': forms.RadioSelect(choices=ANSWERS_GROUP_13, attrs={'class': 'form-check-input'}),
            'learning_difficulties': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'assimilation_of_material': forms.RadioSelect(choices=ANSWERS_GROUP_3, attrs={'class': 'form-check-input'}),
            'study_load_satisfaction': forms.RadioSelect(choices=ANSWERS_GROUP_10, attrs={'class': 'form-check-input'}),
            'study_load_appraisal': forms.RadioSelect(choices=ANSWERS_GROUP_14, attrs={'class': 'form-check-input'}),
            'is_it_interesting_to_study': forms.RadioSelect(choices=ANSWERS_GROUP_16, attrs={'class': 'form-check-input'}),
            'satisfied_with_the_training': forms.RadioSelect(choices=ANSWERS_GROUP_15, attrs={'class': 'form-check-input'}),
            'satisfied_with_the_training_group': forms.RadioSelect(choices=ANSWERS_GROUP_16, attrs={'class': 'form-check-input'}),
            'would_advise': forms.RadioSelect(choices=ANSWERS_GROUP_17, attrs={'class': 'form-check-input'}),
            'were_the_expectations_met': forms.RadioSelect(choices=ANSWERS_GROUP_18, attrs={'class': 'form-check-input'}),
            'how_much_were_the_expectations_met': forms.RadioSelect(choices=ANSWERS_GROUP_19, attrs={'class': 'form-check-input'}),
            'first_opinion': forms.RadioSelect(choices=ANSWERS_GROUP_20, attrs={'class': 'form-check-input'}),
            'current_opinion': forms.RadioSelect(choices=ANSWERS_GROUP_20, attrs={'class': 'form-check-input'}),
            'thought_about_dismissal': forms.RadioSelect(choices=ANSWERS_GROUP_21, attrs={'class': 'form-check-input'}),
            'thoughts_about_not_interesting_life': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'thoughts_life_is_passing_by': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'there_are_plans_to_deduct': forms.RadioSelect(choices=ANSWERS_GROUP_22, attrs={'class': 'form-check-input'}),
            'time_passes_as_a_rule': forms.RadioSelect(choices=ANSWERS_GROUP_23, attrs={'class': 'form-check-input'}),
            'hysterics_or_nervous_breakdown': forms.RadioSelect(choices=ANSWERS_GROUP_7, attrs={'class': 'form-check-input'}),
            'recession_and_rise_in_mood': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'mood_in_the_classroom': forms.RadioSelect(choices=ANSWERS_GROUP_24, attrs={'class': 'form-check-input'}),
            'thoughts_of_separation': forms.RadioSelect(choices=ANSWERS_GROUP_2, attrs={'class': 'form-check-input'}),
            'learning_difficulties_how': forms.RadioSelect(choices=ANSWERS_GROUP_25, attrs={'class': 'form-check-input'}),
            'how_is_adaptation_going': forms.RadioSelect(choices=ANSWERS_GROUP_26, attrs={'class': 'form-check-input'}),
            'you_answered': forms.RadioSelect(choices=ANSWERS_GROUP_27, attrs={'class': 'form-check-input'}),
            'tension': forms.CheckboxSelectMultiple(choices=Tension.objects.all(), attrs={'class': 'form-check-input'}),
            'need_a_conversation': forms.RadioSelect(choices=ANSWERS_GROUP_28, attrs={'class': 'form-check-input conversation_theme'}),
        }




