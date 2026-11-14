---
title: "iostat2pcp(1)"
name: "iostat2pcp"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iostat2pcp/"
description: "iostat2pcp – import iostat data and create a PCP archive"
---

<h2>NAME</h2>
<p> <code>iostat2pcp</code> &#8211; import iostat data and create a PCP archive</p>
<h2>SYNOPSIS</h2>
<p> <code>iostat2pcp</code> [<code>-v</code>] [<code>-S</code> <i>start</i>] [<code>-t</code> <i>interval</i>] [<code>-Z</code> <i>timezone</i>] <i>infile</i> <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>iostat2pcp</code> reads a text file created with <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1) (<i>infile</i>) and translates this into a Performance Co-Pilot (<font SIZE="-1">PCP</font>) archive with the basename <i>outfile</i>. If <i>infile</i> is &#8211; then <i>iostat2pcp</i> reads from standard input, allowing easy preprocessing of the <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1) output with <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) or similar. </p>
<p> The resultant <font SIZE="-1">PCP</font> archive may be used with all the <font SIZE="-1">PCP</font> client tools to graph subsets of the data using <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), perform data reduction and reporting, filter with the <font SIZE="-1">PCP</font> inference engine <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), etc. </p>
<p> A series of physical files will be created with the prefix <i>outfile</i>. These are <i>outfile</i><code>.0</code> (the performance data), <i>outfile</i><code>.meta</code> (the metadata that describes the performance data) and <i>outfile</i><code>.index</code> (a temporal index to improve efficiency of replay operations for the archive). If any of these files exists already, then <code>iostat2pcp</code> will <code>not</code> overwrite them and will exit with an error message. </p>
<p> The first output sample from <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1) contains a statistical summary since boot time and is ignored by <i>iostat2pcp</i>, so the first real data set is the second one in the <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1) output. </p>
<p> The best results are obtained when <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1) was run with its own <code>-t</code> flag, so each output sample is prefixed with a timestamp. Even better is <code>-t</code> with $<code>S_TIME_FORMAT=ISO</code> set in environment when <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1) is run, in which case the timestamp includes the timezone. </p>
<p> Note that if $<code>S_TIME_FORMAT=ISO</code> is <code>not</code> used with the <code>-t</code> option then <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1) may produce a timestamp controlled by <font SIZE="-1"><code>LC_TIME</code></font> from the locale that is in a format <i>iostat2pcp</i> cannot parse. The formats for the timestamp that <i>iostat2pcp</i> accepts are illustrated by these examples:</p>
<dl>
<dt><code>2013-07-06T21:34:39+1000</code></p>
<dd> (for the $<code>S_TIME_FORMAT=ISO</code>).</p>
<dt><code>2013-07-06 21:34:39</code></p>
<dd> (for some of the European formats, e.g. de_AT, de_BE, de_LU and en_DK.utf8).</p>
<dt><code>06/07/13 21:34:39</code></p>
<dd> (for all of the $<font SIZE="-1"><code>LC_TIME</code></font> settings for English locales outside North America, e.g. en_AU, en_GB, en_IE, en_NZ, en_SG and en_ZA, and all the Spanish locales, e.g. es_ES, es_MX and es_AR).</dl>
<p> In particular, note that some common North American $<font SIZE="-1"><code>LC_TIME</code></font> settings will <code>not</code> work with <i>iostat2pcp</i> (namely, en_US, <font SIZE="-1">POSIX</font> and C) because they use the <font SIZE="-1">MM/DD</font> format which may be incorrectly converted with the assumed <font SIZE="-1">DD/MM</font> format. This is another reason to recommend setting $<code>S_TIME_FORMAT=ISO</code>. </p>
<p> If there are no timestamps in the input stream, <i>iostat2pcp</i> will try and deduce the sample interval if basic Disk data (<code>-d</code> option for <i><a href="/docs/linux/man/1-iostat/">iostat</a></i>(1)) is found. If this fails, then the <code>-t</code> option may be used to specify the sample <i>interval</i> in seconds. This option is ignored if timestamps are found in the input stream. </p>
<p> The <code>-S</code> option may be used to specify as start time for the first real sample in <i>infile</i>, where <i>start</i> must have the format <font SIZE="-1">HH:MM:SS</font>. This option is ignored if timestamps are found in the input stream. </p>
<p> The <code>-Z</code> option may be used to specify a timezone. It must have the format +HHMM (for hours and minutes East of <font SIZE="-1">UTC</font>) or -HHMM (for hours and minutes West of <font SIZE="-1">UTC</font>). Note in particular that <code>neither</code> the <code>zoneinfo</code> (aka Olson) format, e.g. Europe/Paris, nor the Posix <font SIZE="-1"><code>TZ</code></font> format, e.g. <font SIZE="-1">EST+5</font> is allowed for the <code>-Z</code> option. This option is ignored if <font SIZE="-1">ISO</font> timestamps are found in the input stream. If the timezone is not specified and cannot be deduced, it defaults to <font SIZE="-1">UTC</font>. </p>
<p> Some additional diagnostic output is generated with the <code>-v</code> option. </p>
<p> <code>iostat2pcp</code> is a Perl script that uses the PCP::LogImport Perl wrapper around the <font SIZE="-1">PCP</font> <i>libpcp_import</i> library, and as such could be used as an example to develop new tools to import other types of performance data and create <font SIZE="-1">PCP</font> archives.</p>
<h2>CAVEAT</h2>
<p> <code>iostat2pcp</code> requires <i>infile</i> to have been created by the version of <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1) from &lt;<a rel="nofollow" href="http://freshmeat.net/projects/sysstat">http://freshmeat.net/projects/sysstat</a>&gt;. </p>
<p> <code>iostat2pcp</code> handles the <code>-c</code> (<font SIZE="-1">CPU</font>), <code>-d</code> (Disk), <code>-x</code> (eXtended Disk) and <code>-p</code> (Partition) report formats (including their <code>-k</code>, <code>-m</code>, <code>-z</code> and <font SIZE="-1"><code>ALL</code></font> variants), but does not accommodate the <code>-n</code> (Network Filesystem) report format from <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1); this is a demand-driven limitation rather than a technical limitation.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Date::Format/">Date::Format</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Date::Parse/">Date::Parse</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-PCP::LogImport/">PCP::LogImport</a></code>(3pm) and <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3). </p>
<h2>Index</h2>
