---
title: "user-dirs-defaults(5)"
name: "user-dirs-defaults"
section: "5"
letter: "u"
url: "/docs/linux/man/5-user-dirs-defaults/"
description: "user-dirs.defaults – default settings for XDG user dirs"
---

<p>user-dirs.defaults &#8211; default settings for XDG user dirs</p>
<h2>Description</h2>
<p>The /etc/xdg/user-dirs.defaults file is a text file that contains the default values for the XDG user dirs which are used by the xdg-user-dirs-update command. </p>
<p> This file contains lines of the form </p>
<dl>
<dd>
<pre><i>NAME</i>=<i>VALUE</i></pre>
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
<p> The values are relative pathnames from the home directory and will be translated on a per-path-element basis into the users locale. </p>
<p> Lines beginning with a # character are ignored.</p>
<h2>Environment</h2>
<p><code>XDG_CONFIG_DIRS</code></p>
<dl>
<dd>The user-dirs.defaults file is located in this directory. The default is /etc/xdg.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xdg-user-dirs-update/">xdg-user-dirs-update</a></code>(1) </p>
