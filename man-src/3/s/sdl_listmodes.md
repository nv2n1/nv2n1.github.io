---
title: "sdl_listmodes(3)"
name: "sdl_listmodes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_listmodes/"
description: "SDL_ListModes – Returns a pointer to an array of available screen dimensions for the given format and video flags"
---

<p>SDL_ListModes &#8211; Returns a pointer to an array of available screen dimensions for the given format and video flags</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_Rect **SDL_ListModes</code>(<code>SDL_PixelFormat *format, Uint32 flags</code>);</p>
<h2>Description</h2>
<p>Return a pointer to an array of available screen dimensions for the given format and video flags, sorted largest to smallest. Returns <code>NULL</code> if there are no dimensions available for a particular format, or <code>-1</code> if any dimension is okay for the given format. </p>
<p> If <code>format</code> is <code>NULL</code>, the mode list will be for the format returned by <i>SDL_GetVideoInfo()</i>-&gt;<code>vfmt</code>. The <code>flag</code> parameter is an OR&#8217;d combination of <i>surface</i> flags. The flags are the same as those used <i></i><code>SDL_SetVideoMode</code> and they play a strong role in deciding what modes are valid. For instance, if you pass <code>SDL_HWSURFACE</code> as a flag only modes that support hardware video surfaces will be returned.</p>
<h2>Example</h2>
<pre><tt>SDL_Rect **modes;
int i;
.
.
.
/* Get available fullscreen/hardware modes */
modes=SDL_ListModes(NULL, SDL_FULLSCREEN|SDL_HWSURFACE);
/* Check is there are any modes available */
if(modes == (SDL_Rect **)0){
 printf(&quot;No modes available!
&quot;);
 exit(-1);
}
/* Check if or resolution is restricted */
if(modes == (SDL_Rect **)-1){
 printf(&quot;All resolutions available.
&quot;);
}
else{
 /* Print valid modes */
 printf(&quot;Available Modes
&quot;);
 for(i=0;modes[i];++i)
 printf(&quot; %d x %d
&quot;, modes[i]-&gt;w, modes[i]-&gt;h);
}
.
.</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_SetVideoMode</code>, <i></i><code>SDL_GetVideoInfo</code>, <i></i><code>SDL_Rect</code>, <i></i><code>SDL_PixelFormat</code></p>
