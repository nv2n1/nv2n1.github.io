---
title: "gradient-convert(1)"
name: "gradient-convert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gradient-convert/"
description: "gradient-convert – convert gradients between formats"
---

<h2 class="name">NAME</h2>
<p> gradient-convert &#8211; convert gradients between formats </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gradient-convert</code> [-b&nbsp;<wbr><i>rgb</i>] [-B] [-c] [-f&nbsp;<wbr><i>rgb</i>] [-g&nbsp;<wbr><i>geometry</i>] [-h] [-i&nbsp;<wbr><i>format</i>] [-n&nbsp;<wbr><i>rgb</i>] [-o&nbsp;<wbr><i>format</i>] [-p] [-T&nbsp;<wbr><i>rgb</i>] [-v] [-V] <i>infile</i> <i>outfile</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>gradient-convert</code> program converts gradients to other formats. It is a wrapper script which make a number of calls the individual programs from the cptutils package so, for example, to convert an Arcview legend (avl) to a PNG image, the programs <code>avlcpt</code>, <code>cptsvg</code> and <code>svgpng</code> would be called in sequence to generate the required file. </p>
<p> The formats of the mandatory <i>infile</i> and <i>outfile</i> arguments are determined from the file extensions, or can be specified explicitly by the <code>-i</code> and <code>-o</code> options.</p>
<h2>OPTIONS</h2>
<p> In the following, all <i>rgb</i> specifications should be of the form <i>red</i>/<i>green</i>/<i>blue</i> where the colour components are integers in the range 0 to 255. </p>
<p> <code>-b</code>, <code>&#8211;background</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the background colour of cpt output. </p>
<p> Note that this only modifies the &quot;background&quot; field in the output cpt file, it does not affect the transparency (see the <code>-T</code> option in that regard).</dl>
<p> <code>-B</code>, <code>&#8211;burst</code></p>
<dl>
<dt>
<dd> Some of the file formats handled by cptutils may contain multiple gradients: the Photoshop (grd) and SVG formats for example. By default, the program will extract only the first gradient from such files; but when the <code>&#8211;burst</code> option is selected then all gradients will be extracted. In this case the argument of the <i>outfile</i> argument must be a directory (and that directory should already exist).</dl>
<p> <code>-c</code>, <code>&#8211;capabilities</code></p>
<dl>
<dt>
<dd> Print the capabilites of the program to stdout. This data (in YAML format) may be used to autoconfigure other programs which wish to use this program. The format should be self-explanatory.</dl>
<p> <code>-f</code>, <code>&#8211;foreground</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the foreground colour of cpt output.</dl>
<p> <code>-g</code>, <code>&#8211;geometry</code> <i>width</i>x<i>height</i></p>
<dl>
<dt>
<dd> Specify the size of the PNG image or SVG preview in pixels.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Brief help.</dl>
<p> <code>-i</code>, <code>&#8211;input-format</code> <i>format</i></p>
<dl>
<dt>
<dd> Specify the format of the input file. Run the program with the <code>&#8211;help</code> option for a list of supported formats.</dl>
<p> <code>-n</code>, <code>&#8211;nan</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the NaN (no data) colour of cpt output.</dl>
<p> <code>-o</code>, <code>&#8211;output-format</code> <i>format</i></p>
<dl>
<dt>
<dd> Specify the format of the output file. Run the program with the <code>&#8211;help</code> option for a list of supported formats.</dl>
<p> <code>-p</code>, <code>&#8211;preview</code></p>
<dl>
<dt>
<dd> Include a preview in the SVG output. See also the <code>&#8211;geometry</code> option.</dl>
<p> <code>-T</code>, <code>&#8211;transparency</code> <i>rgb</i></p>
<dl>
<dt>
<dd> When converting to a format which does not support transparency, replace the transparency with the specified <i>rgb</i> colour.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose operation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Version information.</dl>
<h2>EXAMPLES</h2>
<p> Convert an Arcview Legend to a 200&#215;20 pixel PNG image </p>
<dl>
<dt>
<dd>
<pre>
  gradient-convert -v -g 200x20 legend.avl legend.png 
</pre>
</dl>
<h2>CAVEATS</h2>
<p> The component programs in the conversion will generally have a number of options available for modifying the conversion behaviour, but only the most-often used of these options can be passed to component programs from <code>gradient-convert</code>. </p>
<p> Note also that those options which are passed to component programs are not checked for relevance. Converting a GMT cpt file to GIMP format while using using the irrelevant <code>-g</code> option will not cause an error, it will simply be ignored.</p>
<h2>AUTHOR</h2>
<p> J.J. Green </p>
<h2>Index</h2>
