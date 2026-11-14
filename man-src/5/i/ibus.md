---
title: "ibus(5)"
name: "ibus"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ibus/"
description: "IBUS – dconf database file for IBus"
---

<p><code>IBUS</code> &#8211; dconf database file for IBus</p>
<h2>Synopsis</h2>
<p><code>/etc/dconf/db/ibus</code> </p>
<h2>Description</h2>
<p>IBus is an Intelligent Input Bus. It is a new input framework for Linux OS. It provides full featured and user friendly input method user interface. It also may help developers to develop input method easily. </p>
<p> <code>/etc/dconf/db/ibus</code> is a database file dconf and saves the IBus default settings. It can be generated from /etc/dconf/db/ibus.d/00-upstream-settings by <code>dconf update</code> command with a write privilege in /etc/dconf/db. The saved keys and values can be readed by dconf command. </p>
<dl>
<dd>
<pre>env DCONF_PROFILE=ibus dconf list /desktop/ibus/
</dl></pre>
<h2>Bugs</h2>
<p>If you find a bug, please report it at <a rel="nofollow" href="https://github.com/ibus/ibus/issues">https://github.com/ibus/ibus/issues</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dconf/">dconf</a></code>(1) <code><a href="/docs/linux/man/5-00-upstream-settings/">00-upstream-settings</a></code>(5) </p>
