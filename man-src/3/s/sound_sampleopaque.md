---
title: "sound_sampleopaque(3)"
name: "sound_sampleopaque"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sound_sampleopaque/"
description: "Sound_Sample – Represents sound data in the process of being decoded."
---

<p>Sound_Sample &#8211; Represents sound data in the process of being decoded. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/SDL_sound.h">SDL_sound.h</a>&gt; </p>
<h3>Data Fields</h3>
<p>void * <code>opaque</code> </p>
<p> const <code>Sound_DecoderInfo</code> * <code>decoder</code> </p>
<p> <code>Sound_AudioInfo</code> <code>desired</code> </p>
<p> <code>Sound_AudioInfo</code> <code>actual</code> </p>
<p> void * <code>buffer</code> </p>
<p> Uint32 <code>buffer_size</code> </p>
<p> <code>Sound_SampleFlags</code> <code>flags</code> </p>
<h2>Detailed Description</h2>
<p>Represents sound data in the process of being decoded. </p>
<p> The <code>Sound_Sample</code> structure is the heart of SDL_sound. This holds information about a source of sound data as it is being decoded. EVERY FIELD IN THIS IS READ-ONLY. Please use the API functions to change them.</p>
<h2>Field Documentation</h2>
<h3><code>Sound_AudioInfo</code> <code>Sound_Sample::actual</code></h3>
<p>Actual audio format of sample.</p>
<h3>void* <code>Sound_Sample::buffer</code></h3>
<p>Decoded sound data lands in here.</p>
<h3>Uint32 <code>Sound_Sample::buffer_size</code></h3>
<p>Current size of (buffer), in bytes (Uint8).</p>
<h3>const <code>Sound_DecoderInfo</code>* <code>Sound_Sample::decoder</code></h3>
<p>Decoder used for this sample.</p>
<h3><code>Sound_AudioInfo</code> <code>Sound_Sample::desired</code></h3>
<p>Desired audio format for conversion.</p>
<h3><code>Sound_SampleFlags</code> <code>Sound_Sample::flags</code></h3>
<p>Flags relating to this sample.</p>
<h3>void* <code>Sound_Sample::opaque</code></h3>
<p>Internal use only. Don&#8217;t touch. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SDL_sound from the source code.</p>
