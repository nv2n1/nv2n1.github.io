---
title: "crmadmin(8)"
name: "crmadmin"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crmadmin/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crmadmin</code> <i>command </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crmadmin &#8211; Development tool for performing some crmd-specific commands.</p>
<dl>
<dd>Likely to be replaced by crm_node in the future</dl>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Display only the essential query information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;debug_inc</code>=<i>value</i></p>
<dd>Increase the crmd&#8217;s debug level on the specified host</p>
<dt><code>-d</code>, <code>&#8211;debug_dec</code>=<i>value</i></p>
<dd>Decrease the crmd&#8217;s debug level on the specified host</p>
<dt><code>-S</code>, <code>&#8211;status</code>=<i>value</i></p>
<dd>Display the status of the specified node.</p>
<dd>Result is the node&#8217;s internal FSM state which can be useful for debugging</p>
<dt><code>-D</code>, <code>&#8211;dc_lookup</code></p>
<dd>Display the uname of the node co-ordinating the cluster.</p>
<dd>This is an internal detail and is rarely useful to administrators except when deciding on which node to examine the logs.</p>
<dt><code>-N</code>, <code>&#8211;nodes</code></p>
<dd>Display the uname of all member nodes</p>
<dt> <code>-E</code>, <code>&#8211;election</code> (Advanced) Start an election for the cluster co-ordinator</p>
<dt><code>-K</code>, <code>&#8211;kill</code>=<i>value</i></p>
<dd>(Advanced) Shut down the crmd (not the rest of the clusterstack ) on the specified node</dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>value</i></p>
<dd>
<dd>Time (in milliseconds) to wait before declaring the operation failed</p>
<dt><code>-B</code>, <code>&#8211;bash-export</code></p>
<dd>Create Bash export entries of the form &#8216;export uname=uuid&#8217;</dl>
<h3>Notes:</h3>
<dl>
<dd>The <code>-i</code>,-d,-K and <code>-E</code> commands are rarely used and may be removed in future versions.</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
