---
title: "openproc(3)"
name: "openproc"
section: "3"
letter: "o"
url: "/docs/linux/man/3-openproc/"
description: "openproc, closeproc – initialize process information from /proc/"
---

<p>openproc, closeproc &#8211; initialize process information from /proc/</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;proc/readproc.h&gt;</code></pre>
<p> <code>PROCTAB* openproc (int </code><i>flags</i><code>, &#8230; );</code><br />
 <code>void closeproc (PROCTAB* </code><i>PT</i><code>);</code> </p>
<h2>Synopsis</h2>
<p>The <code>openproc</code> function initializes a PROCTAB structure which can be used by iterated readproc calls to get information on current processes. Depending on <i>flags</i>, openproc may need a second argument or a second and third argument (see below). <code>closeproc</code> closes all files opened by <code>openproc</code> and deallocates the memory allocated by <code>openproc.</code> The PROCTAB structure is defined in <i>&lt;proc/readproc.h&gt;</i> </p>
<h2>Return Value</h2>
<p><code>openproc</code> returns a pointer to a PROCTAB structure, or NULL if an error occurs. This usually means that <i>/proc</i> cannot be read by the process. </p>
<h2>Flags</h2>
<p>The behaviour of <code>openproc</code> is controlled by the following set of flags, which may be ORed together. There are three different kinds of flags. The first group of flags determines which information gets read from /proc/#pid for each process. The second group of flags (of which only one can be enacted for a opendir call) restricts which processes information is read for by providing a list of criteria. The third group of flags restricts this as well, but doesn&#8217;t need arguments. These may be used together again. </p>
<dl>
<dt><code>PROC_FILLMEM</code></dt>
<dd>read information from <i>/proc/#pid/statm</i></dd>
<dt><code>PROC_FILLCOM</code></dt>
<dd>allocate <i>cmdline</i> part of <i>proc_t</i> and read information from <i>/proc/#pid/cmdline</i></dd>
<dt><code>PROC_FILLENV</code></dt>
<dd>allocate <i>environ</i> part of <i>proc_t</i> and read information from <i>/proc/#pid/environ</i></dd>
<dt><code>PROC_FILLUSR</code></dt>
<dd>resolve user ids to names via <i>/etc/passwd</i></dd>
<dt><code>PROC_FILLGRP</code></dt>
<dd>resolve group ids to names via <i>/etc/group</i></dd>
<dt><code>PROC_FILLSTATUS</code></dt>
<dd>read information from <i>/proc/#pid/status</i></dd>
<dt><code>PROC_FILLSTAT</code></dt>
<dd>read information from <i>/proc/#pid/stat</i></dd>
<dt><code>PROC_FILLARG</code></dt>
<dd>equivalent to PROC_FILLCOM</dd>
<dt><code>PROC_FILLCGROUP</code></dt>
<dd>alloc and fill in cgroup</dd>
<dt><code>PROC_FILLSUPGRP</code></dt>
<dd>resolve supplementary group id -&gt; group name</dd>
<dt><code>PROC_FILLOOM</code></dt>
<dd>fill in proc_t oom_score and oom_adj</dd>
<dt><code>PROC_FILLNS</code></dt>
<dd>fill in proc_t namespace information</dd>
<dt><code>PROC_FILLSYSTEMD</code></dt>
<dd>fill in proc_t systemd information</dd>
<dt><code>PROC_LOOSE_TASKS</code></dt>
<dd>threat threads as if they were processes</dd>
<dt><code>PROC_PID</code> (2nd argument pid_t*<i>pidlist</i>)</dt>
<dd>lookup only processes whose pid is contained in <i>pidlist</i> (the list is terminated with 0)</dd>
<dt><code>PROC_UID</code> (arguments uid_t*<i>uidlist</i><code>, int </code><i>n</i>)</dt>
<dd>lookup only processes whose user id is contained in <i>uidlist</i> (where <i>n</i> is the number of uids contained in the list)</dd>
<dt><code>PROC_EDITCGRPCVT</code></dt>
<dd>edit cgroup as single vector</dd>
<dt><code>PROC_EDITCMDLCVT</code></dt>
<dd>edit cmdline as single vector</dd>
<dt><code>PROC_EDITENVRCVT</code></dt>
<dd>edit environ as single vector </dd>
</dl>
<h2>Note</h2>
<p>Only one of the flags needing additional arguments (<code>PROC_{PID,UID}</code>) may be used at a time.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-readproc/">readproc</a></code>(3), <code><a href="/docs/linux/man/3-readproctab/">readproctab</a></code>(3), <code>/proc/</code>, <code>/usr/include/proc/readproc.h</code>,</p>
<h2>Reporting Bugs</h2>
<p>Please send bug reports to</p>
