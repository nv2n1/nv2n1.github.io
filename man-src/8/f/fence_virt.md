---
title: "fence_virt(8)"
name: "fence_virt"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_virt/"
description: "fence_virt – Fencing agent for virtual machines using VM Channel"
---

<p>fence_virt &#8211; Fencing agent for virtual machines using VM Channel </p>
<p> fence_xvm &#8211; Fencing agent for virtual machines using multicast</p>
<h2>Description</h2>
<p>fence_virt and fence_xvm are an I/O Fencing agents which can be used with virtual machines. Fence_xvm is backward compatible with fence_xvmd. Fence_virt and fence_xvm talk to fence_virtd, which supports multiple backend plugins, including:<br/>
&nbsp;<wbr>&#8211; libvirt for single-node operation<br/>
&nbsp;<wbr>&#8211; Cluster Checkpoints when using Linux-cluster release 3.0.0 or later<br/>
&nbsp;<wbr>&#8211; libvirt-qpid for multi-node, non-cluster operation For compatibility, fence_xvm may talk to fence_xvmd from linux-cluster release 2 or later. fence_virt and fence_xvm accept options on the command line as well as from stdin. The fencing daemon sends parameters through stdin when it execs the agent. The agent may be run by itself with command line options, which is useful for testing or turning on or off virtual machines from scripts. </p>
<h2>General Parameters</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>-d</code></dt>
<dd>Increment (command line) debug level <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-H</code></dt>
<dd>Virtual machine (domain UUID or name) to fence </dd>
<dt><code>-o</code></dt>
<dd>Fencing action (null, off, on, reboot, status, monitor, list, or metadata) (Default Value: reboot). See the FENCING ACTIONS section. </dd>
<dt><code>-t</code></dt>
<dd>Fencing timeout (in seconds) (Default Value: 30) </dd>
<dt><code>-w</code></dt>
<dd>Fencing delay (in seconds). The fence agent will wait the specified number of seconds before attempting a fencing operation. (Default Value: 0) </dd>
</dl>
<h2>Multicast Parameters</h2>
<p>These parameters are used only when using fence_virt in multicast mode (e.g. by running fence_xvm). </p>
<dl>
<dt><code>-i</code></dt>
<dd>IP Family (auto, ipv4, ipv6) (Default Value: auto) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-a</code></dt>
<dd>Multicast address (Default Values: 225.0.0.12 / ff02::3:1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-p</code></dt>
<dd>IP port (Default Value: 1229) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-T</code></dt>
<dd>Multicast time-to-live (in hops) (Default Value: 2) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-r</code></dt>
<dd>Multicast retransmit time (in 1/10sec) (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-C</code></dt>
<dd>Authentication (none, sha1, sha256, sha512) (Default Value: sha256) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-c</code></dt>
<dd>Packet hash strength (none, sha1, sha256, sha512) (Default Value: sha256) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-k</code></dt>
<dd>Shared key file (Default Value: /etc/cluster/fence_xvm.key) </dd>
<dt><code>-u</code></dt>
<dd>Specify if using fence_virt with older fence_xvmd installations which are using UUIDs. Fence_virtd ignores this parameter. </dd>
</dl>
<h2>Serial/Vmchannel Parameters</h2>
<p>These parameters are used only when using fence_virt in serial mode (e.g. by running fence_virt). </p>
<dl>
<dt><code>-D</code></dt>
<dd>Serial device (fence_virt mode). On the host, the serial device must be mapped in each domain&#8217;s configuration file. See <a href="/docs/linux/man/5-fence_virt-conf/">fence_virt.conf</a>(5) for more information. Specifying a serial device causes fence_virt to use serial mode (as opposed to VMChannel mode). </dd>
<dt><code>-P</code></dt>
<dd>Serial parameters. (Default Value: 115200,8N1) </dd>
<dt><code>-A</code></dt>
<dd>VMChannel IP address (Default Value: 10.0.2.179) </dd>
<dt><code>-p</code></dt>
<dd>VMChannel IP port (Default Value: 1229) </dd>
</dl>
<h2>General Stdin Parameters</h2>
<p>These parameters are passed to fence_virt via standard input if no command line options are present. They are presented to fence_virt in the form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>name=value <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>debug</code></dt>
<dd>Specify debugging level </dd>
<dt><code>port</code></dt>
<dd>Virtual machine (domain UUID or name) to fence </dd>
<dt><code>action</code></dt>
<dd>Fencing action (null, off, on, reboot, status, monitor, list, or metadata) (Default Value: reboot). See the FENCING ACTIONS section. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>timeout</code></dt>
<dd>Fencing timeout (in seconds) (Default Value: 30) </dd>
</dl>
<h2>Multicast Stdin Parameters</h2>
<dl>
<dt><code>ip_family</code></dt>
<dd>IP Family ([auto], ipv4, ipv6) (Default Value: auto) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>multicast_address</code></dt>
<dd>Multicast address (Defaults: 225.0.0.12 / ff02::3:1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>port</code></dt>
<dd>IP port (Default Value: 1229) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>multicast_ttl</code></dt>
<dd>Multicast time-to-live (in hops) (Default Value: 2) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>retrans</code></dt>
<dd>Multicast retransmit time (in 1/10sec) (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>auth</code></dt>
<dd>Authentication (none, sha1, sha256, sha512) (Default Value: sha256) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>hash</code></dt>
<dd>Packet hash strength (none, sha1, sha256, sha512) (Default Value: sha256) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>key_file</code></dt>
<dd>Shared key file (Default Value: /etc/cluster/fence_xvm.key) </dd>
<dt><code>use_uuid</code></dt>
<dd>Specify if using fence_virt with older fence_xvmd installations which are using UUIDs. Fence_virtd ignores this parameter. </dd>
</dl>
<h2>Serial/Vmchannel Stdin Parameters</h2>
<dl>
<dt><code>serial_device</code></dt>
<dd>Serial device. On the host, the serial device must be mapped in each domain&#8217;s configuration file. See <a href="/docs/linux/man/5-fence_virt-conf/">fence_virt.conf</a>(5) for more information. If specified, causes fence_virt to operate in serial mode (not specifying causes fence_virt to operate in VM Channel mode). </dd>
<dt><code>serial_params</code></dt>
<dd>Serial parameters. Default=115200,8N1. </dd>
<dt><code>channel_ip</code></dt>
<dd>Channel IP. Default=10.0.2.179 </dd>
<dt><code>ipport</code></dt>
<dd>Channel port. Default=1229 </dd>
</dl>
<h2>Fencing Actions</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>off </code></dt>
<dd>&nbsp;<wbr>Destroy or turn off virtual machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>reboot </code></dt>
<dd>Reboot virtual machine; i.e. restart the virtual machine on the same host where it is currently running. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>on </code></dt>
<dd>Turn on a virtual machine. Note: Turning on a virtual machine only works with some fence_virt backends. </dd>
<dt><code>status </code></dt>
<dd>Check whether a virtual machine is running or not. </dd>
<dt><code>monitor </code></dt>
<dd>Check the health of fence_virtd&#8217;s backend plugin. </dd>
<dt><code>list </code></dt>
<dd>List virtual machines which may be fenced by fence_virtd (not supported on all backends). </dd>
<dt><code>metadata </code></dt>
<dd>Print XML metadata to standard output. </dd>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence_virtd/">fence_virtd</a>(8), fence(8), fence_virtd.conf(5) </p>
