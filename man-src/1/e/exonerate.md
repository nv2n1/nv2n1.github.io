---
title: "exonerate(1)"
name: "exonerate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exonerate/"
description: "exonerate – a generic tool for sequence comparison"
---

<h2 class="name">NAME</h2>
<p> exonerate &#8211; a generic tool for sequence comparison</p>
<h2>SYNOPSIS</h2>
<p> <code>exonerate [ options ] &lt;query path&gt; &lt;target path&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>exonerate</code> is a general tool for sequence comparison. </p>
<p> It uses the <code>C4</code> dynamic programming library. It is designed to be both general and fast. It can produce either gapped or ungapped alignments, according to a variety of different alignment models. The C4 library allows sequence alignment using a reduced space full dynamic programming implementation, but also allows automated generation of heuristics from the alignment models, using bounded sparse dynamic programming, so that these alignments may also be rapidly generated. Alignments generated using these heuristics will represent a valid path through the alignment model, yet (unlike the exhaustive alignments), the results are not guaranteed to be optimal. </p>
<h2>CONVENTIONS</h2>
<p> A number of conventions (and idiosyncracies) are used within exonerate. An understanding of them facilitates interpretation of the output.</p>
<dl>
<dt><code>Coordinates</code></p>
<dd> An in-between coordinate system is used, where the positions are counted between the symbols, rather than on the symbols. This numbering scheme starts from zero. This numbering is shown below for the sequence &quot;ACGT&quot;: </p>
<pre>
 A C G T
0 1 2 3 4
</pre>
<p> Hence the subsequence &quot;CG&quot; would have start=1, end=3, and length=2. This coordinate system is used internally in exonerate, and for all the output formats produced with the exception of the &quot;human readable&quot; alignment display and the GFF output where convention and standards dictate otherwise.</p>
<dt><code>Reverse Complements</code></p>
<dd> When an alignment is reported on the reverse complement of a sequence, the coordinates are simply given on the reverse complement copy of the sequence. Hence positions on the sequences are never negative. Generally, the forward strand is indicated by &#8216;+&#8217;, the reverse strand by &#8216;-&#8216;, and an unknown or not-applicable strand (as in the case of a protein sequence) is indicated by &#8216;.&#8217;</p>
<dt><code>Alignment Scores</code></p>
<dd> Currently, only the raw alignment scores are displayed. This score just is the sum of transistion scores used in the dynamic programming. For example, in the case of a Smith-Waterman alignment, this will be the sum of the substitution matrix scores and the gap penalties. </p>
</dl>
<h2>GENERAL OPTIONS</h2>
<p> Most arguments have short and long forms. The long forms are more likely to be stable over time, and hence should be used in scripts which call exonerate.</p>
<dl>
<dt><code>-h | &#8211;shorthelp &lt;boolean&gt;</code></p>
<dd> Show help. This will display a concise summary of the available options, defaults and values currently set.</p>
<dt><code>&#8211;help &lt;boolean&gt;</code></p>
<dd> This shows all the help options including the defaults, the value currently set, and the environment variable which may be used to set each parameter. There will be an indication of which options are mandatory. Mandatory options have no default, and must have a value supplied for exonerate to run. If mandatory options are used in order, their flags may be skipped from the command line (see examples below). Unlike this man page, the information from this option will always be up to date with the latest version of the program.</p>
<dt><code>-v | &#8211;version &lt;boolean&gt;</code></p>
<dd> Display the version number. Also displays other information such as the build date and glib version used. </p>
</dl>
<h2>SEQUENCE INPUT OPTIONS</h2>
<p> Pairwise comparisons will be performed between all query sequences and all target sequences. Generally, for the best performance, shorter sequences (eg. ESTs, shotgun reads, proteins) should be used as the query sequences, and longer sequences (eg. genomic sequences) should be used as the target sequences.</p>
<dl>
<dt><code>-q | &#8211;query &lt;paths&gt;</code></p>
<dd> Specify the query sequences required. These must be in a FASTA format file. Single or muiltiple query sequences may be supplied. Additionally multiple copies of the fasta file may be supplied following a &#8211;query flag, or by using with multiple &#8211;query flags.</p>
<dt><code>-t | &#8211;target &lt;paths&gt;</code></p>
<dd> Specify the target sequences required. Also, must be in a FASTA format file. As with the query sequences, single or multiple target sequences and files may be supplied. The target filename may by replace by a server name and port number in the form of <code>hostname:port</code> when using <code>exonerate-server.</code> See the man page for <code>exonerate-server</code> for more information on running exonerate in client:server mode. <code>NEW(v2.4.0):</code> multiple servers may now be used. These will be queried in parallel if you have set the <code>&#8211;cores</code> option. <code>NEW(v2.4.0):</code> If an input file is not a FASTA format file, it is assumed to contain a list of other fasta files, directories or servers (one per line).</p>
<dt><code>-Q | &#8211;querytype &lt;dna | protein&gt;</code></p>
<dd> Specify the query type to use. If this is not supplied, the query type is assumed to be DNA when the first sequence in the file contains more than 85% [ACGTN] bases. Otherwise, it is assumed to be peptide. This option forces the query type as some nucleotide and peptide sequences can fall either side of this threshold.</p>
<dt><code>-T | &#8211;targettype &lt;dna | protein&gt;</code></p>
<dd> Specify the target type to use. The same as <code>&#8211;querytype</code> (above), except that it applies to the target. Specifying the sequence type will avoid the overhead of having to read the first sequence in the database twice (which may be significant with chromosome-sized sequences)</p>
<dt><code>&#8211;querychunkid &lt;id&gt;</code></p>
<dd>
<dt><code>&#8211;querychunktotal &lt;total&gt;</code></p>
<dd>
<dt><code>&#8211;targetchunkid &lt;id&gt;</code></p>
<dd>
<dt><code>&#8211;targetchunktotal &lt;total&gt;</code></p>
<dd> These options to facilitate running exonerate on compute farms, and avoid having to split up sequence databases into small chunks to run on different nodes. If, for example, you wished to split the target database into three parts, you would run three exonerate jobs on different nodes including the options:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;targetchunkid 1 &#8211;targetchunktotal 3</p>
<dd>
<dt>&#8211;targetchunkid 2 &#8211;targetchunktotal 3</p>
<dd>
<dt>&#8211;targetchunkid 3 &#8211;targetchunktotal 3</p>
<dd></dl>
<p> NB. The granularity offered by this option only goes down to a single sequence, so when there are more chunks than sequences in the database, some processes will do nothing.</dl>
<dl>
<dt><code>-V | &#8211;verbose &lt;int&gt;</code></p>
<dd> Be verbose &#8211; show information about what is going on during the analysis. The default is 1 (little information), the higher the number given, the more information is printed. To silence all the default output from exonerate, use &#8211;verbose 0 &#8211;showalignment no &#8211;showvulgar no </p>
</dl>
<h2>ANALYSIS OPTIONS</h2>
<dl>
<dt><code>-E | &#8211;exhaustive &lt;boolean&gt;</code></p>
<dd> Specify whether or not exhaustive alignment should be used. By default, this is FALSE, and alignment heuristics will be used. If it is set to TRUE, an exhaustive alignment will be calculated. This requires quadratic time, and will be much, much slower, but will provide the optimal result for the given model.</p>
<dt><code>-B | &#8211;bigseq &lt;int&gt;</code></p>
<dd> Perform alignment of large (multi-megabase) sequences. This is very memory efficient and fast when both sequences are chromosome-sized, but currently does not currently permit the use of a word neighbourhood (ie. exactly matching seeds only).</p>
<dt><code>&#8211;revcomp &lt;boolean&gt;</code></p>
<dd> Include comparison of the reverse complement of the query and target where possible. By default, this option is enabled, but when you know the gene is definitely on the forward strand of the query and target, this option can halve the time taken to compute alignments.</p>
<dt><code>&#8211;forcescan &lt;none | query | target&gt;</code></p>
<dd> Force the FSM to scan the query sequence rather than the target. This option is useful, for example, if you have a single piece of genomic sequence and you with to compare it to the whole of dbEST. By scanning the database, rather than the query, the analysis will be completed much more quickly, as the overheads of multiple query FSM construction, multiple target reading and splice site predictions will be removed. By default, exonerate will guess the optimal strategy based on database sequence sizes.</p>
<dt><code>&#8211;saturatethreshold &lt;number&gt;</code></p>
<dd> When set to zero, this option does nothing. Otherwise, once more than this number of words (in addition to the expected number of words by chance) have matched a position on the query, the position on the query will be &#8216;numbed&#8217; (ignore further matches) for the current pairwise comparison.</p>
<dt><code>&#8211;customserver &lt;command&gt;</code></p>
<dd> When using exonerate in client:server mode with a non-standard server, this command allows you to send a custom command to the server. This command is sent by the client (exonerate) before any other commands, and is provided as a way of passing parameters or other commands specific to the custom server. See the <code>exonerate-server</code> man page for more information on running exonerate in client:server mode.</p>
<dt><code>&#8211;cores &lt;number&gt;</code></p>
<dd> The number of cores/CPUs/threads that should be used. On a multi-core or multi-CPU machine, increasing this ammount allows alignment computations to run in parallel on separate CPUs/cores. NB. Generally, it is better to parallelise the analysis by splitting it up into separate jobs, but this option may prove useful for problems such as interactive single-gene queries. </p>
</dl>
<h2>FASTA DATABASE OPTIONS</h2>
<dl>
<dt><code>&#8211;fastasuffix &lt;extension&gt;</code></p>
<dd> If any of the inputs given with <code>&#8211;query</code> or <code>&#8211;target</code> are directories, then exonerate will recursively descent these directories, reading all files ending with this suffix as fasta format input. </p>
</dl>
<h2>GAPPED ALIGNMENT OPTIONS</h2>
<dl>
<dt><code>-m | &#8211;model &lt;alignment model&gt;</code></p>
<dd> Specify the alignment model to use. The models currently supported are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>ungapped</code></p>
<dd> The simplest type of model, used by default. An appropriate model with be selected automatically for the type of input sequences provided.</p>
<dt><code>ungapped:trans</code></p>
<dd> This ungapped model includes translation of all frames of both the query and target sequences. This is similar to an ungapped tblastx type search.</p>
<dt><code>affine:global</code></p>
<dd> This performs gapped global alignment, similar to the Needleman-Wunsch algorithm, except with affine gaps. Global alignment requires that both the sequences in their entirety are included in the alignment.</p>
<dt><code>affine:bestfit</code></p>
<dd> This performs a best fit or best location alignment of the query onto the target sequence. The entire query sequence will be included in the alignment, but only the best location for its alignment on the target sequence.</p>
<dt><code>affine:local</code></p>
<dd> This is local alignment with affine gaps, similar to the Smith-Waterman-Gotoh algorithm. A general-purpose alignment algorithm. As this is local alignment, any subsequence of the query and target sequence may appear in the alignment.</p>
<dt><code>affine:overlap</code></p>
<dd> This type of alignment finds the best overlap between the query and target. The overlap alignment must include the start of the query or target and the end of the query or the target sequence, to align sequences which overlap at the ends, or in the mid-section of a longer sequence.. This is the type of alignment frequently used in assembly algorithms.</p>
<dt><code>est2genome</code></p>
<dd> This model is similar to the affine:local model, but it also includes intron modelling on the target sequence to allow alignment of spliced to unspliced coding sequences for both forward and reversed genes. This is similar to the alignment models used in programs such as EST_GENOME and sim4.</p>
<dt><code>ner</code></p>
<dd> NERs are non-equivalenced regions &#8211; large regions in both the query and target which are not aligned. This model can be used for protein alignments where strongly conserved helix regions will be aligned, but weakly conserved loop regions are not. Similarly, this model could be used to look for co-linearly conserved regions in comparison of genomic sequences.</p>
<dt><code>protein2dna</code></p>
<dd> This model compares a protein sequence to a DNA sequence, incorporating all the appropriate gaps and frameshifts.</p>
<dt><code>protein2dna:bestfit</code></p>
<dd> This is a bestfit version of the protein2dna model, with which the entire protein is included in the alignment. It is currently only available when using exhaustive alignment.</p>
<dt><code>protein2genome</code></p>
<dd> This model allows alignment of a protein sequence to genomic DNA. This is similar to the protein2dna model, with the addition of modelling of introns and intron phases. This model is simliar to those used by genewise.</p>
<dt><code>protein2genome:bestfit</code></p>
<dd> This is a bestfit version of the protein2genome model, with which the entire protein is included in the alignment. It is currently only available when using exhaustive alignment.</p>
<dt><code>coding2coding</code></p>
<dd> This model is similar to the ungapped:trans model, except that gaps and frameshifts are allowed. It is similar to a gapped tblastx search.</p>
<dt><code>coding2genome</code></p>
<dd> This is similar to the est2genome model, except that the query sequence is translated during comparison, allowing a more sensitive comparison.</p>
<dt><code>cdna2genome</code></p>
<dd> This combines properties of the est2genome and coding2genome models, to allow modeling of an whole cDNA where a central coding region can be flanked by non-coding UTRs. When the CDS start and end is known it may be specified using the &#8211;annotation option (see below) to permit only the correct coding region to appear in the alignemnt.</p>
<dt><code>genome2genome</code></p>
<dd> This model is similar to the coding2coding model, except introns are modelled on both sequences. (not working well yet) </p>
</dl>
</dl>
<dl>
<dt>
<dd> The short names u, u:t, a:g, a:b, a:l, a:o, e2g, ner, p2d, p2d:b p2g, p2g:b, c2c, c2g cd2g and g2g can also be used for specifying models.</p>
<dt><code>-s | &#8211;score &lt;threshold&gt;</code></p>
<dd> This is the overall score threshold. Alignments will not be reported below this threshold. For heuristic alignments, the higher this threshold, the less time the analysis will take.</p>
<dt><code>&#8211;percent &lt;percentage&gt;</code></p>
<dd> Report only alignments scoring at least this percentage of the maximal score for each query. eg. use <code>&#8211;percent 90</code> to report alignments with 90% of the maximal score optainable for that query. This option is useful not only because it reduces the spurious matches in the output, but because it generates query-specific thresholds (unlike <code>&#8211;score</code> ) for a set of queries of differing lengths, and will also speed up the search considerably. <code>NB.</code> with this option, it is possible to have a cDNA match its corresponding gene exactly, yet still score less than 100%, due to the addition of the intron penalty scores, hence this option must be used with caution.</p>
<dt><code>&#8211;showalignment &lt;boolean&gt;</code></p>
<dd> Show the alignments in an human readable form.</p>
<dt><code>&#8211;showsugar &lt;boolean&gt;</code></p>
<dd> Display &quot;sugar&quot; output for ungapped alignments. Sugar is Simple UnGapped Alignment Report, which displays ungapped alignments one-per-line. The sugar line starts with the string &quot;sugar:&quot; for easy extraction from the output, and is followed by the the following 9 fields in the order below:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>query_id</code></p>
<dd> Query identifier</p>
<dt><code>query_start</code></p>
<dd> Query position at alignment start</p>
<dt><code>query_end</code></p>
<dd> Query position alignment end</p>
<dt><code>query_strand</code></p>
<dd> Strand of query matched</p>
<dt><code>target_id</code></p>
<dd> |</p>
<dt><code>target_start</code></p>
<dd> | the same 4 fields</p>
<dt><code>target_end</code></p>
<dd> | for the target sequence</p>
<dt><code>target_strand</code></p>
<dd> |</p>
<dt><code>score</code></p>
<dd> The raw alignment score</dl>
</dl>
<dl>
<dt><code>&#8211;showcigar &lt;boolean&gt;</code></p>
<dd> Show the alignments in &quot;cigar&quot; format. Cigar is a Compact Idiosyncratic Gapped Alignment Report, which displays gapped alignments one-per-line. The format starts with the same 9 fields as sugar output (see above), and is followed by a series of &lt;operation, length&gt; pairs where operation is one of match, insert or delete, and the length describes the number of times this operation is repeated.</p>
<dt><code>&#8211;showvulgar &lt;boolean&gt;</code></p>
<dd> Shows the alignments in &quot;vulgar&quot; format. Vulgar is Verbose Useful Labelled Gapped Alignment Report, This format also starts with the same 9 fields as sugar output (see above), and is followed by a series of &lt;label, query_length, target_length&gt; triplets. The label may be one of the following:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>M</code></p>
<dd> Match</p>
<dt><code>C</code></p>
<dd> Codon</p>
<dt><code>G</code></p>
<dd> Gap</p>
<dt><code>N</code></p>
<dd> Non-equivalenced region</p>
<dt><code>5</code></p>
<dd> 5&#8242; splice site</p>
<dt><code>3</code></p>
<dd> 3&#8242; splice site</p>
<dt><code>I</code></p>
<dd> Intron</p>
<dt><code>S</code></p>
<dd> Split codon</p>
<dt><code>F</code></p>
<dd> Frameshift</dl>
</dl>
<dl>
<dt><code>&#8211;showquerygff &lt;boolean&gt;</code></p>
<dd> Report GFF output for features on the query sequence. See <a rel="nofollow" href="http://www.sanger.ac.uk/Software/formats/GFF">http://www.sanger.ac.uk/Software/formats/GFF</a> for more information.</p>
<dt><code>&#8211;showtargetgff &lt;boolean&gt;</code></p>
<dd> Report GFF output for features on the target sequence.</p>
<dt><code>&#8211;ryo &lt;format&gt;</code></p>
<dd> Roll-your-own output format. This allows specification of a printf-esque format line which is used to specify which information to include in the output, and how it is to be shown. The format field may contain the following fields:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>%[qt][idlsSt]</code></p>
<dd> For either {query,target}, report the {id,definition,length,sequence,Strand,type} Sequences are reported in a fasta-format like block (no headers).</p>
<dt><code>%[qt]a[bels]</code></p>
<dd> For either {query,target} region which occurs <code>in the alignment,</code> report the {begin,end,length,sequence}</p>
<dt><code>%[qt]c[bels]</code></p>
<dd> For either {query,target} region which occurs in the <code>coding sequence</code> in the alignment, report the {begin,end,length,sequence}</p>
<dt><code>%s</code></p>
<dd> The raw score</p>
<dt><code>%r</code></p>
<dd> The rank (in results from a bestn search)</p>
<dt><code>%m</code></p>
<dd> Model name</p>
<dt><code>%e[tism]</code></p>
<dd> Equivalenced {total,id,similarity,mismatches} (ie. %em == (%et &#8211; %ei))</p>
<dt><code>%p[isS]</code></p>
<dd> Percent {id,similarity,Self} over the equivalenced portions of the alignment. (ie. %pi == 100*(%ei / %et)). Percent Self is the score over the equivalenced portions of the alignment as a percentage of the self comparison score of the query sequence.</p>
<dt><code>%g</code></p>
<dd> Gene orientation (&#8216;+&#8217; = forward, &#8216;-&#8216; = reverse, &#8216;.&#8217; = unknown)</p>
<dt><code>%S</code></p>
<dd> Sugar block (the 9 fields used in sugar output (see above)</p>
<dt><code>%C</code></p>
<dd> Cigar block (the fields of a cigar line after the sugar portion)</p>
<dt><code>%V</code></p>
<dd> Vulgar block (the fields of a vulgar line after the sugar portion)</p>
<dt><code>%%</code></p>
<dd> Expands to a percentage sign (%)</p>
<dt><code>
</code></p>
<dd> Newline</p>
<dt><code>	</code></p>
<dd> Tab</p>
<dt><code>\</code></p>
<dd> Expands to a backslash (\)</p>
<dt><code>\{</code></p>
<dd> Open curly brace</p>
<dt><code>\}</code></p>
<dd> Close curly brace</p>
<dt><code>{</code></p>
<dd> Begin per-transition output section</p>
<dt><code>}</code></p>
<dd> End per-transition output section</p>
<dt><code>%P[qt][sabe]</code></p>
<dd> Per-transition output for {query,target} {sequence,advance,begin,end}</p>
<dt><code>%P[nsl]</code></p>
<dd> Per-transition output for {name,score,label}</dl>
</dl>
<p> This option is very useful and flexible. For example, to report all the sections of query sequences which feature in alignments in fasta format, use: </p>
<p> &#8211;ryo <code>&quot;&gt;%qi %qd
%qas
&quot;</code> </p>
<p> To output all the symbols and scores in an alignment, try something like: </p>
<p> &#8211;ryo <code>&quot;%V{%Pqs %Pts %Ps
}&quot;</code> </p>
<dl>
<dt><code>-n | &#8211;bestn &lt;number&gt;</code></p>
<dd> Report the best N results for each query. (Only results scoring better than the score threshold<br />
&nbsp;<wbr>will be reported). The option reduces the amount of output generated, and also allows exonerate to speed up the search.</p>
<dt><code>-S | &#8211;subopt &lt;boolean&gt;</code></p>
<dd> This option allows for the reporting of (Waterman-Eggert style) suboptimal alignments. (It is on by default.) All suboptimal (ie. non-intersecting) alignments will be reported for each pair of sequences scoring at least the threshold provided by <code>&#8211;score.</code> </p>
<p> When this option is used with exhaustive alignments, several full quadratic time passes will be required, so the running time will be considerably increased.</p>
<dt><code>-g | &#8211;gappedextension &lt;boolean&gt;</code></p>
<dd> Causes a gapped extension stage to be performed ie. dynamic programming is applied in arbitrarily shaped and dynamically sized regions surrounding HSP seeds. The extension threshold is controlled by the &#8211;extensionthreshold option. </p>
<p> Although sometimes slower than BSDP, gapped extension improves sensitivity with weak, gap-rich alignments such as during cross-species comparison. </p>
<p> <code>NB. This option is now the default. Set it to false</code> to reverse to the old BSDP type alignments. This option may be slower than BSDP for some large scale analyses with simple alignment models.</p>
<dt><code>&#8211;refine &lt;strategy&gt;</code></p>
<dd> Force exonerate to refine alignments generated by heuristics using dynamic programming over larger regions. This takes more time, but improves the quality of the final alignments. </p>
<p> The strategies available for refinement are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> The default &#8211; no refinement is used.</p>
<dt><code>full</code></p>
<dd> An exhaustive alignment is calculated from the pair of sequences in their entirety.</p>
<dt><code>region</code></p>
<dd> DP is applied just to the region of the sequences covered by the heuristic alignment.</dl>
</dl>
<dl>
<dt><code>&#8211;refineboundary &lt;size&gt;</code></p>
<dd> Specify an extra boundary to be included in the region subject to alignment during refinement by region. </p>
</dl>
<h2>VITERBI ALGORITM OPTIONS</h2>
<dl>
<dt><code>-D | &#8211;dpmemory &lt;Mb&gt;</code></p>
<dd> The exhaustive alignment traceback routines use a Hughey-style reduced memory technique. This option specifies how much memory will be used for this. Generally, the more memory is permitted here, the faster the alignments will be produced. </p>
</dl>
<h2>CODE GENERATION OPTIONS</h2>
<dl>
<dt><code>-C | &#8211;compiled &lt;boolean&gt;</code></p>
<dd> This option allows disabling of generated code for dynamic programming. It is mainly used during development of exonerate. When set to FALSE, an &quot;interpreted&quot; version of the dynamic programming implementation is used, which is much slower. </p>
</dl>
<h2>HEURISTIC OPTIONS</h2>
<p> <code>&#8211;terminalrangeint</code> </p>
<p> <code>&#8211;terminalrangeext</code> </p>
<p> <code>&#8211;joinrangeint</code> </p>
<p> <code>&#8211;joinrangeext</code> </p>
<p> <code>&#8211;spanrangeint</code> </p>
<dl>
<dt><code>&#8211;spanrangeext</code></p>
<dd> These options are used to specify the size of the sub-alignment regions to which DP is applied around the ends of the HSPs. This can be at the HSP ends (terminal range), between HSPs (join range), or between HSPs which may be connected by a large region such as an intron or non-equivalenced region (span range). These ranges can be specified for a number of matches back onto the HSP (internal range) or out from the HSP (external range). </p>
</dl>
<h2>SEEDED DYNAMIC PROGRAMMING OPTIONS</h2>
<dl>
<dt><code>-x | &#8211;extensionthreshold &lt;score&gt;</code></p>
<dd> This is the amount by which the score will be allowed to degrade during SDP. This is the equivalent of the hspdropoff penalties, except it is applied during dynamic programming, not HSP extension. Decreasing this parameter will increase the speed of the SDP, and increasing it will increase the sensitivity.</p>
<dt><code>&#8211;singlepass &lt;boolean&gt;</code></p>
<dd> By default the suboptimal SDP alignments are reported by a singlepass algorithm, but may miss some suboptimal alignments that are close together. This option can be used to force the use of a multipass suboptimal alignment algorithm for SDP, resulting in higher quality suboptimal alignments.</dl>
<h2>BSDP OPTIONS</h2>
<dl>
<dt><code>&#8211;joinfilter &lt;limit&gt;</code></p>
<dd> (experimental) </p>
<p> Only allow consider this number of SARs for joining HSPs together. The SARs with the highest potential for appearing in a high-scoring alignment are considered. This option useful for limiting time and memory usage when searching unmasked data with repetitive sequences, but should not be set too low, as valid matches may be ignored. Something like <code>&#8211;joinfilter 32</code> seems to work well.</dl>
<h2>SEQUENCE OPTIONS</h2>
<dl>
<dt><code>&#8211;annotation &lt;path&gt;</code></p>
<dd> Specify basic sequence annotation information. This is most useful with the cdna2genome model, but will work with other models. The annotation file contains four fields per line:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&lt;id&gt; &lt;strand&gt; &lt;cds_start&gt; &lt;cds_length&gt;</p>
<dd>
<dt>Here is a simple example of such a file for 4 cDNAs:</p>
<dd>
</dl>
<dl>
<dt>dhh.human.cdna + 308 1191</p>
<dd></dl>
<p> dhh.mouse.cdna + 250 1191 </p>
<p> csn7a.human.cdna + 178 828 </p>
<p> csn7a.mouse.cdna + 126 828 </p>
<p> These annotation lines will also work when only the first two fields are used. This can be used when specifying which strand of a specific sequence should be included in a comparison.</dl>
<h2>SYMBOL COMPARISON OPTIONS</h2>
<dl>
<dt><code>&#8211;softmaskquery &lt;boolean&gt;</code></p>
<dd> Indicate that the query is softmasked. See description below for <code>&#8211;softmasktarget</code></p>
<dt><code>&#8211;softmasktarget &lt;boolean&gt;</code></p>
<dd> Indicate that the target is softmasked. In a softmasked sequence file, instead of masking regions by Ns or Xs they are masked by putting those regions in lower case (and with unmasked regions in upper case). This option allows the masking to be ignored by some parts of the program, combining the speed of searching masked data with sensitivity of searching unmasked data. The utility <code>fastasoftmask</code> supplied which is supplied with exonerate can be used for producing softmasked sequence from conventionally masked sequence.</p>
<dt><code>-d | &#8211;dnasubmat &lt;name&gt;</code></p>
<dd> Specify the the substitution matrix to be used for DNA comparison. This should be a path to a substitution matrix in same format as that which is used by blast.</p>
<dt><code>-p | &#8211;proteinsubmat &lt;name&gt;</code></p>
<dd> Specify the the substitution matrix to be used for protein comparison. (Both DNA and protein substitution matrices are required for some types of analysis). The use of the special names, <code>nucleic, blosum62, pam250, edit</code> or <code>identity</code> will cause built-in substitution matrices to be used.</dl>
<h2>ALIGNMENT SEEDING OPTIONS</h2>
<dl>
<dt><code>-M | &#8211;fsmmemory &lt;Mb&gt;</code></p>
<dd> Specify the amount of memory to use for the FSM in heuristic analyses. exonerate multiplexes the query to accelerate large-throughput database queries. This figure should always be less than the physical memory on the machine, but when searching large databases, generally, the more memory it is allowed to use, the faster it will go.</p>
<dt><code>&#8211;forcefsm &lt;none | normal | compact&gt;</code></p>
<dd> Force the use of more compact finite state machines for analyses involving big sequences and large word neighbourhoods. By default, exonerate will pick a sensible strategy, so this option will rarely need to be set.</p>
<dt><code>&#8211;wordjump &lt;int&gt;</code></p>
<dd> The jump between query words used to yield the word neighbourhood. If set to 1, every word is used, if set to 2, every other word is used, and if set to the wordlength, only non-overlapping words will be used. This option reduces the memory requirements when using very large query sequences, and makes the search run faster, but it also damages search sensitivity when high values are set.</p>
<dt><code>&#8211;wordambiguity &lt;limit&gt;</code></p>
<dd> This option may be used to allow alignment seeds containing IUPAC ambiguity symbols. The limit is the maximum number of ambiguous words allowed at a single position. If this limit is reached then the position is not used for alignment seeding. Using this option may slow down a search. For large datasets, it is recommended to use <code>esd2esi &#8211;wordambiguity</code> instead, as then the speed overhead is only incurred during indexing, rather than during the database searching itself. NB. This option only works for IUPAC symbols in the target sequence. Query words containing IUPAC symbols are (currently) excluded from seeding.</dl>
<h2>AFFINE MODEL OPTIONS</h2>
<dl>
<dt><code>-o | &#8211;gapopen &lt;penalty&gt;</code></p>
<dd> This is the gap open penalty.</p>
<dt><code>-e | &#8211;gapextend &lt;penalty&gt;</code></p>
<dd> This is the gap extension penalty.</p>
<dt><code>&#8211;codongapopen &lt;penalty&gt;</code></p>
<dd> This is the codon gap open penalty.</p>
<dt><code>&#8211;codongapextend &lt;penalty&gt;</code></p>
<dd> This is the codon gap extension penalty.</dl>
<h2>NER OPTIONS</h2>
<dl>
<dt><code>&#8211;minner &lt;boolean&gt;</code></p>
<dd> Minimum NER length allowed.</p>
<dt><code>&#8211;maxner &lt;length&gt;</code></p>
<dd> Maximum NER length allowed. NB. this option only affects heuristic alignments.</p>
<dt><code>&#8211;neropen &lt;penalty&gt;</code></p>
<dd> Penalty for opening a non-equivalenced region.</dl>
<h2>INTRON MODELLING OPTIONS</h2>
<dl>
<dt><code>&#8211;minintron &lt;length&gt;</code></p>
<dd> Minimum intron length limit. NB. this option only affects heuristic alignments. This is not a hard limit &#8211; it only affects size of introns which are sought during heuristic alignment.</p>
<dt><code>&#8211;maxintron &lt;length&gt;</code></p>
<dd> Maximum intron length limit. See notes above for <code>&#8211;minintron</code></p>
<dt><code>-i | &#8211;intronpenalty &lt;penalty&gt;</code></p>
<dd> Penalty for introduction of an intron.</dl>
<h2>FRAMESHIFT MODELLING OPTIONS</h2>
<dl>
<dt><code>-f | &#8211;frameshift &lt;penalty&gt;</code></p>
<dd> The penalty for the inclusion of a frameshift in an alignment.</dl>
<h2>ALPHABET OPTIONS</h2>
<dl>
<dt><code>&#8211;useaatla &lt;boolean&gt;</code></p>
<dd> Use three-letter abbreviations for AA names. ie. when displaying alignment &quot;Met&quot; is used instead of &quot; M &quot;</dl>
<h2>TRANSLATION OPTIONS</h2>
<dl>
<dt><code>&#8211;geneticcode &lt;code&gt;</code></p>
<dd> Specify an alternative genetic code. The default code (1) is the standard genetic code. Other genetic codes may be specified by in shorthand or longhand form. </p>
<p> In shorthand form, a number between 1 and 23 is used to specify one of 17 built-in genetic code variants. These are genetic code variants taken from: </p>
<p> <code><a rel="nofollow" href="http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi">http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi</a></code> </p>
<p> These are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>1</code></p>
<dd> The Standard Code</p>
<dt><code>2</code></p>
<dd> The Vertebrate Mitochondrial Code</p>
<dt><code>3</code></p>
<dd> The Yeast Mitochondrial Code</p>
<dt><code>4</code></p>
<dd> The Mold, Protozoan, and Coelenterate Mitochondrial Code and the Mycoplasma/Spiroplasma Code</p>
<dt><code>5</code></p>
<dd> The Invertebrate Mitochondrial Code</p>
<dt><code>6</code></p>
<dd> The Ciliate, Dasycladacean and Hexamita Nuclear Code</p>
<dt><code>9</code></p>
<dd> The Echinoderm and Flatworm Mitochondrial Code</p>
<dt><code>10</code></p>
<dd> The Euplotid Nuclear Code</p>
<dt><code>11</code></p>
<dd> The Bacterial and Plant Plastid Code</p>
<dt><code>12</code></p>
<dd> The Alternative Yeast Nuclear Code</p>
<dt><code>13</code></p>
<dd> The Ascidian Mitochondrial Code</p>
<dt><code>14</code></p>
<dd> The Alternative Flatworm Mitochondrial Code</p>
<dt><code>15</code></p>
<dd> Blepharisma Nuclear Code</p>
<dt><code>16</code></p>
<dd> Chlorophycean Mitochondrial Code</p>
<dt><code>21</code></p>
<dd> Trematode Mitochondrial Code</p>
<dt><code>22</code></p>
<dd> Scenedesmus obliquus mitochondrial Code</p>
<dt><code>23</code></p>
<dd> Thraustochytrium Mitochondrial Code&quot;,</dl>
<p> In longhand form, a genetic code variant may be provided as a 64 byte string in TCAG order, eg. the standard genetic code in this form would be: </p>
<p> FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG </p>
</dl>
<h2>HSP CREATION OPTIONS</h2>
<dl>
<dt><code>&#8211;hspfilter &lt;threshold&gt;</code></p>
<dd> Use aggressive HSP filtering to speed up heuristic searches. The threshold specifies the number of HSPs centred about a point in the query which will be stored. Any lower scoring HSPs will be discarded. This is an experimental option to handle speed problems caused by some sequences. A value of about 100 seems to work well.</p>
<dt><code>&#8211;useworddropoff &lt;boolean&gt;</code></p>
<dd> When this is TRUE, the score threshold for admitting words into the word neighbourhood is set to be the initial word score minus the word threshold (see below). This strategy is designed to prevent restricting the word SSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG When this is FALSE, the word threshold is taken to be an absolute value.</p>
<dt><code>&#8211;seedrepeat &lt;count&gt;</code></p>
<dd> The seedrepeat parameter sets the number of seeds which must be found on the same diagonal or reading frame before HSP extension will occur. Increasing the value for <code>&#8211;seedrepeat</code> will speed up searches, and is usually a better option than using longer word lengths, particularly when using the <code>exonerate-server</code> where increasing word lengths requires recomputing the index, and greater increases memory requirements.</p>
<dt><code>-w &#8211;dnawordlen &lt;bases&gt;</code></p>
<dd>
<dt><code>-W &#8211;proteinwordlen &lt;residues&gt;</code></p>
<dd>
<dt><code>-W &#8211;codonnwordlen &lt;bases&gt;</code></p>
<dd> The word length used for DNA, protein or codon words. When performing DNA vs protein comparisons, a the DNA wordlength will always (automatically) be triple the protein wordlength.</p>
<dt><code>&#8211;dnahspdropoff &lt;score&gt;</code></p>
<dd>
<dt><code>&#8211;proteinhspdropoff &lt;score&gt;</code></p>
<dd>
<dt><code>&#8211;codonhspdropoff &lt;score&gt;</code></p>
<dd> The amount by which an HSP score will be allowed to degrade during HSP extension. Separate threshold can be set for dna or protein comparisons.</p>
<dt><code>&#8211;dnahspthreshold &lt;score&gt;</code></p>
<dd>
<dt><code>&#8211;proteinhspthreshold &lt;score&gt;</code></p>
<dd>
<dt><code>&#8211;codonhspthreshold &lt;score&gt;</code></p>
<dd> The HSP score thresholds. An HSP must score at least this much before it will be reported or be used in preparation of a heuristic alignment.</p>
<dt><code>&#8211;dnawordlimit &lt;score&gt;</code></p>
<dd>
<dt><code>&#8211;proteinwordlimit &lt;score&gt;</code></p>
<dd>
<dt><code>&#8211;codonwordlimit &lt;score&gt;</code></p>
<dd> The threshold for admitting DNA or protein words into the word neighbourhood. The behaviour of this option is altered by the <code>&#8211;useworddropoff</code> option (see above). </p>
<dt><code>&#8211;geneseed &lt;threshold&gt;</code></p>
<dd> Exclude HSPs from gapped alignment computation which cannot feature in a alignment containing at least one HSP scoring at least this threshold. </p>
<p> This option provides considerable speed up for gapped alignment computation, but may cause some very gap-rich alignments to be missed. </p>
<p> It is useful when aligning similar sequences back onto genome quickly, eg. try &#8211;geneseed 250</p>
<dt><code>&#8211;geneseedrepeat &lt;count&gt;</code></p>
<dd> The geneseedrepeat parameter is like the seedrepeat parameter, but is only applied when looking for the geneseed hsps. Using a larger value for <code>&#8211;geneseedrepeat</code> will speed up searches when the <code>&#8211;geneseed</code> parameter is also used. (experimental, implementation incomplete)</dl>
<h2>ALIGNMENT OPTIONS</h2>
<dl>
<dt><code>&#8211;alignmentwidth &lt;width&gt;</code></p>
<dd> Width of alignment display. The default is 80.</p>
<dt><code>&#8211;forwardcoordinates &lt;boolean&gt;</code></p>
<dd> By default, all coordinates are reported on the forward strand. Setting this option to false reverts to the old behaviour (pre-0.8.3) whereby alignments on the reverse complement of a sequence are reported using coordinates on the reverse complement.</dl>
<h2>SUB-ALIGNMENT REGION OPTIONS</h2>
<dl>
<dt><code>&#8211;quality &lt;percent&gt;</code></p>
<dd> This option excludes HSPs from BSDP when their components outside of the SARs fall below this quality threshold.</dl>
<h2>SPLICE SITE PREDICTION OPTIONS</h2>
<dl>
<dt><code>&#8211;splice3 &lt;path&gt;</code></p>
<dd>
<dt><code>&#8211;splice5 &lt;path&gt;</code></p>
<dd> Provide a file containing a custom PSSM (position specific score matrix) for prediction of the intron splice sites. </p>
<p> The file format for splice data is simple: lines beginning with &#8216;#&#8217; are comments, a line containing just the word &#8216;splice&#8217; denotes the position of the splice site, and the other lines show the observed relative frequencies of the bases flanking the splice sites in the chosen organism (in ACGT order). </p>
<p> <code>Example 5&#8242; splice data file:</code> </p>
<pre>
 # start of example 5' splice data
 # A C G T
 28 40  17  14
 59 14  13  14
  8  5  81   6
 splice
  0  0 100   0
  0  0   0 100
 54  2  42   2
 74  8  11   8
  5  6  85   4
 16 18  21  45
 # end of test 5' splice data
</pre>
<p> <code>Example 3&#8242; splice data file:</code> </p>
<pre>
 # start of example 3' splice data
 # A C G T
  10  31  14  44
   8  36  14  43
   6  34  12  48
   6  34   8  52
   9  37   9  45
   9  38  10  44
   8  44   9  40
   9  41   8  41
   6  44   6  45
   6  40   6  48
  23  28  26  23
   2  79   1  18
 100   0   0   0
   0   0 100   0
 splice
  28  14  47  11
 # end of example 3' splice data
</pre>
<dt><code>&#8211;forcegtag &lt;boolean&gt;</code></p>
<dd> Only allow splice sites at gt&#8230;.ag sites (or ct&#8230;.ac sites when the gene is reversed) With this restriction in place, the splice site prediction scores are still used and allow tie breaking when there is more than one possible splice site. </p>
</dl>
<h2>STRATEGIES FOR SPEED</h2>
<p> Keep all data on local disks. </p>
<p> Apply the highest acceptable score thresholds using a combination of &#8211;score, &#8211;percent and &#8211;bestn. </p>
<p> Repeat mask and dust the genomic (target) sequence. (Softmask these sequences and use &#8211;softmasktarget). </p>
<p> Increase the &#8211;fsmmemory option to allow more query multiplexing. </p>
<p> Increase the value for &#8211;seedrepeat </p>
<p> When using an alignment model containing introns, set &#8211;geneseed as high as possible. </p>
<p> If you are compiling exonerate yourself, see the README file supplied with the source code for details of compile-time optimisations. </p>
<h2>STRATEGIES FOR SENSITIVITY</h2>
<p> Not documented yet. </p>
<p> Increase the word neighbourhood. Decrease the HSP threshold. Increase the SAR ranges. Run exhaustively. </p>
<h2>ENVIRONMENT</h2>
<p> Not documented yet. </p>
<h2>EXAMPLES</h2>
<p> <code>exonerate cdna.fasta genomic.fasta</code></p>
<dl>
<dt>
<dd> This simplest way in which exonerate may be used. By default, an ungapped alignment model will be used.</dl>
<p> <code>exonerate &#8211;exhaustive y &#8211;model est2genome cdna.fasta genomic.masked.fasta</code></p>
<dl>
<dt>
<dd> Exhaustively align cdnas to genomic sequence. This will be much, much slower, but more accurate. This option causes exonerate to behave like EST_GENOME.</dl>
<p> <code>exonerate &#8211;exhaustive &#8211;model affine:local</code> <code>query.fasta target.fasta</code></p>
<dl>
<dt>
<dd> If the affine:local model is used with exhaustive alignment, you have the Smith-Waterman algorithm.</dl>
<p> <code>exonerate &#8211;exhaustive &#8211;model affine:global</code> <code>protein.fasta protein.fasta</code></p>
<dl>
<dt>
<dd> Switch to a global model, and you have Needleman-Wunsch.</dl>
<p> <code>exonerate &#8211;wordthreshold 1 &#8211;gapped no &#8211;showhsp yes protein.fasta genome.fasta</code></p>
<dl>
<dt>
<dd> Generate ungapped Protein:DNA alignments</dl>
<p> <code>exonerate &#8211;model coding2coding &#8211;score 1000 &#8211;bigseq yes &#8211;proteinhspthreshold 90 chr21.fa chr22.fa</code></p>
<dl>
<dt>
<dd> Perform quick-and-dirty translated pairwise alignment of two very large DNA sequences.</dl>
<p> Many similar combinations should work. Try them out. </p>
<h2>VERSION</h2>
<p> This documentation accompanies version 2.2.0 of the exonerate package.</p>
<h2>AUTHOR</h2>
<p> Guy St.C. Slater. &lt;guy [at] ebi.ac.uk&gt;. See the AUTHORS file accompanying the source code for a list of contributors.</p>
<h2>AVAILABILITY</h2>
<p> This source code for the exonerate package is available under the terms of the GNU <i>general</i> public licence. </p>
<p> Please see the file COPYING which was distrubuted with this package, or <a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a> for details. </p>
<p> This package has been developed as part of the ensembl project. Please see <a rel="nofollow" href="http://www.ensembl.org/">http://www.ensembl.org/</a> for more information.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-exonerate-server/">exonerate-server</a></code>(1), <code><a href="/docs/linux/man/1-ipcress/">ipcress</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/1L-blast/">blast</a></code>(1L). </p>
<h2>Index</h2>
