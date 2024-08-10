from datetime import datetime as dt

def main(event):
  # Use inputs to get data from any action in your workflow and use it in your code instead of having to use the HubSpot API.
  doj = event.get('inputFields').get('doj')
  if doj == None:
    return {
    "outputFields": {
      "total_productive_hours": 0
    }
    }
  else:
    doj = int(doj) #converted the string timestamp to int timestamp
    doj /= 1000 #converted timestemp into seconds
    doj = dt.fromtimestamp(doj) #timestamp to datetime conversion
    doj = doj.strftime('%Y-%m-%d') #converted date into the format that today() function returns
    today = dt.today() #Returns the today's date
    if isinstance(doj, str):
        doj = dt.strptime(doj, '%Y-%m-%d') #Convert the string date into datetime object
    #following lines will extract day, month and year
    day_doj = doj.day
    month_doj = doj.month
    year_doj = doj.year
    day_today = today.day
    month_today = today.month
    year_today = today.year
    max_hours = 140
    #calculating month difference considering the change in year
    months_difference = (year_today - year_doj) * 12 + (month_today - month_doj)
    #determining the multiplier
    if day_doj <= 15:
        if month_today == month_doj:
        	multiplier = 0.5
        elif months_difference == 1:
        	multiplier = 0.75
        else:
        	multiplier = 1
    else:
        if month_today == month_doj:
        	multiplier = 0.5
        elif abs(months_difference) == 1:
        	multiplier = 0.5
        elif abs(months_difference) == 2:
        	multiplier = 0.75
        else:
        	multiplier = 1
    hours = max_hours * multiplier # stores the total productive hours
    hours = int(hours)
    return {
        "outputFields": {
        "total_productive_hours": hours
        }
  }