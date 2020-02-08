import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def issues_per_month(issue_numbers,name="plots/issues_per_month.png"):
    x = []
    for i in range(len(issue_numbers)):
        if issue_numbers[i] != 0:
            x.append(i+1)

    plt.figure(figsize=(10,4))
    issue_numbers = [i for i in issue_numbers if i!=0]
    sns.regplot(x, issue_numbers,lowess=True)
    plt.ylim(0,0.01)
    plt.xticks([i for i in range(0,len(issue_numbers),24)],[2012+i//12 for i in range(0,len(issue_numbers),24)],fontsize=20)
    plt.yticks(fontsize=20)
    plt.savefig(name)
    plt.clf()


def plot_each_year(issue_numbers,start_year):
    if len(issue_numbers)%12 != 0:
        print("Not a mod 12")
        return 0

    num_years = len(issue_numbers)//12

    for i in range(num_years):
        year = start_year+i
        plt.plot(list(range(12)),issue_numbers[i*12:(i+1)*12])
        plt.savefig("plots/{}_issue_numbers.png".format(year))
        plt.clf()

def plot_each_year_toxic(issue_numbers,start_year):
    if len(issue_numbers)%12 != 0:
        print("Not a mod 12")
        return 0

    num_years = len(issue_numbers)//12

    plt.clf()

    for i in range(num_years):
        year = start_year+i
        plt.plot(list(range(12)),issue_numbers[i*12:(i+1)*12])
        plt.savefig("plots/{}_issue_numbers_toxic.png".format(year))

def plot_roc(predicted,actual):
    import scikitplot as skplt
    import matplotlib.pyplot as plt

    y_true =  actual
    y_probas =  predicted # predicted probabilities generated by sklearn classifier
    skplt.metrics.plot_roc_curve(y_true, y_probas)
    plt.show()

def plot_box(plot_1,plot_2):
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot([plot_1,plot_2])

    # Save the figure
    fig.savefig('plots/box_plot.png', bbox_inches='tight')

def plot_box_multiple(box,name):
    fig = plt.figure(1, figsize=(9, 6))
    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(box,showfliers=False)
    plt.xticks(list(range(1,len(name)+1)),name)
    # Save the figure
    fig.savefig('plots/box_plot.png', bbox_inches='tight')

def plot_languages():
    numbers = []
    plt.figure(figsize=(12,4))
    lang_list = ["Haskell","R","Ruby","Python","Java","Javascript","Lua"]
    num_tot = 0
    for lang in lang_list:
        project_toxic = {}
        project_total = {}
        f = open(lang.lower()+"_results.txt").read().split("\n")
        for line in f:
            if " 0" in line or " 1" in line:
                s = line.split(" ")
                project = "/".join(s[0].split("/")[:-1])

                num = int(s[1])

                if project not in project_toxic:
                    project_toxic[project] = 0
                    project_total[project] = 0

                project_total[project]+=1
                project_toxic[project]+=num
                num_tot+=1
        distro = []
        for project in project_total:
            distro.append(project_toxic[project]/project_total[project])

        numbers.append(distro)

    zipped_version = list(zip(numbers,lang_list))
    zipped_version = sorted(zipped_version,key=lambda x: np.median(x[0]))

    numbers = [x[0] for x in zipped_version]
    lang_list = [x[1] for x in zipped_version]


    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(numbers,vert=False,showfliers=False)

    ax.set_yticklabels(lang_list)
    plt.xticks([0,0.005,0.01,0.015,0.02],fontsize=24)
    plt.yticks(fontsize=24)

    # Save the figure
    fig.savefig('plots/langs.png', bbox_inches='tight')
    print(num_tot)

def plot_corporate():
    plt.figure(figsize=(12,4))
    numbers = []
    lang_list = ["Corporate","Uncorporate"]
    num_tot = 0
    for lang in lang_list:
        project_toxic = {}
        project_total = {}
        f = open(lang.lower()+"_results.txt").read().split("\n")
        for line in f:
            if " 0" in line or " 1" in line:
                s = line.split(" ")
                project = "/".join(s[0].split("/")[:-1])

                num = int(s[1])

                if project not in project_toxic:
                    project_toxic[project] = 0
                    project_total[project] = 0

                project_total[project]+=1
                project_toxic[project]+=num
                num_tot+=1
        distro = []
        for project in project_total:
            distro.append(project_toxic[project]/project_total[project])

        numbers.append(distro)

    print("{}".format(num_tot))

    zipped_version = list(zip(numbers,lang_list))
    zipped_version = sorted(zipped_version,key=lambda x: np.median(x[0]))

    numbers = [x[0] for x in zipped_version]
    lang_list = [x[1] for x in zipped_version]


    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(numbers,vert=False,showfliers=False)

    lang_list = [i.replace("Uncorporate","Non Corporate") for i in lang_list]

    ax.set_yticklabels(lang_list)
    plt.yticks(fontsize=28)
    plt.xticks(fontsize=28)

    # Save the figure
    fig.savefig('plots/corporate.png', bbox_inches='tight')

def plot_years():
    dates = ['2012_01_09', '2012_02_13', '2012_03_12', '2012_04_09', '2012_05_14', '2012_06_11', '2012_07_09', '2012_08_13', '2012_09_10', '2012_10_08', '2012_11_12', '2012_12_10', '2013_01_14', '2013_02_11', '2013_03_11', '2013_04_08', '2013_05_13', '2013_06_10', '2013_07_08', '2013_08_12', '2013_09_09', '2013_10_14', '2013_11_11', '2013_12_09', '2014_01_13', '2014_02_10', '2014_03_10', '2014_04_14', '2014_05_12', '2014_06_09', '2014_07_14', '2014_08_11', '2014_09_08', '2014_10_13', '2014_11_10', '2014_12_08', '2015_01_12', '2015_02_09', '2015_03_09', '2015_04_13', '2015_05_11', '2015_06_08', '2015_07_13', '2015_08_10', '2015_09_14', '2015_10_12', '2015_11_09', '2015_12_14', '2016_01_11', '2016_02_08', '2016_03_14', '2016_04_11', '2016_05_09', '2016_06_13', '2016_07_11', '2016_08_08', '2016_09_12', '2016_10_10', '2016_11_14', '2016_12_12', '2017_01_09', '2017_02_13', '2017_03_13', '2017_04_10', '2017_05_08', '2017_06_12', '2017_07_10', '2017_08_14', '2017_09_11', '2017_10_09', '2017_11_13', '2017_12_11', '2018_01_08', '2018_02_12', '2018_03_12', '2018_04_09', '2018_05_14', '2018_06_11', '2018_07_09', '2018_08_13', '2018_09_10', '2018_10_08', '2018_11_12', '2018_12_10']
    nums = []
    total_total = 0
    for i in dates:
        i = i.replace("_","-")
        i+="_results.txt"
        f = open(i).read().split("\n")

        numTotal = 0
        numToxic = 0
        for i in f:
            if " 0" in i or " 1" in i:
                numTotal+=1
                if " 1" in i:
                    numToxic+=1
        nums.append(numToxic/numTotal)
        total_total+=numTotal
    print("There are {}".format(total_total))
    issues_per_month(nums,"plots/year.png")

def plot_removing(scores):
    scores = sorted(scores,key=lambda x: x[1],reverse=True)
    names = list([i[0] for i in scores])
    y_pos = np.arange(len(names))
    fig = plt.figure(1, figsize=(13, 4))
    ax = fig.add_subplot(111)
    ax.barh(y_pos,list([i[1] for i in scores]))
    ax.invert_yaxis()
    ax.set_xlabel("F-0.5 score")
    ax.set_title("Removing Features")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names,fontsize=18)
    plt.savefig("plots/removing.png")

def plot_adding(scores):
    scores = sorted(scores,key=lambda x: x[1])
    names = list([i[0] for i in scores])
    y_pos = np.arange(len(names))
    fig = plt.figure(1, figsize=(13, 4))
    ax = fig.add_subplot(111)
    ax.barh(y_pos,list([i[1] for i in scores]))
    ax.invert_yaxis()
    ax.set_xlabel("F-0.5 score")
    ax.set_title("Adding Features")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(names,fontsize=18)
    plt.savefig("plots/adding.png")


def bar_graph(bars,names):
    x = np.arange(len(bars))
    plt.bar(x, bars)
    plt.xticks(x, names)
    plt.savefig('plots/bar_{}.png'.format("_".join(names)))

#plot_years()
#plot_corporate()
#plot_languages()
#plot_adding([('anger',0.79),('negative',0.817),('vader',0.8098),('length',0),('polarity',0.799),('subjectivity',0.821),('tf_idf',0.757),('word2vec',0.783),('baseline',0.8333)])
plot_removing([('w/o perspective',0.375),('w/o filters',0.769),('w/o polite',0.783),('baseline',0.833)])