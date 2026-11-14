---
title: "florence(1)"
name: "florence"
section: "1"
letter: "f"
url: "/docs/linux/man/1-florence/"
description: "florence – extensible and scalable virtual keyboard for GNOME"
---

<h2 class="name">NAME</h2>
<p> florence &#8211; extensible and scalable virtual keyboard for GNOME </p>
<h2>SYNOPSIS</h2>
<p> <code>florence</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> Florence is an extensible scalable virtual keyboard for GNOME. You need it if you can&#8217;t use a real hardware keyboard, for example because of injury, handicap, your keyboard is broken or because you use a tablet PC, but you must be able to use a pointing device (as a mouse, a trackball, a touchscreen or opengazer); If you can&#8217;t use a pointing device, there is gok, which can be used with just simple switches. </p>
<p> Florence stays out of your way when you don&#8217;t need it: it appears on the screen only when you need it. A timer-based auto-click input method is available to help disabled people having difficulties to click. The ramble mode is another efficient input method that can help. </p>
<p> Florence is primarily intended to be used with the GNOME desktop, although it can be used on any desktop environment by using the <code>&#8211;no-gnome</code> option.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Print help message and exit.</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
<dd> Print Florence version and exit.</dl>
<p> <code>-c, &#8211;config</code></p>
<dl>
<dt>
<dd> Open configuration dialog.</dl>
<p> <code>-d, &#8211;debug</code></p>
<dl>
<dt>
<dd> Launch Florence in verbose mode.</dl>
<p> <code>-n, &#8211;no-gnome</code></p>
<dl>
<dt>
<dd> Use this option if you are not using the GNOME desktop environment. This will disable some GNOME specific features.</dl>
<p> <code>-f</code> <code>, &#8211;focus</code>[<code>=</code><i>WINDOW</i>]</p>
<dl>
<dt>
<dd> With this option, any florence input will go to the selected window. The window argument is the name of the window (the one that most window managers put in the title bar). if the window argument is not provided, florence will select the last focused window. This option is useful for window managers that don&#8217;t support the &quot;not focusable&quot; hint and focus the keyboard window instead of the output one. It can also be useful if you want to input text to a window that is not focused. This option must be used for the keyboard to work in GDM.</dl>
<p> <code>-u</code> <i>FILE</i>, <code>&#8211;use-config=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Use the configuration file provided instead of gconf. The configuration file is a key-value pair file with sections. An example of configuration file is provided at <i>/usr/share/doc/florence/examples/florence.conf</i>.</dl>
<h2>SEE ALSO</h2>
<p> Florence documentation in the GNOME help system. </p>
<p> Florence website: <a rel="nofollow" href="http://florence.sourceforge.net/">http://florence.sourceforge.net/</a></p>
<h2>AUTHOR</h2>
<p> François Agrech &lt;f.agrech [at] gmail.com&gt; </p>
<h2>Index</h2>
