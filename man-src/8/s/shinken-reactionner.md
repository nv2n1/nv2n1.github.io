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
<dt><code>&#8211;version</code></p>
<dd>Show version number and exit</p>
<dl>
<dd></dl>
<dt><code>-c </code>CONFIGFILE, &#8211;config CONFIGFILE</p>
<dd>Config file</p>
<dl>
<dd></dl>
<dt><code>-d, &#8211;daemon</code></p>
<dd>Run in daemon mode</p>
<dl>
<dd></dl>
<dt><code>-r, &#8211;replace</code></p>
<dd>Replace previous running reactionner</p>
<dl>
<dd></dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Print detailed help screen</p>
<dl>
<dd></dl>
<dt><code>&#8211;debugfile </code>DEBUGFILE</p>
<dd>Enable debug logging to DEBUGFILE</p>
<dl>
<dd></dl>
</dl>
<h2>Authors</h2>
<p>David Hannequin. Arthur Gautier. Michael Leinartas.</p>
