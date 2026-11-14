---
title: "htsfile(1)"
name: "htsfile"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htsfile/"
description: "htsfile – identify high-throughput sequencing data files"
---

<h2 class="name">NAME</h2>
<p> htsfile &#8211; identify high-throughput sequencing data files </p>
<h2>SYNOPSIS</h2>
<p> <code>htsfile</code> [<code>-chHv</code>] <i>FILE</i>&#8230;<br />
 <code>htsfile &#8211;copy</code> [<code>-v</code>] <i>FILE DESTFILE</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>htsfile</code> utility attempts to identify what kind of high-throughput sequencing data files the specified files are, and provides minimal viewing capabilities for some kinds of data file. </p>
<p> It can identify sequencing data files such as SAM, BAM, and CRAM; variant calling data files such as VCF and BCF; index files used to index these data files; and compressed versions of many of them. </p>
<p> For each <i>FILE</i> given, <code>htsfile</code> prints a description of the file format determined, using similar keyword conventions to <code><a href="/docs/linux/man/1-file/">file</a></code>(1): &quot;text&quot; indicates a textual file that can probably be viewed on a terminal; &quot;data&quot; indicates binary data; &quot;sequence&quot;, &quot;variant calling&quot;, and &quot;index&quot; indicate different categories of data file. When it can be identified, the name of the particular file format (such as &quot;BAM&quot; or &quot;VCF&quot;) is printed at the start of the description. </p>
<p> When used to view file contents as text, <code>htsfile</code> can optionally show only headers or only data records, but has no other filtering capabilities. Use <code>samtools</code> or <code>bcftools</code> if you need more extensive viewing or filtering capabilities. </p>
<p> Alternatively, when <code>&#8211;copy</code> is used, <code>htsfile</code> takes exactly two arguments and performs a byte-for-byte copy from <i>FILE</i> to <i>DESTFILE</i>. This is similar to <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1), but HTSlib&#8217;s remote file access facilities are available for both source and destination. </p>
<p> The following options are accepted:</p>
<dl>
<dt><code>-c</code>, <code>&#8211;view</code></p>
<dd> Instead of identifying the specified files, display a textual representation of their contents on standard output.</p>
<dt>
<dd> By default, <code>&#8211;view</code> refuses to display files in unknown formats. When <code>&#8211;verbose</code> is also given, the raw contents of such files are displayed, with non-printable characters shown via C-style &quot;
