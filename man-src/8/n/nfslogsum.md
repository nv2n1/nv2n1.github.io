---
title: "nfslogsum(8)"
name: "nfslogsum"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfslogsum/"
description: "nfslogsum – summarize nfswatch log file"
---

<p>nfslogsum &#8211; summarize <code>nfswatch</code> log file</p>
<h2>Synopsis</h2>
<p><code>nfslogsum</code> [ <i>-n</i> ] [ <code>-v</code> ] [ <i>logfile</i> ]</p>
<h2>Description</h2>
<p><i>nfslogsum</i> summarizes log files produced by the <i>nfswatch</i> program. By default the log file <i>nfswatch.log</i> is summarized; an alternate log file can be specified on the command line. </p>
<p> Each <i>nfswatch</i> log file may contain one or more log sessions, each indicated by a header which is printed when logging is turned on. For each log session, <i>nfslogsum</i> tallies up the interval packet totals and prints out a one-page summary of the log session. Total packets and percentages are tabulated for each category and displayed. </p>
<p> The <code>-n</code> option tells <i>nfslogsum</i> to read only the first <i>n</i> entries in the log file. This is useful for summarizing log files in cumulative &#8220;chunks&#8221;. </p>
<p> If the <code>-v</code> option is given, <i>nfslogsum</i> will produce a &#8220;verbose&#8221; summary of the log file. In addition to the summary information printed as described above, a summary of how many calls to each <font SIZE="-1">NFS</font> procedure were made on each file system and individual file will be printed. This summary information is divided into three sections of six columns each. The columns are headed by the names of the <font SIZE="-1">NFS</font> procedures; these are described briefly below:</p>
<dl>
<dt><font SIZE="-1"><code>NULLPROC</code></font></p>
<dd>Do nothing. This procedure is provided to allow server response testing and timing.</p>
<dt><font SIZE="-1"><code>GETATTR</code></font></p>
<dd>Get file attributes (type, mode, number of links, owner&#8217;s uid, owner&#8217;s gid, size, access, modification and change times, etc.). This procedure is used by the <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2) system call, as well as several others.</p>
<dt><font SIZE="-1"><code>SETATTR</code></font></p>
<dd>Set file attributes (mode, owner&#8217;s uid, owner&#8217;s gid, size in bytes, access and modification times). This procedure is used by system calls such as <i><a href="/docs/linux/man/2-chmod/">chmod</a></i>(2), <i><a href="/docs/linux/man/2-chown/">chown</a></i>(2), <i><a href="/docs/linux/man/2-truncate/">truncate</a></i>(2), and so on.</p>
<dt><font SIZE="-1"><code>GETROOT</code></font></p>
<dd>Get file system root. This procedure is obsolete, and has been replaced by a <font SIZE="-1">MOUNT</font> Protocol procedure.</p>
<dt><font SIZE="-1"><code>LOOKUP</code></font></p>
<dd>Look up file name. This procedure is used to obtain an initial file handle for use in current and future requests on that file, and is used by many different system calls.</p>
<dt><font SIZE="-1"><code>READLINK</code></font></p>
<dd>Read from symbolic link. This procedure is used by the <code>readlink</code> system call, and by the kernel.</p>
<dt><font SIZE="-1"><code>READ</code></font></p>
<dd>Read data from file. This procedure is used by the <i><a href="/docs/linux/man/2-read/">read</a></i>(2) system call.</p>
<dt><font SIZE="-1"><code>WCACHE</code></font></p>
<dd>Write to cache. Unused in the current <font SIZE="-1">NFS</font> protocol revision.</p>
<dt><font SIZE="-1"><code>WRITE</code></font></p>
<dd>Write data to file. This procedure is used by the <i><a href="/docs/linux/man/2-write/">write</a></i>(2) system call.</p>
<dt><font SIZE="-1"><code>CREATE</code></font></p>
<dd>Create file. This procedure is used by the <i><a href="/docs/linux/man/2-creat/">creat</a></i>(2) and <i><a href="/docs/linux/man/2-open/">open</a></i>(2) system calls.</p>
<dt><font SIZE="-1"><code>REMOVE</code></font></p>
<dd>Remove file. This procedure is used by the <i><a href="/docs/linux/man/2-unlink/">unlink</a></i>(2) system call.</p>
<dt><font SIZE="-1"><code>RENAME</code></font></p>
<dd>Rename file. This procedure is used by the <code>rename</code> system call.</p>
<dt><font SIZE="-1"><code>LINK</code></font></p>
<dd>Create link to file. This procedure is used by the <i><a href="/docs/linux/man/2-link/">link</a></i>(2) system call.</p>
<dt><font SIZE="-1"><code>SYMLINK</code></font></p>
<dd>Create symbolic link to file. This procedure is used by the <i><a href="/docs/linux/man/2-symlink/">symlink</a></i>(2) system call.</p>
<dt><font SIZE="-1"><code>MKDIR</code></font></p>
<dd>Create directory. This procedure is used by the <i><a href="/docs/linux/man/2-mkdir/">mkdir</a></i>(2) system call.</p>
<dt><font SIZE="-1"><code>RMDIR</code></font></p>
<dd>Remove directory. This procedure is used by the <i><a href="/docs/linux/man/2-rmdir/">rmdir</a></i>(2) system call.</p>
<dt><font SIZE="-1"><code>READDIR</code></font></p>
<dd>Read entries from directory. Generally only one <font SIZE="-1">READDIR</font> call is needed per directory, since a variable number of entries can be returned.</p>
<dt><font SIZE="-1"><code>STATFS</code></font></p>
<dd>Get file system attributes (transfer size, block size, blocks in use, blocks free). This procedure is used by the <i><a href="/docs/linux/man/2-statfs/">statfs</a></i>(2) system call.</dl>
<h2>See Also</h2>
<p><i><a href="//www.systutorials.com/docs/linux/man/8L-nfswatch/">nfswatch</a></i>(8L)</p>
<h2>Bugs</h2>
<p><i>nfslogsum</i> is exteremely sensitive to the format of the log file produced by <i>nfswatch</i>. The log file should not be edited or changed before feeding it to <i>nfslogsum</i>.</p>
<h2>Author</h2>
<p>David A. Curry<br />
 Purdue University<br />
 Engineering Computer Network<br />
 1285 Electrical Engineering Building<br />
 West Lafayette, <font SIZE="-1">IN</font> 47907-1285<br />
 davy [at] ecn.purdue.edu</p>
