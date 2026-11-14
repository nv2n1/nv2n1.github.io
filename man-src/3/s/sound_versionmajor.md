---
title: "sound_versionmajor(3)"
name: "sound_versionmajor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sound_versionmajor/"
description: "Sound_Version – Information the version of SDL_sound in use."
---

<p>Sound_Version &#8211; Information the version of SDL_sound in use. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/SDL_sound.h">SDL_sound.h</a>&gt; </p>
<h3>Data Fields</h3>
<p>int <code>major</code> </p>
<p> int <code>minor</code> </p>
<p> int <code>patch</code> </p>
<h2>Detailed Description</h2>
<p>Information the version of SDL_sound in use. </p>
<p> Represents the library&#8217;s version as three levels: major revision (increments with massive changes, additions, and enhancements), minor revision (increments with backwards-compatible changes to the major revision), and patchlevel (increments with fixes to the minor revision). </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>SOUND_VERSION</code> </p>
<p> <code>Sound_GetLinkedVersion</code></dl>
<h2>Field Documentation</h2>
<h3>int <code>Sound_Version::major</code></h3>
<p>major revision</p>
<h3>int <code>Sound_Version::minor</code></h3>
<p>minor revision</p>
<h3>int <code>Sound_Version::patch</code></h3>
<p>patchlevel </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SDL_sound from the source code.</p>
