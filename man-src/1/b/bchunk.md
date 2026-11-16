---
title: "bchunk(1)"
name: "bchunk"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bchunk/"
description: "bchunk – CD image format conversion from bin/cue to iso/cdr"
---

<h2>NAME</h2>
<p> bchunk &#8211; CD image format conversion from bin/cue to iso/cdr</p>
<h2>SYNOPSIS</h2>
<p> <code>bchunk [-v] [-p] [-r] [-w] [-s] &lt;image.bin&gt; &lt;image.cue&gt; &lt;basename&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>bchunk </code> converts a CD image in a &quot;.bin / .cue&quot; format (sometimes &quot;.raw / .cue&quot;) to a set of .iso and .cdr tracks. </p>
<p> The bin/cue format is used by some non-Unix cd-writing software, but is not supported on most other cd-writing programs. </p>
<p> image.bin is the raw cd image file. image.cue is the track index file containing track types and offsets. basename is used for the beginning part of the created track files. </p>
<p> The produced .iso track contains an ISO file system, which can be mounted through a loop device on Linux systems, or written on a CD-R using cdrecord. The .cdr tracks are in the native CD audio format. They can be either written on a CD-R using cdrecord -audio, or converted to WAV (or any other sound format for that matter) using sox. </p>
<p> It is advisable to edit the .cue file to either MODE2/2352/2048 or MODE2/2352/2324 depending on whether an ISO filesystem or a VCD is desired, respectively. The format itself does not contain this feature and in an ambiguous case it can only guess.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> Makes binchunker print some more unnecessary messages, which should not be of interest for anyone.</dd>
<dt><code>-w</code></dt>
<dd> Makes binchunker write audio tracks in WAV format.</dd>
<dt><code>-s</code></dt>
<dd> Makes binchunker swap byte order in the samples of audio tracks.</dd>
<dt><code>-p</code></dt>
<dd> Makes binchunker go into PSX mode and truncate MODE2/2352 tracks to 2336 bytes at offset 0 instead of normal 2048 bytes at offset 24.</dd>
<dt><code>-r</code></dt>
<dd> Makes binchunker output MODE2/2352 tracks in raw format, from offset 0 for 2352 bytes. Good for MPEG/VCD.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>image.bin</code></dt>
<dd> Raw CD image file</dd>
<dt><code>image.cue</code></dt>
<dd> TOC (Track index, Table Of Contents) file</dd>
<dt><code>*.iso</code></dt>
<dd> Tracks in ISO9660 CD filesystem format. Can be either written on a CD-R using cdrecord, or mounted (on Linux platforms at least) through a loop device (&#8216;mount track.iso /mnt/cdrom -o loop=/dev/loop0,blocksize=1024&#8217;).</dd>
<dt><code>*.cdr</code></dt>
<dd> Audio tracks in native CD audio format. They can be either written on a CD-R using &#8216;cdrecord -audio&#8217;, or converted to WAV (or any other sound format for that matter) using sox (&#8216;sox track.cdr track.wav&#8217;).</dd>
<dt><code>*.wav</code></dt>
<dd> Audio tracks in WAV format.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>cdrecord</code>(1), <code>mkisofs</code>(8), <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1), <code><a href="/docs/linux/man/1-cdrdao/">cdrdao</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Heikki Hannikainen &lt;hessu [at] hes.iki.fi&gt;<br />
 Bob Marietta &lt;marietrg [at] SLU.EDU&gt;<br />
 Colas Nahaboo &lt;Colas [at] Nahaboo.com&gt;<br />
 Godmar Back &lt;gback [at] cs.utah.edu&gt;<br />
 Matthew Green &lt;mrg [at] eterna.com.au&gt; </p>
<h2>Index</h2>
