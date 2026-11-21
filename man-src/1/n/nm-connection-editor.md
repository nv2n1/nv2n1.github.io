---
title: "nm-connection-editor(1)"
name: "nm-connection-editor"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nm-connection-editor/"
description: "nm-connection-editor – network connection editor for NetworkManager"
---

<h2>SYNOPSIS</h2>
<p> <code>nm-connection-editor</code> [ <i>OPTIONS</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nm-connection-editor</code> is a GTK-based application to add, remove, and modify network connections stored by NetworkManager. NetworkManager must be running for any network connections to be added, removed, or modified. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t, &#8211;type=&lt;type&gt;</code></dt>
<dd> Type of connection to create or show. Values are NetworkManager setting names, eg &quot;802-3-ethernet&quot;, &quot;802-11-wireless&quot;, &quot;bridge&quot;, &quot;bond&quot;, &quot;infiniband&quot;, &quot;vlan&quot;, etc. Does nothing if &#8211;create or &#8211;show is not given.</dd>
<dt><code>-s, &#8211;show</code></dt>
<dd> Expand or collapse the network list to highlight the network connection type given by &#8211;type.</dd>
<dt><code>-c, &#8211;create</code></dt>
<dd> Create a new connection of the type given by &#8211;type and allow the user to modify connection details.</dd>
<dt><code>-e, &#8211;edit=&lt;uuid&gt;</code></dt>
<dd> Show the network connection edit window for the connection of the given UUID. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nmcli/">nmcli</a>(1),</code> <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a>(8),</code> <code><a href="/docs/linux/man/1-nm-applet/">nm-applet</a>(1).</code> </p>
