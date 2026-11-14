---
title: "shinken-poller(8)"
name: "shinken-poller"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shinken-poller/"
description: "shinken-poller – Shinken poller daemon"
---

<p>shinken-poller &#8211; Shinken poller daemon</p>
<h2>Synopsis</h2>
<p>shinken-poller [-dr] [-c CONFIGFILE] [&#8212;debugfile DEBUGFILE]</p>
<h2>Description</h2>
<p>The shinken-poller daemon is in charge of launching plugins as requested by schedulers. When the check is finished it returns the result to the schedulers.</p>
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
<dd>Replace previous running poller.</p>
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
<p>Arthur Gautier. David Hannequin Michael Leinartas.</p>
