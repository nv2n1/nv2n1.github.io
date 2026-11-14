---
title: "sndfile-play(1)"
name: "sndfile-play"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sndfile-play/"
description: "sndfile-play – play a sound file"
---

<h2>NAME</h2>
<p> sndfile-play &#8211; play a sound file</p>
<h2>SYNOPSIS</h2>
<p> <code>sndfile-play</code> file</p>
<h2>DESCRIPTION</h2>
<p> sndfile-play plays the specified sound file using : </p>
<pre>
ALSA on Linux
/dev/dsp on systems supporting OSS (including Linux)
/dev/audio on Sun Solaris
CoreAudio on Apple MacOSX
waveOut on Microsoft Win32
</pre>
<p> sndfile-play uses libsndfile (<a rel="nofollow" href="http://www.mega-nerd.com/libsndfile/)">http://www.mega-nerd.com/libsndfile/)</a> to read the file.</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Joshua Haberman &lt;joshua [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). Further additions have been made by Erik de Castro Lopo &lt;erikd [at] mega-nerd.com&gt;. </p>
<h2>Index</h2>
