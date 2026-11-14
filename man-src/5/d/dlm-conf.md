---
title: "dlm-conf(5)"
name: "dlm-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dlm-conf/"
description: "dlm.conf – dlm_controld configuration file"
---

<p>dlm.conf &#8211; dlm_controld configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/dlm/dlm.conf</code> </p>
<h2>Description</h2>
<p>The configuration options in dlm.conf mirror the dlm_controld command line options. The config file additionally allows advanced fencing and lockspace configuration that are not supported on the command line. </p>
<h2>Command line equivalents</h2>
<p>If an option is specified on the command line and in the config file, the command line setting overrides the config file setting. See <code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8) for descriptions and dlm_controld -h for defaults. </p>
<p> Format: </p>
<p> key=val </p>
<p> Example: </p>
<p> log_debug=1<br />
 post_join_delay=10<br />
 protocol=tcp </p>
<p> Options: </p>
<p> daemon_debug<br />
 log_debug<br />
 protocol<br />
 debug_logfile<br />
 enable_plock<br />
 plock_debug<br />
 plock_rate_limit<br />
 plock_ownership<br />
 drop_resources_time<br />
 drop_resources_count<br />
 drop_resources_age<br />
 post_join_delay<br />
 enable_fencing<br />
 enable_concurrent_fencing<br />
 enable_startup_fencing<br />
 enable_quorum_fencing<br />
 enable_quorum_lockspace</p>
<h2>Fencing</h2>
<p>A fence device definition begins with a <code>device</code> line, followed by a number of <code>connect</code> lines, one for each node connected to the device. </p>
<p> A blank line separates device definitions. </p>
<p> Devices are used in the order they are listed. </p>
<p> The <code>device</code> key word is followed by a unique <i>dev_name</i>, the <i>agent</i> program to be used, and <i>args</i>, which are agent arguments specific to the device. </p>
<p> The <code>connect</code> key word is followed by the <i>dev_name</i> of the device section, the node ID of the connected node in the format <code>node=</code><i>nodeid</i> and <i>args</i>, which are agent arguments specific to the node for the given device. </p>
<p> The format of <i>args</i> is key=val on both device and connect lines, each pair separated by a space, e.g. key1=val1 key2=val2 key3=val3. </p>
<p> Format: </p>
<p> <code>device</code> <i> dev_name</i> <i>agent</i> [args]<br />
 <code>connect</code> <i>dev_name</i> <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i> <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i> <code>node=</code><i>nodeid</i> [args] </p>
<p> Example: </p>
<p> device foo fence_foo ipaddr=1.1.1.1 login=x password=y<br />
 connect foo node=1 port=1<br />
 connect foo node=2 port=2<br />
 connect foo node=3 port=3 </p>
<p> device bar fence_bar ipaddr=2.2.2.2 login=x password=y<br />
 connect bar node=1 port=1<br />
 connect bar node=2 port=2<br />
 connect bar node=3 port=3</p>
<h3>Parallel devices</h3>
<p>Some devices, like dual power or dual path, must all be turned off in parallel for fencing to succeed. To define multiple devices as being parallel to each other, use the same base dev_name with different suffixes and a colon separator between base name and suffix. </p>
<p> Format: </p>
<p> <code>device</code> <i> dev_name</i>:1 <i>agent</i> [args]<br />
 <code>connect</code> <i>dev_name</i>:1 <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i>:1 <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i>:1 <code>node=</code><i>nodeid</i> [args] </p>
<p> <code>device</code> <i> dev_name</i>:2 <i>agent</i> [args]<br />
 <code>connect</code> <i>dev_name</i>:2 <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i>:2 <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i>:2 <code>node=</code><i>nodeid</i> [args] </p>
<p> Example: </p>
<p> device foo:1 fence_foo ipaddr=1.1.1.1 login=x password=y<br />
 connect foo:1 node=1 port=1<br />
 connect foo:2 node=2 port=2<br />
 connect foo:3 node=3 port=3 </p>
<p> device foo:2 fence_foo ipaddr=5.5.5.5 login=x password=y<br />
 connect foo:2 node=1 port=1<br />
 connect foo:2 node=2 port=2<br />
 connect foo:2 node=3 port=3</p>
<h3>Unfencing</h3>
<p>A node may sometimes need to &quot;unfence&quot; itself when starting. The unfencing command reverses the effect of a previous fencing operation against it. An example would be fencing that disables a port on a SAN switch. A node could use unfencing to re-enable its switch port when starting up after rebooting. (Care must be taken to ensure it&#8217;s safe for a node to unfence itself. A node often needs to be cleanly rebooted before unfencing itself.) </p>
<p> To specify that a node should unfence itself for a given <code>device,</code> the <code>unfence</code> line is added after the <code>connect</code> lines. </p>
<p> Format: </p>
<p> <code>device</code> <i> dev_name</i> <i>agent</i> [args]<br />
 <code>connect</code> <i>dev_name</i> <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i> <code>node=</code><i>nodeid</i> [args]<br />
 <code>connect</code> <i>dev_name</i> <code>node=</code><i>nodeid</i> [args]<br />
 <code>unfence </code><i>dev_name</i> </p>
<p> Example: </p>
<p> device foo fence_foo ipaddr=1.1.1.1 login=x password=y<br />
 connect foo node=1 port=1<br />
 connect foo node=2 port=2<br />
 connect foo node=3 port=3<br />
 unfence foo</p>
<h3>Simple devices</h3>
<p>In some cases, a single fence device is used for all nodes, and it requires no node-specific args. This would typically be a &quot;bridge&quot; fence device in which an agent is passing a fence request to another subsystem to handle. (Note that a &quot;node=nodeid&quot; arg is always automatically included in agent args, so a node-specific nodeid is always present to minimally identify the victim.) </p>
<p> In such a case, a simplified, single-line fence configuration is possible, with format: </p>
<p> <code>fence_all</code> <i>agent</i> [args] </p>
<p> Example: </p>
<p> fence_all dlm_stonith </p>
<p> A fence_all configuration is not compatible with a fence device configuration (above). </p>
<p> Unfencing can optionally be applied with: </p>
<p> <code>fence_all</code> <i>agent</i> [args]<br />
 <code>unfence_all</code></p>
<h2>Lockspace configuration</h2>
<p>A lockspace definition begins with a <code>lockspace</code> line, followed by a number of <code>master</code> lines. A blank line separates lockspace definitions. </p>
<p> Format: </p>
<p> <code>lockspace</code> <i>ls_name</i> [ls_args]<br />
 <code>master</code> <i> ls_name</i> <code>node=</code><i>nodeid</i> [node_args]<br />
 <code>master</code> <i> ls_name</i> <code>node=</code><i>nodeid</i> [node_args]<br />
 <code>master</code> <i> ls_name</i> <code>node=</code><i>nodeid</i> [node_args]</p>
<h3>Disabling resource directory</h3>
<p>Lockspaces usually use a resource directory to keep track of which node is the master of each resource. The dlm can operate without the resource directory, though, by statically assigning the master of a resource using a hash of the resource name. To enable, set the per-lockspace <code>nodir</code> option to 1. </p>
<p> Example: </p>
<p> lockspace foo nodir=1</p>
<h3>Lock-server configuration</h3>
<p>The nodir setting can be combined with node weights to create a configuration where select node(s) are the master of all resources/locks. These master nodes can be viewed as &quot;lock servers&quot; for the other nodes. </p>
<p> Example of nodeid 1 as master of all resources: </p>
<p> lockspace foo nodir=1<br />
 master foo node=1 </p>
<p> Example of nodeid&#8217;s 1 and 2 as masters of all resources: </p>
<p> lockspace foo nodir=1<br />
 master foo node=1<br />
 master foo node=2 </p>
<p> Lock management will be partitioned among the available masters. There can be any number of masters defined. The designated master nodes will master all resources/locks (according to the resource name hash). When no masters are members of the lockspace, then the nodes revert to the common fully-distributed configuration. Recovery is faster, with little disruption, when a non-master node joins/leaves. </p>
<p> There is no special mode in the dlm for this lock server configuration, it&#8217;s just a natural consequence of combining the &quot;nodir&quot; option with node weights. When a lockspace has master nodes defined, the master has a default weight of 1 and all non-master nodes have weight of 0. An explicit non-zero <code>weight</code> can also be assigned to master nodes, e.g. </p>
<p> lockspace foo nodir=1<br />
 master foo node=1 weight=2<br />
 master foo node=2 weight=1 </p>
<p> In which case node 1 will master 2/3 of the total resources and node 2 will master the other 1/3.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8), <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8) </p>
