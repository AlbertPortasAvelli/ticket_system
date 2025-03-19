from django.shortcuts import render
from django.http import JsonResponse
from .models import Ticket

def ticket_list(request):
    
    tickets= list(Ticket.objects.values())
    return JsonResponse({'tickets': tickets})


def ticket_detail(request, id):
    
    try:
        ticket= Ticket.objects.get(id=id)
        return JsonResponse({'ticket': ticket})
    except Ticket.DoesNotExist:
        return JsonResponse({'error': 'Ticket not found'}, status=404)

def create_ticket(request):
    if request.method == "POST":
        return JsonResponse({'message': 'Ticket created successfully'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)