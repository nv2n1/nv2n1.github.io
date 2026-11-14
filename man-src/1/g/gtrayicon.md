---
title: "gtrayicon(1)"
name: "gtrayicon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtrayicon/"
description: "gtrayicon – Generic tray icon for GNOME"
---

<h2>NAME</h2>
<p> gtrayicon &#8211; Generic tray icon for GNOME </p>
<h2>DESCRIPTION</h2>
<p> Generic tray icon for GNOME is a small utility which allows to add a icon to the system tray that can be used to trigger customized enable/disable actions. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;tooltip=string</code></p>
<dd> string to appear as tooltip</p>
<dt><code>&#8211;activate=cmd</code></p>
<dd> activate command</p>
<dt><code>&#8211;deactivate=cmd</code></p>
<dd> deactivate command</p>
<dt><code>&#8211;activate-icon=icon-path</code></p>
<dd> icon to show for &#8216;activate&#8217; action</p>
<dt><code>&#8211;deactivate-icon=icon-path</code></p>
<dd> icon to show for &#8216;deactivate&#8217;</p>
<dt><code>&#8211;menu-file=menu-path</code></p>
<dd> custom menu to display for right button</p>
<dt><code>&#8211;activated</code></p>
<dd> start in &#8216;activated&#8217; state (default: &#8216;deactivated&#8217; state) </p>
</dl>
<h2>EXAMPLE</h2>
<p> Activate action: start webfs (web server) setting a pid file<br />
 Deactivate action: kill that webfs instance </p>
<dl>
<dt>gtrayicon \</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&#8211;activate=&quot;/usr/bin/webfsd -k&nbsp;<wbr>/tmp/pid.file -r&nbsp;<wbr>/var/www&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;deactivate=&quot;cat&nbsp;<wbr>/tmp/pid.file | xargs -ipid kill -TERM pid&quot; </p>
</dl>
<h2>MENU</h2>
<p> For an example on how to write a menu file,see<br />
 /usr/share/doc/gtrayicon/examples/sample.menu </p>
<h2>SEE ALSO</h2>
<p> Website: <a rel="nofollow" href="http://gtrayicon.sourceforge.net/">http://gtrayicon.sourceforge.net/</a> </p>
<h2>AUTHOR</h2>
<p> Gtrayicon was written by Javier Valencia (javiervalencia80 at gmail.com) This Man page was written by Taylor LeMasurier-Wren &lt;ripps818 [at] gmail.com&gt; </p>
<h2>Index</h2>
