---
title: "geteltorito(1)"
name: "geteltorito"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geteltorito/"
description: "geteltorito – an El Torito boot image extractor"
---

<h2 class="name">NAME</h2>
<p> geteltorito &#8211; an El Torito boot image extractor </p>
<h2>SYNOPSIS</h2>
<p> <code>geteltorito</code> &lt;<i>image</i>|<i>device</i>&gt; [<code>-o</code> <i>outputfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>geteltorito</code> is a Perl script which extracts the initial/default <code>El Torito</code> boot image from a CD if one exists. It will not extract any of other boot images that are allowed by the El Torito standard. </p>
<p> The boot image file is written to <code>stdout</code> and all other information (e.g., image type and size) is written to <code>stderr</code>. To write the image to a file instead of <code>stdout</code>, specify the output filename using <code>-o</code> <i>filename</i>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1), <code><a href="/docs/linux/man/1-isoinfo/">isoinfo</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> geteltorito was written by Rainer Krienke &lt;krienke [at] uni-koblenz.de&gt;. </p>
<p> This manual page was written by Eduard Bloch &lt;blade [at] debian.org&gt; based on README.geteltorito from geteltorito-0.4 package. </p>
<h2>Index</h2>
