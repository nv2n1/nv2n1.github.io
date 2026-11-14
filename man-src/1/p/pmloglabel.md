---
title: "pmloglabel(1)"
name: "pmloglabel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmloglabel/"
description: "pmloglabel – check and repair a performance metrics archive label"
---

<h2>NAME</h2>
<p> <code>pmloglabel</code> &#8211; check and repair a performance metrics archive label</p>
<h2>SYNOPSIS</h2>
<p> <code>pmloglabel</code> [<code>-Llsv</code>] [<code>-h</code> <i>hostname</i>] [<code>-p</code> <i>pid</i>] [<code>-V</code> <i>version</i>] [<code>-Z</code> <i>timezone</i>] <i>archive</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmloglabel</code> verifies, reports on, and can modify all details of the labels in each of the files of a Performance Co-Pilot (PCP) archive log. The archive log has the base name <i>archive</i> and must have been previously created using <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> Each of the files in a PCP archive (metadata, temporal index, and one or more data volumes) must contain a valid label at the start, else the PCP tools will refuse to open the archive at all. </p>
<p> Thus, the primary function of <code>pmloglabel</code> is to be able to repair any inconsistent or corrupt label fields, such that the entire archive is not lost. It will not check the remainder of the archive, but it will give you a fighting chance to recover otherwise lost data. Together, <code>pmloglabel</code> and <code>pmlogextract</code> are able to produce a valid PCP archive from many forms of corruption. </p>
<p> Note that if the temporal index is found to be corrupt, the &quot;*.index&quot; file can be safely moved aside and the archive will still be accessible, however retrievals may take longer without the index. </p>
<p> The options control the specific information to be reported, or the specific fields to be modified:</p>
<dl>
<dt><code>-h</code></p>
<dd> Modify the logged <i>hostname</i> in the archive label, for all files in the archive.</p>
<dt><code>-l</code></p>
<dd> Dump out the archive label, showing the log format version, the time and date for the start and (current) end of the archive, and the host from which the performance metrics values were collected.</p>
<dt><code>-L</code></p>
<dd> Like <code>-l</code>, just a little more verbose, showing also the timezone and creator process identifier from the archive label.</p>
<dt><code>-p</code></p>
<dd> Set the process identifier stored in the archive label to <i>pid</i>, for all files in the archive.</p>
<dt><code>-s</code></p>
<dd> Rewrite the sentinel values which precede and follow the archive label, for all files in the archive.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Additional progress information is produced at each step.</p>
<dt><code>-V</code></p>
<dd> Stamp the <i>version</i> number into the magic number field at the start of the archive label, for all files in the archive.</p>
<dt><code>-Z</code></p>
<dd> Changes the timezone in the archive labels to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</dl>
<h2>EXAMPLES</h2>
<p> The following demonstrates the use of <code>pmloglabel</code> in finding and then correcting a corrupt field (PID) in the label of the temporal index of an archive named &quot;20080125&quot;. </p>
<pre>
$ pmdumplog -l 20080125
pmdumplog: Cannot open archive &quot;20080125&quot;: Illegal label record at start of a PCP archive log file
$ pmloglabel 20080125
Mismatched PID (5264/5011) between temporal index and data volume 0
$ pmloglabel -p 5264 20080125
$ pmdumplog -l 20080125
Log Label (Log Format Version 2)
Performance metrics from host fw1
  commencing Fri Jan 25 00:10:09.341 2008
  ending     Sat Jan 26 00:09:54.344 2008
</pre>
<h2>EXIT STATUS</h2>
<p> <code>pmloglabel</code> exits with status 0 if the archive labels are clean. If invoked incorrectly, the exit status will be 1. If corruption is detected and still exists at the end, the exit status will be 2. If requested to write out the archive labels, and some aspect of that write out fails, then the exit status will be 3.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i></p>
<dd> Default directory for PCP archives containing performance metric values collected from the host <i>hostname</i>.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmlogcheck/">pmlogcheck</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_daily/">pmlogger_daily</a></code>(1), <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
