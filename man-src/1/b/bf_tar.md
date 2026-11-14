---
title: "bf_tar(1)"
name: "bf_tar"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bf_tar/"
description: "bf_tar – shell script to write a tar file of a bogofilter directory to stdout"
---

<h2 class="name">NAME</h2>
<p> bf_tar &#8211; shell script to write a tar file of a bogofilter directory to stdout </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bf_tar</code> [-r] [-R] <i>bogofilter_directory</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>bf_tar</code></p>
<dd>bundles a bogofilter working directory in tar format and copies it to standard output (your console, or where you redirect it, see EXAMPLES below).</p>
<h2>OPTIONS</h2>
<p> The <code>-r</code> option causes <code>bf_tar</code> to remove inactive log files after the archive has been written successfully. The default is to leave log files. </p>
<p> The <code>-R</code> option causes <code>bf_tar</code> to remove inactive log files before the archive is written. This may reduce chances that the resulting archive is recoverable should it become damaged. The archive may be smaller though. The default is to leave log files.</p>
<h2>EXIT STATUS</h2>
<p> The script exits with status code 0 if everything went well, and nonzero if it encountered trouble.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; <code>bf_tar ~/.bogofilter &gt; outfile.tar</code> </p>
<p> Writes a standard .tar file containing the essential files from ~/.bogofilter to outfile.tar.</dl>
<dl>
<dt>
<dd> &bull; <code>bf_tar ~/.bogofilter | gzip -9 -c &gt; outfile.tar.gz</code> </p>
<p> Writes a gzipped .tar.gz file containing the essential files from ~/.bogofilter to outfile.tar.gz.</dl>
<dl>
<dt>
<dd> &bull; <code>bf_tar `pwd`/mydirectory &gt; outfile.tar</code> </p>
<p> Prepend <code>$(pwd)/</code> or <code>`pwd`/</code> if you want to specify an absolute path instead of a relative path.</dl>
<h2>NOTES</h2>
<p> This script is meant for use with Berkeley DB based bogofilter versions. </p>
<p> This script requires a SUSv2 compliant <code>pax</code> utility. </p>
<p> This script expects a SUSv2 compliant shell. Solaris systems should have the SUNWxcu4 package installed (when bogofilter is configured) so that /usr/xpg4/bin/sh can be used.</p>
<h2>AUTHORS</h2>
<p> Matthias Andree </p>
<h2>Index</h2>
