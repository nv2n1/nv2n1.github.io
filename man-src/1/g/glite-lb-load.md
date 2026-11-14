---
title: "glite-lb-load(1)"
name: "glite-lb-load"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-load/"
description: "glite-lb-load – utility for loading job events into the L&B database"
---

<h2 class="name">NAME</h2>
<p> glite-lb-load &#8211; utility for loading job events into the L&amp;B database</p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-load</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-load </code> is utility for loading job events into the L&amp;B database. It is primarilly used for recovery purposes. By default, it loads events from the last dump. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-m, &#8211;server <i>bkserver</i></p>
<dd> L&amp;B server machine name. If not specified, the environment variable EDG_WL_QUERY_SERVER is beeing checked. </p>
<dt>-f, &#8211;file <i>filename</i></p>
<dd> File with dumped data to be loaded. </p>
<dt>-h, &#8211;help</p>
<dd> Display help. </p>
<dt>-v, &#8211;version</p>
<dd> Display version. </p>
<dt>-d, &#8211;debug</p>
<dd> Print diagnostics on the <i>stderr</i>. </p>
</dl>
<h2>FILES</h2>
<p> No configuration files needed. </p>
<h2>ENVIRONMENT</h2>
<p> No environment variables needed. </p>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker valailable at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-glite-lb-bkindex/">glite-lb-bkindex</a></code>(8), <a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a>(8), <a href="/docs/linux/man/1-glite-lb-dump/">glite-lb-dump</a>(1), <a href="/docs/linux/man/1-glite-lb-purge/">glite-lb-purge</a>(1), </p>
<h2>AUTHOR</h2>
<p> EU EGEE, JRA1. </p>
<h2>Index</h2>
