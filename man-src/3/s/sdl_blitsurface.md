---
title: "sdl_blitsurface(3)"
name: "sdl_blitsurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_blitsurface/"
description: "SDL_BlitSurface – This performs a fast blit from the source surface to the destination surface."
---

<p>SDL_BlitSurface &#8211; This performs a fast blit from the source surface to the destination surface.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_BlitSurface</code>(<code>SDL_Surface *src, SDL_Rect *srcrect, SDL_Surface *dst, SDL_Rect *dstrect</code>);</p>
<h2>Description</h2>
<p>This performs a fast blit from the source surface to the destination surface. </p>
<p> Only the position is used in the <code>dstrect</code> (the width and height are ignored). </p>
<p> If either <code>srcrect</code> or <code>dstrect</code> are <code>NULL</code>, the entire surface (<code>src</code> or <code>dst</code>) is copied. </p>
<p> The final blit rectangle is saved in <code>dstrect</code> after all clipping is performed (<code>srcrect</code> is not modified). </p>
<p> The blit function should not be called on a locked surface. </p>
<p> The results of blitting operations vary greatly depending on whether <code>SDL_SRCAPLHA</code> is set or not. See <i>SDL_SetAlpha</i> for an explaination of how this affects your results. Colorkeying and alpha attributes also interact with surface blitting, as the following pseudo-code should hopefully explain. </p>
<pre><tt>if (source surface has SDL_SRCALPHA set) {
 if (source surface has alpha channel (that is, format-&gt;Amask != 0))
 blit using per-pixel alpha, ignoring any colour key
 else {
 if (source surface has SDL_SRCCOLORKEY set)
 blit using the colour key AND the per-surface alpha value
 else
 blit using the per-surface alpha value
 }
} else {
 if (source surface has SDL_SRCCOLORKEY set)
 blit using the colour key
 else
 ordinary opaque rectangular blit
}</tt></pre>
<h2>Return Value</h2>
<p>If the blit is successful, it returns <code>0</code>, otherwise it returns <code>-1</code>. </p>
<p> If either of the surfaces were in video memory, and the blit returns <code>-2</code>, the video memory was lost, so it should be reloaded with artwork and re-blitted: </p>
<pre><tt> while ( SDL_BlitSurface(image, imgrect, screen, dstrect) == -2 ) {
 while ( SDL_LockSurface(image)) &lt; 0 )
 Sleep(10);
 -- Write image pixels to image-&gt;pixels --
 SDL_UnlockSurface(image);
 }</tt></pre>
<p>&nbsp;<wbr>This happens under DirectX 5.0 when the system switches away from your fullscreen application. Locking the surface will also fail until you have access to the video memory again.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_LockSurface</code>, <i></i><code>SDL_FillRect</code>, <i></i><code>SDL_Surface</code>, <i></i><code>SDL_Rect</code></p>
