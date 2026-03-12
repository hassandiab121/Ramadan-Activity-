from datetime import date

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from recieveActivities.forms import JoinActivityForm
from recieveActivities.models import Activity, ActivityParticipant
from recieveActivities.utils import encrypt_phone, decrypt_phone

def show_activities(request):
    activities = Activity.objects.all().order_by('Ramdan_day')
    return render(request, 'show_activities.html', {'activities': activities})


def activity_detail(request, id):
    activity = get_object_or_404(Activity, id=id)
    return render(request, 'activity_detail.html', {'activity': activity})


def join_activity(request, id):
    activity = get_object_or_404(Activity, id=id)

    if request.method == 'POST':
        form = JoinActivityForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            encrypted_phone = encrypt_phone(phone)
            ActivityParticipant.objects.create(activity=activity, phone=encrypted_phone)
            messages.success(request, 'تم تسجيل رقم الواتساب في هذا النشاط بنجاح! وسيتم تذكيرك قبل موعد النشاط ب 24 ساعة')
            return redirect('join_activity', id=activity.id)
    else:
        form = JoinActivityForm()

    return render(
        request,
        'join_activity.html',
        {
            'activity': activity,
            'form': form,
        },
    )


@require_GET
def activities_by_date_json(request):
    """
    Return JSON with activities and participant phone numbers for a given date.
    Expects ?date=YYYY-MM-DD in the query string.
    """
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse(
            {'detail': 'date query parameter is required (YYYY-MM-DD)'},
            status=400,
        )

    try:
        filter_date = date.fromisoformat(date_str)
    except ValueError:
        return JsonResponse(
            {'detail': 'Invalid date format, use YYYY-MM-DD'},
            status=400,
        )

    activities = (
        Activity.objects.filter(date=filter_date)
        .prefetch_related('participants')
        .order_by('Ramdan_day')
    )

    payload = []
    for activity in activities:
        participants_data = []
        for participant in activity.participants.all():
            try:
                phone = decrypt_phone(participant.phone)
            except Exception:
                phone = None

            participants_data.append({'phone': phone})

        payload.append(
            {
                'id': activity.id,
                'name': activity.name,
                'description': activity.description,
                'location': activity.location,
                'date': activity.date.isoformat(),
                'ramadan_day': activity.Ramdan_day,
                'participants': participants_data,
            }
        )

    return JsonResponse(
        {'date': filter_date.isoformat(), 'activities': payload},
        json_dumps_params={'ensure_ascii': False},
    )

def custom_404_error(request, exception):
    messages.success(request, "النشاط الذى تطلبه إنتهى بالفعل")
    return render(request, 'error_404.html')
