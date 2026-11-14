---
title: "toc2cue(1)"
name: "toc2cue"
section: "1"
letter: "t"
url: "/docs/linux/man/1-toc2cue/"
description: "toc2cue – converts a TOC files of"
---

<h2 class="name">NAME</h2>
<p> toc2cue &#8211; converts a TOC files of <i></p>
<p> <a href="/docs/linux/man/1-cdrdao/">cdrdao</a>(1)</i> into a .cue file </p>
<h2>SYNOPSIS</h2>
<p> <code>toc2cue</code> <code>[</code>-v <i>verbosity_level</i><code>]</code> <i>input_toc_file output_cue_file</i> </p>
<p> <code>toc2cue</code> <code>[</code>-V<code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>toc2cue</code> converts a TOC file of <i><a href="/docs/linux/man/1-cdrdao/">cdrdao</a>(1)</i> into a .cue file. </p>
<p> Please note that the resulting cue file is only valid if the toc-file was created with <i><a href="/docs/linux/man/1-cdrdao/">cdrdao</a>(1)</i> using the commands &#8216;read-toc&#8217; or &#8216;read-cd&#8217;. For manually created or edited toc-files the cue file may not be correct. This program just checks for the most obvious toc-file features that cannot be converted to a cue file. Furthermore, if the toc-file contains audio tracks the byte order of the image file will be wrong. This will result in static noise when the cue file is used for recording (even with <i><a href="/docs/linux/man/1-cdrdao/">cdrdao</a>(1)</i> itself). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v </code><i>verbosity_level</i></p>
<dd> Sets the verbosity level to use, can be a integer between 1 and 3. By default, only fatal errors are displayed. A verbosity level of 1 shows warnings, 2 warnings and errors, 3 warnings, errors and internal errors.</p>
<dt><code>-V</code></p>
<dd> Prints the version of toc2cue. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-cdrdao/">cdrdao</a>(1)</i> </p>
<h2>AUTHOR</h2>
<p> <code>toc2cue</code> was written by Andreas Mueller &lt;andreas [at] daneb.de&gt; and is part of <i><a href="/docs/linux/man/1-cdrdao/">cdrdao</a>(1).</i> </p>
<p> This manual page was written by Francois Wendling &lt;frwendling [at] free.fr&gt; and revised by Daniel Baumann &lt;daniel [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
