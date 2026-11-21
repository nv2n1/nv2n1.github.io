---

title: "carbon-aggregator(1)"
name: "carbon-aggregator"
section: "1"
letter: "c"
url: "/docs/linux/man/1-carbon-aggregator/"
description: "carbon-aggregator – buffer metrics over time before reporting to carbon-cache"
---

<h2>NAME</h2>
<p> carbon-aggregator &#8211; buffer metrics over time before reporting to carbon-cache</p>
<h2>SYNOPSYS</h2>
<pre>
carbon-aggregator [options] start
</pre>
<p> carbon-aggregator can be run in front of carbon-cache to buffer metrics over time before reporting them into whisper. </p>
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
<dd> Use the given aggregation rules file.</dd>
<dt><code>&#8211;rewrite-rules=REWRITE_RULES</code></dt>
<dd> Use the given rewrite rules file.</dd></dl>
<h2>AUTHOR</h2>
<p> <code>carbon-aggregator</code>, created by Chris Davis. </p>
<p> This manual page was written by Jonas Genannt &lt;jonas.genannt [at] capi2name.de, for the Debian project (but may be used by others). </p>
