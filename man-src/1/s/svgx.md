---
title: "svgx(1)"
name: "svgx"
section: "1"
letter: "s"
url: "/docs/linux/man/1-svgx/"
description: "svgx – extract gradients from SVG files."
---

<h2 class="name">NAME</h2>
<p> svgx &#8211; extract gradients from SVG files. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>svgx</code> [-a] [-b&nbsp;<wbr><i>rgb</i>] [-f&nbsp;<wbr><i>rgb</i>] [-g&nbsp;<wbr><i>geometry</i>] [-h] [-l] [-n&nbsp;<wbr><i>rgb</i>] [-o&nbsp;<wbr><i>file</i>] [-p] [-s&nbsp;<wbr><i>name</i>] [-t&nbsp;<wbr><i>type</i>] [-T&nbsp;<wbr><i>rgb</i>] [-v] [-V] <i>file</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>svgx</code> program extracts and converts gradients in an SVG file. Unlike most of the other file formats handled by the cptutils package, SVG files may contain multiple gradients, so this program operates a little differently to the other programs in the package. </p>
<p> There are 4 modes of operation: The default is to extract the first gradient found in the file, or one can specify <code>-l</code> to list the names of all gradients in the file; <code>-s</code> to extract the gradient with the specified name or <code>-a</code> to extract all of the gradients. </p>
<p> The output format is specified by the <code>-t</code> option as listed below (in fact there are several aliases for each format: <code>jgd</code> for <code>psp</code>, <code>gimp</code> for <code>ggr</code>, and so on). The <code>svgcpt</code>, <code>svggimp</code>, <code>svggpt</code>, <code>svgcss3</code>, <code>svgpsp</code>, <code>svgpov</code>, <code>svgpng</code>, <code>svgsao</code> and <code>svgsvg</code> programs are wrappers around <code>svgx</code> which use the <code>-t</code> switch to specify output type. </p>
<p> Atypically, the input SVG file is a mandatory argument. The program will write to stdout if the <code>-o</code> option is not specified except when <code>-a</code> has been specified: then files will be produced (with names taken from those of the gradients). </p>
<p> Note that some of the SVG conversions require that the en_US.utf8 locale is enabled. How this is done will depend on your operating system.</p>
<h2>OPTIONS</h2>
<p> In the following, all <i>rgb</i> specifications should be of the form <i>red</i>/<i>green</i>/<i>blue</i> where the colour components are integers in the range 0 to 255. </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Extract all gradients, which will have filenames derived from the gradient names. If this option is used then the argument of the <code>-o</code> option will be interpreted as the output directory.</dl>
<p> <code>-b</code>, <code>&#8211;background</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the background colour of cpt output. </p>
<p> Note that this only modifies the &quot;background&quot; field in the output cpt file, it does not affect the transparency (see the <code>-T</code> option in that regard).</dl>
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
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List the names of all gradients in the file.</dl>
<p> <code>-n</code>, <code>&#8211;nan</code> <i>rgb</i></p>
<dl>
<dt>
<dd> Set the NaN (no data) colour of cpt output.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>path</i></p>
<dl>
<dt>
<dd> Write the output to <i>path</i>, rather than stdout. </p>
<p> If the <code>-a</code> option is specified then the <i>path</i> argument must be a directory (which exists) and the output files will be written into this directory.</dl>
<p> <code>-p</code>, <code>&#8211;preview</code></p>
<dl>
<dt>
<dd> Include a preview in the SVG output. See also the <code>&#8211;geometry</code> option.</dl>
<p> <code>&#8211;strict</code></p>
<dl>
<dt>
<dd> Do not create files which break limits of the format specification. In particular, do not create POV-Ray headers with more than 255 stops.</dl>
<p> <code>-s</code>, <code>&#8211;select</code> <i>name</i></p>
<dl>
<dt>
<dd> Extract the gradient with the specified <i>name</i>, see the <code>-l</code> output for a list of possible values.</dl>
<p> <code>-t</code>, <code>&#8211;type</code> <i>format</i></p>
<dl>
<dt>
<dd> Set the output <i>format</i>, which should be one of <code>cpt</code>, <code>css3</code>, <code>ggr</code>, <code>gpt</code>, <code>psp</code>, <code>pov</code>, <code>png</code>, <code>sao</code> or <code>svg</code>.</dl>
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
<p> Inspect an SVG file for gradients: </p>
<dl>
<dt>
<dd>
<pre>
  svgx -v -l old.svg 
</pre>
</dl>
<p> Extract the gradient &quot;Sunny Road&quot; from the same SVG file, converting the result to cpt: (note that the gradient name needs to be quoted) </p>
<dl>
<dt>
<dd>
<pre>
  svgx -v -t cpt -s &quot;Sunny Road&quot; -o sunny_road.cpt old.svg 
</pre>
</dl>
<p> Extract all of the svg gradients from the file kittens.svg and give each of them a preview: </p>
<dl>
<dt>
<dd>
<pre>
  svgx -v -t svg -a -p kittens.svg  
</pre>
</dl>
<h2>CAVEATS</h2>
<p> An ill-formed SVG gradient may be translated to rubbish while not reporting an error.</p>
<h2>AUTHOR</h2>
<p> J.J. Green</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cptsvg/">cptsvg</a></code>(1), <code><a href="/docs/linux/man/1-gimpsvg/">gimpsvg</a></code>(1), <code><a href="/docs/linux/man/1-pspsvg/">pspsvg</a></code>(1). </p>
<h2>Index</h2>
