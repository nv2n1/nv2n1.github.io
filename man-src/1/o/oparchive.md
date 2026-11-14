---
title: "oparchive(1)"
name: "oparchive"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oparchive/"
description: "oparchive – produce archive of oprofile data for offline analysis"
---

<h2 class="name">NAME</h2>
<p> oparchive &#8211; produce archive of oprofile data for offline analysis </p>
<h2>SYNOPSIS</h2>
<p> <code>oparchive</code> [ <i>options</i> ] [profile specification] <code>-o</code> [directory]</p>
<h2>DESCRIPTION</h2>
<p> <code>oparchive</code> generates a directory populated with executable, debug, and oprofile sample files. This directory can be move to another machine via tar and analyzed without further use of the data collection machine. See <a href="/docs/linux/man/1-oprofile/">oprofile</a>(1) for how to write profile specifications. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help / -? / &#8211;usage</code></p>
<dd> Show help message. </p>
<dt><code>&#8211;version / -v</code></p>
<dd> Show version. </p>
<dt><code>&#8211;verbose / -V [options]</code></p>
<dd> Give verbose debugging output. </p>
<dt><code>&#8211;session-dir=dir_path</code></p>
<dd> Use sample database from the specified directory <i>dir_path</i> instead of the default locations. If <i>&#8211;session-dir</i> is not specified, then <code>oparchive</code> will search for samples in <i>&lt;current_dir&gt;/oprofile_data</i> first. If that directory does not exist, the standard session-dir of /var/lib/oprofile is used. </p>
<dt><code>&#8211;image-path / -p [paths]</code></p>
<dd> Comma-separated list of additional paths to search for binaries. This is needed to find modules in kernels 2.6 and upwards. </p>
<dt><code>&#8211;root / -R [path]</code></p>
<dd> A path to a filesystem to search for additional binaries. </p>
<dt><code>&#8211;output-directory / -o [directory]</code></p>
<dd> Output to the given directory. There is no default. This must be specified. </p>
<dt><code>&#8211;exclude-dependent / -x</code></p>
<dd> Do not include application-specific images for libraries, kernel modules and the kernel. This option only makes sense if the profile session used &#8211;separate. </p>
<dt><code>&#8211;list-files / -l</code></p>
<dd> Only list the files that would be archived, don&#8217;t copy them. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by oparchive. </p>
<h2>FILES</h2>
<p> <i>&lt;current_dir&gt;/oprofile_data/samples</i></p>
<dl>
<dt>
<dd> Or</dl>
<p> <i>/var/lib/oprofile/samples/</i> </p>
<dl>
<dt>
<dd> The location of the generated sample files.</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
