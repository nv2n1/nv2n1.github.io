---
title: "tmpwatch(8)"
name: "tmpwatch"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tmpwatch/"
description: "tmpwatch – removes files which haven’t been accessed for a period of time"
---

<p>tmpwatch &#8211; removes files which haven&#8217;t been accessed for a period of time</p>
<h2>Synopsis</h2>
<p><code>tmpwatch</code> [-u|-m|-c] [-MUXadfqstvx] [&#8211;verbose] [&#8211;force] [&#8211;all]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;nodirs]&nbsp;<wbr>[&#8211;nosymlinks]&nbsp;<wbr>[&#8211;test]&nbsp;<wbr>[&#8211;fuser]&nbsp;<wbr>[&#8211;quiet]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;atime|&#8211;mtime|&#8211;ctime]&nbsp;<wbr>[&#8211;dirmtime]&nbsp;<wbr>[&#8211;exclude&nbsp;<wbr><i>path</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;exclude-user&nbsp;<wbr><i>user</i>]&nbsp;<wbr>[&#8211;exclude-pattern&nbsp;<wbr><i>pattern</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>time</i>&nbsp;<wbr><i>dirs</i> </p>
<h2>Description</h2>
<p><code>tmpwatch</code> recursively removes files which haven&#8217;t been accessed for a given time. Normally, it&#8217;s used to clean up directories which are used for temporary holding space such as /tmp. When changing directories, <code>tmpwatch</code> is very sensitive to possible race conditions and will exit with an error if one is detected. It does not follow symbolic links in the directories it&#8217;s cleaning (even if a symbolic link is given as its argument), does not switch filesystems (including non-trivial bind mounts), skips <i>lost+found</i> directories owned by the root user, and only removes empty directories, regular files, symbolic links, and on some systems also unused sockets. By default, <code>tmpwatch</code> dates files by their atime (access time), not their mtime (modification time). If files aren&#8217;t being removed when <code>ls -l</code> implies they should be, use <code>ls -u</code> to examine their atime to see if that explains the problem. If the &#8211;atime, &#8211;ctime or &#8211;mtime options are used in combination, the decision about deleting a file will be based on the maximum of these times. The &#8211;dirmtime option implies ignoring atime of directories, even if the &#8211;atime option is used. The <i>time</i> parameter defines the threshold for removing files. If the file has not been accessed for <i>time</i>, the file is removed. The <i>time</i> argument is a number with an optional single-character suffix specifying the units: <code>m</code> for minutes, <code>h</code> for hours, <code>d</code> for days. If no suffix is specified, <i>time</i> is in hours. Following this, one or more directories may be given for <code>tmpwatch</code> to clean up. </p>
<h2>Options</h2>
<dl>
<dt><code>-u, &#8211;atime</code></p>
<dd>Make the decision about deleting a file based on the file&#8217;s atime (access time). This is the default. </p>
<p> Note that the periodic <code>updatedb</code> file system scans keep the atime of directories recent. </p>
<dt><code>-m, &#8211;mtime</code></p>
<dd>Make the decision about deleting a file based on the file&#8217;s mtime (modification time) instead of the atime. </p>
<dt><code>-c, &#8211;ctime</code></p>
<dd>Make the decision about deleting a file based on the file&#8217;s ctime (inode change time) instead of the atime; for directories, make the decision based on the mtime. </p>
<dt><code>-M, &#8211;dirmtime</code></p>
<dd>Make the decision about deleting a directory based on the directory&#8217;s mtime (modification time) instead of the atime; completely ignore atime for directories. </p>
<dt><code>-a, &#8211;all</code></p>
<dd>Remove all file types, not just regular files, symbolic links and directories. On systems where <code>tmpwatch</code> can remove unused sockets, make the decision only based on file times, ignoring possible use of the socket. </p>
<dt><code>-d, &#8211;nodirs</code></p>
<dd>Do not attempt to remove directories, even if they are empty. </p>
<dt><code>-f, &#8211;force</code></p>
<dd>Remove root-owned files even if root doesn&#8217;t have write access (akin to <code>rm -f</code>). </p>
<dt><code>-l, &#8211;nosymlinks</code></p>
<dd>Do not attempt to remove symbolic links. </p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Report only fatal errors. </p>
<dt><code>-s, &#8211;fuser</code></p>
<dd>Attempt to use the &quot;fuser&quot; command to see if a file is already open before removing it. Not enabled by default. Does help in some circumstances, but not all. Dependent on fuser being installed in /sbin. Not supported on HP-UX or Solaris. </p>
<dt><code>-t, &#8211;test</code></p>
<dd>Don&#8217;t remove files, but go through the motions of removing them. This implies <code>-v</code>. </p>
<dt><code>-U, &#8211;exclude-user=</code><i>user</i></p>
<dd>Don&#8217;t remove files owned by <i>user</i>, which can be an user name or numeric user ID. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Print a verbose display. Two levels of verboseness are available &#8212; use this option twice to get the most verbose output. </p>
<dt><code>-x, &#8211;exclude=</code><i>path</i></p>
<dd>Skip <i>path</i>; if <i>path</i> is a directory, all files contained in it are skipped too. If <i>path</i> does not exist, it must be an absolute path that contains no symbolic links. </p>
<dt><code>-X</code>, <code>&#8211;exclude-pattern=</code><i>pattern</i></p>
<dd>Skip paths matching <i>pattern</i>; if a directory matches <i>pattern</i>, all files contained in it are skipped too. <i>pattern</i> must match an absolute path that contains no symbolic links. </p>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-cron/">cron</a></i>(1), <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1), <i><a href="/docs/linux/man/1-rm/">rm</a></i>(1), <i><a href="/docs/linux/man/1-fuser/">fuser</a></i>(1) </p>
<h2>Authors</h2>
<pre>Erik Troan &lt;ewt [at] redhat.com&gt;
Preston Brown &lt;pbrown [at] redhat.com&gt;
Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;
Miloslav Trmac &lt;mitr [at] redhat.com&gt;</pre>
