---
title: "tracker3-extract(1)"
name: "tracker3-extract"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-extract/"
description: "tracker3-extract – Extract metadata from a file."
---

<h2 class="name">NAME</h2>
<p> tracker3-extract &#8211; Extract metadata from a file. </p>
<h2>SYNOPSYS</h2>
<p> <code>tracker3 extract</code> <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> <code>tracker3 extract</code> reads the file provided and extracts any metadata it can from this file, then displays the metadata on standard output. </p>
<p> The metadata is displayed as a SPARQL update command, that can be run against a SPARQL endpoint to update its copy of the metadata. </p>
<p> The actual extraction is done by a separate process. This is done to isolate the calling process from any memory leaks or crashes in the libraries Tracker uses to extract metadata. </p>
<p> For more information see the libtracker-extract reference documentation.</p>
<h2>OPTIONS</h2>
<p> <code>-o, &#8211;output-format=&lt;</code><i>FORMAT</i><code>&gt;</code></p>
<dl>
<dt>
<dd> Choose which format to use to output results. Supported formats are <i>sparql</i>, <i>turtle</i> and <i>json-ld</i>.</dl>
<h2>EXAMPLES</h2>
<p> Using command line to extract metadata from a file</p>
<dl>
<dt>
<dd> $ tracker3 extract /path/to/some/file.mp3</dl>
<h2>ENVIRONMENT</h2>
<p> <code>G_MESSAGES_DEBUG</code></p>
<dl>
<dt>
<dd> Controls verbose log output from GLib-based code. Use G_MESSAGES_DEBUG=Tracker to see only Tracker-related logs, or G_MESSAGES_DEBUG=all to see everything.</dl>
<p> <code>TRACKER_DEBUG</code></p>
<dl>
<dt>
<dd> Enables more specialized debug output. Pass a comma-separated list of one or more keywords: </p>
<p> config</p>
<dl>
<dt>
<dd> extractor configuration</dl>
<p> statistics</p>
<dl>
<dt>
<dd> show statistics about how many files were processed</dl>
</dl>
<p> status</p>
<dl>
<dt>
<dd> log the status messages that are published over D-Bus</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-status/">tracker3-status</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-info/">tracker3-info</a></code>(1). </p>
<dl>
<dt>
<dd> &bull; <code>/usr/lib/tracker-1.0/extract-modules/</code></dl>
<dl>
<dt>
<dd> &bull; <code>/usr/share/tracker/extract-rules/</code></dl>
<h2>Index</h2>
