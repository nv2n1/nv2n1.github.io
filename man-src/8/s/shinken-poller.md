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
<dd>Replace previous running poller.</dd>
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
</dl>
<h2>Authors</h2>
<p>Arthur Gautier. David Hannequin Michael Leinartas.</p>
