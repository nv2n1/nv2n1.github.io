---
title: "glite-lb-bkpurge-offline(1)"
name: "glite-lb-bkpurge-offline"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-bkpurge-offline/"
description: "glite-lb-bkpurge-offline – emergency utility for removing inactive jobs from the L&B database"
---

<h2 class="name">NAME</h2>
<p> glite-lb-bkpurge-offline &#8211; emergency utility for removing inactive jobs from the L&amp;B database </p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-bkpurge-offline</code> [<i>OPTIONS</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-bkpurge-offline</code> is a utility for removing inactive jobs from the L&amp;B database. By default, it removes jobs that reached CLEARED, ABORTED and CANCELED state and also OTHER and DONE jobs that are inactive for a specific (rather long) period of time. It calls SQL database commands directly. </p>
<p> This utility is provided for <code>emergency and expert use only</code>. Exact semantics of job age are slightly different from regular <code>glite-lb-bkpurge</code>, there is no synchronization with running L&amp;B server and/or proxy when jobs receive new events while being purged, and error handling is minimal. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> <i>NNN</i>[smhd]</p>
<dd> Purge ABORTED jobs older than NNN seconds/minutes/hours/days (only one number and one letter allowed). If the time is not specified, the default timeout is determined by the server. </p>
<dt><code>-c</code> <i>NNN</i>[smhd]</p>
<dd> Purge CLEARED jobs older than the given age. </p>
<dt><code>-d</code> <i>NNN</i>[smhd]</p>
<dd> Purge DONE jobs older than the given age. </p>
<dt><code>-h</code></p>
<dd> Display help. </p>
<dt><code>-m</code> <i>BKSERVER</i></p>
<dd> L&amp;B server machine name. If not specified, the environment variable EDG_WL_QUERY_SERVER is checked for hostname and port. </p>
<dt><code>-M</code> {singleshot|staged}</p>
<dd> Cleaning method (default=staged). </p>
<dt><code>-n</code> <i>NNN</i>[smhd]</p>
<dd> Purge CANCELED jobs older than the given age. </p>
<dt><code>-o</code> <i>NNN</i>[smhd]</p>
<dd> Purge OTHER jobs (i.e., jobs in states other than ABORTED, CLEARED or CANCELED) older than the given age. </p>
<dt><code>-p</code></p>
<dd> Purge L&amp;B proxy database (default: L&amp;B server DB). </p>
<dt><code>-t</code></p>
<dd> Free unused space if using MyISAM DB engine. Note that MyISAM is not used by default in L&amp;B deployments. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>EDG_WL_QUERY_SERVER</code></p>
<dd> If <code>$EDG_WL_QUERY_SERVER</code> is set, its value is used as the bkserver address. </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>AUTHORS</h2>
<p> L&amp;B Product Team, CESNET. </p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><code><a href="/docs/linux/man/1-glite-lb-purge/">glite-lb-purge</a></code>(1) </p>
<h2>Index</h2>
