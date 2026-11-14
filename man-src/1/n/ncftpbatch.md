---
title: "ncftpbatch(1)"
name: "ncftpbatch"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncftpbatch/"
description: "ncftpbatch – Individual batch FTP job processor"
---

<h2>NAME</h2>
<p> ncftpbatch &#8211; Individual batch FTP job processor</p>
<h2>SYNOPSIS</h2>
<p> <code>ncftpbatch</code> -d </p>
<p> <code>ncftpbatch</code> -l </p>
<p> <code>ncftpbatch</code> -D</p>
<h2>OPTIONS</h2>
<h3>Command line flags:</h3>
<dl>
<dt><code>-d</code></p>
<dd> Begin background processing of FTP jobs in the current user&#8217;s $HOME/.ncftp/spool directory. This returns immediately, because a daemon process is spawned and ran in the background.</p>
<dt><code>-l</code></p>
<dd> Lists the contents of the user&#8217;s job queue.</p>
<dt><code>-D</code></p>
<dd> This is like <code>-d</code>, except that the process does not become a daemon.</dl>
<h2>DESCRIPTION</h2>
<p> This program is responsible for processing background FTP requests. It is normally only run by <i>ncftp</i> and not manually by a human being, however you can run it to manually process the FTP job queue. </p>
<p> The jobs are spool files written to a user&#8217;s $HOME/.ncftp/spool directory and have a special format and file-naming convention (which contains when the job is to be run). <i>ncftp</i> runs this program when it needs to, but if the <i>ncftpbatch</i> daemon dies unexpectedly the jobs that are left in the queue will not be processed until another instance of <i>ncftpbatch</i> is run. </p>
<p> <i>ncftpget</i> and <i>ncftpput</i> can also be used to submit jobs for batch processing, using those utilities&#8217; <code>-b</code> command-line flag. If desired, you can also manually create the spool files although this procedure is not documented here (see the manual page for <i>ncftpspooler</i> for more information on how to do that).</p>
<h2>DIAGNOSTICS</h2>
<p> <i>ncftpbatch</i> writes to its own log file, the $HOME/.ncftp/spool/log file. This file should be examined to determine if any <i>ncftpbatch</i> processes are actively working on jobs.</p>
<h2>AUTHOR</h2>
<p> Mike Gleason, NcFTP Software (<a rel="nofollow" href="http://www.ncftp.com">http://www.ncftp.com</a>).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ncftp/">ncftp</a></i>(1), <i><a href="/docs/linux/man/1-ncftpput/">ncftpput</a></i>(1), <i><a href="/docs/linux/man/1-ncftpget/">ncftpget</a></i>(1). </p>
<h2>Index</h2>
