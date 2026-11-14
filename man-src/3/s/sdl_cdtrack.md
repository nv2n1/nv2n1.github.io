---
title: "sdl_cdtrack(3)"
name: "sdl_cdtrack"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_cdtrack/"
description: "SDL_CDtrack – CD Track Information Structure"
---

<p>SDL_CDtrack &#8211; CD Track Information Structure</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 id;
 Uint8 type;
 Uint32 length;
 Uint32 offset;
} SDL_CDtrack;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>id</code></p>
<dd>Track number (0-99)</p>
<dt><code>type</code></p>
<dd><code>SDL_AUDIO_TRACK</code> or <code>SDL_DATA_TRACK</code></p>
<dt><code>length</code></p>
<dd>Length, in frames, of this track</p>
<dt><code>offset</code></p>
<dd>Frame offset to the beginning of this track</dl>
<h2>Description</h2>
<p><code>SDL_CDtrack</code> stores data on each track on a CD, its fields should be pretty self explainatory. It is a member a the <i></i><code>SDL_CD</code> structure. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> Frames can be converted to standard timings. There are CD_FPS</code> frames per second, so <code>SDL_CDtrack</code>.<code>length</code>/<code>CD_FPS</code>=length_in_seconds.</dl>
<h2>See Also</h2>
<p><i></i><code>SDL_CD</code></p>
