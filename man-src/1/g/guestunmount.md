---
title: "guestunmount(1)"
name: "guestunmount"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestunmount/"
description: "guestunmount – Unmount a guestmounted filesystem"
---

<h2 class="name">NAME</h2>
<p> guestunmount &#8211; Unmount a guestmounted filesystem </p>
<h2>SYNOPSIS</h2>
<pre>
 guestunmount mountpoint
 guestunmount --fd=&lt;FD&gt; mountpoint
</pre>
<h2>DESCRIPTION</h2>
<p> guestunmount is a utility to clean up mounted filesystems automatically. <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1) mounts filesystems using libguestfs. This program unmounts the filesystem when a program or script has finished with it. </p>
<p> guestunmount is a wrapper around the <font SIZE="-1">FUSE </font><i><a href="/docs/linux/man/1-fusermount/">fusermount</a></i>(1) program, which must exist on the current <tt>&quot;PATH&quot;</tt>. </p>
<p> There are two ways to use guestunmount. When called as: </p>
<pre>
 guestunmount mountpoint
</pre>
<p> it unmounts <tt>&quot;mountpoint&quot;</tt> immediately. </p>
<p> When called as: </p>
<pre>
 guestunmount --fd=FD mountpoint
</pre>
<p> it waits until the pipe <tt>&quot;FD&quot;</tt> is closed. This can be used to monitor another process and clean up its mountpoint when that process exits, as described below.</p>
<h3><font SIZE="-1">FROM PROGRAMS</font></h3>
<p> You can just call <tt>&quot;guestunmount mountpoint&quot;</tt> from the program, but a more sophisticated way to use guestunmount is to have it monitor your program so it can clean up the mount point if your program exits unexpectedly. </p>
<p> In the program, create a pipe (eg. by calling <i><a href="/docs/linux/man/2-pipe/">pipe</a></i>(2)). Let <tt>&quot;FD&quot;</tt> be the file descriptor number of the read side of the pipe (ie. <tt>&quot;pipefd[0]&quot;</tt>). </p>
<p> After mounting the filesystem with <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1) (on <tt>&quot;mountpoint&quot;</tt>), fork and run guestunmount like this: </p>
<pre>
 guestunmount --fd=FD mountpoint
</pre>
<p> Close the read side of the pipe in the parent process. </p>
<p> Now, when the write side of the pipe (ie. <tt>&quot;pipefd[1]&quot;</tt>) is closed for any reason, either explicitly or because the parent process exits, guestunmount notices and unmounts the mountpoint. </p>
<p> If your operating system supports it, you should set the <tt>&quot;FD_CLOEXEC&quot;</tt> flag on the write side of the pipe. This is so that other child processes don&#8217;t inherit the file descriptor and keep it open. </p>
<p> Guestunmount never daemonizes itself.</p>
<h3><font SIZE="-1">FROM SHELL SCRIPTS</font></h3>
<p> Since bash doesn&#8217;t provide a way to create an unnamed pipe, use a trap to call guestunmount on exit like this: </p>
<pre>
 trap &quot;guestunmount mountpoint&quot; EXIT INT QUIT TERM
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;fd=FD</code></p>
<dd> Specify the pipe file descriptor to monitor, and delay cleanup until that pipe is closed.</p>
<dt><code>&#8211;help</code></p>
<dd> Display brief help and exit.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t display error messages from fusermount. The return status is still set (see &#8220;<font SIZE="-1">EXIT STATUS&#8221;</font> below).</p>
<dt><code>&#8211;no-retry</code></p>
<dd>
<dt><code>&#8211;retry=N</code></p>
<dd> By default, guestunmount will retry the fusermount operation up to 5 times (that is, it will run it up to 6 times = 1 try + 5 retries). </p>
<p> Use <i>&#8211;no-retry</i> to make guestunmount run fusermount only once. </p>
<p> Use <i>&#8211;retry=N</i> to make guestunmount retry <tt>&quot;N&quot;</tt> times instead of 5. </p>
<p> guestunmount performs an exponential back-off between retries, waiting 1 second, 2 seconds, 4 seconds, etc before each retry.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the program version and exit.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>&quot;PATH&quot;</p>
<dd> The <i><a href="/docs/linux/man/1-fusermount/">fusermount</a></i>(1) program (supplied by <font SIZE="-1">FUSE</font>) must be available on the current <tt>&quot;PATH&quot;</tt>.</dl>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or one of the following error codes:</p>
<dl>
<dt>1</p>
<dd> Program error, eg. could not allocate memory, could not run fusermount. See the error message printed for more information.</p>
<dt>2</p>
<dd> The mount point could not be unmounted even after retrying. See the error message printed for the underlying fusermount error.</p>
<dt>3</p>
<dd> The mount point is not mounted.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1), <i><a href="/docs/linux/man/1-fusermount/">fusermount</a></i>(1), <i><a href="/docs/linux/man/2-pipe/">pipe</a></i>(2), &#8220;<font SIZE="-1">MOUNT LOCAL&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="http://fuse.sf.net/.">http://fuse.sf.net/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2013 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAG">OPTIONS</a></p>
<dd>
<dt><a href="#lbAH">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAI">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAJ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAK">AUTHORS</a></p>
<dd>
<dt><a href="#lbAL">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAM">LICENSE</a></p>
<dd>
<dt><a href="#lbAN">BUGS</a></p>
<dd></dl>
