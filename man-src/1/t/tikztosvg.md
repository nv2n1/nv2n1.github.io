---
title: "tikztosvg(1)"
name: "tikztosvg"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tikztosvg/"
description: "tikztosvg – Render TikZ diagrams to SVG."
---
<h2 class="name">NAME</h2>
<p> tikztosvg - Render TikZ diagrams to SVG. </p>
<h2>SYNOPSIS</h2>
<p> <code>tikztosvg</code> [<i>OPTION</i>]... <i>INPUT_PATH</i>  </p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-tikztosvg/">tikztosvg</a>(1) command renders TikZ diagrams to SVG. </p>
<p> If <i>INPUT_PATH</i> is set to <i>-</i> the input will be read from stdin.  </p>
<h2>OPTIONS</h2>
<p> <code>-o, --output</code>=<i>OUTPUT_PATH</i> </p>
<dl>
<dd> <p> Write output to file <i>OUTPUT_PATH</i>. If set to <i>-</i> the output will be written to stdout. Defaults to the base name of the input file suffixed with the <i>.svg</i> extension. The file is resolved relative to the working directory. </p>
 </dd></dl>
<p> <code>-p, --package</code>=+<i>PACKAGE</i> </p>
<dl>
<dd> <p> Include <i>\usepackage{PACKAGE}</i> when rendering the diagram. The tikz, tikz-cd, pgfplots, amsmath and amssymb packages are always included by default. </p>
 </dd></dl>
<p> <code>-l, --library</code>=+_LIBRARY </p>
<dl>
<dd> <p> Include <i>\usetikzlibrary{LIBRARY}</i> when rendering the diagram. </p>
 </dd></dl>
<p> <code>-q, --quiet</code> </p>
<dl>
<dd> <p> Silence application log messages and script warnings. </p>
 </dd></dl>
<p> <code>--lualatex</code> </p>
<dl>
<dd> <p> Use LuaTeX as the TeX engine. LuaTeX is already the default, so this option doesn&#8217;t really do much. </p>
 </dd></dl>
<p> <code>--xelatex</code> </p>
<dl>
<dd> <p> Use XeTeX as the TeX engine. </p>
 </dd></dl>
<p> <code>--pdflatex</code> </p>
<dl>
<dd> <p> Use pdfTeX as the TeX engine. </p>
 </dd></dl>
<p> <code>-h, --help</code> </p>
<dl>
<dd> <p> Print a help message. </p>
 </dd></dl>
<p> <code>-v, --version</code> </p>
<dl>
<dd> <p> Prints version information. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>tikztosvg</code> requires XeTeX and pdf2svg to be installed. Make sure any additional LaTeX packages are installed before using them in a diagram.  </p>
<h2>EXIT STATUS</h2>
<p> <code>0</code> </p>
<dl>
<dd> <p> Success. </p>
 </dd></dl>
<p> <code>1</code> </p>
<dl>
<dd> <p> Failure (syntax or usage error; configuration error). </p>
 </dd></dl>
<p> <code>[n]</code> </p>
<dl>
<dd> <p> Failure (document processing failure). </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> <code>tikztosvg</code> was written by Pablo </p>
<p> <code>pdf2svg</code> was written by David Barton and Matthew Flaschen  </p>
<h2>RESOURCES</h2>
<p> Git source repository on sourcehut </p>
<dl>
<dd> <p> <i></i> &lt;<a rel="nofollow" href="https://git.sr.ht/~pablo-pie/tikztosvg">https://git.sr.ht/~pablo-pie/tikztosvg</a>&gt; </p>
 </dd></dl>
<p> Bug tracker </p>
<dl>
<dd> <p> <i></i> &lt;<a rel="nofollow" href="https://todo.sr.ht/~pablo-pie/tikztosvg">https://todo.sr.ht/~pablo-pie/tikztosvg</a>&gt; </p>
 </dd></dl>
<p> CTAN package </p>
<dl>
<dd> <p> <i></i> &lt;<a rel="nofollow" href="https://www.ctan.org/pkg/tikztosvg">https://www.ctan.org/pkg/tikztosvg</a>&gt; </p>
 </dd></dl>
<p> TeXLive </p>
<dl>
<dd> <p> <i></i> &lt;<a rel="nofollow" href="https://tug.org/texlive/">https://tug.org/texlive/</a>&gt; </p>
 </dd></dl>
<p> LuaTeX </p>
<dl>
<dd> <p> <i></i> &lt;<a rel="nofollow" href="http://luatex.org/">http://luatex.org/</a>&gt; </p>
 </dd></dl>
<p> XeTeX </p>
<dl>
<dd> <p> <i></i> &lt;<a rel="nofollow" href="http://xetex.sourceforge.net/">http://xetex.sourceforge.net/</a>&gt; </p>
 </dd></dl>
<p> <code>pdfTeX</code> <i></i> &lt;<a rel="nofollow" href="https://www.tug.org/applications/pdftex/">https://www.tug.org/applications/pdftex/</a>&gt;  </p>
<h2>COPYING</h2>
<p> Copyright (C) 2021 Pablo. Free use of this software is granted under the terms of the GPL-3.0 License. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">ENVIRONMENT</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">EXIT STATUS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">RESOURCES</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">COPYING</a></dt>
<dd>  </dd></dl>
