---
title: "retrace-server-cleanup(1)"
name: "retrace-server-cleanup"
section: "1"
letter: "r"
url: "/docs/linux/man/1-retrace-server-cleanup/"
description: "retrace-server-cleanup – Collects garbage from Retrace server."
---

<h2 class="name">NAME</h2>
<p> retrace-server-cleanup &#8211; Collects garbage from Retrace server. </p>
<h2>SYNOPSIS</h2>
<p> <i>retrace-server-cleanup</i></p>
<h2>DESCRIPTION</h2>
<p> The tool collects different kinds of garbage created by Retrace server: </p>
<dl>
<dt>
<dd> &bull; Deletes old tasks. The limit to proclaim task old can be changed in the configuration file (DeleteTaskAfter).</dl>
<dl>
<dt>
<dd> &bull; Kills tasks running for a long time (&gt; 1 hour).</dl>
<dl>
<dt>
<dd> &bull; Cleans up fakeroots and task directories from jobs finished in an unexpected way.</dl>
<p> Should be set in root&#8217;s crontab to run every hour.</p>
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
