---
title: "oggz-validate(1)"
name: "oggz-validate"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-validate/"
description: "oggz-validate — Validate the Ogg framing of one or more files"
---

<h2>NAME</h2>
<p> oggz-validate &#8212; Validate the Ogg framing of one or more files<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-validate </code> [-M <code>num</code> | &#8211;max-errors <code>num</code> ] [-p | &#8211;prefix ] [-s | &#8211;suffix ] [-P | &#8211;partial ] filename &#8230; </p>
<p> <code>oggz-validate</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-validate</code> validates the Ogg framing of one or more Ogg files. </p>
<p> <code>oggz-validate</code> detects the following errors in Ogg framing:<br />
&nbsp;<wbr></p>
<dl>
<dt> &bull;</p>
<dd> File contains no Ogg packets</p>
<dt> &bull;</p>
<dd> Packets out of order</p>
<dt> &bull;</p>
<dd> Packet belongs to unknown serialno</p>
<dt> &bull;</p>
<dd> Granulepos decreasing within track</p>
<dt> &bull;</p>
<dd> Multiple bos pages</p>
<dt> &bull;</p>
<dd> Multiple eos pages</p>
<dt> &bull;</p>
<dd> eos marked but no bos</p>
<dt> &bull;</p>
<dd> Missing eos packets</p>
<dt> &bull;</p>
<dd> eos marked on page with no completed packets</p>
<dt> &bull;</p>
<dd> Granulepos on page with no completed packets</p>
<dt> &bull;</p>
<dd> Theora video bos page after audio bos page</p>
<dt> &bull;</p>
<dd> Terminal header page has non-zero granulepos</p>
<dt> &bull;</p>
<dd> Terminal header page contains non-header packet</p>
<dt> &bull;</p>
<dd> Terminal header page contains non-header segment</dl>
<p> <code>oggz-validate</code> exits with status 0 if all files are valid Ogg files, and with status 1 if one or more errors are found.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-validate</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Error reporting options</h3>
<dl>
<dt>-M <code>num</code>, &#8211;max-errors <code>num</code></p>
<dd> Exit after the specified number of errors. A value of 0 specifies no maximum.</p>
<dt>-p, &#8211;prefix</p>
<dd> Treat input as the prefix of a stream; suppress warnings about missing end-of-stream markers</p>
<dt>-s, &#8211;suffix</p>
<dd> Treat input as the suffix of a stream; suppress warnings about missing beginning-of-stream markers on the first chain</p>
<dt>-P, &#8211;partial</p>
<dd> Treat input as a the middle portion of a stream. Equivalent to both &#8211;prefix and &#8211;suffix</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Conrad Parker April 3, 2005;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-sort/">oggz-sort</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-info/">oggz-info</a></code><code>(1)</code> </p>
<h2>Index</h2>
