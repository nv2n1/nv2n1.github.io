---
title: "shinken-scheduler(8)"
name: "shinken-scheduler"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shinken-scheduler/"
description: "shinken-scheduler – Shinken scheduler daemon"
---

<p>shinken-scheduler &#8211; Shinken scheduler daemon</p>
<h2>Synopsis</h2>
<p>shinken-scheduler [-dr] [-c CONFIGFILE] [&#8212;debugfile DEBUGFILE]</p>
<h2>Description</h2>
<p>Shinken scheduler daemon </p>
<p> The shinken-scheduler manages the dispatching of checks and actions sent to shinken-reactionner and shinken-poller based on configuration sent to it by shinken-arbiter.</p>
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
<dd>Replace previous running scheduler.</p>
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
</dl>
<h2>Authors</h2>
<p>David Hannequin. Arthur Gautier. Michael Leinartas.</p>
