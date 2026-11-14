---
title: "wpa_passphrase(8)"
name: "wpa_passphrase"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wpa_passphrase/"
description: "wpa_passphrase – Generate a WPA PSK from an ASCII passphrase for a SSID"
---

<p>wpa_passphrase &#8211; Generate a WPA PSK from an ASCII passphrase for a SSID</p>
<h2>Synopsis</h2>
<p><code>wpa_passphrase</code> [ <i>ssid</i> ] [ <i>passphrase</i> ] </p>
<h2>Overview</h2>
<p><code>wpa_passphrase</code> pre-computes PSK entries for network configuration blocks of a <i>wpa_supplicant.conf</i> file. An ASCII passphrase and SSID are used to generate a 256-bit PSK.</p>
<h2>Options</h2>
<dl>
<dt><code>ssid</code></p>
<dd>The SSID whose passphrase should be derived.</p>
<dt><code>passphrase</code></p>
<dd>The passphrase to use. If not included on the command line, passphrase will be read from standard input.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-wpa_supplicant-conf/">wpa_supplicant.conf</a></code>(5) <code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8)</p>
<h2>Legal</h2>
<p>wpa_supplicant is copyright (c) 2003-2022, Jouni Malinen &lt;j@w1.fi&gt; and contributors. All Rights Reserved. </p>
<p> This program is licensed under the BSD license (the one with advertisement clause removed).</p>
