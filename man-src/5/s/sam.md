---
title: "sam(5)"
name: "sam"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sam/"
description: "sam – Sequence Alignment/Map file format"
---

<p>sam &#8211; Sequence Alignment/Map file format</p>
<h2>Description</h2>
<p>Sequence Alignment/Map (SAM) format is TAB-delimited. Apart from the header lines, which are started with the `@&#8217; symbol, each alignment line consists of: </p>
<table>
<tr VALIGN=top>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>QNAME</code></td>
<td>Query template/pair NAME
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>FLAG</code></td>
<td>bitwise FLAG
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>RNAME</code></td>
<td>Reference sequence NAME
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>POS</code></td>
<td>1-based leftmost POSition/coordinate of clipped sequence
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>MAPQ</code></td>
<td>MAPping Quality (Phred-scaled)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>CIGAR</code></td>
<td>extended CIGAR string
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>MRNM</code></td>
<td>Mate Reference sequence NaMe (`=&#8217; if same as RNAME)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>MPOS</code></td>
<td>1-based Mate POSition
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>TLEN</code></td>
<td>inferred Template LENgth (insert size)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>SEQ</code></td>
<td>query SEQuence on the same strand as the reference
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>QUAL</code></td>
<td>query QUALity (ASCII-33 gives the Phred base quality)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>12+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>OPT</code></td>
<td>variable OPTional fields in the format TAG:VTYPE:VALUE
</td>
</tr>
</table>
<p> Each bit in the FLAG field is defined as: </p>
<table>
<tr VALIGN=top>
<td>0x0001</td>
<td ALIGN=center><code>p</code></td>
<td>the read is paired in sequencing
</td>
</tr>
<tr VALIGN=top>
<td>0x0002</td>
<td ALIGN=center><code>P</code></td>
<td>the read is mapped in a proper pair
</td>
</tr>
<tr VALIGN=top>
<td>0x0004</td>
<td ALIGN=center><code>u</code></td>
<td>the query sequence itself is unmapped
</td>
</tr>
<tr VALIGN=top>
<td>0x0008</td>
<td ALIGN=center><code>U</code></td>
<td>the mate is unmapped
</td>
</tr>
<tr VALIGN=top>
<td>0x0010</td>
<td ALIGN=center><code>r</code></td>
<td>strand of the query (1 for reverse)
</td>
</tr>
<tr VALIGN=top>
<td>0x0020</td>
<td ALIGN=center><code>R</code></td>
<td>strand of the mate
</td>
</tr>
<tr VALIGN=top>
<td>0x0040</td>
<td ALIGN=center><code>1</code></td>
<td>the read is the first read in a pair
</td>
</tr>
<tr VALIGN=top>
<td>0x0080</td>
<td ALIGN=center><code>2</code></td>
<td>the read is the second read in a pair
</td>
</tr>
<tr VALIGN=top>
<td>0x0100</td>
<td ALIGN=center><code>s</code></td>
<td>the alignment is not primary
</td>
</tr>
<tr VALIGN=top>
<td>0x0200</td>
<td ALIGN=center><code>f</code></td>
<td>the read fails platform/vendor quality checks
</td>
</tr>
<tr VALIGN=top>
<td>0x0400</td>
<td ALIGN=center><code>d</code></td>
<td>the read is either a PCR or an optical duplicate
</td>
</tr>
<tr VALIGN=top>
<td>0x0800</td>
<td ALIGN=center><code>S</code></td>
<td>the alignment is supplementary
</td>
</tr>
</table>
<p> where the second column gives the string representation of the FLAG field.</p>
<h2>See Also</h2>
<dl>
<dt><a rel="nofollow" href="https://github.com/samtools/hts-specs">https://github.com/samtools/hts-specs</a></p>
<dd>The full SAM/BAM file format specification </p>
