---
title: "atalkd(5)"
name: "atalkd"
section: "5"
letter: "a"
url: "/docs/linux/man/5-atalkd/"
description: "atalkd.conf – Configuration file used by"
---

<p>atalkd.conf &#8211; Configuration file used by </p>
<p><a href="/docs/linux/man/8-atalkd/">atalkd</a>(8) to determine the interfaces used by the master Netatalk daemon</p>
<h2>Description</h2>
<p><code>/etc/atalk//atalkd.conf</code> is the configuration file used by atalkd to configure the Appletalk interfaces and their behavior </p>
<p> Any line not prefixed with <code>#</code> is interpreted. The configuration lines are composed like: </p>
<p> <i>Interface</i> <code>[</code> <i>options</i> <code>]</code> </p>
<p> The simplest case is to have either no atalkd.conf, or to have one that has no active lines. In this case, atalkd should auto-discover the local interfaces on the machine. Please note that you cannot split lines. </p>
<p> The interface is the network interface that this to work over, such as <code>eth0</code> for Linux, or <code>le0</code> for Sun. </p>
<p> The possible options and their meanings are: </p>
<p> <code>-addr </code><i>net.node</i></p>
<dl>
<dd>Allows specification of the net and node numbers for this interface, specified in Appletalk numbering format (example: <code>-addr 66.6</code>).</dl>
<p> <code>-dontroute</code></p>
<dl>
<dd>Disables Appletalk routing. It is the opposite of <code>-router</code>.</dl>
<p> <code>-net first[-last]</code></p>
<dl>
<dd>Allows the available net to be set, optionally as a range.</dl>
<p> <code>-noallmulti</code> (linux only)</p>
<dl>
<dd>On linux the interfaces, atalkd uses, are set to ALLMULTI by default caused by countless NICs having problems without being forced into this mode (some even don&#8217;t work with allmulti set). In case, you&#8217;ve a NIC known to support multicasts properly, you might want to set this option causing less packets to be processed</dl>
<p> <code>-phase ( 1 | 2 )</code></p>
<dl>
<dd>Specifies the Appletalk phase that this interface is to use (either Phase 1 or Phase 2).</dl>
<p> <code>-router</code></p>
<dl>
<dd>Like <code>-seed</code>, but allows single interface routing. It is the opposite of <code>-dontroute</code>.</dl>
<p> <code>-seed</code></p>
<dl>
<dd>The seed option only works if you have multiple interfaces. It also causes all missing arguments to be automagically configured from the network.</dl>
<p> <code>-zone </code><i>zonename</i></p>
<dl>
<dd>Specifies a specific zone that this interface should appear on (example: <code>-zone &quot;Parking Lot&quot;</code>). Please note that zones with spaces and other special characters should be enclosed in parentheses.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8) </p>
