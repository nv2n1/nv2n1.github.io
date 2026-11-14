---
title: "mount-exfat-fuse(8)"
name: "mount-exfat-fuse"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-exfat-fuse/"
description: "mount.exfat-fuse – mount an exFAT file system"
---

<p>mount.exfat-fuse &#8211; mount an exFAT file system</p>
<h2>Synopsis</h2>
<p><code>mount.exfat-fuse</code> [ <code>-d</code> ] [ <code>-n</code> ] [ <code>-o</code> <i>options</i> ] [ <code>-V</code> ] [ <code>-v</code> ] <i>device dir</i> </p>
<h2>Description</h2>
<p><code>mount.exfat-fuse</code> is a free exFAT file system implementation with write support. exFAT is a simple file system created by Microsoft. It is intended to replace FAT32 removing some of its limitations. exFAT is a standard FS for SDXC memory cards. </p>
<h2>Command Line Options</h2>
<p>Command line options available:</p>
<dl>
<dt><code>-d</code></p>
<dd>Enable debug logging and do not detach from shell.</p>
<dt><code>-n</code></p>
<dd>Ignored.</p>
<dt><code>-o</code><i> options</i></p>
<dd>File system specific options. For more details see <code>FILE SYSTEM OPTIONS</code> section below.</p>
<dt><code>-V</code></p>
<dd>Print version and copyright.</p>
<dt><code>-v</code></p>
<dd>Ignored. </p>
</dl>
<h2>File System Options</h2>
<dl>
<dt><code>umask=</code><i>value</i></p>
<dd>Set the umask (the bitmask of the permissions that are <code>not</code> present, in octal). The default is 0.</p>
<dt><code>dmask=</code><i>value</i></p>
<dd>Set the umask for directories only.</p>
<dt><code>fmask=</code><i>value</i></p>
<dd>Set the umask for files only.</p>
<dt><code>uid=</code><i>n</i></p>
<dd>Set the owner for all files and directories. The default is the owner of the current process.</p>
<dt><code>gid=</code><i>n</i></p>
<dd>Set the group for all files and directories. The default is the group of the current process.</p>
<dt><code>ro</code></p>
<dd>Mount the file system in read only mode.</p>
<dt><code>noatime</code></p>
<dd>Do not update access time when file is read. </p>
</dl>
<h2>Exit Codes</h2>
<p>Zero is returned on successful mount. Any other code means an error.</p>
<h2>Bugs</h2>
<p>exFAT is a case-insensitive file system. Some things can behave unexpectedly, e.g. directory renaming that changes only case of some characters: <code> $ mv FOO Foo</code><br />
 <code> mv: cannot move &#8216;FOO&#8217; to a subdirectory of itself, &#8216;Foo/FOO&#8217;</code> This happens because <code>mv</code> finds that destination exists (for case-insensitive file systems <code>FOO</code> and <code>Foo</code> are the same thing) and adds source basename to the destination. The file system gets <code>rename(&quot;FOO&quot;,&nbsp;&quot;Foo/FOO&quot;)</code> syscall and returns an error. </p>
<h2>Author</h2>
<p>Andrew Nayenko</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) </p>
