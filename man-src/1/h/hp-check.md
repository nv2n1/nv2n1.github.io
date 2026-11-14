---
title: "hp-check(1)"
name: "hp-check"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-check/"
description: "hp-check – Dependency/Version Check Utility"
---

<h2 class="name">NAME</h2>
<p> hp-check &#8211; Dependency/Version Check Utility </p>
<h2>DESCRIPTION</h2>
<p> Checks dependency versions,permissions of HPLIP. (Run as &#8216;python ./check.py&#8217; from the HPLIP tarball before installation.)</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-check [OPTIONS]</code></p>
<h2>OPTIONS</h2>
<dl>
<dt>Compile-time check:</p>
<dd> -c or &#8211;compile</p>
<dt>Run-time check:</p>
<dd> -r or &#8211;run or &#8211;runtime</p>
<dt>Compile and run-time checks:</p>
<dd> -b or &#8211;both (default)</p>
<dt>Set the logging level:</p>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</p>
<dt>Run in debug mode:</p>
<dd> -g (same as option: -ldebug)</p>
<dt>Output plain text only:</p>
<dd> -t</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</dl>
<h2>NOTES</h2>
<dl>
<dt>1. For checking for the proper build environment for the HPLIP supplied tarball (.tar.gz or .run),</p>
<dd>
<dt>use the &#8211;compile or &#8211;both switches.</p>
<dd>
<dt>2. For checking for the proper runtime environment for a distro supplied package (.deb, .rpm, etc),</p>
<dd>
<dt>use the &#8211;runtime switch.</p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
