from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hare krishna")


def quiz(request):
    # question=[]
    questions = ["one", "two", "three", "four"]
    qno = 0
    if request.GET:
        qno = int(request.GET["qno"])
        qno += 1

    if qno >= len(questions):
        return HttpResponse("end test")
    else:
        question = questions[qno]
    return render(request, "quiz.html", {"qno": qno, "qshow": qno + 1, "question": question})


def tfquiz(request):
    questions = [{"question": "C is a programming language", "answer": True},
                 {"question": "Java is not a programming language", "answer": False},
                 {"question": "C is not a programming language", "answer": False}]
    qno = 0

    if request.GET:
        opt = request.GET["option"]
        a = request.GET["a"]
        if opt == "next":
            qno = int(request.GET["qno"])
            qno += 1
        if opt == "previous":
            qno = int(request.GET["qno"])
            qno -= 1
    if qno >= len(questions):
        return render(request, "result.html")
    question = questions[qno]
    return render(request, "tfquiz.html", {"qno": qno, "qnumber": qno + 1, "question": question})


def squiz(request):
    question = [
        {"question": "what is c language", "a": "programming language", "b": "letter", "c": "code", "d": "all of the above"},
        {"question": "python is a..?", "a": "snake", "b": "programming language", "c": "data",
         "d": "all of the above"},
        {"question": "java is a programming language", "a": "false", "b": "sentence", "c": "true", "d": "all of the above"},
        {"question": "html is a language","a":"false","b":"true","c":"aa","d":"all of the above"}]
    qno = 0
    print(len(question))
    if request.GET:
        #qno += 1
        # print("In Get")
        opt = request.GET["option"]
        # print("opt")
        qno = int(request.GET["qno"])
        if opt == "next":

            qno += 1
        if opt == "previous":

            qno -= 1
        if qno >= len(question):
          return HttpResponse("Quiz Over")
    return render(request, "squiz.html", {"qno": qno, "question": question[qno], })

