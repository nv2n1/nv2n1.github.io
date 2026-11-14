---
title: "lsb_release(1)"
name: "lsb_release"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsb_release/"
description: "lsb_release – print distribution-specific information"
---

<h2 class="name">NAME</h2>
<p> lsb_release &#8211; print distribution-specific information </p>
<h2>SYNOPSIS</h2>
<p> <code>lsb_release</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>lsb_release</code> command provides certain LSB (Linux Standard Base) and distribution-specific information. </p>
<p> If no options are given, the <i>-v</i> option is assumed.</p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with long options starting with two dashes (`&#8211;&#8216;). A summary of options are included below.</p>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Show the version of the LSB against which your current installation is compliant. The version is expressed as a colon separated list of LSB module descriptions.</p>
<dt><code>-i, &#8211;id</code></p>
<dd> Display the distributor&#8217;s ID.</p>
<dt><code>-d, &#8211;description</code></p>
<dd> Display a description of the currently installed distribution.</p>
<dt><code>-r, &#8211;release</code></p>
<dd> Display the release number of the currently installed distribution.</p>
<dt><code>-c, &#8211;codename</code></p>
<dd> Display the code name of the currently installed distribution.</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Display all of the above information.</p>
<dt><code>-s, &#8211;short</code></p>
<dd> Use the short output format for any information displayed. This format omits the leading header(s).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</dl>
<h2>NOTES</h2>
<p> This is a reimplementation of the <code>lsb_release</code> command provided by the Free Standards Group. Any bugs are solely the responsibility of the author below. </p>
<p> Detection of systems using a mix of packages from various distributions or releases is something of a black art; the current heuristic tends to assume that the installation is of the earliest distribution which is still being used by <code>apt</code> but that heuristic is subject to error.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-lsb/">lsb</a>(8)</p>
<h2>AUTHOR</h2>
<p> Chris Lawrence &lt;lawrencc [at] debian.org&gt;. </p>
<h2>Index</h2>
