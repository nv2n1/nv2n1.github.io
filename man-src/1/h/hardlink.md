---
title: "hardlink(1)"
name: "hardlink"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hardlink/"
description: "hardlink – link multiple copies of a file"
---

<h2 class="name">NAME</h2>
<p> hardlink &#8211; link multiple copies of a file </p>
<h2>SYNOPSIS</h2>
<p> <code>hardlink</code> [options] [<i>directory</i>|<i>file</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>hardlink</code> is a tool which replaces copies of a file with hardlinks, therefore saving space.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> print quick usage details to the screen.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> More verbose output. If specified once, every hardlinked file is displayed, if specified twice, it also shows every comparison.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Quiet mode, don&#8217;t print anything.</dl>
<p> <code>-n</code>, <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Do not act, just print what would happen.</dl>
<p> <code>-f</code>, <code>&#8211;respect-name</code></p>
<dl>
<dt>
<dd> Only try to link files with the same (base)name. It&#8217;s strongly recommended to use long options rather than <code>-f</code> which is interpreted in a different way by other <code>hardlink</code> implementations.</dl>
<p> <code>-p</code>, <code>&#8211;ignore-mode</code></p>
<dl>
<dt>
<dd> Link and compare files even if their mode is different. Results may be slightly unpredictable.</dl>
<p> <code>-o</code>, <code>&#8211;ignore-owner</code></p>
<dl>
<dt>
<dd> Link and compare files even if their owner information (user and group) differs. Results may be unpredictable.</dl>
<p> <code>-t</code>, <code>&#8211;ignore-time</code></p>
<dl>
<dt>
<dd> Link and compare files even if their time of modification is different. This is usually a good choice.</dl>
<p> <code>-X</code>, <code>&#8211;respect-xattrs</code></p>
<dl>
<dt>
<dd> Only try to link files with the same extended attributes.</dl>
<p> <code>-m</code>, <code>&#8211;maximize</code></p>
<dl>
<dt>
<dd> Among equal files, keep the file with the highest link count.</dl>
<p> <code>-M</code>, <code>&#8211;minimize</code></p>
<dl>
<dt>
<dd> Among equal files, keep the file with the lowest link count.</dl>
<p> <code>-O</code>, <code>&#8211;keep-oldest</code></p>
<dl>
<dt>
<dd> Among equal files, keep the oldest file (least recent modification time). By default, the newest file is kept. If <code>&#8211;maximize</code> or <code>&#8211;minimize</code> is specified, the link count has a higher precedence than the time of modification.</dl>
<p> <code>-x</code>, <code>&#8211;exclude</code> <i>regex</i></p>
<dl>
<dt>
<dd> A regular expression which excludes files from being compared and linked.</dl>
<p> <code>-i</code>, <code>&#8211;include</code> <i>regex</i></p>
<dl>
<dt>
<dd> A regular expression to include files. If the option <code>&#8211;exclude</code> has been given, this option re-includes files which would otherwise be excluded. If the option is used without <code>&#8211;exclude</code>, only files matched by the pattern are included.</dl>
<p> <code>-s</code>, <code>&#8211;minimum-size</code> <i>size</i></p>
<dl>
<dt>
<dd> The minimum size to consider. By default this is 1, so empty files will not be linked. The <i>size</i> argument may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;).</dl>
<p> <code>-S</code>, <code>&#8211;buffer-size</code> <i>size</i></p>
<dl>
<dt>
<dd> The size of read buffer used when comparing file contents (default: 8KiB). This costs some additional memory but potentially reduces the amount of seek operations and therefore improve performance, especially with mechanic disk drives. Optional factor suffixes are supported, like with the <code>-s</code> option. This is mostly efficient with other filters (i.e. with <code>-f</code> or <code>-X</code>) and can be less efficient with <code>-top</code> options.</dl>
<h2>ARGUMENTS</h2>
<p> <code>hardlink</code> takes one or more directories which will be searched for files to be linked.</p>
<h2>BUGS</h2>
<p> The original <code>hardlink</code> implementation uses the option <code>-f</code> to force hardlinks creation between filesystem. This very rarely usable feature is no more supported by the current hardlink. </p>
<p> <code>hardlink</code> assumes that the trees it operates on do not change during operation. If a tree does change, the result is undefined and potentially dangerous. For example, if a regular file is replaced by a device, hardlink may start reading from the device. If a component of a path is replaced by a symbolic link or file permissions change, security may be compromised. Do not run hardlink on a changing tree or on a tree controlled by another user.</p>
<h2>AUTHOR</h2>
<p> There are multiple <code>hardlink</code> implementations. The very first implementation is from Jakub Jelinek for Fedora distribution, this implementation has been used in util-linux between versions v2.34 to v2.36. The current implementations is based on Debian version from Julian Andres Klode.</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>hardlink</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
