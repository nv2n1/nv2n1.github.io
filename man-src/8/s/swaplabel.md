---
title: "swaplabel(8)"
name: "swaplabel"
section: "8"
letter: "s"
url: "/docs/linux/man/8-swaplabel/"
description: "swaplabel – print or change the label or UUID of a swap area"
---

<p>swaplabel &#8211; print or change the label or UUID of a swap area</p>
<h2>Synopsis</h2>
<p><code>swaplabel</code> [<code>-L</code> <i>label</i>] [<code>-U</code> <i>UUID</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>swaplabel</code> will display or change the label or UUID of a swap partition located on <i>device</i> (or regular file). </p>
<p> If the optional arguments <code>-L</code> and <code>-U</code> are not given, <code>swaplabel</code> will simply display the current swap-area label and UUID of <i>device</i>. </p>
<p> If an optional argument is present, then <code>swaplabel</code> will change the appropriate value on <i>device</i>. These values can also be set during swap creation using <code><a href="/docs/linux/man/8-mkswap/">mkswap</a></code>(8). The <code>swaplabel</code> utility allows changing the label or UUID on an actively used swap device.</p>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-L</code>, <code>&#8211;label</code> <i>label</i></p>
<dl>
<dd>Specify a new <i>label</i> for the device. Swap partition labels can be at most 16 characters long. If <i>label</i> is longer than 16 characters, <code>swaplabel</code> will truncate it and print a warning message.</dl>
<p> <code>-U</code>, <code>&#8211;uuid</code> <i>UUID</i></p>
<dl>
<dd>Specify a new <i>UUID</i> for the device. The <i>UUID</i> must be in the standard 8-4-4-4-12 character format, such as is output by <code><a href="/docs/linux/man/1-uuidgen/">uuidgen</a></code>(1).</dl>
<h2>Environment</h2>
<p>LIBBLKID_DEBUG=all</p>
<dl>
<dd>enables libblkid debug output.</dl>
<h2>Authors</h2>
<p><code>swaplabel</code> was written by and</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-uuidgen/">uuidgen</a></code>(1), <code><a href="/docs/linux/man/8-mkswap/">mkswap</a></code>(8), <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>swaplabel</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
