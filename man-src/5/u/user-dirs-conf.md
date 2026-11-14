---
title: "user-dirs-conf(5)"
name: "user-dirs-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-user-dirs-conf/"
description: "user-dirs.conf – configuration for xdg-user-dirs-update"
---

<p>user-dirs.conf &#8211; configuration for xdg-user-dirs-update</p>
<h2>Description</h2>
<p>The /etc/xdg/user-dirs.conf file is a text file that controls the behavior of the xdg-user-dirs-update command. Users can have their own ~/.config/user-dirs.conf file, which overrides the system-wide configuration. </p>
<p> The following keys are recognised: </p>
<p> enabled=<i>boolean</i></p>
<dl>
<dd>When set to False, xdg-user-dirs-update will not change the XDG user dirs configuration.</dl>
<p> filename_encoding=<i>encoding</i></p>
<dl>
<dd>This sets the filename encoding to use. <i>encoding</i> can be an explicit encoding name, such as UTF-8, or &quot;locale&quot;, which means the encoding of the users locale will be used.</dl>
<p> Lines beginning with a # character are ignored.</p>
<h2>Environment</h2>
<p><code>XDG_CONFIG_DIRS</code></p>
<dl>
<dd>The system-wide user-dirs.conf file is located in this directory. The default is /etc/xdg.</dl>
<p> <code>XDG_CONFIG_HOME</code></p>
<dl>
<dd>The per-user user-dirs.conf file is located in this directory. The default is $HOME/.config.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xdg-user-dirs-update/">xdg-user-dirs-update</a></code>(1) </p>
