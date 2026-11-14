---
title: "afsetvirtualpcmmapping(3)"
name: "afsetvirtualpcmmapping"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afsetvirtualpcmmapping/"
---

afSetVirtualByteOrder, afSetVirtualChannels, afSetVirtualPCMMapping, afSetVirtualSampleFormat - set the virtual data format for a track in an audio file 

<h2>Synopsis</h2><pre>#include &lt;audiofile.h&gt;</pre><pre>int afSetVirtualByteOrder (AFfilehandle file, int track, int byteOrder);</pre><pre>int afSetVirtualChannels (AFfilehandle file, int track, int channels);</pre><pre>int afSetVirtualSampleFormat (AFfilehandle file, int track,
 int sampleFormat, int sampleWidth);</pre><pre>int afSetVirtualPCMMapping (AFfilehandle file, int track,
 double slope, double intercept, double minclip, double maxclip);</pre><h2>Parameters</h2><dl COMPACT><dd>&bull; 

 <i>file</i> is an AFfilehandle which refers to an open audio file and is usually created by afOpenFile.</dl><dl COMPACT><dd>&bull; 

 <i>track</i> is an integer which identifies a particular track in an open audio file. The only valid track is AF_DEFAULT_TRACK for all currently supported file formats.</dl><dl COMPACT><dd>&bull; 

 <i>sampleFormat</i> is an integer which denotes a virtual sample format. Valid values are AF_SAMPFMT_TWOSCOMP, AF_SAMPFMT_UNSIGNED, AF_SAMPFMT_FLOAT, and AF_SAMPFMT_DOUBLE.</dl><dl COMPACT><dd>&bull; 

 <i>sampleWidth</i> is a positive integer which specifies the number of bits in a sample.</dl><dl COMPACT><dd>&bull; 

 <i>channels</i> is a positive integer which specifies the number of interleaved audio channels in the given audio track.</dl><dl COMPACT><dd>&bull; 

 <i>byteOrder</i> is an integer which specifies the virtual byte order of samples in the given audio track. <i>byteOrder</i> can be either AF_BYTEORDER_BIGENDIAN or AF_BYTEORDER_LITTLEENDIAN.</dl><dl COMPACT><dd>&bull; 

 <i>slope</i> and <i>intercept</i> are double-precision floating point values which indicate the audio data sample slope and zero-crossing value, respectively, for the given sample format.</dl><dl COMPACT><dd>&bull; 

 <i>minclip</i> and <i>maxclip</i> are double-precision floating point values which indicates the minimum or maximum sample values to be returned. Any values less than <i>minclip</i> will be set to <i>minclip</i>, and any values greater than <i>maxclip</i> will be set to <i>maxclip</i>.</dl><h2>Return Value</h2>These functions return 0 for success and -1 for failure.
<h2>Author</h2>Michael Pruett &lt;michael [at] 68k.org&gt;
