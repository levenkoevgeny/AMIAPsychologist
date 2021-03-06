# Generated by Django 2.2.7 on 2020-12-22 08:16

from django.db import migrations
from graduate.models import WhatInduceToQuit, WhatKeeps, HowDidTeachersInfluence, HowDidLeadersInfluence


def add_default_data(apps, schema_editor):
    what_induce_to_quit = ['Затрудняюсь ответить', 'Ничего',
                           'Снижение уровня денежного довольствия',
                           'Ухудшение социального пакета и социальных гарантий',
                           'Увеличение выслуги лет для выхода на пенсию',
                           'Негативное отношение родных и близких в связи со службой',
                           'Ухудшение престижа службы, положения (статуса) сотрудника в обществе',
                           'Коррумпированность вашего подразделения',
                           'Отсутствие карьерных перспектив продвижения по службе',
                           'Потеря интереса к должностным обязанностям',
                           'Изменение места жительства (переезд в другую страну)',
                           'Наличие достойной альтернативы службе',
                           'Чрезмерная нагрузка (большой объем работы)',
                           'Ненормированный график работы (регулярные переработки)',
                           'Конфликты с руководством',
                           'Плохой коллектив (конфликтные взаимоотношения)',
                           'Общение с определенными слоями населения (уголовники и др. асоциальные личности)',
                           'Регулярные стрессовые ситуации',
                           '«Палочная» система работы',
                           'Психологическое давление (травля, угрозы) со стороны лиц, негативно настроенных к исполнению вами профессиональных обязанностей',
                           'Внутренние убеждения (нравственные, моральные, этические, религиозные, политические и т.п.)',
                           'Иное (напишите)'
                           ]
    for w_i_q in what_induce_to_quit:
        new_w_i_q = WhatInduceToQuit(what_induce_to_quit=w_i_q)
        new_w_i_q.save()

    what_keeps = ['Ничего',
                  'Служить на благо закона, народа, отечества',
                  'Долг перед Родиной',
                  'Интерес к профессии (специфике службы)',
                  'Карьерные перспективы, продвижения по службе',
                  'Стабильность службы (уверенность в завтрашнем дне)',
                  'Уровень денежного довольствия и его своевременная выплата',
                  'Социальный пакет',
                  'Отсутствие (нет, не вижу) достойной альтернативы службе',
                  'Необходимость финансовой выплаты выставленной за обучение в случае нарушения условий контракта (увольнения)',
                  'Гордость моих родных и близких',
                  'Возможность обзавестись деловыми контактами',
                  'Желание помогать людям',
                  'Хочу стать квалифицированным специалистом (расширение и углубление профессиональной компетентности)',
                  'Положение (статус) среди окружения',
                  'Престижность профессии в обществе',
                  'Чувство личного вклада и значимости проделанной работы',
                  'Нравится, что деятельность часто связана с риском для здоровья и жизни',
                  'Ускоренный выход на пенсию и стремление заработать на высокую пенсию',
                  'Ощущение власти и собственной значимости',
                  'Внутренние убеждения и личные интересы-мотивы',
                  'Затрудняюсь ответить',
                  'Иное (напишите)'
                  ]
    for w_k in what_keeps:
        new_w_k = WhatKeeps(what_keeps=w_k)
        new_w_k.save()

    teachers_influence = [
        'В целом положительно',
        'в целом отрицательно',
        'Никак',
        'Затрудняюсь ответить',
    ]
    for t_i in teachers_influence:
        new_t_i = HowDidTeachersInfluence(how_did_teachers_influence=t_i)
        new_t_i.save()

    leaders_influence = [
        'В целом положительно',
        'В целом отрицательно',
        'Никак',
        'Затрудняюсь ответить',
    ]
    for l_i in leaders_influence:
        new_l_i = HowDidLeadersInfluence(how_did_leaders_influence=l_i)
        new_l_i.save()

class Migration(migrations.Migration):

    dependencies = [
        ('graduate', '0003_auto_20201222_1115'),
    ]

    operations = [
        migrations.RunPython(add_default_data),
    ]
