---
title: "mountstats(8)"
name: "mountstats"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mountstats/"
description: "mountstats – Displays various NFS client per-mount statistics"
---

<p>mountstats &#8211; Displays various NFS client per-mount statistics</p>
<h2>Synopsis</h2>
<p><code>mountstats</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;version</code>] [<code>-f</code>|<code>&#8211;file</code> <i>infile</i>] [<code>-S</code>|<code>&#8211;since</code> <i>sincefile</i>] [ [<code>-n</code>|<code>&#8211;nfs</code>] | [<code>-r</code>|<code>&#8211;rpc</code>] | [<code>-R</code>|<code>&#8211;raw</code>] ] [<i>mountpoint</i>]<i>&#8230;</i> <code>mountstats iostat</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;version</code>] [<code>-f</code>|<code>&#8211;file</code> <i>infile</i>] [<code>-S</code>|<code>&#8211;since</code> <i>sincefile</i>] [<i>interval</i>] [<i>count</i>] [<i>mountpoint</i>]<i>&#8230;</i> <code>mounstats nfsstat</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-v</code>|<code>&#8211;version</code>] [<code>-f</code>|<code>&#8211;file</code> <i>infile</i>] [<code>-S</code>|<code>&#8211;since</code> <i>sincefile</i>] [<code>-3</code>] [<code>-4</code>] [<i>mountpoint</i>]<i>&#8230;</i> </p>
<h2>Description</h2>
<p>The <code>mountstats</code> command displays various NFS client statisitics for each given <i>mountpoint</i>. </p>
<p> If no <i>mountpoint</i> is given, statistics will be displayed for all NFS mountpoints on the client.</p>
<h3>Sub-commands</h3>
<p>Valid <code><a href="/docs/linux/man/8-mountstats/">mountstats</a></code>(8) subcommands are:</p>
<dl>
<dt><code>mountstats</code></p>
<dd>Display a combination of per-op RPC statistics, NFS event counts, and NFS byte counts. This is the default sub-command that will be executed if no sub-command is given.</p>
<dt><code>iostat</code></p>
<dd>Display iostat-like statistics.</p>
<dt><code>nfsstat</code></p>
<dd>Display nfsstat-like statistics.</dl>
<h2>Options</h2>
<h3>Options valid for all sub-commands</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>show the help message and exit</p>
<dt><code>-v, &#8211;version</code></p>
<dd>show program&#8217;s version number and exit</p>
<dt><code>-f </code><i>infile</i>, <code>&#8211;file </code><i>infile</p>
<dd>Read stats from infile</i> instead of <i>/proc/self/mountstats</i>. <i>infile</i> must be in the same format as <i>/proc/self/mountstats</i>. This may be used with the <code>-S</code>|<code>&#8211;since</code> options to display the delta between two different points in time. This may not be used with the <i>interval</i> or <i>count</i> options of the <code>iostat</code> sub-command.</p>
<dt><code>-S </code><i>sincefile</i>, <code>&#8211;since </code><i>sincefile</p>
<dd>Show difference between current stats and those in sincefile</i>. <i>sincefile</i> must be in the same format as <i>/proc/self/mountstats</i>. This may be used with the <code>-f</code>|<code>&#8211;file</code> options to display the delta between two different points in time. This may not be used with the <i>interval</i> or <i>count</i> options of the <code>iostat</code> sub-command.</dl>
<h3>Options specific to the mountstats sub-command</h3>
<p><code>-n, &#8211;nfs</code> Display only the NFS statistics</p>
<dl>
<dt><code>-r, &#8211;rpc</code></p>
<dd>Display only the RPC statistics</p>
<dt><code>-R, &#8211;raw</code></p>
<dd>Display only the raw statistics. This is intended for use with the <code>-f</code>|<code>&#8211;file</code> and <code>-S</code>|<code>&#8211;since</code> options.</dl>
<h3>Options specific to the iostat sub-command</h3>
<dl>
<dt><i>interval</i></p>
<dd>Specifies the amount of time in seconds between each report. The first report contains statistics for the time since each file system was mounted. Each subsequent report contains statistics collected during the interval since the previous report. This may not be used with the <code>-f</code>|<code>&#8211;file</code> or <code>-S</code>|<code>&#8211;since</code> options.</dl>
<dl>
<dt><i>count</i></p>
<dd>Determines the number of reports generated at <i>interval</i> seconds apart. If the <i>interval</i> parameter is specified without the <i>count</i> parameter, the command generates reports continuously. This may not be used with the <code>-f</code>|<code>&#8211;file</code> or <code>-S</code>|<code>&#8211;since</code> options.</dl>
<h3>Options specific to the nfsstat sub-command</h3>
<dl>
<dt><code>-3</code></p>
<dd>Show only NFS version 3 statistics. The default is to show both version 3 and version 4 statistics.</p>
<dt><code>-4</code></p>
<dd>Show only NFS version 4 statistics. The default is to show both version 3 and version 4 statistics.</dl>
<h2>Files</h2>
<dl>
<dt><code>/proc/self/mountstats</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iostat/">iostat</a></code>(8), <code><a href="/docs/linux/man/8-nfsiostat/">nfsiostat</a></code>(8), <code><a href="/docs/linux/man/8-nfsstat/">nfsstat</a></code>(8)</p>
<h2>Author</h2>
<p>Chuck Lever &lt;chuck.lever [at] oracle.com&gt;</p>
