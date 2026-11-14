---
title: "select_mouse_cursor(3)"
name: "select_mouse_cursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-select_mouse_cursor/"
description: "select_mouse_cursor – Tells Allegro to select software or hardware cursor drawing."
---

<p>select_mouse_cursor &#8211; Tells Allegro to select software or hardware cursor drawing.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void select_mouse_cursor(int cursor);</code></pre>
<h2>Description</h2>
<p>This function allows you to use the operating system&#8217;s native mouse cursors rather than some custom cursor. You will need to enable this functionality by calling enable_hardware_cursor() beforehand. If the operating system does not support this functionality, or if it has not been enabled, then Allegro will substitute its own cursor images. You can change these substitute images using set_mouse_cursor_bitmap(). Note that the effects of this function are not apparent until show_mouse() is called. To know whether the operating system&#8217;s native cursor is being used, or if Allegro has made a substitution, you can check the GFX_SYSTEM_CURSOR flag in gfx_capabilities after calling show_mouse(). The cursor argument selects the type of cursor to be displayed: <code>MOUSE_CURSOR_NONE</code> Selects an invisible mouse cursor. In that sense, it is similar to calling show_mouse(NULL); <code>MOUSE_CURSOR_ALLEGRO</code> Selects the custom Allegro cursor, i.e. the one that you set with set_mouse_sprite(). <code>MOUSE_CURSOR_ARROW</code> The operating system default arrow cursor. <code>MOUSE_CURSOR_BUSY</code> The operating system default `busy&#8217; cursor (hourglass). <code>MOUSE_CURSOR_QUESTION</code> The operating system default `question&#8217; cursor (arrow with question mark). <code>MOUSE_CURSOR_EDIT</code> The operating system default `edit&#8217; cursor (vertical bar). Example: </p>
<pre> /* initialize mouse sub-system */
 install_mouse();
 enable_hardware_cursor();
 
 /* Set busy pointer */
 select_mouse_cursor(MOUSE_CURSOR_BUSY);
 show_mouse(screen);
 
 /* Initialize stuff */
 ...
 
 /* Set normal arrow pointer */
 select_mouse_cursor(MOUSE_CURSOR_ARROW);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-show_mouse/">show_mouse</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_sprite/">set_mouse_sprite</a></code>(3), <code><a href="/docs/linux/man/3-gfx_capabilities/">gfx_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-enable_hardware_cursor/">enable_hardware_cursor</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_cursor_bitmap/">set_mouse_cursor_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-show_os_cursor/">show_os_cursor</a></code>(3), <code><a href="/docs/linux/man/3-exsyscur/">exsyscur</a></code>(3) </p>
