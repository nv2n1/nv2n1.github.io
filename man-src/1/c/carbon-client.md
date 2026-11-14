---
title: "carbon-client(1)"
name: "carbon-client"
section: "1"
letter: "c"
url: "/docs/linux/man/1-carbon-client/"
description: "carbon-client – Graphite client to reroute carbon data"
---

<h2>NAME</h2>
<p> carbon-client &#8211; Graphite client to reroute carbon data</p>
<h2>SYNOPSYS</h2>
<pre>
carbon-client [options]
</pre>
<h2>DESCRIPTION</h2>
<p> Graphite client to reroute carbon data </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the embedded help.</p>
<dt><code>&#8211;debug</code></p>
<dd> Log debug info to stdout</p>
<dt><code>&#8211;keyfunc=KEYFUNC</code></p>
<dd> Use a custom key function (path/to/module.py:myFunc)</p>
<dt><code>&#8211;replication=REPLICATION</code></p>
<dd> Replication factor</p>
<dt><code>&#8211;routing=ROUTING</code></p>
<dd> Routing method: &quot;consistent-hashing&quot; (default) or &quot;relay&quot;</p>
<dt><code>&#8211;relayrules=RELAYRULES</code></p>
<dd> relay-rules.conf file to use for relay routing</dl>
<h2>AUTHOR</h2>
<p> <code>carbon-client</code>, created by Chris Davis. </p>
<p> This manual page was written by Jonas Genannt &lt;jonas.genannt [at] capi2name.de, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
