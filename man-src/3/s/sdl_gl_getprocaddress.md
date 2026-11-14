---
title: "sdl_gl_getprocaddress(3)"
name: "sdl_gl_getprocaddress"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_gl_getprocaddress/"
description: "SDL_GL_GetProcAddress – Get the address of a GL function"
---

<p>SDL_GL_GetProcAddress &#8211; Get the address of a GL function</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void *SDL_GL_GetProcAddress</code>(<code>const char* proc</code>);</p>
<h2>Description</h2>
<p>Returns the address of the GL function <code>proc</code>, or <code>NULL</code> if the function is not found. If the GL library is loaded at runtime, with <i></i><code>SDL_GL_LoadLibrary</code>, then <i>all</i> GL functions must be retrieved this way. Usually this is used to retrieve function pointers to OpenGL extensions.</p>
<h2>Example</h2>
<pre><tt>typedef void (*GL_ActiveTextureARB_Func)(unsigned int);
GL_ActiveTextureARB_Func glActiveTextureARB_ptr = 0;
int has_multitexture=1;
.
.
.
/* Get function pointer */
glActiveTextureARB_ptr=(GL_ActiveTextureARB_Func) SDL_GL_GetProcAddress(&quot;glActiveTextureARB&quot;);
/* Check for a valid function ptr */
if(!glActiveTextureARB_ptr){
 fprintf(stderr, &quot;Multitexture Extensions not present.
&quot;);
 has_multitexture=0;
}
.
.
.
.
if(has_multitexture){
 glActiveTextureARB_ptr(GL_TEXTURE0_ARB);
 .
 .
}
else{
 .
 .
}</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_GL_LoadLibrary</code></p>
