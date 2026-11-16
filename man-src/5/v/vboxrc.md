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
</dd><dl>
<dt><code>USERNAME</code></dt>
<dd>
</dd><dt><code>PASSWORD</code></dt>
<dd>Username and password for vboxd login. These settings are used by vbox and vboxctrl. If they are missing, you have to enter them at runtime.</dd>
<dt><code>VOLUME</code></dt>
<dd>Default volume for vbox.</dd>
<dt><code>C_BACKGROUND</code></dt>
<dd>Background color.</dd>
<dt><code>C_STATUSBAR</code></dt>
<dd>Color for normal text in the status bar.</dd>
<dt><code>C_STATUSBAR_HL</code></dt>
<dd>Color for highlighted text in the status bar.</dd>
<dt><code>C_POWERLED_ON</code></dt>
<dd>Color for powerled (on).</dd>
<dt><code>C_POWERLED_OFF</code></dt>
<dd>Color for powerled (off).</dd>
<dt><code>C_STATUSLED_ON</code></dt>
<dd>Color for statusled (on).</dd>
<dt><code>C_STATUSLED_OFF</code></dt>
<dd>Color for statusled (off).</dd>
<dt><code>C_LIST</code></dt>
<dd>Color for list of messages.</dd>
<dt><code>C_LIST_SELECTED</code></dt>
<dd>Color for selected entry in the list of messages.</dd>
<dt><code>C_INFOTEXT</code></dt>
<dd>Color for info texts in the message list.</dd></dl>
</dl>
<p> All color settings have the format TEXTCOLOR:BACKGROUNDCOLOR. You may not use whitespace.</p>
<dl>
<dt>These colors are available for TEXTCOLOR:</dt>
<dd>
<pre>BLACK RED GREEN BROWN BLUE MAGENTA CYAN GRAY
DARKGREY LIGHTRED LIGHTGREEN YELLOW LIGHTBLUE
LIGHTMAGENTA LIGHTCYAN WHITE</pre>
</dd><dt>These colors are available for BACKGROUNDCOLOR:</dt>
<dd>BLACK RED GREEN BROWN BLUE MAGENTA CYAN GREY </dd>
<h2>Files</h2>
<dl>
<dt><code>~/.vboxrc</code></dt>
<dd>this configuration file</dd>
<dt><code>/usr/doc/isdnutils/examples/vboxrc</code></dt>
<dd>an example </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vbox/">vbox</a>(1)</code> </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
</dl>