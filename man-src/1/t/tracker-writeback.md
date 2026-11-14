---
title: "tracker-writeback(1)"
name: "tracker-writeback"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-writeback/"
description: "tracker-writeback – Used to write metadata set in Tracker back to physical files."
---

<h2 class="name">NAME</h2>
<p> tracker-writeback &#8211; Used to write metadata set in Tracker back to physical files.</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker-writeback</code> [<i>OPTION</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>tracker-writeback</code> is not supposed to be run by the user since it is started by its .desktop file when the user logs in. It can also be started manually of course for debugging purposes. You can not run more than one instance of this at the same time. </p>
<p> <code>tracker-writeback</code> writes metadata from the Tracker database back into files only. Currently support is limited to XMP metadata (which covers PNG, JPEG, TIFF, MP4 and 3GPP formats), play lists (which covers MPEGURL, SCPLS and IRIVER formats) and taglib supported mime types (which covers MP3, MP4, OGG, WAV, FLAC and some Windows media formats). </p>
<p> Data is only written back if write-back is enabled in the tracker-miner-fs configuration. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Returns the version of this binary.</p>
<dt><code>-v, &#8211;verbosity={0|1|2|3}</code></p>
<dd> Sets the logging level, 0=errors, 1=minimal, 2=detailed, 3=debug.</p>
<dt><code>-d, &#8211;disable-shutdown</code></p>
<dd> Disable shutting down after 30 seconds of inactivity. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-miner-fs/">tracker-miner-fs</a></code>(1). <code><a href="/docs/linux/man/1-tracker-extract/">tracker-extract</a></code>(1). </p>
<h2>Index</h2>
