---
title: "sdl_createmutex(3)"
name: "sdl_createmutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_createmutex/"
description: "SDL_CreateMutex – Create a mutex"
---

<p>SDL_CreateMutex &#8211; Create a mutex</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> SDL_mutex *SDL_CreateMutex</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>Create a new, unlocked mutex.</p>
<h2>Examples</h2>
<pre><tt>SDL_mutex *mut;
mut=SDL_CreateMutex();
.
.
if(SDL_mutexP(mut)==-1){
 fprintf(stderr, &quot;Couldn't lock mutex
&quot;);
 exit(-1);
}
.
/* Do stuff while mutex is locked */
.
.
if(SDL_mutexV(mut)==-1){
 fprintf(stderr, &quot;Couldn't unlock mutex
&quot;);
 exit(-1);
}
SDL_DestroyMutex(mut);
</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_mutexP</code>, <i></i><code>SDL_mutexV</code>, <i></i><code>SDL_DestroyMutex</code></p>
