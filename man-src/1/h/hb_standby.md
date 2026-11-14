---
title: "hb_standby(1)"
name: "hb_standby"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hb_standby/"
description: "hb_standby – hb_standby is a simple linux-ha shell script. It issues a failover from the node where it is running to the other node, if available."
---

<h2>NAME</h2>
<p> hb_standby &#8211; hb_standby is a simple linux-ha shell script. It issues a failover from the node where it is running to the other node, if available.</p>
<h2>SYNOPSIS</h2>
<p> <code>hb_standby</code> [all|foreign|local|failback]</p>
<h2>DESCRIPTION</h2>
<p> The full path is usually /usr/lib/heartbeat/hb_standby. To get a list of the options to hb_standby issue the command, <code> &quot;/usr/lib/heartbeat/hb_standby &#8211;help&quot; </code>. NOTE: For historical reasons, unlike most scripts where failure to specify an option gives you the list of possible options, failure to provide an option to hb_standby is equivalent to &quot;hb_standby all&quot;. </p>
<p> The meaning of the options is relative. For this sample haresources file: </p>
<p> nodea drbddisk::r0 Filesystem::/dev/drbd0::/local/groups::ext3 10.0.0.1 smb </p>
<p> nodeb drbddisk::r1 Filesystem::/dev/drbd1::/local/ldap::ext3 10.0.0.2 ldap </p>
<dl>
<dt><code>hb_standby local</code></p>
<dd> When run on nodea, means migrate any resources that nodea is the preferred node for. In this case Samba would be shutdown, the IP address 10.0.0.1 would be released, /local/groups would be unmounted, /dev/drbd0 would be placed into secondary and nodeb would take all these services over. When run on nodeb, OpenLDAP would shutdown, 10.0.0.2 would be released, /local/ldap would be unmounted, /dev/drbd1 would be placed into Secondary mode and nodea would take over all these services. </p>
<dt><code>hb_standby foreign</code></p>
<dd> When run on nodea, means migrate any resources that nodea is NOT the preferred node for. In this case OpenLDAP would shutdown, 10.0.0.2 would be released, /local/ldap would be unmounted, /dev/drbd1 would be placed into Secondary mode and nodeb would take over all these services. When run on nodeb, Samba would be shutdown, the IP address 10.0.0.1 would be released, /local/groups would be unmounted, /dev/drbd0 would be placed into secondary and nodea would take all these services over. </p>
<dt><code>hb_standby all</code></p>
<dd> Regardless of which node it&#8217;s run on means to release all resources so the other node takes over all resources. </p>
<dt><code>hb_standby</code></p>
<dd> Without an argument is the same as &quot;hb_standby all&quot; </p>
<dt><code>hb_standby failback</code></p>
<dd> Same as &quot;hb_standby foreign&quot; </p>
</dl>
<h2>CAVEATS</h2>
<p> <code>hb_standby</code> is only usable in R1-style configurations (i.e., those configured using the <i>haresources</i> file). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-hb_takeover/">hb_takeover</a>(1), <a href="/docs/linux/man/8-heartbeat/">heartbeat</a>(8), <a href="/docs/linux/man/1-cl_status/">cl_status</a>(1) </p>
<h2>DOCUMENTATION</h2>
<p> More information may be found at <a rel="nofollow" href="http://linux-ha.org/hb_standby">http://linux-ha.org/hb_standby</a> </p>
<h2>AUTHORS</h2>
<p> linux-ha &#8212; Alan Robertson &lt;alanr [at] unix.sh&gt; <i>et al</i>. </p>
<p> man page &#8212; Guochun Shi &lt;gshi [at] ncsa.uiuc.edu&gt; </p>
<h2>Index</h2>
