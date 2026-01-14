from hm1.models import site


site.objects.create()
# this will do data  addition via shell


#to show all values 
site.objects.all()

# to save 
site.save()

#to access [inside these we have to say row number] and after that we have to tell column name
>>> Site.objects.all()[0].name
'WOW_KOL277_WOW_China_Madhyamgram'

#to update we can use below
x = Site.objects.all()[]
>>> x.name='WoW_KOL277_WOW_China_Madhyamgram'
>>> x.name
'WoW_KOL277_WOW_China_Madhyamgram'


#to delete records
x.delete()

# The values_list() method allows you to return only the columns that you specify.