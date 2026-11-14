---
title: "vboxrc(5)"
name: "vboxrc"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vboxrc/"
description: "vboxrc – user config file for vbox"
---

<p>vboxrc &#8211; user config file for vbox</p>
<h2>Description</h2>
<p>Every user can save settings in ~/.vboxrc. Everything after &quot;#&quot; is ignored, as are empty lines. All arguments must be separated by whitespace (spaces, tabs). Arguments may not contain whitespace. These keywords are allowed:</p>
<dl>
<dd>
<dl>
<dt><code>USERNAME</code></p>
<dd>
<dt><code>PASSWORD</code></p>
<dd>Username and password for vboxd login. These settings are used by vbox and vboxctrl. If they are missing, you have to enter them at runtime.</p>
<dt><code>VOLUME</code></p>
<dd>Default volume for vbox.</p>
<dt><code>C_BACKGROUND</code></p>
<dd>Background color.</p>
<dt><code>C_STATUSBAR</code></p>
<dd>Color for normal text in the status bar.</p>
<dt><code>C_STATUSBAR_HL</code></p>
<dd>Color for highlighted text in the status bar.</p>
<dt><code>C_POWERLED_ON</code></p>
<dd>Color for powerled (on).</p>
<dt><code>C_POWERLED_OFF</code></p>
<dd>Color for powerled (off).</p>
<dt><code>C_STATUSLED_ON</code></p>
<dd>Color for statusled (on).</p>
<dt><code>C_STATUSLED_OFF</code></p>
<dd>Color for statusled (off).</p>
<dt><code>C_LIST</code></p>
<dd>Color for list of messages.</p>
<dt><code>C_LIST_SELECTED</code></p>
<dd>Color for selected entry in the list of messages.</p>
<dt><code>C_INFOTEXT</code></p>
<dd>Color for info texts in the message list.</dl>
</dl>
<p> All color settings have the format TEXTCOLOR:BACKGROUNDCOLOR. You may not use whitespace.</p>
<dl>
<dt>These colors are available for TEXTCOLOR:</p>
<dd>
<pre>BLACK RED GREEN BROWN BLUE MAGENTA CYAN GRAY
DARKGREY LIGHTRED LIGHTGREEN YELLOW LIGHTBLUE
LIGHTMAGENTA LIGHTCYAN WHITE</pre>
<dt>These colors are available for BACKGROUNDCOLOR:</p>
<dd>BLACK RED GREEN BROWN BLUE MAGENTA CYAN GREY </p>
<h2>Files</h2>
<dl>
<dt><code>~/.vboxrc</code></p>
<dd>this configuration file</p>
<dt><code>/usr/doc/isdnutils/examples/vboxrc</code></p>
<dd>an example </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vbox/">vbox</a>(1)</code> </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
