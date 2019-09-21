import matplotlib.pyplot as plt
reportname = 'Basel_weather_2016_daily_simple.csv'
PLOT_FONT_AXIS = {'size' : 'large', 'color': 'Green'}
PLOT_FONT_TITLE = {'fontsize': 18,  'color': 'Orange'}
WSKP_TO_WMS = 0.2278
# open file can be used as well but in order to handle exception with open is used which means any error
# at the time of opening file will be handled with open sytax 
with open(reportname, 'r', encoding='ASCII') as datafile:
 columns = datafile.readline() # reading line from the file and split is used to split columns with ,. 
 columns = columns.split(',')
 
 col_index_temp_avg = columns.index('Temperature daily mean')
 col_index_temp_max = columns.index('Daily Maximum Temprature')
 col_index_temp_min = columns.index('Daily Minimum Temprature')
 col_index_wind = columns.index('Daily wind means')
 col_index_precip = columns.index('Daily total precip')



temps = []
temp_avg =[]
temp_max = []
temp_min = []
wind_WSKP = []
precip_mm = []
 # for loop to obtain the values of the temps from rows 
for row in datafile:
     # here string will be split through , and row are splitted though for loop. 
     value = []
     for x in row.split(','):
          value.append(float(x))
temp.append(value[col_temp_avg])
temp_min.append(value[temp_min])
temp_max.append(value[temp_max])
wind_WSKP.append(value[col_wind])
precip_mm.append(value[col_precip])
 
print('\n Temperature daily mean: \n', temps)

# next part of the program plt will be used. plt is hte plot library which is alreayd imported 
# in the start of the porgram 
# it is the same se fig, histrogram and many other visulization for this purposes. 

plt.figure(figuresize=(19, 10))
plt.plot(temp_min, 'r++' , label=columns[col_temp_min])
plt.plot(temp_max, 'gX:' , label=columns[col_temp_max])
plt.plot(temps, 'b*-', label=columns[col_temp_avg])
 
# Now title, lables, y axis and x axis as well as lengend is applied to get visulization 
plt.xlabel('Time (Day of Year)', **PLOT_FONT_AXIS)
plt.ylabel('Mean Temperature (°C)', **PLOT_FONT_AXIS)
plt.title('2016 Daily Mean Temperatures - Basel', fontdict=PLOT_FONT_TITLE)
plt.legend()  # auto-legend with labels above.
plt.savefig('ben-plot-temps.png')
plt.show()


# 3. Get the daily mean wind speed in m/s (the data file contains wind speed in km/h).
wind_WMS = [wind_WSKP * WSKP_TO_WMS for wind_WSKP in wind_WSKP]


plt.clf()
plt.plot(wind_WMS)
plt.xlabel('Time (Day of Year)', **PLOT_FONT_AXIS)
plt.ylabel('Mean Wind Speed (m/s)', **PLOT_FONT_AXIS)
plt.title('2016 Daily Wind Speeds - Basel', fontdict=PLOT_FONT_TITLE)
plt.savefig('ben-plot-wind.png')
plt.show()


print('\nTotal annual precip = {} mm'.format(sum(precip_mm)))
print('Annual Temp (Max) = {} °C'.format(max(temp_max)))
print('Annual Temp (Min) = {} °C'.format(min(temp_min)))
