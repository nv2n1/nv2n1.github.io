---
title: "sdl_openaudio(3)"
name: "sdl_openaudio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_openaudio/"
description: "SDL_OpenAudio – Opens the audio device with the desired parameters."
---

<p>SDL_OpenAudio &#8211; Opens the audio device with the desired parameters.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_OpenAudio</code>(<code>SDL_AudioSpec *desired, SDL_AudioSpec *obtained</code>);</p>
<h2>Description</h2>
<p>This function opens the audio device with the <code>desired</code> parameters, and returns 0 if successful, placing the actual hardware parameters in the structure pointed to by <code>obtained</code>. If <code>obtained</code> is NULL, the audio data passed to the callback function will be guaranteed to be in the requested format, and will be automatically converted to the hardware audio format if necessary. This function returns -1 if it failed to open the audio device, or couldn&#8217;t set up the audio thread. </p>
<p> To open the audio device a <code>desired</code> <i></i><code>SDL_AudioSpec</code> must be created. </p>
<pre><tt>SDL_AudioSpec *desired;
.
.
desired=(SDL_AudioSpec *)malloc(sizeof(SDL_AudioSpec));</tt></pre>
<p>&nbsp;<wbr>You must then fill this structure with your desired audio specifications.</p>
<dl COMPACT>
<dt><code>desired</code>-&gt;<code>freq</code></p>
<dd>
<dt><code>desired</code>-&gt;<code>format</code></p>
<dd>
<dt><code>desired</code>-&gt;<code>samples</code></p>
<dd>
<dt><code>desired</code>-&gt;<code>callback</code></p>
<dd></dl>
<pre><tt>void callback(void *userdata, Uint8 *stream, int len);</tt></pre>
<p>&nbsp;<wbr><code>userdata</code>&nbsp;<wbr>is the pointer stored in&nbsp;<wbr><code>userdata</code>&nbsp;<wbr>field of the&nbsp;<wbr><code>SDL_AudioSpec</code>.&nbsp;<wbr><code>stream</code>&nbsp;<wbr>is a pointer to the audio buffer you want to fill with information and&nbsp;<wbr><code>len</code>&nbsp;<wbr>is the length of the audio buffer in bytes.</p>
<dl COMPACT>
<dt><code>desired</code>-&gt;<code>userdata</code></p>
<dd></dl>
<p> <code>SDL_OpenAudio</code> reads these fields from the <code>desired</code> <code>SDL_AudioSpec</code> structure pass to the function and attempts to find an audio configuration matching your <code>desired</code>. As mentioned above, if the <code>obtained</code> parameter is <code>NULL</code> then SDL with convert from your <code>desired</code> audio settings to the hardware settings as it plays. </p>
<p> If <code>obtained</code> is <code>NULL</code> then the <code>desired</code> <code>SDL_AudioSpec</code> is your working specification, otherwise the <code>obtained</code> <code>SDL_AudioSpec</code> becomes the working specification and the <code>desirec</code> specification can be deleted. The data in the working specification is used when building <code>SDL_AudioCVT</code>&#8216;s for converting loaded data to the hardware format. </p>
<p> <code>SDL_OpenAudio</code> calculates the <code>size</code> and <code>silence</code> fields for both the <code>desired</code> and <code>obtained</code> specifications. The <code>size</code> field stores the total size of the audio buffer in bytes, while the <code>silence</code> stores the value used to represent silence in the audio buffer </p>
<p> The audio device starts out playing <code>silence</code> when it&#8217;s opened, and should be enabled for playing by calling <i></i><code>SDL_PauseAudio</code>(<code>0</code>) when you are ready for your audio <code>callback</code> function to be called. Since the audio driver may modify the requested <code>size</code> of the audio buffer, you should allocate any local mixing buffers after you open the audio device.</p>
<h2>Examples</h2>
<pre><tt>/* Prototype of our callback function */
void my_audio_callback(void *userdata, Uint8 *stream, int len);
/* Open the audio device */
SDL_AudioSpec *desired, *obtained;
SDL_AudioSpec *hardware_spec;
/* Allocate a desired SDL_AudioSpec */
desired=(SDL_AudioSpec *)malloc(sizeof(SDL_AudioSpec));
/* Allocate space for the obtained SDL_AudioSpec */
obtained=(SDL_AudioSpec *)malloc(sizeof(SDL_AudioSpec));
/* 22050Hz - FM Radio quality */
desired-&gt;freq=22050;
/* 16-bit signed audio */
desired-&gt;format=AUDIO_S16LSB;
/* Mono */
desired-&gt;channels=0;
/* Large audio buffer reduces risk of dropouts but increases response time */
desired-&gt;samples=8192;
/* Our callback function */
desired-&gt;callback=my_audio_callback;
desired-&gt;userdata=NULL;
/* Open the audio device */
if ( SDL_OpenAudio(desired, obtained) &lt; 0 ){
 fprintf(stderr, &quot;Couldn't open audio: %s
&quot;, SDL_GetError());
 exit(-1);
}
/* desired spec is no longer needed */
free(desired);
hardware_spec=obtained;
.
.
/* Prepare callback for playing */
.
.
.
/* Start playing */
SDL_PauseAudio(0);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_AudioSpec</code>, <i></i><code>SDL_LockAudio</code>, <i></i><code>SDL_UnlockAudio</code>, <i></i><code>SDL_PauseAudio</code></p>
