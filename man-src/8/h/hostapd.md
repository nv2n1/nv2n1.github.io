---
title: "hostapd(8)"
name: "hostapd"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hostapd/"
description: "hostapd – IEEE 802.11 AP, IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator"
---

<p>hostapd &#8211; IEEE 802.11 AP, IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator</p>
<h2>Synopsis</h2>
<p><code>hostapd</code> [-hdBKtv] [-P &lt;PID file&gt;] &lt;configuration file(s)&gt;</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>hostapd</code> daemon. </p>
<p> <code>hostapd</code> is a user space daemon for access point and authentication servers. It implements IEEE 802.11 access point management, IEEE 802.1X/WPA/WPA2/EAP Authenticators and RADIUS authentication server. The current version supports Linux (Host AP, mac80211-based drivers) and FreeBSD (net80211). </p>
<p> <code>hostapd</code> is designed to be a &quot;daemon&quot; program that runs in the background and acts as the backend component controlling authentication. <code>hostapd</code> supports separate frontend programs and an example text-based frontend, <code>hostapd_cli</code>, is included with <code>hostapd</code>.</p>
<h2>Options</h2>
<p>A summary of options is included below. For a complete description, run <code>hostapd</code> from the command line.</p>
<dl>
<dt><code>-h</code></dt>
<dd>Show usage.</dd>
<dt><code>-d</code></dt>
<dd>Show more debug messages.</dd>
<dt><code>-dd</code></dt>
<dd>Show even more debug messages.</dd>
<dt><code>-B</code></dt>
<dd>Run daemon in the background.</dd>
<dt><code>-P &lt;PID file&gt;</code></dt>
<dd>Path to PID file.</dd>
<dt><code>-K</code></dt>
<dd>Include key data in debug messages.</dd>
<dt><code>-t</code></dt>
<dd>Include timestamps in some debug messages.</dd>
<dt><code>-v</code></dt>
<dd>Show hostapd version.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-hostapd_cli/">hostapd_cli</a></code>(1).</p>
<h2>Author</h2>
<p>hostapd was written by Jouni Malinen &lt;j@w1.fi&gt;. </p>
<p> This manual page was written by Faidon Liambotis &lt;faidon [at] cube.gr&gt;, for the Debian project (but may be used by others).</p>
