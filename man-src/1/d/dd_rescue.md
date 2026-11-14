---
title: "dd_rescue(1)"
name: "dd_rescue"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dd_rescue/"
description: "dd_rescue – Data recovery and protection tool"
---

<h2>NAME</h2>
<p> dd_rescue &#8211; Data recovery and protection tool</p>
<h2>SYNOPSIS</h2>
<p> <code>dd_rescue</code> [options] infile outfile<br />
 <code>dd_rescue</code> [options] [-2/-3/-4/-z/-Z seed/seedfile] outfile<br />
 <code>dd_rescue</code> [options] [&#8211;shred2/&#8211;shred3/&#8211;shred4/&#8211;random/&#8211;frandom seed/seedfile] outfile</p>
<h2>DESCRIPTION</h2>
<p> <code>dd_rescue</code> is a tool that copies data from a source (file, block device, pipe, &#8230;) to one (or several) output file(s). </p>
<p> If input and output files are seekable (block devices or regular files), <code>dd_rescue</code> does copy with large blocks (softbs) to increase performance. When a read error is encountered, <code>dd_rescue</code> falls back to reading smaller blocks (hardbs), to allow to recover the maximum amount of data. If blocks can still not be read, <code>dd_rescue</code> by default skips over them also in the output file, avoiding to overwrite data that might have been copied there successfully in a previous run. (Option -A / &#8211;alwayswrite changes this.). </p>
<p> <code>dd_rescue</code> can copy in reverse direction as well, allowing to approach a bad spot from both directions. As trying to read over a bad spot of significant size can take very long (and potentially cause further damage), this is an important optimization when recovering data. The <code>dd_rhelp</code> tool takes advantage of this and automates data recovery. <code>dd_rescue</code> does not (by default) truncate the output file. </p>
<p> <code>dd_rescue</code> by default reports on progress, and optionally also writes into a logfile. It has a progress bar and gives an estimate for the remaining time. <code>dd_rescue</code> has a wealth of options that influence its behavior, such as the possibility to use direct IO for input/output, to use fallocate() to preallocate space for the output file, using splice copy (in kernel zerocopy) for efficiency, looking for empty blocks to create sparse files, or using a pseudo random number generator (PRNG) to quickly overwrite data with random numbers. </p>
<p> The modes to overwrite partitions or files with pseudo random numbers make <code>dd_rescue</code> a tool that can be used for secure data deletion and thus not just a data recovery and backup tool but also a data protection tool. </p>
<p> You can use &quot;-&quot; as infile or outfile, meaning stdin or stdout. Note that this means that either file is not seekable, limiting the usefulness of some of dd_rescues features.</p>
<h2>OPTIONS</h2>
<p> When parsing numbers, <code>dd_rescue</code> assumes bytes. It accepts the following suffixes:<br />
 b &#8212; 512 size units (blocks)<br />
 k &#8212; 1024 size units (binary kilobytes, kiB)<br />
 M &#8212; 1024^2 size units (binary megabytes, MiB)<br />
 G &#8212; 1024^3 size units (binary gigabytes, GiB) </p>
<p> The following options may be used to modify the behavior of <code>dd_rescue .</code></p>
<h3>General options</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> This option tells <code>dd_rescue</code> to output a list of options and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> tells <code>dd_rescue</code> to be less verbose.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> makes <code>dd_rescue</code> more verbose.</p>
<dt><code>-c&nbsp;<wbr></code><i>0/1</i>,&nbsp;<wbr><code>&#8211;color=</code><i>0/1</i></p>
<dd> controls whether <code>dd_rescue</code> uses colors. By default it does, unless the terminal type from TERM is unknown or dumb or ends in -m or -mono.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> makes <code>dd_rescue</code> skip some sanity checks (e.g. automatically setting reverse direction when input and output file are the same and ipos &lt; opos).</p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> tells <code>dd_rescue</code> to ask before overwriting existing files.</dl>
<h3>Block sizes</h3>
<dl>
<dt><code>-b&nbsp;<wbr></code><i>softbs</i>,&nbsp;<wbr><code>&#8211;softbs=</code><i>softbs</i>,&nbsp;<wbr><code>&#8211;bs=</code><i>softbs</i></p>
<dd> sets the (larger) block size to <i>softbs</i> bytes. <code>dd_rescue</code> will transfer chunks of that size unless a read error is encountered (or the end of the input file or the maximum transfer size has been reached). The default value for this is 64k for buffered I/O and 1M for direct I/O.</p>
<dt><code>-B&nbsp;<wbr></code><i>hardbs</i>,&nbsp;<wbr><code>&#8211;hardbs=</code><i>hardbs</i>,&nbsp;<wbr><code>&#8211;block-size=</code><i>hardbs</i></p>
<dd> sets the (smaller) fallback block size to <i>hardbs</i> bytes. When <code>dd_rescue</code> encounters read errors, it will fall back to copying data in chunks of this size. This value defaults to 4k for buffered I/O and 512 bytes for direct I/O.<br />
 <i>hardbs</i> should be equal to or smaller than <i>softbs</i>. If both block sizes are identical, no fallback mechanism (and thus no retry) will take place on read errors.</p>
<dt><code>-y&nbsp;<wbr></code><i>syncsize</i>,&nbsp;<wbr><code>&#8211;syncfreq=</code><i>syncsize</i></p>
<dd> tells <code>dd_rescue</code> to call fsync() on the output file every <i>syncsize</i> bytes (will be rounded to multiples of <i>softbs</i> sized blocks). It will also update the progress indicator at least as often. By default, <i>syncsize</i> is set to 0, meaning that fsync() is only issued at the end of the copy operation.</dl>
<h3>Positions and length</h3>
<dl>
<dt><code>-s&nbsp;<wbr></code><i>ipos</i>,&nbsp;<wbr><code>&#8211;ipos=</code><i>ipos</i>,&nbsp;<wbr><code>&#8211;input-position=</code><i>ipos</i></p>
<dd> sets the starting position of the <i>infile</i> to <i>ipos</i>. Note that ipos is specified in bytes (but suffixes can be used, see above), not in terms of <i>softbs</i> or <i>hardbs</i> sized blocks. The default value for this is 0. When reverse direction copy is used, an <i>ipos</i> of 0 is treated specially, meaning the end of file.<br />
 Negative positions result in an error message.</p>
<dt><code>-S&nbsp;<wbr></code><i>opos</i>,&nbsp;<wbr><code>&#8211;opos=</code><i>opos</i>,&nbsp;<wbr><code>&#8211;output-position=</code><i>opos</i></p>
<dd> sets the starting position of the <i>outfile</i> to <i>opos</i>. If not specified, <i>opos</i> is set to <i>ipos</i>, so the file offsets in input and output file are the same. For reverse direction copy, an explicit <i>opos</i> of 0 will position at the end of the output file.</p>
<dt><code>-x</code>, <code>&#8211;extend</code>, <code>&#8211;append</code></p>
<dd> changes the interpretation of the output position to start at the end of the existing output file, making appending to a file convenient. If the output file does not exist, an error will be reported and <code>dd_rescue</code> aborted.</p>
<dt><code>-m&nbsp;<wbr></code><i>maxxfer</i>,&nbsp;<wbr><code>&#8211;maxxfer=</code><i>maxxfer</i>,&nbsp;<wbr><code>&#8211;max-size=</code><i>maxxfer</i></p>
<dd> specifies the maximum number of bytes (suffixes apply, but it&#8217;s NOT counted in blocks) that <code>dd_rescue </code> copies. If EOF is encountered before <i>maxxfer</i> bytes have been transferred, this option will be silently ignored.</p>
<dt><code>-M</code>, <code>&#8211;noextend</code></p>
<dd> tells <code>dd_rescue</code> to not extend the output file. This option is particularly helpful when overwriting a file with random data or zeroes for safe data destruction. If the output file does not exist, an error message will be generated and the program be aborted.</dl>
<h3>Error handling</h3>
<dl>
<dt><code>-e&nbsp;<wbr></code><i>maxerr</i>,&nbsp;<wbr><code>&#8211;maxerr=</code><i>maxerr</i></p>
<dd> tells <code>dd_rescue</code> to exit, after <i>maxerr</i> read errors have been encountered. By default, this is set to 0, resulting in <code>dd_rescue</code> trying to move on until it hits EOF (or <i>maxxfer</i> bytes have been transferred).</p>
<dt><code>-w</code>, <code>&#8211;abort_we</code></p>
<dd> makes <code>dd_rescue</code> abort on any write errors. By default, on reported write errors, <code>dd_rescue</code> tries to rewrite the blocks with small block size writes, so a small failure in a larger block will not cause the whole block not to be written. Note that this may be handled similarly by your Operating System kernel with buffered writes without the user or dd_rescue noticing; the write retry logic in dd_rescue is mostly useful for direct I/O writes where write errors can be reliably detected.<br />
 Write error detection with buffered writes is unreliable; the kernel reports success and traces of the failing writeback operations later may only appear in your syslog. dd_rescue does try to notice the user by calling fsync() and carefully checking the return values of fsync() and close() calls.<br />
 Note that <code>dd_rescue</code> does exit if writes to the output file result in the Operating System reporting that no space is left.</dl>
<h3>Sparse files and write avoidance</h3>
<dl>
<dt><code>-A</code>, <code>&#8211;alwayswrite</code></p>
<dd> changes the behavior of <code>dd_rescue</code> to write zeroes to the output file when the input file could not be read. By default, it just skips over, leaving whatever content was in the output file at the file position before. The default behavior may be desired, if e.g. previous copy operations may have resulted in good data being in place; it may be undesired if the output file may contain garbage (or sensitive information) that should rather be overwritten with zeroes.</p>
<dt><code>-a</code>, <code>&#8211;sparse</code></p>
<dd> will make <code>dd_rescue</code> look for empty blocks (of at least half of <i>softbs</i> size), i.e. blocks filled with zeroes. Rather than writing those zeroes to the output file, it will then skip forward in the output file, resulting in a sparse file, saving space in the output file system (if it supports sparse files). Note that if the output file does already exist and already has data stored at the location where zeroes are skipped over, this will result in an incomplete copy in that the output file is different from the input file at the location where blocks of zeroes were skipped over. <code>dd_rescue</code> tries to detect this and issue a warning, but it does not prevent this from happening</p>
<dt><code>-W</code>, <code>&#8211;avoidwrite</code></p>
<dd> results in <code>dd_rescue</code> reading a block ( <i>softbs</i> sized) from the output file prior to writing it. If it is already identical with the data that would be written to it, the writes are actually avoided. This option may be useful for devices, where e.g. writes should be avoided (e.g. because they may impact the remaining lifetime or because they are very slow compared to reads).</dl>
<h3>Other optimization</h3>
<dl>
<dt><code>-R</code>, <code>&#8211;repeat</code></p>
<dd> tells <code>dd_rescue</code> to only read one block ( <i>softbs</i> sized) and then repeatedly write it to the output file. Note that this results in never hitting EOF on the input file and should be used with a limit for the transfer size (options -m or -M) or when filling up an output device completely.<br />
 This option is automatically set, if the input file name equals &quot;/dev/zero&quot;.</p>
<dt><code>-u</code>, <code>&#8211;rmvtrim</code></p>
<dd> instructs <code>dd_rescue</code> to remove the output file after writing to it has completed and issue a FITRIM on the file system that contains the output file. This makes only sense if writing zeros (or random numbers) as opposed to useful content from another file. (dd_rescue will ask for confirmation if this is specified with a normal input file and no -f (&#8211;force) is used.) This option may be used to ensure that all empty blocks of a file system are filled with zeros (rather than containing fragments of deleted files with possibly sensitive information).<br />
 The FITRIM ioctl (on Linux) tells the flash storage to consider the freed space as unused (like the fstrim tool or the discard option) by issuing ATA TRIM commands. This will only succeed with superuser privileges (but the error can otherwise be safely ignored). This is useful to ensure full performance of flash memory / SSDs. Note that FITRIM can take a while on large file systems, especially if the file systems are not mounted with the discard option and have not been trimmed (with e.g. fstrim) for a while. Not all file systems and not all flash-based storage support this.</p>
<dt><code>-k</code>, <code>&#8211;splice</code></p>
<dd> tells <code>dd_rescue</code> to use the Linux in-kernel zerocopy splice() copy operation rather than reading blocks into a user space buffer. Note that this operation mode does prevent the support of a number of <code>dd_rescue</code> features that can normally be used, such as falling back to smaller block sizes, avoiding writes, sparse mode, repeat optimization, reverse direction copy. A warning is issued to make the user aware.</p>
<dt><code>-P</code>, <code>&#8211;fallocate</code></p>
<dd> results in <code>dd_rescue</code> calling fallocate() on the output file, telling the file system how much space to preallocate for the output file. (The size is determined by the expected last position, as inferred from the input file length and <i>maxxfer</i> ). On file systems that support it, this results in them making better allocation decisions, avoiding fragmentation. (Note that it does not make sense to use sparse together with fallocate().)<br />
 This option is only available if dd_rescue is compiled with fallocate() support. For optimal support, it should be compiled with the libfallocate library.</dl>
<h3>Misc options</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;reverse</code></p>
<dd> tells <code>dd_rescue</code> to copy in reverse direction, starting at <i>ipos</i> (with special case 0 meaning EOF) and working towards the beginning of the file. This is especially helpful if the input file has a bad spot which can be extremely slow to skip over, so approaching it from both directions saves a lot of time (and may prevent further damage).<br />
 Note that <code>dd_rescue</code> does automatically switch to reverse direction copy, if input and output file are identical and the input position is smaller than the output position, similar to the intelligence that memmove() uses to prevent loss of data when overlapping areas are copied. The option -f / &#8211;force does prevent this intelligence from happening.</p>
<dt><code>-p</code>, <code>&#8211;preserve</code></p>
<dd> When copying files, this option does result in file metadata (timestamps, ownership, access rights, xattrs) to be copied, similar to the option with the same name in the cp program.<br />
 Note that ACLs and xattrs will only be copied if <code>dd_rescue</code> has been compiled with libxattr support and the library can be dynamically loaded on the system. Also note that failing to copy the attributes with <i>-p</i> is not considered a failure and thus won&#8217;t negatively affect the exit code of dd_rescue.</p>
<dt><code>-t</code>, <code>&#8211;truncate</code></p>
<dd> tells <code>dd_rescue</code> to open the output file with O_TRUNC, resulting in the output file (if it is a regular file) to be truncated to 0 bytes before writing to it, removing all previous content that the file may have contained. By default, <code>dd_rescue</code> does not remove previous content.</p>
<dt><code>-T</code>, <code>&#8211;trunclast</code></p>
<dd> tells <code>dd_rescue</code> to truncate the output file to the highest copied position after the copy operation completed, thus ensuring there&#8217;s no data beyond the end of the data that has been copied in this run.</p>
<dt><code>-d</code>, <code>&#8211;odir_in</code></p>
<dd> instructs <code>dd_rescue</code> to open <i>infile</i> with O_DIRECT, bypassing the kernel buffers. While this option has a negative effect on performance (the kernel does read-ahead for buffered I/O), it will result in errors to be detected more quickly (kernel won&#8217;t retry) and allows for smaller I/O units (hardware sector size, 512bytes for most hard disks).<br />
 O_DIRECT may not be available on all platforms.</p>
<dt><code>-D</code>, <code>&#8211;odir_out</code></p>
<dd> tells <code>dd_rescue</code> to open <i>outfile</i> with O_DIRECT, bypassing kernel buffers. This has a significant negative effect on performance, as the program needs to wait for writes to hit the disks as opposed to the asynchronous nature of buffered writeback. On the flip side, the return status from writing is reliable this way and smaller I/O chunks (hardware sector size, 512bytes) are possible.</dl>
<h3>Logging</h3>
<dl>
<dt><code>-l&nbsp;<wbr></code><i>logfile</i>,&nbsp;<wbr><code>&#8211;logfile=</code><i>logfile</i></p>
<dd> Unless in quiet mode, <code>dd_rescue</code> does produce constant updates on the status of the copy operation to stderr. With this option, these updates are also written to the specified <i>logfile</i>. The control characters (to move the cursor up to overwrite the existing status lines) are not written to the logfile.</p>
<dt><code>-o&nbsp;<wbr></code><i>bbfile</i>,&nbsp;<wbr><code>&#8211;bbfile=</code><i>bbfile</i></p>
<dd> instructs <code>dd_rescue</code> to write a list of bad blocks to <i>bbfile</i>. The file will contain a list of numbers (ASCII), one per line, where the numbers indicate the offset in terms of <i>hardbs</i> sized blocks. The file format is compatible with that of badblocks. Using dd_rescue on a block device (partition) and setting <i>hardbs</i> to the block size of a file system that you want to create, you should be able to feed the <i>bbfile</i> to mke2fs with the option -l.</dl>
<h3>Multiple output files</h3>
<dl>
<dt><code>-Y&nbsp;<wbr></code><i>ofileX</i>,&nbsp;<wbr><code>&#8211;outfile=</code><i>ofileX</i>,&nbsp;<wbr><code>&#8211;of=</code><i>ofileX</i></p>
<dd> If you want to copy data to multiple files simultaneously, you can specify this option. It can be specified multiple times, so many copies can be made. Note that these files are secondary output files; they share file position with the primary output file <i>outfile</i>. Errors when writing to a secondary output file are ignored.</dl>
<h3>Data protection by overwriting with random numbers</h3>
<dl>
<dt><code>-z&nbsp;<wbr></code><i>RANDSEED</i>,&nbsp;<wbr><code>&#8211;random=</code><i>RANDSEED</i></p>
<dd>
<dt><code>-Z&nbsp;<wbr></code><i>RANDSEED</i>,&nbsp;<wbr><code>&#8211;frandom=</code><i>RANDSEED</i></p>
<dd>
<dt><code>-2&nbsp;<wbr></code><i>RANDSEED</i>,&nbsp;<wbr><code>&#8211;shred2=</code><i>RANDSEED</i></p>
<dd>
<dt><code>-3&nbsp;<wbr></code><i>RANDSEED</i>,&nbsp;<wbr><code>&#8211;shred3=</code><i>RANDSEED</i></p>
<dd>
<dt><code>-4&nbsp;<wbr></code><i>RANDSEED</i>,&nbsp;<wbr><code>&#8211;shred4=</code><i>RANDSEED</i></p>
<dd> When you want to overwrite a file, partition or disk with random data, using /dev/urandom (on Linux) as input is not a very good idea; the interface has not been designed to yield a high bandwidth. It&#8217;s better to use a user space Pseudo Random Number Generator (PRNG). With option -z / &#8211;random, the C library&#8217;s PRNG is used. With -Z / &#8211;frandom and the -2/-3/-4 / &#8211;shred2/3/4 options, an RC4 based PRNG is used.<br />
 Note that in this mode, there is no <i>infile</i> so the first non-option argument is the output file.<br />
 The PRNG needs seeding; the C libraries PRNG takes a 32bit integer (4 bytes); the RC4 based PRNG takes 256 bytes. If <i>RANDSEED</i> is an integer, the integer number will be used to seed the C library&#8217;s PRNG. For the RC4 method, the C library&#8217;s PRNG then generates the 256 bytes to seed it. This creates repeatable PRNG data. The RANDSEED value of 0 is special; it will create a seedval that&#8217;s based on the current time and the process&#8217; PID and should be different for multiple runs of <code>dd_rescue .</code><br />
 If <i>RANDSEED</i> is not an integer, it&#8217;s assumed to be a file name from which the seed values can be read. <code>dd_rescue</code> will read 4 or 256 bytes from the file to seed the C library&#8217;s or the RC4 PRNG. For good pseudo random numbers, using /dev/urandom to seed is a good idea.<br />
 The modes -2/-3/-4 resp. &#8211;shred2/&#8211;shred3/&#8211;shred4 will overwrite the output file multiple times; after each pass, fsync() will ensure that the data does indeed hit the file. The last pass for these modes will overwrite the file with zeroes. The rationale behind doing this is to make it easier to hide that important data may have been overwritten, to make it easier for intelligent storage systems (such as SSDs) to recycle the empty blocks and to allow for better compression of a file system image containing such data.<br />
 With -2 / &#8211;shred2, one pass with RC4 generated PRNG is happening and then zeroes are written. With -3 / &#8211;shred3, there are two passes with RC4 PRNG generated random numbers and a zero pass; the second PRNG pass writes the inverse (bit-wise reversed) numbers from the first pass. -4 / &#8211;shred4 works like -3 / &#8211;shred3, with an additional pass with independent random numbers as third pass.</dl>
<h3>Plugins</h3>
<p> Since version 1.42, <code>dd_rescue</code> has an interface for plugins. Plugins have the ability to analyze the copied data or to transform it prior to it being written.</p>
<dl>
<dt><code>-L&nbsp;<wbr></code><i>plugin1[=param1[:param2[:..]]][,plugin2[=..][,..]]</i></p>
<dd>
<dt><code>&#8211;plugins=</code><i>plugin1[=param1[:param2[:..]]][,plugin2[=..][,..]]</i></p>
<dd> loads plugins plugin1 &#8230; and passes parameters to it. All plugins should support at least the help parameter and provide information on their usage.<br />
 Plugins may impose limits on dd_rescue. Plugins that look at the data can&#8217;t work with splice, as this avoids copying data to user space. Also the interface currently does not facilitate reverse direction copy. Some plugins may impose further restrictions w.r.t. alignment of data in the file or not using sparse detection.<br />
 See section <code>PLUGINS</code> for an overview of available plugins. </p>
</dl>
<h2>PLUGINS</h2>
<h3>null</h3>
<p> The null plugin (ddr_null) does nothing, except if you specify the <code>[no]lnchange</code> or the <code>[no]change</code> options in which case the plugin indicates to others that it transforms the length of the output or the data of the stream. (With the no prefix, it&#8217;s reset to the default no-change indication again.) This may be helpful for testing or to influence which file the hash plugin considers for reading/writing extended attributes from/to and for plugins to change their behavior with respect to hole detection.<br />
 ddr_null_ddr also allows you to specify <code>debug</code> in which case it just reports the blocks that it passes on.</p>
<h3>hash</h3>
<p> When the hash plugin (subsequently referred to as ddr_hash) is loaded, it will calculate a cryptographic hash and optionally also a HMAC over the copied data and print the result at the end of the copy operations. The hash algorithm can be chosen by specifying <code>alg[o[rithm]]=ALG</code> where ALG is one of md5, sha1, sha256, sha224, sha512, sha384. (Specify alg=help to get a list.) To abbreviate the syntax, the alg= piece can be omitted.<br />
 For backwards compatibility, the hash plugin can also be referred to with the old MD5 name; it then defaults to the md5 algorithm.<br />
 The computed value should be identical to calling md5sum/sha256sum/&#8230; on the target file (unless you only write part of the file), but saves time by not accessing the (possibly large) file a second time. The hash plugin handles sparse writes and arbitrary offsets fine. </p>
<p> ddr_hash also supports the parameter <code>append=STRING</code> which appends the given STRING to the output before computing the cryptographic hash. Treating the STRING as a shared secret, this can actually be used to protect against someone not knowing the secret altering the contents (and recomputing the hash) without anyone noticing. It&#8217;s thus a cheap way of a cryptographic signature (but with preshared secrets as opposed to public key cryptography). Use HMAC for a somewhat better way to sign data with a shared secret.<br />
 ddr_hash also supports <code>prepend=STRING</code> which is likely harder to attack with brute force than an appended string. Note that ddr_hash always prepends multiples of the hash algorithm&#8217;s block size and pads the STRING with 0 to match. </p>
<p> ddr_hash can be used to compute a HMAC (Hash-based Message Authentication Code) instead of the plain hash. The HMAC uses a password that&#8217;s prepended and transformed twice to the data which is then hashed twice. HMAC is believed to protect somewhat better against extension or collision attacks than a plain hash (with a plain prepended secret), so it&#8217;s a better way to authenticate data with a shared secret. (You can use append/prepend in addition to HMAC, if you have a need for a scheme with more than one secret.)<br />
 When HMAC is enabled with one of the following parameters, both the plain hash and the HMAC are computed by ddr_hash. Both are output to the console/log, but the HMAC is used instead of the hash value to be written to a CHECKSUMS file or to an extended attribute or checked against (see below). <code>hmacpwd=STRING</code> sets the shared secret (password) for computing the HMAC. Passing the secret on the command line has the disadvantage that the shell may mistreat some bytes as special characters and that the command line may be visible to all logged in users on the system. <code>hmacpwdfd=INT</code> sets a file descriptor from with the secret (password) for HMAC computation will be read. Specifying 0 means standard input, in which case ddr_hash even prints a prompt for you &#8230; Other numbers may be useful if dd_rescue is called from another program that opens a pipe to pass the secret. <code>hmacpwdnm=INNAME</code> sets a file from which the shared secret (password) is read. Note that all bytes (up to 2048 of them) are read and used, including trailing white space, 0-bytes or newlines.<br />
 Please note that the ddr_hash plugin at this point does NOT take a lot of care to prevent the password/pre/appended secret from remaining in memory or leaking into a swap/page file. (This will be improved once I look into encryption plugins.) </p>
<p> ddr_hash accepts the parameter <code>output</code> , which will cause ddr_hash to output the cryptographic hash to stdout in the same format that md5sum/sha256sum/&#8230; use. You can also specify <code>outfd=INT</code> to have the plugin write the hash to a different file descriptor specified by the integer number INT. Note that ddr_hash always processes data in binary mode and correctly indicates this with a star (*) in the output generated with output/outfd=.<br />
 The checksum can also be written to a file by giving the <code>outnm=OUTNAME</code> parameter. Then a file with OUTNAME will be created and a md5sum/sha256sum/&#8230; compatible line will be printed to the file. If the file exists and contains an entry for the file, it will be updated. If the file exists and does not contain an entry for the file, one will be appended. If OUTNAME is omitted, the file name CHECKSUMS.alg (or HMACS.alg if HMAC is enabled) will be used (alg is replaced by the chosen algorithm). If the checksum can&#8217;t be written, a warning will be printed and the exit code of dd_rescue will become non-zero. </p>
<p> The checksum can be validated using <code>checknm=CHKNAME .</code> The file will be read and ddr_hash will look for an md5sum/sha256sum/&#8230; compatible line with a matching file name to take the checksum from and compare it to the one computed. If NAME is omitted, the same default as described above (in outnm=&#8230;) will be used. You can also read the checksum from stdin if you prefer by specifying the <code>check</code> option.<br />
 Note that in any case, the check is only performed after the copy operation is completed &#8212; a faulty checksum will thus NOT result in the copy not taking place. However, the exit code of dd_rescue will indicate the error. (If you want to avoid copying data with a broken checksum into the final target, use a temporary target that you delete upon error and only move to the final location if dd_rescue&#8217;s exit value is 0; you can of course also copy to /dev/null for testing beforehand, but it might be too costly reading the input file twice.) </p>
<p> You can store the cryptographic hash into the files by using the <code>set_xattr</code> option. The hash will be stored into the extended attribute user.checksum.ALG by default (user.hmac.ALG if HMAC is enabled), but you can override the name of the attribute by specifying <code>set_xattr=XATTR.NAME</code> instead. If the xattr can&#8217;t be written, an error will be reported, unless you also specify the <code>fallb[ack][=CHKNAME]</code> option. In that case, ddr_hash tries to write the checksum to the CHKNAME checksums file. (For the default for CHKNAME, see outnm= option above.)<br />
 <code>chk_xattr</code> will validate that the computed hash matches the one read from the extended attribute. The same default attribute name applies and you can likewise override it with <code>chk_xattr=XATTR.NAME .</code> A missing attribute is considered an error (although the same fallback is tried if you specify the fallback option). A broken checksum is of course considered an error as well, but just like with checknm=CHKNAME won&#8217;t prevent the copy. See the discussion there. </p>
<p> Note that for output,outfd,outnm=,set_xattr ddr_hash will use the output file name to attach the checksum to (be it by setting xattr or the file name used in the checksum file), unless a plugin in the chain after ddr_hash indicates that it changes the data. In that case, it will warn and associate the checksum with the input file name, unless there&#8217;s another plugin before ddr_hash in the chain which indicates data transformation as well. In that case, there is no file that the checksum could be associated with and ddr_hash will report an error.<br />
 Likewise for chknm=,check,chk_xattr ddr_hash will use the input file name to get the checksum (be it by reading the xattr or by looking for the input file name in a checksums file) unless there&#8217;s a plugin in the chain before ddr_hash that indicates that it changes the data. The output file name will then be used, unless there&#8217;s another plugin after ddr_hash indicating data change as well, in which case there&#8217;s no file we could get the checksum for and thus an error is reported. </p>
<p> If your system supports extended attributes, those have the advantage of traveling with the files; thus a rename or copy (with dd_rescue -p) will maintain the checksum. Checksum files on the other hand can be handled everywhere (including the transfer via ftp or http) and can be cryptographically signed with PGP/GnuPG. </p>
<p> Please note that the md5 algorithm is NOT recommended any more for good protection against malicious attempts to hide data modification; it&#8217;s not considered strong enough any more to prevent hash collisions. sha1 is better, but the recommendation is to use the SHA-2 family of hashes. On 32bit machines, I&#8217;d recommend sha256, while on 64bit machines, sha512 is faster and thus the best choice. </p>
<p> ddr_hash also supports using the HMAC code and hashes for deriving keys from passwords using the PKCS5 PBKDF2 (password-based key derivation function) that allows you to improve the protection from mediocre passwords by using a salt and a relatively expensive key stretching operation. This is only meant for testing and may be removed in the future. It&#8217;s thus not documented in this man page. See the built-in help function for a brief summary on the usage.</p>
<h3>lzo</h3>
<p> The lzo plugin allows to compress and decompress data using liblzo2. lzo is an algorithm that is faster than most other algorithms but does not compress as well. See the <code><a href="/docs/linux/man/1-ddr_lzo/">ddr_lzo</a></code>(1) man page for more details.</p>
<h3>crypt</h3>
<p> The crypt plugin allows to encrypt and decrypt data on the fly. It currently supports a variety of AES ciphers. See the <code><a href="/docs/linux/man/1-ddr_crypt/">ddr_crypt</a></code>(1) man page for more details.</p>
<h2>EXIT STATUS</h2>
<p> On successful completion, <code>dd_rescue</code> returns an exit code of 0. Any other exit code indicates that the program has aborted because of an error condition or that copying of the data has not been entirely successful. </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>dd_rescue -k -P -p -t infile outfile</code></p>
<dd> copies <i>infile</i> to <i>outfile</i> and does truncate the output file on opening (so deleting any previous data in it), copies mode, times, ownership at the end, uses fallocate to reserve the space for the output file and uses efficient in kernel splice copy method.</p>
<dt><code>dd_rescue -A -d -D -b 512&nbsp;<wbr>/dev/sda&nbsp;<wbr>/dev/sda</code></p>
<dd> reads the contents of every sector of disk sda and writes it back to the same location. Typical hard disks reallocate flaky and faulty sectors on writes, so this operation may result in the complete disk being usable again when there were errors before. Unreadable blocks however will contain zeroes after this.</p>
<dt><code>dd_rescue -2&nbsp;<wbr>/dev/urandom -M outfile</code></p>
<dd> overwrites the file <i>outfile</i> twice; once with good pseudo random numbers and then with zeroes.</p>
<dt><code>dd_rescue -t -a image1.raw image2.raw</code></p>
<dd> copies a file system image and looks for empty blocks to create a sparse output file to save disk space. (If the source file system has been used a bit, on that file system creating a large file with zeroes and removing it again prior to this operation will result in more sectors with zeroes. <code>dd_rescue -u&nbsp;<wbr>/dev/zero DUMMY</code> will achieve this &#8230;)</p>
<dt><code>dd_rescue -ATL hash=md5:output,lzo=compress:bench,MD5:output in out.lzo</code></p>
<dd> copies the file <i>in</i> to <i>out.lzo</i> with using lzo (lzo1x_1) compression and calculating an md5 hash (checksum) on both files. The md5 hashes for both are also written to stdout in the md5sum output format. Note that the compress parameter to lzo is not strictly required here; the plugin could have deduced it from the file names. This example shows that you can specify multiple plugins with multiple parameters; the plugins are forming a filter chain. You can specify the same plugin multiple times.</p>
<dt><code>dd_rescue -L hash=sha512:set_xattr:fallb,null=change infile&nbsp;<wbr>/dev/null</code></p>
<dd> reads the file <i>infile</i> and computes its sha512 hash. It stores it in the input file&#8217;s user.checksum.sha512 attribute (and falls back to writing it to CHECKSUMS.sha512 if xattrs can&#8217;t be written). Note the use of the null plugin with faking data change with the change parameter; this causes the hash plugin to write to the input file which it would not normally have done. Of course this will fail if you don&#8217;t have the appropriate privileges to write xattrs to infile nor to write the checksum to CHECKSUMS.sha512.</dl>
<p> See also README.dd_rescue and <a href="/docs/linux/man/1-ddr_lzo/">ddr_lzo</a>(1) to learn about the possibilities.</p>
<h2>TESTING</h2>
<p> Untested code is buggy, almost always. I happen to have a damaged hard disk that I use for testing dd_rescue from time to time. But to allow for automated testing of error recovery, it&#8217;s better to have predictable failures for the program to deal with. So there is a fault injection framework.<br />
 Specifying <code>-F 5w/1,17r/3,42r/-1,80-84r/0</code> on the command-line will result in in the 5th block (counted in hardblocksize) will fail to be written once (from which dd_rescue should recover, as it tries a second time for failed writes), block no 17 will fail to be read 3 times, block no 42 will read fine once, but then fail afterwards, whereas blocks 80 through 83 are completely unreadable (will fail infinite times). Note that the range excludes the last block (80-84 means 4 blocks starting @ 80).<br />
 Block offsets are always counted in absolute positions, so starting in the middle of a file with -s or reverse copying won&#8217;t affect the absolute position that is hit with the fault injection. (This has changed since 1.98.) </p>
<h2>BUGS/LIMITATIONS</h2>
<p> The source code does use the 64bit functions provided by glibc for file positioning. However, your kernel might not support it, so you might be unable to copy partitions larger then 2GB into a file.<br />
 This program has been written using Linux and only tested on a couple of Linux systems. People have reported to have successfully used it on other Un*xish systems (such as xBSD or M*cOS), but these systems get little regular test coverage; so please be advised to test properly (possibly using the make check test suite included with the source distribution) before relying on dd_rescue on non Linux based systems.<br />
 Currently, the escape sequence for moving the cursor up is hard coded in the sources. It&#8217;s fine for most terminal emulations (including vt100 and linux), but it should use the terminal description database instead.<br />
 Since dd_rescue-1.10, non-seekable input or output files are supported, but there&#8217;s of course limitations to recover errors in such cases. </p>
<p> dd_rescue does not automate the recovery of faulty files or partitions by automatically keeping a list of copied sectors and approaching bad spots from both sides. There is a helper script dd_rhelp from LAB Valentin that does this. Integration of such a mode into <code>dd_rescue</code> itself is non-trivial and due to the complexity of the source code might not happen.<br />
 There also is a tool, GNU ddrescue, that is a reimplementation of this tool and which contains the capabilities to automate recovery of bad files in the way dd_rhelp does. It does not have the feature richness of dd_rescue, but is reported to be easier to operate for error recovery than dd_rescue with dd_rhelp. </p>
<p> If your data is very valuable and you are considering sending your disk to a data recovery company, you might be better off NOT trying to use imaging tools like dd_rescue, dd_rhelp or GNU ddrescue. If you&#8217;re unlucky, the disk has suffered some mechanical damage (e.g. by having been dropped), and continuing to use it may make the head damage the surface further. You may be able to detect this condition by quickly raising error counts in the SMART attributes or by a clicking noise. </p>
<p> Please report bugs to me via email.</p>
<h3>Data destruction considerations</h3>
<p> The modes for overwriting data with pseudo random numbers to securely delete sensitive data on purpose only implement a limited number of overwrites. While Peter Gutmann&#8217;s classic analysis concludes that the then current hard disk technology requires more overwrites to be really secure, the author believes that modern hard disk technology does not allow data restoration of sectors that have been overwritten with the &#8211;shred4 mode. This is in compliance with the recommendations from BSI GSDS M7.15.<br />
 Overwriting whole partitions or disks with random numbers is a fairly safe way to destroy data, unless the underlying storage device does too much magic. SSDs are doing fancy stuff in their Flash Translation Layer (FTL), so this tool might be insufficient to get rid of data. Use SECURITY_ERASE (use hdparm) there or &#8212; if available &#8212; encrypt data with AES256 and safely destroy the key. Normal hard disks have a small risk of leaking a few sectors due to reallocation of flaky sectors.<br />
 For securely destroying single files, your mileage may vary. The more advanced your file system, the less likely dd_rescue&#8217;s destruction will be effective. In particular, journaling file systems may carry old data in the journal. File systems that do copy-on-write (COW) such as btrfs, are very likely to have old copies of your supposedly erased file. It might help somewhat to fill the file systems with zeros (dd_rescue -u /dev/zero /path/to/fs/DUMMYNAME) to force the file system to release and overwrite non-current data after overwriting critical files with random numbers. If you can, better destroy a whole partition or disk.</p>
<h2>SEE ALSO</h2>
<p> <code>README.dd_rescue</code> <code>README.dd_rhelp</code> <code><a href="/docs/linux/man/1-ddr_lzo/">ddr_lzo</a></code>(1)<br />
 <code><a href="/docs/linux/man/1-wipe/">wipe</a></code>(1) <code><a href="/docs/linux/man/1-shred/">shred</a></code>(1) <code><a href="/docs/linux/man/1-ddrescue/">ddrescue</a></code>(1) <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Kurt Garloff &lt;kurt [at] garloff.de&gt;</p>
<h2>CREDITS</h2>
<p> Many little issues were reported by Valentin LAB, the author of <code>dd_rhelp .</code><br />
 The RC4 PRNG (frandom) is a port from Eli Billauer&#8217;s kernel mode PRNG.<br />
 A number of recent ideas and suggestions came from Thomas.</p>
<h2>COPYRIGHT</h2>
<p> This program is protected by the GNU General Public License (GPL) v2 or v3 &#8211; at your option.</p>
<h2>HISTORY</h2>
<p> Since version 1.10, non seekable input and output files are supported.<br />
 Splice copy -k is supported since 1.15.<br />
 A progress bar exists since 1.17.<br />
 Support for preallocation (fallocate) -P exists since 1.19.<br />
 Since 1.23, we default to -y0, enhancing performance.<br />
 The Pseudo Random Number modes have been started with 1.29.<br />
 Write avoidance -W has been implemented in 1.30<br />
 Multiple output files -Y have been added in 1.32.<br />
 Long options and man page came with 1.33.<br />
 Optimized sparse detection (SSE2, armv6, armv8 asm, AVX2) has been present since 1.35 and been enhanced until 1.43.<br />
 We support copying extended attributes since 1.40 using libxattr.<br />
 Removing and (fs)trimming the output file&#8217;s file system exists since 1.41. Support for compilation with bionic (Android&#8217;s C library) with most features enabled also came with 1.41.<br />
 Plugins exist since 1.42, the MD5 plugin came with 1.42, the lzo plugin with 1.43. 1.44 renamed the MD5 plugin to hash and added support for the SHA-2 family of hashes. 1.45 added SHA-1 and the ability to store and validate checksums.<br />
 1.98 brought encryption and the fault injection framework, 1.99 support for ARMv8 crypto acceleration. </p>
<p> Some additional information can be found on<br />
 <a rel="nofollow" href="http://garloff.de/kurt/linux/ddrescue/">http://garloff.de/kurt/linux/ddrescue/</a><br />
 LAB Valentin&#8217;s <code>dd_rhelp</code> can be found on<br />
 <a rel="nofollow" href="http://www.kalysto.org/utilities/dd_rhelp/index.en.html">http://www.kalysto.org/utilities/dd_rhelp/index.en.html</a> </p>
<h2>Index</h2>
