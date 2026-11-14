---
title: "orte-top(1)"
name: "orte-top"
section: "1"
letter: "o"
url: "/docs/linux/man/1-orte-top/"
description: "ompi-top, orte-top – Diagnostic to provide process info similar to the popular \"top\" program."
---

<h2 class="name">NAME</h2>
<p> ompi-top, orte-top &#8211; Diagnostic to provide process info similar to the popular &quot;top&quot; program. </p>
<p> <code>NOTE:</code> <i>ompi-top</i>, and <i>orte-top</i> are exact synonyms for each other. Using any of the names will result in exactly identical behavior.</p>
<h2>SYNOPSIS</h2>
<p> <code>ompi-top</code> [ options ]</p>
<h2>Options</h2>
<p> <i>ompi-top</i> collects and displays process information in a manner similar to that of the popular &quot;top&quot; program.</p>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Display help for this command</p>
<dt><code>-pid | &#8211;pid </code>&lt;value&gt;</p>
<dd> The pid of the mpirun whose processes you want information about, or the name of the file (specified as file:filename) that contains that info. Note that the ompi-top command must be executed on the same node as mpirun to use this option.</p>
<dt><code>-uri | &#8211;uri </code>&lt;value&gt;</p>
<dd> Specify the URI of the mpirun whose processes you want information about, or the name of the file (specified as file:filename) that contains that info. Note that the ompi-top command does not have to be executed on the same node as mpirun to use this option.</p>
<dt><code>-rank | &#8211;rank </code>&lt;value&gt;</p>
<dd> The rank of the processes to be monitored. This can consist of a single rank, or a comma-separated list of ranks. These can include rank ranges separated by a &#8216;-&#8216;. If this option is not provided, or a value of -1 is given, ompi-top will default to displaying information on all ranks.</p>
<dt><code>-bynode | &#8211;bynode</code></p>
<dd> Display the results grouped by node, with each node&#8217;s processes reported in rank order. If this option is not provided, ompi-top will default to displaying all results in rank order.</p>
<dt><code>-update-rate | &#8211;update-rate </code>&lt;value&gt;</p>
<dd> The time (in seconds) between updates of the displayed information. If this option is not provided, ompi-top will default to executing only once.</p>
<dt><code>-timestamp | &#8211;timestamp</code></p>
<dd> Provide an approximate time when each sample was taken. This time is approximate as it only shows the time when the sample command was issued.</p>
<dt><code>-log-file | &#8211;log-file </code>&lt;value&gt;</p>
<dd> Log the results to the specified file instead of displaying them to stdout.</dl>
<h2>DESCRIPTION</h2>
<p> <i>ompi-top</i> collects and displays process information in a manner similar to that of the popular &quot;top&quot; program. It doesn&#8217;t do the fancy screen display, but does allow you to monitor available process information (to the limits of the underlying operating system) of processes irrespective of their location.</p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
