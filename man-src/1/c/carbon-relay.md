---

title: "carbon-relay(1)"
name: "carbon-relay"
section: "1"
letter: "c"
url: "/docs/linux/man/1-carbon-relay/"
description: "carbon-relay – replication and sharding data"
---

<p> carbon-relay &#8211; replication and sharding data</p>
<h2>SYNOPSYS</h2>
<pre>
carbon-relay [options] start
</pre>
<h2>DESCRIPTION</h2>
<p> carbon-relay serves two distinct purposes: replication and sharding. </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show the embedded help.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Run in the foreground, log to stdout</dd>
<dt><code>&#8211;profile=PROFILE</code></dt>
<dd> Record performance profile data to the given file</dd>
<dt><code>&#8211;pidfile=PIDFILE</code></dt>
<dd> Write pid to the given file</dd>
<dt><code>&#8211;config=CONFIG</code></dt>
<dd> Use the given config file</dd>
<dt><code>&#8211;logdir=LOGDIR</code></dt>
<dd> Write logs in the given directory</dd>
<dt><code>&#8211;instance=INSTANCE</code></dt>
<dd> Manage a specific carbon instance</dd>
<dt><code>&#8211;rules=RULES</code></dt>
<dd> se the given relay rules file.</dd></dl>
<h2>AUTHOR</h2>
<p> <code>carbon-relay</code>, created by Chris Davis. </p>
<p> This manual page was written by Jonas Genannt &lt;jonas.genannt [at] capi2name.de, for the Debian project (but may be used by others). </p>
