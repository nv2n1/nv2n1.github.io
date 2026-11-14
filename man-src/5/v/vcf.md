---
title: "vcf(5)"
name: "vcf"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vcf/"
description: "vcf – Variant Call Format"
---

<p>vcf &#8211; Variant Call Format</p>
<h2>Description</h2>
<p>The Variant Call Format (VCF) is a TAB-delimited format with each data line consisting of the following fields: </p>
<table>
<tr VALIGN=top>
<td ALIGN=right>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>CHROM</code></td>
<td>CHROMosome name
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>POS</code></td>
<td>the left-most POSition of the variant
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>ID</code></td>
<td>unique variant IDentifier
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>REF</code></td>
<td>the REFerence allele
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>ALT</code></td>
<td>the ALTernate allele(s) (comma-separated)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>QUAL</code></td>
<td>variant/reference QUALity
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>FILTER</code></td>
<td>FILTERs applied
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>INFO</code></td>
<td>INFOrmation related to the variant (semicolon-separated)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>FORMAT</code></td>
<td>FORMAT of the genotype fields (optional; colon-separated)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>10+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td><code>SAMPLE</code></td>
<td>SAMPLE genotypes and per-sample information (optional)
</td>
</tr>
</table>
<p> The following table gives the <code>INFO</code> tags used by samtools and bcftools.</p>
<dl>
<dt><code>AF1</code></p>
<dd>Max-likelihood estimate of the site allele frequency (AF) of the first ALT allele (double)</p>
<dt><code>DP</code></p>
<dd>Raw read depth (without quality filtering) (int)</p>
<dt><code>DP4</code></p>
<dd># high-quality reference forward bases, ref reverse, alternate for and alt rev bases (int[4])</p>
<dt><code>FQ</code></p>
<dd>Consensus quality. Positive: sample genotypes different; negative: otherwise (int)</p>
<dt><code>MQ</code></p>
<dd>Root-Mean-Square mapping quality of covering reads (int)</p>
<dt><code>PC2</code></p>
<dd>Phred probability of AF in group1 samples being larger (,smaller) than in group2 (int[2])</p>
<dt><code>PCHI2</code></p>
<dd>Posterior weighted chi^2 P-value between group1 and group2 samples (double)</p>
<dt><code>PV4</code></p>
<dd>P-value for strand bias, baseQ bias, mapQ bias and tail distance bias (double[4])</p>
<dt><code>QCHI2</code></p>
<dd>Phred-scaled PCHI2 (int)</p>
<dt><code>RP</code></p>
<dd># permutations yielding a smaller PCHI2 (int)</p>
<dt><code>CLR</code></p>
<dd>Phred log ratio of genotype likelihoods with and without the trio/pair constraint (int)</p>
<dt><code>UGT</code></p>
<dd>Most probable genotype configuration without the trio constraint (string)</p>
<dt><code>CGT</code></p>
<dd>Most probable configuration with the trio constraint (string)</p>
<dt><code>VDB</code></p>
<dd>Tests variant positions within reads. Intended for filtering RNA-seq artifacts around splice sites (float)</p>
<dt><code>RPB</code></p>
<dd>Mann-Whitney rank-sum test for tail distance bias (float)</p>
<dt><code>HWE</code></p>
<dd>Hardy-Weinberg equilibrium test (Wigginton et al) (float)</dl>
<h2>See Also</h2>
<dl>
<dt><a rel="nofollow" href="https://github.com/samtools/hts-specs">https://github.com/samtools/hts-specs</a></p>
<dd>The full VCF/BCF file format specification</p>
<dt><i>A note on exact tests of Hardy-Weinberg equilibrium</i></p>
<dd>Wigginton JE et al PMID:15789306 </p>
