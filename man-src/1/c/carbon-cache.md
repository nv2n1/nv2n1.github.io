---
title: "carbon-cache(1)"
name: "carbon-cache"
section: "1"
letter: "c"
url: "/docs/linux/man/1-carbon-cache/"
description: "carbon-cache – accepts metrics over various protocols and writes them to disk"
---

<h2>NAME</h2>
<p> carbon-cache &#8211; accepts metrics over various protocols and writes them to disk</p>
<h2>SYNOPSYS</h2>
<pre>
carbon-cache [options] start
</pre>
<h2>DESCRIPTION</h2>
<p> carbon-cache accepts metrics over various protocols and writes them to disk as efficiently as possible. This requires caching metric values in RAM as they are received, and flushing them to disk on an interval using the underlying whisper library. </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the embedded help.</p>
<dt><code>&#8211;debug</code></p>
<dd> Run in the foreground, log to stdout</p>
<dt><code>&#8211;profile=PROFILE</code></p>
<dd> Record performance profile data to the given file</p>
<dt><code>&#8211;pidfile=PIDFILE</code></p>
<dd> Write pid to the given file</p>
<dt><code>&#8211;config=CONFIG</code></p>
<dd> Use the given config file</p>
<dt><code>&#8211;logdir=LOGDIR</code></p>
<dd> Write logs in the given directory</p>
<dt><code>&#8211;instance=INSTANCE</code></p>
<dd> Manage a specific carbon instance</dl>
<h2>AUTHOR</h2>
<p> <code>carbon-cache</code>, created by Chris Davis. </p>
<p> This manual page was written by Jonas Genannt &lt;jonas.genannt [at] capi2name.de, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
