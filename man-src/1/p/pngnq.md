---
title: "pngnq(1)"
name: "pngnq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pngnq/"
description: "pngnq – quantize png images"
---

<h2>NAME</h2>
<p> pngnq &#8211; quantize png images</p>
<h2>SYNOPSIS</h2>
<p> <code>pngnq [-vfhV][-s </code> <i>sample_factor</i> <code>][-Q </code> <i>dither</i> <code>][-g</code> <i>gamma</i> <code>][-e </code> <i>extension </i> <code>][-d </code> <i>dir</i> <code>][-n </code> <i>colors</i> <code>][</code> <i>inputfiles</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pngnq</code> Quantizes a 32-bit RGBA PNG image to an 8 bit RGBA palette PNG using the neuquant algorithm. The output file name is the input file name extended with &quot;-nq8.png&quot; or a specified extension. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-v</p>
<dd> Verbose mode. Prints status messages.</p>
<dt>-f</p>
<dd> Force ovewriting of files.</p>
<dt>-s sample factor</p>
<dd> Sample factor. The neuquant algorithm samples pixels stepping by this value. The default value of 3 gives good results. Higher values sample less of the image pixels and thus are faster but less accurate. A factor of 1 samples every image pixel.</p>
<dt>-n colors</p>
<dd> Specifies the number of colors to quantize to. Defaults to 256 which is the maximum. The minimum here is 2.</p>
<dt>-Q dither</p>
<dd> Choose a dithering method: n = no dither (default), f = Floyd Steinberg dithering.</p>
<dt>-g gamma</p>
<dd> Set the image gamma correction. If not present, uses the png file&#8217;s gamma or defaults to 1.0.</p>
<dt>-e extension</p>
<dd> Specifies the new filename extension. Defaults to &quot;-nq8.png&quot;. Pngnq drops .png from the original filenames. If you set the argument of the -e option to .png and choose the -f option the input file will be overwritten.</p>
<dt>-d dir</p>
<dd> Tells pngnq to put output files in a directory other than the one the input files are in.</p>
<dt>input files</p>
<dd> The png files to be processed. Defaults to standard input if not specified. If standard input is being processed the output is sent to standard output.</p>
<dt>-h</p>
<dd> Print program help.</p>
<dt>-V</p>
<dd> Print version number and library versions. </p>
</dl>
<h2>BUGS</h2>
<p> Does not deal correctly with greyscale alpha images with low bit depths, but these wont benefit from quantizing. </p>
<h2>AUTHOR</h2>
<p> Stuart Coyle &lt;stuart.coyle [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-png/">png</a>(5)</code> </p>
<h2>Index</h2>
