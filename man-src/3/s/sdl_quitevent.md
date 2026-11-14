---
title: "sdl_quitevent(3)"
name: "sdl_quitevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_quitevent/"
description: "SDL_QuitEvent – Quit requested event"
---

<p>SDL_QuitEvent &#8211; Quit requested event</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type
} SDL_QuitEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_QUIT</code></dl>
<h2>Description</h2>
<p><code>SDL_QuitEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used whan an event of type <code>SDL_QUIT</code> is reported. </p>
<p> As can be seen, the SDL_QuitEvent structure serves no useful purpose. The event itself, on the other hand, is very important. If you filter out or ignore a quit event then it is impossible for the user to close the window. On the other hand, if you do accept a quit event then the application window will be closed, and screen updates will still report success event though the application will no longer be visible. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> The macro SDL_QuitRequested</code> will return non-zero if a quit event is pending</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_SetEventFilter</code></p>
