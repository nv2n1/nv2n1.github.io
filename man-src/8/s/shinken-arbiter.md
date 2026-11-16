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
<dt><code>&#8211;version</code></dt>
<dd>Show version number and exit</dd>
<dl>
<dd></dd></dl>
<dt><code>-c </code>CONFIGFILE, &#8211;config CONFIGFILE</dt>
<dd>Config file</dd>
<dl>
<dd></dd></dl>
<dt><code>-d, &#8211;daemon</code></dt>
<dd>Run in daemon mode.</dd>
<dl>
<dd></dd></dl>
<dt><code>-r, &#8211;replace</code></dt>
<dd>Replace previous running arbiter.</dd>
<dl>
<dd></dd></dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print detailed help screen.</dd>
<dl>
<dd></dd></dl>
<dt><code>&#8211;debugfile </code>DEBUGFILE</dt>
<dd>Enable debug logging to DEBUGFILE</dd>
<dl>
<dd></dd></dl>
<dt><code>-v, &#8211;verify-config</code></dt>
<dd>Verify config file and exit</dd>
<dl>
<dd></dd></dl>
</dl>
<h2>Authors</h2>
<p>David Hannequin. Arthur Gautier. Michael Leinartas.</p>
