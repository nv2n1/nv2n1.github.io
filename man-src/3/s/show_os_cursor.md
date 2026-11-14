---
title: "show_os_cursor(3)"
name: "show_os_cursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-show_os_cursor/"
description: "show_os_cursor – Low level function to display the operating system cursor. Allegro game programming library."
---

<p>show_os_cursor &#8211; Low level function to display the operating system cursor. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int show_os_cursor(int cursor);</code></pre>
<h2>Description</h2>
<p>In case you do not need Allegro&#8217;s mouse cursor API, which automatically emulates a cursor in software if no other cursor is available, you can use this low level function to try to display or hide the system cursor directly. The cursor parameter takes the same values as select_mouse_cursor. This function is very similar to calling enable_hardware_cursor, select_mouse_cursor and show_mouse, but will not try to do anything if no system cursor is available. </p>
<p> The most common use for this function is to just call it once at the beginning of the program to tell it to display the system cursor inside the Allegro window. The return value can be used to see if this succeeded or not. On some systems (e.g. DirectX fullscreen) this is not supported and the function will always fail, and in other cases only some of the cursors will work, or in the case of MOUSE_CURSOR_ALLEGRO, only certain bitmap sizes may be supported. </p>
<p> You never should use show_os_cursor together with the function show_mouse and other functions affecting it (select_mouse_cursor, enable_hardware_cursor, disable_hardware_cursor, scare_mouse, unscare_mouse). They implement the standard high level mouse API, and don&#8217;t work together with this low level function.</p>
<h2>Return Value</h2>
<p>Returns 0 if a system cursor is being displayed after the function returns, or -1 otherwise. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_cursor_bitmap/">set_mouse_cursor_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-select_mouse_cursor/">select_mouse_cursor</a></code>(3) </p>
