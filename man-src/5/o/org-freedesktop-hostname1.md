---
title: "org-freedesktop-hostname1(5)"
name: "org-freedesktop-hostname1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-hostname1/"
description: "org.freedesktop.hostname1 – The D-Bus interface of systemd-hostnamed"
---

<p>org.freedesktop.hostname1 &#8211; The D-Bus interface of systemd-hostnamed</p>
<h2>Introduction</h2>
<p><code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8) is a system service that can be used to control the hostname and related machine metadata from user programs. This page describes the hostname semantics and the D-Bus interface.</p>
<h2>The D-Bus Api</h2>
<p>The service exposes the following interfaces on the bus: </p>
<dl>
<dd>
<pre>node /org/freedesktop/hostname1 {
 interface org.freedesktop.hostname1 {
 methods:
 SetHostname(in s hostname,
 in b interactive);
 SetStaticHostname(in s hostname,
 in b interactive);
 SetPrettyHostname(in s hostname,
 in b interactive);
 SetIconName(in s icon,
 in b interactive);
 SetChassis(in s chassis,
 in b interactive);
 SetDeployment(in s deployment,
 in b interactive);
 SetLocation(in s location,
 in b interactive);
 GetProductUUID(in b interactive,
 out ay uuid);
 Describe(out s json);
 properties:
 readonly s Hostname = '...';
 readonly s StaticHostname = '...';
 readonly s PrettyHostname = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s DefaultHostname = '...';
 readonly s HostnameSource = '...';
 readonly s IconName = '...';
 readonly s Chassis = '...';
 readonly s Deployment = '...';
 readonly s Location = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KernelName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KernelRelease = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s KernelVersion = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s OperatingSystemPrettyName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s OperatingSystemCPEName = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HomeURL = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HardwareVendor = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s HardwareModel = '...';
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<p> Whenever the hostname or other metadata is changed via the daemon, <code>PropertyChanged</code> signals are sent out to subscribed clients. Changing a hostname using this interface is authenticated via m[blue]<code>polkit</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>Semantics</h2>
<p>The <i>StaticHostname</i> property exposes the &quot;static&quot; hostname configured in /etc/hostname. It is not always in sync with the current hostname as returned by the <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3) system call. If no static hostname is configured this property will be the empty string. </p>
<p> When <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) or <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8) set the hostname, this static hostname <i>has the highest priority</i>. </p>
<p> The <i>Hostname</i> property exposes the actual hostname configured in the kernel via <code><a href="/docs/linux/man/3-sethostname/">sethostname</a></code>(3). It can be different from the static hostname. This property is never empty. </p>
<p> The <i>PrettyHostname</i> property exposes the <i>pretty hostname</i> which is a free-form UTF-8 hostname for presentation to the user. User interfaces should ensure that the pretty hostname and the static hostname stay in sync. E.g. when the former is &quot;Lennart&#8217;s Computer&quot; the latter should be &quot;lennarts-computer&quot;. If no pretty hostname is set this setting will be the empty string. Applications should then find a suitable fallback, such as the dynamic hostname. </p>
<p> The <i>DefaultHostname</i> property exposes the default hostname (configured through <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5), or a fallback set at compilation time). </p>
<p> The <i>HostnameSource</i> property exposes the origin of the currently configured hostname. One of &quot;static&quot; (set from /etc/hostname), &quot;transient&quot; (a non-permanent hostname from an external source), &quot;default&quot; (the value from os-release or the compiled-in fallback). </p>
<p> The <i>IconName</i> property exposes the <i>icon name</i> following the XDG icon naming spec. If not set, information such as the chassis type (see below) is used to find a suitable fallback icon name (i.e. &quot;computer-laptop&quot; vs. &quot;computer-desktop&quot; is picked based on the chassis information). If no such data is available, the empty string is returned. In that case an application should fall back to a replacement icon, for example &quot;computer&quot;. If this property is set to the empty string, the automatic fallback name selection is enabled again. </p>
<p> The <i>Chassis</i> property exposes a <i>chassis type</i>, one of the currently defined chassis types: &quot;desktop&quot;, &quot;laptop&quot;, &quot;server&quot;, &quot;tablet&quot;, &quot;handset&quot;, as well as the special chassis types &quot;vm&quot; and &quot;container&quot; for virtualized systems. Note that in most cases the chassis type will be determined automatically from DMI/SMBIOS/ACPI firmware information. Writing to this setting is hence useful only to override misdetected chassis types, or to configure the chassis type if it could not be auto-detected. Set this property to the empty string to reenable the automatic detection of the chassis type from firmware information. </p>
<p> Note that systemd-hostnamed starts only on request and terminates after a short idle period. This effectively means that <code>PropertyChanged</code> messages are not sent out for changes made directly on the files (as in: administrator edits the files with vi). This is the intended behavior: manual configuration changes should require manual reloading. </p>
<p> The transient (dynamic) hostname exposed by the <i>Hostname</i> property maps directly to the kernel hostname. This hostname should be assumed to be highly dynamic, and hence should be watched directly, without depending on <code>PropertyChanged</code> messages from systemd-hostnamed. To accomplish this, open /proc/sys/kernel/hostname and <code><a href="/docs/linux/man/3-poll/">poll</a></code>(3) for <code>SIGHUP</code> which is triggered by the kernel every time the hostname changes. Again: this is special for the transient (dynamic) hostname, and does not apply to the configured (fixed) hostname. </p>
<p> Applications may read the hostname data directly if hostname change notifications are not necessary. Use <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3), /etc/hostname (possibly with per-distribution fallbacks), and <code><a href="/docs/linux/man/3-machine-info/">machine-info</a></code>(3) for that. For more information on these files and syscalls see the respective man pages. </p>
<p> <i>KernelName</i>, <i>KernelRelease</i>, and <i>KernelVersion</i> expose the kernel name (e.g. &quot;Linux&quot;), release (e.g. &quot;5.0.0-11&quot;), and version (i.e. the build number, e.g. &quot;#11&quot;) as reported by <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2). <i>OperatingSystemPrettyName</i>, <i>OperatingSystemCPEName</i>, and <i>HomeURL</i> expose the <i>PRETTY_NAME=</i>, <i>CPE_NAME=</i> and <i>HOME_URL=</i> fields from <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5). The purpose of those properties is to allow remote clients to access this information over D-Bus. Local clients can access the information directly.</p>
<h3>Methods</h3>
<p><code>SetHostname()</code> sets the transient (dynamic) hostname, which is used if no static hostname is set. This value must be an internet-style hostname, 7-bit lowercase ASCII, no special chars/spaces. An empty string will unset the transient hostname. </p>
<p> <code>SetStaticHostname()</code> sets the static hostname which is exposed by the <i>StaticHostname</i> property. When called with an empty argument, the static configuration in /etc/hostname is removed. Since the static hostname has the highest priority, calling this function usually affects also the <i>Hostname</i> property and the effective hostname configured in the kernel. </p>
<p> <code>SetPrettyHostname()</code> sets the pretty hostname which is exposed by the <i>PrettyHostname</i> property. </p>
<p> <code>SetIconName()</code>, <code>SetChassis()</code>, <code>SetDeployment()</code>, and <code>SetLocation()</code> set the properties <i>IconName</i> (the name of the icon representing for the machine), <i>Chassis</i> (the machine form factor), <i>Deployment</i> (the system deployment environment), and <i>Location</i> (physical system location), respectively. </p>
<p> <i>PrettyHostname</i>, <i>IconName</i>, <i>Chassis</i>, <i>Deployment</i>, and <i>Location</i> are stored in /etc/machine-info. See <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5) for the semantics of those settings. </p>
<p> <code>GetProductUUID()</code> returns the &quot;product UUID&quot; as exposed by the kernel based on DMI information in /sys/class/dmi/id/product_uuid. Reading the file directly requires root privileges, and this method allows access to unprivileged clients through the polkit framework. </p>
<p> <code>Describe()</code> returns a JSON representation of all properties in one.</p>
<h3>Security</h3>
<p>The <i>interactive</i> boolean parameters can be used to control whether polkit should interactively ask the user for authentication credentials if required. </p>
<p> The polkit action for <code>SetHostname()</code> is org.freedesktop.hostname1.set-hostname. For <code>SetStaticHostname()</code> and <code>SetPrettyHostname()</code> it is org.freedesktop.hostname1.set-static-hostname. For <code>SetIconName()</code>, <code>SetChassis()</code>, <code>SetDeployment()</code> and <code>SetLocation()</code> it is org.freedesktop.hostname1.set-machine-info.</p>
<h2>Recommendations</h2>
<p>Here are three examples that show how the pretty hostname and the icon name should be used: </p>
<dl>
<dd>&bull; When registering DNS-SD services: use the pretty hostname in the service name, and pass the icon name in the TXT data, if there is an icon name. Browsing clients can then show the server icon on each service. This is especially useful for WebDAV applications or UPnP media sharing.</dl>
<dl>
<dd>&bull; Set the bluetooth name to the pretty hostname.</dl>
<dl>
<dd>&bull; When your file browser has a &quot;Computer&quot; icon, replace the name with the pretty hostname if set, and the icon with the icon name, if it is set.</dl>
<p> To properly handle name lookups with changing local hostnames without having to edit /etc/hosts, we recommend using systemd-hostnamed in combination with <code><a href="/docs/linux/man/3-nss-myhostname/">nss-myhostname</a></code>(3). </p>
<p> Here are some recommendations to follow when generating a static (internet) hostname from a pretty name: </p>
<dl>
<dd>&bull; Generate a single DNS label only, not an FQDN. That means no dots allowed. Strip them, or replace them with &quot;-&quot;.</dl>
<dl>
<dd>&bull; It&#8217;s probably safer to not use any non-ASCII chars, even if DNS allows this in some way these days. In fact, restrict your charset to &quot;a-zA-Z0-9&quot; and &quot;-&quot;. Strip other chars, or try to replace them in some smart way with chars from this set, for example &quot;ä&quot; → &quot;ae&quot;, and use &quot;-&quot; as the replacement for all punctuation characters and whitespace.</dl>
<dl>
<dd>&bull; Try to avoid creating repeated &quot;-&quot;, as well as &quot;-&quot; as the first or last char.</dl>
<dl>
<dd>&bull; Limit the hostname to 63 chars, which is the length of a DNS label.</dl>
<dl>
<dd>&bull; If after stripping special chars the empty string is the result, you can pass this as-is to systemd-hostnamed in which case it will automatically use a suitable fallback.</dl>
<dl>
<dd>&bull; Uppercase charaacters should be replaced with their lowercase equivalents.</dl>
<p> Note that while systemd-hostnamed applies some checks to the hostname you pass they are much looser than the recommendations above. For example, systemd-hostnamed will also accept &quot;_&quot; in the hostname, but we recommend not using this to avoid clashes with DNS-SD service types. Also systemd-hostnamed allows longer hostnames, but because of the DNS label limitations, we recommend not making use of this. </p>
<p> Here are a couple of example conversions: </p>
<dl>
<dd>&bull; &quot;Lennart&#8217;s PC&quot; → &quot;lennarts-pc&quot;</dl>
<dl>
<dd>&bull; &quot;Müllers Computer&quot; → &quot;muellers-computer&quot;</dl>
<dl>
<dd>&bull; &quot;Voran!&quot; → &quot;voran&quot;</dl>
<dl>
<dd>&bull; &quot;Es war einmal ein Männlein&quot; → &quot;es-war-einmal-ein-maennlein&quot;</dl>
<dl>
<dd>&bull; &quot;Jawoll. Ist doch wahr!&quot; → &quot;jawoll-ist-doch-wahr&quot;</dl>
<dl>
<dd>&bull; &quot;レナート&quot; → &quot;localhost&quot;</dl>
<dl>
<dd>&bull; &quot;&#8230;zack!!! zack!&#8230;&quot; → &quot;zack-zack&quot;</dl>
<p> Of course, an already valid internet hostname label you enter and pass through this conversion should stay unmodified, so that users have direct control of it, if they want &#8212; by simply ignoring the fact that the pretty hostname is pretty and just edit it as if it was the normal internet name.</p>
<h2>Versioning</h2>
<p>These D-Bus interfaces follow m[blue]<code>the usual interface versioning guidelines</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Examples</h2>
<p><code>Example 1. Introspect org.freedesktop.hostname1 on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system \
 --dest org.freedesktop.hostname1 \
 --object-path /org/freedesktop/hostname1</pre>
</dl>
<h2>See Also</h2>
<p>David Zeuthen&#8217;s original Fedora m[blue]<code>Feature page about xdg-hostname</code>m[]<font SIZE="-2">[3]</font></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>polkit</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/software/polkit/docs/latest/">https://www.freedesktop.org/software/polkit/docs/latest/</a></dl>
<dt> 2.</p>
<dd>the usual interface versioning guidelines</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/versioning-dbus.html">http://0pointer.de/blog/projects/versioning-dbus.html</a></dl>
<dt> 3.</p>
<dd>Feature page about xdg-hostname</p>
<dl>
<dd><a rel="nofollow" href="https://fedoraproject.org/wiki/Features/BetterHostname">https://fedoraproject.org/wiki/Features/BetterHostname</a></dl>
