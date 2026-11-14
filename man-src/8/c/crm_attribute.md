---
title: "crm_attribute(8)"
name: "crm_attribute"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_attribute/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_attribute</code> <i>&lt;command&gt; -n &lt;attribute&gt; </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_attribute &#8211; Manage node&#8217;s attributes and cluster options. </p>
<p> Allows node attributes and cluster options to be queried, modified and deleted.</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Print only the value on stdout</p>
<dt><code>-n</code>, <code>&#8211;name</code>=<i>value</i></p>
<dd>Name of the attribute/option to operate on</dl>
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
<dd>Set an attribute for the named node (instead of a cluster option). See also: <code>-l</code></p>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>value</i></p>
<dd>Which part of the configuration to update/delete/query the option in Valid values: crm_config, rsc_defaults, op_defaults, tickets</p>
<dt><code>-l</code>, <code>&#8211;lifetime</code>=<i>value</i></p>
<dd>Lifetime of the node attribute Valid values: reboot, forever</p>
<dt><code>-z</code>, <code>&#8211;utilization</code></p>
<dd>Set an utilization attribute for the node.</p>
<dt><code>-s</code>, <code>&#8211;set-name</code>=<i>value</i></p>
<dd>(Advanced) The attribute set in which to place the value</p>
<dt><code>-i</code>, <code>&#8211;id</code>=<i>value</i></p>
<dd>(Advanced) The ID used to identify the attribute</p>
<dt><code>-d</code>, <code>&#8211;default</code>=<i>value</i></p>
<dd>(Advanced) The default value to display if none is found in the configuration</dl>
<h2>Examples</h2>
<p>Add a new node attribute called &#8216;location&#8217; with the value of &#8216;office&#8217; for host &#8216;myhost&#8217;:</p>
<dl>
<dd># crm_attribute &#8211;node myhost &#8211;name location &#8211;update office</dl>
<p> Query the value of the &#8216;location&#8217; node attribute for host &#8216;myhost&#8217;:</p>
<dl>
<dd># crm_attribute &#8211;node myhost &#8211;name location &#8211;query</dl>
<p> Change the value of the &#8216;location&#8217; node attribute for host &#8216;myhost&#8217;:</p>
<dl>
<dd># crm_attribute &#8211;node myhost &#8211;name location &#8211;update backoffice</dl>
<p> Delete the &#8216;location&#8217; node attribute for host &#8216;myhost&#8217;:</p>
<dl>
<dd># crm_attribute &#8211;node myhost &#8211;name location &#8211;delete</dl>
<p> Query the value of the cluster-delay cluster option:</p>
<dl>
<dd># crm_attribute &#8211;type crm_config &#8211;name cluster-delay &#8211;query</dl>
<p> Query the value of the cluster-delay cluster option. Only print the value:</p>
<dl>
<dd># crm_attribute &#8211;type crm_config &#8211;name cluster-delay &#8211;query &#8211;quiet</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
