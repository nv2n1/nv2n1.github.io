---
title: "nm-settings-keyfile(5)"
name: "nm-settings-keyfile"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nm-settings-keyfile/"
description: "nm-settings-keyfile – Description of keyfile settings plugin"
---

<p>nm-settings-keyfile &#8211; Description of <i>keyfile</i> settings plugin</p>
<h2>Description</h2>
<p>NetworkManager is based on the concept of connection profiles that contain network configuration (see <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5) for details). The profiles can be stored in various formats. NetworkManager uses plugins for reading and writing the data. The plugins can be configured in <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5). </p>
<p> The <i>keyfile</i> plugin is the generic plugin that supports all the connection types and capabilities that NetworkManager has. The files are in a .ini-style format and located in /etc/NetworkManager/system-connections/, /usr/lib/NetworkManager/system-connections/ and /run/NetworkManager/system-connections/. This plugin is always enabled and will automatically be used to store any connections that are not supported by any other active plugin. For security, it will ignore files that are readable or writable by any user other than &#8216;root&#8217; since private keys and passphrases may be stored in plaintext inside the file.</p>
<h2>File Format</h2>
<p>The <i>keyfile</i> config format is a simple .ini-style format. It consists of sections (groups) of key-value pairs. Each section corresponds to a setting name as described in the settings specification (<code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5)). Each configuration key/value pair in the section is one of the properties listed in the settings specification. The majority of properties of the specification is written in the same format into the <i>keyfile</i> too. However some values are inconvenient for people to use. These are stored in the files in more readable ways. These properties are described below. An example could be IP addresses that are not written as integer arrays, but more reasonably as &quot;1.2.3.4/12 1.2.3.254&quot;. More information of the generic key file format can be found at m[blue]<code>GLib key file format</code>m[]<font SIZE="-2">[1]</font> (Lines beginning with a &#8216;#&#8217; are comments, lists are separated by character ; etc.). </p>
<p> Users can create or modify the <i>keyfile</i> connection files manually, even if that is not the recommended way of managing the profiles. However, if they choose to do that, they must inform NetworkManager about their changes (for example via <i>nmcli con (re)load</i>). </p>
<p> <code>Examples of keyfile configuration</code>. </p>
<dl>
<dd>
<pre><code>A sample configuration for an ethernet network:</code>
[connection]
id=Main eth0
uuid=27afa607-ee36-43f0-b8c3-9d245cdc4bb3
type=802-3-ethernet
autoconnect=true
[ipv4]
method=auto
[802-3-ethernet]
mac-address=00:23:5a:47:1f:71</pre>
</dl>
<dl>
<dd>
<pre><code>A sample configuration for WPA-EAP (PEAP with MSCHAPv2) and always-ask secret:</code>
[connection]
id=CompanyWIFI
uuid=cdac6154-a33b-4b15-9904-666772cfa5ee
type=wifi
autoconnect=false
[wifi]
ssid=CorpWLAN
mode=infrastructure
security=802-11-wireless-security
[wifi-security]
key-mgmt=wpa-eap
[ipv4]
method=auto
[ipv6]
method=auto
[802-1x]
eap=peap;
identity=joe
ca-cert=/home/joe/.cert/corp.crt
phase1-peapver=1
phase2-auth=mschapv2
password-flags=2</pre>
</dl>
<dl>
<dd>
<pre><code>A sample configuration for openvpn:</code>
[connection]
id=RedHat-openvpn
uuid=7f9b3356-b210-4c0e-8123-bd116c9c280f
type=vpn
timestamp=1385401165
[vpn]
service-type=org.freedesktop.NetworkManager.openvpn
connection-type=password
password-flags=3
remote=ovpn.my-company.com
cipher=AES-256-CBC
reneg-seconds=0
port=443
username=joe
ca=/etc/openvpn/ISCA.pem
tls-remote=ovpn.my-company.com
[ipv6]
method=auto
[ipv4]
method=auto
ignore-auto-dns=true
never-default=true</pre>
</dl>
<dl>
<dd>
<pre><code>A sample configuration for a bridge and a bridge port:</code>
[connection] [connection]
id=MainBridge id=br-port-1
uuid=171ae855-a0ab-42b6-bd0c-60f5812eea9d uuid=d6e8ae98-71f8-4b3d-9d2d-2e26048fe794
interface-name=MainBridge interface-name=em1
type=bridge type=ethernet
 master=MainBridge
[bridge] slave-type=bridge
interface-name=MainBridge</pre>
</dl>
<dl>
<dd>
<pre><code>A sample configuration for a VLAN:</code>
[connection]
id=VLAN for building 4A
uuid=8ce1c9e0-ce7a-4d2c-aa28-077dda09dd7e
interface-name=VLAN-4A
type=vlan
[vlan]
interface-name=VLAN-4A
parent=eth0
id=4</pre>
</dl>
<h2>Details</h2>
<p><i>keyfile</i> plugin variables for the majority of NetworkManager properties have one-to-one mapping. It means a NetworkManager property is stored in the keyfile as a variable of the same name and in the same format. There are several exceptions to this rule, mainly for making keyfile syntax easier for humans. The exceptions handled specially by <i>keyfile</i> plugin are listed below. Refer to <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5) for all available settings and properties and their description. </p>
<p> <code>Name aliases</code>. Some of the NetworkManager setting names are somewhat hard to type or remember. Therefore <i>keyfile</i> introduces aliases that can be used instead of the names.</p>
<dl>
<dd><i>setting name keyfile alias</i></dl>
<dl>
<dd>802-3-ethernet = ethernet</dl>
<dl>
<dd>802-11-wireless = wifi</dl>
<dl>
<dd>802-11-wireless-security = wifi-security</dl>
<p> <code>Table 1. bridge setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> mac-address </td>
<td> usual hex-digits-and-colons notation </td>
<td> MAC address in traditional hex-digits-and-colons notation, or semicolon separated list of 6 decimal bytes (obsolete)<code> </p>
<p> Example: </code>mac-address=00:22:68:12:79:A2 mac-address=0;34;104;18;121;162;
</td>
</tr>
</table>
<p> <code>Table 2. infiniband setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> mac-address </td>
<td> usual hex-digits-and-colons notation </td>
<td> MAC address in traditional hex-digits-and-colons notation, or or semicolon separated list of 20 decimal bytes (obsolete)<code> </p>
<p> Example: </code>mac-address= 80:00:00:6d:fe:80:00:00:00:00:00:00:00:02:55:00:70:33:cf:01
</td>
</tr>
</table>
<p> <code>Table 3. ipv4 setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> dns </td>
<td> dns </td>
<td> list of DNS IP addresses </td>
<td> List of DNS servers.<code> </p>
<p> Example: </code>dns=1.2.3.4;8.8.8.8;8.8.4.4;
</td>
</tr>
<tr VALIGN=top>
<td> addresses </td>
<td> address1, address2, &#8230; </td>
<td> address/plen </td>
<td> List of static IP addresses.<code> </p>
<p> Example: </code>address1=192.168.100.100/24 address2=10.1.1.5/24
</td>
</tr>
<tr VALIGN=top>
<td> gateway </td>
<td> gateway </td>
<td> string </td>
<td> Gateway IP addresses as a string.<code> </p>
<p> Example: </code>gateway=192.168.100.1
</td>
</tr>
<tr VALIGN=top>
<td> routes </td>
<td> route1, route2, &#8230; </td>
<td> route/plen[,gateway,metric] </td>
<td> List of IP routes.<code> </p>
<p> Example: </code>route1=8.8.8.0/24,10.1.1.1,77 route2=7.7.0.0/16
</td>
</tr>
</table>
<p> <code>Table 4. ipv6 setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> dns </td>
<td> dns </td>
<td> list of DNS IP addresses </td>
<td> List of DNS servers.<code> </p>
<p> Example: </code>dns=2001:4860:4860::8888;2001:4860:4860::8844;
</td>
</tr>
<tr VALIGN=top>
<td> addresses </td>
<td> address1, address2, &#8230; </td>
<td> address/plen </td>
<td> List of static IP addresses.<code> </p>
<p> Example: </code>address1=abbe::cafe/96 address2=2001::1234
</td>
</tr>
<tr VALIGN=top>
<td> gateway </td>
<td> gateway </td>
<td> string </td>
<td> Gateway IP addresses as a string.<code> </p>
<p> Example: </code>gateway=abbe::1
</td>
</tr>
<tr VALIGN=top>
<td> routes </td>
<td> route1, route2, &#8230; </td>
<td> route/plen[,gateway,metric] </td>
<td> List of IP routes.<code> </p>
<p> Example: </code>route1=2001:4860:4860::/64,2620:52:0:2219:222:68ff:fe11:5403
</td>
</tr>
</table>
<p> <code>Table 5. serial setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> parity </td>
<td> parity </td>
<td> &#8216;e&#8217;, &#8216;o&#8217;, or &#8216;n&#8217; </td>
<td> The connection parity; even, odd, or none. Note that older versions of NetworkManager stored this as an integer: 69 (&#8216;E&#8217;) for even, 111 (&#8216;o&#8217;) for odd, or 110 (&#8216;n&#8217;) for none.<code> </p>
<p> Example: </code>parity=n
</td>
</tr>
</table>
<p> <code>Table 6. vpn setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> data </td>
<td> separate variables named after keys of the dictionary </td>
<td> &nbsp; </td>
<td> The keys of the data dictionary are used as variable names directly under [vpn] section.<code> </p>
<p> Example: </code>remote=ovpn.corp.com cipher=AES-256-CBC username=joe
</td>
</tr>
<tr VALIGN=top>
<td> secrets </td>
<td> separate variables named after keys of the dictionary </td>
<td> &nbsp; </td>
<td> The keys of the secrets dictionary are used as variable names directly under [vpn-secrets] section.<code> </p>
<p> Example: </code>password=Popocatepetl
</td>
</tr>
</table>
<p> <code>Table 7. wifi-p2p setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> peer </td>
<td> peer </td>
<td> usual hex-digits-and-colons notation </td>
<td> MAC address in traditional hex-digits-and-colons notation (e.g. 00:22:68:12:79:A2), or semicolon separated list of 6 bytes (obsolete) (e.g. 0;34;104;18;121;162).
</td>
</tr>
</table>
<p> <code>Table 8. 802-3-ethernet setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> mac-address </td>
<td> usual hex-digits-and-colons notation </td>
<td> MAC address in traditional hex-digits-and-colons notation (e.g. 00:22:68:12:79:A2), or semicolon separated list of 6 bytes (obsolete) (e.g. 0;34;104;18;121;162)
</td>
</tr>
<tr VALIGN=top>
<td> cloned-mac-address </td>
<td> cloned-mac-address </td>
<td> usual hex-digits-and-colons notation </td>
<td> Cloned MAC address in traditional hex-digits-and-colons notation (e.g. 00:22:68:12:79:B2), or semicolon separated list of 6 bytes (obsolete) (e.g. 0;34;104;18;121;178).
</td>
</tr>
<tr VALIGN=top>
<td> mac-address-blacklist </td>
<td> mac-address-blacklist </td>
<td> list of MACs (separated with semicolons) </td>
<td> MAC address blacklist.<code> </p>
<p> Example: </code>mac-address-blacklist= 00:22:68:12:79:A6;00:22:68:12:79:78
</td>
</tr>
</table>
<p> <code>Table 9. 802-11-wireless setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> ssid </td>
<td> ssid </td>
<td> string (or decimal-byte list &#8211; obsolete) </td>
<td> SSID of Wi-Fi network.<code> </p>
<p> Example: </code>ssid=Quick Net
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> mac-address </td>
<td> usual hex-digits-and-colons notation </td>
<td> MAC address in traditional hex-digits-and-colons notation (e.g. 00:22:68:12:79:A2), or semicolon separated list of 6 bytes (obsolete) (e.g. 0;34;104;18;121;162).
</td>
</tr>
<tr VALIGN=top>
<td> cloned-mac-address </td>
<td> cloned-mac-address </td>
<td> usual hex-digits-and-colons notation </td>
<td> Cloned MAC address in traditional hex-digits-and-colons notation (e.g. 00:22:68:12:79:B2), or semicolon separated list of 6 bytes (obsolete) (e.g. 0;34;104;18;121;178).
</td>
</tr>
<tr VALIGN=top>
<td> mac-address-blacklist </td>
<td> mac-address-blacklist </td>
<td> list of MACs (separated with semicolons) </td>
<td> MAC address blacklist.<code> </p>
<p> Example: </code>mac-address-blacklist= 00:22:68:12:79:A6;00:22:68:12:79:78
</td>
</tr>
</table>
<p> <code>Table 10. wpan setting (section)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Property </code></td>
<td><code> Keyfile Variable </code></td>
<td><code> Format </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> mac-address </td>
<td> mac-address </td>
<td> usual hex-digits-and-colons notation </td>
<td> MAC address in hex-digits-and-colons notation (e.g. 76:d8:9b:87:66:60:84:ee).
</td>
</tr>
</table>
<h3>Secret flags</h3>
<p>Each secret property in a NetworkManager setting has an associated <i>flags</i> property that describes how to handle that secret. In the <i>keyfile</i> plugin, the value of <i>-flags</i> variable is a decimal number (0 &#8211; 7) defined as a sum of the following values: </p>
<dl>
<dd>&bull; 0 &#8211; (NM owned) &#8211; the system is responsible for providing and storing this secret.</dl>
<dl>
<dd>&bull; 1 &#8211; (agent-owned) &#8211; a user-session secret agent is responsible for providing and storing this secret; when it is required, agents will be asked to provide it.</dl>
<dl>
<dd>&bull; 2 &#8211; (not-saved) &#8211; this secret should not be saved but should be requested from the user each time it is required.</dl>
<dl>
<dd>&bull; 4 &#8211; (not-required) &#8211; in some situations it cannot be automatically determined that a secret is required or not. This flag hints that the secret is not required and should not be requested from the user.</dl>
<h2>Files</h2>
<p>/etc/NetworkManager/system-connections/*</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5), <code><a href="/docs/linux/man/5-nm-settings-ifcfg-rh/">nm-settings-ifcfg-rh</a></code>(5), <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5), <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>GLib key file format</p>
<dl>
<dd><a rel="nofollow" href="https://developer.gnome.org/glib/stable/glib-Key-value-file-parser.html#glib-Key-value-file-parser.description">https://developer.gnome.org/glib/stable/glib-Key-value-file-parser.html#glib-Key-value-file-parser.description</a></dl>
