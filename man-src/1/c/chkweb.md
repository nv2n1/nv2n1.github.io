---
title: "chkweb(1)"
name: "chkweb"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chkweb/"
description: "chkweb – runs the LaTeX parts of a CWEB file through chktex"
---

<h2 class="name">NAME</h2>
<p> chkweb &#8211; runs the LaTeX parts of a CWEB file through chktex </p>
<h2>SYNOPSIS</h2>
<p> <code>chkweb</code> <i>[-hiqrW] [-l &lt;rcfile&gt;] [-[wemn] &lt;[1-42]|all&gt;]</i> <i>[-d[0-&#8230;]] [-o &lt;outfile&gt;] [-[btxgI][0|1]]</i> <code>file1 file2 &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <i>chkweb</i> runs the <i>LaTeX</i> parts of a CWEB file through chktex.</p>
<h2>OPTIONS</h2>
<p> Miscellaneous options:</p>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Print a help screen.</p>
<dt><code>-i &#8211;license</code></p>
<dd> Show distribution information.</p>
<dt><code>-l &#8211;localrc</code></p>
<dd> Read local .chktexrc formatted file.</p>
<dt><code>-d &#8211;debug</code></p>
<dd> Debug information. Give it a number.</p>
<dt><code>-r &#8211;reset</code></p>
<dd> Reset settings to default.</dl>
<p> Muting warning messages:</p>
<dl>
<dt><code>-w &#8211;warnon</code></p>
<dd> Makes msg # given a warning and turns it on.</p>
<dt><code>-e &#8211;erroron</code></p>
<dd> Makes msg # given an error and turns it on.</p>
<dt><code>-m &#8211;msgon</code></p>
<dd> Makes msg # given a message and turns it on.</p>
<dt><code>-n &#8211;nowarn</code></p>
<dd> Mutes msg # given. </p>
</dl>
<p> Output control flags:</p>
<dl>
<dt><code>-V &#8211;pipeverb</code></p>
<dd> How errors are displayed when stdout != tty. Defaults to the same as -v.</p>
<dt><code>-s &#8211;splitchar</code></p>
<dd> String used to split fields when doing -v0</p>
<dt><code>-o &#8211;output</code></p>
<dd> Redirect error report to a file.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Shuts up about version information.</p>
<dt><code>-f &#8211;format</code></p>
<dd> Format to use for output </p>
</dl>
<p> Boolean switches (1 -&gt; enables / 0 -&gt; disables):</p>
<dl>
<dt><code>-b &#8211;backup</code></p>
<dd> Backup output file.</p>
<dt><code>-x &#8211;wipeverb</code></p>
<dd> Ignore contents of `erb&#8217; commands.</p>
<dt><code>-g &#8211;globalrc</code></p>
<dd> Read global .chktexrc file.</p>
<dt><code>-I &#8211;inputfiles</code></p>
<dd> Execute \input statements.</p>
<dt><code>-H &#8211;headererr</code></p>
<dd> Show errors found in front of egin{document}</dl>
<dl>
<dt><code>-W &#8211;version</code></p>
<dd> Version information </p>
</dl>
<p> If no LaTeX files are specified on the command line, we will read from stdin. For explanation of warning/error messages, please consult the main document /usr/share/doc/chktex/ChkTeX.dvi.gz. </p>
<h2>DISTRIBUTION</h2>
<p> Copyright (C) 1996 Jens T. Berger Thielemann </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <i>GNU General Public License </i> as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <code>WITHOUT ANY WARRANTY;</code> without even the implied warranty of <code>MERCHANTABILITY</code> or <code>FITNESS FOR A PARTICULAR PURPOSE.</code> See the <i>GNU General Public License</i> for more details. </p>
<p> You should have received a copy of the <code>GNU General Public License</code> along with this program; if not, write to the <i>Free Software Foundation, Inc.,</i> 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA </p>
<h2>ENVIRONMENT</h2>
<p> No environment variables are used.</p>
<h2>FILES</h2>
<p> None.</p>
<h2>AUTHOR</h2>
<p> Jens T. Berger Thielemann, <i>&lt;jensthi [at] ifi.uio.no&gt;</i> </p>
<p> This manual page was cobbled together by Clint Adams &lt;schizo [at] debian.org&gt;, based on the output of &quot;chktex &#8211;help&quot; and <a href="/docs/linux/man/1-deweb/">deweb</a>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-deweb/">deweb</a>(1), <a href="/docs/linux/man/1-chktex/">chktex</a>(1)</code> </p>
<h2>Index</h2>
