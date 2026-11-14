---
title: "wimlib-imagex-optimize(1)"
name: "wimlib-imagex-optimize"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-optimize/"
description: "wimlib-imagex-optimize – Optimize a WIM archive"
---

<h2>NAME</h2>
<p> wimlib-imagex-optimize &#8211; Optimize a WIM archive</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex optimize</code> <i>WIMFILE</i> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex optimize</code> will rebuild the stand-alone WIM <i>WIMFILE</i>. The new WIM is written to a temporary file, and it is renamed to the original file when it&#8217;s ready. This action will remove any holes that have been left as a result of appending images, so the new WIM may be slightly smaller than the old WIM. </p>
<p> By default, compressed data will be re-used, and not recompressed. Use the <code>&#8211;recompress</code> or <code>&#8211;compress</code>=<i>TYPE</i>[:<i>LEVEL</i>] option to request recompression. </p>
<p> This command is also available as simply <code>wimoptimize</code> if the appropriate hard link or batch file has been installed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>WIMFILE</i>, verify its integrity if an integrity table is present. In addition, include an integrity table in the optimized WIM. If this option is not specified, by default the integrity table (if present) is not checked, and an integrity table is included in the rebuilt WIM if and only if one was present in the original WIM.</p>
<dt><code>&#8211;nocheck</code></p>
<dd> Neither verify the integrity of <i>WIMFILE</i> using the integrity table, nor include an integrity table in the rebuilt WIM file.</p>
<dt><code>&#8211;recompress</code></p>
<dd> Recompress all compressed streams in <i>WIMFILE</i> when rebuilding it. This will greatly increase the time needed to rebuild the WIM file, but it may result in a better compression ratio if wimlib can do a better job than the program that wrote the original file.</p>
<dt><code>&#8211;compress</code>=<i>TYPE</i>[:<i>LEVEL</i>]</p>
<dd> Recompress the WIM file using the specified compression type, and optionally the specified compression level for that compression type. This implies <code>&#8211;recompress</code>.</p>
<dt>
<dd> See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;chunk-size</code>=<i>SIZE</i></p>
<dd> Set the WIM compression chunk size to <i>SIZE</i>. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;solid</code></p>
<dd> Create a &quot;solid&quot; archive that compresses multiple files together. This can result in a higher compression ratio, but has disadvantages such as reduced compatibility. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;solid-chunk-size</code>=<i>SIZE</i></p>
<dd> Like <code>&#8211;chunk-size</code>, but set the chunk size used in solid resources. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;solid-compress</code>=<i>TYPE</i>[:<i>LEVEL</i>]</p>
<dd> Like <code>&#8211;compress</code>, but set the compression type used in solid resources. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details.</p>
<dt><code>&#8211;threads</code>=<i>NUM_THREADS</i></p>
<dd> Number of threads to use for compressing data. Default: autodetect (number of processors). This parameter only has an effect when data recompression is requested.</p>
<dt><code>&#8211;pipable</code></p>
<dd> Rebuild the WIM so that it can be applied fully sequentially, including from a pipe. See <code>wimlib-imagex <a href="/docs/linux/man/1-capture/">capture</a></code>(1) for more details about creating pipable WIMs. By default, when neither <code>&#8211;pipable</code> or <code>&#8211;not-pipable</code> is specified, the rebuilt WIM will be pipable if and only if it was already pipable.</p>
<dt><code>&#8211;not-pipable</code></p>
<dd> Rebuild the WIM in the non-pipable format. (This is the default if <i>WIMFILE</i> is not pipable.)</p>
<dt><code>&#8211;unsafe-compact</code></p>
<dd> Compact the WIM file in-place, without using a temporary file. Existing resources are shifted down to fill holes and new resources are appended as needed. The WIM file is truncated to its final size, which may shrink the on-disk file. THIS OPERATION CANNOT BE SAFELY INTERRUPTED! If the operation is interrupted, then the WIM file will be corrupted, and it may be impossible (or at least very difficult) to recover any data from it. Users of this option are expected to know what they are doing and assume responsibility for any data corruption that may result.</dl>
<h2>NOTES</h2>
<p> <code>wimlib-imagex optimize</code> does not support split WIMs. </p>
<p> <code>wimlib-imagex optimize</code> is roughly equivalent to:</p>
<dl>
<dt>
<dd>
<p> <code>wimlib-imagex export</code> <i>WIMFILE</i> all tmp.wim &amp;&amp; mv tmp.wim <i>WIMFILE</i></dl>
<h2>EXAMPLES</h2>
<p> Rebuild the WIM file &#8216;install.wim&#8217;:</p>
<dl>
<dt>
<dd>
<p> wimoptimize install.wim</dl>
<p> Rebuild and recompress the WIM file &#8216;install.wim&#8217;:</p>
<dl>
<dt>
<dd>
<p> wimoptimize install.wim &#8211;recompress</dl>
<p> Rebuild and recompress the WIM file &#8216;install.wim&#8217;, using LZX (&quot;maximum&quot;) compression at a higher-than-default compression level. The compression chunk size remains unchanged. This command will be slow, but it might be useful for optimizing files for distribution. See <i><a rel="nofollow" href="https://wimlib.net/compression.html">https://wimlib.net/compression.html</a></i> for some benchmark results.</p>
<dl>
<dt>
<dd>
<p> wimoptimize install.wim &#8211;compress=LZX:100</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-export/">wimlib-imagex-export</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-verify/">wimlib-imagex-verify</a></code>(1) </p>
<h2>Index</h2>
