---
title: "cibadmin(8)"
name: "cibadmin"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cibadmin/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>cibadmin</code> <i>command </i>[<i>options</i>] [<i>data</i>]</p>
<h2>Description</h2>
<p>cibadmin &#8211; Provides direct access to the cluster configuration. </p>
<p> Allows the configuration, or sections of it, to be queried, modified, replaced and deleted. </p>
<p> Where necessary, XML data will be obtained using the <code>-X</code>, <code>-x</code>, or <code>-p</code> options.</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-u</code>, <code>&#8211;upgrade</code></p>
<dd>Upgrade the configuration to the latest syntax</p>
<dt><code>-Q</code>, <code>&#8211;query</code></p>
<dd>Query the contents of the CIB</p>
<dt><code>-E</code>, <code>&#8211;erase</code></p>
<dd>Erase the contents of the whole CIB</p>
<dt><code>-B</code>, <code>&#8211;bump</code></p>
<dd>Increase the CIB&#8217;s epoch value by 1</p>
<dt><code>-C</code>, <code>&#8211;create</code></p>
<dd>Create an object in the CIB. Will fail if the object already exists.</p>
<dt><code>-M</code>, <code>&#8211;modify</code></p>
<dd>Find the object somewhere in the CIB&#8217;s XML tree and update it. Fails if the object does not exist unless <code>-c</code> is specified</p>
<dt><code>-P</code>, <code>&#8211;patch</code></p>
<dd>Supply an update in the form of an xml diff (See also: crm_diff)</p>
<dt><code>-R</code>, <code>&#8211;replace</code></p>
<dd>Recursively replace an object in the CIB</p>
<dt><code>-D</code>, <code>&#8211;delete</code></p>
<dd>Delete the first object matching the supplied criteria, Eg. &lt;op id=&quot;rsc1_op1&quot; name=&quot;monitor&quot;/&gt;</p>
<dd>The tagname and all attributes must match in order for the element to be deleted</p>
<dt><code>-d</code>, <code>&#8211;delete-all</code></p>
<dd>When used with <code>&#8211;xpath</code>, remove all matching objects in the configuration instead of just the first one</p>
<dt><code>-a</code>, <code>&#8211;empty</code></p>
<dd>Output an empty CIB</p>
<dt><code>-5</code>, <code>&#8211;md5-sum</code></p>
<dd>Calculate the on-disk CIB digest</p>
<dt><code>-6</code>, <code>&#8211;md5-sum-versioned</code></p>
<dd>Calculate an on-the-wire versioned CIB digest</dl>
<h3>Additional options:</h3>
<dl>
<dt> <code>-f</code>, <code>&#8211;force</code></p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>value</i></p>
<dd>
<dd>Time (in seconds) to wait before declaring the operation failed</p>
<dt><code>-U</code>, <code>&#8211;user</code>=<i>value</i></p>
<dd>Run the command with permissions of the named user (valid only for the root and hacluster accounts)</p>
<dt><code>-s</code>, <code>&#8211;sync-call</code></p>
<dd>Wait for call to complete before returning</p>
<dt><code>-l</code>, <code>&#8211;local</code></p>
<dd>Command takes effect locally. Should only be used for queries</p>
<dt><code>-c</code>, <code>&#8211;allow-create</code></p>
<dd>(Advanced) Allow the target of a <code>&#8211;modify</code>,-M operation to be created if they do not exist</p>
<dt><code>-n</code>, <code>&#8211;no-children</code></p>
<dd>(Advanced) When querying an object, do not return include its children in the result</dl>
<h3>Data:</h3>
<dl>
<dt><code>-X</code>, <code>&#8211;xml-text</code>=<i>value</i></p>
<dd>Retrieve XML from the supplied string</p>
<dt><code>-x</code>, <code>&#8211;xml-file</code>=<i>value</i></p>
<dd>Retrieve XML from the named file</p>
<dt> <code>-p</code>, <code>&#8211;xml-pipe</code> Retrieve XML from stdin</p>
<dt><code>-o</code>, <code>&#8211;scope</code>=<i>value</i></p>
<dd>
<dd>Limit the scope of the operation to a specific section of the CIB.</p>
<dd>Valid values are: nodes, resources, constraints, crm_config, rsc_defaults, op_defaults, status</p>
<dt><code>-A</code>, <code>&#8211;xpath</code>=<i>value</i></p>
<dd>A valid XPath to use instead of <code>&#8211;scope</code>,-o</p>
<dt><code>-e</code>, <code>&#8211;node-path</code></p>
<dd>When performing XPath queries, return the address of any matches found.</p>
<dd>Eg: /cib/configuration/resources/master[@id=&#8217;ms_RH1_SCS&#8217;]/primitive[@id=&#8217;prm_RH1_SCS&#8217;]</p>
<dt><code>-N</code>, <code>&#8211;node</code>=<i>value</i></p>
<dd>(Advanced) Send command to the specified host</dl>
<h2>Examples</h2>
<p>Query the configuration from the local node:</p>
<dl>
<dd># cibadmin &#8211;query &#8211;local</dl>
<p> Query just the cluster options configuration:</p>
<dl>
<dd># cibadmin &#8211;query &#8211;scope crm_config</dl>
<pre><code>Query all 'target-role' settings:


# cibadmin --query --xpath &quot;//nvpair[@name='target-role']&quot;
Remove all 'is-managed' settings:


# cibadmin --delete-all --xpath &quot;//nvpair[@name='is-managed']&quot;</code></pre>
<p> Remove the resource named &#8216;old&#8217;:</p>
<dl>
<dd># cibadmin &#8211;delete &#8211;xml-text &#8216;&lt;primitive id=&quot;old&quot;/&gt;&#8217;</dl>
<p> Remove all resources from the configuration:</p>
<dl>
<dd># cibadmin &#8211;replace &#8211;scope resources &#8211;xml-text &#8216;&lt;resources/&gt;&#8217;</dl>
<p> Replace the complete configuration with the contents of $HOME/pacemaker.xml:</p>
<dl>
<dd># cibadmin &#8211;replace &#8211;xml-file $HOME/pacemaker.xml</dl>
<p> Replace the constraints section of the configuration with the contents of $HOME/constraints.xml:</p>
<dl>
<dd># cibadmin &#8211;replace &#8211;scope constraints &#8211;xml-file $HOME/constraints.xml</dl>
<p> Increase the configuration version to prevent old configurations from being loaded accidentally:</p>
<dl>
<dd># cibadmin &#8211;modify &#8211;xml-text &#8216;&lt;cib admin_epoch=&quot;admin_epoch++&quot;/&gt;&#8217;</dl>
<p> Edit the configuration with your favorite $EDITOR:</p>
<dl>
<dd># cibadmin &#8211;query &gt; $HOME/local.xml</p>
<dd># $EDITOR $HOME/local.xml</p>
<dd># cibadmin &#8211;replace &#8211;xml-file $HOME/local.xml</dl>
<h3>See Also:</h3>
<dl>
<dd><a href="/docs/linux/man/8-crm/">crm</a>(8), <a href="/docs/linux/man/8-pcs/">pcs</a>(8), <a href="/docs/linux/man/8-crm_shadow/">crm_shadow</a>(8), <a href="/docs/linux/man/8-crm_diff/">crm_diff</a>(8)</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
