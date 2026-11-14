---
title: "nmcli-examples(5)"
name: "nmcli-examples"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nmcli-examples/"
description: "nmcli-examples – usage examples of nmcli"
---

<p>nmcli-examples &#8211; usage examples of nmcli</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nmcli </code><code>[OPTIONS&#8230;]</code></dl>
<h2>Description</h2>
<p><i>nmcli</i></p>
<dd>is a command-line client for NetworkManager. It allows controlling NetworkManager and reporting its status. For more information please refer to <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1) manual page. </p>
<p> The purpose of this manual page is to provide you with various examples and usage scenarios of <i>nmcli</i>. </p>
<p> Note: this page has &quot;work-in-progress&quot; status.</p>
<h2>Examples</h2>
<p><code>Example 1. Listing available Wi-Fi APs</code> </p>
<dl>
<dd>
<pre><code>$ nmcli device wifi list
 </code></pre>
</dl>
<dl>
<dd>
<pre>* SSID MODE CHAN RATE SIGNAL BARS SECURITY
 netdatacomm_local Infra 6 54 Mbit/s 37 ▂▄__ WEP
* F1 Infra 11 54 Mbit/s 98 ▂▄▆█ WPA1
 LoremCorp Infra 1 54 Mbit/s 62 ▂▄▆_ WPA2 802.1X
 Internet Infra 6 54 Mbit/s 29 ▂___ WPA1
 HPB110a.F2672A Ad-Hoc 6 54 Mbit/s 22 ▂___ --
 Jozinet Infra 1 54 Mbit/s 19 ▂___ WEP
 VOIP Infra 1 54 Mbit/s 20 ▂___ WEP
 MARTINA Infra 4 54 Mbit/s 32 ▂▄__ WPA2
 N24PU1 Infra 7 11 Mbit/s 22 ▂___ --
 alfa Infra 1 54 Mbit/s 67 ▂▄▆_ WPA2
 bertnet Infra 5 54 Mbit/s 20 ▂___ WPA1 WPA2</pre>
</dl>
<p> This command shows how to list available Wi-Fi networks (APs). You can also use <i>&#8211;fields</i> option for displaying different columns. <code>nmcli -f all dev wifi list</code> will show all of them. </p>
<p> <code>Example 2. Showing general information and properties for a Wi-Fi interface</code> </p>
<dl>
<dd>
<pre><code>$ nmcli -p -f general,wifi-properties device show wlan0
 </code></pre>
</dl>
<dl>
<dd>
<pre>===============================================================================
 Device details (wlan0)
===============================================================================
GENERAL.DEVICE: wlan0
GENERAL.TYPE: wifi
GENERAL.VENDOR: Intel Corporation
GENERAL.PRODUCT: PRO/Wireless 5100 AGN [Shiloh] Network Connection
GENERAL.DRIVER: iwlwifi
GENERAL.DRIVER-VERSION: 3.8.13-100.fc17.x86_64
GENERAL.FIRMWARE-VERSION: 8.83.5.1 build 33692
GENERAL.HWADDR: 00:1E:65:37:A1:D3
GENERAL.MTU: 1500
GENERAL.STATE: 100 (connected)
GENERAL.REASON: 0 (No reason given)
GENERAL.UDI: /sys/devices/pci0000:00/0000:00:1c.1/0000:03:00.0/net/wlan0
GENERAL.IP-IFACE: wlan0
GENERAL.IS-SOFTWARE: no
GENERAL.NM-MANAGED: yes
GENERAL.AUTOCONNECT: yes
GENERAL.FIRMWARE-MISSING: no
GENERAL.CONNECTION: My Alfa WiFi
GENERAL.CON-UUID: 85194f4c-d496-4eec-bae0-d880b4cbcf26
GENERAL.CON-PATH: /org/freedesktop/NetworkManager/ActiveConnection/10
-------------------------------------------------------------------------------
WIFI-PROPERTIES.WEP: yes
WIFI-PROPERTIES.WPA: yes
WIFI-PROPERTIES.WPA2: yes
WIFI-PROPERTIES.TKIP: yes
WIFI-PROPERTIES.CCMP: yes
WIFI-PROPERTIES.AP: no
WIFI-PROPERTIES.ADHOC: yes
-------------------------------------------------------------------------------</pre>
</dl>
<p> This command shows information about a Wi-Fi device. </p>
<p> <code>Example 3. Listing NetworkManager polkit permissions</code> </p>
<dl>
<dd>
<pre><code>$ nmcli general permissions
 </code></pre>
</dl>
<dl>
<dd>
<pre>PERMISSION VALUE
org.freedesktop.NetworkManager.enable-disable-network yes
org.freedesktop.NetworkManager.enable-disable-wifi yes
org.freedesktop.NetworkManager.enable-disable-wwan yes
org.freedesktop.NetworkManager.enable-disable-wimax yes
org.freedesktop.NetworkManager.sleep-wake no
org.freedesktop.NetworkManager.network-control yes
org.freedesktop.NetworkManager.wifi.share.protected yes
org.freedesktop.NetworkManager.wifi.share.open yes
org.freedesktop.NetworkManager.settings.modify.system yes
org.freedesktop.NetworkManager.settings.modify.own yes
org.freedesktop.NetworkManager.settings.modify.hostname auth</pre>
</dl>
<p> This command shows configured polkit permissions for various NetworkManager operations. These permissions or actions (using polkit language) are configured by a system administrator and are not meant to be changed by users. The usual place for the polkit configuration is /usr/share/polkit-1/actions/org.freedesktop.NetworkManager.policy. <i>pkaction</i> command can display description for polkit actions. </p>
<dl>
<dd>
<pre><code> pkaction --action-id org.freedesktop.NetworkManager.network-control --verbose
 </code></pre>
</dl>
<p> More information about polkit can be found at <a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/polkit.">http://www.freedesktop.org/wiki/Software/polkit.</a> </p>
<p> <code>Example 4. Listing NetworkManager log level and domains</code> </p>
<dl>
<dd>
<pre><code>$ nmcli general logging
 </code></pre>
</dl>
<dl>
<dd>
<pre>LEVEL DOMAINS
INFO PLATFORM,RFKILL,ETHER,WIFI,BT,MB,DHCP4,DHCP6,PPP,WIFI_SCAN,IP4,IP6,AUTOIP4,DNS,VPN,SHARING,SUPPLICANT,AGENTS,SETTINGS,SUSPEND,CORE,DEVICE,OLPC,WIMAX,INFINIBAND,FIREWALL,ADSL,BOND,VLAN,BRIDGE,DBUS_PROPS,TEAM,CONCHECK,DCB,DISPATCH</pre>
</dl>
<p> This command shows current NetworkManager logging status. </p>
<p> <code>Example 5. Changing NetworkManager logging</code> </p>
<dl>
<dd>
<pre><code>$ nmcli g log level DEBUG domains CORE,ETHER,IP
$ nmcli g log level INFO domains DEFAULT
 </code></pre>
</dl>
<p> The first command makes NetworkManager log in DEBUG level, and only for CORE, ETHER and IP domains. The second command restores the default logging state. Please refer to the <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5) manual page for available logging levels and domains. </p>
<p> <code>Example 6. Adding a bonding master and two slave connection profiles</code> </p>
<dl>
<dd>
<pre><code>$ nmcli con add type bond ifname mybond0 mode active-backup
$ nmcli con add type bond-slave ifname eth1 master mybond0
$ nmcli con add type bond-slave ifname eth2 master mybond0
 </code></pre>
</dl>
<p> This example demonstrates adding a bond master connection and two slaves. The first command adds a master bond connection, naming the bonding interface <i>mybond0</i> and using <i>active-backup</i> mode. The next two commands add slaves connections, both enslaved to <i>mybond0</i>. The first slave will be bound to <i>eth1</i> interface, the second to <i>eth2</i>. </p>
<p> <code>Example 7. Adding a team master and two slave connection profiles</code> </p>
<dl>
<dd>
<pre><code>$ nmcli con add type team con-name Team1 ifname Team1 config team1-master-json.conf
$ nmcli con add type team-slave con-name Team1-slave1 ifname em1 master Team1
$ nmcli con add type team-slave con-name Team1-slave2 ifname em2 master Team1
 </code></pre>
</dl>
<p> This example demonstrates adding a team master connection profile and two slaves. It is very similar to the bonding example. The first command adds a master team profile, naming the team interface and the profile <i>Team1</i>. The team configuration for the master is read from <i>team1-master-json.conf</i> file. Later, you can change the configuration with <i>modify</i> command (<code>nmcli con modify Team1 team.config team1-master-another-json.conf</code>). The last two commands add slaves profiles, both enslaved to <i>Team1</i>. The first slave will be bound to <i>em1</i> interface, the second to <i>em2</i>. The slaves don&#8217;t specify <i>config</i> and thus <i>teamd</i> will use its default configuration. You will activate the whole setup by activating both slaves: </p>
<dl>
<dd>
<pre><code>$ nmcli con up Team1-slave1
$ nmcli con up Team1-slave2
 </code></pre>
</dl>
<p> By default, the created profiles are marked for auto-activation. But if another connection has been activated on the device, the new profile won&#8217;t activate automatically and you need to activate it manually. </p>
<p> <code>Example 8. Adding a bridge and two slave profiles</code> </p>
<dl>
<dd>
<pre><code>$ nmcli con add type bridge con-name TowerBridge ifname TowerBridge
$ nmcli con add type bridge-slave con-name br-slave-1 ifname ens3 master TowerBridge
$ nmcli con add type bridge-slave con-name br-slave-2 ifname ens4 master TowerBridge
$ nmcli con modify TowerBridge bridge.stp no
 </code></pre>
</dl>
<p> This example demonstrates adding a bridge master connection and two slaves. The first command adds a master bridge connection, naming the bridge interface and the profile as <i>TowerBridge</i>. The next two commands add slaves profiles, both will be enslaved to <i>TowerBridge</i>. The first slave will be tied to <i>ens3</i> interface, the second to <i>ens4</i>. The last command will disable 802.1D STP for the TowerBridge profile. </p>
<p> <code>Example 9. Adding an ethernet connection profile with manual IP configuration</code> </p>
<dl>
<dd>
<pre> <code>
$ nmcli con add con-name my-con-em1 ifname em1 type ethernet ip4 192.168.100.100/24 gw4 192.168.100.1 ip4 1.2.3.4 ip6 abbe::cafe
$ nmcli con mod my-con-em1 ipv4.dns &quot;8.8.8.8 8.8.4.4&quot;
$ nmcli con mod my-con-em1 +ipv4.dns 1.2.3.4
$ nmcli con mod my-con-em1 ipv6.dns &quot;2001:4860:4860::8888 2001:4860:4860::8844&quot;
$ nmcli -p con show my-con-em1
 </code></pre>
</dl>
<p> The first command adds an Ethernet connection profile named <i>my-con-em1</i> that is bound to interface name <i>em1</i>. The profile is configured with static IP addresses. Three addresses are added, two IPv4 addresses and one IPv6. The first IP 192.168.100.100 has a prefix of 24 (netmask equivalent of 255.255.255.0). Gateway entry will become the default route if this profile is activated on em1 interface (and there is no connection with higher priority). The next two addresses do not specify a prefix, so a default prefix will be used, i.e. 32 for IPv4 and 128 for IPv6. The second, third and fourth commands modify DNS parameters of the new connection profile. The last <i>con show</i> command displays the profile so that all parameters can be reviewed. </p>
<p> <code>Example 10. Escaping colon characters in tabular mode</code> </p>
<dl>
<dd>
<pre> <code>
$ nmcli -t -f general -e yes -m tab dev show eth0
 </code></pre>
</dl>
<dl>
<dd>
<pre>GENERAL:eth0:ethernet:Intel Corporation:82567LM Gigabit Network Connection:e1000e:2.1.4-k:1.8-3:00\:22\:68\:15\:29\:21:1500:100 (connected):0 (No reason given):/sys/devices/pci0000\:00/0000\:00\:19.0/net/eth0:eth0:yes:yes:no:ethernet-13:89cbcbc6-dc85-456c-9c8b-bd828fee3917:/org/freedesktop/NetworkManager/ActiveConnection/9</pre>
</dl>
<p> This example shows escaping colon characters in tabular mode. It may be useful for script processing, because &#8216;:&#8217; is used as a field separator. </p>
<p> <code>Example 11. nmcli usage in a NetworkManager dispatcher script to make Ethernet and Wi-Fi mutually exclusive</code> </p>
<dl>
<dd>
<pre>#!/bin/bash
export LC_ALL=C
enable_disable_wifi ()
{
 result=$(nmcli dev | grep &quot;ethernet&quot; | grep -w &quot;connected&quot;)
 if [ -n &quot;$result&quot; ]; then
 nmcli radio wifi off
 else
 nmcli radio wifi on
 fi
}
if [ &quot;$2&quot; = &quot;up&quot; ]; then
 enable_disable_wifi
fi
if [ &quot;$2&quot; = &quot;down&quot; ]; then
 enable_disable_wifi
fi</pre>
</dl>
<p> This dispatcher script makes Wi-Fi mutually exclusive with wired networking. When a wired interface is connected, Wi-Fi will be set to airplane mode (rfkilled). When the wired interface is disconnected, Wi-Fi will be turned back on. Name this script e.g. 70-wifi-wired-exclusive.sh and put it into /etc/NetworkManager/dispatcher.d/ directory. See <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8) manual page for more information about NetworkManager dispatcher scripts. </p>
<p> <code>Example sessions of interactive connection editor</code> </p>
<p> <code>Example 12. Adding an ethernet connection profile in interactive editor (a)</code> </p>
<dl>
<dd>
<pre> <code>
$ nmcli connection edit type ethernet
 </code></pre>
</dl>
<dl>
<dd>
<pre>===| nmcli interactive connection editor |===
Adding a new '802-3-ethernet' connection
Type 'help' or '?' for available commands.
Type 'describe [&lt;setting&gt;.&lt;prop&gt;]' for detailed property description.
You may edit the following settings: connection, 802-3-ethernet (ethernet), 802-1x, ipv4, ipv6, dcb
nmcli&gt; print
===============================================================================
 Connection details
===============================================================================
connection.id: ethernet-4
connection.uuid: de89cdeb-a3e1-4d53-8fa0-c22546c775f4
connection.interface-name: --
connection.type: 802-3-ethernet
connection.autoconnect: yes
connection.autoconnect-priority: 0
connection.timestamp: 0
connection.read-only: no
connection.permissions: 
connection.zone: --
connection.master: --
connection.slave-type: --
connection.secondaries: 
connection.gateway-ping-timeout: 0
-------------------------------------------------------------------------------
802-3-ethernet.port: --
802-3-ethernet.speed: 0
802-3-ethernet.duplex: --
802-3-ethernet.auto-negotiate: yes
802-3-ethernet.mac-address: --
802-3-ethernet.cloned-mac-address: --
802-3-ethernet.mac-address-blacklist: 
802-3-ethernet.mtu: auto
802-3-ethernet.s390-subchannels: 
802-3-ethernet.s390-nettype: --
802-3-ethernet.s390-options: 
-------------------------------------------------------------------------------
ipv4.method: auto
ipv4.dns: 
ipv4.dns-search: 
ipv4.addresses: 
ipv4.gateway: --
ipv4.routes: 
ipv4.route-metric: -1
ipv4.ignore-auto-routes: no
ipv4.ignore-auto-dns: no
ipv4.dhcp-client-id: --
ipv4.dhcp-send-hostname: yes
ipv4.dhcp-hostname: --
ipv4.never-default: no
ipv4.may-fail: yes
-------------------------------------------------------------------------------
ipv6.method: auto
ipv6.dns: 
ipv6.dns-search: 
ipv6.addresses: 
ipv6.gateway: --
ipv6.routes: 
ipv6.route-metric: -1
ipv6.ignore-auto-routes: no
ipv6.ignore-auto-dns: no
ipv6.never-default: no
ipv6.may-fail: yes
ipv6.ip6-privacy: -1 (unknown)
ipv6.dhcp-hostname: --
-------------------------------------------------------------------------------
nmcli&gt; goto ethernet
You may edit the following properties: port, speed, duplex, auto-negotiate, mac-address, cloned-mac-address, mac-address-blacklist, mtu, s390-subchannels, s390-nettype, s390-options
nmcli 802-3-ethernet&gt; set mtu 1492
nmcli 802-3-ethernet&gt; b
nmcli&gt; goto ipv4.addresses
nmcli ipv4.addresses&gt; desc
=== [addresses] ===
[NM property description]
Array of IP addresses.
[nmcli specific description]
Enter a list of IPv4 addresses formatted as:
 ip[/prefix], ip[/prefix],...
Missing prefix is regarded as prefix of 32.
Example: 192.168.1.5/24, 10.0.0.11/24
nmcli ipv4.addresses&gt; set 192.168.1.100/24
Do you also want to set 'ipv4.method' to 'manual'? [yes]: yes
nmcli ipv4.addresses&gt;
nmcli ipv4.addresses&gt; print
addresses: 192.168.1.100/24
nmcli ipv4.addresses&gt; back
nmcli ipv4&gt; b
nmcli&gt; set ipv4.gateway 192.168.1.1
nmcli&gt; verify
Verify connection: OK
nmcli&gt; print
===============================================================================
 Connection details
===============================================================================
connection.id: ethernet-4
connection.uuid: de89cdeb-a3e1-4d53-8fa0-c22546c775f4
connection.interface-name: --
connection.type: 802-3-ethernet
connection.autoconnect: yes
connection.autoconnect-priority: 0
connection.timestamp: 0
connection.read-only: no
connection.permissions: 
connection.zone: --
connection.master: --
connection.slave-type: --
connection.secondaries: 
connection.gateway-ping-timeout: 0
-------------------------------------------------------------------------------
802-3-ethernet.port: --
802-3-ethernet.speed: 0
802-3-ethernet.duplex: --
802-3-ethernet.auto-negotiate: yes
802-3-ethernet.mac-address: --
802-3-ethernet.cloned-mac-address: --
802-3-ethernet.mac-address-blacklist: 
802-3-ethernet.mtu: 1492
802-3-ethernet.s390-subchannels: 
802-3-ethernet.s390-nettype: --
802-3-ethernet.s390-options: 
-------------------------------------------------------------------------------
ipv4.method: manual
ipv4.dns: 
ipv4.dns-search: 
ipv4.addresses: 192.168.1.100/24
ipv4.gateway: 192.168.1.1
ipv4.routes: 
ipv4.route-metric: -1
ipv4.ignore-auto-routes: no
ipv4.ignore-auto-dns: no
ipv4.dhcp-client-id: --
ipv4.dhcp-send-hostname: yes
ipv4.dhcp-hostname: --
ipv4.never-default: no
ipv4.may-fail: yes
-------------------------------------------------------------------------------
ipv6.method: auto
ipv6.dns: 
ipv6.dns-search: 
ipv6.addresses: 
ipv6.routes: 
ipv6.route-metric: -1
ipv6.ignore-auto-routes: no
ipv6.ignore-auto-dns: no
ipv6.never-default: no
ipv6.may-fail: yes
ipv6.ip6-privacy: -1 (unknown)
ipv6.dhcp-hostname: --
-------------------------------------------------------------------------------
nmcli&gt; set ipv4.dns 8.8.8.8 8.8.4.4
nmcli&gt; print
===============================================================================
 Connection details
===============================================================================
connection.id: ethernet-4
connection.uuid: de89cdeb-a3e1-4d53-8fa0-c22546c775f4
connection.interface-name: --
connection.type: 802-3-ethernet
connection.autoconnect: yes
connection.autoconnect-priority: 0
connection.timestamp: 0
connection.read-only: no
connection.permissions: 
connection.zone: --
connection.master: --
connection.slave-type: --
connection.secondaries: 
connection.gateway-ping-timeout: 0
-------------------------------------------------------------------------------
802-3-ethernet.port: --
802-3-ethernet.speed: 0
802-3-ethernet.duplex: --
802-3-ethernet.auto-negotiate: yes
802-3-ethernet.mac-address: --
802-3-ethernet.cloned-mac-address: --
802-3-ethernet.mac-address-blacklist: 
802-3-ethernet.mtu: 1492
802-3-ethernet.s390-subchannels: 
802-3-ethernet.s390-nettype: --
802-3-ethernet.s390-options: 
-------------------------------------------------------------------------------
ipv4.method: manual
ipv4.dns: 8.8.8.8,8.8.4.4
ipv4.dns-search: 
ipv4.addresses: 192.168.1.100/24
ipv4.gateway: 192.168.1.1
ipv4.routes: 
ipv4.route-metric: -1
ipv4.ignore-auto-routes: no
ipv4.ignore-auto-dns: no
ipv4.dhcp-client-id: --
ipv4.dhcp-send-hostname: yes
ipv4.dhcp-hostname: --
ipv4.never-default: no
ipv4.may-fail: yes
-------------------------------------------------------------------------------
ipv6.method: auto
ipv6.dns: 
ipv6.dns-search: 
ipv6.addresses: 
ipv6.gateway: --
ipv6.routes: 
ipv6.route-metric: -1
ipv6.ignore-auto-routes: no
ipv6.ignore-auto-dns: no
ipv6.never-default: no
ipv6.may-fail: yes
ipv6.ip6-privacy: -1 (unknown)
ipv6.dhcp-hostname: --
-------------------------------------------------------------------------------
nmcli&gt; verify
Verify connection: OK
nmcli&gt; save
Connection 'ethernet-4' (de89cdeb-a3e1-4d53-8fa0-c22546c775f4) successfully saved.
nmcli&gt; quit</pre>
</dl>
<p> Example session in the nmcli interactive connection editor. The scenario creates an Ethernet connection profile with static addressing (IPs and DNS).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5), <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5), <code><a href="/docs/linux/man/1-nm-online/">nm-online</a></code>(1), <code><a href="/docs/linux/man/1-nm-applet/">nm-applet</a></code>(1), <code><a href="/docs/linux/man/1-nm-connection-editor/">nm-connection-editor</a></code>(1) </p>
