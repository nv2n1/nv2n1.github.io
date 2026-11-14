---
title: "mcookie(1)"
name: "mcookie"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcookie/"
description: "mcookie – generate magic cookies for xauth"
---

<h2 class="name">NAME</h2>
<p> mcookie &#8211; generate magic cookies for xauth </p>
<h2>SYNOPSIS</h2>
<p> <code>mcookie</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>mcookie</code> generates a 128-bit random hexadecimal number for use with the X authority system. Typical usage:</p>
<dl>
<dt>
<dd>
<p> <code>xauth add :0 . </code>mcookie
</dl>
<p> The &quot;random&quot; number generated is actually the MD5 message digest of random information coming from one of the sources <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) system call, <i>/dev/urandom</i>, <i>/dev/random</i>, or the <i>libc pseudo-random functions</i>, in this preference order. See also the option <code>&#8211;file</code>.</p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;file</code> <i>file</i></p>
<dl>
<dt>
<dd> Use this <i>file</i> as an additional source of randomness (for example <i>/dev/urandom</i>). When <i>file</i> is &#8216;-&#8216;, characters are read from standard input.</dl>
<p> <code>-m</code>, <code>&#8211;max-size</code> <i>number</i></p>
<dl>
<dt>
<dd> Read from <i>file</i> only this <i>number</i> of bytes. This option is meant to be used when reading additional randomness from a file or device. </p>
<p> The <i>number</i> argument may be followed by the multiplicative suffixes KiB=1024, MiB=1024*1024, and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB=1000, MB=1000*1000, and so on for GB, TB, PB, EB, ZB and YB.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Inform where randomness originated, with amount of entropy read from each source.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>FILES</h2>
<p> <i>/dev/urandom</i> </p>
<p> <i>/dev/random</i></p>
<h2>BUGS</h2>
<p> It is assumed that none of the randomness sources will block.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-md5sum/">md5sum</a></code>(1), <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1), <code><a href="/docs/linux/man/3-rand/">rand</a></code>(3)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>mcookie</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
