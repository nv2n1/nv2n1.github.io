---
title: "groff_filenames(5)"
name: "groff_filenames"
section: "5"
letter: "g"
url: "/docs/linux/man/5-groff_filenames/"
description: "groff_filenames – filename extensions for roff and groff"
---

<p>groff_filenames &#8211; filename extensions for roff and groff</p>
<h2>Description</h2>
<p>Since the evolution of <i>roff</i> in the 1970s, a whole bunch of filename extensions for <i>roff</i> files were used. </p>
<p> The <i>roff</i> extensions refer to preprocessors or macro packages. These extensions are fixed in all <i>Unix</i>-like operating systems. </p>
<p> Later on, <code>groff</code> added some more extensions. This <i>man page</i> is about these filename extensions.</p>
<h2>Compression Of Roff Files</h2>
<p>Each <i>roff</i> file can be optionally <i>compressed</i>. That means that the <i>total filename</i> ends with a <i>compressor name</i>. So the whole filename has the structure <i>&lt;name&gt;</i>.<i>&lt;extension&gt;[</i>.<i>&lt;compression&gt;]</i>. </p>
<p> Best-known are the <i>compressor extensions</i> <code>.Z</code>, <code>.gz</code>, and <code>.bzip2</code>. Relatively new is <code>.xz</code>. </p>
<p> From now on, we will ignore the <i>compressions</i> and only comment the structure <i>&lt;name&gt;</i><code>.</code><i>&lt;extension&gt;</i>.</p>
<h2>Man Pages</h2>
<p>The <i>Unix manual pages</i> are widely called <i>man pages</i>. The <i>man page</i> style is the best known part of the <i>roff</i> language. </p>
<p> The extensions for <i>man</i> should be better documented. So this is documented here. </p>
<p> Files written in the <i>man</i> language use the following extension: <code>*.</code><i>&lt;section&gt;[&lt;group&gt;]</i>.</p>
<h3>Man page Sections</h3>
<p>The traditional <i>man page &lt;section&gt;</i> is a digit from <code>1</code> to <code>8</code>.</p>
<dl>
<dt><i>&lt;name&gt;</i><code>.1</code></p>
<dd><i>&lt;name&gt;</i><code>.2</code> <i>&lt;name&gt;</i><code>.3</code> <i>&lt;name&gt;</i><code>.4</code> <i>&lt;name&gt;</i><code>.5</code> <i>&lt;name&gt;</i><code>.6</code> <i>&lt;name&gt;</i><code>.7</code> <i>&lt;name&gt;</i><code>.8</code> Classic man page <i>sections</i>.</dl>
<p> In older commercial <i>Unix</i> systems, the 3 characters <code>l</code>, <code>n</code>, and <code>o</code> were also used as <i>section</i> names. This is today <i>deprecated</i>, but there are still documents in this format.</p>
<dl>
<dt><i>&lt;name&gt;</i><code>.l</code></p>
<dd><i>&lt;name&gt;</i><code>.n</code> <i>&lt;name&gt;</i><code>.o</code> <i>Deprecated</i> man page sections, which stood for &#8220;local&#8221;, &#8220;new&#8221;, and &#8220;old&#8221;, respectively.</dl>
<h3>Man page Group Extensions</h3>
<p>The <i>&lt;group&gt;</i> extension in <code>.</code><i>&lt;section&gt;[&lt;group&gt;]</i> is optional, but it can be any string of word characters. Usually programmers use a group name that is already used, e.g. <code>x</code> for X Window System documents or <code>tcl</code> to refer to the <i>Tcl</i> programming language. </p>
<p> Examples:</p>
<dl>
<dt><code>groff.1</code></p>
<dd>is the man page for <code>groff</code> in <i>section</i> <code>1</code> without a <i>group</i></p>
<dt><code>xargs.1posix.gz</code></p>
<dd>is the man page for the program <code>xargs</code> in <i>section</i> <code>1</code> and <i>group</i> <code>posix</code>; moreover it is <i>compressed</i> with <code>gz</code> (<code>gzip</code>).</p>
<dt><code>config.5ssl</code></p>
<dd><i>OpenSSL CONF</i> library configuration files from <i>section</i> <code>5</code> with <i>group</i> <code>ssl</code>.</p>
<dt><code>dpkg-reconfigure.8cdebconf</code></p>
<dd>man page for the program <code>dpkg-reconfigure</code> in <i>section</i> <code>8</code> and <i>group</i> <code>cdebconf</code>.</dl>
<h3>Source of man pages</h3>
<p>There are 2 <i>roff</i> languages for writing man pages: <code>man</code> and <code>mdoc</code>. </p>
<p> The names of these 2 styles are taken as <i>extensions</i> for the source code files of man pages in the <i>groff</i> package.</p>
<dl>
<dt><i>&lt;name&gt;</i><code>.man</code></p>
<dd><i>traditional</i> Unix-like man page format within groff source files.</p>
<dt><i>&lt;name&gt;</i><code>.</code><i>n</i></p>
<dd>A temporary man page file produced from a <i>name</i><code>.man</code> man page by a run of <code>make</code> within the <code>groff</code> source package.</p>
<dt><i>&lt;name&gt;</i><code>.mdoc</code></p>
<dd>Man page format in BSD.</p>
<dt><i>&lt;name&gt;</i><code>.1b</code></p>
<dd>Man page format in <i>heirloom roff .</i></p>
<dt><i>&lt;name&gt;</i><code>.mandoc</code></p>
<dd>Files using this extension recognize both man page formats in <code>groff</code> and other processors.</dl>
<h2>Traditional Troff Extensions</h2>
<h3>Files Using Macro Packages</h3>
<p>The <i>classical roff</i> languages were interpreted by the traditional <code>troff</code> and <code>nroff</code> programs. </p>
<p> There were several <i>roff</i> languages, each represented by a <i>macro-package</i>. Each of these provided a suitable file name <i>extension</i>:</p>
<dl>
<dt><i>&lt;name&gt;</i><code>.me</code></p>
<dd><i>roff</i> file using the <code>me</code> <i>macro package</i>.</p>
<dt><i>&lt;name&gt;</i><code>.mm</code></p>
<dd><i>roff</i> file using the <code>mm</code> <i>macro package</i></p>
<dt><i>&lt;name&gt;</i><code>.ms</code></p>
<dd><i>roff</i> file using the <code>ms</code> <i>macro package</i></dl>
<p> All of these classical <i>roff</i> languages and their extensions are still very active in <code>groff</code>.</p>
<h3>Source Code for Macro Packages (TMAC Files)</h3>
<p>In traditional <i>roff</i> the source code for the macro packages was stored in <i>TMAC</i> files. Their file names have the form:</p>
<dl>
<dt><code>tmac.</code><i>&lt;package&gt;</i>,</p>
<dd><i>&lt;package&gt;</i> is the name of the macro package without the leading <code>m</code> character, which is reintegrated by the option <code>-m</code>.</dl>
<p> For example, <code>tmac.an</code> is the source for the <code>man</code> macro package. </p>
<p> In the <code>groff</code> source, more suitable file names were integrated, see later on.</p>
<h3>Preprocessors</h3>
<p>Moreover, the following <i>preprocessors</i> were used as filename extension:</p>
<dl>
<dt><i>&lt;name&gt;</i><code>.chem</code></p>
<dd>for the integration of chemical formulas</p>
<dt><i>&lt;name&gt;</i><code>.eqn</code></p>
<dd>for the mathematical use of equations</p>
<dt><i>&lt;name&gt;</i><code>.pic</code></p>
<dd>graphical tool</p>
<dt><i>&lt;name&gt;</i><code>.tbl</code></p>
<dd>for tables with <i>tbl</i></p>
<dt><i>&lt;name&gt;</i><code>.ref</code></p>
<dd>for files using the <code>prefer</code> <i>preprocessor</i></dl>
<h3>Classical Roff Files</h3>
<dl>
<dt><i>&lt;name&gt;</i><code>.t</code></p>
<dd><i>&lt;name&gt;</i><code>.tr</code> for files using the <i>roff</i> language of any kind</dl>
<h2>New Groff Extensions</h2>
<p><i>GNU roff</i> <code>groff</code> is the actual <i>roff</i> standard, both for classical <i>roff</i> and new extensions. So even the used new extensions in the source code should be regarded as actual standard. The following extensions are used instead of classical <code>.t</code> or <code>.tr</code>:</p>
<dl>
<dt><i>&lt;name&gt;</i><code>.groff</code></p>
<dd><i>&lt;name&gt;</i><code>.roff</code> general ending for files using the <i>groff language</i></dl>
<h3>Source Code for Macro Packages (TMAC Files)</h3>
<p>As the classical form <code>tmac.</code><i>&lt;package_without_m&gt;</i>, of the <i>TMAC</i> file names is quite strange, <i>groff</i> added the following structures:</p>
<dl>
<dt><i>&lt;package_without_m&gt;</i><code>.tmac</code></p>
<dd><code>m</code><i>&lt;package&gt;</i><code>.tmac</code> <code>groff_m</code><i>&lt;package&gt;</i><code>.tmac</code></dl>
<h3>Files Using new Macro Packages</h3>
<p><i>Groff</i> uses the following new macro packages:</p>
<dl>
<dt><i>&lt;name&gt;</i><code>.mmse</code></p>
<dd>file with swedish <code>mm</code> <i>macros</i> for <code>groff</code></p>
<dt><i>&lt;name&gt;</i><code>.mom</code></p>
<dd>files written in the <i>groff macro package</i> <code>mom</code></p>
<dt><i>&lt;name&gt;</i><code>.www</code></p>
<dd>files written in <code>HTML</code>-like <i>groff</i> <i>macros</i>.</dl>
<h3>Preprocessors and Postprocessors</h3>
<dl>
<dt><i>&lt;name&gt;</i><code>.hdtbl</code></p>
<dd>Heidelberger tables, an alternative to the preprocessor <i>tbl</i>. See <code><a href="/docs/linux/man/7-groff_hdtbl/">groff_hdtbl</a></code>(7).</p>
<dt><i>&lt;name&gt;</i><code>.grap</code></p>
<dd>files written for the graphical <code>grap</code> processor.</p>
<dt><i>&lt;name&gt;</i><code>.grn</code></p>
<dd>for including <code><a href="/docs/linux/man/1-gremlin/">gremlin</a></code>(1), pictures, see <code><a href="/docs/linux/man/1-grn/">grn</a></code>(1).</p>
<dt><i>&lt;name&gt;</i><code>.pdfroff</code></p>
<dd>transform this file with <code>pdfroff</code> of the <i>groff</i> system</dl>
<h2>Authors</h2>
<p>This document was written by Bernd Warken</p>
<h2>See Also</h2>
<dl>
<dt>History and future</p>
<dd><code><a href="/docs/linux/man/7-roff/">roff</a></code>(7), <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7), <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7), <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dt><i>Compression</i></p>
<dd><code>uncompress</code>(1posix), <code><a href="/docs/linux/man/1-gzip2/">gzip2</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1)</dl>
<p> A man page of the naming form <i>name</i><code>(</code><i>n</i><code>)</code> can be read in text mode by</p>
<dl>
<dd><code>man</code><i> n name</i></dl>
<p> or in graphical mode (PDF) by</p>
<dl>
<dd><code>groffer</code><i> n name</i></dl>
<p> <i>Gunnar Ritter&#8217;s Heirloom roff project</i> You can get this package with the shell command:</p>
<dl>
<dd>$ <code>git clone <a rel="nofollow" href="https://github.com/n-t-roff/heirloom-doctools">https://github.com/n-t-roff/heirloom-doctools</a></code></dl>
