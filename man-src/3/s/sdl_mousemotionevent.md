---
title: "sdl_mousemotionevent(3)"
name: "sdl_mousemotionevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_mousemotionevent/"
description: "SDL_MouseMotionEvent – Mouse motion event structure"
---

<p>SDL_MouseMotionEvent &#8211; Mouse motion event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 Uint8 state;
 Uint16 x, y;
 Sint16 xrel, yrel;
} SDL_MouseMotionEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_MOUSEMOTION</code></p>
<dt><code>state</code></p>
<dd>The current button state</p>
<dt><code>x</code>, <code>y</code></p>
<dd>The X/Y coordinates of the mouse</p>
<dt><code>xrel</code>, <code>yrel</code></p>
<dd>Relative motion in the X/Y direction</dl>
<h2>Description</h2>
<p><code>SDL_MouseMotionEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_MOUSEMOTION</code> is reported. </p>
<p> Simply put, a <code>SDL_MOUSEMOTION</code> type event occurs when a user moves the mouse within the application window or when <i></i><code>SDL_WarpMouse</code> is called. Both the absolute (<code>x</code> and <code>y</code>) and relative (<code>xrel</code> and <code>yrel</code>) coordinates are reported along with the current button states (<code>state</code>). The button state can be interpreted using the <code>SDL_BUTTON</code> macro (see <i></i><code>SDL_GetMouseState</code>). </p>
<p> If the cursor is hidden (<i></i><code>SDL_ShowCursor</code>(0)) and the input is grabbed (<i></i><code>SDL_WM_GrabInput</code>(SDL_GRAB_ON)), then the mouse will give relative motion events even when the cursor reaches the edge fo the screen. This is currently only implemented on Windows and Linux/Unix-a-likes.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_MouseButtonEvent</code></p>
