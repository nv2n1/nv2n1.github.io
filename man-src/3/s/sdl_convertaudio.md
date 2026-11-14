---
title: "sdl_convertaudio(3)"
name: "sdl_convertaudio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_convertaudio/"
description: "SDL_ConvertAudio – Convert audio data to a desired audio format."
---

<p>SDL_ConvertAudio &#8211; Convert audio data to a desired audio format.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_ConvertAudio</code>(<code>SDL_AudioCVT *cvt</code>);</p>
<h2>Description</h2>
<p><code>SDL_ConvertAudio</code> takes one parameter, <code>cvt</code>, which was previously initilized. Initilizing a <i></i><code>SDL_AudioCVT</code> is a two step process. First of all, the structure must be passed to <i></i><code>SDL_BuildAudioCVT</code> along with source and destination format parameters. Secondly, the <code>cvt</code>-&gt;<code>buf</code> and <code>cvt</code>-&gt;<code>len</code> fields must be setup. <code>cvt</code>-&gt;<code>buf</code> should point to the audio data and <code>cvt</code>-&gt;<code>len</code> should be set to the length of the audio data in bytes. Remember, the length of the buffer pointed to by <code>buf</code> show be <code>len</code>*<code>len_mult</code> bytes in length. </p>
<p> Once the <code>SDL_AudioCVT</code>structure is initilized then we can pass it to <code>SDL_ConvertAudio</code>, which will convert the audio data pointer to by <code>cvt</code>-&gt;<code>buf</code>. If <code>SDL_ConvertAudio</code> returned <code>0</code> then the conversion was completed successfully, otherwise <code>-1</code> is returned. </p>
<p> If the conversion completed successfully then the converted audio data can be read from <code>cvt</code>-&gt;<code>buf</code>. The amount of valid, converted, audio data in the buffer is equal to <code>cvt</code>-&gt;<code>len</code>*<code>cvt</code>-&gt;<code>len_ratio</code>.</p>
<h2>Examples</h2>
<pre><tt>/* Converting some WAV data to hardware format */
void my_audio_callback(void *userdata, Uint8 *stream, int len);
SDL_AudioSpec *desired, *obtained;
SDL_AudioSpec wav_spec;
SDL_AudioCVT wav_cvt;
Uint32 wav_len;
Uint8 *wav_buf;
int ret;
/* Allocated audio specs */
desired=(SDL_AudioSpec *)malloc(sizeof(SDL_AudioSpec));
obtained=(SDL_AudioSpec *)malloc(sizeof(SDL_AudioSpec));
/* Set desired format */
desired-&gt;freq=22050;
desired-&gt;format=AUDIO_S16LSB;
desired-&gt;samples=8192;
desired-&gt;callback=my_audio_callback;
desired-&gt;userdata=NULL;
/* Open the audio device */
if ( SDL_OpenAudio(desired, obtained) &lt; 0 ){
 fprintf(stderr, &quot;Couldn't open audio: %s
&quot;, SDL_GetError());
 exit(-1);
}
 
free(desired);
/* Load the test.wav */
if( SDL_LoadWAV(&quot;test.wav&quot;, &amp;wav_spec, &amp;wav_buf, &amp;wav_len) == NULL ){
 fprintf(stderr, &quot;Could not open test.wav: %s
&quot;, SDL_GetError());
 SDL_CloseAudio();
 free(obtained);
 exit(-1);
}
 
/* Build AudioCVT */
ret = SDL_BuildAudioCVT(&amp;wav_cvt,
 wav_spec.format, wav_spec.channels, wav_spec.freq,
 obtained-&gt;format, obtained-&gt;channels, obtained-&gt;freq);
/* Check that the convert was built */
if(ret==-1){
 fprintf(stderr, &quot;Couldn't build converter!
&quot;);
 SDL_CloseAudio();
 free(obtained);
 SDL_FreeWAV(wav_buf);
}
/* Setup for conversion */
wav_cvt.buf=(Uint8 *)malloc(wav_len*wav_cvt.len_mult);
wav_cvt.len=wav_len;
memcpy(wav_cvt.buf, wav_buf, wav_len);
/* We can delete to original WAV data now */
SDL_FreeWAV(wav_buf);
/* And now we're ready to convert */
SDL_ConvertAudio(&amp;wav_cvt);
/* do whatever */
.
.
.
.
</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_BuildAudioCVT</code>, <i></i><code>SDL_AudioCVT</code></p>
