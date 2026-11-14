---
title: "crm_failcount(8)"
name: "crm_failcount"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_failcount/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_failcount</code> <i>-r resource_name command </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_failcount &#8211; A convenience wrapper for crm_attribute </p>
<p> Set, update or remove the failcount for the specified resource on the named node</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>This text</p>
<dt><code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Print only the value on stdout</p>
<dt><code>-r</code>, <code>&#8211;resource-id</code>=<i>value</i></p>
<dd>The resource to update.</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-G</code>, <code>&#8211;query</code></p>
<dd>Query the current value of the attribute/option</p>
<dt><code>-v</code>, <code>&#8211;update</code>=<i>value</i></p>
<dd>Update the value of the attribute/option</p>
<dt><code>-D</code>, <code>&#8211;delete</code></p>
<dd>Delete the attribute/option</dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-N</code>, <code>&#8211;node</code>=<i>value</i></p>
<dd>Set an attribute for the named node (instead of the current one).</p>
<dt><code>-l</code>, <code>&#8211;lifetime</code>=<i>value</i></p>
<dd>Until when should the setting take affect. Valid values: reboot, forever</p>
<dt><code>-i</code>, <code>&#8211;id</code>=<i>value</i></p>
<dd>(Advanced) The ID used to identify the attribute</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
