---
title: "opgprof(1)"
name: "opgprof"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opgprof/"
description: "opgprof – produce gprof-format profile data"
---

<h2 class="name">NAME</h2>
<p> opgprof &#8211; produce gprof-format profile data </p>
<h2>SYNOPSIS</h2>
<p> <code>opgprof</code> [ <i>options</i> ] [profile specification]</p>
<h2>DESCRIPTION</h2>
<p> <code>opgprof</code> outputs gprof-format profile data for a given binary image, from an OProfile session. See <a href="/docs/linux/man/1-oprofile/">oprofile</a>(1) for how to write profile specifications. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help / -? / &#8211;usage</code></p>
<dd> Show help message. </p>
<dt><code>&#8211;version / -v</code></p>
<dd> Show version. </p>
<dt><code>&#8211;verbose / -V [options]</code></p>
<dd> Give verbose debugging output. </p>
<dt><code>&#8211;session-dir=dir_path</code></p>
<dd> Use sample database out of directory dir_path instead of the default location (/var/lib/oprofile). </p>
<dt><code>&#8211;image-path / -p [paths]</code></p>
<dd> Comma-separated list of additional paths to search for binaries. This is needed to find modules in kernels 2.6 and upwards. </p>
<dt><code>&#8211;root / -R [path]</code></p>
<dd> A path to a filesystem to search for additional binaries. </p>
<dt><code>&#8211;threshold / -t [percentage]</code></p>
<dd> Only output data for symbols that have more than the given percentage of total samples. </p>
<dt><code>&#8211;output-filename / -o [file]</code></p>
<dd> Output to the given file instead of the default, gmon.out </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by opgprof. </p>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/oprofile/samples/</i></p>
<dd> The location of the generated sample files. </p>
</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
