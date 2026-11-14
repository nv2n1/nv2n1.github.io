---
title: "hostnamectl(1)"
name: "hostnamectl"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hostnamectl/"
description: "hostnamectl – Control the system hostname"
---

<h2 class="name">NAME</h2>
<p> hostnamectl &#8211; Control the system hostname </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>hostnamectl</code> [OPTIONS&#8230;] {COMMAND}</dl>
<h2>DESCRIPTION</h2>
<p> <code>hostnamectl</code></p>
<dd>may be used to query and change the system hostname and related settings. </p>
<p> <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8) and this tool distinguish three different hostnames: the high-level &quot;pretty&quot; hostname which might include all kinds of special characters (e.g. &quot;Lennart&#8217;s Laptop&quot;), the &quot;static&quot; hostname which is the user-configured hostname (e.g. &quot;lennarts-laptop&quot;), and the transient hostname which is a fallback value received from network configuration (e.g. &quot;node12345678&quot;). If a static hostname is set to a valid value, then the transient hostname is not used. </p>
<p> Note that the pretty hostname has little restrictions on the characters and length used, while the static and transient hostnames are limited to the usually accepted characters of Internet domain names, and 64 characters at maximum (the latter being a Linux limitation). </p>
<p> Use <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) to initialize the system hostname for mounted (but not booted) system images.</p>
<h2>COMMANDS</h2>
<p> The following commands are understood: </p>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Show system hostname and related information. If no command is specified, this is the implied default.</dl>
<p> <code>hostname</code> [<i>NAME</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the system hostname. If an optional argument <i>NAME</i> is provided then the command changes the system hostname to <i>NAME</i>. By default, this will alter the pretty, the static, and the transient hostname alike; however, if one or more of <code>&#8211;static</code>, <code>&#8211;transient</code>, <code>&#8211;pretty</code> are used, only the selected hostnames are changed. If the pretty hostname is being set, and static or transient are being set as well, the specified hostname will be simplified in regards to the character set used before the latter are updated. This is done by removing special characters and spaces. This ensures that the pretty and the static hostname are always closely related while still following the validity rules of the specific name. This simplification of the hostname string is not done if only the transient and/or static hostnames are set, and the pretty hostname is left untouched. </p>
<p> The static and transient hostnames must each be either a single DNS label (a string composed of 7-bit ASCII lower-case characters and no spaces or dots, limited to the format allowed for DNS domain name labels), or a sequence of such labels separated by single dots that forms a valid DNS FQDN. The hostname must be at most 64 characters, which is a Linux limitation (DNS allows longer names).</dl>
<p> <code>icon-name</code> [<i>NAME</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the icon name of the system. If an optional argument <i>NAME</i> is provided then the command changes the icon name to <i>NAME</i>. The icon name is used by some graphical applications to visualize this host. The icon name should follow the m[blue]<code>Icon Naming Specification</code>m[]<font SIZE="-2">[1]</font>.</dl>
<p> <code>chassis</code> [<i>TYPE</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the chassis type. If an optional argument <i>TYPE</i> is provided then the command changes the chassis type to <i>TYPE</i>. The chassis type is used by some graphical applications to visualize the host or alter user interaction. Currently, the following chassis types are defined: &quot;desktop&quot;, &quot;laptop&quot;, &quot;convertible&quot;, &quot;server&quot;, &quot;tablet&quot;, &quot;handset&quot;, &quot;watch&quot;, &quot;embedded&quot;, as well as the special chassis types &quot;vm&quot; and &quot;container&quot; for virtualized systems that lack an immediate physical chassis.</dl>
<p> <code>deployment</code> [<i>ENVIRONMENT</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the deployment environment. If an optional argument <i>ENVIRONMENT</i> is provided then the command changes the deployment environment to <i>ENVIRONMENT</i>. Argument <i>ENVIRONMENT</i> must be a single word without any control characters. One of the following is suggested: &quot;development&quot;, &quot;integration&quot;, &quot;staging&quot;, &quot;production&quot;.</dl>
<p> <code>location</code> [<i>LOCATION</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the location string for the system. If an optional argument <i>LOCATION</i> is provided then the command changes the location string for the system to <i>LOCATION</i>. Argument <i>LOCATION</i> should be a human-friendly, free-form string describing the physical location of the system, if it is known and applicable. This may be as generic as &quot;Berlin, Germany&quot; or as specific as &quot;Left Rack, 2nd Shelf&quot;.</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Do not query the user for authentication for privileged operations.</dl>
<p> <code>&#8211;static</code>, <code>&#8211;transient</code>, <code>&#8211;pretty</code></p>
<dl>
<dt>
<dd> If <code>status</code> is invoked (or no explicit command is given) and one of these switches is specified, <code>hostnamectl</code> will print out just this selected hostname. </p>
<p> If used with <code>set-hostname</code>, only the selected hostname(s) will be updated. When more than one of these switches are specified, all the specified hostnames will be updated.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;json=</code><i>MODE</i></p>
<dl>
<dt>
<dd> Shows output formatted as JSON. Expects one of &quot;short&quot; (for the shortest possible output without any redundant whitespace or line breaks), &quot;pretty&quot; (for a pretty version of the same, with indentation and line breaks) or &quot;off&quot; (to turn off JSON output, the default).</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1), <code><a href="/docs/linux/man/5-hostname/">hostname</a></code>(5), <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Icon Naming Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html">http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html</a></dl>
</dl>
<h2>Index</h2>
