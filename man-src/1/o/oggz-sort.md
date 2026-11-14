---
title: "oggz-sort(1)"
name: "oggz-sort"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-sort/"
description: "oggz-sort — Sort the pages of an Ogg file in order of presentation time."
---

<h2>NAME</h2>
<p> oggz-sort &#8212; Sort the pages of an Ogg file in order of presentation time.<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-sort</code> [-o <code>filename</code> | &#8211;output <code>filename</code> ] filename </p>
<p> <code>oggz-sort</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-sort</code> sorts an Ogg file, interleaving pages in order of presentation time. It correctly interprets the granulepos timestamps of Ogg CELT, CMML, Dirac, FLAC, Kate, PCM, Speex, Theora and Vorbis bitstreams. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz.<br />
&nbsp;<wbr> </p>
<p> Some encoders produce files with incorrect page ordering; for example, some audio and video pages may occur out of order. Although these files are usually playable, it can be difficult to accurately seek or scrub on them, increasing the likelihood of glitches during playback. Players may also need to use more memory in order to buffer the audio and video data for synchronized playback, which can be a problem when the files are viewed on low-memory devices.<br />
&nbsp;<wbr> </p>
<p> Some older Ogg encoders also produce pages which incorrectly have granulepos timestamps recorded that shouldn&#8217;t be: pages which have no completed packets must have a granulepos of -1. <code>oggz-sort</code> will correct such granulepos during the process of sorting.<br />
&nbsp;<wbr> </p>
<p> The tool <code>oggz-validate</code> can be used to check the relative ordering of packets in a file, and also to detect incorrect granulepos on pages with no completed packets. If either of these errors are reported, or use <code>oggz-sort</code> to fix the problem.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-sort</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Miscellaneous options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.<br />
&nbsp;<wbr></p>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Correct the page ordering in broken.ogv: </p>
<dl>
<dt>
<dd> <tt>oggz sort -o fixed.ogv broken.ogv</tt></dl>
<h2>AUTHOR</h2>
<p> Conrad Parker January 25, 2008;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Annodex Association<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-validate/">oggz-validate</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-merge/">oggz-merge</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-diff/">oggz-diff</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> </p>
<h2>Index</h2>
