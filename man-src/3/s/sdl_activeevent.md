---
title: "sdl_activeevent(3)"
name: "sdl_activeevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_activeevent/"
description: "SDL_ActiveEvent – Application visibility event structure"
---

<p>SDL_ActiveEvent &#8211; Application visibility event structure</p>
<h2>Structure Definition</h2>
<pre>
<tt>typedef struct{
  Uint8 type;
  Uint8 gain;
  Uint8 state;
} SDL_ActiveEvent;</tt>
</pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd> <code>SDL_ACTIVEEVENT.</code></p>
<dt><code>gain</code></p>
<dd> 0 if the event is a loss or 1 if it is a gain.</p>
<dt><code>state</code></p>
<dd> <code>SDL_APPMOUSEFOCUS</code> if mouse focus was gained or lost, <code>SDL_APPINPUTFOCUS</code> if input focus was gained or lost, or <code>SDL_APPACTIVE</code> if the application was iconified (<code>gain</code>=0) or restored(<code>gain</code>=1).</dl>
<h2>Description</h2>
<p> <code>SDL_ActiveEvent</code> is a member of the <i></i><code>SDL_Event</code> union and is used when an event of type <code>SDL_ACTIVEEVENT</code> is reported. </p>
<p> When the mouse leaves or enters the window area a <code>SDL_APPMOUSEFOCUS</code> type activation event occurs, if the mouse entered the window then <code>gain</code> will be 1, otherwise <code>gain</code> will be 0. A <code>SDL_APPINPUTFOCUS</code> type activation event occurs when the application loses or gains keyboard focus. This usually occurs when another application is made active. Finally, a <code>SDL_APPACTIVE</code> type event occurs when the application is either minimised/iconified (<code>gain</code>=0) or restored. </p>
<dl COMPACT>
<dt>
<dd> <code>Note: </p>
<p> This event does not occur when an application window is first created.</dl>
<p> </code></p>
<h2>See Also</h2>
<p> <i></i><code>SDL_Event</code>, <i></i><code>SDL_GetAppState</code></p>
