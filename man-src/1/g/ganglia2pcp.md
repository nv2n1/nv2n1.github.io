---
title: "ganglia2pcp(1)"
name: "ganglia2pcp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-ganglia2pcp/"
description: "ganglia2pcp – import ganglia data and create a PCP archive"
---

<h2>NAME</h2>
<p> <code>ganglia2pcp</code> &#8211; import ganglia data and create a PCP archive</p>
<h2>SYNOPSIS</h2>
<p> <code>ganglia2pcp</code> [<code>-s</code> <i>start</i>] [<code>-e</code> <i>end</i>] [<code>-f</code> <i>outfile</i>] [<code>-d</code> <i>outdir</i>] [<code>-Z</code> <i>timezone</i>] [<code>-h</code> <i>hostname</i>] <i>input_dir</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ganglia2pcp</code> is intended to read a set of ganglia files stored in the rrd format and translate them into a Performance Co-Pilot (<font SIZE="-1">PCP</font>) archive with the basename <i>outfile</i>. </p>
<p> The intent of this converter is to take all of the rrd files found in the input_dir and generate a single pcp archive file. The mapping of ganglia metrics to pcp metrics is defined internally. </p>
<p> The resultant <font SIZE="-1">PCP</font> achive may be used with all the <font SIZE="-1">PCP</font> client tools to graph subsets of the data using <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), perform data reduction and reporting, filter with the <font SIZE="-1">PCP</font> inference engine <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), etc. </p>
<p> A series of physical files will be created with the prefix <i>outfile</i>. These are <i>outfile</i><code>.0</code> (the performance data), <i>outfile</i><code>.meta</code> (the metadata that describes the performance data) and <i>outfile</i><code>.index</code> (a temporal index to improve efficiency of replay operations for the archive). If any of these files exists already, then <code>sar2pcp</code> will <code>not</code> overwrite them and will exit with an error message of the form </p>
<p> __pmLogNewFile: blah.0 already exists, not over-written </p>
<p> <code>ganglia2pcp</code> is a Perl script that uses the PCP::LogImport Perl wrapper around the <font SIZE="-1">PCP</font> <i>libpcp_import</i> library, and as such could be used as an example to develop new tools to import other types of performance data and create <font SIZE="-1">PCP</font> archives. The RRDs Perl wrapper is used to parse the raw rrd format files. </p>
<p> Options control the functioning of the converter.</p>
<dl>
<dt><code>-s</code></p>
<dd> The <i>start</i> argument specifies a start time in a format understood by str2time. The default start time is 24 prior to current time.</p>
<dt><code>-e</code></p>
<dd> The <i>end</i> argument specifies a end time in a format understood by str2time. The default start time is current time.</p>
<dt><code>-f</code></p>
<dd> The <i>outfile</i> argument specifies a output file name. The default name is in the standard pmlogger format based on the start time, eg 20150201.00.10</p>
<dt><code>-d</code></p>
<dd> The <i>outdir</i> argument specifies a output to write to. The default is the current directory</p>
<dt><code>-Z</code></p>
<dd> The <i>timezone</i> argument sets the source timezone in the <font SIZE="-1">PCP</font> archive (the default is to use the local timezone). The timezone must have the format +HHMM (for hours and minutes East of <font SIZE="-1">UTC</font>) or -HHMM (for hours and minutes West of <font SIZE="-1">UTC</font>) or <font SIZE="-1">UTC</font>. Note in particular that <code>neither</code> the <code>zoneinfo</code> (aka Olson) format, e.g. Europe/Paris, nor the Posix <font SIZE="-1"><code>TZ</code></font> format, e.g. <font SIZE="-1">EST+5</font> is allowed. Example: timezone=+1100.</p>
<dt><code>-h</code></p>
<dd> The <i>hostname</i> argument specifies a hostname to write to the archive. The default is taken from the directory name that the rrd files reside in.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogsummary/">pmlogsummary</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Date::Parse/">Date::Parse</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Date::Format/">Date::Format</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-PCP::LogImport/">PCP::LogImport</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-RRDs/">RRDs</a></code>(3pm) and <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3). </p>
<h2>Index</h2>
