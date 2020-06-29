from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.template import loader


from zxcvbn import zxcvbn

def index(request):
	return render(request, 'main/index.html', { })

def lookup(request):
	response_data = {}

	if request.POST.get('action') == 'post':
		word = request.POST.get('word')
	results = zxcvbn(word, user_inputs=[])

	response_data['score'] = results['score']
	response_data['crack_times_display'] = results['crack_times_display']
	return JsonResponse(response_data)

def wireframe1(request):
	arr = [1,1,1,1,1,1];
	return render(request, 'main/wireframe1.html', { "len":arr })

def wireframe2(request):
	# arr = [1,1,1,1,1,1];
	return render(request, 'main/wireframe2.html', { })

def svg(request):
	return render(request, 'main/svg.html', { })

def aspect(request):
	return render(request, 'main/aspect.html', { })




def render_intro(request, lesson_id):

	# get this from the id?
	title="Design collaboration that doesn’t break at scale" 
	content = {
	'lesson_1': {
		'title':"Design collaboration that doesn’t break at scale", 
		'parts': {
			'Overview': {'text':'Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on. <br/><br/> Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 1': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 2': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 3': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 4': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 5': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 6': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 7': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 8': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 9': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			}
		},
	'lesson_2': {
		'title':"2Design collaboration that doesn’t break at scale", 
		'parts': {
			'Overview2': {'text':'Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on. <br/><br/> Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 1a': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 2a': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 3a': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 4a': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 5': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 6': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 7': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 8': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			'Part 9': {'text':'Part one - Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
			}
		}, 

	}

	return render(request, 'main/1_page.html', { "lesson_id": lesson_id, "special_type":'intro', "title":title, "content": content['lesson_' + str(lesson_id)] })

def render_slideshow(request, lesson_id, page_id):
	arr = [1,1,1,1];
	content = {
		'lesson_1': { 
			1:[
					{
						'type':'Speaker Notes',
						'text':'Let’s start with a throwback to the 90s. <br/><br/>Who here has been to a BlockBuster? <br/>(if yes) Yea? When was the last time you went? Anyone else?<br/><br/>30 years ago, BlockBuster used to be the norm. If I wanted to watch a movie at home, I would have to drive to my local BlockBuster, browse their rows of shelves, stand in line to check out a DVD or VHS tape, and then drive home. <br/><br/>What do you guys do today if you want to watch a movie?<br/><i>(look for 2-3 answers like - iTunes, Netflix, Amazon Prime, Hulu)</i><br/>'
					}
				], 
			2:[
				{
					'type':'Speaker Notes',
					'text':'Now, in our digital economy, all I have to do is log into an iTunes, Netflix or Amazon Prime and hit play. I can watch a movie anytime, from anywhere, instantaneously, as long as I’m connected to the internet.'
				}
			],
			3:[
				{
					'type':'Speaker Notes',
					'text':'On the flip side, these services also have a lot more information about me. They can track:<br/><ul><li>What movies I’ve seen 10 times</li><li>What movies I stopped watching after 10 minutes</li><li>How often I watch movies, and for how long</li><li>My physical location (based on your IP address)</li><li>My credit card</li></ul>'
				},
				{
					'type':'The Big Idea',
					'text':'Think about how much more information Netflix has about you than a BlockBuster used to. With the move to a digital economy, our digital new services and products have a lot more information about us than they used to. '
				}
			],
			4:[
				{
					'type':'Speaker Notes',
					'text':'Let’s take another example. How many of you have used a physical map?<br/>(if yes) Yea? When was the last time you went? Anyone else?<br/><br/>Well, 30 years ago, this used to be the norm. If I didn’t know the directions to where I was going, I’d pull out one of these. I’d figure out the major highways and major streets that I need to take to get to where I was trying to go -- and probably also pull into a gas station occasionally when we got lost. <br/>'
				}
			],
			5:[
				{
					'type':'Speaker Notes',
					'text':'Now, in our digital economy, all I have to do is enter an address into Google or Apple Maps and hit go. <br/><br/>What is the flipside? What information do Google and Apple Maps have about me now that a physical map could never have known?<br/><i>(look for 2-3 answers like - where you’re going, when you’re going, where you live and work)</i><br/>'
				}
			],
			6:[
				{
					'type':'Speaker Notes',
					'text':'These services have a lot more information about you that a physical map could never have known. They can track exactly where you’re going and when. And they can easily guess:<br/><ul><li>Where you work and where you live</li><li>What your favorite restaurants </li><li>What hotels you stay at when you travel</li><li>Where you bank or shop for groceries</li></ul>'
				}
			]
		}
	}

	print('max key')
	print(max(content['lesson_'+str(lesson_id)].keys()))
	max_ = max(content['lesson_'+str(lesson_id)].keys())
	print('min key')
	print(min(content['lesson_'+str(lesson_id)].keys()))
	min_ = min(content['lesson_'+str(lesson_id)].keys())

	prev_ = page_id-1
	next_ = page_id+1
	if prev_ < min_: 
		prev_ = None
	if next_ > max_:
		next_ = None;

	print(prev_)
	print(next_)

	return render(request, 'main/1_page.html', 
		{ "lesson_id":lesson_id, 
		"page_id":page_id, 
		"slide_template":'main/slides/lesson_'+ str(lesson_id) + '/' + str(page_id) + '.html', 
		"content": content['lesson_'+str(lesson_id)], 
		"prev": prev_,
		"next": next_,
		"arr": arr
		}
	)
	