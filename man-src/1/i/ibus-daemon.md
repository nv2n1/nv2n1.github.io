---

title: "ibus-daemon(1)"
name: "ibus-daemon"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibus-daemon/"
description: "ibus-daemon – daemon program for ibus"
---

<p> <code>ibus-daemon</code> &#8211; daemon program for ibus</p>
<p> <code>ibus-daemon</code> [<i>OPTION</i>]&#8230; </p>
<p> IBus is an Intelligent Input Bus. It is a new input framework for Linux OS. It provides full featured and user friendly input method user interface. It also may help developers to develop input method easily. </p>
<p> <code>ibus-daemon</code> is a daemon program for ibus and it is also a start up program for users to activate ibus daemon, engines and panel. </p>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options </dd>
</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;daemonize</code></dt>
<dd> run ibus as background process.</dd>
<dt><code>-s</code>, <code>&#8211;single</code></dt>
<dd> do not execute panel and config module.</dd>
<dt><code>-x</code>, <code>&#8211;xim</code></dt>
<dd> execute ibus XIM server.</dd>
<dt><code>-n</code>, <code>&#8211;desktop</code>=<i>name</i></dt>
<dd> specify the name of desktop session. [default=gnome]</dd>
<dt><code>-p</code>, <code>&#8211;panel</code>=<i>cmdline</i></dt>
<dd> specify the cmdline of panel program.</dd>
<dt><code>-c</code>, <code>&#8211;config</code>=<i>cmdline</i></dt>
<dd> specify the cmdline of config program.</dd>
<dt><code>-a</code>, <code>&#8211;address</code>=<i>address</i></dt>
<dd> specify the address of ibus daemon.</dd>
<dt><code>-r</code>, <code>&#8211;replace</code></dt>
<dd> if there is an old ibus-daemon is running, it will be replaced.</dd>
<dt><code>-t</code>, <code>&#8211;cache</code>=<i>mode</i> [default is auto]</dt>
<dd> force to re-scan components, and re-create registry cache. auto, refresh, none is available.</dd>
<dt><code>-o</code>, <code>&#8211;timeout</code>=<i>timeout</i> [default is 2000]</dt>
<dd> dbus reply timeout in milliseconds.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> verbose. </dd>
</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://github.com/ibus/ibus/issues">https://github.com/ibus/ibus/issues</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ibus/">ibus</a></code>(1) </p>
