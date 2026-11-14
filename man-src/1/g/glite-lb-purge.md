---
title: "glite-lb-purge(1)"
name: "glite-lb-purge"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-purge/"
description: "glite-lb-purge – utility for removing inactive jobs from the L&B database"
---

<h2 class="name">NAME</h2>
<p> glite-lb-purge &#8211; utility for removing inactive jobs from the L&amp;B database </p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-purge</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-purge</code> is utility for removing inactive jobs from the L&amp;B database. By default, it removes jobs that reached CLEARED, ABORTED and CANCELLED state and also OTHER and DONE jobs that are inactive for specific (rather long) time. It is a command line frontend to server internal purge. It is used by administrators of bkserver and it is not supposed to be used at the user level. </p>
<p> <code>glite-lb-purge </code> may be run periodically in order to avoid database overflow, however the periodic purges are done by server itself, so check the configuration of the server first. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-m, &#8211;server <i>bkserver</i></p>
<dd> L&amp;B server machine name. If not specified, the environment variable EDG_WL_QUERY_SERVER is beeing checked. </p>
<dt>-a, &#8211;aborted NNN[smhd]</p>
<dd> Purge ABORTED jobs older than NNN seconds/minutes/hours/days (only one number and one letter allowed). If the time is not specified, the default timeout is determined by the server. </p>
<dt>-c, &#8211;cleared NNN[smhd]</p>
<dd> Purge CLEARED jobs older than given time. </p>
<dt>-n, &#8211;cancelled NNN[smhd]</p>
<dd> Purge CANCELLED jobs older than given time. </p>
<dt>-e, &#8211;done NNN[smhd]</p>
<dd> Purge DONE jobs older than given time. </p>
<dt>-o, &#8211;other NNN[smhd]</p>
<dd> Purge OTHER (i.e. job in other state than ABORTED, CLEARED or CANCELLED) jobs older than given time. </p>
<dt>-r, &#8211;dry-run</p>
<dd> Do not really purge. </p>
<dt>-j, &#8211;jobs <i>filename</i></p>
<dd> Input file with jobIds of jobs to purge. </p>
<dt>-l, &#8211;return-list</p>
<dd> Return list of jobid matching the purge/dump criteria. </p>
<dt>-s, &#8211;server-dump</p>
<dd> Dump jobs at the server into a file (see bkserverd). </p>
<dt>-i, &#8211;client-dump</p>
<dd> Receive stream of dumped jobs (NOT implemented yet!). </p>
<dt>-h, &#8211;help</p>
<dd> Display help. </p>
<dt>-v, &#8211;version</p>
<dd> Display version. </p>
<dt>-d, &#8211;debug</p>
<dd> Print diagnostics on the <i>stderr</i>. </p>
<dt>-x, &#8211;proxy</p>
<dd> Purge L&amp;B proxy. </p>
<dt>-X, &#8211;sock <i>path</i></p>
<dd> Purge L&amp;B proxy using given socket path. </p>
<dt>-t, &#8211;target-runtime NNN[smhd]</p>
<dd> Throttle purge to the estimated target runtime. </p>
<dt>-b, &#8211;background N</p>
<dd> Purge on the background. Default 1 when throttled purging. </p>
</dl>
<h2>FILES</h2>
<p> No configuration files needed. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>EDG_WL_QUERY_SERVER</code></p>
<dd> If $<code>EDG_WL_QUERY_SERVER</code> is set, its value is used as the bkserver address. </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-glite-lb-bkindex/">glite-lb-bkindex</a></code>(8), <code><a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a></code>(8), <code><a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a></code>(8), <code><a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a></code>(8), <code><a href="/docs/linux/man/1-glite-lb-logevent/">glite-lb-logevent</a></code>(1), <code><a href="/docs/linux/man/1-glite-lb-dump/">glite-lb-dump</a></code>(1), <code><a href="/docs/linux/man/1-glite-lb-load/">glite-lb-load</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> EU EGEE, JRA1. </p>
<h2>Index</h2>
