---
title: "namei(1)"
name: "namei"
section: "1"
letter: "n"
url: "/docs/linux/man/1-namei/"
description: "namei – follow a pathname until a terminal point is found"
---

<h2 class="name">NAME</h2>
<p> namei &#8211; follow a pathname until a terminal point is found </p>
<h2>SYNOPSIS</h2>
<p> <code>namei</code> [options] <i>pathname</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>namei</code> interprets its arguments as pathnames to any type of Unix file (symlinks, files, directories, and so forth). <code>namei</code> then follows each pathname until an endpoint is found (a file, a directory, a device node, etc). If it finds a symbolic link, it shows the link, and starts following it, indenting the output to show the context. </p>
<p> This program is useful for finding &quot;too many levels of symbolic links&quot; problems. </p>
<p> For each line of output, <code>namei</code> uses the following characters to identify the file type found: </p>
<dl>
<dt>
<dd>
<pre>
   f: = the pathname currently being resolved
    d = directory
    l = symbolic link (both the link and its contents are output)
    s = socket
    b = block device
    c = character device
    p = FIFO (named pipe)
    - = regular file
    ? = an error of some kind
</pre>
</dl>
<p> <code>namei</code> prints an informative message when the maximum number of symbolic links this system can have has been exceeded.</p>
<h2>OPTIONS</h2>
<p> <code>-l</code>, <code>&#8211;long</code></p>
<dl>
<dt>
<dd> Use the long listing format (same as <code>-m -o -v</code>).</dl>
<p> <code>-m</code>, <code>&#8211;modes</code></p>
<dl>
<dt>
<dd> Show the mode bits of each file type in the style of <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), for example &#8216;rwxr-xr-x&#8217;.</dl>
<p> <code>-n</code>, <code>&#8211;nosymlinks</code></p>
<dl>
<dt>
<dd> Don&#8217;t follow symlinks.</dl>
<p> <code>-o</code>, <code>&#8211;owners</code></p>
<dl>
<dt>
<dd> Show owner and group name of each file.</dl>
<p> <code>-v</code>, <code>&#8211;vertical</code></p>
<dl>
<dt>
<dd> Vertically align the modes and owners.</dl>
<p> <code>-x</code>, <code>&#8211;mountpoints</code></p>
<dl>
<dt>
<dd> Show mountpoint directories with a &#8216;D&#8217; rather than a &#8216;d&#8217;.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>BUGS</h2>
<p> To be discovered.</p>
<h2>AUTHORS</h2>
<p> The original <code>namei</code> program was written by </p>
<p> The program was rewritten by Karel Zak</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-stat/">stat</a></code>(1), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>namei</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
