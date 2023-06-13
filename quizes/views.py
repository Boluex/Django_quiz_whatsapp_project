from django.shortcuts import render,redirect
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result
from django.contrib.auth import logout
from django.http import HttpResponse
from users.models import profile
import random
from django.contrib.auth.decorators import login_required
from.whatsapp_ai import whatsapp_bot
from users.models import image_data
import mathy
# class QuizListView(ListView):
#     model = Quiz 
#     template_name = 'quizes/main.html'
@login_required(login_url='/login')
def QuizListView(request):
    quiz = Quiz.objects.all()
    return render(request, 'quizes/main.html', {'object_list': quiz})
# @login_required
def quiz_view(request, id):
    if request.user.is_anonymous:
        return redirect('login')
    quiz = Quiz.objects.get(id=id)
    # get_user=User.objects.get(username=request.user.username)
    get_user_id=profile.objects.get(user=request.user)
    return render(request, 'quizes/quiz.html', {'obj': quiz,'token':get_user_id.token})
def quiz_data_view(request, id):
    if request.user.is_anonymous:
        return redirect('quizes:sign-up')
    quiz = Quiz.objects.get(id=id)
    get_user_payment=profile.objects.get(user=request.user)
    questions = []
    if get_user_payment.paid == True:
        # questions = []
        random.shuffle(questions)
        for q in quiz.get_questions():
            answers = []
            for a in q.get_answers():
                answers.append(a.text)
            questions.append({str(q): answers})
            random.shuffle(questions)
        return JsonResponse({
            'data': questions[0:19],
            'time': quiz.time,
        })
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions[0:4],
        'time': quiz.time,
    })
    

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
@login_required()
def save_quiz_view(request, id):
    if is_ajax(request=request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            # print('key: ', k)
            question = Question.objects.filter(text=k).first()
            questions.append(question)
        # print(questions)

        user = request.user
        quiz = Quiz.objects.get(id=id)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
                
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)
        

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})


def over(request):
    logout(request)
    return render(request,'quizes/over.html')




def redirect(request):
    return HttpResponse('<h2>Contact your bot to continue</h2> ')


def new_data(request):
    if request.method == 'POST':
        filter_user=image_data.objects.filter(user=request.user)
        if filter_user.exists():
            filter_user.delete()
            newfile=image_data(user=request.user,image=request.FILES['resume'])
            newfile.save()
            return redirect('redirect')
        newfile=image_data(user=request.user,image=request.FILES['resume'])
        newfile.save()
        return redirect('redirect')
    return HttpResponse('not a POST method')


# /home/deji/Desktop/deji/PycharmProjects/pythonProject/quiz_proj/files
# def get_image(request):
#     get_image_model=image_data.objects.get(id=5)
#     images=get_image_model.image
#     # imagepath="quiz_proj//files" + images
#     imagepath=images.path
#     textimages=textimage(imagepath)
#     print(textimages)
#     textans=whatsapp_bot(textimages)
#     return HttpResponse(textans)