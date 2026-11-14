---
title: "ccs_tool(8)"
name: "ccs_tool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ccs_tool/"
description: "ccs_tool – The tool used to make online updates of CCS config files."
---

<p>ccs_tool &#8211; The tool used to make online updates of CCS config files. </p>
<h2>Synopsis</h2>
<p><code>ccs_tool</code> [<i>OPTION</i>].. &lt;<code>command</code>&gt; </p>
<h2>Description</h2>
<p><code>ccs_tool</code> is part of the Cluster Configuration System (CCS). It is used to make online updates to cluster.conf. It can also be used to upgrade old style (GFS &lt;= 6.0) CCS archives to the new xml cluster.conf format. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Help. Print out the usage.</p>
<dt><code>-V</code></p>
<dd>Print the version information. </p>
<p> sub-commands have their own options, see below for more detail</dl>
<h2>Commands</h2>
<dl>
<dt><code>addnode</code> [options] <i>&lt;node&gt; [&lt;fenceoption=value&gt;]&#8230;</i></p>
<dd>Adds a new node to the cluster configuration file. Fencing device options are specified as key=value pairs (as many as required) and are entered into the configuration file as is. See the documentation for your fencing agent for more details (eg a powerswitch fence device may need to know which port the node is connected to).<br />
 <i>Options:</i><br />
 -v &lt;votes&gt; Number of votes for this node (mandatory)<br />
 -n &lt;nodeid&gt; Node id for this node (optional)<br />
 -i &lt;interface&gt; Network interface to use for this node. Mandatory if the cluster is using multicast as transport. Forbidden if not.<br />
 -m &lt;multicast&gt; Multicast address for cluster. Only allowed on the first node to be added to the file. Subsequent nodes will use either multicast or broadcast depending on the properties of the first node.<br />
 -f &lt;fencedevice&gt; Name of fence device to use for this node. The fence device section must already have been added to the file, probably using the addfence command.<br />
 -c &lt;file&gt; Config file to use. Defaults to /etc/cluster/cluster.conf<br />
 -o &lt;file&gt; Output file. Defaults to the same as -c<br />
 -C Don&#8217;t run &quot;ccs_tool update&quot; after changing file. This will happen by default if the input file is the same as the output file.<br />
 -F Force a &quot;ccs_tool update&quot; even if the input and output files are different. </p>
<dt><code>delnode</code> [options] <i>&lt;node&gt;</i></p>
<dd>Delete a node from the cluster configuration file. Note: there is no &quot;edit&quot; command so to change the properties of a node you must delete it and add it back in with the new properties.<br />
 <i>Options:</i><br />
 -c &lt;file&gt; Config file to use. Defaults to /etc/cluster/cluster.conf<br />
 -o &lt;file&gt; Output file. Defaults to the same as -c<br />
 -C Don&#8217;t run &quot;ccs_tool update&quot; after changing file. This will happen by default if the input file is the same as the output file.<br />
 -F Force a &quot;ccs_tool update&quot; even if the input and output files are different. </p>
<dt><code>addfence</code> [options] <i>&lt;name&gt; &lt;agent&gt; [&lt;option&gt;=&lt;value&gt;]&#8230;</i></p>
<dd>Adds a new fence device section to the cluster configuration file. &lt;agent&gt; is the name of the fence agent that controls the device. the options following are entered as key-value pairs. See the fence agent documentation for details about these. eg: you may need to enter the IP address and username/password for a powerswitch fencing device.<br />
 <i>Options:</i><br />
 -c &lt;file&gt; Config file to use. Defaults to /etc/cluster/cluster.conf<br />
 -o &lt;file&gt; Output file. Defaults to the same as -c<br />
 -C Don&#8217;t run &quot;ccs_tool update&quot; after changing file. This will happen by default if the input file is the same as the output file.<br />
 -F Force a &quot;ccs_tool update&quot; even if the input and output files are different. </p>
<dt><code>delfence</code> [options] <i>&lt;node&gt;</i></p>
<dd>Deletes a fencing device from the cluster configuration file. delfence will allow you to remove a fence device that is in use by nodes. This is to allow changes to be made, but be aware that it may produce an invalid configuration file if you don&#8217;t add it back in again.<br />
 <i>Options:</i><br />
 -c &lt;file&gt; Config file to use. Defaults to /etc/cluster/cluster.conf<br />
 -o &lt;file&gt; Output file. Defaults to the same as -c<br />
 -C Don&#8217;t run &quot;ccs_tool update&quot; after changing file. This will happen by default if the input file is the same as the output file.<br />
 -F Force a &quot;ccs_tool update&quot; even if the input and output files are different. </p>
<dt><code>lsnode [options] </code></p>
<dd>List the nodes in the configuration file. This is (hopefully obviously) not necessarily the same as the nodes currently in the cluster, but it should be a superset.<br />
 <i>Options:</i><br />
 -v Verbose. Lists all the properties of the node, and the node-specific properties of the fence device too.<br />
 -c &lt;file&gt; Config file to use. Defaults to /etc/cluster/cluster.conf </p>
<dt><code>lsfence [options] </code></p>
<dd>List all the fence devices in the cluster configuration file.<br />
 <i>Options:</i><br />
 -v Verbose. Lists all the properties of the fence device rather than just the names and agents.<br />
 -c &lt;file&gt; Config file to use. Defaults to /etc/cluster/cluster.conf </p>
<dt><code>create [options] </code> <i>&lt;clustername&gt;</i></p>
<dd>Create a new, skeleton, configuration file. Note that &quot;create&quot; on its own will not create a valid configuration file. Fence agents and nodes will need to be added to it before handing it over to ccsd. The new configuration file will have a version number of 1. Subsequent addnode/delnode/addfence/delfence operations will increment the version number by 1 each time.<br />
 <i>Options:</i> </p>
<p> -c &lt;file&gt; Config file to create. Defaults to /etc/cluster/cluster.conf </p>
<dt><code>addnodeids</code></p>
<dd>Adds node ID numbers to all the nodes in cluster.conf. In RHEL4, node IDs were optional and assigned by cman when a node joined the cluster. In RHEL5 they must be pre-assigned in cluster.conf. This command will not change any node IDs that are already set in cluster.conf, it will simply add unique node ID numbers to nodes that do not already have them. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a>(5) </p>
