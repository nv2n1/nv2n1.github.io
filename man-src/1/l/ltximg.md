---
title: "ltximg(1)"
name: "ltximg"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ltximg/"
description: "ltximg – LaTeX environments to image and standalone files"
---

<h2 class="name">NAME</h2>
<p> ltximg &#8211; LaTeX environments to image and standalone files </p>
<h2>SYNOPSIS</h2>
<p> <code>ltximg</code> [&lt;<i>options</i>&gt;] [&#8211;] &lt;<i>filename</i>&gt;.&lt;<i>tex</i>|<i>ltx</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>ltximg</code> automates the process of extracting and converting environments from LaTeX file to image formats and <i>standalone</i> files using <i>ghostscript</i> and <i>poppler-utils</i>. Generates a one file with only extracted environments and other with all extracted environments converted to <tt>&quot;\includegraphics&quot;</tt>. </p>
<p> By default the extracted environments are: </p>
<p> <code>preview</code> <code>pspicture</code> <code>tikzpicture</code> <code>pgfpicture</code> <code>psgraph</code> <code>postscript</code> <code>PSTexample</code></p>
<h2>OPTIONS</h2>
<p> Options that accept a value require either a blank space or <tt>&quot;=&quot;</tt> between the option and the value. Multiple short options can be bundling and if the last option takes a comma separated list you need <tt>&quot;--&quot;</tt> at the end. Relative or absolute paths for directories and files is not supported. </p>
<p> If used without [&lt;<i>options</i>&gt;] the extracted environments are converted to <i>pdf</i> image format and saved in <tt>&quot;./images&quot;</tt> directory using <tt>&quot;pdflatex&quot;</tt> and <i>preview</i> package for process. </p>
<p> General script options:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display command line help and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display current version and exit.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Verbose printing information.</p>
<dt><code>-l</code>, <code>&#8211;log</code></p>
<dd> Write <tt>&quot;.log&quot;</tt> file with debug information.</p>
<dt><code>-t</code>, <code>&#8211;tif</code></p>
<dd> Create <tt>&quot;.tif&quot;</tt> files using <i>ghostscript</i>.</p>
<dt><code>-b</code>, <code>&#8211;bmp</code></p>
<dd> Create <tt>&quot;.bmp&quot;</tt> files using <i>ghostscript</i>.</p>
<dt><code>-j</code>, <code>&#8211;jpg</code></p>
<dd> Create <tt>&quot;.jpg&quot;</tt> files using <i>ghostscript</i>.</p>
<dt><code>-p</code>, <code>&#8211;png</code></p>
<dd> Create <tt>&quot;.png&quot;</tt> files using <i>ghostscript</i>.</p>
<dt><code>-e</code>, <code>&#8211;eps</code></p>
<dd> Create <tt>&quot;.eps&quot;</tt> files using <i>pdftops</i>.</p>
<dt><code>-s</code>, <code>&#8211;svg</code></p>
<dd> Create <tt>&quot;.svg&quot;</tt> files using <i>pdftocairo</i>.</p>
<dt><code>-P</code>, <code>&#8211;ppm</code></p>
<dd> Create <tt>&quot;.ppm&quot;</tt> files using <i>pdftoppm</i>.</p>
<dt><code>-g</code>, <code>&#8211;gray</code></p>
<dd> Gray scale for images using <i>ghostscript</i>.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Capture <tt>&quot;\psset&quot;</tt> and <tt>&quot;	ikzset&quot;</tt> to extract.</p>
<dt><code>-n</code>, <code>&#8211;noprew</code></p>
<dd> Create images files without <i>preview</i> package.</p>
<dt><code>-r</code> <i>integer</i>, <code>&#8211;runs</code>=<i>integer</i></p>
<dd> Set the number of times the compiler will run on the <i>input</i> file for environment extraction (default: 1).</p>
<dt><code>-d</code> <i>integer</i>, <code>&#8211;dpi</code>=<i>integer</i></p>
<dd> Dots per inch resolution for images (default: 150).</p>
<dt><code>-m</code> <i>integer</i>, <code>&#8211;margins</code>=<i>integer</i></p>
<dd> Set margins in bp for <i>pdfcrop</i> (default: 0).</p>
<dt><code>-o</code> <i>filename</i>, <code>&#8211;output</code>=<i>filename</i></p>
<dd> Create <i>output</i> file.</p>
<dt><code>&#8211;imgdir</code>=<i>dirname</i></p>
<dd> Set name of directory to save images and files (default: images).</p>
<dt><code>&#8211;prefix</code>=<i>string</i></p>
<dd> Set <i>prefix</i> append to each generated files (default: fig).</p>
<dt><code>&#8211;myverb</code>=<i>macroname</i></p>
<dd> Add <tt>&quot;\macroname&quot;</tt> to verbatim inline search (default: myverb).</p>
<dt><code>&#8211;clean</code>=<i>doc</i>|<i>pst</i>|<i>tkz</i>|<i>all</i>|<i>off</i></p>
<dd> Removes specific block text in <i>output</i> file (default: doc).</p>
<dt><code>&#8211;zip</code></p>
<dd> Compress files generated in <tt>&quot;.zip&quot;</tt> format.</p>
<dt><code>&#8211;tar</code></p>
<dd> Compress files generated in <tt>&quot;.tar.gz&quot;</tt> format.</p>
<dt><code>&#8211;srcenv</code></p>
<dd> Create files with only code of environments.</p>
<dt><code>&#8211;subenv</code></p>
<dd> Create standalone files for environments.</p>
<dt><code>&#8211;shell</code></p>
<dd> Enable <tt>&quot;\write18{SHELL COMMAND}&quot;</tt>.</p>
<dt><code>&#8211;latex</code></p>
<dd> Using <tt>&quot;latex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>input</i> and <tt>&quot;pdflatex&quot;</tt> for compiler <i>output</i>.</p>
<dt><code>&#8211;dvips</code></p>
<dd> Using <tt>&quot;latex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>input</i> and <tt>&quot;latex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>output</i>.</p>
<dt><code>&#8211;dvilua</code></p>
<dd> Using <tt>&quot;dvilualatex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>input</i> and <tt>&quot;lualatex&quot;</tt> for compiler <i>output</i>.</p>
<dt><code>&#8211;dvipdf</code></p>
<dd> Using <tt>&quot;latex&gt;dvipdfmx&quot;</tt> for compiler <i>input</i> and <tt>&quot;latex&gt;dvipdfmx&quot;</tt> for compiler <i>output</i>.</p>
<dt><code>&#8211;xetex</code></p>
<dd> Using <tt>&quot;xelatex&quot;</tt> for compiler <i>input</i> and <i>output</i>.</p>
<dt><code>&#8211;luatex</code></p>
<dd> Using <tt>&quot;lualatex&quot;</tt> for compiler <i>input</i> and <i>output</i>.</p>
<dt><code>&#8211;arara</code></p>
<dd> Use <tt>&quot;arara&quot;</tt> for compiler <i>input</i> and <i>output</i>.</p>
<dt><code>&#8211;latexmk</code></p>
<dd> Using <tt>&quot;latexmk&quot;</tt> for compiler <i>output</i> file.</p>
<dt><code>&#8211;norun</code></p>
<dd> Run script, but no create images files.</p>
<dt><code>&#8211;nopdf</code></p>
<dd> Don&#8217;t create a <tt>&quot;.pdf&quot;</tt> image files.</p>
<dt><code>&#8211;nocrop</code></p>
<dd> Don&#8217;t run <i>pdfcrop</i>.</p>
<dt><code>&#8211;extrenv</code>=<i>env1,env2,&#8230;</i></p>
<dd> Add new environments to extract.</p>
<dt><code>&#8211;skipenv</code>=<i>env1,env2,&#8230;</i></p>
<dd> Skip some default environments to extract.</p>
<dt><code>&#8211;verbenv</code>=<i>env1,env2,&#8230;</i></p>
<dd> Add new verbatim environments.</p>
<dt><code>&#8211;writenv</code>=<i>env1,env2,&#8230;</i></p>
<dd> Add new verbatim write environments.</p>
<dt><code>&#8211;deltenv</code>=<i>env1,env2,&#8230;</i></p>
<dd> Delete environments in <i>output</i> file.</dl>
<h2>EXAMPLE</h2>
<p> <code>ltximg</code> &#8211;latex -e -p &#8211;subenv -o test-out.ltx test-in.ltx </p>
<p> Create a <tt>&quot;./images&quot;</tt> directory (if it doesn&#8217;t exist) with all extracted environments converted to <tt>&quot;.pdf&quot;</tt>, <tt>&quot;.eps&quot;</tt>, <tt>&quot;.png&quot;</tt> and <i>standalone</i> files, a file <i>test-in-fig-all.ltx</i> with all extracted environments and the file <i>test-out.ltx</i> with all environments converted to <tt>&quot;\includegraphics&quot;</tt> using <tt>&quot;latex&gt;dvips&gt;ps2pdf&quot;</tt> and <i>preview</i> package for <i>test-in.ltx</i> and <tt>&quot;pdflatex&quot;</tt> for <i>test-out.ltx</i>.</p>
<h2>DOCUMENTATION</h2>
<p> For full documentation use: </p>
<p> texdoc <code>ltximg</code></p>
<h2>ISSUES AND REPORTS</h2>
<p> <code>Repository</code> : &lt;<a rel="nofollow" href="https://github.com/pablgonz/ltximg">https://github.com/pablgonz/ltximg</a>&gt; </p>
<p> <code>Bug tracker</code>: &lt;<a rel="nofollow" href="https://github.com/pablgonz/ltximg/issues">https://github.com/pablgonz/ltximg/issues</a>&gt;</p>
<h2>AUTHOR</h2>
<p> Pablo González Luengo, <i>pablgonz [at] yahoo.com</i>.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 2013-2021 Pablo González, <i>pablgonz [at] yahoo.com</i>. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> General Public License for more details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1), <code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1), <code><a href="/docs/linux/man/1-pdfcrop/">pdfcrop</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1) </p>
<h2>Index</h2>
