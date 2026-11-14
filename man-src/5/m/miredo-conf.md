---
title: "miredo-conf(5)"
name: "miredo-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-miredo-conf/"
description: "miredo.conf – configuration for Miredo"
---

<p>miredo.conf &#8211; configuration for Miredo</p>
<h2>Synopsis</h2>
<p><code>miredo.conf</code> </p>
<h2>Descripton</h2>
<p><i>miredo.conf</i> is the configuration file for <code>Miredo</code>. Each configuration directive consists of one directive name, possibly followed by one or several spaces and a value for the directive. White spaces, empty lines and lines starting with &#8216;#&#8217; are ignored. </p>
<p> Directives are case-insensitive. A comprehensive list of the supported directives follows:</p>
<h2>Modes</h2>
<dl>
<dt><code>RelayType</code> (<code>client</code>|<code>autoclient</code>|<code>relay</code>|<code>cone</code>|<code>restricted</code>)</p>
<dd>Specifies what type of Teredo relay/client Miredo will serve as. There are three possible choices: </p>
<dt><code>client</code> mode (the default)</p>
<dd>In <code>client</code> mode, <code>Miredo</code> acts as a <i>Teredo client</i>. Miredo will first authenticate with a <i>Teredo server</i> (see <code>ServerAddress</code>), and if successful, will setup a Teredo tunneling interface with a public Teredo IPv6 address and a default IPv6 route. That virtual networking interface can be used to reach the IPv6 Internet as well as Teredo clients. </p>
<p> The use of Miredo as a Teredo client allows nodes to get an IPv6 connectivity from behind a NAT router device, as it tunnels IPv6 packets over UDP/IPv4 with special support for NAT routers. Routers of that kind usually only forward TCP, UDP, and some ICMP, IPv4 packets (with some limitation). </p>
<p> <code>NOTE:</code> Use of <code>Miredo</code> as a <i>Teredo client</i> is possible even if the system already has IPv6 connectivity through another way (native, 6to4, TSP, etc). In that case, Miredo will only be used to reach other Teredo clients, as its tunneling interface has a default route with a higher metric (which is to say a lower priority) than the other network interfaces. </p>
<dt><code>autoclient</code> is currently an alias for <code>client</code> mode.</p>
<dd>
<dt><code>cone</code> mode (<code>relay</code> also works)</p>
<dd>In <code>cone</code> mode, <code>Miredo</code> acts as a <i>Teredo relay</i>. It will assume that it has public global <i>IPv4</i> connectivity with no firewall. In other words, the UDP port used by Miredo must receive unsoliticited traffic from the IPv4 Internet (see also <code>BindPort</code>). Miredo will create a virtual networking interface with a route toward Teredo clients. </p>
<p> <i>Teredo relays</i> forward IPv6 packets between <i>Teredo clients</i> and the IPv6 Internet. For that to work, Teredo relays <code>MUST</code> have a working IPv6 connectivity through a way distinct from Teredo tunneling (native, 6to4, ISATAP, etc). </p>
<p> <code>Warning:</code> This mode should only be used if the node has a public IPv4 address, or if it is behind a full cone NAT-router with proper port forwarding rules. Otherwise the tunnel will <code>NOT WORK PROPERLY</code>. Note that many NAT port forwarding implementations are broken. </p>
<dt><code>restricted</code> mode</p>
<dd>This mode is identical to the cone mode documented above, with the exception that <i>direct Teredo bubbles</i> will be sent. Theoretically (see RFC4380) this permits operation of a Teredo relay from behind a restricted-port NAT. In practice, this makes NAT traversal extremely unreliable. This setting is present for backward syntax compatibility of the miredo.conf file. PLEASE DO NOT USE THIS MODE. </p>
</dl>
<h2>Client Options</h2>
<p>The following directives are only available in <i>(auto)client</i> mode. </p>
<dl>
<dt><code>ServerAddress </code><i>hostname</i></p>
<dd>The <code>ServerAddress</code> directive specifies the hostname or numerical IPv4 address of the <i>Teredo server</i> to use. <i>Teredo clients</i> needs a <i>Teredo server</i> to establish and maintain their IPv6 over UDP/IPv4 tunnel across a NAT device. </p>
<p> This directive <code>MUST</code> be specified when Miredo is in <i>client</i> mode. <i>hostname</i> must resolve to a valid IPv4 address. If it is not present, and no server hostname is specified on the command line when starting miredo either, the program will fail. </p>
<dt><code>ServerAddress2 </code><i>hostname2</i></p>
<dd>Miredo assumes that the secondary Teredo server address equals the primary server address plus one. If that is not the case, this directive must be used. </p>
</dl>
<h2>Relay Options</h2>
<p>The following directives are only available in <i>relay</i> mode. They are not available in <i>(auto)client</i> mode. </p>
<dl>
<dt><code>Prefix </code><i>teredo_prefix</i></p>
<dd>This directive specifies the <code>Teredo prefix</code> which the Teredo relay and/or server will advertise. <i>teredo_prefix</i> must be a valid IPv6 prefix. </p>
<p> The default value is <code>2001:0000::</code>. </p>
<p> <code>Do not use that directive</code> if you don&#8217;t know what you are doing, as it is more than likely to break your Teredo connectivity. That option must not be used when Miredo serves as a Teredo client. </p>
<dt><code>InterfaceMTU </code><i>mtu</i></p>
<dd>This directive overrides the default MTU size of 1280 bytes for the Teredo tunneling interface. It should not be used if the default Teredo prefix is used. </p>
</dl>
<h2>General Options</h2>
<dl>
<dt><code>InterfaceName </code><i>ifname</i></p>
<dd>Specify the name of the Teredo tunneling interface which Miredo will create (&quot;miredo&quot; by default). On some systems, it is not possible to redefine the tunnel name. </p>
<dt><code>BindAddress </code><i>bind_address</i></p>
<dd>Bind the Teredo relay or Teredo client to a specific IPv4 address. By default, it is not bound to any particular IPv4 address. </p>
<p> Use this option if you have trouble with the default value, such as if you have a multi-homed host with equal-cost IPv4 routing, or if you have specific firewalling constraints. </p>
<dt><code>BindPort </code><i>udp_port</i></p>
<dd>Define the UDP (IPv4) port number to be used by the relay or client. By default, the operating system allocates an unused port automatically. </p>
<p> Use this option if you have firewalling constraints which can cause Miredo to fail when not using a fixed predefined port. </p>
<dt><code>SyslogFacility </code><i>facility</i></p>
<dd>Specify which syslog&#8217;s facility is to be used by Miredo for logging. Possible values are: <code>daemon</code> (the default), <code>local0</code>, &#8230; <code>local7</code>, <code>kern</code> and <code>user</code> (see <a href="/docs/linux/man/2-syslog/">syslog</a>(2)). </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-miredo/">miredo</a>(8) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/miredo/">http://www.remlab.net/miredo/</a></p>
