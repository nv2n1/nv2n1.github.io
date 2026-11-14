---
title: "cdlabelgen(1)"
name: "cdlabelgen"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdlabelgen/"
description: "cdlabelgen – CD/DVD labels, jewel case inserts, and envelopes creator. Generates frontcards and traycards for CD cases, single-cd envelopes, DVD case inserts, as well as output suitable for direct ..."
---

<h2 class="name">NAME</h2>
<p> cdlabelgen &#8211; CD/DVD labels, jewel case inserts, and envelopes creator. Generates frontcards and traycards for CD cases, single-cd envelopes, DVD case inserts, as well as output suitable for direct printing on CD/DVD. </p>
<h2>SYNOPSIS</h2>
<p> cdlabelgen [ <code>-c</code> &lt;category&gt; <code>-s</code> &lt;subcategory&gt; <code>-i</code> &lt;item1%item2%etc&gt; <code>-f</code> &lt;itemsfile&gt; <code>-v</code> &lt;num_items_cover&gt; <code>-e</code> &lt;cover_epsfile&gt; <code>-S</code> &lt;cover_eps_scaleratio&gt;[,&lt;image_x_offset&gt;,&lt;image_y_offset_inches&gt;] <code>-E</code> &lt;tray_epsfile&gt; <code>-T</code> &lt;tray_eps_scaleratio&gt;[,&lt;image_x_offset&gt;,&lt;image_y_offset_inches&gt;] <code>-d</code> &lt;date&gt; <code>-D</code> <code>-o</code> &lt;outputfile&gt; <code>-t</code> &lt;template&gt; <code>-b</code> <code>-C</code> <code>-w</code> <code>-h</code> <code>-m</code> <code>-M</code> <code>-O</code> <code>-p</code> <code>-y</code> &lt;page_offset_inches&gt; <code>-l</code> &lt;line_width_points&gt;] <code>&#8211;create-dvd-inside</code> <code>&#8211;create-dvd-outside</code> <code>&#8211;slim-double-case</code> <code>&#8211;double-case</code> <code>&#8211;create-cdlabel</code> <code>&#8211;rotate-endcaps</code> <code>&#8211;plaque-color</code> &lt;r,g,b&gt; <code>&#8211;category-color</code> &lt;r,g,b&gt; <code>&#8211;subcategory-color</code> &lt;r,g,b&gt; <code>&#8211;text-color</code> &lt;r,g,b&gt; <code>-n</code> &lt;volume/number in set&gt; <code>&#8211;rows-columns</code> &lt;row_count_for_items,column_count_for_items&gt; <code>&#8211;tray-overlay</code> &lt;overlay_epsfile&gt; <code>&#8211;tray-overlay-scaleratio</code> &lt;tray_overlay_image_scaleratio&gt;[,&lt;image_x_offset&gt;,&lt;image_y_offset_inches&gt;]</p>
<h2>VERSION</h2>
<dl>
<dt>Version 4.2.0, April 2012</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> cdlabelgen&#8217;s purpose in life is twofold:</p>
<dl>
<dt>&bull;</p>
<dd> To be run automatically and swiftly from a shell script and automatically generate a frontcard and a traycard for a cd&#8212;usually data archive cd&#8217;s. The traycard (which goes behind the <font SIZE="-1">CD</font> itself) is U-shaped and the ends of the <font SIZE="-1">CD</font> case bear the label of what the <font SIZE="-1">CD</font> is. Inside inserts for DVDs are also supported.</p>
<dt>&bull;</p>
<dd> To have a minimum of dependencies&#8212;cdlabelgen only requires perl.</dl>
<p> cdlabelgen was designed to simplify the process of generating labels for <font SIZE="-1">CD</font>&#8216;s. It originated as a program to allow auto generation of frontcards and traycards for <font SIZE="-1">CD</font>&#8216;s burned via an automated mechanism (specifically for archiving data), but has now become popular for labelling <font SIZE="-1">CD</font> compilations of mp3&#8217;s, and copies of CDs. Note that cdlabelgen does not actually print anything&#8212;it just spits out postscript, which you can then do with as you please. It can also be combined with output from other programs such as &#8220;barcodegen&#8221; &#8211; to print a barcode as a tray overlay image. </p>
<p> The latest version of cdlabelgen as well as this document can be found at <a rel="nofollow" href="http://www.aczoom.com/tools/cdinsert/.">http://www.aczoom.com/tools/cdinsert/.</a> The software package includes <font SIZE="-1">CGI</font> scripts that can be used to serve cdlabelgen over the internet. An older version may be available at: <a rel="nofollow" href="http://www.red-bean.com/~bwf/software/cdlabelgen/.">http://www.red-bean.com/~bwf/software/cdlabelgen/.</a> </p>
<p> cdlabelgen comes with several eps images for you to use on your labels. These images can be found in /usr/local/lib/cdlabelgen or /usr/share/cdlabelgen or /opt/lib/cdlabelgen/ or /usr/local/share/cdlabelgen, depending on your installation. Included are a Recycling icon, an mp3 icon, the Compact Disc icon (with and without &#8216;Digital&#8217; on it), Tux the penguin, and the new Debian &#8216;swirl&#8217; logo. Two color background images called Music Notes are also available. </p>
<p> CDs: cdlabelgen prints a &#8216;tongue&#8217; as part of the traycard. This folds around and is viewable from the front in jewel boxes that are entirely clear (<font SIZE="-1">CD</font> holder piece is not opaque). If you do not have a clear <font SIZE="-1">CD</font> holder in your jewel box, you may find it easier to just cut the &#8216;tongue&#8217; off&#8212;it&#8217;s a bit easier to fold without it. </p>
<p> Paper Sizes: Normal <font SIZE="-1">CD</font> cases, Slim <font SIZE="-1">CD</font> cases, <font SIZE="-1">DVD</font> inside inserts can be printed on a letter or A4 sized page. <font SIZE="-1">CD/DVD</font> Envelopes and <font SIZE="-1">DVD</font> outside inserts will not fit on a letter sized paper, a larger paper size will be needed to make it fit. </p>
<p> cdlabelgen requires Perl Version 5.003 or greater. Ghostscript is not required, but <code>is</code> recommended so that you can test out your labels without wasting paper.</p>
<h2>SWITCHES</h2>
<dl>
<dt><code>-c, &#8211;category &lt;category</code>&gt;</p>
<dd> Set the category (title) for the <font SIZE="-1">CD</font></p>
<dt><code>-s, &#8211;subcategory &lt;subcategory</code>&gt;</p>
<dd> Set the subcategory (subtitle) for the <font SIZE="-1">CD</font></p>
<dt><code>-i, &#8211;items &lt;items</code>&gt;</p>
<dd> &#8216;items&#8217; should be a &#8216;%&#8217; separated list of items to print on the traycard of the <font SIZE="-1">CD</font>. Note that if the number of items are too many to fit on the tray card, cdlabelgen will leave out some items at the end. cdlabelgen automatically flows the items into 2, 3, 4, or 5 columns and scales the fontsize accordingly, unless the <tt>&quot;-P&quot;</tt> option is used. You can insert blank lines by inserting 2 percent signs in a row into the items list.</p>
<dt><code>-f, &#8211;items-from-file &lt;filename</code>&gt;</p>
<dd> Get item names from file named filename. Each item should be on its own line separated by carriage returns. cdlabelgen automatically flows the items into 2, 3, 4, or 5 columns and scales the fontsize or clips the items as needed. You can insert blank lines by placing blank lines between items in this file. </p>
<p> Special commands can be embedded in the file, all of these commands should be present starting at the first column of the line. The codes are used to change the font for an item, the code itself is not printed in the output. </p>
<pre><code>
{#BI} - make the item bold and italic{#I} - make the item italic{#B} - make the item bold{#M} - make the item mono - spaced(Courier font){#MB} - make the item monospaced and bold(Courier - Bold font)
</code></pre>
<p> Example: </p>
<pre>
 {#MB}    Text 1 Item
would print the line &quot;    Text 1 Item&quot; in a monospaced bold font.
</pre>
<dt><code>-v, &#8211;cover-items &lt;number_of_items_for_cover</code>&gt;</p>
<dd> Normally, all the items are printed on the tray card. But if you have a large number of items, you may wish to print some items on the cover, and rest on the tray card. This option provides a way of specifying how many items should be printed on the cover. Default is 0 (i.e., print no item on the cover, print all items on the tray). The items to be printed on the cover are taken from the list of items, from the top of the list. Note that if the number of items is too many to fit on the cover, it will result in items being dropped. As of Jan 2002, around 250-300 items can be fitted on the cover or the tray, depending on whether a title/subtitle/date is used or not.</p>
<dt><code>-d, &#8211;date &lt;date</code>&gt;</p>
<dd> Set the date to be used as &#8216;date&#8217; if not set or not overridden with the <code>-D</code> flag, today&#8217;s date will be used (default is today&#8217;s date). Use this option if you don&#8217;t like cdlabelgen&#8217;s default format of YYCC-MM-YY, for example.</p>
<dt><code>-D, &#8211;no-date</code></p>
<dd> Do not print <code>any</code> date (overrides <code>-d</code> as well)</p>
<dt><code>-e, &#8211;cover-image &lt;cover_epsfile</code>&gt;</p>
<dd> Filename of eps file to print on cover. Note that cdlabelgen requires that the eps file contain a proper &#8216;%%BoundingBox LLx LLy URx URy&#8217; declaration according to the PostScript Document Structuring Conventions. cdlabelgen uses this line to determine the dimensions of the eps graphic so that it can position it appropriately on the cover. Note that cdlabelgen first looks for this file in your working directory. If it doesn&#8217;t find it there, it will look in the list of directories where the default eps files are stored (see <tt>@where_is_the_template</tt>). This makes it easy to use the images shipped with cdlabgelgen without typing miles of pathnames.</p>
<dt><code>-S, &#8211;cover-image-scaleratio &lt;cover_eps_scaleratio [,image_x_offset,image_y_offset_inches]</code>&gt;</p>
<dd> The ratio by which you want to scale the epsfile that appears on the cover. If you omit this flag, cdlabelgen assumes a scaleratio of 1.0. This flag allows you to squeeze larger graphics into the cover or expand smaller graphics to fill the cover. Scaleratio must be a number (int or float). </p>
<p> If the scale value passed is 0 (or 0.0), then the logo is used as a background image &#8211; it will be scaled as required to fit the entire cover. </p>
<p> The -S option also takes optional translate arguments. Normally images are printed on the cover and the tray so that the bottom-right of the image is anchored to the bottom-right of the cover or tray. To move the images away from the bottom and right borders, use this option. For example, to leave two inches of gap between the image and the bottom border, and 0.5 inches from the left border, and use 1.0 scaleratio, use this: <code>-S 1.0,-2,0.5</code> </p>
<p> This offset only applies when the image is being used as a logo &#8211; i.e., image is not being used as background to fill the entire cover or tray.</p>
<dt><code>-E, &#8211;tray-image &lt;tray_epsfile</code>&gt;</p>
<dd> Filename of eps file to print on traycard. Note that cdlabelgen requires that the eps file contain a proper &#8216;%%BoundingBox LLx LLy URx URy&#8217; declaration according to the PostScript Document Structuring Conventions. cdlabelgen uses this line to determine the dimensions of the eps graphic so that it can position it appropriately on the cover. Note that cdlabelgen first looks for this file in your working directory. If it doesn&#8217;t find it there, it will look in the list of directories where the default eps files are stored (see <tt>@where_is_the_template</tt>). This makes it easy to use the images shipped with cdlabgelgen without typing miles of pathnames.</p>
<dt><code>-T, &#8211;tray-image-scaleratio &lt;tray_eps_scaleratio [,image_x_offset,image_y_offset_inches]</code>&gt;</p>
<dd> The ratio by which you want to scale the epsfile that appears on the traycard. If you omit this flag, cdlabelgen assumes a scaleratio of 1. This flag allows you to squeeze larger graphics into the traycard or expand smaller graphics to fill the traycard. Scaleratio must be a positive number (int or float) specifying the scale. </p>
<p> If the scale value passed is the word <code>fill1</code>, then the image is used as a background &#8211; it is scaled so that it completely fills the interior tray card region. The value <code>0</code> (or 0.0) works same as the <code>fill1</code> argument. </p>
<p> If the value passed is the word <code>fill2</code>, then the image is used as a background to fill more than just the tray. For normal <font SIZE="-1">CD</font> cases, the image is scaled so that it completely fills both the tray card region, and the two endcaps (but not the extreme right-hand &#8216;tongue-cap&#8217;) for normal cd cases. For Slim <font SIZE="-1">CD</font> cases or <font SIZE="-1">DVD</font> Inside/Outside covers, the tray image will fill both the tray and cover regions (including any spines). For directly printing on a <font SIZE="-1">CD</font> (&#8211;create-cdlabel), fill2 option works like the fill1 option. </p>
<p> The -T option also takes optional translate arguments. Normally images are printed on the cover and the tray so that the bottom-right of the image is anchored to the bottom-right of the cover or tray. To move the images away from the bottom and right borders, use this option. For example, to leave two inches of gap between the image and the bottom border, and 0.5 inches from the left border, and use 1.0 scaleratio, use this: <code>-T 1.0,-2,0.5</code> </p>
<p> This offset only applies when the image is being used as a logo &#8211; i.e., image is not being used as background to fill the entire cover or tray.</p>
<dt><code>-o, &#8211;output-file &lt;outputfile</code>&gt;</p>
<dd> If the <code>-o</code> flag is used, cdlabelgen prints to outputfile instead of <font SIZE="-1">STDOUT</font>.</p>
<dt><code>-t, &#8211;template &lt;template</code>&gt;</p>
<dd> Specify explicitly which template to use. This is useful if you need to debug the PostScript code in the template, use a different template, or if you have created your own template to use in lieu of the one provided with cdlabelgen.</p>
<dt><code>-b, &#8211;no-tray-plaque</code></p>
<dd> Suppresses printing of the Plaque on the traycard, thus allowing you to either fit even more items on the traycard, or to use a slightly larger font size for the items.</p>
<dt><code>-C, &#8211;no-cover-plaque</code></p>
<dd> Suppresses printing of the plaque on the front cover, thus allowing a cover image that fills the front cover, but still displaying category and sub-category information in the other usual places.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> print out the usage message</p>
<dt><code>-w, &#8211;tray-word-wrap</code></p>
<dd> Enables word wrapping of the items that print on the traycard. Note that this is *not* extensively tested and may be buggy! Make sure that you preview your label before printing it if you use this flag. </p>
<p> If there is a problem with <tt>&quot;-w&quot;</tt>, the best option right now is to split lines in the input itself, and to omit the <tt>&quot;-w&quot;</tt> option.</p>
<dt><code>-m, &#8211;slim-case</code></p>
<dd> Creates covers suitable for use in slim cd-cases, this means no tray card (the tray card is now the inside front cover). This creates a two page, folding cover insert. This could also be used in normal cd cases as an inside insert. </p>
<p> Slim case option can be used with outside dvd inserts ( &#8211;create-dvd-outside ) also &#8211; in which case the outside insert is created for half-height <font SIZE="-1">DVD</font> case.</p>
<dt><code>-O, &#8211;outside-foldout</code></p>
<dd> Output slim cd cover cases (or dvd inserts) with the order of the pages switched so the folding line lies on the outside of a normal case. Can be used when printing either the slim-cd-case or dvd-inside inserts. </p>
<p> This option is best used along with option -m (&#8211;slim-case) or &#8211;create-dvd-inside.</p>
<dt><code>&#8211;rotate-endcaps</code></p>
<dd> Endcap text is rotated by 180 degrees, to flip the text around.</p>
<dt><code>-M, &#8211;create-envelope</code></p>
<dd> Creates covers suitable for use as envelopes for a <font SIZE="-1">CD</font>. Guide lines are printed, to aid in folding the printout correctly.</p>
<dt><code>&#8211;create-dvd-inside</code></p>
<dd> Creates inserts suitable for use as inside insert for a normal <font SIZE="-1">DVD</font> case. Guide lines are printed, to aid in folding the printout correctly. Note: <font SIZE="-1">DVD</font> inserts may not print fully on Letter or A4 sized paper printers; it may require larger paper sizes.</p>
<dt><code>&#8211;create-dvd-outside</code></p>
<dd> Creates inserts suitable for use as outside cover inserts for a normal <font SIZE="-1">DVD</font> case. Guide lines are printed, to aid in folding the printout correctly. Note: <font SIZE="-1">DVD</font> inserts may not print fully on Letter or A4 sized paper printers; it may require larger paper sizes. </p>
<p> Slim case option ( &#8211;slim-case ) can be used with outside dvd inserts also &#8211; in which case the outside insert is created for half-height <font SIZE="-1">DVD</font> case.</p>
<dt><code>&#8211;double-case</code></p>
<dd> Create covers for double-sided <font SIZE="-1">DVD</font> cases that hold 6 DVDs. Only double-width <font SIZE="-1">DVD</font> cases are supported, double-width <font SIZE="-1">CD</font> cases are not supported. Therefore, using &#8211;double-case also implies the &#8211;create-dvd-outside option. Note: <font SIZE="-1">DVD</font> inserts may not print fully on Letter or A4 sized paper printers; it may require larger paper sizes.</p>
<dt><code>&#8211;slim-double-case</code></p>
<dd> Create covers for double-sided <font SIZE="-1">DVD</font> cases that hold 6 DVDs in boxes 1.5 times the depth of normal dvd cases. Only <font SIZE="-1">DVD</font> cases are supported with this option, slim-double-width <font SIZE="-1">CD</font> cases are not supported. Therefore, using &#8211;slim-double-case also implies the &#8211;create-dvd-outside option. Note: <font SIZE="-1">DVD</font> inserts may not print fully on Letter or A4 sized paper printers; it may require larger paper sizes.</p>
<dt><code>&#8211;create-cdlabel</code></p>
<dd> For directly printing on a <font SIZE="-1">CD</font> or <font SIZE="-1">DVD</font>. As of January 2005, there are inkjets printers that can print on certain types of blank <font SIZE="-1">CD/DVD</font> discs. Only a small number of items can be printed on the <font SIZE="-1">CD</font>, and the number of characters in the title and subtitle is also limited. Always check the output visually by using PostScript viewers or printing on paper, before printing on the <font SIZE="-1">CD</font>. </p>
<p> With this option, the top portion of the disc represents the &#8220;cover&#8221; area &#8211; so arguments related to the cover: title (&#8211;category), subtitle (&#8211;subcategory), &#8211;no-cover-plaque, &#8211;cover-items, &#8211;cover-image, etc all apply to the top area. The bottom portion of the disc represents the &#8220;tray&#8221; area, so arguments related to the tray: &#8211;no-tray-plaque, &#8211;tray-image, etc all apply to the bottom area. The date (&#8211;date) string, if present, is printed along the bottom curved edge of the disc. </p>
<p> Background images can be specified using the &#8211;cover-image option, modified as need by the &#8211;cover-image-scaleratio. If &#8211;tray-image is also specified, note that the cover image is printed first, then the tray image overwrites the cover image. The title/items text is then finally printed over all the images. </p>
<p> The &#8211;no-tray-plaque and/or &#8211;no-cover-plaque (along with &#8211;cover-items) option is also recommended with &#8211;create-cdlabel, otherwise there may be no space for any items to be printed on the disc. </p>
<p> The &#8211;clip-items option is also recommended.</p>
<dt><code>-p, &#8211;clip-items</code></p>
<dd> Enables clipping of items; uses fixed font size for all items. Normally, the template.ps used by cdlabelgen will try to fit an item in a given column by reducing the font size if needed. This is ok if done for one or two items, but if done too often, it makes the tray card look ugly, with text of varying font sizes. </p>
<p> Use this option to use a fixed width font for all items. If the item is too large to fit in a column, the text will be clipped instead.</p>
<dt><code>-y, &#8211;page-offset [&lt;page_x_offset_inches,]&lt;page_y_offset_inches</code></p>
<dd> Use this to move the entire output up or down (y_offset), to make the output fit on appropriate sized paper. For letter sized paper, 0.8 works well, and for A4 paper, 1.5 works well. The value is in units of inches. An optional X-axis offset can also be specified. Default values: 1 inch for X-axis, 0.8 inches for Y-axis.</p>
<dt><code>-l, &#8211;line-width &lt;line_width_points</code>&gt;</p>
<dd> Specify size in points of the edge and interior lines of the cover and tray card. If this is 0, then the lines are omitted for both the cover and tray (but guide cut lines are still printed). The size is specified in points (1 point is 1/72 inch).</p>
<dt><code>&#8211;plaque-color &lt;r,g,b</code>&gt;</p>
<dd> Specify a color to fill plaque. Color must be specified using the rgb components, each value should be between 0 and 255.</p>
<dt><code>&#8211;category-color &lt;r,g,b</code>&gt;</p>
<dd> Specify a color for category. Color must be specified using the rgb components, each value should be between 0 and 255.</p>
<dt><code>&#8211;subcategory-color &lt;r,g,b</code>&gt;</p>
<dd> Specify a color for subcategory. Color must be specified using the rgb components, each value should be between 0 and 255.</p>
<dt><code>&#8211;text-color &lt;r,g,b</code>&gt;</p>
<dd> Specify a color for text &#8211; this is used for the list of items, and the date display under the plaque and in the end-caps. Color must be specified using the rgb components, each value should be between 0 and 255.</p>
<dt><code>-n, &#8211;number-in-set &lt;string</code>&gt;</p>
<dd> Append volume information to the end of the date string. This should be a single string. If used in conjuction with <tt>&quot;-D&quot;</tt>, it will be in place of the date; otherwise, it is appended to the date as &#8220; &#8211; &lt;number-in-set&gt;&#8221;</p>
<dt><code>&#8211;rows-columns &lt;row_count_for_items,column_count_for_items</code>&gt;</p>
<dd> The &#8211;rows-columns options forces the list of items to be printed using that many rows, and that many columns. Both numbers have to be provided, no spaces, for example: &#8211;rows-columns=11,3 </p>
<p> The list of items is laid out in top-down, left-to-right fashion. Use blank items in the input, to get appropriately aligned columns. </p>
<p> &#8211;rows-columns applies to the list of items wherever they are printed &#8211; normally on the tray only, but may include cover, or the top and bottom portions of the round printouts for direct <font SIZE="-1">CD</font> label printing. Same values apply to all these variations, so if you need different number of rows/columns for cover vs tray, you can use two different runs of cdlabelgen, to get two postscript files, and pick the cover from one printout, and tray from the other. This will work for jewel-case inserts, but may not work for direct <font SIZE="-1">CD</font> label printing.</p>
<dt><code>&#8211;tray-overlay overlay_epsfile</code></p>
<dd> Filename of eps file to print as overlay on traycard. This image is printed over the background image (tray-image) as well as the list of items. Therefore, this is useful for things like barcodes. In terms of <font SIZE="-1">EPS</font> file requirements, see the &#8211;tray-image option description.</p>
<dt><code>&#8211;tray-overlay-scaleratio tray_overlay_image_scaleratio[,image_x_offset,image_y_offset_inches]</code></p>
<dd> The ratio by which you want to scale the epsfile that is used with the &#8211;tray-overlay option, and optionally to translate the overlay. Normally overlay image is printed on the tray so that the bottom-right of the image is anchored to the bottom-right of the tray. To move the images away from the bottom and right borders, use this option. For example, to leave 0.1 inches of gap between the image and the bottom border, and 0.2 inches from the right border, and use 1.0 scaleratio (no scaling), use this: <code>&#8211;tray-overlay-scaleratio 1.0,-0.2,0.1</code></dl>
<h2>EXAMPLES</h2>
<p>cdlabelgen &#8211; c &#8220;My Filesystem&#8221; &#8211; s &#8220;/usr/local/foo&#8221; &#8211; e postscript / recycle.eps &gt; foo.ps<br />
                                                                                           cdlabelgen &#8211;<br />
                                                                                       c &#8220;title of cd&#8221; &#8211; s &#8220;subtitle&#8221; &#8211; i &#8220;Item 1%and Item 2%a third item here perhaps&#8221; &#8211; e postscript / recycle.eps &#8211; o bar.ps cdlabelgen &#8211; c &#8220;Fitz&#8221; &#8211; s &#8220;home directory&#8221; &#8211; o qux.ps cdlabelgen &#8211; c &#8220;Backups&#8221; &#8211; s &#8220;home directory&#8221; &#8211; n &#8220;4 of 5&#8221; Direct printing on a CD or<br />
    DVD,<br />
    if file &#8220;example5.txt&#8221; has list of items : cdlabelgen&#8211; clip &#8211; items&#8211; no &#8211; tray &#8211; plaque&#8211; date &#8220;Jan 2005&#8221; &#8211; c &#8220;Collections 12&#8221; &#8211; s &#8220;- english songs -&#8221; &#8211;cover &#8211; image &#8220;music2.eps&#8221; &#8211;cover &#8211; image &#8211; scaleratio 0.0 &#8211;tray &#8211; image &#8220;mp3.eps&#8221; &#8211;tray &#8211; image &#8211; scaleratio 0.5, -0.5, 2 &#8211;page &#8211; offset 0.5, 0.5 &#8211; f example5.txt &#8211; o test.ps</p>
<h2>CHARACTER ENCODINGS &#8211; using ogonkify</h2>
<p> cdlabelgen uses the Helvetica family of fonts for various text items, using the default encoding of ISO-Latin1. </p>
<p> To use other encodings, the &#8220;ogonkify&#8221; program can be used; this is a package available at <a rel="nofollow" href="http://www.pps.jussieu.fr/~jch/software/ogonkify/">http://www.pps.jussieu.fr/~jch/software/ogonkify/</a> The output from cdlabelgen can be piped into ogonkify, example for Latin2 encoding: </p>
<pre>
   cdlabelgen &lt;args&gt;  | ogonkify -H -eL2    &gt; &lt;outputfilename&gt;
</pre>
<p> See the man page for ogonkify for other possible values for the encoding. </p>
<p> Hint: if you always work with a particular encoding, you can just run ogonkify on template.ps &#8211; and use the output as the new template.ps. </p>
<pre>
   ogonkify -H -eL2 template.ps &gt; template-enc.ps
</pre>
<p> This way ogonkify has to be run only once, cdlabelgen output will contain the correctly encoded fonts from the modified template.ps. Use the -t cdlabelgen option to specify the new template-enc.ps file, or save the old template.ps and renmae template-enc.ps to template.ps.</p>
<h2>PRINTING</h2>
<p> When using tools such as Adobe Acrobat to print the .ps or a .pdf file, make sure that &#8220;Fit To Paper&#8221; option is unchecked. Also uncheck any option that will perform scaling up or down of the cdlabelgen output file. </p>
<p> Failure to do so will result in incorrect size printouts. </p>
<p> Paper Sizes: Normal <font SIZE="-1">CD</font> cases, Slim <font SIZE="-1">CD</font> cases, <font SIZE="-1">DVD</font> inside inserts can be printed on a letter or A4 sized page. <font SIZE="-1">CD/DVD</font> Envelopes and <font SIZE="-1">DVD</font> outside inserts will not fit on a letter sized paper, a larger paper size will be needed to make it fit. </p>
<p> When using different sized paper, experimentation with the <code>-y</code> (also: <code>&#8211;page-offset</code>) [&lt;page_x_offset_inches,]&lt;page_y_offset_inches&gt; option may be required to place the image in the printable region of the paper.</p>
<h2>AUTHOR</h2>
<p> Avinash Chopde &lt;<i>avinash [at] aczoom.com</i>&gt; </p>
<p> Original author: B. W. Fitzpatrick &lt;<i>fitz [at] red-bean.com</i>&gt;</p>
<h2>THANKS</h2>
<p>    &#8211; Karl Fogel, for general encouragement and that free software vibe<br />
    &#8211; Adam Di Carlo, for bug testing, help and making the .deb<br />
    &#8211; Greg Gallagher, for bug testing, coding, and tons of suggestions<br />
    &#8211; Goran Larsson, for feedback and date fixes<br />
    &#8211; Jens Claussen, for the patch to allow arbitrary ISO-Latin1 characters<br />
    &#8211; Bernard Quatermass, for contributing several excellent new features<br />
    &#8211; Sebastian Wenzler &lt;sick [at] home.and.drunk.at&gt; for reports, tests, RPM [&#8217;01]<br />
    &#8211; Peter Bieringer &lt;pb [at] bieringer.de&gt; for RPM .spec file [&#8217;02]<br />
    &#8211; Ronald Rael Harvest &lt;number6 [at] cox.net&gt; for original envelope template [&#8217;02]<br />
    &#8211; Alessandro Dotti Contra &lt;alessandro.dotti [at] libero.it&gt; for color support,<br />
        man page and other improvements [&#8217;02]<br />
        Mathias Herberts<br />
    &#8211; Mathias Herberts &lt;Mathias.Herberts [at] iroise.net&gt;, for slim cdcase foldout<br />
    &#8211; Stephan Grund &lt;Stephan.Grund [at] isst.fraunhofer.de&gt;, for monospaced<br />
      font and for rotated-end-caps text support<br />
    &#8211; Dominique Dumont &lt;dod [at] debian.org&gt;<br />
        for half-height DVD case support<br />
        for slim-double depth DVD case support<br />
        (patches forwarded by Juan Manuel Garcia Molina &lt;juanma [at] debian.org&gt;)<br />
    &#8211; Peter Bieringer &lt;pb [at] bieringer.de&gt; for testing CD label printint [&#8217;05]<br />
    &#8211; Andras Salamon &lt;asalamon [at] chello.hu&gt; for double-width DVD support [&#8217;08]</p>
<h2>TODO</h2>
<pre><code>
 ** Word wrap does not work well at all. It will clip lines, or it will
    auto-reduce the font size, both of which option look bad.
 ** Ability to change the text style on a given line:
    {#B}Track#  {#P}Title   {#I} Text...
    [Workaround available: just use multi columns input, use blank
     lines to spread out input items into columns]
 ** Ability to select or specify fonts for the text/items
</code></pre>
<h2>Index</h2>
