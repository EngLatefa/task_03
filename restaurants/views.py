from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"restaurants": [
	    	{
		        "name": "Ask Italian",
		        "type": "italian",
		        "rating": "4.5"
	    	},
	    	{
		        "name": "Fridays",
		        "type": "American",
		        "rating": "5"
		    },
		    {
		        "name": "Noodles",
		        "type": "Chinese",
		        "rating": "3.5"
		    }
    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
	    "resturaunt": {
			    "name": "Ask Italian",
			    "type": "italian",
			    "rating": "4.5",
			    "location": "union square",
			    "style": "cosy",
            }
            }
    return render(request, 'detail.html', context)
