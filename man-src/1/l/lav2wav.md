---
title: "lav2wav(1)"
name: "lav2wav"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lav2wav/"
description: "lav2wav – Extract the audio out of MJPEG container files to stdout"
---

<h2 class="name">NAME</h2>
<p> lav2wav &#8211; Extract the audio out of MJPEG container files to stdout</p>
<h2>SYNOPSIS</h2>
<p> <code>lav2wav</code> [<code>-s</code> <i>num</i>] [<code>-c</code> <i>num</i>] [<code>-v</code> <i>num</i>] [<code>-I</code>] [<code>-R</code>] [<code>-r</code> <i>samplerate,</i> <i>bitesize,</i> <i>channels</i>] <i>lavfile1 </i>[<i>lavfile2 </i>&#8230;<i> lavfileN</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>lav2wav</code> can be used to extract the audio to stdout. This output goes to stdout and can be saved as a wav file or piped to another sound processing tool that is able to handle the wav format. This can be mp2enc and toolame for mpeg layer 2 audio, or for example lame for mpeg layer 3 audio. </p>
<p> The input files may be any combination of AVI (.avi), Quicktime (.qt) or editlist files so long as they are all lavtools- readable (e.g. MJPEG-encoded AVI/Quicktime or DV type 2 AVI). </p>
<h2>OPTIONS</h2>
<p> <code>lav2wav</code> accepts the following options: </p>
<dl>
<dt><code>-s</code><i> num</i></p>
<dd> Start extracting at video frame (num)</p>
<dt><code>-c</code><i> num</i></p>
<dd> Extract (num) frames of audio</p>
<dt><code>-v</code><i> num</i></p>
<dd> Verbosity level (0, 1 or 2)</p>
<dt><code>-I</code></p>
<dd> Ignore unsupported bitrates/bits per sample</p>
<dt><code>-R</code></p>
<dd> If the file does not contain any sound. lav2wav will create silence with 44100kHz Sampelrate, 16 Bit audio bitsize and 2 Chanels</p>
<dt><code>-r</code><i> sr,bs,ch</i></p>
<dd> If the file does not contain any sound lav2wav will generate silence with the values you supply the samplerate (sr), audio-bitsize (bs) and channel (ch). </p>
</dl>
<h2>BUGS</h2>
<p> The &quot;WAV&quot; file format (technically: RIFF) is really very much less than ideal for a tool intended to be used in pipelines as lav2wav is. The problem is that the header includes a field specifying the length of the file. This can&#8217;t be filled in except by seeking back to the begining and over-writing. If the output is unseekable (e.g. pipe) lav2wav simply writes a large length into the header and leaves it at that. Most tools like <a href="/docs/linux/man/1-sox/">sox</a>(1) or <a href="/docs/linux/man/1-mp2enc/">mp2enc</a>(1) either ignore the length field anyway or only give a warning.<br />
 The audio length is inacurate calculated when lav2wav generates silence. This happens only if you have NTSC framerate and than it creates for every hour of video 1.1498sec too less of silence. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Bernhard Praschinger.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mp2enc/">mp2enc</a></code>(1), <code><a href="/docs/linux/man/1-sox/">sox</a>(1)</code> </p>
<h2>Index</h2>
