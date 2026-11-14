---
title: "prepmx(1)"
name: "prepmx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prepmx/"
description: "prepmx – preprocessor for PMX, easy music typesetting program"
---

<h2 class="name">NAME</h2>
<p> prepmx &#8211; preprocessor for PMX, easy music typesetting program </p>
<h2>SYNOPSIS</h2>
<p> <code>prepmx</code> [<i>options</i>] <i>jobname</i> [<i>outdir/</i>] [<i>stylefile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>M-Tx</code> is an easy to use preprocessor language for the <code>PMX</code> music typesetting program, aimed at people who are not experts. For an easy example, have a look at the following example: </p>
<p>&nbsp;<wbr>&nbsp;c2+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;g&nbsp;<wbr>&nbsp;<wbr>&nbsp;| b4d-&nbsp;<wbr>&nbsp;c1 d c2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;c8 g+&nbsp;e g c- g+&nbsp;e g | d g f g&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c- g+&nbsp;e g | </p>
<p> For syntax reference, please look at the M-Tx manual written by Dirk Laurie, the creator of the M-Tx language and the author of <code><a href="/docs/linux/man/1-prepmx/">prepmx</a></code>(1), its command-line utility. </p>
<p> <code>prepmx</code> processes the file <i>jobname</i>.mtx to generate <i>jobname</i>.pmx. You can then process this file using the <code><a href="/docs/linux/man/1-pmxab/">pmxab</a></code>(1) command, which is a preprocessor for MusiXTeX. </p>
<p> <i>outdir/</i> is the directory where `pmx&#8217; will put the final .tex file. Note that the trailing slash is mandatory. You can provide a <i>stylefile</i> for M-Tx. If omitted, the file `mtxstyle.txt&#8217; in the current directory is used, if there is one.</p>
<h2>OPTIONS</h2>
<p> Options can also be specified in a `Options:&#8217; line in the preamble, which takes precedence over the command line.</p>
<dl>
<dt><code>-b</code></p>
<dd> disable unbeamVocal</p>
<dt><code>-c</code></p>
<dd> disable doChords</p>
<dt><code>-D</code></p>
<dd> enable debugMode</p>
<dt><code>-f</code></p>
<dd> enable solfaNoteNames</p>
<dt><code>-i</code></p>
<dd> enable ignoreErrors</p>
<dt><code>-m</code></p>
<dd> disable doLyrics</p>
<dt><code>-n</code></p>
<dd> enable instrumentNames</p>
<dt><code>-t</code></p>
<dd> disable doUptext</p>
<dt><code>-u</code></p>
<dd> disable uptextOnRests</p>
<dt><code>-v</code></p>
<dd> enable beVerbose</p>
<dt><code>-w</code></p>
<dd> enable pedanticWarnings</p>
<dt><code>&#8211;</code><i>n</i></p>
<dd> select Special Case <i>n</i></p>
<dt><code>-H</code></p>
<dd> print enabled status of all options</dl>
<h2>EXIT STATUS</h2>
<p> If no error was found, <code>prepmx</code> exits with return code 0. In case of an error, the line number of the processed line is returned. This may not always be the line containing the actual error. A return status of 10000 means that the input file was empty or could not be opened.</p>
<h2>SEE ALSO</h2>
<p> <code>M-Tx</code> User&#8217;s Guide (mtxdoc.pdf)<br />
 <a href="/docs/linux/man/1-pmxab/">pmxab</a>(1), <a href="/docs/linux/man/1-musixtex/">musixtex</a>(1)</p>
<h2>AUTHORS</h2>
<p> prepmx was written by Dirk Laurie &lt;dirk.laurie [at] gmail.com&gt;. This manual page was written by Roland Stigge &lt;stigge [at] antcom.de&gt; for the Debian project. It was revised and extended by Nis Martensen &lt;nis.martensen [at] web.de&gt; and Bob Tennent &lt;rdt [at] cs.queensu.ca&gt;. </p>
<h2>Index</h2>
