---
title: "nm-settings-ifcfg-rh(5)"
name: "nm-settings-ifcfg-rh"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nm-settings-ifcfg-rh/"
description: "nm-settings-ifcfg-rh – Description of ifcfg-rh settings plugin"
---

<p>nm-settings-ifcfg-rh &#8211; Description of <i>ifcfg-rh</i> settings plugin</p>
<h2>Description</h2>
<p>NetworkManager is based on the concept of connection profiles that contain network configuration (see <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5) for details). The profiles can be stored in various formats. NetworkManager uses plugins for reading and writing the data. The plugins can be configured in <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5). </p>
<p> The <i>ifcfg-rh</i> plugin is used on the Fedora and Red Hat Enterprise Linux distributions to read/write configuration from/to the traditional /etc/sysconfig/network-scripts/ifcfg-* files. Each NetworkManager connection maps to one ifcfg-* file, with possible usage of keys-* for passwords, route-* for static IPv4 routes and route6-* for static IPv6 routes. The plugin currently supports reading and writing Ethernet, Wi-Fi, InfiniBand, VLAN, Bond, Bridge, and Team connections. Unsupported connection types (such as WWAN, PPPoE, VPN, or ADSL) are handled by <i>keyfile</i> plugin (<code><a href="/docs/linux/man/5-nm-settings-keyfile/">nm-settings-keyfile</a></code>(5)). The main reason for using <i>ifcfg-rh</i> plugin is the compatibility with legacy configurations for <i>ifup</i> and <i>ifdown</i> (initscripts).</p>
<h2>File Format</h2>
<p>The <i>ifcfg-rh</i> config format is a simple text file containing VARIABLE=&quot;value&quot; lines. The format is described in sysconfig.txt of <i>initscripts</i> package. Note that the configuration files may be sourced by <i>initscripts</i>, so they must be valid shell scripts. That means, for instance, that # character can be used for comments, strings with spaces must be quoted, special characters must be escaped, etc. </p>
<p> Users can create or modify the <i>ifcfg-rh</i> connection files manually, even if that is not the recommended way of managing the profiles. However, if they choose to do that, they must inform NetworkManager about their changes (see <i>monitor-connection-file</i> in <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5), and <i>nmcli con (re)load</i>). </p>
<p> <code>Some ifcfg-rh configuration examples:</code>. </p>
<dl>
<dd>
<pre><code>Simple DHCP ethernet configuration:</code>
NAME=ethernet
UUID=1c4ddf70-01bf-46d6-b04f-47e842bd98da
TYPE=Ethernet
BOOTPROTO=dhcp
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
ONBOOT=yes</pre>
</dl>
<dl>
<dd>
<pre><code>Simple ethernet configuration with static IP:</code>
TYPE=Ethernet
BOOTPROTO=none
IPADDR=10.1.0.25
PREFIX=24
GATEWAY=10.1.0.1
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_PEERDNS=yes
IPV6_PEERROUTES=yes
IPV6_FAILURE_FATAL=no
NAME=ethernet-em2
UUID=51bb3904-c0fc-4dfe-83b2-0a71e7928c13
DEVICE=em2
ONBOOT=yes</pre>
</dl>
<dl>
<dd>
<pre><code>WPA2 Enterprise WLAN (TTLS with inner MSCHAPV2 authentication):</code>
ESSID=&quot;CompanyWLAN&quot;
MODE=Managed
KEY_MGMT=WPA-EAP
TYPE=Wireless
IEEE_8021X_EAP_METHODS=TTLS
IEEE_8021X_IDENTITY=joe
IEEE_8021X_PASSWORD_FLAGS=ask
IEEE_8021X_INNER_AUTH_METHODS=MSCHAPV2
IEEE_8021X_CA_CERT=/home/joe/.cert/company.crt
BOOTPROTO=dhcp
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=no
NAME=MyCompany
UUID=f79848ff-11a6-4810-9e1a-99039dea84c4
ONBOOT=yes</pre>
</dl>
<dl>
<dd>
<pre><code>Bridge and bridge port configuration:</code>
ifcfg-bridge: ifcfg-bridge-port:
NAME=bridge NAME=bridge007-port-eth0
UUID=4be99ce0-c5b2-4764-8b77-ec226e440125 UUID=3ad56c4a-47e1-419b-b0d4-8ad86eb967a3
DEVICE=bridge007 DEVICE=eth0
STP=yes ONBOOT=yes
TYPE=Bridge TYPE=Ethernet
BRIDGING_OPTS=priority=32768 BRIDGE=bridge007
ONBOOT=yes
BOOTPROTO=dhcp</pre>
</dl>
<dl>
<dd>
<pre><code>Bonding configuration:</code>
ifcfg-BOND: ifcfg-BOND-slave:
NAME=BOND NAME=BOND-slave
UUID=b41888aa-924c-450c-b0f8-85a4f0a51b4a UUID=9bb048e4-286a-4cc3-b104-007dbd20decb
DEVICE=bond100 DEVICE=eth0
BONDING_OPTS=&quot;mode=balance-rr miimon=100&quot; ONBOOT=yes
TYPE=Bond TYPE=Ethernet
BONDING_MASTER=yes MASTER=bond100
ONBOOT=yes SLAVE=yes
BOOTPROTO=dhcp</pre>
</dl>
<dl>
<dd>
<pre><code>Team and team port configuration:</code>
ifcfg-my_team0:
DEVICE=team0
TEAM_CONFIG=&quot;{ \&quot;device\&quot;: \&quot;team0\&quot;, \&quot;runner\&quot;: {\&quot;name\&quot;: \&quot;roundrobin\&quot;}, \&quot;ports\&quot;: {\&quot;eth1\&quot;: {}, \&quot;eth2\&quot;: {}} }&quot;
DEVICETYPE=Team
BOOTPROTO=dhcp
NAME=team0-profile
UUID=1d3460a0-7b37-457f-a300-fe8d92da4807
ONBOOT=yes
ifcfg-my_team0_slave1:
NAME=team0-slave1
UUID=d5aed298-c567-4cc1-b808-6d38ecef9e64
DEVICE=eth1
ONBOOT=yes
TEAM_MASTER=team0
DEVICETYPE=TeamPort
ifcfg-my_team0_slave2:
NAME=team0-slave2
UUID=94e75f4e-e5ad-401c-8962-31e0ae5d2215
DEVICE=eth2
ONBOOT=yes
TEAM_MASTER=team0
DEVICETYPE=TeamPort</pre>
</dl>
<p> The UUID values in the config files must be unique. You can use <i>uuidgen</i> command line tool to generate such values. Alternatively, you can leave out UUID entirely. In that case NetworkManager will generate a UUID based on the file name.</p>
<h2>Differences Against Initscripts</h2>
<p>The main differences of NetworkManager ifcfg-rh plugin and traditional initscripts are: </p>
<p> <code>NM_CONTROLLED=yes|no</code></p>
<dl>
<dd>NM_CONTROLLED is NetworkManager-specific variable used by NetworkManager for determining whether the device of the <i>ifcfg</i> file should be managed. NM_CONTROLLED=yes is supposed if the variable is not present in the file. Note that if you have more <i>ifcfg</i> files for a single device, NM_CONTROLLED=no in one of the files will cause the device not to be managed. The profile may not even be the active one.</dl>
<p> <code>New variables</code></p>
<dl>
<dd>NetworkManager has introduced some new variable, not present in initscripts, to be able to store data for its new features. The variables are marked as extensions in the tables below.</dl>
<p> <code>Semantic change of variables</code></p>
<dl>
<dd>NetworkManager had to slightly change the semantic for a few variables. </p>
<dl>
<dd>&bull; PEERDNS &#8211; initscripts interpret PEERDNS=no to mean &quot;never touch resolv.conf&quot;. NetworkManager interprets it to say &quot;never add automatic (DHCP, PPP, VPN, etc.) nameservers to resolv.conf&quot;.</dl>
<dl>
<dd>&bull; ONBOOT &#8211; initscripts use ONBOOT=yes to mark the devices that are to be activated during boot. NetworkManager extents this to also mean that this profile can be used for auto-connecting at any time.</dl>
<dl>
<dd>&bull; BOOTPROTO &#8211; NetworkManager supports traditional values <i>none</i> (static), <i>dhcp</i>. But it also allows additional values to enable new addressing methods. They are <i>autoip</i> for IPv4 link-local addressing using Avahi daemon and <i>shared</i> for connection sharing. When <i>shared</i> is used, NetworkManager assigns the interface 10.42.0.1, or it uses the first static address, if configured.</dl>
<dl>
<dd>&bull; HWADDR &#8211; initscripts compare the currently set hardware address of a device, while NetworkManager considers the permanent one.</dl>
</dl>
<p> See the next section for detailed mapping of NetworkManager properties and <i>ifcfg-rh</i> variables. Variable names, format and usage differences in NetworkManager and initscripts are documented in the tables below.</p>
<h2>Details</h2>
<p><i>ifcfg-rh</i> plugin variables marked with <i>(+)</i> are NetworkManager specific extensions not understood by traditional initscripts. </p>
<p> <code>Table 1. 802-1x setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> eap </td>
<td> IEEE_8021X_EAP_METHODS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> EAP method for 802.1X authentication.<code> </p>
<p> Example: </code>IEEE_8021X_EAP_METHODS=PEAP<code> </p>
<p> Allowed values: </code>&quot;LEAP&quot;, &quot;PWD&quot;, &quot;TLS&quot;, &quot;PEAP&quot;, &quot;TTLS&quot;, &quot;FAST&quot;
</td>
</tr>
<tr VALIGN=top>
<td> identity </td>
<td> IEEE_8021X_IDENTITY<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Identity for EAP authentication methods.<code> </p>
<p> Example: </code>IEEE_8021X_IDENTITY=itsme
</td>
</tr>
<tr VALIGN=top>
<td> anonymous-identity </td>
<td> IEEE_8021X_ANON_IDENTITY<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Anonymous identity for EAP authentication methods.
</td>
</tr>
<tr VALIGN=top>
<td> pac-file </td>
<td> IEEE_8021X_PAC_FILE<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> File with PAC (Protected Access Credential) for EAP-FAST.<code> </p>
<p> Example: </code>IEEE_8021X_PAC_FILE=/home/joe/my-fast.pac
</td>
</tr>
<tr VALIGN=top>
<td> ca-cert </td>
<td> IEEE_8021X_CA_CERT<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> CA certificate for EAP.<code> </p>
<p> Example: </code>IEEE_8021X_CA_CERT=/home/joe/cacert.crt
</td>
</tr>
<tr VALIGN=top>
<td> ca-path </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> The property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> subject-match </td>
<td> IEEE_8021X_SUBJECT_MATCH<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Substring to match subject of server certificate against.<code> </p>
<p> Example: </code>IEEE_8021X_SUBJECT_MATCH=&quot;Red Hat&quot;
</td>
</tr>
<tr VALIGN=top>
<td> altsubject-matches </td>
<td> IEEE_8021X_ALTSUBJECT_MATCHES<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> List of strings to be matched against the altSubjectName.<code> </p>
<p> Example: </code>IEEE_8021X_ALTSUBJECT_MATCHES=&quot;s1.domain.cc&quot;
</td>
</tr>
<tr VALIGN=top>
<td> domain-suffix-match </td>
<td> IEEE_8021X_DOMAIN_SUFFIX_MATCH<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Suffix to match domain of server certificate against.
</td>
</tr>
<tr VALIGN=top>
<td> client-cert </td>
<td> IEEE_8021X_CLIENT_CERT<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Client certificate for EAP.<code> </p>
<p> Example: </code>IEEE_8021X_CLIENT_CERT=/home/joe/mycert.crt
</td>
</tr>
<tr VALIGN=top>
<td> phase1-peapver </td>
<td> IEEE_8021X_PEAP_VERSION<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Use to force a specific PEAP version.<code> </p>
<p> Allowed values: </code>0, 1
</td>
</tr>
<tr VALIGN=top>
<td> phase1-peaplabel </td>
<td> IEEE_8021X_PEAP_FORCE_NEW_LABEL<i>(+)</i> </td>
<td> no </td>
<td> Use to force the new PEAP label during key derivation.<code> </p>
<p> Allowed values: </code>yes, no
</td>
</tr>
<tr VALIGN=top>
<td> phase1-fast-provisioning </td>
<td> IEEE_8021X_FAST_PROVISIONING<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Enable in-line provisioning of EAP-FAST credentials.<code> </p>
<p> Example: </code>IEEE_8021X_FAST_PROVISIONING=&quot;allow-auth allow-unauth&quot;<code> </p>
<p> Allowed values: </code>space-separated list of these values [allow-auth, allow-unauth]
</td>
</tr>
<tr VALIGN=top>
<td> phase1-auth-flags </td>
<td> IEEE_8021X_PHASE1_AUTH_FLAGS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Authentication flags for the supplicant<code> </p>
<p> Example: </code>IEEE_8021X_PHASE1_AUTH_FLAGS=&quot;tls-1-0-disable tls-1-1-disable&quot;<code> </p>
<p> Allowed values: </code>space-separated list of authentication flags names
</td>
</tr>
<tr VALIGN=top>
<td> phase2-auth </td>
<td> IEEE_8021X_INNER_AUTH_METHODS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Inner non-EAP authentication methods. IEEE_8021X_INNER_AUTH_METHODS can contain values both for &#8216;phase2-auth&#8217; and &#8216;phase2-autheap&#8217; properties.<code> </p>
<p> Example: </code>IEEE_8021X_INNER_AUTH_METHODS=PAP<code> </p>
<p> Allowed values: </code>&quot;PAP&quot;, &quot;CHAP&quot;, &quot;MSCHAP&quot;, &quot;MSCHAPV2&quot;, &quot;GTC&quot;, &quot;OTP&quot;, &quot;MD5&quot; and &quot;TLS&quot;
</td>
</tr>
<tr VALIGN=top>
<td> phase2-autheap </td>
<td> IEEE_8021X_INNER_AUTH_METHODS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Inner EAP-based authentication methods. Note that IEEE_8021X_INNER_AUTH_METHODS is also used for &#8216;phase2-auth&#8217; values.<code> </p>
<p> Example: </code>IEEE_8021X_INNER_AUTH_METHODS=&quot;MSCHAPV2 EAP-TLS&quot;<code> </p>
<p> Allowed values: </code>&quot;EAP-MD5&quot;, &quot;EAP-MSCHAPV2&quot;, &quot;EAP-GTC&quot;, &quot;EAP-OTP&quot; and &quot;EAP-TLS&quot;
</td>
</tr>
<tr VALIGN=top>
<td> phase2-subject-match </td>
<td> IEEE_8021X_PHASE2_SUBJECT_MATCH<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Substring to match subject of server certificate against.<code> </p>
<p> Example: </code>IEEE_8021X_PHASE2_SUBJECT_MATCH=&quot;Red Hat&quot;
</td>
</tr>
<tr VALIGN=top>
<td> phase2-altsubject-matches </td>
<td> IEEE_8021X_PHASE2_ALTSUBJECT_MATCHES<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td> phase2-domain-suffix-match </td>
<td> IEEE_8021X_PHASE2_DOMAIN_SUFFIX_MATCH<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Suffix to match domain of server certificate for phase 2 against.
</td>
</tr>
<tr VALIGN=top>
<td> phase2-client-cert </td>
<td> IEEE_8021X_INNER_CLIENT_CERT<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Client certificate for inner EAP method.<code> </p>
<p> Example: </code>IEEE_8021X_INNER_CLIENT_CERT=/home/joe/mycert.crt
</td>
</tr>
<tr VALIGN=top>
<td> password </td>
<td> IEEE_8021X_PASSWORD<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> UTF-8 encoded password used for EAP. It can also go to &quot;key-&quot; lookaside file, or it can be owned by a secret agent.
</td>
</tr>
<tr VALIGN=top>
<td> password-flags </td>
<td> IEEE_8021X_PASSWORD_FLAGS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password flags for IEEE_8021X_PASSWORD password. (see the section called &#8220;Secret flags&#8221; for _FLAGS values)
</td>
</tr>
<tr VALIGN=top>
<td> password-raw </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> The property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> password-raw-flags </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> The property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> private-key </td>
<td> IEEE_8021X_PRIVATE_KEY<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Private key for EAP-TLS.<code> </p>
<p> Example: </code>IEEE_8021X_PRIVATE_KEY=/home/joe/mykey.p12
</td>
</tr>
<tr VALIGN=top>
<td> private-key-password </td>
<td> IEEE_8021X_PRIVATE_KEY_PASSWORD<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password for IEEE_8021X_PRIVATE_KEY. It can also go to &quot;key-&quot; lookaside file, or it can be owned by a secret agent.
</td>
</tr>
<tr VALIGN=top>
<td> private-key-password-flags </td>
<td> IEEE_8021X_PRIVATE_KEY_PASSWORD_FLAGS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password flags for IEEE_8021X_PRIVATE_KEY_PASSWORD password. (see the section called &#8220;Secret flags&#8221; for _FLAGS values)
</td>
</tr>
<tr VALIGN=top>
<td> phase2-private-key </td>
<td> IEEE_8021X_INNER_PRIVATE_KEY<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Private key for inner authentication method for EAP-TLS.
</td>
</tr>
<tr VALIGN=top>
<td> phase2-private-key-password </td>
<td> IEEE_8021X_INNER_PRIVATE_KEY_PASSWORD<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password for IEEE_8021X_INNER_PRIVATE_KEY. It can also go to &quot;key-&quot; lookaside file, or it can be owned by a secret agent.
</td>
</tr>
<tr VALIGN=top>
<td> phase2-private-key-password-flags </td>
<td> IEEE_8021X_INNER_PRIVATE_KEY_PASSWORD_FLAGS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password flags for IEEE_8021X_INNER_PRIVATE_KEY_PASSWORD password. (see the section called &#8220;Secret flags&#8221; for _FLAGS values)
</td>
</tr>
<tr VALIGN=top>
<td> pin </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> The property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> pin-flags </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> The property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> system-ca-certs </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> The property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> auth-timeout </td>
<td> IEEE_8021X_AUTH_TIMEOUT<i>(+)</i> </td>
<td> 0 </td>
<td> Timeout in seconds for the 802.1X authentication. Zero means the global default or 25.
</td>
</tr>
</table>
<p> <code>Table 2. bond setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> options </td>
<td> BONDING_OPTS </td>
<td> &nbsp;<wbr> </td>
<td> Bonding options.<code> </p>
<p> Example: </code>BONDING_OPTS=&quot;miimon=100 mode=broadcast&quot;
</td>
</tr>
</table>
<p> <code>Table 3. bridge-port setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> priority </td>
<td> BRIDGING_OPTS: priority= </td>
<td> 32 </td>
<td> STP priority.<code> </p>
<p> Allowed values: </code>0 &#8211; 63
</td>
</tr>
<tr VALIGN=top>
<td> path-cost </td>
<td> BRIDGING_OPTS: path_cost= </td>
<td> 100 </td>
<td> STP cost.<code> </p>
<p> Allowed values: </code>1 &#8211; 65535
</td>
</tr>
<tr VALIGN=top>
<td> hairpin-mode </td>
<td> BRIDGING_OPTS: hairpin_mode= </td>
<td> yes </td>
<td> Hairpin mode of the bridge port.
</td>
</tr>
</table>
<p> <code>Table 4. bridge setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> MACADDR<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> MAC address of the bridge. Note that this requires a recent kernel support, originally introduced in 3.15 upstream kernel) MACADDR for bridges is an NM extension.
</td>
</tr>
<tr VALIGN=top>
<td> stp </td>
<td> STP </td>
<td> no </td>
<td> Span tree protocol participation.
</td>
</tr>
<tr VALIGN=top>
<td> priority </td>
<td> BRIDGING_OPTS: priority= </td>
<td> 32768 </td>
<td> STP priority.<code> </p>
<p> Allowed values: </code>0 &#8211; 32768
</td>
</tr>
<tr VALIGN=top>
<td> forward-delay </td>
<td> DELAY </td>
<td> 15 </td>
<td> STP forwarding delay.<code> </p>
<p> Allowed values: </code>2 &#8211; 30
</td>
</tr>
<tr VALIGN=top>
<td> hello-time </td>
<td> BRIDGING_OPTS: hello_time= </td>
<td> 2 </td>
<td> STP hello time.<code> </p>
<p> Allowed values: </code>1 &#8211; 10
</td>
</tr>
<tr VALIGN=top>
<td> max-age </td>
<td> BRIDGING_OPTS: max_age= </td>
<td> 20 </td>
<td> STP maximum message age.<code> </p>
<p> Allowed values: </code>6 &#8211; 40
</td>
</tr>
<tr VALIGN=top>
<td> ageing-time </td>
<td> BRIDGING_OPTS: ageing_time= </td>
<td> 300 </td>
<td> Ethernet MAC ageing time.<code> </p>
<p> Allowed values: </code>0 &#8211; 1000000
</td>
</tr>
<tr VALIGN=top>
<td> multicast-snooping </td>
<td> BRIDGING_OPTS: multicast_snooping= </td>
<td> 1 </td>
<td> IGMP snooping support.<code> </p>
<p> Allowed values: </code>0 or 1
</td>
</tr>
</table>
<p> <code>Table 5. connection setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> id </td>
<td> NAME<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> User friendly name for the connection profile.
</td>
</tr>
<tr VALIGN=top>
<td> uuid </td>
<td> UUID<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> UUID for the connection profile. When missing, NetworkManager creates the UUID itself (by hashing the filename).
</td>
</tr>
<tr VALIGN=top>
<td> stable-id </td>
<td> STABLE_ID<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Token to generate stable IDs.
</td>
</tr>
<tr VALIGN=top>
<td> interface-name </td>
<td> DEVICE </td>
<td> &nbsp;<wbr> </td>
<td> Interface name of the device this profile is bound to. The variable can be left out when the profile should apply for more devices. Note that DEVICE can be required for some connection types.
</td>
</tr>
<tr VALIGN=top>
<td> type </td>
<td> TYPE (DEVICETYPE, DEVICE) </td>
<td> &nbsp;<wbr> </td>
<td> Base type of the connection. DEVICETYPE is used for teaming connections.<code> </p>
<p> Example: </code>TYPE=Ethernet; TYPE=Bond; TYPE=Bridge; DEVICETYPE=TeamPort<code> </p>
<p> Allowed values: </code>Ethernet, Wireless, InfiniBand, Bridge, Bond, Vlan, Team, TeamPort
</td>
</tr>
<tr VALIGN=top>
<td> permissions </td>
<td> USERS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> USERS restrict the access for this conenction to certain users only.<code> </p>
<p> Example: </code>USERS=&quot;joe bob&quot;
</td>
</tr>
<tr VALIGN=top>
<td> autoconnect </td>
<td> ONBOOT </td>
<td> yes </td>
<td> Whether the connection should be autoconnected (not only while booting).
</td>
</tr>
<tr VALIGN=top>
<td> autoconnect-priority </td>
<td> AUTOCONNECT_PRIORITY<i>(+)</i> </td>
<td> 0 </td>
<td> Connection priority for automatic activation. Connections with higher numbers are preferred when selecting profiles for automatic activation.<code> </p>
<p> Example: </code>AUTOCONNECT_PRIORITY=20<code> </p>
<p> Allowed values: </code>-999 to 999
</td>
</tr>
<tr VALIGN=top>
<td> autoconnect-retries </td>
<td> AUTOCONNECT_RETRIES<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> The number of times a connection should be autoactivated before giving up and switching to the next one.<code> </p>
<p> Example: </code>AUTOCONNECT_RETRIES=1<code> </p>
<p> Allowed values: </code>-1 (use global default), 0 (forever) or a positive value
</td>
</tr>
<tr VALIGN=top>
<td> zone </td>
<td> ZONE<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Trust level of this connection. The string is usually used for a firewall.<code> </p>
<p> Example: </code>ZONE=Work
</td>
</tr>
<tr VALIGN=top>
<td> master </td>
<td> MASTER, MASTER_UUID, TEAM_MASTER, TEAM_MASTER_UUID, BRIDGE, BRIDGE_UUID </td>
<td> &nbsp;<wbr> </td>
<td> Reference to master connection. The variable used depends on the connection type and the value. In general, if the *_UUID variant is present, the variant without *_UUID is ignored. NetworkManager attempts to write both for compatibility with legacy tooling.
</td>
</tr>
<tr VALIGN=top>
<td> slave-type </td>
<td> MASTER, MASTER_UUID, TEAM_MASTER, TEAM_MASTER_UUID, DEVICETYPE, BRIDGE, BRIDGE_UUID </td>
<td> &nbsp;<wbr> </td>
<td> Slave type doesn&#8217;t map directly to a variable, but it is recognized using different variables. MASTER and MASTER_UUID for bonding, TEAM_MASTER, TEAM_MASTER_UUID and DEVICETYPE for teaming, BRIDGE and BRIDGE_UUID for bridging.
</td>
</tr>
<tr VALIGN=top>
<td> autoconnect-slaves </td>
<td> AUTOCONNECT-SLAVES<i>(+)</i> </td>
<td> missing variable means global default </td>
<td> Whether slaves of this connection should be auto-connected when this connection is activated.
</td>
</tr>
<tr VALIGN=top>
<td> secondaries </td>
<td> SECONDARY_UUIDS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> UUID of VPN connections that should be activated together with this connection.
</td>
</tr>
<tr VALIGN=top>
<td> gateway-ping-timeout </td>
<td> GATEWAY_PING_TIMEOUT<i>(+)</i> </td>
<td> 0 </td>
<td> If greater than zero, the IP connectivity will be checked by pinging the gateway and waiting for the specified timeout (in seconds).<code> </p>
<p> Example: </code>GATEWAY_PING_TIMEOUT=5
</td>
</tr>
<tr VALIGN=top>
<td> metered </td>
<td> CONNECTION_METERED<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Whether the device is metered<code> </p>
<p> Example: </code>CONNECTION_METERED=yes<code> </p>
<p> Allowed values: </code>yes,no,unknown
</td>
</tr>
<tr VALIGN=top>
<td> lldp </td>
<td> LLDP<i>(+)</i> </td>
<td> missing variable means global default </td>
<td> whether LLDP is enabled for the connection<code> </p>
<p> Example: </code>LLDP=no<code> </p>
<p> Allowed values: </code>boolean value or &#8216;rx&#8217;
</td>
</tr>
</table>
<p> <code>Table 6. dcb setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> app-fcoe-flags </td>
<td> DCB_APP_FCOE_ENABLE, DCB_APP_FCOE_ADVERTISE, DCB_APP_FCOE_WILLING </td>
<td> no </td>
<td> FCOE flags.<code> </p>
<p> Example: </code>DCB_APP_FCOE_ENABLE=yes DCB_APP_FCOE_ADVERTISE=yes
</td>
</tr>
<tr VALIGN=top>
<td> app-fcoe-priority </td>
<td> DCB_APP_FCOE_PRIORITY </td>
<td> &nbsp;<wbr> </td>
<td> Priority of FCoE frames.<code> </p>
<p> Allowed values: </code>0 &#8211; 7
</td>
</tr>
<tr VALIGN=top>
<td> app-fcoe-mode </td>
<td> DCB_APP_FCOE_MODE </td>
<td> fabric </td>
<td> FCoE controller mode.<code> </p>
<p> Allowed values: </code>fabric, vn2vn
</td>
</tr>
<tr VALIGN=top>
<td> app-iscsi-flags </td>
<td> DCB_APP_ISCSI_ENABLE, DCB_APP_ISCSI_ADVERTISE, DCB_APP_ISCSI_WILLING </td>
<td> no </td>
<td> iSCSI flags.
</td>
</tr>
<tr VALIGN=top>
<td> app-iscsi-priority </td>
<td> DCB_APP_ISCSI_PRIORITY </td>
<td> &nbsp;<wbr> </td>
<td> Priority of iSCSI frames.<code> </p>
<p> Allowed values: </code>0 &#8211; 7
</td>
</tr>
<tr VALIGN=top>
<td> app-fip-flags </td>
<td> DCB_APP_FIP_ENABLE, DCB_APP_FIP_ADVERTISE, DCB_APP_FIP_WILLING </td>
<td> no </td>
<td> FIP flags.
</td>
</tr>
<tr VALIGN=top>
<td> app-fip-priority </td>
<td> DCB_APP_FIP_PRIORITY </td>
<td> &nbsp;<wbr> </td>
<td> Priority of FIP frames.<code> </p>
<p> Allowed values: </code>0 &#8211; 7
</td>
</tr>
<tr VALIGN=top>
<td> priority-flow-control-flags </td>
<td> DCB_PFC_ENABLE, DCB_PFC_ADVERTISE, DCB_PFC_WILLING </td>
<td> no </td>
<td> Priority flow control flags.
</td>
</tr>
<tr VALIGN=top>
<td> priority-flow-control </td>
<td> DCB_PFC_UP </td>
<td> &nbsp;<wbr> </td>
<td> Priority flow control values. String of 8 &quot;0&quot; and &quot;1&quot;, where &quot;0&quot;. means &quot;do not transmit priority pause&quot;, &quot;1&quot; means &quot;transmit pause&quot;.<code> </p>
<p> Example: </code>DCB_PFC_UP=01101110
</td>
</tr>
<tr VALIGN=top>
<td> priority-group-flags </td>
<td> DCB_PG_ENABLE, DCB_PG_ADVERTISE, DCB_PG_WILLING </td>
<td> no </td>
<td> Priority groups flags.
</td>
</tr>
<tr VALIGN=top>
<td> priority-group-id </td>
<td> DCB_PG_ID </td>
<td> &nbsp;<wbr> </td>
<td> Priority groups values. String of eight priorities (0 &#8211; 7) or &quot;f&quot; (unrestricted).<code> </p>
<p> Example: </code>DCB_PG_ID=1205f173
</td>
</tr>
<tr VALIGN=top>
<td> priority-group-bandwidth </td>
<td> DCB_PG_PCT </td>
<td> &nbsp;<wbr> </td>
<td> Priority groups values. Eight bandwidths (in percent), separated with commas.<code> </p>
<p> Example: </code>DCB_PG_PCT=10,5,10,15,10,10,10,30
</td>
</tr>
<tr VALIGN=top>
<td> priority-bandwidth </td>
<td> DCB_PG_UPPCT </td>
<td> &nbsp;<wbr> </td>
<td> Priority values. Eight bandwidths (in percent), separated with commas. The sum of the numbers must be 100.<code> </p>
<p> Example: </code>DCB_PG_UPPCT=7,13,10,10,15,15,10,20
</td>
</tr>
<tr VALIGN=top>
<td> priority-strict-bandwidth </td>
<td> DCB_PG_STRICT </td>
<td> &nbsp;<wbr> </td>
<td> Priority values. String of eight &quot;0&quot; or &quot;1&quot;, where &quot;0&quot; means &quot;may not utilize all bandwidth&quot;, &quot;1&quot; means &quot;may utilize all bandwidth&quot;.<code> </p>
<p> Example: </code>DCB_PG_STRICT=01101110
</td>
</tr>
<tr VALIGN=top>
<td> priority-traffic-class </td>
<td> DCB_PG_UP2TC </td>
<td> &nbsp;<wbr> </td>
<td> Priority values. String of eight trafic class values (0 &#8211; 7).<code> </p>
<p> Example: </code>DCB_PG_UP2TC=01623701
</td>
</tr>
</table>
<p> All DCB related configuration is a NetworkManager extension. DCB=yes must be used explicitly to enable DCB so that the rest of the DCB_* variables can apply. </p>
<p> <code>Table 7. dummy setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
</table>
<p> <code>Table 8. infiniband setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> HWADDR </td>
<td> &nbsp;<wbr> </td>
<td> IBoIP 20-byte hardware address of the device (in traditional hex-digits-and-colons notation). Note that for initscripts this is the current MAC address of the device as found during ifup. For NetworkManager this is the permanent MAC address. Or in case no permanent MAC address exists, the MAC address initially configured on the device.<code> </p>
<p> Example: </code>HWADDR=01:02:03:04:05:06:07:08:09:0A:01:02:03:04:05:06:07:08:09:11
</td>
</tr>
<tr VALIGN=top>
<td> mtu </td>
<td> MTU </td>
<td> &nbsp;<wbr> </td>
<td> MTU of the interface.
</td>
</tr>
<tr VALIGN=top>
<td> transport-mode </td>
<td> CONNECTED_MODE </td>
<td> CONNECTED_MODE=no </td>
<td> CONNECTED_MODE=yes for &quot;connected&quot; mode, CONNECTED_MODE=no for &quot;datagram&quot; mode
</td>
</tr>
<tr VALIGN=top>
<td> p-key </td>
<td> PKEY_ID (and PKEY=yes) </td>
<td> PKEY=no </td>
<td> InfiniBand P_Key. The value can be a hex number prefixed with &quot;0x&quot; or a decimal number. When PKEY_ID is specified, PHYSDEV and DEVICE also must be specified.<code> </p>
<p> Example: </code>PKEY=yes PKEY_ID=2 PHYSDEV=mlx4_ib0 DEVICE=mlx4_ib0.8002
</td>
</tr>
<tr VALIGN=top>
<td> parent </td>
<td> PHYSDEV (PKEY=yes) </td>
<td> PKEY=no </td>
<td> InfiniBand parent device.<code> </p>
<p> Example: </code>PHYSDEV=ib0
</td>
</tr>
</table>
<p> <code>Table 9. ipv4 setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> method </td>
<td> BOOTPROTO </td>
<td> none </td>
<td> Method used for IPv4 protocol configuration.<code> </p>
<p> Allowed values: </code>none, dhcp (bootp), static, ibft, autoip, shared
</td>
</tr>
<tr VALIGN=top>
<td> dns </td>
<td> DNS1, DNS2, &#8230; </td>
<td> &nbsp;<wbr> </td>
<td> List of DNS servers. Even if NetworkManager supports many DNS servers, initscripts and resolver only care about the first three, usually.<code> </p>
<p> Example: </code>DNS1=1.2.3.4 DNS2=10.0.0.254 DNS3=8.8.8.8
</td>
</tr>
<tr VALIGN=top>
<td> dns-search </td>
<td> DOMAIN </td>
<td> &nbsp;<wbr> </td>
<td> List of DNS search domains.
</td>
</tr>
<tr VALIGN=top>
<td> addresses </td>
<td> IPADDR, PREFIX, IPADDR1, PREFIX1, &#8230; </td>
<td> &nbsp;<wbr> </td>
<td> List of static IP addresses.<code> </p>
<p> Example: </code>IPADDR=10.5.5.23 PREFIX=24 IPADDR1=1.1.1.2 PREFIX1=16
</td>
</tr>
<tr VALIGN=top>
<td> gateway </td>
<td> GATEWAY </td>
<td> &nbsp;<wbr> </td>
<td> Gateway IP address.<code> </p>
<p> Example: </code>GATEWAY=10.5.5.1
</td>
</tr>
<tr VALIGN=top>
<td> routes </td>
<td> ADDRESS1, NETMASK1, GATEWAY1, METRIC1, OPTIONS1, &#8230; </td>
<td> &nbsp;<wbr> </td>
<td> List of static routes. They are not stored in ifcfg-* file, but in route-* file instead.
</td>
</tr>
<tr VALIGN=top>
<td> ignore-auto-routes </td>
<td> PEERROUTES<i>(+)</i> </td>
<td> yes </td>
<td> PEERROUTES has the opposite meaning as &#8216;ignore-auto-routes&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> ignore-auto-dns </td>
<td> PEERDNS </td>
<td> yes </td>
<td> PEERDNS has the opposite meaning as &#8216;ignore-auto-dns&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> dhcp-send-hostname </td>
<td> DHCP_SEND_HOSTNAME<i>(+)</i> </td>
<td> yes </td>
<td> Whether DHCP_HOSTNAME should be sent to the DHCP server.
</td>
</tr>
<tr VALIGN=top>
<td> dhcp-hostname </td>
<td> DHCP_HOSTNAME </td>
<td> &nbsp;<wbr> </td>
<td> Hostname to send to the DHCP server. When both DHCP_HOSTNAME and DHCP_FQDN are specified only the latter is used.
</td>
</tr>
<tr VALIGN=top>
<td> never-default </td>
<td> DEFROUTE (GATEWAYDEV in /etc/sysconfig/network) </td>
<td> yes </td>
<td> DEFROUTE=no tells NetworkManager that this connection should not be assigned the default route. DEFROUTE has the opposite meaning as &#8216;never-default&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> may-fail </td>
<td> IPV4_FAILURE_FATAL<i>(+)</i> </td>
<td> no </td>
<td> IPV4_FAILURE_FATAL has the opposite meaning as &#8216;may-fail&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> route-metric </td>
<td> IPV4_ROUTE_METRIC<i>(+)</i> </td>
<td> -1 </td>
<td> IPV4_ROUTE_METRIC is the default IPv4 metric for routes on this connection. If set to -1, a default metric based on the device type is used.
</td>
</tr>
<tr VALIGN=top>
<td> dns-priority </td>
<td> IPV4_DNS_PRIORITY<i>(+)</i> </td>
<td> 0 </td>
<td> The priority for DNS servers of this connection. Lower values have higher priority. If zero, the default value will be used (50 for VPNs, 100 for other connections). A negative value prevents DNS from other connections with greater values to be used.<code> </p>
<p> Example: </code>IPV4_DNS_PRIORITY=20
</td>
</tr>
<tr VALIGN=top>
<td> dhcp-client-id </td>
<td> DHCP_CLIENT_ID<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> A string sent to the DHCP server to identify the local machine.<code> </p>
<p> Example: </code>DHCP_CLIENT_ID=ax-srv-1
</td>
</tr>
<tr VALIGN=top>
<td> dad-timeout </td>
<td> ARPING_WAIT </td>
<td> missing variable means global default (config override or 3) </td>
<td> Timeout (in seconds) for performing DAD before configuring IPv4 addresses. 0 turns off the DAD completely, -1 means default value.<code> </p>
<p> Example: </code>ARPING_WAIT=2
</td>
</tr>
<tr VALIGN=top>
<td> dhcp-timeout </td>
<td> IPV4_DHCP_TIMEOUT<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> A timeout after which the DHCP transaction fails in case of no response.<code> </p>
<p> Example: </code>IPV4_DHCP_TIMEOUT=10
</td>
</tr>
<tr VALIGN=top>
<td> dhcp-fqdn </td>
<td> DHCP_FQDN </td>
<td> &nbsp;<wbr> </td>
<td> FQDN to send to the DHCP server. When both DHCP_HOSTNAME and DHCP_FQDN are specified only the latter is used.<code> </p>
<p> Example: </code>DHCP_FQDN=foo.bar.com
</td>
</tr>
</table>
<p> <code>Table 10. ipv6 setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> method </td>
<td> IPV6INIT, IPV6FORWARDING, IPV6_AUTOCONF, DHCPV6C </td>
<td> IPV6INIT=yes; IPV6FORWARDING=no; IPV6_AUTOCONF=!IPV6FORWARDING, DHCPV6=no </td>
<td> Method used for IPv6 protocol configuration. ignore ~ IPV6INIT=no; auto ~ IPV6_AUTOCONF=yes; dhcp ~ IPV6_AUTOCONF=no and DHCPV6C=yes
</td>
</tr>
<tr VALIGN=top>
<td> dns </td>
<td> DNS1, DNS2, &#8230; </td>
<td> &nbsp;<wbr> </td>
<td> List of DNS servers. NetworkManager uses the variables both for IPv4 and IPv6.
</td>
</tr>
<tr VALIGN=top>
<td> dns-search </td>
<td> DOMAIN </td>
<td> &nbsp;<wbr> </td>
<td> List of DNS search domains.
</td>
</tr>
<tr VALIGN=top>
<td> addresses </td>
<td> IPV6ADDR, IPV6ADDR_SECONDARIES </td>
<td> &nbsp;<wbr> </td>
<td> List of static IP addresses.<code> </p>
<p> Example: </code>IPV6ADDR=ab12:9876::1 IPV6ADDR_SECONDARIES=&quot;ab12:9876::2 ab12:9876::3&quot;
</td>
</tr>
<tr VALIGN=top>
<td> gateway </td>
<td> IPV6_DEFAULTGW </td>
<td> &nbsp;<wbr> </td>
<td> Gateway IP address.<code> </p>
<p> Example: </code>IPV6_DEFAULTGW=abbe::1
</td>
</tr>
<tr VALIGN=top>
<td> routes </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> List of static routes. They are not stored in ifcfg-* file, but in route6-* file instead in the form of command line for &#8216;ip route add&#8217;.
</td>
</tr>
<tr VALIGN=top>
<td> ignore-auto-routes </td>
<td> IPV6_PEERROUTES<i>(+)</i> </td>
<td> yes </td>
<td> IPV6_PEERROUTES has the opposite meaning as &#8216;ignore-auto-routes&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> ignore-auto-dns </td>
<td> IPV6_PEERDNS<i>(+)</i> </td>
<td> yes </td>
<td> IPV6_PEERDNS has the opposite meaning as &#8216;ignore-auto-dns&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> dhcp-hostname </td>
<td> DHCP_HOSTNAME </td>
<td> &nbsp;<wbr> </td>
<td> Hostname to send the DHCP server.
</td>
</tr>
<tr VALIGN=top>
<td> never-default </td>
<td> IPV6_DEFROUTE<i>(+)</i>, (and IPV6_DEFAULTGW, IPV6_DEFAULTDEV in /etc/sysconfig/network) </td>
<td> IPV6_DEFROUTE=yes (when no variable specified) </td>
<td> IPV6_DEFROUTE=no tells NetworkManager that this connection should not be assigned the default IPv6 route. IPV6_DEFROUTE has the opposite meaning as &#8216;never-default&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> may-fail </td>
<td> IPV6_FAILURE_FATAL<i>(+)</i> </td>
<td> no </td>
<td> IPV6_FAILURE_FATAL has the opposite meaning as &#8216;may-fail&#8217; property.
</td>
</tr>
<tr VALIGN=top>
<td> route-metric </td>
<td> IPV6_ROUTE_METRIC<i>(+)</i> </td>
<td> -1 </td>
<td> IPV6_ROUTE_METRIC is the default IPv6 metric for routes on this connection. If set to -1, a default metric based on the device type is used.
</td>
</tr>
<tr VALIGN=top>
<td> dns-priority </td>
<td> IPV6_DNS_PRIORITY<i>(+)</i> </td>
<td> 0 </td>
<td> The priority for DNS servers of this connection. Lower values have higher priority. If zero, the default value will be used (50 for VPNs, 100 for other connections). A negative value prevents DNS from other connections with greater values to be used.<code> </p>
<p> Example: </code>IPV6_DNS_PRIORITY=20
</td>
</tr>
<tr VALIGN=top>
<td> ip6-privacy </td>
<td> IPV6_PRIVACY, IPV6_PRIVACY_PREFER_PUBLIC_IP<i>(+)</i> </td>
<td> no </td>
<td> Configure IPv6 Privacy Extensions for SLAAC (RFC4941).<code> </p>
<p> Example: </code>IPV6_PRIVACY=rfc3041 IPV6_PRIVACY_PREFER_PUBLIC_IP=yes<code> </p>
<p> Allowed values: </code>IPV6_PRIVACY: no, yes (rfc3041 or rfc4941); IPV6_PRIVACY_PREFER_PUBLIC_IP: yes, no
</td>
</tr>
<tr VALIGN=top>
<td> addr-gen-mode </td>
<td> IPV6_ADDR_GEN_MODE </td>
<td> eui64 </td>
<td> Configure IPv6 Stable Privacy addressing for SLAAC (RFC7217).<code> </p>
<p> Example: </code>IPV6_ADDR_GEN_MODE=stable-privacy<code> </p>
<p> Allowed values: </code>IPV6_ADDR_GEN_MODE: eui64, stable-privacy
</td>
</tr>
<tr VALIGN=top>
<td> token </td>
<td> IPV6_TOKEN </td>
<td> &nbsp;<wbr> </td>
<td> The IPv6 tokenized interface identifier token<code> </p>
<p> Example: </code>IPV6_TOKEN=::53
</td>
</tr>
</table>
<p> <code>Table 11. macsec setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
</table>
<p> <code>Table 12. proxy setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> method </td>
<td> PROXY_METHOD<i>(+)</i> </td>
<td> none </td>
<td> Method for proxy configuration. For &quot;auto&quot;, WPAD is used for proxy configuration, or set the PAC file via PAC_URL or PAC_SCRIPT.<code> </p>
<p> Allowed values: </code>none, auto
</td>
</tr>
<tr VALIGN=top>
<td> browser-only </td>
<td> BROWSER_ONLY<i>(+)</i> </td>
<td> no </td>
<td> Whether the proxy configuration is for browser only.
</td>
</tr>
<tr VALIGN=top>
<td> pac-url </td>
<td> PAC_URL<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> URL for PAC file.<code> </p>
<p> Example: </code>PAC_URL=<a rel="nofollow" href="http://wpad.mycompany.com/wpad.dat">http://wpad.mycompany.com/wpad.dat</a>
</td>
</tr>
<tr VALIGN=top>
<td> pac-script </td>
<td> PAC_SCRIPT<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Path of the PAC script.<code> </p>
<p> Example: </code>PAC_SCRIPT=/home/joe/proxy.pac
</td>
</tr>
</table>
<p> <code>Table 13. team-port setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> config </td>
<td> TEAM_PORT_CONFIG </td>
<td> &nbsp;<wbr> </td>
<td> Team port configuration in JSON. See man teamd.conf for details.
</td>
</tr>
</table>
<p> <code>Table 14. team setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> config </td>
<td> TEAM_CONFIG </td>
<td> &nbsp;<wbr> </td>
<td> Team configuration in JSON. See man teamd.conf for details.
</td>
</tr>
</table>
<p> <code>Table 15. user setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
</table>
<p> <code>Table 16. 802-3-ethernet setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> port </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> The property is not saved by the plugin.
</td>
</tr>
<tr VALIGN=top>
<td> speed </td>
<td> ETHTOOL_OPTS </td>
<td> &nbsp;<wbr> </td>
<td> Fixed speed for the ethernet link. It is added as &quot;speed&quot; parameter in the ETHTOOL_OPTS variable.
</td>
</tr>
<tr VALIGN=top>
<td> duplex </td>
<td> ETHTOOL_OPTS </td>
<td> &nbsp;<wbr> </td>
<td> Fixed duplex mode for the ethernet link. It is added as &quot;duplex&quot; parameter in the ETHOOL_OPTS variable.
</td>
</tr>
<tr VALIGN=top>
<td> auto-negotiate </td>
<td> ETHTOOL_OPTS </td>
<td> &nbsp;<wbr> </td>
<td> Whether link speed and duplex autonegotiation is enabled. It is not saved only if disabled and no values are provided for the &quot;speed&quot; and &quot;duplex&quot; parameters (skips link configuration).
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> HWADDR </td>
<td> &nbsp;<wbr> </td>
<td> Hardware address of the device in traditional hex-digits-and-colons notation (e.g. 00:22:68:14:5A:05). Note that for initscripts this is the current MAC address of the device as found during ifup. For NetworkManager this is the permanent MAC address. Or in case no permanent MAC address exists, the MAC address initially configured on the device.
</td>
</tr>
<tr VALIGN=top>
<td> cloned-mac-address </td>
<td> MACADDR </td>
<td> &nbsp;<wbr> </td>
<td> Cloned (spoofed) MAC address in traditional hex-digits-and-colons notation (e.g. 00:22:68:14:5A:99).
</td>
</tr>
<tr VALIGN=top>
<td> generate-mac-address-mask </td>
<td> GENERATE_MAC_ADDRESS_MASK<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> the MAC address mask for generating randomized and stable cloned-mac-address.
</td>
</tr>
<tr VALIGN=top>
<td> mac-address-blacklist </td>
<td> HWADDR_BLACKLIST<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> It denies usage of the connection for any device whose address is listed.<code> </p>
<p> Example: </code>HWADDR_BLACKLIST=&quot;00:22:68:11:69:08 00:11:22:11:44:55&quot;
</td>
</tr>
<tr VALIGN=top>
<td> mtu </td>
<td> MTU </td>
<td> &nbsp;<wbr> </td>
<td> MTU of the interface.
</td>
</tr>
<tr VALIGN=top>
<td> s390-subchannels </td>
<td> SUBCHANNELS </td>
<td> &nbsp;<wbr> </td>
<td> Subchannels for IBM S390 hosts.<code> </p>
<p> Example: </code>SUBCHANNELS=0.0.b00a,0.0.b00b,0.0.b00c
</td>
</tr>
<tr VALIGN=top>
<td> s390-nettype </td>
<td> NETTYPE </td>
<td> &nbsp;<wbr> </td>
<td> Network type of the S390 host.<code> </p>
<p> Example: </code>NETTYPE=qeth<code> </p>
<p> Allowed values: </code>&quot;qeth&quot;, &quot;lcs&quot; or &quot;ctc&quot;
</td>
</tr>
<tr VALIGN=top>
<td> s390-options </td>
<td> OPTIONS and PORTNAME, CTCPROTO, </td>
<td> &nbsp;<wbr> </td>
<td> S390 device options. All options go to OPTIONS, except for &quot;portname&quot; and &quot;ctcprot&quot; that have their own variables.
</td>
</tr>
</table>
<p> <code>Table 17. 802-11-wireless-security setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> key-mgmt </td>
<td> KEY_MGMT<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Key management menthod.<code> </p>
<p> Allowed values: </code>IEEE8021X, WPA-PSK, WPA-EAP
</td>
</tr>
<tr VALIGN=top>
<td> wep-tx-keyidx </td>
<td> DEFAULTKEY </td>
<td> 1 </td>
<td> Index of active WEP key.<code> </p>
<p> Allowed values: </code>1, 2, 3, 4
</td>
</tr>
<tr VALIGN=top>
<td> auth-alg </td>
<td> SECURITYMODE<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Authentication algorithm for WEP.<code> </p>
<p> Allowed values: </code>restricted, open, leap
</td>
</tr>
<tr VALIGN=top>
<td> proto </td>
<td> WPA_ALLOW_WPA<i>(+)</i>, WPA_ALLOW_WPA2<i>(+)</i> </td>
<td> no </td>
<td> Allowed WPA protocols, WPA and WPA2 (RSN).<code> </p>
<p> Allowed values: </code>yes, no
</td>
</tr>
<tr VALIGN=top>
<td> pairwise </td>
<td> CIPHER_PAIRWISE<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Restrict pairwise encryption algorithms, specified as a space separated list.<code> </p>
<p> Allowed values: </code>CCMP, TKIP
</td>
</tr>
<tr VALIGN=top>
<td> group </td>
<td> CIPHER_GROUP<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Restrict group/broadcast encryption algorithms, specified as a space separated list.<code> </p>
<p> Allowed values: </code>CCMP, TKIP, WEP40, WEP104
</td>
</tr>
<tr VALIGN=top>
<td> leap-username </td>
<td> IEEE_8021X_IDENTITY<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Login name for LEAP.
</td>
</tr>
<tr VALIGN=top>
<td> wep-key0 </td>
<td> KEY1, KEY_PASSPHRASE1<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> The first WEP key (used in most networks). See also DEFAULTKEY for key index.
</td>
</tr>
<tr VALIGN=top>
<td> wep-key1 </td>
<td> KEY2, KEY_PASSPHRASE2<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> WEP key with index 1. See also DEFAULTKEY for key index.
</td>
</tr>
<tr VALIGN=top>
<td> wep-key2 </td>
<td> KEY3, KEY_PASSPHRASE3<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> WEP key with index 2. See also DEFAULTKEY for key index.
</td>
</tr>
<tr VALIGN=top>
<td> wep-key3 </td>
<td> KEY4, KEY_PASSPHRASE4<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> WEP key with index 3. See also DEFAULTKEY for key index.
</td>
</tr>
<tr VALIGN=top>
<td> wep-key-flags </td>
<td> WEP_KEY_FLAGS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password flags for KEY&lt;i&gt;, KEY_PASSPHRASE&lt;i&gt; password. (see the section called &#8220;Secret flags&#8221; for _FLAGS values)
</td>
</tr>
<tr VALIGN=top>
<td> psk </td>
<td> WPA_PSK </td>
<td> &nbsp;<wbr> </td>
<td> Pre-Shared-Key for WPA networks.
</td>
</tr>
<tr VALIGN=top>
<td> psk-flags </td>
<td> WPA_PSK_FLAGS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password flags for WPA_PSK_FLAGS. (see the section called &#8220;Secret flags&#8221; for _FLAGS values)<code> </p>
<p> Example: </code>WPA_PSK_FLAGS=user
</td>
</tr>
<tr VALIGN=top>
<td> leap-password </td>
<td> IEEE_8021X_PASSWORD<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password for LEAP. It can also go to &quot;key-&quot; lookaside file, or it can be owned by a secret agent.
</td>
</tr>
<tr VALIGN=top>
<td> leap-password-flags </td>
<td> IEEE_8021X_PASSWORD_FLAGS<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Password flags for IEEE_8021X_PASSWORD_FLAGS. (see the section called &#8220;Secret flags&#8221; for _FLAGS values)
</td>
</tr>
<tr VALIGN=top>
<td> wep-key-type </td>
<td> KEY&lt;i&gt; or KEY_PASSPHRASE&lt;i&gt;<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> KEY is used for &quot;key&quot; type (10 or 26 hexadecimal characters, or 5 or 13 character string prefixed with &quot;s:&quot;). KEY_PASSPHRASE is used for WEP passphrases.<code> </p>
<p> Example: </code>KEY1=s:ahoj, KEY1=0a1c45bc02, KEY_PASSPHRASE1=mysupersecretkey
</td>
</tr>
</table>
<p> <code>Table 18. 802-11-wireless setting</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Ifcfg-rh Variable </code></td>
<td><code> Default </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> ssid </td>
<td> ESSID </td>
<td> &nbsp;<wbr> </td>
<td> SSID of Wi-Fi network.<code> </p>
<p> Example: </code>ESSID=&quot;Quick Net&quot;
</td>
</tr>
<tr VALIGN=top>
<td> mode </td>
<td> MODE </td>
<td> &nbsp;<wbr> </td>
<td> Wi-Fi network mode.<code> </p>
<p> Allowed values: </code>Ad-Hoc, Managed (Auto) [case insensitive]
</td>
</tr>
<tr VALIGN=top>
<td> band </td>
<td> BAND<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> BAND alone is honored, but CHANNEL overrides BAND since it implies a band.<code> </p>
<p> Example: </code>BAND=bg<code> </p>
<p> Allowed values: </code>a, bg
</td>
</tr>
<tr VALIGN=top>
<td> channel </td>
<td> CHANNEL </td>
<td> &nbsp;<wbr> </td>
<td> Channel used for the Wi-Fi communication. Channels greater than 14 mean &quot;a&quot; band, otherwise the band is &quot;bg&quot;.<code> </p>
<p> Example: </code>CHANNEL=6
</td>
</tr>
<tr VALIGN=top>
<td> bssid </td>
<td> BSSID<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Restricts association only to a single AP.<code> </p>
<p> Example: </code>BSSID=00:1E:BD:64:83:21
</td>
</tr>
<tr VALIGN=top>
<td> rate </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> This property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> tx-power </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> This property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> HWADDR </td>
<td> &nbsp;<wbr> </td>
<td> Hardware address of the device in traditional hex-digits-and-colons notation (e.g. 00:22:68:14:5A:05). Note that for initscripts this is the current MAC address of the device as found during ifup. For NetworkManager this is the permanent MAC address. Or in case no permanent MAC address exists, the MAC address initially configured on the device.
</td>
</tr>
<tr VALIGN=top>
<td> cloned-mac-address </td>
<td> MACADDR </td>
<td> &nbsp;<wbr> </td>
<td> Cloned (spoofed) MAC address in traditional hex-digits-and-colons notation (e.g. 00:22:68:14:5A:99).
</td>
</tr>
<tr VALIGN=top>
<td> generate-mac-address-mask </td>
<td> GENERATE_MAC_ADDRESS_MASK<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> the MAC address mask for generating randomized and stable cloned-mac-address.
</td>
</tr>
<tr VALIGN=top>
<td> mac-address-blacklist </td>
<td> HWADDR_BLACKLIST<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> It denies usage of the connection for any device whose address is listed.
</td>
</tr>
<tr VALIGN=top>
<td> seen-bssids </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> This property is not handled by ifcfg-rh plugin.
</td>
</tr>
<tr VALIGN=top>
<td> mtu </td>
<td> MTU </td>
<td> &nbsp;<wbr> </td>
<td> MTU of the wireless interface.
</td>
</tr>
<tr VALIGN=top>
<td> hidden </td>
<td> SSID_HIDDEN<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Whether the network hides the SSID.
</td>
</tr>
<tr VALIGN=top>
<td> powersave </td>
<td> POWERSAVE<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Enables or disables Wi-Fi power saving.<code> </p>
<p> Example: </code>POWERSAVE=enable<code> </p>
<p> Allowed values: </code>default, ignore, enable, disable
</td>
</tr>
<tr VALIGN=top>
<td> mac-address-randomization </td>
<td> MAC_ADDRESS_RANDOMIZATION<i>(+)</i> </td>
<td> &nbsp;<wbr> </td>
<td> Enables or disables Wi-Fi MAC address randomization.<code> </p>
<p> Example: </code>MAC_ADDRESS_RANDOMIZATION=always<code> </p>
<p> Allowed values: </code>default, never, always
</td>
</tr>
<tr VALIGN=top>
<td> security </td>
<td> (none) </td>
<td> &nbsp;<wbr> </td>
<td> This property is deprecated and not handled by ifcfg-rh-plugin.
</td>
</tr>
</table>
<p> The following settings are not supported by <i>ifcfg-rh</i> plugin: </p>
<p> adsl, bluetooth, ppp, pppoe, serial, generic, gsm, cdma, 802-11-olpc-mesh, wimax, vpn, macvlan, vxlan, tun, ip-tunnel</p>
<h3>Secret flags</h3>
<p>Each secret property in a NetworkManager setting has an associated <i>flags</i> property that describes how to handle that secret. In the <i>fcfg-rh</i> plugin variables for secret flags have a <i>_FLAGS</i> suffix. The variables contain one or more of the following values (space separated). Missing (or empty) *_FLAGS variable means that the password is owned by NetworkManager. </p>
<dl>
<dd>&bull; user &#8211; a user-session secret agent is responsible for providing and storing this secret; when it is required, agents will be asked to provide it.</dl>
<dl>
<dd>&bull; ask &#8211; the associated password is not saved but it will be requested from the user each time it is required.</dl>
<dl>
<dd>&bull; unused &#8211; in some situations it cannot be automatically determined that a secret is required or not. This flag hints that the secret is not required and should not be requested from the user.</dl>
<h2>Files</h2>
<p>/etc/sysconfig/network-scripts/ifcfg-* </p>
<p> /etc/sysconfig/network-scripts/keys-* </p>
<p> /etc/sysconfig/network-scripts/route-* </p>
<p> /etc/sysconfig/network-scripts/route6-* </p>
<p> /usr/share/doc/initscripts/sysconfig.txt</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5), <code><a href="/docs/linux/man/5-nm-settings-keyfile/">nm-settings-keyfile</a></code>(5), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5), <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7) </p>
