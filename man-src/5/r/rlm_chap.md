---
title: "rlm_chap(5)"
name: "rlm_chap"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_chap/"
description: "rlm_chap – FreeRADIUS Module"
---

<p>rlm_chap &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_chap</i> module provides CHAP functionality. This module validates a user with CHAP authentication. If called in Authorize, it will look for CHAP-Password attribute in the Acess-Request and adds an Auth-Type attribute set to CHAP if the Config-Items list unless Auth-Type has already set. CHAP authentication requires access to the clear-text password for the user. Standard Unix system authentication or passwords encrypted via crypt() are not compatible with CHAP. </p>
<h2>Sections</h2>
<p><code>authorization,</code> <code>authentication</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
