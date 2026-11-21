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
<dt><code>-B</code></dt>
<dd> Specifies the default size of the buffer to use for sending and receiving. (Default value: 32768 bytes.)</dd>
<dt><code>-b</code></dt>
<dd> File to read commands from, &#8216;-&#8216; for stdin. (Default value: interactive/stdin.)</dd>
<dt><code>-R</code></dt>
<dd> Number of requests to make before waiting for a reply.</dd>
<dt><code>-s</code></dt>
<dd> Subsystem/server program to connect to.</dd></dl>
<p> The following commands are recognised by <code>cftp</code> :</p>
<dl>
<dt><code>cd </code><i>path</i></dt>
<dd> Change the remote directory to &#8216;path&#8217;.</dd>
<dt><code>chgrp </code><i>gid path</i></dt>
<dd> Change the gid of &#8216;path&#8217; to &#8216;gid&#8217;.</dd>
<dt><code>chmod </code><i>mode path</i></dt>
<dd> Change mode of &#8216;path&#8217; to &#8216;mode&#8217;.</dd>
<dt><code>chown </code><i>uid path</i></dt>
<dd> Change uid of &#8216;path&#8217; to &#8216;uid&#8217;.</dd>
<dt><code>exit</code></dt>
<dd> Disconnect from the server.</dd>
<dt><code>get </code><i>remote-path </i>[<i>local-path</i> ]</dt>
<dd> Get remote file and optionally store it at specified local path.</dd>
<dt><code>help</code></dt>
<dd> Get a list of available commands.</dd>
<dt><code>lcd </code><i>path</i></dt>
<dd> Change local directory to &#8216;path&#8217;.</dd>
<dt><code>lls </code>[<i>ls-options </i>[<i>path</i> ] ]</dt>
<dd> Display local directory listing.</dd>
<dt><code>lmkdir </code><i>path</i></dt>
<dd> Create local directory.</dd>
<dt><code>ln </code><i>linkpath targetpath</i></dt>
<dd> Symlink remote file.</dd>
<dt><code>lpwd</code></dt>
<dd> Print the local working directory.</dd>
<dt><code>ls </code>[<i>-l </i>[<i>path</i> ] ]</dt>
<dd> Display remote directory listing.</dd>
<dt><code>mkdir </code><i>path</i></dt>
<dd> Create remote directory.</dd>
<dt><code>progress</code></dt>
<dd> Toggle progress bar.</dd>
<dt><code>put </code><i>local-path </i>[<i>remote-path</i> ]</dt>
<dd> Transfer local file to remote location</dd>
<dt><code>pwd</code></dt>
<dd> Print the remote working directory.</dd>
<dt><code>quit</code></dt>
<dd> Disconnect from the server.</dd>
<dt><code>rename </code><i>oldpath newpath</i></dt>
<dd> Rename remote file.</dd>
<dt><code>rmdir </code><i>path</i></dt>
<dd> Remove remote directory.</dd>
<dt><code>rm </code><i>path</i></dt>
<dd> Remove remote file.</dd>
<dt><code>version</code></dt>
<dd> Print the SFTP version.</dd>
<dt><code>?</code></dt>
<dd> Synonym for &#8216;help&#8217;.</dd></dl>
<h2>AUTHOR</h2>
<p> cftp by Paul Swartz &lt;z3p [at] twistedmatrix.com&gt;. Man page by Mary Gardiner &lt;mary [at] twistedmatrix.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2008 Twisted Matrix Laboratories<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
