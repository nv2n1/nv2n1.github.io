---
title: "glite-lb-dump(1)"
name: "glite-lb-dump"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-dump/"
description: "glite-lb-dump – utility for dumping job events from L&B database"
---

<h2 class="name">NAME</h2>
<p> glite-lb-dump &#8211; utility for dumping job events from L&amp;B database</p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-dump</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-dump </code> is utility for dumping job events from L&amp;B database. It is primarilly used for statistical purposes. By default, it dumps events from the time when the last dum ended upto now. </p>
<p> <code>glite-lb-dump </code> may be run periodically, however the periodic dumps are done by server itself, so check the configuration of the server first. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code><i></i>,<code>&#8211;server</code><i>mkserver</i></p>
<dd> L&amp;B server machine name. If not specified, the environment variable EDG_WL_QUERY_SERVER is beeing checked. </p>
<dt><code>-f</code><i></i>,<code>&#8211;from</code><i>YYYYMMDDHHmmss</i></p>
<dd> Beginning of the time interval for events to be dumped. </p>
<dt><code>-t</code><i></i>,<code>&#8211;to</code><i>YYYYMMDDHHmmss</i></p>
<dd> End of the time interval for events to be dumped. </p>
<dt><code>-h</code><i></i>,<code>&#8211;help</code></p>
<dd> Display help. </p>
<dt><code>-v</code><i></i>,<code>&#8211;version</code></p>
<dd> Display version. </p>
<dt><code>-d</code>, &#8211;debug</p>
<dd> Print diagnostics on the <i>stderr</i>. </p>
</dl>
<h2>FILES</h2>
<p> No configuration files needed. </p>
<h2>ENVIRONMENT</h2>
<p> No environment variables needed. </p>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-glite-lb-bkindex/">glite-lb-bkindex</a></code>(8), <a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a>(8), <a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a>(8), <a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a>(8), <a href="/docs/linux/man/1-glite-lb-logevent/">glite-lb-logevent</a>(1), </p>
<h2>AUTHOR</h2>
<p> EU EGEE, JRA1. </p>
<h2>Index</h2>
