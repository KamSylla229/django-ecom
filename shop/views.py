from django.shortcuts import render
from  .models import *
from django.http import JsonResponse

# Create your views here.

def shop(request, *args,**kwargs):
    """Vue principale"""
    produits = Produit.objects.all()
    context = {
        "produits": produits
    }

    return render(request, 'shop/index.html', context)


def  panier(request, *args, **kwargs):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(client=client, complete=False)
        article=commande.commandearticle_set.all()
    else:
        artciles = []
        commande ={
            'get_panier_total':0,
            'get_panier_article':0
        }

    context= {
        'articles': articles,
        'commande': commande
    }

    return render(request, 'shop/panier.html', context)

def commande(request, *args, **kwargs):
    if request.user.is_authenticated:
        client = request.user.client
        commande, created = Commande.objects.get_or_create(client=client, complete=False)
        article=commande.commandearticle_set.all()
    else:
        artciles = []
        commande ={
            'get_panier_total':0,
            'get_panier_article':0
        }

    context= {
        'articles': articles,
        'commande': commande
    }

    return render(request, 'shop/commande.html', context)

def update_article(request, *args, **kwargs):
    return JsonResponse("produit modifier", safe=False)


