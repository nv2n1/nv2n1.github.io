---
title: "telinit(8)"
name: "telinit"
section: "8"
letter: "t"
url: "/docs/linux/man/8-telinit/"
description: "telinit – Change SysV runlevel"
---

<p>telinit &#8211; Change SysV runlevel</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>telinit </code><code>[OPTIONS&#8230;]</code><code>{COMMAND}</code></dl>
<h2>Description</h2>
<p><code>telinit</code></p>
<dd>may be used to change the SysV system runlevel. Since the concept of SysV runlevels is obsolete the runlevel requests will be transparently translated into systemd unit activation requests.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;no-wall</code></p>
<dl>
<dd>Do not send wall message before reboot/halt/power-off.</dl>
<p> The following commands are understood: </p>
<p> <code>0</code></p>
<dl>
<dd>Power-off the machine. This is translated into an activation request for poweroff.target and is equivalent to <code>systemctl poweroff</code>.</dl>
<p> <code>6</code></p>
<dl>
<dd>Reboot the machine. This is translated into an activation request for reboot.target and is equivalent to <code>systemctl reboot</code>.</dl>
<p> <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code></p>
<dl>
<dd>Change the SysV runlevel. This is translated into an activation request for runlevel2.target, runlevel3.target, &#8230; and is equivalent to <code>systemctl isolate runlevel2.target</code>, <code>systemctl isolate runlevel3.target</code>, &#8230;</dl>
<p> <code>1</code>, <code>s</code>, <code>S</code></p>
<dl>
<dd>Change into system rescue mode. This is translated into an activation request for rescue.target and is equivalent to <code>systemctl rescue</code>.</dl>
<p> <code>q</code>, <code>Q</code></p>
<dl>
<dd>Reload daemon configuration. This is equivalent to <code>systemctl daemon-reload</code>.</dl>
<p> <code>u</code>, <code>U</code></p>
<dl>
<dd>Serialize state, reexecute daemon and deserialize state again. This is equivalent to <code>systemctl daemon-reexec</code>.</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>Notes</h2>
<p>This is a legacy command available for compatibility only. It should not be used anymore, as the concept of runlevels is obsolete.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1) </p>
