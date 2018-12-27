import unicodecsv
from datetime import datetime as dt
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns

def parse_date(date):
    if date =='':
        return None
    else:
        return dt.strptime(date,'%Y-%m-%d')

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

def remove_udacity_accounts(data):
    udacity_test_accounts = set()
    for enrollment in enrollments:
        if enrollment['is_udacity']:
            udacity_test_accounts.add(enrollment['account_key'])

    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days >= 0

def remove_free_trial_cancels(data, paid_students):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

def group_data(data,key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

def sum_grouped_items(grouped_data, field_name ):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key]=total
    return summed_data

def describe_data(data, plot_title, x_label, y_label):
    total = list(data.values())
    print('Mean:{:.2f}'.format(np.mean(total)))
    print('Standard Deviation:{:.2f}'.format(np.std(total)))
    print('Minimum:{:.2f}'.format(np.min(total)))
    print('Maximum:{:.2f}'.format(np.max(total)))
    plt.hist(total, bins=20)
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

unique_enrolled_students = get_unique_students(enrollments)

for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity']  == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] =  int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

unique_engagement_students = get_unique_students(daily_engagement)

unique_project_submitters = get_unique_students(project_submissions)

num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students\
            and enrollment['join_date'] != enrollment['cancel_date']:
        num_problem_students += 1

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

paid_students = {}
for enrollment in non_udacity_enrollments:
    if not enrollment['is_canceled']  or enrollment['days_to_cancel']>7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments, paid_students)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement, paid_students)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions, paid_students)

paid_students_engagements_in_first_week = []
for engagement_record in paid_engagement:
    # add field_name 'has_visited'
    if engagement_record['num_courses_visited'] > 0:
        engagement_record['has_visited'] = 1
    else:
        engagement_record['has_visited'] = 0

    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']
    if within_one_week(join_date, engagement_record_date):
            paid_students_engagements_in_first_week.append(engagement_record)

engagement_by_account = group_data(paid_students_engagements_in_first_week,'account_key')


total_minutes_by_account = sum_grouped_items(engagement_by_account, 'total_minutes_visited')
describe_data(total_minutes_by_account,'total minutes','contas','minutos')

total_completed_lessons_by_account = sum_grouped_items(engagement_by_account, 'lessons_completed')
describe_data(total_completed_lessons_by_account,'qtde lições completas','contas','lições')

#Verify the student with max minutes
student_with_max_minutes = None
max_minutes = 0
for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student

for engagement_record in paid_students_engagements_in_first_week:
    if engagement_record['account_key'] == student_with_max_minutes:
        foo = 1 #just to have some code here
#        print(engagement_record)

days_visited_by_account = sum_grouped_items(engagement_by_account, 'has_visited')
describe_data(days_visited_by_account,'qtde visitas','dias','visitas')


###################################################
#                      11                         #
###################################################
subway_project_lessons_keys = ['746169184', '3176718735']

pass_subway_project = set()
for submissions in paid_submissions:
    project = submissions['lesson_key']
    rating = submissions['assigned_rating']

    if project in subway_project_lessons_keys and \
            (rating =='PASSED' or rating == 'DISTINCTION'):
        pass_subway_project.add(submissions['account_key'])

print(len(pass_subway_project))

passing_engagement = []
non_passing_engagement = []

for engagement_record in paid_students_engagements_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print(len(passing_engagement))
print(len(non_passing_engagement))

passing_engagement_by_account = group_data(passing_engagement, 'account_key')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')

print('Non-passing minutes:')
non_passing_minutes = sum_grouped_items(non_passing_engagement_by_account, 'total_minutes_visited')
describe_data(non_passing_minutes,'total minutes dos que não passaram','contas','minutos')

print('Passing minutes:')
passing_minutes = sum_grouped_items(passing_engagement_by_account, 'total_minutes_visited')
describe_data(passing_minutes,'total minutes dos que passaram','contas','minutos')

print('Non-passing lessons:')
non_passing_lessons = sum_grouped_items(non_passing_engagement_by_account,'lessons_completed')
describe_data(non_passing_lessons,'qtde de lições dos que não passaram','contas','lições')

print('Passing lessons:')
passing_lessons = sum_grouped_items(passing_engagement_by_account,'lessons_completed')
describe_data(passing_lessons,'qtde de lições dos que passaram','contas','lições')

print('Non-passing visits:')
non_passing_visits = sum_grouped_items(non_passing_engagement_by_account,'has_visited')
describe_data(non_passing_visits,'qtde de visitas do que não passaram','dias','visitas')

print('Passing visits:')
passing_visits = sum_grouped_items(passing_engagement_by_account,'has_visited')
describe_data(passing_visits,'qtde de visitas do que passaram','dias','visitas')



