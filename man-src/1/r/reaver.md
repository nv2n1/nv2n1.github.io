---
title: "reaver(1)"
name: "reaver"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reaver/"
description: "Reaver – WPS Cracker"
---

<h2>NAME</h2>
<p> <code>Reaver</code> &#8211; WPS Cracker</p>
<h2>SYNOPSIS</h2>
<p> <code>reaver -i &lt;interface&gt; -b &lt;target bssid&gt; -vv</code></p>
<h2>DESCRIPTION</h2>
<p> Reaver implements a brute force attack against WiFi Protected Setup which can crack the WPS pin of an access point in a matter of hours and subsequently recover the WPA/WPA2 passphrase. </p>
<p> Specifically, Reaver targets the registrar functionality of WPS, which is flawed in that it only takes 11,000 attempts to guess the correct WPS pin in order to become a WPS registrar. Once registred as a registrar with the access point, the access point will give you the WPA passphrase.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd> <code>-m, &#8211;mac=&lt;mac&gt;</code></p>
<dl>
<dt>
<dd> MAC of the host system (should be resolved automatically)</dl>
</dl>
<dl>
<dt>
<dd> <code>-e, &#8211;essid=&lt;ssid&gt;</code></p>
<dl>
<dt>
<dd> ESSID of the target AP. Unless cloaked, this will be resolved automatically.</dl>
</dl>
<dl>
<dt>
<dd> <code>-c, &#8211;channel=&lt;channel&gt;</code></p>
<dl>
<dt>
<dd> Set the 802.11 channel for the interface (implies -f)</dl>
</dl>
<dl>
<dt>
<dd> <code>-o, &#8211;out-file=&lt;file&gt;</code></p>
<dl>
<dt>
<dd> Send output to a log file [default: stdout]</dl>
</dl>
<dl>
<dt>
<dd> <code>-f, &#8211;fixed</code></p>
<dl>
<dt>
<dd> Disable channel hopping</dl>
</dl>
<dl>
<dt>
<dd> <code>-5, &#8211;5ghz</code></p>
<dl>
<dt>
<dd> Use 5GHz 802.11 channels</dl>
</dl>
<dl>
<dt>
<dd> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Display non-critical warnings (-vv for more)</dl>
</dl>
<dl>
<dt>
<dd> <code>-q, &#8211;quiet</code></p>
<dl>
<dt>
<dd> Only display critical messages</dl>
</dl>
<dl>
<dt>
<dd> <code>-i, &#8211;interface=&lt;wlan&gt;</code></p>
<dl>
<dt>
<dd> Name of the monitor-mode interface to use</dl>
</dl>
<dl>
<dt>
<dd> <code>-b, &#8211;bssid=&lt;mac&gt;</code></p>
<dl>
<dt>
<dd> BSSID of the target AP</dl>
</dl>
<dl>
<dt>
<dd> <code>-p, &#8211;pin=&lt;wps pin&gt;</code></p>
<dl>
<dt>
<dd> Use the specified WPS pin</dl>
</dl>
<dl>
<dt>
<dd> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Show help</dl>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Craig Heffner &lt;cheffner [at] tacnetsol.com&gt;, Tactical Network Solutions. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
