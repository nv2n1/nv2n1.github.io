---
title: "networkmanager-dispatcher(8)"
name: "networkmanager-dispatcher"
section: "8"
letter: "n"
url: "/docs/linux/man/8-networkmanager-dispatcher/"
description: "NetworkManager-dispatcher – Dispatch user scripts for NetworkManager"
---

<p>NetworkManager-dispatcher &#8211; Dispatch user scripts for NetworkManager</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>NetworkManager </code><code>[OPTIONS&#8230;]</code></dl>
<h2>Description</h2>
<dd>NetworkManager-dispatcher service is a D-Bus activated service that runs user provided scripts upon certain changes in NetworkManager. </p>
<p> NetworkManager-dispatcher will execute scripts in the /{etc,usr/lib}/NetworkManager/dispatcher.d directory or subdirectories in alphabetical order in response to network events. Each script should be a regular executable file owned by root. Furthermore, it must not be writable by group or other, and not setuid. </p>
<p> Each script receives two arguments, the first being the interface name of the device an operation just happened on, and second the action. For device actions, the interface is the name of the kernel interface suitable for IP configuration. Thus it is either VPN_IP_IFACE, DEVICE_IP_IFACE, or DEVICE_IFACE, as applicable. For the <i>hostname</i> action the device name is always &quot;none&quot; and for <i>connectivity-change</i> it is empty. </p>
<p> The actions are: </p>
<p> <i>pre-up</i></p>
<dl>
<dd>The interface is connected to the network but is not yet fully activated. Scripts acting on this event must be placed or symlinked into the /etc/NetworkManager/dispatcher.d/pre-up.d directory, and NetworkManager will wait for script execution to complete before indicating to applications that the interface is fully activated.</dl>
<p> <i>up</i></p>
<dl>
<dd>The interface has been activated.</dl>
<p> <i>pre-down</i></p>
<dl>
<dd>The interface will be deactivated but has not yet been disconnected from the network. Scripts acting on this event must be placed or symlinked into the /etc/NetworkManager/dispatcher.d/pre-down.d directory, and NetworkManager will wait for script execution to complete before disconnecting the interface from its network. Note that this event is not emitted for forced disconnections, like when carrier is lost or a wireless signal fades. It is only emitted when there is an opportunity to cleanly handle a network disconnection event.</dl>
<p> <i>down</i></p>
<dl>
<dd>The interface has been deactivated.</dl>
<p> <i>vpn-pre-up</i></p>
<dl>
<dd>The VPN is connected to the network but is not yet fully activated. Scripts acting on this event must be placed or symlinked into the /etc/NetworkManager/dispatcher.d/pre-up.d directory, and NetworkManager will wait for script execution to complete before indicating to applications that the VPN is fully activated.</dl>
<p> <i>vpn-up</i></p>
<dl>
<dd>A VPN connection has been activated.</dl>
<p> <i>vpn-pre-down</i></p>
<dl>
<dd>The VPN will be deactivated but has not yet been disconnected from the network. Scripts acting on this event must be placed or symlinked into the /etc/NetworkManager/dispatcher.d/pre-down.d directory, and NetworkManager will wait for script execution to complete before disconnecting the VPN from its network. Note that this event is not emitted for forced disconnections, like when the VPN terminates unexpectedly or general connectivity is lost. It is only emitted when there is an opportunity to cleanly handle a VPN disconnection event.</dl>
<p> <i>vpn-down</i></p>
<dl>
<dd>A VPN connection has been deactivated.</dl>
<p> <i>hostname</i></p>
<dl>
<dd>The system hostname has been updated. Use <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2) to retrieve it. The interface name (first argument) is empty and no environment variable is set for this action.</dl>
<p> <i>dhcp4-change</i></p>
<dl>
<dd>The DHCPv4 lease has changed (renewed, rebound, etc).</dl>
<p> <i>dhcp6-change</i></p>
<dl>
<dd>The DHCPv6 lease has changed (renewed, rebound, etc).</dl>
<p> <i>connectivity-change</i></p>
<dl>
<dd>The network connectivity state has changed (no connectivity, went online, etc).</dl>
<p> The environment contains more information about the interface and the connection. The following variables are available for the use in the dispatcher scripts: </p>
<p> <i>NM_DISPATCHER_ACTION</i></p>
<dl>
<dd>The dispatcher action like &quot;up&quot; or &quot;dhcp4-change&quot;, identical to the first command line argument. Since NetworkManager 1.12.0.</dl>
<p> <i>CONNECTION_UUID</i></p>
<dl>
<dd>The UUID of the connection profile.</dl>
<p> <i>CONNECTION_ID</i></p>
<dl>
<dd>The name (ID) of the connection profile.</dl>
<p> <i>CONNECTION_DBUS_PATH</i></p>
<dl>
<dd>The NetworkManager D-Bus path of the connection.</dl>
<p> <i>CONNECTION_FILENAME</i></p>
<dl>
<dd>The backing file name of the connection profile (if any).</dl>
<p> <i>CONNECTION_EXTERNAL</i></p>
<dl>
<dd>If &quot;1&quot;, this indicates that the connection describes a network configuration created outside of NetworkManager.</dl>
<p> <i>DEVICE_IFACE</i></p>
<dl>
<dd>The interface name of the control interface of the device. Depending on the device type, this differs from <i>DEVICE_IP_IFACE</i>. For example for ADSL devices, this could be &#8216;atm0&#8217; or for WWAN devices it might be &#8216;ttyUSB0&#8217;.</dl>
<p> <i>DEVICE_IP_IFACE</i></p>
<dl>
<dd>The IP interface name of the device. This is the network interface on which IP addresses and routes will be configured.</dl>
<p> <i>IP4_ADDRESS_N</i></p>
<dl>
<dd>The IPv4 address in the format &quot;address/prefix gateway&quot;, where N is a number from 0 to (# IPv4 addresses &#8211; 1). gateway item in this variable is deprecated, use IP4_GATEWAY instead.</dl>
<p> <i>IP4_NUM_ADDRESSES</i></p>
<dl>
<dd>The variable contains the number of IPv4 addresses the script may expect.</dl>
<p> <i>IP4_GATEWAY</i></p>
<dl>
<dd>The gateway IPv4 address in traditional numbers-and-dots notation.</dl>
<p> <i>IP4_ROUTE_N</i></p>
<dl>
<dd>The IPv4 route in the format &quot;address/prefix next-hop metric&quot;, where N is a number from 0 to (# IPv4 routes &#8211; 1).</dl>
<p> <i>IP4_NUM_ROUTES</i></p>
<dl>
<dd>The variable contains the number of IPv4 routes the script may expect.</dl>
<p> <i>IP4_NAMESERVERS</i></p>
<dl>
<dd>The variable contains a space-separated list of the DNS servers.</dl>
<p> <i>IP4_DOMAINS</i></p>
<dl>
<dd>The variable contains a space-separated list of the search domains.</dl>
<p> <i>DHCP4_&lt;dhcp-option-name&gt;</i></p>
<dl>
<dd>If the connection used DHCP for address configuration, the received DHCP configuration is passed in the environment using standard DHCP option names, prefixed with &quot;DHCP4_&quot;, like &quot;DHCP4_HOST_NAME=foobar&quot;.</dl>
<p> <i>IP6_&lt;name&gt; and DHCP6_&lt;name&gt;</i></p>
<dl>
<dd>The same variables as for IPv4 are available for IPv6, but the prefixes are IP6_ and DHCP6_ instead.</dl>
<p> <i>CONNECTIVITY_STATE</i></p>
<dl>
<dd>The network connectivity state, which can take the values defined by the NMConnectivityState type, from the org.freedesktop.NetworkManager D-Bus API: unknown, none, portal, limited or full. Note: this variable will only be set for connectivity-change actions.</dl>
<p> In case of VPN, VPN_IP_IFACE is set, and IP4_*, IP6_* variables with VPN prefix are exported too, like VPN_IP4_ADDRESS_0, VPN_IP4_NUM_ADDRESSES. </p>
<p> Dispatcher scripts are run one at a time, but asynchronously from the main NetworkManager process, and will be killed if they run for too long. If your script might take arbitrarily long to complete, you should spawn a child process and have the parent return immediately. Scripts that are symbolic links pointing inside the /etc/NetworkManager/dispatcher.d/no-wait.d/ directory are run immediately, without waiting for the termination of previous scripts, and in parallel. Also beware that once a script is queued, it will always be run, even if a later event renders it obsolete. (Eg, if an interface goes up, and then back down again quickly, it is possible that one or more &quot;up&quot; scripts will be run after the interface has gone down.)</p>
<h2>Bugs</h2>
<p>Please report any bugs you find in NetworkManager at the m[blue]<code>NetworkManager issue tracker</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>See Also</h2>
<p>m[blue]<code>NetworkManager home page</code>m[]<font SIZE="-2">[2]</font>, <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8),</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>NetworkManager issue tracker</p>
<dl>
<dd><a rel="nofollow" href="https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues">https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/issues</a></dl>
<dt> 2.</p>
<dd>NetworkManager home page</p>
<dl>
<dd><a rel="nofollow" href="https://networkmanager.dev">https://networkmanager.dev</a></dl>
