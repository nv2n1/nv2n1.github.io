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
<dt><code>-a</code></p>
<dd>
<pre>
 Show author information
</pre>
<dt><code>-b</code></p>
<dd>
<pre>
 Suppress the warning dialog when docking non-normal windows (blind mode)
</pre>
<dt><code>-d</code> <i>secs</i></p>
<dd>
<pre>
 Maximum time in seconds to allow for a command to start and open a window
 [default: 5 seconds]
</pre>
<dt><code>-e</code> <i>type</i></p>
<dd>
<pre>
 Name matching syntax. Choices are:
  n = normal, substring matching [default]
  r = regex (regular expression)
  u = unix wildcard
  w = wildcard
  x = W3C XML Schema 1.1
</pre>
<dt><code>-f</code></p>
<dd>
<pre>
 Dock window that has focus (active window)
</pre>
<dt><code>-h</code></p>
<dd>
<pre>
 Display this help, then exit
</pre>
<dt><code>-i</code> <i>file</i></p>
<dd>
<pre>
 Custom icon path
</pre>
<dt><code>-j</code></p>
<dd>
<pre>
 Case sensitive name (title) matching
</pre>
<dt><code>-k</code></p>
<dd>
<pre>
 Regex minimal matching
</pre>
<dt><code>-l</code></p>
<dd>
<pre>
 Iconify when focus lost
</pre>
<dt><code>-m</code></p>
<dd>
<pre>
 Keep application window showing (don't hide on dock)
</pre>
<dt><code>-n</code> <i>name</i></p>
<dd>
<pre>
 Match window based on its title
</pre>
<dt><code>-o</code></p>
<dd>
<pre>
 Iconify when obscured by other windows
</pre>
<dt><code>-p</code> <i>secs</i></p>
<dd>
<pre>
 By default, when the title of the application changes,
 a popup is displayed from the system tray for 4 seconds
 Works well with xmms
</pre>
<dt><code>-q</code></p>
<dd>
<pre>
 Disable ballooning title changes (quiet)
</pre>
<dt><code>-r</code></p>
<dd>
<pre>
 Remove this application from the pager
</pre>
<dt><code>-s</code></p>
<dd>
<pre>
 Make the window sticky (appears on all desktops)
</pre>
<dt><code>-t</code></p>
<dd>
<pre>
 Remove this application from the taskbar
</pre>
<dt><code>-v, &#8211;version</code></p>
<dd>
<pre>
 Show the KDocker version string, then exit
</pre>
<dt><code>-w</code> <i>wid</i></p>
<dd>
<pre>
 Window id of the application to dock
 Assumes hex number of the form 0x###...
</pre>
<dt><code>-x</code> <i>pid</i></p>
<dd>
<pre>
 Process id of the application to dock
 Assumes decimal number of the form ###...
</pre>
</dl>
<h2>AUTHOR</h2>
<pre>
 KDocker was written by Girish Ramakrishnan
 Revised and maintained by John Schember
</pre>
<h2>REPORTING BUGS</h2>
<p> Bugs and wishes to the KDocker Home Page &lt;<a rel="nofollow" href="https://github.com/user-none/KDocker">https://github.com/user-none/KDocker</a>&gt; </p>
<h2>Index</h2>
