import csv
import pandas as pd
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go 
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#fig = ff.create_distplot([data], ["Math scores"], show_hist=False)
#fig.show()

mean = statistics.mean(data)
stddev = statistics.stdev(data)
print("mean of population: ", mean)
print("stddev of population: ", stddev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

sample_mean = statistics.mean(mean_list)
sample_stddev = statistics.stdev(mean_list)
print("mean of sample: ", sample_mean)
print("stddev of sample: ", sample_stddev)

first_stddev_start, first_stddev_end = mean-stddev, mean+stddev 
second_stddev_start, second_stddev_end = mean-(2*stddev), mean+(2*stddev)
third_stddev_start, third_stddev_end = mean-(3*stddev), mean+(3*stddev)

print("std1", first_stddev_start, first_stddev_end)
print("std2", second_stddev_start, second_stddev_end)
print("std3", third_stddev_start, third_stddev_end)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_stddev_start, first_stddev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stddev_start, second_stddev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stddev_start, third_stddev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x = [third_stddev_end, third_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
#fig.show()

# Finding the mean of first data1 and plotting it
df1 = pd.read_csv("data1.csv")
data1 = df1["Math_score"].tolist()

mean_of_sample1 = statistics.mean(data1)
print("mean of sample1: " ,mean_of_sample1)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample1, mean_of_sample1], y = [0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.show()

# Finding the mean of data2 and plotting it
df2 = pd.read_csv("data2.csv")
data2 = df2["Math_score"].tolist()

mean_of_sample2 = statistics.mean(data2)
print("mean of sample2: " ,mean_of_sample2)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample2, mean_of_sample2], y = [0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.show()

# Finding the mean of data3 and plotting it
df3 = pd.read_csv("data3.csv")
data3 = df3["Math_score"].tolist()

mean_of_sample3 = statistics.mean(data3)
print("mean of sample3: " ,mean_of_sample3)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample3, mean_of_sample3], y = [0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stddev_end, third_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

df6 = pd.read_csv("School_1_Sample.csv")
data6 = df6["Math_score"].tolist()

mean_of_sample6 = statistics.mean(data6)
print("mean of sample6: " ,mean_of_sample6)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample6, mean_of_sample6], y = [0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stddev_end, third_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

df4 = pd.read_csv("School_2_Sample.csv")
data4 = df4["Math_score"].tolist()

mean_of_sample4 = statistics.mean(data4)
print("mean of sample4: " ,mean_of_sample4)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample4, mean_of_sample4], y = [0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stddev_end, third_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

df5 = pd.read_csv("School_3_Sample.csv")
data5 = df5["Math_score"].tolist()

mean_of_sample5 = statistics.mean(data5)
print("mean of sample5: " ,mean_of_sample5)

fig = ff.create_distplot([mean_list], ["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample5, mean_of_sample5], y = [0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stddev_end, third_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

z_score1 = (mean_of_sample6 - mean)/stddev
z_score2 = (mean_of_sample4 - mean)/stddev
z_score3 = (mean_of_sample5 - mean)/stddev
print("z score of samp6: ", z_score1)
print("z score of samp4: ", z_score2)
print("z score of samp5: ", z_score3)