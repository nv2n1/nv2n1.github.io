---
title: "collectl2pcp(1)"
name: "collectl2pcp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collectl2pcp/"
description: "collectl2pcp – import collectl data to a PCP archive"
---

<h2>NAME</h2>
<p> <code>collectl2pcp</code> &#8211; import collectl data to a PCP archive</p>
<h2>SYNOPSIS</h2>
<p> <code>collectl2pcp</code> [<code>-F</code>] [<code>-v</code>] [<code>-?</code>] <i>file</i> [<i>file</i> &#8230;] <i>archive</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>collectl2pcp</code> reads raw <code><a href="/docs/linux/man/1-collectl/">collectl</a></code>(1) data from each <i>file</i> and creates a new PCP archive with basename <i>archive</i>. Each input <i>file</i> may be gzipped (with <code>.gz</code> suffix). The PCP <i>archive</i> and at least one input <i>file</i> are required arguments. </p>
<p> The options to <code>collectl2pcp</code> are as follows.</p>
<dl>
<dt><code>-F</code></p>
<dd> Overwrite <i>archive</i> (and the index and meta files) if it already exists.</p>
<dt><code>-v</code></p>
<dd> Report progress and errors verbosely. This also reports a count of unsupported metric data in the <code><a href="/docs/linux/man/1-collectl/">collectl</a></code>(1) input file(s), which is normally silently skipped.</p>
<dt><i>file</i> [<i>file</i> &#8230;]</p>
<dd> These are the <code><a href="/docs/linux/man/1-collectl/">collectl</a></code>(1) input files. If more than one is given, they must contain data for the same host and be given in time-stamp chronological order on the command line. Note that when <code><a href="/docs/linux/man/1-collectl/">collectl</a></code>(1) is run as a service, it normally creates files with date based names that will sort chronologically (e.g. <code>/var/log/collectl/*.gz</code> will be sorted correctly).</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-collectl/">collectl</a></code>(1), <code><a href="/docs/linux/man/1-pmcollectl/">pmcollectl</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
