---
title: "inkscape-sk(1)"
name: "inkscape-sk"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkscape-sk/"
description: "Inkscape – editor SVG (Scalable Vector Graphics)."
---

<p>Inkscape &#8211; editor SVG (Scalable Vector Graphics). </p>
<h2>Synopsis</h2>
<p><tt>&quot;inkscape [voľby] [názov súboru ...]&quot;</tt> </p>
<p> voľby: </p>
<pre> -?, --help 
 --usage 
 -V, --version
 -f, --file=NÁZOVSÚBORU 
 -e, --export-png=NÁZOVSÚBORU 
 -a, --export-area=x0:y0:x1:y1 
 -C, --export-area-canvas
 -D, --export-area-drawing
 --export-area-snap
 -i, --export-id=ID 
 -j, --export-id-only 
 -t, --export-use-hints
 -b, --export-background=FARBA 
 -y, --export-background-opacity=HODNOTA 
 -d, --export-dpi=DPI 
 -w, --export-width=ŠÍRKA 
 -h, --export-height=VÝŠKA 
 -P, --export-ps=NÁZOVSÚBORU
 -E, --export-eps=NÁZOVSÚBORU
 -A, --export-pdf=NÁZOVSÚBORU
 -T, --export-text-to-path
 --export-bbox-page 
 -l, --export-plain-svg=NÁZOVSÚBORU 
 -p, --print=PRINTER
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
<h2>Opis</h2>
<p><code>Inkscape</code> je editor súborov vektorovej grafiky vo formáte <code>Scalable Vector Graphics (</code><font SIZE="-1"><code>SVG</code></font><code>)</code> s grafickým rozhraním, ktorého schopnosti sú podobné <code>Adobe Illustrator</code>, <code>CorelDraw</code>, <code>Xara Xtreme</code>, atď. Medzi vlastnosti Inkscape patria všestranné tvary, bézierove krivky, kreslenie voľbou rukou, viacriadkový text, text na ceste, alpha blending, ľubovoľné afínne transformácie, farebné prechody a výplň vzorkou, úprava uzlov, mnohé formáty na export a import vrátane <font SIZE="-1">PNG</font> a <font SIZE="-1">PDF,</font> zoskupovanie, vrstvy, živé klony a veľa iného. Rozhranie je navrhnuté pre komfortné a efektívne ovládanie pre skúseného používateľa, pričom dodržiava štandardy <font SIZE="-1"><code>GNOME</code></font>, takže používateľ oboznámený s inými aplikáciami <font SIZE="-1">GNOME</font> si môže ovládanie rozhrania rýchlo osvojiť. </p>
<p> <font SIZE="-1"><code>SVG</code></font> je štandardný W3C <font SIZE="-1">XML</font> formát pre dvojrozmernú vektorovú grafiku. Umožňuje definíciu objektov kresby pomocou bodov, ciest a primitívnych tvarov. Farby, písma, šírka ťahu atď sa pri týchto objektoch uvádzajú ako atribúty „štýlu“. Zámer je taký, že keďže <font SIZE="-1">SVG</font> je štandard a jeho súbory sú text/xml, bude možné použiť <font SIZE="-1">SVG</font> súbory vo veľkom počte programov v širokom spektre aplikácií. </p>
<p> <code>Inkscape</code> používa <font SIZE="-1">SVG</font> ako svoj natívny formát dokumentu a jeho cieľom je stať sa kresliacim programom plne konformným <font SIZE="-1">SVG</font> súborom, dostupným open source komunite.</p>
<h2>Voľby</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Zobrazí správu s pomocou</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Zobrazí verziu a dátum zostavenia Inkscape.</p>
<dt><code>-a</code> <i>x0:y0:x1:y1</i>, <code>&#8211;export-area</code>=<i>x0:y0:x1:y1</i></p>
<dd>Pri exporte <font SIZE="-1">PNG,</font> nastaví exportovanú oblasť v používateľských jednotkách <font SIZE="-1">SVG </font>(anonymné jednotky dĺžky bežne používané v Inkscape <font SIZE="-1">SVG</font>). Štandardne sa exportuje celé kresliace plátno dokumentu. Bod (0,0) je spodný dolný roh.</p>
<dt><code>-C</code>, <code>&#8211;export-area-canvas</code></p>
<dd>Pri exporte <font SIZE="-1">NG, PDF, PS</font> a <font SIZE="-1">EPS</font> je exportovaná oblasť celé kresliace plátno dokumentu (stránka). Toto je štandardné nastavenie pre <font SIZE="-1">PNG, PDF</font> a <font SIZE="-1">PS,</font> takže ju nemusíte uvádzať ak nepoužívate &#8211;export-id na exportovanie konkrétneho objektu. Pri exporte <font SIZE="-1">EPS</font> to však nie je štandardné nastavenie. Naviac pri <font SIZE="-1">EPS</font> neumožňuje špecifikácia formátu aby bolo ohraničenie väčšie ako obsah dokumentu. To znamená, že ak pri exporte <font SIZE="-1">EPS</font> použijete &#8211;export-area-canvas, ohraničenie plátna sa oreže dnu na ohraničenie objektu ak je menšie.</p>
<dt><code>-D</code>, <code>&#8211;export-area-drawing</code></p>
<dd>Pri exporte <font SIZE="-1">PNG, PDF, PS</font> a <font SIZE="-1">EPS</font> je exportovaná oblasť celá kresba (nie plátno), t.j. ohraničenie všetkých objektov dokumentu (alebo exportovaného objektu ak je použité &#8211;export-id). S touto voľbou budú na exportovanom obrázku iba viditeľné objekty dokumentu bez okrajov alebo orezania. Toto je štandardná exportná oblasť pre <font SIZE="-1">EPS.</font> Pri <font SIZE="-1">PNG</font> je možné použiť túto voľbu v kombinácii s &#8211;export-use-hints.</p>
<dt><code>&#8211;export-area-snap</code></p>
<dd>Pri exporte png prichytí oblasť exportu smerom von na najbližšiu celočíselnú používateľskú jednotku <font SIZE="-1">SVG </font>(px). Ak používate štandardné rozlíšenie na export 90 dpi a vaša grafika je zarovnaná na pixle aby sa minimalizoval antialiasing, tento prepínač vám umožní zachovať toto zarovnanie aj ak exportujete ohraničenie nejakého objektu (pmocou &#8211;export-id alebo &#8211;export-area-drawing), ktoré samotné nie je zarovnané na pixle.</p>
<dt><code>-b</code> <i></i><font SIZE="-1"><i>FARBA</i></font><i></i>, <code>&#8211;export-background</code>=<i></i><font SIZE="-1"><i>FARBA</i></font><i></i></p>
<dd>Farba pozadia exportovaného <font SIZE="-1">PNG.</font> Toto môže byť akýkoľvek reťazec špecifikujúci farbu, ktorý <font SIZE="-1">SVG</font> podporuje, napr. „#ff007f“ alebo „rgb(255, 0, 128)“. Ak nie je nastavená, použije sa farba nastavená v Inkscape v dialógu Možnosti dokumentu (uložená v atribúte pagecolor= v sodipodi:namedview).</p>
<dt><code>-d</code> <i></i><font SIZE="-1"><i>DPI</i></font><i></i>, <code>&#8211;export-dpi</code>=<i></i><font SIZE="-1"><i>DPI</i></font><i></i></p>
<dd>Použité rozlíšenie na export <font SIZE="-1">PNG.</font> Tiež sa používa pri rasterizácii filtrovaných objektov pri exporte do <font SIZE="-1">PS, EPS</font> a <font SIZE="-1">PDF </font>(ak neuvediete &#8211;export-ignore-filters na potlačenie rasterizácie). Štandardne 90, čo zodpovedá 1 používateľskej jednotke <font SIZE="-1">SVG. </font>(px, tiež nazývaná „používateľská jednotka“) exportovanej na 1 pixel bitmapy. Táto hodnota má precedenciu pred odporúčaným <font SIZE="-1">DPI</font> pri použití s prepínačom &#8211;export-use-hints.</p>
<dt><code>-e</code> <i>NÁZOVSÚBORU</i>, <code>&#8211;export-png</code>=<i>NÁZOVSÚBORU</i></p>
<dd>Názov súboru pre export <font SIZE="-1">PNG.</font> Ak už existuje, bude prepísaní bez pýtania sa.</p>
<dt><code>-f</code> <i>NÁZOVSÚBORU</i>, <code>&#8211;file</code>=<i>NÁZOVSÚBORU</i></p>
<dd>Otvorí zadané dokumenty. Je možné vynechať reťazec voľby, t.j. môžete uviesť zoznam súborov bez -f.</p>
<dt><code>-g</code>, <code>&#8211;with-gui</code></p>
<dd>Pokúsiť sa použiť <font SIZE="-1">GUI </font>(na unixových systémoch, použiť X server aj keď nie je nastavená premenná <tt>$DISPLAY</tt>).</p>
<dt><code>-h</code> <i>VÝŠKA</i>, <code>&#8211;export-height</code>=<i>VÝŠKA</i></p>
<dd>Výška generovaných bitmáp v pixloch. Táto hodnota má precedenciu pred nastavením &#8211;export-dpi (alebo odporúčaním <font SIZE="-1">DPI</font> pri použití s prepínačom &#8211;export-use-hints).</p>
<dt><code>-i</code> <i></i><font SIZE="-1"><i>ID</i></font><i></i>, <code>&#8211;export-id</code>=<i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd>Pri exporte <font SIZE="-1">PNG, PS, EPS</font> a <font SIZE="-1">PDF</font> hodnota atribútu id objektu, ktorý chcete exportovať z dokumentu. Žiadne iné objekty sa neexportujú. Štandardne sa exportuje ohraničenie objektu. To môžete zmeniť použitím voľby &#8211;export-area (iba pri <font SIZE="-1">PNG</font>) alebo &#8211;export-area-canvas.</p>
<dt><code>-j</code>, <code>&#8211;export-id-only</code></p>
<dd>Exportovať do <font SIZE="-1">PNG</font> iba objekt s id zadaným v &#8211;export-id. Všetky ostatné objekty sa skryjú a nezobrazia sa v exporte ani keď prekrývajú exportovaný objekt. Ak nie je uvedené &#8211;export-id, táto voľba sa ignoruje. Pri exporte <font SIZE="-1">PDF</font> je toto štandardná voľba, takže jej uvedenie nemá žiadny vplyv.</p>
<dt><code>-l</code>, <code>&#8211;export-plain-svg</code>=<i>NÁZOVSÚBORU</i></p>
<dd>Exportovať dokumenty do formátu čisté <font SIZE="-1">SVG,</font> bez menných priestorov sodipodi: alebo inkscape: namespaces a bez metadát <font SIZE="-1">RDF.</font></p>
<dt><code>-x</code>, <code>&#8211;extension-directory</code></p>
<dd>Vypíše aktuálny adresár rozšírení, ktorý bol nastavený pre Inkscape a potom skončí. Využívajú to externé rozšírenia aby použili rovnakú konfiguráciu ako pôvodná inštalácia Inkscape.</p>
<dt><code>&#8211;verb-list</code></p>
<dd>Vypíše všetky slovesá dostupné v Inkscape podľa <font SIZE="-1">ID.</font> Tieto <font SIZE="-1">ID</font> možno použiť pri definovaní klávesových máp alebo menu. Tiež ich možno použiť na príkazovom riadku s voľbou &#8211;verb.</p>
<dt><code>&#8211;verb</code>=<i>VERB-ID</i>, <code>&#8211;select</code>=<i>OBJECT-ID</i></p>
<dd>Tieto dve voľby spolu poskytujú základné možnosti skriptovania v Inkscape z príkazového riadka. Obe sa môžu na príkazovom riadku vyskytovať ľubovoľný počet krát a vykonajú sa v tomto poradí na každom určenom dokumente. </p>
<p> Príkaz &#8211;verb vykoná uvedené sloveso ako keby bolo zavolané z menu alebo klávesovou skratkou. Dialógy sa objavia ak sú súčasťou slovesa. Ak chcete vypísať zoznam dostupných <font SIZE="-1">ID,</font> použite voľby príkazového riadka &#8211;verb-list. </p>
<p> Príkaz &#8211;select spôsobí výber objektov s uvedeným <font SIZE="-1">ID.</font> To umožňuje vykonávanie slovies na nich. Ak chcete zrušiť všetky výbery, použite &#8211;verb=EditDeselect. <font SIZE="-1">ID</font> objektov sú dostupné v závislosti na dokumente, ktorý sa má načítať.</p>
<dt><code>-p</code> <i>TLAČIAREŇ</i>, <code>&#8211;print</code>=<i>TLAČIAREŇ</i></p>
<dd>Vytlačí dokumenty na určenej tlačiarni pomocou „lpr -P TLAČIAREŇ“. Ak chcete výstup poslať rúrou inému príkazu, môžete použiť „| PRÍKAZ“ alebo „&gt; NÁZOVSÚBORU“ ak chcete namiesto tlačenia zapísať výstup v PostScripte do súboru. Pamätajte na to, že musíte použiť vhodné úvodzovky pre váš shell, napr. </p>
<p> inkscape &#8211;print=&#8217;| ps2pdf &#8211; mydoc.pdf&#8217; mydoc.svg</p>
<dt><code>-t</code>, <code>&#8211;export-use-hints</code></p>
<dd>Použiť názov exportovaného súboru a atribút <font SIZE="-1">DPI</font> uložené v exportovanom objekte (iba s voľbou &#8211;export-id). Tieto údaje sa nastavujú automaticky keď exportujete výber z grafického rozhrania Inkscape. Takže napr. ak exportujete útvar s id=&#8220;path231&#8221; ako /home/me/shape.png pri 300 dpi z dokument.svg z grafického rozhrania Inkscape a uložíte dokument, neskôr budete môcť exportovať útvar do rovnakého súboru s rovnakým rozlíšením jednoducho spustením </p>
<p> inkscape -i path231 -t document.svg </p>
<p> Ak spolu s touto voľbou použijete &#8211;export-dpi, &#8211;export-width alebo &#8211;export-height bude sa atribút <font SIZE="-1">DPI</font> ignorovať a použije sa hodnota zadaná na príkazovom riadku. Ak spolu s touto voľbou použijete &#8211;export-png, bude sa atribút názvov súboru ignorovať a použije sa hodnota zadaná na príkazovom riadku.</p>
<dt><code>-w</code> <i>ŠÍRKA</i>, <code>&#8211;export-width</code>=<i>ŠÍRKA</i></p>
<dd>Výška generovaných bitmáp v pixeloch. Táto hodnota má precedenciu pred nastavením &#8211;export-dpi (alebo odporúčaním <font SIZE="-1">DPI</font> pri použití s prepínačom &#8211;export-use-hints).</p>
<dt><code>-y</code> <i></i><font SIZE="-1"><i>HODNOTA</i></font><i></i>, <code>&#8211;export-background-opacity</code>=<i></i><font SIZE="-1"><i>HODNOTA</i></font><i></i></p>
<dd>Krytie pozadia exportovaných súborov <font SIZE="-1">PNG.</font> Toto môže byť hodnota buď medzi 0.0 a 1.0 (kde 0.0 znamená celkom priehľadné a 1.0 plné krytie) alebo väčšia ako 1 do 255 (kde 255 znamená plné krytie). Ak nie je hodnota nastavená a nepoužije sa voľba -b, použije sa krytie stránky nastavené v Inkscape v dialógu Vlastnosti dokumentu (uložené v atribúte inkscape:pageopacity= sodipodi:namedview). Ak nie je hodnota nastavená a použije sa voľba -b použije sa hodnota 255 (plné krytie).</p>
<dt><code>-P</code> <i>NÁZOVSÚBORU</i>, <code>&#8211;export-ps</code>=<i>NÁZOVSÚBORU</i></p>
<dd>Exportovať dokumenty do formátu PostScript. Pamätajte, že PostScript nepodporuje priesvitnosť, takže akékoľvek priesvitné objekty v pôvodnom <font SIZE="-1">SVG</font> sa automaticky rasterizujú. Priložia sa použité písma alebo podmnožina použitých znakov. Štandardná oblasť exportu je plátno a môžete ju nastaviť na kresbu pomocou &#8211;export-area-drawing. Ak chcete exportovať jediný objekt, môžete použiť &#8211;export-id (všetky ostatné sa skryjú); v tom prípade bude oblasťou exportu ohraničenie uvedeného objektu, ale možno ho nastaviť na plátno voľbou &#8211;export-area-canvas.</p>
<dt><code>-E</code> <i>NÁZOVSÚBORU</i>, <code>&#8211;export-eps</code>=<i>NÁZOVSÚBORU</i></p>
<dd>Exportovať dokumenty do formátu Encapsulated PostScript. Pamätajte, že PostScript nepodporuje priesvitnosť, takže akékoľvek priesvitné objekty v pôvodnom <font SIZE="-1">SVG</font> sa automaticky rasterizujú. Priložia sa použité písma alebo podmnožina použitých znakov. Štandardná oblasť exportu je kresba a môžete ju však nastaviť na plátno, pozrite si však obmedzenia v popise voľby &#8211;export-area-drawing. Ak chcete exportovať jediný objekt, môžete použiť &#8211;export-id (všetky ostatné sa skryjú).</p>
<dt><code>-A</code> <i>NÁZOVSÚBORU</i>, <code>&#8211;export-pdf</code>=<i>NÁZOVSÚBORU</i></p>
<dd>Exportovať dokumenty do formátu <font SIZE="-1">PDF</font> format. Tento formát zachováva priesvitnosť z pôvodného <font SIZE="-1">SVG.</font> Priložia sa použité písma alebo podmnožina použitých znakov. Štandardná oblasť exportu je plátno a môžete ju nastaviť na kresbu pomocou &#8211;export-area-drawing. Ak chcete exportovať jediný objekt, môžete použiť &#8211;export-id (všetky ostatné sa skryjú); v tom prípade bude oblasťou exportu ohraničenie uvedeného objektu, ale možno ho nastaviť na plátno voľbou &#8211;export-area-canvas.</p>
<dt><code>-T</code>, <code>&#8211;export-text-to-path</code></p>
<dd>Konvertovať pri exporte textové objekty na cesty kde sa dá (pri exporte <font SIZE="-1">PS, EPS</font> a <font SIZE="-1">PDF</font>).</p>
<dt><code>&#8211;export-ignore-filters</code></p>
<dd>Exportovať objekty s filtrami (napr. s rozostrením) ako vektorovú grafiku a ignorovať filtre (pri exporte <font SIZE="-1">PS, EPS</font> a <font SIZE="-1">PDF</font>). Štandardne sa všetky objekty s filtrami rasterizujú s rozlíšením &#8211;export-dpi (štandardne 90 dpi) čím sa zachová ich vzhľad.</p>
<dt><code>-I</code>, <code>&#8211;query-id</code></p>
<dd>Nastaviť <font SIZE="-1">ID</font> objektu, ktoré rozmery zisťujeme. Ak nie je nastavené, voľby požiadavky vrátia rozmer kresby (t.j. všetkých objektov dokumentu), nie stránky či zobrazenia.</p>
<dt><code>-X</code>, <code>&#8211;query-x</code></p>
<dd>Zistiť súradnicu X kresby alebo, ak je určený, objektu s &#8211;query-id. Vrátená hodnota je v px (používateľské jednotky <font SIZE="-1">SVG</font>).</p>
<dt><code>-Y</code>, <code>&#8211;query-y</code></p>
<dd>Zistiť súradnicu Y kresby alebo, ak je určený, objektu s &#8211;query-id. Vrátená hodnota je v px (používateľské jednotky <font SIZE="-1">SVG</font>).</p>
<dt><code>-W</code>, <code>&#8211;query-width</code></p>
<dd>Zistiť šírku kresby alebo, ak je určený, objektu s &#8211;query-id. Vrátená hodnota je v px (používateľské jednotky <font SIZE="-1">SVG</font>).</p>
<dt><code>-H</code>, <code>&#8211;query-height</code></p>
<dd>Zistiť výšku kresby alebo, ak je určený, objektu s &#8211;query-id. Vrátená hodnota je v px (používateľské jednotky <font SIZE="-1">SVG</font>).</p>
<dt><code>-S</code>, <code>&#8211;query-all</code></p>
<dd>Vypíše zoznam všetkých objektov v dokumente <font SIZE="-1">SVG</font> s definovaným id spolu s ich súradnicou x,y, šírkou a výškou vo formáte s hodnotami oddelenom čiarkami.</p>
<dt><code>&#8211;shell</code></p>
<dd>Ak je zadaný tento parameter, Inkscape vstúpi do interaktívneho režimu príkazového riadka. V tomto režime píšete príkazy na príkazovom riadku a Inkscape ich vykonáva bez toho aby ste museli pri každom príkaze spúšťať novú inštanciu Inkscape. Táto vlastnosť je najužitočnejšia v skriptoch a pri použití na serveri: nepridáva nové schopnosti, ale umožňuje vám zlepšovať nároky na rýchlosť a pamäť akéhokoľvek skriptu, ktorý opakovane volá Inkscape aby vykonal úlohy z príkazového riadka (ako export alebo konverzie). Každý príkaz v režime shellu musí byť úplný platný príkaz Inkscape ale bez názvu programu Inkscape, napr. „subor.svg &#8211;export-pdf=subor.pdf“.</p>
<dt><code>&#8211;vacuum-defs</code></p>
<dd>Odstráni všetky nepoužité položky zo sekcie &lt;lt&gt;defs&lt;gt&gt; <font SIZE="-1">SVG</font> súboru. Ak túto voľbu zadáte spolu s &#8211;export-plain-svg, bude mať vplyv iba na exportovaný súbor. Ak ju použijete samostatne, zmení sa existujúci súbor.</p>
<dt><code>-z</code>, <code>&#8211;without-gui</code></p>
<dd>Neotvírať grafické rozhranie (na unixových systémoch nepoužívať X server), iba spracovať súbory z konzoly. Táto voľba sa predpokladá pri voľbách -p, -e, -l a &#8211;vacuum-defs.</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd>Táto štandardná voľba <font SIZE="-1">GTK</font> vynucuje, že akékoľvek upozornenia, ktoré sú zvyčajne neškodné, spôsobia ukončenie Inkscape (čo je užitočné pri ladení).</p>
<dt><code>&#8211;usage</code></p>
<dd>Zobrazí stručnú správu o tom ako používať Inkscape.</dl>
<h2>Konfigurácia</h2>
<p>Hlavný konfiguračný súboor je ~/.config/Inkscape/preferences.xml. Ukladá rozličné nastavenia, ktoré môžete zmeniť v Inkscape (prevažne v dialógu Nastavenia Inkscape). Do podadresárov tohto adresára tiež môžete umiestniť vlastné: </p>
<p> $HOME/.config/Inkscape/extensions/ &#8211; rozširujúce efekty. </p>
<p> $HOME/.config/Inkscape/icons/ &#8211; ikony. </p>
<p> $HOME/.config/Inkscape/keys/ &#8211; mapy kláves. </p>
<p> $HOME/.config/Inkscape/templates/ &#8211; šablóny nových súborov.</p>
<h2>Diagnostika</h2>
<p>Program vráti nulovú hodnotu pri úspešnom a nenulovú pri neúspešnom ukončení. </p>
<p> Na štandardný chybový výstup alebo štandardný výstup môže vypísať rozličné chybové hlásenia alebo upozornenia. Ak sa program správa chybne alebo havaruje v súvislosti s konkrétnym <font SIZE="-1">SVG</font> súborom, prehliadnutie tohto výstupu pomôže zistiť dôvod zlyhania.</p>
<h2>Príklady</h2>
<p>Hoci je <code>Inkscape</code> zjavne v prvom rade aplikácia s grafickým používateľským rozhraním, tiež ho možno použiť na spracovanie <font SIZE="-1">SVG</font> z príkazového riadka. </p>
<p> Otvorenie <font SIZE="-1">SVG</font> súboru v grafickom rozhraní: </p>
<pre> inkscape subor.svg</pre>
<p>Vytlačenie <font SIZE="-1">SVG</font> súboru z príkazového riadka: </p>
<pre> inkscape subor.svg -p '| lpr'</pre>
<p>Export <font SIZE="-1">SVG</font> súboru do <font SIZE="-1">PNG</font> v predvolenom rozlíšení 90 dpi (jedna používateľská jednotka <font SIZE="-1">SVG</font> zodpovedá jednému pixlu bitmapy): </p>
<pre> inkscape subor.svg --export-png=subor.png</pre>
<p>To isté, ale veľkosť súboru <font SIZE="-1">PNG</font> je vynútená na 600&#215;400 pixlov: </p>
<pre> inkscape subor.svg --export-png=subor.png -w600 -h400</pre>
<p>To isté, ale exportuje kresbu (ohraničenie všetkých objektov), nie stránku: </p>
<pre> inkscape subor.svg --export-png=subor.png --export-area-drawing</pre>
<p>Exportuje do <font SIZE="-1">PNG</font> objekt s id=&#8220;text1555&#8221; s použitím názvu súboru a rozlíšenia, ktoré boli použité pri poslednom exporte objektu z grafického rozhrania: </p>
<pre> inkscape subor.svg --export-id=text1555 --export-use-hints</pre>
<p>To isté, ale použiť rozlíšenie 90 dpi, určiť názov súboru a prichytiť exportovanú oblasť smerom von k najbližšej celej hodnte používateľskej jednotky <font SIZE="-1">SVG </font>(aby sa zachovalo zarovnanie objektov na pixle a tak minimalizoval aliasing): </p>
<pre> inkscape subor.svg --export-id=text1555 --export-png=text.png --export-area-snap</pre>
<p>Previesť Inkscape <font SIZE="-1">SVG</font> na čistý <font SIZE="-1">SVG</font> dokument: </p>
<pre> inkscape subor1.svg --export-plain-svg=subor2.svg</pre>
<p>Previesť <font SIZE="-1">SVG</font> dokument na <font SIZE="-1">EPS,</font> pričom prevedie všetky texty na cesty: </p>
<pre> inkscape subor.svg --export-eps=subor.eps --export-text-to-path</pre>
<p>Zistiť šírku objektu s id=&#8220;text1555&#8221;: </p>
<pre> inkscape subor.svg --query-width --query-id text1555</pre>
<p>Duplikovať objekt s id=&#8220;path1555&#8221;, otočiť duplikát o 90 stupňov, uložiť <font SIZE="-1">SVG</font> a skončiť: </p>
<pre> inkscape subor.svg --select=path1555 --verb=EditDuplicate --verb=ObjectRotate90 --verb=FileSave --verb=FileClose</pre>
<h2>Prostredie</h2>
<p><font SIZE="-1"><code>DISPLAY</code></font> zistenie predvoleného hostiteľa a čísla displeja. </p>
<p> <font SIZE="-1"><code>TMPDIR</code></font> nastavenie predvoleného adresára pre dočasné súbory. Adresár musí existovať.</p>
<h2>Témy</h2>
<p>Ak chcete načítať odlišnú sadu ikon ako predvolený súbor $PREFIX/share/inkscape/icons/icons.svg, použije sa adresár $HOME/.inkscape/icons/. Ikony sa načítavajú podľa názvu (napr. <i>fill_none.svg</i>) alebo ak nie sú nájdené z <i>icons.svg</i>. Ak sa ikona nenačíta ani z jedného z týchto miest, použije sa predvolené umiestnenie systému. </p>
<p> Potrebné ikony sa načítavajú zo <font SIZE="-1">SVG</font> súborov hľadaním <font SIZE="-1">SVG</font> id so zodpovedajúcim názvom ikony. (Napr. pri načítaní ikony „fill_none“ zo súboru sa ako ikona vykreslí ohraničenie „fill_none“, či už pochádza zo súboru <i>fill_none.svg</i> alebo <i>icons.svg</i>.)</p>
<h2>Ďalšie Informácie</h2>
<p>Umiestnenie kanonickej dokumentácie k <code>Inkscape</code> je na <a rel="nofollow" href="http://www.inkscape.org/.">http://www.inkscape.org/.</a> Webová stránka obsahuje novinky, dokumentáciu, návody, príklady, archívy konferencií, poslednú vydanú verziu programu, databázy chýb a žiadostí o nové funkcie, fóra a ďalšie.</p>
<h2>Pozri Aj</h2>
<p>potrace, cairo, <i><a href="/docs/linux/man/1-rsvg/">rsvg</a></i>(1), batik, ghostscript, pstoedit. </p>
<p> Testovací balík konformnosti so štandardom <font SIZE="-1">SVG: </font> <a rel="nofollow" href="http://www.w3.org/Graphics/SVG/Test/">http://www.w3.org/Graphics/SVG/Test/</a> </p>
<p> Nástroj na testovanie platnosti <font SIZE="-1">SVG: </font> <a rel="nofollow" href="http://jiggles.w3.org/svgvalidator/">http://jiggles.w3.org/svgvalidator/</a> </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.1 Specification</i> <i>W3C Recommendation 14 January 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG11/">http://www.w3.org/TR/SVG11/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.2 Specification</i> <i>W3C Working Draft 13 November 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG12/">http://www.w3.org/TR/SVG12/</a>&gt; </p>
<p> <i></i><font SIZE="-1"><i>SVG 1.1/1.2/2.0</i></font><i> Requirements</i> <i>W3C Working Draft 22 April 2002</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG2Reqs/">http://www.w3.org/TR/SVG2Reqs/</a>&gt; </p>
<p> <i>Document Object Model (</i><font SIZE="-1"><i>DOM</i></font><i>): Level 2 Core</i> <i>Arnaud Le Hors et al editors, W3C</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/DOM-Level-2-Core/">http://www.w3.org/TR/DOM-Level-2-Core/</a>&gt;</p>
<h2>Poznámky Ku Grafickému Rozhraniu</h2>
<p>Ak sa chcete naučiť pracovať s grafickým rozhraním Inkscape Pomocník &gt; Návody. </p>
<p> Okrem <font SIZE="-1">SVG</font> dokáže Inkscape importovať (Súbor &gt; Importovať) väčšinu bitmapových formátov (<font SIZE="-1">PNG, BMP, JPG, XPM, GIF</font> atď.), čistý text (vyžaduje Perl), <font SIZE="-1">PS</font> a <font SIZE="-1">EPS </font>(vyžaduje Ghostscript), formáty <font SIZE="-1">PDF</font> a <font SIZE="-1">AI </font>(<font SIZE="-1">AI</font> verzie 9.0 alebo novšia). </p>
<p> Inkscape exportuje 32-bitové <font SIZE="-1">PNG</font> obrázky (Súbor &gt; Exportovať) a tiež <font SIZE="-1">AI, PS, EPS, PDF, DXF, </font> a niekoľko ďalších formátov pomocou Súbor &gt; Uložiť ako. </p>
<p> Inkscape dokáže cyužiť informáciu o tlaku a sklone grafického tabletu na nastavenie šírky, uhla a sily niektorých nástrojov vrátane kaligrafického pera. </p>
<p> Inkscape obsahuje grafické rozhranie k jadru na vektorizáciu bitmáp Potrace (<a rel="nofollow" href="http://potrace.sf.net">http://potrace.sf.net</a>), ktoré je súčasťou Inkscape. </p>
<p> Inkscape dokáže využívať externé skripty (filtre štandardného vstupu/výstupu), ktoré predstavujú príkazy v menu Efekty. Skript môže mať grafický dialóg na nastavenie parametrov a dokáže zistiť <font SIZE="-1">ID</font> vybraných objektov na ktoré sa bude aplikovať prostredníctvom príkazového riadka. Inkscape obsahuje sadu efektov napísaných v jazyku Python.</p>
<h2>Klávesové Väzby</h2>
<p>Úplný zoznam skratiek klávesnice a myši nájdete v súbore doc/keys.html alebo pomocou príkazu Použitie klávesnice a myši v menu Pomocník.</p>
<h2>Chyby</h2>
<p>Je známych množstvo chýb. Existujúce chyby kontrolujte a nové hláste na webstránke inkscape.org. Tiež si prečítajte sekciu Známe problémy v Poznámkach k vydaniu vašej verzie (súbor „NEWS“).</p>
<h2>Autori</h2>
<p>Kód vďačí za svoju existenciu množstvu prispievateľov do jeho rozličných foriem. Nasledovný zoznam je určite neúplný, ale slúži na uznanie mnohých ramien, na ktorých táto aplikácia stojí: </p>
<p> Maximilian Albert, Joshua A. Andler, Tavmjong Bah, Pierre Barbry-Blot, Jean-François Barraud, Campbell Barton, Bill Baxter, John Beard, John Bintz, Arpad Biro, Nicholas Bishop, Joshua L. Blocher, Hanno Böck, Tomasz Boczkowski, Henrik Bohre, Boldewyn, Daniel Borgmann, Bastien Bouclet, Hans Breuer, Gustav Broberg, Christopher Brown, Marcus Brubaker, Luca Bruno, Nicu Buculei, Bulia Byak, Pierre Caclin, Ian Caldwell, Gail Carmichael, Ed Catmur, Chema Celorio, Jabiertxo Arraiza Cenoz, Johan Ceuppens, Zbigniew Chyla, Alexander Clausen, John Cliff, Kees Cook, Ben Cromwell, Robert Crosbie, Jon Cruz, Aurélie De-Cooman, Kris De Gussem, Milosz Derezynski, Daniel Díaz, Bruno Dilly, Larry Doolittle, Nicolas Dufour, Tim Dwyer, Maxim V. Dziumanenko, Johan Engelen, Miklos Erdelyi, Ulf Erikson, Noé Falzon, Frank Felfe, Andrew Fitzsimon, Edward Flick, Marcin Floryan, Fred, Ben Fowler, Cedric Gemy, Steren Giannini, Olivier Gondouin, Ted Gould, Toine de Greef, Michael Grosberg, Bryce Harrington, Dale Harvey, Aurélio Adnauer Heckert, Carl Hetherington, Jos Hirth, Hannes Hochreiner, Thomas Holder, Joel Holdsworth, Christoffer Holmstedt, Alan Horkan, Karl Ove Hufthammer, Richard Hughes, Nathan Hurst, inductiveload, Thomas Ingham, Jean-Olivier Irisson, Bob Jamison, Ted Janeczko, jEsuSdA, Lauris Kaplinski, Lynn Kerby, Niko Kiirala, James Kilfiger, Nikita Kitaev, Jason Kivlighn, Adrian Knoth, Krzysztof Kosiński, Petr Kovar, Benoît Lavorata, Alex Leone, Julien Leray, Raph Levien, Diederik van Lierop, Nicklas Lindgren, Vitaly Lipatov, Ivan Louette, Fernando Lucchesi Bastos Jurema, Pierre-Antoine Marc, Aurel-Aimé Marmion, Colin Marquardt, Craig Marshall, Ivan Masár, Dmitry G. Mastrukov, David Mathog, Matiphas, Michael Meeks, Federico Mena, MenTaLguY, Aubanel Monnier, Vincent Montagne, Tim Mooney, Derek P. Moore, Chris Morgan, Peter Moulder, Jörg Müller, Yukihiro Nakai, Victor Navez, Christian Neumair, Nick, Andreas Nilsson, Mitsuru Oka, Vinícius dos Santos Oliveira, Martin Owens, Alvin Penner, Matthew Petroff, Jon Phillips, Zdenko Podobny, Alexandre Prokoudine, Jean-René Reinhard, Alexey Remizov, Frederic Rodrigo, Hugo Rodrigues, Juarez Rudsatz, Xavier Conde Rueda, Felipe Corrêa da Silva Sanches, Christian Schaller, Marco Scholten, Tom von Schwerdtner, Danilo Šegan, Abhishek Sharma, Shivaken, Michael Sloan, John Smith, Boštjan Špetič, Aaron Spike, Kaushik Sridharan, Ralf Stephan, Dariusz Stojek, Martin Sucha, ~suv, Pat Suwalski, Adib Taraben, Hugh Tebby, Jonas Termeau, David Turner, Andre Twupack, Aleksandar Urošević, Alex Valavanis, Joakim Verona, Lucas Vieites, Daniel Wagenaar, Liam P. White, Sebastian Wüst, Michael Wybrow, Gellule Xg, Daniel Yacob, David Yip, Masatake Yamato </p>
<p> Túto manuálovú stránku zostavil Bryce Harrington &lt;brycehar [at] bryceharrington.com&gt;.</p>
<h2>História</h2>
<p>Kód, ktorý sa neskôr stal kódom Inkscape začal svoj život v roku 1999 ako program Gill, aplikácia <font SIZE="-1">GNOME</font> Illustrator, ktorú vytvoril Raph Levien. Cieľom, ktorý si Gill kládol bolo nakoniec podporovať kompletný štandard <font SIZE="-1">SVG.</font> Raph implementoval bézierový PostScriptový obrazový model vrátane výplne a ťahu, štýlov zakončenia a spojenia čiar, textu atď. Raphhova stránka o Gill je <a rel="nofollow" href="http://www.levien.com/svg/.">http://www.levien.com/svg/.</a> Práca na Gill sa spomalila alebo zastavila v roku 2000. </p>
<p> Ďalším stelesnením kódu sa stal veľmi populárny program Sodipodi, ktorý viedol Lauris Kaplinski. Kód sa zmenil na veľmi mocný ilustračný nástroj počas niekoľkých rokov práce na ňom po pridaní niekoľkých nových vlasntostí, podpory jazykov, portovania na Windows a iné operačné systémy a odstránení závislostí. </p>
<p> Inkscape vytvorili v roku 2003 štyria aktívni vývojári Sodipodi &#8211; Bryce Harrington, MenTaLguY, Nathan Hurst a Ted Gould, ktorí chceli kód posunúť novým smerom so zameraním na konformnosť s <font SIZE="-1">SVG,</font> vzľad a správanie rozhrania a túžbou otvoriť príležitosť vývoja viacerým prispievateľom. Projekt postupoval rýchlo a získal si množstvo veľmi aktívnych prispievateľov a vlastností. </p>
<p> Mnoho práce v raných dňoch projektu sa zameriavalo na stabilizáciu kódu a internacionalizáciu. Pôvodné vykresľovacie jadro zdedené zo Sodipodi bolo spojené s mnohými matematickými hraničnými prípadmi, ktoré viedli k neočakávaným haváriám pri použití programu na iné ako rutinné úlohy. Toto vykresľovacie jadro nahradil Livarot, ktorý hoci tiež nie je dokonalý, bol výrazne menej náchylný na chyby. Projekt tiež praktikoval časté začleňovanie kódu a posmeľoval používateľov v používaní vývojových verzií programu. To pomohlo s ranou identifikáciou chýb a zabezpečilo jednoduchý spôsob ako používatelia mohli overiť funkčnosť opráv. V dôsledku Inkscape si Inkscape zaslúžil všeobecnú reputáciu robustnosti a spoľahlivosti. </p>
<p> Tiež sa rozvinuli snahy o internacionalizáciu a lokalizáciu rozhrania, ktoré pomohli programu získať prispievateľov z celého sveta. </p>
<p> Inkscape mal prínosný vplyv na vizuálnu atraktivitu open source vo všeobecnosti, pretože poskytol nástroj na tvorbu a zdieľanie ikon, štartovacích obrazoviek, grafiky webových stránok atď. Istým spôsobom okrem toho, že je to len „program na kreslenie“ hral Inkscape dôležitú úlohu pri vylepšení vizuálnej stránky open source širokému publiku.</p>
<h2>Autorské Práva A Licencia</h2>
<p><code>Copyright (C)</code> 1999-2008 Autori. </p>
<p> <code>Inkscape</code> je slobodný softvér; môžete ho používať a šíriť za podmienok licencie <font SIZE="-1">GPL.</font></p>
