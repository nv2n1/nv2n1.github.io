---
title: "grsync-batch(1)"
name: "grsync-batch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grsync-batch/"
description: "GRSYNC-BATCH – Grsync batch session runner"
---

<h2 class="name">NAME</h2>
<p> GRSYNC-BATCH &#8211; Grsync batch session runner</p>
<h2>SYNOPSIS</h2>
<p> <code>grsync-batch [-f] [-d] [session_name|file_name]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>GRSYNC-BATCH</code> is a script which can be used to automate rsync runs using grsync sessions (see man grsync). for example it can be put into crontab for scheduled execution on terminal, and to get the results via email. </p>
<h2>OPTIONS</h2>
<p> <code>GRSYNC-BATCH</code> by default loads the session you specify on the command line from your grsync.ini default configuration file. if you specify the -f option, it will be treated as a file name to load instead. in this case, only one session can be present in the file so there is no need to specify the session. the -d option makes a dry-run, i.e. simulation (run but don&#8217;t make any changes) </p>
<h2>SEE ALSO</h2>
<p> <code>Website</code> &lt;<a rel="nofollow" href="http://www.opbyte.it/grsync/">http://www.opbyte.it/grsync/</a>&gt;, <code>grsync</code> </p>
<h2>AUTHOR</h2>
<p> GRSYNC was written by Piero Orsoni &lt;info [at] opbyte.it&gt;. </p>
<p> This manual page was written by Piero Orsoni </p>
<h2>Index</h2>
