---
title: "crm_shadow(8)"
name: "crm_shadow"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_shadow/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_shadow</code> <i>(query|command) </i>[<i>modifiers</i>]</p>
<h2>Description</h2>
<p>crm_shadow &#8211; Perform configuration changes in a sandbox before updating the live cluster. </p>
<p> Sets up an environment in which configuration tools (cibadmin, crm_resource, etc) work offline instead of against a live cluster, allowing changes to be previewed and tested for side-effects.</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</dl>
<h3>Queries:</h3>
<dl>
<dt><code>-w</code>, <code>&#8211;which</code></p>
<dd>Indicate the active shadow copy</p>
<dt><code>-p</code>, <code>&#8211;display</code></p>
<dd>Display the contents of the active shadow copy</p>
<dt><code>-E</code>, <code>&#8211;edit</code></p>
<dd>Edit the contents of the active shadow copy with your favorite $EDITOR</p>
<dt><code>-d</code>, <code>&#8211;diff</code></p>
<dd>Display the changes in the active shadow copy</p>
<dt><code>-F</code>, <code>&#8211;file</code></p>
<dd>Display the location of the active shadow copy file</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;create</code>=<i>value</i></p>
<dd>Create the named shadow copy of the active cluster configuration</p>
<dt><code>-e</code>, <code>&#8211;create-empty</code>=<i>value</i></p>
<dd>Create the named shadow copy with an empty cluster configuration. Optional: <code>&#8211;validate-with</code></p>
<dt><code>-C</code>, <code>&#8211;commit</code>=<i>value</i></p>
<dd>Upload the contents of the named shadow copy to the cluster</p>
<dt><code>-D</code>, <code>&#8211;delete</code>=<i>value</i></p>
<dd>Delete the contents of the named shadow copy</p>
<dt><code>-r</code>, <code>&#8211;reset</code>=<i>value</i></p>
<dd>Recreate the named shadow copy from the active cluster configuration</p>
<dt><code>-s</code>, <code>&#8211;switch</code>=<i>value</i></p>
<dd>(Advanced) Switch to the named shadow copy</dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>(Advanced) Force the action to be performed</p>
<dt><code>-b</code>, <code>&#8211;batch</code></p>
<dd>(Advanced) Don&#8217;t spawn a new shell</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>(Advanced) Upload the entire CIB, including status, with <code>&#8211;commit</code></p>
<dt><code>-v</code>, <code>&#8211;validate-with</code>=<i>value</i></p>
<dd>(Advanced) Create an older configuration version</dl>
<h2>Examples</h2>
<p>Create a blank shadow configuration:</p>
<dl>
<dd># crm_shadow &#8211;create-empty myShadow</dl>
<p> Create a shadow configuration from the running cluster:</p>
<dl>
<dd># crm_shadow &#8211;create myShadow</dl>
<p> Display the current shadow configuration:</p>
<dl>
<dd># crm_shadow &#8211;display</dl>
<p> Discard the current shadow configuration (named myShadow):</p>
<dl>
<dd># crm_shadow &#8211;delete myShadow</dl>
<p> Upload the current shadow configuration (named myShadow) to the running cluster:</p>
<dl>
<dd># crm_shadow &#8211;commit myShadow</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
