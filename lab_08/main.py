import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked


def change_bool_survived_for_string(passengers: pd.DataFrame):
    passengers["Survived"] = np.where(passengers["Survived"] == 1, "Alive", "Dead")


def death_alive_for_every_sex_and_pclass(passengers: pd.DataFrame):
    data_class_sex_alive = passengers[["Pclass", "Survived", "Sex"]].copy()
    change_bool_survived_for_string(data_class_sex_alive)
    return_data = data_class_sex_alive.value_counts().to_frame("SurvivalsCount")
    return_data = return_data.sort_values(by=["Pclass", "Survived", "Sex"], ascending=[False, True, True])
    return return_data


def stat_for_number_fields_for_every_sex(passengers: pd.DataFrame):
    data_sex_class_age_ticket_fare = passengers[["Sex", "Pclass", "Age", "Ticket", "Fare"]].copy()
    return data_sex_class_age_ticket_fare.value_counts()


def fill_with_rate_of_survivability_by_port(inner_passengers: pd.DataFrame):
    rate_of_live = []
    passengers_count_by_port = inner_passengers["Embarked"].value_counts()
    stat_passengers = inner_passengers.value_counts()
    for i in range(len(stat_passengers)):
        if (stat_passengers.index[i])[0] == "S":
            rate_of_live.append(stat_passengers[i] / passengers_count_by_port["S"])
        if (stat_passengers.index[i])[0] == "C":
            rate_of_live.append(stat_passengers[i] / passengers_count_by_port["C"])
        if (stat_passengers.index[i])[0] == "Q":
            rate_of_live.append(stat_passengers[i] / passengers_count_by_port["Q"])
    return rate_of_live


def fill_with_rate_of_survivability_by_pclass(inner_passengers: pd.DataFrame):
    rate_of_live = []
    passengers_count_by_pclass = inner_passengers["Pclass"].value_counts()
    stat_passengers = inner_passengers.value_counts()
    for i in range(len(stat_passengers)):
        if (stat_passengers.index[i])[0] == 3:
            rate_of_live.append(stat_passengers.iloc[i] / passengers_count_by_pclass[3])
        if (stat_passengers.index[i])[0] == 2:
            rate_of_live.append(stat_passengers.iloc[i] / passengers_count_by_pclass[2])
        if (stat_passengers.index[i])[0] == 1:
            rate_of_live.append(stat_passengers.iloc[i] / passengers_count_by_pclass[1])
    return rate_of_live


def port_influence_for_alive(passengers: pd.DataFrame):
    data_port_alive = passengers[["Embarked", "Survived"]].copy()
    change_bool_survived_for_string(data_port_alive)

    rate_of_live = fill_with_rate_of_survivability_by_port(data_port_alive)
    return_data = data_port_alive.value_counts().to_frame("CountOfSurvival")
    return_data["RateOfSurvival"] = rate_of_live

    return_data = return_data.sort_values(["Embarked", "Survived"])

    return return_data


def find_top_ten_popular_surnames(passengers: pd.DataFrame):
    full_name_data = passengers["Name"].copy()
    full_name_data["Surname"] = full_name_data.str.split(",").str.get(0)
    return full_name_data["Surname"].value_counts().head(10)


def find_top_ten_popular_names(passengers: pd.DataFrame):
    full_name_data = passengers["Name"].copy()
    full_name_data["Surname"] = full_name_data.str.split(",").str.get(1)
    full_name_data["Surname"] = (full_name_data["Surname"]
                                 .str.removeprefix(" Mr. ")
                                 .str.removeprefix(" Miss. ")
                                 .str.removeprefix(" Mrs. ")
                                 .str.removeprefix(" Master. "))
    return full_name_data["Surname"].value_counts().head(10)


def fill_missing_values_by_avg(passengers: pd.DataFrame):
    passengers_data = passengers.copy()
    passengers_data["Fare"] = passengers_data["Fare"].fillna(passengers_data["Fare"].mean())
    passengers_data["Age"] = passengers_data["Age"].fillna(int(passengers_data["Age"].mean()))
    return passengers_data


def pclass_and_sex_influence_for_alive(passengers: pd.DataFrame):
    data_pclass_alive = passengers[["Pclass", "Sex", "Survived", "Age"]].copy()
    passengers_count = passengers.count().iloc[0]
    change_bool_survived_for_string(data_pclass_alive)
    return_data = data_pclass_alive.value_counts().to_frame("CountOfSurvival")
    return_data["RateOfSurvival"] = return_data["CountOfSurvival"]/passengers_count

    return_data = return_data.reset_index()

    return_data = return_data.drop(return_data[return_data['Survived'] == "Dead"].index)

    return_data = return_data.sort_values(["Survived", "CountOfSurvival"], ascending=[True, False])
    return return_data


def try_to_calculate_probability(passengers: pd.DataFrame, stats: pd.DataFrame):
    data_class_try = passengers.copy()
    stats = stats.reset_index()
    stats_data = stats[["Pclass", "Sex", "Age", "RateOfSurvival"]]

    result = pd.merge(data_class_try, stats_data, how="left", on=["Pclass", "Sex", "Age"])
    result = result.fillna(result["RateOfSurvival"].mean())
    print(result)


def graph_for_age_survival(passengers: pd.DataFrame):
    passengers_data = passengers.copy()
    passengers_count = passengers.count().iloc[0]
    result_data = passengers_data[["Age", "Survived"]].value_counts().to_frame("CountOfSurvival").reset_index()
    new_result = result_data[result_data["Survived"] == 1][["Age", "CountOfSurvival"]]
    another_result = passengers_data["Age"].value_counts().to_frame("Count").reset_index()
    print(another_result)
    #new_result["PercentOfSurvival"] = (new_result["CountOfSurvival"] / passengers_count) * 100

    print(new_result)
    new_result = new_result.merge(another_result, on="Age")
    #new_result["PercentOfSurvival"] = (new_result["CountOfSurvival"] / passengers_count) * 100
    #new_result["PercentOfSurvival"] = (new_result["CountOfSurvival"] / result_data["CountOfSurvival"]) * 100
    new_result["PercentOfSurvival"] = new_result["CountOfSurvival"] / new_result["Count"]

    plt.bar(new_result['Age'], new_result['PercentOfSurvival'], align='center')
    plt.xlabel("Age")
    plt.ylabel("Count of alive")
    plt.show()


data = pd.read_csv('train.csv')
data2 = pd.read_csv('test.csv')

task_1_data = death_alive_for_every_sex_and_pclass(data)
task_2_data = stat_for_number_fields_for_every_sex(data)
task_3_data = port_influence_for_alive(data)
task_4_surnames_data = find_top_ten_popular_surnames(data)
task_4_names_data = find_top_ten_popular_names(data)
task_5_data = fill_missing_values_by_avg(data)

print("Task 1:")
print(task_1_data)

print("Task 2:")
print(task_2_data)

print("Task 3:")
print(task_3_data)

print("Task 4:")
print(task_4_surnames_data)
print(task_4_names_data)

print("Task 5:")
print(task_5_data)

print("Task 6:")
stats_data_sorted = pclass_and_sex_influence_for_alive(data)
try_to_calculate_probability(data2, stats_data_sorted)

print("Task 7:")
graph_for_age_survival(data)
