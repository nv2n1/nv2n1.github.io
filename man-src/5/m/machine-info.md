---
title: "machine-info(5)"
name: "machine-info"
section: "5"
letter: "m"
url: "/docs/linux/man/5-machine-info/"
description: "machine-info – Local machine information file"
---

<p>machine-info &#8211; Local machine information file</p>
<h2>Synopsis</h2>
<p>/etc/machine-info</p>
<h2>Description</h2>
<p>The /etc/machine-info file contains machine metadata. </p>
<p> The basic file format of machine-info is a newline-separated list of environment-like shell-compatible variable assignments. It is possible to source the configuration from shell scripts, however, beyond mere variable assignments no shell features are supported, allowing applications to read the file without implementing a shell compatible execution engine. </p>
<p> /etc/machine-info contains metadata about the machine that is set by the user or administrator. The settings configured here have the highest precedence. When not set, appropriate values may be determined automatically, based on the information about the hardware or other configuration files. It is thus completely fine for this file to not be present. </p>
<p> You may use <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1) to change the settings of this file from the command line.</p>
<h2>Options</h2>
<p>The following machine metadata parameters may be set using /etc/machine-info: </p>
<p> <i>PRETTY_HOSTNAME=</i></p>
<dl>
<dd>A pretty human-readable UTF-8 machine identifier string. This should contain a name like &quot;Lennart&#8217;s Laptop&quot; which is useful to present to the user and does not suffer by the syntax limitations of internet domain names. If possible, the internet hostname as configured in /etc/hostname should be kept similar to this one. Example: if this value is &quot;Lennart&#8217;s Computer&quot; an Internet hostname of &quot;lennarts-computer&quot; might be a good choice. If this parameter is not set, an application should fall back to the Internet hostname for presentation purposes.</dl>
<p> <i>ICON_NAME=</i></p>
<dl>
<dd>An icon identifying this machine according to the m[blue]<code>XDG Icon Naming Specification</code>m[]<font SIZE="-2">[1]</font>. If this parameter is not set, an application should fall back to &quot;computer&quot; or a similar icon name.</dl>
<p> <i>CHASSIS=</i></p>
<dl>
<dd>The chassis type. Currently, the following chassis types are defined: &quot;desktop&quot;, &quot;laptop&quot;, &quot;convertible&quot;, &quot;server&quot;, &quot;tablet&quot;, &quot;handset&quot;, &quot;watch&quot;, and &quot;embedded&quot;, as well as the special chassis types &quot;vm&quot; and &quot;container&quot; for virtualized systems that lack an immediate physical chassis. </p>
<p> Note that most systems allow detection of the chassis type automatically (based on firmware information or suchlike). This setting should only be used to override a misdetection or to manually configure the chassis type where automatic detection is not available.</dl>
<p> <i>DEPLOYMENT=</i></p>
<dl>
<dd>Describes the system deployment environment. One of the following is suggested: &quot;development&quot;, &quot;integration&quot;, &quot;staging&quot;, &quot;production&quot;.</dl>
<p> <i>LOCATION=</i></p>
<dl>
<dd>Describes the system location if applicable and known. Takes a human-friendly, free-form string. This may be as generic as &quot;Berlin, Germany&quot; or as specific as &quot;Left Rack, 2nd Shelf&quot;.</dl>
<h2>Example</h2>
<dl>
<dd>
<pre>PRETTY_HOSTNAME=&quot;Lennart's Tablet&quot;
ICON_NAME=computer-tablet
CHASSIS=tablet
DEPLOYMENT=production</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5), <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>XDG Icon Naming Specification</p>
<dl>
<dd><a rel="nofollow" href="http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html">http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html</a></dl>
