---
title: "chemtool(1)"
name: "chemtool"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chemtool/"
description: "chemtool – chemical structures editor"
---

<h2 class="name">NAME</h2>
<p> chemtool &#8211; chemical structures editor</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>chemtool</code> [<i>filename</i>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>chemtool</code></p>
<dd>is a program for drawing organic molecules and exporting them as a X bitmap, PNG, PicTeX, Xfig, SVG, SXD, MDL or EPS file. It runs under the X Window System using the GTK widget set. </p>
<p> The program offers essentially unlimited undo/redo, two text fonts plus symbols, seven colors, drawing at several zoom scales, and square and hexagonal backdrop grids for easier alignment. </p>
<h2>EXAMPLES</h2>
<p> In all drawing and editing modes, mouse button one (usually the left button) is used to mark or draw objects, while button three (the right button) can be used to delete objects of the current type. The middle button is mainly used in the bond drawing modes where it allows fast changing of bondtypes. Starting with version 1.5, the default storage directory for datafiles, and the filename extension to use, can be saved via a configuration dialog.</p>
<h3>Drawing of bonds:</h3>
<p> Bonds can be drawn in 4 different angle settings (hexagon with 30&#176; intervals, two pentagons with 72&#176; intervals (different orientation), and a 45&#176; i octagon). (Intermediate angles are possible in all of these modes as well &#8211; just ignore the marker points in this case). </p>
<p> The bond style chooser in the center of the button bar determines the type of bond that is drawn &#8211; initially, this is a single bond. If you want to change the type of a bond later, either click on it with the middle button of your mouse to advance to the next type(s), or select the appropriate type in the chooser and then switch to bondtype mode and pick all bonds that you want to change over to the new type. (The color used for the bond is updated at the same time if necessary.) Pressing the middle mousebutton on a bond when in &#8216;Bondtype&#8217; mode reverses the direction of that bond. </p>
<p> Using the third (usually the right) mouse button deletes the bond next to the cursor position. </p>
<p> The available bond types are: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> single bond</p>
<dt>&bull;</p>
<dd> double bond</p>
<dt>&bull;</p>
<dd> double bond (shorter line on the other side)</p>
<dt>&bull;</p>
<dd> centered double bond</p>
<dt>&bull;</p>
<dd> triple bond (flanking lines shorter than central)</p>
<dt>&bull;</p>
<dd> triple bond (with equal line lengths)</p>
<dt>&bull;</p>
<dd> quadruple bond</p>
<dt>&bull;</p>
<dd> wedge-shaped bond</p>
<dt>&bull;</p>
<dd> dashed wedge-shaped bond</p>
<dt>&bull;</p>
<dd> wavy line</p>
<dt>&bull;</p>
<dd> half arrow</p>
<dt>&bull;</p>
<dd> regular arrow</p>
<dt>&bull;</p>
<dd> wide bond</p>
<dt>&bull;</p>
<dd> circle</p>
<dt>&bull;</p>
<dd> dotted line</p>
<dt>&bull;</p>
<dd> overlapping single bond (which cuts out a segment from any bond it crosses)</p>
<dt>&bull;</p>
<dd> light pi orbital lobe</p>
<dt>&bull;</p>
<dd> dark pi orbital lobe</dl>
</dl>
<h3>Semiautomatic drawing of rings:</h3>
<p> Rings of 3 to 12 members can be drawn easily by holding down the Ctrl key while drawing a line. This line will then become the first segment of a ring that is automatically drawn in clockwise direction. The size of the ring defaults to that appropriate for the selected drawing mode (i.e. 5, 6 or 8 sides), but it can be set on a per-ring basis by pressing Ctlr-&lt;number&gt; before drawing the ring, where numbers 3-9 correspond to 3 to 9-membered rings, while 0 to 2 select 10, 11 and 12-membered rings, respectively. </p>
<p> Newly drawn rings can be deleted by pressing Ctrl and mouse button 3 together. </p>
<h3>Drawing of curved lines:</h3>
<p> Curved lines for objects like arrows or orbital lobes can be drawn in spline curve mode by specifying four control points that form a bounding polygon (startpoint, two points on either side of the peak, endpoint). Of the regular bondtypes available in the Style menu, the &#8216;single line&#8217;, &#8216;semiarrow&#8217;, arrow and &#8216;dashed line&#8217; retain their usual function, while the &#8216;wide line&#8217; type is used to denote a filled polygon. The control points are only visible in <i>Move </i> mode, where they can be dragged around to change the form of a curve after it is drawn. </p>
<h3>Setting bond style</h3>
<p> In bond style mode, clicking on any bond in the diagram changes its representation to the type selected in the pull-down menu next to the <i>Type </i> button. </p>
<p> The additional bond type available in the pulldown menu, </p>
<dl>
<dt>
<dd> curved arrow</dl>
<p> is only available for drawing. It is actually a shortcut for one of the curve drawing functions described above, with the second and third control points automatically generated. As such, it can not be converted to or from any of the conventional bond types. </p>
<p> (One can, however, convert it to any of the other curve types, e.g. to change the type of arrowhead). The shape of the arrow will usually need to be adjusted by shifting the control point that appears alongside it in &#8216;Move&#8217; mode. </p>
<h3>Inserting text</h3>
<p> Text written into the text box can be positioned with the cursor and may appear left, middle or right-aligned in the drawing. Text size and color is selectable from a fixed list of choices. There are two special characters to be used for sub- and superscripting the following character: </p>
<dl>
<dt>
<dd> &#8216;^&#8217; to shift up <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(e.g. N^+)</p>
<p> &#8216;_&#8217; to shift down<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(e.g. CH_3)
</dl>
<p> The control character &#8216;|&#8217; is used to italicise the following character, as in |t-Bu. </p>
<p> A bold fonttype, typically used for numbering compounds, can be selected by preceding the character with a &#8216;#&#8217;. </p>
<p> The special character &#8216;@&#8217; switches to symbol mode, which uses the standard X11 symbol font. All alphabetic keys produce the corresponding Greek characters in this mode, and several other symbols are available if their standard Latin1 equivalents are already mapped onto the keyboard: </p>
<dl>
<dt>
<dd> yen -&gt; infinity </p>
<p> hyphen -&gt; uparrow </p>
<p> macron -&gt; downarrow</dl>
<p> The symbols &#8216;plusminus&#8217; and &#8216;registered&#8217; (trademark) are already in the standard font, although they are not normally available on the keyboard. Use the following commands (or add the declarations to your <i>.xmodmaprc</i> ) to make them available via &lt;AltGr&gt;+&lt;Key&gt; (&lt;RightAlt&gt;+&lt;Key&gt;): </p>
<dl>
<dt>
<dd> xmodmap -e &#8216;keysym r = r R registered&#8217; \<br />
&nbsp;<wbr>&nbsp;<wbr>-e&nbsp;<wbr>&#8216;keysym o&nbsp;<wbr>=&nbsp;<wbr>o O yen&#8217;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-e&nbsp;<wbr>&#8216;keysym p&nbsp;<wbr>=&nbsp;<wbr>p P plusminus&#8217;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-e&nbsp;<wbr>&#8216;keysym u&nbsp;<wbr>=&nbsp;<wbr>u U hyphen&#8217;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-e&nbsp;<wbr>&#8216;keysym d&nbsp;<wbr>=&nbsp;<wbr>d D macron&#8217;</dl>
<p> (this leads to AltGr-P = plusminus, AltGr-R = registered in normal mode and AltGr-O = infinity, AltGr-U = uparrow, AltGr-D = downarrow in symbol font). </p>
<p> For &#8216;dots-and-crosses&#8217; diagrams, the following mappings to the symbol font might be useful: acute -&gt; cross (e.g. keysym x = x X acute) middle dot -&gt; filled dot (e.g. keysym d = d D periodcentered) (using the degree sign for the open dot). </p>
<p> Circled versions of the plus and minus signs for denoting ionic charge are available as @+ and @- . </p>
<p> When you want to use symbols as sub- or superscripts, place the sub- or superscripting character before the &#8216;@&#8217; character, e.g. K_@a . </p>
<p> In text mode, the right mouse button deletes the label at the cursor position. Changing the size, font or color of a label can be done by left-clicking on it after choosing the desired combination of settings. When the text entry box above the drawing area is empty, only the settings are updated without changing the contents of the label, otherwise the label text is replaced as well. If you want to copy the text of an existing label to the text entry box, click on it with the middle mouse button. </p>
<h3>Labeling shortcuts</h3>
<p> In all bond drawing modes, several keyboard shortcuts are available to add atom symbols without having to leave drawing mode. The label is placed at the current drawing position (the endpoint of the last line drawn, or the spot last clicked on). </p>
<p> The keys &#8216;c&#8217;,&#8217;h&#8217;,&#8217;n&#8217;,&#8217;o&#8217;,&#8217;s&#8217;,&#8217;p&#8217; and &#8216;r&#8217; insert the corresponding capital letter, &#8216;l&#8217; (lowercase L) inserts &#8216;Cl&#8217;, while &#8216;1&#8217;, &#8216;2&#8217;, &#8216;3&#8217; insert CH,CH_2 and CH_3, respectively. The asterisk key (*) inserts a filled circle. </p>
<p> Pressing the space bar once allows you to enter arbitrary labels, which will be placed at the current position when you press the Return key. </p>
<h3>Drawing electron pairs</h3>
<p> The keys of the numeric keypad can be used to draw short &#8216;electron pair&#8217; lines next to an element symbol &#8211; if one imagines the element symbol to be sitting on the central &#8216;5&#8217; key, each key draws the appropriate electron pair for its position. When used together with the Shift key, two dots are drawn instead of a line &#8211; simply delete one of the dots again if you need an odd number of electrons. </p>
<h3>Numbering atoms</h3>
<p> For quick numbering of the atoms in a molecule, switch to one of the text modes, hold down the Control key and pick each atom in succession with the left mouse button. Numbering starts at 1, and the sequence can be reset at any time by clicking the right mouse button. If you need to use your own numbering scheme, clicking the middle button (while still holding down the Control key) makes it pick up whatever number is in the text entry field. </p>
<h3>Centering</h3>
<p> If there is not enough space for your molecule you can put it in the middle of the sheet with the center button. </p>
<h3>Exporting to foreign formats:</h3>
<p> You can export your molecules as an X bitmap, a PNG or EMF image, an encapsulated postscript file, an input file for Brian Smith&#8217; <code><a href="/docs/linux/man/1-xfig/">xfig</a></code>(1) program, an MDL ver. 2000 molfile for data exchange with commercial packages, an SVG file for XHTML web pages, or in the PicTeX format for direct inclusion in LaTeX documents. The PicTeX, PNG, EMF and Postscript output functions rely on the <code>fig2dev</code>81) program from the <code><a href="/docs/linux/man/1-transfig/">transfig</a></code>(1) package and are only available when this program was detected on startup. If the <code><a href="/docs/linux/man/1-fig2sxd/">fig2sxd</a></code>(1) program is installed, an additional export option is available for OpenOffice SXD format. Likewise, if the (open)babel program is installed, an additional Export menu providing access to all filetypes supported by this tool becomes available. </p>
<p> You can create the outputs in different sizes according to the current zoom scale. Postscript and PicTeX files can also be created at arbitrary scales selectable on the export file menu. </p>
<p> An option in the configuration menu can be set to call <code>fig2dev</code> in international language mode, which will automatically render any text written in the alternate (Times) font using the postscript font appropriate for the current locale (currently Croatian, Cyrillic, Czech, Hungarian, Japanese, Korean, Polish). See the <code>fig2dev</code> documentation for details. </p>
<p> To include the PicTeX-file in your LaTeX document, you will need the pictex macro package. Depending on the versions you use, you might also have to load the &#8216;color&#8217; package in the preamble of your LaTeX file. If you experience &#8216;TeX capacity exceeded&#8217; error messages, increase the extra_mem_bot parameter in your <i>texmf.cnf</i> file (usually in <i>/usr/share/texmf/web2c</i>, <i>/usr/local/texmf</i> or <i>/etc/texmf</i>). Pictex is known for its unusual (by tex standards) memory requirements, and the standard settings do not account for this (although you may find a comment a la &#8216;change this if you use pictex&#8217; in the <i>texmf.cnf</i> file). Something like extra_mem_bot=400000 should not hurt on any moderately modern system. </p>
<h3>Printing drawings</h3>
<p> Since version 1.5, direct printing of diagrams to a Postscript-capable printing device (or more typically a print queue running ghostscript) is possible. The paper size, magnification, printer name and the print command to use (currently either <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1) or <code><a href="/docs/linux/man/1-kprinter/">kprinter</a></code>(1)) can be stored in the Configuration Dialog. </p>
<h3>Selecting all or parts of a drawing for transformations:</h3>
<p> Using the &#8216;Mark&#8217; button, you can easily select parts of the current drawing by enclosing them with a &#8216;rubberband&#8217; rectangle. </p>
<p> If you need to add atoms outside of the rectangular area to your selection, simply draw another rubberband around them while holding down the Ctrl key. </p>
<p> The selected parts will appear highlighted in blue and are immediately available for </p>
<dl>
<dt><i>moving</i></p>
<dd> simply drag the fragment to the desired position with the mouse while holding down the left mouse button. (If you only need to move individual atoms or bonds, you can simply pick and drag them in &#8216;Move&#8217; mode without having to mark them first).</p>
<dt><i>rotating</i></p>
<dd> horizontal movement of the mouse translates to smooth rotation around the pivot point selected when pressing the mouse button</p>
<dt><i>flipping </i></p>
<dd> (mirroring) the fragment about a horizontal or vertical mirror plane through its center: this is performed by clicking on the appropriate menu button</p>
<dt><i>copying</i></p>
<dd> clicking on the &#8216;Copy&#8217; menu button creates an exact copy of the selected fragment slightly offset to the original. The mark is automatically transferred to the new copy.</p>
<dt><i>rescaling</i></p>
<dd> horizontal mouse movement is translated into a smooth increase or decrease of size of the marked fragment</p>
<dt><i>deleting</i></p>
<dd> to delete the marked fragment, simply click the third (usually the right) mouse button after it is highlighted.</p>
<dt><i>framing</i></p>
<dd> choosing one of the icons from the drop-down list of frame and bracket styles draws the corresponding object, e.g. a pair of round parentheses, around the highlighted fragment.</p>
<dt><i>optimizing</i></p>
<dd> clicking on the &#8216;bucket and broom&#8217; symbol invokes a function that removes overlapping (duplicate) bonds and labels from the drawing and straightens lines that are almost horizontal or vertical. </p>
</dl>
<h3>Adding previously saved figures:</h3>
<p> To add another molecule from a previously saved chemtool drawing, select it in the file selection window that comes up when you press the &#8216;Add&#8217; button. Single clicking on any filename in the list displays a small preview of the molecule to aid in selection. The newly added molecule is automatically made active so that it can be repositioned as desired. </p>
<p> If you want to add it to a predefined position on another molecule, you can mark that attachment site by left-clicking on it instead of dragging the marker rectangle. A small green dot will appear at what is now the reference position for the new part. If you save molecules with such a marker set, it will in turn define their attachment site when they are added to another drawing. </p>
<h3>Adding one of the predefined templates:</h3>
<p> Selecting &#8216;Templates&#8217; from the &#8216;Tools&#8217; menu opens a second window with a small collection of predefined structures. Simply click on the image of the desired molecule to add it to your drawing. The Template window can be kept open throughout a chemtool session &#8211; if it is hidden by another window, you can move it to the front by selecting the &#8216;Template&#8217; menu in chemtool again. </p>
<p> The data in the template system differ from normal chemtool drawings only by the fact that they are stored within the program, and in a slightly awkward format (x and y coordinates listed separately in the source file templates.h). These are meant to provide a convenient basis set available to all users, but not individually extendable (you can use the &#8216;Add&#8217; function for your own structures). Please let us know if you want specific molecules added to the templates &#8211; their name or ideally a regular chemtool drawing file is all we need. (send email to martin [at] ruby.chemie.uni-freiburg.de) </p>
<h3>Importing foreign file formats:</h3>
<p> Chemtool provides functions for importing files in both the PDB format used by the Protein Database (and by most molecular modeling packages) and the proprietary MDL molfile format used by ISISdraw and understood by other structure drawing packages and database frontends. </p>
<p> As both are 3D file formats, while chemtool only handles 2D projections, imported molecules are read into a temporary storage at first and displayed in blue on the canvas. This 3D representation can then be rotated using the mouse. Only after pressing the Return key on the keyboard is it converted into the final 2D projection that can be edited. While such a 3d import is in progress, all normal drawing and editing functions are disabled. </p>
<p> With MDL molfile import, the carbon atom labels are automatically discarded. For PDB import, the amount of labeling can be chosen in the file selection dialog, which offers retention of either all labels, only those of non-hydrogen atoms, or only the non-numeric part of the labels. </p>
<p> If the program babel is installed &#8211; either the original version written by Pat Walters or the more recent OpenBabel effort &#8211; chemtool will automatically offer a menu option for importing from any of the file formats this supports. </p>
<h3>Determining sum formula and molecular weight:</h3>
<p> The distribution contains a helper program, <code><a href="/docs/linux/man/1-cht/">cht</a></code>(1), by Radek Liboska (Prague) to calculate sum formula and (exact) molecular weight from a chemtool drawing file. It is also available from within chemtool to calculate these data for the current structure or a marked fragment of it. <code>cht</code> can be misled by duplicate bonds ( chemtool does not remove overlapping bonds, such as they might result from fusing ring systems, automatically) and by the &#8216;aromatic ring&#8217; symbol, so you should avoid these and check the plausibility of the generated sum formula where possible. </p>
<h3>Drawing functions not available within Chemtool:</h3>
<p> For features not currently supported by chemtool, like general line-drawing functions, getting Brian Smith&#8217;s XFig drawing package <code>xfig</code> is highly recommended. About the only thing it does not offer is support for &#8216;chemical&#8217; linetypes and drawing angles &#8211; which is why chemtool was written as a sort of companion program. (There will probably be more of the most sorely needed drawing options added to chemtool over time, but duplicating the more general-purpose features of <code>xfig</code> seems rather pointless.) </p>
<h2>LICENSE</h2>
<p> <code>chemtool</code> and its companion program <code>cht</code> are available under the terms of the GNU General Public License (see the file &#8216;COPYING&#8217; in the package). This software comes with ABSOLUTELY NO WARRANTY. </p>
<h2>AUTHORS</h2>
<dl>
<dt><code>Thomas Volk</code></p>
<dd> Original author and maintainer up to 1.1.1.</p>
<dt><code>Dr. Martin Kroeker </code>&lt;martin [at] ruby.chemie.uni-freiburg.de&gt;</p>
<dd> Maintainer and primary author since 1.1.2.</dl>
<p> <code>Radek Liboska, PhD </code>&lt;liboska [at] uochb.cas.cz&gt; </p>
<p> <code>Michael Banck </code>&lt;mbanck [at] gmx.net&gt; </p>
<p> and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-babel/">babel</a></code>(1), <code><a href="/docs/linux/man/1-cht/">cht</a></code>(1), <code><a href="/docs/linux/man/1-fig2dev/">fig2dev</a></code>(1), <code><a href="/docs/linux/man/1-fig2sxd/">fig2sxd</a></code>(1), <code><a href="/docs/linux/man/1-transfig/">transfig</a></code>(1), <code><a href="/docs/linux/man/1-xfig/">xfig</a></code>(1) </p>
<p> Homepage:<br />
 <i><a rel="nofollow" href="http://ruby.chemie.uni-freiburg.de/~martin/chemtool/chemtool.html">http://ruby.chemie.uni-freiburg.de/~martin/chemtool/chemtool.html</a></i> </p>
<h2>Index</h2>
