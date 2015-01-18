def greet(name):
	print "hello",name;
	#we do not need () after print method actually
	#if we need to print all the ouput in one line, we need to add trailing comma after the print

greet("aaron");
#because this is a globle function without class, we do not need to add the object of the class before it

friends = ["john","pat","haha"]
for i, name in enumerate(friends):
	print ("iteration {place} is {name}".format(place = i, name=name))

	#using enumerate function whenever we want to get the index and the value at the same time

price_dic = {"apple":0.40, "banana":0.55}
my_order = {"apple":10, "banana":6}
#the number in my_order dic is the number of fruits I bought
total_bill = sum(price_dic[index] * my_order[index] for index in my_order)
total_bill2 = sum(price_dic[index] * my_order[index] for index in price_dic)

print "I should pay $ %.2f to the grocer" %total_bill;

print("I should pay $ %.2f to the grocer" %total_bill2);