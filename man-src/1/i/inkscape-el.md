---
title: "inkscape-el(1)"
name: "inkscape-el"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkscape-el/"
---

<h2>Ονομα</h2>
<p>Inkscape &#8211; ένα πρόγραμμα επεξεργασίας SVG (κλιμακώσιμων γραφικών διανυσμάτων)</p>
<h2>Συνοψη</h2>
<p><tt>&quot;inkscape [επιλογές [όνομα_αρχείου ...]&quot;</tt> </p>
<p> επιλογές: </p>
<pre> -?, --help 
 --usage 
 -V, --version
 -f, --file=FILENAME 
 -e, --export-png=FILENAME 
 -a, --export-area=x0:y0:x1:y1 
 -C, --export-area-page
 -D, --export-area-drawing
 --export-area-snap
 -i, --export-id=ID 
 -j, --export-id-only 
 -t, --export-use-hints
 -b, --export-background=COLOR 
 -y, --export-background-opacity=VALUE 
 -d, --export-dpi=DPI 
 -w, --export-width=WIDTH 
 -h, --export-height=HEIGHT 
 -P, --export-ps=FILENAME
 -E, --export-eps=FILENAME
 -A, --export-pdf=FILENAME
 --export-pdf-version=VERSION-STRING
 --export-latex
 --export-ps-level {2,3}
 -T, --export-text-to-path
 --export-ignore-filters
 -l, --export-plain-svg=FILENAME 
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
<h2>Περιγραφη</h2>
<p><code>Inkscape</code> είναι ένας επεξεργαστής GUI για αρχεία σχεδίασης τύπου <code>Scalable Vector Graphics (</code><code>SVG</code><code>)</code>, με δυνατότητες παρόμοιες με <code>Adobe Illustrator</code>, <code>CorelDraw</code>, <code>Xara Xtreme</code>, κλ. χαρακτηριστικά Inkscape που περιλαμβάνουν εύχρηστα σχήματα, μονοπάτια bezier, ελεύθερη σχεδίαση, κείμενο πολλαπλής γραμμής, κείμενο σε μονοπάτι, ανάμειξη άλφα, μετασχηματισμούς ελεύθερου συσχετισμού, διαβαθμίσεις και γεμίσματα μοτίβων, επεξεργασία κόμβου, πολλές μορφές εξαγωγής και εισαγωγής περιλαμβάνοντας PNG και PDF, ομαδοποίηση, στρώσεις, ζωντανούς κλώνους και πολλά άλλα. Η διεπαφή σχεδιάστηκε να είναι άνετη και αποτελεσματική για έμπειρους χρήστες, ενώ παραμένει συμβατή με πρότυπα <code>GNOME</code>, έτσι ώστε χρήστες εξοικειωμένοι με άλλες εφαρμογές GNOME να μπορούν να μάθουν τη διεπαφή της γρήγορα. </p>
<p> <code>SVG</code> είναι ένα πρότυπο W3C τύπου XML για δισδιάστατη σχεδίαση διανύσματος. Επιτρέπει ορισμό αντικειμένων στη σχεδίαση χρησιμοποιώντας σημεία, μονοπάτια και αρχέτυπα σχήματα. Χρώματα, γραμματοσειρές, πλάτη πινελιάς κ.ο.κ καθορίζονται ως γνωρίσματα `μορφοποίησης&#8217; σε αυτά τα αντικείμενα. Ο σκοπός είναι ότι αφού SVG είναι ένα πρότυπο και αφού τα αρχεία του είναι κείμενο/xml, θα είναι δυνατή η χρήση αρχείων SVG σε έναν αρκετά μεγάλο αριθμό προγραμμάτων και για μεγάλο εύρος χρήσεων. </p>
<p> Το <code>Inkscape</code> χρησιμοποιεί SVG ως εγγενή του τύπο αρχείων και έχει το σκοπό να γίνει το πιο πλήρως συμβατό πρόγραμμα σχεδίασης για αρχεία SVG διαθέσιμα στην κοινότητα ανοικτού κώδικα.</p>
<h2>Επιλογες</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd>Προβολή μηνύματος βοήθειας</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Προβολή έκδοσης Inkscape και ημερομηνία μεταγλώττισης.</dd>
<dt><code>-a</code> <i>x0:y0:x1:y1</i>, <code>&#8211;export-area</code>=<i>x0:y0:x1:y1</i></dt>
<dd>Στην εξαγωγή PNG, ορίστε την εξαγόμενη περιοχή σε μονάδες χρήστη SVG (μονάδες ανώνυμου μήκους κανονικά χρησιμοποιούνται στο Inkscape SVG). Η προεπιλογή είναι η εξαγωγή της συνολικής σελίδας εγγράφου. Το σημείο (0,0) είναι η κάτω αριστερή γωνία.</dd>
<dt><code>-C</code>, <code>&#8211;export-area-page</code></dt>
<dd>Στην εξαγωγή PNG, PDF, PS και EPS, η εξαγόμενη περιοχή είναι η σελίδα. Αυτή είναι η προεπιλογή για PNG, PDF και PS, έτσι δεν χρειάζεται να το καθορίσετε εκτός και χρησιμοποιείτε &#8211;export-id για εξαγωγή ενός ειδικού αντικειμένου. Στο EPS, όμως, αυτό δεν είναι προεπιλεγμένο. Επιπλέον για EPS, η προδιαγραφή του τύπου δεν επιτρέπει το οριακό του πλαίσιο να επεκτείνεται πέρα από το περιεχόμενο του. Αυτό σημαίνει ότι όταν &#8211;export-area-page χρησιμοποιείται με εξαγωγή EPS, το οριακό πλαίσιο της σελίδας θα περικοπεί προς τα μέσα του οριακού πλαισίου του περιεχομένου εάν είναι μικρότερο.</dd>
<dt><code>-D</code>, <code>&#8211;export-area-drawing</code></dt>
<dd>Στην εξαγωγή PNG, PDF, PS και EPS, εξαγόμενη περιοχή είναι το σχέδιο (όχι η σελίδα), δηλαδή το οριακό πλαίσιο όλων των αντικειμένων του εγγράφου (ή του εξαγόμενου αντικειμένου εάν &#8211;export-id χρησιμοποιείται). Με αυτήν την επιλογή, η εξαγόμενη εικόνα θα εμφανίσει όλα τα ορατά αντικείμενα του εγγράφου χωρίς περιθώρια ή περικοπή. Αυτή είναι η προεπιλεγμένη περιοχή εξαγωγής για EPS. Για PNG, μπορεί να χρησιμοποιηθεί σε συνδυασμό με &#8211;export-use-hints.</dd>
<dt><code>&#8211;export-area-snap</code></dt>
<dd>Για εξαγωγή PNG, προσαρμογή της περιοχής εξαγωγής προς τα έξω στον πλησιέστερο ακέραιο SVG τιμών μονάδας χρήστη (px). Εάν χρησιμοποιείτε την προεπιλεγμένη ανάλυση εξαγωγής των 90 dpi και τα γραφικά σας προσαρμόζονται στα εικονοστοιχεία για ελαχιστοποίηση εξομάλυνσης, αυτός ο διακόπτης σας επιτρέπει να διατηρήσετε αυτή την ευθυγράμμιση ακόμα κι αν εξάγετε μερικά οριακά πλαίσια αντικειμένου (με &#8211;export-id ή &#8211;export-area-drawing) που είναι το ίδιο μη ευθυγραμμιζόμενο με εικονοστοιχεία.</dd>
<dt><code>-b</code> <i></i><i>COLOR</i><i></i>, <code>&#8211;export-background</code>=<i></i><i>COLOR</i><i></i></dt>
<dd>Το χρώμα παρασκηνίου του εξαγόμενου PNG. Αυτό μπορεί να είναι οποιοδήποτε αλφαριθμητικό υποστηριζόμενου χρώματος SVG, π.χ. &#8220;#ff007f&#8221; ή &#8220;rgb(255, 0, 128)&#8221;. Εάν δεν οριστεί, τότε το χρώμα της σελίδας που ορίστηκε στο Inkscape στο διάλογο επιλογών εγγράφου θα χρησιμοποιηθεί (καταχωρημένο στο pagecolor= attribute of sodipodi:namedview).</dd>
<dt><code>-d</code> <i></i><i>DPI</i><i></i>, <code>&#8211;export-dpi</code>=<i></i><i>DPI</i><i></i></dt>
<dd>Η χρησιμοποιούμενη ανάλυση για εξαγωγή PNG. Χρησιμοποιείται επίσης για τη στάθμη εικονογραφικοποίησης των φιλτραρισμένων αντικειμένων όταν εξάγονται σε PS, EPS, ή PDF (εκτός και καθορίσετε &#8211;export-ignore-filters για να καταργήσετε την εικονογραφικοποίηση). Η προεπιλογή είναι 90 dpi, που αντιστοιχεί σε 1 μονάδα χρήστη SVG (px, που λέγεται επίσης &#8220;μονάδα χρήστη&#8221;) εξαγωγής ανά 1 εικονοστοιχείο ψηφιογραφίας. Αυτή η τιμή υπερισχύει της υπόδειξης DPI εάν χρησιμοποιηθεί με &#8211;export-use-hints.</dd>
<dt><code>-e</code> <i></i><i>FILENAME</i><i></i>, <code>&#8211;export-png</code>=<i></i><i>FILENAME</i><i></i></dt>
<dd>Καθορισμός του ονόματος αρχείου για εξαγωγή PNG. Εάν ήδη υπάρχει, το αρχείο θα αντικατασταθεί χωρίς ερώτηση.</dd>
<dt><code>-f</code> <i></i><i>FILENAME</i><i></i>, <code>&#8211;file</code>=<i></i><i>FILENAME</i><i></i></dt>
<dd>Άνοιγμα καθορισμένων εγγράφων. Το αλφαριθμητικό επιλογής μπορεί να παραληφθεί, δηλαδή μπορείτε να καταγράψετε τα ονόματα αρχείου χωρίς -f.</dd>
<dt><code>-g</code>, <code>&#8211;with-gui</code></dt>
<dd>Δοκιμάστε να χρησιμοποιήσετε το GUI (σε Unix, χρησιμοποιήστε τον εξυπηρετητή X ακόμα κι αν το <tt>$DISPLAY</tt> δεν καθορίζεται).</dd>
<dt><code>-h</code> <i></i><i>HEIGHT</i><i></i>, <code>&#8211;export-height</code>=<i></i><i>HEIGHT</i><i></i></dt>
<dd>Το ύψος της δημιουργημένης ψηφιογραφίας σε εικονοστοιχεία. Αυτή η τιμή υπερισχύει του ορισμού &#8211;export-dpi (ή της υπόδειξης DPI, εάν χρησιμοποιείται με &#8211;export-use-hints).</dd>
<dt><code>-i</code> <i></i><i>ID</i><i></i>, <code>&#8211;export-id</code>=<i></i><i>ID</i><i></i></dt>
<dd>For PNG, PS, EPS, PDF and plain SVG export, the id attribute value of the object that you want to export from the document; all other objects are not exported. By default the exported area is the bounding box of the object; you can override this using &#8211;export-area (PNG only) or &#8211;export-area-page.</dd>
<dt><code>-j</code>, <code>&#8211;export-id-only</code></dt>
<dd>For PNG and plain SVG, only export the object whose id is given in &#8211;export-id. All other objects are hidden and won&#8217;t show in export even if they overlay the exported object. Without &#8211;export-id, this option is ignored. For PDF export, this is the default, so this option has no effect.</dd>
<dt><code>-l</code>, <code>&#8211;export-plain-svg</code>=<i></i><i>FILENAME</i><i></i></dt>
<dd>Εξαγωγή αντικειμένων σε απλή μορφή SVG, χωρίς κενά ονόματος sodipodi: ή inkscape και χωρίς μεταδεδομένα RDF.</dd>
<dt><code>-x</code>, <code>&#8211;extension-directory</code></dt>
<dd>Καταγράφει τον τρέχοντα κατάλογο επέκτασης που το Inkscape ρύθμισε για χρήση και εξέρχεται. Αυτό χρησιμοποιείται για εξωτερική επέκταση για να χρησιμοποιηθεί η ίδια ρύθμιση όπως η αρχική εγκατάσταση του Inkscape.</dd>
<dt><code>&#8211;verb-list</code></dt>
<dd>Καταγράφει όλα τα διαθέσιμα ρήματα στο Inkscape με ταυτότητα. Αυτή η ταυτότητα μπορεί να χρησιμοποιηθεί για ορισμό χαρτογράφησης πλήκτρων ή μενού. Μπορεί επίσης να χρησιμοποιηθεί με την επιλογή γραμμής εντολής &#8211;verb.</dd>
<dt><code>&#8211;verb</code>=<i>VERB-ID</i>, <code>&#8211;select</code>=<i>OBJECT-ID</i></dt>
<dd>Αυτές οι δύο επιλογές δουλεύουν μαζί για να δώσουν κάποια βασικά σενάρια για το Inkscape από τη γραμμή εντολών. Και οι δύο μπορούν να συμβούν όσες φορές χρειάζονται στη γραμμή εντολών και εκτελούνται με τη σειρά σε κάθε έγγραφο που καθορίζεται. </dd>
<p> Η εντολή &#8211;verb θα εκτελέσει ένα ειδικό ρήμα σαν να καλέστηκε από ένα μενού ή κουμπί. Οι διάλογοι θα εμφανιστούν, εάν αυτό είναι τμήμα του ρήματος. Για λήψη μιας λίστας των διαθέσιμων ταυτοτήτων ρημάτων, χρησιμοποιήστε την επιλογή γραμμής εντολής &#8211;verb-list. </p>
<p> Η εντολή &#8211;select θα προκαλέσει τα αντικείμενα που έχουν τις καθορισμένες ταυτότητες να επιλεγούν. Αυτό επιτρέπει ποικίλα ρήματα να επενεργήσουν σε αυτά. Για να αφαιρέσετε όλες τις επιλογές χρησιμοποιήστε &#8211;verb=EditDeselect. Οι διαθέσιμες ταυτότητες αντικειμένων εξαρτώνται από το καθοριζόμενο έγγραφο για φόρτωση.</p>
<dt><code>-p</code> <i></i><i>PRINTER</i><i></i>, <code>&#8211;print</code>=<i></i><i>PRINTER</i><i></i></dt>
<dd>Εκτύπωση εγγράφων στον καθορισμένο εκτυπωτή χρησιμοποιώντας `lpr -P ΕΚΤΥΠΩΤΗΣ&#8217;. Εναλλακτικά χρησιμοποιήστε `| COMMAND&#8216; για να καθορίσετε μια διαφορετική εντολή διοχέτευσης, ή χρησιμοποιήστε `&gt; ΟΝΟΜΑΑΡΧΕΙΟΥ&#8217; για να γράψετε την έξοδο PostScript σε ένα αρχείο αντί για εκτύπωση. Να θυμόσαστε να βάλετε κατάλληλα εισαγωγικά για το κέλυφος σας, π.χ. </dd>
<p> inkscape &#8211;print=&#8217;| ps2pdf &#8211; mydoc.pdf&#8217; mydoc.svg</p>
<dt><code>-t</code>, <code>&#8211;export-use-hints</code></dt>
<dd>Χρησιμοποιήστε όνομα αρχείου και υποδείξεις DPI αποθηκευμένες στο εξαγόμενο αντικείμενο (μόνο με &#8211;export-id). Αυτές οι υποδείξεις ορίζονται αυτόματα, όταν εξάγετε επιλογή μες το Inkscape. Έτσι, για παράδειγμα, εάν εξάγετε ένα σχήμα με id=&#8220;path231&#8221; ως /home/me/shape.png στα 300 dpi από document.svg χρησιμοποιώντας Inkscape GUI και αποθηκεύσετε το έγγραφο, έπειτα αργότερα θα μπορείτε να το επανεξάγετε αυτό το σχήμα στο ίδιο αρχείο με την ίδια ανάλυση απλά με </dd>
<p> inkscape -i path231 -t document.svg </p>
<p> Εάν χρησιμοποιήσετε &#8211;export-dpi, &#8211;export-width ή &#8211;export-height με αυτήν την επιλογή, έπειτα η υπόδειξη DPI θα αγνοηθεί και η τιμή από τη γραμμή εντολής θα χρησιμοποιηθεί. Εάν χρησιμοποιήσετε &#8211;export-png με αυτήν την επιλογή, τότε η υπόδειξη ονόματος αρχείου θα αγνοηθεί και το όνομα αρχείου από τη γραμμή εντολών θα χρησιμοποιηθεί.</p>
<dt><code>-w</code> <i></i><i>WIDTH</i><i></i>, <code>&#8211;export-width</code>=<i></i><i>WIDTH</i><i></i></dt>
<dd>Το πλάτος της δημιουργούμενης ψηφιογραφίας σε εικονοστοιχεία. Αυτή η τιμή υπερισχύει της ρύθμισης &#8211;export-dpi (ή της υπόδειξης DPI εάν χρησιμοποιείται με &#8211;export-use-hints).</dd>
<dt><code>-y</code> <i></i><i>VALUE</i><i></i>, <code>&#8211;export-background-opacity</code>=<i></i><i>VALUE</i><i></i></dt>
<dd>Η αδιαφάνεια του παρασκηνίου του εξαγόμενου PNG. Αυτό μπορεί να είναι η τιμή είτε μεταξύ 0 και 1 (0 σημαίνει πλήρη διαφάνεια και 1 πλήρη αδιαφάνεια) ή μεγαλύτερη από 1 μέχρι 255 (255 σημαίνει πλήρης αδιαφάνεια). Εάν δεν οριστεί και η επιλογή -b δεν χρησιμοποιηθεί, τότε η αδιαφάνεια της σελίδας που ορίζεται στο Inkscape στο διάλογο επιλογών εγγράφου θα χρησιμοποιηθεί (καταχωρημένη στο γνώρισμα inkscape:pageopacity= attribute του sodipodi:namedview). Εάν δεν οριστεί αλλά χρησιμοποιηθεί η επιλογή -b, τότε η τιμή 255 (πλήρης αδιαφάνεια) θα χρησιμοποιηθεί.</dd>
<dt><code>-P</code> <i></i><i>FILENAME</i><i></i>, <code>&#8211;export-ps</code>=<i></i><i>FILENAME</i><i></i></dt>
<dd>Εξαγωγή εγγράφων σε μορφή PostScript. Σημειώστε ότι το PostScript δεν υποστηρίζει διαφάνεια, έτσι οποιαδήποτε διαφανή αντικείμενα στο αρχικό SVG θα εικονογραφικοποιηθούν αυτόματα. Οι χρησιμοποιούμενες γραμματοσειρές είναι υποσύνολο και ενσωματωμένες. Η προεπιλεγμένη περιοχή εξαγωγής είναι σελίδα. Μπορείτε να την ορίσετε στο σχέδιο με &#8211;export-area-drawing. Μπορείτε να καθορίσετε &#8211;export-id για εξαγωγή ενός μονού αντικειμένου (όλα τα άλλα κρύβονται). Στην περίπτωση αυτή η περιοχή εξαγωγής είναι το οριακό πλαίσιο αυτού του αντικειμένου, αλλά μπορεί να οριστεί σε σελίδα με &#8211;export-area-page.</dd>
<dt><code>-E</code> <i></i><i>FILENAME</i><i></i>, <code>&#8211;export-eps</code>=<i></i><i>FILENAME</i><i></i></dt>
<dd>Εξαγωγή εγγράφων σε μορφή ενσωματωμένου PostScript. Σημειώστε ότι το PostScript δεν υποστηρίζει διαφάνεια, έτσι οποιαδήποτε διαφανή αντικείμενα στο αρχικό SVG θα εικονογραφικοποιηθούν αυτόματα. Οι χρησιμοποιούμενες γραμματοσειρές είναι υποσύνολο και ενσωματωμένες. Η προεπιλεγμένη περιοχή εξαγωγής είναι σχέδιο. Μπορείτε να το ορίσετε στη σελίδα, όμως δείτε &#8211;export-area-page για εφαρμοζόμενους περιορισμούς. Μπορείτε να καθορίσετε &#8211;export-id για να εξάγετε ένα μονό αντικείμενο (όλα τα άλλα κρύβονται).</dd>
<dt><code>-A</code> <i></i><i>FILENAME</i><i></i>, <code>&#8211;export-pdf</code>=<i></i><i>FILENAME</i><i></i></dt>
<dd>Εξαγωγή εγγράφων σε μορφή PDF. Αυτή η μορφή διατηρεί τη διαφάνεια στο αρχικό SVG. Οι χρησιμοποιούμενες γραμματοσειρές είναι υποσύνολο και ενσωματωμένες. Η προεπιλεγμένη περιοχή εξαγωγής είναι σελίδα. Μπορείτε να το ορίσετε σε σχέδιο, με &#8211;export-area-drawing. Μπορείτε να καθορίσετε &#8211;export-id για να εξάγετε ένα μονό αντικείμενο (όλα τα άλλα κρύβονται). Σε αυτή την περίπτωση περιοχή εξαγωγής είναι αυτή του οριακού πλαισίου αντικειμένου, αλλά μπορεί να οριστεί σε σελίδα με &#8211;export-area-page.</dd>
<dt><code>&#8211;export-pdf-version</code>=<i>PDF-VERSION</i></dt>
<dd>Select the PDF version of the exported PDF file. This option basically exposes the PDF version selector found in the PDF-export dialog of the GUI. You must provide one of the versions from that combo-box, e.g. &#8220;1.4&#8221;. The default pdf export version is &#8220;1.4&#8221;.</dd>
<dt><code>&#8211;export-latex</code></dt>
<dd>(για εξαγωγή PS, EPS και PDF) Χρησιμοποιείται για δημιουργία εικόνων για έγγραφα LaTeX, όπου το κείμενο της εικόνας στοιχειοθετείται από LaTeX. Όταν εξάγετε σε μορφή PDF/PS/EPS, αυτή η επιλογή διαιρεί την έξοδο σε ένα αρχείο PDF/PS/EPS (π.χ. όπως ορίζεται από &#8211;export-pdf) και ένα αρχείο LaTeX. Το κείμενο δεν εξάγεται σε αρχείο PDF/PS/EPS, αλλά αντίθετα θα εμφανιστεί στο αρχείο LaTeX. Αυτό το αρχείο LaTeX συμπεριλαμβάνει το PDF/PS/EPS. Είσοδος του αρχείου LaTeX (\input{image.tex}) στο έγγραφό σας LaTeX θα εμφανίσει την εικόνα και όλο το κείμενο θα στοιχειοθετείται από LaTeX. Δείτε το τελικό αρχείο LaTeX για περισσότερες πληροφορίες. Επίσης δείτε την έξοδο τερματικού GNUPlot&#8217;s `epslatex&#8217;.</dd>
<dt><code>-T</code>, <code>&#8211;export-text-to-path</code></dt>
<dd>Convert text objects to paths on export, where applicable (for PS, EPS, PDF and SVG export).</dd>
<dt><code>&#8211;export-ignore-filters</code></dt>
<dd>Εξαγωγή φιλτραρισμένων αντικειμένων (π.χ. αυτά με θόλωση) όπως διανύσματα, αγνοώντας τα φίλτρα (για εξαγωγή PS, EPS και PDF). Από προεπιλογή, όλα τα φιλτραρισμένα αντικείμενα εικονογραφικοποιούνται στο &#8211;export-dpi (προεπιλογή 90 dpi), διατηρώντας την εμφάνιση.</dd>
<dt><code>-I</code>, <code>&#8211;query-id</code></dt>
<dd>Ορισμός της ταυτότητας του αντικειμένου του οποίου οι διαστάσεις αναζητούνται. Εάν δεν οριστεί, οι επιλογές ερωτήματος θα επιστρέψουν τις διαστάσεις του σχεδίου (δηλαδή όλα τα αντικείμενα εγγράφου), όχι τη σελίδα ή το πλαίσιο θέασης</dd>
<dt><code>-X</code>, <code>&#8211;query-x</code></dt>
<dd>Ερώτημα της συντεταγμένης Χ του σχεδίου ή, εάν καθοριστεί, του αντικειμένου με &#8211;query-id. Η επιστρεφόμενη τιμή είναι σε px (μονάδες χρήστη SVG).</dd>
<dt><code>-Y</code>, <code>&#8211;query-y</code></dt>
<dd>Ερώτημα της συντεταγμένης Υ του σχεδίου ή, εάν καθοριστεί, του αντικειμένου με &#8211;query-id. Η επιστρεφόμενη τιμή είναι σε px (μονάδες χρήστη SVG).</dd>
<dt><code>-W</code>, <code>&#8211;query-width</code></dt>
<dd>Ερώτημα του πλάτους του σχεδίου ή, εάν καθοριστεί, του αντικειμένου με &#8211;query-id. Η επιστρεφόμενη τιμή είναι σε px (μονάδες χρήστη SVG).</dd>
<dt><code>-H</code>, <code>&#8211;query-height</code></dt>
<dd>Ερώτημα του ύψους Ερώτημα της συντεταγμένης Χ του σχεδίου ή, εάν καθοριστεί, του αντικειμένου με &#8211;query-id. Η επιστρεφόμενη τιμή είναι σε px (μονάδες χρήστη SVG).</dd>
<dt><code>-S</code>, <code>&#8211;query-all</code></dt>
<dd>Εκτυπώνει μια λίστα όλων των αντικειμένων που είναι οριοθετημένοι με κόμμα στο έγγραφο SVG με καθορισμένες ταυτότητες, μαζί με τις τιμές τους x, y, πλάτους και ύψους.</dd>
<dt><code>&#8211;shell</code></dt>
<dd>Με αυτήν την παράμετρο, το Inkscape θα εισάγει μια κατάσταση κελύφους διαδραστικής γραμμής εντολής. Σε αυτήν την κατάσταση, πληκτρολογήστε εντολές στην προτροπή και το Inkscape τις εκτελεί, χωρίς να πρέπει να τρέξετε ένα νέο αντίγραφο του Inkscape για κάθε εντολή. Αυτό το χαρακτηριστικό είναι ιδιαίτερα χρήσιμο για χρήσεις σεναρίου και εξυπηρετητή: δεν προσθέτει νέες δυνατότητες, αλλά σας επιτρέπει να βελτιώσετε τις απαιτήσεις ταχύτητας και μνήμης οποιουδήποτε σεναρίου που καλεί επανειλημμένα το Inkscape να εκτελέσει εργασίες γραμμής εντολών (όπως εξαγωγή ή συζητήσεις). Κάθε εντολή σε κατάσταση κελύφους πρέπει να είναι μια πλήρως έγκυρη γραμμή εντολής Inkscape, αλλά χωρίς το όνομα προγράμματος Inkscape, π.χ. &#8220;file.svg &#8211;export-pdf=file.pdf&#8221;.</dd>
<dt><code>&#8211;vacuum-defs</code></dt>
<dd>Αφαιρεί όλα τα αχρησιμοποίητα στοιχεία από την ενότητα &lt;lt&gt;defs&lt;gt&gt; του αρχείου SVG. Εάν αυτή η επιλογή κληθεί σε συνδυασμό με την &#8211;export-plain-svg, μόνο το εξαγόμενο αρχείο θα επηρεαστεί. Εάν χρησιμοποιηθεί μόνη, το καθορισμένο αρχείο θα τροποποιηθεί επιτόπου.</dd>
<dt><code>-z</code>, <code>&#8211;without-gui</code></dt>
<dd>Μην ανοίγετε το GUI (σε Unix, μην χρησιμοποιείτε εξυπηρετητή X). Μόνο επεξεργασία των αρχείων από την κονσόλα. Αυτό αναλαμβάνεται για επιλογές -p, -e, -l και &#8211;vacuum-defs.</dd>
<dt><code>&#8211;g-fatal-warnings</code></dt>
<dd>Αυτή η πρότυπη επιλογή GTK εξαναγκάζει οποιεσδήποτε προειδοποιήσεις, συνήθως αβλαβείς, να προκαλέσουν εγκατάλειψη του Inkscape (χρήσιμο για αποσφαλμάτωση).</dd>
<dt><code>&#8211;usage</code></dt>
<dd>Προβολή ενός σύντομου μηνύματος χρήσης.</dd></dl>
<h2>Διαμορφωση</h2>
<p>Το κυρίως αρχείο διαμόρφωσης είναι τοποθετημένο στο ~/.config/inkscape/preferences.xml. Αποθηκεύει μια ποικιλία ρυθμίσεων διαμόρφωσης που μπορείτε να αλλάξετε στο Inkscape (συνήθως στο διάλογο προτιμήσεων του Inkscape). Επίσης στους υποκαταλόγους εκεί, μπορείτε να τοποθετήσετε το δικό σας: </p>
<p> $HOME/.config/inkscape/extensions/ &#8211; εφέ επέκτασης. </p>
<p> $HOME/.config/inkscape/icons/ &#8211; εικονίδια. </p>
<p> $HOME/.config/inkscape/keys/ &#8211; χάρτες πληκτρολογίου. </p>
<p> $HOME/.config/inkscape/templates/ &#8211; πρότυπα νέων αρχείων.</p>
<h2>Διαγνωστικα</h2>
<p>Το πρόγραμμα επιστρέφει μηδέν σε επιτυχία ή μη μηδέν σε αποτυχία. </p>
<p> Μια ποικιλία μηνυμάτων λαθών και προειδοποιήσεων μπορεί να τυπωθεί στο STDERR ή STDOUT. Εάν το πρόγραμμα συμπεριφέρεται ακανόνιστα με ένα συγκεκριμένο αρχείο SVG ή καταρρέει, είναι χρήσιμο να κοιτάξετε σε αυτή την έξοδο για στοιχεία.</p>
<h2>Παραδειγματα</h2>
<p>Αν και προφανώς το <code>Inkscape</code> σκοπεύει κυρίως ως μια εφαρμογή GUI, μπορεί επίσης να χρησιμοποιηθεί για να κάνει επεξεργασία SVG στη γραμμή εντολών επίσης. </p>
<p> Άνοιγμα ενός αρχείου SVG στο GUI: </p>
<pre> inkscape filename.svg</pre>
<p>Εκτύπωση ενός αρχείου SVG από τη γραμμή εντολών: </p>
<pre> inkscape filename.svg -p '| lpr'</pre>
<p>Εξαγωγή ενός αρχείου SVG σε PNG με την προκαθορισμένη ανάλυση των 90dpi (μια μονάδα χρήστη SVG μεταφράζει σε ένα εικονοστοιχείο ψηφιογραφίας): </p>
<pre> inkscape filename.svg --export-png=filename.png</pre>
<p>Το ίδιο, αλλά εξαναγκάζει το αρχείο PNG να είναι 600&#215;400 εικονοστοιχεία: </p>
<pre> inkscape filename.svg --export-png=filename.png -w600 -h400</pre>
<p>Το ίδιο, αλλά εξάγει το σχέδιο (οριακά πλαίσια όλων των αντικειμένων), όχι τη σελίδα: </p>
<pre> inkscape filename.svg --export-png=filename.png --export-area-drawing</pre>
<p>Εξαγωγή σε PNG του αντικειμένου με id=&#8220;text1555&#8221;, χρησιμοποιώντας το όνομα αρχείου εξόδου και την ανάλυση που χρησιμοποιήθηκε για αυτό το αντικείμενο την τελευταία φορά, όταν εξάχθηκε από το GUI: </p>
<pre> inkscape filename.svg --export-id=text1555 --export-use-hints</pre>
<p>Το ίδιο, αλλά χρήση της επιλεγμένης ανάλυσης 90 dpi, καθορισμός του ονόματος αρχείου και προσαρμογή της εξαγόμενης περιοχής προς τα έξω στις πιο κοντινές ακέραιες τιμές μονάδας χρήστη SVG (για να διατηρηθεί η ευθυγράμμιση εικονοστοιχείου των αντικειμένων και έτσι να ελαχιστοποιηθεί η εξομάλυνση): </p>
<pre> inkscape filename.svg --export-id=text1555 --export-png=text.png --export-area-snap</pre>
<p>Μετατροπή ενός εγγράφου Inkscape SVG σε απλό SVG: </p>
<pre> inkscape filename1.svg --export-plain-svg=filename2.svg</pre>
<p>Μετατροπή ενός εγγράφου SVG σε EPS, μετατρέποντας όλα τα κείμενα σε μονοπάτια: </p>
<pre> inkscape filename.svg --export-eps=filename.eps --export-text-to-path</pre>
<p>Ερώτημα πλάτους του αντικειμένου με id=&#8220;text1555&#8221;: </p>
<pre> inkscape filename.svg --query-width --query-id text1555</pre>
<p>Διπλασιασμός του αντικειμένου με id=&#8220;path1555&#8221;, περιστροφή του διπλότυπου κατά 90 μοίρες, αποθήκευση SVG και έξοδος: </p>
<pre> inkscape filename.svg --select=path1555 --verb=EditDuplicate --verb=ObjectRotate90 --verb=FileSave --verb=FileClose</pre>
<h2>Περιβαλλον</h2>
<p><code>DISPLAY</code> για λήψη του προεπιλεγμένου αριθμού υποδοχής και εμφάνισης. </p>
<p> <code>TMPDIR</code> για ορισμό του προεπιλεγμένου μονοπατιού του καταλόγου για χρήση των προσωρινών αρχείων. Ο κατάλογος πρέπει να υπάρχει. </p>
<p> <code>INKSCAPE_PROFILE_DIR</code> to set the path of the directory to use for the user profile.</p>
<h2>Θεματα</h2>
<p>Για φόρτωση διαφορετικών εικονιδίων καθορίζει αντί για το προεπιλεγμένο αρχείο $PREFIX/share/inkscape/icons/icons.svg, χρησιμοποιείται ο κατάλογος $HOME/.config/inkscape/icons/. Τα εικονίδια φορτώνονται κατ&#8217; όνομα (π.χ. <i>fill_none.svg</i>), ή εάν δεν βρεθεί τότε από <i>icons.svg</i>. Εάν το εικονίδιο δεν φορτωθεί από κάποια από αυτές τις θέσεις, επιστρέφει στην προεπιλεγμένη θέση του συστήματος. </p>
<p> Τα απαιτούμενα εικονίδια φορτώνονται από αρχεία SVG αναζητώντας για την ταυτότητα SVG με το όνομα εικονιδίου που ταιριάζει. (Π.χ., για φόρτωμα του εικονιδίου &#8220;fill_none&#8221; από ένα αρχείο, το οριακό πλαίσιο που αναζητήθηκε για ταυτότητα SVG &#8220;fill_none&#8221; αποδίδεται ως εικονίδιο, είτε έρχεται από <i>fill_none.svg</i> ή <i>icons.svg</i>.)</p>
<h2>Αλλες Πληροφοριες</h2>
<p>Η κανονική θέση για εύρεση των πληροφοριών <code>Inkscape</code> είναι στο <a rel="nofollow" href="http://www.inkscape.org/.">http://www.inkscape.org/.</a> Η ιστοσελίδα έχει νέα, τεκμηρίωση, μαθήματα, παραδείγματα, αρχείο λίστας αλληλογραφίας, την τελευταία έκδοση του προγράμματος, βάσεις δεδομένων ερωτημάτων για σφάλματα και χαρακτηριστικά και άλλα.</p>
<h2>Δειτε Επισης</h2>
<p>potrace, cairo, <i><a href="/docs/linux/man/1-rsvg/">rsvg</a></i>(1), batik, ghostscript, pstoedit. </p>
<p> πακέτο ελέγχου συμβατότητας SVG: <a rel="nofollow" href="http://www.w3.org/Graphics/SVG/Test/">http://www.w3.org/Graphics/SVG/Test/</a> </p>
<p> Επικυρωτής SVG: <a rel="nofollow" href="http://jiggles.w3.org/svgvalidator/">http://jiggles.w3.org/svgvalidator/</a> </p>
<p> <i>Scalable Vector Graphics (</i><i>SVG</i><i>) 1.1 Specification</i> <i>W3C Recommendation 14 January 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG11/">http://www.w3.org/TR/SVG11/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><i>SVG</i><i>) 1.2 Specification</i> <i>W3C Working Draft 13 November 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG12/">http://www.w3.org/TR/SVG12/</a>&gt; </p>
<p> <i></i><i>SVG 1.1/1.2/2.0</i><i> Requirements</i> <i>W3C Working Draft 22 April 2002</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG2Reqs/">http://www.w3.org/TR/SVG2Reqs/</a>&gt; </p>
<p> <i>Document Object Model (</i><i>DOM</i><i>): Level 2 Core</i> <i>Arnaud Le Hors et al editors, W3C</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/DOM-Level-2-Core/">http://www.w3.org/TR/DOM-Level-2-Core/</a>&gt;</p>
<h2>Σημειωσεις Gui</h2>
<p>Για να μάθετε για τη λειτουργία Inkscape&#8217;s GUI, διαβάστε τα μαθήματα στο Βοήθεια &gt; Μαθήματα. </p>
<p> Πέρα από SVG, το Inkscape μπορεί να εισάγει (Αρχείο &gt; Εισαγωγή) τις περισσότερες μορφές ψηφιογραφίας (PNG, BMP, JPG, XPM, GIF, κλ.), απλό κείμενο (απαιτεί Perl), PS και EPS (απαιτεί Ghostscript), PDF και μορφή AI (AI έκδοση 9.0 ή νεότερη). </p>
<p> Inkscape exports 32-bit PNG images (File &gt; Export PNG Image) as well as AI, PS, EPS, PDF, DXF, and several other formats via File &gt; Save as. </p>
<p> Το Inkscape μπορεί να χρησιμοποιήσει την πίεση και κλίση μιας πένας γραφικής πινακίδας για πλάτος, γωνία και εξαναγκασμό της επενέργειας πολλών εργαλείων, συμπεριλαμβανόμενης της καλλιγραφικής πένας. </p>
<p> Το Inkscape περιλαμβάνει ένα GUI σύστημα επικοινωνίας στη μηχανή ανίχνευσης ψηφιογραφίας Potrace (<a rel="nofollow" href="http://potrace.sf.net)">http://potrace.sf.net)</a> που ενσωματώνεται στο Inkscape. </p>
<p> Το Inkscape μπορεί να χρησιμοποιήσει εξωτερικά σενάρια (φίλτρα stdin-to-stdout) που αναπαριστάνονται από εντολές στο μενού επεκτάσεων. Ένα σενάριο μπορεί να έχει ένα διάλογο GUI για ορισμό ποικίλων παραμέτρων και μπορεί να λάβει τις ταυτότητες των επιλεγμένων αντικειμένων στα οποία δρα μέσω της γραμμής εντολών. Το Inkscape έρχεται με μια ταξινόμηση εφέ γραμμένη σε Python.</p>
<h2>Συνδυασμοι Πληκτρων</h2>
<p>Για λήψη μιας πλήρους λίστας των συντομεύσεων πληκτρολογίου και ποντικιού, δείτε doc/keys.html ή χρησιμοποιήστε την εντολή πλήκτρα και ποντίκι στο μενού βοήθειας.</p>
<h2>Σφαλματα</h2>
<p>Πολλά σφάλματα είναι γνωστά. Παρακαλώ κοιτάξτε στον ιστότοπο (inkscape.org) για να δείτε τα αναφερθέντα σφάλματα και να αναφέρετε νεοευρεθέντα θέματα. Δείτε επίσης την ενότητα γνωστών θεμάτων στις σημειώσεις έκδοσης για την έκδοσή σας (αρχείο`NEWS&#8216;).</p>
<h2>Συγγραφεις</h2>
<p>Αυτή η βάση κώδικα χρωστάει την ύπαρξη της σε ένα μεγάλο αριθμό συντελεστών μέσα από τις ποικίλες τους μεταμορφώσεις. Η ακόλουθη λίστα είναι σίγουρα ατελής, αλλά εξυπηρετεί στην αναγνώριση ότι αυτή η εφαρμογή κάθεται σε πολλούς ώμους: </p>
<p> Maximilian Albert, Joshua A. Andler, Tavmjong Bah, Pierre Barbry-Blot, Jean-François Barraud, Campbell Barton, Bill Baxter, John Beard, John Bintz, Arpad Biro, Nicholas Bishop, Joshua L. Blocher, Hanno Böck, Tomasz Boczkowski, Henrik Bohre, Boldewyn, Daniel Borgmann, Bastien Bouclet, Hans Breuer, Gustav Broberg, Christopher Brown, Marcus Brubaker, Luca Bruno, Nicu Buculei, Bulia Byak, Pierre Caclin, Ian Caldwell, Gail Carmichael, Ed Catmur, Chema Celorio, Jabiertxo Arraiza Cenoz, Johan Ceuppens, Zbigniew Chyla, Alexander Clausen, John Cliff, Kees Cook, Ben Cromwell, Robert Crosbie, Jon Cruz, Aurélie De-Cooman, Kris De Gussem, Milosz Derezynski, Daniel Díaz, Bruno Dilly, Larry Doolittle, Nicolas Dufour, Tim Dwyer, Maxim V. Dziumanenko, Johan Engelen, Miklos Erdelyi, Ulf Erikson, Noé Falzon, Frank Felfe, Andrew Fitzsimon, Edward Flick, Marcin Floryan, Fred, Ben Fowler, Cedric Gemy, Steren Giannini, Olivier Gondouin, Ted Gould, Toine de Greef, Michael Grosberg, Bryce Harrington, Dale Harvey, Aurélio Adnauer Heckert, Carl Hetherington, Jos Hirth, Hannes Hochreiner, Thomas Holder, Joel Holdsworth, Christoffer Holmstedt, Alan Horkan, Karl Ove Hufthammer, Richard Hughes, Nathan Hurst, inductiveload, Thomas Ingham, Jean-Olivier Irisson, Bob Jamison, Ted Janeczko, jEsuSdA, Lauris Kaplinski, Lynn Kerby, Niko Kiirala, James Kilfiger, Nikita Kitaev, Jason Kivlighn, Adrian Knoth, Krzysztof Kosiński, Petr Kovar, Benoît Lavorata, Alex Leone, Julien Leray, Raph Levien, Diederik van Lierop, Nicklas Lindgren, Vitaly Lipatov, Ivan Louette, Fernando Lucchesi Bastos Jurema, Pierre-Antoine Marc, Aurel-Aimé Marmion, Colin Marquardt, Craig Marshall, Ivan Masár, Dmitry G. Mastrukov, David Mathog, Matiphas, Michael Meeks, Federico Mena, MenTaLguY, Aubanel Monnier, Vincent Montagne, Tim Mooney, Derek P. Moore, Chris Morgan, Peter Moulder, Jörg Müller, Yukihiro Nakai, Victor Navez, Christian Neumair, Nick, Andreas Nilsson, Mitsuru Oka, Vinícius dos Santos Oliveira, Martin Owens, Alvin Penner, Matthew Petroff, Jon Phillips, Zdenko Podobny, Alexandre Prokoudine, Jean-René Reinhard, Alexey Remizov, Frederic Rodrigo, Hugo Rodrigues, Juarez Rudsatz, Xavier Conde Rueda, Felipe Corrêa da Silva Sanches, Christian Schaller, Marco Scholten, Tom von Schwerdtner, Danilo Šegan, Abhishek Sharma, Shivaken, Michael Sloan, John Smith, Boštjan Špetič, Aaron Spike, Kaushik Sridharan, Ralf Stephan, Dariusz Stojek, Martin Sucha, ~suv, Pat Suwalski, Adib Taraben, Hugh Tebby, Jonas Termeau, David Turner, Andre Twupack, Aleksandar Urošević, Alex Valavanis, Joakim Verona, Lucas Vieites, Daniel Wagenaar, Liam P. White, Sebastian Wüst, Michael Wybrow, Gellule Xg, Daniel Yacob, David Yip, Masatake Yamato </p>
<p> This man page was put together by Bryce Harrington &lt;brycehar [at] bryceharrington.org&gt;.</p>
<h2>Ιστορικο</h2>
<p>Ο βασικός κώδικας που θα γινόταν Inkscape ξεκίνησε τη ζωή της στο 1999 όπως το πρόγραμμα Gill, η εφαρμογή GNOME Illustrator, δημιουργημένη από τον Raph Levien. Ο δηλωμένος σκοπός για το Gill ήταν να υποστηρίξει τελικά όλο το SVG. Ο Raph υποστήριξε το πρότυπο εικόνας bezier PostScript, συμπεριλαμβάνοντας πινελιά και γέμισμα, μορφοποίηση γραμμής τέλους, μορφοποίηση ενωμένης γραμμής, κειμένου κλ. Η ιστοσελίδα του Raph Gill είναι στο <a rel="nofollow" href="http://www.levien.com/svg/.">http://www.levien.com/svg/.</a> Η δουλειά στο Gill φαίνεται να επιβραδύνθηκε ή να σταμάτησε το 2000. </p>
<p> Η επόμενη μεταμόρφωση του βασικού κώδικα ήταν να γίνει το πολύ δημοφιλές πρόγραμμα Sodipodi, καθοδηγούμενο από Lauris Kaplinski. Ο βασικός κώδικας μετατράπηκε σε ένα ισχυρό πρόγραμμα εικονογράφησης κατά τη διάρκεια πολλών χρόνων δουλειάς, προσθέτοντας πολλά καινούργια χαρακτηριστικά, πολυγλωσσική υποστήριξη, μεταφορά σε Windows και άλλα λειτουργικά συστήματα και αφαίρεση των εξαρτήσεων. </p>
<p> Το Inkscape σχεδιάστηκε το 2003 από τέσσερις ενεργούς προγραμματιστές του Sodipodi Bryce Harrington, MenTaLguY, Nathan Hurst και Ted Gould που ήθελαν να πάρουν μια διαφορετική κατεύθυνση με το βασικό κώδικα σε όρους εστίασης της συμβατότητας SVG, εμφάνισης και αίσθησης διεπαφής και μια επιθυμία ανοίγματος των ευκαιριών ανάπτυξης σε περισσότερους συμμετέχοντες. Το σχέδιο προόδευσε γρήγορα, κερδίζοντας έναν αριθμό πολύ ενεργών συντελεστών και χαρακτηριστικών. </p>
<p> Πολλή δουλειά τον πρώτο καιρό του σχεδίου εστιάστηκε στη σταθεροποίηση του κώδικα και στην διεθνοποίηση. Η αρχική σχεδίαση που κληρονομήθηκε από το Sodipodi διανθίστηκε με έναν αριθμό μαθηματικών περιπτώσεων που οδήγησε σε αναπάντεχες καταρρεύσεις, όταν το πρόγραμμα σπρώχτηκε πέρα από τις χρήσεις ρουτίνας. Αυτή η σχεδίαση αντικαταστάθηκε από το Livarot που ενώ δεν τελειοποίησε καμιά από τις δυο, ήταν σημαντικά λιγότερα επιρρεπής σε σφάλματα. Το σχέδιο υιοθέτησε επίσης μια πρακτική υποβολής κώδικα συχνά και ενεθάρρυνε τους χρήστες να τρέχουν εξελικτικά στιγμιότυπα του προγράμματος. Αυτό βοήθησε την ταυτοποίηση νέων σφαλμάτων γρήγορα και επιβεβαίωσε ότι ήταν εύκολο για χρήστες να επιβεβαιώνουν τις διορθώσεις. Ως αποτέλεσμα, οι εκδόσεις του Inkscape κέρδισαν γενικά μια φήμη ευρωστίας και αξιοπιστίας. </p>
<p> Παρόμοια, έγιναν προσπάθειες για διεθνοποίηση και τοπικοποίηση της διεπαφής, που βοήθησε το πρόγραμμα να κερδίσει συντελεστές παγκόσμια. </p>
<p> Το Inkscape είχε μια ευεργετική επίδραση στην οπτική έλξη του ανοιχτού λογισμικού γενικά, παρέχοντας ένα εργαλείο για δημιουργία και διανομή εικονιδίων, αρχικών εικόνων, τεχνών ιστότοπων κλ. Κατά κάποιο τρόπο, παρά το ότι είναι &#8220;μόνο ένα σχεδιαστικό πρόγραμμα&#8221;, το Inkscape έχει παίξει ένα σημαντικό ρόλο στη δημιουργία ανοιχτού κώδικα περισσότερο οπτικά διεγερτικού σε μεγαλύτερα ακροατήρια.</p>
<h2>Πνευματικα Δικαιωματα Και Αδεια</h2>
<p><code>Copyright (C)</code> 1999-2010 από τους συγγραφείς. </p>
<p> <code>Inkscape</code> είναι ελεύθερο λογισμικό. Μπορείτε να το αναδιανείμετε και/ή να το τροποποιήσετε με τους όρους του GPL.</p>
