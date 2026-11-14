---
title: "samtools(1)"
name: "samtools"
section: "1"
letter: "s"
url: "/docs/linux/man/1-samtools/"
description: "samtools – Utilities for the Sequence Alignment/Map (SAM) format"
---

<h2 class="name">NAME</h2>
<p> samtools &#8211; Utilities for the Sequence Alignment/Map (SAM) format </p>
<h2>SYNOPSIS</h2>
<p> samtools addreplacerg -r &#8216;ID:fish&#8217; -r &#8216;LB:1334&#8217; -r &#8216;SM:alpha&#8217; -o output.bam input.bam </p>
<p> samtools ampliconclip -b bed.file input.bam </p>
<p> samtools ampliconstats primers.bed in.bam </p>
<p> samtools bedcov aln.sorted.bam </p>
<p> samtools calmd in.sorted.bam ref.fasta </p>
<p> samtools cat out.bam in1.bam in2.bam in3.bam </p>
<p> samtools collate -o aln.name_collated.bam aln.sorted.bam </p>
<p> samtools consensus -o out.fasta in.bam </p>
<p> samtools coverage aln.sorted.bam </p>
<p> samtools cram-size -v -o out.size in.cram </p>
<p> samtools depad input.bam </p>
<p> samtools depth aln.sorted.bam </p>
<p> samtools dict -a GRCh38 -s &quot;Homo sapiens&quot; ref.fasta </p>
<p> samtools faidx ref.fasta </p>
<p> samtools fasta input.bam &gt; output.fasta </p>
<p> samtools fastq input.bam &gt; output.fastq </p>
<p> samtools fixmate in.namesorted.sam out.bam </p>
<p> samtools flags PAIRED,UNMAP,MUNMAP </p>
<p> samtools flagstat aln.sorted.bam </p>
<p> samtools fqidx ref.fastq </p>
<p> samtools head in.bam </p>
<p> samtools idxstats aln.sorted.bam </p>
<p> samtools import input.fastq &gt; output.bam </p>
<p> samtools index aln.sorted.bam </p>
<p> samtools markdup in.algnsorted.bam out.bam </p>
<p> samtools merge out.bam in1.bam in2.bam in3.bam </p>
<p> samtools mpileup -C50 -f ref.fasta -r chr3:1,000-2,000 in1.bam in2.bam </p>
<p> samtools phase input.bam </p>
<p> samtools quickcheck in1.bam in2.cram </p>
<p> samtools reference -o ref.fa in.cram </p>
<p> samtools reheader in.header.sam in.bam &gt; out.bam </p>
<p> samtools reset -o /tmp/reset.bam processed.bam </p>
<p> samtools samples input.bam </p>
<p> samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam </p>
<p> samtools split merged.bam </p>
<p> samtools stats aln.sorted.bam </p>
<p> samtools targetcut input.bam </p>
<p> samtools tview aln.sorted.bam ref.fasta </p>
<p> samtools view -bt ref_list.txt -o aln.bam aln.sam.gz </p>
<h2>DESCRIPTION</h2>
<p> Samtools is a set of utilities that manipulate alignments in the SAM (Sequence Alignment/Map), BAM, and CRAM formats. It converts between the formats, does sorting, merging and indexing, and can retrieve reads in any regions swiftly. </p>
<p> Samtools is designed to work on a stream. It regards an input file `-&#8216; as the standard input (stdin) and an output file `-&#8216; as the standard output (stdout). Several commands can thus be combined with Unix pipes. Samtools always output warning and error messages to the standard error output (stderr). </p>
<p> Samtools is also able to open files on remote FTP or HTTP(S) servers if the file name starts with `<a href="ftp://',">ftp://&#8217;,</a> `<a rel="nofollow" href="http://',">http://&#8217;,</a> etc. Samtools checks the current working directory for the index file and will download the index upon absence. Samtools does not retrieve the entire alignment file unless it is asked to do so. </p>
<p> If an index is needed, samtools looks for the index suffix appended to the filename, and if that isn&#8217;t found it tries again without the filename suffix (for example <code>in.bam.bai</code> followed by <code>in.bai</code>). However if an index is in a completely different location or has a different name, both the main data filename and index filename can be pasted together with <code>##idx##</code>. For example <code>/data/in.bam##idx##/indices/in.bam.bai</code> may be used to explicitly indicate where the data and index files reside. </p>
<h2>COMMANDS</h2>
<p> Each command has its own man page which can be viewed using e.g. <code>man samtools-view</code> or with a recent GNU man using <code>man samtools view</code>. Below we have a brief summary of syntax and sub-command description. </p>
<p> Options common to all sub-commands are documented below in the GLOBAL COMMAND OPTIONS section. </p>
<dl>
<dt><code>view</code></p>
<dd> samtools view [<i>options</i>] <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i> [<i>region</i>&#8230;] </p>
<p> With no options or regions specified, prints all alignments in the specified input alignment file (in SAM, BAM, or CRAM format) to standard output in SAM format (with no header by default). </p>
<p> You may specify one or more space-separated region specifications after the input filename to restrict output to only those alignments which overlap the specified region(s). Use of region specifications requires a coordinate-sorted and indexed input file. </p>
<p> Options exist to change the output format from SAM to BAM or CRAM, so this command also acts as a file format conversion utility. </p>
<dt><code>tview</code></p>
<dd> samtools tview [<code>-p</code> <i>chr:pos</i>] [<code>-s</code> <i>STR</i>] [<code>-d</code> <i>display</i>] &lt;in.sorted.bam&gt; [ref.fasta] </p>
<p> Text alignment viewer (based on the ncurses library). In the viewer, press `?&#8217; for help and press `g&#8217; to check the alignment start from a region in the format like `chr10:10,000,000&#8242; or `=10,000,000&#8242; when viewing the same reference sequence. </p>
<dt><code>quickcheck</code></p>
<dd> samtools quickcheck [<i>options</i>] <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i> [ &#8230; ] </p>
<p> Quickly check that input files appear to be intact. Checks that beginning of the file contains a valid header (all formats) containing at least one target sequence and then seeks to the end of the file and checks that an end-of-file (EOF) is present and intact (BAM only). </p>
<p> Data in the middle of the file is not read since that would be much more time consuming, so please note that this command will not detect internal corruption, but is useful for testing that files are not truncated before performing more intensive tasks on them. </p>
<p> This command will exit with a non-zero exit code if any input files don&#8217;t have a valid header or are missing an EOF block. Otherwise it will exit successfully (with a zero exit code). </p>
<dt><code>head</code></p>
<dd> samtools head [<i>options</i>] <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i> </p>
<p> Prints the input file&#8217;s headers and optionally also its first few alignment records. This command always displays the headers as they are in the file, never adding an extra @PG header itself. </p>
<dt><code>index</code></p>
<dd> samtools index [<code>-bc</code>] [<code>-m</code> <i>INT</i>] <i>aln.sam.gz</i>|<i>aln.bam</i>|<i>aln.cram</i> [<i>out.index</i>] </p>
<p> Index a coordinate-sorted SAM, BAM or CRAM file for fast random access. Note for SAM this only works if the file has been BGZF compressed first. (Starting from Samtools 1.16, this command can also be given several alignment filenames, which are indexed individually.) </p>
<p> This index is needed when <i>region</i> arguments are used to limit <code>samtools view</code> and similar commands to particular regions of interest. </p>
<p> If an output filename is given, the index file will be written to <i>out.index</i>. Otherwise, for a CRAM file <i>aln.cram</i>, index file <i>aln.cram</i><code>.crai</code> will be created; for a BAM or SAM file <i>aln.bam</i>, either <i>aln.bam</i><code>.bai</code> or <i>aln.bam</i><code>.csi</code> will be created, depending on the index format selected. </p>
<dt><code>sort</code></p>
<dd> samtools sort [<code>-l</code> <i>level</i>] [<code>-m</code> <i>maxMem</i>] [<code>-o</code> <i>out.bam</i>] [<code>-O</code> <i>format</i>] [<code>-n</code>] [<code>-t</code> <i>tag</i>] [<code>-T</code> <i>tmpprefix</i>] [<code>-@</code> <i>threads</i>] [<i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i>] </p>
<p> Sort alignments by leftmost coordinates, or by read name when <code>-n</code> is used. An appropriate <code>@HD-SO</code> sort order header tag will be added or an existing one updated if necessary. </p>
<p> The sorted output is written to standard output by default, or to the specified file (<i>out.bam</i>) when <code>-o</code> is used. This command will also create temporary files <i>tmpprefix</i><code>.</code><i>%d</i><code>.bam</code> as needed when the entire alignment data cannot fit into memory (as controlled via the <code>-m</code> option). </p>
<p> Consider using <code>samtools collate</code> instead if you need name collated data without a full lexicographical sort. </p>
<p> Note that if the sorted output file is to be indexed with <code>samtools index</code>, the default coordinate sort must be used. Thus the <code>-n</code> and <code>-t</code> options are incompatible with <code>samtools index</code>. </p>
<dt><code>collate</code></p>
<dd> samtools collate [<i>options</i>] <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i> [<i>&lt;prefix&gt;</i>] </p>
<p> Shuffles and groups reads together by their names. A faster alternative to a full query name sort, <code>collate</code> ensures that reads of the same name are grouped together in contiguous groups, but doesn&#8217;t make any guarantees about the order of read names between groups. </p>
<p> The output from this command should be suitable for any operation that requires all reads from the same template to be grouped together. </p>
<dt><code>cram-size</code></p>
<dd> samtools cram-size [<i>options</i>] <i>in.cram</i> </p>
<p> Produces a summary of CRAM block Content ID numbers and their associated Data Series stored within them. Optionally a more detailed breakdown of how each data series is encoded per container may also be listed using the <code>-e</code> or <code>&#8211;encodings</code> option. </p>
<dt><code>idxstats</code></p>
<dd> samtools idxstats <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i> </p>
<p> Retrieve and print stats in the index file corresponding to the input file. Before calling idxstats, the input BAM file should be indexed by samtools index. </p>
<p> If run on a SAM or CRAM file or an unindexed BAM file, this command will still produce the same summary statistics, but does so by reading through the entire file. This is far slower than using the BAM indices. </p>
<p> The output is TAB-delimited with each line consisting of reference sequence name, sequence length, # mapped reads and # unmapped reads. It is written to stdout. </p>
<dt><code>flagstat</code></p>
<dd> samtools flagstat <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i> </p>
<p> Does a full pass through the input file to calculate and print statistics to stdout. </p>
<p> Provides counts for each of 13 categories based primarily on bit flags in the FLAG field. Each category in the output is broken down into QC pass and QC fail, which is presented as &quot;#PASS + #FAIL&quot; followed by a description of the category. </p>
<dt><code>flags</code></p>
<dd> samtools flags <i>INT</i>|<i>STR</i>[,&#8230;] </p>
<p> Convert between textual and numeric flag representation. </p>
<p> <code>FLAGS:</code> </p>
<table>
<tr VALIGN=top>
<td ALIGN=right><code>0x1</code></td>
<td>PAIRED</td>
<td>paired-end (or multiple-segment) sequencing technology
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x2</code></td>
<td>PROPER_PAIR</td>
<td>each segment properly aligned according to the aligner
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x4</code></td>
<td>UNMAP</td>
<td>segment unmapped
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x8</code></td>
<td>MUNMAP</td>
<td>next segment in the template unmapped
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x10</code></td>
<td>REVERSE</td>
<td>SEQ is reverse complemented
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x20</code></td>
<td>MREVERSE</td>
<td>SEQ of the next segment in the template is reverse complemented
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x40</code></td>
<td>READ1</td>
<td>the first segment in the template
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x80</code></td>
<td>READ2</td>
<td>the last segment in the template
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x100</code></td>
<td>SECONDARY</td>
<td>secondary alignment
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x200</code></td>
<td>QCFAIL</td>
<td>not passing quality controls
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x400</code></td>
<td>DUP</td>
<td>PCR or optical duplicate
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x800</code></td>
<td>SUPPLEMENTARY</td>
<td>supplementary alignment
</td>
</tr>
</table>
<dt><code>stats</code></p>
<dd> samtools stats [<i>options</i>] <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i> [<i>region</i>&#8230;] </p>
<p> samtools stats collects statistics from BAM files and outputs in a text format. The output can be visualized graphically using plot-bamstats. </p>
<dt><code>bedcov</code></p>
<dd> samtools bedcov [<i>options</i>] <i>region.bed</i> <i>in1.sam</i>|<i>in1.bam</i>|<i>in1.cram</i>[&#8230;] </p>
<p> Reports the total read base count (i.e. the sum of per base read depths) for each genomic region specified in the supplied BED file. The regions are output as they appear in the BED file and are 0-based. Counts for each alignment file supplied are reported in separate columns. </p>
<dt><code>depth</code></p>
<dd> samtools depth [<i>options</i>] [<i>in1.sam</i>|<i>in1.bam</i>|<i>in1.cram</i> [<i>in2.sam</i>|<i>in2.bam</i>|<i>in2.cram</i>] [&#8230;]] </p>
<p> Computes the read depth at each position or region. </p>
<dt><code>ampliconstats</code></p>
<dd> samtools ampliconstats [<i>options</i>] <i>primers.bed</i> <i>in.sam</i>|<i>in.bam</i>|<i>in.cram</i>[&#8230;] </p>
<p> samtools ampliconstats collects statistics from one or more input alignment files and produces tables in text format. The output can be visualized graphically using plot-ampliconstats. </p>
<p> The alignment files should have previously been clipped of primer sequence, for example by <code>samtools ampliconclip</code> and the sites of these primers should be specified as a bed file in the arguments. </p>
<dt><code>mpileup</code></p>
<dd> samtools mpileup [<code>-EB</code>] [<code>-C</code> <i>capQcoef</i>] [<code>-r</code> <i>reg</i>] [<code>-f</code> <i>in.fa</i>] [<code>-l</code> <i>list</i>] [<code>-Q</code> <i>minBaseQ</i>] [<code>-q</code> <i>minMapQ</i>] <i>in.bam</i> [<i>in2.bam</i> [<i>&#8230;</i>]] </p>
<p> Generate textual pileup for one or multiple BAM files. For VCF and BCF output, please use the <code>bcftools mpileup</code> command instead. Alignment records are grouped by sample (SM) identifiers in @RG header lines. If sample identifiers are absent, each input file is regarded as one sample. </p>
<p> See the samtools-mpileup man page for a description of the pileup format and options. </p>
<dt><code>consensus</code></p>
<dd> samtools consensus [<code>options</code>] <i>in.bam</i> </p>
<p> Generate consensus from a SAM, BAM or CRAM file based on the contents of the alignment records. The consensus is written either as FASTA, FASTQ, or a pileup oriented format. </p>
<p> The default output for FASTA and FASTQ formats include one base per non-gap consensus. Hence insertions with respect to the aligned reference will be included and deletions removed. This behaviour can be adjusted. </p>
<p> Two consensus calling algorithms are offered. The default computes a heterozygous consensus in a Bayesian manner, derived from the &quot;Gap5&quot; consensus algorithm. A simpler base frequency counting method is also available. </p>
<dt><code>reference</code></p>
<dd> samtools reference [<code>options</code>] <i>in.bam</i> </p>
<p> Generate a reference from a SAM, BAM or CRAM file based on the contents of the SEQuence field and the MD:Z: auxiliary tags, or from the embedded reference blocks within a CRAM file (provided it was constructed using the <code>embed_ref=1</code> option). </p>
<dt><code>coverage</code></p>
<dd> samtools coverage [<i>options</i>] [<i>in1.sam</i>|<i>in1.bam</i>|<i>in1.cram</i> [<i>in2.sam</i>|<i>in2.bam</i>|<i>in2.cram</i>] [&#8230;]] </p>
<p> Produces a histogram or table of coverage per chromosome. </p>
<dt><code>merge</code></p>
<dd> samtools merge [<code>-nur1f</code>] [<code>-h</code> <i>inh.sam</i>] [<code>-t</code> <i>tag</i>] [<code>-R</code> <i>reg</i>] [<code>-b</code> <i>list</i>] <i>out.bam</i> <i>in1.bam</i> [<i>in2.bam</i> <i>in3.bam</i> &#8230; <i>inN.bam</i>] </p>
<p> Merge multiple sorted alignment files, producing a single sorted output file that contains all the input records and maintains the existing sort order. </p>
<p> If <code>-h</code> is specified the @SQ headers of input files will be merged into the specified header, otherwise they will be merged into a composite header created from the input headers. If the @SQ headers differ in order this may require the output file to be re-sorted after merge. </p>
<p> The ordering of the records in the input files must match the usage of the <code>-n</code> and <code>-t</code> command-line options. If they do not, the output order will be undefined. See <code>sort</code> for information about record ordering. </p>
<dt><code>split</code></p>
<dd> samtools split [<i>options</i>] <i>merged.sam</i>|<i>merged.bam</i>|<i>merged.cram</i> </p>
<p> Splits a file by read group, producing one or more output files matching a common prefix (by default based on the input filename) each containing one read-group. </p>
<dt><code>cat</code></p>
<dd> samtools cat [<code>-b</code> <i>list</i>] [<code>-h</code> <i>header.sam</i>] [<code>-o</code> <i>out.bam</i>] <i>in1.bam</i> <i>in2.bam</i> [ &#8230; ] </p>
<p> Concatenate BAMs or CRAMs. Although this works on either BAM or CRAM, all input files must be the same format as each other. The sequence dictionary of each input file must be identical, although this command does not check this. This command uses a similar trick to <code>reheader</code> which enables fast BAM concatenation. </p>
<dt><code>import</code></p>
<dd> samtools import [<i>options</i>] <i>in.fastq</i> [ &#8230; ] </p>
<p> Converts one or more FASTQ files to unaligned SAM, BAM or CRAM. These formats offer a richer capability of tracking sample meta-data via the SAM header and per-read meta-data via the auxiliary tags. The <code>fastq</code> command may be used to reverse this conversion. </p>
<dt><code>fastq/a</code></p>
<dd> samtools fastq [<i>options</i>] <i>in.bam</i><br />
 samtools fasta [<i>options</i>] <i>in.bam</i> </p>
<p> Converts a BAM or CRAM into either FASTQ or FASTA format depending on the command invoked. The files will be automatically compressed if the file names have a .gz or .bgzf extension. </p>
<p> The input to this program must be collated by name. Use <code>samtools collate</code> or <code>samtools sort -n</code> to ensure this. </p>
<dt><code>faidx</code></p>
<dd> samtools faidx &lt;ref.fasta&gt; [region1 [&#8230;]] </p>
<p> Index reference sequence in the FASTA format or extract subsequence from indexed reference sequence. If no region is specified, <code>faidx</code> will index the file and create <i>&lt;ref.fasta&gt;.fai</i> on the disk. If regions are specified, the subsequences will be retrieved and printed to stdout in the FASTA format. </p>
<p> The input file can be compressed in the <code>BGZF</code> format. </p>
<p> FASTQ files can be read and indexed by this command. Without using <code>&#8211;fastq</code> any extracted subsequence will be in FASTA format. </p>
<dt><code>fqidx</code></p>
<dd> samtools fqidx &lt;ref.fastq&gt; [region1 [&#8230;]] </p>
<p> Index reference sequence in the FASTQ format or extract subsequence from indexed reference sequence. If no region is specified, <code>fqidx</code> will index the file and create <i>&lt;ref.fastq&gt;.fai</i> on the disk. If regions are specified, the subsequences will be retrieved and printed to stdout in the FASTQ format. </p>
<p> The input file can be compressed in the <code>BGZF</code> format. </p>
<p> <code>samtools fqidx</code> should only be used on fastq files with a small number of entries. Trying to use it on a file containing millions of short sequencing reads will produce an index that is almost as big as the original file, and searches using the index will be very slow and use a lot of memory. </p>
<dt><code>dict</code></p>
<dd> samtools dict <i>ref.fasta</i>|<i>ref.fasta.gz</i> </p>
<p> Create a sequence dictionary file from a fasta file. </p>
<dt><code>calmd</code></p>
<dd> samtools calmd [<code>-Eeubr</code>] [<code>-C</code> <i>capQcoef</i>] <i>aln.bam</i> <i>ref.fasta</i> </p>
<p> Generate the MD tag. If the MD tag is already present, this command will give a warning if the MD tag generated is different from the existing tag. Output SAM by default. </p>
<p> Calmd can also read and write CRAM files although in most cases it is pointless as CRAM recalculates MD and NM tags on the fly. The one exception to this case is where both input and output CRAM files have been / are being created with the <i>no_ref</i> option. </p>
<dt><code>fixmate</code></p>
<dd> samtools fixmate [<code>-rpcm</code>] [<code>-O</code> <i>format</i>] <i>in.nameSrt.bam out.bam</i> </p>
<p> Fill in mate coordinates, ISIZE and mate related flags from a name-sorted alignment. </p>
<dt><code>markdup</code></p>
<dd> samtools markdup [<code>-l</code> <i>length</i>] [<code>-r</code>] [<code>-s</code>] [<code>-T</code>] [<code>-S</code>] <i>in.algsort.bam out.bam</i> </p>
<p> Mark duplicate alignments from a coordinate sorted file that has been run through <code>samtools fixmate</code> with the <code>-m</code> option. This program relies on the MC and ms tags that fixmate provides. </p>
<dt><code>rmdup</code></p>
<dd> samtools rmdup [-sS] &lt;input.srt.bam&gt; &lt;out.bam&gt; </p>
<p> <code>This command is obsolete. Use markdup instead.</code> </p>
<dt><code>addreplacerg</code></p>
<dd> samtools addreplacerg [<code>-r</code> <i>rg-line</i> | <code>-R</code> <i>rg-ID</i>] [<code>-m</code> <i>mode</i>] [<code>-l</code> <i>level</i>] [<code>-o</code> <i>out.bam</i>] <i>in.bam</i> </p>
<p> Adds or replaces read group tags in a file. </p>
<dt><code>reheader</code></p>
<dd> samtools reheader [<code>-iP</code>] <i>in.header.sam in.bam</i> </p>
<p> Replace the header in <i>in.bam</i> with the header in <i>in.header.sam</i>. This command is much faster than replacing the header with a BAM&rarr;SAM&rarr;BAM conversion. </p>
<p> By default this command outputs the BAM or CRAM file to standard output (stdout), but for CRAM format files it has the option to perform an in-place edit, both reading and writing to the same file. No validity checking is performed on the header, nor that it is suitable to use with the sequence data itself. </p>
<dt><code>targetcut</code></p>
<dd> samtools targetcut [<code>-Q</code> <i>minBaseQ</i>] [<code>-i</code> <i>inPenalty</i>] [<code>-0</code> <i>em0</i>] [<code>-1</code> <i>em1</i>] [<code>-2</code> <i>em2</i>] [<code>-f</code> <i>ref</i>] <i>in.bam</i> </p>
<p> This command identifies target regions by examining the continuity of read depth, computes haploid consensus sequences of targets and outputs a SAM with each sequence corresponding to a target. When option <code>-f</code> is in use, BAQ will be applied. This command is <code>only</code> designed for cutting fosmid clones from fosmid pool sequencing [Ref. Kitzman et al. (2010)]. </p>
<dt><code>phase</code></p>
<dd> samtools phase [<code>-AF</code>] [<code>-k</code> <i>len</i>] [<code>-b</code> <i>prefix</i>] [<code>-q</code> <i>minLOD</i>] [<code>-Q</code> <i>minBaseQ</i>] <i>in.bam</i> </p>
<p> Call and phase heterozygous SNPs. </p>
<dt><code>depad</code></p>
<dd> samtools depad [<code>-SsCu1</code>] [<code>-T</code> <i>ref.fa</i>] [<code>-o</code> <i>output</i>] <i>in.bam</i> </p>
<p> Converts a BAM aligned against a padded reference to a BAM aligned against the depadded reference. The padded reference may contain verbatim &quot;*&quot; bases in it, but &quot;*&quot; bases are also counted in the reference numbering. This means that a sequence base-call aligned against a reference &quot;*&quot; is considered to be a cigar match (&quot;M&quot; or &quot;X&quot;) operator (if the base-call is &quot;A&quot;, &quot;C&quot;, &quot;G&quot; or &quot;T&quot;). After depadding the reference &quot;*&quot; bases are deleted and such aligned sequence base-calls become insertions. Similarly transformations apply for deletions and padding cigar operations. </p>
<dt><code>ampliconclip</code></p>
<dd> samtools ampliconclip [<code>-o</code> <i>out.file</i>] [<code>-f</code> <i>stat.file</i>] [<code>&#8211;soft-clip</code>] [<code>&#8211;hard-clip</code>] [<code>&#8211;both-ends</code>] [<code>&#8211;strand</code>] [<code>&#8211;clipped</code>] [<code>&#8211;fail</code>] [<code>&#8211;no-PG</code>] <code>-b</code> <i>bed.file in.file</i> </p>
<p> Clip reads in a SAM compatible file based on data from a BED file. </p>
<dt><code>samples</code></p>
<dd> samtools samples [<code>-o</code> <i>out.file</i>] [<code>-i</code>] [<code>-T</code> <i>TAG</i>] [<code>-f</code> <i>refs.fasta</i>] [<code>-F</code> <i>refs_list</i>] [<code>-X</code>] </p>
<p> Prints the samples from alignment files </p>
<dt><code>reset</code></p>
<dd> samtools reset [<code>-o</code> <i>FILE</i>] [<code>-x</code>/<code>&#8211;remove-tag</code> <i>tag_list</i>] [<code>&#8211;keep-tag</code> <i>tag_list</i>] [<code>&#8211;reject-PG</code> <i>pgid</i>] [<code>&#8211;no-RG</code>] [<code>&#8211;no-PG</code>] [&#8230;] </p>
<p> Removes alignment information from records, producing an unaligned SAM, BAM or CRAM file. Flags are reset, header tags are updated or removed as appropriate, and auxiliary tags are removed or retained as specified. Note that the sort order is unchanged. </p>
</dl>
<h2>SAMTOOLS OPTIONS</h2>
<p> These are options that are passed after the <code>samtools</code> command, before any sub-command is specified. </p>
<dl>
<dt><code>help</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Display a brief usage message listing the samtools commands available. If the name of a command is also given, e.g., <code>samtools help view</code>, the detailed usage message for that particular command is displayed. </p>
<dt><code>&#8211;version</code></p>
<dd> Display the version numbers and copyright information for samtools and the important libraries used by samtools. </p>
<dt><code>&#8211;version-only</code></p>
<dd> Display the full samtools version number in a machine-readable format.</dl>
<h2>GLOBAL COMMAND OPTIONS</h2>
<p> Several long-options are shared between multiple samtools sub-commands: <code>&#8211;input-fmt</code>, <code>&#8211;input-fmt-option</code>, <code>&#8211;output-fmt</code>, <code>&#8211;output-fmt-option</code>, <code>&#8211;reference</code>, <code>&#8211;write-index</code>, and <code>&#8211;verbosity</code>. The input format is auto-detected and specifying the format is unnecessary, so this option is rarely offered. Note that not all subcommands have all options. Consult the subcommand help for more details. </p>
<p> Format strings recognised are &quot;sam&quot;, &quot;sam.gz&quot;, &quot;bam&quot; and &quot;cram&quot;. They may be followed by a comma separated list of options as <i>key</i> or <i>key</i>=<i>value</i>. See below for examples. </p>
<p> The <code>fmt-option</code> arguments accept either a single <i>option</i> or <i>option</i>=<i>value</i>. Note that some options only work on some file formats and only on read or write streams. If value is unspecified for a boolean option, the value is assumed to be 1. The valid options are as follows.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>level=</code><i>INT</i></p>
<dd> Output only. Specifies the compression level from 1 to 9, or 0 for uncompressed. If the output format is SAM, this also enables BGZF compression, otherwise SAM defaults to uncompressed.</p>
<dt><code>nthreads=</code><i>INT</i></p>
<dd> Specifies the number of threads to use during encoding and/or decoding. For BAM this will be encoding only. In CRAM the threads are dynamically shared between encoder and decoder.</p>
<dt><code>filter=</code><i>STRING</i></p>
<dd> Apply filter STRING to all incoming records, rejecting any that do not satisfy the expression. See the FILTER EXPRESSIONS section below for specifics.</p>
<dt><code>reference=</code><i>fasta_file</i></p>
<dd> Specifies a FASTA reference file for use in CRAM encoding or decoding. It usually is not required for decoding except in the situation of the MD5 not being obtainable via the REF_PATH or REF_CACHE environment variables.</p>
<dt><code>decode_md=</code><i>0|1</i></p>
<dd> CRAM input only; defaults to 1 (on). CRAM does not typically store MD and NM tags, preferring to generate them on the fly. When this option is 0 missing MD, NM tags will not be generated. It can be particularly useful when combined with a file encoded using store_md=1 and store_nm=1.</p>
<dt><code>store_md=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). CRAM normally only stores MD tags when the reference is unknown and lets the decoder generate these values on-the-fly (see decode_md).</p>
<dt><code>store_nm=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). CRAM normally only stores NM tags when the reference is unknown and lets the decoder generate these values on-the-fly (see decode_md).</p>
<dt><code>ignore_md5=</code><i>0|1</i></p>
<dd> CRAM input only; defaults to 0 (off). When enabled, md5 checksum errors on the reference sequence and block checksum errors within CRAM are ignored. Use of this option is strongly discouraged.</p>
<dt><code>required_fields=</code><i>bit-field</i></p>
<dd> CRAM input only; specifies which SAM columns need to be populated. By default all fields are used. Limiting the decode to specific columns can have significant performance gains. The bit-field is a numerical value constructed from the following table. </p>
<table>
<tr VALIGN=top>
<td ALIGN=right><code>0x1</code></td>
<td>SAM_QNAME
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x2</code></td>
<td>SAM_FLAG
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x4</code></td>
<td>SAM_RNAME
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x8</code></td>
<td>SAM_POS
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x10</code></td>
<td>SAM_MAPQ
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x20</code></td>
<td>SAM_CIGAR
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x40</code></td>
<td>SAM_RNEXT
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x80</code></td>
<td>SAM_PNEXT
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x100</code></td>
<td>SAM_TLEN
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x200</code></td>
<td>SAM_SEQ
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x400</code></td>
<td>SAM_QUAL
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x800</code></td>
<td>SAM_AUX
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right><code>0x1000</code></td>
<td>SAM_RGAUX
</td>
</tr>
</table>
<dt><code>name_prefix=</code><i>string</i></p>
<dd> CRAM input only; defaults to output filename. Any sequences with auto-generated read names will use <i>string</i> as the name prefix.</p>
<dt><code>multi_seq_per_slice=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). By default CRAM generates one container per reference sequence, except in the case of many small references (such as a fragmented assembly).</p>
<dt><code>version=</code><i>major.minor</i></p>
<dd> CRAM output only. Specifies the CRAM version number. Acceptable values are &quot;2.1&quot; and &quot;3.0&quot;.</p>
<dt><code>seqs_per_slice=</code><i>INT</i></p>
<dd> CRAM output only; defaults to 10000.</p>
<dt><code>slices_per_container=</code><i>INT</i></p>
<dd> CRAM output only; defaults to 1. The effect of having multiple slices per container is to share the compression header block between multiple slices. This is unlikely to have any significant impact unless the number of sequences per slice is reduced. (Together these two options control the granularity of random access.)</p>
<dt><code>embed_ref=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). If 1, this will store portions of the reference sequence in each slice, permitting decode without having requiring an external copy of the reference sequence.</p>
<dt><code>no_ref=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). If 1, sequences will be stored verbatim with no reference encoding. This can be useful if no reference is available for the file.</p>
<dt><code>use_bzip2=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). Permits use of bzip2 in CRAM block compression.</p>
<dt><code>use_lzma=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). Permits use of lzma in CRAM block compression.</p>
<dt><code>use_fqz=</code><i>0|1</i></p>
<dd> CRAM &ge; 3.1 output only; enables and disables the fqzcomp quality compression method. This is on by default for version 3.1 and above only when the small and archive profiles are in use.</p>
<dt><code>use_tok=</code><i>0|1</i></p>
<dd> CRAM &ge; 3.1 output only; enables and disables the namne tokeniser compression method. This is on by default for version 3.1 and above.</p>
<dt><code>lossy_names=</code><i>0|1</i></p>
<dd> CRAM output only; defaults to 0 (off). If 1, templates with all members within the same CRAM slice will have their read names removed. New names will be automatically generated during decoding. Also see the <code>name_prefix</code> option.</p>
<dt><code>fast, normal, small, archive</code></p>
<dd> CRAM output only. Set the CRAM compression profile. This is a simplified way of setting many output options at once. It changes the following options according to the profile in use. The &quot;normal&quot; profile is the default. </p>
<table>
<tr VALIGN=top>
<td><code>Option</code></td>
<td><code>fast</code></td>
<td><code>normal</code></td>
<td><code>small</code></td>
<td><code>archive</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>level</code></td>
<td>1</td>
<td>5</td>
<td>6</td>
<td>7
</td>
</tr>
<tr VALIGN=top>
<td><code>use_bzip2</code></td>
<td>off</td>
<td>off</td>
<td>on</td>
<td>on
</td>
</tr>
<tr VALIGN=top>
<td><code>use_lzma</code></td>
<td>off</td>
<td>off</td>
<td>off</td>
<td>on if level&gt;7
</td>
</tr>
<tr VALIGN=top>
<td><code>use_tok(*)</code></td>
<td>off</td>
<td>on</td>
<td>on</td>
<td>on
</td>
</tr>
<tr VALIGN=top>
<td><code>use_fqz(*)</code></td>
<td>off</td>
<td>off</td>
<td>on</td>
<td>on
</td>
</tr>
<tr VALIGN=top>
<td><code>use_arith(*)</code></td>
<td>off</td>
<td>off</td>
<td>off</td>
<td>on
</td>
</tr>
<tr VALIGN=top>
<td><code>seqs_per_slice</code></td>
<td>10000</td>
<td>10000</td>
<td>25000</td>
<td>100000
</td>
</tr>
</table>
<p> (*) <code>use_tok</code>, <code>use_fqz</code> and <code>use_arith</code> are only enabled for CRAM version 3.1 and above. </p>
<p> The <code>level</code> listed is only the default value, and will not be set if it has been explicitly changed already. Additionally <code>bases_per_slice</code> is set to <code>500*seqs_per_slice</code> unless previously explicitly set. </p>
</dl>
</dl>
<p> For example: </p>
<pre><code>
samtools view-- input - fmt - option decode_md = 0 --output - fmt cram, version = 3.0 --output - fmt - option embed_ref-- output - fmt - option seqs_per_slice = 2000 - o foo.cram foo.bam samtools view - O cram, small - o bar.cram bar.bam
</code></pre>
<p> The <code>&#8211;write-index</code> option enables automatic index creation while writing out BAM, CRAM or bgzf SAM files. Note to get compressed SAM as the output format you need to manually request a compression level, otherwise all SAM files are uncompressed. By default SAM and BAM will use CSI indices while CRAM will use CRAI indices. If you need to create BAI indices note that it is possible to specify the name of the index being written to, and hence the format, by using the <code>filename##idx##indexname</code> notation. </p>
<p> For example: to convert a BAM to a compressed SAM with CSI indexing: </p>
<pre>
samtools view -h -O sam,level=6 --write-index in.bam -o out.sam.gz
</pre>
<p> To convert a SAM to a compressed BAM using BAI indexing: </p>
<pre>
samtools view --write-index in.sam -o out.bam##idx##out.bam.bai
</pre>
<p> The <code>&#8211;verbosity </code><i>INT</i> option sets the verbosity level for samtools and HTSlib. The default is 3 (HTS_LOG_WARNING); 2 reduces warning messages and 0 or 1 also reduces some error messages, while values greater than 3 produce increasing numbers of additional warnings and logging messages. </p>
<h2>REFERENCE SEQUENCES</h2>
<p> The CRAM format requires use of a reference sequence for both reading and writing. </p>
<p> When reading a CRAM the <code>@SQ</code> headers are interrogated to identify the reference sequence MD5sum (<code>M5:</code> tag) and the local reference sequence filename (<code>UR:</code> tag). Note that <i>http://</i> and <i>ftp://</i> based URLs in the UR: field are not used, but local fasta filenames (with or without <i>file://</i>) can be used. </p>
<p> To create a CRAM the <code>@SQ</code> headers will also be read to identify the reference sequences, but M5: and UR: tags may not be present. In this case the <code>-T</code> and <code>-t</code> options of samtools view may be used to specify the fasta or fasta.fai filenames respectively (provided the .fasta.fai file is also backed up by a .fasta file). </p>
<p> The search order to obtain a reference is:</p>
<dl>
<dt>1.</p>
<dd> Use any local file specified by the command line options (eg -T).</p>
<dt>2.</p>
<dd> Look for MD5 via REF_CACHE environment variable.</p>
<dt>3.</p>
<dd> Look for MD5 in each element of the REF_PATH environment variable.</p>
<dt>4.</p>
<dd> Look for a local file listed in the UR: header tag. </p>
</dl>
<h2>FILTER EXPRESSIONS</h2>
<p> Filter expressions are used as an on-the-fly checking of incoming SAM, BAM or CRAM records, discarding records that do not match the specified expression. </p>
<p> The language used is primarily C style, but with a few differences in the precedence rules for bit operators and the inclusion of regular expression matching. </p>
<p> The operator precedence, from strongest binding to weakest, is: </p>
<table>
<tr VALIGN=top>
<td>Grouping</td>
<td><code>(, )</code></td>
<td>E.g. &quot;(1+2)*3&quot;
</td>
</tr>
<tr VALIGN=top>
<td>Values:</td>
<td><code>literals, vars</code></td>
<td>Numbers, strings and variables
</td>
</tr>
<tr VALIGN=top>
<td>Unary ops:</td>
<td><code>+, -, !, ~ </code></td>
<td>E.g. -10 +10, !10 (not), ~5 (bit not)
</td>
</tr>
<tr VALIGN=top>
<td>Math ops:</td>
<td><code>*, /, %</code></td>
<td>Multiply, division and (integer) modulo
</td>
</tr>
<tr VALIGN=top>
<td>Math ops:</td>
<td><code>+, &#8211;</code></td>
<td>Addition / subtraction
</td>
</tr>
<tr VALIGN=top>
<td>Bit-wise:</td>
<td><code>&amp;</code></td>
<td>Integer AND
</td>
</tr>
<tr VALIGN=top>
<td>Bit-wise</td>
<td><code>^</code></td>
<td>Integer XOR
</td>
</tr>
<tr VALIGN=top>
<td>Bit-wise</td>
<td><code>|</code></td>
<td>Integer OR
</td>
</tr>
<tr VALIGN=top>
<td>Conditionals:</td>
<td><code>&gt;, &gt;=, &lt;, &lt;=</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Equality:</td>
<td><code>==, !=, =~, !~</code></td>
<td>=~ and !~ match regular expressions
</td>
</tr>
<tr VALIGN=top>
<td>Boolean:</td>
<td><code>&amp;&amp;, ||</code></td>
<td>Logical AND / OR
</td>
</tr>
</table>
<p> Expressions are computed using floating point mathematics, so &quot;10 / 4&quot; evaluates to 2.5 rather than 2. They may be written as integers in decimal or &quot;0x&quot; plus hexadecimal, and floating point with or without exponents.However operations that require integers first do an implicit type conversion, so &quot;7.9 % 5&quot; is 2 and &quot;7.9 &amp; 4.1&quot; is equivalent to &quot;7 &amp; 4&quot;, which is 4. Strings are always specified using double quotes. To get a double quote in a string, use backslash. Similarly a double backslash is used to get a literal backslash. For example <code>ab\&quot;c\d</code> is the string <code>ab&quot;c\d</code>. </p>
<p> Comparison operators are evaluated as a match being 1 and a mismatch being 0, thus &quot;(2 &gt; 1) + (3 &lt; 5)&quot; evaluates as 2. All comparisons involving undefined (null) values are deemed to be false. </p>
<p> The variables are where the file format specifics are accessed from the expression. The variables correspond to SAM fields, for example to find paired alignments with high mapping quality and a very large insert size, we may use the expression &quot;<code>mapq &gt;= 30 &amp;&amp; (tlen &gt;= 100000 || tlen &lt;= -100000)</code>&quot;. Valid variable names and their data types are: </p>
<table>
<tr VALIGN=top>
<td><code>endpos</code></td>
<td>int</td>
<td>Alignment end position (1-based)
</td>
</tr>
<tr VALIGN=top>
<td><code>flag</code></td>
<td>int</td>
<td>Combined FLAG field
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.paired</code></td>
<td>int</td>
<td>Single bit, 0 or 1
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.proper_pair</code></td>
<td>int</td>
<td>Single bit, 0 or 2
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.unmap</code></td>
<td>int</td>
<td>Single bit, 0 or 4
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.munmap</code></td>
<td>int</td>
<td>Single bit, 0 or 8
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.reverse</code></td>
<td>int</td>
<td>Single bit, 0 or 16
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.mreverse</code></td>
<td>int</td>
<td>Single bit, 0 or 32
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.read1</code></td>
<td>int</td>
<td>Single bit, 0 or 64
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.read2</code></td>
<td>int</td>
<td>Single bit, 0 or 128
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.secondary</code></td>
<td>int</td>
<td>Single bit, 0 or 256
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.qcfail</code></td>
<td>int</td>
<td>Single bit, 0 or 512
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.dup</code></td>
<td>int</td>
<td>Single bit, 0 or 1024
</td>
</tr>
<tr VALIGN=top>
<td><code>flag.supplementary</code></td>
<td>int</td>
<td>Single bit, 0 or 2048
</td>
</tr>
<tr VALIGN=top>
<td><code>library</code></td>
<td>string</td>
<td>Library (LB header via RG)
</td>
</tr>
<tr VALIGN=top>
<td><code>mapq</code></td>
<td>int</td>
<td>Mapping quality
</td>
</tr>
<tr VALIGN=top>
<td><code>mpos</code></td>
<td>int</td>
<td>Synonym for pnext
</td>
</tr>
<tr VALIGN=top>
<td><code>mrefid</code></td>
<td>int</td>
<td>Mate reference number (0 based)
</td>
</tr>
<tr VALIGN=top>
<td><code>mrname</code></td>
<td>string</td>
<td>Synonym for rnext
</td>
</tr>
<tr VALIGN=top>
<td><code>ncigar</code></td>
<td>int</td>
<td>Number of cigar operations
</td>
</tr>
<tr VALIGN=top>
<td><code>pnext</code></td>
<td>int</td>
<td>Mate&#8217;s alignment position (1-based)
</td>
</tr>
<tr VALIGN=top>
<td><code>pos</code></td>
<td>int</td>
<td>Alignment position (1-based)
</td>
</tr>
<tr VALIGN=top>
<td><code>qlen</code></td>
<td>int</td>
<td>Alignment length: no. query bases
</td>
</tr>
<tr VALIGN=top>
<td><code>qname</code></td>
<td>string</td>
<td>Query name
</td>
</tr>
<tr VALIGN=top>
<td><code>qual</code></td>
<td>string</td>
<td>Quality values (raw, 0 based)
</td>
</tr>
<tr VALIGN=top>
<td><code>refid</code></td>
<td>int</td>
<td>Integer reference number (0 based)
</td>
</tr>
<tr VALIGN=top>
<td><code>rlen</code></td>
<td>int</td>
<td>Alignment length: no. reference bases
</td>
</tr>
<tr VALIGN=top>
<td><code>rname</code></td>
<td>string</td>
<td>Reference name
</td>
</tr>
<tr VALIGN=top>
<td><code>rnext</code></td>
<td>string</td>
<td>Mate&#8217;s reference name
</td>
</tr>
<tr VALIGN=top>
<td><code>sclen</code></td>
<td>int</td>
<td>Number of soft-clipped bases
</td>
</tr>
<tr VALIGN=top>
<td><code>seq</code></td>
<td>string</td>
<td>Sequence
</td>
</tr>
<tr VALIGN=top>
<td><code>tlen</code></td>
<td>int</td>
<td>Template length (insert size)
</td>
</tr>
<tr VALIGN=top>
<td><code>[XX]</code></td>
<td>int / string</td>
<td>XX tag value
</td>
</tr>
</table>
<p> Flags are returned either as the whole flag value or by checking for a single bit. Hence the filter expression <code>flag.dup</code> is equivalent to <code>flag &amp; 1024</code>. </p>
<p> &quot;qlen&quot; and &quot;rlen&quot; are measured using the CIGAR string to count the number of query (sequence) and reference bases consumed. Note &quot;qlen&quot; may not exactly match the length of the &quot;seq&quot; field if the sequence is &quot;*&quot;. &quot;sclen&quot; is the number of soft-clipped bases. When combined in &quot;qlen-sclen&quot; it can give the number of sequence bases used in the alignment, distinguishing between global alignment and local alignment length. </p>
<p> &quot;endpos&quot; is the (1-based inclusive) position of the rightmost mapped base of the read, as measured using the CIGAR string, and for mapped reads is equivalent to &quot;pos+rlen-1&quot;. For unmapped reads, it is the same as &quot;pos&quot;. </p>
<p> Reference names may be matched either by their string forms (&quot;rname&quot; and &quot;mrname&quot;) or as the Nth <code>@SQ</code> line (counting from zero) as stored in BAM using &quot;tid&quot; and &quot;mtid&quot; respectively. </p>
<p> Auxiliary tags are described in square brackets and these expand to either integer or string as defined by the tag itself (<code>XX:Z:</code><i>string</i> or <code>XX:i:</code><i>int</i>). For example <code>[NM]&gt;=10</code> can be used to look for alignments with many mismatches and <code>[RG]=~&quot;grp[ABC]-&quot;</code> will match the read-group string. </p>
<p> If no comparison is used with an auxiliary tag it is taken simply to be a test for the existence of that tag. So <code>[NM]</code> will return any record containing an NM tag, even if that tag is zero (<code>NM:i:0</code>). In htslib &lt;= 1.15 negating this with <code>![NM]</code> gave misleading results as it was true if the tag did not exist or did exist but was zero. Now this is strictly does-not-exist. An explicit <code>exists([NM])</code> and <code>!exists([NM])</code> function has also been added to make this intention clear. </p>
<p> Similarly in htslib &lt;= 1.15 using <code>[NM]!=0</code> was true both when the tag existed and was not zero as well as when the tag did not exist. From 1.16 onwards all comparison operators are only true for tags that exist, so <code>[NM]!=0</code> works as expected. </p>
<p> Some simple functions are available to operate on strings. These treat the strings as arrays of bytes, permitting their length, minimum, maximum and average values to be computed. These are useful for processing Quality Scores. </p>
<table>
<tr VALIGN=top>
<td><code>length(x)</code></td>
<td>Length of the string (excluding nul char)
</td>
</tr>
<tr VALIGN=top>
<td><code>min(x)</code></td>
<td>Minimum byte value in the string
</td>
</tr>
<tr VALIGN=top>
<td><code>max(x)</code></td>
<td>Maximum byte value in the string
</td>
</tr>
<tr VALIGN=top>
<td><code>avg(x)</code></td>
<td>Average byte value in the string
</td>
</tr>
</table>
<p> Note that &quot;avg&quot; is a floating point value and it may be NAN for empty strings. This means that &quot;avg(qual)&quot; does not produce an error for records that have both seq and qual of &quot;*&quot;. NAN values will fail any conditional checks, so e.g. &quot;avg(qual) &gt; 20&quot; works and will not report these records. NAN also fails all equality, &lt; and &gt; comparisons, and returns zero when given as an argument to the <code>exists</code> function. It can be negated with <code>!x</code> in which case it becomes true. </p>
<p> Functions that operate on both strings and numerics: </p>
<table>
<tr VALIGN=top>
<td><code>exists(x)</code></td>
<td>True if the value exists (or is explicitly true).
</td>
</tr>
<tr VALIGN=top>
<td><code>default(x,d)</code></td>
<td>Value <code>x</code> if it exists or <code>d</code> if not.
</td>
</tr>
</table>
<p> Functions that apply only to numeric values: </p>
<table>
<tr VALIGN=top>
<td><code>sqrt(x)</code></td>
<td>Square root of <code>x</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>log(x)</code></td>
<td>Natural logarithm of <code>x</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>pow(x, y)</code></td>
<td>Power function, <code>x</code> to the power of <code>y</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>exp(x)</code></td>
<td>Base-e exponential, equivalent to <code>pow(e,x)</code>
</td>
</tr>
</table>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>HTS_PATH</code></p>
<dd> A colon-separated list of directories in which to search for HTSlib plugins. If $HTS_PATH starts or ends with a colon or contains a double colon (<code>::</code>), the built-in list of directories is searched at that point in the search. </p>
<p> If no HTS_PATH variable is defined, the built-in list of directories specified when HTSlib was built is used, which typically includes <code>/usr/local/libexec/htslib</code> and similar directories. </p>
<dt><code>REF_PATH</code></p>
<dd> A colon separated (semi-colon on Windows) list of locations in which to look for sequences identified by their MD5sums. This can be either a list of directories or URLs. Note that if a URL is included then the colon in http:// and ftp:// and the optional port number will be treated as part of the URL and not a PATH field separator. For URLs, the text <code>%s</code> will be replaced by the MD5sum being read. </p>
<p> If no REF_PATH has been specified it will default to <code><a rel="nofollow" href="http://www.ebi.ac.uk/ena/cram/md5/%s">http://www.ebi.ac.uk/ena/cram/md5/%s</a></code> and if REF_CACHE is also unset, it will be set to <code>$XDG_CACHE_HOME/hts-ref/%2s/%2s/%s</code>. If <code>$XDG_CACHE_HOME</code> is unset, <code>$HOME/.cache</code> (or a local system temporary directory if no home directory is found) will be used similarly. </p>
<dt><code>REF_CACHE</code></p>
<dd> This can be defined to a single location housing a local cache of references. Upon downloading a reference it will be stored in the location pointed to by REF_CACHE. REF_CACHE will be searched before attempting to load via the REF_PATH search list. If no REF_PATH is defined, both REF_PATH and REF_CACHE will be automatically set (see above), but if REF_PATH is defined and REF_CACHE not then no local cache is used. </p>
<p> To avoid many files being stored in the same directory, REF_CACHE may be defined as a pattern using <code>%</code><i>num</i><code>s</code> to consume <i>num</i> characters of the MD5sum and <code>%s</code> to consume all remaining characters. If REF_CACHE lacks <code>%s</code> then it will get an implicit <code>/%s</code> appended. </p>
<p> To aid population of the REF_CACHE directory a script <code>misc/seq_cache_populate.pl</code> is provided in the Samtools distribution. This takes a fasta file or a directory of fasta files and generates the MD5sum named files. </p>
<p> For example if you use <code>seq_cache_populate -subdirs 2 -root /local/ref_cache</code> to create 2 nested subdirectories (the default), each consuming 2 characters of the MD5sum, then REF_CACHE must be set to <code>/local/ref_cache/%2s/%2s/%s</code>.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>o</p>
<dd> Import SAM to BAM when <code>@SQ</code> lines are present in the header: </p>
<pre>
samtools view -b aln.sam &gt; aln.bam
</pre>
<p> If <code>@SQ</code> lines are absent: </p>
<pre>
samtools faidx ref.fa
samtools view -bt ref.fa.fai aln.sam &gt; aln.bam
</pre>
<p> where <i>ref.fa.fai</i> is generated automatically by the <code>faidx</code> command. </p>
<dt>o</p>
<dd> Convert a BAM file to a CRAM file using a local reference sequence. </p>
<pre>
samtools view -C -T ref.fa aln.bam &gt; aln.cram
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Heng Li from the Sanger Institute wrote the original C version of samtools. Bob Handsaker from the Broad Institute implemented the BGZF library. Petr Danecek and Heng Li wrote the VCF/BCF implementation. James Bonfield from the Sanger Institute developed the CRAM implementation. Other large code contributions have been made by John Marshall, Rob Davies, Martin Pollard, Andrew Whitwham, Valeriu Ohan, Vasudeva Sarma (all while primarily at the Sanger Institute), with numerous other smaller but valuable contributions. See the per-command manual pages for further authorship. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-samtools-addreplacerg/">samtools-addreplacerg</a></i>(1), <i><a href="/docs/linux/man/1-samtools-ampliconclip/">samtools-ampliconclip</a></i>(1), <i><a href="/docs/linux/man/1-samtools-ampliconstats/">samtools-ampliconstats</a></i>(1), <i><a href="/docs/linux/man/1-samtools-bedcov/">samtools-bedcov</a></i>(1), <i><a href="/docs/linux/man/1-samtools-calmd/">samtools-calmd</a></i>(1), <i><a href="/docs/linux/man/1-samtools-cat/">samtools-cat</a></i>(1), <i><a href="/docs/linux/man/1-samtools-collate/">samtools-collate</a></i>(1), <i><a href="/docs/linux/man/1-samtools-consensus/">samtools-consensus</a></i>(1), <i><a href="/docs/linux/man/1-samtools-coverage/">samtools-coverage</a></i>(1), <i><a href="/docs/linux/man/1-samtools-cram-size/">samtools-cram-size</a></i>(1), <i><a href="/docs/linux/man/1-samtools-depad/">samtools-depad</a></i>(1), <i><a href="/docs/linux/man/1-samtools-depth/">samtools-depth</a></i>(1), <i><a href="/docs/linux/man/1-samtools-dict/">samtools-dict</a></i>(1), <i><a href="/docs/linux/man/1-samtools-faidx/">samtools-faidx</a></i>(1), <i><a href="/docs/linux/man/1-samtools-fasta/">samtools-fasta</a></i>(1), <i><a href="/docs/linux/man/1-samtools-fastq/">samtools-fastq</a></i>(1), <i><a href="/docs/linux/man/1-samtools-fixmate/">samtools-fixmate</a></i>(1), <i><a href="/docs/linux/man/1-samtools-flags/">samtools-flags</a></i>(1), <i><a href="/docs/linux/man/1-samtools-flagstat/">samtools-flagstat</a></i>(1), <i><a href="/docs/linux/man/1-samtools-fqidx/">samtools-fqidx</a></i>(1), <i><a href="/docs/linux/man/1-samtools-head/">samtools-head</a></i>(1), <i><a href="/docs/linux/man/1-samtools-idxstats/">samtools-idxstats</a></i>(1), <i><a href="/docs/linux/man/1-samtools-import/">samtools-import</a></i>(1), <i><a href="/docs/linux/man/1-samtools-index/">samtools-index</a></i>(1), <i><a href="/docs/linux/man/1-samtools-markdup/">samtools-markdup</a></i>(1), <i><a href="/docs/linux/man/1-samtools-merge/">samtools-merge</a></i>(1), <i><a href="/docs/linux/man/1-samtools-mpileup/">samtools-mpileup</a></i>(1), <i><a href="/docs/linux/man/1-samtools-phase/">samtools-phase</a></i>(1), <i><a href="/docs/linux/man/1-samtools-quickcheck/">samtools-quickcheck</a></i>(1), <i><a href="/docs/linux/man/1-samtools-reference/">samtools-reference</a></i>(1), <i><a href="/docs/linux/man/1-samtools-reheader/">samtools-reheader</a></i>(1), <i><a href="/docs/linux/man/1-samtools-reset/">samtools-reset</a></i>(1), <i><a href="/docs/linux/man/1-samtools-rmdup/">samtools-rmdup</a></i>(1), <i><a href="/docs/linux/man/1-samtools-sort/">samtools-sort</a></i>(1), <i><a href="/docs/linux/man/1-samtools-split/">samtools-split</a></i>(1), <i><a href="/docs/linux/man/1-samtools-stats/">samtools-stats</a></i>(1), <i><a href="/docs/linux/man/1-samtools-targetcut/">samtools-targetcut</a></i>(1), <i><a href="/docs/linux/man/1-samtools-tview/">samtools-tview</a></i>(1), <i><a href="/docs/linux/man/1-samtools-view/">samtools-view</a></i>(1), <i><a href="/docs/linux/man/1-bcftools/">bcftools</a></i>(1), <i><a href="/docs/linux/man/5-sam/">sam</a></i>(5), <i><a href="/docs/linux/man/1-tabix/">tabix</a></i>(1) </p>
<p> Samtools website: &lt;<a rel="nofollow" href="http://www.htslib.org/">http://www.htslib.org/</a>&gt;<br />
 File format specification of SAM/BAM,CRAM,VCF/BCF: &lt;<a rel="nofollow" href="http://samtools.github.io/hts-specs">http://samtools.github.io/hts-specs</a>&gt;<br />
 Samtools latest source: &lt;<a rel="nofollow" href="https://github.com/samtools/samtools">https://github.com/samtools/samtools</a>&gt;<br />
 HTSlib latest source: &lt;<a rel="nofollow" href="https://github.com/samtools/htslib">https://github.com/samtools/htslib</a>&gt;<br />
 Bcftools website: &lt;<a rel="nofollow" href="http://samtools.github.io/bcftools">http://samtools.github.io/bcftools</a>&gt; </p>
<h2>Index</h2>
