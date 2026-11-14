---
title: "networkd-conf(5)"
name: "networkd-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-networkd-conf/"
description: "networkd.conf, networkd.conf.d – Global Network configuration files"
---

<p>networkd.conf, networkd.conf.d &#8211; Global Network configuration files</p>
<h2>Synopsis</h2>
<p>/etc/systemd/networkd.conf </p>
<p> /etc/systemd/networkd.conf.d/*.conf </p>
<p> /lib/systemd/networkd.conf.d/*.conf</p>
<h2>Description</h2>
<p>These configuration files control global network parameters. Currently the DHCP Unique Identifier (DUID).</p>
<h2>Configuration Directories And Precedence</h2>
<p>The default configuration is set during compilation, so configuration is only needed when it is necessary to deviate from those defaults. Initially, the main configuration file in /etc/systemd/ contains commented out entries showing the defaults as a guide to the administrator. Local overrides can be created by editing this file or by creating drop-ins, as described below. Using drop-ins for local configuration is recommended over modifications to the main configuration file. </p>
<p> In addition to the &quot;main&quot; configuration file, drop-in configuration snippets are read from /usr/lib/systemd/*.conf.d/, /usr/local/lib/systemd/*.conf.d/, and /etc/systemd/*.conf.d/. Those drop-ins have higher precedence and override the main configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence, and for options which accept a list of values, entries are collected as they occur in the sorted files. </p>
<p> When packages need to customize the configuration, they can install drop-ins under /usr/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. Drop-ins have to be used to override package drop-ins, since the main configuration file has lower precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file.</p>
<h2>[Network] Section Options</h2>
<p>The following options are available in the [Network] section: </p>
<p> <i>SpeedMeter=</i></p>
<dl>
<dd>Takes a boolean. If set to yes, then <code>systemd-networkd</code> measures the traffic of each interface, and <code>networkctl status </code><i>INTERFACE</i> shows the measured speed. Defaults to no.</dl>
<p> <i>SpeedMeterIntervalSec=</i></p>
<dl>
<dd>Specifies the time interval to calculate the traffic speed of each interface. If <i>SpeedMeter=no</i>, the value is ignored. Defaults to 10sec.</dl>
<p> <i>ManageForeignRoutingPolicyRules=</i></p>
<dl>
<dd>A boolean. When true, <code>systemd-networkd</code> will remove rules that are not configured in .network files (except for rules with protocol &quot;kernel&quot;). When false, it will not remove any foreign rules, keeping them even if they are not configured in a .network file. Defaults to yes.</dl>
<p> <i>ManageForeignRoutes=</i></p>
<dl>
<dd>A boolean. When true, <code>systemd-networkd</code> will remove routes that are not configured in .network files (except for routes with protocol &quot;kernel&quot;, &quot;dhcp&quot; when <i>KeepConfiguration=</i> is true or &quot;dhcp&quot;, and &quot;static&quot; when <i>KeepConfiguration=</i> is true or &quot;static&quot;). When false, it will not remove any foreign routes, keeping them even if they are not configured in a .network file. Defaults to yes.</dl>
<p> <i>RouteTable=</i></p>
<dl>
<dd>Defines the route table name. Takes a whitespace-separated list of the pairs of route table name and number. The route table name and number in each pair are separated with a colon, i.e., &quot;<i>name</i>:<i>number</i>&quot;. The route table name must not be &quot;default&quot;, &quot;main&quot;, or &quot;local&quot;, as these route table names are predefined with route table number 253, 254, and 255, respectively. The route table number must be an integer in the range 1&#8230;4294967295. This setting can be specified multiple times. If an empty string is specified, then the list specified earlier are cleared. Defaults to unset.</dl>
<h2>[Dhcpv4] Section Options</h2>
<p>This section configures the DHCP Unique Identifier (DUID) value used by DHCP protocol. DHCPv4 client protocol sends IAID and DUID to the DHCP server when acquiring a dynamic IPv4 address if <code>ClientIdentifier=duid</code>. IAID and DUID allows a DHCP server to uniquely identify the machine and the interface requesting a DHCP IP address. To configure IAID and ClientIdentifier, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5). </p>
<p> The following options are understood: </p>
<p> <i>DUIDType=</i></p>
<dl>
<dd>Specifies how the DUID should be generated. See m[blue]<code>RFC 3315</code>m[]<font SIZE="-2">[1]</font> for a description of all the options. </p>
<p> The following values are understood: </p>
<p> <code>vendor</code></p>
<dl>
<dd>If &quot;DUIDType=vendor&quot;, then the DUID value will be generated using &quot;43793&quot; as the vendor identifier (systemd) and hashed contents of <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5). This is the default if <i>DUIDType=</i> is not specified.</dl>
<p> <code>uuid</code></p>
<dl>
<dd>If &quot;DUIDType=uuid&quot;, and <i>DUIDRawData=</i> is not set, then the product UUID is used as a DUID value. If a system does not have valid product UUID, then an application-specific <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) is used as a DUID value. About the application-specific machine ID, see <code><a href="/docs/linux/man/3-sd_id128_get_machine_app_specific/">sd_id128_get_machine_app_specific</a></code>(3).</dl>
<p> <code>link-layer-time[:</code><i>TIME</i><code>]</code>, <code>link-layer</code></p>
<dl>
<dd>If &quot;link-layer-time&quot; or &quot;link-layer&quot; is specified, then the MAC address of the interface is used as a DUID value. The value &quot;link-layer-time&quot; can take additional time value after a colon, e.g. &quot;link-layer-time:2018-01-23 12:34:56 UTC&quot;. The default time value is &quot;2000-01-01 00:00:00 UTC&quot;.</dl>
<p> In all cases, <i>DUIDRawData=</i> can be used to override the actual DUID value that is used.</dl>
<p> <i>DUIDRawData=</i></p>
<dl>
<dd>Specifies the DHCP DUID value as a single newline-terminated, hexadecimal string, with each byte separated by &quot;:&quot;. The DUID that is sent is composed of the DUID type specified by <i>DUIDType=</i> and the value configured here. </p>
<p> The DUID value specified here overrides the DUID that <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) generates from the machine ID. To configure DUID per-network, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5). The configured DHCP DUID should conform to the specification in m[blue]<code>RFC 3315</code>m[]<font SIZE="-2">[2]</font>, m[blue]<code>RFC 6355</code>m[]<font SIZE="-2">[3]</font>. To configure IAID, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5). </p>
<p> <code>Example 1. A DUIDType=vendor with a custom value</code> </p>
<dl>
<dd>
<pre>DUIDType=vendor
DUIDRawData=00:00:ab:11:f9:2a:c2:77:29:f9:5c:00</pre>
</dl>
<p> This specifies a 14 byte DUID, with the type DUID-EN (&quot;00:02&quot;), enterprise number 43793 (&quot;00:00:ab:11&quot;), and identifier value &quot;f9:2a:c2:77:29:f9:5c:00&quot;.</dl>
<h2>[Dhcpv6] Section Options</h2>
<p>This section configures the DHCP Unique Identifier (DUID) value used by DHCPv6 protocol. DHCPv6 client protocol sends the DHCP Unique Identifier and the interface Identity Association Identifier (IAID) to a DHCPv6 server when acquiring a dynamic IPv6 address. IAID and DUID allows a DHCPv6 server to uniquely identify the machine and the interface requesting a DHCP IP address. To configure IAID, see <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5). </p>
<p> The following options are understood: </p>
<p> <i>DUIDType=</i>, <i>DUIDRawData=</i></p>
<dl>
<dd>As in the [DHCPv4] section.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/3-sd_id128_get_machine_app_specific/">sd_id128_get_machine_app_specific</a></code>(3)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>RFC 3315</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc3315#section-9">https://tools.ietf.org/html/rfc3315#section-9</a></dl>
<dt> 2.</p>
<dd>RFC 3315</p>
<dl>
<dd><a rel="nofollow" href="http://tools.ietf.org/html/rfc3315#section-9">http://tools.ietf.org/html/rfc3315#section-9</a></dl>
<dt> 3.</p>
<dd>RFC 6355</p>
<dl>
<dd><a rel="nofollow" href="http://tools.ietf.org/html/rfc6355">http://tools.ietf.org/html/rfc6355</a></dl>
