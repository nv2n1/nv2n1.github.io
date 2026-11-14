---
title: "shtool-install(1)"
name: "shtool-install"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-install/"
description: "shtool install – GNU shtool"
---

<h2 class="name">NAME</h2>
<p> shtool install &#8211; GNU shtool </p>
<p><a href="/docs/linux/man/1-install/">install</a>(1) command</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool install</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-t</code>|<code>&#8211;trace</code>] [<code>-d</code>|<code>&#8211;mkdir</code>] [<code>-c</code>|<code>&#8211;copy</code>] [<code>-C</code>|<code>&#8211;compare-copy</code>] [<code>-s</code>|<code>&#8211;strip</code>] [<code>-m</code>|<code>&#8211;mode</code> <i>mode</i>] [<code>-o</code>|<code>&#8211;owner</code> <i>owner</i>] [<code>-g</code>|<code>&#8211;group</code> <i>group</i>] [<code>-e</code>|<code>&#8211;exec</code> <i>sed-cmd</i>] <i>file</i> [<i>file</i> &#8230;] <i>path</i></p>
<h2>DESCRIPTION</h2>
<p> This command installs a one or more <i>file</i>s to a given target <i>path</i> providing all important options of the <font SIZE="-1">BSD</font> <i><a href="/docs/linux/man/1-install/">install</a></i>(1) command. The trick is that the functionality is provided in a portable way.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display some processing information.</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Enable the output of the essential shell commands which are executed.</p>
<dt><code>-d</code>, <code>&#8211;mkdir</code></p>
<dd> To maximize <font SIZE="-1">BSD</font> compatiblity, the <font SIZE="-1">BSD &quot;</font><code>shtool</code> <tt>&quot;install -d&quot;</tt>&#8220; usage is internally mapped to the &#8221;<code>shtool</code> <tt>&quot;mkdir -f -p -m 755&quot;</tt>&quot; command.</p>
<dt><code>-c</code>, <code>&#8211;copy</code></p>
<dd> Copy the <i>file</i> to the target <i>path</i>. Default is to move.</p>
<dt><code>-C</code>, <code>&#8211;compare-copy</code></p>
<dd> Same as <code>-c</code> except if the destination file already exists and is identical to the source file, no installation is done and the target remains untouched.</p>
<dt><code>-s</code>, <code>&#8211;strip</code></p>
<dd> This option strips program executables during the installation, see <i><a href="/docs/linux/man/1-strip/">strip</a></i>(1). Default is to install verbatim.</p>
<dt><code>-m</code>, <code>&#8211;mode</code> <i>mode</i></p>
<dd> The file mode applied to the target, see <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). Setting mode to &quot;<tt>&quot;-&quot;</tt>&quot; skips this step and leaves the operating system default which is usually based on <i><a href="/docs/linux/man/1-umask/">umask</a></i>(1). Some file modes require superuser privileges to be set. Default is 0755.</p>
<dt><code>-o</code>, <code>&#8211;owner</code> <i>owner</i></p>
<dd> The file owner name or id applied to the target, see <i><a href="/docs/linux/man/1-chown/">chown</a></i>(1). This option requires superuser privileges to execute. Default is to skip this step and leave the operating system default which is usually based on the executing uid or the parent setuid directory.</p>
<dt><code>-g</code>, <code>&#8211;group</code> <i>group</i></p>
<dd> The file group name or id applied to the target, see <i><a href="/docs/linux/man/1-chgrp/">chgrp</a></i>(1). This option requires superuser privileges to execute to the fullest extend, otherwise the choice of <i>group</i> is limited on most operating systems. Default is to skip this step and leave the operating system default which is usually based on the executing gid or the parent setgid directory.</p>
<dt><code>-e</code>, <code>&#8211;exec</code> <i>sed-cmd</i></p>
<dd> This option can be used one or multiple times to apply one or more <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) commands to the file contents during installation.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   Makefile
 install:
      :
     shtool install -c -s -m 4755 foo $(bindir)/
     shtool install -c -m 644 foo.man $(mandir)/man1/foo.1
     shtool install -c -m 644 -e &quot;s/@p@/$prefix/g&quot; foo.conf $(etcdir)/
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>install</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1997 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>. It was prompted by portability issues in the installation procedures of <font SIZE="-1"><code>OSSP</code></font> libraries.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-umask/">umask</a></i>(1), <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1), <i><a href="/docs/linux/man/1-chown/">chown</a></i>(1), <i><a href="/docs/linux/man/1-chgrp/">chgrp</a></i>(1), <i><a href="/docs/linux/man/1-strip/">strip</a></i>(1), <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1). </p>
<h2>Index</h2>
