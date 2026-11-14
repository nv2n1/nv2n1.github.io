---
title: "dasdseq(1)"
name: "dasdseq"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dasdseq/"
description: "dasdseq – Hercules DSORG=PS retrieval command"
---

<h2>NAME</h2>
<p> <code>dasdseq</code> &#8211; Hercules DSORG=PS retrieval command </p>
<h2>SYNOPSIS</h2>
<p> <code>dasdseq</code> [options&#8230;] <code>image </code>[sf=shadow] <code>filespec</code><br />
 <code>dasdseq </code>[-debug] [-expert] [-ascii] <code>image </code>[sf=shadow] [attr] <code>filespec </code>[debugopts] [ascii] </p>
<h2>DESCRIPTION</h2>
<p> Hercules command to retrieve a DSORG=PS (sequential) dataset from CKD/CCKD DASD. The dataset is presumed to be encoded in EBCDIC. The second form of the command is for &#8216;expert mode&#8217; users, and allows more advanced access to data on the DASD image. </p>
<h2>OPTIONS</h2>
<p> The following options are used to specify dasdseq behavior. Surround each option by blank(s). Options are divided into three categories: <code>required, optional, and expert mode operands.</code> </p>
<h2>Required operands</h2>
<h3>image</h3>
<p> specifies the Hercules CKD/CCKD DASD filename (sometimes referred to as the DASD image file)</p>
<h3>filespec</h3>
<p> dataset name of the file to retrieve. Case insensitive, converted to upper case for searching VTOC on image DASD volume. </p>
<h2>Optional operands</h2>
<h3>sf=shadow</h3>
<p> For CCKD images which also use shadow files, specifies the [path/]filename of the shadow file. Note the sf=, which must be present for this option. </p>
<h3>-ascii</h3>
<p> convert the output file to ASCII (from EBCDIC). Additionally, trailing blanks are trimmed. The &#8216;ascii&#8217; option (no leading dash) is deprecated, and may be removed in a future release. </p>
<h2>Expert mode operands</h2>
<p> All expert mode operands are considered to be experimental. </p>
<p> <code> dasdseq [-debug] [-expert] [-ascii] image [sf=shadow] [attr] filespec [debugopts]</code> </p>
<h3>-debug</h3>
<p> Additional debug options are displayed. Specifying -debug will (eventually) display dataset extent information. </p>
<h3>attr</h3>
<p> dataset attributes (only useful with -abs) </p>
<p> <code>[-recfm fb] [-lrecl aa]</code> </p>
<p> -recfm designates RECFM, reserved for future support </p>
<p> fb &#8211; fixed, blocked (only RECFM currently supported) </p>
<p> -lrecl designates dataset LRECL </p>
<p> aa &#8211; decimal logical record length (default 80) </p>
<p> Blocksize need not be specified; dasdseq handles whatever block size comes off the volume. </p>
<h3>filespec</h3>
<p> composed of the following sub-operands, in the following order: <code>heads, abs, filename.</code> </p>
<h3>-heads xx</h3>
<p> defines # tracks per cylinder on device; xx = decimal number of heads per cylinder on device </p>
<h3>-abs cc hh tt [&#8230;] [-abs cc hh tt]</h3>
<p> -abs indicates the beginning of each extent&#8217;s location in terms of absolute dasd image location. </p>
<p> cc &#8211; decimal cylinder number (relative zero) </p>
<p> hh &#8211; decimal head number (relative zero) </p>
<p> tt &#8211; decimal number of tracks in extent </p>
<p> When -abs is specified, each -abs group specifies one dataset extent. For multi-extent datasets, -abs groups may be repeated as needed, in the order in which the dataset&#8217;s extents occur. A maximum of 123 extents are supported. With -abs, no VTOC structure is implied; a F1 DSCB will not be sought. Dasdseq will frequently report &#8216;track not found in extent table&#8217; (along with a message from fbcopy about rc -1 from convert_tt) due to potentially missing EOF markers in the extent, and the fact that the F1 DSCB DS1LSTAR field is not valid. Check your output file before you panic. Fbcopy -abs ignores EOF, in case you are attempting to recovery PDS member(s) from a damaged dasd volume, preferring to wait until all tracks in the extent have been processed. Tracks containing PDS members may have more than one EOF per track. Expect a lot of associated manual effort with -abs. </p>
<p> When -abs is -not- specified, filename specifies the MVS DSORG=PS dataset on the volume. The dasd image volume containing the dataset must have a valid VTOC structure, and a F1 DSCB describing the dataset. </p>
<h3>filename</h3>
<p> will be the filename of the output file in the current directory; output filename in the same case as the command line filename. </p>
<h3>debugopts</h3>
<p> Produces debugging output, refer to the source code. </p>
<p> <code>verbose [x [y [z]]]</code> </p>
<p> verbose debug output level (default = 0 when not specified). Higher numbers produce more output. </p>
<p> x main program (default = 1 when verbose specified) </p>
<p> y copyfile + showf1 </p>
<p> z dasdutil </p>
<h2>SEE ALSO</h2>
<dl>
<dt>dasdpdsu for DSORG=PO datasets</p>
<dd>
<dt><a href="/docs/linux/man/4-cckd/">cckd</a>(4) for CCKD DASD</p>
<dd>
<dt><a rel="nofollow" href="http://www.hercules-390.org/cckddasd.html">http://www.hercules-390.org/cckddasd.html</a> which describes</p>
<dd> the Hercules CCKD DASD facility.</p>
<dt><a rel="nofollow" href="http://www.hercules-390.org/">http://www.hercules-390.org/</a> the Hercules emulator homepage.</p>
<dd>
</dl>
<h2>HISTORY</h2>
<p> 2003-03-10 originally written by James M. Morrison </p>
<h2>Index</h2>
