---
title: "shtool-mkdir(1)"
name: "shtool-mkdir"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-mkdir/"
description: "shtool mkdir – GNU shtool"
---

<h2 class="name">NAME</h2>
<p> shtool mkdir &#8211; GNU shtool </p>
<p><a href="/docs/linux/man/1-mkdir/">mkdir</a>(1) style command</p>
<h2>SYNOPSIS</h2>
<p> <code>shtool mkdir</code> [<code>-t</code>|<code>&#8211;trace</code>] [<code>-f</code>|<code>&#8211;force</code>] [<code>-p</code>|<code>&#8211;parents</code>] [<code>-m</code>|<code>&#8211;mode</code> <i>mode</i>] [<code>-o</code>|<code>&#8211;owner</code> <i>owner</i>] [<code>-g</code>|<code>&#8211;group</code> <i>group</i>] <i>dir</i> [<i>dir</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This is a <i><a href="/docs/linux/man/1-mkdir/">mkdir</a></i>(1) style command with additional options and the ability to be smart if the directory already exists which is important for installation procedures.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Shows the actually involved shell commands.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Forced continuation and no complaints if directory already exists. Default is to terminate with error.</p>
<dt><code>-p</code>, <code>&#8211;parents</code></p>
<dd> Automatic parent directory creation. Default is to only create the last directory in the path and fail if parents are missing.</p>
<dt><code>-m</code>, <code>&#8211;mode</code> <i>mode</i></p>
<dd> The directory mode applied to the directory, see <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). Omitting mode skips this step and leaves the operating system default which is usually based on <i><a href="/docs/linux/man/1-umask/">umask</a></i>(1). Some directory modes require superuser privileges to be set. Default is to stick with operating system defaults.</p>
<dt><code>-o</code>, <code>&#8211;owner</code> <i>owner</i></p>
<dd> The directory owner name or id applied to the directory, see <i><a href="/docs/linux/man/1-chown/">chown</a></i>(1). This option requires superuser privileges to execute. Default is to skip this step and leave the operating system default which is usually based on the executing uid or the parent setuid directory.</p>
<dt><code>-g</code>, <code>&#8211;group</code> <i>group</i></p>
<dd> The directory group name or id applied to the directory, see <i><a href="/docs/linux/man/1-chgrp/">chgrp</a></i>(1). This option requires superuser privileges to execute to the fullest extend, otherwise the choice of <i>group</i> is limited on most operating systems. Default is to skip this step and leave the operating system default which is usually based on the executing gid or the parent setgid directory.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   Makefile
 install:
     shtool mkdir -f -p -m 755 $(bindir)
     shtool mkdir -f -p -m 755 $(mandir)/man1
      :
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>mkdir</code> command was originally written for Public Domain by Noah Friedman and later revised by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1999 for inclusion into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-mkdir/">mkdir</a></i>(1). </p>
<h2>Index</h2>
