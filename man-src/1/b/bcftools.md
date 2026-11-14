---
title: "bcftools(1)"
name: "bcftools"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcftools/"
description: "bcftools – utilities for variant calling and manipulating VCFs and BCFs."
---

<h2 class="name">NAME</h2>
<p> bcftools &#8211; utilities for variant calling and manipulating VCFs and BCFs. </p>
<h2>SYNOPSIS</h2>
<p> <code>bcftools</code> [&#8211;version|&#8211;version-only] [&#8211;help] [<i>COMMAND</i>] [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> BCFtools is a set of utilities that manipulate variant calls in the Variant Call Format (VCF) and its binary counterpart BCF. All commands work transparently with both VCFs and BCFs, both uncompressed and BGZF-compressed. </p>
<p> Most commands accept VCF, bgzipped VCF and BCF with filetype detected automatically even when streaming from a pipe. Indexed VCF and BCF will work in all situations. Un-indexed VCF and BCF and streams will work in most, but not all situations. In general, whenever multiple VCFs are read simultaneously, they must be indexed and therefore also compressed. (Note that files with non-standard index names can be accessed as e.g. &quot;bcftools view -r X:2928329 file.vcf.gz##idx##non-standard-index-name&quot;.) </p>
<p> BCFtools is designed to work on a stream. It regards an input file &quot;-&quot; as the standard input (stdin) and outputs to the standard output (stdout). Several commands can thus be combined with Unix pipes.</p>
<h3>VERSION</h3>
<p> This manual page was last updated <code>2023-03-28 13:46 BST</code> and refers to bcftools git version <code>1.17-15-gf2d2fdf8+</code>.</p>
<h3>BCF1</h3>
<p> The obsolete BCF1 format output by versions of samtools &lt;= 0.1.19 is <code>not</code> compatible with this version of bcftools. To read BCF1 files one can use the view command from old versions of bcftools packaged with samtools versions &lt;= 0.1.19 to convert to VCF, which can then be read by this version of bcftools. </p>
<dl>
<dt>
<dd>
<pre>
    samtools-0.1.19/bcftools/bcftools view file.bcf1 | bcftools view
</pre>
</dl>
<h3>VARIANT CALLING</h3>
<p> See <i>bcftools call</i> for variant calling from the output of the <i>samtools mpileup</i> command. In versions of samtools &lt;= 0.1.19 calling was done with <i>bcftools view</i>. Users are now required to choose between the old samtools calling model (<i>-c/&#8211;consensus-caller</i>) and the new multiallelic calling model (<i>-m/&#8211;multiallelic-caller</i>). The multiallelic calling model is recommended for most tasks.</p>
<h3>FILTERING EXPRESSIONS</h3>
<p> See <code>EXPRESSIONS</code></p>
<h2>LIST OF COMMANDS</h2>
<p> For a full list of available commands, run <code>bcftools</code> without arguments. For a full list of available options, run <code>bcftools</code> <i>COMMAND</i> without arguments. </p>
<dl>
<dt>
<dd> &bull; <code>annotate</code> .. edit VCF files, add or remove annotations</dl>
<dl>
<dt>
<dd> &bull; <code>call</code> .. SNP/indel calling (former &quot;view&quot;)</dl>
<dl>
<dt>
<dd> &bull; <code>cnv</code> .. Copy Number Variation caller</dl>
<dl>
<dt>
<dd> &bull; <code>concat</code> .. concatenate VCF/BCF files from the same set of samples</dl>
<dl>
<dt>
<dd> &bull; <code>consensus</code> .. create consensus sequence by applying VCF variants</dl>
<dl>
<dt>
<dd> &bull; <code>convert</code> .. convert VCF/BCF to other formats and back</dl>
<dl>
<dt>
<dd> &bull; <code>csq</code> .. haplotype aware consequence caller</dl>
<dl>
<dt>
<dd> &bull; <code>filter</code> .. filter VCF/BCF files using fixed thresholds</dl>
<dl>
<dt>
<dd> &bull; <code>gtcheck</code> .. check sample concordance, detect sample swaps and contamination</dl>
<dl>
<dt>
<dd> &bull; <code>head</code> .. view VCF/BCF file headers</dl>
<dl>
<dt>
<dd> &bull; <code>index</code> .. index VCF/BCF</dl>
<dl>
<dt>
<dd> &bull; <code>isec</code> .. intersections of VCF/BCF files</dl>
<dl>
<dt>
<dd> &bull; <code>merge</code> .. merge VCF/BCF files files from non-overlapping sample sets</dl>
<dl>
<dt>
<dd> &bull; <code>mpileup</code> .. multi-way pileup producing genotype likelihoods</dl>
<dl>
<dt>
<dd> &bull; <code>norm</code> .. normalize indels</dl>
<dl>
<dt>
<dd> &bull; <code>plugin</code> .. run user-defined plugin</dl>
<dl>
<dt>
<dd> &bull; <code>polysomy</code> .. detect contaminations and whole-chromosome aberrations</dl>
<dl>
<dt>
<dd> &bull; <code>query</code> .. transform VCF/BCF into user-defined formats</dl>
<dl>
<dt>
<dd> &bull; <code>reheader</code> .. modify VCF/BCF header, change sample names</dl>
<dl>
<dt>
<dd> &bull; <code>roh</code> .. identify runs of homo/auto-zygosity</dl>
<dl>
<dt>
<dd> &bull; <code>sort</code> .. sort VCF/BCF files</dl>
<dl>
<dt>
<dd> &bull; <code>stats</code> .. produce VCF/BCF stats (former vcfcheck)</dl>
<dl>
<dt>
<dd> &bull; <code>view</code> .. subset, filter and convert VCF and BCF files</dl>
<h2>LIST OF SCRIPTS</h2>
<p> Some helper scripts are bundled with the bcftools code. </p>
<dl>
<dt>
<dd> &bull; <code>gff2gff</code> .. converts a GFF file to the format required by <code>csq</code></dl>
<dl>
<dt>
<dd> &bull; <code>plot-vcfstats</code> .. plots the output of <code>stats</code></dl>
<h2>COMMANDS AND OPTIONS</h2>
<h3>Common Options</h3>
<p> The following options are common to many bcftools commands. See usage for specific commands to see if they apply. </p>
<p> <i>FILE</i></p>
<dl>
<dt>
<dd> Files can be both VCF or BCF, uncompressed or BGZF-compressed. The file &quot;-&quot; is interpreted as standard input. Some tools may require tabix- or CSI-indexed files.</dl>
<p> <code>-c, &#8211;collapse</code> <i>snps</i>|<i>indels</i>|<i>both</i>|<i>all</i>|<i>some</i>|<i>none</i>|<i>id</i></p>
<dl>
<dt>
<dd> Controls how to treat records with duplicate positions and defines compatible records across multiple input files. Here by &quot;compatible&quot; we mean records which should be considered as identical by the tools. For example, when performing line intersections, the desire may be to consider as identical all sites with matching positions (<code>bcftools isec -c</code> <i>all</i>), or only sites with matching variant type (<code>bcftools isec -c</code> <i>snps</i>~ <code>-c</code> <i>indels</i>), or only sites with all alleles identical (<code>bcftools isec -c</code> <i>none</i>). </p>
<p> <i>none</i></p>
<dl>
<dt>
<dd> only records with identical REF and ALT alleles are compatible</dl>
<p> <i>some</i></p>
<dl>
<dt>
<dd> only records where some subset of ALT alleles match are compatible</dl>
<p> <i>all</i></p>
<dl>
<dt>
<dd> all records are compatible, regardless of whether the ALT alleles match or not. In the case of records with the same position, only the first will be considered and appear on output.</dl>
<p> <i>snps</i></p>
<dl>
<dt>
<dd> any SNP records are compatible, regardless of whether the ALT alleles match or not. For duplicate positions, only the first SNP record will be considered and appear on output.</dl>
<p> <i>indels</i></p>
<dl>
<dt>
<dd> all indel records are compatible, regardless of whether the REF and ALT alleles match or not. For duplicate positions, only the first indel record will be considered and appear on output.</dl>
<p> <i>both</i></p>
<dl>
<dt>
<dd> abbreviation of &quot;<code>-c</code> <i>indels</i>~ <code>-c</code> <i>snps</i>&quot;</dl>
<p> <i>id</i></p>
<dl>
<dt>
<dd> only records with identical ID column are compatible. Supported by <code>bcftools merge</code> only.</dl>
</dl>
<p> <code>-f, &#8211;apply-filters</code> <i>LIST</i></p>
<dl>
<dt>
<dd> Skip sites where FILTER column does not contain any of the strings listed in <i>LIST</i>. For example, to include only sites which have no filters set, use <code>-f</code> <i>.,PASS</i>.</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> Do not append version and command line information to the output VCF header.</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> When output consists of a single stream, write it to <i>FILE</i> rather than to standard output, where it is written by default. The file type is determined automatically from the file name suffix and in case a conflicting <code>-O</code> option is given, the file name suffix takes precedence.</dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> Output compressed BCF (<i>b</i>), uncompressed BCF (<i>u</i>), compressed VCF (<i>z</i>), uncompressed VCF (<i>v</i>). Use the -Ou option when piping between bcftools subcommands to speed up performance by removing unnecessary compression/decompression and VCF&larr;&rarr;BCF conversion. ~ The compression level of the compressed formats (<i>b</i> and <i>z</i>) can be set by by appending a number between 0-9.</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:beg-end</i>|<i>chr:beg-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> Comma-separated list of regions, see also <code>-R, &#8211;regions-file</code>. Overlapping records are matched even when the starting coordinate is outside of the region, unlike the <code>-t/-T</code> options where only the POS coordinate is checked. Note that <code>-r</code> cannot be used in combination with <code>-R</code>.</dl>
<p> <code>-R, &#8211;regions-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> Regions can be specified either on command line or in a VCF, BED, or tab-delimited file (the default). The columns of the tab-delimited file can contain either positions (two-column format: CHROM, POS) or intervals (three-column format: CHROM, BEG, END), but not both. Positions are 1-based and inclusive. The columns of the tab-delimited BED file are also CHROM, POS and END (trailing columns are ignored), but coordinates are 0-based, half-open. To indicate that a file be treated as BED rather than the 1-based tab-delimited file, the file must have the &quot;.bed&quot; or &quot;.bed.gz&quot; suffix (case-insensitive). Uncompressed files are stored in memory, while bgzip-compressed and tabix-indexed region files are streamed. Note that sequence names must match exactly, &quot;chr20&quot; is not the same as &quot;20&quot;. Also note that chromosome ordering in <i>FILE</i> will be respected, the VCF will be processed in the order in which chromosomes first appear in <i>FILE</i>. However, within chromosomes, the VCF will always be processed in ascending genomic coordinate order no matter what order they appear in <i>FILE</i>. Note that overlapping regions in <i>FILE</i> can result in duplicated out of order positions in the output. This option requires indexed VCF/BCF files. Note that <code>-R</code> cannot be used in combination with <code>-r</code>.</dl>
<p> <code>&#8211;regions-overlap</code> <i>pos</i>|<i>record</i>|<i>variant</i>|<i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> This option controls how overlapping records are determined: set to <code>pos</code> or <code>0</code> if the VCF record has to have POS inside a region (this corresponds to the default behavior of <code>-t/-T</code>); set to <code>record</code> or <code>1</code> if also overlapping records with POS outside a region should be included (this is the default behavior of <code>-r/-R</code>, and includes indels with POS at the end of a region, which are technically outside the region); or set to <code>variant</code> or <code>2</code> to include only true overlapping variation (compare the full VCF representation &quot;TA&gt;T-&quot; vs the true sequence variation &quot;A&gt;-&quot;).</dl>
<p> <code>-s, &#8211;samples</code> [^]<i>LIST</i></p>
<dl>
<dt>
<dd> Comma-separated list of samples to include or exclude if prefixed with &quot;^.&quot; (Note that when multiple samples are to be excluded, the &quot;^&quot; prefix is still present only once, e.g. &quot;^SAMPLE1,SAMPLE2&quot;.) The sample order is updated to reflect that given on the command line. Note that in general tags such as INFO/AC, INFO/AN, etc are not updated to correspond to the subset samples. <code>bcftools view</code> is the exception where some tags will be updated (unless the <code>-I, &#8211;no-update</code> option is used; see <code>bcftools view</code> documentation). To use updated tags for the subset in another command one can pipe from <code>view</code> into that command. For example:</dl>
<dl>
<dt>
<dd>
<pre>
    bcftools view -Ou -s sample1,sample2 file.vcf | bcftools query -f %INFO/AC	%INFO/AN

</pre>
</dl>
<p> <code>-S, &#8211;samples-file</code> [^]<i>FILE</i></p>
<dl>
<dt>
<dd> File of sample names to include or exclude if prefixed with &quot;^&quot;. One sample per line. See also the note above for the <code>-s, &#8211;samples</code> option. The sample order is updated to reflect that given in the input file. The command <code>bcftools call</code> accepts an optional second column indicating ploidy (0, 1 or 2) or sex (as defined by <code>&#8211;ploidy</code>, for example &quot;F&quot; or &quot;M&quot;), for example:</dl>
<dl>
<dt>
<dd>
<pre>
    sample1    1
    sample2    2
    sample3    2
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
    sample1    M
    sample2    F
    sample3    F
</pre>
</dl>
<p> If the second column is not present, the sex &quot;F&quot; is assumed. With <code>bcftools call -C</code> <i>trio</i>, PED file is expected. The program ignores the first column and the last indicates sex (1=male, 2=female), for example: </p>
<dl>
<dt>
<dd>
<pre>
    ignored_column  daughterA fatherA  motherA  2
    ignored_column  sonB      fatherB  motherB  1
</pre>
</dl>
<p> <code>-t, &#8211;targets</code> [^]<i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> Similar as <code>-r, &#8211;regions</code>, but the next position is accessed by streaming the whole VCF/BCF rather than using the tbi/csi index. Both <code>-r</code> and <code>-t</code> options can be applied simultaneously: <code>-r</code> uses the index to jump to a region and <code>-t</code> discards positions which are not in the targets. Unlike <code>-r</code>, targets can be prefixed with &quot;^&quot; to request logical complement. For example, &quot;^X,Y,MT&quot; indicates that sequences X, Y and MT should be skipped. Yet another difference between the <code>-t/-T</code> and <code>-r/-R</code> is that <code>-r/-R</code> checks for proper overlaps and considers both POS and the end position of an indel, while <code>-t/-T</code> considers the POS coordinate only (by default; see also <code>&#8211;regions-overlap</code> and <code>&#8211;targets-overlap</code>). Note that <code>-t</code> cannot be used in combination with <code>-T</code>.</dl>
<p> <code>-T, &#8211;targets-file</code> [^]<i>FILE</i></p>
<dl>
<dt>
<dd> Same <code>-t, &#8211;targets</code>, but reads regions from a file. Note that <code>-T</code> cannot be used in combination with <code>-t</code>. </p>
<p> With the <code>call -C</code> <i>alleles</i> command, third column of the targets file must be comma-separated list of alleles, starting with the reference allele. Note that the file must be compressed and indexed. Such a file can be easily created from a VCF using:</dl>
<dl>
<dt>
<dd>
<pre>
    bcftools query -f'%CHROM	%POS	%REF,%ALT
' file.vcf | bgzip -c &gt; als.tsv.gz &amp;&amp; tabix -s1 -b2 -e2 als.tsv.gz
</pre>
</dl>
<p> <code>&#8211;targets-overlap</code> <i>pos</i>|<i>record</i>|<i>variant</i>|<i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> Same as <code>&#8211;regions-overlap</code> but for <code>-t/-T</code>.</dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> Use multithreading with <i>INT</i> worker threads. The option is currently used only for the compression of the output stream, only when <i>&#8211;output-type</i> is <i>b</i> or <i>z</i>. Default: 0.</dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output files. Can be used only for compressed BCF and VCF output.</dl>
<h3>bcftools annotate <i>[OPTIONS]</i> <i>FILE</i></h3>
<p> Add or remove annotations. </p>
<p> <code>-a, &#8211;annotations</code> <i>file</i></p>
<dl>
<dt>
<dd> Bgzip-compressed and tabix-indexed file with annotations. The file can be VCF, BED, or a tab-delimited file with mandatory columns CHROM, POS (or, alternatively, FROM and TO), optional columns REF and ALT, and arbitrary number of annotation columns. BED files are expected to have the &quot;.bed&quot; or &quot;.bed.gz&quot; suffix (case-insensitive), otherwise a tab-delimited file is assumed. Note that in case of tab-delimited file, the coordinates POS, FROM and TO are one-based and inclusive. When REF and ALT are present, only matching VCF records will be annotated. If the END coordinate is present in the annotation file and given on command line as &quot;-c ~INFO/END&quot;, then VCF records will be matched also by the INFO/END coordinate. If ID is present in the annotation file and given as &quot;-c ~ID&quot;, then VCF records will be matched also by the ID column. ~<br />
 ~<br />
 When multiple ALT alleles are present in the annotation file (given as comma-separated list of alleles), at least one must match one of the alleles in the corresponding VCF record. Similarly, at least one alternate allele from a multi-allelic VCF record must be present in the annotation file. ~<br />
 ~<br />
 Missing values can be added by providing &quot;.&quot; in place of actual value and using the missing value modifier with <code>-c</code>, such as &quot;.TAG&quot;. ~<br />
 ~<br />
 Note that flag types, such as &quot;INFO/FLAG&quot;, can be annotated by including a field with the value &quot;1&quot; to set the flag, &quot;0&quot; to remove it, or &quot;.&quot; to keep existing flags. See also <code>-c, &#8211;columns</code> and <code>-h, &#8211;header-lines</code>.</dl>
<dl>
<dt>
<dd>
<pre>
    # Sample annotation file with columns CHROM, POS, STRING_TAG, NUMERIC_TAG
    1  752566  SomeString      5
    1  798959  SomeOtherString 6
</pre>
</dl>
<p> <code>-c, &#8211;columns</code> <i>list</i></p>
<dl>
<dt>
<dd> Comma-separated list of columns or tags to carry over from the annotation file (see also <code>-a, &#8211;annotations</code>). If the annotation file is not a VCF/BCF, <i>list</i> describes the columns of the annotation file and must include CHROM, POS (or, alternatively, FROM and TO), and optionally REF and ALT. Unused columns which should be ignored can be indicated by &quot;-&quot;. ~<br />
 ~<br />
 If the annotation file is a VCF/BCF, only the edited columns/tags must be present and their order does not matter. The columns ID, QUAL, FILTER, INFO and FORMAT can be edited, where INFO tags can be written both as &quot;INFO/TAG&quot; or simply &quot;TAG&quot;, and FORMAT tags can be written as &quot;FORMAT/TAG&quot; or &quot;FMT/TAG&quot;. The imported VCF annotations can be renamed as &quot;DST_TAG:=SRC_TAG&quot; or &quot;FMT/DST_TAG:=FMT/SRC_TAG&quot;. ~<br />
 ~<br />
 To carry over all INFO annotations, use &quot;INFO&quot;. To add all INFO annotations except &quot;TAG&quot;, use &quot;^INFO/TAG&quot;. By default, existing values are replaced. ~<br />
 ~<br />
 By default, existing tags are overwritten unless the source value is a missing value (i.e. &quot;.&quot;). If also missing values should be carried over (and overwrite existing tags), use &quot;.TAG&quot; instead of &quot;TAG&quot;. To add annotations without overwriting existing values (that is, to add tags that are absent or to add values to existing tags with missing values), use &quot;+TAG&quot; instead of &quot;TAG&quot;. These can be combined, for example &quot;.+TAG&quot; can be used to add TAG even if the source value is missing but only if TAG does not exist in the target file; existing tags will not be overwritten. To append to existing values (rather than replacing or leaving untouched), use &quot;=TAG&quot; (instead of &quot;TAG&quot; or &quot;+TAG&quot;). To replace only existing values without modifying missing annotations, use &quot;-TAG&quot;. To match the record also by ID or INFO/END, in addition to REF and ALT, use &quot;~ID&quot; or &quot;~INFO/END&quot;. If position needs to be replaced, mark the column with the new position as &quot;~POS&quot;. ~<br />
 ~<br />
 If the annotation file is not a VCF/BCF, all new annotations must be defined via <code>-h, &#8211;header-lines</code>. ~<br />
 ~<br />
 See also the <code>-l, &#8211;merge-logic</code> option.</dl>
<p> <code>-C, &#8211;columns-file</code> <i>file</i></p>
<dl>
<dt>
<dd> Read the list of columns from a file (normally given via the <code>-c, &#8211;columns</code> option). &quot;-&quot; to skip a column of the annotation file. One column name per row, an additional space- or tab-separated field can be present to indicate the merge logic (normally given via the <code>-l, &#8211;merge-logic</code> option). This is useful when many annotations are added at once.</dl>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> continue even when parsing errors, such as undefined tags, are encountered. Note this can be an unsafe operation and can result in corrupted BCF files. If this option is used, make sure to sanity check the result thoroughly.</dl>
<p> <code>-h, &#8211;header-lines</code> <i>file</i></p>
<dl>
<dt>
<dd> Lines to append to the VCF header, see also <code>-c, &#8211;columns</code> and <code>-a, &#8211;annotations</code>. For example:</dl>
<dl>
<dt>
<dd>
<pre>
    ##INFO=&lt;ID=NUMERIC_TAG,Number=1,Type=Integer,Description=&quot;Example header line&quot;&gt;
    ##INFO=&lt;ID=STRING_TAG,Number=1,Type=String,Description=&quot;Yet another header line&quot;&gt;
</pre>
</dl>
<p> <code>-I, &#8211;set-id</code> [+]<i>FORMAT</i></p>
<dl>
<dt>
<dd> assign ID on the fly. The format is the same as in the <code>query</code> command (see below). By default all existing IDs are replaced. If the format string is preceded by &quot;+&quot;, only missing IDs will be set. For example, one can use</dl>
<dl>
<dt>
<dd>
<pre>
    bcftools annotate --set-id +'%CHROM\_%POS\_%REF\_%FIRST_ALT' file.vcf
</pre>
</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-k, &#8211;keep-sites</code></p>
<dl>
<dt>
<dd> keep sites which do not pass <code>-i</code> and <code>-e</code> expressions instead of discarding them</dl>
<p> <code>-l, &#8211;merge-logic</code> <i>tag:first</i>|<i>append</i>|<i>append-missing</i>|<i>unique</i>|<i>sum</i>|<i>avg</i>|<i>min</i>|<i>max</i>[,&#8230;]</p>
<dl>
<dt>
<dd> When multiple regions overlap a single record, this option defines how to treat multiple annotation values when setting <i>tag</i> in the destination file: use the first encountered value ignoring the rest (<i>first</i>); append allowing duplicates (<i>append</i>); append even if the appended value is missing, i.e. is a dot (<i>append-missing</i>); append discarding duplicate values (<i>unique</i>); sum the values (<i>sum</i>, numeric fields only); average the values (<i>avg</i>); use the minimum value (<i>min</i>) or the maximum (<i>max</i>). + Note that this option is intended for use with BED or TAB-delimited annotation files only. Moreover, it is effective only when either <i>REF</i> and <i>ALT</i> or <i>BEG</i> and <i>END</i> <code>&#8211;columns</code> are present . + Multiple rules can be given either as a comma-separated list or giving the option multiple times. This is an experimental feature.</dl>
<p> <code>-m, &#8211;mark-sites</code> <i>TAG</i></p>
<dl>
<dt>
<dd> annotate sites which are present (&quot;+&quot;) or absent (&quot;-&quot;) in the <code>-a</code> file with a new INFO/TAG flag</dl>
<p> <code>&#8211;min-overlap</code> <i>ANN</i>:&#8217;VCF&#8217;</p>
<dl>
<dt>
<dd> minimum overlap required as a fraction of the variant in the annotation <code>-a</code> file (<i>ANN</i>), in the target VCF file (<i>:VCF</i>), or both for reciprocal overlap (<i>ANN:VCF</i>). By default overlaps of arbitrary length are sufficient. The option can be used only with the tab-delimited annotation <code>-a</code> file and with <i>BEG</i> and <i>END</i> columns present.</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;pair-logic</code> <i>snps</i>|<i>indels</i>|<i>both</i>|<i>all</i>|<i>some</i>|<i>exact</i></p>
<dl>
<dt>
<dd> Controls how to match records from the annotation file to the target VCF. Effective only when <code>-a</code> is a VCF or BCF. The option replaces the former uninuitive <code>&#8211;collapse</code>. See <code>Common Options</code> for more.</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;rename-annots</code> <i>file</i></p>
<dl>
<dt>
<dd> rename annotations according to the map in <i>file</i>, with &quot;old_name new_name
&quot; pairs separated by whitespaces, each on a separate line. The old name must be prefixed with the annotation type: INFO, FORMAT, or FILTER.</dl>
<p> <code>&#8211;rename-chrs</code> <i>file</i></p>
<dl>
<dt>
<dd> rename chromosomes according to the map in <i>file</i>, with &quot;old_name new_name
&quot; pairs separated by whitespaces, each on a separate line.</dl>
<p> <code>-s, &#8211;samples</code> [^]<i>LIST</i></p>
<dl>
<dt>
<dd> subset of samples to annotate, see also <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> subset of samples to annotate. If the samples are named differently in the target VCF and the <code>-a, &#8211;annotations</code> VCF, the name mapping can be given as &quot;src_name dst_name
&quot;, separated by whitespaces, each pair on a separate line.</dl>
<p> <code>&#8211;single-overlaps</code></p>
<dl>
<dt>
<dd> use this option to keep memory requirements low with very large annotation files. Note, however, that this comes at a cost, only single overlapping intervals are considered in this mode. This was the default mode until the commit af6f0c9 (Feb 24 2019).</dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-x, &#8211;remove</code> <i>list</i></p>
<dl>
<dt>
<dd> List of annotations to remove. Use &quot;FILTER&quot; to remove all filters or &quot;FILTER/SomeFilter&quot; to remove a specific filter. Similarly, &quot;INFO&quot; can be used to remove all INFO tags and &quot;FORMAT&quot; to remove all FORMAT tags except GT. To remove all INFO tags except &quot;FOO&quot; and &quot;BAR&quot;, use &quot;^INFO/FOO,INFO/BAR&quot; (and similarly for FORMAT and FILTER). &quot;INFO&quot; can be abbreviated to &quot;INF&quot; and &quot;FORMAT&quot; to &quot;FMT&quot;.</dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<p> <code>Examples:</code> </p>
<dl>
<dt>
<dd>
<pre>
    # Remove three fields
    bcftools annotate -x ID,INFO/DP,FORMAT/DP file.vcf.gz
    # Remove all INFO fields and all FORMAT fields except for GT and PL
    bcftools annotate -x INFO,^FORMAT/GT,FORMAT/PL file.vcf
    # Add ID, QUAL and INFO/TAG, not replacing TAG if already present
    bcftools annotate -a src.bcf -c ID,QUAL,+TAG dst.bcf
    # Carry over all INFO and FORMAT annotations except FORMAT/GT
    bcftools annotate -a src.bcf -c INFO,^FORMAT/GT dst.bcf
    # Annotate from a tab-delimited file with six columns (the fifth is ignored),
    # first indexing with tabix. The coordinates are 1-based.
    tabix -s1 -b2 -e2 annots.tab.gz
    bcftools annotate -a annots.tab.gz -h annots.hdr -c CHROM,POS,REF,ALT,-,TAG file.vcf
    # Annotate from a tab-delimited file with regions (1-based coordinates, inclusive)
    tabix -s1 -b2 -e3 annots.tab.gz
    bcftools annotate -a annots.tab.gz -h annots.hdr -c CHROM,FROM,TO,TAG input.vcf
    # Annotate from a bed file (0-based coordinates, half-closed, half-open intervals)
    bcftools annotate -a annots.bed.gz -h annots.hdr -c CHROM,FROM,TO,TAG input.vcf
    # Transfer the INFO/END tag, matching by POS,REF,ALT and ID. This example assumes
    # that INFO/END is already present in the VCF header.
    bcftools annotate -a annots.tab.gz  -c CHROM,POS,~ID,REF,ALT,INFO/END input.vcf
    # For more examples see <a rel="nofollow" href="http://samtools.github.io/bcftools/howtos/annotate.html">http://samtools.github.io/bcftools/howtos/annotate.html</a>
</pre>
</dl>
<h3>bcftools call <i>[OPTIONS]</i> <i>FILE</i></h3>
<p> This command replaces the former <code>bcftools view</code> caller. Some of the original functionality has been temporarily lost in the process of transition under <i>htslib</i> &lt;<a rel="nofollow" href="http://github.com/samtools/htslib">http://github.com/samtools/htslib</a>&gt;, but will be added back on popular demand. The original calling model can be invoked with the <code>-c</code> option.</p>
<h3>File format options:</h3>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;ploidy</code> <i>ASSEMBLY</i>[<i>?</i>]</p>
<dl>
<dt>
<dd> predefined ploidy, use <i>list</i> (or any other unused word) to print a list of all predefined assemblies. Append a question mark to print the actual definition. See also <code>&#8211;ploidy-file</code>.</dl>
<p> <code>&#8211;ploidy-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> ploidy definition given as a space/tab-delimited list of CHROM, FROM, TO, SEX, PLOIDY. The SEX codes are arbitrary and correspond to the ones used by <code>&#8211;samples-file</code>. The default ploidy can be given using the starred records (see below), unlisted regions have ploidy 2. The default ploidy definition is</dl>
<dl>
<dt>
<dd>
<pre>
    X 1 60000 M 1
    X 2699521 154931043 M 1
    Y 1 59373566 M 1
    Y 1 59373566 F 0
    MT 1 16569 M 1
    MT 1 16569 F 1
    *  * *     M 2
    *  * *     F 2
</pre>
</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>Input/output options:</h3>
<p> <code>-A, &#8211;keep-alts</code></p>
<dl>
<dt>
<dd> output all alternate alleles present in the alignments even if they do not appear in any of the genotypes</dl>
<p> <code>-f, &#8211;format-fields</code> <i>list</i></p>
<dl>
<dt>
<dd> comma-separated list of FORMAT fields to output for each sample. Currently GQ and GP fields are supported. For convenience, the fields can be given as lower case letters. Prefixed with &quot;^&quot; indicates a request for tag removal of auxiliary tags useful only for calling.</dl>
<p> <code>-F, &#8211;prior-freqs</code> <i>AN</i>,<i>AC</i></p>
<dl>
<dt>
<dd> take advantage of prior knowledge of population allele frequencies. The workflow looks like this:</dl>
<dl>
<dt>
<dd>
<pre><code>
#Extract AN, AC values from an existing VCF, such 1000Genomes
bcftools query - f '%CHROM	%POS	%REF	%ALT	%AN	%AC
' 1000Genomes.bcf | bgzip - c &gt; AFs.tab.gz
#If the tags AN, AC are not already present, use the + fill - tags plugin
                                                                                                bcftools +
                                                                                            fill - tags 1000Genomes.bcf |
    bcftools query - f '%CHROM	%POS	%REF	%ALT	%AN	%AC
' | bgzip - c &gt; AFs.tab.gz tabix - s1 - b2 - e2 AFs.tab.gz
#Create a VCF header description, here we name the tags REF_AN, REF_AC
                                                                                                             cat AFs.hdr##INFO = &lt;ID = REF_AN, Number = 1, Type = Integer, Description = "Total number of alleles in reference genotypes"&gt;##INFO = &lt;ID = REF_AC, Number = A, Type = Integer, Description = "Allele count in reference genotypes for each ALT allele"&gt;
#Now before calling, stream the raw mpileup output through `bcftools annotate` to add the frequencies
                                                                                                                                                                                                                                                           bcftools mpileup[...] - Ou |
                                                                                                                                                                                                                                                   bcftools annotate - a AFs.tab.gz - h AFs.hdr - c CHROM,
                                                                                                                 POS, REF, ALT, REF_AN, REF_AC - Ou | bcftools call - mv - F REF_AN, REF_AC[...]
</code></pre>
</dl>
<p> <code>-G, &#8211;group-samples</code> <i>FILE</i>|<i>&#8211;</i></p>
<dl>
<dt>
<dd> by default, all samples are assumed to come from a single population. This option allows to group samples into populations and apply the HWE assumption within but not across the populations. <i>FILE</i> is a tab-delimited text file with sample names in the first column and group names in the second column. If <i>&#8211;</i> is given instead, no HWE assumption is made at all and single-sample calling is performed. (Note that in low coverage data this inflates the rate of false positives.) The <code>-G</code> option requires the presence of per-sample FORMAT/QS or FORMAT/AD tag generated with <code>bcftools mpileup -a QS</code> (or <code>-a AD</code>).</dl>
<p> <code>-g, &#8211;gvcf</code> <i>INT</i></p>
<dl>
<dt>
<dd> output also gVCF blocks of homozygous REF calls. The parameter <i>INT</i> is the minimum per-sample depth required to include a site in the non-variant block.</dl>
<p> <code>-i, &#8211;insert-missed</code> <i>INT</i></p>
<dl>
<dt>
<dd> output also sites missed by mpileup but present in <code>-T, &#8211;targets-file</code>.</dl>
<p> <code>-M, &#8211;keep-masked-ref</code></p>
<dl>
<dt>
<dd> output sites where REF allele is N</dl>
<p> <code>-V, &#8211;skip-variants</code> <i>snps</i>|<i>indels</i></p>
<dl>
<dt>
<dd> skip indel/SNP sites</dl>
<p> <code>-v, &#8211;variants-only</code></p>
<dl>
<dt>
<dd> output variant sites only</dl>
<h3>Consensus/variant calling options:</h3>
<p> <code>-c, &#8211;consensus-caller</code></p>
<dl>
<dt>
<dd> the original <code>samtools</code>/<code>bcftools</code> calling method (conflicts with <code>-m</code>)</dl>
<p> <code>-C, &#8211;constrain</code> <i>alleles</i>|<i>trio</i></p>
<dl>
<dt>
<dd>
<p> <i>alleles</i></p>
<dl>
<dt>
<dd> call genotypes given alleles. See also <code>-T, &#8211;targets-file</code>.</dl>
<p> <i>trio</i></p>
<dl>
<dt>
<dd> call genotypes given the father-mother-child constraint. See also <code>-s, &#8211;samples</code> and <code>-n, &#8211;novel-rate</code>.</dl>
</dl>
<p> <code>-m, &#8211;multiallelic-caller</code></p>
<dl>
<dt>
<dd> alternative model for multiallelic and rare-variant calling designed to overcome known limitations in <code>-c</code> calling model (conflicts with <code>-c</code>)</dl>
<p> <code>-n, &#8211;novel-rate</code> <i>float</i>[,&#8230;]</p>
<dl>
<dt>
<dd> likelihood of novel mutation for constrained <code>-C</code> <i>trio</i> calling. The trio genotype calling maximizes likelihood of a particular combination of genotypes for father, mother and the child P(F=i,M=j,C=k) = P(unconstrained) * Pn + P(constrained) * (1-Pn). By providing three values, the mutation rate Pn is set explicitly for SNPs, deletions and insertions, respectively. If two values are given, the first is interpreted as the mutation rate of SNPs and the second is used to calculate the mutation rate of indels according to their length as Pn=<i>float</i>*exp(-a-b*len), where a=22.8689, b=0.2994 for insertions and a=21.9313, b=0.2856 for deletions [pubmed:23975140]. If only one value is given, the same mutation rate Pn is used for SNPs and indels.</dl>
<p> <code>-p, &#8211;pval-threshold</code> <i>float</i></p>
<dl>
<dt>
<dd> with <code>-c</code>, accept variant if P(ref|D) &lt; <i>float</i>.</dl>
<p> <code>-P, &#8211;prior</code> <i>float</i></p>
<dl>
<dt>
<dd> expected substitution rate, or 0 to disable the prior. Only with <code>-m</code>.</dl>
<p> <code>-t, &#8211;targets</code> <i>file</i>|<i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-X, &#8211;chromosome-X</code></p>
<dl>
<dt>
<dd> haploid output for male samples (requires PED file with <code>-s</code>)</dl>
<p> <code>-Y, &#8211;chromosome-Y</code></p>
<dl>
<dt>
<dd> haploid output for males and skips females (requires PED file with <code>-s</code>)</dl>
<h3>bcftools cnv <i>[OPTIONS]</i> <i>FILE</i></h3>
<p> Copy number variation caller, requires a VCF annotated with the Illumina&#8217;s B-allele frequency (BAF) and Log R Ratio intensity (LRR) values. The HMM considers the following copy number states: CN 2 (normal), 1 (single-copy loss), 0 (complete loss), 3 (single-copy gain).</p>
<h3>General Options:</h3>
<p> <code>-c, &#8211;control-sample</code> <i>string</i></p>
<dl>
<dt>
<dd> optional control sample name. If given, pairwise calling is performed and the <code>-P</code> option can be used</dl>
<p> <code>-f, &#8211;AF-file</code> <i>file</i></p>
<dl>
<dt>
<dd> read allele frequencies from a tab-delimited file with the columns CHR,POS,REF,ALT,AF</dl>
<p> <code>-o, &#8211;output-dir</code> <i>path</i></p>
<dl>
<dt>
<dd> output directory</dl>
<p> <code>-p, &#8211;plot-threshold</code> <i>float</i></p>
<dl>
<dt>
<dd> call <code>matplotlib</code> to produce plots for chromosomes with quality at least <i>float</i>, useful for visual inspection of the calls. With <code>-p 0</code>, plots for all chromosomes will be generated. If not given, a <code>matplotlib</code> script will be created but not called.</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;query-sample</code> <i>string</i></p>
<dl>
<dt>
<dd> query sample name</dl>
<p> <code>-t, &#8211;targets</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<h3>HMM Options:</h3>
<p> <code>-a, &#8211;aberrant</code> <i>float</i>[,<i>float</i>]</p>
<dl>
<dt>
<dd> fraction of aberrant cells in query and control. The hallmark of duplications and contaminations is the BAF value of heterozygous markers which is dependent on the fraction of aberrant cells. Sensitivity to smaller fractions of cells can be increased by setting <code>-a</code> to a lower value. Note however, that this comes at the cost of increased false discovery rate.</dl>
<p> <code>-b, &#8211;BAF-weight</code> <i>float</i></p>
<dl>
<dt>
<dd> relative contribution from BAF</dl>
<p> <code>-d, &#8211;BAF-dev</code> <i>float</i>[,<i>float</i>]</p>
<dl>
<dt>
<dd> expected BAF deviation in query and control, i.e. the noise observed in the data.</dl>
<p> <code>-e, &#8211;err-prob</code> <i>float</i></p>
<dl>
<dt>
<dd> uniform error probability</dl>
<p> <code>-l, &#8211;LRR-weight</code> <i>float</i></p>
<dl>
<dt>
<dd> relative contribution from LRR. With noisy data, this option can have big effect on the number of calls produced. In truly random noise (such as in simulated data), the value should be set high (1.0), but in the presence of systematic noise when LRR are not informative, lower values result in cleaner calls (0.2).</dl>
<p> <code>-L, &#8211;LRR-smooth-win</code> <i>int</i></p>
<dl>
<dt>
<dd> reduce LRR noise by applying moving average given this window size</dl>
<p> <code>-O, &#8211;optimize</code> <i>float</i></p>
<dl>
<dt>
<dd> iteratively estimate the fraction of aberrant cells, down to the given fraction. Lowering this value from the default 1.0 to say, 0.3, can help discover more events but also increases noise</dl>
<p> <code>-P, &#8211;same-prob</code> <i>float</i></p>
<dl>
<dt>
<dd> the prior probability of the query and the control sample being the same. Setting to 0 calls both independently, setting to 1 forces the same copy number state in both.</dl>
<p> <code>-x, &#8211;xy-prob</code> <i>float</i></p>
<dl>
<dt>
<dd> the HMM probability of transition to another copy number state. Increasing this values leads to smaller and more frequent calls.</dl>
<h3>bcftools concat <i>[OPTIONS]</i> <i>FILE1</i> <i>FILE2</i> [&#8230;]</h3>
<p> Concatenate or combine VCF/BCF files. All source files must have the same sample columns appearing in the same order. Can be used, for example, to concatenate chromosome VCFs into one VCF, or combine a SNP VCF and an indel VCF into one. The input files must be sorted by chr and position. The files must be given in the correct order to produce sorted VCF on output unless the <code>-a, &#8211;allow-overlaps</code> option is specified. With the &#8211;naive option, the files are concatenated without being recompressed, which is very fast.. </p>
<p> <code>-a, &#8211;allow-overlaps</code></p>
<dl>
<dt>
<dd> First coordinate of the next file can precede last record of the current file.</dl>
<p> <code>-c, &#8211;compact-PS</code></p>
<dl>
<dt>
<dd> Do not output PS tag at each site, only at the start of a new phase set block.</dl>
<p> <code>-d, &#8211;rm-dups</code> <i>snps</i>|<i>indels</i>|<i>both</i>|<i>all</i>|<i>exact</i></p>
<dl>
<dt>
<dd> Output duplicate records of specified type present in multiple files only once. Note that records duplicate within one file are not removed with this option, for that use <code>bcftools norm -d</code> instead.<br />
 In other words, the default behavior of the program is similar to unix &quot;cat&quot; in that when two files contain a record with the same position, that position will appear twice on output. With <code>-d</code>, every line that finds a matching record in another file will be printed only once.<br />
 Requires <code>-a, &#8211;allow-overlaps</code>.</dl>
<p> <code>-D, &#8211;remove-duplicates</code></p>
<dl>
<dt>
<dd> Alias for <code>-d exact</code></dl>
<p> <code>-f, &#8211;file-list</code> <i>FILE</i></p>
<dl>
<dt>
<dd> Read file names from <i>FILE</i>, one file name per line.</dl>
<p> <code>-l, &#8211;ligate</code></p>
<dl>
<dt>
<dd> Ligate phased VCFs by matching phase at overlapping haplotypes. Note that the option is intended for VCFs with perfect overlap, sites in overlapping regions present in one but missing in the other are dropped.</dl>
<p> <code>&#8211;ligate-force</code></p>
<dl>
<dt>
<dd> Keep all sites and ligate even non-overlapping chunks and chunks with imperfect overlap</dl>
<p> <code>&#8211;ligate-warn</code></p>
<dl>
<dt>
<dd> Drop sites in imperfect overlaps</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-n, &#8211;naive</code></p>
<dl>
<dt>
<dd> Concatenate VCF or BCF files without recompression. This is very fast but requires that all files are of the same type (all VCF or all BCF) and have the same headers. This is because all tags and chromosome names in the BCF body rely on the order of the contig and tag definitions in the header. A header check compatibility is performed and the program throws an error if it is not safe to use the option.</dl>
<p> <code>&#8211;naive-force</code></p>
<dl>
<dt>
<dd> Same as &#8211;naive, but header compatibility is not checked. Dangerous, use with caution.</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-q, &#8211;min-PQ</code> <i>INT</i></p>
<dl>
<dt>
<dd> Break phase set if phasing quality is lower than <i>INT</i></dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code>. Requires <code>-a, &#8211;allow-overlaps</code>.</dl>
<p> <code>-R, &#8211;regions-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code>. Requires <code>-a, &#8211;allow-overlaps</code>.</dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>bcftools consensus <i>[OPTIONS]</i> <i>FILE</i></h3>
<p> Create consensus sequence by applying VCF variants to a reference fasta file. By default, the program will apply all ALT variants to the reference fasta to obtain the consensus sequence. Using the <code>&#8211;sample</code> (and, optionally, <code>&#8211;haplotype</code>) option will apply genotype (haplotype) calls from FORMAT/GT. Note that the program does not act as a primitive variant caller and ignores allelic depth information, such as INFO/AD or FORMAT/AD. For that, consider using the <code>setGT</code> plugin. </p>
<p> <code>-a, &#8211;absent</code> <i>CHAR</i></p>
<dl>
<dt>
<dd> replace positions absent from VCF with CHAR</dl>
<p> <code>-c, &#8211;chain</code> <i>FILE</i></p>
<dl>
<dt>
<dd> write a chain file for liftover</dl>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-f, &#8211;fasta-ref</code> <i>FILE</i></p>
<dl>
<dt>
<dd> reference sequence in fasta format</dl>
<p> <code>-H, &#8211;haplotype</code> N|<i>R</i>|<i>A</i>|<i>I</i>|<i>LR</i>|<i>LA</i>|<i>SR</i>|<i>SA</i>|<i>NpIu</i></p>
<dl>
<dt>
<dd> choose which allele from the FORMAT/GT field to use (the codes are case-insensitive): </p>
<p> <i>N</i></p>
<dl>
<dt>
<dd> N={1,2,3,&#8230;}, the allele index within the genotype, regardless of phasing</dl>
<p> <i>R</i></p>
<dl>
<dt>
<dd> the REF allele (in heterozygous genotypes)</dl>
<p> <i>A</i></p>
<dl>
<dt>
<dd> the ALT allele (in heterozygous genotypes)</dl>
<p> <i>I</i></p>
<dl>
<dt>
<dd> IUPAC code for all genotypes</dl>
<p> <i>LR, LA</i></p>
<dl>
<dt>
<dd> the longer allele. If both have the same length, use the REF allele (LR), or the ALT allele (LA)</dl>
<p> <i>SR, SA</i></p>
<dl>
<dt>
<dd> the shorter allele. If both have the same length, use the REF allele (SR), or the ALT allele (SA)</dl>
<p> <i>NpIu</i></p>
<dl>
<dt>
<dd> N={1,2,3,&#8230;}, the allele index within genotype for phased genotypes and IUPAC code for unphased genotypes. For example, <i>1pIu</i> or <i>2pIu</i></dl>
</dl>
<p> Note that the <code>-H, &#8211;haplotype</code> option requires the <code>-s, &#8211;samples</code> option, unless exactly one sample is present in the VCF </p>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-I, &#8211;iupac-codes</code></p>
<dl>
<dt>
<dd> output variants in the form of IUPAC ambiguity codes determined from FORMAT/GT fields. By default all samples are used and can be subset with -s, &#8211;samples and -S, &#8211;samples-file. Use -s &#8211; to ignore samples and use only the REF and ALT columns. NOTE: prior to version 1.17 the IUPAC codes were determined solely from REF,ALT columns and sample genotypes were not considered.</dl>
<p> <code>&#8211;mark-del</code> <i>CHAR</i></p>
<dl>
<dt>
<dd> instead of removing sequence, insert CHAR for deletions</dl>
<p> <code>&#8211;mark-ins</code> <i>uc</i>|<i>lc</i></p>
<dl>
<dt>
<dd> highlight inserted sequence in uppercase (uc) or lowercase (lc), leaving the rest of the sequence as is</dl>
<p> <code>&#8211;mark-snv</code> <i>uc</i>|<i>lc</i></p>
<dl>
<dt>
<dd> highlight substitutions in uppercase (uc) or lowercase (lc), leaving the rest of the sequence as is</dl>
<p> <code>-m, &#8211;mask</code> <i>FILE</i></p>
<dl>
<dt>
<dd> BED file or TAB file with regions to be replaced with N (the default) or as specified by the next <code>&#8211;mask-with</code> option. See discussion of <code>&#8211;regions-file</code> in <code>Common Options</code> for file format details.</dl>
<p> <code>&#8211;mask-with</code> <i>CHAR</i>|<i>lc</i>|<i>uc</i></p>
<dl>
<dt>
<dd> replace sequence from <code>&#8211;mask</code> with CHAR, skipping overlapping variants, or change to lowercase (lc) or uppercase (uc)</dl>
<p> <code>-M, &#8211;missing</code> <i>CHAR</i></p>
<dl>
<dt>
<dd> instead of skipping the missing genotypes, output the character CHAR (e.g. &quot;?&quot;)</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> write output to a file</dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> apply variants of the listed samples. See also the option -I, &#8211;iupac-codes</dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> apply variants of the samples listed in the file. See also the option -I, &#8211;iupac-codes</dl>
<p> <code>Examples:</code> </p>
<dl>
<dt>
<dd>
<pre>
    # Apply variants present in sample &quot;NA001&quot;, output IUPAC codes for hets
    bcftools consensus -i -s NA001 -f in.fa in.vcf.gz &gt; out.fa
    # Create consensus for one region. The fasta header lines are then expected
    # in the form &quot;&gt;chr:from-to&quot;. Ignore samples and consider only the REF and ALT columns
    samtools faidx ref.fa 8:11870-11890 | bcftools consensus -s - in.vcf.gz -o out.fa
    # For more examples see <a rel="nofollow" href="http://samtools.github.io/bcftools/howtos/consensus-sequence.html">http://samtools.github.io/bcftools/howtos/consensus-sequence.html</a>
</pre>
</dl>
<h3>bcftools convert <i>[OPTIONS]</i> <i>FILE</i></h3>
<h3>VCF input options:</h3>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>VCF output options:</h3>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<h3>GEN/SAMPLE conversion:</h3>
<p> <code>-G, &#8211;gensample2vcf</code> <i>prefix</i> or <i>gen-file</i>,<i>sample-file</i></p>
<dl>
<dt>
<dd> convert IMPUTE2 output to VCF. One of the ID columns (&quot;SNP ID&quot; or &quot;rsID&quot; in <i></i> &lt;<a rel="nofollow" href="https://www.cog-genomics.org/plink/2.0/formats#gen">https://www.cog-genomics.org/plink/2.0/formats#gen</a>&gt;) must be of the form &quot;CHROM:POS_REF_ALT&quot; to detect possible strand swaps. ~<br />
 When the <code>&#8211;vcf-ids</code> option is given, the other column (autodetected) is used to fill the ID column of the VCF. ~<br />
 See also <code>-g</code> and <code>&#8211;3N6</code> options.</dl>
<p> <code>-g, &#8211;gensample</code> <i>prefix</i> or <i>gen-file</i>,<i>sample-file</i></p>
<dl>
<dt>
<dd> convert from VCF to gen/sample format used by IMPUTE2 and SHAPEIT. The columns of .gen file format are ID1,ID2,POS,A,B followed by three genotype probabilities P(AA), P(AB), P(BB) for each sample. In order to prevent strand swaps, the program uses IDs of the form &quot;CHROM:POS_REF_ALT&quot;. When the <code>&#8211;vcf-ids</code> option is given, the second column is set to match the ID column of the VCF. ~<br />
 See also <code>-G</code> and <code>&#8211;3N6</code> options. ~<br />
 The file .gen and .sample file format are:</dl>
<dl>
<dt>
<dd>
.gen(with&#8211; 3N6 &#8211;vcf &#8211; ids)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -chr1 1 : 111485207_G_A rsID1 111485207 G A 0 1 0 0 1 0 chr1 1 : 111494194_C_T rsID2 111494194 C T 0 1 0 0 0 1<br />
    .gen(with&#8211; vcf &#8211; ids)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 : 111485207_G_A rsID1 111485207 G A 0 1 0 0 1 0 1 : 111494194_C_T rsID2 111494194 C T 0 1 0 0 0 1<br />
    .gen(the default)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;1 : 111485207_G_A 1 : 111485207_G_A 111485207 G A 0 1 0 0 1 0 1 : 111494194_C_T 1 : 111494194_C_T 111494194 C T 0 1 0 0 0 1<br />
    .sample<br />
    &#8212; &#8212; &#8212; -ID_1 ID_2 missing<br />
    0 0 0 sample1 sample1 0 sample2 sample2 0
</dl>
<p> <code>&#8211;3N6</code></p>
<dl>
<dt>
<dd> Expect/Create files in the 3*N+6 column format. This is the new .gen file format with the first column containing the chromosome name, see <i></i> &lt;<a rel="nofollow" href="https://www.cog-genomics.org/plink/2.0/formats#gen">https://www.cog-genomics.org/plink/2.0/formats#gen</a>&gt;</dl>
<p> <code>&#8211;tag</code> <i>STRING</i></p>
<dl>
<dt>
<dd> tag to take values for .gen file: GT,PL,GL,GP</dl>
<p> <code>&#8211;sex</code> <i>FILE</i></p>
<dl>
<dt>
<dd> output sex column in the sample file. The FILE format is</dl>
<dl>
<dt>
<dd>
<pre>
    MaleSample    M
    FemaleSample  F
</pre>
</dl>
<p> <code>&#8211;vcf-ids</code></p>
<dl>
<dt>
<dd> output VCF IDs in the second column instead of CHROM:POS_REF_ALT</dl>
<h3>gVCF conversion:</h3>
<p> <code>&#8211;gvcf2vcf</code></p>
<dl>
<dt>
<dd> convert gVCF to VCF, expanding REF blocks into sites. Note that the <code>-i</code> and <code>-e</code> options work differently with this switch. In this situation the filtering expressions define which sites should be expanded and which sites should be left unmodified, but all sites are printed on output. In order to drop sites, stream first through <code>bcftools view</code>.</dl>
<p> <code>-f, &#8211;fasta-ref</code> <i>file</i></p>
<dl>
<dt>
<dd> reference sequence in fasta format. Must be indexed with samtools faidx</dl>
<h3>HAP/SAMPLE conversion:</h3>
<p> <code>&#8211;hapsample2vcf</code> <i>prefix</i> or <i>hap-file</i>,<i>sample-file</i></p>
<dl>
<dt>
<dd> convert from hap/sample format to VCF. The columns of .hap file are similar to .gen file above, but there are only two haplotype columns per sample. Note that the first or the second column of the .hap file is expected to be in the form &quot;CHR:POS_REF_ALT[_END]&quot;, with the _END being optional for defining the INFO/END tag when ALT is a symbolic allele. For example:</dl>
<dl>
<dt>
<dd>
.hap(with&#8211; vcf &#8211; ids)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1 : 111485207_G_A rsID1 111485207 G A 0 1 0 0 1 : 111495231_A_ &lt; DEL &gt; _111495784 rsID3 111495231 A&lt;DEL&gt; 0 0 1 0<br />
                                                                                                                                .hap(the default)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;1 1 : 111485207_G_A 111485207 G A 0 1 0 0 1 1 : 111495231_A_ &lt; DEL<br />
    &gt; _111495784 111495231 A&lt;DEL&gt; 0 0 1 0
</dl>
<p> <code>&#8211;hapsample</code> <i>prefix</i> or <i>hap-file</i>,<i>sample-file</i></p>
<dl>
<dt>
<dd> convert from VCF to hap/sample format used by IMPUTE2 and SHAPEIT. The columns of .hap file begin with ID,RSID,POS,REF,ALT. In order to prevent strand swaps, the program uses IDs of the form &quot;CHROM:POS_REF_ALT&quot;.</dl>
<p> <code>&#8211;haploid2diploid</code></p>
<dl>
<dt>
<dd> with <code>-h</code> option converts haploid genotypes to homozygous diploid genotypes. For example, the program will print <i>0 0</i> instead of the default <i>0 &#8211;</i>. This is useful for programs which do not handle haploid genotypes correctly.</dl>
<p> <code>&#8211;sex</code> <i>FILE</i></p>
<dl>
<dt>
<dd> output sex column in the sample file. The FILE format is</dl>
<dl>
<dt>
<dd>
<pre>
    MaleSample    M
    FemaleSample  F
</pre>
</dl>
<p> <code>&#8211;vcf-ids</code></p>
<dl>
<dt>
<dd> the second column of the .hap file holds the VCF ids, the first column is of the form &quot;CHR:POS_REF_ALT[_END]&quot;. Without the option, the format follows <i></i> &lt;<a rel="nofollow" href="https://www.cog-genomics.org/plink/2.0/formats#haps">https://www.cog-genomics.org/plink/2.0/formats#haps</a>&gt; with ids (the second column) of the form &quot;CHR:POS_REF_ALT[_END]&quot;</dl>
<h3>HAP/LEGEND/SAMPLE conversion:</h3>
<p> <code>-H, &#8211;haplegendsample2vcf</code> <i>prefix</i> or <i>hap-file</i>,<i>legend-file</i>,<i>sample-file</i></p>
<dl>
<dt>
<dd> convert from hap/legend/sample format used by IMPUTE2 to VCF. See also <code>-h, &#8211;hapslegendsample</code> below.</dl>
<p> <code>-h, &#8211;haplegendsample</code> <i>prefix</i> or <i>hap-file</i>,<i>legend-file</i>,<i>sample-file</i></p>
<dl>
<dt>
<dd> convert from VCF to hap/legend/sample format used by IMPUTE2 and SHAPEIT. The columns of .legend file ID,POS,REF,ALT. In order to prevent strand swaps, the program uses IDs of the form &quot;CHROM:POS_REF_ALT&quot;. The .sample file is quite basic at the moment with columns for population, group and sex expected to be edited by the user. For example:</dl>
<dl>
<dt>
<dd>
.hap&#8211; &#8212; -0 1 0 0 1 0 0 1 0 0 0 1<br />
    .legend&#8211; &#8212; &#8212; -id position a0 a1 1 : 111485207_G_A 111485207 G A 1 : 111494194_C_T 111494194 C T<br />
    .sample&#8211; &#8212; &#8212; -sample population group sex<br />
        sample1 sample1 sample1 2 sample2 sample2 sample2 2
</dl>
<p> <code>&#8211;haploid2diploid</code></p>
<dl>
<dt>
<dd> with <code>-h</code> option converts haploid genotypes to homozygous diploid genotypes. For example, the program will print <i>0 0</i> instead of the default <i>0 &#8211;</i>. This is useful for programs which do not handle haploid genotypes correctly.</dl>
<p> <code>&#8211;sex</code> <i>FILE</i></p>
<dl>
<dt>
<dd> output sex column in the sample file. The FILE format is</dl>
<dl>
<dt>
<dd>
<pre>
    MaleSample    M
    FemaleSample  F
</pre>
</dl>
<p> <code>&#8211;vcf-ids</code></p>
<dl>
<dt>
<dd> output VCF IDs instead of &quot;CHROM:POS_REF_ALT&quot;. Note that this option can be used with <code>&#8211;haplegendsample</code> but not with <code>&#8211;haplegendsample2vcf</code>.</dl>
<h3>TSV conversion:</h3>
<p> <code>&#8211;tsv2vcf</code> <i>file</i></p>
<dl>
<dt>
<dd> convert from TSV (tab-separated values) format (such as generated by 23andMe) to VCF. The input file fields can be tab- or space- delimited</dl>
<p> <code>-c, &#8211;columns</code> <i>list</i></p>
<dl>
<dt>
<dd> comma-separated list of fields in the input file. In the current version, the fields CHROM, POS, ID, and AA are expected and can appear in arbitrary order, columns which should be ignored in the input file can be indicated by &quot;-&quot;. The AA field lists alleles on the forward reference strand, for example &quot;CC&quot; or &quot;CT&quot; for diploid genotypes or &quot;C&quot; for haploid genotypes (sex chromosomes). Insertions and deletions are not supported yet, missing data can be indicated with &quot;&#8211;&quot;.</dl>
<p> <code>-f, &#8211;fasta-ref</code> <i>file</i></p>
<dl>
<dt>
<dd> reference sequence in fasta format. Must be indexed with samtools faidx</dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> list of sample names. See <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> file of sample names. See <code>Common Options</code></dl>
<p> <code>Example:</code> </p>
<dl>
<dt>
<dd>
<pre>
# Convert 23andme results into VCF
bcftools convert -c ID,CHROM,POS,AA -s SampleName -f 23andme-ref.fa --tsv2vcf 23andme.txt -Oz -o out.vcf.gz
</pre>
</dl>
<h3>bcftools csq <i>[OPTIONS]</i> <i>FILE</i></h3>
<p> Haplotype aware consequence predictor which correctly handles combined variants such as MNPs split over multiple VCF records, SNPs separated by an intron (but adjacent in the spliced transcript) or nearby frame-shifting indels which in combination in fact are not frame-shifting. </p>
<p> The output VCF is annotated with INFO/BCSQ and FORMAT/BCSQ tag (configurable with the <code>-c</code> option). The latter is a bitmask of indexes to INFO/BCSQ, with interleaved haplotypes. See the usage examples below for using the %TBCSQ converter in <code>query</code> for extracting a more human readable form from this bitmask. The construction of the bitmask limits the number of consequences that can be referenced per sample in the FORMAT/BCSQ tags. By default this is 15, but if more are required, see the <code>&#8211;ncsq</code> option. </p>
<p> The program requires on input a VCF/BCF file, the reference genome in fasta format (<code>&#8211;fasta-ref</code>) and genomic features in the GFF3 format downloadable from the Ensembl website (<code>&#8211;gff-annot</code>), and outputs an annotated VCF/BCF file. Currently, only Ensembl GFF3 files are supported. </p>
<p> By default, the input VCF should be phased. If phase is unknown, or only partially known, the <code>&#8211;phase</code> option can be used to indicate how to handle unphased data. Alternatively, haplotype aware calling can be turned off with the <code>&#8211;local-csq</code> option. </p>
<p> If conflicting (overlapping) variants within one haplotype are detected, a warning will be emitted and predictions will be based on only the first variant in the analysis. </p>
<p> Symbolic alleles are not supported. They will remain unannotated in the output VCF and are ignored for the prediction analysis. </p>
<p> <code>-c, &#8211;custom-tag</code> <i>STRING</i></p>
<dl>
<dt>
<dd> use this custom tag to store consequences rather than the default BCSQ tag</dl>
<p> <code>-B, &#8211;trim-protein-seq</code> <i>INT</i></p>
<dl>
<dt>
<dd> abbreviate protein-changing predictions to maximum of INT aminoacids. For example, instead of writing the whole modified protein sequence with potentially hundreds of aminoacids, with <code>-B 1</code> only an abbreviated version such as <i>25E..329&gt;25G..94</i> will be written.</dl>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-f, &#8211;fasta-ref</code> <i>FILE</i></p>
<dl>
<dt>
<dd> reference sequence in fasta format (required)</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> run even if some sanity checks fail. Currently the option allows to skip transcripts in malformatted GFFs with incorrect phase</dl>
<p> <code>-g, &#8211;gff-annot</code> <i>FILE</i></p>
<dl>
<dt>
<dd> GFF3 annotation file (required), such as <i></i> &lt;<a href="ftp://ftp.ensembl.org/pub/current_gff3/homo_sapiens">ftp://ftp.ensembl.org/pub/current_gff3/homo_sapiens</a>&gt;. The script <code>gff2gff</code> can help with conversion from non-standard GFF formats. An example of a minimal working GFF file:</dl>
<dl>
<dt>
<dd>
#The program looks for &#8220;CDS&#8221;, &#8220;exon&#8221;, &#8220;three_prime_UTR&#8221; and &#8220;five_prime_UTR&#8221; lines,<br />
#looks up their parent transcript(determined from the &#8220;Parent=transcript:&#8221; attribute),<br />
#the gene(determined from the transcript&#8217;s &#8220;Parent=gene:&#8221; attribute), and the biotype<br />
#(the most interesting is &#8220;protein_coding&#8221;).<br />
#<br />
#Attributes required for<br />
#gene lines:<br />
#- ID = gene : &lt;gene_id&gt;<br />
#- biotype = &lt;biotype&gt;<br />
#- Name = &lt;gene_name&gt;[optional]<br />
#<br />
#transcript lines:<br />
#- ID = transcript : &lt;transcript_id&gt;<br />
#- Parent = gene : &lt;gene_id&gt;<br />
#- biotype = &lt;biotype&gt;<br />
#<br />
#other lines(CDS, exon, five_prime_UTR, three_prime_UTR):<br />
#- Parent = transcript : &lt;transcript_id&gt;<br />
#<br />
#Supported biotypes:<br />
#- see the function gff_parse_biotype() in bcftools / csq.c<br />
1 ignored_field gene 21 2148.-.ID = gene : GeneId;<br />
biotype = protein_coding;<br />
Name = GeneName 1 ignored_field transcript 21 2148.-.ID = transcript : TranscriptId;<br />
Parent = gene : GeneId;<br />
biotype = protein_coding 1 ignored_field three_prime_UTR 21 2054.-.Parent = transcript : TranscriptId 1 ignored_field exon 21 2148.-.Parent = transcript : TranscriptId 1 ignored_field CDS 21 2148.- 1 Parent = transcript : TranscriptId 1 ignored_field five_prime_UTR 210 2148.-.Parent = transcript : TranscriptId
</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-l, &#8211;local-csq</code></p>
<dl>
<dt>
<dd> switch off haplotype-aware calling, run localized predictions considering only one VCF record at a time</dl>
<p> <code>-n, &#8211;ncsq</code> <i>INT</i></p>
<dl>
<dt>
<dd> maximum number of per-haplotype consequences to consider for each site. The INFO/BCSQ column includes all consequences, but only the first <i>INT</i> will be referenced by the FORMAT/BCSQ fields. The default value is 15 which corresponds to one 32-bit integer per diploid sample, after accounting for values reserved by the BCF specification. Note that increasing the value leads to increased size of the output BCF.</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>t</i>|<i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code>. In addition, a custom tab-delimited plain text output can be printed (<i>t</i>).</dl>
<p> <code>-p, &#8211;phase</code> <i>a</i>|<i>m</i>|<i>r</i>|<i>R</i>|<i>s</i></p>
<dl>
<dt>
<dd> how to handle unphased heterozygous genotypes: </p>
<p> <i>a</i></p>
<dl>
<dt>
<dd> take GTs as is, create haplotypes regardless of phase (0/1 &rarr; 0|1)</dl>
<p> <i>m</i></p>
<dl>
<dt>
<dd> merge all GTs into a single haplotype (0/1 &rarr; 1, 1/2 &rarr; 1)</dl>
<p> <i>r</i></p>
<dl>
<dt>
<dd> require phased GTs, throw an error on unphased heterozygous GTs</dl>
<p> <i>R</i></p>
<dl>
<dt>
<dd> create non-reference haplotypes if possible (0/1 &rarr; 1|1, 1/2 &rarr; 1|2)</dl>
<p> <i>s</i></p>
<dl>
<dt>
<dd> skip unphased heterozygous GTs</dl>
</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dt>
<dd> suppress warning messages</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> samples to include or &quot;-&quot; to apply all variants and ignore samples</dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<p> <code>Examples:</code> </p>
<dl>
<dt>
<dd>
#Basic usage<br />
bcftools csq &#8211; f hs37d5.fa &#8211; g Homo_sapiens.GRCh37 .82.gff3.gz in.vcf &#8211; Ob &#8211; o out.bcf<br />
#Extract the translated haplotype consequences.The following TBCSQ variations<br />
#are recognised:<br />
#% TBCSQ..print consequences in all haplotypes in separate columns<br />
#% TBCSQ{0 }..print the first haplotype only<br />
#% TBCSQ{1 }..print the second haplotype only<br />
#% TBCSQ{* }..print a list of unique consequences present in either haplotype<br />
                                                                                 bcftools query &#8211;<br />
    f &#8216;[%CHROM	%POS	%SAMPLE	%TBCSQ
]&#8217; out.bcf
</dl>
<p> <code>Examples of BCSQ annotation:</code> </p>
<dl>
<dt>
<dd>
<pre>
    # Two separate VCF records at positions 2:122106101 and 2:122106102
    # change the same codon. This UV-induced C&gt;T dinucleotide mutation
    # has been annotated fully at the position 2:122106101 with
    #   - consequence type
    #   - gene name
    #   - ensembl transcript ID
    #   - coding strand (+ fwd, - rev)
    #   - amino acid position (in the coding strand orientation)
    #   - list of corresponding VCF variants
    # The annotation at the second position gives the position of the full
    # annotation
    BCSQ=missense|CLASP1|ENST00000545861|-|1174P&gt;1174L|122106101G&gt;A+122106102G&gt;A
    BCSQ=@122106101
    # A frame-restoring combination of two frameshift insertions C&gt;CG and T&gt;TGG
    BCSQ=@46115084
    BCSQ=inframe_insertion|COPZ2|ENST00000006101|-|18AGRGP&gt;18AQAGGP|46115072C&gt;CG+46115084T&gt;TGG
    # Stop gained variant
    BCSQ=stop_gained|C2orf83|ENST00000264387|-|141W&gt;141*|228476140C&gt;T
    # The consequence type of a variant downstream from a stop are prefixed with *
    BCSQ=*missense|PER3|ENST00000361923|+|1028M&gt;1028T|7890117T&gt;C
</pre>
</dl>
<p> <code>Supported consequence types</code> </p>
<dl>
<dt>
<dd>
<pre>
3_prime_utr
5_prime_utr
coding_sequence
feature_elongation
frameshift
inframe_altering
inframe_deletion
inframe_insertion
intergenic
intron
missense
non_coding
splice_acceptor
splice_donor
splice_region
start_lost
start_retained
stop_gained
stop_lost
stop_retained
synonymous
</pre>
</dl>
<p> See also <i></i> &lt;<a rel="nofollow" href="https://ensembl.org/info/genome/variation/prediction/predicted_data.html">https://ensembl.org/info/genome/variation/prediction/predicted_data.html</a>&gt;</p>
<h3>bcftools filter <i>[OPTIONS]</i> <i>FILE</i></h3>
<p> Apply fixed-threshold filters. </p>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-g, &#8211;SnpGap</code> <i>INT</i>[:&#8217;indel&#8217;,<i>mnp</i>,<i>bnd</i>,<i>other</i>,<i>overlap</i>]</p>
<dl>
<dt>
<dd> filter SNPs within <i>INT</i> base pairs of an indel or other other variant type. The following example demonstrates the logic of <code>&#8211;SnpGap</code> <i>3</i> applied on a deletion and an insertion:</dl>
<dl>
<dt>
<dd>
<pre>
The SNPs at positions 1 and 7 are filtered, positions 0 and 8 are not:
         0123456789
    ref  .G.GT..G..
    del  .A.G-..A..
Here the positions 1 and 6 are filtered, 0 and 7 are not:
         0123-456789
    ref  .G.G-..G..
    ins  .A.GT..A..
</pre>
</dl>
<p> <code>-G, &#8211;IndelGap</code> <i>INT</i></p>
<dl>
<dt>
<dd> filter clusters of indels separated by <i>INT</i> or fewer base pairs allowing only one to pass. The following example demonstrates the logic of <code>&#8211;IndelGap</code> <i>2</i> applied on a deletion and an insertion:</dl>
<dl>
<dt>
<dd>
<pre>
The second indel is filtered:
         012345678901
    ref  .GT.GT..GT..
    del  .G-.G-..G-..
And similarly here, the second is filtered:
         01 23 456 78
    ref  .A-.A-..A-..
    ins  .AT.AT..AT..
</pre>
</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>&#8211;mask</code> [^]<i>REGION</i></p>
<dl>
<dt>
<dd> Soft filter regions, prepepend &quot;^&quot; to negate. Requires <code>-s, &#8211;soft-filter</code>.</dl>
<p> <code>-M, &#8211;mask-file</code> [^]<i>FILE</i></p>
<dl>
<dt>
<dd> Soft filter regions listed in a file, &quot;^&quot; to negate. Requires <code>-s, &#8211;soft-filter</code>.</dl>
<p> <code>&#8211;mask-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> Same as <code>&#8211;regions-overlap</code> but for <code>&#8211;mask/&#8211;mask-file</code>. See <code>Common Options</code>. [1]</dl>
<p> <code>-m, &#8211;mode</code> [<i>+x</i>]</p>
<dl>
<dt>
<dd> define behaviour at sites with existing FILTER annotations. The default mode replaces existing filters of failed sites with a new FILTER string while leaving sites which pass untouched when non-empty and setting to &quot;PASS&quot; when the FILTER string is absent. The &quot;+&quot; mode appends new FILTER strings of failed sites instead of replacing them. The &quot;x&quot; mode resets filters of sites which pass to &quot;PASS&quot;. Modes &quot;+&quot; and &quot;x&quot; can both be set.</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;soft-filter</code> <i>STRING</i>|<i>+</i></p>
<dl>
<dt>
<dd> annotate FILTER column with <i>STRING</i> or, with <i>+</i>, a unique filter name generated by the program (&quot;Filter%d&quot;).</dl>
<p> <code>-S, &#8211;set-GTs</code> <i>.</i>|<i>0</i></p>
<dl>
<dt>
<dd> set genotypes of failed samples to missing value (<i>.</i>) or reference allele (<i>0</i>)</dl>
<p> <code>-t, &#8211;targets</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>bcftools gtcheck [<i>OPTIONS</i>] [<code>-g</code> <i>genotypes.vcf.gz</i>] <i>query.vcf.gz</i></h3>
<p> Checks sample identity. The program can operate in two modes. If the <code>-g</code> option is given, the identity of samples from <i>query.vcf.gz</i> is checked against the samples in the <code>-g</code> file. Without the <code>-g</code> option, multi-sample cross-check of samples in <i>query.vcf.gz</i> is performed. </p>
<p> <code>&#8211;distinctive-sites</code> <i>NUM[,MEM[,DIR]]</i></p>
<dl>
<dt>
<dd> Find sites that can distinguish between at least NUM sample pairs. If the number is smaller or equal to 1, it is interpreted as the fraction of pairs. The optional MEM string sets the maximum memory used for in-memory sorting and DIR is the temporary directory for external sorting. This option requires also <code>&#8211;pairs</code> to be given.</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Stop after first record to estimate required time.</dl>
<p> <code>-e, &#8211;error-probability</code> <i>INT</i></p>
<dl>
<dt>
<dd> Interpret genotypes and genotype likelihoods probabilistically. The value of <i>INT</i> represents genotype quality when GT tag is used (e.g. Q=30 represents one error in 1,000 genotypes and Q=40 one error in 10,000 genotypes) and is ignored when PL tag is used (in that case an arbitrary non-zero integer can be provided). See also the <code>-u, &#8211;use</code> option below. If set to 0, the discordance equals to the number of mismatching genotypes when GT vs GT is compared. Note that the values with and without <code>-e</code> are not comparable, only values generated with <code>-e 0</code> correspond to mismatching genotypes. If performance is an issue, set to 0 for faster run but less accurate results.</dl>
<p> <code>-g, &#8211;genotypes</code> <i>FILE</i></p>
<dl>
<dt>
<dd> VCF/BCF file with reference genotypes to compare against</dl>
<p> <code>-H, &#8211;homs-only</code></p>
<dl>
<dt>
<dd> Homozygous genotypes only, useful with low coverage data (requires <code>-g, &#8211;genotypes</code>)</dl>
<p> <code>&#8211;n-matches</code> <i>INT</i></p>
<dl>
<dt>
<dd> Print only top INT matches for each sample, 0 for unlimited. Use negative value to sort by HWE probability rather than the number of discordant sites. Note that average score is used to determine the top matches, not absolute values.</dl>
<p> <code>&#8211;no-HWE-prob</code></p>
<dl>
<dt>
<dd> Disable calculation of HWE probability to reduce memory requirements with comparisons between very large number of sample pairs.</dl>
<p> <code>-p, &#8211;pairs</code> <i>LIST</i></p>
<dl>
<dt>
<dd> A comma-separated list of sample pairs to compare. When the <code>-g</code> option is given, the first sample must be from the query file, the second from the <code>-g</code> file, third from the query file etc (qry,gt[,qry,gt..]). Without the <code>-g</code> option, the pairs are created the same way but both samples are from the query file (qry,qry[,qry,qry..])</dl>
<p> <code>-P, &#8211;pairs-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> A file with tab-delimited sample pairs to compare. The first sample in the pair must come from the query file, the second from the genotypes file when <code>-g</code> is given</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> Restrict to comma-separated list of regions, see <code>Common Options</code></dl>
<p> *-R, &#8211;regions-file&#8217; <i>FILE</i></p>
<dl>
<dt>
<dd> Restrict to regions listed in a file, see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> [<i>qry</i>|<i>gt</i>]:&#8217;LIST&#8217;: List of query samples or <code>-g</code> samples. If neither <code>-s</code> nor <code>-S</code> are given, all possible sample pair combinations are compared </p>
<p> <code>-S, &#8211;samples-file</code> [<i>qry</i>|<i>gt</i>]:&#8217;FILE&#8217; File with the query or <code>-g</code> samples to compare. If neither <code>-s</code> nor <code>-S</code> are given, all possible sample pair combinations are compared </p>
<p> <code>-t, &#8211;targets</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-u, &#8211;use</code> <i>TAG1</i>[,<i>TAG2</i>]</p>
<dl>
<dt>
<dd> specifies which tag to use in the query file (<i>TAG1</i>) and the <code>-g</code> (<i>TAG2</i>) file. By default, the PL tag is used in the query file and GT in the <code>-g</code> file when available.</dl>
<p> <code>Examples:</code> </p>
<dl>
<dt>
<dd>
<pre>
   # Check discordance of all samples from B against all sample in A
   bcftools gtcheck -g A.bcf B.bcf
   # Limit comparisons to the fiven list of samples
   bcftools gtcheck -s gt:a1,a2,a3 -s qry:b1,b2 -g A.bcf B.bcf
   # Compare only two pairs a1,b1 and a1,b2
   bcftools gtcheck -p a1,b1,a1,b2 -g A.bcf B.bcf
</pre>
</dl>
<h3>bcftools head [<i>OPTIONS</i>] [<i>FILE</i>]</h3>
<p> By default, prints all headers from the specified input file to standard output in VCF format. The input file may be in VCF or BCF format; if no <i>FILE</i> is specified, standard input will be read. With appropriate options, only some of the headers and/or additionally some of the variant records will be printed. </p>
<p> The <code>bcftools head</code> command outputs VCF headers almost exactly as they appear in the input file: it may add a ##FILTER=&lt;ID=PASS&gt; header if not already present, but it never adds version or command line information itself.</p>
<h3>Options:</h3>
<p> <code>-h, &#8211;header</code> <i>INT</i></p>
<dl>
<dt>
<dd> Display only the first <i>INT</i> header lines. By default, all header lines are displayed.</dl>
<p> <code>-n, &#8211;records</code> <i>INT</i></p>
<dl>
<dt>
<dd> Also display the first <i>INT</i> variant records. By default, no variant records are displayed.</dl>
<h3>bcftools index [<i>OPTIONS</i>] <i>in.bcf</i>|<i>in.vcf.gz</i></h3>
<p> Creates index for bgzip compressed VCF/BCF files for random access. CSI (coordinate-sorted index) is created by default. The CSI format supports indexing of chromosomes up to length 2^31. TBI (tabix index) index files, which support chromosome lengths up to 2^29, can be created by using the <i>-t/&#8211;tbi</i> option or using the <i>tabix</i> program packaged with htslib. When loading an index file, bcftools will try the CSI first and then the TBI.</p>
<h3>Indexing options:</h3>
<p> <code>-c, &#8211;csi</code></p>
<dl>
<dt>
<dd> generate CSI-format index for VCF/BCF files [default]</dl>
<p> <code>-f, &#8211;force</code></p>
<dl>
<dt>
<dd> overwrite index if it already exists</dl>
<p> <code>-m, &#8211;min-shift </code><i>INT</i></p>
<dl>
<dt>
<dd> set minimal interval size for CSI indices to 2^INT; default: 14</dl>
<p> <code>-o, &#8211;output </code><i>FILE</i></p>
<dl>
<dt>
<dd> output file name. If not set, then the index will be created using the input file name plus a <i>.csi</i> or <i>.tbi</i> extension</dl>
<p> <code>-t, &#8211;tbi</code></p>
<dl>
<dt>
<dd> generate TBI-format index for VCF files</dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<h3>Stats options:</h3>
<p> <code>-a, &#8211;all</code></p>
<dl>
<dt>
<dd> Used in conjunction with <code>-s, &#8211;stats</code>, print per contig stats for all contigs, even those with zero records and those for which no stats are recorded in the index file (shown as <i>.</i>).</dl>
<p> <code>-n, &#8211;nrecords</code></p>
<dl>
<dt>
<dd> print the number of records based on the CSI or TBI index files</dl>
<p> <code>-s, &#8211;stats</code></p>
<dl>
<dt>
<dd> Print per contig stats based on the CSI or TBI index files. Output format is three tab-delimited columns listing the contig name, contig length (<i>.</i> if unknown) and number of records for the contig. Contigs with zero records are not printed by default.</dl>
<h3>bcftools isec [<i>OPTIONS</i>] <i>A.vcf.gz</i> <i>B.vcf.gz</i> [&#8230;]</h3>
<p> Creates intersections, unions and complements of VCF files. Depending on the options, the program can output records from one (or more) files which have (or do not have) corresponding records with the same position in the other files. </p>
<p> <code>-c, &#8211;collapse</code> <i>snps</i>|<i>indels</i>|<i>both</i>|<i>all</i>|<i>some</i>|<i>none</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-C, &#8211;complement</code></p>
<dl>
<dt>
<dd> output positions present only in the first file but missing in the others</dl>
<p> <code>-e, &#8211;exclude</code> <i>&#8211;</i>|<i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. If <code>-e</code> (or <code>-i</code>) appears only once, the same filtering expression will be applied to all input files. Otherwise, <code>-e</code> or <code>-i</code> must be given for each input file. To indicate that no filtering should be performed on a file, use &quot;-&quot; in place of <i>EXPRESSION</i>, as shown in the example below. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-f, &#8211;apply-filters</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. See discussion of <code>-e, &#8211;exclude</code> above.</dl>
<p> <code>-n, &#8211;nfiles</code> [+-=]<i>INT</i>|~<i>BITMAP</i></p>
<dl>
<dt>
<dd> output positions present in this many (=), this many or more (+), this many or fewer (-), or the exact same (~) files</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code>. When several files are being output, their names are controlled via <code>-p</code> instead.</dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-p, &#8211;prefix</code> <i>DIR</i></p>
<dl>
<dt>
<dd> if given, subset each of the input files accordingly. See also <code>-w</code>.</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-w, &#8211;write</code> <i>LIST</i></p>
<dl>
<dt>
<dd> list of input files to output given as 1-based indices. With <code>-p</code> and no <code>-w</code>, all files are written.</dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file. This is done automatically with the <code>-p</code> option.</dl>
<h3>Examples:</h3>
<p> Create intersection and complements of two sets saving the output in dir/* </p>
<dl>
<dt>
<dd>
<pre>
    bcftools isec -p dir A.vcf.gz B.vcf.gz
</pre>
</dl>
<p> Filter sites in A (require INFO/MAF&gt;=0.01) and B (require INFO/dbSNP) but not in C, and create an intersection, including only sites which appear in at least two of the files after filters have been applied </p>
<dl>
<dt>
<dd>
<pre>
    bcftools isec -e'MAF&lt;0.01' -i'dbSNP=1' -e- A.vcf.gz B.vcf.gz C.vcf.gz -n +2 -p dir
</pre>
</dl>
<p> Extract and write records from A shared by both A and B using exact allele match </p>
<dl>
<dt>
<dd>
<pre>
    bcftools isec -p dir -n=2 -w1 A.vcf.gz B.vcf.gz
</pre>
</dl>
<p> Extract records private to A or B comparing by position only </p>
<dl>
<dt>
<dd>
<pre>
    bcftools isec -p dir -n-1 -c all A.vcf.gz B.vcf.gz
</pre>
</dl>
<p> Print a list of records which are present in A and B but not in C and D </p>
<dl>
<dt>
<dd>
<pre>
    bcftools isec -n~1100 -c all A.vcf.gz B.vcf.gz C.vcf.gz D.vcf.gz
</pre>
</dl>
<h3>bcftools merge [<i>OPTIONS</i>] <i>A.vcf.gz</i> <i>B.vcf.gz</i> [&#8230;]</h3>
<p> Merge multiple VCF/BCF files from non-overlapping sample sets to create one multi-sample file. For example, when merging file <i>A.vcf.gz</i> containing samples <i>S1</i>, <i>S2</i> and <i>S3</i> and file <i>B.vcf.gz</i> containing samples <i>S3</i> and <i>S4</i>, the output file will contain five samples named <i>S1</i>, <i>S2</i>, <i>S3</i>, <i>2:S3</i> and <i>S4</i>. </p>
<p> Note that it is responsibility of the user to ensure that the sample names are unique across all files. If they are not, the program will exit with an error unless the option <code>&#8211;force-samples</code> is given. The sample names can be also given explicitly using the <code>&#8211;print-header</code> and <code>&#8211;use-header</code> options. </p>
<p> Note that only records from different files can be merged, never from the same file. For &quot;vertical&quot; merge take a look at <code>bcftools concat</code> or <code>bcftools norm -m</code> instead. </p>
<p> <code>&#8211;force-samples</code></p>
<dl>
<dt>
<dd> if the merged files contain duplicate samples names, proceed anyway. Duplicate sample names will be resolved by prepending the index of the file as it appeared on the command line to the conflicting sample name (see <i>2:S3</i> in the above example).</dl>
<p> <code>&#8211;print-header</code></p>
<dl>
<dt>
<dd> print only merged header and exit</dl>
<p> <code>&#8211;use-header</code> <i>FILE</i></p>
<dl>
<dt>
<dd> use the VCF header in the provided text <i>FILE</i></dl>
<p> <code>-0 &#8211;missing-to-ref</code></p>
<dl>
<dt>
<dd> assume genotypes at missing sites are 0/0</dl>
<p> <code>-f, &#8211;apply-filters</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-F, &#8211;filter-logic</code> <i>x</i>|<i>+</i></p>
<dl>
<dt>
<dd> Set the output record to PASS if any of the inputs is PASS (<i>x</i>), or apply all filters (<i>+</i>), which is the default.</dl>
<p> <code>-g, &#8211;gvcf</code> <i>&#8211;</i>|<i>FILE</i></p>
<dl>
<dt>
<dd> merge gVCF blocks, INFO/END tag is expected. If the reference fasta file <i>FILE</i> is not given and the dash (<i>&#8211;</i>) is given, unknown reference bases generated at gVCF block splits will be substituted with N&#8217;s. The <code>&#8211;gvcf</code> option uses the following default INFO rules: <code>-i QS:sum,MinDP:min,I16:sum,IDV:max,IMF:max</code> and the following missing rules: <code>-M PL:max,AD:0</code>.</dl>
<p> <code>-i, &#8211;info-rules</code> <i>&#8211;</i>|<i>TAG:METHOD</i>[,&#8230;]</p>
<dl>
<dt>
<dd> Rules for merging INFO fields (scalars or vectors) or <i>&#8211;</i> to disable the default rules. <i>METHOD</i> is one of <i>sum</i>, <i>avg</i>, <i>min</i>, <i>max</i>, <i>join</i>. Default is <i>DP:sum,DP4:sum</i> if these fields exist in the input files. Fields with no specified rule will take the value from the first input file. The merged QUAL value is currently set to the maximum. This behaviour is not user controllable at the moment.</dl>
<p> <code>-l, &#8211;file-list</code> <i>FILE</i></p>
<dl>
<dt>
<dd> Read file names from <i>FILE</i>, one file name per line.</dl>
<p> <code>-L, &#8211;local-alleles</code> <i>INT</i></p>
<dl>
<dt>
<dd> Sites with many alternate alleles can require extremely large storage space which can exceed the 2GB size limit representable by BCF. This is caused by Number=G tags (such as FORMAT/PL) which store a value for each combination of reference and alternate alleles. The <code>-L, &#8211;local-alleles</code> option allows to replace such tags with a localized tag (FORMAT/LPL) which only includes a subset of alternate alleles relevant for that sample. A new FORMAT/LAA tag is added which lists 1-based indices of the alternate alleles relevant (local) for the current sample. The number <i>INT</i> gives the maximum number of alternate alleles that can be included in the PL tag. The default value is 0 which disables the feature and outputs values for all alternate alleles.</dl>
<p> <code>-m, &#8211;merge</code> <i>snps</i>|<i>indels</i>|<i>both</i>|<i>snp-ins-del</i>|<i>all</i>|<i>none</i>|<i>id</i></p>
<dl>
<dt>
<dd> The option controls what types of multiallelic records can be created:</dl>
<dl>
<dt>
<dd>
<pre>
-m none        ..  no new multiallelics, output multiple records instead
-m snps        ..  allow multiallelic SNP records
-m indels      ..  allow multiallelic indel records
-m both        ..  both SNP and indel records can be multiallelic
-m all         ..  SNP records can be merged with indel records
-m snp-ins-del ..  allow multiallelic SNVs, insertions, deletions, but don't mix them
-m id          ..  merge by ID
</pre>
</dl>
<p> <code>-M, &#8211;missing-rules</code> <i>&#8211;</i>|<i>TAG:METHOD</i>[,&#8230;]</p>
<dl>
<dt>
<dd> Rules for merging vector tags at multiallelic sites. When input files have different alternate alleles, vector fields pertaining to unobserved alleles are set to missing (<i>.</i>) by default. The <i>METHOD</i> is one of <i>.</i> (the default, use missing values), <i>NUMBER</i> (use a constant value, e.g. 0), <i>max</i> (the maximum value observed for other alleles in the sample). When <code>&#8211;gvcf</code> option is set, the rule <code>-M PL:max,AD:0</code> is implied. This can be overriden with providing <code>-M &#8211;</code> or <code>-M PL:.,AD:.</code>. Note that if the unobserved allele is explicitly present as <i>&lt;*&gt;</i> or <i>&lt;NON_REF&gt;</i>, then its corresponding value will be used regardless of <code>-M</code> settings.</dl>
<p> <code>&#8211;no-index</code></p>
<dl>
<dt>
<dd> the option allows to merge files without indexing them first. In order for this option to work, the user must ensure that the input files have chromosomes in the same order and consistent with the order of sequences in the VCF header.</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>bcftools mpileup [<i>OPTIONS</i>] <code>-f</code> <i>ref.fa</i> <i>in.bam</i> [<i>in2.bam</i> [&#8230;]]</h3>
<p> Generate VCF or BCF containing genotype likelihoods for one or multiple alignment (BAM or CRAM) files. This is based on the original <code>samtools mpileup</code> command (with the <code>-v</code> or <code>-g</code> options) producing genotype likelihoods in VCF or BCF format, but not the textual pileup output. The <code>mpileup</code> command was transferred to bcftools in order to avoid errors resulting from use of incompatible versions of samtools and bcftools when using in the mpileup+bcftools call pipeline. </p>
<p> Individuals are identified from the SM tags in the @RG header lines. Multiple individuals can be pooled in one alignment file, also one individual can be separated into multiple files. If sample identifiers are absent, each input file is regarded as one sample. </p>
<p> Note that there are two orthogonal ways to specify locations in the input file; via <code>-r</code> <i>region</i> and <code>-t</code> <i>positions</i>. The former uses (and requires) an index to do random access while the latter streams through the file contents filtering out the specified regions, requiring no index. The two may be used in conjunction. For example a BED file containing locations of genes in chromosome 20 could be specified using <code>-r 20 -t chr20.bed</code>, meaning that the index is used to find chromosome 20 and then it is filtered for the regions listed in the BED file. Also note that the <code>-r</code> option can be much slower than <code>-t</code> with many regions and can require more memory when multiple regions and many alignment files are processed.</p>
<h3>Input options</h3>
<p> <code>-6, &#8211;illumina1.3+</code></p>
<dl>
<dt>
<dd> Assume the quality is in the Illumina 1.3+ encoding.</dl>
<p> <code>-A, &#8211;count-orphans</code></p>
<dl>
<dt>
<dd> Do not skip anomalous read pairs in variant calling.</dl>
<p> <code>-b, &#8211;bam-list</code> <i>FILE</i></p>
<dl>
<dt>
<dd> List of input alignment files, one file per line [null]</dl>
<p> <code>-B, &#8211;no-BAQ</code></p>
<dl>
<dt>
<dd> Disable probabilistic realignment for the computation of base alignment quality (BAQ). BAQ is the Phred-scaled probability of a read base being misaligned. Applying this option greatly helps to reduce false SNPs caused by misalignments.</dl>
<p> <code>-C, &#8211;adjust-MQ</code> <i>INT</i></p>
<dl>
<dt>
<dd> Coefficient for downgrading mapping quality for reads containing excessive mismatches. Given a read with a phred-scaled probability q of being generated from the mapped position, the new mapping quality is about sqrt((INT-q)/INT)*INT. A zero value (the default) disables this functionality.</dl>
<p> <code>-D, &#8211;full-BAQ</code></p>
<dl>
<dt>
<dd> Run the BAQ algorithm on all reads, not just those in problematic regions. This matches the behaviour for Bcftools 1.12 and earlier. </p>
<p> By default mpileup uses heuristics to decide when to apply the BAQ algorithm. Most sequences will not be BAQ adjusted, giving a CPU time closer to &#8211;no-BAQ, but it will still be applied in regions with suspected problematic alignments. This has been tested to work well on single sample data with even allele frequency, but the reliability is unknown for multi-sample calling and for low allele frequency variants so full BAQ is still recommended in those scenarios.</dl>
<p> <code>-d, &#8211;max-depth</code> <i>INT</i></p>
<dl>
<dt>
<dd> At a position, read maximally <i>INT</i> reads per input file. Note that the original <code>samtools mpileup</code> command had a minimum value of <i>8000/n</i> where <i>n</i> was the number of input files given to mpileup. This means that in <code>samtools mpileup</code> the default was highly likely to be increased and the <code>-d</code> parameter would have an effect only once above the cross-sample minimum of 8000. This behavior was problematic when working with a combination of single- and multi-sample bams, therefore in <code>bcftools mpileup</code> the user is given the full control (and responsibility), and an informative message is printed instead [250]</dl>
<p> <code>-E, &#8211;redo-BAQ</code></p>
<dl>
<dt>
<dd> Recalculate BAQ on the fly, ignore existing BQ tags</dl>
<p> <code>-f, &#8211;fasta-ref</code> <i>FILE</i></p>
<dl>
<dt>
<dd> The <code>faidx</code>-indexed reference file in the FASTA format. The file can be optionally compressed by <code>bgzip</code>. Reference is required by default unless the <code>&#8211;no-reference</code> option is set [null]</dl>
<p> <code>&#8211;no-reference</code></p>
<dl>
<dt>
<dd> Do not require the <code>&#8211;fasta-ref</code> option.</dl>
<p> <code>-G, &#8211;read-groups</code> <i>FILE</i></p>
<dl>
<dt>
<dd> list of read groups to include or exclude if prefixed with &quot;^&quot;. One read group per line. This file can also be used to assign new sample names to read groups by giving the new sample name as a second white-space-separated field, like this: &quot;read_group_id new_sample_name&quot;. If the read group name is not unique, also the bam file name can be included: &quot;read_group_id file_name sample_name&quot;. If all reads from the alignment file should be treated as a single sample, the asterisk symbol can be used: &quot;* file_name sample_name&quot;. Alignments without a read group ID can be matched with &quot;?&quot;. <code>NOTE:</code> The meaning of <code>bcftools mpileup -G</code> is the opposite of <code>samtools mpileup -G</code>.</dl>
<dl>
<dt>
<dd>
<pre>
    RG_ID_1
    RG_ID_2  SAMPLE_A
    RG_ID_3  SAMPLE_A
    RG_ID_4  SAMPLE_B
    RG_ID_5  FILE_1.bam  SAMPLE_A
    RG_ID_6  FILE_2.bam  SAMPLE_A
    *        FILE_3.bam  SAMPLE_C
    ?        FILE_3.bam  SAMPLE_D
</pre>
</dl>
<p> <code>&#8211;indels-2.0</code></p>
<dl>
<dt>
<dd> A new EXPERIMENTAL indel calling model which aims to address some known deficiencies of the current indel calling algorithm. Specifically, it uses diploid reference consensus sequence. Note that in the current version it has the potential to increase sensitivity but at the cost of decreased specificity</dl>
<p> <code>-q, -min-MQ</code> <i>INT</i></p>
<dl>
<dt>
<dd> Minimum mapping quality for an alignment to be used [0]</dl>
<p> <code>-Q, &#8211;min-BQ</code> <i>INT</i></p>
<dl>
<dt>
<dd> Minimum base quality for a base to be considered [13]</dl>
<p> <code>&#8211;max-BQ</code> <i>INT</i></p>
<dl>
<dt>
<dd> Caps the base quality to a maximum value [60]. This can be particularly useful on technologies that produce overly optimistic high qualities, leading to too many false positives or incorrect genotype assignments.</dl>
<p> <code>-r, &#8211;regions</code> <i>CHR</i>|<i>CHR:POS</i>|<i>CHR:FROM-TO</i>|<i>CHR:FROM-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> Only generate mpileup output in given regions. Requires the alignment files to be indexed. If used in conjunction with -l then considers the intersection; see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> As for <code>-r, &#8211;regions</code>, but regions read from FILE; see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;ignore-RG</code></p>
<dl>
<dt>
<dd> Ignore RG tags. Treat all reads in one alignment file as one sample.</dl>
<p> <code>&#8211;ls, &#8211;skip-all-set</code></p>
<dl>
<dt>
<dd> Skip reads with all of the FLAG bits set [null]</dl>
<p> <code>&#8211;ns, &#8211;skip-any-set</code></p>
<dl>
<dt>
<dd> Skip reads with any of the FLAG bits set. This option replaces and is synonymous to the deprecated <code>&#8211;ff, &#8211;excl-flags</code> [UNMAP,SECONDARY,QCFAIL,DUP]</dl>
<p> <code>&#8211;lu, &#8211;skip-all-unset</code></p>
<dl>
<dt>
<dd> Skip reads with all of the FLAG bits unset. This option replaces and is synonymous to the deprecated <code>&#8211;rf, &#8211;incl-flags</code> [null]</dl>
<p> <code>&#8211;nu, &#8211;skip-any-unset</code></p>
<dl>
<dt>
<dd> Skip reads with any of the FLAG bits unset [null]</dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> list of sample names. See <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> file of sample names to include or exclude if prefixed with &quot;^&quot;. One sample per line. This file can also be used to rename samples by giving the new sample name as a second white-space-separated column, like this: &quot;old_name new_name&quot;. If a sample name contains spaces, the spaces can be escaped using the backslash character, for example &quot;Not\ a\ good\ sample\ name&quot;.</dl>
<p> <code>-t, &#8211;targets</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-x, &#8211;ignore-overlaps</code></p>
<dl>
<dt>
<dd> Disable read-pair overlap detection.</dl>
<p> <code>&#8211;seed</code> <i>INT</i></p>
<dl>
<dt>
<dd> Set the random number seed used when sub-sampling deep regions [0].</dl>
<h3>Output options</h3>
<p> <code>-a, &#8211;annotate</code> <i>LIST</i></p>
<dl>
<dt>
<dd> Comma-separated list of FORMAT and INFO tags to output. (case-insensitive, the &quot;FORMAT/&quot; prefix is optional, and use &quot;?&quot; to list available annotations on the command line) [null]:</dl>
<dl>
<dt>
<dd>
FORMAT / AD..Allelic depth(Number = R, Type = Integer) FORMAT / ADF..Allelic depths on the forward strand(Number = R, Type = Integer) FORMAT / ADR..Allelic depths on the reverse strand(Number = R, Type = Integer) FORMAT / DP..Number of high &#8211; quality bases(Number = 1, Type = Integer) FORMAT / SP..Phred &#8211; scaled strand bias P &#8211; value(Number = 1, Type = Integer) FORMAT / SCR..Number of soft &#8211; clipped reads(Number = 1, Type = Integer) INFO / AD..Total allelic depth(Number = R, Type = Integer) INFO / ADF..Total allelic depths on the forward strand(Number = R, Type = Integer) INFO / ADR..Total allelic depths on the reverse strand(Number = R, Type = Integer) INFO / SCR..Number of soft &#8211; clipped reads(Number = 1, Type = Integer) FORMAT / DV..Deprecated in favor of FORMAT / AD;<br />
Number of high &#8211; quality non &#8211; reference bases, (Number = 1, Type = Integer)<br />
                                                        FORMAT<br />
                                                    / DP4..Deprecated in favor of FORMAT / ADF and FORMAT / ADR;<br />
Number of high &#8211; quality ref &#8211; forward, ref &#8211; reverse,<br />
    alt &#8211; forward and alt &#8211; reverse bases(Number = 4, Type = Integer) FORMAT / DPR..Deprecated in favor of FORMAT / AD; Number of high-quality bases for each observed allele (Number=R,Type=Integer)<br />
INFO/DPR    .. Deprecated in favor of INFO/AD; Number of high-quality bases for each observed allele (Number=R,Type=Integer)
</dl>
<p> <code>-g, &#8211;gvcf</code> <i>INT</i>[,&#8230;]</p>
<dl>
<dt>
<dd> output gVCF blocks of homozygous REF calls, with depth (DP) ranges specified by the list of integers. For example, passing <i>5,15</i> will group sites into two types of gVCF blocks, the first with minimum per-sample DP from the interval [5,15) and the latter with minimum depth 15 or more. In this example, sites with minimum per-sample depth less than 5 will be printed as separate records, outside of gVCF blocks.</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> Write output to <i>FILE</i>, rather than the default of standard output. (The same short option is used for both <code>&#8211;open-prob</code> and <code>&#8211;output</code>. If <code>-o</code>&#8216;s argument contains any non-digit characters other than a leading + or &#8211; sign, it is interpreted as <code>&#8211;output</code>. Usually the filename extension will take care of this, but to write to an entirely numeric filename use <code>-o ./123</code> or <code>&#8211;output 123</code>.)</dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-U, &#8211;mwu-u</code></p>
<dl>
<dt>
<dd> The the previous Mann-Whitney U test score from version 1.12 and earlier. This is a probability score, but importantly it folds probabilities above or below the desired score into the same P. The new Mann-Whitney U test score is a &quot;Z score&quot;, expressing the score as the number of standard deviations away from the mean (with zero being matching the mean). It keeps both positive and negative values. This can be important for some tests where errors are asymmetric. </p>
<dl>
<dt>
<dd>
<pre>
This option changes the INFO field names produced back to the ones
used by the earlier Bcftools releases.  For excample BQBZ becomes
BQB.
</pre>
</dl>
</dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>Options for SNP/INDEL genotype likelihood computation</h3>
<p> <code>-X, &#8211;config</code> <i>STR</i></p>
<dl>
<dt>
<dd> Specify a platform specific configuration profile. The profile should be one of <i>1.12</i>, <i>illumina</i>, <i>ont</i> or <i>pacbio-ccs</i>. Settings applied are as follows: </p>
<dl>
<dt>
<dd>
1.12 &#8211; Q13 &#8211; h100 &#8211; m1 illumina[default values] ont &#8211; B &#8211; Q5&#8211; max &#8211; BQ 30 &#8211; I pacbio &#8211; ccs &#8211; D &#8211; Q5&#8211; max &#8211; BQ 50 &#8211; F0 .1 &#8211; o25 &#8211; e1 &#8211; M99999
</dl>
</dl>
<p> <code>&#8211;ar, &#8211;ambig-reads</code> <i>drop</i>|<i>incAD</i>|<i>incAD0</i></p>
<dl>
<dt>
<dd> What to do with ambiguous indel reads that do not span an entire short tandem repeat region: discard ambiguous reads from calling and do not increment high-quality AD depth counters (<i>drop</i>), exclude from calling but increment AD counters proportionally (<i>incAD</i>), exclude from calling and increment the first value of the AD counter (<i>incAD0</i>) [<i>drop</i>]</dl>
<p> <code>-e, &#8211;ext-prob</code> <i>INT</i></p>
<dl>
<dt>
<dd> Phred-scaled gap extension sequencing error probability. Reducing <i>INT</i> leads to longer indels [20]</dl>
<p> <code>-F, &#8211;gap-frac</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> Minimum fraction of gapped reads [0.002]</dl>
<p> <code>-h, &#8211;tandem-qual</code> <i>INT</i></p>
<dl>
<dt>
<dd> Coefficient for modeling homopolymer errors. Given an <i>l</i>-long homopolymer run, the sequencing error of an indel of size s is modeled as <i>INT</i>*s/l [500] Increasing this informs the caller that indels in long homopolymers are more likely genuine and less likely to be sequencing artifacts. Hence increasing tandem-qual will have higher recall and lower precision. Bcftools 1.12 and earlier had a default of 100, which was tuned around more error prone instruments. Note changing this may have a minor impact on SNP calling too. For maximum SNP calling accuracy, it may be preferable to adjust this lower again, although this will adversely affect indels.</dl>
<p> <code>&#8211;indel-bias</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> Skews the indel scores up or down, trading recall (low false-negative) vs precision (low false-positive) [1.0]. In Bcftools 1.12 and earlier this parameter didn&#8217;t exist, but had an implied value of 1.0. If you are planning to do heavy filtering of variants, selecting the best quality ones only (favouring precision over recall), it is advisable to set this lower (such as 0.75) while higher depth samples or where you favour recall rates over precision may work better with a higher value such as 2.0.</dl>
<p> <code>&#8211;indel-size</code> <i>INT</i></p>
<dl>
<dt>
<dd> Indel window size to use when assessing the quality of candidate indels. Note that although the window size approximately corresponds to the maximum indel size considered, it is not an exact threshold [110]</dl>
<p> <code>-I, &#8211;skip-indels</code></p>
<dl>
<dt>
<dd> Do not perform INDEL calling</dl>
<p> <code>-L, &#8211;max-idepth</code> <i>INT</i></p>
<dl>
<dt>
<dd> Skip INDEL calling if the average per-sample depth is above <i>INT</i> [250]</dl>
<p> <code>-m, &#8211;min-ireads</code> <i>INT</i></p>
<dl>
<dt>
<dd> Minimum number gapped reads for indel candidates <i>INT</i> [1]</dl>
<p> <code>-M, &#8211;max-read-len</code> <i>INT</i></p>
<dl>
<dt>
<dd> The maximum read length permitted by the BAQ algorithm [500]. Variants are still called on longer reads, but they will not be passed through the BAQ method. This limit exists to prevent excessively long BAQ times and high memory usage. Note if partial BAQ is enabled with <i>-D</i> then raising this parameter will likely not have a significant a CPU cost.</dl>
<p> <code>-o, &#8211;open-prob</code> <i>INT</i></p>
<dl>
<dt>
<dd> Phred-scaled gap open sequencing error probability. Reducing <i>INT</i> leads to more indel calls. (The same short option is used for both <code>&#8211;open-prob</code> and <code>&#8211;output</code>. When -o&#8217;s argument contains only an optional + or &#8211; sign followed by the digits 0 to 9, it is interpreted as <code>&#8211;open-prob</code>.) [40]</dl>
<p> <code>-p, &#8211;per-sample-mF</code></p>
<dl>
<dt>
<dd> Apply <code>-m</code> and <code>-F</code> thresholds per sample to increase sensitivity of calling. By default both options are applied to reads pooled from all samples.</dl>
<p> <code>-P, &#8211;platforms</code> <i>STR</i></p>
<dl>
<dt>
<dd> Comma-delimited list of platforms (determined by <code>@RG-PL</code>) from which indel candidates are obtained. It is recommended to collect indel candidates from sequencing technologies that have low indel error rate such as ILLUMINA [all]</dl>
<h3>Examples:</h3>
<p> Call SNPs and short INDELs, then mark low quality sites and sites with the read depth exceeding a limit. (The read depth should be adjusted to about twice the average read depth as higher read depths usually indicate problematic regions which are often enriched for artefacts.) One may consider to add <code>-C50</code> to mpileup if mapping quality is overestimated for reads containing excessive mismatches. Applying this option usually helps for BWA-backtrack alignments, but may not other aligners. </p>
<dl>
<dt>
<dd>
<pre>
    bcftools mpileup -Ou -f ref.fa aln.bam | \
    bcftools call -Ou -mv | \
    bcftools filter -s LowQual -e '%QUAL&lt;20 || DP&gt;100' &gt; var.flt.vcf
</pre>
</dl>
<h3>bcftools norm [<i>OPTIONS</i>] <i>file.vcf.gz</i></h3>
<p> Left-align and normalize indels, check if REF alleles match the reference, split multiallelic sites into multiple rows; recover multiallelics from multiple rows. Left-alignment and normalization will only be applied if the <code>&#8211;fasta-ref</code> option is supplied. </p>
<p> <code>-a, &#8211;atomize</code></p>
<dl>
<dt>
<dd> Decompose complex variants, e.g. split MNVs into consecutive SNVs. See also <code>&#8211;atom-overlaps</code> and <code>&#8211;old-rec-tag</code>.</dl>
<p> <code>&#8211;atom-overlaps</code> <i>.</i>|<i>*</i></p>
<dl>
<dt>
<dd> Alleles missing because of an overlapping variant can be set either to missing (.) or to the star alele (*), as recommended by the VCF specification. IMPORTANT: Note that asterisk is expaneded by shell and must be put in quotes or escaped by a backslash:</dl>
<dl>
<dt>
<dd>
<pre>
    # Before atomization:
    100  CC  C,GG   1/2
    # After:
    #   bcftools norm -a .
    100         C         G      ./1
    100         CC         C      1/.
    101         C         G      ./1
    # After:
    #   bcftools norm -a '*'
    #   bcftools norm -a \*
    100         C         G,*    2/1
    100         CC         C,*    1/2
    101         C         G,*    2/1
</pre>
</dl>
<p> <code>-c, &#8211;check-ref</code> <i>e</i>|<i>w</i>|<i>x</i>|<i>s</i></p>
<dl>
<dt>
<dd> what to do when incorrect or missing REF allele is encountered: exit (<i>e</i>), warn (<i>w</i>), exclude (<i>x</i>), or set/fix (<i>s</i>) bad sites. The <i>w</i> option can be combined with <i>x</i> and <i>s</i>. Note that <i>s</i> can swap alleles and will update genotypes (GT) and AC counts, but will not attempt to fix PL or other fields. Also note, and this cannot be stressed enough, that <i>s</i> will NOT fix strand issues in your VCF, do NOT use it for that purpose!!! (Instead see <i></i> &lt;<a rel="nofollow" href="http://samtools.github.io/bcftools/howtos/plugin.af-dist.html">http://samtools.github.io/bcftools/howtos/plugin.af-dist.html</a>&gt; and <i></i> &lt;<a rel="nofollow" href="http://samtools.github.io/bcftools/howtos/plugin.fixref.html.">http://samtools.github.io/bcftools/howtos/plugin.fixref.html.</a>&gt;)</dl>
<p> <code>-d, &#8211;rm-dup</code> <i>snps</i>|<i>indels</i>|<i>both</i>|<i>all</i>|<i>exact</i></p>
<dl>
<dt>
<dd> If a record is present multiple times, output only the first instance. See also <code>&#8211;collapse</code> in <code>Common Options</code>.</dl>
<p> <code>-D, &#8211;remove-duplicates</code></p>
<dl>
<dt>
<dd> If a record is present in multiple files, output only the first instance. Alias for <code>-d none</code>, deprecated.</dl>
<p> <code>-f, &#8211;fasta-ref</code> <i>FILE</i></p>
<dl>
<dt>
<dd> reference sequence. Supplying this option will turn on left-alignment and normalization, however, see also the <code>&#8211;do-not-normalize</code> option below.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> try to proceed with <code>-m-</code> even if malformed tags with incorrect number of fields are encountered, discarding such tags. (Experimental, use at your own risk.)</dl>
<p> <code>&#8211;keep-sum</code> <i>TAG</i>[,&#8230;]</p>
<dl>
<dt>
<dd> keep vector sum constant when splitting multiallelic sites. Only AD tag is currently supported. See also <i></i> &lt;<a rel="nofollow" href="https://github.com/samtools/bcftools/issues/360">https://github.com/samtools/bcftools/issues/360</a>&gt;</dl>
<p> <code>-m, &#8211;multiallelics</code> <code>&#8211;</code>|<code>+</code>[<i>snps</i>|<i>indels</i>|<i>both</i>|<i>any</i>]</p>
<dl>
<dt>
<dd> split multiallelic sites into biallelic records (<code>&#8211;</code>) or join biallelic sites into multiallelic records (<code>+</code>). An optional type string can follow which controls variant types which should be split or merged together: If only SNP records should be split or merged, specify <i>snps</i>; if both SNPs and indels should be merged separately into two records, specify <i>both</i>; if SNPs and indels should be merged into a single record, specify <i>any</i>.</dl>
<p> <code>&#8211;multi-overlaps</code> <i>0</i>|<i>.</i></p>
<dl>
<dt>
<dd> use the reference (<i>0</i>) or missing (<i>.</i>) allele for overlapping alleles after splitting multiallelic sites</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-N, &#8211;do-not-normalize</code></p>
<dl>
<dt>
<dd> the <i>-c s</i> option can be used to fix or set the REF allele from the reference <i>-f</i>. The <i>-N</i> option will not turn on indel normalisation as the <i>-f</i> option normally implies</dl>
<p> <code>&#8211;old-rec-tag</code> <i>STR</i></p>
<dl>
<dt>
<dd> Add INFO/STR annotation with the original record. The format of the annotation is CHROM|POS|REF|ALT|USED_ALT_IDX.</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;strict-filter</code></p>
<dl>
<dt>
<dd> when merging (<i>-m+</i>), merged site is PASS only if all sites being merged PASS</dl>
<p> <code>-t, &#8211;targets</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-w, &#8211;site-win</code> <i>INT</i></p>
<dl>
<dt>
<dd> maximum distance between two records to consider when locally sorting variants which changed position during the realignment</dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>bcftools [plugin <i>NAME</i>|+<i>NAME</i>] <i>[OPTIONS]</i> <i>FILE</i> &#8212; <i>[PLUGIN OPTIONS]</i></h3>
<p> A common framework for various utilities. The plugins can be used the same way as normal commands only their name is prefixed with &quot;+&quot;. Most plugins accept two types of parameters: general options shared by all plugins followed by a separator, and a list of plugin-specific options. There are some exceptions to this rule, some plugins do not accept the common options and implement their own parameters. Therefore please pay attention to the usage examples that each plugin comes with.</p>
<h3>VCF input options:</h3>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<h3>VCF output options:</h3>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>Plugin options:</h3>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> list plugin&#8217;s options</dl>
<p> <code>-l, &#8211;list-plugins</code></p>
<dl>
<dt>
<dd> List all available plugins. </p>
<p> By default, appropriate system directories are searched for installed plugins. You can override this by setting the BCFTOOLS_PLUGINS environment variable to a colon-separated list of directories to search. If BCFTOOLS_PLUGINS begins with a colon, ends with a colon, or contains adjacent colons, the system directories are also searched at that position in the list of directories.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> print debugging information to debug plugin failure</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
<dd> print version string and exit</dl>
<h3>List of plugins coming with the distribution:</h3>
<p> <code>ad-bias</code></p>
<dl>
<dt>
<dd> find positions with wildly varying ALT allele frequency (Fisher test on FMT/AD)</dl>
<p> <code>add-variantkey</code></p>
<dl>
<dt>
<dd> add VariantKey INFO fields VKX and RSX</dl>
<p> <code>af-dist</code></p>
<dl>
<dt>
<dd> collect AF deviation stats and GT probability distribution given AF and assuming HWE</dl>
<p> <code>allele-length</code></p>
<dl>
<dt>
<dd> count the frequency of the length of REF, ALT and REF+ALT</dl>
<p> <code>check-ploidy</code></p>
<dl>
<dt>
<dd> check if ploidy of samples is consistent for all sites</dl>
<p> <code>check-sparsity</code></p>
<dl>
<dt>
<dd> print samples without genotypes in a region or chromosome</dl>
<p> <code>color-chrs</code></p>
<dl>
<dt>
<dd> color shared chromosomal segments, requires trio VCF with phased GTs</dl>
<p> <code>contrast</code></p>
<dl>
<dt>
<dd> runs a basic association test, per-site or in a region, and checks for novel alleles and genotypes in two groups of samples. Adds the following INFO annotations: </p>
<dl>
<dt>
<dd> &bull; PASSOC .. Fisher&#8217;s exact test probability of genotypic association (REF vs non-REF allele)</dl>
<dl>
<dt>
<dd> &bull; FASSOC .. proportion of non-REF allele in controls and cases</dl>
<dl>
<dt>
<dd> &bull; NASSOC .. number of control-ref, control-alt, case-ref and case-alt alleles</dl>
<dl>
<dt>
<dd> &bull; NOVELAL .. lists samples with a novel allele not observed in the control group</dl>
<dl>
<dt>
<dd> &bull; NOVELGT .. lists samples with a novel genotype not observed in the control group</dl>
</dl>
<p> <code>counts</code></p>
<dl>
<dt>
<dd> a minimal plugin which counts number of SNPs, Indels, and total number of sites.</dl>
<p> <code>dosage</code></p>
<dl>
<dt>
<dd> print genotype dosage. By default the plugin searches for PL, GL and GT, in that order.</dl>
<p> <code>fill-from-fasta</code></p>
<dl>
<dt>
<dd> fill INFO or REF field based on values in a fasta file</dl>
<p> <code>fill-tags</code></p>
<dl>
<dt>
<dd> set various INFO tags. The list of tags supported in this version: </p>
<dl>
<dt>
<dd> &bull; INFO/AC Number:A Type:Integer .. Allele count in genotypes</dl>
<dl>
<dt>
<dd> &bull; INFO/AC_Hom Number:A Type:Integer .. Allele counts in homozygous genotypes</dl>
<dl>
<dt>
<dd> &bull; INFO/AC_Het Number:A Type:Integer .. Allele counts in heterozygous genotypes</dl>
<dl>
<dt>
<dd> &bull; INFO/AC_Hemi Number:A Type:Integer .. Allele counts in hemizygous genotypes</dl>
<dl>
<dt>
<dd> &bull; INFO/AF Number:A Type:Float .. Allele frequency</dl>
<dl>
<dt>
<dd> &bull; INFO/AN Number:1 Type:Integer .. Total number of alleles in called genotypes</dl>
<dl>
<dt>
<dd> &bull; INFO/ExcHet Number:A Type:Float .. Test excess heterozygosity; 1=good, 0=bad</dl>
<dl>
<dt>
<dd> &bull; INFO/END Number:1 Type:Integer .. End position of the variant</dl>
<dl>
<dt>
<dd> &bull; INFO/F_MISSING Number:1 Type:Float .. Fraction of missing genotypes</dl>
<dl>
<dt>
<dd> &bull; INFO/HWE Number:A Type:Float .. HWE test (PMID:15789306); 1=good, 0=bad</dl>
<dl>
<dt>
<dd> &bull; INFO/MAF Number:A Type:Float .. Minor Allele frequency</dl>
<dl>
<dt>
<dd> &bull; INFO/NS Number:1 Type:Integer .. Number of samples with data</dl>
<dl>
<dt>
<dd> &bull; INFO/TYPE Number:. Type:String .. The record type (REF,SNP,MNP,INDEL,etc)</dl>
<dl>
<dt>
<dd> &bull; FORMAT/VAF Number:A Type:Float .. The fraction of reads with the alternate allele, requires FORMAT/AD or ADF+ADR</dl>
<dl>
<dt>
<dd> &bull; FORMAT/VAF1 Number:1 Type:Float .. The same as FORMAT/VAF but for all alternate alleles cumulatively</dl>
<dl>
<dt>
<dd> &bull; TAG=func(TAG) Number:1 Type:Integer .. Experimental support for user-defined expressions such as &quot;DP=sum(DP)&quot;</dl>
</dl>
<p> <code>fixploidy</code></p>
<dl>
<dt>
<dd> sets correct ploidy</dl>
<p> <code>fixref</code></p>
<dl>
<dt>
<dd> determine and fix strand orientation</dl>
<p> <code>frameshifts</code></p>
<dl>
<dt>
<dd> annotate frameshift indels</dl>
<p> <code>GTisec</code></p>
<dl>
<dt>
<dd> count genotype intersections across all possible sample subsets in a vcf file</dl>
<p> <code>GTsubset</code></p>
<dl>
<dt>
<dd> output only sites where the requested samples all exclusively share a genotype</dl>
<p> <code>guess-ploidy</code></p>
<dl>
<dt>
<dd> determine sample sex by checking genotype likelihoods (GL,PL) or genotypes (GT) in the non-PAR region of chrX.</dl>
<p> <code>gvcfz</code></p>
<dl>
<dt>
<dd> compress gVCF file by resizing non-variant blocks according to specified criteria</dl>
<p> <code>impute-info</code></p>
<dl>
<dt>
<dd> add imputation information metrics to the INFO field based on selected FORMAT tags</dl>
<p> <code>indel-stats</code></p>
<dl>
<dt>
<dd> calculates per-sample or de novo indels stats. The usage and format is similar to <code>smpl-stats</code> and <code>trio-stats</code></dl>
<p> <code>isecGT</code></p>
<dl>
<dt>
<dd> compare two files and set non-identical genotypes to missing</dl>
<p> <code>mendelian</code></p>
<dl>
<dt>
<dd> count Mendelian consistent / inconsistent genotypes (deprecated, use +mendelian2 instead)</dl>
<p> <code>mendelian2</code></p>
<dl>
<dt>
<dd> count Mendelian consistent / inconsistent genotypes.</dl>
<p> <code>missing2ref</code></p>
<dl>
<dt>
<dd> sets missing genotypes (&quot;./.&quot;) to ref allele (&quot;0/0&quot; or &quot;0|0&quot;)</dl>
<p> <code>parental-origin</code></p>
<dl>
<dt>
<dd> determine parental origin of a CNV region</dl>
<p> <code>prune</code></p>
<dl>
<dt>
<dd> prune sites by missingness, allele frequency or linkage disequilibrium. Alternatively, annotate sites with r2, Lewontin&#8217;s D&#8217; (PMID:19433632), Ragsdale&#8217;s D (PMID:31697386).</dl>
<p> <code>remove-overlaps</code></p>
<dl>
<dt>
<dd> remove overlapping variants and duplicate sites</dl>
<p> <code>scatter</code></p>
<dl>
<dt>
<dd> intended as an inverse to bcftools concat, scatter VCF by chunks or regions, creating multiple VCFs.</dl>
<p> <code>setGT</code></p>
<dl>
<dt>
<dd> general tool to set genotypes according to rules requested by the user</dl>
<p> <code>smpl-stats</code></p>
<dl>
<dt>
<dd> calculates basic per-sample stats. The usage and format is similar to <code>indel-stats</code> and <code>trio-stats</code>.</dl>
<p> <code>split</code></p>
<dl>
<dt>
<dd> split VCF by sample, creating single- or multi-sample VCFs</dl>
<p> <code>split-vep</code></p>
<dl>
<dt>
<dd> extract fields from structured annotations such as INFO/CSQ created by bcftools/csq or VEP. These can be added as a new INFO field to the VCF or in a custom text format. See <i></i> &lt;<a rel="nofollow" href="http://samtools.github.io/bcftools/howtos/plugin.split-vep.html">http://samtools.github.io/bcftools/howtos/plugin.split-vep.html</a>&gt; for more.</dl>
<p> <code>tag2tag</code></p>
<dl>
<dt>
<dd> Convert between similar tags, such as GL,PL,GP or QR,QA,QS.</dl>
<p> <code>trio-dnm2</code></p>
<dl>
<dt>
<dd> screen variants for possible de-novo mutations in trios</dl>
<p> <code>trio-stats</code></p>
<dl>
<dt>
<dd> calculate transmission rate in trio children. The usage and format is similar to <code>indel-stats</code> and <code>smpl-stats</code>.</dl>
<p> <code>trio-switch-rate</code></p>
<dl>
<dt>
<dd> calculate phase switch rate in trio samples, children samples must have phased GTs</dl>
<p> <code>variant-distance</code></p>
<dl>
<dt>
<dd> annotate sites with the distance to the nearest variant</dl>
<p> <code>variantkey-hex</code></p>
<dl>
<dt>
<dd> generate unsorted VariantKey-RSid index files in hexadecimal format</dl>
<h3>Examples:</h3>
<dl>
<dt>
<dd>
<pre>
# List options common to all plugins
bcftools plugin
# List available plugins
bcftools plugin -l
# Run a plugin
bcftools plugin counts in.vcf
# Run a plugin using the abbreviated &quot;+&quot; notation
bcftools +counts in.vcf
# Run a plugin from an explicit location
bcftools +/path/to/counts.so in.vcf
# The input VCF can be streamed just like in other commands
cat in.vcf | bcftools +counts
# Print usage information of plugin &quot;dosage&quot;
bcftools +dosage -h
# Replace missing genotypes with 0/0
bcftools +missing2ref in.vcf
# Replace missing genotypes with 0|0
bcftools +missing2ref in.vcf -- -p
</pre>
</dl>
<h3>Plugins troubleshooting:</h3>
<p> Things to check if your plugin does not show up in the <code>bcftools plugin -l</code> output: </p>
<dl>
<dt>
<dd> &bull; Run with the <code>-v</code> option for verbose output: <code>bcftools plugin -lv</code></dl>
<dl>
<dt>
<dd> &bull; Does the environment variable BCFTOOLS_PLUGINS include the correct path?</dl>
<h3>Plugins API:</h3>
<dl>
<dt>
<dd>
// Short description used by &#8216;bcftools plugin -l&#8217;<br />
const char *about(void);<br />
// Longer description used by &#8216;bcftools +name -h&#8217;<br />
const char *usage(void);<br />
// Called once at startup, allows initialization of local variables.<br />
// Return 1 to suppress normal VCF/BCF header output, -1 on critical<br />
// errors, 0 otherwise.<br />
int init(int argc, char **argv, bcf_hdr_t *in_hdr, bcf_hdr_t *out_hdr);<br />
// Called for each VCF record, return NULL to suppress the output<br />
bcf1_t *process(bcf1_t *rec);<br />
// Called after all lines have been processed to clean up<br />
void destroy(void);
</dl>
<h3>bcftools polysomy [<i>OPTIONS</i>] <i>file.vcf.gz</i></h3>
<p> Detect number of chromosomal copies in VCFs annotates with the Illumina&#8217;s B-allele frequency (BAF) values. Note that this command is not compiled in by default, see the section <code>Optional Compilation with GSL</code> in the INSTALL file for help.</p>
<h3>General options:</h3>
<p> <code>-o, &#8211;output-dir</code> <i>path</i></p>
<dl>
<dt>
<dd> output directory</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;sample</code> <i>string</i></p>
<dl>
<dt>
<dd> sample name</dl>
<p> <code>-t, &#8211;targets</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> verbose debugging output which gives hints about the thresholds and decisions made by the program. Note that the exact output can change between versions.</dl>
<h3>Algorithm options:</h3>
<p> <code>-b, &#8211;peak-size</code> <i>float</i></p>
<dl>
<dt>
<dd> the minimum peak size considered as a good match can be from the interval [0,1] where larger is stricter</dl>
<p> <code>-c, &#8211;cn-penalty</code> <i>float</i></p>
<dl>
<dt>
<dd> a penalty for increasing copy number state. How this works: multiple peaks are always a better fit than a single peak, therefore the program prefers a single peak (normal copy number) unless the absolute deviation of the multiple peaks fit is significantly smaller. Here the meaning of &quot;significant&quot; is given by the <i>float</i> from the interval [0,1] where larger is stricter.</dl>
<p> <code>-f, &#8211;fit-th</code> <i>float</i></p>
<dl>
<dt>
<dd> threshold for goodness of fit (normalized absolute deviation), smaller is stricter</dl>
<p> <code>-i, &#8211;include-aa</code></p>
<dl>
<dt>
<dd> include also the AA peak in CN2 and CN3 evaluation. This usually requires increasing <code>-f</code>.</dl>
<p> <code>-m, &#8211;min-fraction</code> <i>float</i></p>
<dl>
<dt>
<dd> minimum distinguishable fraction of aberrant cells. The experience shows that trustworthy are estimates of 20% and more.</dl>
<p> <code>-p, &#8211;peak-symmetry</code> <i>float</i></p>
<dl>
<dt>
<dd> a heuristics to filter failed fits where the expected peak symmetry is violated. The <i>float</i> is from the interval [0,1] and larger is stricter</dl>
<h3>bcftools query [<i>OPTIONS</i>] <i>file.vcf.gz</i> [<i>file.vcf.gz</i> [&#8230;]]</h3>
<p> Extracts fields from VCF or BCF files and outputs them in user-defined format. </p>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>&#8211;force-samples</code></p>
<dl>
<dt>
<dd> continue even when some samples requested via <code>-s/-S</code> do not exist</dl>
<p> <code>-f, &#8211;format</code> <i>FORMAT</i></p>
<dl>
<dt>
<dd> learn by example, see below</dl>
<p> <code>-H, &#8211;print-header</code></p>
<dl>
<dt>
<dd> print header</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-l, &#8211;list-samples</code></p>
<dl>
<dt>
<dd> list sample names and exit</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-u, &#8211;allow-undef-tags</code></p>
<dl>
<dt>
<dd> do not throw an error if there are undefined tags in the format string, print &quot;.&quot; instead</dl>
<p> <code>-v, &#8211;vcf-list</code> <i>FILE</i></p>
<dl>
<dt>
<dd> process multiple VCFs listed in the file</dl>
<h3>Format:</h3>
<dl>
<dt>
<dd>
%CHROM          The CHROM column (similarly also other columns: POS, ID, REF, ALT, QUAL, FILTER)<br />
%END            End position of the REF allele<br />
%END0           End position of the REF allele in 0-based coordinates<br />
%FIRST_ALT      Alias for %ALT{0}<br />
%FORMAT         Prints all FORMAT fields or a subset of samples with -s or -S<br />
%GT             Genotype (e.g. 0/1)<br />
%INFO           Prints the whole INFO column<br />
%INFO/TAG       Any tag in the INFO column<br />
%IUPACGT        Genotype translated to IUPAC ambiguity codes (e.g. M instead of C/A)<br />
%LINE           Prints the whole line<br />
%MASK           Indicates presence of the site in other files (with multiple files)<br />
%N_PASS(expr)   Number of samples that pass the filtering expression (see *&lt;&lt;expressions,EXPRESSIONS&gt;&gt;*)<br />
%POS0           POS in 0-based coordinates<br />
%PBINOM(TAG)    Calculate phred-scaled binomial probability, the allele index is determined from GT<br />
%SAMPLE         Sample name<br />
%TAG{INT}       Curly brackets to print a subfield (e.g. INFO/TAG{1}, the indexes are 0-based)<br />
%TBCSQ          Translated FORMAT/BCSQ. See the csq command above for explanation and examples.<br />
%TGT            Translated genotype (e.g. C/A)<br />
%TYPE           Variant type (REF, SNP, MNP, INDEL, BND, OTHER)<br />
[]              Format fields must be enclosed in brackets to loop over all samples<br />

              new line<br />
	              tab character
</dl>
<dl>
<dt>
<dd>
<pre>
Everything else is printed verbatim.
</pre>
</dl>
<h3>Examples:</h3>
<dl>
<dt>
<dd>
<pre>
# Print chromosome, position, ref allele and the first alternate allele
bcftools query -f '%CHROM  %POS  %REF  %ALT{0}
' file.vcf.gz
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# Similar to above, but use tabs instead of spaces, add sample name and genotype
bcftools query -f '%CHROM	%POS	%REF	%ALT[	%SAMPLE=%GT]
' file.vcf.gz
</pre>
</dl>
<dl>
<dt>
<dd>
#Print FORMAT / GT fields followed by FORMAT / GT fields<br />
bcftools query &#8211; f &#8216;GQ:[ %GQ] 	 GT:[ %GT]
&#8217; file.vcf
</dl>
<dl>
<dt>
<dd>
<pre>
# Make a BED file: chr, pos (0-based), end pos (1-based), id
bcftools query -f'%CHROM	%POS0	%END	%ID
' file.bcf
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# Print only samples with alternate (non-reference) genotypes
bcftools query -f'[%CHROM:%POS %SAMPLE %GT
]' -i'GT=&quot;alt&quot;' file.bcf
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# Print all samples at sites with at least one alternate genotype
bcftools view -i'GT=&quot;alt&quot;' file.bcf -Ou | bcftools query -f'[%CHROM:%POS %SAMPLE %GT
]'
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# Print phred-scaled binomial probability from FORMAT/AD tag for all heterozygous genotypes
bcftools query -i'GT=&quot;het&quot;' -f'[%CHROM:%POS %SAMPLE %GT %PBINOM(AD)
]' file.vcf
</pre>
</dl>
<dl>
<dt>
<dd>
#Print the second value of AC field if bigger than 10. Note the(unfortunate) difference in<br />
#index subscript notation : formatting expressions(-f) uses &#8220;{}&#8221; while filtering expressions<br />
#(- i) use &#8220;[]&#8221;.This is for historic reasons and backward &#8211; compatibility.<br />
bcftools query &#8211; f &#8216;%AC{1}
&#8217; &#8211; i &#8216;AC[1]&gt;10&#8217; file.vcf.gz
</dl>
<h3>bcftools reheader [<i>OPTIONS</i>] <i>file.vcf.gz</i></h3>
<p> Modify header of VCF/BCF files, change sample names. </p>
<p> <code>-f, &#8211;fai</code> <i>FILE</i></p>
<dl>
<dt>
<dd> add to the header contig names and their lengths from the provided fasta index file (.fai). Lengths of existing contig lines will be updated and contig lines not present in the fai file will be removed</dl>
<p> <code>-h, &#8211;header</code> <i>FILE</i></p>
<dl>
<dt>
<dd> new VCF header</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> <i>FILE</i></p>
<dl>
<dt>
<dd> new sample names, one name per line, in the same order as they appear in the VCF file. Alternatively, only samples which need to be renamed can be listed as &quot;old_name new_name
&quot; pairs separated by whitespaces, each on a separate line. If a sample name contains spaces, the spaces can be escaped using the backslash character, for example &quot;Not\ a\ good\ sample\ name&quot;.</dl>
<p> <code>-T, &#8211;temp-prefix</code> <i>PATH</i></p>
<dl>
<dt>
<dd> template for temporary file names, used with <code>-f</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<h3>bcftools roh [<i>OPTIONS</i>] <i>file.vcf.gz</i></h3>
<p> A program for detecting runs of homo/autozygosity. Only bi-allelic sites are considered.</p>
<h3>The HMM model:</h3>
<dl>
<dt>
<dd>
Notation : D = Data, AZ = autozygosity, HW = Hardy &#8211; Weinberg(non &#8211; autozygosity),<br />
           f = non &#8211; ref allele frequency<br />
                         Emission probabilities : oAZ = P_i(D | AZ) = (1 &#8211; f) * P(D | RR) + f * P(D | AA)<br />
                                                                                                    oHW = P_i(D | HW) = (1 &#8211; f) ^ 2 * P(D | RR) + f ^ 2 * P(D | AA) + 2 * f * (1 &#8211; f) * P(D | RA) Transition probabilities : tAZ = P(AZ | HW)..from HW to AZ,<br />
           the &#8211; a parameter<br />
                     tHW = P(HW | AZ)..from AZ to HW,<br />
           the &#8211; H parameter<br />
                     ci = P_i(C)..probability of cross &#8211; over at site i,<br />
           from genetic map<br />
               AZi = P_i(AZ)..probability of site i being AZ / non &#8211; AZ,<br />
           scaled so that AZi + HWi = 1 HWi = P_i(HW)<br />
               P_{i + 1}(AZ) = oAZ * max[(1 &#8211; tAZ * ci) * AZ{i &#8211; 1}, tAZ *ci *(1 &#8211; AZ{i &#8211; 1})] P_{i + 1}(HW) = oHW * max[(1 &#8211; tHW * ci) * (1 &#8211; AZ{i &#8211; 1}), tHW *ci *AZ{i &#8211; 1}]
</dl>
<h3>General Options:</h3>
<p> <code>&#8211;AF-dflt</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> in case allele frequency is not known, use the <i>FLOAT</i>. By default, sites where allele frequency cannot be determined, or is 0, are skipped.</dl>
<p> <code>&#8211;AF-tag</code> <i>TAG</i></p>
<dl>
<dt>
<dd> use the specified INFO tag <i>TAG</i> as an allele frequency estimate instead of the default AC and AN tags. Sites which do not have <i>TAG</i> will be skipped.</dl>
<p> <code>&#8211;AF-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> Read allele frequencies from a tab-delimited file containing the columns: CHROM	POS	REF,ALT	AF. The file can be compressed with <code>bgzip</code> and indexed with tabix -s1 -b2 -e2. Sites which are not present in the <i>FILE</i> or have different reference or alternate allele will be skipped. Note that such a file can be easily created from a VCF using:</dl>
<dl>
<dt>
<dd>
<pre>
    bcftools query -f'%CHROM	%POS	%REF,%ALT	%INFO/TAG
' file.vcf | bgzip -c &gt; freqs.tab.gz
</pre>
</dl>
<p> <code>-b, &#8211;buffer-size</code> <i>INT</i>[,<i>INT</i>]</p>
<dl>
<dt>
<dd> when the entire many-sample file cannot fit into memory, a sliding buffer approach can be used. The first value is the number of sites to keep in memory. If negative, it is interpreted as the maximum memory to use, in MB. The second, optional, value sets the number of overlapping sites. The default overlap is set to roughly 1% of the buffer size.</dl>
<p> <code>-e, &#8211;estimate-AF</code> <i>FILE</i></p>
<dl>
<dt>
<dd> estimate the allele frequency by recalculating INFO/AC and INFO/AN on the fly, using the specified <i>TAG</i> which can be either FORMAT/GT (&quot;GT&quot;) or FORMAT/PL (&quot;PL&quot;). If <i>TAG</i> is not given, &quot;GT&quot; is assumed. Either all samples (&quot;-&quot;) or samples listed in <i>FILE</i> will be included. For example, use &quot;PL,-&quot; to estimate AF from FORMAT/PL of all samples. If neither <code>-e</code> nor the other <code>&#8211;AF-&#8230;</code> options are given, the allele frequency is estimated from AC and AN counts which are already present in the INFO field.</dl>
<p> <code>&#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-G, &#8211;GTs-only</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> use genotypes (FORMAT/GT fields) ignoring genotype likelihoods (FORMAT/PL), setting PL of unseen genotypes to <i>FLOAT</i>. Safe value to use is 30 to account for GT errors.</dl>
<p> <code>&#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-I, &#8211;skip-indels</code></p>
<dl>
<dt>
<dd> skip indels as their genotypes are usually enriched for errors</dl>
<p> <code>-m, &#8211;genetic-map</code> <i>FILE</i></p>
<dl>
<dt>
<dd> genetic map in the format required also by IMPUTE2. Only the first and third column are used (position and Genetic_Map(cM)). The <i>FILE</i> can be a single file or a file mask, where string &quot;{CHROM}&quot; is replaced with chromosome name.</dl>
<p> <code>-M, &#8211;rec-rate</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> constant recombination rate per bp. In combination with <code>&#8211;genetic-map</code>, the <code>&#8211;rec-rate</code> parameter is interpreted differently, as <i>FLOAT</i>-fold increase of transition probabilities, which allows the model to become more sensitive yet still account for recombination hotspots. Note that also the range of the values is therefore different in both cases: normally the parameter will be in the range (1e-3,1e-9) but with <code>&#8211;genetic-map</code> it will be in the range (10,1000).</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> Write output to the <i>FILE</i>, by default the output is printed on stdout</dl>
<p> <code>-O, &#8211;output-type</code> <i>s</i>|<i>r</i>[<i>z</i>]</p>
<dl>
<dt>
<dd> Generate per-site output (<i>s</i>) or per-region output (<i>r</i>). By default both types are printed and the output is uncompressed. Add <i>z</i> for a compressed output.</dl>
<dl>
<dt>
<dd>
<pre>
    # Output fields:
    RG = predicted homo/autozygous regions
        - Sample
        - Chromosome
        - Start
        - End
        - Length (bp)
        - Number of markers
        - Quality .. average phred score in the region from the forward-backward algorithm
    ST = per-site output showing:
        - Sample
        - Chromosome
        - Position
        - State .. predicted state from the Viterbi algorithm, 0 for normal (HW, Hardy-Weinberg) or 1 for autozygous (AZ)
        - Quality .. quality score from the forward-backward algorithm
</pre>
</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<h3>HMM Options:</h3>
<p> <code>-a, &#8211;hw-to-az</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> P(AZ|HW) transition probability from AZ (autozygous) to HW (Hardy-Weinberg) state</dl>
<p> <code>-H, &#8211;az-to-hw</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> P(HW|AZ) transition probability from HW to AZ state</dl>
<p> <code>-V, &#8211;viterbi-training</code> <i>FLOAT</i></p>
<dl>
<dt>
<dd> estimate HMM parameters using Baum-Welch algorithm, using the convergence threshold <i>FLOAT</i>, e.g. 1e-10 (experimental)</dl>
<h3>bcftools sort [<i>OPTIONS</i>] file.bcf</h3>
<p> <code>-m, &#8211;max-mem</code> <i>FLOAT</i>[<i>kMG</i>]</p>
<dl>
<dt>
<dd> Maximum memory to use. Approximate, affects the number of temporary files written to the disk. Note that if the command fails at this step because of too many open files, your system limit on the number of open files (&quot;ulimit&quot;) may need to be increased.</dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;temp-dir</code> <i>DIR</i></p>
<dl>
<dt>
<dd> Use this directory to store temporary files</dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>bcftools stats [<i>OPTIONS</i>] <i>A.vcf.gz</i> [<i>B.vcf.gz</i>]</h3>
<p> Parses VCF or BCF and produces text file stats which is suitable for machine processing and can be plotted using <code>plot-vcfstats</code>. When two files are given, the program generates separate stats for intersection and the complements. By default only sites are compared, <code>-s</code>/<code>-S</code> must given to include also sample columns. When one VCF file is specified on the command line, then stats by non-reference allele frequency, depth distribution, stats by quality and per-sample counts, singleton stats, etc. are printed. When two VCF files are given, then stats such as concordance (Genotype concordance by non-reference allele frequency, Genotype concordance by sample, Non-Reference Discordance) and correlation are also printed. Per-site discordance (PSD) is also printed in <code>&#8211;verbose</code> mode. </p>
<p> <code>&#8211;af-bins</code> <i>LIST</i>|<i>FILE</i></p>
<dl>
<dt>
<dd> comma separated list of allele frequency bins (e.g. 0.1,0.5,1) or a file listing the allele frequency bins one per line (e.g. 0.1
0.5
1)</dl>
<p> <code>&#8211;af-tag</code> <i>TAG</i></p>
<dl>
<dt>
<dd> allele frequency INFO tag to use for binning. By default the allele frequency is estimated from AC/AN, if available, or directly from the genotypes (GT) if not.</dl>
<p> <code>-1, &#8211;1st-allele-only</code></p>
<dl>
<dt>
<dd> consider only the 1st alternate allele at multiallelic sites</dl>
<p> <code>-c, &#8211;collapse</code> <i>snps</i>|<i>indels</i>|<i>both</i>|<i>all</i>|<i>some</i>|<i>none</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-d, &#8211;depth</code> <i>INT</i>,<i>INT</i>,<i>INT</i></p>
<dl>
<dt>
<dd> ranges of depth distribution: min, max, and size of the bin</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> produce verbose per-site and per-sample output</dl>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-E, &#8211;exons</code> <i>file.gz</i></p>
<dl>
<dt>
<dd> tab-delimited file with exons for indel frameshifts statistics. The columns of the file are CHR, FROM, TO, with 1-based, inclusive, positions. The file is BGZF-compressed and indexed with tabix</dl>
<dl>
<dt>
<dd>
<pre>
    tabix -s1 -b2 -e3 file.gz
</pre>
</dl>
<p> <code>-f, &#8211;apply-filters</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-F, &#8211;fasta-ref</code> <i>ref.fa</i></p>
<dl>
<dt>
<dd> faidx indexed reference sequence file to determine INDEL context</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include only sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-I, &#8211;split-by-ID</code></p>
<dl>
<dt>
<dd> collect stats separately for sites which have the ID column set (&quot;known sites&quot;) or which do not have the ID column set (&quot;novel sites&quot;).</dl>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-u, &#8211;user-tstv</code> <i>&lt;TAG[:min:max:n]&gt;</i></p>
<dl>
<dt>
<dd> collect Ts/Tv stats for any tag using the given binning [0:1:100]</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> produce verbose per-site and per-sample output</dl>
<h3>bcftools view [<i>OPTIONS</i>] <i>file.vcf.gz</i> [<i>REGION</i> [&#8230;]]</h3>
<p> View, subset and filter VCF or BCF files by position and filtering expression. Convert between VCF and BCF. Former <code>bcftools subset</code>.</p>
<h3>Output options</h3>
<p> <code>-G, &#8211;drop-genotypes</code></p>
<dl>
<dt>
<dd> drop individual genotype information (after subsetting if <code>-s</code> option is set)</dl>
<p> <code>-h, &#8211;header-only</code></p>
<dl>
<dt>
<dd> output the VCF header only (see also <code>bcftools head</code>)</dl>
<p> <code>-H, &#8211;no-header</code></p>
<dl>
<dt>
<dd> suppress the header in VCF output</dl>
<p> <code>&#8211;with-header</code></p>
<dl>
<dt>
<dd> output both VCF header and records (this is the default, but the option is useful for explicitness or to reset the effects of <code>-h</code> or <code>-H</code>)</dl>
<p> <code>-l, &#8211;compression-level</code> [<i>0-9</i>]</p>
<dl>
<dt>
<dd> compression level. 0 stands for uncompressed, 1 for best speed and 9 for best compression.</dl>
<p> <code>&#8211;no-version</code></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-O, &#8211;output-type</code> <i>b</i>|<i>u</i>|<i>z</i>|<i>v</i>[0-9]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-o, &#8211;output</code> <i>FILE</i>: output file name. If not present, the default is to print to standard output (stdout). </p>
<p> <code>-r, &#8211;regions</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-R, &#8211;regions-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;regions-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-t, &#8211;targets</code> <i>chr</i>|<i>chr:pos</i>|<i>chr:from-to</i>|<i>chr:from-</i>[,&#8230;]</p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-T, &#8211;targets-file</code> <i>file</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;targets-overlap</code> <i>0</i>|<i>1</i>|<i>2</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;threads</code> <i>INT</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>&#8211;write-index</code></p>
<dl>
<dt>
<dd> Automatically index the output file</dl>
<h3>Subset options:</h3>
<p> <code>-a, &#8211;trim-alt-alleles</code></p>
<dl>
<dt>
<dd> remove alleles not seen in the genotype fields from the ALT column. Note that if no alternate allele remains after trimming, the record itself is not removed but ALT is set to &quot;.&quot;. If the option <code>-s</code> or <code>-S</code> is given, removes alleles not seen in the subset. INFO and FORMAT tags declared as Type=A, G or R will be trimmed as well.</dl>
<p> <code>&#8211;force-samples</code></p>
<dl>
<dt>
<dd> only warn about unknown subset samples</dl>
<p> <code>-I, &#8211;no-update</code></p>
<dl>
<dt>
<dd> do not (re)calculate INFO fields for the subset (currently INFO/AC and INFO/AN)</dl>
<p> <code>-s, &#8211;samples</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code>. Note that it is possible to create multiple subsets simultaneously using the <code>split</code> plugin.</dl>
<p> <code>-S, &#8211;samples-file</code> <i>FILE</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code>. Note that it is possible to create multiple subsets simultaneously using the <code>split</code> plugin.</dl>
<h3>Filter options:</h3>
<p> Note that filter options below dealing with counting the number of alleles will, for speed, first check for the values of AC and AN in the INFO column to avoid parsing all the genotype (FORMAT/GT) fields in the VCF. This means that filters like <i>&#8211;uncalled</i>, &#8211;exclude-uncalled&#8217;, or <i>&#8211;min-af 0.1</i> will be calculated from INFO/AC and INFO/AN when available or FORMAT/GT otherwise. However, it will not attempt to use any other existing field, like INFO/AF for example. For that, use <i>&#8211;exclude AF&lt;0.1</i> instead. </p>
<p> Also note that one must be careful when sample subsetting and filtering is performed in a single command because the order of internal operations can influence the result. For example, the <code>-i/-e</code> filtering is performed before sample removal, but the <code>-P</code> filtering is performed after, and some are inherently ambiguous, for example allele counts can be taken from the INFO column when present but calculated on the fly when absent. Therefore it is strongly recommended to spell out the required order explicitly by separating such commands into two steps. (Make sure to use the <code>-O u</code> option when piping!) </p>
<p> <code>-c, &#8211;min-ac</code> <i>INT</i>[<i>:nref</i>|<i>:alt1</i>|<i>:minor</i>|<i>:major</i>|:&#8217;nonmajor&#8217;]</p>
<dl>
<dt>
<dd> minimum allele count (INFO/AC) of sites to be printed. Specifying the type of allele is optional and can be set to non-reference (<i>nref</i>, the default), 1st alternate (<i>alt1</i>), the least frequent (<i>minor</i>), the most frequent (<i>major</i>) or sum of all but the most frequent (<i>nonmajor</i>) alleles.</dl>
<p> <code>-C, &#8211;max-ac</code> <i>INT</i>[<i>:nref</i>|<i>:alt1</i>|<i>:minor</i>|:&#8217;major&#8217;|:&#8217;nonmajor&#8217;]</p>
<dl>
<dt>
<dd> maximum allele count (INFO/AC) of sites to be printed. Specifying the type of allele is optional and can be set to non-reference (<i>nref</i>, the default), 1st alternate (<i>alt1</i>), the least frequent (<i>minor</i>), the most frequent (<i>major</i>) or sum of all but the most frequent (<i>nonmajor</i>) alleles.</dl>
<p> <code>-e, &#8211;exclude</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> exclude sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-f, &#8211;apply-filters</code> <i>LIST</i></p>
<dl>
<dt>
<dd> see <code>Common Options</code></dl>
<p> <code>-g, &#8211;genotype</code> [^][<i>hom</i>|<i>het</i>|<i>miss</i>]</p>
<dl>
<dt>
<dd> include only sites with one or more homozygous (<i>hom</i>), heterozygous (<i>het</i>) or missing (<i>miss</i>) genotypes. When prefixed with <i>^</i>, the logic is reversed; thus <i>^het</i> excludes sites with heterozygous genotypes.</dl>
<p> <code>-i, &#8211;include</code> <i>EXPRESSION</i></p>
<dl>
<dt>
<dd> include sites for which <i>EXPRESSION</i> is true. For valid expressions see <code>EXPRESSIONS</code>.</dl>
<p> <code>-k, &#8211;known</code></p>
<dl>
<dt>
<dd> print known sites only (ID column is not &quot;.&quot;)</dl>
<p> <code>-m, &#8211;min-alleles</code> <i>INT</i></p>
<dl>
<dt>
<dd> print sites with at least <i>INT</i> alleles listed in REF and ALT columns</dl>
<p> <code>-M, &#8211;max-alleles</code> <i>INT</i></p>
<dl>
<dt>
<dd> print sites with at most <i>INT</i> alleles listed in REF and ALT columns. Use <code>-m2 -M2 -v snps</code> to only view biallelic SNPs.</dl>
<p> <code>-n, &#8211;novel</code></p>
<dl>
<dt>
<dd> print novel sites only (ID column is &quot;.&quot;)</dl>
<p> <code>-p, &#8211;phased</code></p>
<dl>
<dt>
<dd> print sites where all samples are phased. Haploid genotypes are considered phased. Missing genotypes considered unphased unless the phased bit is set.</dl>
<p> <code>-P, &#8211;exclude-phased</code></p>
<dl>
<dt>
<dd> exclude sites where all samples are phased</dl>
<p> <code>-q, &#8211;min-af</code> <i>FLOAT</i>[<i>:nref</i>|<i>:alt1</i>|<i>:minor</i>|<i>:major</i>|<i>:nonmajor</i>]</p>
<dl>
<dt>
<dd> minimum allele frequency (INFO/AC / INFO/AN) of sites to be printed. Specifying the type of allele is optional and can be set to non-reference (<i>nref</i>, the default), 1st alternate (<i>alt1</i>), the least frequent (<i>minor</i>), the most frequent (<i>major</i>) or sum of all but the most frequent (<i>nonmajor</i>) alleles.</dl>
<p> <code>-Q, &#8211;max-af</code> <i>FLOAT</i>[<i>:nref</i>|<i>:alt1</i>|<i>:minor</i>|<i>:major</i>|<i>:nonmajor</i>]</p>
<dl>
<dt>
<dd> maximum allele frequency (INFO/AC / INFO/AN) of sites to be printed. Specifying the type of allele is optional and can be set to non-reference (<i>nref</i>, the default), 1st alternate (<i>alt1</i>), the least frequent (<i>minor</i>), the most frequent (<i>major</i>) or sum of all but the most frequent (<i>nonmajor</i>) alleles.</dl>
<p> <code>-u, &#8211;uncalled</code></p>
<dl>
<dt>
<dd> print sites without a called genotype, i.e. print sites with all genotypes missing. Note that the missingness is determined from INFO/AN and AC tags when available to avoid parsing sample fields.</dl>
<p> <code>-U, &#8211;exclude-uncalled</code></p>
<dl>
<dt>
<dd> exclude sites without a called genotype, i.e. print sites with at least one non-missing genotype. Note that the missingness is determined from INFO/AN and AC tags when available to avoid parsing sample fields.</dl>
<p> <code>-v, &#8211;types</code> <i>snps</i>|<i>indels</i>|<i>mnps</i>|<i>other</i></p>
<dl>
<dt>
<dd> comma-separated list of variant types to select. Site is selected if any of the ALT alleles is of the type requested. Types are determined by comparing the REF and ALT alleles in the VCF record not INFO tags like INFO/INDEL or INFO/VT. Use <code>&#8211;include</code> to select based on INFO tags.</dl>
<p> <code>-V, &#8211;exclude-types</code> <i>snps</i>|<i>indels</i>|<i>mnps</i>|<i>ref</i>|<i>bnd</i>|<i>other</i></p>
<dl>
<dt>
<dd> comma-separated list of variant types to exclude. Site is excluded if any of the ALT alleles is of the type requested. Types are determined by comparing the REF and ALT alleles in the VCF record not INFO tags like INFO/INDEL or INFO/VT. Use <code>&#8211;exclude</code> to exclude based on INFO tags.</dl>
<p> <code>-x, &#8211;private</code></p>
<dl>
<dt>
<dd> print sites where only the subset samples carry an non-reference allele. Requires <code>&#8211;samples</code> or <code>&#8211;samples-file</code>.</dl>
<p> <code>-X, &#8211;exclude-private</code></p>
<dl>
<dt>
<dd> exclude sites where only the subset samples carry an non-reference allele</dl>
<h3>bcftools help [<i>COMMAND</i>] | bcftools &#8211;help [<i>COMMAND</i>]</h3>
<p> Display a brief usage message listing the bcftools commands available. If the name of a command is also given, e.g., bcftools help view, the detailed usage message for that particular command is displayed.</p>
<h3>bcftools [<i>&#8211;version</i>|<i>-v</i>]</h3>
<p> Display the version numbers and copyright information for bcftools and the important libraries used by bcftools.</p>
<h3>bcftools [<i>&#8211;version-only</i>]</h3>
<p> Display the full bcftools version number in a machine-readable format.</p>
<h2>FILTERING EXPRESSIONS</h2>
<p> These filtering expressions are accepted by most of the commands. </p>
<p> <code>Valid expressions may contain:</code> </p>
<dl>
<dt>
<dd> &bull; numerical constants, string constants, file names (this is currently supported only to filter by the ID column) </p>
<dl>
<dt>
<dd>
<pre>
1, 1.0, 1e-4
&quot;String&quot;
@file_name
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; arithmetic operators (addition, multiplication, subtraction, division, modulo) </p>
<dl>
<dt>
<dd>
<pre>
+, *, -, /, %
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; comparison operators </p>
<dl>
<dt>
<dd>
== (same as =), &gt;, &gt;=, &lt;=, &lt;, !=
</dl>
</dl>
<dl>
<dt>
<dd> &bull; regex operators &quot;\~&quot; and its negation &quot;!~&quot;. The expressions are case sensitive unless &quot;/i&quot; is added. </p>
<dl>
<dt>
<dd>
<pre>
INFO/HAYSTACK ~ &quot;needle&quot;
INFO/HAYSTACK ~ &quot;NEEDless/i&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; parentheses </p>
<dl>
<dt>
<dd>
<pre>
(, )
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; logical operators. See also the examples below and the <i>filtering tutorial</i> &lt;<a rel="nofollow" href="http://samtools.github.io/bcftools/howtos/filtering.html">http://samtools.github.io/bcftools/howtos/filtering.html</a>&gt; about the distinction between &quot;&amp;&amp;&quot; vs &quot;&amp;&quot; and &quot;||&quot; vs &quot;|&quot;. </p>
<dl>
<dt>
<dd>
<pre>
&amp;&amp;,  &amp;, ||,  |
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; INFO tags, FORMAT tags, column names </p>
<dl>
<dt>
<dd>
<pre>
INFO/DP or DP
FORMAT/DV, FMT/DV, or DV
FILTER, QUAL, ID, CHROM, POS, REF, ALT[0]
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; the FILTER column can be queried as follows: </p>
<dl>
<dt>
<dd>
FILTER=&#8221;PASS&#8221;<br />
FILTER=&#8221;.&#8221;<br />
FILTER=&#8221;A&#8221;          .. exact match, for example &#8220;A;B&#8221; does not pass<br />
FILTER=&#8221;A;B&#8221;        .. exact match, &#8220;A;B&#8221; and &#8220;B;A&#8221; pass, everything else fails<br />
FILTER!=&#8221;A&#8221;         .. exact match, for example &#8220;A;B&#8221; does pass<br />
FILTER~&#8221;A&#8221;          .. subset match, for example both &#8220;A&#8221; and &#8220;A;B&#8221; pass<br />
FILTER~&#8221;A;B&#8221;        .. subset match, pass only if both &#8220;A&#8221; and &#8220;B&#8221; are present<br />
FILTER!~&#8221;A&#8221;         .. complement match, for example both &#8220;A&#8221; and &#8220;A;B&#8221; fail<br />
FILTER!~&#8221;A;B&#8221;       .. complement match, fail if both &#8220;A&#8221; and &#8220;B&#8221; are present
</dl>
</dl>
<dl>
<dt>
<dd> &bull; 1 (or 0) to test the presence (or absence) of a flag </p>
<dl>
<dt>
<dd>
<pre>
FlagA=1 &amp;&amp; FlagB=0
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; &quot;.&quot; to test missing values </p>
<dl>
<dt>
<dd>
<pre>
DP=&quot;.&quot;, DP!=&quot;.&quot;, ALT=&quot;.&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; missing genotypes can be matched regardless of phase and ploidy (&quot;.|.&quot;, &quot;./.&quot;, &quot;.&quot;, &quot;0|.&quot;) using these expressions </p>
<dl>
<dt>
<dd>
<pre>
GT=&quot;mis&quot;, GT~&quot;\.&quot;, GT!~&quot;\.&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; missing genotypes can be matched including the phase and ploidy (&quot;.|.&quot;, &quot;./.&quot;, &quot;.&quot;) using these expressions </p>
<dl>
<dt>
<dd>
<pre>
GT=&quot;.|.&quot;, GT=&quot;./.&quot;, GT=&quot;.&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; sample genotype: reference (haploid or diploid), alternate (hom or het, haploid or diploid), missing genotype, homozygous, heterozygous, haploid, ref-ref hom, alt-alt hom, ref-alt het, alt-alt het, haploid ref, haploid alt (case-insensitive) </p>
<dl>
<dt>
<dd>
<pre>
GT=&quot;ref&quot;
GT=&quot;alt&quot;
GT=&quot;mis&quot;
GT=&quot;hom&quot;
GT=&quot;het&quot;
GT=&quot;hap&quot;
GT=&quot;RR&quot;
GT=&quot;AA&quot;
GT=&quot;RA&quot; or GT=&quot;AR&quot;
GT=&quot;Aa&quot; or GT=&quot;aA&quot;
GT=&quot;R&quot;
GT=&quot;A&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; TYPE for variant type in REF,ALT columns (indel,snp,mnp,ref,bnd,other,overlap). Use the regex operator &quot;\~&quot; to require at least one allele of the given type or the equal sign &quot;=&quot; to require that all alleles are of the given type. Compare </p>
<dl>
<dt>
<dd>
<pre>
TYPE=&quot;snp&quot;
TYPE~&quot;snp&quot;
TYPE!=&quot;snp&quot;
TYPE!~&quot;snp&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; array subscripts (0-based), &quot;*&quot; for any element, &quot;-&quot; to indicate a range. Note that for querying FORMAT vectors, the colon &quot;:&quot; can be used to select a sample and an element of the vector, as shown in the examples below. </p>
<dl>
<dt>
<dd>
INFO / AF[0] &gt; 0.3..first AF value bigger than 0.3 FORMAT / AD [0:0] &gt; 30..first AD value of the first sample bigger than 30 FORMAT / AD [0:1]..first sample, second AD value FORMAT / AD [1:0]..second sample, first AD value DP4[*] == 0..any DP4 value FORMAT / DP[0] &gt; 30..DP of the first sample bigger than 30 FORMAT / DP[1 &#8211; 3] &gt; 10..samples 2 &#8211; 4 FORMAT / DP[1 &#8211; ]&lt;7..all samples but the first FORMAT / DP[0, 2 &#8211; 4]&gt; 20..samples 1, 3 &#8211; 5 FORMAT / AD [0:1]..first sample, second AD field FORMAT / AD [0:*], AD [0:] or AD[0]..first sample, any AD field FORMAT / AD [*:1] or AD[:1]..any sample, second AD field(DP4[0] + DP4[1]) / (DP4[2] + DP4[3]) &gt; 0.3 CSQ[*] ~&#8221;missense_variant.*deleterious&#8221;
</dl>
</dl>
<dl>
<dt>
<dd> &bull; in addition to array subscripts shown above, it is possible to subscript arrays of Number=R tags by alleles found in FORMAT/GT (starting with version 1.17). For example </p>
<dl>
<dt>
<dd>
FORMAT/AD[GT] &gt; 10        .. require support of more than 10 reads for each allele<br />
FORMAT/AD[0:GT] &gt; 10      .. same as above, but in the first sample<br />
sSUM(FORMAT/AD[GT]) &gt; 20  .. require total sample depth bigger than 20
</dl>
</dl>
<dl>
<dt>
<dd> &bull; with many samples it can be more practical to provide a file with sample names, one sample name per line </p>
<dl>
<dt>
<dd>
<pre>
GT[@samples.txt]=&quot;het&quot; &amp; binom(AD)&lt;0.01
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; function on FORMAT tags (over samples) and INFO tags (over vector fields): maximum; minimum; arithmetic mean (AVG is synonymous with MEAN); median; standard deviation from mean; sum; string length; absolute value; number of elements: </p>
<dl>
<dt>
<dd>
<pre>
MAX, MIN, AVG, MEAN, MEDIAN, STDEV, SUM, STRLEN, ABS, COUNT
</pre>
</dl>
<p> Note that functions above evaluate to a single value across all samples and are intended to select sites, not samples, even when applied on FORMAT tags. However, when prefixed with SMPL_ (or &quot;s&quot; for brevity, e.g. SMPL_MAX or sMAX), they will evaluate to a vector of per-sample values when applied on FORMAT tags: </p>
<dl>
<dt>
<dd>
<pre>
SMPL_MAX, SMPL_MIN, SMPL_AVG, SMPL_MEAN, SMPL_MEDIAN, SMPL_STDEV, SMPL_SUM,
sMAX, sMIN, sAVG, sMEAN, sMEDIAN, sSTDEV, sSUM
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; two-tailed binomial test. Note that for N=0 the test evaluates to a missing value and when FORMAT/GT is used to determine the vector indices, it evaluates to 1 for homozygous genotypes. </p>
<dl>
<dt>
<dd>
binom(FMT / AD)..GT can be used to determine the correct index<br />
    binom(AD[0], AD[1])<br />
        ..or<br />
    the fields can be given explicitly<br />
        phred(binom())<br />
            ..the same as binom but phred<br />
        &#8211; scaled
</dl>
</dl>
<dl>
<dt>
<dd> &bull; variables calculated on the fly if not present: number of alternate alleles; number of samples; count of alternate alleles; minor allele count (similar to AC but is always smaller than 0.5); frequency of alternate alleles (AF=AC/AN); frequency of minor alleles (MAF=MAC/AN); number of alleles in called genotypes; number of samples with missing genotype; fraction of samples with missing genotype; indel length (deletions negative, insertions positive) </p>
<dl>
<dt>
<dd>
<pre>
N_ALT, N_SAMPLES, AC, MAC, AF, MAF, AN, N_MISSING, F_MISSING, ILEN
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; the number (N_PASS) or fraction (F_PASS) of samples which pass the expression </p>
<dl>
<dt>
<dd>
<pre>
N_PASS(GQ&gt;90 &amp; GT!=&quot;mis&quot;) &gt; 90
F_PASS(GQ&gt;90 &amp; GT!=&quot;mis&quot;) &gt; 0.9
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; custom perl filtering. Note that this command is not compiled in by default, see the section <code>Optional Compilation with Perl</code> in the INSTALL file for help and misc/demo-flt.pl for a working example. The demo defined the perl subroutine &quot;severity&quot; which can be invoked from the command line as follows: </p>
<dl>
<dt>
<dd>
<pre>
perl:path/to/script.pl; perl.severity(INFO/CSQ) &gt; 3
</pre>
</dl>
</dl>
<p> <code>Notes:</code> </p>
<dl>
<dt>
<dd> &bull; String comparisons and regular expressions are case-insensitive</dl>
<dl>
<dt>
<dd> &bull; Comma in strings is interpreted as a separator and when multiple values are compared, the OR logic is used. Consequently, the following two expressions are equivalent but not the third: </p>
<dl>
<dt>
<dd>
<pre>
-i 'TAG=&quot;hello,world&quot;'
-i 'TAG=&quot;hello&quot; || TAG=&quot;world&quot;'
-i 'TAG=&quot;hello&quot; &amp;&amp; TAG=&quot;world&quot;'
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; Variables and function names are case-insensitive, but not tag names. For example, &quot;qual&quot; can be used instead of &quot;QUAL&quot;, &quot;strlen()&quot; instead of &quot;STRLEN()&quot; , but not &quot;dp&quot; instead of &quot;DP&quot;.</dl>
<dl>
<dt>
<dd> &bull; When querying multiple values, all elements are tested and the OR logic is used on the result. For example, when querying &quot;TAG=1,2,3,4&quot;, it will be evaluated as follows: </p>
<dl>
<dt>
<dd>
&#8211; i &#8216;TAG[*]=1&#8217;..true, the record will be printed &#8211; i &#8216;TAG[*]!=1&#8217;..true &#8211; e &#8216;TAG[*]=1&#8217;..false, the record will be discarded &#8211; e &#8216;TAG[*]!=1&#8217;..false &#8211; i &#8216;TAG[0]=1&#8217;..true &#8211; i &#8216;TAG[0]!=1&#8217;..false &#8211; e &#8216;TAG[0]=1&#8217;..false &#8211; e &#8216;TAG[0]!=1&#8217;..true
</dl>
</dl>
<dl>
<dt>
<dd> &bull; When arithmetic operators are used on vectors A and B, the following logic is used to compute the resulting vector C: </p>
<dl>
<dt>
<dd> &bull; C_i = A_i + B_i when length(A)==B(A) and sets length&#169;=length(A)</dl>
<dl>
<dt>
<dd> &bull; C_i = A_i + B_0 when length(B)=1 and sets length&#169;=length(A)</dl>
<dl>
<dt>
<dd> &bull; C_i = A_0 + B_i when length(A)=1 and sets length&#169;=length(B)</dl>
<dl>
<dt>
<dd> &bull; throw an error when length(A)!=length(B) AND length(A)!=1 AND length(B)!=1</dl>
</dl>
<p> <code>Examples:</code> </p>
<dl>
<dt>
<dd>
<pre>
MIN(DV)&gt;5       .. selects the whole site, evaluates min across all values and samples
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
SMPL_MIN(DV)&gt;5  .. selects matching samples, evaluates within samples
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
MIN(DV/DP)&gt;0.3
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
MIN(DP)&gt;10 &amp; MIN(DV)&gt;3
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
FMT/DP&gt;10  &amp; FMT/GQ&gt;10 .. both conditions must be satisfied within one sample
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
FMT/DP&gt;10 &amp;&amp; FMT/GQ&gt;10 .. the conditions can be satisfied in different samples
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
QUAL&gt;10 |  FMT/GQ&gt;10   .. true for sites with QUAL&gt;10 or a sample with GQ&gt;10, but selects only samples with GQ&gt;10
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
QUAL&gt;10 || FMT/GQ&gt;10   .. true for sites with QUAL&gt;10 or a sample with GQ&gt;10, plus selects all samples at such sites
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
TYPE = "snp" &amp;&amp; QUAL &gt;= 10 &amp;&amp; (DP4[2] + DP4[3] &gt; 2)
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
COUNT(GT=&quot;hom&quot;)=0      .. no homozygous genotypes at the site
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
AVG(GQ)&gt;50             .. average (arithmetic mean) of genotype qualities bigger than 50
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
ID=@file       .. selects lines with ID present in the file
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
ID!=@~/file    .. skip lines with ID present in the ~/file
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
MAF[0]&lt;0.05    .. select rare variants at 5% cutoff
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
POS&gt;=100   .. restrict your range query, e.g. 20:100-200 to strictly sites with POS in that range.
</pre>
</dl>
<p> <code>Shell expansion:</code> </p>
<p> Note that expressions must often be quoted because some characters have special meaning in the shell. An example of expression enclosed in single quotes which cause that the whole expression is passed to the program as intended: </p>
<dl>
<dt>
<dd>
<pre>
bcftools view -i '%ID!=&quot;.&quot; &amp; MAF[0]&lt;0.01'
</pre>
</dl>
<p> Please refer to the documentation of your shell for details.</p>
<h2>SCRIPTS</h2>
<h3>gff2gff</h3>
<p> Attempts to fix a GFF file to be correctly parsed by <code>csq</code>. </p>
<dl>
<dt>
<dd>
<pre>
zcat in.gff.gz | gff2gff | gzip -c &gt; out.gff.gz
</pre>
</dl>
<h3>plot-vcfstats [<i>OPTIONS</i>] <i>file.vchk</i> [&#8230;]</h3>
<p> Script for processing output of <code>bcftools stats</code>. It can merge results from multiple outputs (useful when running the stats for each chromosome separately), plots graphs and creates a PDF presentation. </p>
<p> <code>-m, &#8211;merge</code></p>
<dl>
<dt>
<dd> Merge vcfstats files to STDOUT, skip plotting.</dl>
<p> <code>-p, &#8211;prefix</code> <i>DIR</i></p>
<dl>
<dt>
<dd> The output directory. This directory will be created if it does not exist.</dl>
<p> <code>-P, &#8211;no-PDF</code></p>
<dl>
<dt>
<dd> Skip the PDF creation step.</dl>
<p> <code>-r, &#8211;rasterize</code></p>
<dl>
<dt>
<dd> Rasterize PDF images for faster rendering. This is the default and the opposite of <code>-v, &#8211;vectors</code>.</dl>
<p> <code>-s, &#8211;sample-names</code></p>
<dl>
<dt>
<dd> Use sample names for xticks rather than numeric IDs.</dl>
<p> <code>-t, &#8211;title</code> <i>STRING</i></p>
<dl>
<dt>
<dd> Identify files by these titles in plots. The option can be given multiple times, for each ID in the <code>bcftools stats</code> output. If not present, the script will use abbreviated source file names for the titles.</dl>
<p> <code>-v, &#8211;vectors</code></p>
<dl>
<dt>
<dd> Generate vector graphics for PDF images, the opposite of <code>-r, &#8211;rasterize</code>.</dl>
<p> <code>-T, &#8211;main-title</code> <i>STRING</i></p>
<dl>
<dt>
<dd> Main title for the PDF.</dl>
<p> <code>Example:</code> </p>
<dl>
<dt>
<dd>
<pre>
# Generate the stats
bcftools stats -s - &gt; file.vchk
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# Plot the stats
plot-vcfstats -p outdir file.vchk
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
# The final looks can be customized by editing the generated
# 'outdir/plot.py' script and re-running manually
cd outdir &amp;&amp; python plot.py &amp;&amp; pdflatex summary.tex
</pre>
</dl>
<h2>PERFORMANCE</h2>
<p> HTSlib was designed with BCF format in mind. When parsing VCF files, all records are internally converted into BCF representation. Simple operations, like removing a single column from a VCF file, can be therefore done much faster with standard UNIX commands, such as <code>awk</code> or <code>cut</code>. Therefore it is recommended to use BCF as input/output format whenever possible to avoid large overhead of the VCF &rarr; BCF &rarr; VCF conversion.</p>
<h2>BUGS</h2>
<p> Please report any bugs you encounter on the github website: <i></i> &lt;<a rel="nofollow" href="http://github.com/samtools/bcftools">http://github.com/samtools/bcftools</a>&gt;</p>
<h2>AUTHORS</h2>
<p> Heng Li from the Sanger Institute wrote the original C version of htslib, samtools and bcftools. Bob Handsaker from the Broad Institute implemented the BGZF library. Petr Danecek is maintaining and further developing bcftools, together with the rest of the <i>samtools team</i> &lt;<a rel="nofollow" href="https://www.sanger.ac.uk/tool/samtools-bcftools-htslib">https://www.sanger.ac.uk/tool/samtools-bcftools-htslib</a>&gt;. Many other people contributed to the program and to the file format specifications, both directly and indirectly by providing patches, testing and reporting bugs. We thank them all.</p>
<h2>RESOURCES</h2>
<p> BCFtools GitHub website: <i></i> &lt;<a rel="nofollow" href="http://github.com/samtools/bcftools">http://github.com/samtools/bcftools</a>&gt; </p>
<p> Samtools GitHub website: <i></i> &lt;<a rel="nofollow" href="http://github.com/samtools/samtools">http://github.com/samtools/samtools</a>&gt; </p>
<p> HTSlib GitHub website: <i></i> &lt;<a rel="nofollow" href="http://github.com/samtools/htslib">http://github.com/samtools/htslib</a>&gt; </p>
<p> File format specifications: <i></i> &lt;<a rel="nofollow" href="http://samtools.github.io/hts-specs">http://samtools.github.io/hts-specs</a>&gt; </p>
<p> BCFtools documentation: <i></i> &lt;<a rel="nofollow" href="http://samtools.github.io/bcftools">http://samtools.github.io/bcftools</a>&gt; </p>
<p> BCFtools wiki page: <i></i> &lt;<a rel="nofollow" href="https://github.com/samtools/bcftools/wiki">https://github.com/samtools/bcftools/wiki</a>&gt;</p>
<h2>COPYING</h2>
<p> The MIT/Expat License or GPL License, see the LICENSE document for details. Copyright (c) Genome Research Ltd. </p>
<h2>Index</h2>
<dt><a href="#lbCX">FILTERING EXPRESSIONS</a></p>
<dd>
<dt><a href="#lbCY">SCRIPTS</a></p>
<dd>
<dt><a href="#lbDB">PERFORMANCE</a></p>
<dd>
<dt><a href="#lbDC">BUGS</a></p>
<dd>
<dt><a href="#lbDD">AUTHORS</a></p>
<dd>
<dt><a href="#lbDE">RESOURCES</a></p>
<dd>
<dt><a href="#lbDF">COPYING</a></p>
<dd></dl>
