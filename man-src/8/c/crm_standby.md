---
title: "crm_standby(8)"
name: "crm_standby"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_standby/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_standby</code> <i>&lt;command&gt; </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_standby &#8211; convenience wrapper for crm_attribute </p>
<p> Check, enable or disable standby mode for a cluster node. Nodes in standby mode may not host cluster resources.</p>
<h3>Commands:</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Display this text and exit</p>
<dt><code>&#8211;version</code></p>
<dd>Display version information and exit</p>
<dt><code>-G</code>, <code>&#8211;query</code></p>
<dd>Display the current value of standby mode (on/off)</p>
<dt><code>-v</code>, <code>&#8211;update=</code>&lt;value&gt;</p>
<dd>Update the value of standby mode (on/off)</p>
<dt><code>-D</code>, <code>&#8211;delete</code></p>
<dd>Let standby mode use default value</dl>
<h2>Options</h2>
<dl>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output (may be specified multiple times)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Print nothing on stdout except the standby status</p>
<dt><code>-N</code>, <code>&#8211;node=</code>&lt;value&gt;</p>
<dd>Operate on the named node instead of the current one</p>
<dt> <code>-l</code>, <code>&#8211;lifetime=</code>&lt;value&gt; Until when the setting should take effect (reboot/forever)</p>
<dt><code>-i</code>, <code>&#8211;id=</code>&lt;value&gt;</p>
<dd>(Advanced) ID used to identify the XML attribute</dl>
<h2>Author</h2>
<dd>Written by Andrew Beekhof</p>
