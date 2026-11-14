---
title: "tracker-extract(1)"
name: "tracker-extract"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-extract/"
description: "tracker-extract – Extract metadata from a file."
---

<h2 class="name">NAME</h2>
<p> tracker-extract &#8211; Extract metadata from a file.</p>
<h2>SYNOPSYS</h2>
<p> <code>tracker extract</code> <i>FILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>tracker extract</code> reads the file provided and extracts any metadata it can from this file, then displays the metadata on standard output. </p>
<p> The metadata is displayed as a SPARQL update command, that can be run against a SPARQL endpoint to update its copy of the metadata. </p>
<p> The actual extraction is done by a separate process. This is done to isolate the calling process from any memory leaks or crashes in the libraries Tracker uses to extract metadata. </p>
<p> For more information see the libtracker-extract reference documentation. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, &#8211;verbosity</code>=&lt;<i>LEVEL</i>&gt;</p>
<dd> This sets the log verbosity for the extractor process. </p>
<p> The possible <i>LEVEL</i> options are: </p>
<dl>
<dt>
<dd> &bull; <i>debug</i> &#8211; Show EVERYTHING, from debug messages to errors. </p>
<p> &bull; <i>detailed</i> &#8211; Show enough detail to understand what is happening. </p>
<p> &bull; <i>minimal</i> &#8211; Show an overview of what is going on </p>
<p> &bull; <i>errors</i> &#8211; Show only warnings, criticals, errors or fatal events.</dl>
<dt><code>-o, &#8211;output-format</code>=&lt;<i>FORMAT</i>&gt;</p>
<dd> Choose which format to use to output results. Supported formats are <i>sparql</i>, <i>turtle</i> and <i>json-ld</i>. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Using command line to extract metadata from a file:</p>
<dd>
<p> $ tracker extract /path/to/some/file.mp3 </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_EXTRACTORS_DIR</code></p>
<dd> This is the directory which tracker uses to load the shared libraries from (used for extracting metadata for specific file types). These are needed on each invocation of tracker-store. If unset it will default to the correct place. This is used mainly for testing purposes. The default location is /usr/lib/tracker-1.0/extract-modules/.</p>
<dt><code>TRACKER_EXTRACTOR_RULES_DIR</code></p>
<dd> This is the directory which tracker uses to load the rules files from. The rules files describe extractor modules and their supported MIME types. The default location is /usr/share/tracker/extract-rules/.</p>
<dt><code>TRACKER_USE_CONFIG_FILES</code></p>
<dd> Don&#8217;t use GSettings, instead use a config file similar to how settings were saved in 0.10.x. That is, a file which is much like an .ini file. These are saved to $HOME/.config/tracker/ </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-sparql/">tracker-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker-stats/">tracker-stats</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1).</p>
<dl>
<dt><code>/usr/lib/tracker-1.0/extract-modules/</code></p>
<dd>
<dt><code>/usr/share/tracker/extract-rules/</code></p>
<dd>
</dl>
<h2>Index</h2>
