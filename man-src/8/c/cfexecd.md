---
title: "cfexecd(8)"
name: "cfexecd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfexecd/"
description: "cfengine – network configuration engine"
---

<p>cfengine &#8211; network configuration engine</p>
<h2>Synopsis</h2>
<p>/usr/local/sbin/cfexecd </p>
<h2>Description</h2>
<p><code>cfengine</code> is a language based system specifically designed for testing and configuring unix-like systems attached to a TCP/IP network. Th cfexecd is a wrapper for local execution of cfagent. It may be used to capture cfagent output and send it as mail when run cron cron, e.g. 0,30 * * * * /var/cfengine/bin/cfexecd -F or it can be run in daemon mode with scheduling parameters set in cfagent.conf. All control parameters are set in cfagent.conf.</p>
<dl>
<dt>-F (&#8211;no-fork)</p>
<dd>Run the executor in non-daemom (cron wrapper) mode. </p>
<h2>Author</h2>
<p>Mark Burgess, Oslo University College</p>
<h2>Information</h2>
<p><a rel="nofollow" href="http://www.cfengine.org">http://www.cfengine.org</a></p>
