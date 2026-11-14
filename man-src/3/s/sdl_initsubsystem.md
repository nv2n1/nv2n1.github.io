---
title: "sdl_initsubsystem(3)"
name: "sdl_initsubsystem"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_initsubsystem/"
description: "SDL_InitSubSystem – Initialize subsystems"
---

<p>SDL_InitSubSystem &#8211; Initialize subsystems</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_InitSubSystem</code>(<code>Uint32 flags</code>);</p>
<h2>Description</h2>
<p>After SDL has been initialized with <i></i><code>SDL_Init</code> you may initialize uninitialized subsystems with <code>SDL_InitSubSystem</code>. The <code>flags</code> parameter is the same as that used in <i></i><code>SDL_Init</code>.</p>
<h2>Examples</h2>
<pre><tt>/* Seperating Joystick and Video initialization. */
SDL_Init(SDL_INIT_VIDEO);
.
.
SDL_SetVideoMode(640, 480, 16, SDL_DOUBLEBUF|SDL_FULLSCREEN);
.
/* Do Some Video stuff */
.
.
/* Initialize the joystick subsystem */
SDL_InitSubSystem(SDL_INIT_JOYSTICK);
/* Do some stuff with video and joystick */
.
.
.
/* Shut them both down */
SDL_Quit();</tt></pre>
<h2>Return Value</h2>
<p>Returns <code>-1</code> on an error or <code>0</code> on success.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Init</code>, <i></i><code>SDL_Quit</code>, <i></i><code>SDL_QuitSubSystem</code></p>
