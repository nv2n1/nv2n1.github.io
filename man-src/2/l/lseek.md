---
title: "lseek(2)"
name: "lseek"
section: "2"
letter: "l"
url: "/docs/linux/man/2-lseek/"
description: "lseek – reposition read/write file offset"
---

<h2 class="name">NAME</h2>
<p> lseek &#8211; reposition read/write file offset </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>off_t lseek(int </code><i>fd</i><code>, off_t </code><i>offset</i><code>, int </code><i>whence</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>lseek</code>() repositions the file offset of the open file description associated with the file descriptor <i>fd</i> to the argument <i>offset</i> according to the directive <i>whence</i> as follows:</p>
<dl>
<dt><code>SEEK_SET</code></p>
<dd> The file offset is set to <i>offset</i> bytes.</p>
<dt><code>SEEK_CUR</code></p>
<dd> The file offset is set to its current location plus <i>offset</i> bytes.</p>
<dt><code>SEEK_END</code></p>
<dd> The file offset is set to the size of the file plus <i>offset</i> bytes.</dl>
<p> <code>lseek</code>() allows the file offset to be set beyond the end of the file (but this does not change the size of the file). If data is later written at this point, subsequent reads of the data in the gap (a &quot;hole&quot;) return null bytes (&#8216;
