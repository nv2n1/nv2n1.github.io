---

title: "ltximg(1)"
name: "ltximg"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ltximg/"
description: "ltximg – LaTeX environments to image and standalone files"
---

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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display command line help and exit.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display current version and exit.</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> Verbose printing information.</dd>
<dt><code>-l</code>, <code>&#8211;log</code></dt>
<dd> Write <tt>&quot;.log&quot;</tt> file with debug information.</dd>
<dt><code>-t</code>, <code>&#8211;tif</code></dt>
<dd> Create <tt>&quot;.tif&quot;</tt> files using <i>ghostscript</i>.</dd>
<dt><code>-b</code>, <code>&#8211;bmp</code></dt>
<dd> Create <tt>&quot;.bmp&quot;</tt> files using <i>ghostscript</i>.</dd>
<dt><code>-j</code>, <code>&#8211;jpg</code></dt>
<dd> Create <tt>&quot;.jpg&quot;</tt> files using <i>ghostscript</i>.</dd>
<dt><code>-p</code>, <code>&#8211;png</code></dt>
<dd> Create <tt>&quot;.png&quot;</tt> files using <i>ghostscript</i>.</dd>
<dt><code>-e</code>, <code>&#8211;eps</code></dt>
<dd> Create <tt>&quot;.eps&quot;</tt> files using <i>pdftops</i>.</dd>
<dt><code>-s</code>, <code>&#8211;svg</code></dt>
<dd> Create <tt>&quot;.svg&quot;</tt> files using <i>pdftocairo</i>.</dd>
<dt><code>-P</code>, <code>&#8211;ppm</code></dt>
<dd> Create <tt>&quot;.ppm&quot;</tt> files using <i>pdftoppm</i>.</dd>
<dt><code>-g</code>, <code>&#8211;gray</code></dt>
<dd> Gray scale for images using <i>ghostscript</i>.</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> Capture <tt>&quot;\psset&quot;</tt> and <tt>&quot;	ikzset&quot;</tt> to extract.</dd>
<dt><code>-n</code>, <code>&#8211;noprew</code></dt>
<dd> Create images files without <i>preview</i> package.</dd>
<dt><code>-r</code> <i>integer</i>, <code>&#8211;runs</code>=<i>integer</i></dt>
<dd> Set the number of times the compiler will run on the <i>input</i> file for environment extraction (default: 1).</dd>
<dt><code>-d</code> <i>integer</i>, <code>&#8211;dpi</code>=<i>integer</i></dt>
<dd> Dots per inch resolution for images (default: 150).</dd>
<dt><code>-m</code> <i>integer</i>, <code>&#8211;margins</code>=<i>integer</i></dt>
<dd> Set margins in bp for <i>pdfcrop</i> (default: 0).</dd>
<dt><code>-o</code> <i>filename</i>, <code>&#8211;output</code>=<i>filename</i></dt>
<dd> Create <i>output</i> file.</dd>
<dt><code>&#8211;imgdir</code>=<i>dirname</i></dt>
<dd> Set name of directory to save images and files (default: images).</dd>
<dt><code>&#8211;prefix</code>=<i>string</i></dt>
<dd> Set <i>prefix</i> append to each generated files (default: fig).</dd>
<dt><code>&#8211;myverb</code>=<i>macroname</i></dt>
<dd> Add <tt>&quot;\macroname&quot;</tt> to verbatim inline search (default: myverb).</dd>
<dt><code>&#8211;clean</code>=<i>doc</i>|<i>pst</i>|<i>tkz</i>|<i>all</i>|<i>off</i></dt>
<dd> Removes specific block text in <i>output</i> file (default: doc).</dd>
<dt><code>&#8211;zip</code></dt>
<dd> Compress files generated in <tt>&quot;.zip&quot;</tt> format.</dd>
<dt><code>&#8211;tar</code></dt>
<dd> Compress files generated in <tt>&quot;.tar.gz&quot;</tt> format.</dd>
<dt><code>&#8211;srcenv</code></dt>
<dd> Create files with only code of environments.</dd>
<dt><code>&#8211;subenv</code></dt>
<dd> Create standalone files for environments.</dd>
<dt><code>&#8211;shell</code></dt>
<dd> Enable <tt>&quot;\write18{SHELL COMMAND}&quot;</tt>.</dd>
<dt><code>&#8211;latex</code></dt>
<dd> Using <tt>&quot;latex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>input</i> and <tt>&quot;pdflatex&quot;</tt> for compiler <i>output</i>.</dd>
<dt><code>&#8211;dvips</code></dt>
<dd> Using <tt>&quot;latex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>input</i> and <tt>&quot;latex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>output</i>.</dd>
<dt><code>&#8211;dvilua</code></dt>
<dd> Using <tt>&quot;dvilualatex&gt;dvips&gt;ps2pdf&quot;</tt> for compiler <i>input</i> and <tt>&quot;lualatex&quot;</tt> for compiler <i>output</i>.</dd>
<dt><code>&#8211;dvipdf</code></dt>
<dd> Using <tt>&quot;latex&gt;dvipdfmx&quot;</tt> for compiler <i>input</i> and <tt>&quot;latex&gt;dvipdfmx&quot;</tt> for compiler <i>output</i>.</dd>
<dt><code>&#8211;xetex</code></dt>
<dd> Using <tt>&quot;xelatex&quot;</tt> for compiler <i>input</i> and <i>output</i>.</dd>
<dt><code>&#8211;luatex</code></dt>
<dd> Using <tt>&quot;lualatex&quot;</tt> for compiler <i>input</i> and <i>output</i>.</dd>
<dt><code>&#8211;arara</code></dt>
<dd> Use <tt>&quot;arara&quot;</tt> for compiler <i>input</i> and <i>output</i>.</dd>
<dt><code>&#8211;latexmk</code></dt>
<dd> Using <tt>&quot;latexmk&quot;</tt> for compiler <i>output</i> file.</dd>
<dt><code>&#8211;norun</code></dt>
<dd> Run script, but no create images files.</dd>
<dt><code>&#8211;nopdf</code></dt>
<dd> Don&#8217;t create a <tt>&quot;.pdf&quot;</tt> image files.</dd>
<dt><code>&#8211;nocrop</code></dt>
<dd> Don&#8217;t run <i>pdfcrop</i>.</dd>
<dt><code>&#8211;extrenv</code>=<i>env1,env2,&#8230;</i></dt>
<dd> Add new environments to extract.</dd>
<dt><code>&#8211;skipenv</code>=<i>env1,env2,&#8230;</i></dt>
<dd> Skip some default environments to extract.</dd>
<dt><code>&#8211;verbenv</code>=<i>env1,env2,&#8230;</i></dt>
<dd> Add new verbatim environments.</dd>
<dt><code>&#8211;writenv</code>=<i>env1,env2,&#8230;</i></dt>
<dd> Add new verbatim write environments.</dd>
<dt><code>&#8211;deltenv</code>=<i>env1,env2,&#8230;</i></dt>
<dd> Delete environments in <i>output</i> file.</dd></dl>
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
<p> <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1), <code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1), <code>pdfcrop</code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1) </p>
