---
title: "retrace-server-worker(1)"
name: "retrace-server-worker"
section: "1"
letter: "r"
url: "/docs/linux/man/1-retrace-server-worker/"
description: "retrace-server-worker – Executes the retrace job."
---

<h2 class="name">NAME</h2>
<p> retrace-server-worker &#8211; Executes the retrace job. </p>
<h2>SYNOPSIS</h2>
<p> <i>retrace-server-worker</i> task_id.</p>
<h2>DESCRIPTION</h2>
<p> The tool uses mock to prepare a virtual environment for the retrace, runs GDB, saves backtrace and cleans up the virtual environment. The task_id argument is a number derived from the name of the directory where crash data is saved (by default <i>/var/spool/retrace-server/task_id</i>).</p>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> &bull; Michal Toman &lt;m[blue]<code>_mtoman [at] redhat.com_</code>m[]<font SIZE="-2">[1]</font>&gt;</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> _mtoman [at] redhat.com_</p>
<dl>
<dt>
<dd> mailto:_mtoman [at] redhat.com_</dl>
</dl>
<h2>Index</h2>
