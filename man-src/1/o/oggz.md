---
title: "oggz(1)"
name: "oggz"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz/"
description: "oggz — inspect and manipulate Ogg multimedia files"
---

<h2>NAME</h2>
<p> oggz &#8212; inspect and manipulate Ogg multimedia files<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz</code>help <code>command</code> command <code>args</code></p>
<h2>Description</h2>
<p> <code>oggz</code> is a suite of tools for manipulating Ogg multimedia files. It supports multiplexed files conformant with RFC3533. Oggz can parse headers for CELT, CMML, Dirac, FLAC, Kate, PCM, Speex, Theora and Vorbis, and can read and write Ogg Skeleton logical bitstreams.<br />
&nbsp;<wbr></p>
<h2>Commands</h2>
<dl>
<dt> &bull;</p>
<dd> <code>help</code>Display help for a specific subcommand (eg. &quot;oggz help chop&quot;)</dl>
<h3>Reporting</h3>
<dl>
<dt> &bull;</p>
<dd> <code>diff</code>Hexdump the packets of two Ogg files and output differences.</p>
<dt> &bull;</p>
<dd> <code>dump</code>Hexdump packets of an Ogg file, or revert an Ogg file from such a hexdump.</p>
<dt> &bull;</p>
<dd> <code>info</code>Display information about one or more Ogg files and their bitstreams.</p>
<dt> &bull;</p>
<dd> <code>scan</code>Scan an Ogg file and output characteristic landmarks.</p>
<dt> &bull;</p>
<dd> <code>validate</code>Validate the Ogg framing of one or more files.</dl>
<h3>Extraction</h3>
<dl>
<dt> &bull;</p>
<dd> <code>rip</code>Extract one or more logical bitstreams from an Ogg file.</dl>
<h3>Editing</h3>
<dl>
<dt> &bull;</p>
<dd> <code>chop</code>Extract the part of an Ogg file between given start and/or end times.</p>
<dt> &bull;</p>
<dd> <code>comment</code>List or edit comments in an Ogg file. <code>merge</code>Merge Ogg files together, interleaving pages in order of presentation time.<code>sort</code>Sort the pages of an Ogg file in order of presentation time.</dl>
<h2>Options</h2>
<p> <code>oggz</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Conrad Parker July 9, 2008;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Annodex Association<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ogginfo/">ogginfo</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> </p>
<h2>Index</h2>
