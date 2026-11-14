---
title: "faidx(5)"
name: "faidx"
section: "5"
letter: "f"
url: "/docs/linux/man/5-faidx/"
description: "faidx – an index enabling random access to FASTA and FASTQ files"
---

<p>faidx &#8211; an index enabling random access to FASTA and FASTQ files</p>
<h2>Synopsis</h2>
<p><i>file.fa</i>.fai, <i>file.fasta</i>.fai, <i>file.fq</i>.fai, <i>file.fastq</i>.fai</p>
<h2>Description</h2>
<p>Using an <code>fai index</code> file in conjunction with a FASTA/FASTQ file containing reference sequences enables efficient access to arbitrary regions within those reference sequences. The index file typically has the same filename as the corresponding FASTA/FASTQ file, with <code>.fai</code> appended. </p>
<p> An <code>fai index</code> file is a text file consisting of lines each with five TAB-delimited columns for a FASTA file and six for FASTQ: </p>
<table>
<tr VALIGN=top>
<td><code>NAME</code></td>
<td>Name of this reference sequence
</td>
</tr>
<tr VALIGN=top>
<td><code>LENGTH</code></td>
<td>Total length of this reference sequence, in bases
</td>
</tr>
<tr VALIGN=top>
<td><code>OFFSET</code></td>
<td>Offset in the FASTA/FASTQ file of this sequence&#8217;s first base
</td>
</tr>
<tr VALIGN=top>
<td><code>LINEBASES</code></td>
<td>The number of bases on each line
</td>
</tr>
<tr VALIGN=top>
<td><code>LINEWIDTH</code></td>
<td>The number of bytes in each line, including the newline
</td>
</tr>
<tr VALIGN=top>
<td><code>QUALOFFSET</code></td>
<td>Offset of sequence&#8217;s first quality within the FASTQ file
</td>
</tr>
</table>
<p> The <code>NAME</code> and <code>LENGTH</code> columns contain the same data as would appear in the <code>SN</code> and <code>LN</code> fields of a SAM <code>@SQ</code> header for the same reference sequence. </p>
<p> The <code>OFFSET</code> column contains the offset within the FASTA/FASTQ file, in bytes starting from zero, of the first base of this reference sequence, i.e., of the character following the newline at the end of the header line (the &quot;<code>&gt;</code>&quot; line in FASTA, &quot;<code>@</code>&quot; in FASTQ). Typically the lines of a <code>fai index</code> file appear in the order in which the reference sequences appear in the FASTA/FASTQ file, so <code>.fai</code> files are typically sorted according to this column. </p>
<p> The <code>LINEBASES</code> column contains the number of bases in each of the sequence lines that form the body of this reference sequence, apart from the final line which may be shorter. The <code>LINEWIDTH</code> column contains the number of <i>bytes</i> in each of the sequence lines (except perhaps the final line), thus differing from <code>LINEBASES</code> in that it also counts the bytes forming the line terminator. </p>
<p> The <code>QUALOFFSET</code> works the same way as <code>OFFSET</code> but for the first quality score of this reference sequence. This would be the first character following the newline at the end of the &quot;<code>+</code>&quot; line. For FASTQ files only.</p>
<h3>FASTA Files</h3>
<p>In order to be indexed with <code>samtools faidx</code>, a FASTA file must be a text file of the form </p>
<dl>
<dd>&gt;<i>name</i> [<i>description</i>&#8230;]<br />
 ATGCATGCATGCATGCATGCATGCATGCAT<br />
 GCATGCATGCATGCATGCATGCATGCATGC<br />
 ATGCAT<br />
 &gt;<i>name</i> [<i>description</i>&#8230;]<br />
 ATGCATGCATGCAT<br />
 GCATGCATGCATGC<br />
 [&#8230;]</dl>
<p> In particular, each reference sequence must be &quot;well-formatted&quot;, i.e., all of its sequence lines must be the same length, apart from the final sequence line which may be shorter. (While this sequence line length must be the same within each sequence, it may vary between different reference sequences in the same FASTA file.) </p>
<p> This also means that although the FASTA file may have Unix- or Windows-style or other line termination, the newline characters present must be consistent, at least within each reference sequence. </p>
<p> The <code>samtools</code> implementation uses the first word of the &quot;<code>&gt;</code>&quot; header line text (i.e., up to the first whitespace character, having skipped any initial whitespace after the &quot;&gt;&quot;) as the <code>NAME</code> column.</p>
<h3>FASTQ Files</h3>
<p>FASTQ files for indexing work in the same way as the FASTA files. </p>
<dl>
<dd>@<i>name</i> [<i>description&#8230;]</i><br />
 ATGCATGCATGCATGCATGCATGCATGCAT<br />
 GCATGCATGCATGCATGCATGCATGCATGC<br />
 ATGCAT<br />
 +<br />
 FFFA@@FFFFFFFFFFHHB:::@BFFFFGG<br />
 HIHIIIIIIIIIIIIIIIIIIIIIIIFFFF<br />
 8011&lt;&lt;<br />
 @<i>name</i> [<i>description&#8230;]</i><br />
 ATGCATGCATGCAT<br />
 GCATGCATGCATGC<br />
 +<br />
 IIA94445EEII==<br />
 =&gt;IIIIIIIIICCC<br />
 [&#8230;]</dl>
<p> Quality lines must be wrapped at the same length as the corresponding sequence lines.</p>
<h2>Example</h2>
<p>For example, given this FASTA file </p>
<dl>
<dd>&gt;one<br />
 ATGCATGCATGCATGCATGCATGCATGCAT<br />
 GCATGCATGCATGCATGCATGCATGCATGC<br />
 ATGCAT<br />
 &gt;two another chromosome<br />
 ATGCATGCATGCAT<br />
 GCATGCATGCATGC
</dl>
<p> formatted with Unix-style (LF) line termination, the corresponding fai index would be</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>one</td>
<td ALIGN=right>66&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>30&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td>two</td>
<td ALIGN=right>28&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>98&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
<p> If the FASTA file were formatted with Windows-style (CR-LF) line termination, the fai index would be</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>one</td>
<td ALIGN=right>66&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>30&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td>two</td>
<td ALIGN=right>28&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>103&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
<p> An example FASTQ file </p>
<dl>
<dd>@fastq1<br />
 ATGCATGCATGCATGCATGCATGCATGCAT<br />
 GCATGCATGCATGCATGCATGCATGCATGC<br />
 ATGCAT<br />
 +<br />
 FFFA@@FFFFFFFFFFHHB:::@BFFFFGG<br />
 HIHIIIIIIIIIIIIIIIIIIIIIIIFFFF<br />
 8011&lt;&lt;<br />
 @fastq2<br />
 ATGCATGCATGCAT<br />
 GCATGCATGCATGC<br />
 +<br />
 IIA94445EEII==<br />
 =&gt;IIIIIIIIICCC
</dl>
<p> Formatted with Unix-style line termination would give this fai index</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>fastq1</td>
<td ALIGN=right>66&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>30&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>79&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
<tr VALIGN=top>
<td>fastq2</td>
<td ALIGN=right>28&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>156&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td ALIGN=right>188&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;
</td>
</tr>
</table>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-samtools/">samtools</a></i>(1)</p>
<dl>
<dt><a rel="nofollow" href="https://en.wikipedia.org/wiki/FASTA_format">https://en.wikipedia.org/wiki/FASTA_format</a></p>
<dd>
<dt><a rel="nofollow" href="https://en.wikipedia.org/wiki/FASTQ_format">https://en.wikipedia.org/wiki/FASTQ_format</a></p>
<dd>Further description of the FASTA and FASTQ formats </p>
