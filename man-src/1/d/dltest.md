---
title: "dltest(1)"
name: "dltest"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dltest/"
description: "dltest – A simple library symbol test"
---

<h2>NAME</h2>
<p> dltest &#8211; A simple library symbol test </p>
<h2>SYNOPSIS</h2>
<p> <code>dltest</code> <i>library symbol</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>dltest</code> is simple test of occurence of the <i>symbol</i> in the <i>library</i>. The <i>library</i> must be a full (with path) file name of the shared object, in which the search for <i>symbol</i> should be performed. </p>
<p> Without any parameters, dltest print short help message. </p>
<h2>EXAMPLES</h2>
<p> To determine if the symbol <code>printf</code> is found in the <i>libc-2.18.so</i>: </p>
<dl>
<dt>
<dd> $ dltest /usr/lib/libc-2.18.so printf</dl>
<h2>AUTHORS</h2>
<p> The authors of unixODBC are Peter Harvey and Nick Gorham For the full list of contributors see the <i>AUTHORS</i> file. </p>
<h2>COPYRIGHT</h2>
<p> unixODBC is licensed under the GNU Lesser General Public License. For details about the license, see the <i>COPYING</i> file. </p>
<h2>Index</h2>
