# Name:          Laila Zaidi                                                    
  2                                                       
  6                                                                                 
  7 def main():                                                                     
  8    fp = open("crimes.tsv", "r")                                                 
  9    header = fp.readline()                                                       
 10   # lines_num = sum(1 for line in fp)                                           
 11    lines = fp.readlines()                                                       
 12    fp.close()                                                                   
 13    time1 = open("times.tsv", "r")                                               
 14    header2 = time1.readline()                                                   
 15    times = time1.readlines()                                                    
 16    time1.close()                                                                
 17    file_w = open("robberies.tsv", "w")                                          
 18    crimes_created = create_crimes(lines)                                        
 19    crimes_sorted = sort_crimes(crimes_created)                                  
 20    file_w.write("ID\tCategory\tDayOfWeek\tMonth\tHour\n")                       
 21    crimes_updated = update_crimes(crimes_sorted, times)                         
 22    no_crimes = len(crimes_sorted)                                               
 23    #file_w.write("ID\tCategory\tDayOfWeek\tMonth\tHour\n") #\n                  
 24    for i in crimes_sorted:                                                      
 25                                                                                 
 26                                                                                 
 27        string = str(i)                                                          
 28        file_w.write(string)                                                     
 29                                                                                 
 30    file_w.close()                                                               
 31   # fp.close()                                                                  
 32    time1.close()                                                                
 33                                                                                 
 34                                                                                 
 35                                                                                 
 36    print("NUMBER OF PROCESSED ROBBERIES:", no_crimes)
    print("      DAY WITH MOST ROBBERIES:", get_day(crimes_updated))             
 38    print("    MONTH WITH MOST ROBBERIES:", get_month(crimes_updated))           
 39    print("     HOUR WITH MOST ROBBERIES:", get_hour(crimes_updated))            
 40                                                                                 
 41 #research file i/o and how to develop this in main, calling on functions later on
 42                                                                                 
 43                                                                                 
 44                                                                                 
 45                                                                                 
 46                                                                                 
 47 class Crime:                                                                    
 48     def __init__(self, crime_id, category):                                     
 49          self.crime_id = crime_id #crimes.tsv                                   
 50          self.category = category #crimes.tsv                                   
 51          self.day_of_week = None #times.tsv                                     
 52          self.month = None #times.tsv, full word                                
 53          self.hour = None #times.tsv, AM/PM format                              
 54                                                                                 
 55                                                                                 
 56                                                                                 
 57     def __eq__(self, other):                                                    
 58         if self.crime_id == other.crime_id:                                     
 59            return True                                                          
 60         return False                                                            
 61                                                                                 
 62                                                                                 
 63     def __repr__(self):                                                         
 64         return "{0}\t{1}\t{2}\t{3}\t{4}\n".format(self.crime_id,                
 65                    self.category, self.day_of_week, self.month, self.hour)      
                                                                                                                                            65,9          13%
    def set_time(self, day_of_week, month, hour):                               
 73         #day_of_week = string containing a day of the week                      
 74         #month = integer between 1 and 12                                       
 75         #hour = integer between 0 and 23                                        
 76         #no tests for this one                                                  
 77         self.day_of_week = day_of_week                                          
 78        # self.month = month                                                     
 79        # self.hour = hour                                                       
 80         months = ["January", "February", "March", "April", "May", "June", "July",
 81                  "August", "September", "October", "November", "December"]      
 82         month = str(month)                                                      
 83         month1 = month.split("/")                                               
 84         month2 = int(month1[0])                                                 
 85         month_name = months[month2 - 1]                                         
 86         month = month_name #how do i update stuff????                           
 87         self.month = month                                                      
 88         hours = ["1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", 
 89              "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM",         
 90              "6PM", "7PM", "8PM", "9PM", "10PM", "11PM", "12AM"]                
 91         hour = str(hour)                                                        
 92         hour1 = hour.split(":")                                                 
 93         the_hour = hour1[0]                                                     
 94         hour_int = int(the_hour) // 1                                           
 95         hour = hours[hour_int - 1]                                              
 96       #  print(day_of_week)                                                     
 97       #  print(month)                                                           
 98       #  print(hour)                                                            
 99         self.hour = hour                                                        
100 def create_crimes(lines):                                                       
118     #lines = list of strings, returns                                           
119                                                                                 
120                                                                                 
121    my_list = []                                                                 
122    for i in lines:                                                              
123      index = i.split("\t")                                                      
124      id_ = int(index[0])                                                        
125      crime_temp = Crime(id_, index[1])                                          
126      if index[1] == "ROBBERY" and crime_temp not in my_list:                    
127         my_list.append(crime_temp) #?????                                       
128    return my_list                                                               
129                                                                                 
130                                                                                 
131                                                                                 
132 def sort_crimes(crimes):                                                        
133    #takes a list of crime objects and returns a list of crime objects           
134    #sorted by SELECTION SORT (going over in class)                              
135    #crimes = list of crime objects, like 3600                                   
136    #returns a list of crime objects sorted by ID number                         
137     for i in range(len(crimes) - 1, 0, -1):                                     
138        max_val = 0                                                              
139        for  n in range(1, i + 1):                                               
140           if crimes[n].crime_id > crimes[max_val].crime_id:                     
141               max_val = n                                                       
142        temp = crimes[i]                                                         
143        crimes[i] = crimes[max_val]                                              
144        crimes[max_val] = temp                                                   
145     return crimes                                                               
146                                                                                 
147    def update_crimes(crimes, lines):                                               
150        #returns a list of crime objects with updated attributes from times.tsv  
151        #crimes = sorted crimes, lines = list of strings from times.tsv          
152        my_list = []                                                             
153        fix = 3                                                                  
154        for i in lines:                                                          
155           index = i.split("\t")                                                 
156           id_ = index[0]                                                        
157           func_id = int(index[0])                                               
158           day_of_week = index[1]                                                
159           month = index[2]                                                      
160           hour = index[fix]                                                     
161           my_obj = find_crime(crimes, func_id)                                  
162           if my_obj is not None:                                                
163             my_obj.set_time(day_of_week, month, hour)                           
164    #         my_list.append(my_obj)                                             
165        return crimes                                                            
166                                                                                 
167  def find_crime(crimes, crime_id):                                               
173       start = 0                                                                 
174       end = len(crimes) - 1                                                     
175       found = 0                                                                 
176       while start <= end:                                                       
177          middle = (start + end) // 2                                            
178          if crime_id == crimes[middle].crime_id:                                
179              found = 1                                                          
180              return crimes[middle]                                              
181          else:                                                                  
182             if crime_id < crimes[middle].crime_id:                              
183                end = middle - 1                                                 
184             if crime_id > crimes[middle].crime_id:                              
185                start = middle + 1                                               
186       return None                                                               
187                                                                                 
188                                                                                 
189                                                                                 
190 def get_day(crimes_updated):                                                    
191     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", 
192            "Sunday"]                                                            
193     counter = []                                                                
194     day = [i.day_of_week for i in crimes_updated] #list of ONLY day_of_week attributes
195     for n in days: #find the amount of every day, add to get a value            
196        if n in day:                                                             
197           count = day.count(n)                                                  
198           counter.append(count) #append values to a list in order               
199        else:                                                                    
200          counter.append(0)                                                      
201     max_val = max(counter) #find the max value in hte list                      
202     maxval = counter.index(max_val) #find max value in list                     
203     my_day = days[maxval] #get index in original list                           
204     return my_day                                                               
205                                                                                 
206                                                                                   
211 def get_month(crimes_updated):                                                  
212        months = ["January", "February", "March", "April", "May", "June", "July",
213                  "August", "September", "October", "November", "December"]      
214        counter = []                                                             
215        month = [i.month for i in crimes_updated]                                
216        for n in months:                                                         
217           if n in month:                                                        
218              count = month.count(n)                                             
219              counter.append(count)                                              
220           else:                                                                 
221              counter.append(0)                                                  
222        max_val = max(counter)                                                   
223        maxval = counter.index(max_val)                                          
224        my_month = months[maxval]                                                
225        return my_month                                                          
226                                                                                 
227                                                                                 
228 def get_hour(crimes_updated):                                                   
229     hours = ["1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM",     
230              "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM",         
231              "6PM", "7PM", "8PM", "9PM", "10PM", "11PM", "12AM"]                
232     counter = []                                                                
233     hour = [i.hour for i in crimes_updated]                                     
234     for n in hours:                                                             
235           if n in hour:                                                         
236             count = hour.count(n)                                               
237             counter.append(count)                                               
238           else:                                                                 
239             counter.append(0)                                                   
240     max_val = max(counter)                                                      
241     maxval = counter.index(max_val)                                             
                my_hour = hours[maxval]                                                     
243     return my_hour                                                              
244                                                                                                   
                                        
