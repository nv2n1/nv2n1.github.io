---
title: "pssvg(1)"
name: "pssvg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pssvg/"
description: "pssvg – convert Photoshop® gradients to SVG."
---

<h2 class="name">NAME</h2>
<p> pssvg &#8211; convert Photoshop&#174; gradients to SVG. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pssvg</code> [-b&nbsp;<wbr><i>rgb</i>] [-f&nbsp;<wbr><i>rgb</i>] [-h] [-o&nbsp;<wbr><i>file</i>] [-t&nbsp;<wbr><i>format</i>] [-v] [-V] <i>file</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>pssvg</code> program converts Photoshop grd5 gradients to the SVG format. Unlike most of the other file formats handled by the cptutils package, grd5 files may contain multiple gradients and all of the input gradients will be converted to gradients in the output file. One can then use <code><a href="/docs/linux/man/1-svgx/">svgx</a></code>(1) to extract single gradients and convert them to other formats. </p>
<p> Photoshop gradient files will often contain a number of gradients with the same name. These names are used as the basis for the SVG titles (the id attributes), but since these must be unique, the program will append _01, _02, &#8230; to duplicate names in order to form the titles. Alternatively once can employ the <code>&#8211;title</code> option to generate a uniform sequence of titles. </p>
<p> Atypically, the input Photoshop grd5 file is a mandatory argument. The program will write to stdout if the <code>&#8211;output</code> option is not specified.</p>
<h2>OPTIONS</h2>
<p> In the following, all <i>rgb</i> specifications should be of the form <i>red</i>/<i>green</i>/<i>blue</i> where the colour components are integers in the range 0 to 255. </p>
<p> <code>-b</code>, <code>&#8211;background</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the background colour of the output.</dl>
<p> <code>-f</code>, <code>&#8211;foreground</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the foreground colour of the output.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file</i></p>
<dl>
<dt>
<dd> Write the output to <i>file</i>, rather than stdout.</dl>
<p> <code>-t</code>, <code>&#8211;title</code> <i>format</i></p>
<dl>
<dt>
<dd> This option generates the SVG gradient titles (the id attributes) according to the specified <i>format</i>. </p>
<p> The <i>format</i> argument should be a <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) format string containing a single integer directive (and that directive will be replaced by the gradient number). Thus &quot;gradient-%03i&quot; will produce ids &quot;gradient-001&quot;, &quot;gradient-002&quot;, &#8230;</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>EXAMPLE</h2>
<p> Convert a Photoshop gradient, foo.grd, to a set of GIMP gradients, foo-001.ggr, foo-002.ggr, &#8230; </p>
<dl>
<dt>
<dd>
<pre>
  pssvg -v -t &quot;foo-%03i&quot; -o tmp.svg foo.grd
  svggimp -v -a tmp.svg  
</pre>
</dl>
<h2>CAVEATS</h2>
<p> The program handles RGB, HSB, LAB, CMYK and greyscale colour stops, converting them all to RGB and then merging the results with the opacity channel to create SVG RGBA stops. Conversion of non-RGB stops is naive and takes no account of colour profiles, so the results are generally sub-optimal. Integration of a CMS (colour management system) into the program to perform these conversions is under investigation. </p>
<p> The program does not handle &quot;Book Colours&quot; (PANTONE, COLOR FINDER, etc) for legal reasons. </p>
<p> The SVG output format does not support back/foreground colours; consequently, if the input specifies any stops with back/fairground colours then these will be converted to the colour specified by the <code>&#8211;background</code> and <code>&#8211;foreground</code> options, respectively. </p>
<p> The smoothness parameter used by Photoshop (which seems to parameterise some kind of spline) is not yet handled; the output contains only linear splines (corresponding to a smoothness of 0%). The result is that the SVG output will sometimes look more &quot;angular&quot; than the Photoshop input. Fixing this will require research into the precise nature of the spline parameterisation used in the input. </p>
<p> Noise gradients would seem to be difficult to convert to SVG without using a huge number of stops in the output, so these will probably not be supported by this program.</p>
<h2>NOTES</h2>
<p> Adobe Photoshop&#174; is a trademark of Adobe Systems Inc. PANTONE&#174; is a trademark of Pantone LLC. COLOR FINDER&#174; is a trademark of Toyo Ink Mfg. Co., Ltd. </p>
<p> This program was written using the reverse-engineered specification of the grd5 format by Valek Filippov, Alexandre Prokoudine and Michel Mariani.</p>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-svgx/">svgx</a></code>(1). </p>
<h2>Index</h2>
