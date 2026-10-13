const RAW = `01|Ain|ARA|Bourg-en-Bresse|Porte le nom d'un affluent du Rhône ; bordé par le Rhône et la Saône|Monastère royal de Brou ; volailles de Bresse
02|Aisne|HDF|Laon|Traversé par l'Aisne et l'Oise|Familistère de Guise ; château de Villers-Cotterêts (Cité de la langue française)
03|Allier|ARA|Moulins|Porte le nom de la rivière qui le traverse du sud au nord|Vichy, ville thermale
04|Alpes-de-Haute-Provence|PAC|Digne-les-Bains|Gorges du Verdon (rive nord) ; la Durance|Lavandes du plateau de Valensole ; citadelle de Sisteron
05|Hautes-Alpes|PAC|Gap|Massif des Écrins ; la Durance y prend sa source|Briançon, plus haute ville de France ; fortifications de Vauban
06|Alpes-Maritimes|PAC|Nice|Parc du Mercantour ; Côte d'Azur|Festival de Cannes ; entoure la principauté de Monaco
07|Ardèche|ARA|Privas|Gorges creusées par la rivière qui lui donne son nom|Pont d'Arc ; grotte Chauvet
08|Ardennes|GE|Charleville-Mézières|Méandres de la Meuse ; massif forestier frontalier de la Belgique|Château fort de Sedan ; ville natale de Rimbaud
09|Ariège|OCC|Foix|Pyrénées ; frontière avec l'Andorre|Château de Montségur (cathares) ; grotte de Niaux
10|Aube|GE|Troyes|La Seine et la rivière éponyme ; lacs de la forêt d'Orient|Capitale des magasins d'usine ; champagne de la Côte des Bar
11|Aude|OCC|Carcassonne|Fleuve côtier éponyme ; littoral méditerranéen|Cité médiévale fortifiée ; château de Peyrepertuse
12|Aveyron|OCC|Rodez|Rivières Aveyron, Lot et Tarn ; plateau de l'Aubrac|Viaduc de Millau ; fromage de Roquefort ; abbatiale de Conques
13|Bouches-du-Rhône|PAC|Marseille|Delta du Rhône : la Camargue ; les calanques|Notre-Dame-de-la-Garde ; Aix-en-Provence
14|Calvados|NOR|Caen|Côte Fleurie ; plages du Débarquement (Omaha, Juno, Sword…)|Tapisserie de Bayeux ; Deauville ; une eau-de-vie de cidre porte son nom
15|Cantal|ARA|Aurillac|Plus grand volcan d'Europe ; le puy Mary|Fromage éponyme ; viaduc de Garabit (Eiffel)
16|Charente|NAQ|Angoulême|Fleuve éponyme|Cognac ; Festival international de la bande dessinée
17|Charente-Maritime|NAQ|La Rochelle|Îles de Ré et d'Oléron ; estuaire de la Charente|Fort Boyard ; la frégate Hermione à Rochefort
18|Cher|CVL|Bourges|Rivière éponyme ; abrite le centre géographique de la France|Vignoble de Sancerre ; Printemps musical de sa préfecture
19|Corrèze|NAQ|Tulle|Plateau de Millevaches ; la Dordogne|Collonges-la-Rouge ; terre d'élection de Chirac et Hollande
2A|Corse-du-Sud|COR|Ajaccio|Aiguilles de Bavella ; falaises de Bonifacio|Maison natale de Napoléon ; îles Lavezzi|Corse du Sud
2B|Haute-Corse|COR|Bastia|Cap Corse ; Monte Cinto, point culminant de l'île|Corte, ancienne capitale de Pascal Paoli ; réserve de Scandola
21|Côte-d'Or|BFC|Dijon|Source de la Seine ; côte viticole|Hospices de Beaune ; moutarde ; site d'Alésia|Cote d'Or
22|Côtes-d'Armor|BRE|Saint-Brieuc|Côte de granit rose ; île de Bréhat|Cap Fréhel ; fort La Latte|Cotes d'Armor
23|Creuse|NAQ|Guéret|Rivière éponyme ; plateau de Millevaches|Tapisserie d'Aubusson ; l'un des départements les moins peuplés
24|Dordogne|NAQ|Périgueux|Rivière éponyme ; vallée de la Vézère|Grotte de Lascaux ; Sarlat ; foie gras du Périgord
25|Doubs|BFC|Besançon|Rivière éponyme et son saut ; frontière suisse|Comté ; usine Peugeot de Sochaux ; citadelle de Vauban
26|Drôme|ARA|Valence|Rivière éponyme ; massif du Vercors (sud)|Nougat de Montélimar ; Palais idéal du facteur Cheval
27|Eure|NOR|Évreux|Rivière éponyme ; boucles de la Seine|Jardins de Monet à Giverny ; Château-Gaillard
28|Eure-et-Loir|CVL|Chartres|Plaine de la Beauce ; deux rivières dans son nom|Cathédrale gothique célèbre pour ses vitraux bleus (UNESCO)
29|Finistère|BRE|Quimper|Pointe du Raz ; île d'Ouessant ; son nom signifie « fin de la terre »|Port militaire de Brest ; ville close de Concarneau
30|Gard|OCC|Nîmes|Les Cévennes ; Camargue gardoise ; nom tiré du Gardon|Pont du Gard ; arènes romaines
31|Haute-Garonne|OCC|Toulouse|Fleuve éponyme ; Pyrénées (Luchon)|Cité de l'espace ; Airbus ; le Capitole
32|Gers|OCC|Auch|Rivière éponyme ; cœur de la Gascogne|Armagnac ; d'Artagnan ; festival Jazz in Marciac
33|Gironde|NAQ|Bordeaux|Estuaire éponyme ; dune du Pilat ; bassin d'Arcachon|Vignoble de Saint-Émilion ; plus vaste département de métropole
34|Hérault|OCC|Montpellier|Fleuve côtier éponyme ; étang de Thau|Port de Sète ; cirque de Navacelles ; Saint-Guilhem-le-Désert
35|Ille-et-Vilaine|BRE|Rennes|Deux rivières dans son nom|Cité corsaire de Saint-Malo ; château de Fougères
36|Indre|CVL|Châteauroux|Rivière éponyme ; la Brenne et ses étangs|Maison de George Sand à Nohant
37|Indre-et-Loire|CVL|Tours|Loire, Cher et Indre s'y rejoignent|Châteaux de Chenonceau, Amboise et Villandry
38|Isère|ARA|Grenoble|Rivière éponyme ; Vercors, Chartreuse, Oisans|Station de l'Alpe d'Huez ; Jeux olympiques d'hiver de 1968
39|Jura|BFC|Lons-le-Saunier|Massif éponyme ; cascades du Hérisson|Vin jaune ; Arbois, ville de Pasteur
40|Landes|NAQ|Mont-de-Marsan|Plus grande forêt artificielle d'Europe ; l'Adour|Surf à Hossegor ; courses landaises
41|Loir-et-Cher|CVL|Blois|Deux rivières dans son nom ; la Sologne|Château de Chambord ; château de Cheverny
42|Loire|ARA|Saint-Étienne|Cours supérieur du fleuve éponyme ; monts du Forez|Club de football des « Verts » ; ancienne manufacture d'armes
43|Haute-Loire|ARA|Le Puy-en-Velay|Volcans du Velay ; gorges de l'Allier|Départ d'un chemin de Compostelle ; lentilles vertes
44|Loire-Atlantique|PDL|Nantes|Estuaire de la Loire ; marais de Brière|Château des ducs de Bretagne ; sel de Guérande
45|Loiret|CVL|Orléans|Porte le nom d'une petite rivière ; traversé par la Loire|Jeanne d'Arc libère sa préfecture en 1429 ; pont-canal de Briare
46|Lot|OCC|Cahors|Rivière éponyme ; causses du Quercy|Rocamadour ; Saint-Cirq-Lapopie ; gouffre de Padirac
47|Lot-et-Garonne|NAQ|Agen|Deux cours d'eau dans son nom|Pruneaux ; château de Nérac
48|Lozère|OCC|Mende|Mont éponyme ; gorges du Tarn ; département le moins peuplé|La Bête du Gévaudan
49|Maine-et-Loire|PDL|Angers|Confluent de la Maine et de la Loire|Abbaye de Fontevraud ; Cadre noir de Saumur
50|Manche|NOR|Saint-Lô|Mer éponyme ; presqu'île du Cotentin|Mont-Saint-Michel ; port de Cherbourg ; Utah Beach
51|Marne|GE|Châlons-en-Champagne|Rivière éponyme ; montagne de Reims|Cathédrale des sacres de Reims ; champagne d'Épernay
52|Haute-Marne|GE|Chaumont|La Marne y prend sa source ; plateau de Langres|Colombey-les-Deux-Églises (de Gaulle) ; remparts de Langres
53|Mayenne|PDL|Laval|Rivière éponyme|Cité médiévale de Sainte-Suzanne ; abbaye d'Évron
54|Meurthe-et-Moselle|GE|Nancy|Deux rivières dans son nom ; frontière belge et luxembourgeoise|Place Stanislas ; cristallerie de Baccarat
55|Meuse|GE|Bar-le-Duc|Fleuve éponyme|Champ de bataille de Verdun ; madeleines de Commercy
56|Morbihan|BRE|Vannes|Golfe éponyme ; Belle-Île ; presqu'île de Quiberon|Alignements de Carnac ; Festival interceltique de Lorient
57|Moselle|GE|Metz|Rivière éponyme ; frontières allemande et luxembourgeoise|Centre Pompidou de sa préfecture ; ligne Maginot ; faïence de Sarreguemines
58|Nièvre|BFC|Nevers|La Loire ; le Morvan|Circuit de Magny-Cours ; vin de Pouilly-Fumé
59|Nord|HDF|Lille|Frontière belge ; l'Escaut|Département le plus peuplé de France ; la Braderie de sa préfecture
60|Oise|HDF|Beauvais|Rivière éponyme|Château de Chantilly ; armistice de 1918 près de Compiègne ; château de Pierrefonds
61|Orne|NOR|Alençon|Rivière éponyme ; le Perche|Village de Camembert ; Haras national du Pin
62|Pas-de-Calais|HDF|Arras|Détroit éponyme ; caps Gris-Nez et Blanc-Nez|Louvre-Lens ; entrée du tunnel sous la Manche ; Le Touquet
63|Puy-de-Dôme|ARA|Clermont-Ferrand|Volcan éponyme ; chaîne des Puys (UNESCO) ; le Sancy|Vulcania ; siège de Michelin
64|Pyrénées-Atlantiques|NAQ|Pau|Pays basque et Béarn ; frontière espagnole côté océan|Biarritz ; jambon de Bayonne
65|Hautes-Pyrénées|OCC|Tarbes|Cirque de Gavarnie ; pic du Midi|Sanctuaire de Lourdes ; col du Tourmalet
66|Pyrénées-Orientales|OCC|Perpignan|Le Canigou ; Côte Vermeille ; Catalogne française|Collioure ; four solaire d'Odeillo ; vin de Banyuls
67|Bas-Rhin|GE|Strasbourg|Fleuve frontière avec l'Allemagne ; Vosges du Nord|Parlement européen ; château du Haut-Kœnigsbourg
68|Haut-Rhin|GE|Colmar|Fleuve frontière ; le Grand Ballon|Cité de l'automobile à Mulhouse ; route des vins d'Alsace
69|Rhône|ARA|Lyon|Confluent du Rhône et de la Saône|Basilique de Fourvière ; vignoble du Beaujolais
70|Haute-Saône|BFC|Vesoul|Rivière éponyme ; plateau des Mille Étangs|Chapelle de Ronchamp (Le Corbusier)
71|Saône-et-Loire|BFC|Mâcon|Deux cours d'eau dans son nom|Abbaye de Cluny ; communauté de Taizé ; Le Creusot
72|Sarthe|PDL|Le Mans|Rivière éponyme|Course automobile des 24 Heures ; rillettes
73|Savoie|ARA|Chambéry|Lac du Bourget ; massif de la Vanoise|Val-d'Isère, Courchevel ; JO d'Albertville 1992
74|Haute-Savoie|ARA|Annecy|Mont Blanc ; rive sud du lac Léman|Chamonix ; eaux d'Évian ; reblochon
75|Paris|IDF|Paris|Traversé par la Seine ; plus petit département de France|Tour Eiffel ; musée du Louvre
76|Seine-Maritime|NOR|Rouen|Estuaire de la Seine ; falaises d'Étretat|Port du Havre ; palais Bénédictine de Fécamp
77|Seine-et-Marne|IDF|Melun|Plus vaste département d'Île-de-France|Disneyland Paris ; château de Fontainebleau ; brie de Meaux
78|Yvelines|IDF|Versailles|Forêt de Rambouillet|Château de Louis XIV ; Saint-Germain-en-Laye
79|Deux-Sèvres|NAQ|Niort|Marais poitevin, la « Venise verte » ; deux rivières homonymes|Chabichou ; capitale des mutuelles d'assurance
80|Somme|HDF|Amiens|Baie éponyme et ses phoques|Plus vaste cathédrale gothique de France ; bataille de 1916
81|Tarn|OCC|Albi|Rivière éponyme ; Montagne Noire|Cathédrale Sainte-Cécile en brique ; Cordes-sur-Ciel
82|Tarn-et-Garonne|OCC|Montauban|Confluent du Tarn et de la Garonne|Cloître de Moissac ; chasselas
83|Var|PAC|Toulon|Massifs des Maures et de l'Estérel ; îles d'Hyères ; le fleuve qui lui a donné son nom ne le traverse plus|Saint-Tropez ; premier port militaire de France
84|Vaucluse|PAC|Avignon|Mont Ventoux ; fontaine éponyme|Palais des Papes ; Festival de théâtre ; Châteauneuf-du-Pape
85|Vendée|PDL|La Roche-sur-Yon|Îles de Noirmoutier et d'Yeu|Puy du Fou ; départ du Vendée Globe aux Sables-d'Olonne
86|Vienne|NAQ|Poitiers|Rivière éponyme|Futuroscope ; bataille de 732 (Charles Martel)
87|Haute-Vienne|NAQ|Limoges|Rivière éponyme ; monts d'Ambazac|Porcelaine ; village martyr d'Oradour-sur-Glane
88|Vosges|GE|Épinal|Massif éponyme ; la Moselle y prend sa source|Imagerie populaire ; Domrémy (Jeanne d'Arc) ; Vittel
89|Yonne|BFC|Auxerre|Rivière éponyme ; nord du Morvan|Vin de Chablis ; basilique de Vézelay ; château de Guédelon
90|Territoire de Belfort|BFC|Belfort|Ballon d'Alsace ; la « trouée » entre Vosges et Jura|Lion sculpté par Bartholdi ; festival des Eurockéennes|Belfort
91|Essonne|IDF|Évry-Courcouronnes|Rivière éponyme|Plateau de Saclay ; Génopole
92|Hauts-de-Seine|IDF|Nanterre|Boucles de la Seine, à l'ouest de Paris|Quartier d'affaires de La Défense ; manufacture de Sèvres
93|Seine-Saint-Denis|IDF|Bobigny|Canal de l'Ourcq ; au nord-est de Paris|Stade de France ; basilique, nécropole des rois de France
94|Val-de-Marne|IDF|Créteil|Confluent de la Seine et de la Marne|Marché international de Rungis ; château de Vincennes
95|Val-d'Oise|IDF|Cergy|Vallée de l'Oise ; Vexin français|Auvers-sur-Oise (Van Gogh) ; aéroport de Roissy-Charles-de-Gaulle|Val d'Oise
971|Guadeloupe|DOM|Basse-Terre|Archipel en forme de papillon ; volcan de la Soufrière|Mémorial ACTe ; Antilles françaises
972|Martinique|DOM|Fort-de-France|Montagne Pelée (éruption de 1902)|L'« île aux fleurs » ; rhum agricole AOC
973|Guyane|DOM|Cayenne|Forêt amazonienne ; fleuve Maroni|Centre spatial de Kourou ; plus vaste département de France
974|La Réunion|DOM|Saint-Denis|Piton de la Fournaise ; cirques de Mafate, Cilaos et Salazie|Océan Indien ; vanille Bourbon|Réunion
976|Mayotte|DOM|Mamoudzou|Archipel des Comores ; un immense lagon|101e département, depuis 2011 ; ylang-ylang`;