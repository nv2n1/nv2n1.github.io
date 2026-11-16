---
title: "attrd_updater(8)"
name: "attrd_updater"
section: "8"
letter: "a"
url: "/docs/linux/man/8-attrd_updater/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>attrd_updater</code> <i>command -n attribute </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>attrd_updater &#8211; Tool for updating cluster node attributes</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd>This text</dd>
<dt>-$, <code>&#8211;version</code></dt>
<dd>Version information</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd>Increase debug output</dd>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>value</i></dt>
<dd>The attribute&#8217;s name</dd></dl>
<h3>Commands:</h3>
<dl>
<dt><code>-U</code>, <code>&#8211;update</code>=<i>value</i></dt>
<dd>Update the attribute&#8217;s value in attrd. If this causes the value to change, it will also be updated in the cluster configuration</dd>
<dt><code>-B</code>, <code>&#8211;update-both</code>=<i>value</i></dt>
<dd>Update the attribute&#8217;s value and time to wait (dampening) in attrd. If this causes the value or dampening to change, the attribute will also be written to the cluster configuration, so be aware that repeatedly changing the dampening reduces its effectiveness.</dd>
<dt><code>-Y</code>, <code>&#8211;update-delay</code></dt>
<dd>Update the attribute&#8217;s dampening in attrd (requires <code>-d</code>/&#8211;delay). If this causes the dampening to change, the attribute will also be written to the cluster configuration, so be aware that repeatedly changing the dampening reduces its effectiveness.</dd>
<dt><code>-Q</code>, <code>&#8211;query</code></dt>
<dd>Query the attribute&#8217;s value from attrd</dd>
<dt><code>-D</code>, <code>&#8211;delete</code></dt>
<dd>Delete the attribute in attrd. If a value was previously set, it will also be removed from the cluster configuration</dd>
<dt><code>-R</code>, <code>&#8211;refresh</code></dt>
<dd>(Advanced) Force the attrd daemon to resend all current values to the CIB</dd></dl>
<h3>Additional options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>value</i></dt>
<dd>The time to wait (dampening) in seconds for further changes before writing</dd>
<dt><code>-s</code>, <code>&#8211;set</code>=<i>value</i></dt>
<dd>(Advanced) The attribute set in which to place the value</dd>
<dt><code>-N</code>, <code>&#8211;node</code>=<i>value</i></dt>
<dd>Set the attribute for the named node (instead of the local one)</dd>
<dt><code>-A</code>, <code>&#8211;all</code></dt>
<dd>Show values of the attribute for all nodes (query only)</dd>
<dt><code>-l</code>, <code>&#8211;lifetime</code>=<i>value</i></dt>
<dd>(Deprecated) Lifetime of the node attribute (silently ignored by cluster)</dd>
<dt><code>-p</code>, <code>&#8211;private</code></dt>
<dd>If this creates a new attribute, never write the attribute to the CIB</dd></dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
