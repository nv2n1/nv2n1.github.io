---
title: "katedj(1)"
name: "katedj"
section: "1"
letter: "k"
url: "/docs/linux/man/1-katedj/"
description: "KateDJ – edits and remixes Kate streams in Ogg"
---

<p>KateDJ &#8211; edits and remixes Kate streams in Ogg</p>
<h2>Synopsis</h2>
<p><code>KateDJ</code> <code>[-hV]</code> </p>
<h2>Description</h2>
<p><code>KateDJ</code> allows extracting Kate tracks embedded in an Ogg stream, editing them, and rebuilding the Ogg stream after the Kate tracks are modified. </p>
<p> <code>KateDJ</code> is a simple GUI program, so usage is UI driven, rather than command line driven. </p>
<p> This is a walkthrough of the usual program flow: </p>
<p> Select <code>&#8216;Load Ogg stream&#8217;</code> to select the Ogg file you want to remix. </p>
<p> Select <code>&#8216;Demux file&#8217;</code> to extract Kate streams from this file to a temporary directory. Depending on the size of the Ogg file, that step may take a while. A message will then tell you where the temporary files have been placed. All Kate streams will be decoded to a text description and placed in this temporary directory, and a list of them, along with their serial number, language, and category, will be displayed in a list. </p>
<p> Those files may then be edited at will, either in the embedded editor by double clicking on the stream in the supplied list, or with your favorite text editor. Any modification may be done, including removing some of those files altogether, or even adding some. However, in order to be recognized, any new files <code>must</code> be named according to the same naming convention as the existing ones. </p>
<p> Once the desired modifications are done, select <code>&#8216;Remux file from parts&#8217;</code> to attempt to recreate the Ogg stream. If any error occurs (eg, syntax error in the Kate files), a message will inform you. Once the errors are fixed, select <code>&#8216;Remux file from parts&#8217;</code> again, until the operation succeeds. </p>
<p> The embedded editor can test a modified stream, so it more convenient for quick modifications, while your editor of choice may be more powerful for complex modification. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Show command line help.</p>
<dt><code>-V</code></p>
<dd>Show version information. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-katedec/">katedec</a></code>(1), <code><a href="/docs/linux/man/1-kateenc/">kateenc</a></code>(1), <code><a href="/docs/linux/man/1-katalyzer/">katalyzer</a></code>(1)</p>
