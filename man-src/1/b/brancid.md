---
title: "brancid(1)"
name: "brancid"
section: "1"
letter: "b"
url: "/docs/linux/man/1-brancid/"
description: "rancid – Cisco configuration filter"
---

<h2>NAME</h2>
<p> rancid &#8211; Cisco configuration filter</p>
<h2>SYNOPSIS</h2>
<p> <code>rancid</code> [<code>-dlCV</code>] [<code>-t device_type</code>] (<code>-f</code> filename | hostname) </p>
<p> <code>rancid</code> [<code>-dhlCV</code>] <code>-t device_type</code> (<code>-f</code> filename | hostname)</p>
<h2>DESCRIPTION</h2>
<p> <code>rancid</code> is a collection of <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) scripts which uses the login scripts (see <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1)) to login to a device, execute commands to display the configuration, etc, then filters the output for formatting, security, and so on. <code>rancid&#8217;s</code> product is a file with the name of it&#8217;s last argument plus the suffix .new. For example, <i>hostname.new</i>. </p>
<p> <code>rancid</code> is also a <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) script that operates much like <code>rancid,</code> but is generic and will eventually obsolete the <code>rancid</code> script. It uses the device_type specified with the -t option to look-up a device description that defines what it does to collect and process device information. </p>
<p> There are scripts complementary to <code>rancid</code> for other platforms and/or manufacturers that are supported by <code><a href="/docs/linux/man/1-rancid/">rancid</a></code>(1). Briefly, these are: </p>
<dl>
<dt><code>agmrancid</code></p>
<dd> Cisco Anomaly Guard Module (AGM)</p>
<dt><code>arancid</code></p>
<dd> Alteon WebOS switches</p>
<dt><code>arrancid</code></p>
<dd> Arista Networks devices</p>
<dt><code>brancid</code></p>
<dd> Bay Networks (nortel)</p>
<dt><code>cat5rancid</code></p>
<dd> Cisco catalyst switches</p>
<dt><code>cssrancid</code></p>
<dd> Cisco content services switches</p>
<dt><code>erancid</code></p>
<dd> ADC-kentrox EZ-T3 mux</p>
<dt><code>f10rancid</code></p>
<dd> Force10</p>
<dt><code>f5rancid</code></p>
<dd> F5 BigIPs</p>
<dt><code>fnrancid</code></p>
<dd> Fortinet Firewalls</p>
<dt><code>rancid</code></p>
<dd> The generic rancid script; supporting Allied Telesis AW+ devices, Arbor Networks Appliances, Cisco IOS, Cisco IOS-XR, Cisco WLC, Dell switches, Compass EOS, and Juniper JUNOS. It uses the device O/S modules for parsing routines. See <code><a href="/docs/linux/man/3-rancid/">rancid</a></code>(3) for details.</p>
<dt><code>hrancid</code></p>
<dd> HP Procurve Switches</p>
<dt><code>htranicd</code></p>
<dd> Hitachi Routers</p>
<dt><code>jerancid</code></p>
<dd> Juniper Networks E-series</p>
<dt><code>jrancid</code></p>
<dd> Juniper Networks</p>
<dt><code>mrancid</code></p>
<dd> MRTd</p>
<dt><code>mtrancid</code></p>
<dd> Mikrotik routesrs</p>
<dt><code>nrancid</code></p>
<dd> Netscreen firewalls</p>
<dt><code>nsrancid</code></p>
<dd> Netscaler</p>
<dt><code>nxrancid</code></p>
<dd> Cisco Nexus boxes</p>
<dt><code>prancid</code></p>
<dd> Procket Networks</p>
<dt><code>rivrancid</code></p>
<dd> Riverstone</p>
<dt><code>rrancid</code></p>
<dd> Redback</p>
<dt><code>srancid</code></p>
<dd> SMC switch (some Dell OEMs)</p>
<dt><code>trancid</code></p>
<dd> Netopia sDSL/T1 routers</p>
<dt><code>tntrancid</code></p>
<dd> Lucent TNT</p>
<dt><code>xirancid</code></p>
<dd> Xirrus arrays</p>
<dt><code>xrancid</code></p>
<dd> Extreme switches</p>
<dt><code>xrrancid</code></p>
<dd> Cisco IOS-XR boxes</p>
<dt><code>zrancid</code></p>
<dd> Zebra routing software</dl>
<p> The command-line options are as follows:</p>
<dl>
<dt><code>-C</code></p>
<dd> Prints the login command that would be used to collect data from the device.</p>
<dt><code>-V</code></p>
<dd> Prints package name and version strings.</p>
<dt><code>-d</code></p>
<dd> Display debugging information.</p>
<dt><code>-h</code></p>
<dd> Display a usage line and exit.</p>
<dt><code>-l</code></p>
<dd> Display somewhat less debugging information.</p>
<dt><code>-t</code></p>
<dd> Device type, of the given host or file, that is defined in <code>rancid.types.base</code> or <code>rancid.types.conf .</code></p>
<dt><code>-f</code></p>
<dd> <code>rancid</code> should interpret the next argument as a filename which contains the output it would normally collect from the device ( <i>hostname</i>) with <i><a href="/docs/linux/man/1-clogin/">clogin</a></i>(1).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></code>(1), <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1), <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), <code><a href="/docs/linux/man/5-rancid-types-conf/">rancid.types.conf</a></code>(5), <code><a href="/docs/linux/man/3-rancid/">rancid</a></code>(3)</p>
<h2>CAVEATS</h2>
<p> Cisco IOS offers a DHCP server that maintains a text database which can be stored remotely or on local storage. If stored locally, the file changes constantly and causes constant diffs from rancid. If this file&#8217;s name (&#8216;ip dhcp database&#8217;) matches the regex dhcp_[^[:space:].].txt, it will be filtered. </p>
<p> For Catalyst switches running CatOS, type <code>cat5,</code> the prompt must end with &#8216;&gt;&#8217;. <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1) looks for &#8216;&gt;&#8217; to determine when a login is successful. For example: </p>
<pre>
cat5k&gt;
cat5k&gt; enable
Password: 
cat5k&gt; (enable) 
</pre>
<p> <code>rancid</code> works on Cisco Catalyst 1900 series switches that are running Enterprise Edition software. This software provides a menu at connection time that allows a command line interface to be used by entering &#8216;K&#8217; at the prompt. </p>
<h2>Index</h2>
