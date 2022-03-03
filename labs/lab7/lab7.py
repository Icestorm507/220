"""
Dylan Benton Embrey
3/2/2022
Lab 7.py
Computer Programming Labs 7: Input and Output
Problem: This code will help show averages and compare them.
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    weighted_averages_list = []
    for line in in_file:
        all_values = line.split(":")
        name = all_values[0]
        numbers = all_values[1].strip()
        weights = []
        grades = []
        for i in range(1, len(weights), 2):
            num_weight = int(weights[i])
            weights.append(num_weight)
        for i in range(0, len(grades), 2):
            num_grade = int(grades[i])
            grades.append(num_grade)
        for i in range(len(all_values)):
            weighted_average = ((weights[i]) * (grades[i])) + weighted_average
            final_weight_average = weighted_average / 100
            weighted_averages_list.append(final_weight_average)
            print(all_values[0] + ' ' + all_values[1] + "'s average: {0:.1f}".format(final_weight_average))
        total_average_weighted = (sum(weighted_averages_list) / len(weighted_averages_list))
        print("\nClass Average: ", total_average_weighted)
    in_file.close()
    out_file.close()


weighted_average("grades.txt", "avg.txt")
