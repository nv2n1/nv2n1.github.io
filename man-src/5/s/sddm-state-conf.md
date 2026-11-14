---
title: "sddm-state-conf(5)"
name: "sddm-state-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sddm-state-conf/"
description: "state.conf – sddm display manager configuration"
---

<p>state.conf &#8211; sddm display manager configuration</p>
<h2>Synopsis</h2>
<p>~sddm/state.conf</p>
<h2>Description</h2>
<p>This file carries state configuration for the sddm display manager <code><a href="/docs/linux/man/1-sddm/">sddm</a></code>(1).</p>
<h2>Options</h2>
<p>All options are configured in the [Last] section:</p>
<dl>
<dt><i>Session=</i></p>
<dd>Name of the session file of the last session selected. This session will be preselected when the login screen shows up. Default value is empty.</p>
<dt><i>User=</i></p>
<dd>Name of last logged-in user. This username will be preselected/shown when the login screen shows up. Default value is empty.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sddm/">sddm</a></code>(1) The full documentation for sddm is available at <i><a rel="nofollow" href="https://github.com/sddm/sddm">https://github.com/sddm/sddm</a></i> </p>
