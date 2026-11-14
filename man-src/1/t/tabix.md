---
title: "tabix(1)"
name: "tabix"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tabix/"
description: "tabix – Generic indexer for TAB-delimited genome position files"
---

<h2 class="name">NAME</h2>
<p> tabix &#8211; Generic indexer for TAB-delimited genome position files </p>
<h2>SYNOPSIS</h2>
<p> <code>tabix</code> [<code>-0lf</code>] [<code>-p</code> gff|bed|sam|vcf] [<code>-s</code> <i>seqCol</i>] [<code>-b</code> <i>begCol</i>] [<code>-e</code> <i>endCol</i>] [<code>-S</code> <i>lineSkip</i>] [<code>-c</code> <i>metaChar</i>] <i>in.tab.bgz</i> [<i>region1 </i>[<i>region2 </i>[<i>&#8230;</i>]]] </p>
<h2>DESCRIPTION</h2>
<p> Tabix indexes a TAB-delimited genome position file <i>in.tab.bgz</i> and creates an index file (<i>in.tab.bgz.tbi</i> or <i>in.tab.bgz.csi</i>) when <i>region</i> is absent from the command-line. The input data file must be position sorted and compressed by <code>bgzip</code> which has a <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) like interface. </p>
<p> After indexing, tabix is able to quickly retrieve data lines overlapping <i>regions</i> specified in the format &quot;chr:beginPos-endPos&quot;. (Coordinates specified in this region format are 1-based and inclusive.) </p>
<p> Fast data retrieval also works over network if URI is given as a file name and in this case the index file will be downloaded if it is not present locally. </p>
<p> The tabix (<i>.tbi</i>) and BAI index formats can handle individual chromosomes up to 512 Mbp (2^29 bases) in length. If your input file might contain data lines with begin or end positions greater than that, you will need to use a CSI index. </p>
<h2>INDEXING OPTIONS</h2>
<dl>
<dt><code>-0, &#8211;zero-based</code></p>
<dd> Specify that the position in the data file is 0-based half-open (e.g. UCSC files) rather than 1-based.</p>
<dt><code>-b, &#8211;begin </code><i>INT</i></p>
<dd> Column of start chromosomal position. [4]</p>
<dt><code>-c, &#8211;comment </code><i>CHAR</i></p>
<dd> Skip lines started with character CHAR. [#]</p>
<dt><code>-C, &#8211;csi</code></p>
<dd> Produce CSI format index instead of classical tabix or BAI style indices.</p>
<dt><code>-e, &#8211;end </code><i>INT</i></p>
<dd> Column of end chromosomal position. The end column can be the same as the start column. [5]</p>
<dt><code>-f, &#8211;force </code></p>
<dd> Force to overwrite the index file if it is present.</p>
<dt><code>-m, &#8211;min-shift </code><i>INT</i></p>
<dd> Set minimal interval size for CSI indices to 2^INT [14]</p>
<dt><code>-p, &#8211;preset </code><i>STR</i></p>
<dd> Input format for indexing. Valid values are: gff, bed, sam, vcf. This option should not be applied together with any of <code>-s</code>, <code>-b</code>, <code>-e</code>, <code>-c</code> and <code>-0</code>; it is not used for data retrieval because this setting is stored in the index file. [gff]</p>
<dt><code>-s, &#8211;sequence </code><i>INT</i></p>
<dd> Column of sequence name. Option <code>-s</code>, <code>-b</code>, <code>-e</code>, <code>-S</code>, <code>-c</code> and <code>-0</code> are all stored in the index file and thus not used in data retrieval. [1]</p>
<dt><code>-S, &#8211;skip-lines </code><i>INT</i></p>
<dd> Skip first INT lines in the data file. [0] </p>
</dl>
<h2>QUERYING AND OTHER OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;print-header </code></p>
<dd> Print also the header/meta lines.</p>
<dt><code>-H, &#8211;only-header </code></p>
<dd> Print only the header/meta lines.</p>
<dt><code>-l, &#8211;list-chroms </code></p>
<dd> List the sequence names stored in the index file.</p>
<dt><code>-r, &#8211;reheader </code><i>FILE</i></p>
<dd> Replace the header with the content of FILE</p>
<dt><code>-R, &#8211;regions </code><i>FILE</i></p>
<dd> Restrict to regions listed in the FILE. The FILE can be BED file (requires .bed, .bed.gz, .bed.bgz file name extension) or a TAB-delimited file with CHROM, POS, and, optionally, POS_TO columns, where positions are 1-based and inclusive. When this option is in use, the input file may not be sorted.</p>
<dt><code>-T, &#8211;targets </code><i>FILE</i></p>
<dd> Similar to <code>-R</code> but the entire input will be read sequentially and regions not listed in FILE will be skipped.</p>
<dt><code>-D </code></p>
<dd> Do not download the index file before opening it. Valid for remote files only.</p>
<dt><code>&#8211;cache </code><i>INT</i></p>
<dd> Set the BGZF block cache size to INT megabytes. [10] </p>
<p> This is of most benefit when the <code>-R</code> option is used, which can cause blocks to be read more than once. Setting the size to 0 will disable the cache.</p>
<dt><code>&#8211;separate-regions</code></p>
<dd> This option can be used when multiple regions are supplied in the command line and the user needs to quickly see which file records belong to which region. For this, a line with the name of the region, preceded by the file specific comment symbol, is inserted in the output before its corresponding group of records.</p>
<dt><code>&#8211;verbosity </code><i>INT</i></p>
<dd> Set verbosity of logging messages printed to stderr. The default is 3, which turns on error and warning messages; 2 reduces warning messages; 1 prints only error messages and 0 is mostly silent. Values higher than 3 produce additional informational and debugging messages.</dl>
<h2>EXAMPLE</h2>
<p> (grep &quot;^#&quot; in.gff; grep -v &quot;^#&quot; in.gff | sort -t&quot;`printf &#8216;	&#8217;`&quot; -k1,1 -k4,4n) | bgzip &gt; sorted.gff.gz; </p>
<p> tabix -p gff sorted.gff.gz; </p>
<p> tabix sorted.gff.gz chr1:10,000,000-20,000,000; </p>
<h2>NOTES</h2>
<p> It is straightforward to achieve overlap queries using the standard B-tree index (with or without binning) implemented in all SQL databases, or the R-tree index in PostgreSQL and Oracle. But there are still many reasons to use tabix. Firstly, tabix directly works with a lot of widely used TAB-delimited formats such as GFF/GTF and BED. We do not need to design database schema or specialized binary formats. Data do not need to be duplicated in different formats, either. Secondly, tabix works on compressed data files while most SQL databases do not. The GenCode annotation GTF can be compressed down to 4%. Thirdly, tabix is fast. The same indexing algorithm is known to work efficiently for an alignment with a few billion short reads. SQL databases probably cannot easily handle data at this scale. Last but not the least, tabix supports remote data retrieval. One can put the data file and the index at an FTP or HTTP server, and other users or even web services will be able to get a slice without downloading the entire file. </p>
<h2>AUTHOR</h2>
<p> Tabix was written by Heng Li. The BGZF library was originally implemented by Bob Handsaker and modified by Heng Li for remote file access and in-memory caching. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bgzip/">bgzip</a></i>(1), <i><a href="/docs/linux/man/1-samtools/">samtools</a></i>(1) </p>
<h2>Index</h2>
