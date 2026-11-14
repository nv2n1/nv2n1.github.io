---
title: "sdl_gl_setattribute(3)"
name: "sdl_gl_setattribute"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_gl_setattribute/"
description: "SDL_GL_SetAttribute – Set a special SDL/OpenGL attribute"
---

<p>SDL_GL_SetAttribute &#8211; Set a special SDL/OpenGL attribute</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_GL_SetAttribute</code>(<code>SDL_GLattr attr, int value</code>);</p>
<h2>Description</h2>
<p>Sets the OpenGL <i>attribute</i> <code>attr</code> to <code>value</code>. The attributes you set don&#8217;t take effect until after a call to <i></i><code>SDL_SetVideoMode</code>. You should use <i></i><code>SDL_GL_GetAttribute</code> to check the values after a <code>SDL_SetVideoMode</code> call.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> on success, or <code>-1</code> on error.</p>
<h2>Example</h2>
<pre><tt>SDL_GL_SetAttribute( SDL_GL_RED_SIZE, 5 );
SDL_GL_SetAttribute( SDL_GL_GREEN_SIZE, 5 );
SDL_GL_SetAttribute( SDL_GL_BLUE_SIZE, 5 );
SDL_GL_SetAttribute( SDL_GL_DEPTH_SIZE, 16 );
SDL_GL_SetAttribute( SDL_GL_DOUBLEBUFFER, 1 );
if ( (screen=SDL_SetVideoMode( 640, 480, 16, SDL_OPENGL )) == NULL ) {
 fprintf(stderr, &quot;Couldn't set GL mode: %s
&quot;, SDL_GetError());
 SDL_Quit();
 return;
}</tt></pre>
<dl COMPACT>
<dd><code>Note: </p>
<p> The SDL_DOUBLEBUF</code> flag is not required to enable double buffering when setting an OpenGL video mode. Double buffering is enabled or disabled using the SDL_GL_DOUBLEBUFFER attribute.</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_GL_GetAttribute</code>, <i>GL Attributes</i></p>
