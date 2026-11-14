---
title: "pqrm(1)"
name: "pqrm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pqrm/"
description: "nwpqjob – Perform operations on the jobs in NetWare print queue"
---

<h2>NAME</h2>
<p> nwpqjob &#8211; Perform operations on the jobs in NetWare print queue</p>
<h2>SYNOPSIS</h2>
<p> <code>nwpqjob</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] &lt; <code>-d</code> | <code>-r</code> &gt; <i>queue_name</i> <i>job_ID</i> [ <i>another_job_ID</i> &#8230; ] </p>
<p> <code>pqrm</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] <i>queue_name</i> <i>job_ID</i> [ <i>another_job_ID</i> &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <code>pqrm</code> or <code>nwpqjob -d</code> remove specified jobs from the specified NetWare print queue. </p>
<p> <code>nwpqjob -r</code> resumes specified job in the specified NetWare print queue. </p>
<p> <code>nwpqjob</code> looks up the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of <code>.nwclient</code> MUST be 600, for security reasons. </p>
<h2>OPTIONS</h2>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Delete specified print job(s). This is default operation for <code>pqrm</code>.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Resume (clear <i>OPERATOR HOLD</i> and <i>USER HOLD</i> flags) specified print job(s).</dl>
<p> <code>queue_name</code></p>
<dl>
<dt>
<dd> <code>queue_name</code> is used to specify queue. You can not use wildcards in the name.</dl>
<p> <code>job_ID</code> , <code>another_job_ID</code></p>
<dl>
<dt>
<dd> <code>job_ID</code> is used to specify which job has to be deleted or resumed.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> <code>server</code> is the name of the server you want to use.</dl>
<p> <code>-U</code> <i>user name</i></p>
<dl>
<dt>
<dd> If the user name your NetWare administrator gave to you differs from your unix user-id, you should use <code>-U</code> to tell the server about your NetWare user name.</dl>
<p> <code>-P</code> <i>password</i></p>
<dl>
<dt>
<dd> You may want to give the password required by the server on the command line. You should be careful about using passwords in scripts.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> <code>-n</code> should be given to mount shares which do not require a password to log in. </p>
<p> If neither <code>-n</code> nor <code>-P</code> are given, pqstat prompts for a password.</dl>
<p> <code>-C</code></p>
<dl>
<dt>
<dd> By default, passwords are converted to uppercase before they are sent to the server, because most servers require this. You can turn off this conversion by <code>-C.</code></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-nwclient/">nwclient</a>(5), <a href="/docs/linux/man/1-nprint/">nprint</a>(1), <a href="/docs/linux/man/1-slist/">slist</a>(1), <a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8), <a href="/docs/linux/man/1-pqlist/">pqlist</a>(1), <a href="/docs/linux/man/1-pqstat/">pqstat</a>(1)</code> </p>
<h2>CREDITS</h2>
<p> nwpqjob was written by Petr Vandrovec (vandrove [at] vc.cvut.cz). Resuming of print jobs was added by Zdenek Roub (zroub [at] ssps.zcu.cz). </p>
<h2>Index</h2>
