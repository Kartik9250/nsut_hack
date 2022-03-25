from django.shortcuts import render

posts =[
	{
		'user': 'kartik',
		'slot booked': 'A1',
		'date': '19/03/2003',
		'entry-time': '10:90',
		'exit-time': '11:30'
	},
	{'user': 'kartik',
		'slot booked': 'A1',
		'date': '19/03/2003',
		'entry-time': '10:90',
		'exit-time': '11:30'}
]
def home(request):
	context = {
		'posts': posts
	}
	return render(request ,'Site/home.html', context)

def about(request):
	return render(request ,'Site/about.html')