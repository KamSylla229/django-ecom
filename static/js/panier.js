var	produitBtns	=	document.getElementsByClassName('update-panier');
for	(var	i	=	0;	i	<	produitBtns.length;	i++){
    produitBtns[i].addEventListener('click',	function(){

        var	produitId	=	this.dataset.produit;

        var	action	=	this.dataset.action;

        if (user=="AnymousUser"){
            console.log("L'utilisateur n'est pas authentifié")
        }else{
            console.log("produit",	produitId,	"avction",	action);
        }

    })
}