---
title: "pcp-collectl(1)"
name: "pcp-collectl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-collectl/"
description: "pmcollectl, pcp-collectl – collect data that describes the current system status"
---

<h2>NAME</h2>
<p> <code>pmcollectl</code>, <code>pcp-collectl</code> &#8211; collect data that describes the current system status</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp collectl</code> [<code>-f</code> <i>file</i> | <code>-p</code> <i>file</i> &#8230;] <i>[options</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-collectl</code> is a system-level performance monitoring utility that records or displays specific operating system data for one or more sets of subsystems. Any of the subsystems (such as CPU, Disks, Memory or Sockets) can be included or excluded from data collection. Data can either be displayed immediately to a terminal, or stored in files for retrospective analysis. </p>
<p> <code>pcp-collectl</code> is a <code><a href="/docs/linux/man/1-python/">python</a></code>(1) script providing much of the functionality available from the <code><a href="/docs/linux/man/1-collectl/">collectl</a></code>(1) Linux utility (which happens to be written in <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1)). </p>
<p> It makes use of the Performance Co-Pilot (PCP) toolkit to simplify its implementation, as well as provide more of the <code>collectl</code> functionality on platforms other than Linux. </p>
<p> <code>pcp-collectl</code> has two primary modes of operation:</p>
<dl>
<dt>1.</p>
<dd> Record Mode (<code>-f</code> or <code>&#8211;filename</code> option) which reads data from a live system and writes output to a file or displays it on a terminal.</p>
<dt>2.</p>
<dd> Playback Mode (<code>-p</code> or <code>-a</code> option) which reads data from one or more PCP archive files and displays output on a terminal. Note that these files are <i>not</i> raw <code>collectl</code> format data, rather they are archives created by the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) utility (possibly indirectly, through use of the <code>-f</code> option to <code>pcp-collectl</code>).</dl>
<h2>RECORD MODE OPTIONS</h2>
<p> In this mode data is taken from a <code>live</code> system and either displayed on the terminal or written to a PCP archive. </p>
<p> <code>-h host</code></p>
<dl>
<dt>
<dd> Display metrics from <i>host</i> instead of displaying metrics from the local host.</dl>
<p> <code>-c, &#8211;count samples</code></p>
<dl>
<dt>
<dd> The number of samples to record.</dl>
<p> <code>-f, &#8211;filename filename</code></p>
<dl>
<dt>
<dd> This is the name of a PCP archive to write the output to.</dl>
<p> <code>-i, &#8211;interval interval</code></p>
<dl>
<dt>
<dd> This is the sampling interval in seconds. The default is 1 second.</dl>
<p> <code>-R, &#8211;runtime duration</code></p>
<dl>
<dt>
<dd> Specify the duration of data collection where the duration is a number followed by one of <code>wdhms,</code> indicating how many weeks, days, hours, minutes or seconds the collection is to be taken for.</dl>
<h2>PLAYBACK MODE OPTIONS</h2>
<p> In this mode, data is read from one or more PCP data files that were generated with the recording option, or indirectly via the <code>pmlogger</code> utility. </p>
<p> <code>-f, &#8211;filename filename</code></p>
<dl>
<dt>
<dd> If specified, this is the name of a PCP archive to write the output to (rather than the terminal).</dl>
<p> <code>-p, &#8211;playback filename</code></p>
<dl>
<dt>
<dd> Read data from the specified PCP archive folio files(s) &#8211; refer to <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1) for archive folio details.</dl>
<p> <code>-a, &#8211;archive filename</code></p>
<dl>
<dt>
<dd> Read data from the specified PCP raw archive files(s). The argument is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives.</dl>
<h2>COMMON OPTIONS</h2>
<p> The following options are supported in both record and playback modes. </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display standard help message.</dl>
<p> <code>-s, &#8211;subsys subsystem</code></p>
<dl>
<dt>
<dd> This field controls which subsystem data is to be collected or played back for. The rules for displaying results vary depending on the type of data to be displayed. If you write data for CPUs and DISKs to a raw file and play it back with -sc, you will only see CPU data. If you play it back with <code>-scm</code> you will still only see CPU data since memory data was not collected. To see the current set of default subsystems, which are a subset of this full list, use <code>-h</code>. </p>
<p> The default is &quot;cdn&quot;, which stands for CPU, Disk and Network summary data.</p>
<dl>
<dt><code>SUMMARY SUBSYSTEMS</code></p>
<dd></dl>
<p> c &#8211; CPU<br />
 d &#8211; Disk<br />
 f &#8211; NFS V3 Data<br />
 j &#8211; Interrupts<br />
 m &#8211; Memory<br />
 n &#8211; Networks</p>
<dl>
<dt>
<dd></dl>
<dl>
<dt><code>DETAIL SUBSYSTEMS</code></p>
<dd></dl>
<p> This is the set of <code>detail</code> data from which in most cases the corresponding summary data is derived. So, if one has 3 disks and chooses <code>-sd,</code> one will only see a single total taken across all 3 disks. If one chooses <code>-sD,</code> individual disk totals will be reported but no totals. </p>
<p> C &#8211; CPU<br />
 D &#8211; Disk<br />
 F &#8211; NFS Data<br />
 J &#8211; Interrupts<br />
 M &#8211; Memory node data, which is also known as NUMA data<br />
 N &#8211; Networks</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Display output in verbose mode. This often displays more data than in the default mode. When displaying detail data, verbose mode is forced. Furthermore, if summary data for a single subsystem is to be displayed in verbose mode, the headers are only repeated occasionally whereas if multiple subsystems are involved each needs their own header.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-collectl/">collectl</a></code>(1), <code><a href="/docs/linux/man/1-collectl2pcp/">collectl2pcp</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/1-python/">python</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), <code><a href="/docs/linux/man/1-pmprobe/">pmprobe</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), and <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<h2>Index</h2>
