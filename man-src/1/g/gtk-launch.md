---
title: "gtk-launch(1)"
name: "gtk-launch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-launch/"
description: "gtk-launch – Launch an application"
---

<h2 class="name">NAME</h2>
<p> gtk-launch &#8211; Launch an application </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gtk-launch</code> [OPTION&#8230;] APPLICATION [URI&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gtk-launch</code></p>
<dd>launches an application using the given name. The application is started with proper startup notification on a default display, unless specified otherwise. </p>
<p> <code>gtk-launch</code> takes at least one argument, the name of the application to launch. The name should match application desktop file name, as residing in /usr/share/application, with or without the &#8216;.desktop&#8217; suffix. </p>
<p> If called with more than one argument, the rest of them besides the application name are considered URI locations and are passed as arguments to the launched application.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints the program version and exits.</dl>
<h2>Index</h2>
