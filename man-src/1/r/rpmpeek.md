---
title: "rpmpeek(1)"
name: "rpmpeek"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmpeek/"
description: "rpmpeek – execute command within RPM contents"
---

<h2 class="name">NAME</h2>
<p> rpmpeek &#8211; execute command within RPM contents </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmpeek</code> [<code>-n</code>] [<code>-h</code>] <i></i><font SIZE="-1"><i>RPM</i></font><i></i> <i>command</i> [<i>args</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>rpmpeek</code> unpacks <i></i><font SIZE="-1"><i>RPM</i></font><i></i> contents into a temporary directory and executes a <i>command</i> under that directory. The directory is purged upon exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code></p>
<dd> Do not preserve attributes of unpacked files.</p>
<dt><code>-h</code></p>
<dd> Display the usage and exit.</dl>
<h2>AUTHOR</h2>
<p> Written by Alexey Tourbin &lt;at [at] altlinux.org&gt;.</p>
<h2>COPYING</h2>
<p> Copyright (c) 2005 Alexey Tourbin, <font SIZE="-1">ALT</font> Linux Team. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-rpm/">rpm</a></i>(8), <i><a href="/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></i>(8), <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1). </p>
<h2>Index</h2>
