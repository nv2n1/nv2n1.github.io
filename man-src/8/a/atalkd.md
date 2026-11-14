---
title: "atalkd(8)"
name: "atalkd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atalkd/"
description: "atalkd – AppleTalk RTMP, NBP, ZIP, and AEP manager"
---

<p>atalkd &#8211; AppleTalk RTMP, NBP, ZIP, and AEP manager</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>atalkd</code> [-f&nbsp;<wbr><i>configfile</i>] [-1] [-2]</dl>
<h2>Description</h2>
<p><code>atalkd</code></p>
<dd>is responsible for all user level AppleTalk network management. This includes routing, name registration and lookup, zone lookup, and the AppleTalk Echo Protocol (similar to <code><a href="/docs/linux/man/8-ping/">ping</a></code>(8)). <code>atalkd</code> is typically started at boot time, out of /etc/rc. It first reads from its configuration file, /etc/atalk//atalkd.conf. If there is no configuration file, <code>atalkd</code> will attempt to configure all available interfaces and will create a configuration file. The file consists of a series of interfaces, one per line. Lines with `#&#8217; in the first column are ignored, as are blank lines. The syntax is </p>
<p> <i>interface</i> [ <code>-seed</code> ] [ <code>-phase</code> <i>number</i> ] [ <code>-net</code> <i>net-range</i> ] [ <code>-addr</code> <i>address</i> ] [ <code>-zone</code> <i>zonename</i> ] &#8230; </p>
<p> Note that all fields except the interface are optional. The loopback interface is configured automatically. If <code>-seed</code> is specified, all other fields must be present. Also, <code>atalkd</code> will exit during bootstrapping, if a router disagrees with its seed information. If <code>-seed</code> is not given, all other information may be overriden during auto-configuration. If no <code>-phase</code> option is given, the default phase as given on the command line is used (the default is 2). If <code>-addr</code> is given and <code>-net</code> is not, a net-range of one is assumed. </p>
<p> The first -zone directive for each interface is the &#8220;default&#8221; zone. Under Phase 1, there is only one zone. Under Phase 2, all routers on the network are configured with the default zone and must agree. <code>atalkd</code> maps &#8220;*&#8221; to the default zone of the first interface. Note: The default zone for a machine is determined by the configuration of the local routers; to appear in a non-default zone, each service, e.g. <code>afpd</code>, must individually specify the desired zone. See also <code><a href="/docs/linux/man/3-nbp_name/">nbp_name</a></code>(3).</p>
<h2>Routing</h2>
<p>If you are connecting a netatalk router to an existing AppleTalk internet, you should first contact your local network administrators to obtain appropriate network addresses. </p>
<p> <code>atalkd</code> can provide routing between interfaces by configuring multiple interfaces. Each interface must be assigned a unique net-range between 1 and 65279 (0 and 65535 are illegal, and addresses between 65280 and 65534 are reserved for startup). It is best to choose the smallest useful net-range, i.e. if you have three machines on an Ethernet, don&#8217;t chose a net-range of 1000-2000. Each net-range may have an arbitrary list of zones associated with it.</p>
<h2>Examples</h2>
<p>Below is an example configuration file for a sun4/40. The machine has two interfaces, &#8220;le0&#8221; and &#8220;le1&#8221;. The &#8220;le0&#8221; interface is configured automatically from other routers on the network. The machine is the only router for the &#8220;le1&#8221; interface. </p>
<dl>
<dd>
<pre> le0
 le1 -seed -net 9461-9471 -zone netatalk -zone Argus</pre>
</dl>
<p> <code>atalkd</code> automatically acts as a router if there is more than one interface.</p>
<h2>Files</h2>
<p>/etc/atalk//atalkd.conf configuration file</p>
<h2>Bugs</h2>
<p>On some systems, <code>atalkd</code> can not be restarted.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-atalkd-conf/">atalkd.conf</a></code>(5) </p>
