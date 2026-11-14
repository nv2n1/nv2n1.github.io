---
title: "wimlib-imagex-export(1)"
name: "wimlib-imagex-export"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-export/"
description: "wimlib-imagex-export – Exports an image from a WIM archive to an existing or new WIM archive"
---

<h2>NAME</h2>
<p> wimlib-imagex-export &#8211; Exports an image from a WIM archive to an existing or new WIM archive</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex export</code> <i>SRC_WIMFILE</i> <i>SRC_IMAGE</i> <i>DEST_WIMFILE</i> [<i>DEST_IMAGE_NAME</i> [<i>DEST_IMAGE_DESCRIPTION</i>]] [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Copies the specified image in <i>SRC_WIMFILE</i> to <i>DEST_WIMFILE</i>, optionally changing its name and/or description and/or compression type. If <i>DEST_WIMFILE</i> exists, it is taken be a WIM archive to which the image will be appended. Otherwise, it is created as a new WIM archive containing only the exported image. This command is also available as simply <code>wimexport</code> if the appropriate hard link or batch file has been installed. </p>
<p> <i>SRC_IMAGE</i> specifies the image in <i>SRC_WIMFILE</i> to export. It may be a 1-based index of an image in <i>SRC_WIMFILE</i>, the name of an image in <i>SRC_WIMFILE</i>, or the keyword &quot;all&quot; to indicate that all images in <i>SRC_WIMFILE</i> are to be exported. Use the <code>wimlib-imagex info</code> (1) command to list the images a WIM file contains. </p>
<p> If specified, <i>DEST_IMAGE_NAME</i> is the name to give the image being exported to <i>DEST_WIMFILE</i>. The default is its name in <i>SRC_WIMFILE</i>. <i>DEST_IMAGE_NAME</i> cannot be specified if multiple images are being exported. </p>
<p> If specified, <i>DEST_IMAGE_DESCRIPTION</i> is the description to give the image being exported to <i>DEST_WIMFILE</i>. The default is its description in <i>SRC_WIMFILE</i>. </p>
<p> <code>wimlib-imagex export</code> supports exporting images from stand-alone WIMs as well as from split WIMs. However, you cannot export an image to a split WIM. See <code>SPLIT WIMS</code>. </p>
<p> <code>wimlib-imagex export</code> also supports exporting images from a non-pipable WIM into a (possibly new) pipable WIM, and vice versa. Furthermore, it will export a pipable WIM directly to standard output if &quot;-&quot; is specified as <i>DEST_WIMFILE</i> (this implies <code>&#8211;pipable</code>). See <code>&#8211;pipable</code> and <code>&#8211;not-pipable</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;boot</code></p>
<dd> Specifies that the exported image is to be the bootable image of the destination WIM archive.</p>
<dt>
<dd> If multiple images are being exported, this flag indicates that the image in the <i>SRC_WIMFILE</i> that is currently marked as bootable is to be made bootable in <i>DEST_WIMFILE</i>. If no image in <i>SRC_WIMFILE</i> is bootable, it is an error.</p>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>SRC_WIMFILE</i>, and <i>DEST_WIMFILE</i> if it exists, verify the file&#8217;s integrity if the integrity table is present; additionally, when writing <i>DEST_WIMFILE</i> with the new image(s) added, write an integrity table. If neither <code>&#8211;check</code> nor <code>&#8211;nocheck</code> is specified, an integrity table is included in <i>DEST_WIMFILE</i> if and only if <i>DEST_WIMFILE</i> already existed and it had an integrity table before.</p>
<dt><code>&#8211;nocheck</code></p>
<dd> When writing <i>DEST_WIMFILE</i> with the new image(s) added, do not write an integrity table. If neither <code>&#8211;check</code> nor <code>&#8211;nocheck</code> is specified, an integrity table is included in <i>DEST_WIMFILE</i> if and only if <i>DEST_WIMFILE</i> already existed and it had an integrity table before.</p>
<dt><code>&#8211;compress</code>=<i>TYPE</i>[:<i>LEVEL</i>]</p>
<dd> Specifies the compression type, and optionally the compression level for that compression type, for <i>DEST_WIMFILE</i>. Setting the compression type only has an effect if <i>DEST_WIMFILE</i> does not yet exist, since if <i>DEST_WIMFILE</i> exists, the compression type must be the same as that of <i>DEST_WIMFILE</i>.</p>
<dt>
<dd> See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;recompress</code></p>
<dd> Force all exported data to be recompressed, even if the destination WIM will use the same compression type as the source WIM.</p>
<dt><code>&#8211;chunk-size</code>=<i>SIZE</i></p>
<dd> Set the WIM compression chunk size to <i>SIZE</i>. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;solid</code></p>
<dd> Create a &quot;solid&quot; archive that compresses multiple files together. This can result in a higher compression ratio, but has disadvantages such as reduced compatibility. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;solid-chunk-size</code>=<i>SIZE</i></p>
<dd> Like <code>&#8211;chunk-size</code>, but set the chunk size used in solid resources. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;solid-compress</code>=<i>TYPE</i>[:<i>LEVEL</i>]</p>
<dd> Like <code>&#8211;compress</code>, but set the compression type used in solid resources. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;threads</code>=<i>NUM_THREADS</i></p>
<dd> Number of threads to use for compressing data. Default: autodetect (number of processors). Note: multiple compressor threads are not very useful when exporting to a WIM with the same compression type as the source WIM, since wimlib optimizes this case by re-using the raw compressed data.</p>
<dt><code>&#8211;rebuild</code></p>
<dd> When exporting image(s) to an existing WIM: rebuild the entire WIM rather than appending data to the end of it. Rebuilding the WIM is slower, but will save a little bit of space that would otherwise be left as a hole in the WIM. Also see <code>wimlib-imagex optimize</code>.</p>
<dt><code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot;</p>
<dd> File glob of additional WIMs or split WIM parts to reference resources from. See <code>SPLIT_WIMS</code>. This option can be specified multiple times. Note: <i>GLOB</i> is listed in quotes because it is interpreted by <code>wimlib-imagex</code> and may need to be quoted to protect against shell expansion.</p>
<dt><code>&#8211;pipable</code></p>
<dd> Build, or rebuild, <i>DEST_WIMFILE</i> as a &quot;pipable WIM&quot; so that it can be applied fully sequentially, including from a pipe. See <code>wimlib-imagex <a href="/docs/linux/man/1-capture/">capture</a></code>(1) for more details about creating pipable WIMs. The default without this option is to make <i>DEST_WIMFILE</i> pipable if and only if it already existed and was already pipable, or was &quot;-&quot; (standard output).</p>
<dt><code>&#8211;not-pipable</code></p>
<dd> Build, or rebuild, <i>DEST_WIMFILE</i> as a normal, non-pipable WIM. This is the default behavior, unless <i>DEST_WIMFILE</i> already existed and was already pipable, or if <i>DEST_WIMFILE</i> was &quot;-&quot; (standard output).</p>
<dt><code>&#8211;wimboot</code></p>
<dd> Mark the destination image as WIMBoot-compatible. Also, if exporting to a new archive, set the compression type to that recommended for WIMBoot (currently, XPRESS with 4096 byte chunks).</p>
<dt><code>&#8211;unsafe-compact</code></p>
<dd> Compact the WIM archive in-place and append any new data, eliminating &quot;holes&quot;. In general, this option should <i>not</i> be used because a failed or interrupted compaction will corrupt the WIM archive. For more information, see the documentation for this option in <code>wimlib-imagex-optimize</code> (1).</dl>
<h2>SPLIT WIMS</h2>
<p> You may use <code>wimlib-imagex export</code> to export images from a split WIM. The <i>SRC_WIMFILE</i> argument must specify the first part of the split WIM, while the additional parts of the split WIM must be specified in one or more <code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot; options. Since globbing is built into the <code>&#8211;ref</code> option, typically only one <code>&#8211;ref</code> option is necessary. For example, the names for the split WIM parts usually go something like: </p>
<dl>
<dt>
<dd>
<pre>
mywim.swm
mywim2.swm
mywim3.swm
mywim4.swm
mywim5.swm
</dl>
To export the first image of this split WIM to a new or existing WIM file
&quot;other.wim&quot;, run:
<dl><dt><dd>wimlib-imagex export mywim.swm 1 other.wim --ref=&quot;mywim*.swm&quot;
</dl>
</pre>
<h2>NOTES</h2>
<p> <i>Data integrity</i>: Except when using <code>&#8211;unsafe-compact</code>, it is safe to abort a <code>wimlib-imagex export</code> command partway through. However, after doing this, it is recommended to run <code>wimlib-imagex optimize</code> on the destination WIM to remove any data that was appended to the physical WIM file but not yet incorporated into the structure of the WIM, unless the WIM was being rebuilt (e.g. with <code>&#8211;rebuild</code>), in which case you should delete the temporary file left over. </p>
<p> <i>Single instancing</i>: The WIM format uses single-instance streams (roughly, &quot;files&quot;). When an image is exported, only the streams (&quot;files&quot;) not already present in the destination WIM will be copied. However, a new copy of the image&#8217;s metadata resource, which describes the full directory structure, will always be created. </p>
<p> <i>ESD files</i>: wimlib v1.6.0 and later can export images from version 3584 WIMs, which usually contain LZMS-compressed solid resources and may carry the <i>.esd</i> file extension rather than <i>.wim</i>. However, <i>.esd</i> files downloaded directly by the Windows 8 web downloader have encrypted segments, and wimlib cannot export images from such files until they are first decrypted. In addition, to ensure the destination archive is created in the original WIM format rather than in the newer format, specify <code>&#8211;compress</code>=<i>LZX</i> (or <code>&#8211;compress</code>=<i>maximum</i>).</p>
<h2>EXAMPLES</h2>
<p> Export the second image of &#8216;boot.wim&#8217; to the new WIM file &#8216;new.wim&#8217;:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex export boot.wim 2 new.wim</dl>
<p> The above example creates &quot;new.wim&quot; with the same compression type as &quot;boot.wim&quot;. If you wish to change the compression type, specify <code>&#8211;compress</code>=<i>TYPE</i>; for example:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex export boot.wim 2 new.wim &#8211;compress=LZX</dl>
<p> Export &quot;ESD to WIM&quot; &#8212; that is, solid WIM to non-solid WIM:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex export install.esd all install.wim &#8211;compress=LZX</dl>
<p> Export &quot;WIM to ESD&quot; &#8212; that is, non-solid WIM to solid WIM:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex export install.wim all install.esd &#8211;solid</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-info/">wimlib-imagex-info</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-optimize/">wimlib-imagex-optimize</a></code>(1) </p>
<h2>Index</h2>
