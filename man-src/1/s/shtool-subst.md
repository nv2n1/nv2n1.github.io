---
title: "shtool-subst(1)"
name: "shtool-subst"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-subst/"
description: "shtool subst – GNU shtool"
---

<h2 class="name">NAME</h2>
<p> shtool subst &#8211; GNU shtool </p>
<p><a href="/docs/linux/man/1-sed/">sed</a>(1) substitution operations</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool subst</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-t</code>|<code>&#8211;trace</code>] [<code>-n</code>|<code>&#8211;nop</code>] [<code>-w</code>|<code>&#8211;warning</code>] [<code>-q</code>|<code>&#8211;quiet</code>] [<code>-s</code>|<code>&#8211;stealth</code>] [<code>-i</code>|<code>&#8211;interactive</code>] [<code>-b</code>|<code>&#8211;backup</code> <i>ext</i>] [<code>-e</code>|<code>&#8211;exec</code> <i>cmd</i>] [<code>-f</code>|<code>&#8211;file</code> <i>cmd-file</i>] [<i>file</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This command applies one or more <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) substitution operations to <i>stdin</i> or any number of files.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display some processing information.</dd>
<dt><code>-t</code>, <code>&#8211;trace</code></dt>
<dd> Enable the output of the essential shell commands which are executed.</dd>
<dt><code>-n</code>, <code>&#8211;nop</code></dt>
<dd> No operation mode. Actual execution of the essential shell commands which would be executed is suppressed.</dd>
<dt><code>-w</code>, <code>&#8211;warning</code></dt>
<dd> Show warning on substitution operation resulting in no content change on <i>every</i> file. The default is to show a warning on substitution operations resulted in no content change on <i>all</i> files.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Suppress warning on substitution operation resulting in no content change.</dd>
<dt><code>-s</code>, <code>&#8211;stealth</code></dt>
<dd> Stealth operation. Preserve timestamp on <i>file</i>.</dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> Enter interactive mode where the user has to approve each operation.</dd>
<dt><code>-b</code>, <code>&#8211;backup</code> <i>ext</i></dt>
<dd> Preserve backup of original file using file name extension <i>ext</i>. Default is to overwrite the original file.</dd>
<dt><code>-e</code>, <code>&#8211;exec</code> <i>cmd</i></dt>
<dd> Specify <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) command directly.</dd>
<dt><code>-f</code>, <code>&#8211;file</code> <i>cmd-file</i></dt>
<dd> Read <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) command from <i>file</i>.</dd></dl>
<h2>EXAMPLE</h2>
<pre><code>
#shell script
shtool subst - i - e 's;(c) \([0-9]*\)-2000;(c) \1-2001;' *.[ch]
#RPM spec - file
                       % install shtool subst -
    v - n - e 's;^\(prefix=\).*;\1 $RPM_BUILD_ROOT%{_prefix};g' - e 's;^\(sysconfdir=\).*;\1 $RPM_BUILD_ROOT%{_prefix}/etc;g' \
         `find.- name Makefile - print` make install
</code></pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>subst</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 2001 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>. It was prompted by the need to have a uniform and convenient patching frontend to <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) operations in the <code>OpenPKG</code> package specifications.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1). </p>
<h2>Index</h2>
