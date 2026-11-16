---
title: "crm_resource(8)"
name: "crm_resource"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_resource/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_resource</code> <i>(query|command) </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_resource &#8211; Perform tasks related to cluster resources. Allows resources to be queried (definition and location), modified, and moved around the cluster.</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd>This text</dd>
<dt>-$, <code>&#8211;version</code></dt>
<dd>Version information</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd>Increase debug output</dd>
<dt><code>-Q</code>, <code>&#8211;quiet</code></dt>
<dd>Print only the value on stdout</dd>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>value</i></dt>
<dd>Resource ID</dd></dl>
<h3>Queries:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;list</code></dt>
<dd>List all cluster resources</dd>
<dt><code>-l</code>, <code>&#8211;list-raw</code></dt>
<dd>List the IDs of all instantiated resources (no groups/clones/&#8230;)</dd>
<dt><code>-O</code>, <code>&#8211;list-operations</code></dt>
<dd>List active resource operations. Optionally filtered by resource (<code>-r</code>) and/or node (<code>-N</code>)</dd>
<dt><code>-o</code>, <code>&#8211;list-all-operations</code></dt>
<dd>List all resource operations. Optionally filtered by resource (<code>-r</code>) and/or node (<code>-N</code>)</dd>
<dt><code>-j</code>, <code>&#8211;pending</code></dt>
<dd>Display pending state if &#8216;record-pending&#8217; is enabled</dd>
<dt><code>&#8211;list-standards</code></dt>
<dd>List supported standards</dd>
<dt><code>&#8211;list-ocf-providers</code></dt>
<dd>List all available OCF providers</dd>
<dt><code>&#8211;list-agents</code>=<i>value</i></dt>
<dd>List all agents available for the named standard and/or provider.</dd>
<dt><code>&#8211;list-ocf-alternatives</code>=<i>value</i></dt>
<dd>List all available providers for the named OCF agent</dd>
<dt><code>&#8211;show-metadata</code>=<i>value</i></dt>
<dd>Show the metadata for the named class:provider:agent</dd>
<dt><code>-q</code>, <code>&#8211;query-xml</code></dt>
<dd>Query the definition of a resource (template expanded)</dd>
<dt><code>-w</code>, <code>&#8211;query-xml-raw</code></dt>
<dd>Query the definition of a resource (raw xml)</dd>
<dt><code>-W</code>, <code>&#8211;locate</code></dt>
<dd>Display the current location(s) of a resource</dd>
<dt><code>-A</code>, <code>&#8211;stack</code></dt>
<dd>Display the prerequisites and dependents of a resource</dd>
<dt><code>-a</code>, <code>&#8211;constraints</code></dt>
<dd>Display the (co)location constraints that apply to a resource</dd></dl>
<h3>Commands:</h3>
<dl>
<dt><code>-C</code>, <code>&#8211;cleanup</code></dt>
<dd>Delete the resource history and re-check the current state. Optional: <code>&#8211;resource</code></dd>
<dt><code>-p</code>, <code>&#8211;set-parameter</code>=<i>value</i></dt>
<dd>Set the named parameter for a resource. See also <code>-m</code>, <code>&#8211;meta</code></dd>
<dt><code>-g</code>, <code>&#8211;get-parameter</code>=<i>value</i></dt>
<dd>Display the named parameter for a resource. See also <code>-m</code>, <code>&#8211;meta</code></dd>
<dt><code>-d</code>, <code>&#8211;delete-parameter</code>=<i>value</i></dt>
<dd>Delete the named parameter for a resource. See also <code>-m</code>, <code>&#8211;meta</code></dd></dl>
<h3>Resource location:</h3>
<dl>
<dt><code>-M</code>, <code>&#8211;move</code></dt>
<dd>Move a resource from its current location to the named destination. Requires: <code>&#8211;host</code>. Optional: <code>&#8211;lifetime</code>, <code>&#8211;master</code></dd>
<dd>NOTE: This may prevent the resource from running on the previous location node until the implicit constraints expire or are removed with <code>&#8211;unban</code></dd>
<dt><code>-B</code>, <code>&#8211;ban</code></dt>
<dd>Prevent the named resource from running on the named <code>&#8211;host</code>. Requires: <code>&#8211;resource</code>. Optional: <code>&#8211;host</code>, <code>&#8211;lifetime</code>, <code>&#8211;master</code></dd>
<dd>If <code>&#8211;host</code> is not specified, it defaults to:</dd>
<dd>* the current location for primitives and groups, or</dd>
<dd>* the current location of the master for m/s resources with master-max=1</dd>
<dd>All other situations result in an error as there is no sane default.</dd>
<dd>NOTE: This will prevent the resource from running on this node until the constraint expires or is removed with <code>&#8211;clear</code></dd>
<dt><code>-U</code>, <code>&#8211;clear</code></dt>
<dd>Remove all constraints created by the <code>&#8211;ban</code> and/or <code>&#8211;move</code> commands. Requires: <code>&#8211;resource</code>. Optional: <code>&#8211;host</code>, <code>&#8211;master</code></dd>
<dd>If <code>&#8211;host</code> is not specified, all constraints created by <code>&#8211;ban</code> and <code>&#8211;move</code> will be removed for the named resource.</dd>
<dt><code>-u</code>, <code>&#8211;lifetime</code>=<i>value</i></dt>
<dd>Lifespan of constraints created by the <code>&#8211;ban</code> and <code>&#8211;move</code> commands</dd>
<dt><code>&#8211;master</code></dt>
<dd>Limit the scope of the <code>&#8211;ban</code>, <code>&#8211;move</code> and <code>&#8211;clear</code> commands to the Master role. For <code>&#8211;ban</code> and <code>&#8211;move</code>, the previous master can still remain active in the Slave role.</dd></dl>
<h3>Advanced Commands:</h3>
<dl>
<dt><code>-D</code>, <code>&#8211;delete</code></dt>
<dd>(Advanced) Delete a resource from the CIB</dd>
<dt><code>-F</code>, <code>&#8211;fail</code></dt>
<dd>(Advanced) Tell the cluster this resource has failed</dd>
<dt><code>&#8211;restart</code></dt>
<dd>(Advanced) Tell the cluster to restart this resource and anything that depends on it</dd>
<dt><code>&#8211;wait</code></dt>
<dd>(Advanced) Wait until the cluster settles into a stable state</dd>
<dt><code>&#8211;force-demote</code></dt>
<dd>(Advanced) Bypass the cluster and demote a resource on the local node. Additional detail with <code>-V</code></dd>
<dt><code>&#8211;force-stop</code></dt>
<dd>(Advanced) Bypass the cluster and stop a resource on the local node. Additional detail with <code>-V</code></dd>
<dt><code>&#8211;force-start</code></dt>
<dd>(Advanced) Bypass the cluster and start a resource on the local node. Additional detail with <code>-V</code></dd>
<dt><code>&#8211;force-promote</code></dt>
<dd>(Advanced) Bypass the cluster and promote a resource on the local node. Additional detail with <code>-V</code></dd>
<dt><code>&#8211;force-check</code></dt>
<dd>(Advanced) Bypass the cluster and check the state of a resource on the local node. Additional detail with <code>-V</code></dd></dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-N</code>, <code>&#8211;node</code>=<i>value</i></dt>
<dd>Host uname</dd>
<dt><code>&#8211;recursive</code></dt>
<dd>Follow colocation chains when using <code>&#8211;set-parameter</code></dd>
<dt><code>-t</code>, <code>&#8211;resource-type</code>=<i>value</i></dt>
<dd>Resource type (primitive, clone, group, &#8230;)</dd>
<dt><code>-v</code>, <code>&#8211;parameter-value</code>=<i>value</i></dt>
<dd>Value to use with <code>-p</code> or <code>-S</code></dd>
<dt><code>-m</code>, <code>&#8211;meta</code></dt>
<dd>Modify a resource&#8217;s configuration option rather than one which is passed to the resource agent script. For use with <code>-p</code>, <code>-g</code>, <code>-d</code></dd>
<dt><code>-z</code>, <code>&#8211;utilization</code></dt>
<dd>Modify a resource&#8217;s utilization attribute. For use with <code>-p</code>, <code>-g</code>, <code>-d</code></dd>
<dt><code>-s</code>, <code>&#8211;set-name</code>=<i>value</i></dt>
<dd>(Advanced) ID of the instance_attributes object to change</dd>
<dt><code>-i</code>, <code>&#8211;nvpair</code>=<i>value</i></dt>
<dd>(Advanced) ID of the nvpair object to change/delete</dd>
<dt><code>-T</code>, <code>&#8211;timeout</code>=<i>value</i></dt>
<dd>(Advanced) Abort if command does not finish in this time (with <code>&#8211;restart</code> or <code>&#8211;wait</code>)</dd>
<dt> <code>-f</code>, <code>&#8211;force</code></dt></dl>
<h2>Examples</h2>
<dd>List the configured resources:</dd>
<dl>
<dd># crm_resource &#8211;list</dd></dl>
<p> List the available OCF agents:</p>
<dl>
<dd># crm_resource &#8211;list-agents ocf</dd></dl>
<p> List the available OCF agents from the linux-ha project:</p>
<dl>
<dd># crm_resource &#8211;list-agents ocf:heartbeat</dd></dl>
<p> Display the current location of &#8216;myResource&#8217;:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;locate</dd></dl>
<p> Move &#8216;myResource&#8217; to another machine:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;move</dd></dl>
<p> Move &#8216;myResource&#8217; to a specific machine:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;move &#8211;node altNode</dd></dl>
<p> Allow (but not force) &#8216;myResource&#8217; to move back to its original location:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;un-move</dd></dl>
<p> Tell the cluster that &#8216;myResource&#8217; failed:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;fail</dd></dl>
<p> Stop &#8216;myResource&#8217; (and anything that depends on it):</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;set-parameter target-role &#8211;meta &#8211;parameter-value Stopped</dd></dl>
<p> Tell the cluster not to manage &#8216;myResource&#8217;: </p>
<p> The cluster will not attempt to start or stop the resource under any circumstances. Useful when performing maintenance tasks on a resource.</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;set-parameter is-managed &#8211;meta &#8211;parameter-value false</dd></dl>
<p> Erase the operation history of &#8216;myResource&#8217; on &#8216;aNode&#8217;: </p>
<p> The cluster will &#8216;forget&#8217; the existing resource state (including any errors) and attempt to recover the resource. Useful when a resource had failed permanently and has been repaired by an administrator.</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;cleanup &#8211;node aNode</dd></dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
