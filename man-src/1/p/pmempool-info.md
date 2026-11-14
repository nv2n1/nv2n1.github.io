---
title: "pmempool-info(1)"
name: "pmempool-info"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmempool-info/"
description: "pmempool-info – Print basic information about Persistent Memory Pool file"
---

<h2>NAME</h2>
<p> pmempool-info &#8211; Print basic information about Persistent Memory Pool file</p>
<h2>SYNOPSIS</h2>
<p> <code>pmempool info</code> [&lt;options&gt;] &lt;file&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>pmempool</code> invoked with <code>info</code> command analyzes an existing pool created by <code>NVML</code> libraries. The main task of this command is to print all usable information from pool headers and user data in human readable format. It automatically recognizes pool type by parsing and analyzing pool header. The recognition is done by checking the signature in pool header. The main job of <code>info</code> command is to present internal data structures as they are stored in file but <i>not</i> for checking consistency. For this purpose there is the <code><a href="/docs/linux/man/1-pmempool-check/">pmempool-check</a>(1)</code> command available. </p>
<p> The <code>pmempool</code> with <code>info</code> command analyzes pool file as long as it is possible regarding <i>correctness</i> of internal meta-data (correct offsets, sizes etc.). If it is <i>not</i> possible to analyze the rest of the file, <code>pmempool</code> exits with error code and prints appropriate error message. </p>
<p> Currently there is lack of interprocess synchronization for pool files, so the <code>info</code> command should be invoked off-line. Using <code>pmempool</code> on pool file which may be modified by another process may lead to unexpected errors in pool file. </p>
<p> <code>pmempool info</code> opens pool file in <i>read-only</i> mode so the file will remain untouched after processing. </p>
<p> The <code>info</code> command may collect and print basic statistics about data usage. The statistics are specific to the type of pool. See <code>STATISTICS</code> section for details. </p>
<p> Although the pool consistency is <i>not</i> checked by the <code>info</code> command, it prints information about checksum errors and/or offsets errors. </p>
<h3>Common options:</h3>
<p> By default the <code>info</code> command of <code>pmempool</code> prints information about the most important internal data structures from pool. The particular set of headers and meta-data depend on pool type. The pool type is recognized automatically and appropriate information is displayed in human-readable format. </p>
<p> To force processing specified file(s) as desired pool type use <code>-f</code> option with appropriate name of pool type. The valid names off pool types are <i>blk ,</i> <i>log ,</i> <i>obj</i> or <i>btt.</i> This option may be useful when the pool header is corrupted and automatic recognition of pool type fails. </p>
<p> <code>-f, &#8211;force</code> blk|log|obj|btt</p>
<dl>
<dt>
<dd> Force parsing pool as specified pool type.</dl>
<p> By default only pool headers and internal meta-data are displayed. To display user data use <code>-d</code> option. Using <code>-r</code> option you can specify number of blocks/bytes/data chunks or objects using special text format. See <code>RANGE</code> section for details. The range refers to <i>block numbers</i> in case of pmem blk pool type, to <i>chunk numbers</i> in case of pmem log pool type and to <i>object numbers</i> in case of pmem obj pool type. See <code>EXAMPLES</code> section for an example of usage of these options. </p>
<p> <code>-d, &#8211;data</code></p>
<dl>
<dt>
<dd> Dump user data in hexadecimal format. In case of pmem <i>blk</i> pool type data is dumped in <i>blocks.</i> In case of pmem <i>log</i> pool type data is dumped as a whole or in <i>chunks</i> if <code>-w</code> option is used (See <code>Options for PMEMLOG</code> section for details).</dl>
<p> <code>-r, &#8211;range</code> &lt;range&gt;</p>
<dl>
<dt>
<dd> Range of blocks/data chunks/objects/zone headers/chunk headers/lanes. See <code>RANGE</code> section for details about range format.</dl>
<p> <code>-n, &#8211;human</code></p>
<dl>
<dt>
<dd> Print sizes in human-readable format with appropriate units (e.g. 4k, 8M, 16G).</dl>
<p> <code>-x, &#8211;headers-hex</code></p>
<dl>
<dt>
<dd> Print pool&#8217;s internal data in mixed format which consists of hexadecimal dump of header&#8217;s data and parsed format displayed in human-readable format. This allows to see how data is stored in file.</dl>
<p> <code>-s, &#8211;stats</code></p>
<dl>
<dt>
<dd> Print pool&#8217;s statistics. See <code>STATISTICS</code> section for details.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<h3>Options for PMEMLOG:</h3>
<p> <code>-w, &#8211;walk</code> &lt;size&gt;</p>
<dl>
<dt>
<dd> Use this option to walk through used data with fixed data chunk size. See <code>pmemlog_walk</code>() in <code><a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a>(3)</code> for details.</dl>
<h3>Options for PMEMBLK:</h3>
<p> By default the <code>info</code> command displays the pmem blk header and BTT (Block Translation Table) Info header in case of pmem blk pool type. </p>
<p> To display BTT Map and/or BTT FLOG (Free List and Log) use <code>-m</code> and <code>-g</code> options respectively or increase verbosity level. </p>
<p> In order to display BTT Info header backup use <code>-B</code> option. </p>
<p> <code>-m, &#8211;map</code></p>
<dl>
<dt>
<dd> Print BTT Map entries.</dl>
<p> <code>-g, &#8211;flog</code></p>
<dl>
<dt>
<dd> Print BTT FLOG entries.</dl>
<p> <code>-B, &#8211;backup</code></p>
<dl>
<dt>
<dd> Print BTT Info header backup.</dl>
<p> By default the <code>info</code> command displays all data blocks when <code>-d</code> options is used. However it is possible to skip blocks marked with <i>zero</i> and/or <i>error</i> flags. It is also possible to skip blocks which are <i>not</i> marked with any flag. Skipping blocks has impact on blocks ranges (e.g. display 10 blocks marked with error flag in the range from 0 to 10000) and statistics. </p>
<p> <code>-z, &#8211;skip-zeros</code></p>
<dl>
<dt>
<dd> Skip blocks marked with <i>zero</i> flag.</dl>
<p> <code>-e, &#8211;skip-error</code></p>
<dl>
<dt>
<dd> Skip blocks marked with <i>error</i> flag.</dl>
<p> <code>-u, &#8211;skip-no-flag</code></p>
<dl>
<dt>
<dd> Skip blocks <i>not</i> marked with any flag.</dl>
<h3>Options for PMEMOBJ:</h3>
<p> By default the <code>info</code> command displays pool header and <code>pmem obj</code> pool descriptor. In order to print information about other data structures one of the following options may be used. </p>
<p> <code>-l, &#8211;lanes [&lt;range&gt;]</code></p>
<dl>
<dt>
<dd> Print information about lanes. If range is not specified all lanes are displayed. The range can be specified using <code>-r</code> option right after the <code>-l</code> option. See <code>RANGE</code> section for details about range format.</dl>
<p> <code>-R, &#8211;recovery</code></p>
<dl>
<dt>
<dd> Print information about only those lanes which require recovery process. This option requires <code>-l, &#8211;lanes</code> option.</dl>
<p> <code>-S, &#8211;section tx,allocator,list</code></p>
<dl>
<dt>
<dd> Print information only about specified sections from lane. The section types may be separated by comma. This option requires <code>-l, &#8211;lanes</code> option.</dl>
<p> <code>-O, &#8211;object-store</code></p>
<dl>
<dt>
<dd> Print information about all allocated objects.</dl>
<p> <code>-t, &#8211;types &lt;range&gt;</code></p>
<dl>
<dt>
<dd> Print information about allocated objects only from specified range of type numbers. If <code>-s, &#8211;stats</code> option is specified the objects statistics refer to objects from specified range of type numbers. This option requires <code>-O, &#8211;object-store</code> or <code>-s, &#8211;stats</code> options. See <code>RANGE</code> section for details about range format.</dl>
<p> <code>-E, &#8211;no-empty</code></p>
<dl>
<dt>
<dd> Ignore empty lists of objects. This option requires <code>-O, &#8211;object-store</code> option.</dl>
<p> <code>-o, &#8211;root</code></p>
<dl>
<dt>
<dd> Print information about a root object.</dl>
<p> <code>-A, &#8211;alloc-header</code></p>
<dl>
<dt>
<dd> Print object&#8217;s allocation header. This option requires <code>-O, &#8211;object-store</code> or <code>-l, &#8211;lanes</code> or <code>-o, &#8211;root</code> options. <code></dl>
<p> </code> </p>
<p> <code>-a, &#8211;oob-header</code></p>
<dl>
<dt>
<dd> Print object&#8217;s out of band header. This option requires <code>-O, &#8211;object-store</code> or <code>-l, &#8211;lanes</code> or <code>-o, &#8211;root</code> options. <code></dl>
<p> </code> </p>
<p> <code>-H, &#8211;heap</code></p>
<dl>
<dt>
<dd> Print information about <code>pmemobj</code> heap. By default only a heap header is displayed.</dl>
<p> <code>-Z, &#8211;zones</code></p>
<dl>
<dt>
<dd> If the <code>-H, &#8211;heap</code> option is used, print information about zones from specified range. If the <code>-O, &#8211;object-store</code> option is used, print information about objects only from specified range of zones. This option requires <code>-O, &#8211;object-store</code> , <code>-H, &#8211;heap</code> or <code>-s, &#8211;stats</code> options. The range can be specified using <code>-r</code> option right after the <code>-Z</code> option. See <code>RANGE</code> section for details about range format.</dl>
<p> <code>-C, &#8211;chunks [&lt;range&gt;]</code></p>
<dl>
<dt>
<dd> If the <code>-H, &#8211;heap</code> option is used, print information about chunks from specified range. By default information about chunks of types <code>used ,</code> <code>free</code> and <code>run</code> are displayed. If the <code>-O, &#8211;object-store</code> option is used, print information about objects from specified range of chunks within a zone. This option requires <code>-O, &#8211;object-store</code> , <code>-H, &#8211;heap</code> or <code>-s, &#8211;stats</code> options. The range can be specified using <code>-r</code> option right after the <code>-C</code> option. See <code>RANGE</code> section for details about range format.</dl>
<p> <code>-T, &#8211;chunk-type used,free,run,footer</code></p>
<dl>
<dt>
<dd> Print only specified type(s) of chunks. The multiple types may be specified separated by comma. This option requires <code>-H, &#8211;heap</code> and <code>-C, &#8211;chunks</code> options.</dl>
<p> <code>-b, &#8211;bitmap</code></p>
<dl>
<dt>
<dd> Print bitmap of used blocks in chunks of type run. This option requires <code>-H, &#8211;heap</code> and <code>-C, &#8211;chunks</code> options.</dl>
<p> <code>-p, &#8211;replica &lt;num&gt;</code></p>
<dl>
<dt>
<dd> Print information from <code>&lt;num&gt;</code> replica. The 0 value means the master pool file.</dl>
<h2>RANGE</h2>
<p> Using <code>-r, &#8211;range</code> option it is possible to dump only a range of user data. This section describes valid format of <i>&lt;range&gt;</i> string. </p>
<p> You can specify multiple ranges separated by commas. </p>
<p> <code>&lt;first&gt;-&lt;last&gt;</code></p>
<dl>
<dt>
<dd> All blocks/bytes/data chunks from <code>&lt;first&gt;</code> to <code>&lt;last&gt;</code> will be dumped.</dl>
<p> <code>-&lt;last&gt;</code></p>
<dl>
<dt>
<dd> All blocks/bytes/data chunks up to <code>&lt;last&gt;</code> will be dumped.</dl>
<p> <code>&lt;first&gt;-</code></p>
<dl>
<dt>
<dd> All blocks/bytes/data chunks starting from <code>&lt;first&gt;</code> will be dumped.</dl>
<p> <code>&lt;number&gt;</code></p>
<dl>
<dt>
<dd> Only <code>&lt;number&gt;</code> block/byte/data chunk will be dumped.</dl>
<h2>STATISTICS</h2>
<p> Below is the description of statistical measures for specific pool types.</p>
<h3>PMEMLOG</h3>
<dl>
<dt><code>Total</code></p>
<dd> Total space in pool.</p>
<dt><code>Available</code></p>
<dd> Size and percentage of available space.</p>
<dt><code>Used</code></p>
<dd> Size and percentage of used space.</dl>
<h3>PMEMBLK</h3>
<dl>
<dt><code>Total blocks</code></p>
<dd> Total number of blocks in pool.</p>
<dt><code>Zeroed blocks</code></p>
<dd> Number and percentage of blocks marked with <i>zero</i> flag.</p>
<dt><code>Error blocks</code></p>
<dd> Number and percentage of blocks marked with <i>error</i> flag.</p>
<dt><code>Blocks without any flag</code></p>
<dd> Number and percentage of blocks <i>not</i> marked with any flag.</p>
<dt><code>NOTE:</code></p>
<dd> In case of pmemblk, statistics are evaluated for blocks which meet requirements regarding:</dl>
<p> <i>range</i> of blocks ( <code>-r</code> option), </p>
<p> <i>skipped</i> types of blocks ( <code>-z, -e, -u</code> options).</p>
<h3>PMEMOBJ</h3>
<dl>
<dt><code>Object store</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Number of objects</code></p>
<dd> Total number of objects and number of objects per type number.</p>
<dt><code>Number of bytes</code></p>
<dd> Total number of bytes and number of bytes per type number.</dl>
</dl>
<dt><code>Heap</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Number of zones</code></p>
<dd> Total number of zones in the pool.</p>
<dt><code>Number of used zones</code></p>
<dd> Number of used zones in the pool.</dl>
</dl>
<dt><code>Zone</code></p>
<dd> The zone&#8217;s statistics are presented for each zone separately and the aggregated results from all zones.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Number of chunks</code></p>
<dd> Total number of chunks in the zone and number of chunks of specified type.</p>
<dt><code>Chunks size</code></p>
<dd> Total size of all chunks in the zone and sum of sizes of chunks of specified type.</dl>
</dl>
<dt><code>Allocation classes</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Units</code></p>
<dd> Total number of units of specified class.</p>
<dt><code>Used units</code></p>
<dd> Number of used units of specified class.</p>
<dt><code>Bytes</code></p>
<dd> Total number of bytes of specified class.</p>
<dt><code>Used bytes</code></p>
<dd> Number of used bytes of specified class.</p>
<dt><code>Total bytes</code></p>
<dd> Total number of bytes of all classes.</p>
<dt><code>Total used bytes</code></p>
<dd> Total number of used bytes of all classes.</dl>
</dl>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pmempool info ./pmemblk</p>
<dd> # Parse and print information about pmem blk file.</p>
<dt>pmempool info -f blk ./pmemblk</p>
<dd> # Force parsing pmemblk file as PMEM BLK pool type.</p>
<dt>pmempool info -d ./pmemlog</p>
<dd> # Print information and data in hexadecimal dump format for file pmem log.</p>
<dt>pmempool info -d -r10-100 -eu ./pmemblk</p>
<dd> # Print information from pmemblk file. Dump data blocks from 10 to 100, skip blocks marked with error flag and not marked with any flag.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libpmemblk/">libpmemblk</a>(3) <a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a>(3) <a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code></p>
<h2>PMEMPOOL</h2>
<p> Part of the <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code> suite. </p>
<h2>Index</h2>
