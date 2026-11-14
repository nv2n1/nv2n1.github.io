---
title: "hivexml(1)"
name: "hivexml"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hivexml/"
description: "hivexml – Convert Windows Registry binary \"hive\" into XML"
---

<h2 class="name">NAME</h2>
<p> hivexml &#8211; Convert Windows Registry binary &quot;hive&quot; into XML </p>
<h2>SYNOPSIS</h2>
<pre>
 hivexml [-dk] hivefile &gt; output.xml
</pre>
<h2>DESCRIPTION</h2>
<p> This program converts a single Windows Registry binary &#8220;hive&#8221; file into a self-describing <font SIZE="-1">XML</font> format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Enable lots of debug messages. If you find a Registry file that this program cannot parse, please enable this option and post the complete output <i>and</i> the Registry file in your bug report.</p>
<dt><code>-k</code></p>
<dd> Keep going even if we find errors in the Registry file. This skips over any parts of the Registry that we cannot read.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-hivex/">hivex</a></i>(3), <i><a href="/docs/linux/man/1-hivexget/">hivexget</a></i>(1), <i><a href="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1), <i><a href="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1), <i><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1), <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), &lt;<a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a>&gt;, <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1).</p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 Red Hat Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font> </p>
<h2>Index</h2>
