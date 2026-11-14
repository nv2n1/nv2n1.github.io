---
title: "febootstrap-run(8)"
name: "febootstrap-run"
section: "8"
letter: "f"
url: "/docs/linux/man/8-febootstrap-run/"
description: "febootstrap-run – Run extra commands in febootstrap root filesystem"
---

<p>febootstrap-run &#8211; Run extra commands in febootstrap root filesystem</p>
<h2>Synopsis</h2>
<pre> febootstrap-run [--options] DIR [--] [CMD ...]</pre>
<h2>Description</h2>
<p>This can be used to run extra commands in the febootstrap root filesystem. It is just a simple wrapper around the standard <tt>&quot;fakeroot&quot;</tt> and <tt>&quot;fakechroot&quot;</tt> commands. </p>
<p> If given, the <tt>&quot;CMD ...&quot;</tt> is run inside the root filesystem. The command acts as if it was run as root and chrooted into the root filesystem. </p>
<p> If the command is omitted, then we start a shell. </p>
<p> If <tt>&quot;CMD ...&quot;</tt> could contain anything starting with a <tt>&quot;-&quot;</tt> character then use <tt>&quot;--&quot;</tt> to separate <tt>&quot;febootstrap-run&quot;</tt> parameters from the command: </p>
<pre> febootstrap-run ./f10 -- ls -l</pre>
<h2>Options</h2>
<dl>
<dt><code>&#8211;ro</code></p>
<dd>Usually any changes to permissions made by the command are recorded in the <tt>&quot;fakeroot.log&quot;</tt> file. However if <tt>&quot;--ro&quot;</tt> flag is given, then changes to permissions are not recorded. (Note: changes to file contents still happen).</dl>
<h2>Examples</h2>
<p>Remove a directory subtree safely: </p>
<pre> febootstrap-run initramfs -- rm -r /etc</pre>
<p>(This requires that you have a compatible &#8216;rm&#8217; command in the root). </p>
<p> Another way to do complex operations from a script is to export a function: </p>
<pre> #!/bin/bash
 do_stuff ()
 {
 # complex operations inside the root
 }
 export -f do_stuff
 febootstrap-run root -- bash -c do_stuff</pre>
<h2>Environment Variables</h2>
<p>Some <i><a href="/docs/linux/man/1-fakechroot/">fakechroot</a></i>(1) environment variables are applicable. In particular you may want to set: </p>
<pre> export FAKECHROOT_EXCLUDE_PATH=/proc</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8), <i><a href="/docs/linux/man/8-febootstrap-install/">febootstrap-install</a></i>(8), <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1), <i><a href="/docs/linux/man/1-fakechroot/">fakechroot</a></i>(1).</p>
<h2>Authors</h2>
<p>Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>Copyright</h2>
<p>(C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" href="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.</p>
