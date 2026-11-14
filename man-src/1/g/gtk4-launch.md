---
title: "gtk4-launch(1)"
name: "gtk4-launch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk4-launch/"
description: "gtk4-launch – Launch an application"
---

<h2 class="name">NAME</h2>
<p> gtk4-launch &#8211; Launch an application </p>
<h2>SYNOPSIS</h2>
<pre><code>
gtk4 - launch[OPTIONS...]&lt;APPLICATION&gt;[URI...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>gtk4-launch</code> launches an application using the given name. The application is started with proper startup notification on a default display, unless specified otherwise. </p>
<p> <code>gtk4-launch</code> takes at least one argument, the name of the application to launch. The name should match application desktop file name, as residing in the applications subdirectories of the XDG data directories, with or without the <code>.desktop</code> suffix. </p>
<p> If called with more than one argument, the rest of them besides the application name are considered URI locations and are passed as arguments to the launched application.</p>
<h2>OPTIONS</h2>
<p> <code>-?, -h, &#8211;help</code> Print the command&#8217;s help and exit. </p>
<p> <code>&#8211;version</code> Print the command&#8217;s version and exit.</p>
<h2>ENVIRONMENT</h2>
<p> Some environment variables affect the behavior of <code>gtk4-launch</code>: </p>
<p> <code>XDG_DATA_HOME, XDG_DATA_DIRS</code> The environment variables specifying the XDG data directories. </p>
<h2>Index</h2>
