from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, OptionForm
from .models import Question, Option, Result
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

# Create your views here.



def index(request):
    questions = Question.objects.all
    user_questions = []
    if request.user.is_authenticated:
        user_questions = Question.objects.filter(user=request.user)
        print(user_questions)
    return render(request, "ordersorter/index.html", {
        "questions": questions,
        "user_questions": user_questions
    })

def test(request):
    
    return render(request, "ordersorter/test.html")

def poll(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(request.method)
    # question = Question.objects.get(pk=question_id)
    if request.method == "POST":
        # the post name is in the name tag in the html... its not the id
        newname = request.POST["resultName"]
        items = request.POST.getlist("order")
        # items = request.POST.
        print(items)
        # items = request.POST['orderItem']
        theorder = {'items': items}
        newResult = Result(name=newname, order=theorder, question=question)

        newResult.save()
        # question.results.add(newResult)
        question.save()
        context = {
            'question': question,
        }
        return HttpResponseRedirect(reverse('ordersorter:results', args=(question.id,)))
        
        # return render(request, 'ordersorter/results.html', context)
    else:
        return render(request, 'ordersorter/poll.html', {
            'question': question,
        })


    

def edit(request, question_id):
    question = Question.objects.get(pk=question_id)
    # question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        if request.POST.get("button") == "add-option":
            newOptionText = request.POST["optionText"]
            if newOptionText != "":
                newOption = Option(optionText=newOptionText, question=question)
                newOption.save()
                questionText = request.POST["question"]
                description = request.POST["description"]
                question.question = questionText
                question.description = description
                question.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('ordersorter:edit', args=(question.id,)))
            else:
                context = {
                    'question': question,
                    'message': f"Option value cannot be empty",
                    'form': OptionForm()
                }
                return render(request, 'ordersorter/edit.html', context)
        if request.POST.get("button") == "update-question":
            questionText = request.POST["question"]
            description = request.POST["description"]
            question.save()
            return HttpResponseRedirect(reverse('ordersorter:edit', args=(question.id,)))

        print(request.POST)
        # delete the option, by first looping through all the options to find which one was clicked on
        for option in question.options.all():
            if f'{option.id}' in request.POST:
                option.delete()
                return HttpResponseRedirect(reverse('ordersorter:edit', args=(question.id,)))

    context = {
        'question': question,
        'form': OptionForm()
    }
    return render(request, 'ordersorter/edit.html', context)
    

def create(request):

    if request.method == 'GET':
        context = {
            'form': QuestionForm(),
            'message': ''
        }

        return render(request, "ordersorter/create.html", context)

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            context = {
                "question": question
            }
            return HttpResponseRedirect(reverse('ordersorter:edit', args=(question.id,)))

        return render(request, "ordersorter/create.html")

def results(request, question_id):
    question = question = get_object_or_404(Question, pk=question_id)
    
    # if a result gets deleted, we should be able to reload the page...
    if request.method == 'POST':
        # print(request.POST)
        # delete the option, by first looping through all the options to find which one was clicked on
        resultId = request.POST['delete']
        # print(resultId)
        for result in question.results.all():
            # print(f"comparing {result.id} to {resultId}")
            if str(result.id) == str(resultId):
                # print(f"deleting result {result.id}")
            # if f'{result.id}' in request.POST:
                result.delete()
                return HttpResponseRedirect(reverse('ordersorter:results', args=(question.id,)))

    scoresDict = calculateScores(question)
    # sort the scores
    scoresDict = dict(sorted(scoresDict.items(), key=lambda item: item[1], reverse=True))
    # surveyStats contains an array of the winning message with the winner(s) and score along with loser, most ones, most topThress. 
    surveyStats = getSurveyStats(scoresDict, question)
    
    context = {
        'question': question,
        # 'results': results,
        'range':range(len(question.options.all())),
        'scoresDict': scoresDict,
        'surveyStats': surveyStats

    }
    return render(request, 'ordersorter/results.html', context)

# helper functions to calculate the results
def calculateScores(question):
    results = question.results.all()
    # empty dictionary, planning on storing the scores for each option
    scoresDict = {}
    for option in question.options.all():
        scoresDict[option.optionText] = 0
    # loop through the results order and add to the score for that option
    for result in results:
        mult = len(question.options.all())
        for item in result.order["items"]:
            # Add item to dictionary in case it was deleted from the list
            if item not in scoresDict:
                scoresDict[item] = 0
            scoresDict[item] += mult
            mult-=1
    return scoresDict

def getSurveyStats(scoresDict, question):
    results = []
    results.append(getWinnerOrLoser(scoresDict, "HIGHEST SCORE: ", True))
    results.append(getMostExtremes(question, "TOP CHOICE THE MOST: ", True))
    results.append(getMostTopOrBottomThree(question, "CHOSEN TOP 3 THE MOST: ", True))
    results.append(getWinnerOrLoser(scoresDict, "LOWEST SCORE: ", False))
    results.append(getMostExtremes(question, "LAST CHOICE THE MOST: ", False))
    results.append(getMostTopOrBottomThree(question, "CHOSEN IN BOTTOM 3 THE MOST: ", False))
    results.append(f"TOTAL SURVEYS: {len(question.results.all())}")
    return results
    
# this method will return either the highest or lowest score, based on the parameters. isWinner is used to determine max or min
def getWinnerOrLoser(scoresDict, output, isWinner):
    winners = []
    # first find highest score...
    if len(scoresDict.items()) == 0:
        return f"{output} None"
    highestScore = max(scoresDict.values()) if isWinner else min(scoresDict.values())
    
    # next find keys that match the highest score...
    for key, value in scoresDict.items():
        if value == highestScore:
            winners.append(key)
    # print(winners)
    message=f"{output}"
    if len(winners) == 1:
        message+=f"{winners[0]} ({highestScore})"
    elif len(winners) == 2:
        message+=f"{winners[0]} and {winners[1]} ({highestScore})"
    else:
        for i in range(0, len(winners)-1):
            message += f"{winners[i]}, "
        message += f"and {winners[-1]} "

        message += f"({highestScore})"
    return message

# this method can be used to determine which option has the most top choice and which one has the most bottom choice
def getMostExtremes(question, output, isTop):
    results = question.results.all()

    if len(results) == 0:
        return f"{output} None"
    # empty dictionary, planning on storing the scores for each option
    number1s = {}
    for result in results:
        if result.order["items"]:
            if len(result.order["items"]) > 0:
                pos = 0 if isTop else -1
                currentnum1 = result.order["items"][pos]
                if currentnum1 not in number1s:
                    number1s[currentnum1] = 1
                else:
                    number1s[currentnum1] += 1

    highestNum = max(number1s.values())
    # print(highestNum)
    mostOnes = []
    for key,value in number1s.items():
        if value == highestNum:
            mostOnes.append(key)
    # print(mostOnes)
    message=f"{output}"
    if len(mostOnes) == 1:
        message+=f"{mostOnes[0]} ({highestNum}) times"
    elif len(mostOnes) == 2:
        message+=f"{mostOnes[0]} and {mostOnes[1]} ({highestNum}) times"
    else:
        for i in range(0, len(mostOnes)-1):
            message += f"{mostOnes[i]}, "
        message += f"and {mostOnes[-1]} "
        message += f" ({highestNum}) times"
    return message

# this method will comput the options that are selected in the top 3 or bottom 3 the most.
def getMostTopOrBottomThree(question, output, isTop):
    results = question.results.all()
    # empty dictionary, planning on storing the scores for each option
    if len(results) == 0:
        return f"{output} None"
    top3s = {}
    for result in results:
        try:
            if len(result.order["items"]) >= 1:
                current = result.order["items"][0] if isTop else result.order["items"][-1]
                if current not in top3s:
                    top3s[current] = 1
                else:
                    top3s[current] += 1
            if len(result.order["items"]) >= 2:
                current = result.order["items"][1] if isTop else result.order["items"][-2]
                if current not in top3s:
                    top3s[current] = 1
                else:
                    top3s[current] += 1
            if len(result.order["items"]) >= 3:
                current = result.order["items"][2] if isTop else result.order["items"][-3]
                if current not in top3s:
                    top3s[current] = 1
                else:
                    top3s[current] += 1  
        except:
            print(f"result does not contain any items{result}")
    # get highest value in number1's
    highestNum = max(top3s.values())
    mostOnes = []
    for key,value in top3s.items():
        if value == highestNum:
            mostOnes.append(key)
    message=f"{output}"
    if len(mostOnes) == 1:
        message+=f"{mostOnes[0]} ({highestNum}) times"
    elif len(mostOnes) == 2:
        message+=f"{mostOnes[0]} and {mostOnes[1]} ({highestNum}) times"
    else:
        for i in range(0, len(mostOnes)-1):
            message += f"{mostOnes[i]}, "
        message += f"and {mostOnes[-1]} "

        message += f" ({highestNum}) times"
    return message





