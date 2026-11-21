---

title: "retrace-server-worker(1)"
name: "retrace-server-worker"
section: "1"
letter: "r"
url: "/docs/linux/man/1-retrace-server-worker/"
description: "retrace-server-worker – Executes the retrace job."
---

<p> <i>retrace-server-worker</i> task_id.</p>
<p> The tool uses mock to prepare a virtual environment for the retrace, runs GDB, saves backtrace and cleans up the virtual environment. The task_id argument is a number derived from the name of the directory where crash data is saved (by default <i>/var/spool/retrace-server/task_id</i>).</p>
<h2>AUTHORS</h2>
<dl>
<dt>
</dt><dd> &bull; Michal Toman &lt;m[blue]<code>_mtoman [at] redhat.com_</code>m[]<font SIZE="-2">[1]</font>&gt;</dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> _mtoman [at] redhat.com_</dd>
<dl>
<dt>
</dt><dd> mailto:_mtoman [at] redhat.com_</dd></dl>
</dl>
