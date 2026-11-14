---
title: "winbind_krb5_locator(7)"
name: "winbind_krb5_locator"
section: "7"
letter: "w"
url: "/docs/linux/man/7-winbind_krb5_locator/"
description: "winbind_krb5_locator – A plugin for MIT and Heimdal Kerberos for detecting KDCs using Windows semantics."
---

<p>winbind_krb5_locator &#8211; A plugin for MIT and Heimdal Kerberos for detecting KDCs using Windows semantics.</p>
<h2>Description</h2>
<p>This plugin is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> winbind_krb5_locator is a plugin that permits MIT and Heimdal Kerberos libraries to detect Kerberos Servers (for the KDC and kpasswd service) using the same semantics that other tools of the Samba suite use. This include site-aware DNS service record lookups and caching of closest dc. The plugin uses the public locator API provided by most modern Kerberos implementations.</p>
<h2>Prerequisites</h2>
<p>MIT Kerberos (at least version 1.5) or Heimdal Kerberos (at least version 1.0) is required. </p>
<p> The plugin queries the <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) daemon which needs to be configured and started separately. </p>
<p> The winbind_krb5_locator.so file needs to be manually copied to the plugin directory of the system Kerberos library. For MIT Kerberos this is often: /usr/lib/krb5/plugins/libkrb5/. For Heimdal Kerberos this is often: /usr/lib/plugin/krb5/. Please check your local Kerberos installation for the correct paths. No modification in /etc/krb5.conf is required to enable the use of this plugin. </p>
<p> After copying the locator plugin to the appropriate plugin directory it should immediately be available for use. Users should be able to kinit into their kerberized Windows environment without any modification or servers being put manually into /etc/krb5.conf.</p>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The winbind_krb5_locator manpage was written by Guenther Deschner.</p>
