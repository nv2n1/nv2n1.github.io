---
title: "corosync-notifyd(8)"
name: "corosync-notifyd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-notifyd/"
description: "corosync-notifyd – Listen for important corosync events and send dbus and/or snmp traps."
---

<p>corosync-notifyd &#8211; Listen for important corosync events and send dbus and/or snmp traps.</p>
<h2>Synopsis</h2>
<p><code>corosync-notifyd [-f] [-l] [-o] [-s] [-m] [manager] [-d] [-h]</code></p>
<h2>Description</h2>
<p><code>corosync-notifyd</code> uses corosync API to listen for important cluster events and can log them, generate dbus signals or genterate snmp traps.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Start application in foreground.</p>
<dt><code>-l</code></p>
<dd>Log all events.</p>
<dt><code>-o</code></p>
<dd>Print events to stdout (turns on -l).</p>
<dt><code>-s</code></p>
<dd>Send SNMP traps on all events.</p>
<dt><code>-m</code></p>
<dd>Set the SNMP manager address.</p>
<dt><code>-d</code></p>
<dd>Send DBUS signals on all events.</p>
<dt><code>-h</code></p>
<dd>Print this help</dl>
<h2>Examples</h2>
<p>$ corosync-notifyd -o<br />
 corosync-notifyd[18505]: troll[23374016] corosync-notify:18505:12 is now connected to corosync<br />
 corosync-notifyd[18505]: troll[23374016] corosync-notify:18505:13 is now disconnected from corosync<br />
 corosync-notifyd[18505]: troll[23374016] is now quorate<br />
 corosync-notifyd[18505]: r2[1550100672] ip:192.168.100.92 joined<br />
 corosync-notifyd[18505]: r2[1550100672] ip:192.168.100.92 left </p>
<p> $ corosync-notifyd -d<br />
 Note this output below is from &quot;dbus-monitor &#8211;system&quot; </p>
<pre><code>signal sender=:1.216 -&gt; dest=(null destination) serial=2 path=/com/redhat/cluster/corosync;

interface=com.redhat.cluster.corosync; member=ConnectionStateChange


string &quot;troll&quot;


uint32 23374016


string &quot;corosync-notify:18900:12&quot;


string &quot;connected&quot;

signal sender=:1.216 -&gt; dest=(null destination) serial=3 path=/com/redhat/cluster/corosync;

interface=com.redhat.cluster.corosync; member=ConnectionStateChange


string &quot;troll&quot;


uint32 23374016


string &quot;corosync-notify:18900:13&quot;


string &quot;disconnected&quot;

signal sender=:1.216 -&gt; dest=(null destination) serial=4 path=/com/redhat/cluster/corosync;

interface=com.redhat.cluster.corosync; member=QorumStateChange


string &quot;troll&quot;


uint32 23374016


string &quot;quorate&quot;

signal sender=:1.216 -&gt; dest=(null destination) serial=5 path=/com/redhat/cluster/corosync;

interface=com.redhat.cluster.corosync; member=NodeStateChange


string &quot;r2&quot;


uint32 1550100672


string &quot;192.168.100.92&quot;


string &quot;joined&quot;

signal sender=:1.216 -&gt; dest=(null destination) serial=6 path=/com/redhat/cluster/corosync;

interface=com.redhat.cluster.corosync; member=NodeStateChange


string &quot;r2&quot;


uint32 1550100672


string &quot;192.168.100.92&quot;


string &quot;left&quot;</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync/">corosync</a></code>(8), <code><a href="/docs/linux/man/8-corosync-cmapctl/">corosync-cmapctl</a></code>(8), <code><a href="/docs/linux/man/1-dbus-monitor/">dbus-monitor</a></code>(1),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
