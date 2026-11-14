---
title: "sdl_userevent(3)"
name: "sdl_userevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_userevent/"
description: "SDL_UserEvent – A user-defined event type"
---

<p>SDL_UserEvent &#8211; A user-defined event type</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 type;
 int code;
 void *data1;
 void *data2;
} SDL_UserEvent;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>type</code></p>
<dd><code>SDL_USEREVENT</code> through to <code>SDL_NUMEVENTS-1</code></p>
<dt><code>code</code></p>
<dd>User defined event code</p>
<dt><code>data1</code></p>
<dd>User defined data pointer</p>
<dt><code>data2</code></p>
<dd>User defined data pointer</dl>
<h2>Description</h2>
<p><code>SDL_UserEvent</code> is in the <code>user</code> member of the structure <i></i><code>SDL_Event</code>. This event is unique, it is never created by SDL but only by the user. The event can be pushed onto the event queue using <i></i><code>SDL_PushEvent</code>. The contents of the structure members or completely up to the programmer, the only requirement is that <code>type</code> is a value from <code>SDL_USEREVENT</code> to <code>SDL_NUMEVENTS-1</code> (inclusive).</p>
<h2>Examples</h2>
<pre><tt>SDL_Event event;
event.type = SDL_USEREVENT;
event.user.code = my_event_code;
event.user.data1 = significant_data;
event.user.data2 = 0;
SDL_PushEvent(&amp;event);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_Event</code>, <i></i><code>SDL_PushEvent</code></p>
