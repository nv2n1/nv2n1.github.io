---
title: "kdocker(1)"
name: "kdocker"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kdocker/"
description: "kdocker - dock any application in the system tray SYNOPSIS kdocker [options]"
---

<h2 class="name">NAME</h2>
<pre>
 kdocker - dock any application in the system tray
</pre>
<h2>SYNOPSIS</h2>
<p> <code>kdocker</code> [<i>options</i>]<i></i></p>
<h2>DESCRIPTION</h2>
<pre>
 KDocker is a program that will dock any application to the system tray
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd>
<pre>
 Show author information
</pre>
</dd><dt><code>-b</code></dt>
<dd>
<pre>
 Suppress the warning dialog when docking non-normal windows (blind mode)
</pre>
</dd><dt><code>-d</code> <i>secs</i></dt>
<dd>
<pre>
 Maximum time in seconds to allow for a command to start and open a window
 [default: 5 seconds]
</pre>
</dd><dt><code>-e</code> <i>type</i></dt>
<dd>
<pre>
 Name matching syntax. Choices are:
  n = normal, substring matching [default]
  r = regex (regular expression)
  u = unix wildcard
  w = wildcard
  x = W3C XML Schema 1.1
</pre>
</dd><dt><code>-f</code></dt>
<dd>
<pre>
 Dock window that has focus (active window)
</pre>
</dd><dt><code>-h</code></dt>
<dd>
<pre>
 Display this help, then exit
</pre>
</dd><dt><code>-i</code> <i>file</i></dt>
<dd>
<pre>
 Custom icon path
</pre>
</dd><dt><code>-j</code></dt>
<dd>
<pre>
 Case sensitive name (title) matching
</pre>
</dd><dt><code>-k</code></dt>
<dd>
<pre>
 Regex minimal matching
</pre>
</dd><dt><code>-l</code></dt>
<dd>
<pre>
 Iconify when focus lost
</pre>
</dd><dt><code>-m</code></dt>
<dd>
<pre>
 Keep application window showing (don't hide on dock)
</pre>
</dd><dt><code>-n</code> <i>name</i></dt>
<dd>
<pre>
 Match window based on its title
</pre>
</dd><dt><code>-o</code></dt>
<dd>
<pre>
 Iconify when obscured by other windows
</pre>
</dd><dt><code>-p</code> <i>secs</i></dt>
<dd>
<pre>
 By default, when the title of the application changes,
 a popup is displayed from the system tray for 4 seconds
 Works well with xmms
</pre>
</dd><dt><code>-q</code></dt>
<dd>
<pre>
 Disable ballooning title changes (quiet)
</pre>
</dd><dt><code>-r</code></dt>
<dd>
<pre>
 Remove this application from the pager
</pre>
</dd><dt><code>-s</code></dt>
<dd>
<pre>
 Make the window sticky (appears on all desktops)
</pre>
</dd><dt><code>-t</code></dt>
<dd>
<pre>
 Remove this application from the taskbar
</pre>
</dd><dt><code>-v, &#8211;version</code></dt>
<dd>
<pre>
 Show the KDocker version string, then exit
</pre>
</dd><dt><code>-w</code> <i>wid</i></dt>
<dd>
<pre>
 Window id of the application to dock
 Assumes hex number of the form 0x###...
</pre>
</dd><dt><code>-x</code> <i>pid</i></dt>
<dd>
<pre>
 Process id of the application to dock
 Assumes decimal number of the form ###...
</pre>
</dd></dl>
<h2>AUTHOR</h2>
<pre>
 KDocker was written by Girish Ramakrishnan
 Revised and maintained by John Schember
</pre>
<h2>REPORTING BUGS</h2>
<p> Bugs and wishes to the KDocker Home Page &lt;<a rel="nofollow" href="https://github.com/user-none/KDocker">https://github.com/user-none/KDocker</a>&gt; </p>
<h2>Index</h2>
