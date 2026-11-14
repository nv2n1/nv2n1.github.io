---
title: "oggz-chop(1)"
name: "oggz-chop"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-chop/"
description: "oggz-chop — Extract the part of an Ogg file between given start and/or end times."
---

<h2>NAME</h2>
<p> oggz-chop &#8212; Extract the part of an Ogg file between given start and/or end times.<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-chop</code> [-o <code>filename</code> | &#8211;output <code>filename</code> ] [-s <code>start_time</code> | &#8211;start <code>start_time</code> ] [-e <code>end_time</code> | &#8211;end <code>end_time</code> ] [-k | &#8211;no-skeleton ] filename </p>
<p> <code>oggz-chop</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-chop</code> chops a section of an Ogg file. It correctly interprets the granulepos timestamps of Ogg CELT, CMML, Dirac, FLAC, Kate, PCM, Speex, Theora and Vorbis bitstreams. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz.<br />
&nbsp;<wbr> </p>
<p> The output file contains copies of the headers of the input file, and all the codec data required to correctly decode the content between the start and end times specified on the commandline. For codecs with data dependencies like video keyframes, the keyframe prior to the starting time will be included in the output.<br />
&nbsp;<wbr> </p>
<p> Note that <code>oggz-chop</code> operates by copying pages of Ogg data; it does not strip partial packets from the first or last data page included in the output. It does however ensure to set the end of stream flag on the last page of each logical bitstream.<br />
&nbsp;<wbr> </p>
<p> Skeleton handling: By default, the output will contain a Skeleton track specifying the start of the chop as presentation time.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-chop</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Output options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.<br />
&nbsp;<wbr></p>
<dt>-s <code>start_time</code>, &#8211;start <code>start_time</code></p>
<dd> Specify the start time of the chopped section to output.<br />
&nbsp;<wbr></p>
<dt>-e <code>end_time</code>, &#8211;end <code>end_time</code></p>
<dd> Specify the end time of the chopped section to output.<br />
&nbsp;<wbr></p>
<dt>-k , &#8211;no-skeleton</p>
<dd> Do NOT include a Skeleton bitstream in the output.<br />
&nbsp;<wbr></p>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Extract the first minute of file.ogx: </p>
<dl>
<dt>
<dd> <tt>oggz chop -e 1:00 file.ogx</tt></dl>
<p> Extract from the second to the fifth minute of file.ogx: </p>
<dl>
<dt>
<dd> <tt>oggz chop -s 2:00 -e 5:00 -o output.ogx file.ogx</tt></dl>
<p> Extract, specifying SMPTE-25 frame offsets: </p>
<dl>
<dt>
<dd> <tt>oggz chop -s smpte-25:00:02:03::12 -e smpte-25:00:05:02::04 -o output.ogv file.ogv</tt></dl>
<h2>Server configuration</h2>
<p> The following configuration for Apache httpd will enable oggz-chop. As with most Apache directives, this may of course be restricted to particular Directories or Locations: </p>
<p> ScriptAlias /oggz-chop /usr/bin/oggz-chop<br />
&nbsp;<wbr> </p>
<p> Action application/ogg /oggz-chop<br />
&nbsp;<wbr></p>
<h3>HTTP/1.1 Cacheability</h3>
<p> oggz-chop generates Last-Modified HTTP headers, and responds correctly to If-Modified-Since conditional GET requests.<br />
&nbsp;<wbr></p>
<h2>AUTHOR</h2>
<p> Conrad Parker February 25, 2008;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Annodex Association<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-validate/">oggz-validate</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-merge/">oggz-merge</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> </p>
<h2>Index</h2>
