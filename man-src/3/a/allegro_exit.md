---
title: "allegro_exit(3)"
name: "allegro_exit"
section: "3"
letter: "a"
url: "/docs/linux/man/3-allegro_exit/"
description: "allegro_exit – Closes down the Allegro system."
---

<h2>NAME</h2>
<p> allegro_exit &#8211; Closes down the Allegro system.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void allegro_exit();</code></p>
<h2>DESCRIPTION</h2>
<p> Closes down the Allegro system. This includes returning the system to text mode and removing whatever mouse, keyboard, and timer routines have been installed. You don&#8217;t normally need to bother making an explicit call to this function, because allegro_init() installs it as an atexit() routine so it will be called automatically when your program exits. </p>
<p> Note that after you call this function, other functions like destroy_bitmap() will most likely crash. This is a problem for C++ global destructors, which usually get called after atexit(), so don&#8217;t put Allegro calls in them. You can write the destructor code in another method which you can manually call before your program exits, avoiding this problem. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_allegro/">install_allegro</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3), <code><a href="/docs/linux/man/3-exxfade/">exxfade</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3) </p>
<h2>Index</h2>
