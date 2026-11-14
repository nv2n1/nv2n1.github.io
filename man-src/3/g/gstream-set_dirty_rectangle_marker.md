---
title: "gstream-set_dirty_rectangle_marker(3)"
name: "gstream-set_dirty_rectangle_marker"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_dirty_rectangle_marker/"
description: "set_dirty_rectangle_marker"
---

<h2>NAME</h2>
<p> set_dirty_rectangle_marker</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_dirty_rectangle_marker(void (*drm)(int, int, int, int))</code></p>
<h2>DESCRIPTION</h2>
<p> Sets a function which the gstream will use to mark the areas that it draws inside as &quot;dirty&quot;; this can, for instance, be very useful in conjuction with a dirty rectangle system in a game where you are using the gstream to output various information during the main loop. The gstream will then automatically be able to inform the system about the parts of the bitmap it has changed so that you don&#8217;t have to take up that responsibility. </p>
<p> The provided function will be given the parameters: x and y coordinates, and width and height of the rectangle, in that order. So if you&#8217;re using DRS, you could call this function like this (since that function takes these four parameters x, y, width, height directly): </p>
<pre>
   set_dirty_rectangle_marker(DRS_add_rectangle);  
   
</pre>
<p> The marker type function is typedef&#8217;ed in the class gbuf, which may come in handy in some situations: </p>
<pre><code>
gbuf::dirty_rectangle_marker tmp_drm;

//...

tmp_drm = gs1.get_dirty_rectangle_marker();
gs1.set_dirty_rectangle_marker(gs2.get_dirty_rectangle_marker());
gs2.set_dirty_rectangle_marker(tmp_drm);
</code></pre>
<p> Pass the function a null pointer to prevent the gstream from thinking about dirty rectangles, e.g. </p>
<pre><code>
set_dirty_rectangle_marker(0); // or perhaps
set_dirty_rectangle_marker(NULL);
</code></pre>
<p> If you don&#8217;t know what the &quot;dirty&quot; principle is all about: well, it is a screen-updating technique similar to double buffering but where you mark the areas that you have drawn on (which made them dirty), and then later when you need to update the screen only blit these areas (thereby cleaning the,) instead of the whole buffer. I suggest you get your hands on DRS if this has made you curious, since it contains an longer introduction to the principle (and also the routines to make it work, by the way :-). It can be fetched at </p>
<p> <a rel="nofollow" href="http://sunsite.dk/olau/drs/">http://sunsite.dk/olau/drs/</a> </p>
<p> The default value of the dirty rectangle marker is the null pointer so that the gstream will not bother marking any rectangles. </p>
<p> Note that only the outputter will mark any rectangles dirty, and not the inputter since it is blocking program anyway, waiting for input, meanwhile preventing the main loop from reaching the place where it updates the rectangles. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-get_dirty_rectangle_marker/">gstream-get_dirty_rectangle_marker</a></code>(3) </p>
<h2>Index</h2>
