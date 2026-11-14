---
title: "cftp(1)"
name: "cftp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cftp/"
description: "cftp – Conch command-line SFTP client"
---

<h2>NAME</h2>
<p> <code>cftp</code> &#8211; Conch command-line SFTP client</p>
<h2>SYNOPSIS</h2>
<p> <code>cftp</code> [-<code>B </code><i>buffer_size</i> ] [-<code>b </code><i>command_file</i> ] [-<code>R </code><i>num_requests</i> ] [-<code>s </code><i>subsystem</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>cftp</code> is a client for logging into a remote machine and executing commands to send and receive file information. It can wrap a number of file transfer subsystems </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-B</code></p>
<dd> Specifies the default size of the buffer to use for sending and receiving. (Default value: 32768 bytes.)</p>
<dt><code>-b</code></p>
<dd> File to read commands from, &#8216;-&#8216; for stdin. (Default value: interactive/stdin.)</p>
<dt><code>-R</code></p>
<dd> Number of requests to make before waiting for a reply.</p>
<dt><code>-s</code></p>
<dd> Subsystem/server program to connect to.</dl>
<p> The following commands are recognised by <code>cftp</code> :</p>
<dl>
<dt><code>cd </code><i>path</i></p>
<dd> Change the remote directory to &#8216;path&#8217;.</p>
<dt><code>chgrp </code><i>gid path</i></p>
<dd> Change the gid of &#8216;path&#8217; to &#8216;gid&#8217;.</p>
<dt><code>chmod </code><i>mode path</i></p>
<dd> Change mode of &#8216;path&#8217; to &#8216;mode&#8217;.</p>
<dt><code>chown </code><i>uid path</i></p>
<dd> Change uid of &#8216;path&#8217; to &#8216;uid&#8217;.</p>
<dt><code>exit</code></p>
<dd> Disconnect from the server.</p>
<dt><code>get </code><i>remote-path </i>[<i>local-path</i> ]</p>
<dd> Get remote file and optionally store it at specified local path.</p>
<dt><code>help</code></p>
<dd> Get a list of available commands.</p>
<dt><code>lcd </code><i>path</i></p>
<dd> Change local directory to &#8216;path&#8217;.</p>
<dt><code>lls </code>[<i>ls-options </i>[<i>path</i> ] ]</p>
<dd> Display local directory listing.</p>
<dt><code>lmkdir </code><i>path</i></p>
<dd> Create local directory.</p>
<dt><code>ln </code><i>linkpath targetpath</i></p>
<dd> Symlink remote file.</p>
<dt><code>lpwd</code></p>
<dd> Print the local working directory.</p>
<dt><code>ls </code>[<i>-l </i>[<i>path</i> ] ]</p>
<dd> Display remote directory listing.</p>
<dt><code>mkdir </code><i>path</i></p>
<dd> Create remote directory.</p>
<dt><code>progress</code></p>
<dd> Toggle progress bar.</p>
<dt><code>put </code><i>local-path </i>[<i>remote-path</i> ]</p>
<dd> Transfer local file to remote location</p>
<dt><code>pwd</code></p>
<dd> Print the remote working directory.</p>
<dt><code>quit</code></p>
<dd> Disconnect from the server.</p>
<dt><code>rename </code><i>oldpath newpath</i></p>
<dd> Rename remote file.</p>
<dt><code>rmdir </code><i>path</i></p>
<dd> Remove remote directory.</p>
<dt><code>rm </code><i>path</i></p>
<dd> Remove remote file.</p>
<dt><code>version</code></p>
<dd> Print the SFTP version.</p>
<dt><code>?</code></p>
<dd> Synonym for &#8216;help&#8217;.</dl>
<h2>AUTHOR</h2>
<p> cftp by Paul Swartz &lt;z3p [at] twistedmatrix.com&gt;. Man page by Mary Gardiner &lt;mary [at] twistedmatrix.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2008 Twisted Matrix Laboratories<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
