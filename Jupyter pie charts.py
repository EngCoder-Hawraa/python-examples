import matplotlib.pyplot as pyplot

labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45,30,15,10]

explode = (.1,0,0,0)
pyplot.pie(sizes,explode=explode,labels=labels,
           autopct='%1.f%%', shadow=True,
           counterclock=False,startangle=45)
pyplot.show()