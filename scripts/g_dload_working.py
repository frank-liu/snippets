#
# thrown together by james allen munsch, some credit to http://stackoverflow.com/users/1404614/jaimecervantes
# and here : http://stackoverflow.com/questions/9318577/python-the-right-url-to-download-pictures-from-google-image-search
#
import os
import glob
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson
from threading import Thread

# Start FancyURLopener with defined version 
class MyOpener(FancyURLopener): 
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()

def mk_dir(p):
	if os.path.exists(p) is True:
		print "Directory already exists: "+p
		return True
	os.mkdir(p)
	print "MADE DIR: "+p




def ch_dir(p):
	os.chdir(p)
	print "CHANGED TO: "+p

def get_item(term,p):

	mk_dir(p)
	ch_dir(p)
	print "searching: "+term

	
	c = []
	for i in range(0,10):
		# Notice that the start changes for each iteration in order to request a new set of images for each loop
		url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+str(term)+'&start='+str(i*4)+'&userip=MyIP')
		print url
		request = urllib2.Request(url, None, {'Referer': 'testing'})
		response = urllib2.urlopen(request)

		# Get results using JSON
		results = simplejson.load(response)

		try:		
			data = results['responseData']
		except:
			print "oops on results: "
			pass

		try:
			dataInfo = data['results']
		except:
			print "oops on data: "
			pass

		for myUrl in dataInfo:
		    c.append(myUrl['unescapedUrl'])

		# Sleep for one second to prevent IP blocking from Google
		time.sleep(1)

	return c


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def google_term(t_args):

	for items in t_args:
		s_name = items[0]
		p = items[1]
		term = items[2]
# test
#		if os.path.exists(p+):
#			pass
		

		mk_dir(p)
		ch_dir(p)
		# check to see if urls.txt has already been downloaded if so then pass
		if os.path.exists(p+'/urls.txt') is True:
			print "Checking if urls exist"			
			fl = file_len(p+'/urls.txt')
			if fl >= 40:
				print "Urls exist for: "+p
				continue
		

		url_list = get_item(term,p)	
# test
#		url_list = ['1.com','2.com']		



		ff = open(p+'/urls.txt','w')
		ff.close()
		ff = open(p+'/urls.txt','a')

		for item in url_list:
			ff.write(item+'\n')
		ff.close()

		print "Done Writing urls to: "+p+"/urls.txt"
		ff.close()






def loopcount(t_args,var = 0):
	
	loopcounter = []
	z = []
	for items in t_args:
	#	print t_args
		s_name = items[0]
		p = items[1]
		term = items[2]
		# add a global counter variable
		loopcounter.append(0)
		# create z
		urls_read = open(p+'/urls.txt')
		x = [s_name,p,term,loopcounter,urls_read]
		z.append(x)


	for items in z:
		items.append(var)
		start_thread(items)
		var = var + 1
				



def start_thread(xxx):
	
	print "Starting Thread for: "+str(xxx[0])
	t = Thread(target=get_urls, args=(xxx,))
	t.start()



def get_urls(zzz):
	
	s_name = zzz[0]
	p = zzz[1]
	term = zzz[2]
	loopcounter = zzz[3]
	v = zzz[5]
	urls = zzz[4]

#	print "#############"
#	print s_name
#	print p
#	print term
#	print loopcounter
#	print v
#	print urls
#	print "##########################"

#ch_dir(p)
	for url in urls:
		try:
			ch_dir(p)
#			print "var: "+str(var)
#			print "lc:"+str(loopcounter)
#			print "lc_var: "+str(loopcounter[var])
#			print "Retrieving: "+url
#			os.system('touch '+str(loopcounter[v])+'.jpg')
			myopener.retrieve(url,str(loopcounter[v])+'.jpg')
#			print "finished: "+url
			loopcounter[zzz[5]] = loopcounter[zzz[5]] + 1
		except:
			print url
			raise
#		var = var + 1
	print "get_urls:"+str(v)
	print loopcounter
	return v
		
def search(srch,d):
	# Define search term
	searchTerms_20 = []
	t_args = []
	# Replace spaces ' ' in search term for '%20' in order to comply with request

	for item in srch:
		t2 = item.replace(' ','%20')
		searchTerms_20.append(t2)
	
	for term in searchTerms_20:
		s_name = term.replace('%20','_')
		p = os.path.expanduser(d)+s_name
		term = term
		temp = []

		temp.append(s_name)
		temp.append(p)
		temp.append(term)

		t_args.append(temp)
	return t_args



###########
# run 
###########

terms = ["annoying banner ads"]
d = os.getcwd()+'/'



# dictionary of [['s_name0','p0','term0'],['s_name1','p1','term1'], ... ['s_nameN','pN','termN']]





t_args = search(terms,d)
#print t_args
#exit()

#write_imacros(t_args)
#exit()

# writes url files needed for loopcount_dload
google_term(t_args)



# download loop count for variables
loopcount(t_args)
	








