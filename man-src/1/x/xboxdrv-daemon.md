---
title: "xboxdrv-daemon(1)"
name: "xboxdrv-daemon"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xboxdrv-daemon/"
description: "xboxdrv-daemon – A simple daemon that automatically launches xboxdrv when it detects a controller."
---

<h2>NAME</h2>
<p> xboxdrv-daemon &#8211; A simple daemon that automatically launches xboxdrv when it detects a controller.</p>
<h2>SYNOPSIS</h2>
<p> <code>xboxdrv</code> [OPTION]&#8230; [&#8211;] {XBOXDRV} [ARGS]&#8230;</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help text and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose with printed output.</p>
<dt><code>-a FILENAME, &#8211;attach=FILENAME</code></p>
<dd> Launch EXE when a new controller is connected</p>
<dt><code>-d FILENAME, &#8211;detach=FILENAME</code></p>
<dd> Launch EXE when a controller is detached</p>
<dt><code>-x FILENAME, &#8211;xboxdrv=FILENAME</code></p>
<dd> Set the location of the xboxdrv executable</dl>
<h2>RUNNING XBOXDRV VIA XBOXDRV-DAEMON</h2>
<p> <code>xboxdrv-daemon</code> allows you to run xboxdrv automatically whenever you plug in a gamepad. Since xboxdrv-daemon.py needs to know where xboxdrv is located you need to supply the location of the xboxdrv binary manually if its not located in <code>PATH</code>: </p>
<pre>
% xboxdrv-daemon --xboxdrv ./xboxdrv
</pre>
<p> You can pass arguments to xboxdrv after a double dash &#8216;&#8211;&#8216;: </p>
<pre>
% xboxdrv-daemon -- --buttonmap B=A,X=A,Y=A
</pre>
<p> You can also run scripts that get started after xboxdrv is started via: </p>
<pre>
% xboxdrv-daemon \
  --attach /home/juser/xboxdrv_attach \
  --detach /home/juser/xboxdrv_deatach
</pre>
<p> This is useful in Kiosk settings, such as a media center PC, where you might want to restart the media center to have the controller working properly after it got attached. </p>
<p> Note that you can&#8217;t dynamically reconfigurabilty xboxdrv when you launch it automatically via the daemon, so using this daemon isn&#8217;t generally recommend. </p>
<p> When you want configurability and automatic launching, it is recomment that you write little startup scripts for your games, such as this: </p>
<pre>
#!/bin/sh
# Start xboxdrv and remember its PID in the variable XBOXPID
xboxdrv --trigger-as-button -s &amp;amp;
XBOXPID=$!
# Give xboxdrv a second to startup and create the device
sleep 1
# Launch your favorite game
your_favorite_game
# Kill xboxdrv and wait for it to finish
kill $XBOXPID
wait $XBOXPID
# EOF #
</pre>
<p> That way you can individually configure every game and still not have to worry about launching xboxdrv manually.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xboxdrv/">xboxdrv</a>(1) </p>
<h2>Index</h2>
