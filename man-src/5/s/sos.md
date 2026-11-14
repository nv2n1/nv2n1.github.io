---
title: "sos(5)"
name: "sos"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sos/"
description: "sos.conf – sosreport configuration"
---

<p>sos.conf &#8211; sosreport configuration</p>
<h2>Description</h2>
<p>sosreport uses a configuration file at /etc/sos.conf.</p>
<h2>Parameters</h2>
<p>There are two sections in the sosreport configuration file: plugins, and tunables. Options are set using &#8216;ini&#8217;-style <code>name = value</code> pairs. </p>
<p> Some options accept a comma separated list of values. </p>
<dl>
<dt><code>[plugins]</code></p>
<dd>disable Comma separated list of plugins to disable.</p>
<dt><code>[tunables]</code></p>
<dd>plugin.option Alter available options for defined plugin.</dl>
<h2>Examples</h2>
<p>To disable the &#8216;general&#8217; and &#8216;filesys&#8217; plugins: </p>
<p> [plugins]<br />
 disable = general, filesys </p>
<p> To disable rpm package verification in the RPM plugin: </p>
<p> [tunables]<br />
 rpm.rpmva = off</p>
<h2>Files</h2>
<p>/etc/sos.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-sosreport/">sosreport</a>(1) </p>
