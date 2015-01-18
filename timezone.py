from time import localtime;
activities = {8:"sleeping",17:"working",9:"commuting",12:"eating",22:"playing"}
current_time = localtime();
hour = current_time.tm_hour;

for time_index in sorted(activities.keys()):
	if hour < time_index:
		print activities[time_index];
		break;

else:
	print "after the whole loop we have not met with any valid time schedule"