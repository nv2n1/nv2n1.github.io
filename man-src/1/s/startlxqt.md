---
title: "startlxqt(1)"
name: "startlxqt"
section: "1"
letter: "s"
url: "/docs/linux/man/1-startlxqt/"
description: "startlxqt – script to initialize and launch LXQt sessions"
---

<h2>NAME</h2>
<p> startlxqt &#8211; script to initialize and launch LXQt sessions</p>
<h2>SYNOPSIS</h2>
<p> <code>startlxqt</code></p>
<h2>DESCRIPTION</h2>
<p> <code>startlxqt</code> is a shell script meant to initialize and launch LXQt sessions. It is as such similar to counterparts of other desktop environments like startlxde in LXDE or startkde in KDE. </p>
<p> It&#8217;s main tasks are exporting environment variables, partly after performing corresponding checks, and launching <code>lxqt-session</code>, the LXQt session manager. </p>
<p> It is not meant to be run by users. Rather, it is invoked as backend, e. g. by script <code>startx</code> on virtual terminals or display managers like SDDM or LightDM, see section <i>EXAMPLE</i>.</p>
<h2>FILES</h2>
<p> <i>$XDG_DATA_DIRS/xsessions/lxqt.desktop</i></p>
<dl>
<dt>
<dd> Desktop entry file stating startlxqt as binary needed to start LXQt sessions. Sourced e. g. by display managers.</dl>
<h2>BUGS</h2>
<p> None at the time of this writing. Bugs can be reported on <a rel="nofollow" href="https://github.com/lxde/lxqt/issues.">https://github.com/lxde/lxqt/issues.</a></p>
<h2>EXAMPLE</h2>
<p> To start an LXQt session from a virtual terminal (virtual console) add a line </p>
<dl>
<dt>
<dd> exec startlxqt</dl>
<p> to file <i>~/.xinitrc</i>. An LXQt session will then be launched by running <code>startx</code>. </p>
<p> Display managers are making use of scripts like <code>startlxqt</code> automatically. Information about available desktop environments is provided by files <i>$XDG_DATA_DIRS/xsessions/*.desktop</i>, typically <i>/usr/share/xessions/*.desktop</i>.<br />
 File <i>lxqt.desktop</i> provided by LXQt is stating <code>startlxqt</code> in key <i>Exec</i> while making sure the session manager <code>lxqt-session</code> does exist by stating it in key <i>TryExec</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lxqt-session/">lxqt-session</a></code>(1) <code><a href="/docs/linux/man/1-startx/">startx</a></code>(1) <code><a href="/docs/linux/man/1-sddm/">sddm</a></code>(1) </p>
<p> <code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec/">http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec/</a></code></p>
<dl>
<dt>
<dd> Desktop Entry Specification defining desktop entry files (*.desktop).</dl>
<h2>Index</h2>
