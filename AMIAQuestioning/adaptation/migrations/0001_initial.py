# Generated by Django 2.2.7 on 2021-02-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tension', models.CharField(max_length=255, verbose_name='Напряжение, неудовлетворенность, дискомфорт или сложность')),
            ],
            options={
                'verbose_name': 'Напряжение',
                'verbose_name_plural': 'Напряжения',
                'ordering': ('tension',),
            },
        ),
        migrations.CreateModel(
            name='Adaptation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('group', models.CharField(max_length=255, verbose_name='Группа')),
                ('position', models.IntegerField(verbose_name='Должность')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата заполнения')),
                ('physical_well_being', models.IntegerField(verbose_name='1. Свое физическое самочувствие оцениваю как')),
                ('hard_to_concentrate', models.IntegerField(verbose_name='2. Мне сложно сосредоточиться')),
                ('remember_information', models.IntegerField(verbose_name='3. Я хорошо запоминаю информацию')),
                ('more_hard_to_concentrate', models.IntegerField(verbose_name='4. Мне труднее сконцентрироваться, чет большинству курсантов, с которыми я вместе обучаюсь')),
                ('sleep', models.IntegerField(verbose_name='5. В последнее время, мой сон преимущественно...')),
                ('sleep_last_time', models.IntegerField(verbose_name='6. В последнее время, как правило, я...')),
                ('sleep_morning', models.IntegerField(verbose_name='7. По утрам чувствую, что выспался и отдохнул')),
                ('sleep_in_daytime', models.IntegerField(verbose_name='8. В дневное время суток чувствую сонливость')),
                ('headache', models.IntegerField(verbose_name='9. Из-за переживаний и волнений головная боль случается')),
                ('appetite_as_a_rule', models.IntegerField(verbose_name='10. Как правило у меня (апетит)')),
                ('fast_fatiguability', models.IntegerField(verbose_name='11. Отмечаете ли Вы у себя быструю утомляемость')),
                ('tell_about_the_study_group', models.IntegerField(verbose_name='12. Что Вы можете сказать о Вашей учебной группе')),
                ('conflicts_in_group', models.IntegerField(verbose_name='13. Как часто в Вашей учебной группе происходят межличностные конфликты?')),
                ('significant_unresolved_issues', models.IntegerField(verbose_name='14. На данный момент, есть ли у Вас значимые неразрешенные конфликты')),
                ('go_through_a_conflict', models.IntegerField(verbose_name='15. Какой из конфликтов, вы бы переживали дольше всего')),
                ('climate_in_group', models.IntegerField(verbose_name='16. Как Вы оцениваете психологический климам в Вашей группе')),
                ('satisfied_with_the_relationship', models.IntegerField(verbose_name='17. Удовлетворены ли Вы взаимоотношениями в коллективе')),
                ('team_cohesion', models.IntegerField(verbose_name='18. Удовлетворены ли Вы сплоченностью Вашего коллектива')),
                ('impression_of_not_understanding', models.IntegerField(verbose_name='19. У меня складывается впечатление, что в группе не понимают')),
                ('opinion_does_not_match', models.IntegerField(verbose_name='20. Мое мнение не совпадает с мнением одногруппников')),
                ('others_do_not_fair', models.IntegerField(verbose_name='21. Окружающие особенно часто поступают несправедливо')),
                ('strained_relationship', models.IntegerField(verbose_name='22. Есть ли в группе люди, с которыми у Вас натянутые отношения')),
                ('group_membership', models.IntegerField(verbose_name='23. Как бы вы оценили свою принадлежность к группе')),
                ('safe_trust_no_one', models.IntegerField(verbose_name='24. Самое безопасное для меня - никому не доверять')),
                ('attitude_needs_improvement', models.IntegerField(verbose_name='25. Отношение руководства нуждается в улучшении')),
                ('average_score', models.IntegerField(verbose_name='26. Средний балл по итогам первой сессии')),
                ('learning_difficulties', models.IntegerField(verbose_name='27. Возникают ли у Вас трудности в учебе')),
                ('assimilation_of_material', models.IntegerField(verbose_name='28. Усвоение мариала у меня медленнее')),
                ('study_load_satisfaction', models.IntegerField(verbose_name='29. Удовлетворены ли Вы нагрузками в учебе')),
                ('study_load_appraisal', models.IntegerField(verbose_name='30. Как бы Вы оценили свою учебную нагрузку')),
                ('is_it_interesting_to_study', models.IntegerField(verbose_name='31. Интересно ли Вам обучаться в Академии МВД')),
                ('satisfied_with_the_training', models.IntegerField(verbose_name='32. Удовлетворены ли Вы тем как проходит Ваше обучение')),
                ('satisfied_with_the_training_group', models.IntegerField(verbose_name='33. Как Вы думаете, большинство одногруппников довольны обучением больше, чем Вы')),
                ('would_advise', models.IntegerField(verbose_name='34. Посоветовали бы Вы своим знакомым поступать в Академию МВД')),
                ('were_the_expectations_met', models.IntegerField(verbose_name='35. Оправдались ли Ваши ожидания по поводу обучения в Академии МВД')),
                ('how_much_were_the_expectations_met', models.IntegerField(verbose_name='36. На сколько оправдались Ваши ожидания в отношении обучения в Академии МВД')),
                ('first_opinion', models.IntegerField(verbose_name='37. Ваше личное мнение об обучении в Академии МВД на момент КМБ')),
                ('current_opinion', models.IntegerField(verbose_name='38. Ваше личное мнение об обучении в Академии МВД на данный момент')),
                ('thought_about_dismissal', models.IntegerField(verbose_name='39. Задумывались ли Вы об уходе')),
                ('thoughts_about_not_interesting_life', models.IntegerField(verbose_name='40. Мысли - курсантская жизнь не кажется такой интересной')),
                ('thoughts_life_is_passing_by', models.IntegerField(verbose_name='41. Ощущаю, что жизнь проходит мимо меня')),
                ('there_are_plans_to_deduct', models.IntegerField(verbose_name='42. Есть ли у Вас планы отчислиться из Академии МВД')),
                ('time_passes_as_a_rule', models.IntegerField(verbose_name='43. Как правило, время в Академии МВД для меня протекает')),
                ('hysterics_or_nervous_breakdown', models.IntegerField(verbose_name='44. Бывали ли истерика или нервный срыв')),
                ('recession_and_rise_in_mood', models.IntegerField(verbose_name='45. Бывают ли у Вас без видимой причины спады и подъемы настроения')),
                ('mood_in_the_classroom', models.IntegerField(verbose_name='46. С каким настроением Вы обычно посещаете учебные занятия')),
                ('thoughts_of_separation', models.IntegerField(verbose_name='47. Беспокоят ли Вас мысли о разлуке с родными и близкими')),
                ('learning_difficulties_how', models.IntegerField(verbose_name='48. Как поступаете, когда сталкиваетесь с трудностями в процессе обучения')),
                ('how_is_adaptation_going', models.IntegerField(verbose_name='49. Как проходит Ваша адаптация к бытовым условиям')),
                ('you_answered', models.IntegerField(verbose_name='50. На предложенные вопосы Вы отвечали')),
                ('the_future_i_imagine', models.TextField(verbose_name='52.1 Свое будущее в Академии МВД я представляю')),
                ('i_know_it_is_stupid_but_afraid', models.TextField(verbose_name='52.2 Знаю, что глупо, но боюсь')),
                ('i_doubt_that', models.TextField(verbose_name='52.3 Сомневаюсь в том, что')),
                ('most_outrages_me', models.TextField(verbose_name='52.4 Больше всего меня возмущает')),
                ('idea_of_the_chosen_profession', models.TextField(verbose_name='52.5 Мое представление о выбранной профессии')),
                ('obeying_orders', models.TextField(verbose_name='52.6 Подчинение приказам для меня')),
                ('life_motto', models.TextField(verbose_name='52.7 Мой жизненный девиз звучит так')),
                ('if_everyone_is_against_me', models.TextField(verbose_name='52.8 Если все против меня, то')),
                ('ideas_and_assumptions', models.TextField(verbose_name='53. Ваши идеи и предположения по улучшению процесса')),
                ('need_a_conversation', models.IntegerField(verbose_name='54. Необходима ли Вам беседа с психологом')),
                ('need_a_conversation_theme', models.TextField(blank=True, null=True, verbose_name='54.1 Тема беседы с психологом')),
                ('tension', models.ManyToManyField(to='adaptation.Tension', verbose_name='51. Что вызывает у Вас наибольшее напряжение, неудовлетворенность')),
            ],
            options={
                'verbose_name': 'Адаптация',
                'verbose_name_plural': 'Адаптации',
                'ordering': ('fio',),
            },
        ),
    ]
