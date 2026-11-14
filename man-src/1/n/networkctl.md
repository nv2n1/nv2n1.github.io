---
title: "networkctl(1)"
name: "networkctl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-networkctl/"
description: "networkctl – Query the status of network links"
---

<h2 class="name">NAME</h2>
<p> networkctl &#8211; Query the status of network links </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>networkctl</code> [OPTIONS&#8230;] COMMAND [LINK&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>networkctl</code></p>
<dd>may be used to introspect the state of the network links as seen by <code>systemd-networkd</code>. Please refer to <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) for an introduction to the basic concepts, functionality, and configuration syntax.</p>
<h2>COMMANDS</h2>
<p> The following commands are understood: </p>
<p> <code>list</code> [<i>PATTERN&#8230;</i>]</p>
<dl>
<dt>
<dd> Show a list of existing links and their status. If one ore more <i>PATTERN</i>s are specified, only links matching one of them are shown. If no further arguments are specified shows all links, otherwise just the specified links. Produces output similar to: </p>
<dl>
<dt>
<dd>
<pre>
IDX LINK         TYPE     OPERATIONAL SETUP
  1 lo           loopback carrier     unmanaged
  2 eth0         ether    routable    configured
  3 virbr0       ether    no-carrier  unmanaged
  4 virbr0-nic   ether    off         unmanaged
4 links listed.
</pre>
</dl>
<p> The operational status is one of the following: </p>
<p> missing</p>
<dl>
<dt>
<dd> the device is missing</dl>
<p> off</p>
<dl>
<dt>
<dd> the device is powered down</dl>
<p> no-carrier</p>
<dl>
<dt>
<dd> the device is powered up, but it does not yet have a carrier</dl>
<p> dormant</p>
<dl>
<dt>
<dd> the device has a carrier, but is not yet ready for normal traffic</dl>
<p> degraded-carrier</p>
<dl>
<dt>
<dd> for bond or bridge master, one of the bonding or bridge slave network interfaces is in off, no-carrier, or dormant state</dl>
<p> carrier</p>
<dl>
<dt>
<dd> the link has a carrier, or for bond or bridge master, all bonding or bridge slave network interfaces are enslaved to the master</dl>
<p> degraded</p>
<dl>
<dt>
<dd> the link has carrier and addresses valid on the local link configured</dl>
<p> enslaved</p>
<dl>
<dt>
<dd> the link has carrier and is enslaved to bond or bridge master network interface</dl>
<p> routable</p>
<dl>
<dt>
<dd> the link has carrier and routable address configured</dl>
<p> The setup status is one of the following: </p>
<p> pending</p>
<dl>
<dt>
<dd> udev is still processing the link, we don&#8217;t yet know if we will manage it</dl>
<p> failed</p>
<dl>
<dt>
<dd> networkd failed to manage the link</dl>
<p> configuring</p>
<dl>
<dt>
<dd> in the process of retrieving configuration or configuring the link</dl>
<p> configured</p>
<dl>
<dt>
<dd> link configured successfully</dl>
<p> unmanaged</p>
<dl>
<dt>
<dd> networkd is not handling the link</dl>
<p> linger</p>
<dl>
<dt>
<dd> the link is gone, but has not yet been dropped by networkd</dl>
</dl>
<p> <code>status</code> [<i>PATTERN&#8230;</i>]</p>
<dl>
<dt>
<dd> Show information about the specified links: type, state, kernel module driver, hardware and IP address, configured DNS servers, etc. If one ore more <i>PATTERN</i>s are specified, only links matching one of them are shown. </p>
<p> When no links are specified, an overall network status is shown. Also see the option <code>&#8211;all</code>. </p>
<p> Produces output similar to: </p>
<dl>
<dt>
<dd>
<pre>
●        State: routable
  Online state: online
       Address: 10.193.76.5 on eth0
                192.168.122.1 on virbr0
                169.254.190.105 on eth0
                fe80::5054:aa:bbbb:cccc on eth0
       Gateway: 10.193.11.1 (CISCO SYSTEMS, INC.) on eth0
           DNS: 8.8.8.8
                8.8.4.4
</pre>
</dl>
<p> In the overall network status, the online state depends on the individual online state of all required links. Managed links are required for online by default. In this case, the online state is one of the following: </p>
<p> unknown</p>
<dl>
<dt>
<dd> all links have unknown online status (i.e. there are no required links)</dl>
<p> offline</p>
<dl>
<dt>
<dd> all required links are offline</dl>
<p> partial</p>
<dl>
<dt>
<dd> some, but not all, required links are online</dl>
<p> online</p>
<dl>
<dt>
<dd> all required links are online</dl>
</dl>
<p> <code>lldp</code> [<i>PATTERN&#8230;</i>]</p>
<dl>
<dt>
<dd> Show discovered LLDP (Link Layer Discovery Protocol) neighbors. If one or more <i>PATTERN</i>s are specified only neighbors on those interfaces are shown. Otherwise shows discovered neighbors on all interfaces. Note that for this feature to work, <i>LLDP=</i> must be turned on for the specific interface, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) for details. </p>
<p> Produces output similar to: </p>
<dl>
<dt>
<dd>
<pre><code>
LINK CHASSIS ID SYSTEM NAME CAPS PORT ID PORT DESCRIPTION
        enp0s25 00 : e0 : 4c : 00 : 00 : 00 GS1900..b........2 Port #2 Capability Flags : o -
    Other;
p - Repeater;
b - Bridge;
w - WLAN Access Point;
r - Router;
t - Telephone;
d - DOCSIS cable device;
a - Station;
c - Customer VLAN;
s - Service VLAN, m - Two - port MAC Relay(TPMR) 1 neighbors listed.
</code></pre>
</dl>
</dl>
<p> <code>label</code></p>
<dl>
<dt>
<dd> Show numerical address labels that can be used for address selection. This is the same information that <code><a href="/docs/linux/man/8-ip-addrlabel/">ip-addrlabel</a></code>(8) shows. See m[blue]<code>RFC 3484</code>m[]<font SIZE="-2">[1]</font> for a discussion of address labels. </p>
<p> Produces output similar to: </p>
<dl>
<dt>
<dd>
<pre>
Prefix/Prefixlen                          Label
        ::/0                                  1
    fc00::/7                                  5
    fec0::/10                                11
    2002::/16                                 2
    3ffe::/16                                12
 2001:10::/28                                 7
    2001::/32                                 6
::ffff:0.0.0.0/96                             4
        ::/96                                 3
       ::1/128                                0
</pre>
</dl>
</dl>
<p> <code>delete</code> <i>DEVICE&#8230;</i></p>
<dl>
<dt>
<dd> Deletes virtual netdevs. Takes interface name or index number.</dl>
<p> <code>up</code> <i>DEVICE&#8230;</i></p>
<dl>
<dt>
<dd> Bring devices up. Takes interface name or index number.</dl>
<p> <code>down</code> <i>DEVICE&#8230;</i></p>
<dl>
<dt>
<dd> Bring devices down. Takes interface name or index number.</dl>
<p> <code>renew</code> <i>DEVICE&#8230;</i></p>
<dl>
<dt>
<dd> Renew dynamic configurations e.g. addresses received from DHCP server. Takes interface name or index number.</dl>
<p> <code>forcerenew</code> <i>DEVICE&#8230;</i></p>
<dl>
<dt>
<dd> Send a FORCERENEW message to all connected clients, triggering DHCP reconfiguration. Takes interface name or index number.</dl>
<p> <code>reconfigure</code> <i>DEVICE&#8230;</i></p>
<dl>
<dt>
<dd> Reconfigure network interfaces. Takes interface name or index number. Note that this does not reload .netdev or .network corresponding to the specified interface. So, if you edit config files, it is necessary to call <code>networkctl reload</code> first to apply new settings.</dl>
<p> <code>reload</code></p>
<dl>
<dt>
<dd> Reload .netdev and .network files. If a new .netdev file is found, then the corresponding netdev is created. Note that even if an existing .netdev is modified or removed, <code>systemd-networkd</code> does not update or remove the netdev. If a new, modified or removed .network file is found, then all interfaces which match the file are reconfigured.</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-a</code> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Show all links with <code>status</code>.</dl>
<p> <code>-s</code> <code>&#8211;stats</code></p>
<dl>
<dt>
<dd> Show link statistics with <code>status</code>.</dl>
<p> <code>-l</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize the output.</dl>
<p> <code>-n</code>, <code>&#8211;lines=</code></p>
<dl>
<dt>
<dd> When used with <code>status</code>, controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument. Defaults to 10.</dl>
<p> <code>&#8211;json=</code><i>MODE</i></p>
<dl>
<dt>
<dd> Shows output formatted as JSON. Expects one of &quot;short&quot; (for the shortest possible output without any redundant whitespace or line breaks), &quot;pretty&quot; (for a pretty version of the same, with indentation and line breaks) or &quot;off&quot; (to turn off JSON output, the default).</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dt>
<dd> Do not print the legend, i.e. column headers and the footer with hints.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5), <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> RFC 3484</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc3484">https://tools.ietf.org/html/rfc3484</a></dl>
</dl>
<h2>Index</h2>
