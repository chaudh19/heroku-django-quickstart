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



def render_intro(request, lesson_id):

	# get this from the id?
	title="Design collaboration that doesn’t break at scale" 
	content = {
	'lesson_1': {
		'title':"Design collaboration that doesn’t break at scale", 
		'parts': {
			'Overview': {'text':'Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
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
			'Overview2': {'text':'Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.', 'time':'3 minutes'},
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

	content = {
		'lesson_1': { 
			1:[
					{
						'type':'Speaker Notes',
						'text':'ONE Import your Sketch and Adobe XD files\n\n<br/> into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.'
					},
					{
						'type':'Big idea',
						'text':'ONE With the move to a digital economy, our digital new services and products have a lot more information about us than they used to. These next few slides use tangible examples (like Blockbuster vs Netflix, or film cameras vs Instagram) to help students explore what kind of information we’re sharing with these digital services.'
					},
					{
						'type':'Speaker Notes',
						'text':'ONE Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.'
					}
				], 
			2:[
				{
					'type':'Speaker Notes',
					'text':'TWO Import your Sketch and Adobe XD files into Abstract and instantly create a centralized place for your most up-to-date design work and supporting documentation. In Abstract, the latest version is called master, so there’s never any confusion about what’s final and what’s still being worked on.'
				},
				{
					'type':'Big idea',
					'text':'TWO With the move to a digital economy, our digital new services and products have a lot more information about us than they used to. These next few slides use tangible examples (like Blockbuster vs Netflix, or film cameras vs Instagram) to help students explore what kind of information we’re sharing with these digital services.'
				}
			]
		}
	}

	return render(request, 'main/1_page.html', 
		{ "lesson_id":lesson_id, 
		"page_id":page_id, 
		"slide_template":'main/slides/lesson_'+ str(lesson_id) + '/' + str(page_id) + '.html', 
		"content": content['lesson_'+str(lesson_id)], 
		"prev":page_id-1,
		"next":page_id+1,
		}
	)
	