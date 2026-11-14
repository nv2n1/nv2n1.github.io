---
title: "febootstrap-install(8)"
name: "febootstrap-install"
section: "8"
letter: "f"
url: "/docs/linux/man/8-febootstrap-install/"
---

febootstrap-install - Install a file in an febootstrap root filesystem

<h2>Synopsis</h2>

<pre> febootstrap-install ROOT LOCALFILE TARGETPATH MODE OWNER[.GROUP]</pre>

<h2>Description</h2>

This can be used to safely install a new file in an febootstrap root filesystem. 

 Just copying a file in isn't usually safe, for reasons which are to do with the <i><a HREF="/docs/linux/man/8-fakeroot/">fakeroot</a></i>(8) command.

<h2>Example</h2>

<pre> febootstrap-install initramfs new-fstab /etc/fstab ugo=rw root.root</pre>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8), <i><a HREF="/docs/linux/man/8-febootstrap-run/">febootstrap-run</a></i>(8), <i><a HREF="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1), <i><a HREF="/docs/linux/man/1-fakechroot/">fakechroot</a></i>(1).

<h2>Authors</h2>

Richard W.M. Jones &lt;rjones @ redhat . com&gt;

<h2>Copyright</h2>

(C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" HREF="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;. 

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.
