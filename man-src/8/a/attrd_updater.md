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
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>value</i></p>
<dd>The attribute&#8217;s name</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-U</code>, <code>&#8211;update</code>=<i>value</i></p>
<dd>Update the attribute&#8217;s value in attrd. If this causes the value to change, it will also be updated in the cluster configuration</p>
<dt><code>-B</code>, <code>&#8211;update-both</code>=<i>value</i></p>
<dd>Update the attribute&#8217;s value and time to wait (dampening) in attrd. If this causes the value or dampening to change, the attribute will also be written to the cluster configuration, so be aware that repeatedly changing the dampening reduces its effectiveness.</p>
<dt><code>-Y</code>, <code>&#8211;update-delay</code></p>
<dd>Update the attribute&#8217;s dampening in attrd (requires <code>-d</code>/&#8211;delay). If this causes the dampening to change, the attribute will also be written to the cluster configuration, so be aware that repeatedly changing the dampening reduces its effectiveness.</p>
<dt><code>-Q</code>, <code>&#8211;query</code></p>
<dd>Query the attribute&#8217;s value from attrd</p>
<dt><code>-D</code>, <code>&#8211;delete</code></p>
<dd>Delete the attribute in attrd. If a value was previously set, it will also be removed from the cluster configuration</p>
<dt><code>-R</code>, <code>&#8211;refresh</code></p>
<dd>(Advanced) Force the attrd daemon to resend all current values to the CIB</dl>
<h3>Additional options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>value</i></p>
<dd>The time to wait (dampening) in seconds for further changes before writing</p>
<dt><code>-s</code>, <code>&#8211;set</code>=<i>value</i></p>
<dd>(Advanced) The attribute set in which to place the value</p>
<dt><code>-N</code>, <code>&#8211;node</code>=<i>value</i></p>
<dd>Set the attribute for the named node (instead of the local one)</p>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd>Show values of the attribute for all nodes (query only)</p>
<dt><code>-l</code>, <code>&#8211;lifetime</code>=<i>value</i></p>
<dd>(Deprecated) Lifetime of the node attribute (silently ignored by cluster)</p>
<dt><code>-p</code>, <code>&#8211;private</code></p>
<dd>If this creates a new attribute, never write the attribute to the CIB</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
