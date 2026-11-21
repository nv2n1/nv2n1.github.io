---

title: "fcitx-remote(1)"
name: "fcitx-remote"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcitx-remote/"
description: "fcitx-remote – Tool for control fcitx state via console"
---

<p> <code>fcitx-remote</code> [<i>OPTION</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd> inactivate input method</dd>
<dt><code>-o</code></dt>
<dd> activate input method</dd>
<dt><code>-r</code></dt>
<dd> reload fcitx config</dd>
<dt><code>-t</code></dt>
<dd> switch between active/inactive</dd>
<dt><code>-s</code><i> imname</i></dt>
<dd> switch to the input method uniquely identified by <i>imname</i></dd>
<dt>[<i>no option</i>]</dt>
<dd> display fcitx state, 0 for close, 1 for inactive, 2 for active</dd>
<dt><code>-h</code></dt>
<dd> display help and exit</dd></dl>
<h2>FILES</h2>
<p> fcitx will create socket at <i>/tmp/fcitx-socket-&lt;displayname&gt;</i>, so user must have permission to access <i>/tmp</i> folder.</p>
<h2>SEE ALSO</h2>
<p> Please see the homepage at <code><a rel="nofollow" href="https://fcitx-im.org/">https://fcitx-im.org/</a></code> </p>
