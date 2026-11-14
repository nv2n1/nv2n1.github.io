---
title: "sndfile-interleave(1)"
name: "sndfile-interleave"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sndfile-interleave/"
description: "sndfile-interleave – convert multiple single channel files into a multi-channel file sndfile-deinterleave – split a multi-channel into multiple single channel files"
---

<h2>NAME</h2>
<p> sndfile-interleave &#8211; convert multiple single channel files into a multi-channel file<br />
 sndfile-deinterleave &#8211; split a multi-channel into multiple single channel files</p>
<h2>SYNOPSIS</h2>
<p> <code>sndfile-interleave</code> &lt;input 1&gt; &lt;input 2&gt; &#8230; -o &lt;output file&gt;<br />
 <code>sndfile-deinterleave</code> filename </p>
<h2>DESCRIPTION</h2>
<p> sndfile-interleave and sndfile-deinterleave use libsndfile (<a rel="nofollow" href="http://www.mega-nerd.com/libsndfile/)">http://www.mega-nerd.com/libsndfile/)</a> to convert back and forth between multiple single channel files and a single multi-channel sound file. </p>
<p> Run &quot;sndfile-interleave &#8211;help&quot; or &quot;sndfile-deinterleave &#8211;help&quot; for more information </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Erik de Castro Lopo &lt;erikd [at] mega-nerd.com&gt;. </p>
<h2>Index</h2>
