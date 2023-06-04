from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#By Carlos

#Fim by Carlos

def logoutusuario(request):
    logout(request)
    return redirect('lista_tutores')

def loginusuario(request):
    if request.method == "POST":
        username = request.POST['nome']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_tutores')
        else:
            messages.success(request, ("Username ou Senha Incorreto(s)."))
            return redirect('login')
    
    
    else:
        return render(request, 'brotherInCode/login.html', {})

def lista_tutores(request):
    res = []
    tutores = Tutores.objects.all()
    for tutor in tutores:
        especializacoes = EspecializacaoTutor.objects.filter(id_tutor=tutor)
        avaliacoes = AvaliacaoTutor.objects.filter(id_tutor=tutor)
        res.append({
            'id_tutor': tutor.id_tutor,
            'nome': tutor.nome,
            'especializacoes': EspecializacaoTutorSerializer(especializacoes, many=True).data,
            'estrelas': [0]*int(sum([avaliacao.nota for avaliacao in avaliacoes])/len(avaliacoes)) if len(avaliacoes) > 0 else [0],
        })
    return render(request, 'brotherInCode/main2.html', {'tutores': res})


def perfil_tutor(request, id_tutor):
    tutor = Tutores.objects.get(id_tutor=id_tutor)
    especializacoes = EspecializacaoTutor.objects.filter(id_tutor=tutor)
    avaliacoes = AvaliacaoTutor.objects.filter(id_tutor=tutor)
    horarios = HorariosTutor.objects.filter(id_tutor=tutor)
    res = {
        'id_tutor': tutor.id_tutor,
        'nome': tutor.nome,
        'sobre': tutor.sobre,
        'especializacoes': EspecializacaoTutorSerializer(especializacoes, many=True).data,
        'estrelas': [0]*int(sum([avaliacao.nota for avaliacao in avaliacoes])/len(avaliacoes)) if len(avaliacoes) > 0 else [0],
        'horarios': HorariosTutorSerializer(horarios, many=True).data,
    }
    
    return render(request, 'brotherInCode/main.html', {'tutor': res})


def perfil_usuario(request):
    user = request.user.id
    try:
        usuario = Alunos.objects.get(id_user=user)
    except:
        usuario = Tutores.objects.get(id_user=user)

    res = {
        'id': usuario.pk,
        'id_user': usuario.id_user,
        'nome': usuario.nome,
        'username': usuario.id_user.username,
        'email': usuario.email,
    }
    
    aluno = Alunos()
    if type(usuario) == type(aluno):
        interesses = InteresseAluno.objects.filter(id_aluno=usuario)
        res['interesses'] = InteresseAlunoSerializer(interesses, many=True).data
    else:
        especializacoes = EspecializacaoTutor.objects.filter(id_tutor=usuario)
        res['sobre'] = usuario.sobre
        res['especializacoes'] = EspecializacaoTutorSerializer(especializacoes, many=True).data
    
    return render(request, 'brotherInCode/perfil.html', {'usuario': res})


def tutorias(request):
    res = []
    tutorias = Tutoria.objects.filter(id_aluno=request.user.id) #+ Tutoria.objects.filter(id_tutor=request.user.id)
    for tutoria in tutorias:
        res.append({
            'id_tutoria': tutoria.id_tutoria,
            'tutor': tutoria.id_tutor,
            'data': tutoria.data,
            'horario': HorariosTutorSerializer(tutoria.id_horario_tutor).data,
            'area_do_conhecimento': tutoria.id_sub_area_conhecimento.nome,
            'link': tutoria.link,
        })
    
    return render(request, 'brotherInCode/tutorias.html', {'tutorias': res})

def quem_somos(request):
    return render(request, 'brotherInCode/quem somos.html')

#def login(request):
#    return render(request, 'brotherInCode/login.html')

def cadastro(request):
    return render(request, 'brotherInCode/joinUs.html')
