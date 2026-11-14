---
title: "user-dirs-dirs(5)"
name: "user-dirs-dirs"
section: "5"
letter: "u"
url: "/docs/linux/man/5-user-dirs-dirs/"
description: "user-dirs.dirs – settings for XDG user dirs"
---

<p>user-dirs.dirs &#8211; settings for XDG user dirs</p>
<h2>Description</h2>
<p>The $HOME/.config/user-dirs.dirs file is a text file that contains the user-specific values for the XDG user dirs. It is created and updated by the xdg-user-dirs-update command. </p>
<p> This file contains lines of the form </p>
<dl>
<dd>
<pre>XDG_<i>NAME</i>_DIR=<i>VALUE</i></pre>
</dl>
<p> The following names are recognised:</p>
<dl>
<dd>DESKTOP</dl>
<dl>
<dd>DOWNLOAD</dl>
<dl>
<dd>TEMPLATES</dl>
<dl>
<dd>PUBLICSHARE</dl>
<dl>
<dd>DOCUMENTS</dl>
<dl>
<dd>MUSIC</dl>
<dl>
<dd>PICTURES</dl>
<dl>
<dd>VIDEOS</dl>
<p> <i>VALUE</i> must be of the form &quot;$HOME/Path&quot; or &quot;/Path&quot;. </p>
<p> Lines beginning with a # character are ignored. </p>
<p> The format of user-dirs.dirs is designed to allow direct sourcing of this file in shell scripts.</p>
<h2>Environment</h2>
<p><code>XDG_CONFIG_DIRS</code></p>
<dl>
<dd>The user-dirs.defaults file is located in this directory. The default is /etc/xdg.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xdg-user-dirs-update/">xdg-user-dirs-update</a></code>(1) </p>
