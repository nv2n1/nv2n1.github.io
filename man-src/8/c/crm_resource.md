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
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-Q</code>, <code>&#8211;quiet</code></p>
<dd>Print only the value on stdout</p>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>value</i></p>
<dd>Resource ID</dl>
<h3>Queries:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;list</code></p>
<dd>List all cluster resources</p>
<dt><code>-l</code>, <code>&#8211;list-raw</code></p>
<dd>List the IDs of all instantiated resources (no groups/clones/&#8230;)</p>
<dt><code>-O</code>, <code>&#8211;list-operations</code></p>
<dd>List active resource operations. Optionally filtered by resource (<code>-r</code>) and/or node (<code>-N</code>)</p>
<dt><code>-o</code>, <code>&#8211;list-all-operations</code></p>
<dd>List all resource operations. Optionally filtered by resource (<code>-r</code>) and/or node (<code>-N</code>)</p>
<dt><code>-j</code>, <code>&#8211;pending</code></p>
<dd>Display pending state if &#8216;record-pending&#8217; is enabled</p>
<dt><code>&#8211;list-standards</code></p>
<dd>List supported standards</p>
<dt><code>&#8211;list-ocf-providers</code></p>
<dd>List all available OCF providers</p>
<dt><code>&#8211;list-agents</code>=<i>value</i></p>
<dd>List all agents available for the named standard and/or provider.</p>
<dt><code>&#8211;list-ocf-alternatives</code>=<i>value</i></p>
<dd>List all available providers for the named OCF agent</p>
<dt><code>&#8211;show-metadata</code>=<i>value</i></p>
<dd>Show the metadata for the named class:provider:agent</p>
<dt><code>-q</code>, <code>&#8211;query-xml</code></p>
<dd>Query the definition of a resource (template expanded)</p>
<dt><code>-w</code>, <code>&#8211;query-xml-raw</code></p>
<dd>Query the definition of a resource (raw xml)</p>
<dt><code>-W</code>, <code>&#8211;locate</code></p>
<dd>Display the current location(s) of a resource</p>
<dt><code>-A</code>, <code>&#8211;stack</code></p>
<dd>Display the prerequisites and dependents of a resource</p>
<dt><code>-a</code>, <code>&#8211;constraints</code></p>
<dd>Display the (co)location constraints that apply to a resource</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-C</code>, <code>&#8211;cleanup</code></p>
<dd>Delete the resource history and re-check the current state. Optional: <code>&#8211;resource</code></p>
<dt><code>-p</code>, <code>&#8211;set-parameter</code>=<i>value</i></p>
<dd>Set the named parameter for a resource. See also <code>-m</code>, <code>&#8211;meta</code></p>
<dt><code>-g</code>, <code>&#8211;get-parameter</code>=<i>value</i></p>
<dd>Display the named parameter for a resource. See also <code>-m</code>, <code>&#8211;meta</code></p>
<dt><code>-d</code>, <code>&#8211;delete-parameter</code>=<i>value</i></p>
<dd>Delete the named parameter for a resource. See also <code>-m</code>, <code>&#8211;meta</code></dl>
<h3>Resource location:</h3>
<dl>
<dt><code>-M</code>, <code>&#8211;move</code></p>
<dd>Move a resource from its current location to the named destination. Requires: <code>&#8211;host</code>. Optional: <code>&#8211;lifetime</code>, <code>&#8211;master</code></p>
<dd>NOTE: This may prevent the resource from running on the previous location node until the implicit constraints expire or are removed with <code>&#8211;unban</code></p>
<dt><code>-B</code>, <code>&#8211;ban</code></p>
<dd>Prevent the named resource from running on the named <code>&#8211;host</code>. Requires: <code>&#8211;resource</code>. Optional: <code>&#8211;host</code>, <code>&#8211;lifetime</code>, <code>&#8211;master</code></p>
<dd>If <code>&#8211;host</code> is not specified, it defaults to:</p>
<dd>* the current location for primitives and groups, or</p>
<dd>* the current location of the master for m/s resources with master-max=1</p>
<dd>All other situations result in an error as there is no sane default.</p>
<dd>NOTE: This will prevent the resource from running on this node until the constraint expires or is removed with <code>&#8211;clear</code></p>
<dt><code>-U</code>, <code>&#8211;clear</code></p>
<dd>Remove all constraints created by the <code>&#8211;ban</code> and/or <code>&#8211;move</code> commands. Requires: <code>&#8211;resource</code>. Optional: <code>&#8211;host</code>, <code>&#8211;master</code></p>
<dd>If <code>&#8211;host</code> is not specified, all constraints created by <code>&#8211;ban</code> and <code>&#8211;move</code> will be removed for the named resource.</p>
<dt><code>-u</code>, <code>&#8211;lifetime</code>=<i>value</i></p>
<dd>Lifespan of constraints created by the <code>&#8211;ban</code> and <code>&#8211;move</code> commands</p>
<dt><code>&#8211;master</code></p>
<dd>Limit the scope of the <code>&#8211;ban</code>, <code>&#8211;move</code> and <code>&#8211;clear</code> commands to the Master role. For <code>&#8211;ban</code> and <code>&#8211;move</code>, the previous master can still remain active in the Slave role.</dl>
<h3>Advanced Commands:</h3>
<dl>
<dt><code>-D</code>, <code>&#8211;delete</code></p>
<dd>(Advanced) Delete a resource from the CIB</p>
<dt><code>-F</code>, <code>&#8211;fail</code></p>
<dd>(Advanced) Tell the cluster this resource has failed</p>
<dt><code>&#8211;restart</code></p>
<dd>(Advanced) Tell the cluster to restart this resource and anything that depends on it</p>
<dt><code>&#8211;wait</code></p>
<dd>(Advanced) Wait until the cluster settles into a stable state</p>
<dt><code>&#8211;force-demote</code></p>
<dd>(Advanced) Bypass the cluster and demote a resource on the local node. Additional detail with <code>-V</code></p>
<dt><code>&#8211;force-stop</code></p>
<dd>(Advanced) Bypass the cluster and stop a resource on the local node. Additional detail with <code>-V</code></p>
<dt><code>&#8211;force-start</code></p>
<dd>(Advanced) Bypass the cluster and start a resource on the local node. Additional detail with <code>-V</code></p>
<dt><code>&#8211;force-promote</code></p>
<dd>(Advanced) Bypass the cluster and promote a resource on the local node. Additional detail with <code>-V</code></p>
<dt><code>&#8211;force-check</code></p>
<dd>(Advanced) Bypass the cluster and check the state of a resource on the local node. Additional detail with <code>-V</code></dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-N</code>, <code>&#8211;node</code>=<i>value</i></p>
<dd>Host uname</p>
<dt><code>&#8211;recursive</code></p>
<dd>Follow colocation chains when using <code>&#8211;set-parameter</code></p>
<dt><code>-t</code>, <code>&#8211;resource-type</code>=<i>value</i></p>
<dd>Resource type (primitive, clone, group, &#8230;)</p>
<dt><code>-v</code>, <code>&#8211;parameter-value</code>=<i>value</i></p>
<dd>Value to use with <code>-p</code> or <code>-S</code></p>
<dt><code>-m</code>, <code>&#8211;meta</code></p>
<dd>Modify a resource&#8217;s configuration option rather than one which is passed to the resource agent script. For use with <code>-p</code>, <code>-g</code>, <code>-d</code></p>
<dt><code>-z</code>, <code>&#8211;utilization</code></p>
<dd>Modify a resource&#8217;s utilization attribute. For use with <code>-p</code>, <code>-g</code>, <code>-d</code></p>
<dt><code>-s</code>, <code>&#8211;set-name</code>=<i>value</i></p>
<dd>(Advanced) ID of the instance_attributes object to change</p>
<dt><code>-i</code>, <code>&#8211;nvpair</code>=<i>value</i></p>
<dd>(Advanced) ID of the nvpair object to change/delete</p>
<dt><code>-T</code>, <code>&#8211;timeout</code>=<i>value</i></p>
<dd>(Advanced) Abort if command does not finish in this time (with <code>&#8211;restart</code> or <code>&#8211;wait</code>)</p>
<dt> <code>-f</code>, <code>&#8211;force</code></dl>
<h2>Examples</h2>
<dd>List the configured resources:</p>
<dl>
<dd># crm_resource &#8211;list</dl>
<p> List the available OCF agents:</p>
<dl>
<dd># crm_resource &#8211;list-agents ocf</dl>
<p> List the available OCF agents from the linux-ha project:</p>
<dl>
<dd># crm_resource &#8211;list-agents ocf:heartbeat</dl>
<p> Display the current location of &#8216;myResource&#8217;:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;locate</dl>
<p> Move &#8216;myResource&#8217; to another machine:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;move</dl>
<p> Move &#8216;myResource&#8217; to a specific machine:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;move &#8211;node altNode</dl>
<p> Allow (but not force) &#8216;myResource&#8217; to move back to its original location:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;un-move</dl>
<p> Tell the cluster that &#8216;myResource&#8217; failed:</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;fail</dl>
<p> Stop &#8216;myResource&#8217; (and anything that depends on it):</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;set-parameter target-role &#8211;meta &#8211;parameter-value Stopped</dl>
<p> Tell the cluster not to manage &#8216;myResource&#8217;: </p>
<p> The cluster will not attempt to start or stop the resource under any circumstances. Useful when performing maintenance tasks on a resource.</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;set-parameter is-managed &#8211;meta &#8211;parameter-value false</dl>
<p> Erase the operation history of &#8216;myResource&#8217; on &#8216;aNode&#8217;: </p>
<p> The cluster will &#8216;forget&#8217; the existing resource state (including any errors) and attempt to recover the resource. Useful when a resource had failed permanently and has been repaired by an administrator.</p>
<dl>
<dd># crm_resource &#8211;resource myResource &#8211;cleanup &#8211;node aNode</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
