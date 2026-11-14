---
title: "sound_decoderinfourl(3)"
name: "sound_decoderinfourl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sound_decoderinfourl/"
description: "Sound_DecoderInfo – Information about available soudn decoders."
---

<p>Sound_DecoderInfo &#8211; Information about available soudn decoders. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/SDL_sound.h">SDL_sound.h</a>&gt; </p>
<h3>Data Fields</h3>
<p>const char ** <code>extensions</code> </p>
<p> const char * <code>description</code> </p>
<p> const char * <code>author</code> </p>
<p> const char * <code>url</code> </p>
<h2>Detailed Description</h2>
<p>Information about available soudn decoders. </p>
<p> Each decoder sets up one of these structs, which can be retrieved via the <code>Sound_AvailableDecoders()</code> function. EVERY FIELD IN THIS IS READ-ONLY. </p>
<p> The extensions field is a NULL-terminated list of ASCIZ strings. You should read it like this: </p>
<pre> const char **ext;
 for (ext = info-&gt;extensions; *ext != NULL; ext++) {
 printf(' File extension '%s', *ext);
 }</pre>
<p><code>See also:</code></p>
<dl COMPACT>
<dd><code>Sound_AvailableDecoders</code></dl>
<h2>Field Documentation</h2>
<h3>const char* <code>Sound_DecoderInfo::author</code></h3>
<h3>const char* <code>Sound_DecoderInfo::description</code></h3>
<p>Human readable description of decoder.</p>
<h3>const char** <code>Sound_DecoderInfo::extensions</code></h3>
<p>File extensions, list ends with NULL.</p>
<h3>const char* <code>Sound_DecoderInfo::url</code></h3>
<p>URL specific to this decoder. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SDL_sound from the source code.</p>
