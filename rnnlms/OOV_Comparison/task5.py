import sys

from augment_vocab import augment

language = str(sys.argv[1])
aug = str(sys.argv[2]) # yes or no

if aug == "yes":

	k_vals = [10,100,1000,10000,100000,1000000,10000000]

	for k in k_vals:

		print("OOV for {}, Subwords granularity 1, k {} = ".format(language,k), augment(language, "../Text_Gen/s1_{}/s1_{}.txt".format(language,k)))

		print("OOV for {}, Subwords granularity 2, k {} = ".format(language,k), augment(language, "../Text_Gen/s2_{}/s2_{}.txt".format(language,k)))

		print("OOV for {}, Subwords granularity 3, k {} = ".format(language,k), augment(language, "../Text_Gen/s3_{}/s3_{}.txt".format(language,k)))

		print("--------------------------------------------------------")

else:

	print("OOV for {} = ".format(language), augment(language, ""))


# Graph Plotting
from matplotlib import pyplot as plt

s1 = [augment(language, "")]
s2 = [augment(language, "")]
s3 = [augment(language, "")]

k_vals = [10,100,1000,10000,100000,1000000,10000000]

for k in k_vals:
	s1.append(augment(language, "../Text_Gen/s1_{}/s1_{}.txt".format(language,k)))
	s2.append(augment(language, "../Text_Gen/s2_{}/s2_{}.txt".format(language,k)))
	s3.append(augment(language, "../Text_Gen/s3_{}/s3_{}.txt".format(language,k)))


#-----------
f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.set_xlabel("k")
ax1.set_ylabel("OOV Rate")
ax1.set_title("OOV rates for subwords")

y_vals = s1
x_vals = [0] + k_vals
ax1.plot(x_vals,y_vals,"-..")

y_vals = s2
x_vals = [0] + k_vals
ax1.plot(x_vals,y_vals,"-..")

y_vals = s3
x_vals = [0] + k_vals
ax1.plot(x_vals,y_vals,"-..")

plt.legend(["s1","s2","s3"])

plt.show()

#-----------


#-----------
f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax1.set_xlabel("k")
ax1.set_ylabel("OOV Rate")
ax1.set_title("OOV rates for subwords")

y_vals = s1
x_vals = [0] + k_vals
ax1.loglog(x_vals,y_vals,"-..")

y_vals = s2
x_vals = [0] + k_vals
ax1.loglog(x_vals,y_vals,"-..")

y_vals = s3
x_vals = [0] + k_vals
ax1.loglog(x_vals,y_vals,"-..")

plt.legend(["s1","s2","s3"])

plt.show()

#-----------