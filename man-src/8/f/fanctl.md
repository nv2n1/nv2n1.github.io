---
title: "fanctl(8)"
name: "fanctl"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fanctl/"
description: "fanctl – fan bridge administration"
---

<p>fanctl &#8211; fan bridge administration</p>
<h2>Synopsis</h2>
<p><code>fanctl up [&lt;options&gt;&#8230;]</code><br />
 <code>fanctl down [&lt;options&gt;&#8230;]</code><br />
 <code>fanctl up -a</code><br />
 <code>fanctl down -a</code><br />
 <code>fanctl down -e</code><br />
 <code>fanctl show</code><br />
 <code>fanctl help</code></p>
<h2>Description</h2>
<p><code>fanctl</code> is used to set up, tear down, and inspect Fan bridge mappings and devices in the linux kernel.</p>
<dl>
<dt><code>NOTE:</code></p>
<dd>Future versions of the commands will make <code>fanatic</code> the primary interface for interacting with Fan networks. For maximum portability <code>fanctl</code> should only be used if absolutely necessary.</dl>
<p> A network Fan is a mechanism for expanding the range of IP addresses available to a system. It is most useful for containers such as Docker and LXC/LXD, but it can be used in other contexts as well. Fan works by creating a bridge that uses a mathematical mapping between the host&#8217;s (or underlay&#8217;s) /16 address and the Fan&#8217;s (or overlay&#8217;s) /8 address. By mapping addresses in this way, a 253-fold increase in address space can be achieved. For example, if the host machine uses a subnet of 172.16.0.0/16 and assigns a 250.0.0.0/8 Fan to an IP address of 172.16.3.4, the hosts&#8217;s Fan overlay addresses will be in the 250.3.4.0/24 subnet, where 250 is derived from the user defined overlay network prefix.</p>
<h2>Command Syntax</h2>
<dl>
<dt><code>fanctl up -u &lt;underlay&gt; -o &lt;overlay&gt; [&lt;options&gt;]</code></p>
<dd>Sets up a new Fan bridge mapping <code>overlay</code> addresses to the corresponding <code>underlay</code> addresses on the local network. Using the example, the new bridge is named <i>fan-250</i> based on the overlay and underlay addresses specified (see ADDRESSING below). The <code>options</code> are described in the OPTIONS section below.</p>
<dt><code>fanctl down -u &lt;underlay&gt; -o &lt;overlay&gt;</code></p>
<dd>Tears down a previously-configured Fan bridge and associated mapping. This action will fail if the bridge is still in use.</p>
<dt><code>fanctl up -a</code></p>
<dd>Sets up all Fans defined in /etc/network/fan if present.</p>
<dt><code>fanctl down -a</code></p>
<dd>Tears down all automatically defined Fan bridges on the system. These may be identified in the <i>fanctl show</i> output via the <i>auto</i> flag.</p>
<dt><code>fanctl down -e</code></p>
<dd>Tears down all defined Fan bridges on the system.</p>
<dt><code>fanctl show</code></p>
<dd>Lists all currently defined Fan bridges in the system; for instance:</dl>
<pre><dl><dt><dd># fanctl show
Bridge Underlay Overlay Flags
fan-250 172.16.3.4/16 250.0.0.0/8 dhcp host-reserve 1
</dl></pre>
<dl>
<dt><code>fanctl config set -u &lt;underlay&gt; -o &lt;overlay&gt; [&lt;options&gt;&#8230;]</code></p>
<dd>Sets configuration options for the underlay/overlay combination specified (or clears any individual configuration if no options are specified).<br />
 To add options, the current set of options has to be obtained via <code>fanctl config show</code> and added to the list of new options.</p>
<dt><code>fanctl config show -u &lt;underlay&gt; -o &lt;overlay&gt;</code></p>
<dd>Displays any additional configuration options for the underlay/overlay combination specified.</p>
<dt><code>fanctl config list</code></p>
<dd>Displays all underlay/overlay combinations which have additional configuration.</p>
<dt><code>fanctl help [&lt;command&gt;]</code></p>
<dd>Displays basic usage information for <code>fanctl</code>. When used with a specific command limits output to that command.</dl>
<h2>Addressing</h2>
<p>The Fan mapping is defined by a combination of the <code>underlay</code> and <code>overlay</code> addresses. Each is defined as a CIDR network address. For example: </p>
<pre><dl><dt><dd># fanctl up -u 172.16.3.4/16 -o 250.0.0.0/8
</dl></pre>
<p>This example defines an overlay of <i>250.0.0.0/8</i> and an underlay of <i>172.16.3.4/16</i>. When mapping an address in the 250.0.0.0/8 subnet, we take the 16 bits of destination address starting at bit 8 and replace the bottom 16 bits of the underlay address with it. For example, attempting to talk to 250.3.4.15 will trigger the packet to be sent to 172.16.3.4 for delivery. </p>
<p> It is not always possible to know the local underlay address at the time the configuration is generated (such as when a common configuration is desired on all systems). In this case we can specify the underlay address using only the underlay prefix, or by reference to an interface. </p>
<p> For example, to bring up a Fan bridge slice for each address in the 172.16.0.0/16 subnet, the following example examines each interface as it is currently configured and configures a matching slice at that time: </p>
<pre><dl><dt><dd># fanctl up -u 172.16.0.0/16 -o 250.0.0.0/8
</dl></pre>
<p>To bring up Fan slices corresponding to the addresses on a specific interface we can substitute the interface name: </p>
<pre><dl><dt><dd># fanctl up -u ens3/16 -o 250.0.0.0/8
</dl></pre>
<p>To bring up Fan slices corresponding to the addresses on the primary network interface (the interface with the default route), the keyword <i>default</i> can be substituted: </p>
<pre><dl><dt><dd># fanctl up -u default/16 -o 250.0.0.0/8
</dl></pre>
<h2>Limitations</h2>
<p>Currently Fan can only apply overlay addresses with a /8 network mask, and underlay addresses with a /16 network mask. We expect to relax this limitation in a later update.</p>
<h2>Options</h2>
<dl>
<dt><code>-u &lt;underlay&gt;|&#8211;underlay=&lt;underlay&gt;</code></p>
<dd>Specify the underlay network address and mask.</p>
<dt><code>-o &lt;overlay&gt;|&#8211;overlay=&lt;overlay&gt;</code></p>
<dd>Specify the overlay network address and mask.</p>
<dt><code>&#8211;type=&lt;type&gt;</code></p>
<dd>Sets the encapsulation type for this Fan bridge. May be ipip or vxlan (default) only. You should not normally need to specify this.</p>
<dt><code>&#8211;mode=&lt;mode&gt;</code></p>
<dd>Sets the bridge mode. May be compact (default) or sliced only. In compact mode a single Fan bridge per overlay network is created. In sliced mode a Fan bridge is created for each local Fan slice. sliced mode is considered legacy. You should not normally need to specify this.</p>
<dt><code>&#8211;dhcp</code></p>
<dd>Turns on automatic address allocation for the Fan bridge. A dnsmasq instance is started attached to the bridge allocating the unreserved addresses to entities attached to the Fan bridge.</p>
<dt><code>&#8211;host-reserve=&lt;count&gt;</code></p>
<dd>By default the .1 address on the Fan bridge is allocated to the host, enabling it to communicate with entities on the Fan bridge. This option reserves additional addresses for host applications to use. A <i>host-reserve 4</i> reserves .1 through .4 in the Fan bridge for host use.</p>
<dt><code>&#8211;bridge=&lt;name&gt;</code></p>
<dd>By default the bridge name is based on the overlay and underlay addresses specified (see ADDRESSING above). This option overrides the name to one you specify.</p>
<dt><code>&#8211;enable</code></p>
<dd>This option marks the Fan bridge to be automatically configured when the underlying interface comes up. This is primarily used in the local Fan persistent configuration to enable centrally configured Fan mappings on a specific host. (See PERSISTENT CONFIGURATION below).</dl>
<h2>Persistent Configuration</h2>
<p><code>NOTE:</code> The location and content of the configuration files should still be considered unstable as they could change in future. Use of <code>fanatic</code> is highly recommended as this command will make any necessary changes to the right config files. </p>
<p> Fan mappings are configured via <i>/etc/network/fan</i> by pairs of local (underlay) and overlay network addresses. The first element of each pair specifies the underlay range which should be mapped into the overlay network specified by the second element. For example: </p>
<pre><dl><dt><dd># RFC1918 - we recommend you use these for easy interop with
# other FAN users on small private networks. They provide
# around 250 IP's per 192.168.0.0/16 address, or 16 per
# 172.16.0.0/12 address.
# local overlay
192.168.0.0/16 250.0.0.0/8
172.16.0.0/12 251.0.0.0/8
</dl></pre>
<p>Comments are introduced via a hash (#), and blank lines are ignored. </p>
<p> Note, that the local (underlay) range does not need to match the subnet mask of the interface as long as all addresses of the larger scope are routeable. If for example the interface is configured as 192.168.122.2/24 but can reach all 192.168.0.0/16 addresses that will be part of the Fan network, the local (underlay) address of 192.168.0.0/16 can be used regardless. </p>
<p> It is expected that the <i>/etc/network/fan</i> configuration is globally managed ensuring that all hosts have consistent overlay to underlay mappings. Local deviation is managed via the <code>fanctl config</code> subcommand. This allow a local host to record additional flags against a specific overlay/underlay combination. For example: </p>
<pre><dl><dt><dd># fanctl config set -u 172.16.0.0/16 -o 250.0.0.0/8 --enable
</dl></pre>
<p>will set the <code>&#8211;enable</code> option to the local host configuration, triggering this Fan to be configured when the host interface is configured.</p>
<h2>Fan Bridges</h2>
<p>By default each Fan bridge represents a Fan overlay network which is expressed locally on the machine. The Fan bridge will have the various slice addresses mapped to it. </p>
<p> In legacy sliced mode each Fan bridge represents a slice of a Fan overlay network which is expressed locally on the machine. The Fan bridge will have the overlay addresses representing one local IP address mapped to it. A machine may have more than one local address on the underlay network, enabling it to have more than one such slice mapped. It may also have more than one overlay range defined for each local IP address. </p>
<p> Each Fan bridge is a separate broadcast domain, with routing between the bridges both locally and globally within the Fan. </p>
<p> Each Fan bridge appears as a bridge on the system, named for the overlay subnet hosted by that particular Fan bridge and the underlay address prefix for which it carries traffic. For our <i>250.0.0.0/8</i> on <i>172.16.3.4</i> example, the bridge would be named <i>fan-250</i> and would carry all traffic for <i>250.3.4.0/24</i>.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-fanatic/">fanatic</a></i>(8), <code>/usr/share/doc/ubuntu-fan/README</code></p>
<h2>AUTHOR(s)</h2>
<p>Andy Whitcroft &lt;apw [at] canonical.com&gt;,<br />
 Stefan Bader &lt;stefan.bader [at] canonical.com&gt;</p>
