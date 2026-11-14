---
title: "sar2pcp(1)"
name: "sar2pcp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sar2pcp/"
description: "sar2pcp – import sar data and create a PCP archive"
---

<h2>NAME</h2>
<p> <code>sar2pcp</code> &#8211; import sar data and create a PCP archive</p>
<h2>SYNOPSIS</h2>
<p> <code>sar2pcp</code> <i>infile</i> <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>sar2pcp</code> is intended to read a binary System Activity Reporting (sar) data file as created by <code><a href="/docs/linux/man/1-sadc/">sadc</a></code>(1) (<i>infile</i>) and translate this into a Performance Co-Pilot (<font SIZE="-1">PCP</font>) archive with the basename <i>outfile</i>. </p>
<p> However, if <i>infile</i> has the suffix .xml, then it will be considered already in <font SIZE="-1">XML</font> format and <code>sar2pcp</code> will operate directly on it. </p>
<p> The resultant <font SIZE="-1">PCP</font> achive may be used with all the <font SIZE="-1">PCP</font> client tools to graph subsets of the data using <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), perform data reduction and reporting, filter with the <font SIZE="-1">PCP</font> inference engine <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), etc. </p>
<p> A series of physical files will be created with the prefix <i>outfile</i>. These are <i>outfile</i><code>.0</code> (the performance data), <i>outfile</i><code>.meta</code> (the metadata that describes the performance data) and <i>outfile</i><code>.index</code> (a temporal index to improve efficiency of replay operations for the archive). If any of these files exists already, then <code>sar2pcp</code> will <code>not</code> overwrite them and will exit with an error message of the form </p>
<p> __pmLogNewFile: blah.0 already exists, not over-written </p>
<p> <code>sar2pcp</code> is a Perl script that uses the PCP::LogImport Perl wrapper around the <font SIZE="-1">PCP</font> <i>libpcp_import</i> library, and as such could be used as an example to develop new tools to import other types of performance data and create <font SIZE="-1">PCP</font> archives. A Python wrapper module is also available.</p>
<h2>CAVEATS</h2>
<p> When not using the <font SIZE="-1">XML</font> input option, <code>sar2pcp</code> requires <i>infile</i> to have been created by a version of <code><a href="/docs/linux/man/1-sadc/">sadc</a></code>(1) from &lt;<a rel="nofollow" href="http://sebastien.godard.pagesperso-orange.fr/">http://sebastien.godard.pagesperso-orange.fr/</a>&gt; which includes the <code><a href="/docs/linux/man/1-sadf/">sadf</a></code>(1) utility to translate <i>infile</i> into an <font SIZE="-1">XML</font> stream (any since version 6); <code>sar2pcp</code> will automatically run <code><a href="/docs/linux/man/1-sadf/">sadf</a></code>(1) and translate the resultant <font SIZE="-1">XML</font> into a <font SIZE="-1">PCP</font> archive. </p>
<p> When using binary <code>sadc</code> files it is important to ensure the installed <code>sadf</code> is compatible with the version of <code>sadc</code> that originally generated the binary files. Simply assuming a newer installed version will work is unfortunately far too optimistic, and nor should one assume that binary data from different platforms (e.g. different endianness) will work &#8211; these issues are due to limitations in <code>sadc</code> and <code>sadf</code>, and not in <code>sar2pcp</code> itself. </p>
<p> Fortunately, the <code>sadf</code> message indicating that an incompatibility has been detected is consistent across versions, and is always prefixed </p>
<p> Invalid system activity file </p>
<p> Using an <font SIZE="-1">XML</font> <i>infile</i> has the advantage that the installed version of <code>sadf</code> is completely bypassed. <code>sar2pcp</code> undertakes to transform any valid <font SIZE="-1">XML</font> produced by any of the different variations of <code>sadf</code> into a valid <font SIZE="-1">PCP</font> archive. Any version of <font SIZE="-1">PCP</font> will be able to interpret the archive files produced by any version of <code>sar2pcp</code>, and you are also free to move the binary <font SIZE="-1">PCP</font> archive between different platforms, different hardware, even different operating systems &#8211; it Just Works (<font SIZE="-1">TM</font>).</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogsummary/">pmlogsummary</a></code>(1), <code><a href="/docs/linux/man/1-sadc/">sadc</a></code>(1), <code><a href="/docs/linux/man/1-sadf/">sadf</a></code>(1), <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Date::Parse/">Date::Parse</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Date::Format/">Date::Format</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-PCP::LogImport/">PCP::LogImport</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-XML::TokeParser/">XML::TokeParser</a></code>(3pm) and <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3). </p>
<h2>Index</h2>
