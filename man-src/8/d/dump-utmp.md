---
title: "dump-utmp(8)"
name: "dump-utmp"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dump-utmp/"
description: "dump-utmp – print an utmp file in human-readable format."
---

<p>dump-utmp &#8211; print an utmp file in human-readable format.</p>
<h2>Synopsis</h2>
<p><code>dump-utmp</code> [<code>-r</code>|<code>&#8211;reverse</code>] [<code>-R</code>|<code>&#8211;raw</code>] [<code>-n</code>|<code>&#8211;num</code> <i>recs</i>] [<code>-h</code>|<code>&#8211;help</code>] [ <i>files</i>] </p>
<h2>Description</h2>
<p><code>dump-utmp</code> <i>filename</i> prints a list of all logins. This list is usually written in <i>/var/log/wtmp</i>. All fields are separated by vertical line. Fields are: <i>user name</i>, <i>tty</i>, <i>type</i>, <i>id</i>, <i>pid</i>, <i>hostaddr</i>, <i>host</i>, <i>time</i>. </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints the usage string and default locations of system files to standard output and exits.</p>
<dt><code>-n, &#8211;num recs</code></p>
<dd>Number of lines to print.</p>
<dt><code>-r, &#8211;reverse</code></p>
<dd>Start printing from last records.</p>
<dt><code>-R, &#8211;raw</code></p>
<dd>Print raw records, not human-readable. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>wtmp</i></p>
<dd>The system wide login record file. See <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5) for further details. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-sa/">sa</a></code>(8). </p>
<h2>Author</h2>
<p>The GNU accounting utilities were written by Noel Cragg &lt;noel [at] gnu.ai.mit.edu&gt;. </p>
<p> This manual page was written by Ognyan Kulev &lt;ogi [at] fmi.uni-sofia.bg&gt; and updated by Daniel Baumann &lt;daniel [at] debian.org&gt; for the Debian project (but may be used by others).</p>
