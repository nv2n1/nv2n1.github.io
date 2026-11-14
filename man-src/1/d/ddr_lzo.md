---
title: "ddr_lzo(1)"
name: "ddr_lzo"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddr_lzo/"
description: "ddr_lzo – Data de/compression plugin for dd_rescue"
---

<h2>NAME</h2>
<p> ddr_lzo &#8211; Data de/compression plugin for dd_rescue</p>
<h2>SYNOPSIS</h2>
<p> <code>-L lzo[=option[:option[:&#8230;]]]</code><br />
 or<br />
 <code>-L /path/to/libddr_lzo.so[=option[:option[:&#8230;]]]</code></p>
<h2>DESCRIPTION</h2>
<h3>About</h3>
<p> LZO is an algorithm that de/compresses data. It is tuned for speed (especially decompression speed) and trades the size of the compressed file for it to some degree. There are variants with slow compression (yet still very fast decompression) available though. See the algorithm parameter below. </p>
<p> This plugin has been written for <code>dd_rescue</code> and uses the plugin interface from it. See the <code><a href="/docs/linux/man/1-dd_rescue/">dd_rescue</a>(1)</code> man page for more information on <code>dd_rescue.</code></p>
<h2>OPTIONS</h2>
<p> Options are passed using <code>dd_rescue</code> option passing syntax: The name of the plugin (lzo) is optionally followed by an equal sign (=) and options are separated by a colon (:). the <code>lzo</code> plugin also allows for most options to be abbreviated to five or six letters. See the EXAMPLES section below.</p>
<h3>Compression or decompression</h3>
<p> The lzo dd_rescue plugin (subsequently referred to as just ddr_lzo which reflects the variable parts of the filename libddr_lzo.so) choses compression or decompression mode automatically if one of the input/output files has an [lt]zo suffix; otherwise you may specify <code>compr[ess] </code> or <code>decom[press] </code> parameters on the command line.<br />
 The parameter <code>opt[imize] </code> will tell ddr_lzo to do an optimization pass after compression. This might speed up decompression by a few percent when creating compressed data with high compression levels and large block sizes. </p>
<p> The plugin also supports the parameter <code>bench[mark] ;</code> if it&#8217;s specified, it will output some information about CPU usage and resulting compression or decompression bandwidth. (For small files, the numbers become meaningless due to jitter and limited time resolution &#8212; ddr_lzo will skip the output if the numbers are very tiny.)</p>
<h3>De/compression algorithm</h3>
<p> The lzo plugin supports a number of the (de)compression algorithms from liblzo2. You can specify which one you want to use by passing <code>algo=XXX ,</code> where XXX can be lzo1x_1, lzo1x_1_15, lzo1x_999, lzo1x_1_11, lzo1x_1_12, lzo1y_1, lzo1y_999, lzo1f_1, lzo1f_999, lzo1b_1 &#8230; lzo1b_9, lzo1b_99, lzo1b_999, lzo2a_999. Pass <code>algo=help </code> to get a list of available algorithms. Consult the liblzo documentation for more information on the algorithms. Note that only the first three are supported by lzop (it can decompress the first five though, as they&#8217;re all handled by the same decompression routine).<br />
 The default (lzo1x_1) is a good choice for fast compression and very fast decompression and ensures compatibility with lzop. For higher compression you might want to chose lzo1x_999, which is very slow but lzop compatible or lzo2a_999, which is twice as fast, but not compatible with lzop.</p>
<h3>Debugging</h3>
<p> The <code>debug </code> flag will cause the ddr_lzo to output information about blocks and other internal data. It&#8217;s meant for debugging purposes. </p>
<p> Finally there is also a <code>flags=XXXX </code> parameter. This sets the flags field in the header (default is 0x03000403) and is used for testing only. It is not sanity checked and you can easily set values that will break decompression or cause ddr_lzo to abort. Really only use for development purposes when you know meaning of the various bits.</p>
<h3>Error recovery</h3>
<p> On compression, when input bytes can&#8217;t be read, ddr_lzo will encode holes in the compressed output file &#8212; these will be skipped over on decompression. </p>
<p> On decompression, erroneous blocks can be detected by the checksums (most often) or by the decompressor. The lzo plugin tries to continue in that case if the block header that specifies de/compressed lengths is intact. It will then result in a block being skipped over (hole) and the decompression will be continued with the next block. This avoids corrupt data to end up in the output file (or preexisting, potentially good data there being overwritten).<br />
 The behaviour can be modified by specifying the <code>nodisc[ard]</code> option. When given, the decompressor&#8217;s output (filled up with zeros if too short for the block) will be written to the output file. Even if we know that the data is incorrect, with some luck, parts of the block may actually be valid. </p>
<p> When the block headers are corrupt, your situation is desperate, as you will have lost the remainder of the file. To recover pieces after such a block header corruption, ddr_lzo supports the <code>search</code> option. With it, the plugin will search the input file (starting from the position given in dd_rescue with -s) for data that looks like a block header and if a valid looking header is found, it will start decompressing from that position. (If you can&#8217;t find the data you look for, you might actually study the output generated with the debug flag.)</p>
<h2>Supported dd_rescue features</h2>
<p> dd_rescue supports appending to files with the -x/&#8211;extend option. If ddr_lzo is loaded and the output file is an existing .lzo file, the new data will be appended in the format specified by the existing LZOP header. If the header does not indicate a multipart (archive) file, the EOF marker will be overwritten, so that a valid .lzo file is created. Otherwise a new part will be appended. </p>
<p> When dd_rescue can&#8217;t read data or a sizable amount of zero-filled data is found and the -a/&#8211;sparse option is active, then dd_rescue will create sparse files (files with holes inside). This is an optimization to save space &#8212; the holes are interpreted as zeroes again on normal reads, so this is transparent. The holes also can be useful to ensure that good data is not overwritten with zeroes when data couldn&#8217;t be read.<br />
 When the lzo module gets fed holes in compression mode, it will encode them in the compressed output file in a special way (using lzop multipart feature, as lzop unfortunately chokes on blocks with 0 compressed length). On decompression, the holes will result in the data being jumped over again (creating a hole in the output file, if no data preexists at the location).</p>
<h2>lzop compatibility</h2>
<p> The plugin uses the lzo1x_1 algorithm by default (just like lzop does by default) and generates adler32 checksums to allow detecting data corruption. The compressed files are compatible with lzop and ddr_lzo should handle files generated by lzop.<br />
 Multipart (archive) files from lzop are decompressed to ONE output file in the order they are stored.<br />
 Multipart files created by the lzo plugin to encode holes will be extracted to several files from lzop. The holes are encoded in the filenames (with a sequence number and the hole size up to 1TB; use the timestamp for huge holes), so a proper assembly of the fragments is possible even without ddr_lzo. </p>
<p> lzop only supports the lzo1x_ family of algorithms. If you chose another algorithm to compress data with ddr_lzo, it will set the needed_version_to_extract field in the resulting lzop file to ddr_lzo&#8217;s own version (1.789) to indicate incompatibility with lzop (as of 1.03).<br />
 lzop by default uses block sizes of 256kiB (on Unix systems), but supports de/compression with smaller block sizes as well. It needs to be recompiled to support block sizes up to a possible maximum of 64MiB. Thus staying below or at 256kiB is recommended; even when lzop compatibility is no concern, blocks larger than 16MiB are not recommended, see below.</p>
<h3>Blocksize considerations</h3>
<p> When decompressing, the (soft) block size chosen in dd_rescue must be sufficient (at least half the size of the blocksize used when compressing); if you chose too small blocks, ddr_lzo will warn and exit.<br />
 For compression, the chosen (soft)blocksize in dd_rescue will determine the size of blocks to be fed to the lzo??_?_compress() routines. Larger block sizes will typically result in slightly better compression ratios, though the returns on increasing the block size quickly diminish after 64k.<br />
 The default from dd_rescue (128kiB) is a good choice. It is NOT recommended to increase the block size too much &#8212; when an lzo file gets corrupted, at least one block will be lost; larger blocks result in larger damage. Also, blocks larger than 16MiB will not work well with the error tolerance features of ddr_lzo. Also note that blocks larger than 256kiB need recompilation of lzop if you want to be able to use lzop to process the .lzo files; blocks larger than 64MiB prevent decompression even with a recompiled lzop.</p>
<h2>BUGS/LIMITATIONS</h2>
<h3>Maturity</h3>
<p> The plugin is new as of dd_rescue 1.43. Do not yet rely on data saved with ddr_lzo as the only backup for valuable data. Also expect some changes to ddr_lzo in the not too distant future. (This should not break the file format, as we&#8217;re following lzop &#8230;.)<br />
 Compressed data is more sensitive to data corruption than plain data. Note that the checksums (adler32 or crc32) in the lzop file format do NOT allow to correct for errors; they just allow a somewhat reliable detection of data corruption. (Ideally, a 32bit checksum just misses 1 out of 2^32 corruptions; on small changes, crc32 comes a bit closer to the ideal than adler32. You may pass the <code>crc32</code> option to use crc32 instead of adler32 checksums at the expense of some speed &#8212; unfortunately the crc32 polynomial for lzop/gzip/&#8230; is not the crc32c polynomial that has hardware support on many CPUs these days.) Also note that the checksums are NOT cryptographic hashes; a malicious attacker can easily find modifications of data that do not alter the checksums. Use MD5 or better SHA-256/SHA-512 for ensuring integrity against attackers. Use par2 or similar software to create error correcting codes (Reed-Solomon / Erasure Codes) if you want to be able to recover data in face of corruption.</p>
<h3>Security</h3>
<p> While care has been applied to check the result of memory allocations &#8230;, the decompressor code has not been audited and only limited fuzzing has been applied to ensure it&#8217;s not vulnerable to malicious data &#8212; be careful when you process data from untrusted sources.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>dd_rescue -ptAL lzo=algo=lzo1x_1_15:compress,hash=alg=sha256 infile outfile</code></p>
<dd> compresses data from <i>infile</i> into <i>outfile</i> using the algorithm lzo1x_1_15 and calculates the sha256 hash value of outfile. outfile will have time stamp and access rights copied over from infile and it will be emptied before (if the file happens to exist). The output file won&#8217;t have encoded holes; errors in the infile will result in zeros.</p>
<dt><code>dd_rescue -aL MD5,lzo=compr:bench,MD5,lzo=decompress,MD5 infile infile2</code></p>
<dd> will copy <i>infile</i> to <i>infile2</i> compressing the data and decompressing it again on the fly. It will output MD5 hashes for the compressed data as well (though it&#8217;s not stored) and for the two infiles &#8212; the output should be identical, obviously. This command is rather artificial, used for testing. The -a flag makes dd_rescue detect zero blocks and create holes, thus testing hole encoding (sparse files) and decoding as well if the infile has sizable regions filled with zeros.</p>
<dt><code>dd_rescue -s1M -S0 -L lzo=search,nodiscard infile.lzo outfile</code></p>
<dd> will search for a lzop block header in infile.lzo starting at position 1MiB into the file and decompress the remainder of the file. On finding corrupted blocks, it will still write the output from the decompressor to outfile.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dd_rescue/">dd_rescue</a></code>(1) <code>liblzo2 documentation</code> <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Kurt Garloff &lt;kurt [at] garloff.de&gt;</p>
<h2>CREDITS</h2>
<p> The liblzo2 library and algorithm has been written by Markus Oberhumer.<br />
 <a rel="nofollow" href="http://www.oberhumer.com/opensource/lzo/">http://www.oberhumer.com/opensource/lzo/</a> </p>
<h2>COPYRIGHT</h2>
<p> This plugin is under the same license as dd_rescue: The GNU General Public License (GPL) v2 or v3 &#8211; at your option.</p>
<h2>HISTORY</h2>
<p> ddr_lzo plugin was first introduced with dd_rescue 1.43 (May 2014). </p>
<p> Some additional information can be found on<br />
 <a rel="nofollow" href="http://garloff.de/kurt/linux/ddrescue/">http://garloff.de/kurt/linux/ddrescue/</a> </p>
<h2>Index</h2>
