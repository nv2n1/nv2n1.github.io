---
title: "pcs(8)"
name: "pcs"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pcs/"
description: "pcs – pacemaker/corosync configuration system"
---

<p>pcs &#8211; pacemaker/corosync configuration system</p>
<h2>Synopsis</h2>
<p><code>pcs</code> [<i>-f file</i>] [<i>-h</i>] [<i>commands</i>]&#8230;</p>
<h2>Description</h2>
<p>Control and configure pacemaker and corosync.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage and exit.</p>
<dt><code>-f</code> file</p>
<dd>Perform actions on file instead of active CIB.</p>
<dt><code>&#8211;debug</code></p>
<dd>Print all network traffic and external commands run.</p>
<dt><code>&#8211;version</code></p>
<dd>Print pcs version information.</dl>
<h3>Commands:</h3>
<dl>
<dt>cluster</p>
<dd>Configure cluster options and nodes.</p>
<dt>resource</p>
<dd>Manage cluster resources.</p>
<dt>stonith</p>
<dd>Configure fence devices.</p>
<dt>constraint</p>
<dd>Set resource constraints.</p>
<dt>property</p>
<dd>Set pacemaker properties.</p>
<dt>acl</p>
<dd>Set pacemaker access control lists.</p>
<dt>qdevice</p>
<dd>Manage quorum device provider on the local host.</p>
<dt>quorum</p>
<dd>Manage cluster quorum settings.</p>
<dt>booth</p>
<dd>Manage booth (cluster ticket manager).</p>
<dt>status</p>
<dd>View cluster status.</p>
<dt>config</p>
<dd>View and manage cluster configuration.</p>
<dt>pcsd</p>
<dd>Manage pcs daemon.</p>
<dt>node</p>
<dd>Manage cluster nodes.</p>
<dt>alert</p>
<dd>Manage pacemaker alerts.</dl>
<h3>resource</h3>
<dl>
<dt>[show [&lt;resource id&gt;] | <code>&#8211;full</code> | <code>&#8211;groups</code> | <code>&#8211;hide-inactive</code>]</p>
<dd>Show all currently configured resources or if a resource is specified show the options for the configured resource. If <code>&#8211;full</code> is specified, all configured resource options will be displayed. If <code>&#8211;groups</code> is specified, only show groups (and their resources). If <code>&#8211;hide-inactive</code> is specified, only show active resources.</p>
<dt>list [&lt;standard|provider|type&gt;] [<code>&#8211;nodesc</code>]</p>
<dd>Show list of all available resources, optionally filtered by specified type, standard or provider. If <code>&#8211;nodesc</code> is used then descriptions of resources are not printed.</p>
<dt>describe &lt;standard:provider:type|type&gt;</p>
<dd>Show options for the specified resource.</p>
<dt>create &lt;resource id&gt; &lt;standard:provider:type|type&gt; [resource options] [op &lt;operation action&gt; &lt;operation options&gt; [&lt;operation action&gt; &lt;operation options&gt;]&#8230;] [meta &lt;meta options&gt;&#8230;] [<code>&#8211;clone</code> &lt;clone options&gt; | <code>&#8211;master</code> &lt;master options&gt; | <code>&#8211;group</code> &lt;group id&gt; [<code>&#8211;before</code> &lt;resource id&gt; | <code>&#8211;after</code> &lt;resource id&gt;]] [<code>&#8211;disabled</code>] [<code>&#8211;wait</code>[=n]]</p>
<dd>Create specified resource. If <code>&#8211;clone</code> is used a clone resource is created. If <code>&#8211;master</code> is specified a master/slave resource is created. If <code>&#8211;group</code> is specified the resource is added to the group named. You can use <code>&#8211;before</code> or <code>&#8211;after</code> to specify the position of the added resource relatively to some resource already existing in the group. If <code>&#8211;disabled</code> is specified the resource is not started automatically. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the resource to start and then return 0 if the resource is started, or 1 if the resource has not yet started. If &#8216;n&#8217; is not specified it defaults to 60 minutes. </p>
<p> Example: Create a new resource called &#8216;VirtualIP&#8217; with IP address 192.168.0.99, netmask of 32, monitored everything 30 seconds, on eth2: pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.99 cidr_netmask=32 nic=eth2 op monitor interval=30s</p>
<dt>delete &lt;resource id|group id|master id|clone id&gt;</p>
<dd>Deletes the resource, group, master or clone (and all resources within the group/master/clone).</p>
<dt>enable &lt;resource id&gt; [<code>&#8211;wait</code>[=n]]</p>
<dd>Allow the cluster to start the resource. Depending on the rest of the configuration (constraints, options, failures, etc), the resource may remain stopped. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the resource to start and then return 0 if the resource is started, or 1 if the resource has not yet started. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>disable &lt;resource id&gt; [<code>&#8211;wait</code>[=n]]</p>
<dd>Attempt to stop the resource if it is running and forbid the cluster from starting it again. Depending on the rest of the configuration (constraints, options, failures, etc), the resource may remain started. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the resource to stop and then return 0 if the resource is stopped or 1 if the resource has not stopped. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>restart &lt;resource id&gt; [node] [<code>&#8211;wait</code>=n]</p>
<dd>Restart the resource specified. If a node is specified and if the resource is a clone or master/slave it will be restarted only on the node specified. If <code>&#8211;wait</code> is specified, then we will wait up to &#8216;n&#8217; seconds for the resource to be restarted and return 0 if the restart was successful or 1 if it was not.</p>
<dt>debug-start &lt;resource id&gt; [<code>&#8211;full</code>]</p>
<dd>This command will force the specified resource to start on this node ignoring the cluster recommendations and print the output from starting the resource. Using <code>&#8211;full</code> will give more detailed output. This is mainly used for debugging resources that fail to start.</p>
<dt>debug-stop &lt;resource id&gt; [<code>&#8211;full</code>]</p>
<dd>This command will force the specified resource to stop on this node ignoring the cluster recommendations and print the output from stopping the resource. Using <code>&#8211;full</code> will give more detailed output. This is mainly used for debugging resources that fail to stop.</p>
<dt>debug-promote &lt;resource id&gt; [<code>&#8211;full</code>]</p>
<dd>This command will force the specified resource to be promoted on this node ignoring the cluster recommendations and print the output from promoting the resource. Using <code>&#8211;full</code> will give more detailed output. This is mainly used for debugging resources that fail to promote.</p>
<dt>debug-demote &lt;resource id&gt; [<code>&#8211;full</code>]</p>
<dd>This command will force the specified resource to be demoted on this node ignoring the cluster recommendations and print the output from demoting the resource. Using <code>&#8211;full</code> will give more detailed output. This is mainly used for debugging resources that fail to demote.</p>
<dt>debug-monitor &lt;resource id&gt; [<code>&#8211;full</code>]</p>
<dd>This command will force the specified resource to be moniored on this node ignoring the cluster recommendations and print the output from monitoring the resource. Using <code>&#8211;full</code> will give more detailed output. This is mainly used for debugging resources that fail to be monitored.</p>
<dt>move &lt;resource id&gt; [destination node] [<code>&#8211;master</code>] [lifetime=&lt;lifetime&gt;] [<code>&#8211;wait</code>[=n]]</p>
<dd>Move the resource off the node it is currently running on by creating a -INFINITY location constraint to ban the node. If destination node is specified the resource will be moved to that node by creating an INFINITY location constraint to prefer the destination node. If <code>&#8211;master</code> is used the scope of the command is limited to the master role and you must use the master id (instead of the resource id). If lifetime is specified then the constraint will expire after that time, otherwise it defaults to infinity and the constraint can be cleared manually with &#8216;pcs resource clear&#8217; or &#8216;pcs constraint delete&#8217;. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the resource to move and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes. If you want the resource to preferably avoid running on some nodes but be able to failover to them use &#8216;pcs location avoids&#8217;.</p>
<dt>ban &lt;resource id&gt; [node] [<code>&#8211;master</code>] [lifetime=&lt;lifetime&gt;] [<code>&#8211;wait</code>[=n]]</p>
<dd>Prevent the resource id specified from running on the node (or on the current node it is running on if no node is specified) by creating a -INFINITY location constraint. If <code>&#8211;master</code> is used the scope of the command is limited to the master role and you must use the master id (instead of the resource id). If lifetime is specified then the constraint will expire after that time, otherwise it defaults to infinity and the constraint can be cleared manually with &#8216;pcs resource clear&#8217; or &#8216;pcs constraint delete&#8217;. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the resource to move and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes. If you want the resource to preferably avoid running on some nodes but be able to failover to them use &#8216;pcs location avoids&#8217;.</p>
<dt>clear &lt;resource id&gt; [node] [<code>&#8211;master</code>] [<code>&#8211;wait</code>[=n]]</p>
<dd>Remove constraints created by move and/or ban on the specified resource (and node if specified). If <code>&#8211;master</code> is used the scope of the command is limited to the master role and you must use the master id (instead of the resource id). If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the operation to finish (including starting and/or moving resources if appropriate) and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>standards</p>
<dd>List available resource agent standards supported by this installation (OCF, LSB, etc.).</p>
<dt>providers</p>
<dd>List available OCF resource agent providers.</p>
<dt>agents [standard[:provider]]</p>
<dd>List available agents optionally filtered by standard and provider.</p>
<dt>update &lt;resource id&gt; [resource options] [op [&lt;operation action&gt; &lt;operation options&gt;]&#8230;] [meta &lt;meta operations&gt;&#8230;] [<code>&#8211;wait</code>[=n]]</p>
<dd>Add/Change options to specified resource, clone or multi-state resource. If an operation (op) is specified it will update the first found operation with the same action on the specified resource, if no operation with that action exists then a new operation will be created. (WARNING: all existing options on the updated operation will be reset if not specified.) If you want to create multiple monitor operations you should use the &#8216;op add&#8217; &amp; &#8216;op remove&#8217; commands. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the changes to take effect and then return 0 if the changes have been processed or 1 otherwise. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>op add &lt;resource id&gt; &lt;operation action&gt; [operation properties]</p>
<dd>Add operation for specified resource.</p>
<dt>op remove &lt;resource id&gt; &lt;operation action&gt; [&lt;operation properties&gt;&#8230;]</p>
<dd>Remove specified operation (note: you must specify the exact operation properties to properly remove an existing operation).</p>
<dt>op remove &lt;operation id&gt;</p>
<dd>Remove the specified operation id.</p>
<dt>op defaults [options]</p>
<dd>Set default values for operations, if no options are passed, lists currently configured defaults.</p>
<dt>meta &lt;resource id | group id | master id | clone id&gt; &lt;meta options&gt; [<code>&#8211;wait</code>[=n]]</p>
<dd>Add specified options to the specified resource, group, master/slave or clone. Meta options should be in the format of name=value, options may be removed by setting an option without a value. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the changes to take effect and then return 0 if the changes have been processed or 1 otherwise. If &#8216;n&#8217; is not specified it defaults to 60 minutes. Example: pcs resource meta TestResource failure-timeout=50 stickiness=</p>
<dt>group add &lt;group id&gt; &lt;resource id&gt; [resource id] &#8230; [resource id] [<code>&#8211;before</code> &lt;resource id&gt; | <code>&#8211;after</code> &lt;resource id&gt;] [<code>&#8211;wait</code>[=n]]</p>
<dd>Add the specified resource to the group, creating the group if it does not exist. If the resource is present in another group it is moved to the new group. You can use <code>&#8211;before</code> or <code>&#8211;after</code> to specify the position of the added resources relatively to some resource already existing in the group. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the operation to finish (including moving resources if appropriate) and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>group remove &lt;group id&gt; &lt;resource id&gt; [resource id] &#8230; [resource id] [<code>&#8211;wait</code>[=n]]</p>
<dd>Remove the specified resource(s) from the group, removing the group if it no resources remain. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the operation to finish (including moving resources if appropriate) and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>ungroup &lt;group id&gt; [resource id] &#8230; [resource id] [<code>&#8211;wait</code>[=n]]</p>
<dd>Remove the group (note: this does not remove any resources from the cluster) or if resources are specified, remove the specified resources from the group. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the operation to finish (including moving resources if appropriate) and the return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>clone &lt;resource id | group id&gt; [clone options]&#8230; [<code>&#8211;wait</code>[=n]]</p>
<dd>Setup up the specified resource or group as a clone. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the operation to finish (including starting clone instances if appropriate) and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>unclone &lt;resource id | group id&gt; [<code>&#8211;wait</code>[=n]]</p>
<dd>Remove the clone which contains the specified group or resource (the resource or group will not be removed). If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the operation to finish (including stopping clone instances if appropriate) and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>master [&lt;master/slave id&gt;] &lt;resource id | group id&gt; [options] [<code>&#8211;wait</code>[=n]]</p>
<dd>Configure a resource or group as a multi-state (master/slave) resource. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the operation to finish (including starting and promoting resource instances if appropriate) and then return 0 on success or 1 on error. If &#8216;n&#8217; is not specified it defaults to 60 minutes. Note: to remove a master you must remove the resource/group it contains.</p>
<dt>manage &lt;resource id&gt; &#8230; [resource n]</p>
<dd>Set resources listed to managed mode (default).</p>
<dt>unmanage &lt;resource id&gt; &#8230; [resource n]</p>
<dd>Set resources listed to unmanaged mode.</p>
<dt>defaults [options]</p>
<dd>Set default values for resources, if no options are passed, lists currently configured defaults.</p>
<dt>cleanup [&lt;resource id&gt;] [<code>&#8211;node</code> &lt;node&gt;]</p>
<dd>Cleans up the resource in the lrmd (useful to reset the resource status and failcount). This tells the cluster to forget the operation history of a resource and re-detect its current state. This can be useful to purge knowledge of past failures that have since been resolved. If a resource id is not specified then all resources/stonith devices will be cleaned up. If a node is not specified then resources on all nodes will be cleaned up.</p>
<dt>failcount show &lt;resource id&gt; [node]</p>
<dd>Show current failcount for specified resource from all nodes or only on specified node.</p>
<dt>failcount reset &lt;resource id&gt; [node]</p>
<dd>Reset failcount for specified resource on all nodes or only on specified node. This tells the cluster to forget how many times a resource has failed in the past. This may allow the resource to be started or moved to a more preferred location.</p>
<dt>relocate dry-run [resource1] [resource2] &#8230;</p>
<dd>The same as &#8216;relocate run&#8217; but has no effect on the cluster.</p>
<dt>relocate run [resource1] [resource2] &#8230;</p>
<dd>Relocate specified resources to their preferred nodes. If no resources are specified, relocate all resources. This command calculates the preferred node for each resource while ignoring resource stickiness. Then it creates location constraints which will cause the resources to move to their preferred nodes. Once the resources have been moved the constraints are deleted automatically. Note that the preferred node is calculated based on current cluster status, constraints, location of resources and other settings and thus it might change over time.</p>
<dt>relocate show</p>
<dd>Display current status of resources and their optimal node ignoring resource stickiness.</p>
<dt>relocate clear</p>
<dd>Remove all constraints created by the &#8216;relocate run&#8217; command.</p>
<dt>utilization [&lt;resource id&gt; [&lt;name&gt;=&lt;value&gt; &#8230;]]</p>
<dd>Add specified utilization options to specified resource. If resource is not specified, shows utilization of all resources. If utilization options are not specified, shows utilization of specified resource. Utilization option should be in format name=value, value has to be integer. Options may be removed by setting an option without a value. Example: pcs resource utilization TestResource cpu= ram=20</dl>
<h3>cluster</h3>
<dl>
<dt>auth [node] [&#8230;] [<code>-u</code> username] [<code>-p</code> password] [<code>&#8211;force</code>] [<code>&#8211;local</code>]</p>
<dd>Authenticate pcs to pcsd on nodes specified, or on all nodes configured in corosync.conf if no nodes are specified (authorization tokens are stored in ~/.pcs/tokens or /var/lib/pcsd/tokens for root). By default all nodes are also authenticated to each other, using <code>&#8211;local</code> only authenticates the local node (and does not authenticate the remote nodes with each other). Using <code>&#8211;force</code> forces re-authentication to occur.</p>
<dt>setup [<code>&#8211;start</code> [<code>&#8211;wait</code>[=&lt;n&gt;]]] [<code>&#8211;local</code>] [<code>&#8211;enable</code>] <code>&#8211;name</code> &lt;cluster name&gt; &lt;node1[,node1-altaddr]&gt; [&lt;node2[,node2-altaddr]&gt;] [&#8230;] [<code>&#8211;transport</code> udpu|udp] [<code>&#8211;rrpmode</code> active|passive] [<code>&#8211;addr0</code> &lt;addr/net&gt; [[[<code>&#8211;mcast0</code> &lt;address&gt;] [<code>&#8211;mcastport0</code> &lt;port&gt;] [<code>&#8211;ttl0</code> &lt;ttl&gt;]] | [<code>&#8211;broadcast0</code>]] [<code>&#8211;addr1</code> &lt;addr/net&gt; [[[<code>&#8211;mcast1</code> &lt;address&gt;] [<code>&#8211;mcastport1</code> &lt;port&gt;] [<code>&#8211;ttl1</code> &lt;ttl&gt;]] | [<code>&#8211;broadcast1</code>]]]] [<code>&#8211;wait_for_all</code>=&lt;0|1&gt;] [<code>&#8211;auto_tie_breaker</code>=&lt;0|1&gt;] [<code>&#8211;last_man_standing</code>=&lt;0|1&gt; [<code>&#8211;last_man_standing_window</code>=&lt;time in ms&gt;]] [<code>&#8211;ipv6</code>] [<code>&#8211;token</code> &lt;timeout&gt;] [<code>&#8211;token_coefficient</code> &lt;timeout&gt;] [<code>&#8211;join</code> &lt;timeout&gt;] [<code>&#8211;consensus</code> &lt;timeout&gt;] [<code>&#8211;miss_count_const</code> &lt;count&gt;] [<code>&#8211;fail_recv_const</code> &lt;failures&gt;]</p>
<dd>Configure corosync and sync configuration out to listed nodes. <code>&#8211;local</code> will only perform changes on the local node, <code>&#8211;start</code> will also start the cluster on the specified nodes, <code>&#8211;wait</code> will wait up to &#8216;n&#8217; seconds for the nodes to start, <code>&#8211;enable</code> will enable corosync and pacemaker on node startup, <code>&#8211;transport</code> allows specification of corosync transport (default: udpu; udp for RHEL 6 clusters), <code>&#8211;rrpmode</code> allows you to set the RRP mode of the system. Currently only &#8216;passive&#8217; is supported or tested (using &#8216;active&#8217; is not recommended). The <code>&#8211;wait_for_all</code>, <code>&#8211;auto_tie_breaker</code>, <code>&#8211;last_man_standing</code>, <code>&#8211;last_man_standing_window</code> options are all documented in corosync&#8217;s <a href="/docs/linux/man/5-votequorum/">votequorum</a>(5) man page. These options are not supported on RHEL 6 clusters. </p>
<p> <code>&#8211;ipv6</code> will configure corosync to use ipv6 (instead of ipv4). This option is not supported on RHEL 6 clusters. </p>
<p> <code>&#8211;token</code> &lt;timeout&gt; sets time in milliseconds until a token loss is declared after not receiving a token (default 1000 ms) </p>
<p> <code>&#8211;token_coefficient</code> &lt;timeout&gt; sets time in milliseconds used for clusters with at least 3 nodes as a coefficient for real token timeout calculation (token + (number_of_nodes &#8211; 2) * token_coefficient) (default 650 ms) This option is not supported on RHEL 6 clusters. </p>
<p> <code>&#8211;join</code> &lt;timeout&gt; sets time in milliseconds to wait for join messages (default 50 ms) </p>
<p> <code>&#8211;consensus</code> &lt;timeout&gt; sets time in milliseconds to wait for consensus to be achieved before starting a new round of membership configuration (default 1200 ms) </p>
<p> <code>&#8211;miss_count_const</code> &lt;count&gt; sets the maximum number of times on receipt of a token a message is checked for retransmission before a retransmission occurs (default 5 messages) </p>
<p> <code>&#8211;fail_recv_const</code> &lt;failures&gt; specifies how many rotations of the token without receiving any messages when messages should be received may occur before a new configuration is formed (default 2500 failures) </p>
<p> Configuring Redundant Ring Protocol (RRP) </p>
<p> When using udpu specifying nodes, specify the ring 0 address first followed by a &#8216;,&#8217; and then the ring 1 address. </p>
<p> Example: pcs cluster setup &#8211;name cname nodeA-0,nodeA-1 nodeB-0,nodeB-1 </p>
<p> When using udp, using <code>&#8211;addr0</code> and <code>&#8211;addr1</code> will allow you to configure rrp mode for corosync. It&#8217;s recommended to use a network (instead of IP address) for <code>&#8211;addr0</code> and <code>&#8211;addr1</code> so the same corosync.conf file can be used around the cluster. <code>&#8211;mcast0</code> defaults to 239.255.1.1 and <code>&#8211;mcast1</code> defaults to 239.255.2.1, <code>&#8211;mcastport0/1</code> default to 5405 and ttl defaults to 1. If <code>&#8211;broadcast</code> is specified, <code>&#8211;mcast0/1</code>, <code>&#8211;mcastport0/1</code> &amp; <code>&#8211;ttl0/1</code> are ignored.</p>
<dt>start [<code>&#8211;all</code>] [node] [&#8230;] [<code>&#8211;wait</code>[=&lt;n&gt;]]</p>
<dd>Start corosync &amp; pacemaker on specified node(s), if a node is not specified then corosync &amp; pacemaker are started on the local node. If <code>&#8211;all</code> is specified then corosync &amp; pacemaker are started on all nodes. If <code>&#8211;wait</code> is specified, wait up to &#8216;n&#8217; seconds for nodes to start.</p>
<dt>stop [<code>&#8211;all</code>] [node] [&#8230;]</p>
<dd>Stop corosync &amp; pacemaker on specified node(s), if a node is not specified then corosync &amp; pacemaker are stopped on the local node. If <code>&#8211;all</code> is specified then corosync &amp; pacemaker are stopped on all nodes.</p>
<dt>kill</p>
<dd>Force corosync and pacemaker daemons to stop on the local node (performs kill -9). Note that init system (e.g. systemd) can detect that cluster is not running and start it again. If you want to stop cluster on a node, run pcs cluster stop on that node.</p>
<dt>enable [<code>&#8211;all</code>] [node] [&#8230;]</p>
<dd>Configure corosync &amp; pacemaker to run on node boot on specified node(s), if node is not specified then corosync &amp; pacemaker are enabled on the local node. If <code>&#8211;all</code> is specified then corosync &amp; pacemaker are enabled on all nodes.</p>
<dt>disable [<code>&#8211;all</code>] [node] [&#8230;]</p>
<dd>Configure corosync &amp; pacemaker to not run on node boot on specified node(s), if node is not specified then corosync &amp; pacemaker are disabled on the local node. If <code>&#8211;all</code> is specified then corosync &amp; pacemaker are disabled on all nodes. Note: this is the default after installation.</p>
<dt>remote-node add &lt;hostname&gt; &lt;resource id&gt; [options]</p>
<dd>Enables the specified resource as a remote-node resource on the specified hostname (hostname should be the same as &#8216;uname -n&#8217;).</p>
<dt>remote-node remove &lt;hostname&gt;</p>
<dd>Disables any resources configured to be remote-node resource on the specified hostname (hostname should be the same as &#8216;uname -n&#8217;).</p>
<dt>status</p>
<dd>View current cluster status (an alias of &#8216;pcs status cluster&#8217;).</p>
<dt>pcsd-status [node] [&#8230;]</p>
<dd>Get current status of pcsd on nodes specified, or on all nodes configured in corosync.conf if no nodes are specified.</p>
<dt>sync</p>
<dd>Sync corosync configuration to all nodes found from current corosync.conf file (cluster.conf on systems running Corosync 1.x).</p>
<dt>cib [filename] [scope=&lt;scope&gt; | <code>&#8211;config</code>]</p>
<dd>Get the raw xml from the CIB (Cluster Information Base). If a filename is provided, we save the CIB to that file, otherwise the CIB is printed. Specify scope to get a specific section of the CIB. Valid values of the scope are: configuration, nodes, resources, constraints, crm_config, rsc_defaults, op_defaults, status. <code>&#8211;config</code> is the same as scope=configuration. Do not specify a scope if you want to edit the saved CIB using pcs (pcs -f &lt;command&gt;).</p>
<dt>cib-push &lt;filename&gt; [diff-against=&lt;filename_original&gt; | scope=&lt;scope&gt; | <code>&#8211;config</code>] [<code>&#8211;wait</code>[=&lt;n&gt;]]</p>
<dd>Push the raw xml from &lt;filename&gt; to the CIB (Cluster Information Base). You can obtain the CIB by running the &#8216;pcs cluster cib&#8217; command, which is recommended first step when you want to perform desired modifications (pcs <code>-f</code> &lt;command&gt;) for the one-off push. If diff-against is specified, pcs diffs contents of filename against contents of filename_original and pushes the result to the CIB. Specify scope to push a specific section of the CIB. Valid values of the scope are: configuration, nodes, resources, constraints, crm_config, rsc_defaults, op_defaults. <code>&#8211;config</code> is the same as scope=configuration. Use of <code>&#8211;config</code> is recommended. Do not specify a scope if you need to push the whole CIB or be warned in the case of outdated CIB. If &#8211;wait is specified wait up to &#8216;n&#8217; seconds for changes to be applied. WARNING: the selected scope of the CIB will be overwritten by the current content of the specified file. </p>
<p> Example:<br />
&nbsp;<wbr>pcs cluster cib&nbsp;<wbr>&gt;&nbsp;<wbr>original.xml<br />
&nbsp;<wbr>cp original.xml new.xml<br />
&nbsp;<wbr>pcs -f new.xml constraint location apache prefers node2<br />
&nbsp;<wbr>pcs cluster cib-push new.xml diff-against=original.xml</p>
<dt>cib-upgrade</p>
<dd>Upgrade the CIB to conform to the latest version of the document schema.</p>
<dt>edit [scope=&lt;scope&gt; | <code>&#8211;config</code>]</p>
<dd>Edit the cib in the editor specified by the $EDITOR environment variable and push out any changes upon saving. Specify scope to edit a specific section of the CIB. Valid values of the scope are: configuration, nodes, resources, constraints, crm_config, rsc_defaults, op_defaults. <code>&#8211;config</code> is the same as scope=configuration. Use of <code>&#8211;config</code> is recommended. Do not specify a scope if you need to edit the whole CIB or be warned in the case of outdated CIB.</p>
<dt>node add &lt;node[,node-altaddr]&gt; [<code>&#8211;start</code> [<code>&#8211;wait</code>[=&lt;n&gt;]]] [<code>&#8211;enable</code>] [<code>&#8211;watchdog</code>=&lt;watchdog-path&gt;]</p>
<dd>Add the node to corosync.conf and corosync on all nodes in the cluster and sync the new corosync.conf to the new node. If <code>&#8211;start</code> is specified also start corosync/pacemaker on the new node, if <code>&#8211;wait</code> is sepcified wait up to &#8216;n&#8217; seconds for the new node to start. If <code>&#8211;enable</code> is specified enable corosync/pacemaker on new node. When using Redundant Ring Protocol (RRP) with udpu transport, specify the ring 0 address first followed by a &#8216;,&#8217; and then the ring 1 address. Use <code>&#8211;watchdog</code> to specify path to watchdog on newly added node, when SBD is enabled in cluster.</p>
<dt>node remove &lt;node&gt;</p>
<dd>Shutdown specified node and remove it from pacemaker and corosync on all other nodes in the cluster.</p>
<dt>uidgid</p>
<dd>List the current configured uids and gids of users allowed to connect to corosync.</p>
<dt>uidgid add [uid=&lt;uid&gt;] [gid=&lt;gid&gt;]</p>
<dd>Add the specified uid and/or gid to the list of users/groups allowed to connect to corosync.</p>
<dt>uidgid rm [uid=&lt;uid&gt;] [gid=&lt;gid&gt;]</p>
<dd>Remove the specified uid and/or gid from the list of users/groups allowed to connect to corosync.</p>
<dt>corosync [node]</p>
<dd>Get the corosync.conf from the specified node or from the current node if node not specified.</p>
<dt>reload corosync</p>
<dd>Reload the corosync configuration on the current node.</p>
<dt>destroy [<code>&#8211;all</code>]</p>
<dd>Permanently destroy the cluster on the current node, killing all corosync/pacemaker processes removing all cib files and the corosync.conf file. Using <code>&#8211;all</code> will attempt to destroy the cluster on all nodes configure in the corosync.conf file. WARNING: This command permantly removes any cluster configuration that has been created. It is recommended to run &#8216;pcs cluster stop&#8217; before destroying the cluster.</p>
<dt>verify [<code>-V</code>] [filename]</p>
<dd>Checks the pacemaker configuration (cib) for syntax and common conceptual errors. If no filename is specified the check is performed on the currently running cluster. If <code>-V</code> is used more verbose output will be printed.</p>
<dt>report [<code>&#8211;from</code> &quot;YYYY-M-D H:M:S&quot; [<code>&#8211;to</code> &quot;YYYY-M-D&quot; H:M:S&quot;]] dest</p>
<dd>Create a tarball containing everything needed when reporting cluster problems. If <code>&#8211;from</code> and <code>&#8211;to</code> are not used, the report will include the past 24 hours.</dl>
<h3>stonith</h3>
<dl>
<dt>[show [stonith id]] [<code>&#8211;full</code>]</p>
<dd>Show all currently configured stonith devices or if a stonith id is specified show the options for the configured stonith device. If <code>&#8211;full</code> is specified all configured stonith options will be displayed.</p>
<dt>list [filter] [<code>&#8211;nodesc</code>]</p>
<dd>Show list of all available stonith agents (if filter is provided then only stonith agents matching the filter will be shown). If <code>&#8211;nodesc</code> is used then descriptions of stonith agents are not printed.</p>
<dt>describe &lt;stonith agent&gt;</p>
<dd>Show options for specified stonith agent.</p>
<dt>create &lt;stonith id&gt; &lt;stonith device type&gt; [stonith device options] [op &lt;operation action&gt; &lt;operation options&gt; [&lt;operation action&gt; &lt;operation options&gt;]&#8230;] [meta &lt;meta options&gt;&#8230;]</p>
<dd>Create stonith device with specified type and options.</p>
<dt>update &lt;stonith id&gt; [stonith device options]</p>
<dd>Add/Change options to specified stonith id.</p>
<dt>delete &lt;stonith id&gt;</p>
<dd>Remove stonith id from configuration.</p>
<dt>cleanup [&lt;stonith id&gt;] [<code>&#8211;node</code> &lt;node&gt;]</p>
<dd>Cleans up the stonith device in the lrmd (useful to reset the status and failcount). This tells the cluster to forget the operation history of a stonith device and re-detect its current state. This can be useful to purge knowledge of past failures that have since been resolved. If a stonith id is not specified then all resources/stonith devices will be cleaned up. If a node is not specified then resources on all nodes will be cleaned up.</p>
<dt>level</p>
<dd>Lists all of the fencing levels currently configured.</p>
<dt>level add &lt;level&gt; &lt;node&gt; &lt;devices&gt;</p>
<dd>Add the fencing level for the specified node with a comma separated list of devices (stonith ids) to attempt for that node at that level. Fence levels are attempted in numerical order (starting with 1) if a level succeeds (meaning all devices are successfully fenced in that level) then no other levels are tried, and the node is considered fenced.</p>
<dt>level remove &lt;level&gt; [node id] [stonith id] &#8230; [stonith id]</p>
<dd>Removes the fence level for the level, node and/or devices specified. If no nodes or devices are specified then the fence level is removed.</p>
<dt>level clear [node|stonith id(s)]</p>
<dd>Clears the fence levels on the node (or stonith id) specified or clears all fence levels if a node/stonith id is not specified. If more than one stonith id is specified they must be separated by a comma and no spaces. Example: pcs stonith level clear dev_a,dev_b</p>
<dt>level verify</p>
<dd>Verifies all fence devices and nodes specified in fence levels exist.</p>
<dt>fence &lt;node&gt; [<code>&#8211;off</code>]</p>
<dd>Fence the node specified (if <code>&#8211;off</code> is specified, use the &#8216;off&#8217; API call to stonith which will turn the node off instead of rebooting it).</p>
<dt>confirm &lt;node&gt; [<code>&#8211;force</code>]</p>
<dd>Confirm that the host specified is currently down. This command should <code>ONLY</code> be used when the node specified has already been confirmed to be powered off and to have no access to shared resources. </p>
<p> <code>WARNING: If this node is not actually powered off or it does have access to shared resources, data corruption/cluster failure can occur. To prevent accidental running of this command, &#8211;force or interactive user response is required in order to proceed.</code></p>
<dt>sbd enable [<code>&#8211;watchdog</code>=&lt;path&gt;[@&lt;node&gt;]] &#8230; [&lt;SBD_OPTION&gt;=&lt;value&gt;] &#8230;</p>
<dd>Enable SBD in cluster. Default path for watchdog device is /dev/watchdog. Allowed SBD options: SBD_WATCHDOG_TIMEOUT (default: 5), SBD_DELAY_START (default: no) and SBD_STARTMODE (default: clean). </p>
<p> <code>WARNING: Cluster has to be restarted in order to apply these changes.</code> </p>
<p> Example of enabling SBD in cluster with watchdogs on node1 will be /dev/watchdog2, on node2 /dev/watchdog1, /dev/watchdog0 on all other nodes and watchdog timeout will bet set to 10 seconds: </p>
<p> pcs stonith sbd enable &#8211;watchdog=/dev/watchdog2 [at] node1 &#8211;watchdog=/dev/watchdog1 [at] node2 &#8211;watchdog=/dev/watchdog0 SBD_WATCHDOG_TIMEOUT=10 </p>
<dt>sbd disable</p>
<dd>Disable SBD in cluster. </p>
<p> <code>WARNING: Cluster has to be restarted in order to apply these changes.</code></p>
<dt>sbd status</p>
<dd>Show status of SBD services in cluster.</p>
<dt>sbd config</p>
<dd>Show SBD configuration in cluster.</dl>
<h3>acl</h3>
<dl>
<dt>[show]</p>
<dd>List all current access control lists.</p>
<dt>enable</p>
<dd>Enable access control lists.</p>
<dt>disable</p>
<dd>Disable access control lists.</p>
<dt>role create &lt;role id&gt; [description=&lt;description&gt;] [((read | write | deny) (xpath &lt;query&gt; | id &lt;id&gt;))&#8230;]</p>
<dd>Create a role with the id and (optional) description specified. Each role can also have an unlimited number of permissions (read/write/deny) applied to either an xpath query or the id of a specific element in the cib.</p>
<dt>role delete &lt;role id&gt;</p>
<dd>Delete the role specified and remove it from any users/groups it was assigned to.</p>
<dt>role assign &lt;role id&gt; [to] &lt;username/group&gt;</p>
<dd>Assign a role to a user or group already created with &#8216;pcs acl user/group create&#8217;.</p>
<dt>role unassign &lt;role id&gt; [from] &lt;username/group&gt;</p>
<dd>Remove a role from the specified user.</p>
<dt>user create &lt;username&gt; &lt;role id&gt; [&lt;role id&gt;]&#8230;</p>
<dd>Create an ACL for the user specified and assign roles to the user.</p>
<dt>user delete &lt;username&gt;</p>
<dd>Remove the user specified (and roles assigned will be unassigned for the specified user).</p>
<dt>group create &lt;group&gt; &lt;role id&gt; [&lt;role id&gt;]&#8230;</p>
<dd>Create an ACL for the group specified and assign roles to the group.</p>
<dt>group delete &lt;group&gt;</p>
<dd>Remove the group specified (and roles assigned will be unassigned for the specified group).</p>
<dt>permission add &lt;role id&gt; ((read | write | deny) (xpath &lt;query&gt; | id &lt;id&gt;))&#8230;</p>
<dd>Add the listed permissions to the role specified.</p>
<dt>permission delete &lt;permission id&gt;</p>
<dd>Remove the permission id specified (permission id&#8217;s are listed in parenthesis after permissions in &#8216;pcs acl&#8217; output).</dl>
<h3>property</h3>
<dl>
<dt>[list|show [&lt;property&gt; | <code>&#8211;all</code> | <code>&#8211;defaults</code>]] | [<code>&#8211;all</code> | <code>&#8211;defaults</code>]</p>
<dd>List property settings (default: lists configured properties). If <code>&#8211;defaults</code> is specified will show all property defaults, if <code>&#8211;all</code> is specified, current configured properties will be shown with unset properties and their defaults. Run &#8216;man pengine&#8217; and &#8216;man crmd&#8217; to get a description of the properties.</p>
<dt>set [<code>&#8211;force</code> | <code>&#8211;node</code> &lt;nodename&gt;] &lt;property&gt;=[&lt;value&gt;] [&lt;property&gt;=[&lt;value&gt;] &#8230;]</p>
<dd>Set specific pacemaker properties (if the value is blank then the property is removed from the configuration). If a property is not recognized by pcs the property will not be created unless the <code>&#8211;force</code> is used. If <code>&#8211;node</code> is used a node attribute is set on the specified node. Run &#8216;man pengine&#8217; and &#8216;man crmd&#8217; to get a description of the properties.</p>
<dt>unset [<code>&#8211;node</code> &lt;nodename&gt;] &lt;property&gt;</p>
<dd>Remove property from configuration (or remove attribute from specified node if <code>&#8211;node</code> is used). Run &#8216;man pengine&#8217; and &#8216;man crmd&#8217; to get a description of the properties.</dl>
<h3>constraint</h3>
<dl>
<dt>[list|show] <code>&#8211;full</code></p>
<dd>List all current location, order and colocation constraints, if <code>&#8211;full</code> is specified also list the constraint ids.</p>
<dt>location &lt;resource id&gt; prefers &lt;node[=score]&gt;&#8230;</p>
<dd>Create a location constraint on a resource to prefer the specified node and score (default score: INFINITY).</p>
<dt>location &lt;resource id&gt; avoids &lt;node[=score]&gt;&#8230;</p>
<dd>Create a location constraint on a resource to avoid the specified node and score (default score: INFINITY).</p>
<dt>location &lt;resource id&gt; rule [id=&lt;rule id&gt;] [resource-discovery=&lt;option&gt;] [role=master|slave] [constraint-id=&lt;id&gt;] [score=&lt;score&gt;|score-attribute=&lt;attribute&gt;] &lt;expression&gt;</p>
<dd>Creates a location rule on the specified resource where the expression looks like one of the following: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defined|not_defined&nbsp;<wbr>&lt;attribute&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;attribute&gt;&nbsp;<wbr>lt|gt|lte|gte|eq|ne&nbsp;<wbr>[string|integer|version]&nbsp;<wbr>&lt;value&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date gt|lt&nbsp;<wbr>&lt;date&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date in_range&nbsp;<wbr>&lt;date&gt;&nbsp;<wbr>to&nbsp;<wbr>&lt;date&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date in_range&nbsp;<wbr>&lt;date&gt;&nbsp;<wbr>to duration&nbsp;<wbr>&lt;duration options&gt;&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date-spec&nbsp;<wbr>&lt;date spec options&gt;&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;expression&gt;&nbsp;<wbr>and|or&nbsp;<wbr>&lt;expression&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(&nbsp;<wbr>&lt;expression&gt;&nbsp;<wbr>)<br />
 where duration options and date spec options are: hours, monthdays, weekdays, yeardays, months, weeks, years, weekyears, moon. If score is omitted it defaults to INFINITY. If id is omitted one is generated from the resource id. If resource-discovery is omitted it defaults to &#8216;always&#8217;.</p>
<dt>location [show [resources|nodes [node id|resource id]&#8230;] [<code>&#8211;full</code>]]</p>
<dd>List all the current location constraints, if &#8216;resources&#8217; is specified location constraints are displayed per resource (default), if &#8216;nodes&#8217; is specified location constraints are displayed per node. If specific nodes or resources are specified then we only show information about them. If <code>&#8211;full</code> is specified show the internal constraint id&#8217;s as well.</p>
<dt>location add &lt;id&gt; &lt;resource id&gt; &lt;node&gt; &lt;score&gt; [resource-discovery=&lt;option&gt;]</p>
<dd>Add a location constraint with the appropriate id, resource id, node name and score. (For more advanced pacemaker usage.)</p>
<dt>location remove &lt;id&gt; [&lt;resource id&gt; &lt;node&gt; &lt;score&gt;]</p>
<dd>Remove a location constraint with the appropriate id, resource id, node name and score. (For more advanced pacemaker usage.)</p>
<dt>order [show] [<code>&#8211;full</code>]</p>
<dd>List all current ordering constraints (if <code>&#8211;full</code> is specified show the internal constraint id&#8217;s as well).</p>
<dt>order [action] &lt;resource id&gt; then [action] &lt;resource id&gt; [options]</p>
<dd>Add an ordering constraint specifying actions (start, stop, promote, demote) and if no action is specified the default action will be start. Available options are kind=Optional/Mandatory/Serialize, symmetrical=true/false, require-all=true/false and id=&lt;constraint-id&gt;.</p>
<dt>order set &lt;resource1&gt; [resourceN]&#8230; [options] [set &lt;resourceX&gt; &#8230; [options]] [setoptions [constraint_options]]</p>
<dd>Create an ordered set of resources. Available options are sequential=true/false, require-all=true/false, action=start/promote/demote/stop and role=Stopped/Started/Master/Slave. Available constraint_options are id=&lt;constraint-id&gt;, kind=Optional/Mandatory/Serialize and symmetrical=true/false.</p>
<dt>order remove &lt;resource1&gt; [resourceN]&#8230;</p>
<dd>Remove resource from any ordering constraint</p>
<dt>colocation [show] [<code>&#8211;full</code>]</p>
<dd>List all current colocation constraints (if <code>&#8211;full</code> is specified show the internal constraint id&#8217;s as well).</p>
<dt>colocation add [master|slave] &lt;source resource id&gt; with [master|slave] &lt;target resource id&gt; [score] [options] [id=constraint-id]</p>
<dd>Request &lt;source resource&gt; to run on the same node where pacemaker has determined &lt;target resource&gt; should run. Positive values of score mean the resources should be run on the same node, negative values mean the resources should not be run on the same node. Specifying &#8216;INFINITY&#8217; (or &#8216;-INFINITY&#8217;) for the score forces &lt;source resource&gt; to run (or not run) with &lt;target resource&gt; (score defaults to &quot;INFINITY&quot;). A role can be master or slave (if no role is specified, it defaults to &#8216;started&#8217;).</p>
<dt>colocation set &lt;resource1&gt; [resourceN]&#8230; [options] [set &lt;resourceX&gt; &#8230; [options]] [setoptions [constraint_options]]</p>
<dd>Create a colocation constraint with a resource set. Available options are sequential=true/false, require-all=true/false, action=start/promote/demote/stop and role=Stopped/Started/Master/Slave. Available constraint_options are id, score, score-attribute and score-attribute-mangle.</p>
<dt>colocation remove &lt;source resource id&gt; &lt;target resource id&gt;</p>
<dd>Remove colocation constraints with specified resources.</p>
<dt>ticket [show] [<code>&#8211;full</code>]</p>
<dd>List all current ticket constraints (if <code>&#8211;full</code> is specified show the internal constraint id&#8217;s as well).</p>
<dt>ticket add &lt;ticket&gt; [&lt;role&gt;] &lt;resource id&gt; [&lt;options&gt;] [id=&lt;constraint-id&gt;]</p>
<dd>Create a ticket constraint for &lt;resource id&gt;. Available option is loss-policy=fence/stop/freeze/demote. A role can be master, slave, started or stopped.</p>
<dt>ticket set &lt;resource1&gt; [&lt;resourceN&gt;]&#8230; [&lt;options&gt;] [set &lt;resourceX&gt; &#8230; [&lt;options&gt;]] setoptions &lt;constraint_options&gt;</p>
<dd>Create a ticket constraint with a resource set. Available options are sequential=true/false, require-all=true/false, action=start/promote/demote/stop and role=Stopped/Started/Master/Slave. Required constraint option is ticket=&lt;ticket&gt;. Optional constraint options are id=&lt;constraint-id&gt; and loss-policy=fence/stop/freeze/demote.</p>
<dt>ticket remove &lt;ticket&gt; &lt;resource id&gt;</p>
<dd>Remove all ticket constraints with &lt;ticket&gt; from &lt;resource id&gt;.</p>
<dt>remove [constraint id]&#8230;</p>
<dd>Remove constraint(s) or constraint rules with the specified id(s).</p>
<dt>ref &lt;resource&gt;&#8230;</p>
<dd>List constraints referencing specified resource.</p>
<dt>rule add &lt;constraint id&gt; [id=&lt;rule id&gt;] [role=master|slave] [score=&lt;score&gt;|score-attribute=&lt;attribute&gt;] &lt;expression&gt;</p>
<dd>Add a rule to a constraint where the expression looks like one of the following: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defined|not_defined&nbsp;<wbr>&lt;attribute&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;attribute&gt;&nbsp;<wbr>lt|gt|lte|gte|eq|ne&nbsp;<wbr>[string|integer|version]&nbsp;<wbr>&lt;value&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date gt|lt&nbsp;<wbr>&lt;date&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date in_range&nbsp;<wbr>&lt;date&gt;&nbsp;<wbr>to&nbsp;<wbr>&lt;date&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date in_range&nbsp;<wbr>&lt;date&gt;&nbsp;<wbr>to duration&nbsp;<wbr>&lt;duration options&gt;&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>date-spec&nbsp;<wbr>&lt;date spec options&gt;&#8230; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;expression&gt;&nbsp;<wbr>and|or&nbsp;<wbr>&lt;expression&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(&nbsp;<wbr>&lt;expression&gt;&nbsp;<wbr>)<br />
 where duration options and date spec options are: hours, monthdays, weekdays, yeardays, months, weeks, years, weekyears, moon If score is ommited it defaults to INFINITY. If id is ommited one is generated from the constraint id.</p>
<dt>rule remove &lt;rule id&gt;</p>
<dd>Remove a rule if a rule id is specified, if rule is last rule in its constraint, the constraint will be removed.</dl>
<h3>qdevice</h3>
<dl>
<dt>status &lt;device model&gt; [<code>&#8211;full</code>] [&lt;cluster name&gt;]</p>
<dd>Show runtime status of specified model of quorum device provider. Using <code>&#8211;full</code> will give more detailed output. If &lt;cluster name&gt; is specified, only information about the specified cluster will be displayed.</p>
<dt>setup model &lt;device model&gt; [<code>&#8211;enable</code>] [<code>&#8211;start</code>]</p>
<dd>Configure specified model of quorum device provider. Quorum device then can be added to clusters by running &quot;pcs quorum device add&quot; command in a cluster. <code>&#8211;start</code> will also start the provider. <code>&#8211;enable</code> will configure the provider to start on boot.</p>
<dt>destroy &lt;device model&gt;</p>
<dd>Disable and stop specified model of quorum device provider and delete its configuration files.</p>
<dt>start &lt;device model&gt;</p>
<dd>Start specified model of quorum device provider.</p>
<dt>stop &lt;device model&gt;</p>
<dd>Stop specified model of quorum device provider.</p>
<dt>kill &lt;device model&gt;</p>
<dd>Force specified model of quorum device provider to stop (performs kill -9). Note that init system (e.g. systemd) can detect that the qdevice is not running and start it again. If you want to stop the qdevice, run &quot;pcs qdevice stop&quot; command.</p>
<dt>enable &lt;device model&gt;</p>
<dd>Configure specified model of quorum device provider to start on boot.</p>
<dt>disable &lt;device model&gt;</p>
<dd>Configure specified model of quorum device provider to not start on boot.</dl>
<h3>quorum</h3>
<dl>
<dt>[config]</p>
<dd>Show quorum configuration.</p>
<dt>status</p>
<dd>Show quorum runtime status.</p>
<dt>device add [&lt;generic options&gt;] model &lt;device model&gt; [&lt;model options&gt;]</p>
<dd>Add a quorum device to the cluster. Quorum device needs to be created first by &quot;pcs qdevice setup&quot; command. It is not possible to use more than one quorum device in a cluster simultaneously. Generic options, model and model options are all documented in corosync&#8217;s <a href="/docs/linux/man/8-corosync-qdevice/">corosync-qdevice</a>(8) man page.</p>
<dt>device remove</p>
<dd>Remove a quorum device from the cluster.</p>
<dt>device status [<code>&#8211;full</code>]</p>
<dd>Show quorum device runtime status. Using <code>&#8211;full</code> will give more detailed output.</p>
<dt>device update [&lt;generic options&gt;] [model &lt;model options&gt;]</p>
<dd>Add/Change quorum device options. Generic options and model options are all documented in corosync&#8217;s <a href="/docs/linux/man/8-corosync-qdevice/">corosync-qdevice</a>(8) man page. Requires the cluster to be stopped. </p>
<p> WARNING: If you want to change &quot;host&quot; option of qdevice model net, use &quot;pcs quorum device remove&quot; and &quot;pcs quorum device add&quot; commands to set up configuration properly unless old and new host is the same machine.</p>
<dt>expected-votes &lt;votes&gt;</p>
<dd>Set expected votes in the live cluster to specified value. This only affects the live cluster, not changes any configuration files.</p>
<dt>unblock [<code>&#8211;force</code>]</p>
<dd>Cancel waiting for all nodes when establishing quorum. Useful in situations where you know the cluster is inquorate, but you are confident that the cluster should proceed with resource management regardless. This command should ONLY be used when nodes which the cluster is waiting for have been confirmed to be powered off and to have no access to shared resources. </p>
<p> <code>WARNING: If the nodes are not actually powered off or they do have access to shared resources, data corruption/cluster failure can occur. To prevent accidental running of this command, &#8211;force or interactive user response is required in order to proceed.</code></p>
<dt>update [auto_tie_breaker=[0|1]] [last_man_standing=[0|1]] [last_man_standing_window=[&lt;time in ms&gt;]] [wait_for_all=[0|1]]</p>
<dd>Add/Change quorum options. At least one option must be specified. Options are documented in corosync&#8217;s <a href="/docs/linux/man/5-votequorum/">votequorum</a>(5) man page. Requires the cluster to be stopped.</dl>
<h3>booth</h3>
<dl>
<dt>setup sites &lt;address&gt; &lt;address&gt; [&lt;address&gt;&#8230;] [arbitrators &lt;address&gt; &#8230;] [<code>&#8211;force</code>]</p>
<dd>Write new booth configuration with specified sites and arbitrators. Total number of peers (sites and arbitrators) must be odd. When the configuration file already exists, command fails unless <code>&#8211;force</code> is specified.</p>
<dt>destroy</p>
<dd>Remove booth configuration files.</p>
<dt>ticket add &lt;ticket&gt; [&lt;name&gt;=&lt;value&gt; &#8230;]</p>
<dd>Add new ticket to the current configuration. Ticket options are specified in booth manpage. </p>
<dt>ticket remove &lt;ticket&gt;</p>
<dd>Remove the specified ticket from the current configuration.</p>
<dt>config [&lt;node&gt;]</p>
<dd>Show booth configuration from the specified node or from the current node if node not specified.</p>
<dt>create ip &lt;address&gt;</p>
<dd>Make the cluster run booth service on the specified ip address as a cluster resource. Typically this is used to run booth site.</p>
<dt>remove</p>
<dd>Remove booth resources created by the &quot;pcs booth create&quot; command.</p>
<dt>restart</p>
<dd>Restart booth resources created by the &quot;pcs booth create&quot; command.</p>
<dt>ticket grant &lt;ticket&gt; [&lt;site address&gt;]</p>
<dd>Grant the ticket for the site specified by address. Site address which has been specified with &#8216;pcs booth create&#8217; command is used if &#8216;site address&#8217; is omitted. Specifying site address is mandatory when running this command on an arbitrator.</p>
<dt>ticket revoke &lt;ticket&gt; [&lt;site address&gt;]</p>
<dd>Revoke the ticket for the site specified by address. Site address which has been specified with &#8216;pcs booth create&#8217; command is used if &#8216;site address&#8217; is omitted. Specifying site address is mandatory when running this command on an arbitrator.</p>
<dt>status</p>
<dd>Print current status of booth on the local node.</p>
<dt>pull &lt;node&gt;</p>
<dd>Pull booth configuration from the specified node.</p>
<dt>sync [<code>&#8211;skip-offline</code>]</p>
<dd>Send booth configuration from the local node to all nodes in the cluster.</p>
<dt>enable</p>
<dd>Enable booth arbitrator service.</p>
<dt>disable</p>
<dd>Disable booth arbitrator service.</p>
<dt>start</p>
<dd>Start booth arbitrator service.</p>
<dt>stop</p>
<dd>Stop booth arbitrator service.</dl>
<h3>status</h3>
<dl>
<dt>[status] [<code>&#8211;full</code> | <code>&#8211;hide-inactive</code>]</p>
<dd>View all information about the cluster and resources (<code>&#8211;full</code> provides more details, <code>&#8211;hide-inactive</code> hides inactive resources).</p>
<dt>resources [&lt;resource id&gt; | <code>&#8211;full</code> | <code>&#8211;groups</code> | <code>&#8211;hide-inactive</code>]</p>
<dd>Show all currently configured resources or if a resource is specified show the options for the configured resource. If <code>&#8211;full</code> is specified, all configured resource options will be displayed. If <code>&#8211;groups</code> is specified, only show groups (and their resources). If <code>&#8211;hide-inactive</code> is specified, only show active resources.</p>
<dt>groups</p>
<dd>View currently configured groups and their resources.</p>
<dt>cluster</p>
<dd>View current cluster status.</p>
<dt>corosync</p>
<dd>View current membership information as seen by corosync.</p>
<dt>quorum</p>
<dd>View current quorum status.</p>
<dt>qdevice &lt;device model&gt; [<code>&#8211;full</code>] [&lt;cluster name&gt;]</p>
<dd>Show runtime status of specified model of quorum device provider. Using <code>&#8211;full</code> will give more detailed output. If &lt;cluster name&gt; is specified, only information about the specified cluster will be displayed.</p>
<dt>nodes [corosync|both|config]</p>
<dd>View current status of nodes from pacemaker. If &#8216;corosync&#8217; is specified, print nodes currently configured in corosync, if &#8216;both&#8217; is specified, print nodes from both corosync &amp; pacemaker. If &#8216;config&#8217; is specified, print nodes from corosync &amp; pacemaker configuration.</p>
<dt>pcsd [&lt;node&gt;] &#8230;</p>
<dd>Show the current status of pcsd on the specified nodes. When no nodes are specified, status of all nodes is displayed.</p>
<dt>xml</p>
<dd>View xml version of status (output from crm_mon <code>-r</code> <code>-1</code> <code>-X</code>).</dl>
<h3>config</h3>
<dl>
<dt>[show]</p>
<dd>View full cluster configuration.</p>
<dt>backup [filename]</p>
<dd>Creates the tarball containing the cluster configuration files. If filename is not specified the standard output will be used.</p>
<dt>restore [<code>&#8211;local</code>] [filename]</p>
<dd>Restores the cluster configuration files on all nodes from the backup. If filename is not specified the standard input will be used. If <code>&#8211;local</code> is specified only the files on the current node will be restored.</p>
<dt>checkpoint</p>
<dd>List all available configuration checkpoints.</p>
<dt>checkpoint view &lt;checkpoint_number&gt;</p>
<dd>Show specified configuration checkpoint.</p>
<dt>checkpoint restore &lt;checkpoint_number&gt;</p>
<dd>Restore cluster configuration to specified checkpoint.</p>
<dt>import-cman output=&lt;filename&gt; [input=&lt;filename&gt;] [<code>&#8211;interactive</code>] [output-format=corosync.conf|cluster.conf] [dist=&lt;dist&gt;]</p>
<dd>Converts RHEL 6 (CMAN) cluster configuration to Pacemaker cluster configuration. Converted configuration will be saved to &#8216;output&#8217; file. To send the configuration to the cluster nodes the &#8216;pcs config restore&#8217; command can be used. If <code>&#8211;interactive</code> is specified you will be prompted to solve incompatibilities manually. If no input is specified /etc/cluster/cluster.conf will be used. You can force to create output containing either cluster.conf or corosync.conf using the output-format option. Optionally you can specify output version by setting &#8216;dist&#8217; option e. g. rhel,6.8 or redhat,7.3 or debian,7 or ubuntu,trusty. You can get the list of supported dist values by running the &quot;clufter <code>&#8211;list-dists</code>&quot; command. If &#8216;dist&#8217; is not specified, it defaults to this node&#8217;s version if that matches output-format, otherwise redhat,6.7 is used for cluster.conf and redhat,7.1 is used for corosync.conf.</p>
<dt>import-cman output=&lt;filename&gt; [input=&lt;filename&gt;] [<code>&#8211;interactive</code>] output-format=pcs-commands|pcs-commands-verbose [dist=&lt;dist&gt;]</p>
<dd>Converts RHEL 6 (CMAN) cluster configuration to a list of pcs commands which recreates the same cluster as Pacemaker cluster when executed. Commands will be saved to &#8216;output&#8217; file. For other options see above.</p>
<dt>export pcs-commands|pcs-commands-verbose [output=&lt;filename&gt;] [dist=&lt;dist&gt;]</p>
<dd>Creates a list of pcs commands which upon execution recreates the current cluster running on this node. Commands will be saved to &#8216;output&#8217; file or written to stdout if &#8216;output&#8217; is not specified. Use pcs-commands to get a simple list of commands, whereas pcs-commands-verbose creates a list including comments and debug messages. Optionally specify output version by setting &#8216;dist&#8217; option e. g. rhel,6.8 or redhat,7.3 or debian,7 or ubuntu,trusty. You can get the list of supported dist values by running the &quot;clufter <code>&#8211;list-dists</code>&quot; command. If &#8216;dist&#8217; is not specified, it defaults to this node&#8217;s version.</dl>
<h3>pcsd</h3>
<dl>
<dt>certkey &lt;certificate file&gt; &lt;key file&gt;</p>
<dd>Load custom certificate and key files for use in pcsd.</p>
<dt>sync-certificates</p>
<dd>Sync pcsd certificates to all nodes found from current corosync.conf file (cluster.conf on systems running Corosync 1.x). WARNING: This will restart pcsd daemon on the nodes.</p>
<dt>clear-auth [<code>&#8211;local</code>] [<code>&#8211;remote</code>]</p>
<dd>Removes all system tokens which allow pcs/pcsd on the current system to authenticate with remote pcs/pcsd instances and vice-versa. After this command is run this node will need to be re-authenticated with other nodes (using &#8216;pcs cluster auth&#8217;). Using <code>&#8211;local</code> only removes tokens used by local pcs (and pcsd if root) to connect to other pcsd instances, using <code>&#8211;remote</code> clears authentication tokens used by remote systems to connect to the local pcsd instance.</dl>
<h3>node</h3>
<dl>
<dt>attribute [[&lt;node&gt;] [<code>&#8211;name</code> &lt;name&gt;] | &lt;node&gt; &lt;name&gt;=&lt;value&gt; &#8230;]</p>
<dd>Manage node attributes. If no parameters are specified, show attributes of all nodes. If one parameter is specified, show attributes of specified node. If <code>&#8211;name</code> is specified, show specified attribute&#8217;s value from all nodes. If more parameters are specified, set attributes of specified node. Attributes can be removed by setting an attribute without a value.</p>
<dt>maintenance [<code>&#8211;all</code>] | [&lt;node&gt;]&#8230;</p>
<dd>Put specified node(s) into maintenance mode, if no node or options are specified the current node will be put into maintenance mode, if <code>&#8211;all</code> is specified all nodes will be put into maintenace mode.</p>
<dt>unmaintenance [<code>&#8211;all</code>] | [&lt;node&gt;]&#8230;</p>
<dd>Remove node(s) from maintenance mode, if no node or options are specified the current node will be removed from maintenance mode, if <code>&#8211;all</code> is specified all nodes will be removed from maintenance mode.</p>
<dt>standby [<code>&#8211;all</code> | &lt;node&gt;] [<code>&#8211;wait</code>[=n]]</p>
<dd>Put specified node into standby mode (the node specified will no longer be able to host resources), if no node or options are specified the current node will be put into standby mode, if <code>&#8211;all</code> is specified all nodes will be put into standby mode. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the node(s) to be put into standby mode and then return 0 on success or 1 if the operation not succeeded yet. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>unstandby [<code>&#8211;all</code> | &lt;node&gt;] [<code>&#8211;wait</code>[=n]]</p>
<dd>Remove node from standby mode (the node specified will now be able to host resources), if no node or options are specified the current node will be removed from standby mode, if <code>&#8211;all</code> is specified all nodes will be removed from standby mode. If <code>&#8211;wait</code> is specified, pcs will wait up to &#8216;n&#8217; seconds for the node(s) to be removed from standby mode and then return 0 on success or 1 if the operation not succeeded yet. If &#8216;n&#8217; is not specified it defaults to 60 minutes.</p>
<dt>utilization [[&lt;node&gt;] [<code>&#8211;name</code> &lt;name&gt;] | &lt;node&gt; &lt;name&gt;=&lt;value&gt; &#8230;]</p>
<dd>Add specified utilization options to specified node. If node is not specified, shows utilization of all nodes. If <code>&#8211;name</code> is specified, shows specified utilization value from all nodes. If utilization options are not specified, shows utilization of specified node. Utilization option should be in format name=value, value has to be integer. Options may be removed by setting an option without a value. Example: pcs node utilization node1 cpu=4 ram=</dl>
<h3>alert</h3>
<dl>
<dt>[config|show]</p>
<dd>Show all configured alerts.</p>
<dt>create path=&lt;path&gt; [id=&lt;alert-id&gt;] [description=&lt;description&gt;] [options [&lt;option&gt;=&lt;value&gt;]&#8230;] [meta [&lt;meta-option&gt;=&lt;value&gt;]&#8230;]</p>
<dd>Define an alert handler with specified path. Id will be automatically generated if it is not specified.</p>
<dt>update &lt;alert-id&gt; [path=&lt;path&gt;] [description=&lt;description&gt;] [options [&lt;option&gt;=&lt;value&gt;]&#8230;] [meta [&lt;meta-option&gt;=&lt;value&gt;]&#8230;]</p>
<dd>Update existing alert handler with specified id.</p>
<dt>remove &lt;alert-id&gt;</p>
<dd>Remove alert handler with specified id.</p>
<dt>recipient add &lt;alert-id&gt; value=&lt;recipient-value&gt; [id=&lt;recipient-id&gt;] [description=&lt;description&gt;] [options [&lt;option&gt;=&lt;value&gt;]&#8230;] [meta [&lt;meta-option&gt;=&lt;value&gt;]&#8230;]</p>
<dd>Add new recipient to specified alert handler.</p>
<dt>recipient update &lt;recipient-id&gt; [value=&lt;recipient-value&gt;] [description=&lt;description&gt;] [options [&lt;option&gt;=&lt;value&gt;]&#8230;] [meta [&lt;meta-option&gt;=&lt;value&gt;]&#8230;]</p>
<dd>Update existing recipient identified by it&#8217;s id.</p>
<dt>recipient remove &lt;recipient-id&gt;</p>
<dd>Remove specified recipient.</dl>
<h2>Examples</h2>
<dl>
<dt>Show all resources</p>
<dd><code># pcs resource show</code></p>
<dt>Show options specific to the &#8216;VirtualIP&#8217; resource</p>
<dd><code># pcs resource show VirtualIP</code></p>
<dt>Create a new resource called &#8216;VirtualIP&#8217; with options</p>
<dd><code># pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.0.99 cidr_netmask=32 nic=eth2 op monitor interval=30s</code></p>
<dt>Create a new resource called &#8216;VirtualIP&#8217; with options</p>
<dd><code># pcs resource create VirtualIP IPaddr2 ip=192.168.0.99 cidr_netmask=32 nic=eth2 op monitor interval=30s</code></p>
<dt>Change the ip address of VirtualIP and remove the nic option</p>
<dd><code># pcs resource update VirtualIP ip=192.168.0.98 nic=</code></p>
<dt>Delete the VirtualIP resource</p>
<dd><code># pcs resource delete VirtualIP</code></p>
<dt>Create the MyStonith stonith fence_virt device which can fence host &#8216;f1&#8217;</p>
<dd><code># pcs stonith create MyStonith fence_virt pcmk_host_list=f1</code></p>
<dt>Set the stonith-enabled property to false on the cluster (which disables stonith)</p>
<dd><code># pcs property set stonith-enabled=false</code> </p>
