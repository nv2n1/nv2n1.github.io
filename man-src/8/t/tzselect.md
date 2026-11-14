---
title: "tzselect(8)"
name: "tzselect"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tzselect/"
description: "tzselect – select a timezone"
---

<p>tzselect &#8211; select a timezone</p>
<h2>Synopsis</h2>
<p><code>tzselect</code></p>
<h2>Description</h2>
<p>The <code>tzselect</code> program asks the user for information about the current location, and outputs the resulting timezone description to standard output. The output is suitable as a value for the <code>TZ</code> environment variable. </p>
<p> All interaction with the user is done via standard input and standard error.</p>
<h2>Exit Status</h2>
<p>The exit status is zero if a timezone was successfully obtained from the user, and is nonzero otherwise.</p>
<h2>Environment</h2>
<dl>
<dt><code>AWK</code></p>
<dd>Name of a POSIX-compliant <i>awk</i> program (default: <code>awk</code>).</p>
<dt><code>TZDIR</code></p>
<dd>Name of the directory containing timezone data files (default: <i>/usr/share/zoneinfo</i>).</dl>
<h2>Files</h2>
<dl>
<dt><code>TZDIR</code><i>/iso3166.tab</i></p>
<dd>Table of ISO 3166 2-letter country codes and country names.</p>
<dt><code>TZDIR</code><i>/zone.tab</i></p>
<dd>Table of country codes, latitude and longitude, TZ values, and descriptive comments.</p>
<dt><code>TZDIR</code><i>/</i><i>TZ</i></p>
<dd>Timezone data file for timezone <i>TZ</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-tzfile/">tzfile</a></code>(5), <code><a href="/docs/linux/man/8-zdump/">zdump</a></code>(8), <code><a href="/docs/linux/man/8-zic/">zic</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
