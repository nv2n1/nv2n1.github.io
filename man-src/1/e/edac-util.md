---
title: "edac-util(1)"
name: "edac-util"
section: "1"
letter: "e"
url: "/docs/linux/man/1-edac-util/"
description: "edac-util – EDAC error reporting utility."
---

<h2 class="name">NAME</h2>
<p> edac-util &#8211; EDAC error reporting utility.</p>
<h2>SYNOPSIS</h2>
<p> <code>edac-util </code> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>edac-util</code> program reads information from EDAC (Error Detection and Correction) drivers in the kernel, using files exported by these drivers in sysfs. With no options, <code>edac-util</code> will report any uncorrected error (UE) or corrected error (CE) information recorded by EDAC, along with any DIMM label information registered with EDAC. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a summary of the command-line options.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Quiet mode. For some reports, <code>edac-util</code> will report corrected and uncorrected error counts for all MC, csrow, and channel combinations, even if the current count of errors is zero. The <i>&#8211;quiet</i> flag will suppress the display of any locations with zero errors, thus creating a more terse report. No output will be generated if there are zero total errors currently recorded by EDAC. Additionally, the use of <i>&#8211;quiet</i> will suppress all informational and debug messages, displaying only fatal errors.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Increase verbosity. Multiple <i>-v</i>&#8216;s may be used.</p>
<dt><code>-s, &#8211;status</code></p>
<dd> Displays the current status of EDAC drivers. <code>edac-util</code> will report whether it detects that EDAC drivers are loaded, and the number of memory controllers (MCs) found in sysfs. In verbose mode, the MC id and name of each controller will also be printed.</p>
<dt><code>-r, &#8211;report=</code><i>report,&#8230;</i></p>
<dd> Specify the report to generate. Currently, the available reports are <i>default</i>, <i>simple</i>, <i>full</i>, <i>ue</i>, and <i>ce</i>. These reports are detailed in the <code>EDAC REPORTS</code> section below. More than one report may be specified in a comma-separated list. </p>
</dl>
<h2>EDAC REPORTS</h2>
<dl>
<dt><code>default</code></p>
<dd> The <i>default</i> <code>edac-util</code> report is generated when the program is run without any options. If there are no errors logged by EDAC, this report will display &quot;No errors to report.&quot; to stdout. Otherwise, error counts for each MC, csrow, channel combination with attributed errors are displayed, along with corresponding DIMM labels, if these labels have been registered in sysfs. </p>
<p> The default report will also display any errors that do not have any DIMM information. These errors occur when errors are reported in the memory controller overflow register, indicating that more than one error occurred during a given EDAC poll cycle. It is usually obvious from which DIMM locations these errors were generated.</p>
<dt><code>simple</code></p>
<dd> The <i>simple</i> report reports total corrected and uncorrected errors for each MC detected on the system. It also displays a tally of total errors. With the <i>&#8211;quiet</i> option, only non-zero error counts are displayed.</p>
<dt><code>full</code></p>
<dd> The <i>full</i> report generates a line of output for every MC, csrow, channel combination found in EDAC sysfs. This includes counts of errors with no information (&quot;noinfo&quot; errors). Output is of the form: </p>
<pre>
MC:(csrow|noinfo):(label|all):(UE|CE):count 
</pre>
<p> With the <i>&#8211;quiet</i> option, only non-zero error counts will be displayed.</p>
<dt><code>ue</code></p>
<dd> This report simply displays the total number of Uncorrected Errors (UEs) detected on the system. With the <i>&#8211;quiet</i> option, output will be suppressed unless there are 1 or more errors to report.</p>
<dt><code>ce</code></p>
<dd> This report simply displays the total number of Corrected Errors (CEs) detected on the system. With the <i>&#8211;quiet</i> option, output will be suppressed unless there are 1 or more errors to report. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-edac/">edac</a></code>(3), <code><a href="/docs/linux/man/8-edac-ctl/">edac-ctl</a></code>(8) </p>
<h2>Index</h2>
