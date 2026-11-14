---
title: "bwa(1)"
name: "bwa"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bwa/"
description: "bwa – Burrows-Wheeler Alignment Tool"
---

<h2>NAME</h2>
<p> bwa &#8211; Burrows-Wheeler Alignment Tool</p>
<h2>SYNOPSIS</h2>
<p> bwa index ref.fa </p>
<p> bwa mem ref.fa reads.fq &gt; aln-se.sam </p>
<p> bwa mem ref.fa read1.fq read2.fq &gt; aln-pe.sam </p>
<p> bwa aln ref.fa short_read.fq &gt; aln_sa.sai </p>
<p> bwa samse ref.fa aln_sa.sai short_read.fq &gt; aln-se.sam </p>
<p> bwa sampe ref.fa aln_sa1.sai aln_sa2.sai read1.fq read2.fq &gt; aln-pe.sam </p>
<p> bwa bwasw ref.fa long_read.fq &gt; aln.sam </p>
<h2>DESCRIPTION</h2>
<p> BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to 1Mbp. BWA-MEM and BWA-SW share similar features such as long-read support and split alignment, but BWA-MEM, which is the latest, is generally recommended for high-quality queries as it is faster and more accurate. BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads. </p>
<p> For all the algorithms, BWA first needs to construct the FM-index for the reference genome (the <code>index</code> command). Alignment algorithms are invoked with different sub-commands: <code>aln</code>/<code>samse</code>/<code>sampe</code> for BWA-backtrack, <code>bwasw</code> for BWA-SW and <code>mem</code> for the BWA-MEM algorithm. </p>
<h2>COMMANDS AND OPTIONS</h2>
<dl>
<dt><code>index</code></p>
<dd> <code>bwa index</code> [<code>-p</code> <i>prefix</i>] [<code>-a</code> <i>algoType</i>] <i>db.fa</i> </p>
<p> Index database sequences in the FASTA format. </p>
<p> <code>OPTIONS:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-p</code><i>&nbsp;<wbr>STR</i></p>
<dd> Prefix of the output database [same as db filename]</p>
<dt><code>-a</code><i>&nbsp;<wbr>STR</i></p>
<dd> Algorithm for constructing BWT index. BWA implements two algorithms for BWT construction: <code>is</code> and <code>bwtsw</code>. The first algorithm is a little faster for small database but requires large RAM and does not work for databases with total length longer than 2GB. The second algorithm is adapted from the BWT-SW source code. It in theory works with database with trillions of bases. When this option is not specified, the appropriate algorithm will be chosen automatically.</dl>
</dl>
<dt><code>mem</code></p>
<dd> <code>bwa mem</code> [<code>-aCHjMpP</code>] [<code>-t</code> <i>nThreads</i>] [<code>-k</code> <i>minSeedLen</i>] [<code>-w</code> <i>bandWidth</i>] [<code>-d</code> <i>zDropoff</i>] [<code>-r</code> <i>seedSplitRatio</i>] [<code>-c</code> <i>maxOcc</i>] [<code>-D</code> <i>chainShadow</i>] [<code>-m</code> <i>maxMateSW</i>] [<code>-W</code> <i>minSeedMatch</i>] [<code>-A</code> <i>matchScore</i>] [<code>-B</code> <i>mmPenalty</i>] [<code>-O</code> <i>gapOpenPen</i>] [<code>-E</code> <i>gapExtPen</i>] [<code>-L</code> <i>clipPen</i>] [<code>-U</code> <i>unpairPen</i>] [<code>-R</code> <i>RGline</i>] [<code>-H</code> <i>HDlines</i>] [<code>-v</code> <i>verboseLevel</i>] <i>db.prefix</i> <i>reads.fq</i> [<i>mates.fq</i>] </p>
<p> Align 70bp-1Mbp query sequences with the BWA-MEM algorithm. Briefly, the algorithm works by seeding alignments with maximal exact matches (MEMs) and then extending seeds with the affine-gap Smith-Waterman algorithm (SW). </p>
<p> If <i>mates.fq</i> file is absent and option <code>-p</code> is not set, this command regards input reads are single-end. If <i>mates.fq</i> is present, this command assumes the <i>i</i>-th read in <i>reads.fq</i> and the <i>i</i>-th read in <i>mates.fq</i> constitute a read pair. If <code>-p</code> is used, the command assumes the 2<i>i</i>-th and the (2<i>i</i>+1)-th read in <i>reads.fq</i> constitute a read pair (such input file is said to be interleaved). In this case, <i>mates.fq</i> is ignored. In the paired-end mode, the <code>mem</code> command will infer the read orientation and the insert size distribution from a batch of reads. </p>
<p> The BWA-MEM algorithm performs local alignment. It may produce multiple primary alignments for different part of a query sequence. This is a crucial feature for long sequences. However, some tools such as Picard&#8217;s markDuplicates does not work with split alignments. One may consider to use option <code>-M</code> to flag shorter split hits as secondary. </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ALGORITHM OPTIONS:</code></p>
<dd>
<dt><code>-t</code><i>&nbsp;<wbr>INT</i></p>
<dd> Number of threads [1]</p>
<dt><code>-k</code><i>&nbsp;<wbr>INT</i></p>
<dd> Minimum seed length. Matches shorter than <i>INT</i> will be missed. The alignment speed is usually insensitive to this value unless it significantly deviates from 20. [19]</p>
<dt><code>-w</code><i>&nbsp;<wbr>INT</i></p>
<dd> Band width. Essentially, gaps longer than <i>INT</i> will not be found. Note that the maximum gap length is also affected by the scoring matrix and the hit length, not solely determined by this option. [100]</p>
<dt><code>-d</code><i>&nbsp;<wbr>INT</i></p>
<dd> Off-diagonal X-dropoff (Z-dropoff). Stop extension when the difference between the best and the current extension score is above |<i>i</i>&#8211;<i>j</i>|*<i>A</i>+<i>INT</i>, where <i>i</i> and <i>j</i> are the current positions of the query and reference, respectively, and <i>A</i> is the matching score. Z-dropoff is similar to BLAST&#8217;s X-dropoff except that it doesn&#8217;t penalize gaps in one of the sequences in the alignment. Z-dropoff not only avoids unnecessary extension, but also reduces poor alignments inside a long good alignment. [100]</p>
<dt><code>-r</code><i>&nbsp;<wbr>FLOAT</i></p>
<dd> Trigger re-seeding for a MEM longer than <i>minSeedLen</i>*<i>FLOAT</i>. This is a key heuristic parameter for tuning the performance. Larger value yields fewer seeds, which leads to faster alignment speed but lower accuracy. [1.5]</p>
<dt><code>-c</code><i>&nbsp;<wbr>INT</i></p>
<dd> Discard a MEM if it has more than <i>INT</i> occurence in the genome. This is an insensitive parameter. [500]</p>
<dt><code>-D</code><i>&nbsp;<wbr>INT</i></p>
<dd> Drop chains shorter than <i>FLOAT</i> fraction of the longest overlapping chain [0.5]</p>
<dt><code>-m</code><i>&nbsp;<wbr>INT</i></p>
<dd> Perform at most <i>INT</i> rounds of mate-SW [50]</p>
<dt><code>-W</code><i>&nbsp;<wbr>INT</i></p>
<dd> Drop a chain if the number of bases in seeds is smaller than <i>INT</i>. This option is primarily used for longer contigs/reads. When positive, it also affects seed filtering. [0]</p>
<dt><code>-P</code></p>
<dd> In the paired-end mode, perform SW to rescue missing hits only but do not try to find hits that fit a proper pair. </p>
<dt><code>SCORING OPTIONS:</code></p>
<dd>
<dt><code>-A</code><i>&nbsp;<wbr>INT</i></p>
<dd> Matching score. [1]</p>
<dt><code>-B</code><i>&nbsp;<wbr>INT</i></p>
<dd> Mismatch penalty. The sequence error rate is approximately: {.75 * exp[<a href="/docs/linux/man/4--log/">-log</a>(4) * B/A]}. [4]</p>
<dt><code>-O</code><i>&nbsp;<wbr>INT[,INT]</i></p>
<dd> Gap open penalty. If two numbers are specified, the first is the penalty of openning a deletion and the second for openning an insertion. [6]</p>
<dt><code>-E</code><i>&nbsp;<wbr>INT[,INT]</i></p>
<dd> Gap extension penalty. If two numbers are specified, the first is the penalty of extending a deletion and second for extending an insertion. A gap of length k costs O + k*E (i.e. <code>-O</code> is for opening a zero-length gap). [1]</p>
<dt><code>-L</code><i>&nbsp;<wbr>INT[,INT]</i></p>
<dd> Clipping penalty. When performing SW extension, BWA-MEM keeps track of the best score reaching the end of query. If this score is larger than the best SW score minus the clipping penalty, clipping will not be applied. Note that in this case, the SAM AS tag reports the best SW score; clipping penalty is not deduced. If two numbers are provided, the first is for 5&#8242;-end clipping and second for 3&#8242;-end clipping. [5]</p>
<dt><code>-U</code><i>&nbsp;<wbr>INT</i></p>
<dd> Penalty for an unpaired read pair. BWA-MEM scores an unpaired read pair as scoreRead1+scoreRead2-<i>INT</i> and scores a paired as scoreRead1+scoreRead2-insertPenalty. It compares these two scores to determine whether we should force pairing. A larger value leads to more aggressive read pair. [17] </p>
<dt><code>INPUT/OUTPUT OPTIONS:</code></p>
<dd>
<dt><code>-p</code></p>
<dd> Smart pairing. If two adjacent reads have the same name, they are considered to form a read pair. This way, paired-end and single-end reads can be mixed in a single FASTA/Q stream.</p>
<dt><code>-R</code><i>&nbsp;<wbr>STR</i></p>
<dd> Complete read group header line. &#8216;	&#8217; can be used in <i>STR</i> and will be converted to a TAB in the output SAM. The read group ID will be attached to every read in the output. An example is &#8216;@RG	ID:foo	SM:bar&#8217;. [null]</p>
<dt><code>-H</code><i>&nbsp;<wbr>ARG</i></p>
<dd> If ARG starts with @, it is interpreted as a string and gets inserted into the output SAM header; otherwise, ARG is interpreted as a file with all lines starting with @ in the file inserted into the SAM header. [null]</p>
<dt><code>-T</code><i>&nbsp;<wbr>INT</i></p>
<dd> Don&#8217;t output alignment with score lower than <i>INT</i>. This option affects output and occasionally SAM flag 2. [30]</p>
<dt><code>-j</code></p>
<dd> Treat ALT contigs as part of the primary assembly (i.e. ignore the <i>db.prefix.alt</i> file).</p>
<dt><code>-h</code><i>&nbsp;<wbr>INT[,INT2]</i></p>
<dd> If a query has not more than <i>INT</i> hits with score higher than 80% of the best hit, output them all in the XA tag. If <i>INT2</i> is specified, BWA-MEM outputs up to <i>INT2</i> hits if the list contains a hit to an ALT contig. [5,200]</p>
<dt><code>-a</code></p>
<dd> Output all found alignments for single-end or unpaired paired-end reads. These alignments will be flagged as secondary alignments.</p>
<dt><code>-C</code></p>
<dd> Append append FASTA/Q comment to SAM output. This option can be used to transfer read meta information (e.g. barcode) to the SAM output. Note that the FASTA/Q comment (the string after a space in the header line) must conform the SAM spec (e.g. BC:Z:CGTAC). Malformated comments lead to incorrect SAM output.</p>
<dt><code>-Y</code></p>
<dd> Use soft clipping CIGAR operation for supplementary alignments. By default, BWA-MEM uses soft clipping for the primary alignment and hard clipping for supplementary alignments.</p>
<dt><code>-M</code></p>
<dd> Mark shorter split hits as secondary (for Picard compatibility).</p>
<dt><code>-v</code><i>&nbsp;<wbr>INT</i></p>
<dd> Control the verbose level of the output. This option has not been fully supported throughout BWA. Ideally, a value 0 for disabling all the output to stderr; 1 for outputting errors only; 2 for warnings and errors; 3 for all normal messages; 4 or higher for debugging. When this option takes value 4, the output is not SAM. [3]</p>
<dt><code>-I</code><i>&nbsp;<wbr>FLOAT[,FLOAT[,INT[,INT]]]</i></p>
<dd> Specify the mean, standard deviation (10% of the mean if absent), max (4 sigma from the mean if absent) and min (4 sigma if absent) of the insert size distribution. Only applicable to the FR orientation. By default, BWA-MEM infers these numbers and the pair orientations given enough reads. [inferred] </p>
</dl>
</dl>
<dt><code>aln</code></p>
<dd> bwa aln [-n maxDiff] [-o maxGapO] [-e maxGapE] [-d nDelTail] [-i nIndelEnd] [-k maxSeedDiff] [-l seedLen] [-t nThrds] [-cRN] [-M misMsc] [-O gapOsc] [-E gapEsc] [-q trimQual] &lt;in.db.fasta&gt; &lt;in.query.fq&gt; &gt; &lt;out.sai&gt; </p>
<p> Find the SA coordinates of the input reads. Maximum <i>maxSeedDiff</i> differences are allowed in the first <i>seedLen</i> subsequence and maximum <i>maxDiff</i> differences are allowed in the whole sequence. </p>
<p> <code>OPTIONS:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-n</code><i>&nbsp;<wbr>NUM</i></p>
<dd> Maximum edit distance if the value is INT, or the fraction of missing alignments given 2% uniform base error rate if FLOAT. In the latter case, the maximum edit distance is automatically chosen for different read lengths. [0.04]</p>
<dt><code>-o</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum number of gap opens [1]</p>
<dt><code>-e</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum number of gap extensions, -1 for k-difference mode (disallowing long gaps) [-1]</p>
<dt><code>-d</code><i>&nbsp;<wbr>INT</i></p>
<dd> Disallow a long deletion within INT bp towards the 3&#8242;-end [16]</p>
<dt><code>-i</code><i>&nbsp;<wbr>INT</i></p>
<dd> Disallow an indel within INT bp towards the ends [5]</p>
<dt><code>-l</code><i>&nbsp;<wbr>INT</i></p>
<dd> Take the first INT subsequence as seed. If INT is larger than the query sequence, seeding will be disabled. For long reads, this option is typically ranged from 25 to 35 for `-k 2&#8242;. [inf]</p>
<dt><code>-k</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum edit distance in the seed [2]</p>
<dt><code>-t</code><i>&nbsp;<wbr>INT</i></p>
<dd> Number of threads (multi-threading mode) [1]</p>
<dt><code>-M</code><i>&nbsp;<wbr>INT</i></p>
<dd> Mismatch penalty. BWA will not search for suboptimal hits with a score lower than (bestScore-misMsc). [3]</p>
<dt><code>-O</code><i>&nbsp;<wbr>INT</i></p>
<dd> Gap open penalty [11]</p>
<dt><code>-E</code><i>&nbsp;<wbr>INT</i></p>
<dd> Gap extension penalty [4]</p>
<dt><code>-R</code><i>&nbsp;<wbr>INT</i></p>
<dd> Proceed with suboptimal alignments if there are no more than INT equally best hits. This option only affects paired-end mapping. Increasing this threshold helps to improve the pairing accuracy at the cost of speed, especially for short reads (~32bp).</p>
<dt><code>-c</code></p>
<dd> Reverse query but not complement it, which is required for alignment in the color space. (Disabled since 0.6.x)</p>
<dt><code>-N</code></p>
<dd> Disable iterative search. All hits with no more than <i>maxDiff</i> differences will be found. This mode is much slower than the default.</p>
<dt><code>-q</code><i>&nbsp;<wbr>INT</i></p>
<dd> Parameter for read trimming. BWA trims a read down to argmax_x{\sum_{i=x+1}^l(INT-q_i)} if q_l&lt;INT where l is the original read length. [0]</p>
<dt><code>-I</code></p>
<dd> The input is in the Illumina 1.3+ read format (quality equals ASCII-64).</p>
<dt><code>-B</code><i>&nbsp;<wbr>INT</i></p>
<dd> Length of barcode starting from the 5&#8242;-end. When <i>INT</i> is positive, the barcode of each read will be trimmed before mapping and will be written at the <code>BC</code> SAM tag. For paired-end reads, the barcode from both ends are concatenated. [0]</p>
<dt><code>-b</code></p>
<dd> Specify the input read sequence file is the BAM format. For paired-end data, two ends in a pair must be grouped together and options <code>-1</code> or <code>-2</code> are usually applied to specify which end should be mapped. Typical command lines for mapping pair-end data in the BAM format are: </p>
<p>&nbsp;<wbr>bwa aln ref.fa -b1 reads.bam&nbsp;<wbr>&gt;&nbsp;<wbr>1.sai<br />
&nbsp;<wbr>bwa aln ref.fa -b2 reads.bam&nbsp;<wbr>&gt;&nbsp;<wbr>2.sai<br />
&nbsp;<wbr>bwa sampe ref.fa 1.sai 2.sai reads.bam reads.bam&nbsp;<wbr>&gt;&nbsp;<wbr>aln.sam</p>
<dt><code>-0</code></p>
<dd> When <code>-b</code> is specified, only use single-end reads in mapping.</p>
<dt><code>-1</code></p>
<dd> When <code>-b</code> is specified, only use the first read in a read pair in mapping (skip single-end reads and the second reads).</p>
<dt><code>-2</code></p>
<dd> When <code>-b</code> is specified, only use the second read in a read pair in mapping. <code></dl>
</dl>
<p> </code> </p>
<dt><code>samse</code></p>
<dd> bwa samse [-n maxOcc] &lt;in.db.fasta&gt; &lt;in.sai&gt; &lt;in.fq&gt; &gt; &lt;out.sam&gt; </p>
<p> Generate alignments in the SAM format given single-end reads. Repetitive hits will be randomly chosen. </p>
<p> <code>OPTIONS:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-n</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum number of alignments to output in the XA tag for reads paired properly. If a read has more than INT hits, the XA tag will not be written. [3]</p>
<dt><code>-r</code><i>&nbsp;<wbr>STR</i></p>
<dd> Specify the read group in a format like `@RG	ID:foo	SM:bar&#8217;. [null]</dl>
</dl>
<dt><code>sampe</code></p>
<dd> bwa sampe [-a maxInsSize] [-o maxOcc] [-n maxHitPaired] [-N maxHitDis] [-P] &lt;in.db.fasta&gt; &lt;in1.sai&gt; &lt;in2.sai&gt; &lt;in1.fq&gt; &lt;in2.fq&gt; &gt; &lt;out.sam&gt; </p>
<p> Generate alignments in the SAM format given paired-end reads. Repetitive read pairs will be placed randomly. </p>
<p> <code>OPTIONS:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-a</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum insert size for a read pair to be considered being mapped properly. Since 0.4.5, this option is only used when there are not enough good alignment to infer the distribution of insert sizes. [500]</p>
<dt><code>-o</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum occurrences of a read for pairing. A read with more occurrneces will be treated as a single-end read. Reducing this parameter helps faster pairing. [100000]</p>
<dt><code>-P</code></p>
<dd> Load the entire FM-index into memory to reduce disk operations (base-space reads only). With this option, at least 1.25N bytes of memory are required, where N is the length of the genome.</p>
<dt><code>-n</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum number of alignments to output in the XA tag for reads paired properly. If a read has more than INT hits, the XA tag will not be written. [3]</p>
<dt><code>-N</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum number of alignments to output in the XA tag for disconcordant read pairs (excluding singletons). If a read has more than INT hits, the XA tag will not be written. [10]</p>
<dt><code>-r</code><i>&nbsp;<wbr>STR</i></p>
<dd> Specify the read group in a format like `@RG	ID:foo	SM:bar&#8217;. [null]</dl>
</dl>
<dt><code>bwasw</code></p>
<dd> bwa bwasw [-a matchScore] [-b mmPen] [-q gapOpenPen] [-r gapExtPen] [-t nThreads] [-w bandWidth] [-T thres] [-s hspIntv] [-z zBest] [-N nHspRev] [-c thresCoef] &lt;in.db.fasta&gt; &lt;in.fq&gt; [mate.fq] </p>
<p> Align query sequences in the <i>in.fq</i> file. When <i>mate.fq</i> is present, perform paired-end alignment. The paired-end mode only works for reads Illumina short-insert libraries. In the paired-end mode, BWA-SW may still output split alignments but they are all marked as not properly paired; the mate positions will not be written if the mate has multiple local hits. </p>
<p> <code>OPTIONS:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-a</code><i>&nbsp;<wbr>INT</i></p>
<dd> Score of a match [1]</p>
<dt><code>-b</code><i>&nbsp;<wbr>INT</i></p>
<dd> Mismatch penalty [3]</p>
<dt><code>-q</code><i>&nbsp;<wbr>INT</i></p>
<dd> Gap open penalty [5]</p>
<dt><code>-r</code><i>&nbsp;<wbr>INT</i></p>
<dd> Gap extension penalty. The penalty for a contiguous gap of size k is q+k*r. [2]</p>
<dt><code>-t</code><i>&nbsp;<wbr>INT</i></p>
<dd> Number of threads in the multi-threading mode [1]</p>
<dt><code>-w</code><i>&nbsp;<wbr>INT</i></p>
<dd> Band width in the banded alignment [33]</p>
<dt><code>-T</code><i>&nbsp;<wbr>INT</i></p>
<dd> Minimum score threshold divided by a [37]</p>
<dt><code>-c</code><i>&nbsp;<wbr>FLOAT</i></p>
<dd> Coefficient for threshold adjustment according to query length. Given an l-long query, the threshold for a hit to be retained is a*max{T,c*<a href="/docs/linux/man/l-log/">log</a>(l)}. [5.5]</p>
<dt><code>-z</code><i>&nbsp;<wbr>INT</i></p>
<dd> Z-best heuristics. Higher -z increases accuracy at the cost of speed. [1]</p>
<dt><code>-s</code><i>&nbsp;<wbr>INT</i></p>
<dd> Maximum SA interval size for initiating a seed. Higher -s increases accuracy at the cost of speed. [3]</p>
<dt><code>-N</code><i>&nbsp;<wbr>INT</i></p>
<dd> Minimum number of seeds supporting the resultant alignment to skip reverse alignment. [5]</dl>
</dl>
</dl>
<h2>SAM ALIGNMENT FORMAT</h2>
<p> The output of the <code>`aln&#8217;</code> command is binary and designed for BWA use only. BWA outputs the final alignment in the SAM (Sequence Alignment/Map) format. Each line consists of: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Col</code></td>
<td ALIGN=center><code>Field</code></td>
<td ALIGN=center><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>QNAME</td>
<td>Query (pair) NAME
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>FLAG</td>
<td>bitwise FLAG
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>RNAME</td>
<td>Reference sequence NAME
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>POS</td>
<td>1-based leftmost POSition/coordinate of clipped sequence
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>MAPQ</td>
<td>MAPping Quality (Phred-scaled)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>CIAGR</td>
<td>extended CIGAR string
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>MRNM</td>
<td>Mate Reference sequence NaMe (`=&#8217; if same as RNAME)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>MPOS</td>
<td>1-based Mate POSistion
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>ISIZE</td>
<td>Inferred insert SIZE
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>SEQ</td>
<td>query SEQuence on the same strand as the reference
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>QUAL</td>
<td>query QUALity (ASCII-33 gives the Phred base quality)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>OPT</td>
<td>variable OPTional fields in the format TAG:VTYPE:VALUE
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Each bit in the FLAG field is defined as: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Chr</code></td>
<td ALIGN=center><code>Flag</code></td>
<td ALIGN=center><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>p</td>
<td>0x0001</td>
<td>the read is paired in sequencing
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>P</td>
<td>0x0002</td>
<td>the read is mapped in a proper pair
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>u</td>
<td>0x0004</td>
<td>the query sequence itself is unmapped
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>U</td>
<td>0x0008</td>
<td>the mate is unmapped
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>r</td>
<td>0x0010</td>
<td>strand of the query (1 for reverse)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>R</td>
<td>0x0020</td>
<td>strand of the mate
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1</td>
<td>0x0040</td>
<td>the read is the first read in a pair
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>2</td>
<td>0x0080</td>
<td>the read is the second read in a pair
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>s</td>
<td>0x0100</td>
<td>the alignment is not primary
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>f</td>
<td>0x0200</td>
<td>QC failure
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>d</td>
<td>0x0400</td>
<td>optical or PCR duplicate
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>S</td>
<td>0x0800</td>
<td>supplementary alignment
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The Please check &lt;<a rel="nofollow" href="http://samtools.sourceforge.net">http://samtools.sourceforge.net</a>&gt; for the format specification and the tools for post-processing the alignment. </p>
<p> BWA generates the following optional fields. Tags starting with `X&#8217; are specific to BWA. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Tag</code></td>
<td ALIGN=center><code>Meaning</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>NM</code></td>
<td>Edit distance
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>MD</code></td>
<td>Mismatching positions/bases
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>AS</code></td>
<td>Alignment score
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>BC</code></td>
<td>Barcode sequence
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>SA</code></td>
<td>Supplementary alignments
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>X0</code></td>
<td>Number of best hits
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>X1</code></td>
<td>Number of suboptimal hits found by BWA
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XN</code></td>
<td>Number of ambiguous bases in the referenece
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XM</code></td>
<td>Number of mismatches in the alignment
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XO</code></td>
<td>Number of gap opens
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XG</code></td>
<td>Number of gap extentions
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XT</code></td>
<td>Type: Unique/Repeat/N/Mate-sw
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XA</code></td>
<td>Alternative hits; format: /(chr,pos,CIGAR,NM;)*/
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XS</code></td>
<td>Suboptimal alignment score
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XF</code></td>
<td>Support from forward/reverse alignment
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>XE</code></td>
<td>Number of supporting seeds
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Note that XO and XG are generated by BWT search while the CIGAR string by Smith-Waterman alignment. These two tags may be inconsistent with the CIGAR string. This is not a bug. </p>
<h2>NOTES ON SHORT-READ ALIGNMENT</h2>
<h3>Alignment Accuracy</h3>
<p> When seeding is disabled, BWA guarantees to find an alignment containing maximum <i>maxDiff</i> differences including <i>maxGapO</i> gap opens which do not occur within <i>nIndelEnd</i> bp towards either end of the query. Longer gaps may be found if <i>maxGapE</i> is positive, but it is not guaranteed to find all hits. When seeding is enabled, BWA further requires that the first <i>seedLen</i> subsequence contains no more than <i>maxSeedDiff</i> differences. </p>
<p> When gapped alignment is disabled, BWA is expected to generate the same alignment as Eland version 1, the Illumina alignment program. However, as BWA change `N&#8217; in the database sequence to random nucleotides, hits to these random sequences will also be counted. As a consequence, BWA may mark a unique hit as a repeat, if the random sequences happen to be identical to the sequences which should be unqiue in the database. </p>
<p> By default, if the best hit is not highly repetitive (controlled by -R), BWA also finds all hits contains one more mismatch; otherwise, BWA finds all equally best hits only. Base quality is NOT considered in evaluating hits. In the paired-end mode, BWA pairs all hits it found. It further performs Smith-Waterman alignment for unmapped reads to rescue reads with a high erro rate, and for high-quality anomalous pairs to fix potential alignment errors. </p>
<h3>Estimating Insert Size Distribution</h3>
<p> BWA estimates the insert size distribution per 256*1024 read pairs. It first collects pairs of reads with both ends mapped with a single-end quality 20 or higher and then calculates median (Q2), lower and higher quartile (Q1 and Q3). It estimates the mean and the variance of the insert size distribution from pairs whose insert sizes are within interval [Q1-2(Q3-Q1), Q3+2(Q3-Q1)]. The maximum distance x for a pair considered to be properly paired (SAM flag 0x2) is calculated by solving equation Phi((x-mu)/sigma)=x/L*p0, where mu is the mean, sigma is the standard error of the insert size distribution, L is the length of the genome, p0 is prior of anomalous pair and Phi() is the standard cumulative distribution function. For mapping Illumina short-insert reads to the human genome, x is about 6-7 sigma away from the mean. Quartiles, mean, variance and x will be printed to the standard error output. </p>
<h3>Memory Requirement</h3>
<p> With bwtsw algorithm, 5GB memory is required for indexing the complete human genome sequences. For short reads, the <code>aln</code> command uses ~3.2GB memory and the <code>sampe</code> command uses ~5.4GB. </p>
<h3>Speed</h3>
<p> Indexing the human genome sequences takes 3 hours with bwtsw algorithm. Indexing smaller genomes with IS algorithms is faster, but requires more memory. </p>
<p> The speed of alignment is largely determined by the error rate of the query sequences (r). Firstly, BWA runs much faster for near perfect hits than for hits with many differences, and it stops searching for a hit with l+2 differences if a l-difference hit is found. This means BWA will be very slow if r is high because in this case BWA has to visit hits with many differences and looking for these hits is expensive. Secondly, the alignment algorithm behind makes the speed sensitive to [k log(N)/m], where k is the maximum allowed differences, N the size of database and m the length of a query. In practice, we choose k w.r.t. r and therefore r is the leading factor. I would not recommend to use BWA on data with r&gt;0.02. </p>
<p> Pairing is slower for shorter reads. This is mainly because shorter reads have more spurious hits and converting SA coordinates to chromosomal coordinates are very costly. </p>
<h2>CHANGES IN BWA-0.6</h2>
<p> Since version 0.6, BWA has been able to work with a reference genome longer than 4GB. This feature makes it possible to integrate the forward and reverse complemented genome in one FM-index, which speeds up both BWA-short and BWA-SW. As a tradeoff, BWA uses more memory because it has to keep all positions and ranks in 64-bit integers, twice larger than 32-bit integers used in the previous versions. </p>
<p> The latest BWA-SW also works for paired-end reads longer than 100bp. In comparison to BWA-short, BWA-SW tends to be more accurate for highly unique reads and more robust to relative long INDELs and structural variants. Nonetheless, BWA-short usually has higher power to distinguish the optimal hit from many suboptimal hits. The choice of the mapping algorithm may depend on the application. </p>
<h2>SEE ALSO</h2>
<p> BWA website &lt;<a rel="nofollow" href="http://bio-bwa.sourceforge.net">http://bio-bwa.sourceforge.net</a>&gt;, Samtools website &lt;<a rel="nofollow" href="http://samtools.sourceforge.net">http://samtools.sourceforge.net</a>&gt; </p>
<h2>AUTHOR</h2>
<p> Heng Li at the Sanger Institute wrote the key source codes and integrated the following codes for BWT construction: bwtsw &lt;<a rel="nofollow" href="http://i.cs.hku.hk/~ckwong3/bwtsw/">http://i.cs.hku.hk/~ckwong3/bwtsw/</a>&gt;, implemented by Chi-Kwong Wong at the University of Hong Kong and IS &lt;<a rel="nofollow" href="http://yuta.256.googlepages.com/sais">http://yuta.256.googlepages.com/sais</a>&gt; originally proposed by Nong Ge &lt;<a rel="nofollow" href="http://www.cs.sysu.edu.cn/nong/">http://www.cs.sysu.edu.cn/nong/</a>&gt; at the Sun Yat-Sen University and implemented by Yuta Mori. </p>
<h2>LICENSE AND CITATION</h2>
<p> The full BWA package is distributed under GPLv3 as it uses source codes from BWT-SW which is covered by GPL. Sorting, hash table, BWT and IS libraries are distributed under the MIT license. </p>
<p> If you use the BWA-backtrack algorithm, please cite the following paper: </p>
<p> Li H. and Durbin R. (2009) Fast and accurate short read alignment with Burrows-Wheeler transform. Bioinformatics, 25, 1754-1760. [PMID: 19451168] </p>
<p> If you use the BWA-SW algorithm, please cite: </p>
<p> Li H. and Durbin R. (2010) Fast and accurate long-read alignment with Burrows-Wheeler transform. Bioinformatics, 26, 589-595. [PMID: 20080505] </p>
<p> If you use BWA-MEM or the fastmap component of BWA, please cite: </p>
<p> Li H. (2013) Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM. arXiv:1303.3997v1 [q-bio.GN]. </p>
<p> It is likely that the BWA-MEM manuscript will not appear in a peer-reviewed journal. </p>
<h2>HISTORY</h2>
<p> BWA is largely influenced by BWT-SW. It uses source codes from BWT-SW and mimics its binary file formats; BWA-SW resembles BWT-SW in several ways. The initial idea about BWT-based alignment also came from the group who developed BWT-SW. At the same time, BWA is different enough from BWT-SW. The short-read alignment algorithm bears no similarity to Smith-Waterman algorithm any more. While BWA-SW learns from BWT-SW, it introduces heuristics that can hardly be applied to the original algorithm. In all, BWA does not guarantee to find all local hits as what BWT-SW is designed to do, but it is much faster than BWT-SW on both short and long query sequences. </p>
<p> I started to write the first piece of codes on 24 May 2008 and got the initial stable version on 02 June 2008. During this period, I was acquainted that Professor Tak-Wah Lam, the first author of BWT-SW paper, was collaborating with Beijing Genomics Institute on SOAP2, the successor to SOAP (Short Oligonucleotide Analysis Package). SOAP2 has come out in November 2008. According to the SourceForge download page, the third BWT-based short read aligner, bowtie, was first released in August 2008. At the time of writing this manual, at least three more BWT-based short-read aligners are being implemented. </p>
<p> The BWA-SW algorithm is a new component of BWA. It was conceived in November 2008 and implemented ten months later. </p>
<p> The BWA-MEM algorithm is based on an algorithm finding super-maximal exact matches (SMEMs), which was first published with the fermi assembler paper in 2012. I first implemented the basic SMEM algorithm in the <code>fastmap</code> command for an experiment and then extended the basic algorithm and added the extension part in Feburary 2013 to make BWA-MEM a fully featured mapper. </p>
<h2>Index</h2>
