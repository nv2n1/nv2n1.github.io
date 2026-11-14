---
title: "djvups(1)"
name: "djvups"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvups/"
description: "djvups – Convert DjVu documents to PostScript."
---

<h2>NAME</h2>
<p> djvups &#8211; Convert DjVu documents to PostScript. </p>
<h2>SYNOPSIS</h2>
<p> <code>djvups [</code><i>options</i><code>] [</code><i>djvufile</i><code>] [</code><i>outputfile</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> This program decodes DjVu file <i>djvufile</i>, and generates a PostScript file named <i>outputfile</i>. The DjVu data is read from the standard input when argument <i>djvufile</i> is not specified or when it is equal to a single dash. Similarly, the output data is written to the standard output when argument <i>outputfile</i> is not specified or equal to a single dash. </p>
<p> PostScript printers have various capabilities. Investigate options <code>-level</code> and <code>-gray</code> for obtaining the best results. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Prints the list of recognized options.</p>
<dt><code>-verbose</code></p>
<dd> Displays a progress bar.</p>
<dt><code>-page=</code><i>pagespec</i></p>
<dd> Specify the document pages to be converted. The page specification <i>pagespec </i> contains one or more comma-separated page ranges. A page range is either a page number, or two page numbers separated by a dash. Specification <code>1-10</code>, for instance, prints pages 1 to 10. Specification <code>1,3,99999-4</code> prints pages 1 and 3, followed by all the document pages in reverse order up to page 4.</p>
<dt><code>-format=ps</code></p>
<dd> Produce a PostScript file. This is the default.</p>
<dt><code>-format=eps</code></p>
<dd> Produce an Encapsulated PostScript file. Encapsulated PostScript files are suitable for embedding images into other documents. Encapsulated PostScript file can only contain a single page. Setting this option overrides the options <code>-copies</code>, <code>-orientation</code>, <code>-zoom</code>, <code>-cropmarks</code>, and <code>-booklet</code>.</p>
<dt><code>-copies=</code><i>n</i></p>
<dd> Specify the number of copies to print.</p>
<dt><code>-orientation=</code><i>orient</i></p>
<dd> Specify whether pages should be printed using the <code>auto</code>, <code>portrait</code>, or <code>landscape </code> orientation.</p>
<dt><code>-mode=</code><i>modespec</i></p>
<dd> Specify how pages should be decoded. The default mode, <code>color</code>, renders all the layers of the DjVu documents. Mode <code>black</code> only renders the foreground layer mask. This mode does not work with DjVuPhoto images because these files have no foreground layer mask. Modes <code>foreground</code> and <code>background</code> only render the foreground layer or the background layer of a DjVuDocument image.</p>
<dt><code>-zoom=</code><i>zoomspec</i></p>
<dd> Specify a zoom factor <i>zoomspec</i>. The default zoom factor, <code>auto</code>, scales the image to fit the page. Argument <i>zoomspec</i> also can be a number in range <code>25</code> to <code>2400</code> representing a magnification percentage relative to the original size of the document.</p>
<dt><code>-frame=</code><i>yesno</i></p>
<dd> Specifying <code>yes</code> causes the generation of a thin gray border representing the boundaries of the document pages. The default is <code>no</code>.</p>
<dt><code>-cropmarks=</code><i>yesno</i></p>
<dd> Specifying <code>yes</code> causes the generation of crop marks indicating where pages should be cut. The default is <code>no</code>.</p>
<dt><code>-level=</code><i>languagelevel</i></p>
<dd> Select the language level of the generated PostScript. <i>languagelevel</i>. Valid language levels are <code>1</code>, <code>2</code>, and <code>3</code>. Level <code>3 </code> produces the most compact and fast printing PostScript files. Some of these files however require a very modern printer. Level <code>2 </code> is the default value. The generated PostScript files are almost as compact and work with all but the oldest PostScript printers. Level <code>1</code> can be used as a last resort option.</p>
<dt><code>-color=</code><i>yesno</i></p>
<dd> The default value, <code>yes</code>, generates a color PostScript file. Specifying value <code>no</code> converts the image to gray scale. The resulting PostScript file is smaller and marginally more portable.</p>
<dt><code>-gray</code></p>
<dd> This option is equivalent to option <code>-color=no</code> and is provided for convenience.</p>
<dt><code>-colormatch=</code><i>yesno</i></p>
<dd> The default value, <code>yes</code>, generates a PostScript file using device independent colors in compliance with the <font SIZE="-1">sRGB</font> specification. Modern printers then produce colors that match the original as well as possible. Specifying value <code>no</code> generates a PostScript file using device dependent colors. This is sometimes useful with older printers. You can then use option <code>-gamma</code> to tune the output colors.</p>
<dt><code>-gamma=</code><i>gammaspec</i></p>
<dd> Specify a gamma correction factor for the device dependent PostScript colors. Argument <i>gammaspec</i> must be in range <code>0.3</code> to <code>5.0</code>. Gamma correction normally pertains to cathodic screens only. It gets meaningful for printers because several models interpret device dependent RGB colors by emulating the color response of a cathodic tube.</p>
<dt><code>-booklet=</code><i>opt</i></p>
<dd> Turns the booklet printing mode on. The booklet mode prints two pages on each side in a way suitable for making a booklet by folding the sheets. Option <i>opt</i> can take values <code>no</code> for disabling the booklet mode, <code>yes</code> for enabling the recto/verso booklet mode, and <code>recto</code> or <code>verso</code> to print only one side of each sheet.</p>
<dt><code>-bookletmax=</code><i>max</i></p>
<dd> Specifies the maximal number of pages per booklet. A single printout might then be composed of several booklets. Argument <i>max</i> is rounded up to the next multiple of 4. Specifying <code>0</code> sets no maximal number of pages and ensures that the printout will produce a single booklet. This is the default.</p>
<dt><code>-bookletalign=</code><i>align</i></p>
<dd> Specifies a positive or negative offset applied to the verso of each sheet. Argument <i>align</i> is expressed in points (one point is 1/72th of an inch, or 0.352 millimeter) This is useful with certain printers to ensure that both recto and verso are properly aligned. The default value is of course <code>0</code>.</p>
<dt><code>-bookletfold=</code><i>base[+incr]</i></p>
<dd> Specifies the extra margin left between both pages on a single sheet. The base value <i>base</i> is expressed in points (one point is 1/72th of an inch, or 0.352 millimeter). This margin is incremented for each outer sheet by value <i>incr</i> expressed in millipoints. The default value is <code>18+200</code>. </p>
</dl>
<h2>CREDITS</h2>
<p> This program was written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt;, Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt;, and Florin Nicsa. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-ddjvu/">ddjvu</a></code>(1). <code><a href="/docs/linux/man/1-djview/">djview</a></code>(1) </p>
<h2>Index</h2>
