---
title: "opimport(1)"
name: "opimport"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opimport/"
description: "opimport – converts sample database files"
---

<h2 class="name">NAME</h2>
<p> opimport &#8211; converts sample database files </p>
<h2>SYNOPSIS</h2>
<p> <code>opimport</code> [ <i>options</i> ] input_file</p>
<h2>DESCRIPTION</h2>
<p> <code>opimport</code> converts sample database files from a foreign binary format (abi) to the native format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;abi / -a</code></dt>
<dd> Input abi file description location. </dd>
<dt><code>&#8211;force / -f</code></dt>
<dd> Force conversion even if the input and output abi are identical. </dd>
<dt><code>&#8211;output / -o filename</code></dt>
<dd> Specify the output filename. If the output file already exists it is not overwritten but data are accumulated in. Sample filename are informative for post profile tools and must be kept identical, in other word the pathname from the first path component containing a &#8216;{&#8216; must be kept as it in the output filename. </dd>
<dt><code>&#8211;help / -? / &#8211;usage</code></dt>
<dd> Show help message. </dd>
<dt><code>&#8211;verbose / -V</code></dt>
<dd> Give verbose debugging output. </dd>
<dt><code>&#8211;version / -v</code></dt>
<dd> Show version. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by opimport </p>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/oprofile/abi</i></dt>
<dd> The abi file description of the sample database files </dd>
</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</dt>
<dd>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
