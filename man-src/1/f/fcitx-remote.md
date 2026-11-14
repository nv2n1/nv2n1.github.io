---
title: "fcitx-remote(1)"
name: "fcitx-remote"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcitx-remote/"
description: "fcitx-remote – Tool for control fcitx state via console"
---

<h2 class="name">NAME</h2>
<p> fcitx-remote &#8211; Tool for control fcitx state via console </p>
<h2>SYNOPSIS</h2>
<p> <code>fcitx-remote</code> [<i>OPTION</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> inactivate input method</p>
<dt><code>-o</code></p>
<dd> activate input method</p>
<dt><code>-r</code></p>
<dd> reload fcitx config</p>
<dt><code>-t</code></p>
<dd> switch between active/inactive</p>
<dt><code>-s</code><i> imname</i></p>
<dd> switch to the input method uniquely identified by <i>imname</i></p>
<dt>[<i>no option</i>]</p>
<dd> display fcitx state, 0 for close, 1 for inactive, 2 for active</p>
<dt><code>-h</code></p>
<dd> display help and exit</dl>
<h2>FILES</h2>
<p> fcitx will create socket at <i>/tmp/fcitx-socket-&lt;displayname&gt;</i>, so user must have permission to access <i>/tmp</i> folder.</p>
<h2>SEE ALSO</h2>
<p> Please see the homepage at <code><a rel="nofollow" href="https://fcitx-im.org/">https://fcitx-im.org/</a></code> </p>
<h2>Index</h2>
