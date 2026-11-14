---
title: "nm-system-settings(5)"
name: "nm-system-settings"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nm-system-settings/"
description: "nm-system-settings.conf – Deprecated NetworkManager configuration file"
---

<p>nm-system-settings.conf &#8211; Deprecated NetworkManager configuration file</p>
<h2>Synopsis</h2>
<p>/etc/NetworkManager/nm-system-settings.conf<br />
 or<br />
 <i>&lt;SYSCONFDIR&gt;</i>/NetworkManager/nm-system-settings.conf<br />
 where &lt;SYSCONFDIR&gt; depends on your distribution or build.</p>
<h2>Description</h2>
<p><i>nm-system-settings.conf</i> is a deprecated configuration file for <code>NetworkManager</code> (5). While this file can still be used, NetworkManager now defaults to reading the config file &lt;SYSCONFDIR&gt;/NetworkManager/NetworkManager.conf instead, falling back to nm-system-settings.conf if NetworkManager.conf does not exist.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/5-networkmanager-conf/">NetworkManager.conf</a></code>(5). </p>
