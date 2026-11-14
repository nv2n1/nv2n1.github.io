---
title: "newhelp(1)"
name: "newhelp"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newhelp/"
description: "newhelp – generate a performance metrics help database"
---

<h2>NAME</h2>
<p> <code>newhelp</code> &#8211; generate a performance metrics help database</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/newhelp</code> [<code>-V</code>] [<code>-n</code> <i>pmnsfile</i>] [<code>-o</code> <i>outputfile</i>] [<code>-v</code> <i>version</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>newhelp</code> generates the Performance Co-Pilot help text files used by Performance Metric Domain Agents (PMDAs). </p>
<p> Normally <code>newhelp</code> operates on the default Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative namespace is loaded from the file <i>pmnsfile</i>. </p>
<p> When there is only one input file, the base name of the new database is derived from the name of the input <i>file</i>, otherwise the <code>-o</code> flag must be given to explicitly name the database. If no input files are supplied, <code>newhelp</code> reads from the standard input stream, in which case the <code>-o</code> flag must be given. </p>
<p> If the output file name is determined to be <code>foo</code>, <code>newhelp</code> will create <code>foo.dir</code> and <code>foo.pag</code>. </p>
<p> Although historically there have been multiple help text file formats, the only format currently supported using the <code>-v</code> option is <i>version</i> 2, and this is the default if no <code>-v</code> flag is provided. </p>
<p> The <code>-V</code> flag causes verbose messages to be printed while <code>newhelp</code> is parsing its input. </p>
<p> The first line of each entry in a help source file consists of an &#8220;@&#8221; character beginning the line followed by a space and then the performance metric name and a one line description of the metric. Following lines (up to the next line beginning with &#8220;@&#8221; or end of file) may contain a verbose help description. E.g. </p>
<pre>
#
# This is an example of newhelp's input syntax
#
@ kernel.all.cpu.idle CPU idle time
A cumulative count of the number of milliseconds
of CPU idle time, summed over all processors.
</pre>
<p> Three-part numeric metric identifiers (PMIDs) may be used in place of metric names, e.g. 60.0.23 rather than kernel.all.cpu.idle in the example above. Other than for dynamic metrics (where the existence of a metric is known to a PMDA, but not visible in the PMNS and hence has no name that could be known to <i>newhelp</i>) use of this syntactic variant is not encouraged. </p>
<p> Lines beginning with &#8220;#&#8221; are ignored, as are blank lines in the file before the first &#8220;@&#8221;. The verbose help text is optional. </p>
<p> As a special case, a &#8220;metric&#8221; name of the form <i>NNN.MM</i> (for numeric <i>NNN</i> and <i>MM</i>) is interpreted as an instance domain identification, and the text describes the instance domain.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chkhelp/">chkhelp</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindomtext/">pmLookupInDomText</a></code>(3), <code><a href="/docs/linux/man/3-pmlookuptext/">pmLookupText</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
