import pymysql
import plotly
import plotly.plotly as py # You have to install plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt # you must have matplotlib installed

grade_ranges = {} # python empty dictionary , stores key:value pair
grade =[] # python list

# initialzing the dictionary for 4 classes of salary ranges, salary ranges stored
# as string which is key intial number of instructors in the salary range is 0 are key
grade_ranges["A"]=0;
grade_ranges["A-"]=0;
grade_ranges["B+"]=0;
grade_ranges["B"]=0;
grade_ranges["B-"]=0;
grade_ranges["C+"]=0;
grade_ranges["C"]=0;
grade_ranges["C-"]=0;
grade_ranges["D+"]=0;
grade_ranges["D"]=0;
grade_ranges["D-"]=0;
grade_ranges["F"]=0;

def classify(val): # function takes salary value and increments value of the key/salary-range where the salary falls into
   if val=="A":
      grade_ranges["A"] +=1;
   elif val=="A-":
      grade_ranges["A-"] +=1;  
   elif val=="B+":
      grade_ranges["B+"] +=1;
   elif val=="B":
      grade_ranges["B"] += 1;
   elif val=="B-":
      grade_ranges["B-"] += 1;
   elif val=="C+":
      grade_ranges["C+"] += 1;
   elif val=="C":
      grade_ranges["C"] += 1;
   elif val=="C-":
      grade_ranges["C-"] += 1;
   elif val=="D+":
      grade_ranges["D+"] += 1;
   elif val=="D":
      grade_ranges["D"] += 1;
   elif val=="D-":
      grade_ranges["D-"] += 1;
   else:
      grade_ranges["F"] += 1;

db = pymysql.connect("localhost","root","","university" ) # connecting to the database using pymysql interface.
# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM takes"

#print "ID","Name","Dept_name","salary"
field_names = "ID, grade".split(","); # creating field headers for instructor table
for i in range(0, len(field_names)): # printing the headers
   print ('{0: <30}'.format("| " + field_names[i]),)
print ("|")


try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()



   num_col = len(results[0])
   for row in results:
      for col in range(0, num_col):
         print ("|",)
         print ('{0:<15}'.format(row[col]),)
         if col==5:
            classify(row[col]) # determining range of the salary
            grade.append(row[col]) # creating the list of all salary from the instructor table
      print ("|")


except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()

plt.figure()
plt.plot(grade) # plot the salary array as a line graph
#plt.show()# display the graph

plt.figure()
plt.pie(grade_ranges.values(), labels=grade_ranges.keys())
plt.show()


#For plotting pie chart, you have to create an account at https://plot.ly to see the plotings # please use your api key and username in the following line.
plotly.tools.set_credentials_file(username='mhossai2', api_key='i1xo7M5mtcDu9Rxj7keD')
# create a pie chart for different salary ranges. The values are the number of instructors counted for the salary ranges
trace = go.Pie(labels=grade_ranges.keys(), values=grade_ranges.values())
#py.plot([trace], filename='basic_pie_chart',auto_open=True) # to plot online in notebook use py.iplot instead of py.plot
#The above line gives you a link to the pie chart
