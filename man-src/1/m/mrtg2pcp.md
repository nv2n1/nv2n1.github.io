---
title: "mrtg2pcp(1)"
name: "mrtg2pcp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg2pcp/"
description: "mrtg2pcp – import MRTG data and create a PCP archive"
---

<h2>NAME</h2>
<p> <code>mrtg2pcp</code> &#8211; import MRTG data and create a PCP archive</p>
<h2>SYNOPSIS</h2>
<p> <code>mrtg2pcp</code> <i>hostname</i> <i>devname</i> <i>timezone</i> <i>infile</i> <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mrtg2pcp</code> is intended to read an <font SIZE="-1">MRTG</font> log file as created by <code><a href="/docs/linux/man/1-mrtg/">mrtg</a></code>(1) and translate this into a Performance Co-Pilot (<font SIZE="-1">PCP</font>) archive with the basename <i>outfile</i>. The <i>hostname</i>, <i>devname</i>, and <i>timezone</i> arguments specify information about the system for which the statistics were gathered. </p>
<p> The resultant <font SIZE="-1">PCP</font> achive may be used with all the <font SIZE="-1">PCP</font> client tools to graph subsets of the data using <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), perform data reduction and reporting, filter with the <font SIZE="-1">PCP</font> inference engine <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), etc. </p>
<p> A series of physical files will be created with the prefix <i>outfile</i>. These are <i>outfile</i><code>.0</code> (the performance data), <i>outfile</i><code>.meta</code> (the metadata that describes the performance data) and <i>outfile</i><code>.index</code> (a temporal index to improve efficiency of replay operations for the archive). If any of these files exists already, then <code>mrtg2pcp</code> will <code>not</code> overwrite them and will exit with an error message of the form </p>
<p> __pmLogNewFile: blah.0 already exists, not over-written </p>
<p> <code>mrtg2pcp</code> is a Perl script that uses the PCP::LogImport Perl wrapper around the <font SIZE="-1">PCP</font> <i>libpcp_import</i> library, and as such could be used as an example to develop new tools to import other types of performance data and create <font SIZE="-1">PCP</font> archives.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mrtg/">mrtg</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3) and <code><a href="//www.systutorials.com/docs/linux/man/3pm-PCP::LogImport/">PCP::LogImport</a></code>(3pm). </p>
<h2>Index</h2>
