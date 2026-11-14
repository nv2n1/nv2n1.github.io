---
title: "sdl_resizeevent(3)"
name: "sdl_resizeevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_resizeevent/"
description: "SDL_ResizeEvent – Window resize event structure"
---

<p>SDL_ResizeEvent &#8211; Window resize event structure</p>
<h2>Structure Definition</h2>
<pre>
<tt>typedef struct{
  Uint8 type;
  int w, h;
} SDL_ResizeEvent;</tt>
</pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd> <code>SDL_VIDEORESIZE</code></p>
<dt><code>w</code>, <code>h</code></p>
<dd> New width and height of the window</dl>
<h2>Description</h2>
<p> <code>SDL_ResizeEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_VIDEORESIZE</code> is reported. </p>
<p> When <code>SDL_RESIZABLE</code> is passed as a <code>flag</code> to <i></i><code>SDL_SetVideoMode</code> the user is allowed to resize the applications window. When the window is resized an <code>SDL_VIDEORESIZE</code> is report, with the new window width and height values stored in <code>w</code> and <code>h</code>, respectively. When an <code>SDL_VIDEORESIZE</code> is received the window should be resized to the new dimensions using <i></i><code>SDL_SetVideoMode</code>.</p>
<h2>See Also</h2>
<p> <i></i><code>SDL_Event</code>, <i></i><code>SDL_SetVideoMode</code></p>
