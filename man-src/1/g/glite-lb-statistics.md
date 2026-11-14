---
title: "glite-lb-statistics(1)"
name: "glite-lb-statistics"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-statistics/"
description: "glite-lb-statistics – tool for converting L&B job dump to Job History Record in XML"
---

<h2 class="name">NAME</h2>
<p> glite-lb-statistics &#8211; tool for converting L&amp;B job dump to Job History Record in XML </p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-statistics</code> [<i>OPTIONS</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-statistics</code> takes a dump file for one job and converts it to an XML-encoded Job History Record that contains all the relevant information from the job&#8217;s life. The Job History Records can be fed into statistics tools to reveal interesting information about job behavior in the Grid. </p>
<p> The dump file should be a dump for a single job only. Typically, the <code><a href="/docs/linux/man/1-glite-lb-dump_exporter/">glite-lb-dump_exporter</a></code>(1) utility is used to convert L&amp;B server dumps for further processing by <code><a href="/docs/linux/man/1-glite-lb-statistics/">glite-lb-statistics</a></code>(1). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code>, &#8211;versionone</p>
<dd> Use version 1 of the attributes (it is obsolete now). </p>
<dt><code>-f</code>, file <i>FILE</i></p>
<dd> A dump file to process. </p>
<dt><code>-h</code>, &#8211;help</p>
<dd> Display help and exit. </p>
<dt><code>-o</code>, &#8211;outfile <i>FILE</i></p>
<dd> Output filename. </p>
<dt><code>-V</code>, &#8211;version</p>
<dd> Output version information and exit. </p>
<dt><code>-v</code>, &#8211;verbose</p>
<dd> Print extensive debug output to stderr. </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>AUTHORS</h2>
<p> L&amp;B Product Team, CESNET. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-glite-lb-dump_exporter/">glite-lb-dump_exporter</a></code>(1), <code><a href="/docs/linux/man/1-glite-lb-purge/">glite-lb-purge</a></code>(1), README.LB-statistics </p>
<h2>Index</h2>
