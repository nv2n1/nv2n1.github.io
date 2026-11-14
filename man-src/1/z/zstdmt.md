---
title: "zstdmt(1)"
name: "zstdmt"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zstdmt/"
description: "zstd – zstd, zstdmt, unzstd, zstdcat – Compress or decompress .zst files"
---

<h2 class="name">NAME</h2>
<p> <code>zstd</code> &#8211; zstd, zstdmt, unzstd, zstdcat &#8211; Compress or decompress .zst files </p>
<h2>SYNOPSIS</h2>
<p> <code>zstd</code> [<i>OPTIONS</i>] [-|<i>INPUT-FILE</i>] [-o <i>OUTPUT-FILE</i>] </p>
<p> <code>zstdmt</code> is equivalent to <code>zstd -T0</code> </p>
<p> <code>unzstd</code> is equivalent to <code>zstd -d</code> </p>
<p> <code>zstdcat</code> is equivalent to <code>zstd -dcf</code></p>
<h2>DESCRIPTION</h2>
<p> <code>zstd</code> is a fast lossless compression algorithm and data compression tool, with command line syntax similar to <code>gzip (1)</code> and <code>xz (1)</code>. It is based on the <code>LZ77</code> family, with further FSE &amp; huff0 entropy stages. <code>zstd</code> offers highly configurable compression speed, with fast modes at &gt; 200 MB/s per core, and strong modes nearing lzma compression ratios. It also features a very fast decoder, with speeds &gt; 500 MB/s per core. </p>
<p> <code>zstd</code> command line syntax is generally similar to gzip, but features the following differences :</p>
<dl>
<dt>&bull;</p>
<dd> Source files are preserved by default. It&#8217;s possible to remove them automatically by using the <code>&#8211;rm</code> command.</p>
<dt>&bull;</p>
<dd> When compressing a single file, <code>zstd</code> displays progress notifications and result summary by default. Use <code>-q</code> to turn them off.</p>
<dt>&bull;</p>
<dd> <code>zstd</code> does not accept input from console, but it properly accepts <code>stdin</code> when it&#8217;s not the console.</p>
<dt>&bull;</p>
<dd> <code>zstd</code> displays a short help page when command line is an error. Use <code>-q</code> to turn it off.</p>
<dt>
<dd></dl>
<p> <code>zstd</code> compresses or decompresses each <i>file</i> according to the selected operation mode. If no <i>files</i> are given or <i>file</i> is <code>&#8211;</code>, <code>zstd</code> reads from standard input and writes the processed data to standard output. <code>zstd</code> will refuse to write compressed data to standard output if it is a terminal : it will display an error message and skip the <i>file</i>. Similarly, <code>zstd</code> will refuse to read compressed data from standard input if it is a terminal. </p>
<p> Unless <code>&#8211;stdout</code> or <code>-o</code> is specified, <i>files</i> are written to a new file whose name is derived from the source <i>file</i> name:</p>
<dl>
<dt>&bull;</p>
<dd> When compressing, the suffix <code>.zst</code> is appended to the source filename to get the target filename.</p>
<dt>&bull;</p>
<dd> When decompressing, the <code>.zst</code> suffix is removed from the source filename to get the target filename</p>
<dt>
<dd></dl>
<h3>Concatenation with .zst files</h3>
<p> It is possible to concatenate <code>.zst</code> files as is. <code>zstd</code> will decompress such files as if they were a single <code>.zst</code> file.</p>
<h2>OPTIONS</h2>
<h3>Integer suffixes and special values</h3>
<p> In most places where an integer argument is expected, an optional suffix is supported to easily indicate large integers. There must be no space between the integer and the suffix.</p>
<dl>
<dt><code>KiB</code></p>
<dd> Multiply the integer by 1,024 (2^10). <code>Ki</code>, <code>K</code>, and <code>KB</code> are accepted as synonyms for <code>KiB</code>.</p>
<dt><code>MiB</code></p>
<dd> Multiply the integer by 1,048,576 (2^20). <code>Mi</code>, <code>M</code>, and <code>MB</code> are accepted as synonyms for <code>MiB</code>.</dl>
<h3>Operation mode</h3>
<p> If multiple operation mode options are given, the last one takes effect.</p>
<dl>
<dt><code>-z</code>, <code>&#8211;compress</code></p>
<dd> Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the command name (for example, <code>unzstd</code> implies <code>&#8211;decompress</code>).</p>
<dt><code>-d</code>, <code>&#8211;decompress</code>, <code>&#8211;uncompress</code></p>
<dd> Decompress.</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> Test the integrity of compressed <i>files</i>. This option is equivalent to <code>&#8211;decompress &#8211;stdout</code> except that the decompressed data is discarded instead of being written to standard output. No files are created or removed.</p>
<dt><code>-b#</code></p>
<dd> Benchmark file(s) using compression level #</p>
<dt><code>&#8211;train FILEs</code></p>
<dd> Use FILEs as a training set to create a dictionary. The training set should contain a lot of small files (&gt; 100).</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> Display information related to a zstd compressed file, such as size, ratio, and checksum. Some of these fields may not be available. This command can be augmented with the <code>-v</code> modifier.</dl>
<h3>Operation modifiers</h3>
<dl>
<dt>&bull;</p>
<dd> <code>-#</code>: <code>#</code> compression level [1-19] (default: 3)</p>
<dt>&bull;</p>
<dd> <code>&#8211;ultra</code>: unlocks high compression levels 20+ (maximum 22), using a lot more memory. Note that decompression will also require more memory when using these levels.</p>
<dt>&bull;</p>
<dd> <code>&#8211;fast[=#]</code>: switch to ultra-fast compression levels. If <code>=#</code> is not present, it defaults to <code>1</code>. The higher the value, the faster the compression speed, at the cost of some compression ratio. This setting overwrites compression level if one was set previously. Similarly, if a compression level is set after <code>&#8211;fast</code>, it overrides it.</p>
<dt>&bull;</p>
<dd> <code>-T#</code>, <code>&#8211;threads=#</code>: Compress using <code>#</code> working threads (default: 1). If <code>#</code> is 0, attempt to detect and use the number of physical CPU cores. In all cases, the nb of threads is capped to ZSTDMT_NBWORKERS_MAX==200. This modifier does nothing if <code>zstd</code> is compiled without multithread support.</p>
<dt>&bull;</p>
<dd> <code>&#8211;single-thread</code>: Does not spawn a thread for compression, use a single thread for both I/O and compression. In this mode, compression is serialized with I/O, which is slightly slower. (This is different from <code>-T1</code>, which spawns 1 compression thread in parallel of I/O). This mode is the only one available when multithread support is disabled. Single-thread mode features lower memory usage. Final compressed result is slightly different from <code>-T1</code>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;adapt[=min=#,max=#]</code> : <code>zstd</code> will dynamically adapt compression level to perceived I/O conditions. Compression level adaptation can be observed live by using command <code>-v</code>. Adaptation can be constrained between supplied <code>min</code> and <code>max</code> levels. The feature works when combined with multi-threading and <code>&#8211;long</code> mode. It does not work with <code>&#8211;single-thread</code>. It sets window size to 8 MB by default (can be changed manually, see <code>wlog</code>). Due to the chaotic nature of dynamic adaptation, compressed result is not reproducible. <i>note</i> : at the time of this writing, <code>&#8211;adapt</code> can remain stuck at low speed when combined with multiple worker threads (&gt;=2).</p>
<dt>&bull;</p>
<dd> <code>&#8211;long[=#]</code>: enables long distance matching with <code>#</code> <code>windowLog</code>, if not <code>#</code> is not present it defaults to <code>27</code>. This increases the window size (<code>windowLog</code>) and memory usage for both the compressor and decompressor. This setting is designed to improve the compression ratio for files with long matches at a large distance.</p>
<dt>
<dd> Note: If <code>windowLog</code> is set to larger than 27, <code>&#8211;long=windowLog</code> or <code>&#8211;memory=windowSize</code> needs to be passed to the decompressor.</p>
<dt>&bull;</p>
<dd> <code>-D DICT</code>: use <code>DICT</code> as Dictionary to compress or decompress FILE(s)</p>
<dt>&bull;</p>
<dd> <code>&#8211;patch-from FILE</code>: Specify the file to be used as a reference point for zstd&#8217;s diff engine. This is effectively dictionary compression with some convenient parameter selection, namely that windowSize &gt; srcSize.</p>
<dt>
<dd> Note: cannot use both this and -D together Note: <code>&#8211;long</code> mode will be automatically activated if chainLog &lt; fileLog (fileLog being the windowLog required to cover the whole file). You can also manually force it. Node: for all levels, you can use &#8211;patch-from in &#8211;single-thread mode to improve compression ratio at the cost of speed Note: for level 19, you can get increased compression ratio at the cost of speed by specifying <code>&#8211;zstd=targetLength=</code> to be something large (i.e 4096), and by setting a large <code>&#8211;zstd=chainLog=</code></p>
<dt>&bull;</p>
<dd> <code>&#8211;rsyncable</code> : <code>zstd</code> will periodically synchronize the compression state to make the compressed file more rsync-friendly. There is a negligible impact to compression ratio, and the faster compression levels will see a small compression speed hit. This feature does not work with <code>&#8211;single-thread</code>. You probably don&#8217;t want to use it with long range mode, since it will decrease the effectiveness of the synchronization points, but your milage may vary.</p>
<dt>&bull;</p>
<dd> <code>-C</code>, <code>&#8211;[no-]check</code>: add integrity check computed from uncompressed data (default: enabled)</p>
<dt>&bull;</p>
<dd> <code>&#8211;[no-]content-size</code>: enable / disable whether or not the original size of the file is placed in the header of the compressed file. The default option is &#8211;content-size (meaning that the original size will be placed in the header).</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-dictID</code>: do not store dictionary ID within frame header (dictionary compression). The decoder will have to rely on implicit knowledge about which dictionary to use, it won&#8217;t be able to check if it&#8217;s correct.</p>
<dt>&bull;</p>
<dd> <code>-M#</code>, <code>&#8211;memory=#</code>: Set a memory usage limit. By default, Zstandard uses 128 MB for decompression as the maximum amount of memory the decompressor is allowed to use, but you can override this manually if need be in either direction (ie. you can increase or decrease it).</p>
<dt>
<dd> This is also used during compression when using with &#8211;patch-from=. In this case, this parameter overrides that maximum size allowed for a dictionary. (128 MB).</p>
<dt>&bull;</p>
<dd> <code>&#8211;stream-size=#</code> : Sets the pledged source size of input coming from a stream. This value must be exact, as it will be included in the produced frame header. Incorrect stream sizes will cause an error. This information will be used to better optimize compression parameters, resulting in better and potentially faster compression, especially for smaller source sizes.</p>
<dt>&bull;</p>
<dd> <code>&#8211;size-hint=#</code>: When handling input from a stream, <code>zstd</code> must guess how large the source size will be when optimizing compression parameters. If the stream size is relatively small, this guess may be a poor one, resulting in a higher compression ratio than expected. This feature allows for controlling the guess when needed. Exact guesses result in better compression ratios. Overestimates result in slightly degraded compression ratios, while underestimates may result in significant degradation.</p>
<dt>&bull;</p>
<dd> <code>-o FILE</code>: save result into <code>FILE</code></p>
<dt>&bull;</p>
<dd> <code>-f</code>, <code>&#8211;force</code>: overwrite output without prompting, and (de)compress symbolic links</p>
<dt>&bull;</p>
<dd> <code>-c</code>, <code>&#8211;stdout</code>: force write to standard output, even if it is the console</p>
<dt>&bull;</p>
<dd> <code>&#8211;[no-]sparse</code>: enable / disable sparse FS support, to make files with many zeroes smaller on disk. Creating sparse files may save disk space and speed up decompression by reducing the amount of disk I/O. default: enabled when output is into a file, and disabled when output is stdout. This setting overrides default and can force sparse mode over stdout.</p>
<dt>&bull;</p>
<dd> <code>&#8211;rm</code>: remove source file(s) after successful compression or decompression. If used in combination with -o, will trigger a confirmation prompt (which can be silenced with -f), as this is a destructive operation.</p>
<dt>&bull;</p>
<dd> <code>-k</code>, <code>&#8211;keep</code>: keep source file(s) after successful compression or decompression. This is the default behavior.</p>
<dt>&bull;</p>
<dd> <code>-r</code>: operate recursively on directories</p>
<dt>&bull;</p>
<dd> <code>&#8211;filelist FILE</code> read a list of files to process as content from <code>FILE</code>. Format is compatible with <code>ls</code> output, with one file per line.</p>
<dt>&bull;</p>
<dd> <code>&#8211;output-dir-flat DIR</code>: resulting files are stored into target <code>DIR</code> directory, instead of same directory as origin file. Be aware that this command can introduce name collision issues, if multiple files, from different directories, end up having the same name. Collision resolution ensures first file with a given name will be present in <code>DIR</code>, while in combination with <code>-f</code>, the last file will be present instead.</p>
<dt>&bull;</p>
<dd> <code>&#8211;output-dir-mirror DIR</code>: similar to <code>&#8211;output-dir-flat</code>, the output files are stored underneath target <code>DIR</code> directory, but this option will replicate input directory hierarchy into output <code>DIR</code>.</p>
<dt>
<dd> If input directory contains &quot;..&quot;, the files in this directory will be ignored. If input directory is an absolute directory (i.e. &quot;/var/tmp/abc&quot;), it will be stored into the &quot;output-dir/var/tmp/abc&quot;. If there are multiple input files or directories, name collision resolution will follow the same rules as <code>&#8211;output-dir-flat</code>.</p>
<dt>&bull;</p>
<dd> <code>&#8211;format=FORMAT</code>: compress and decompress in other formats. If compiled with support, zstd can compress to or decompress from other compression algorithm formats. Possibly available options are <code>zstd</code>, <code>gzip</code>, <code>xz</code>, <code>lzma</code>, and <code>lz4</code>. If no such format is provided, <code>zstd</code> is the default.</p>
<dt>&bull;</p>
<dd> <code>-h</code>/<code>-H</code>, <code>&#8211;help</code>: display help/long help and exit</p>
<dt>&bull;</p>
<dd> <code>-V</code>, <code>&#8211;version</code>: display version number and exit. Advanced : <code>-vV</code> also displays supported formats. <code>-vvV</code> also displays POSIX support. <code>-q</code> will only display the version number, suitable for machine reading.</p>
<dt>&bull;</p>
<dd> <code>-v</code>, <code>&#8211;verbose</code>: verbose mode, display more information</p>
<dt>&bull;</p>
<dd> <code>-q</code>, <code>&#8211;quiet</code>: suppress warnings, interactivity, and notifications. specify twice to suppress errors too.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-progress</code>: do not display the progress bar, but keep all other messages.</p>
<dt>&bull;</p>
<dd> <code>&#8211;show-default-cparams</code>: Shows the default compression parameters that will be used for a particular src file. If the provided src file is not a regular file (eg. named pipe), the cli will just output the default parameters. That is, the parameters that are used when the src size is unknown.</p>
<dt>&bull;</p>
<dd> <code>&#8212;</code>: All arguments after <code>&#8212;</code> are treated as files</p>
<dt>
<dd></dl>
<h3>Restricted usage of Environment Variables</h3>
<p> Using environment variables to set parameters has security implications. Therefore, this avenue is intentionally restricted. Only <code>ZSTD_CLEVEL</code> and <code>ZSTD_NBTHREADS</code> are currently supported. They set the compression level and number of threads to use during compression, respectively. </p>
<p> <code>ZSTD_CLEVEL</code> can be used to set the level between 1 and 19 (the &quot;normal&quot; range). If the value of <code>ZSTD_CLEVEL</code> is not a valid integer, it will be ignored with a warning message. <code>ZSTD_CLEVEL</code> just replaces the default compression level (<code>3</code>). </p>
<p> <code>ZSTD_NBTHREADS</code> can be used to set the number of threads <code>zstd</code> will attempt to use during compression. If the value of <code>ZSTD_NBTHREADS</code> is not a valid unsigned integer, it will be ignored with a warning message. &#8216;ZSTD_NBTHREADS<code>has a default value of (</code>1<code>), and is capped at ZSTDMT_NBWORKERS_MAX==200.</code>zstd` must be compiled with multithread support for this to have any effect. </p>
<p> They can both be overridden by corresponding command line arguments: <code>-#</code> for compression level and <code>-T#</code> for number of compression threads.</p>
<h2>DICTIONARY BUILDER</h2>
<p> <code>zstd</code> offers <i>dictionary</i> compression, which greatly improves efficiency on small files and messages. It&#8217;s possible to train <code>zstd</code> with a set of samples, the result of which is saved into a file called a <code>dictionary</code>. Then during compression and decompression, reference the same dictionary, using command <code>-D dictionaryFileName</code>. Compression of small files similar to the sample set will be greatly improved.</p>
<dl>
<dt><code>&#8211;train FILEs</code></p>
<dd> Use FILEs as training set to create a dictionary. The training set should contain a lot of small files (&gt; 100), and weight typically 100x the target dictionary size (for example, 10 MB for a 100 KB dictionary).</p>
<dt>
<dd> Supports multithreading if <code>zstd</code> is compiled with threading support. Additional parameters can be specified with <code>&#8211;train-fastcover</code>. The legacy dictionary builder can be accessed with <code>&#8211;train-legacy</code>. The cover dictionary builder can be accessed with <code>&#8211;train-cover</code>. Equivalent to <code>&#8211;train-fastcover=d=8,steps=4</code>.</p>
<dt><code>-o file</code></p>
<dd> Dictionary saved into <code>file</code> (default name: dictionary).</p>
<dt><code>&#8211;maxdict=#</code></p>
<dd> Limit dictionary to specified size (default: 112640).</p>
<dt><code>-#</code></p>
<dd> Use <code>#</code> compression level during training (optional). Will generate statistics more tuned for selected compression level, resulting in a <i>small</i> compression ratio improvement for this level.</p>
<dt><code>-B#</code></p>
<dd> Split input files in blocks of size # (default: no split)</p>
<dt><code>&#8211;dictID=#</code></p>
<dd> A dictionary ID is a locally unique ID that a decoder can use to verify it is using the right dictionary. By default, zstd will create a 4-bytes random number ID. It&#8217;s possible to give a precise number instead. Short numbers have an advantage : an ID &lt; 256 will only need 1 byte in the compressed frame header, and an ID &lt; 65536 will only need 2 bytes. This compares favorably to 4 bytes default. However, it&#8217;s up to the dictionary manager to not assign twice the same ID to 2 different dictionaries.</p>
<dt><code>&#8211;train-cover[=k#,d=#,steps=#,split=#,shrink[=#]]</code></p>
<dd> Select parameters for the default dictionary builder algorithm named cover. If <i>d</i> is not specified, then it tries <i>d</i> = 6 and <i>d</i> = 8. If <i>k</i> is not specified, then it tries <i>steps</i> values in the range [50, 2000]. If <i>steps</i> is not specified, then the default value of 40 is used. If <i>split</i> is not specified or split &lt;= 0, then the default value of 100 is used. Requires that <i>d</i> &lt;= <i>k</i>. If <i>shrink</i> flag is not used, then the default value for <i>shrinkDict</i> of 0 is used. If <i>shrink</i> is not specified, then the default value for <i>shrinkDictMaxRegression</i> of 1 is used.</p>
<dt>
<dd> Selects segments of size <i>k</i> with highest score to put in the dictionary. The score of a segment is computed by the sum of the frequencies of all the subsegments of size <i>d</i>. Generally <i>d</i> should be in the range [6, 8], occasionally up to 16, but the algorithm will run faster with d &lt;= <i>8</i>. Good values for <i>k</i> vary widely based on the input data, but a safe range is [2 * <i>d</i>, 2000]. If <i>split</i> is 100, all input samples are used for both training and testing to find optimal <i>d</i> and <i>k</i> to build dictionary. Supports multithreading if <code>zstd</code> is compiled with threading support. Having <i>shrink</i> enabled takes a truncated dictionary of minimum size and doubles in size until compression ratio of the truncated dictionary is at most <i>shrinkDictMaxRegression%</i> worse than the compression ratio of the largest dictionary.</p>
<dt>
<dd> Examples:</p>
<dt>
<dd> <code>zstd &#8211;train-cover FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-cover=k=50,d=8 FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-cover=d=8,steps=500 FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-cover=k=50 FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-cover=k=50,split=60 FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-cover=shrink FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-cover=shrink=2 FILEs</code></p>
<dt><code>&#8211;train-fastcover[=k#,d=#,f=#,steps=#,split=#,accel=#]</code></p>
<dd> Same as cover but with extra parameters <i>f</i> and <i>accel</i> and different default value of split If <i>split</i> is not specified, then it tries <i>split</i> = 75. If <i>f</i> is not specified, then it tries <i>f</i> = 20. Requires that 0 &lt; <i>f</i> &lt; 32. If <i>accel</i> is not specified, then it tries <i>accel</i> = 1. Requires that 0 &lt; <i>accel</i> &lt;= 10. Requires that <i>d</i> = 6 or <i>d</i> = 8.</p>
<dt>
<dd> <i>f</i> is log of size of array that keeps track of frequency of subsegments of size <i>d</i>. The subsegment is hashed to an index in the range [0,2^<i>f</i> &#8211; 1]. It is possible that 2 different subsegments are hashed to the same index, and they are considered as the same subsegment when computing frequency. Using a higher <i>f</i> reduces collision but takes longer.</p>
<dt>
<dd> Examples:</p>
<dt>
<dd> <code>zstd &#8211;train-fastcover FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-fastcover=d=8,f=15,accel=2 FILEs</code></p>
<dt><code>&#8211;train-legacy[=selectivity=#]</code></p>
<dd> Use legacy dictionary builder algorithm with the given dictionary <i>selectivity</i> (default: 9). The smaller the <i>selectivity</i> value, the denser the dictionary, improving its efficiency but reducing its possible maximum size. <code>&#8211;train-legacy=s=#</code> is also accepted.</p>
<dt>
<dd> Examples:</p>
<dt>
<dd> <code>zstd &#8211;train-legacy FILEs</code></p>
<dt>
<dd> <code>zstd &#8211;train-legacy=selectivity=8 FILEs</code></dl>
<h2>BENCHMARK</h2>
<dl>
<dt><code>-b#</code></p>
<dd> benchmark file(s) using compression level #</p>
<dt><code>-e#</code></p>
<dd> benchmark file(s) using multiple compression levels, from <code>-b#</code> to <code>-e#</code> (inclusive)</p>
<dt><code>-i#</code></p>
<dd> minimum evaluation time, in seconds (default: 3s), benchmark mode only</p>
<dt><code>-B#</code>, <code>&#8211;block-size=#</code></p>
<dd> cut file(s) into independent blocks of size # (default: no block)</p>
<dt><code>&#8211;priority=rt</code></p>
<dd> set process priority to real-time</dl>
<p> <code>Output Format:</code> CompressionLevel#Filename : IntputSize -&gt; OutputSize (CompressionRatio), CompressionSpeed, DecompressionSpeed </p>
<p> <code>Methodology:</code> For both compression and decompression speed, the entire input is compressed/decompressed in-memory to measure speed. A run lasts at least 1 sec, so when files are small, they are compressed/decompressed several times per run, in order to improve measurement accuracy.</p>
<h2>ADVANCED COMPRESSION OPTIONS</h2>
<h3>&#8211;zstd[=options]:</h3>
<p> <code>zstd</code> provides 22 predefined compression levels. The selected or default predefined compression level can be changed with advanced compression options. The <i>options</i> are provided as a comma-separated list. You may specify only the options you want to change and the rest will be taken from the selected or default compression level. The list of available <i>options</i>:</p>
<dl>
<dt><code>strategy</code>=<i>strat</i>, <code>strat</code>=<i>strat</i></p>
<dd> Specify a strategy used by a match finder.</p>
<dt>
<dd> There are 9 strategies numbered from 1 to 9, from faster to stronger: 1=ZSTD_fast, 2=ZSTD_dfast, 3=ZSTD_greedy, 4=ZSTD_lazy, 5=ZSTD_lazy2, 6=ZSTD_btlazy2, 7=ZSTD_btopt, 8=ZSTD_btultra, 9=ZSTD_btultra2.</p>
<dt><code>windowLog</code>=<i>wlog</i>, <code>wlog</code>=<i>wlog</i></p>
<dd> Specify the maximum number of bits for a match distance.</p>
<dt>
<dd> The higher number of increases the chance to find a match which usually improves compression ratio. It also increases memory requirements for the compressor and decompressor. The minimum <i>wlog</i> is 10 (1 KiB) and the maximum is 30 (1 GiB) on 32-bit platforms and 31 (2 GiB) on 64-bit platforms.</p>
<dt>
<dd> Note: If <code>windowLog</code> is set to larger than 27, <code>&#8211;long=windowLog</code> or <code>&#8211;memory=windowSize</code> needs to be passed to the decompressor.</p>
<dt><code>hashLog</code>=<i>hlog</i>, <code>hlog</code>=<i>hlog</i></p>
<dd> Specify the maximum number of bits for a hash table.</p>
<dt>
<dd> Bigger hash tables cause less collisions which usually makes compression faster, but requires more memory during compression.</p>
<dt>
<dd> The minimum <i>hlog</i> is 6 (64 B) and the maximum is 30 (1 GiB).</p>
<dt><code>chainLog</code>=<i>clog</i>, <code>clog</code>=<i>clog</i></p>
<dd> Specify the maximum number of bits for a hash chain or a binary tree.</p>
<dt>
<dd> Higher numbers of bits increases the chance to find a match which usually improves compression ratio. It also slows down compression speed and increases memory requirements for compression. This option is ignored for the ZSTD_fast strategy.</p>
<dt>
<dd> The minimum <i>clog</i> is 6 (64 B) and the maximum is 29 (524 Mib) on 32-bit platforms and 30 (1 Gib) on 64-bit platforms.</p>
<dt><code>searchLog</code>=<i>slog</i>, <code>slog</code>=<i>slog</i></p>
<dd> Specify the maximum number of searches in a hash chain or a binary tree using logarithmic scale.</p>
<dt>
<dd> More searches increases the chance to find a match which usually increases compression ratio but decreases compression speed.</p>
<dt>
<dd> The minimum <i>slog</i> is 1 and the maximum is &#8216;windowLog&#8217; &#8211; 1.</p>
<dt><code>minMatch</code>=<i>mml</i>, <code>mml</code>=<i>mml</i></p>
<dd> Specify the minimum searched length of a match in a hash table.</p>
<dt>
<dd> Larger search lengths usually decrease compression ratio but improve decompression speed.</p>
<dt>
<dd> The minimum <i>mml</i> is 3 and the maximum is 7.</p>
<dt><code>targetLength</code>=<i>tlen</i>, <code>tlen</code>=<i>tlen</i></p>
<dd> The impact of this field vary depending on selected strategy.</p>
<dt>
<dd> For ZSTD_btopt, ZSTD_btultra and ZSTD_btultra2, it specifies the minimum match length that causes match finder to stop searching. A larger <code>targetLength</code> usually improves compression ratio but decreases compression speed. t For ZSTD_fast, it triggers ultra-fast mode when &gt; 0. The value represents the amount of data skipped between match sampling. Impact is reversed : a larger <code>targetLength</code> increases compression speed but decreases compression ratio.</p>
<dt>
<dd> For all other strategies, this field has no impact.</p>
<dt>
<dd> The minimum <i>tlen</i> is 0 and the maximum is 128 Kib.</p>
<dt><code>overlapLog</code>=<i>ovlog</i>, <code>ovlog</code>=<i>ovlog</i></p>
<dd> Determine <code>overlapSize</code>, amount of data reloaded from previous job. This parameter is only available when multithreading is enabled. Reloading more data improves compression ratio, but decreases speed.</p>
<dt>
<dd> The minimum <i>ovlog</i> is 0, and the maximum is 9. 1 means &quot;no overlap&quot;, hence completely independent jobs. 9 means &quot;full overlap&quot;, meaning up to <code>windowSize</code> is reloaded from previous job. Reducing <i>ovlog</i> by 1 reduces the reloaded amount by a factor 2. For example, 8 means &quot;windowSize/2&quot;, and 6 means &quot;windowSize/8&quot;. Value 0 is special and means &quot;default&quot; : <i>ovlog</i> is automatically determined by <code>zstd</code>. In which case, <i>ovlog</i> will range from 6 to 9, depending on selected <i>strat</i>.</p>
<dt><code>ldmHashLog</code>=<i>lhlog</i>, <code>lhlog</code>=<i>lhlog</i></p>
<dd> Specify the maximum size for a hash table used for long distance matching.</p>
<dt>
<dd> This option is ignored unless long distance matching is enabled.</p>
<dt>
<dd> Bigger hash tables usually improve compression ratio at the expense of more memory during compression and a decrease in compression speed.</p>
<dt>
<dd> The minimum <i>lhlog</i> is 6 and the maximum is 30 (default: 20).</p>
<dt><code>ldmMinMatch</code>=<i>lmml</i>, <code>lmml</code>=<i>lmml</i></p>
<dd> Specify the minimum searched length of a match for long distance matching.</p>
<dt>
<dd> This option is ignored unless long distance matching is enabled.</p>
<dt>
<dd> Larger/very small values usually decrease compression ratio.</p>
<dt>
<dd> The minimum <i>lmml</i> is 4 and the maximum is 4096 (default: 64).</p>
<dt><code>ldmBucketSizeLog</code>=<i>lblog</i>, <code>lblog</code>=<i>lblog</i></p>
<dd> Specify the size of each bucket for the hash table used for long distance matching.</p>
<dt>
<dd> This option is ignored unless long distance matching is enabled.</p>
<dt>
<dd> Larger bucket sizes improve collision resolution but decrease compression speed.</p>
<dt>
<dd> The minimum <i>lblog</i> is 1 and the maximum is 8 (default: 3).</p>
<dt><code>ldmHashRateLog</code>=<i>lhrlog</i>, <code>lhrlog</code>=<i>lhrlog</i></p>
<dd> Specify the frequency of inserting entries into the long distance matching hash table.</p>
<dt>
<dd> This option is ignored unless long distance matching is enabled.</p>
<dt>
<dd> Larger values will improve compression speed. Deviating far from the default value will likely result in a decrease in compression ratio.</p>
<dt>
<dd> The default value is <code>wlog &#8211; lhlog</code>.</dl>
<h3>Example</h3>
<p> The following parameters sets advanced compression options to something similar to predefined level 19 for files bigger than 256 KB: </p>
<p> <code>&#8211;zstd</code>=wlog=23,clog=23,hlog=22,slog=6,mml=3,tlen=48,strat=6</p>
<h3>-B#:</h3>
<p> Select the size of each compression job. This parameter is available only when multi-threading is enabled. Default value is <code>4 * windowSize</code>, which means it varies depending on compression level. <code>-B#</code> makes it possible to select a custom value. Note that job size must respect a minimum value which is enforced transparently. This minimum is either 1 MB, or <code>overlapSize</code>, whichever is largest.</p>
<h2>BUGS</h2>
<p> Report bugs at: <a rel="nofollow" href="https://github.com/facebook/zstd/issues">https://github.com/facebook/zstd/issues</a></p>
<h2>AUTHOR</h2>
<p> Yann Collet </p>
<h2>Index</h2>
