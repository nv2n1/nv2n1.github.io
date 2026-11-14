---
title: "00-upstream-settings(5)"
name: "00-upstream-settings"
section: "5"
letter: "0"
url: "/docs/linux/man/5-00-upstream-settings/"
description: "00-upstream-settings – dconf configuration file"
---

<p><code>00-upstream-settings</code> &#8211; dconf configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/dconf/db/ibus.d/00-upstream-settings</code> </p>
<h2>Description</h2>
<p>IBus is an Intelligent Input Bus. It is a new input framework for Linux OS. It provides full featured and user friendly input method user interface. It also may help developers to develop input method easily. </p>
<p> <code>00-upstream-settings</code> is a text configuration file of dconf and can be converted to /etc/dconf/db/ibus by <code>dconf update</code> command with a write privilege in /etc/dconf/db. /etc/dconf/db/ibus is a database file of dconf and saves the IBus default settings. The saved keys and values can be readed by dconf command. </p>
<dl>
<dd>
<pre>env DCONF_PROFILE=ibus dconf list /desktop/ibus/
</dl></pre>
<h2>Bugs</h2>
<p>If you find a bug, please report it at <a rel="nofollow" href="https://github.com/ibus/ibus/issues">https://github.com/ibus/ibus/issues</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dconf/">dconf</a></code>(1) <code><a href="/docs/linux/man/5-ibus/">ibus</a></code>(5) </p>
