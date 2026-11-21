---
title: "xirancid(1)"
name: "xirancid"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xirancid/"
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
<dt><code>agmrancid</code></dt>
<dd> Cisco Anomaly Guard Module (AGM)</dd>
<dt><code>arancid</code></dt>
<dd> Alteon WebOS switches</dd>
<dt><code>arrancid</code></dt>
<dd> Arista Networks devices</dd>
<dt><code>brancid</code></dt>
<dd> Bay Networks (nortel)</dd>
<dt><code>cat5rancid</code></dt>
<dd> Cisco catalyst switches</dd>
<dt><code>cssrancid</code></dt>
<dd> Cisco content services switches</dd>
<dt><code>erancid</code></dt>
<dd> ADC-kentrox EZ-T3 mux</dd>
<dt><code>f10rancid</code></dt>
<dd> Force10</dd>
<dt><code>f5rancid</code></dt>
<dd> F5 BigIPs</dd>
<dt><code>fnrancid</code></dt>
<dd> Fortinet Firewalls</dd>
<dt><code>rancid</code></dt>
<dd> The generic rancid script; supporting Allied Telesis AW+ devices, Arbor Networks Appliances, Cisco IOS, Cisco IOS-XR, Cisco WLC, Dell switches, Compass EOS, and Juniper JUNOS. It uses the device O/S modules for parsing routines. See <code><a href="/docs/linux/man/3-rancid/">rancid</a></code>(3) for details.</dd>
<dt><code>hrancid</code></dt>
<dd> HP Procurve Switches</dd>
<dt><code>htranicd</code></dt>
<dd> Hitachi Routers</dd>
<dt><code>jerancid</code></dt>
<dd> Juniper Networks E-series</dd>
<dt><code>jrancid</code></dt>
<dd> Juniper Networks</dd>
<dt><code>mrancid</code></dt>
<dd> MRTd</dd>
<dt><code>mtrancid</code></dt>
<dd> Mikrotik routesrs</dd>
<dt><code>nrancid</code></dt>
<dd> Netscreen firewalls</dd>
<dt><code>nsrancid</code></dt>
<dd> Netscaler</dd>
<dt><code>nxrancid</code></dt>
<dd> Cisco Nexus boxes</dd>
<dt><code>prancid</code></dt>
<dd> Procket Networks</dd>
<dt><code>rivrancid</code></dt>
<dd> Riverstone</dd>
<dt><code>rrancid</code></dt>
<dd> Redback</dd>
<dt><code>srancid</code></dt>
<dd> SMC switch (some Dell OEMs)</dd>
<dt><code>trancid</code></dt>
<dd> Netopia sDSL/T1 routers</dd>
<dt><code>tntrancid</code></dt>
<dd> Lucent TNT</dd>
<dt><code>xirancid</code></dt>
<dd> Xirrus arrays</dd>
<dt><code>xrancid</code></dt>
<dd> Extreme switches</dd>
<dt><code>xrrancid</code></dt>
<dd> Cisco IOS-XR boxes</dd>
<dt><code>zrancid</code></dt>
<dd> Zebra routing software</dd></dl>
<p> The command-line options are as follows:</p>
<dl>
<dt><code>-C</code></dt>
<dd> Prints the login command that would be used to collect data from the device.</dd>
<dt><code>-V</code></dt>
<dd> Prints package name and version strings.</dd>
<dt><code>-d</code></dt>
<dd> Display debugging information.</dd>
<dt><code>-h</code></dt>
<dd> Display a usage line and exit.</dd>
<dt><code>-l</code></dt>
<dd> Display somewhat less debugging information.</dd>
<dt><code>-t</code></dt>
<dd> Device type, of the given host or file, that is defined in <code>rancid.types.base</code> or <code>rancid.types.conf .</code></dd>
<dt><code>-f</code></dt>
<dd> <code>rancid</code> should interpret the next argument as a filename which contains the output it would normally collect from the device ( <i>hostname</i>) with <i><a href="/docs/linux/man/1-clogin/">clogin</a></i>(1).</dd></dl>
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
