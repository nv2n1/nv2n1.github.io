---
title: "cockpit(1)"
name: "cockpit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cockpit/"
description: "cockpit – Cockpit"
---

<h2 class="name">NAME</h2>
<p> cockpit &#8211; Cockpit </p>
<h2>DESCRIPTION</h2>
<p> Cockpit is a web accessible interactive admin interface for Linux machines. Cockpit can usually be accessed on port 9090 of the machine it&#8217;s installed on. Cockpit starts on demand. Use your system credentials to log in.</p>
<h2>COMPONENTS</h2>
<p> The <code>cockpit-ws</code> web service listens on port 9090 and is started on demand by <code>systemd</code>. The Cockpit web service authenticates the user, loads Cockpit into the browser, and starts <code>cockpit-bridge</code> in a Linux user session. </p>
<p> The <code>cockpit-bridge</code> provides Cockpit in the web browser with access to the system APIs. It does this over its standard in and standard out. The bridge is started like a shell once per Linux user session.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the m[blue]<code>upstream bug tracker</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>AUTHOR</h2>
<p> Cockpit has been written by many m[blue]<code>contributors</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code>Cockpit Guide</code>m[]<font SIZE="-2">[3]</font>, <code><a href="/docs/linux/man/8-cockpit-ws/">cockpit-ws</a></code>(8), <code><a href="/docs/linux/man/1-cockpit-bridge/">cockpit-bridge</a></code>(1), <code><a href="/docs/linux/man/5-cockpit-conf/">cockpit.conf</a></code>(5), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> upstream bug tracker</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/cockpit-project/cockpit/issues/new">https://github.com/cockpit-project/cockpit/issues/new</a></dl>
<dt> 2.</p>
<dd> contributors</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/cockpit-project/cockpit/">https://github.com/cockpit-project/cockpit/</a></dl>
<dt> 3.</p>
<dd> Cockpit Guide</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://cockpit-project.org/guide/latest/">http://cockpit-project.org/guide/latest/</a></dl>
</dl>
<h2>Index</h2>
