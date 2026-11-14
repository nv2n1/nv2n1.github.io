---
title: "munin-check(8)"
name: "munin-check"
section: "8"
letter: "m"
url: "/docs/linux/man/8-munin-check/"
description: "munin-check – A program to fix permissions of Munin directories and files"
---

<p>munin-check &#8211; A program to fix permissions of Munin directories and files</p>
<h2>Synopsis</h2>
<p>munin-check [&#8211;options]</p>
<h2>Options</h2>
<dl>
<dt><code>-h|&#8211;help</code></p>
<dd>
<pre> Display usage information.</pre>
<dt><code>-f|&#8211;fix-permissions</code></p>
<dd>Fix the permissions of the munin dirs and files.</dl>
<h2>Description</h2>
<p>munin-check is a utility that fixes the permissions of the munin directories and files. </p>
<p> Note: munin-check needs superuser rights. </p>
<p> Please don&#8217;t use this script if you are using &#8216;graph_strategy cgi&#8217;! It doesn&#8217;t care about the right permissions for www-data yet&#8230;</p>
<h2>Author</h2>
<p>Matthias Schmitz</p>
<h2>Copyright</h2>
<p>Copyright (C) 2002-2008 Matthias Schmitz. </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License</p>
