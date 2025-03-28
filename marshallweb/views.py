from django.shortcuts import render
from datetime import datetime

# Create your views here.

today = datetime.now().strftime('%A').lower()


def index(request):
    return render(request, 'index.html', {
    'title': "Marshall's",   
    'today': today,
    
    })
   
   
def nightclubs(request):
    return render(request, 'nightclubs.html', {
    'title': 'Nightclubs',   
    })
    
      
def date(request, day):
    day.lower()
    
    return render(request, 'date.html', {
    'title': f'EVENTS ON {day.upper()}S',   
    'day': day
    })
    

def contact(request):
    return render(request, 'contact.html', {
    'title': 'Contact us',   
    })


def photos(request):
    return render(request, 'photos.html', {
    'title': 'Photos',   
    })
    
   
def pacha(request):
    parties = {
        'monday': 'VIBRA @ Main Room\nReggaeton | Afrobeat | Hip-Hop | R&B',
        'tuesday': 'FLIRT TUESDAY @ Main Room\nHip Hop | Reggaeton | Afrobeat | R&B',
        'wednesday': 'FULL PARTY @ Main Room\nHip Hop | Reggaeton | Afrobeat | R&B',
        'thursday': 'BAE @ Main Room\nReggaeton | Trap | Top Hits | Hip Hop',
        'friday': '''MOULAGA @ Main Room\nTop Hits | Reggaeton | R&B\n

                    EROS @ Red Room\n
                    Techno | Tech House''',
        'saturday': '''PEGAO @ Main Room\n
                    R&B | Hip Hop | Afrobeat | Reggaeton\n

                    SINNER @ Red Room\n
                    Techno | Tech House''',
        'sunday': '''SIGHT @ Main Room\n
                    Techno | Tech House | House\n

                    D’LOCOS @ Red Room \n 
                    Reggaeton | Hits'''
    }

    party_today = parties.get(today, "There are no events scheduled for today")
    return render(request, 'discos/pacha.html', {
    'title': 'Pacha',
    'party_today': party_today,   
   
                  
    })    

def otto(request):
    parties = {
        'thursday': 'PURO PERREO\nReggaeton | Trap | Dembow',
        'friday': 'BLACK DRAGON\nHip Hop | Open format | Hits',
        'saturday': 'PURE SHÔKO\nDJ PAPIS - DJ OUMAR',
        
    }

    party_today = parties.get(today, "There are no events scheduled for today")
    return render(request, 'discos/otto.html', {
    'title': 'Otto',
    'party_today': party_today,   
   
                  
    })    

def opium(request):
    parties = {
        'monday': 'BLACKOUT MONDAYS\nEDM | House ',
        'tuesday': 'LADIES NIGHT\nTop Hits | Reggaeton',
        'wednesday': 'EUPHORIA\nLatin | Reggaeton',
        'thursday': 'JET LAG\nTop Hits',
        'friday': 'ADDICTED\nTop Hits',
        'saturday': 'JUST OPIUM\nTop Hits',
        'sunday': 'MANDRAKE\nTop Hits | Reggaeton',
    }
    
    party_today = parties.get(today, "There are no events scheduled for today")
    return render(request, 'discos/opium.html', {
    'title': 'Opium',
    'party_today': party_today, 
                  
    })    

def downtown(request):
    parties = {
        'thursday': 'Thursdays Downtown\nTop Hits | Reggaeton',
        'friday': 'Fridays Downtown\nTop Hits | Reggaeton',
        'saturday': 'Saturdays Downtown\nTop Hits | Reggaeton',
        
    }

    party_today = parties.get(today, "There are no events scheduled for today")
    return render(request, 'discos/downtown.html', {
    'title': 'Downtown',
    'party_today': party_today,   
   
                  
    })    

def biblio(request):
    parties = {
        'thursday': 'Thursdays La Biblio\nTop Hits | Reggaeton',
        'friday': 'Thursdays La Biblio\nTop Hits | Reggaeton',
        'saturday': 'Thursdays La Biblio\nTop Hits | Reggaeton',
    }

    party_today = parties.get(today, "There are no events scheduled for today")
    return render(request, 'discos/biblio.html', {
    'title': 'La Biblio',
    'party_today': party_today,   
   
                  
    })    


def cookies(request):
    return render(request, 'cookies.html')