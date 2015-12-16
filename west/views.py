from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from west.models import Character, CharacterForm



def staff(request):
    staff_list = Character.objects.all()
    print(staff_list)
    # staff_str = map(str,staff_list)
    # context ={'label': ' '.join(staff_str)}
    # return HttpResponse("" + ' '.join(staff_str) + "")
    # return render(request, 'templay.html', context)
    return render(request, 'templay.html', {'staffs': staff_list, 'label': 'Label'})

def first_page(request):
    return HttpResponse("Hello West")


def templay(request):
    context = {}
    context['label'] = 'hello django'
    return render(request, 'templay.html',context)


def form(request):
    return render(request, 'form.html')

def investigate(request):
    if request.POST:
        submitted = request.POST['staff']
        new_record = Character(name=submitted)
        new_record.save()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff']=all_records
    return render(request, "investigate.html", ctx)


def investigate_form(request):
    if request.POST:
        form = CharacterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            submitted = form.cleaned_data['name']
            new_record=Character(name=submitted)
            print('save %s' % submitted)
            new_record.save()
    form = CharacterForm()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form'] =  form
    return render(request, "investigate_form.html", ctx)
