---

title: "retrace-server-cleanup(1)"
name: "retrace-server-cleanup"
section: "1"
letter: "r"
url: "/docs/linux/man/1-retrace-server-cleanup/"
description: "retrace-server-cleanup – Collects garbage from Retrace server."
---

<p> retrace-server-cleanup &#8211; Collects garbage from Retrace server. </p>
<h2>SYNOPSIS</h2>
<p> <i>retrace-server-cleanup</i></p>
<h2>DESCRIPTION</h2>
<p> The tool collects different kinds of garbage created by Retrace server: </p>
<dl>
<dt>
</dt><dd> &bull; Deletes old tasks. The limit to proclaim task old can be changed in the configuration file (DeleteTaskAfter).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Kills tasks running for a long time (&gt; 1 hour).</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Cleans up fakeroots and task directories from jobs finished in an unexpected way.</dd></dl>
<p> Should be set in root&#8217;s crontab to run every hour.</p>
<h2>AUTHORS</h2>
<dl>
<dt>
</dt><dd> &bull; Michal Toman &lt;m[blue]<code>_mtoman [at] redhat.com_</code>m[][1]&gt;</dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> _mtoman [at] redhat.com_</dd>
<dl>
<dt>
</dt><dd> mailto:_mtoman [at] redhat.com_</dd></dl>
</dl>
