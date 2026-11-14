---
title: "jigdo-lite(1)"
name: "jigdo-lite"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jigdo-lite/"
description: "jigdo-lite – Download jigdo files using wget"
---

<h2 class="name">NAME</h2>
<p> jigdo-lite &#8211; Download jigdo files using wget </p>
<h2>SYNOPSIS</h2>
<p> <code>jigdo-lite</code> [ <code>URL</code> ] </p>
<h2>DESCRIPTION</h2>
<p> See <code><a href="/docs/linux/man/1-jigdo-file/">jigdo-file</a></code>(1) for an introduction to Jigsaw Download. </p>
<p> Given the URL of a `<i>.jigdo</i>&#8216; file, <code>jigdo-lite</code> downloads the large file (e.g. a CD image) that has been made available through that URL. <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) is used to download the necessary pieces of administrative data (contained in the `<i>.jigdo</i>&#8216; file and a corresponding `<i>.template</i>&#8216; file) as well as the many pieces that the large file is made from. The <code><a href="/docs/linux/man/1-jigdo-file/">jigdo-file</a></code>(1) utility is used to reconstruct the large file from the pieces. </p>
<p> `<i>.jigdo</i>&#8216; files that contain references to Debian mirrors are treated specially: When such a file is recognized, you are asked to select one mirror out of a list of all Debian mirrors. </p>
<p> If <code>URL</code> is not given on the command line, the script prompts for a location to download the `<i>.jigdo</i>&#8216; file from. The following command line options are recognized:</p>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Output short summary of command syntax.</p>
<dt><code>-v &#8211;version</code></p>
<dd> Output version number.</p>
<dt><code>&#8211;scan </code><i>FILES</i></p>
<dd> Do not ask for &quot;Files to scan&quot;, use this path.</p>
<dt><code>&#8211;noask</code></p>
<dd> Do not ask any questions, instead behave as if the user had pressed Return at all prompts. This can be useful when running <code>jigdo-lite</code> from cron jobs or in other non-interactive environments.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jigdo-file/">jigdo-file</a></code>(1), <code><a href="/docs/linux/man/1-jigdo-mirror/">jigdo-mirror</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) (or `<code>info wget</code>&#8216;) </p>
<p> CD images for Debian Linux can be downloaded with jigdo &lt;URL:<a rel="nofollow" href="http://www.debian.org/CD/jigdo-cd/">http://www.debian.org/CD/jigdo-cd/</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Jigsaw Download &lt;URL:<a rel="nofollow" href="http://atterer.net/jigdo/">http://atterer.net/jigdo/</a>&gt; was written by Richard Atterer &lt;jigdo atterer.net&gt;, to make downloading of CD ROM images for the Debian Linux distribution more convenient. </p>
<h2>Index</h2>
