---

title: "scroll_screen(3)"
name: "scroll_screen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scroll_screen/"
---

 </p>
<h2>NAME</h2>
<p> scroll_screen &#8211; Requests a hardware scroll request. Allegro game programming library.  </p>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int scroll_screen(int x, int y);</code>  </p>
<p> Attempts to scroll the hardware screen to display a different part of the virtual screen (initially it will be positioned at 0, 0, which is the top left corner). You can use this to move the screen display around in a large virtual screen space, or to page flip back and forth between two non-overlapping areas of the virtual screen. Note that to draw outside the original position in the screen bitmap you will have to alter the clipping rectangle with set_clip_rect(). </p>
<p> Mode-X scrolling is reliable and will work on any card, other drivers may not work or not work reliably. See the platform-specific section of the docs for more information. </p>
<p> Allegro will handle any necessary vertical retrace synchronisation when scrolling the screen, so you don&#8217;t need to call vsync() before it. This means that scroll_screen() has the same time delay effects as vsync().  </p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success. Returns non-zero if the graphics driver can&#8217;t handle hardware scrolling or the virtual screen is not large enough. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-show_video_bitmap/">show_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-request_scroll/">request_scroll</a></code>(3), <code><a href="/docs/linux/man/3-request_video_bitmap/">request_video_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-exscroll/">exscroll</a></code>(3) </p>
