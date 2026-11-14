---
title: "sdl_wasinit(3)"
name: "sdl_wasinit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_wasinit/"
---

SDL_WasInit - Check which subsystems are initialized
<h2>Synopsis</h2><b>#include &quot;SDL.h&quot; 

 Uint32 SDL_WasInit</b>(<b>Uint32 flags</b>);
<h2>Description</h2><b>SDL_WasInit</b> allows you to see which SDL subsytems have been <i>initialized</i>. <b>flags</b> is a bitwise OR'd combination of the subsystems you wish to check (see <i></i><b>SDL_Init</b> for a list of subsystem flags).
<h2>Return Value</h2><b>SDL_WasInit</b> returns a bitwised OR'd combination of the initialized subsystems.
<h2>Examples</h2><pre><tt>
/* Here are several ways you can use SDL_WasInit() */
/* Get init data on all the subsystems */
Uint32 subsystem_init;
subsystem_init=SDL_WasInit(SDL_INIT_EVERYTHING);
if(subsystem_init&amp;SDL_INIT_VIDEO)
 printf(&quot;Video is initialized.
&quot;);
else
 printf(&quot;Video is not initialized.
&quot;);
/* Just check for one specfic subsystem */
if(SDL_WasInit(SDL_INIT_VIDEO)!=0)
 printf(&quot;Video is initialized.
&quot;);
else
 printf(&quot;Video is not initialized.
&quot;);
/* Check for two subsystems */
Uint32 subsystem_mask=SDL_INIT_VIDEO|SDL_INIT_AUDIO;
if(SDL_WasInit(subsystem_mask)==subsystem_mask)
 printf(&quot;Video and Audio initialized.
&quot;);
else
 printf(&quot;Video and Audio not initialized.
&quot;);
</tt></pre><h2>See Also</h2><i></i><b>SDL_Init</b>, <i></i><b>SDL_Subsystem</b>
