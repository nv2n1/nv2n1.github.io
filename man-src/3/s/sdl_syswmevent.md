---
title: "sdl_syswmevent(3)"
name: "sdl_syswmevent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_syswmevent/"
description: "SDL_SysWMEvent – Platform-dependent window manager event."
---

<p>SDL_SysWMEvent &#8211; Platform-dependent window manager event.</p>
<h2>Description</h2>
<p>The system window manager event contains a pointer to system-specific information about unknown window manager events. If you enable this event using <i></i><code>SDL_EventState()</code>, it will be generated whenever unhandled events are received from the window manager. This can be used, for example, to implement cut-and-paste in your application. </p>
<pre><tt>typedef struct {
 Uint8 type; /* Always SDL_SysWM */
 } SDL_SysWMEvent;</tt></pre>
<p>&nbsp;<wbr>If you want to obtain system-specific information about the window manager, you can fill the version member of a&nbsp;<wbr><code>SDL_SysWMinfo</code>&nbsp;<wbr>structure&nbsp;<wbr>(details can be found in&nbsp;<wbr><code>SDL_syswm.h</code>, which must be included)&nbsp;<wbr>using the&nbsp;<wbr><code>SDL_VERSION()</code>&nbsp;<wbr>macro found in&nbsp;<wbr><code>SDL_version.h</code>, and pass it to the function:&nbsp;<wbr> </p>
<p> <code>int SDL_GetWMInfo</code>(<code>SDL_SysWMinfo *info</code>);</p>
<h2>See Also</h2>
<p><i></i><code>SDL_EventState</code></p>
