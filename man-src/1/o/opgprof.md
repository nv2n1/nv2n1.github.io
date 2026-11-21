---
title: "opgprof(1)"
name: "opgprof"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opgprof/"
description: "opgprof – produce gprof-format profile data"
---

<h2>SYNOPSIS</h2>
<p> <code>opgprof</code> [ <i>options</i> ] [profile specification]</p>
<h2>DESCRIPTION</h2>
<p> <code>opgprof</code> outputs gprof-format profile data for a given binary image, from an OProfile session. See <a href="/docs/linux/man/1-oprofile/">oprofile</a>(1) for how to write profile specifications. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help / -? / &#8211;usage</code></dt>
<dd> Show help message. </dd>
<dt><code>&#8211;version / -v</code></dt>
<dd> Show version. </dd>
<dt><code>&#8211;verbose / -V [options]</code></dt>
<dd> Give verbose debugging output. </dd>
<dt><code>&#8211;session-dir=dir_path</code></dt>
<dd> Use sample database out of directory dir_path instead of the default location (/var/lib/oprofile). </dd>
<dt><code>&#8211;image-path / -p [paths]</code></dt>
<dd> Comma-separated list of additional paths to search for binaries. This is needed to find modules in kernels 2.6 and upwards. </dd>
<dt><code>&#8211;root / -R [path]</code></dt>
<dd> A path to a filesystem to search for additional binaries. </dd>
<dt><code>&#8211;threshold / -t [percentage]</code></dt>
<dd> Only output data for symbols that have more than the given percentage of total samples. </dd>
<dt><code>&#8211;output-filename / -o [file]</code></dt>
<dd> Output to the given file instead of the default, gmon.out </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by opgprof. </p>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/oprofile/samples/</i></dt>
<dd> The location of the generated sample files. </dd>
</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</dt>
<dd>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
