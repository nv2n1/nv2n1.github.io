---
title: "pptpd-conf(5)"
name: "pptpd-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pptpd-conf/"
description: "pptpd.conf – PPTP VPN daemon configuration"
---

<p><code>pptpd.conf</code> &#8211; PPTP VPN daemon configuration</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8) reads options from this file, usually <i>/etc/pptpd.conf</i>. Most options can be overridden by the command line. The local and remote IP addresses for clients must come from the configuration file or from <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) configuration files.</p>
<h2>Options</h2>
<dl>
<dt><code>option </code><i>option-file</i></p>
<dd>the name of an option file to be passed to <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) in place of the default <i>/etc/ppp/options</i> so that PPTP specific options can be given. Equivalent to the command line <code>&#8211;option</code> option. </p>
<dt><code>stimeout </code><i>seconds</i></p>
<dd>number of seconds to wait for a PPTP packet before forking the <code><a href="/docs/linux/man/8-pptpctrl/">pptpctrl</a></code>(8) program to handle the client. The default is 10 seconds. This is a denial of service protection feature. Equivalent to the command line <code>&#8211;stimeout</code> option.</p>
<dt><code>logwtmp</code></p>
<dd>update <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5) as users connect and disconnect. See <code><a href="/docs/linux/man/1-wtmp/">wtmp</a></code>(1).</p>
<dt><code>debug</code></p>
<dd>turns on debugging mode, sending debugging information to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). Has no effect on <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) debugging. Equivalent to the command line <code>&#8211;debug</code> option.</p>
<dt><code>bcrelay </code><i>internal-interface</i></p>
<dd>turns on broadcast relay mode, sending all broadcasts received on the server&#8217;s internal interface to the clients. Equivalent to the command line <code>&#8211;bcrelay</code> option. </p>
<dt><code>connections </code><i>n</i></p>
<dd>limits the number of client connections that may be accepted. If pptpd is allocating IP addresses (e.g. <code>delegate</code> is not used) then the number of connections is also limited by the <code>remoteip</code> option. The default is 100. </p>
<dt><code>delegate</code></p>
<dd>delegates the allocation of client IP addresses to <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8). Without this option, which is the default, pptpd manages the list of IP addresses for clients and passes the next free address to pppd. With this option, pptpd does not pass an address, and so pppd may use radius or chap-secrets to allocate an address. </p>
<dt><code>localip </code><i>ip-specification</i></p>
<dd>one or many IP addresses to be used at the local end of the tunnelled PPP links between the server and the client. If one address only is given, this address is used for all clients. Otherwise, one address per client must be given, and if there are no free addresses then any new clients will be refused. <code>localip</code> will be ignored if the <code>delegate</code> option is used.</p>
<dt><code>remoteip </code><i>ip-specification</i></p>
<dd>a list of IP addresses to assign to remote PPTP clients. Each connected client must have a different address, so there must be at least as many addresses as you have simultaneous clients, and preferably some spare, since you cannot change this list without restarting pptpd. A warning will be sent to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) when the IP address pool is exhausted. <code>remoteip</code> will be ignored if the <code>delegate</code> option is used.</p>
<dt><code>noipparam</code></p>
<dd>by default, the original client IP address is given to ip-up scripts using the <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) option <code>ipparam.</code> The <code>noipparam</code> option prevents this. Equivalent to the command line <code>&#8211;noipparam</code> option.</p>
<dt><code>listen </code><i>ip-address</i></p>
<dd>the local interface IP address to listen on for incoming PPTP connections (TCP port 1723). Equivalent to the command line <code>&#8211;listen</code> option.</p>
<dt><code>vrf </code><i>vrf-name</i></p>
<dd>VRF to use for the TCP listening socket as well as the GRE packets. Equivalent to the command line <code>&#8211;vrf</code> option.</p>
<dt><code>pidfile </code><i>pid-file</i></p>
<dd>specifies an alternate location to store the process ID file (default /var/run/pptpd.pid). Equivalent to the command line <code>&#8211;pidfile</code> option.</p>
<dt><code>speed </code><i>speed</i></p>
<dd>specifies a speed (in bits per second) to pass to the PPP daemon as the interface speed for the tty/pty pair. This is ignored by some PPP daemons, such as Linux&#8217;s <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8). The default is 115200 bytes per second, which some implementations interpret as meaning &quot;no limit&quot;. Equivalent to the command line <code>&#8211;speed</code> option.</dl>
<h2>Notes</h2>
<p>An <i>ip-specification</i> above (for the <code>localip</code> and <code>remoteip</code> tags) may be a list of IP addresses (for example 192.168.0.2,192.168.0.3), a range (for example 192.168.0.1-254 or 192.168.0-255.2) or some combination (for example 192.168.0.2,192.168.0.5-8). For some valid pairs might be (depending on use of the VPN): <code>localip </code><i>192.168.0.1</i><br />
 <code>remoteip </code><i>192.168.0.2-254</i> or <code>localip </code><i>192.168.1.2-254</i><br />
 <code>remoteip </code><i>192.168.0.2-254</i> </p>
<h2>Routing Checklist &#8211; Proxyarp</h2>
<p>Allocate a section of your LAN addresses for use by clients. </p>
<p> In <i>/etc/ppp/options.pptpd.</i> set the <code>proxyarp</code> option. In <i>pptpd.conf</i> do not set <code>localip</code> option, but set <code>remoteip</code> to the allocated address range. Enable kernel forwarding of packets, (e.g. using <i>/proc/sys/net/ipv4/ip_forward</i> ). </p>
<p> The server will advertise the clients to the LAN using ARP, providing it&#8217;s own ethernet address. <code><a href="/docs/linux/man/8-bcrelay/">bcrelay</a></code>(8) should not be required.</p>
<h2>Routing Checklist &#8211; Forwarding</h2>
<p>Allocate a subnet for the clients that is routable from your LAN, but is not part of your LAN. </p>
<p> In <i>pptpd.conf</i> set <code>localip</code> to a single address or range in the allocated subnet, set <code>remoteip</code> to a range in the allocated subnet. Enable kernel forwarding of packets, (e.g. using <i>/proc/sys/net/ipv4/ip_forward</i> ). The LAN must have a route to the clients using the server as gateway. </p>
<p> The server will forward the packets unchanged between the clients and the LAN. <code><a href="/docs/linux/man/8-bcrelay/">bcrelay</a></code>(8) will be required to support broadcast protocols such as NETBIOS.</p>
<h2>Routing Checklist &#8211; Masquerade</h2>
<p>Allocate a subnet for the clients that is not routable from your LAN, and not otherwise routable from the server (e.g. 10.0.0.0/24). </p>
<p> Set <code>localip</code> to a single address in the subnet (e.g. 10.0.0.1), set <code>remoteip</code> to a range for the rest of the subnet, (e.g. 10.0.0.2-200). Enable kernel forwarding of packets, (e.g. using <i>/proc/sys/net/ipv4/ip_forward</i> ). Enable masquerading on eth0 (e.g. <i>iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE</i> ). </p>
<p> The server will translate the packets between the clients and the LAN. The clients will appear to the LAN as having the address corresponding to the server. The LAN need not have an explicit route to the clients. <code><a href="/docs/linux/man/8-bcrelay/">bcrelay</a></code>(8) will be required to support broadcast protocols such as NETBIOS.</p>
<h2>Firewall Rules</h2>
<p><code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8) accepts control connections on TCP port 1723, and then uses GRE (protocol 47) to exchange data packets. Add these rules to your <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) configuration, or use them as the basis for your own rules: </p>
<p> iptables &#8211;append INPUT &#8211;protocol 47 &#8211;jump ACCEPT </p>
<pre>iptables --append INPUT --protocol tcp --match tcp \
<br>
 --destination-port 1723 --jump ACCEPT </pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8), <code><a href="/docs/linux/man/8-pptpd/">pptpd</a></code>(8), <code><a href="/docs/linux/man/5-pptpd-conf/">pptpd.conf</a></code>(5). </p>
