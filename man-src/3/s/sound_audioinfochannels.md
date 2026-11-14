---
title: "sound_audioinfochannels(3)"
name: "sound_audioinfochannels"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sound_audioinfochannels/"
description: "Sound_AudioInfo – Information about an existing sample’s format."
---

<p>Sound_AudioInfo &#8211; Information about an existing sample&#8217;s format. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/SDL_sound.h">SDL_sound.h</a>&gt; </p>
<h3>Data Fields</h3>
<p>Uint16 <code>format</code> </p>
<p> Uint8 <code>channels</code> </p>
<p> Uint32 <code>rate</code> </p>
<h2>Detailed Description</h2>
<p>Information about an existing sample&#8217;s format. </p>
<p> These are the basics of a decoded sample&#8217;s data structure: data format (see AUDIO_U8 and friends in SDL_audio.h), number of channels, and sample rate. If you need more explanation than that, you should stop developing sound code right now. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>Sound_SampleNew </p>
<p> Sound_SampleNewFromFile</dl>
<h2>Field Documentation</h2>
<h3>Uint8 <code>Sound_AudioInfo::channels</code></h3>
<p>Number of sound channels. 1 == mono, 2 == stereo.</p>
<h3>Uint16 <code>Sound_AudioInfo::format</code></h3>
<p>Equivalent of SDL_AudioSpec.format.</p>
<h3>Uint32 <code>Sound_AudioInfo::rate</code></h3>
<p>Sample rate; frequency of sample points per second. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SDL_sound from the source code.</p>
