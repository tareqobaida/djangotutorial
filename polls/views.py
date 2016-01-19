from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.views import generic
from .models import Question, Choice
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='latest_question_list'
	def get_queryset(self):
		""" return the las five published questions """
		return Question.objects.order_by('-pub_date')[:5]
	
	
class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'
def vote(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#redisplay the question voting format
		return render( request, 'polls/detail.html', 
		{'question':question, 'error_message': 'You dont select a choice'})
	else:
		selected_choice.vote+=1
		selected_choice.save()
	#always return a HtttpResponseRedirect after dealing with post data. this prevents data from being posted twice
	#if a user hits the back button
	return HttpResponseRedirect(reverse('polls:results', args=(question.id)))