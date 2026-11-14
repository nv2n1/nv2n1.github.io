---
title: "inkscape-fr(1)"
name: "inkscape-fr"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkscape-fr/"
---

<h2>Nom</h2>
<p>Inkscape &#8211; programme d&#8217;édition <font SIZE="-1">SVG </font>(Scalable Vector Graphics).</p>
<h2>Synopsis</h2>
<p><tt>&quot;inkscape [options] [nom_de_fichier ...]&quot;</tt> </p>
<p> options: </p>
<pre> -?, --help 
 --usage 
 -V, --version
 -f, --file=NOMDEFICHIER 
 -e, --export-png=NOMDEFICHIER 
 -a, --export-area=x0:y0:x1:y1 
 -C, --export-area-page
 -D, --export-area-drawing
 --export-area-snap
 -i, --export-id=ID 
 -j, --export-id-only 
 -t, --export-use-hints
 -b, --export-background=COULEUR 
 -y, --export-background-opacity=VALEUR 
 -d, --export-dpi=DPI 
 -w, --export-width=LARGEUR 
 -h, --export-height=HAUTEUR 
 -P, --export-ps=NOMDEFICHIER
 -E, --export-eps=NOMDEFICHIER
 -A, --export-pdf=NOMDEFICHIER
 --export-pdf-version=NUMERODEVERSION
 --export-latex
 --export-ps-level {2,3}
 -T, --export-text-to-path
 --export-ignore-filters
 -l, --export-plain-svg=NOMDEFICHIER 
 -p, --print=IMPRIMANTE
 -I, --query-id=ID 
 -X, --query-x
 -Y, --query-y
 -W, --query-width
 -H, --query-height
 -S, --query-all
 -x, --extension-directory
 --verb-list
 --verb=VERB-ID
 --select=OBJECT-ID
 --shell
 -g, --with-gui 
 -z, --without-gui 
 --vacuum-defs
 --g-fatal-warnings</pre>
<h2>Description</h2>
<p><code>Inkscape</code> est un éditeur de dessin au format <code>Scalable Vector Graphics (</code><font SIZE="-1"><code>SVG</code></font><code>)</code> doté d&#8217;une interface graphique, offrant des possibilités similaires à <code>Adobe Illustrator</code>, <code>CorelDraw</code>, <code>Xara Xtreme</code>, etc. Les fonctionnalités d&#8217;Inkscape comprennent une gestion versatile des formes, le dessin à main levée et les courbes de Bézier, le texte multiligne, le texte suivant un chemin, la transparence, les transformations affines, les remplissages par motif ou dégradé, l&#8217;édition de nœuds, l&#8217;export <font SIZE="-1">SVG</font> vers <font SIZE="-1">PNG,</font> le groupement, les calques, les clones interactifs et bien plus encore. L&#8217;interface est conçue pour être confortable et efficace pour les utilisateurs expérimentés tout en restant conforme aux spécifications de <font SIZE="-1"><code>GNOME</code></font> permettant ainsi aux utilisateurs d&#8217;applications <font SIZE="-1">GNOME</font> de s&#8217;y habituer rapidement. </p>
<p> Le format <font SIZE="-1"><code>SVG</code></font> est un format <font SIZE="-1">XML</font> standard pour le dessin vectoriel 2D. Il permet de définir des objets sur un dessin par l&#8217;utilisation de points, chemins et formes primitives. Les couleurs, fontes, largeur de contour et autres sont spécifiés en tant qu&#8217;attributs de &#8216;style&#8217; de ces objets. Le but est de rendre possible l&#8217;utilisation de fichiers <font SIZE="-1">SVG</font> pour un grand nombre de programmes et d&#8217;utilisation, <font SIZE="-1">SVG</font> étant un standard et ses fichiers du type texte/xml. </p>
<p> <code>Inkscape</code> utilise le <font SIZE="-1">SVG</font> comme format natif de ses documents, et a pour but de devenir le plus conforme des programmes de dessin <font SIZE="-1">SVG,</font> disponible pour la communauté du logiciel libre.</p>
<h2>Options</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Affiche un message d&#8217;aide.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Affiche la version d&#8217;Inkscape et la date de compilation.</p>
<dt><code>-a</code> <i>x0:y0:x1:y1</i>, <code>&#8211;export-area</code>=<i>x0:y0:x1:y1</i></p>
<dd>Pour l&#8217;export en <font SIZE="-1">PNG,</font> définit la zone à exporter en pixels <font SIZE="-1">SVG </font>(unité anonyme de longueur utilisée normalement par le format <font SIZE="-1">SVG</font> Inkscape). Le comportement par défaut est d&#8217;exporter la page du document. Le point (0,0) est le coin inférieur gauche.</p>
<dt><code>-C</code>, <code>&#8211;export-area-page</code></p>
<dd>Pour l&#8217;export en <font SIZE="-1">PNG, PDF, PS</font> et <font SIZE="-1">EPS,</font> la zone exportée est la page. C&#8217;est habituellement le comportement par défaut pour les formats <font SIZE="-1">PNG, PDF</font> et <font SIZE="-1">PS,</font> aussi spécifier cette option n&#8217;est pas nécessaire pour ces formats sauf si l&#8217;option &#8211;export-id est utilisée pour exporter un objet spécifique. En <font SIZE="-1">EPS,</font> cependant, il ne s&#8217;agit pas du comportement par défaut. De plus, pour l&#8217;<font SIZE="-1">EPS,</font> la spécification du format n&#8217;autorise pas sa boîte englobante à s&#8217;étendre au-delà de son contenu, ce qui signifie que lorsque l&#8217;option &#8211;export-area-page est utilisée pour l&#8217;export <font SIZE="-1">EPS,</font> la boîte englobante de la page sera redimensionnée pour s&#8217;adapter à la boîte englobante de son contenu si elle est plus petite.</p>
<dt><code>-D</code>, <code>&#8211;export-area-drawing</code></p>
<dd>Pour l&#8217;export en <font SIZE="-1">PNG, PDF, PS</font> et <font SIZE="-1">EPS,</font> la zone à exporter est le dessin entier (pas la page), c&#8217;est à dire la boîte englobante de l&#8217;ensemble des objets du document (ou des objets exportés lorsque l&#8217;option &#8211;export-id est utilisée). Avec cette option, l&#8217;image exportée n&#8217;affichera que les objets visibles du document sans marge ni massicotage. Il s&#8217;agit de l&#8217;option par défaut pour l&#8217;export au format <font SIZE="-1">EPS.</font> Peut être combiné, lors de l&#8217;export en <font SIZE="-1">PNG,</font> avec &#8211;export-use-hints.</p>
<dt><code>&#8211;export-area-snap</code></p>
<dd>Arrondi les dimensions de la zone à exporter aux valeurs entières supérieures en unités <font SIZE="-1">SVG</font> utilisateur (px). Si vous utilisez une résolution d&#8217;export de 90 ppp et que vos objets sont alignés aux pixels afin de minimiser l&#8217;anti-crénelage, cette option permet de préserver cet alignement même si l&#8217;export se fait selon des boîtes de contour (avec &#8211;export-id ou &#8211;export-area-drawing) qui ne sont pas correctement alignées sur les pixels.</p>
<dt><code>-b</code> <i></i><font SIZE="-1"><i>COULEUR</i></font><i></i>, <code>&#8211;export-background</code>=<i></i><font SIZE="-1"><i>COULEUR</i></font><i></i></p>
<dd>Couleur de fond du <font SIZE="-1">PNG</font> exporté. Cette valeur peut être n&#8217;importe quelle chaîne de couleur supportée par le format <font SIZE="-1">SVG,</font> par exemple &#8220;#ff007f&#8221; ou &#8220;rgb(255, 0, 128)&#8221;. Si cette couleur n&#8217;est pas définie, la couleur de page définie dans Inkscape via la boîte de dialogue Préférences du document sera utilisée (enregistrée dans l&#8217;attribut pagecolor= de sodipodi:namedview).</p>
<dt><code>-d</code> <i></i><font SIZE="-1"><i>PPP</i></font><i></i>, <code>&#8211;export-dpi</code>=<i></i><font SIZE="-1"><i>PPP</i></font><i></i></p>
<dd>La résolution utilisée pour l&#8217;export en <font SIZE="-1">PNG.</font> Elle est également utilisée pour définir le niveau de rastérisation des objets filtrés lors de l&#8217;export en <font SIZE="-1">PS, EPS</font> ou <font SIZE="-1">PDF </font>(sauf si l&#8217;option &#8211;export-ignore-filters est utilisée). Elle est de 90 par défaut, correspondant à 1 pixel <font SIZE="-1">SVG </font>(px, aussi appelé « unité utilisateur ») s&#8217;exportant vers 1 pixel bitmap. Cette valeur préempte la <font SIZE="-1">PPP</font> enregistrée avec le document si la commande est utilisée avec &#8211;export-use-hints.</p>
<dt><code>-e</code> <i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i>, <code>&#8211;export-png</code>=<i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i></p>
<dd>Spécifie le nom de fichier pour l&#8217;export en <font SIZE="-1">PNG. S</font>&#8216;il existe déjà, il sera écrasé sans demande de confirmation.</p>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i>, <code>&#8211;file</code>=<i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i></p>
<dd>Ouvre le(s) document(s) spécifié(s). La chaîne d&#8217;option peut être omise, c&#8217;est à dire que vous pouvez lister les noms de fichier sans -f.</p>
<dt><code>-g</code>, <code>&#8211;with-gui</code></p>
<dd>Tente d&#8217;utiliser l&#8217;interface graphique (sous Unix, utilise le serveur X, même si <tt>$DISPLAY</tt> n&#8217;est pas défini).</p>
<dt><code>-h</code> <i></i><font SIZE="-1"><i>HAUTEUR</i></font><i></i>, <code>&#8211;export-height</code>=<i></i><font SIZE="-1"><i>HAUTEUR</i></font><i></i></p>
<dd>Hauteur du bitmap généré en pixels. Cette valeur préempte l&#8217;option &#8211;export-dpi (ou la <font SIZE="-1">PPP</font> enregistrée avec le document si &#8211;export-use-hints est aussi utilisé).</p>
<dt><code>-i</code> <i></i><font SIZE="-1"><i>ID</i></font><i></i>, <code>&#8211;export-id</code>=<i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd>Lors des exportations <font SIZE="-1">PNG, PS, EPS, PDF</font> et <font SIZE="-1">SVG</font> simple, valeur de l&#8217;attribut id de l&#8217;objet que vous voulez exporter depuis le document (aucun autre objet n&#8217;est exporté). Par défaut la zone exportée est la boîte englobante de l&#8217;objet ; vous pouvez préempter ce comportement en utilisant &#8211;export-area (pour le <font SIZE="-1">PNG</font> seulement) ou &#8211;export-area-page.</p>
<dt><code>-j</code>, <code>&#8211;export-id-only</code></p>
<dd>Pour les formats <font SIZE="-1">PNG</font> et <font SIZE="-1">SVG</font> simple, n&#8217;exporte que l&#8217;objet dont l&#8217;id est spécifiée avec avec l&#8217;option &#8211;export-id. Tout les autres objets seront cachés et n&#8217;apparaîtront pas dans le fichier exporté même s&#8217;ils chevauchent l&#8217;objet effectivement exporté. Cette option est ignorée si &#8211;export-id n&#8217;est pas aussi utilisé.</p>
<dt><code>-l</code>, <code>&#8211;export-plain-svg</code>=<i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i></p>
<dd>Exporte le(s) document(s) en <font SIZE="-1">SVG</font> brut, sans espace de nom sodipodi: ou inkscape: et sans métadonnées <font SIZE="-1">RDF.</font></p>
<dt><code>-x</code>, <code>&#8211;extension-directory</code></p>
<dd>Liste le contenu du répertoire d&#8217;extensions configuré en tant que tel par Inkscape, puis sort. Cette option est utilisée afin que les extensions externes utilisent la configuration originale générée à l&#8217;installation d&#8217;Inkscape.</p>
<dt><code>&#8211;verb-list</code></p>
<dd>Liste tous les verbes disponibles dans Inkscape par identifiant. Cet identifiant peut être utilisé pour définir les actions du clavier ou les menus. Il peut également être utilisé avec l&#8217;option de ligne de commande &#8211;verb.</p>
<dt><code>&#8211;verb</code>=<i>VERB-ID</i>, <code>&#8211;select</code>=<i>OBJECT-ID</i></p>
<dd>Ces deux options fonctionnent de concert pour offrir la possibilité d&#8217;écrire des scripts simples pour Inkscape depuis la ligne de commande. Il peuvent apparaître sur la ligne de commande aussi souvent que nécessaire et sont exécutés dans l&#8217;ordre pour tous les documents spécifiés. </p>
<p> La commande &#8211;verb exécute une action spécifique comme si elle était appelée depuis un menu ou un bouton. Un boîte de dialogue apparaît lorsqu&#8217;elle fait partie de l&#8217;action. Utilisez l&#8217;option &#8211;verb-list pour lister les identifiants d&#8217;action disponibles. </p>
<p> La commande &#8211;select sélectionne les objects correspondants à l&#8217;identifiant spécifié. Les actions suivantes ne s&#8217;appliquent alors qu&#8217;à cette sélection. Pour désélectionner tous les objets, utilisez &#8211;verb=EditDeselect. Les identifiants d&#8217;objet disponibles dépendent du document ouvert.</p>
<dt><code>-p</code> <i></i><font SIZE="-1"><i>IMPRIMANTE</i></font><i></i>, <code>&#8211;print</code>=<i></i><font SIZE="-1"><i>IMPRIMANTE</i></font><i></i></p>
<dd>Imprime le(s) document(s) vers l&#8217;imprimante spécifiée en utilisant `lpr -P <font SIZE="-1">IMPRIMANTE</font>&#8216;. Vous pouvez aussi utiliser `| <font SIZE="-1">COMMANDE</font>&#8216; pour spécifier un tube de commande différent, ou utiliser `&gt; <font SIZE="-1">NOMDEFICHIER</font>&#8216; pour écrire le résultat PostScript dans un fichier au lieu de l&#8217;imprimer. N&#8217;oubliez pas d&#8217;utiliser les guillemets appropriés pour votre shell, par exemple : </p>
<p> inkscape &#8211;print=&#8217;| ps2pdf &#8211; mondoc.pdf&#8217; mondoc.svg</p>
<dt><code>-t</code>, <code>&#8211;export-use-hints</code></p>
<dd>Utilise le nom de fichier et la <font SIZE="-1">PPP</font> enregistrés avec l&#8217;objet exporté (uniquement si &#8211;export-id est spécifié). Ces valeurs sont automatiquement spécifiées si vous exportez la sélection depuis Inkscape. Donc, si par exemple, vous exportez la forme id=&#8220;path231&#8221; en tant que /home/me/shape.png avec une résolution de 300 ppp depuis document.svg en utilisant l&#8217;interface graphique d&#8217;Inkscape, et sauvez le document, vous pourrez réexporter plus tard cette forme vers le même fichier et avec la même résolution en utilisant simplement la commande : </p>
<p> inkscape -i path231 -t document.svg </p>
<p> Si vous utilisez &#8211;export-dpi, &#8211;export-width, ou &#8211;export-height avec cette option, la <font SIZE="-1">PPP</font> enregistrée avec le document sera ignorée et la valeur fournie à la ligne de commande utilisée. Si vous utilisez &#8211;export-png avec cette option, le nom de fichier enregistré avec le document sera ignoré et le nom de fichier fourni à la ligne de commande utilisé.</p>
<dt><code>-w</code> <i></i><font SIZE="-1"><i>LARGEUR</i></font><i></i>, <code>&#8211;export-width</code>=<i></i><font SIZE="-1"><i>LARGEUR</i></font><i></i></p>
<dd>Largeur du bitmap généré en pixels. Cette valeur préempte l&#8217;option &#8211;export-dpi setting (ou la <font SIZE="-1">PPP</font> enregistrée avec le document si &#8211;export-use-hints est aussi utilisé).</p>
<dt><code>-y</code> <i></i><font SIZE="-1"><i>VALEUR</i></font><i></i>, <code>&#8211;export-background-opacity</code>=<i></i><font SIZE="-1"><i>VALEUR</i></font><i></i></p>
<dd>Opacité du fond du <font SIZE="-1">PNG</font> exporté. Cela peut être une valeur entre 0.0 et 1.0 (0.0 : complètement transparent, 1.0 complètement opaque) ou supérieure à 1 et inférieure à 255 (255 : complètement opaque). Si cette valeur n&#8217;est pas spécifiée et si l&#8217;option -b n&#8217;est pas utilisée, l&#8217;opacité de la page enregistrée avec le document (dans l&#8217;attribut inkscape:pageopacity= de sodipodi:namedview) sera utilisée. Si cette valeur n&#8217;est pas spécifiée mais que l&#8217;option -b est utilisée, la valeur 255 (opacité complète) sera utilisée.</p>
<dt><code>-P</code> <i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i>, <code>&#8211;export-ps</code>=<i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i></p>
<dd>Exporte le ou les documents au format PostScript. Notez que PostScript ne supporte pas la transparence, et que tout objet transparent dans le <font SIZE="-1">SVG</font> original sera automatiquement rastérisé. Les polices utilisés sont incorporées en tant que sous-ensemble. La zone d&#8217;exportation par défaut est la page, mais vous pouvez choisir de limiter cette zone au dessin avec l&#8217;option &#8211;export-area-drawing. Il est également possible de n&#8217;exporter qu&#8217;un objet en spécifiant &#8211;export-id (tous les autres objets sont cachés). Dans ce cas, la zone d&#8217;exportation correspond à celle de l&#8217;objet choisi, à moins que vous n&#8217;ajoutiez l&#8217;option &#8211;export-area-page pour que cette zone prenne la taille de la page.</p>
<dt><code>-E</code> <i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i>, <code>&#8211;export-eps</code>=<i></i><font SIZE="-1"><i>NOMDEFICHIER</i></font><i></i></p>
<dd>Exporte le ou les documents au format Encapsulated PostScript. Notez que PostScript ne supporte pas la transparence, et que tout objet transparent dans le <font SIZE="-1">SVG</font> original sera automatiquement rastérisé. Les polices utilisés sont incorporées en tant que sous-ensemble. La zone d&#8217;exportation par défaut est la page, mais vous pouvez choisir de limiter cette zone au dessin avec l&#8217;option &#8211;export-area-drawing. Il est également possible de n&#8217;exporter qu&#8217;un objet en spécifiant &#8211;export-id (tous les autres objets sont cachés).</p>
<dt><code>-A</code> <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>, <code>&#8211;export-pdf</code>=<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd>Exporte le ou les documents au format <font SIZE="-1">PDF.</font> Ce format préserve la transparence des objets présents dans le <font SIZE="-1">SVG</font> original. Les polices utilisés sont incorporées en tant que sous-ensemble. La zone d&#8217;exportation par défaut est la page, mais vous pouvez choisir de limiter cette zone au dessin avec l&#8217;option &#8211;export-area-drawing. Il est également possible de n&#8217;exporter qu&#8217;un objet en spécifiant &#8211;export-id (tous les autres objets sont cachés). Dans ce cas, la zone d&#8217;exportation correspond à celle de l&#8217;objet choisi, à moins que vous n&#8217;ajoutiez l&#8217;option &#8211;export-area-page pour que cette zone prenne la taille de la page.</p>
<dt><code>&#8211;export-pdf-version</code>=<i>VERSION-PDF</i></p>
<dd>Sélectionne la version <font SIZE="-1">PDF</font> utilisée pour exporter le fichier. Cette option ne fait que réutiliser le sélecteur de version <font SIZE="-1">PDF</font> présent dans la boîte de dialogue d&#8217;exportation en <font SIZE="-1">PDF</font> de l&#8217;interface graphique. Vous devez donc fournir une des versions proposées par ce sélecteur (par exemple « 1.4 ». La version par défaut est « 1.4 ».</p>
<dt><code>&#8211;export-latex</code></p>
<dd>Pour l&#8217;exportation en <font SIZE="-1">PS, EPS</font> ou <font SIZE="-1">PDF.</font> Utilisé pour créer des images pour les documents LaTeX, pour lesquels les textes sont composés par LaTeX. Lors de l&#8217;exportation <font SIZE="-1">PS, EPS</font> ou <font SIZE="-1">PDF,</font> cette option sépare la sortie en un fichier <font SIZE="-1">PS, EPS</font> ou <font SIZE="-1">PDF </font>(lorsque, par exemple, l&#8217;option &#8211;export-pdf est positionnée) et en un fichier LaTeX. Le text n&#8217;est pas enregistré dans le <font SIZE="-1">PS, EPS</font> ou <font SIZE="-1">PDF,</font> mais apparaît dans le fichier LaTex, qui lui-même inclut le <font SIZE="-1">PS, EPS</font> ou <font SIZE="-1">PDF.</font> Inclure le fichier LaTeX (\input{image.tex}) dans un document LaTeX fait alors apparaître l&#8217;image, et tout le texte composé par LaTeX. Se référer au document LaTeX généré pour de plus amples informations (voir également la sortie terminal de la commande GNUPlot `epslatex&#8217;).</p>
<dt><code>-T</code>, <code>&#8211;export-text-to-path</code></p>
<dd>Convertit les objets texte en chemins lors de l&#8217;export, si applicable (pour l&#8217;exportation en <font SIZE="-1">PS, EPS, PDF</font> ou <font SIZE="-1">SVG</font>).</p>
<dt><code>&#8211;export-ignore-filters</code></p>
<dd>Exporte les objets filtrés (avec du flou, par exemple) comme des vecteurs, en ignorant les filtres (pour l&#8217;exportation en <font SIZE="-1">PS, EPS</font> ou <font SIZE="-1">PDF</font>). Par défaut, tous les objets filtrés sont rastérisés à une définition choisie par &#8211;export-dpi (par défaut 90 ppp), en préservant son apparence.</p>
<dt><code>-I</code>, <code>&#8211;query-id</code></p>
<dd>Identifiant de l&#8217;objet dont les dimensions sont demandées. Si cette option n&#8217;est pas utilisée, la commande retournera les dimensions du dessin, pas de la page ou de la zone affichée.</p>
<dt><code>-X</code>, <code>&#8211;query-x</code></p>
<dd>Demande l&#8217;abscisse (coordonnée X) du dessin ou, si spécifié avec &#8211;query-id, de l&#8217;objet. La valeur retournée est en pixels (unité utilisateur <font SIZE="-1">SVG</font>).</p>
<dt><code>-Y</code>, <code>&#8211;query-y</code></p>
<dd>Demande l&#8217;ordonnée (coordonnée Y) du dessin ou, si spécifié avec &#8211;query-id de l&#8217;objet. La valeur retournée est en pixels (unité utilisateur <font SIZE="-1">SVG</font>).</p>
<dt><code>-W</code>, <code>&#8211;query-width</code></p>
<dd>Demande la largeur du dessin ou, si spécifié avec &#8211;query-id, de l&#8217;objet. La valeur retournée est en pixels (unité utilisateur <font SIZE="-1">SVG</font>).</p>
<dt><code>-H</code>, <code>&#8211;query-height</code></p>
<dd>Demande la hauteur du dessin ou, si spécifié avec &#8211;query-id, de l&#8217;objet. La valeur retournée est en pixels (unité utilisateur <font SIZE="-1">SVG</font>).</p>
<dt><code>-S</code>, <code>&#8211;query-all</code></p>
<dd>Affiche un liste délimitée par des virgules des tous les objets du document <font SIZE="-1">SVG</font> comprenant leur identifiant, et les valeurs x, y, largeur et hauteur.</p>
<dt><code>&#8211;shell</code></p>
<dd>Avec ce paramètre, Inkscape entre en mode de ligne de commande interactif. Dans ce mode, vous pouvez envoyer des commandes à Inkscape par le prompt, sans avoir à lancer une nouvelle instance du logiciel à chaque commande. Cette fonctionnalité est particulièrement utile pour une utilisation en scripts et en serveur. Elle permet d&#8217;améliorer la vitesse d&#8217;exécution et l&#8217;occupation en mémoire des scripts utilisés de façon répétée. Chaque commande, dans ce mode, doit contenir tous les paramètres d&#8217;une ligne de commande classique, à l&#8217;exception du nom du programme (inkscape), comme dans l&#8217;exemple suivant : &#8220;fichier.svg &#8211;export-pdf=fichier.pdf&#8221;.</p>
<dt><code>&#8211;vacuum-defs</code></p>
<dd>Supprime tous les éléments inutilisés de la section &lt;lt&gt;defs&lt;gt&gt; du fichier <font SIZE="-1">SVG.</font> Si cette option est utilisée avec &#8211;export-plain-svg, seul le fichier exporté sera affecté. Si cette option est utilisée seule, le fichier spécifié sera modifié.</p>
<dt><code>-z</code>, <code>&#8211;without-gui</code></p>
<dd>Ne lance pas l&#8217;interface graphique (sous Unix, n&#8217;utilise pas le server X) ; ne traite les fichiers que depuis la console. Ceci est présupposé pour les options -p, -e, -l et &#8211;vacuum-defs.</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd>Cette option <font SIZE="-1">GTK</font> standard force l&#8217;arrêt d&#8217;Inkscape dès qu&#8217;un message d&#8217;avertssement (généralement sans gravité) est envoyé (utilisée à des fins de déboggage).</p>
<dt><code>&#8211;usage</code></p>
<dd>Affiche un bref message sur l&#8217;utilisation d&#8217;Inkscape.</dl>
<h2>Configuration</h2>
<p>Le fichier de configuration principal est placé dans ~/.config/Inkscape/preferences.xml. Il contient plusieurs types de paramétrages dont vous pouvez changer la valeur dans Inkscape (la plupart dans la boîte de dialogue Préférences d&#8217;Inkscape). Vous pouvez ajouter des configurations spécifiques dans les sous-répertoires suivants : </p>
<p> $HOME/.config/Inkscape/extensions/ &#8211; extensions. </p>
<p> $HOME/.config/Inkscape/icons/ &#8211; icônes. </p>
<p> $HOME/.config/Inkscape/keys/ &#8211; association des touches du clavier aux commandes. </p>
<p> $HOME/.config/Inkscape/templates/ &#8211; modèles de fichiers.</p>
<h2>Diagnostics</h2>
<p>Le programme retourne la valeur zéro après une utilisation réussie ou différente de zéro après un problème. </p>
<p> Des messages d&#8217;erreur et des avertissements divers peuvent être envoyés vers <font SIZE="-1">STDERR</font> ou <font SIZE="-1">STDOUT.</font> Si le programme se comporte de façon erratique avec un fichier <font SIZE="-1">SVG</font> particulier, ou se plante, il est utile de chercher des indices dans ces messages.</p>
<h2>Exemples</h2>
<p>Bien qu&#8217;<code>Inkscape</code> soit principalement conçu comme une application graphique, il peut aussi être utilisé depuis la ligne de commande pour certaines opérations <font SIZE="-1">SVG.</font> </p>
<p> Ouvrir un fichier <font SIZE="-1">SVG</font> avec l&#8217;interface graphique : </p>
<pre> inkscape nomdefichier.svg</pre>
<p>Imprimer un fichier <font SIZE="-1">SVG :</font> </p>
<pre> inkscape nomdefichier.svg -p '| lpr'</pre>
<p>Exporter un fichier <font SIZE="-1">SVG</font> en <font SIZE="-1">PNG</font> avec la résolution par défaut de 90 ppp (un pixel bitmap correspondant à une unité utilisateur <font SIZE="-1">SVG</font>) : </p>
<pre> inkscape nomdefichier.svg --export-png=nomdefichier.png</pre>
<p>Idem, mais en forçant les dimensions du fichier à 600&#215;400 pixels : </p>
<pre> inkscape nomdefichier.svg --export-png=nomdefichier.png -w600 -h400</pre>
<p>Idem, mais en exportant le dessin (la boîte englobante de tous les objets), et pas la page : </p>
<pre> inkscape nomdefichier.svg --export-png=nomdefichier.png --export-area-drawing</pre>
<p>Exporter en <font SIZE="-1">PNG</font> l&#8217;objet id=&#8220;text1555&#8221;, en utilisant le nom de fichier et la résolution utilisés la dernière fois qu&#8217;il a été exporté depuis l&#8217;interface graphique : </p>
<pre> inkscape nomdefichier.svg --export-id=text1555 --export-use-hints</pre>
<p>Idem, mais en utilisant une résolution de 90 ppp, en spécifiant un nom de fichier et en arrondissant la zone à exporter aux valeurs entières juste supérieures en unités utilisateur <font SIZE="-1">SVG </font>(afin de préserver l&#8217;alignement des objets sur des pixels et minimiser l&#8217;anti-crénelage) : </p>
<pre> inkscape nomdefichier.svg --export-id=text1555 --export-png=text.png --export-area-snap</pre>
<p>Convertir un document du format <font SIZE="-1">SVG</font> Inkscape au format <font SIZE="-1">SVG</font> brut : </p>
<pre> inkscape nomdefichier1.svg --export-plain-svg=nomdefichier2.svg</pre>
<p>Convertir un document <font SIZE="-1">SVG</font> en <font SIZE="-1">EPS,</font> en convertissant les textes en chemins : </p>
<pre> inkscape nomdefichier.svg --export-eps=nomdefichier.eps --export-text-to-path</pre>
<p>Demander la largeur de l&#8217;objet avec un id=&#8220;text1555&#8221; : </p>
<pre> inkscape nomdefichier.svg --query-width --query-id text1555</pre>
<p>Dupliquer l&#8217;objet ayant pour identifiant id=&#8220;path1555&#8221;, puis appliquer une rotation de 90 degrés sur le duplicat, enregistrer le <font SIZE="-1">SVG</font> et quitter : </p>
<pre> inkscape nomdefichier.svg --select=path1555 --verb=EditDuplicate --verb=ObjectRotate90 --verb=FileSave --verb=FileClose</pre>
<h2>Environement</h2>
<p><font SIZE="-1"><code>DISPLAY</code></font> pour obtenir l&#8217;hôte par défaut et le numéro d&#8217;affichage. </p>
<p> <font SIZE="-1"><code>TMPDIR</code></font> pour définir le chemin par défaut du répertoire à utiliser pour stocker les fichier temporaires. Le répertoire doit exister. </p>
<p> <font SIZE="-1"><code>INKSCAPE_PROFILE_DIR</code></font> pour définir le chemin du répertoire à utiliser pour le profil utilisateur.</p>
<h2>Thèmes</h2>
<p>Vous pouvez remplacer le fichier d&#8217;icônes par défaut $PREFIX/share/inkscape/icons/icons.svg en utilisant le répertoire $HOME/.config/inkscape/icons/. Les icônes sont chargées par nom (ex. : <i>fill_none.svg</i>) ou, si elles sont introuvables, depuis le fichier <i>icons.svg</i>. Si une icône n&#8217;est pas trouvée dans l&#8217;un de ces emplacements, elle est chargée depuis l&#8217;emplacement par défaut du système. </p>
<p> Les icônes nécessaires sont chargées depuis les fichiers <font SIZE="-1">SVG</font> par recherche de l&#8217;id <font SIZE="-1">SVG</font> correspondant (Par exemple, pour charger l&#8217;icône &#8220;fill_none&#8221; depuis un fichier, le contenu identifié par l&#8217;id <font SIZE="-1">SVG </font>&#8220;fill_none&#8221; est rendu en tant que cette icône, qu&#8217;il vienne du fichier <i>fill_none.svg</i> ou du fichier <i>icons.svg</i>).</p>
<h2>Autres Informations</h2>
<p>L&#8217;endroit principal pour trouver des informations sur <code>Inkscape</code> est <a rel="nofollow" href="http://www.inkscape.org/.">http://www.inkscape.org/.</a> Le site web contient des liens vers d&#8217;autres éléments pertinents : documentation, didacticiels, manuel de l&#8217;utilisateur, exemples, archives des listes de diffusion, la dernière version d&#8217;Inkscape, les bases contenant les défauts et les demandes d&#8217;évolution, et bien d&#8217;autres choses.</p>
<h2>Voir Aussi</h2>
<p>potrace, cairo, <i><a href="/docs/linux/man/1-rsvg/">rsvg</a></i>(1), batik, ghostscript, pstoedit. </p>
<p> Suite de tests de conformité <font SIZE="-1">SVG : </font> <a rel="nofollow" href="http://www.w3.org/Graphics/SVG/Test/">http://www.w3.org/Graphics/SVG/Test/</a> </p>
<p> Validation de <font SIZE="-1">SVG : </font> <a rel="nofollow" href="http://jiggles.w3.org/svgvalidator/">http://jiggles.w3.org/svgvalidator/</a> </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.1 Specification</i> <i>W3C Recommendation 14 January 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG11/">http://www.w3.org/TR/SVG11/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.2 Specification</i> <i>W3C Working Draft 13 November 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG12/">http://www.w3.org/TR/SVG12/</a>&gt; </p>
<p> <i></i><font SIZE="-1"><i>SVG 1.1/1.2/2.0</i></font><i> Requirements</i> <i>W3C Working Draft 22 April 2002</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG2Reqs/">http://www.w3.org/TR/SVG2Reqs/</a>&gt; </p>
<p> <i>Document Object Model (</i><font SIZE="-1"><i>DOM</i></font><i>): Level 2 Core</i> <i>Arnaud Le Hors et al editors, W3C</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/DOM-Level-2-Core/">http://www.w3.org/TR/DOM-Level-2-Core/</a>&gt;</p>
<h2>Notes Sur L&#8217;Interface Graphique</h2>
<p>Pour vous familiariser avec l&#8217;utilisation de l&#8217;interface graphique d&#8217;Inkscape, consultez les didacticiels dans Aide &gt; Didacticiels. </p>
<p> Inkscape permet d&#8217;importer (Fichier &gt; Importer) la plupart des formats bitmaps <font SIZE="-1">PNG, BMP, JPG, XPM, GIF,</font> etc.), du texte brut (nécessite Perl), <font SIZE="-1">PS</font> et <font SIZE="-1">EPS </font>(nécessite Ghostscript) et les formats <font SIZE="-1">PDF</font> et <font SIZE="-1">AI </font>(documents Adobe Illustrato 9.0 ou plus récent). </p>
<p> Inkscape permet d&#8217;exporter (Fichier &gt; Exporter une image <font SIZE="-1">PNG</font>) des images <font SIZE="-1">PNG</font> 32-bits, mais aussi aux formats <font SIZE="-1">AI, PS, EPS, PDF, DXF</font> et plusieurs autres formats (via Fichier &gt; Enregistrer sous). </p>
<p> Inkscape supporte la pression et l&#8217;inclinaison du stylet d&#8217;une tablette graphique pour la largeur, la force et l&#8217;angle de plusieurs outils dont la plume calligraphique. </p>
<p> Inkscape comporte une interface graphique pour le moteur de vectorisation de bitmaps Potrace (<a rel="nofollow" href="http://potrace.sf.net)">http://potrace.sf.net)</a> qui est inclus dans Inkscape. </p>
<p> Inkscape peut utiliser des scripts externes (filtres de stdin vers stdout) représentés par des commandes dans le menu Effets. Un script peut avoir une interface graphique, sous forme de boîte de dialogue, permettant de définir différents paramètres et peut obtenir les IDs des objets sélectionnés sur lesquels agir depuis la ligne de commande. Inkscape est livré avec un assortiment d&#8217;effets écrits en Python dédiés principalement à la manipulation de chemin.</p>
<h2>Raccourcis Clavier</h2>
<p>Pour obtenir une liste complète des raccourcis clavier et souris, consultez le fichier doc/keys.html, ou utilisez la commande Clavier et souris dans le menu d&#8217;aide de l&#8217;interface graphique.</p>
<h2>Défauts</h2>
<p>Beaucoup de bugs sont connus ; veuillez s&#8217;il vous plaît consulter le site web pour vérifier ceux qui ont déjà été rapportés et pour soumettre de nouveaux problèmes. Consultez aussi la section &#8220;Known Issues&#8221; des notes de votre version (dans le fichier `<font SIZE="-1">NEWS</font>&#8216;).</p>
<h2>Auteurs</h2>
<p>Ce code doit son existence à un grand nombre de contributeurs tout au long de ses différentes incarnations. La liste qui suit est certainement incomplète mais permet de reconnaître les nombreuses épaules sur lesquelles cette application s&#8217;est appuyée : </p>
<p> Maximilian Albert, Joshua A. Andler, Tavmjong Bah, Pierre Barbry-Blot, Jean-François Barraud, Campbell Barton, Bill Baxter, John Beard, John Bintz, Arpad Biro, Nicholas Bishop, Joshua L. Blocher, Hanno Böck, Tomasz Boczkowski, Henrik Bohre, Boldewyn, Daniel Borgmann, Bastien Bouclet, Hans Breuer, Gustav Broberg, Christopher Brown, Marcus Brubaker, Luca Bruno, Nicu Buculei, Bulia Byak, Pierre Caclin, Ian Caldwell, Gail Carmichael, Ed Catmur, Chema Celorio, Jabiertxo Arraiza Cenoz, Johan Ceuppens, Zbigniew Chyla, Alexander Clausen, John Cliff, Kees Cook, Ben Cromwell, Robert Crosbie, Jon Cruz, Aurélie De-Cooman, Kris De Gussem, Milosz Derezynski, Daniel Díaz, Bruno Dilly, Larry Doolittle, Nicolas Dufour, Tim Dwyer, Maxim V. Dziumanenko, Johan Engelen, Miklos Erdelyi, Ulf Erikson, Noé Falzon, Frank Felfe, Andrew Fitzsimon, Edward Flick, Marcin Floryan, Fred, Ben Fowler, Cedric Gemy, Steren Giannini, Olivier Gondouin, Ted Gould, Toine de Greef, Michael Grosberg, Bryce Harrington, Dale Harvey, Aurélio Adnauer Heckert, Carl Hetherington, Jos Hirth, Hannes Hochreiner, Thomas Holder, Joel Holdsworth, Christoffer Holmstedt, Alan Horkan, Karl Ove Hufthammer, Richard Hughes, Nathan Hurst, inductiveload, Thomas Ingham, Jean-Olivier Irisson, Bob Jamison, Ted Janeczko, jEsuSdA, Lauris Kaplinski, Lynn Kerby, Niko Kiirala, James Kilfiger, Nikita Kitaev, Jason Kivlighn, Adrian Knoth, Krzysztof Kosiński, Petr Kovar, Benoît Lavorata, Alex Leone, Julien Leray, Raph Levien, Diederik van Lierop, Nicklas Lindgren, Vitaly Lipatov, Ivan Louette, Fernando Lucchesi Bastos Jurema, Pierre-Antoine Marc, Aurel-Aimé Marmion, Colin Marquardt, Craig Marshall, Ivan Masár, Dmitry G. Mastrukov, David Mathog, Matiphas, Michael Meeks, Federico Mena, MenTaLguY, Aubanel Monnier, Vincent Montagne, Tim Mooney, Derek P. Moore, Chris Morgan, Peter Moulder, Jörg Müller, Yukihiro Nakai, Victor Navez, Christian Neumair, Nick, Andreas Nilsson, Mitsuru Oka, Vinícius dos Santos Oliveira, Martin Owens, Alvin Penner, Matthew Petroff, Jon Phillips, Zdenko Podobny, Alexandre Prokoudine, Jean-René Reinhard, Alexey Remizov, Frederic Rodrigo, Hugo Rodrigues, Juarez Rudsatz, Xavier Conde Rueda, Felipe Corrêa da Silva Sanches, Christian Schaller, Marco Scholten, Tom von Schwerdtner, Danilo Šegan, Abhishek Sharma, Shivaken, Michael Sloan, John Smith, Boštjan Špetič, Aaron Spike, Kaushik Sridharan, Ralf Stephan, Dariusz Stojek, Martin Sucha, ~suv, Pat Suwalski, Adib Taraben, Hugh Tebby, Jonas Termeau, David Turner, Andre Twupack, Aleksandar Urošević, Alex Valavanis, Joakim Verona, Lucas Vieites, Daniel Wagenaar, Liam P. White, Sebastian Wüst, Michael Wybrow, Gellule Xg, Daniel Yacob, David Yip, Masatake Yamato </p>
<p> Cette page de manuel a été créée par Bryce Harrington &lt;brycehar [at] bryceharrington.org&gt;.</p>
<h2>Historique</h2>
<p>Le code qui allait devenir Inkscape est né en 1999, avec le programme Gill, <font SIZE="-1">GNOME</font> Illustrator, créé par Raph Levien. L&#8217;objectif défini pour Gill était de supporter complètement le format <font SIZE="-1">SVG.</font> Raph a codé le modèle Postcript de courbes de Bézier, incluant le remplissage et le contour, les coiffes et raccords de lignes, le texte, etc. La page de Raph consacrée à Gill se trouve sur <a rel="nofollow" href="http://www.levien.com/svg/.">http://www.levien.com/svg/.</a> Le travail sur Gill semble avoir diminué ou s&#8217;être arrêté en 2000. </p>
<p> L&#8217;incarnation suivante du code allait devenir le très populaire Sodipodi, mené par Lauris Kaplinski. Le code est devenu un outil d&#8217;illustration puissant après plusieurs années de travail, ajoutant plusieurs nouvelles fonctionnalités, le support multilingue, le portage sous Windows et d&#8217;autres systèmes d&#8217;exploitation et éliminant certaines dépendances. </p>
<p> Inkscape a été lancé en 2003 par quatre développeurs actifs de Sodipodi (Bryce Harrington, MenTaLguY, Nathan Hurst et Ted Gould), qui voulaient faire prendre une orientation différente au code en termes de focalisation sur la conformité <font SIZE="-1">SVG,</font> aspect et fonctionnement de l&#8217;interface, et d&#8217;opportunités de développement ouvertes à plus de participants. Le projet a progressé rapidement, gagnant de nombreux contributeurs et une multitude de fonctionnalités. </p>
<p> Beaucoup de travail a été depuis consacré à la stabilisation du code et à l&#8217;internationalisation. Le moteur de rendu hérité de Sodipodi comportait de nombreuses spécificités qui entrainaient de plantages lorsque l&#8217;utilisation du programme sortait des sentiers battus. Ce moteur a alors été remplacé par Livarot qui, bien qu&#8217;imparfait, générait moins d&#8217;erreurs. Le projet a également adopté la bonne habitude de publier son code régulièrement, et encouragé les utilisateurs à tester des versions en développement du logiciel, ce qui a bien aidé dans l&#8217;identification des nouveaux défauts, et donné les moyens aux utilisateurs de vérifier que les anciens étaient bien corrigés. Inkscape a ainsi acquis une réputation de programme robuste et fiable. </p>
<p> En parallèle, des efforts ont été faits pour améliorer l&#8217;internationalisation et la localisation de l&#8217;interface, ce qui a apporté au projet de nouveaux contributeurs tout autour du monde. </p>
<p> Inkscape a eu un impact positif sur l&#8217;attractivité visuelle de l&#8217;Open Source en général, en offrant un outil pour créer et partager des icônes, écrans d&#8217;accueil, art pour le web, etc. D&#8217;une certaine façon, bien que n&#8217;étant qu&#8217;un &#8220;simple outil de dessin&#8221;, Inkscape a joué un rôle important en rendant l&#8217;Open Source plus stimulant visuellement parlant pour un plus large public.</p>
<h2>Copyright Et License</h2>
<p><code>Copyright (C)</code> 1999-2011 des auteurs. </p>
<p> <code>Inkscape</code> est un logiciel libre; vous pouvez le redistribuer et/ou le modifier selon les termes de la license <font SIZE="-1">GPL. </font></p>
