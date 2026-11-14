---
title: "toast(1)"
name: "toast"
section: "1"
letter: "t"
url: "/docs/linux/man/1-toast/"
description: "toast — GSM 06.10 lossy sound compression"
---

<h2>NAME</h2>
<p> toast &#8212; GSM 06.10 lossy sound compression</p>
<h2>SYNOPSIS</h2>
<p> <code>toast</code> [ <code>-cdfpvhualsFC</code> ] [ <i>filename&#8230;</i> ] </p>
<p> <code>untoast</code> [ <code>-cfpvhuaslF</code> ] [ <i>filename&#8230;</i> ] </p>
<p> <code>tcat</code> [ <code>-vhuaslF</code> ] [ <i>filename&#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Toast compresses the sound files given on its command line. Each file is replaced by a file with the extension <i>.gsm .</i> If no files are specified, the compression is applied to the standard input, and its result is written to standard output. </p>
<p> Toasted files can be restored to something not quite unlike their original form by running toast <i>-d</i> , or <i>untoast</i> , on the .gsm-files or standard input. </p>
<p> The program <i>tcat</i> (the same as running <i>untoast -c</i> ) uncompresses its input on standard output, but leaves the compressed .gsm-files alone. </p>
<p> When files are compressed or uncompressed into other files, the ownership (if run by root), modes, accessed and modified times are maintained between both versions.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> (cat) Write to the standard output; no files are changed.</p>
<dt><code>-d</code></p>
<dd> (decode) Decode, rather than encode, the files.</p>
<dt><code>-f</code></p>
<dd> (force) Force replacement of output files if they exist. If -f is omitted and toast (or untoast) is run interactively from a terminal, the user is prompted as to whether the file should be replaced.</p>
<dt><code>-p</code></p>
<dd> (precious) Do not delete the source files. Source files are implicitly left alone whenever -c is specified or tcat is run.</p>
<dt><code>-C</code></p>
<dd> (LTP cut-off) Ignore most sample values when calculating the GSM long-term correlation lag during encoding. (The multiplications that do this are a bottleneck of the algorithm.) The resulting encoding process will not produce exactly the same results as GSM 06.10 would, but remains close enough to be compatible.<br />
 The <code>-C</code> option applies only to the encoder and is silently ignored by the decoder.</p>
<dt><code>-F</code></p>
<dd> (fast) On systems with a floating point processor, but without a multiplication instruction, -F sacrifices standard conformance to performance and nearly doubles the speed of the algorithm.<br />
 The resulting encoding and decoding process will not produce exactly the same results as GSM 06.10 would, but remains close enough to be compatible.<br />
 The default is standard-conforming operation.</p>
<dt><code>-v</code></p>
<dd> (version)&nbsp;<wbr> outputs the version of toast (or untoast or tcat) to stdout and exits.</p>
<dt><code>-h</code></p>
<dd> (help)&nbsp;<wbr> prints a short overview of the options.</dl>
<p> Toast, untoast and tcat try to guess the appropriate audio data format from the file suffix. Command line options can also specify a format to be used for all files.<br />
 The following formats are supported:</p>
<dl>
<dt><code>-u</code></p>
<dd> (&mu;U-law) 8 kHz, 8 bit &mu;U-law encoding (file suffix .u)</p>
<dt><code>-a</code></p>
<dd> (A-law) 8 kHz, 8 bit A-law encoding (file suffix .A)</p>
<dt><code>-s</code></p>
<dd> (Sun audio) 8 kHz, 8 bit &mu;U-law encoding with audio header (file suffix .au)</p>
<dt><code>-l</code></p>
<dd> (linear) 8 kHz, 16 bit signed linear encoding in host byte order with 13 significant bits (file suffix .l)</dl>
<p> In absence of options or suffixes to specify a format, &mu;U-law encoding as forced by -u is assumed. </p>
<h2>PECULIARITIES</h2>
<p> A four bit magic number is prefixed to each 32 1/2-byte GSM frame, mainly because 32 1/2-bytes are rather clumsy to handle.</p>
<h2>WARNING</h2>
<p> The compression algorithm used is a lossy compression algorithm devised especially for speech; on no account should it be used for text, pictures or any other non-speech-data you consider valuable.</p>
<h2>BUGS</h2>
<p> Please direct bug reports to jutta [at] cs.tu-berlin.de.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-gsm/">gsm</a>(3) </p>
<h2>Index</h2>
