---
title: "shinken-reactionner(8)"
name: "shinken-reactionner"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shinken-reactionner/"
description: "shinken-reactionner – Shinken reactionner daemon"
---

<p>shinken-reactionner &#8211; Shinken reactionner daemon</p>
<h2>Synopsis</h2>
<p>shinken-reactionner [-dr] [-c CONFIGFILE] [&#8212;debugfile DEBUGFILE]</p>
<h2>Description</h2>
<p>Shinken reactionner daemon </p>
<p> The shinken-reactionner is similar to shinken-poller but handles actions such as notifications and event-handlers from the schedulers rather than checks.</p>
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
<dd>Run in daemon mode</dd>
<dl>
<dd></dd></dl>
<dt><code>-r, &#8211;replace</code></dt>
<dd>Replace previous running reactionner</dd>
<dl>
<dd></dd></dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print detailed help screen</dd>
<dl>
<dd></dd></dl>
<dt><code>&#8211;debugfile </code>DEBUGFILE</dt>
<dd>Enable debug logging to DEBUGFILE</dd>
<dl>
<dd></dd></dl>
</dl>
<h2>Authors</h2>
<p>David Hannequin. Arthur Gautier. Michael Leinartas.</p>
