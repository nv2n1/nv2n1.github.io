---
title: "show_mouse(3)"
name: "show_mouse"
section: "3"
letter: "s"
url: "/docs/linux/man/3-show_mouse/"
description: "show_mouse – Tells Allegro to display a mouse pointer on the screen."
---

<p>show_mouse &#8211; Tells Allegro to display a mouse pointer on the screen.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void show_mouse(BITMAP *bmp);</code></pre>
<h2>Description</h2>
<p>Tells Allegro to display a mouse pointer on the screen. This will only work if the timer module has been installed. The mouse pointer will be drawn onto the specified bitmap, which should normally be `screen&#8217; (see later for information about bitmaps). To hide the mouse pointer, call show_mouse(NULL). Warning: if you draw anything onto the screen while the pointer is visible, a mouse movement interrupt could occur in the middle of your drawing operation. If this happens the mouse buffering and graphics drawing code will get confused and will leave &#8216;mouse droppings&#8217; all over the screen. To prevent this, you must make sure you turn off the mouse pointer whenever you draw onto the screen. This is not needed if you are using a hardware cursor. Note: you must not be showing a mouse pointer on a bitmap at the time that the bitmap is destroyed with destroy_bitmap(), e.g. call show_mouse(NULL); before destroying the bitmap. This does not apply to `screen&#8217; since you never destroy `screen&#8217; with destroy_bitmap(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_mouse/">install_mouse</a></code>(3), <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-set_mouse_sprite/">set_mouse_sprite</a></code>(3), <code><a href="/docs/linux/man/3-scare_mouse/">scare_mouse</a></code>(3), <code><a href="/docs/linux/man/3-freeze_mouse_flag/">freeze_mouse_flag</a></code>(3), <code><a href="/docs/linux/man/3-show_os_cursor/">show_os_cursor</a></code>(3), <code><a href="/docs/linux/man/3-exmouse/">exmouse</a></code>(3), <code><a href="/docs/linux/man/3-expal/">expal</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exsyscur/">exsyscur</a></code>(3) </p>
