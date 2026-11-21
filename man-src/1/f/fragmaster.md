---

title: "fragmaster(1)"
name: "fragmaster"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fragmaster/"
description: "fragmaster – Using psfrag constructs with pdflatex"
---

<pre><code> fragmaster [options]
 Create EPS and PDF files with embedded psfrag substitutions.
 Options:
  -h,--help Brief usage guide.
  -m,--man Show full man page (needs perldoc)
  --clean Clean auto-generated $basename.{eps,pdf} files.
  --debug Show more info and leave temporary files behind.
  --force Rebuild everything ignoring modification times.
  --dirfm=file Use given file as optional per-directory
                     fragmaster fm control file instead of default
                     &quot;fragmaster.dfm&quot;.
</code></pre>
<p> <code>fragmaster</code> is a perl script that helps using psfrag constructs with <code>pdflatex</code>. </p>
<p> <code>psfrag</code> is a LaTeX package which allows one to replace text elements in included <font SIZE="-1">EPS</font> graphics by arbitrary LaTeX output. Because <code>psfrag</code> uses PostScript for making the replacements, in principle you can&#8217;t use <code>psfrag</code> with <code>pdflatex</code> which doesn&#8217;t have any interfaces to PostScript. </p>
<p> <code>fragmaster</code> produces a new <font SIZE="-1">EPS</font> from your original <font SIZE="-1">EPS</font> which already contains all those <code>psfrag</code> replacements. This new <font SIZE="-1">EPS</font> graphic actually can be converted to <font SIZE="-1">PDF</font> including all replacements. The resulting ``encapsulated&#8217;&#8216; <font SIZE="-1">PDF</font> can then be used with pdflatex. </p>
<p> <code>fragmaster</code> will scan the current directory for files which end in <i>_fm</i> and have a <i>_fm.eps</i> counterpart. Looking at the modification dates, the script checks if the output files have to be rebuilt and does so if necessary (a little like ``make&#8217;&#8216; would do it). </p>
<p> In your LaTeX document you can include the produced graphics using </p>
<pre><code> \includegraphics{&lt;graphics&gt;}
</code></pre>
<p> conveniently omitting file extension. <code>latex</code> will choose the <font SIZE="-1">EPS,</font> <code>pdflatex</code> will choose the <font SIZE="-1">PDF.</font>  </p>
<code></code><h3>fragmaster control file and other related files.</h3>
<p> To use the script you have to create two files per graphic: </p>
<pre><code>    * &lt;graphics&gt;_fm.eps: the EPS file itself,
    * &lt;graphics&gt;_fm: a fragmaster control file.
</code></pre>
<p> From these files the psfragged graphics will be created: </p>
<pre><code>    * &lt;graphics&gt;.eps,
    * &lt;graphics&gt;.pdf
</code></pre>
<p> The <i>_fm</i> control file is basically a LaTeX file (with optionally special comments) and can look like this: </p>
<pre><code> % Just an ordinary comment
 %
 % Some special comments:
 % fmclass: book
 % fmclassopt: 11pt
 % fmopt: width=6cm
 %
 % Another special comment:
 % head:
 % \usepackage{amsmath}
 % end head
 % psfrag commands:
 \psfrag{x}{$x$}
 \psfrag{y}{$y = x^2$}
</code></pre>
<p> Special comment <code>&quot;fmclass:&quot;</code> will make the script use given class instead of default <code>&quot;article&quot;</code> class. </p>
<p> Special comment <code>&quot;fmclassopt:&quot;</code> will make the script use given options as class options instead of default <code>&quot;12pt&quot;</code>. </p>
<p> The special comment <code>&quot;fmopt:&quot;</code> will be evaluated such that the following text will by passed as optional argument to <code>&quot;\includegraphics&quot;</code>. This way you can e.g. adjust the relation between graphics size and font size using something like <code>&quot;fmopt: width=6cm&quot;</code>. No global default for this. </p>
<p> The special comment construct <code>&quot;head:/end head&quot;</code> causes the lines in between to be included in the preamble of the LaTeX temporary document after having the leading comment characters ``%&#8216;&#8216; stripped off. This way, you can include LaTeX packages, as in <code>&quot;\usepackage{amsmath}&quot;</code>. No global default for this.  </p>
<code></code><h3>Per-directory fragmaster dir control file.</h3>
<p> You can set per-directory <code>&quot;fmclass:&quot;</code>, <code>&quot;fmclassopt:&quot;</code>, <code>&quot;fmopt:&quot;</code> and <code>&quot;head:/end head&quot;</code> options by means of a per-directory fragmaster control file <i>fragmaster.dfm</i> with similar syntax as above. You can use another file by means of the <code>--dirfm</code> option. Note that options set this way are mutually exclusive, any option set in per-file <i>_fm</i> file will completely override associated option in per-directory file, and options set in per-directory file will override initial defaults (<code>&quot;\documentclass[12pt]{article}&quot;</code>). Empty options are ignored. </p>
<p> This is work in progress and still needs extensive checking. Double-check that modification date based rebuilds are working properly.  </p>
<h2>KNOWN PROBLEMS</h2>
<p> In case the <font SIZE="-1">EPS</font> will be produced as landscape graphics, i.e. <code>gv</code> shows <i>Landscape</i> instead of <i>Portrait</i> in the menu bar, and the graphic will end up turned around 90 degrees in your document, then it is likely that your original <font SIZE="-1">EPS</font> is wider than it is tall. In this case some (more recent) versions of <code>dvips</code> make the ``smart&#8217;&#8216; assumption that your graphic is landscape, even though the graphic&#8217;s proportions don&#8217;t tell anything about the orientation of its contents... This still can happen in case your input <font SIZE="-1">EPS</font> matches a standard paper size. </p>
<p> Anyway, you can make <code>dvips</code> behave nicer by specifying the following line in <i>/usr/share/texmf/dvips/config/config.pdf</i> (or a local equivalent inside <i>/usr/local/share/texmf</i>): </p>
<p> @ custom 0pt 0pt </p>
<p> In the likely case that you&#8217;re wondering why, I&#8217;d recommend the <code>dvipsk</code> sources warmly to you...  </p>
<h2>AUTHORS</h2>
<p> Tilman Vogel &lt;tilman vogel web de&gt; (dot at dot) and Agustin Martin &lt;agustin6martin gmail com&gt; (at dot)  </p>
<h2>HISTORY</h2>
<p> This script was inspired by a posting from Karsten Roemke &lt;k roemke gmx de&gt; (dot at dot) with subject ``psfrag pdflatex, lange her&#8217;&#8216; in de.comp.text.tex on 2003-11-11 05:25:44 <font SIZE="-1">PST.</font> </p>
<p> Karsten Roemke was inspired for his solution by postings from Thomas Wimmer.  </p>
<h2>COPYRIGHT</h2>
<pre><code> Copyright (C) 2004 Tilman Vogel
 Copyright (C) 2011-2015 Agustin Martin
</code></pre>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
