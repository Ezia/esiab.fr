Title: Undruidic Championship
Slug: undruidic-championship
Status: hidden

<table class="table table-hover">
    <tbody>   
        <tr>
            <th scope="row" class="text-right">Sujet</th>
            <td>Projet de jeu dans le cadre d'un cours à l'UQAC</td>
        </tr>
        <tr>
            <th scope="row" class="text-right">Déroulement</th>
            <td>Septembre à décembre 2017 (4 mois dont 4 sprints de 1 semaine)</td>
        </tr>
        <tr>
            <th scope="row" class="text-right">Rôle</th>
            <td>Développeur (réseau et gameplay)</td>
        </tr>
        <tr>
            <th scope="row" class="text-right">Outils</th>
            <td>Unreal Engine (Blueprints), Git, HuBoard, méthode Scrum</td>
        </tr>
        <tr>
            <th scope="row" class="text-right">Equipe</th>
            <td>Esia Belbachir, Maxime Brodat, Aurélien Durance</td>
        </tr>
        <tr>
            <th scope="row" class="text-right">Lien GitHub</th>
            <td>
                <a href="https://github.com/MrFouss/Undruidic-Championship">Undruidic Championship</a>
            </td>
        </tr>
    </tbody>
</table>

## Concept

*Unreal Championship* est un jeu **multijoueur** de **combat à la première personne**. Les joueurs incarnent des druides s'opposant dans la forêt de Broceliande. Le druide vainqueur est celui qui réussit à cumuler le plus de points en tuant ses adversaires dans le temps imparti.

#### Combat

Les druides ont la capacité de se rendre **invisibles** lorsqu'ils sont immobiles. Cependant, cet avantage a un coût puisque leur vie diminue quand ils l'utilisent. Pour pouvoir infliger des dégâts à leurs adversaires, des armes sont disséminées dans l'arène.

<div class="row">     
    <div class="col-12 col-lg-6 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/game_01.jpg" alt="Apparition">
        <div class="text-center">Apparition</div>
    </div>
    <div class="col-12 col-lg-6 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/disappearing_character.jpg" alt="Disparition">
        <div class="text-center">Disparition</div>
    </div>
</div>

Les druides disposent uniquement d'**armes au corps à corps** (bâton, épée et hache), ils vont donc devoir faire preuve de **ruse** afin de se rapprocher **discrètement** de leurs ennemis. De plus, les armes les plus puissantes sont disposées au centre de l'arène, là où il est plus difficile de passer sans se faire repérer.

#### Ambiance visuelle

<div class="row align-items-center">    
    <div class="col-12 col-lg-5 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/tendance - low poly.jpg" alt="Flat low poly">
        <div class="text-center">Flat low poly</div>
    </div>
    <div class="col-12 col-lg-7 py-4">
        <p>Nous avons pris la décision de <strong>fabriquer nos propres assets</strong>.</p>
        <p>
        Lors de la phase de conception, j'ai travaillé avec Maxime Brodat pour définir l'<strong>ambiance graphique</strong> que nous souhaitions. J'ai réalisé les <strong>dessins de concept</strong> et les <strong>planches de tendance</strong>, tandis que Maxime s'est occupé de réaliser les assets en 3D. Nous avons opté pour un style <strong>low-poly</strong> et des <strong>textures plates</strong> afin de simplifier le processus de création des assets.
        </p>
    </div>
</div>

##### Environnement

<div class="row align-items-center">    
    <div class="col-12 col-lg-6 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/tendance2.3.jpg" alt="Couleurs et ambiance">
        <div class="text-center">Couleurs et ambiance</div>
    </div>
     <div class="col-12 col-lg-6 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/diorama_hill.jpg" alt="Prototype d'environnement">
        <div class="text-center">Prototype d'environnement</div>
    </div>
</div>

<div class="row">    
    <div class="col-12 col-lg-6">
        <img style="width: 100%;" src="/images/undruidic-championship/broceliande_1.jpg" alt="Environnement 1">
    </div>
    <div class="col-12 col-lg-6">
        <img style="width: 100%;" src="/images/undruidic-championship/broceliande_2.jpg" alt="Environnement 2">
    </div>
</div>
<div class="text-center pb-4">Environnement dans le jeu</div>

##### HUD

<div class="row align-items-center">    
    <div class="col-12 col-lg-6 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/hud3.1.1.jpg" alt="Prototype de HUD">
        <div class="text-center">Prototype de HUD</div>
    </div>
    <div class="col-12 col-lg-6 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/scoreboard.jpg" alt="HUD dans le jeu">
        <div class="text-center">HUD dans le jeu</div>
    </div>
</div>

#### Multijoueur

<div class="row align-items-center">
    <div class="col-12 col-lg-6 py-4">
        La mise en <strong>réseau</strong> du jeu a pris une grande partie du temps de développement. J'ai travaillé sur cet aspect avec Aurélien Durance. Pour jouer, l'un des joueurs doit héberger une partie que les autres rejoignent.
    </div>    
    <div class="col-12 col-lg-6 py-4">
        <img style="width: 100%;" src="/images/undruidic-championship/lobby.jpg" alt="Lobby">
        <div class="text-center">Lobby</div>
    </div>
</div>

## Expérience

Ce projet a été riche en **nouvelles expériences** et m'a beaucoup appris, **aussi bien dans ce qui s'est bien passé que dans les problèmes que nous avons rencontrés**.

Ce projet m'a permis de mettre en pratique mes connaissances théoriques de **gestion de projet** Scrum :

* Constituer un *Game Design Document*, un *Game Concept Document* et un backlog produit
* Plannifier le développement en sprints

J'ai par ailleurs découvert le **développement sur Unreal Engine** :

* Apprendre a utiliser l'environnement de développement
* Comprendre la structure du moteur et comment l'utiliser
* Développer en Blueprints
* Développer l'aspect réseau du jeu

Nous avons aussi commis des **erreurs**, principalement de gestion de projet :

* Projet ambitieux compte tenu du temps imparti et de nos connaissances initiales, notamment la partie réseau et la création des assets
* Planification difficile et imprécise à cause d'un backlog produit mal défini
* Manque de communication au sein de l'équipe
* Réunions de sprint trop superficielles