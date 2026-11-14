---
title: "pmlogmv(1)"
name: "pmlogmv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogmv/"
description: "pmlogmv – move (rename) Performance Co-Pilot archive files"
---

<h2>NAME</h2>
<p> <code>pmlogmv</code> &#8211; move (rename) Performance Co-Pilot archive files</p>
<h2>SYNOPSIS</h2>
<p> <code>pmlogmv</code> [<i>-NV</i>] <i>oldname</i> <i>newname</i></p>
<h2>DESCRIPTION</h2>
<p> A Performance Co-Pilot (PCP) archive consists of multiple files as created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). <code>pmlogmv</code> allows all the files of a single PCP archive to be moved or renamed as a group in a single operation. </p>
<p> The <i>oldname</i> argument identifies the target archive, and may be either the basename that is common to all files in that archive or one of the archive&#8217;s files. The new archive&#8217;s basename is <i>newname</i>. </p>
<p> The <code>-N</code> option performs a dry-run, checking and reporting what changes would be made without making any changes. </p>
<p> Additional reporting verbosity may be requested with the <code>-V</code> option. </p>
<p> Because PCP archives are important records of system activity, special care is taken to ensure the integrity of an archive&#8217;s files. For recoverable problems encountered during the execution of <code>pmlogmv</code>, all the files associated with <i>oldname</i> will be preserved, and no new files with the <i>newname</i> prefix will be created. &#8220;Recoverable problems&#8221; include signals that can be caught (such as SIGHUP, SIGINT, SIGQUIT and SIGTERM), permissions issues, new files already existing, file system full events, etc. </p>
<p> The implementation of <code>pmlogmv</code> uses hard links in the file system and so follows the semantic restrictions of <i><a href="/docs/linux/man/2-ln/">ln</a></i>(2) which for most systems means the directories containing both the <i>oldname</i> and the <i>newname</i> PCP archive files need to be writeable and within the <code>same</code> file system.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ln/">ln</a></code>(2) and <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1).</p>
<h2>DIAGNOSTICS</h2>
<p> All error and warning messages are intended to be easily understood and errors produce a non-zero exit status. </p>
<h2>Index</h2>
