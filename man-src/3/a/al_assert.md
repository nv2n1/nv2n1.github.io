---
title: "al_assert(3)"
name: "al_assert"
section: "3"
letter: "a"
url: "/docs/linux/man/3-al_assert/"
description: "al_assert – Asserts at the specified file and line number. Allegro game programming library."
---

<h2>NAME</h2>
<p> al_assert &#8211; Asserts at the specified file and line number. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void al_assert(const char *file, int line);</code></p>
<h2>DESCRIPTION</h2>
<p> Raises an assert for an error at the specified file and line number. The file parameter is always given in ASCII format. By default, this will call the system driver&#8217;s assert handler. If there is none, the error will be sent to stderr and the program will abort. However, if the environment variable ALLEGRO_ASSERT is set, this function writes a message into the file specified by the environment variable and program execution will continue. If none of this behaviours is wanted, you can override them with a custom assert handler. </p>
<p> You will usually want to use the ASSERT() macro instead of calling this function directly. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-assert/">ASSERT</a></code>(3), <code><a href="/docs/linux/man/3-al_trace/">al_trace</a></code>(3), <code><a href="/docs/linux/man/3-register_assert_handler/">register_assert_handler</a></code>(3) </p>
<h2>Index</h2>
