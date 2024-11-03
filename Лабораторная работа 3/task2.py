def find_common_participants(str1, str2, divider=','):
    participants_list1 = str1.split(divider)
    participants_list2 = str2.split(divider)

    common_participants = list(set(participants_list1).intersection(participants_list2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(participants)
