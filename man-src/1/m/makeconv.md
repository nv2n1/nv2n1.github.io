---
title: "makeconv(1)"
name: "makeconv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makeconv/"
description: "makeconv – compile a converter table"
---

<h2 class="name">NAME</h2>
<p> <code>makeconv</code> &#8211; compile a converter table </p>
<h2>SYNOPSIS</h2>
<p> <code>makeconv</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] <i>convertertable</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>makeconv</code> converts the ICU converter table <i>convertertable</i> into a binary file. The binary file has the same base name as <i>convertertable</i> but has a <code>.cnv</code> extension (instead of the typical <code>.ucm</code> extension of the <i>convertertable</i> file). This binary file can then be read directly by ICU, or used by <code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1) for incorporation into a larger archive or library. </p>
<p> The <i>convertertable</i> must be in the ICU ucm (Unicode Codepage Mapping) format in order to be understood by <code>makeconv</code>. The ICU ucm format is similar to the IBM NLTC upmap/tpmap/rpmap files. Comments in the <i>convertertable</i> are handled as follows. If a comment (starting with a `#&#8217; sign) that is after some text does contain the fallback indicator `|&#8217; then only the text starting with the `#&#8217; sign, and ending before the `|&#8217; sign, is ignored. Otherwise, or if the comment is the first thing on the line, the comment runs up to the end of the line. This special handling of comments is to accommodate the practice of putting fallback information in comments in the strict IBM NLTC ucmap format. </p>
<p> Note that new converters will be automatically found by ICU after their installation in ICU&#8217;s data directory. They do not need to be listed in the <code><a href="/docs/linux/man/5-convrtrs-txt/">convrtrs.txt</a></code>(5) converters aliases file in order to be available to applications using ICU. They do need to be listed there if one wants to give them aliases, or tags, though.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd> Include a copyright notice in the binary data.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd> Set the destination directory to <i>destination</i>. The default destination directory is specified by the environment variable <code>ICU_DATA</code>.</dl>
<h2>CAVEATS</h2>
<p> If an existing converter table is changed and recompiled using <code>makeconv</code>, the resulting binary file must be packaged in the same way that it was packaged initially. For example, if converters were grouped together in an archive or a library with <code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1), then the archive or library must be rebuilt with the new binary file. A standalone binary converter file will not take precedence over a packaged one.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ICU_DATA</code></p>
<dd> Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>VERSION</h2>
<p> 70.1</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000 IBM, Inc. and others.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-convrtrs-txt/">convrtrs.txt</a></code>(5)<br />
 <code><a href="/docs/linux/man/1-pkgdata/">pkgdata</a></code>(1) </p>
<h2>Index</h2>
