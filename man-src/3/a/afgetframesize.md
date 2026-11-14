---
title: "afgetframesize(3)"
name: "afgetframesize"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afgetframesize/"
---

afGetFrameSize - calculate the frame size in bytes for an audio track 

<h2>Synopsis</h2><pre>#include &lt;audiofile.h&gt;</pre><pre>float afGetFrameSize (AFfilehandle file, int track, int expand3to4);</pre><h2>Parameters</h2><i>file</i> is a valid AFfilehandle. 

 <i>track</i> is an integer which refers to a specific audio track in the file. At present no supported audio file format allows for more than one audio track within a file, so track should always be AF_DEFAULT_TRACK. 

 <i>expand3to4</i> is a boolean-valued integer indicating whether frame size calculation will treat 24-bit data as having a size of 3 bytes or 4 bytes.
<h2>Description</h2>afGetFrameSize returns the number of bytes in a frame in a given audio track. 

 A sample frame consists of one or more samples. For a monaural track, a sample frame will always contain one sample. For a stereophonic track, a sample frame will always contain two samples, one for the left channel and one for the right channel. 

 A non-zero value of <i>expand3to4</i> should be used when calculating the frame size for storage in memory (since 24-bit audio data is presented in memory as a 4-byte sign-extended integer), while a value of zero should be used for calculating storage on disk where no padding is added. The parameter <i>expand3to4</i> is ignored unless the specified audio track contains 24-bit audio data.
<h2>Author</h2>Michael Pruett &lt;michael [at] 68k.org&gt;
