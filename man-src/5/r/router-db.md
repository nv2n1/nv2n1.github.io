---
title: "router-db(5)"
name: "router-db"
section: "5"
letter: "r"
url: "/docs/linux/man/5-router-db/"
description: "router.db – rancid group configuration file"
---

<p>router.db &#8211; rancid group configuration file</p>
<h2>Description</h2>
<p><code>router.db</code> contains information for devices which are members of a rancid group. <i><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></i>(1) reads this file to compile a list of devices which it should collect.</p>
<h2>Syntax</h2>
<p>One device is listed per-line, where the syntax is: </p>
<pre>&lt;device_name&gt;;&lt;device_type&gt;;&lt;state&gt;[;comments]</pre>
<p>For example: </p>
<pre>scooby.shrubbery.net;cisco;up</pre>
<p>The fields are as follows:</p>
<dl>
<dt><code>&lt;device_name&gt;</code></dt>
<dd>The name of the device, which must resolve via <i>gethostbyname</i>, used as the argument to <i><a href="/docs/linux/man/1-telnet/">telnet</a></i>(1), <i><a href="/docs/linux/man/1-rsh/">rsh</a></i>(1), or <i><a href="/docs/linux/man/1-ssh/">ssh</a></i>(1), to connect to the device. Once converted to lower-case, this also becomes the name of the file used to store the configuration under <i>$BASEDIR/&lt;group&gt;/configs</i>. </dd>
<p> Experience has shown that using the device&#8217;s FQDN (Fully Qualified Domain Name) works best, as in the example above.</p>
<dt><code>&lt;device_type&gt;</code></dt>
<dd>The type of device from the set:</dd>
<dl>
<dd>
</dd><dl>
<dd><code>agm</code> A Cisco Anomoly Guard Module (aka Riverhead). Suspect that at some point the UI will become more cisco-like and it can be merged with the IOS rancid module.</dd>
<dd><code>alteon</code> An Alteon WebOS switches.</dd>
<dd><code>arista</code> An Arista Networks device.</dd>
<dd><code>avocent</code> An Avocent Cyclades console server.</dd>
<dd><code>baynet</code> A Bay Networks router.</dd>
<dd><code>cat5</code> A Cisco catalyst series 5000 and 4000 switches (i.e.: running the catalyst OS, not IOS).</dd>
<dd><code>cisco</code> A Cisco router, PIX, or switch such as the 3500XL or 6000 running IOS (or IOS-like) OS, but not IOS-XR.</dd>
<dd><code>cisco-nx</code> A Cisco Nexus switch/router.</dd>
<dd><code>cisco-xr</code> A Cisco device running IOS-XR.</dd>
<dd><code>cisco-wlc</code> A Cisco Wireless Controller.</dd>
<dd><code>css</code> A Cisco content services switch.</dd>
<dd><code>enterasys</code> An enterasys NAS. This is currently an alias for the <code>riverstone</code> device type.</dd>
<dd><code>erx</code> A Juniper E-series edge router.</dd>
<dd><code>dell</code> A Dell switch. Known working models are DES-3010F, DES-3052P, DES-3526, and DES-3550. Note that Dell OEMs some equipment and has purchased some companies, so a Dell product may not work with the dell rancid module but may work with smc or force10.</dd>
<dd><code>extreme</code> An Extreme switch.</dd>
<dd><code>ezt3</code> An ADC-Kentrox EZ-T3 mux.</dd>
<dd><code>f5</code> A F5 BigIP switch.</dd>
<dd><code>force10</code> A Force10 router.</dd>
<dd><code>fortigate</code> A Fortinet firewall.</dd>
<dd><code>foundry</code> A Foundry router, switch, or router-switch. This includes HP Procurve switches that are OEMs of Foundry products, such as the HP9304M.</dd>
<dd><code>hitachi</code> A Hitachi router.</dd>
<dd><code>hp</code> A HP Procurve switch such as the 2524 or 4108 procurve switches. Also see the <code>foundry</code> type.</dd>
<dd><code>juniper</code> A Juniper router.</dd>
<dt><code>mikrotik</code></dt>
<dd>A Mikrotik router.</dd>
<dt><code>mrtd</code></dt>
<dd>A host running the (Merit) MRTd daemon.</dd>
<dd><code>netscalar</code> A Netscalar load balancer.</dd>
<dd><code>netscreen</code> A Netscreen firewall.</dd>
<dd><code>paloalto</code> A Palo Alto Networks device.</dd>
<dd><code>procket</code> A Procket router.</dd>
<dd><code>redback</code> A Redback router, NAS, etc.</dd>
<dd><code>riverstone</code> A Riverstone NAS or Cabletron (starting with version ~9.0.3) router.</dd>
<dd><code>smc</code> A SMC switch (some Dell OEMs).</dd>
<dd><code>ciscowlc</code> A Cisco WLC.</dd>
<dd><code>xirrus</code> A Xirrus array.</dd>
<dd><code>zebra</code> Zebra routing software.</dd></dl>
</dl>
<dt><code>&lt;state&gt;</code></dt>
<dd>The state is either &quot;up&quot;, or some other arbitrary value, e.g. &quot;down&quot;. If the device is not marked &quot;up&quot; the device&#8217;s configuration will not be collected. It is highly recommended that comments are made for any router not listed as up, so as to indicate the reason a router is not to be polled, e.g.: </dd>
<p> dial1.paris;cisco;up;<br/>
 core1.paris;cisco;down;in testing until 5/5/2001.<br/>
 core2.paris;cisco;ticketed;Ticket 6054234, 5/3/2001<br/>
 border1.paris;juniper;up; </p>
<p> The script &quot;downreport&quot; in util/ can be used to produce a report of routers in router.db that are not marked &quot;up&quot;.</dl>
<dl>
<dt><code>[comments]</code></dt>
<dd>Freeform string to describe the current state of the router.</dd></dl>
<p> A &#8220;#&#8221; at the begining of a line is a comment; the entire line is ignored. </p>
<p> If a device is deleted from the <code>router.db</code> file, then <code>rancid</code> will clean up by removing the device&#8217;s config file from <i>$BASEDIR/&lt;group&gt;/configs</i>. The device will be removed from the revision control system. It is possible, in most cases, to resurrect or check-out copies of deleted device configurations.</p>
<h2>Files</h2>
<dl>
<dt><code>$BASEDIR/&lt;group&gt;/router.db</code></dt>
<dd>Configuration file described here, where &lt;group&gt; is a device group name defined in the variable <i>LIST_OF_GROUPS</i> within <i>$BASEDIR/etc/rancid.conf</i>. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></code>(1), <code><a href="/docs/linux/man/1-rancid/">rancid</a></code>(1), <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5)</p>
<h2>History</h2>
<p>In RANCID releases prior to 3.0, <code>router.db</code> used colons (:) as its field separator. This was changed to allow IPv6 addresses to be used in router.db.</p>
