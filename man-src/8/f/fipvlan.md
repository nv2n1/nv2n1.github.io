---
title: "fipvlan(8)"
name: "fipvlan"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fipvlan/"
description: "fipvlan – Fibre Channel over Ethernet VLAN Discovery"
---

<p>fipvlan &#8211; Fibre Channel over Ethernet VLAN Discovery</p>
<h2>Synopsis</h2>
<p><code>fipvlan</code> [-c|&#8211;create] [-d|&#8211;debug] [-s|&#8211;start] [-m|&#8211;mode fabric|vn2vn] [-u|&#8211;link-up] <i>interfaces</i> </p>
<p> <code>fipvlan</code> -a|&#8211;auto [-c|&#8211;create] [-d|&#8211;debug] [-s|&#8211;start] [-m|&#8211;mode fabric|vn2vn] [-l|&#8211;link-retry <i>count</i>] [-u|&#8211;link-up] </p>
<p> <code>fipvlan</code> -h|&#8211;help </p>
<p> <code>fipvlan</code> -v|&#8211;version</p>
<h2>Description</h2>
<p>The <code>fipvlan</code> command performs Fibre Channel over Ethernet (FCoE) Initialization Protocol (FIP) VLAN Discovery over Ethernet interfaces. <code>fipvlan</code> can be used as a diagnostic tool to determine which VLANs have FCoE services available on a network, prior to configuring VLAN interfaces and the <i>Open-FCoE</i> initiator. <code>fipvlan</code> can also be used to create VLAN interfaces as they are discovered, and to start the <i>Open-FCoE</i> initiator. The <code>&#8211;create</code> and <code>&#8211;start</code> options are primarily intended to be used as part of an <i>Open-FCoE</i> boot solution. FCoE instances started in this way cannot be destroyed or reset by fcoeadm. </p>
<p> <code>fipvlan</code> takes a list of network interface names to run the VLAN discovery protocol over, or the <code>&#8211;auto</code> option to use all available Ethernet interfaces. </p>
<p> <code>fipvlan</code> will enable any interface which is found disabled. If no response is received on that interface it will be shutdown again when <code>fipvlan</code> terminates.</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;auto</code></p>
<dl>
<dd>Use all Ethernet interfaces currently available</dl>
<p> <code>-c</code>, <code>&#8211;create</code></p>
<dl>
<dd>Create network interfaces for discovered FCoE VLANs. If a VLAN device already exists for a discovered VLAN, a new VLAN device will not be created.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Enable debugging output</dl>
<p> <code>-s</code>, <code>&#8211;start</code></p>
<dl>
<dd>Start the <i>Open-FCoE</i> initiator on discovered FCoE VLANs</dl>
<p> <code>-m</code>, <code>&#8211;mode</code></p>
<dl>
<dd>fabric|vn2vn Specify whether VLAN discovery is performed in the default fabric mode, or in VN2VN mode.</dl>
<p> <code>-f</code>, <code>&#8211;suffix</code> <i>suffix</i></p>
<dl>
<dd>Append the specified string <i>suffix</i> to VLAN interface names.</dl>
<p> <code>-l</code>, <code>&#8211;link-retry</code> <i>count</i></p>
<dl>
<dd>Retry check for link up to <i>count</i> times. The link state is checked every 1000 ms. The default number of retries is 20.</dl>
<p> <code>-u</code>, <code>&#8211;link-up</code></p>
<dl>
<dd>Leave link up if a FIP response has been received.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display a help message with basic usage instructions</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display the <code>fipvlan</code> version string</dl>
<h2>Vlan Naming Conventions</h2>
<p>If a new VLAN device is created, it will have the name <i>dev</i>.<i>vlan</i>; where <i>dev</i> is the name of the Ethernet parent device and <i>vlan</i> is the discovered VLAN ID number. An optional suffix may be appended to this with the the <code>-f</code> command line option.</p>
<h2>Examples</h2>
<p>Display all discoverable VLANs with FCoE services </p>
<dl>
<dd>
<pre>fipvlan --auto</pre>
</dl>
<p> Discover FCoE VLANs on interface eth2, create VLAN devices and start the <i>Open-FCoE</i> initiator </p>
<dl>
<dd>
<pre>fipvlan --create --start eth2</pre>
</dl>
<p> In this example if FCoE services were available on VLAN 101 of network interface eth2, then a VLAN interface eth2.101 would be created and used as the parent device for the initiator.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fcoeadm/">fcoeadm</a></code>(8) <code><a href="/docs/linux/man/8-fcoemon/">fcoemon</a></code>(8)</p>
<h2>Support</h2>
<p><code>fipvlan</code> is part of the <i>fcoe-utils</i> package, maintained through the <i>Open-FCoE</i> project. Resources for both developers and users can be found at the <i>Open-FCoE</i> website <a rel="nofollow" href="http://open-fcoe.org/">http://open-fcoe.org/</a></p>
