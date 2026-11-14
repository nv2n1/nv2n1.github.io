---
title: "flow-rptfmt(1)"
name: "flow-rptfmt"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-rptfmt/"
description: "flow-rptfmt – Format the output of flow-report in ASCII or HTML"
---

<h2>NAME</h2>
<p> flow-rptfmt &#8211; Format the output of flow-report in ASCII or HTML</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-rptfmt</code> [ <code>-hHnp</code> ] [ <code>-a</code><i> alarm_time</i> ] [ <code>-f</code><i> format</i> ] [ <code>-F</code><i> fields</i> ] [ <code>-m</code><i> max_lines</i> ] [ <code>-s</code><i> sort_field</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-rptfmt</code> utility processes the CSV output of flow-report into formatted ASCII or HTML. Sorting, maximum display lines, field filter, header display, and name substitution are supported during post processing. Additionally an alarm can be set for use in CGI scripts to limit the CPU time of formatting.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code><i> alarm_time</i></p>
<dd> Exit after <i>alarm_time</i> seconds.</p>
<dt><code>-f</code><i> ascii</i><code>|</code><i>html</i></p>
<dd> Set output format. Defaults to ASCII.</p>
<dt><code>-F</code><i> display_fields</i></p>
<dd> Limit columns to <i>display_fields</i></p>
<dt><code>-h</code></p>
<dd> Help.</p>
<dt><code>-H</code></p>
<dd> Display header information.</p>
<dt><code>-m </code><i>max_lines</i></p>
<dd> Limit rows to max_lines.</p>
<dt><code>-n</code></p>
<dd> Enable symbol table lookups.</p>
<dt><code>-p</code></p>
<dd> Display in percent total form.</p>
<dt><code>-s</code><i> sort_field</i></p>
<dd> Sort on <i>sort_field</i>. Prepend with + for ascending, &#8211; for descending sort.</dl>
<h2>EXAMPLES</h2>
<p> Format the output of daily-ip-protocol.txt in ASCII. Display the ip-protocol and octets fields in percent total format with symbols. Limit output to top 5 sorted by octets. </p>
<p> <code>cat daily-ip-protocol.txt | flow-rptfmt -fascii -Fip-protocol,octets -p -n -m5 </code></p>
<h2>BUGS</h2>
<p> Sorting could be faster. Percent totals could be faster. May not work with flow-report prior to 0.68.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
