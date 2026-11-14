---
title: "shinken-arbiter(8)"
name: "shinken-arbiter"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shinken-arbiter/"
description: "shinken-arbiter – Shinken arbiter daemon"
---

<p>shinken-arbiter &#8211; Shinken arbiter daemon</p>
<h2>Synopsis</h2>
<p>shinken-arbiter [-dr] [-c CONFIGFILE] [&#8212;debugfile DEBUGFILE] shinken-arbiter -v [-c CONFIGFILE]</p>
<h2>Description</h2>
<p>Shinken arbiter daemon </p>
<p> The shinken-arbiter daemon reads the configuration, divides it into parts (N schedulers = N parts), and distributes them to the appropriate Shinken daemons. Additionally, it manages the high availability features: if a particular daemon dies, it re-routes the configuration managed by this failed daemon to the configured spare. Finally, it receives input from users (such as external commands from nagios.cmd) and routes them to the appropriate daemon. There can only be one active arbiter in the architecture.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Show version number and exit</p>
<dl>
<dd></dl>
<dt><code>-c </code>CONFIGFILE, &#8211;config CONFIGFILE</p>
<dd>Config file</p>
<dl>
<dd></dl>
<dt><code>-d, &#8211;daemon</code></p>
<dd>Run in daemon mode.</p>
<dl>
<dd></dl>
<dt><code>-r, &#8211;replace</code></p>
<dd>Replace previous running arbiter.</p>
<dl>
<dd></dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Print detailed help screen.</p>
<dl>
<dd></dl>
<dt><code>&#8211;debugfile </code>DEBUGFILE</p>
<dd>Enable debug logging to DEBUGFILE</p>
<dl>
<dd></dl>
<dt><code>-v, &#8211;verify-config</code></p>
<dd>Verify config file and exit</p>
<dl>
<dd></dl>
</dl>
<h2>Authors</h2>
<p>David Hannequin. Arthur Gautier. Michael Leinartas.</p>
