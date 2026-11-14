---
title: "systemd-dnssd(5)"
name: "systemd-dnssd"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-dnssd/"
description: "systemd.dnssd – DNS-SD configuration"
---

<p>systemd.dnssd &#8211; DNS-SD configuration</p>
<h2>Synopsis</h2>
<p><i>network_service</i>.dnssd</p>
<h2>Description</h2>
<p>DNS-SD setup is performed by <code><a href="/docs/linux/man/8-systemd-resolved/">systemd-resolved</a></code>(8). </p>
<p> The main network service file must have the extension .dnssd; other extensions are ignored. </p>
<p> The .dnssd files are read from the files located in the system network directories /usr/lib/systemd/dnssd and /usr/local/lib/systemd/dnssd, the volatile runtime network directory /run/systemd/dnssd and the local administration network directory /etc/systemd/dnssd. All configuration files are collectively sorted and processed in lexical order, regardless of the directories in which they live. However, files with identical filenames replace each other. Files in /etc/ have the highest priority, files in /run/ take precedence over files with the same name in /lib/. This can be used to override a system-supplied configuration file with a local file if needed. </p>
<p> Along with the network service file foo.dnssd, a &quot;drop-in&quot; directory foo.dnssd.d/ may exist. All files with the suffix &quot;.conf&quot; from this directory will be parsed after the file itself is parsed. This is useful to alter or add configuration settings, without having to modify the main configuration file. Each drop-in file must have appropriate section headers. </p>
<p> In addition to /etc/systemd/dnssd, drop-in &quot;.d&quot; directories can be placed in /usr/lib/systemd/dnssd or /run/systemd/dnssd directories. Drop-in files in /etc/ take precedence over those in /run/ which in turn take precedence over those in /usr/lib/ or /usr/local/lib. Drop-in files under any of these directories take precedence over the main network service file wherever located.</p>
<h2>[Service] Section Options</h2>
<p>The network service file contains a [Service] section, which specifies a discoverable network service announced in a local network with Multicast DNS broadcasts. </p>
<p> <i>Name=</i></p>
<dl>
<dd>An instance name of the network service as defined in the section 4.1.1 of m[blue]<code>RFC 6763</code>m[]<font SIZE="-2">[1]</font>, e.g. &quot;webserver&quot;. </p>
<p> The option supports simple specifier expansion. The following expansions are understood: </p>
<p> <code>Table 1. Specifiers available</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Specifier </code></td>
<td><code> Meaning </code></td>
<td><code> Details </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%a&quot; </td>
<td> Architecture </td>
<td> A short string identifying the architecture of the local system. A string such as <code>x86</code>, <code>x86-64</code> or <code>arm64</code>. See the architectures defined for <i>ConditionArchitecture=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for a full list.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%A&quot; </td>
<td> Operating system image version </td>
<td> The operating system image version identifier of the running system, as read from the <i>IMAGE_VERSION=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%b&quot; </td>
<td> Boot ID </td>
<td> The boot ID of the running system, formatted as string. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%B&quot; </td>
<td> Operating system build ID </td>
<td> The operating system build identifier of the running system, as read from the <i>BUILD_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%H&quot; </td>
<td> Host name </td>
<td> The hostname of the running system.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%m&quot; </td>
<td> Machine ID </td>
<td> The machine ID of the running system, formatted as string. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%M&quot; </td>
<td> Operating system image identifier </td>
<td> The operating system image identifier of the running system, as read from the <i>IMAGE_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%o&quot; </td>
<td> Operating system ID </td>
<td> The operating system identifier of the running system, as read from the <i>ID=</i> field of /etc/os-release. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%v&quot; </td>
<td> Kernel release </td>
<td> Identical to <code>uname -r</code> output.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%w&quot; </td>
<td> Operating system version ID </td>
<td> The operating system version identifier of the running system, as read from the <i>VERSION_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%W&quot; </td>
<td> Operating system variant ID </td>
<td> The operating system variant identifier of the running system, as read from the <i>VARIANT_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%%&quot; </td>
<td> Single percent sign </td>
<td> Use &quot;%%&quot; in place of &quot;%&quot; to specify a single percent sign.
</td>
</tr>
</table>
</dl>
<p> <i>Type=</i></p>
<dl>
<dd>A type of the network service as defined in the section 4.1.2 of m[blue]<code>RFC 6763</code>m[]<font SIZE="-2">[1]</font>, e.g. &quot;_http._tcp&quot;.</dl>
<p> <i>Port=</i></p>
<dl>
<dd>An IP port number of the network service.</dl>
<p> <i>Priority=</i></p>
<dl>
<dd>A priority number set in <code>SRV</code> resource records corresponding to the network service.</dl>
<p> <i>Weight=</i></p>
<dl>
<dd>A weight number set in <code>SRV</code> resource records corresponding to the network service.</dl>
<p> <i>TxtText=</i></p>
<dl>
<dd>A whitespace-separated list of arbitrary key/value pairs conveying additional information about the named service in the corresponding TXT resource record, e.g. &quot;path=/portal/index.html&quot;. Keys and values can contain C-style escape sequences which get translated upon reading configuration files. </p>
<p> This option together with <i>TxtData=</i> may be specified more than once, in which case multiple TXT resource records will be created for the service. If the empty string is assigned to this option, the list is reset and all prior assignments will have no effect.</dl>
<p> <i>TxtData=</i></p>
<dl>
<dd>A whitespace-separated list of arbitrary key/value pairs conveying additional information about the named service in the corresponding TXT resource record where values are base64-encoded string representing any binary data, e.g. &quot;data=YW55IGJpbmFyeSBkYXRhCg==&quot;. Keys can contain C-style escape sequences which get translated upon reading configuration files. </p>
<p> This option together with <i>TxtText=</i> may be specified more than once, in which case multiple TXT resource records will be created for the service. If the empty string is assigned to this option, the list is reset and all prior assignments will have no effect.</dl>
<h2>Examples</h2>
<p><code>Example 1. HTTP service</code> </p>
<dl>
<dd>
<pre># /etc/systemd/dnssd/http.dnssd
[Service]
Name=%H
Type=_http._tcp
Port=80
TxtText=path=/stats/index.html t=temperature_sensor</pre>
</dl>
<p> This makes the http server running on the host discoverable in the local network given MulticastDNS is enabled on the network interface. </p>
<p> Now the utility &quot;resolvectl&quot; should be able to resolve the service to the host&#8217;s name: </p>
<dl>
<dd>
<pre>$ resolvectl service meteo._http._tcp.local
meteo._http._tcp.local: meteo.local:80 [priority=0, weight=0]
 169.254.208.106%senp0s21f0u2u4
 fe80::213:3bff:fe49:8aa%senp0s21f0u2u4
 path=/stats/index.html
 t=temperature_sensor
 (meteo/_http._tcp/local)
-- Information acquired via protocol mDNS/IPv6 in 4.0ms.
-- Data is authenticated: yes</pre>
</dl>
<p> &quot;Avahi&quot; running on a different host in the same local network should see the service as well: </p>
<dl>
<dd>
<pre>$ avahi-browse -a -r
+ enp3s0 IPv6 meteo Web Site local
+ enp3s0 IPv4 meteo Web Site local
= enp3s0 IPv6 meteo Web Site local
 hostname = [meteo.local]
 address = [fe80::213:3bff:fe49:8aa]
 port = [80]
 txt = [&quot;path=/stats/index.html&quot; &quot;t=temperature_sensor&quot;]
= enp3s0 IPv4 meteo Web Site local
 hostname = [meteo.local]
 address = [169.254.208.106]
 port = [80]
 txt = [&quot;path=/stats/index.html&quot; &quot;t=temperature_sensor&quot;]</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8), <code><a href="/docs/linux/man/1-resolvectl/">resolvectl</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>RFC 6763</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc6763">https://tools.ietf.org/html/rfc6763</a></dl>
