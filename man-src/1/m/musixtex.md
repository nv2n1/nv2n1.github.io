---
title: "musixtex(1)"
name: "musixtex"
section: "1"
letter: "m"
url: "/docs/linux/man/1-musixtex/"
description: "musixtex – processes MusiXTeX files, using pre-processors prepmx, xml2pmx, pmxab and autosp as necessary, and then deletes intermediate and log files (unless -i is used)"
---

<h2 class="name">NAME</h2>
<p> musixtex &#8211; processes MusiXTeX files, using pre-processors prepmx, xml2pmx, pmxab and autosp as necessary, and then deletes intermediate and log files (unless <code>-i </code> is used) </p>
<h2>SYNOPSIS</h2>
<p> [ texlua ] <code>musixtex[.lua]</code> { <i>option </i> | <i>jobname </i> [ .xml | .mtx | .pmx | .aspc | .tex | .ltx ] } &#8230;</p>
<h2>DESCRIPTION</h2>
<dl>
<dt>If a jobname argument has a .tex extension, the default effect is to process the file using</p>
<dd>
<dt><code><a href="/docs/linux/man/1-etex/">etex</a></code>(1)</p>
<dd> (first pass)</p>
<dt><code><a href="/docs/linux/man/1-musixflx/">musixflx</a></code>(1)</p>
<dd> (second pass)</p>
<dt><code><a href="/docs/linux/man/1-etex/">etex</a></code>(1)</p>
<dd> (third pass)</p>
<dt><code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1)</p>
<dd> (dvi to Postscript)</p>
<dt><code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1)</p>
<dd> (Postscript to Portable Document Format)</p>
<dt>normally followed by removal of intermediate and log files. A log musixtex.log is generated, even if other log files are removed.</p>
<dd></dl>
<p> If a jobname argument has a .pmx extension, the file is first preprocessed using <code><a href="/docs/linux/man/1-pmxab/">pmxab</a></code>(1) and the resulting .tex file is processed as above. </p>
<p> If a jobname argument has a .xml extension, the file is first preprocessed using <code><a href="/docs/linux/man/1-xml2pmx/">xml2pmx</a></code>(1) and the resulting .pmx file is processed as above. </p>
<p> If a jobname argument has a .mtx extension, the file is first preprocessed using <code><a href="/docs/linux/man/1-prepmx/">prepmx</a></code>(1) and the resulting .pmx file is processed as above. </p>
<p> If a jobname argument has a .ltx extension, the file is processed using <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) (or <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1)) in place of <code>etex</code>. </p>
<p> If a jobname argument has a .aspc extension, the file is first preprocessed using <code><a href="/docs/linux/man/1-autosp/">autosp</a></code>(1) and the resulting .tex or .ltx file is processed as above. </p>
<p> If a jobname argument has none of these extensions, the script will look for a file <i>jobname</i>.xml or <i>jobname</i>.mtx or <i>jobname</i>.pmx or <i>jobname</i>.aspc or <i>jobname</i>.tex or <i>jobname</i>.ltx<i>,</i> in that order, and process it as above.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, -version, &#8211;version</code></p>
<dd> output program name and version number, and quit</p>
<dt><code>-h, -help, &#8211;help</code></p>
<dd> output usage summary and quit</p>
<dt><code>-l </code></p>
<dd> assume LaTeX source; implied if the file has .ltx extension</p>
<dt><code>-p </code></p>
<dd> change the TeX processor to <code><a href="/docs/linux/man/1-pdfetex/">pdfetex</a></code>(1) or <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1) (and doesn&#8217;t run a dvi processor)</p>
<dt><code>-c</code></p>
<dd> preprocess pmx file using <code><a href="/docs/linux/man/1-pmxchords/">pmxchords</a></code>(1)</p>
<dt><code>-d </code></p>
<dd> don&#8217;t generate a .ps file and change the dvi processor to <code><a href="/docs/linux/man/1-dvipdfm/">dvipdfm</a></code>(1)</p>
<dt><code>-D dvix</code></p>
<dd> use <code>dvix </code> as the dvi processor; e.g., -D &quot;dvipdfm -m 0.9&quot;. Use -d <i>before </i> -D to suppress .ps generation.</p>
<dt><code>-P ps2pdf</code></p>
<dd> use <code>ps2pdf</code> as the Postscript processor; e.g., -P &quot;ps2pdf -sPAPERSIZE=a4&quot;</p>
<dt><code>-F fmt</code></p>
<dd> use <code>fmt</code> as the TeX processor; e.g., -F &quot;luatex &#8211;output-format=dvi&quot;</p>
<dt><code>-m</code></p>
<dd> stop processing at the pmx file</p>
<dt><code>-M mtxx</code></p>
<dd> use <code>mtxx</code> as the mtx preprocessor; e.g., -M &quot;prepmx -i&quot;.</p>
<dt><code>-X pmxx </code></p>
<dd> use <code>pmxx</code> as the pmx preprocessor; e.g., -X &quot;./pmxab&quot;,</p>
<dt><code>-A aspcx</code></p>
<dd> use <code>aspcx</code> as the aspc preprocessor; e.g., -A &quot;autosp -l&quot;.</p>
<dt><code>-L xmlx</code></p>
<dd> use <code>xmlx</code> as the xml preprocessor; e.g., -L &quot;./XML2PMX&quot;.</p>
<dt><code>-t</code></p>
<dd> stop processing at the tex/mid files</p>
<dt><code>-s </code></p>
<dd> stop processing at the dvi file</p>
<dt><code>-g</code></p>
<dd> stop processing at the ps file</p>
<dt><code>-i</code></p>
<dd> retain intermediate and log files</p>
<dt><code>-1</code></p>
<dd> one-pass [pdf][la]tex processing; i.e., without calling <code>musixflx</code></p>
<dt><code>-x</code></p>
<dd> call <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1) to update index database</p>
<dt><code>-f</code></p>
<dd> restore default processing</p>
<dt><code>-q</code></p>
<dd> quiet mode (only musixtex&#8217;s own messages); other messages are diverted to a temporary file. If an error occurs at the TeX stage, processing halts immediately and the tail of the log file is sent to stderr. Version information is copied from the temporary file to the log file. </p>
<dt>Options affect processing of all succeeding MusiXTeX files unless changed by another option. Option flags cannot be combined; e.g., use <code> -l -x </code> rather than <code> -lx</code>.</p>
<dd>
<p> Note that four TeX engines are available via the -l and -p options:</p>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;etex&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;latex&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-l<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pdfetex&nbsp;<wbr>&nbsp;<wbr>&nbsp;-p<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pdflatex&nbsp;<wbr>&nbsp;-l -p</p>
<dt>If the -F option is used, options -l and -p need to be set if the engine name does not contain &quot;latex&quot; and &quot;pdf&quot; respectively. For example, the above four engines can be replaced by:</p>
<dd>
&nbsp;<wbr>&nbsp;-F&nbsp;&quot;luatex &#8211;output-format=dvi&quot;&nbsp;<br />
&nbsp;<wbr>&nbsp;-F&nbsp;&quot;lualatex &#8211;output-format=dvi&quot;<br />
&nbsp;<wbr>&nbsp;-F&nbsp;&quot;luatex&quot;&nbsp;-p<br />
&nbsp;<wbr>&nbsp;-F&nbsp;&quot;lualatex&quot;&nbsp;-p </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autosp/">autosp</a></code>(1), <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1), <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-pdfetex/">pdfetex</a></code>(1), <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1), <code><a href="/docs/linux/man/1-makeindex/">makeindex</a></code>(1), <code><a href="/docs/linux/man/1-musixflx/">musixflx</a></code>(1), <code><a href="/docs/linux/man/1-dvipdfm/">dvipdfm</a></code>(1), <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1), <code><a href="/docs/linux/man/1-pmxab/">pmxab</a></code>(1), <code><a href="/docs/linux/man/1-pmxchords/">pmxchords</a></code>(1), <code><a href="/docs/linux/man/1-prepmx/">prepmx</a></code>(1), <code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1), <code><a href="/docs/linux/man/1-xml2pmx/">xml2pmx</a></code>(1) and musixdoc.pdf.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Bob Tennent &lt;rdt [at] cs.queensu.ca&gt;. </p>
<h2>Index</h2>
