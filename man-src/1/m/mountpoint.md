---
title: "mountpoint(1)"
name: "mountpoint"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mountpoint/"
description: "mountpoint – see if a directory or file is a mountpoint"
---

<h2 class="name">NAME</h2>
<p> mountpoint &#8211; see if a directory or file is a mountpoint </p>
<h2>SYNOPSIS</h2>
<p> <code>mountpoint</code> [<code>-d</code>|<code>-q</code>] <i>directory</i>|<i>file</i> </p>
<p> <code>mountpoint</code> <code>-x</code> <i>device</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mountpoint</code> checks whether the given <i>directory</i> or <i>file</i> is mentioned in the <i>/proc/self/mountinfo</i> file.</p>
<h2>OPTIONS</h2>
<p> <code>-d</code>, <code>&#8211;fs-devno</code></p>
<dl>
<dt>
<dd> Show the major/minor numbers of the device that is mounted on the given directory.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Be quiet &#8211; don&#8217;t print anything.</dl>
<p> <code>&#8211;nofollow</code></p>
<dl>
<dt>
<dd> Do not follow symbolic link if it the last element of the <i>directory</i> path.</dl>
<p> <code>-x</code>, <code>&#8211;devno</code></p>
<dl>
<dt>
<dd> Show the major/minor numbers of the given blockdevice on standard output.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>EXIT STATUS</h2>
<p> <code>mountpoint</code> has the following exit status values: </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> success; the directory is a mountpoint, or device is block device on <code>&#8211;devno</code></dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> failure; incorrect invocation, permissions or system error</dl>
<p> <code>32</code></p>
<dl>
<dt>
<dd> failure; the directory is not a mountpoint, or device is not a block device on <code>&#8211;devno</code></dl>
<h2>ENVIRONMENT</h2>
<p> LIBMOUNT_DEBUG=all</p>
<dl>
<dt>
<dd> enables libmount debug output.</dl>
<h2>NOTES</h2>
<p> The util-linux <code>mountpoint</code> implementation was written from scratch for libmount. The original version for sysvinit suite was written by Miquel van Smoorenburg.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>mountpoint</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
