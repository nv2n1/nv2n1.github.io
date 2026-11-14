---
title: "stat(1)"
name: "stat"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stat/"
description: "stat – display file or file system status"
---

<h2 class="name">NAME</h2>
<p> stat &#8211; display file or file system status </p>
<h2>SYNOPSIS</h2>
<p> <code>stat</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Display file or file system status. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-L</code>, <code>&#8211;dereference</code></p>
<dd> follow links</p>
<dt><code>-f</code>, <code>&#8211;file-system</code></p>
<dd> display file system status instead of file status</p>
<dt><code>&#8211;cached</code>=<i>,MODE/</i></p>
<dd> specify how to use cached attributes; useful on remote file systems. See MODE below</p>
<dt><code>-c</code> <code>&#8211;format</code>=<i>,FORMAT/</i></p>
<dd> use the specified FORMAT instead of the default; output a newline after each use of FORMAT</p>
<dt><code>&#8211;printf</code>=<i>,FORMAT/</i></p>
<dd> like <code>&#8211;format</code>, but interpret backslash escapes, and do not output a mandatory trailing newline; if you want a newline, include 
 in FORMAT</p>
<dt><code>-t</code>, <code>&#8211;terse</code></p>
<dd> print the information in terse form</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> The <code>&#8211;cached</code> MODE argument can be; always, never, or default. `always` will use cached attributes if available, while `never` will try to synchronize with the latest attributes, and `default` will leave it up to the underlying file system. </p>
<p> The valid format sequences for files (without <code>&#8211;file-system</code>):</p>
<dl>
<dt>%a</p>
<dd> permission bits in octal (note &#8216;#&#8217; and &#8216;0&#8217; printf flags)</p>
<dt>%A</p>
<dd> permission bits and file type in human readable form</p>
<dt>%b</p>
<dd> number of blocks allocated (see %B)</p>
<dt>%B</p>
<dd> the size in bytes of each block reported by %b</p>
<dt>%C</p>
<dd> SELinux security context string</p>
<dt>%d</p>
<dd> device number in decimal</p>
<dt>%D</p>
<dd> device number in hex</p>
<dt>%f</p>
<dd> raw mode in hex</p>
<dt>%F</p>
<dd> file type</p>
<dt>%g</p>
<dd> group ID of owner</p>
<dt>%G</p>
<dd> group name of owner</p>
<dt>%h</p>
<dd> number of hard links</p>
<dt>%i</p>
<dd> inode number</p>
<dt>%m</p>
<dd> mount point</p>
<dt>%n</p>
<dd> file name</p>
<dt>%N</p>
<dd> quoted file name with dereference if symbolic link</p>
<dt>%o</p>
<dd> optimal I/O transfer size hint</p>
<dt>%s</p>
<dd> total size, in bytes</p>
<dt>%t</p>
<dd> major device type in hex, for character/block device special files</p>
<dt>%T</p>
<dd> minor device type in hex, for character/block device special files</p>
<dt>%u</p>
<dd> user ID of owner</p>
<dt>%U</p>
<dd> user name of owner</p>
<dt>%w</p>
<dd> time of file birth, human-readable; &#8211; if unknown</p>
<dt>%W</p>
<dd> time of file birth, seconds since Epoch; 0 if unknown</p>
<dt>%x</p>
<dd> time of last access, human-readable</p>
<dt>%X</p>
<dd> time of last access, seconds since Epoch</p>
<dt>%y</p>
<dd> time of last data modification, human-readable</p>
<dt>%Y</p>
<dd> time of last data modification, seconds since Epoch</p>
<dt>%z</p>
<dd> time of last status change, human-readable</p>
<dt>%Z</p>
<dd> time of last status change, seconds since Epoch</dl>
<p> Valid format sequences for file systems:</p>
<dl>
<dt>%a</p>
<dd> free blocks available to non-superuser</p>
<dt>%b</p>
<dd> total data blocks in file system</p>
<dt>%c</p>
<dd> total file nodes in file system</p>
<dt>%d</p>
<dd> free file nodes in file system</p>
<dt>%f</p>
<dd> free blocks in file system</p>
<dt>%i</p>
<dd> file system ID in hex</p>
<dt>%l</p>
<dd> maximum length of filenames</p>
<dt>%n</p>
<dd> file name</p>
<dt>%s</p>
<dd> block size (for faster transfers)</p>
<dt>%S</p>
<dd> fundamental block size (for block counts)</p>
<dt>%t</p>
<dd> file system type in hex</p>
<dt>%T</p>
<dd> file system type in human readable form</dl>
<h3>&#8211;terse is equivalent to the following FORMAT:</h3>
<dl>
<dt>
<dd> %n %s %b %f %u %g %D %i %h %t %T %X %Y %Z %W %o %C</dl>
<h3>&#8211;terse &#8211;file-system is equivalent to the following FORMAT:</h3>
<dl>
<dt>
<dd> %n %i %l %t %s %S %b %f %a %c %d</dl>
<p> NOTE: your shell may have its own version of stat, which usually supersedes the version described here. Please refer to your shell&#8217;s documentation for details about the options it supports.</p>
<h2>AUTHOR</h2>
<p> Written by Michael Meskes.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-stat/">stat</a>(2), <a href="/docs/linux/man/2-statfs/">statfs</a>(2), <a href="/docs/linux/man/2-statx/">statx</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/stat">https://www.gnu.org/software/coreutils/stat</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) stat invocation&#8217; </p>
<h2>Index</h2>
