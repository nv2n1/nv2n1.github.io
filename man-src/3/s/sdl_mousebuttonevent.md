---
title: "sdl_mousebuttonevent(3)"
name: "sdl_mousebuttonevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_mousebuttonevent/"
description: "SDL_MouseButtonEvent – Mouse button event structure"
---

<p>SDL_MouseButtonEvent &#8211; Mouse button event structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 Uint8 button;
 Uint8 state;
 Uint16 x, y;
} SDL_MouseButtonEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_MOUSEBUTTONDOWN</code> or <code>SDL_MOUSEBUTTONUP</code></p>
<dt><code>button</code></p>
<dd>The mouse button index (SDL_BUTTON_LEFT, SDL_BUTTON_MIDDLE, SDL_BUTTON_RIGHT)</p>
<dt><code>state</code></p>
<dd><code>SDL_PRESSED</code> or <code>SDL_RELEASED</code></p>
<dt><code>x</code>, <code>y</code></p>
<dd>The X/Y coordinates of the mouse at press/release time</dl>
<h2>Description</h2>
<p><code>SDL_MouseButtonEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_MOUSEBUTTONDOWN</code> or <code>SDL_MOUSEBUTTONUP</code> is reported. </p>
<p> When a mouse button press or release is detected then number of the button pressed (from 1 to 255, with 1 usually being the left button and 2 the right) is placed into <code>button</code>, the position of the mouse when this event occured is stored in the <code>x</code> and the <code>y</code> fields. Like <i></i><code>SDL_KeyboardEvent</code>, information on whether the event was a press or a release event is stored in both the <code>type</code> and <code>state</code> fields, but this should be obvious.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_MouseMotionEvent</code></p>
