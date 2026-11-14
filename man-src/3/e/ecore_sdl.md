---
title: "ecore_sdl(3)"
name: "ecore_sdl"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_sdl/"
description: "Ecore_Sdl.h – Ecore SDL system functions."
---

<p>Ecore_Sdl.h &#8211; Ecore SDL system functions. </p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>_Ecore_Sdl_Event_Key_Down</code><br />
 <i>SDL Key Down event. </i><br />
 struct <code>_Ecore_Sdl_Event_Key_Up</code><br />
 <i>SDL Key Up event. </i><br />
 struct <code>_Ecore_Sdl_Event_Mouse_Button_Down</code><br />
 <i>SDL Mouse Down event. </i><br />
 struct <code>_Ecore_Sdl_Event_Mouse_Button_Up</code><br />
 <i>SDL Mouse Up event. </i><br />
 struct <code>_Ecore_Sdl_Event_Mouse_Move</code><br />
 <i>SDL Mouse Move event. </i><br />
 struct <code>_Ecore_Sdl_Event_Mouse_Wheel</code><br />
 <i>SDL Mouse Wheel event. </i></p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_sdl_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_Sdl library. </i></p>
<h3>Variables</h3>
<p>EAPI int <code>ECORE_SDL_EVENT_KEY_DOWN</code><br />
 <i>SDL Key Down event. </i><br />
 EAPI int <code>ECORE_SDL_EVENT_KEY_UP</code><br />
 <i>SDL Key Up event. </i><br />
 EAPI int <code>ECORE_SDL_EVENT_MOUSE_BUTTON_DOWN</code><br />
 <i>SDL Mouse Down event. </i><br />
 EAPI int <code>ECORE_SDL_EVENT_MOUSE_BUTTON_UP</code><br />
 <i>SDL Mouse Up event. </i><br />
 EAPI int <code>ECORE_SDL_EVENT_MOUSE_MOVE</code><br />
 <i>SDL Mouse Move event. </i><br />
 EAPI int <code>ECORE_SDL_EVENT_MOUSE_WHEEL</code><br />
 <i>SDL Mouse Wheel event. </i><br />
 EAPI int <code>ECORE_SDL_EVENT_GOT_FOCUS</code><br />
 <i>SDL Mouse Wheel event. </i><br />
 EAPI int <code>ECORE_SDL_EVENT_LOST_FOCUS</code><br />
 <i>SDL Mouse Wheel event. </i></p>
<h2>Detailed Description</h2>
<p>Ecore SDL system functions. </p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_sdl_shutdown (void)</h3>
<p>Shuts down the Ecore_Sdl library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of times the system has been initialised without being shut down.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
