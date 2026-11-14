---
title: "fbpanel(1)"
name: "fbpanel"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbpanel/"
description: "fbpanel – a NETWM compliant lightweight GTK2-based panel for UNIX desktop."
---

<h2>NAME</h2>
<p> fbpanel &#8211; a NETWM compliant lightweight GTK2-based panel for UNIX desktop.</p>
<h2>SYNOPSIS</h2>
<p> <code>fbpanel</code> [<i>OPTION</i>] </p>
<h2>DESCRIPTION</h2>
<p> fbpanel is desktop panel which provides graphical information and feedback about desktop activity and allows interaction with the window manager. It features:</p>
<dl>
<dt> * taskbar &#8211; shows a list of the managed windows (tasks)</p>
<dt> * pager &#8211; thumbnailed view of the desktop.</p>
<dt> * launchbar &#8211; buttons to quickly launch applications</p>
<dt> * show desktop &#8211; button to iconify or shade all windows</p>
<dt> * image &#8211; display an image</p>
<dt> * clock &#8211; show the current time and/or date</p>
<dt> * system tray &#8211; tray for XEMBED icons (aka docklets)</dl>
<dd>fbpanel requires NETWM (<a rel="nofollow" href="http://www.freedesktop.org">www.freedesktop.org</a>) compliant window manager. You can run many instances of fbpanel each with its own configuration (see <code>OPTIONS</code> below). </p>
<p> Most updated info about fbpanel can be found on its home page: <a rel="nofollow" href="http://fbpanel.sf.net/">http://fbpanel.sf.net/</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> &#8212; print help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> &#8212; print version and exit.</p>
<dt><code>&#8211;log &lt;number&gt;</code></p>
<dd> &#8212; set log level 0-5. 0 &#8211; none 5 &#8211; chatty</p>
<dt><code>&#8211;configure</code></p>
<dd> &#8212; open configuration dialog</p>
<dt><code>&#8211;profile &lt;name&gt;</code></p>
<dd> &#8212; use specified profile. The profile is loaded from the file ~/.fbpanel/&lt;name&gt;. If that fails, fbpanel will load /usr/share/fbpanel/&lt;name&gt;. No -p option is equivalent to -p default</p>
<dt><code>-h</code></p>
<dd> &#8212; same as &#8211;help</p>
<dt><code>-p</code></p>
<dd> &#8212; same as &#8211;profile</p>
<dt><code>-v</code></p>
<dd> &#8212; same as &#8211;version</p>
<dt><code>-C</code></p>
<dd> &#8212; same as &#8211;configure </p>
</dl>
<h2>CUSTOMIZATION</h2>
<p> To change default settings, copy profile file to your home directory </p>
<p>mkdir -p&nbsp;<wbr>~/.fbpanel<br />
cp&nbsp;<wbr>/usr/share/fbpanel/default&nbsp;<wbr>~/.fbpanel<br />
 and edit it. Default profile file contains comments and explanation inside, so it should be easy. For full list of options please visit fbpanel&#8217;s home page. </p>
<h2>FILES</h2>
<dl>
<dt>/usr/share/fbpanel</p>
<dd> Directory with system-wide resources and default settings</p>
<dt>~/.fbpanel/</p>
<dd> Directory with the user&#8217;s private profiles</p>
<dt>~/.fbpanel/default</p>
<dd> The user&#8217;s default profile.</dl>
<h2>AUTHOR</h2>
<p> fbpanel was written by Anatoly Asviyan &lt;aanatoly [at] users.sf.net&gt;. This manual page was originally written for the Debian GNU/Linux system by Shyamal Prasad &lt;shyamal [at] member.fsf.org&gt;. </p>
<h2>Index</h2>
