---
title: "fio(1)"
name: "fio"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fio/"
description: "fio – flexible I/O tester"
---

<h2>NAME</h2>
<p> fio &#8211; flexible I/O tester</p>
<h2>SYNOPSIS</h2>
<p> <code>fio</code> [<i>options</i>] [<i>jobfile</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>fio</code> is a tool that will spawn a number of threads or processes doing a particular type of I/O action as specified by the user. The typical use of fio is to write a job file matching the I/O load one wants to simulate.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code><i></i>=type</p>
<dd> Enable verbose tracing of various fio actions. May be `all&#8217; for all types or individual types separated by a comma (eg &#8211;debug=io,file). `help&#8217; will list all available tracing options.</p>
<dt><code>&#8211;output</code><i></i>=filename</p>
<dd> Write output to <i>filename</i>.</p>
<dt><code>&#8211;output-format</code><i></i>=format</p>
<dd> Set the reporting format to <i>normal</i>, <i>terse</i>, or <i>json</i>.</p>
<dt><code>&#8211;runtime</code><i></i>=runtime</p>
<dd> Limit run time to <i>runtime</i> seconds.</p>
<dt><code>&#8211;bandwidth-log</code></p>
<dd> Generate per-job bandwidth logs.</p>
<dt><code>&#8211;minimal</code></p>
<dd> Print statistics in a terse, semicolon-delimited format.</p>
<dt><code>&#8211;append-terse</code></p>
<dd> Print statistics in selected mode AND terse, semicolon-delimited format.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>&#8211;terse-version</code><i></i>=version</p>
<dd> Set terse version output format (Current version 3, or older version 2).</p>
<dt><code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>&#8211;cpuclock-test</code></p>
<dd> Perform test and validation of internal CPU clock</p>
<dt><code>&#8211;crctest[</code>=test]</p>
<dd> Test the speed of the builtin checksumming functions. If no argument is given, all of them are tested. Or a comma separated list can be passed, in which case the given ones are tested.</p>
<dt><code>&#8211;cmdhelp</code><i></i>=command</p>
<dd> Print help information for <i>command</i>. May be `all&#8217; for all commands.</p>
<dt><code>&#8211;enghelp</code><i></i>=ioengine[,command]</p>
<dd> List all commands defined by <i>ioengine</i>, or print help for <i>command</i> defined by <i>ioengine</i>.</p>
<dt><code>&#8211;showcmd</code><i></i>=jobfile</p>
<dd> Convert <i>jobfile</i> to a set of command-line options.</p>
<dt><code>&#8211;eta</code><i></i>=when</p>
<dd> Specifies when real-time ETA estimate should be printed. <i>when</i> may be one of `always&#8217;, `never&#8217; or `auto&#8217;.</p>
<dt><code>&#8211;eta-newline</code><i></i>=time</p>
<dd> Force an ETA newline for every `time` period passed.</p>
<dt><code>&#8211;status-interval</code><i></i>=time</p>
<dd> Report full output status every `time` period passed.</p>
<dt><code>&#8211;readonly</code></p>
<dd> Turn on safety read-only checks, preventing any attempted write.</p>
<dt><code>&#8211;section</code><i></i>=sec</p>
<dd> Only run section <i>sec</i> from job file. This option can be used multiple times to add more sections to run.</p>
<dt><code>&#8211;alloc-size</code><i></i>=kb</p>
<dd> Set the internal smalloc pool size to <i>kb</i> kilobytes.</p>
<dt><code>&#8211;warnings-fatal</code></p>
<dd> All fio parser warnings are fatal, causing fio to exit with an error.</p>
<dt><code>&#8211;max-jobs</code><i></i>=nr</p>
<dd> Set the maximum allowed number of jobs (threads/processes) to support.</p>
<dt><code>&#8211;server</code><i></i>=args</p>
<dd> Start a backend server, with <i>args</i> specifying what to listen to. See client/server section.</p>
<dt><code>&#8211;daemonize</code><i></i>=pidfile</p>
<dd> Background a fio server, writing the pid to the given pid file.</p>
<dt><code>&#8211;client</code><i></i>=host</p>
<dd> Instead of running the jobs locally, send and run them on the given host or set of hosts. See client/server section.</p>
<dt><code>&#8211;idle-prof</code><i></i>=option</p>
<dd> Report cpu idleness on a system or percpu basis (<i>option</i>=system,percpu) or run unit work calibration only (<i>option</i>=calibrate).</dl>
<h2>JOB FILE FORMAT</h2>
<p> Job files are in `ini&#8217; format. They consist of one or more job definitions, which begin with a job name in square brackets and extend to the next job name. The job name can be any ASCII string except `global&#8217;, which has a special meaning. Following the job name is a sequence of zero or more parameters, one per line, that define the behavior of the job. Any line starting with a `;&#8217; or `#&#8217; character is considered a comment and ignored. </p>
<p> If <i>jobfile</i> is specified as `-&#8216;, the job file will be read from standard input.</p>
<h3>Global Section</h3>
<p> The global section contains default parameters for jobs specified in the job file. A job is only affected by global sections residing above it, and there may be any number of global sections. Specific job definitions may override any parameter set in global sections.</p>
<h2>JOB PARAMETERS</h2>
<h3>Types</h3>
<p> Some parameters may take arguments of a specific type. Anywhere a numeric value is required, an arithmetic expression may be used, provided it is surrounded by parentheses. Supported operators are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>addition (+)</code></p>
<dd>
<dt><code>subtraction (-)</code></p>
<dd>
<dt><code>multiplication (*)</code></p>
<dd>
<dt><code>division (/)</code></p>
<dd>
<dt><code>modulus (%)</code></p>
<dd>
<dt><code>exponentiation (^)</code></p>
<dd></dl>
</dl>
</dl>
<p> For time values in expressions, units are microseconds by default. This is different than for time values not in expressions (not enclosed in parentheses). The types used are:</p>
<dl>
<dt><i>str</i></p>
<dd> String: a sequence of alphanumeric characters.</p>
<dt><i>int</i></p>
<dd> SI integer: a whole number, possibly containing a suffix denoting the base unit of the value. Accepted suffixes are `k&#8217;, &#8216;M&#8217;, &#8216;G&#8217;, &#8216;T&#8217;, and &#8216;P&#8217;, denoting kilo (1024), mega (1024^2), giga (1024^3), tera (1024^4), and peta (1024^5) respectively. If prefixed with &#8216;0x&#8217;, the value is assumed to be base 16 (hexadecimal). A suffix may include a trailing &#8216;b&#8217;, for instance &#8216;kb&#8217; is identical to &#8216;k&#8217;. You can specify a base 10 value by using &#8216;KiB&#8217;, &#8216;MiB&#8217;,&#8217;GiB&#8217;, etc. This is useful for disk drives where values are often given in base 10 values. Specifying &#8217;30GiB&#8217; will get you 30*1000^3 bytes. When specifying times the default suffix meaning changes, still denoting the base unit of the value, but accepted suffixes are &#8216;D&#8217; (days), &#8216;H&#8217; (hours), &#8216;M&#8217; (minutes), &#8216;S&#8217; Seconds, &#8216;ms&#8217; (or msec) milli seconds, &#8216;us&#8217; (or &#8216;usec&#8217;) micro seconds. Time values without a unit specify seconds. The suffixes are not case sensitive.</p>
<dt><i>bool</i></p>
<dd> Boolean: a true or false value. `0&#8242; denotes false, `1&#8242; denotes true.</p>
<dt><i>irange</i></p>
<dd> Integer range: a range of integers specified in the format <i>lower</i>:<i>upper</i> or <i>lower</i>&#8211;<i>upper</i>. <i>lower</i> and <i>upper</i> may contain a suffix as described above. If an option allows two sets of ranges, they are separated with a `,&#8217; or `/&#8217; character. For example: `8-8k/8M-4G&#8217;.</p>
<dt><i>float_list</i></p>
<dd> List of floating numbers: A list of floating numbers, separated by a &#8216;:&#8217; character.</dl>
<h3>Parameter List</h3>
<dl>
<dt><code>name</code><i></i>=str</p>
<dd> May be used to override the job name. On the command line, this parameter has the special purpose of signalling the start of a new job.</p>
<dt><code>description</code><i></i>=str</p>
<dd> Human-readable description of the job. It is printed when the job is run, but otherwise has no special purpose.</p>
<dt><code>directory</code><i></i>=str</p>
<dd> Prefix filenames with this directory. Used to place files in a location other than `./&#8217;. You can specify a number of directories by separating the names with a &#8216;:&#8217; character. These directories will be assigned equally distributed to job clones creates with <i>numjobs</i> as long as they are using generated filenames. If specific <i>filename(s)</i> are set fio will use the first listed directory, and thereby matching the <i>filename</i> semantic which generates a file each clone if not specified, but let all clones use the same if set. See <i>filename</i> for considerations regarding escaping certain characters on some platforms.</p>
<dt><code>filename</code><i></i>=str</p>
<dd> <code>fio</code> normally makes up a file name based on the job name, thread number, and file number. If you want to share files between threads in a job or several jobs, specify a <i>filename</i> for each of them to override the default. If the I/O engine is file-based, you can specify a number of files by separating the names with a `:&#8217; character. `-&#8216; is a reserved name, meaning stdin or stdout, depending on the read/write direction set. On Windows, disk devices are accessed as \.PhysicalDrive0 for the first device, \.PhysicalDrive1 for the second etc. Note: Windows and FreeBSD prevent write access to areas of the disk containing in-use data (e.g. filesystems). If the wanted filename does need to include a colon, then escape that with a &#8216;\&#8217; character. For instance, if the filename is &quot;/dev/dsk/foo@3,0:c&quot;, then you would use filename=&quot;/dev/dsk/foo@3,0\:c&quot;.</p>
<dt><code>filename_format</code><i></i>=str</p>
<dd> If sharing multiple files between jobs, it is usually necessary to have fio generate the exact names that you want. By default, fio will name a file based on the default file format specification of <code>jobname.jobnumber.filenumber</code>. With this option, that can be customized. Fio will recognize and replace the following keywords in this string:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>$jobname</code></p>
<dd> The name of the worker thread or process.</p>
<dt><code>$jobnum</code></p>
<dd> The incremental number of the worker thread or process.</p>
<dt><code>$filenum</code></p>
<dd> The incremental number of the file for that worker thread or process.</dl>
</dl>
<p> To have dependent jobs share a set of files, this option can be set to have fio generate filenames that are shared between the two. For instance, if <code>testfiles.$filenum</code> is specified, file number 4 for any job will be named <code>testfiles.4</code>. The default of <code>$jobname.$jobnum.$filenum</code> will be used if no other format specifier is given.</dl>
</dl>
<dl>
<dt><code>lockfile</code><i></i>=str</p>
<dd> Fio defaults to not locking any files before it does IO to them. If a file or file descriptor is shared, fio can serialize IO to that file to make the end result consistent. This is usual for emulating real workloads that share files. The lock modes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> No locking. This is the default.</p>
<dt><code>exclusive</code></p>
<dd> Only one thread or process may do IO at a time, excluding all others.</p>
<dt><code>readwrite</code></p>
<dd> Read-write locking on the file. Many readers may access the file at the same time, but writes get exclusive access.</dl>
</dl>
</dl>
</dl>
<p> <code>opendir</code><i></i>=str Recursively open any files below directory <i>str</i>.</p>
<dl>
<dt><code>readwrite</code><i></i>=str, rw<i></i>=str</p>
<dd> Type of I/O pattern. Accepted values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>read</code></p>
<dd> Sequential reads.</p>
<dt><code>write</code></p>
<dd> Sequential writes.</p>
<dt><code>trim</code></p>
<dd> Sequential trim (Linux block devices only).</p>
<dt><code>randread</code></p>
<dd> Random reads.</p>
<dt><code>randwrite</code></p>
<dd> Random writes.</p>
<dt><code>randtrim</code></p>
<dd> Random trim (Linux block devices only).</p>
<dt><code>rw, readwrite</code></p>
<dd> Mixed sequential reads and writes.</p>
<dt><code>randrw </code></p>
<dd> Mixed random reads and writes.</p>
<dt><code>trimwrite</code></p>
<dd> Trim and write mixed workload. Blocks will be trimmed first, then the same blocks will be written to.</dl>
</dl>
<p> For mixed I/O, the default split is 50/50. For certain types of io the result may still be skewed a bit, since the speed may be different. It is possible to specify a number of IO&#8217;s to do before getting a new offset, this is done by appending a `:<i>&lt;nr&gt;</i> to the end of the string given. For a random read, it would look like <code>rw=randread:8</code> for passing in an offset modifier with a value of 8. If the postfix is used with a sequential IO pattern, then the value specified will be added to the generated offset for each IO. For instance, using <code>rw=write:4k</code> will skip 4k for every write. It turns sequential IO into sequential IO with holes. See the <code>rw_sequencer</code> option.</dl>
<dt><code>rw_sequencer</code><i></i>=str</p>
<dd> If an offset modifier is given by appending a number to the <code>rw=&lt;str&gt;</code> line, then this option controls how that number modifies the IO offset being generated. Accepted values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>sequential</code></p>
<dd> Generate sequential offset</p>
<dt><code>identical</code></p>
<dd> Generate the same offset</dl>
</dl>
<p> <code>sequential</code> is only useful for random IO, where fio would normally generate a new random offset for every IO. If you append eg 8 to randread, you would get a new random offset for every 8 IO&#8217;s. The result would be a seek for only every 8 IO&#8217;s, instead of for every IO. Use <code>rw=randread:8</code> to specify that. As sequential IO is already sequential, setting <code>sequential</code> for that would not result in any differences. <code>identical</code> behaves in a similar fashion, except it sends the same offset 8 number of times before generating a new offset.</dl>
</dl>
<dl>
<dt><code>kb_base</code><i></i>=int</p>
<dd> The base unit for a kilobyte. The defacto base is 2^10, 1024. Storage manufacturers like to use 10^3 or 1000 as a base ten unit instead, for obvious reasons. Allowed values are 1024 or 1000, with 1024 being the default.</p>
<dt><code>unified_rw_reporting</code><i></i>=bool</p>
<dd> Fio normally reports statistics on a per data direction basis, meaning that read, write, and trim are accounted and reported separately. If this option is set fio sums the results and reports them as &quot;mixed&quot; instead.</p>
<dt><code>randrepeat</code><i></i>=bool</p>
<dd> Seed the random number generator used for random I/O patterns in a predictable way so the pattern is repeatable across runs. Default: true.</p>
<dt><code>allrandrepeat</code><i></i>=bool</p>
<dd> Seed all random number generators in a predictable way so results are repeatable across runs. Default: false.</p>
<dt><code>randseed</code><i></i>=int</p>
<dd> Seed the random number generators based on this seed value, to be able to control what sequence of output is being generated. If not set, the random sequence depends on the <code>randrepeat</code> setting.</p>
<dt><code>fallocate</code><i></i>=str</p>
<dd> Whether pre-allocation is performed when laying down files. Accepted values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Do not pre-allocate space.</p>
<dt><code>posix</code></p>
<dd> Pre-allocate via <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3).</p>
<dt><code>keep</code></p>
<dd> Pre-allocate via <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) with FALLOC_FL_KEEP_SIZE set.</p>
<dt><code>0</code></p>
<dd> Backward-compatible alias for &#8216;none&#8217;.</p>
<dt><code>1</code></p>
<dd> Backward-compatible alias for &#8216;posix&#8217;.</dl>
</dl>
<p> May not be available on all supported platforms. &#8216;keep&#8217; is only available on Linux. If using ZFS on Solaris this must be set to &#8216;none&#8217; because ZFS doesn&#8217;t support it. Default: &#8216;posix&#8217;.</dl>
<dt><code>fadvise_hint</code><i></i>=bool</p>
<dd> Use <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2) to advise the kernel what I/O patterns are likely to be issued. Default: true.</p>
<dt><code>fadvise_stream</code><i></i>=int</p>
<dd> Use <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2) to advise the kernel what stream ID the writes issued belong to. Only supported on Linux. Note, this option may change going forward.</p>
<dt><code>size</code><i></i>=int</p>
<dd> Total size of I/O for this job. <code>fio</code> will run until this many bytes have been transferred, unless limited by other options (<code>runtime</code>, for instance, or increased/descreased by <code>io_size</code>). Unless <code>nrfiles</code> and <code>filesize</code> options are given, this amount will be divided between the available files for the job. If not set, fio will use the full size of the given files or devices. If the files do not exist, size must be given. It is also possible to give size as a percentage between 1 and 100. If size=20% is given, fio will use 20% of the full size of the given files or devices.</p>
<dt><code>io_size</code><i></i>=int,<code> io_limit </code>=int</p>
<dd> Normally fio operates within the region set by <code>size</code>, which means that the <code>size</code> option sets both the region and size of IO to be performed. Sometimes that is not what you want. With this option, it is possible to define just the amount of IO that fio should do. For instance, if <code>size</code> is set to 20G and <code>io_limit</code> is set to 5G, fio will perform IO within the first 20G but exit when 5G have been done. The opposite is also possible &#8211; if <code>size</code> is set to 20G, and <code>io_size</code> is set to 40G, then fio will do 40G of IO within the 0..20G region.</p>
<dt><code>fill_device</code><i></i>=bool,<code> fill_fs</code><i></i>=bool</p>
<dd> Sets size to something really large and waits for ENOSPC (no space left on device) as the terminating condition. Only makes sense with sequential write. For a read workload, the mount point will be filled first then IO started on the result. This option doesn&#8217;t make sense if operating on a raw device node, since the size of that is already known by the file system. Additionally, writing beyond end-of-device will not return ENOSPC there.</p>
<dt><code>filesize</code><i></i>=irange</p>
<dd> Individual file sizes. May be a range, in which case <code>fio</code> will select sizes for files at random within the given range, limited to <code>size</code> in total (if that is given). If <code>filesize</code> is not specified, each created file is the same size.</p>
<dt><code>file_append</code><i></i>=bool</p>
<dd> Perform IO after the end of the file. Normally fio will operate within the size of a file. If this option is set, then fio will append to the file instead. This has identical behavior to setting offset to the size of a file. This option is ignored on non-regular files.</p>
<dt><code>blocksize</code><i></i>=int[,int],<code> bs</code><i></i>=int[,int]</p>
<dd> Block size for I/O units. Default: 4k. Values for reads, writes, and trims can be specified separately in the format <i>read</i>,<i>write</i>,<i>trim</i> either of which may be empty to leave that value at its default. If a trailing comma isn&#8217;t given, the remainder will inherit the last value set.</p>
<dt><code>blocksize_range</code><i></i>=irange[,irange],<code> bsrange</code><i></i>=irange[,irange]</p>
<dd> Specify a range of I/O block sizes. The issued I/O unit will always be a multiple of the minimum size, unless <code>blocksize_unaligned</code> is set. Applies to both reads and writes if only one range is given, but can be specified separately with a comma separating the values. Example: bsrange=1k-4k,2k-8k. Also (see <code>blocksize</code>).</p>
<dt><code>bssplit</code><i></i>=str</p>
<dd> This option allows even finer grained control of the block sizes issued, not just even splits between them. With this option, you can weight various block sizes for exact control of the issued IO for a job that has mixed block sizes. The format of the option is bssplit=blocksize/percentage, optionally adding as many definitions as needed separated by a colon. Example: bssplit=4k/10:64k/50:32k/40 would issue 50% 64k blocks, 10% 4k blocks and 40% 32k blocks. <code>bssplit</code> also supports giving separate splits to reads and writes. The format is identical to what the <code>bs</code> option accepts, the read and write parts are separated with a comma.</p>
<dt><code>blocksize_unaligned</code>, bs_unaligned</p>
<dd> If set, any size in <code>blocksize_range</code> may be used. This typically won&#8217;t work with direct I/O, as that normally requires sector alignment.</p>
<dt><code>blockalign</code><i></i>=int[,int],<code> ba</code><i></i>=int[,int]</p>
<dd> At what boundary to align random IO offsets. Defaults to the same as &#8216;blocksize&#8217; the minimum blocksize given. Minimum alignment is typically 512b for using direct IO, though it usually depends on the hardware block size. This option is mutually exclusive with using a random map for files, so it will turn off that option.</p>
<dt><code>bs_is_seq_rand</code><i></i>=bool</p>
<dd> If this option is set, fio will use the normal read,write blocksize settings as sequential,random instead. Any random read or write will use the WRITE blocksize settings, and any sequential read or write will use the READ blocksize setting.</p>
<dt><code>zero_buffers</code></p>
<dd> Initialize buffers with all zeros. Default: fill buffers with random data.</p>
<dt><code>refill_buffers</code></p>
<dd> If this option is given, fio will refill the IO buffers on every submit. The default is to only fill it at init time and reuse that data. Only makes sense if zero_buffers isn&#8217;t specified, naturally. If data verification is enabled, refill_buffers is also automatically enabled.</p>
<dt><code>scramble_buffers</code><i></i>=bool</p>
<dd> If <code>refill_buffers</code> is too costly and the target is using data deduplication, then setting this option will slightly modify the IO buffer contents to defeat normal de-dupe attempts. This is not enough to defeat more clever block compression attempts, but it will stop naive dedupe of blocks. Default: true.</p>
<dt><code>buffer_compress_percentage</code><i></i>=int</p>
<dd> If this is set, then fio will attempt to provide IO buffer content (on WRITEs) that compress to the specified level. Fio does this by providing a mix of random data and a fixed pattern. The fixed pattern is either zeroes, or the pattern specified by <code>buffer_pattern</code>. If the pattern option is used, it might skew the compression ratio slightly. Note that this is per block size unit, for file/disk wide compression level that matches this setting. Note that this is per block size unit, for file/disk wide compression level that matches this setting, you&#8217;ll also want to set refill_buffers.</p>
<dt><code>buffer_compress_chunk</code><i></i>=int</p>
<dd> See <code>buffer_compress_percentage</code>. This setting allows fio to manage how big the ranges of random data and zeroed data is. Without this set, fio will provide <code>buffer_compress_percentage</code> of blocksize random data, followed by the remaining zeroed. With this set to some chunk size smaller than the block size, fio can alternate random and zeroed data throughout the IO buffer.</p>
<dt><code>buffer_pattern</code><i></i>=str</p>
<dd> If set, fio will fill the IO buffers with this pattern. If not set, the contents of IO buffers is defined by the other options related to buffer contents. The setting can be any pattern of bytes, and can be prefixed with 0x for hex values. It may also be a string, where the string must then be wrapped with &quot;&quot;, e.g.:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>buffer_pattern</code>=&quot;abcd&quot;</p>
<dl>
<dt>
<dd> or</dl>
<p> <code>buffer_pattern</code>=-12</p>
<dl>
<dt>
<dd> or</dl>
<p> <code>buffer_pattern</code>=0xdeadface</dl>
<p> Also you can combine everything together in any order: </p>
<dl>
<dt>
<dd> <code>buffer_pattern</code>=0xdeadface&quot;abcd&quot;-12</dl>
</dl>
<dt><code>dedupe_percentage</code><i></i>=int</p>
<dd> If set, fio will generate this percentage of identical buffers when writing. These buffers will be naturally dedupable. The contents of the buffers depend on what other buffer compression settings have been set. It&#8217;s possible to have the individual buffers either fully compressible, or not at all. This option only controls the distribution of unique buffers.</p>
<dt><code>nrfiles</code><i></i>=int</p>
<dd> Number of files to use for this job. Default: 1.</p>
<dt><code>openfiles</code><i></i>=int</p>
<dd> Number of files to keep open at the same time. Default: <code>nrfiles</code>.</p>
<dt><code>file_service_type</code><i></i>=str</p>
<dd> Defines how files to service are selected. The following types are defined:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>random</code></p>
<dd> Choose a file at random.</p>
<dt><code>roundrobin</code></p>
<dd> Round robin over opened files (default).</p>
<dt><code>sequential</code></p>
<dd> Do each file in the set sequentially.</dl>
</dl>
<p> The number of I/Os to issue before switching to a new file can be specified by appending `:<i>int</i>&#8216; to the service type.</dl>
<dt><code>ioengine</code><i></i>=str</p>
<dd> Defines how the job issues I/O. The following types are defined:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>sync</code></p>
<dd> Basic <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) I/O. <code><a href="/docs/linux/man/2-fseek/">fseek</a></code>(2) is used to position the I/O location.</p>
<dt><code>psync</code></p>
<dd> Basic <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2) or <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2) I/O.</p>
<dt><code>vsync</code></p>
<dd> Basic <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2) or <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2) I/O. Will emulate queuing by coalescing adjacent IOs into a single submission.</p>
<dt><code>pvsync</code></p>
<dd> Basic <code><a href="/docs/linux/man/2-preadv/">preadv</a></code>(2) or <code><a href="/docs/linux/man/2-pwritev/">pwritev</a></code>(2) I/O.</p>
<dt><code>libaio</code></p>
<dd> Linux native asynchronous I/O. This ioengine defines engine specific options.</p>
<dt><code>posixaio</code></p>
<dd> POSIX asynchronous I/O using <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3) and <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3).</p>
<dt><code>solarisaio</code></p>
<dd> Solaris native asynchronous I/O.</p>
<dt><code>windowsaio</code></p>
<dd> Windows native asynchronous I/O.</p>
<dt><code>mmap</code></p>
<dd> File is memory mapped with <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) and data copied using <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3).</p>
<dt><code>splice</code></p>
<dd> <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) is used to transfer the data and <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2) to transfer data from user-space to the kernel.</p>
<dt><code>syslet-rw</code></p>
<dd> Use the syslet system calls to make regular read/write asynchronous.</p>
<dt><code>sg</code></p>
<dd> SCSI generic sg v3 I/O. May be either synchronous using the SG_IO ioctl, or if the target is an sg character device, we use <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) for asynchronous I/O.</p>
<dt><code>null</code></p>
<dd> Doesn&#8217;t transfer any data, just pretends to. Mainly used to exercise <code>fio</code> itself and for debugging and testing purposes.</p>
<dt><code>net</code></p>
<dd> Transfer over the network. The protocol to be used can be defined with the <code>protocol</code> parameter. Depending on the protocol, <code>filename</code>, <code>hostname</code>, <code>port</code>, or <code>listen</code> must be specified. This ioengine defines engine specific options.</p>
<dt><code>netsplice</code></p>
<dd> Like <code>net</code>, but uses <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) and <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2) to map data and send/receive. This ioengine defines engine specific options.</p>
<dt><code>cpuio</code></p>
<dd> Doesn&#8217;t transfer any data, but burns CPU cycles according to <code>cpuload</code> and <code>cpucycles</code> parameters.</p>
<dt><code>guasi</code></p>
<dd> The GUASI I/O engine is the Generic Userspace Asynchronous Syscall Interface approach to asynchronous I/O.<br />
 See &lt;<a rel="nofollow" href="http://www.xmailserver.org/guasi-lib.html">http://www.xmailserver.org/guasi-lib.html</a>&gt;.</p>
<dt><code>rdma</code></p>
<dd> The RDMA I/O engine supports both RDMA memory semantics (RDMA_WRITE/RDMA_READ) and channel semantics (Send/Recv) for the InfiniBand, RoCE and iWARP protocols.</p>
<dt><code>external</code></p>
<dd> Loads an external I/O engine object file. Append the engine filename as `:<i>enginepath</i>&#8216;.</p>
<dt><code>falloc</code></p>
<dd>
IO engine that does regular linux native fallocate call to simulate data transfer as fio ioengine </p>
<p>&nbsp;<wbr>&nbsp;<wbr>DDIR_READ&nbsp;<wbr>&nbsp;<wbr>does fallocate(,mode&nbsp;<wbr>=&nbsp;<wbr>FALLOC_FL_KEEP_SIZE,) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>DIR_WRITE does fallocate(,mode&nbsp;<wbr>=&nbsp;<wbr>0) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>DDIR_TRIM does fallocate(,mode&nbsp;<wbr>=&nbsp;<wbr>FALLOC_FL_KEEP_SIZE|FALLOC_FL_PUNCH_HOLE)</p>
<dt><code>e4defrag</code></p>
<dd> IO engine that does regular EXT4_IOC_MOVE_EXT ioctls to simulate defragment activity request to DDIR_WRITE event</p>
<dt><code>rbd</code></p>
<dd> IO engine supporting direct access to Ceph Rados Block Devices (RBD) via librbd without the need to use the kernel rbd driver. This ioengine defines engine specific options.</p>
<dt><code>gfapi</code></p>
<dd> Using Glusterfs libgfapi sync interface to direct access to Glusterfs volumes without having to go through FUSE. This ioengine defines engine specific options.</p>
<dt><code>gfapi_async</code></p>
<dd> Using Glusterfs libgfapi async interface to direct access to Glusterfs volumes without having to go through FUSE. This ioengine defines engine specific options.</p>
<dt><code>libhdfs</code></p>
<dd> Read and write through Hadoop (HDFS). The <code>filename</code> option is used to specify host,port of the hdfs name-node to connect. This engine interprets offsets a little differently. In HDFS, files once created cannot be modified. So random writes are not possible. To imitate this, libhdfs engine expects bunch of small files to be created over HDFS, and engine will randomly pick a file out of those files based on the offset generated by fio backend. (see the example job file to create such files, use rw=write option). Please note, you might want to set necessary environment variables to work with hdfs/libhdfs properly.</p>
<dt><code>mtd</code></p>
<dd> Read, write and erase an MTD character device (e.g., /dev/mtd0). Discards are treated as erases. Depending on the underlying device type, the I/O may have to go in a certain pattern, e.g., on NAND, writing sequentially to erase blocks and discarding before overwriting. The writetrim mode works well for this constraint.</dl>
</dl>
</dl>
<dt><code>iodepth</code><i></i>=int</p>
<dd> Number of I/O units to keep in flight against the file. Note that increasing iodepth beyond 1 will not affect synchronous ioengines (except for small degress when verify_async is in use). Even async engines may impose OS restrictions causing the desired depth not to be achieved. This may happen on Linux when using libaio and not setting <code>direct</code>=1, since buffered IO is not async on that OS. Keep an eye on the IO depth distribution in the fio output to verify that the achieved depth is as expected. Default: 1.</p>
<dt><code>iodepth_batch</code><i></i>=int</p>
<dd> Number of I/Os to submit at once. Default: <code>iodepth</code>.</p>
<dt><code>iodepth_batch_complete</code><i></i>=int</p>
<dd> This defines how many pieces of IO to retrieve at once. It defaults to 1 which<br />
&nbsp;<wbr>means that we&#8217;ll ask for a minimum of 1 IO in the retrieval process from the kernel. The IO retrieval will go on until we hit the limit set by <code>iodepth_low</code>. If this variable is set to 0, then fio will always check for completed events before queuing more IO. This helps reduce IO latency, at the cost of more retrieval system calls.</p>
<dt><code>iodepth_low</code><i></i>=int</p>
<dd> Low watermark indicating when to start filling the queue again. Default: <code>iodepth</code>.</p>
<dt><code>io_submit_mode</code><i></i>=str</p>
<dd> This option controls how fio submits the IO to the IO engine. The default is <code>inline</code>, which means that the fio job threads submit and reap IO directly. If set to <code>offload</code>, the job threads will offload IO submission to a dedicated pool of IO threads. This requires some coordination and thus has a bit of extra overhead, especially for lower queue depth IO where it can increase latencies. The benefit is that fio can manage submission rates independently of the device completion rates. This avoids skewed latency reporting if IO gets back up on the device side (the coordinated omission problem).</p>
<dt><code>direct</code><i></i>=bool</p>
<dd> If true, use non-buffered I/O (usually O_DIRECT). Default: false.</p>
<dt><code>atomic</code><i></i>=bool</p>
<dd> If value is true, attempt to use atomic direct IO. Atomic writes are guaranteed to be stable once acknowledged by the operating system. Only Linux supports O_ATOMIC right now.</p>
<dt><code>buffered</code><i></i>=bool</p>
<dd> If true, use buffered I/O. This is the opposite of the <code>direct</code> parameter. Default: true.</p>
<dt><code>offset</code><i></i>=int</p>
<dd> Offset in the file to start I/O. Data before the offset will not be touched.</p>
<dt><code>offset_increment</code><i></i>=int</p>
<dd> If this is provided, then the real offset becomes the offset + offset_increment * thread_number, where the thread number is a counter that starts at 0 and is incremented for each sub-job (i.e. when numjobs option is specified). This option is useful if there are several jobs which are intended to operate on a file in parallel disjoint segments, with even spacing between the starting points.</p>
<dt><code>number_ios</code><i></i>=int</p>
<dd> Fio will normally perform IOs until it has exhausted the size of the region set by <code>size</code>, or if it exhaust the allocated time (or hits an error condition). With this setting, the range/size can be set independently of the number of IOs to perform. When fio reaches this number, it will exit normally and report status. Note that this does not extend the amount of IO that will be done, it will only stop fio if this condition is met before other end-of-job criteria.</p>
<dt><code>fsync</code><i></i>=int</p>
<dd> How many I/Os to perform before issuing an <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) of dirty data. If 0, don&#8217;t sync. Default: 0.</p>
<dt><code>fdatasync</code><i></i>=int</p>
<dd> Like <code>fsync</code>, but uses <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) instead to only sync the data parts of the file. Default: 0.</p>
<dt><code>write_barrier</code><i></i>=int</p>
<dd> Make every Nth write a barrier write.</p>
<dt><code>sync_file_range</code><i></i>=str:int</p>
<dd> Use <code><a href="/docs/linux/man/2-sync_file_range/">sync_file_range</a></code>(2) for every val number of write operations. Fio will track range of writes that have happened since the last <code><a href="/docs/linux/man/2-sync_file_range/">sync_file_range</a></code>(2) call. str can currently be one or more of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>wait_before</code></p>
<dd> SYNC_FILE_RANGE_WAIT_BEFORE</p>
<dt><code>write</code></p>
<dd> SYNC_FILE_RANGE_WRITE</p>
<dt><code>wait_after</code></p>
<dd> SYNC_FILE_RANGE_WRITE</p>
<dt></dl>
</dl>
<dd></dl>
<p> So if you do sync_file_range=wait_before,write:8, fio would use <code>SYNC_FILE_RANGE_WAIT_BEFORE | SYNC_FILE_RANGE_WRITE</code> for every 8 writes. Also see the <code><a href="/docs/linux/man/2-sync_file_range/">sync_file_range</a></code>(2) man page. This option is Linux specific.</p>
<dl>
<dt><code>overwrite</code><i></i>=bool</p>
<dd> If writing, setup the file first and do overwrites. Default: false.</p>
<dt><code>end_fsync</code><i></i>=bool</p>
<dd> Sync file contents when a write stage has completed. Default: false.</p>
<dt><code>fsync_on_close</code><i></i>=bool</p>
<dd> If true, sync file contents on close. This differs from <code>end_fsync</code> in that it will happen on every close, not just at the end of the job. Default: false.</p>
<dt><code>rwmixread</code><i></i>=int</p>
<dd> Percentage of a mixed workload that should be reads. Default: 50.</p>
<dt><code>rwmixwrite</code><i></i>=int</p>
<dd> Percentage of a mixed workload that should be writes. If <code>rwmixread</code> and <code>rwmixwrite</code> are given and do not sum to 100%, the latter of the two overrides the first. This may interfere with a given rate setting, if fio is asked to limit reads or writes to a certain rate. If that is the case, then the distribution may be skewed. Default: 50.</p>
<dt><code>random_distribution</code><i></i>=str:float</p>
<dd> By default, fio will use a completely uniform random distribution when asked to perform random IO. Sometimes it is useful to skew the distribution in specific ways, ensuring that some parts of the data is more hot than others. Fio includes the following distribution models:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>random</code></p>
<dd> Uniform random distribution</p>
<dt><code>zipf</code></p>
<dd> Zipf distribution</p>
<dt><code>pareto</code></p>
<dd> Pareto distribution</p>
<dt></dl>
</dl>
<dd></dl>
<p> When using a zipf or pareto distribution, an input value is also needed to define the access pattern. For zipf, this is the zipf theta. For pareto, it&#8217;s the pareto power. Fio includes a test program, genzipf, that can be used visualize what the given input values will yield in terms of hit rates. If you wanted to use zipf with a theta of 1.2, you would use random_distribution=zipf:1.2 as the option. If a non-uniform model is used, fio will disable use of the random map.</p>
<dl>
<dt><code>percentage_random</code><i></i>=int</p>
<dd> For a random workload, set how big a percentage should be random. This defaults to 100%, in which case the workload is fully random. It can be set from anywhere from 0 to 100. Setting it to 0 would make the workload fully sequential. It is possible to set different values for reads, writes, and trim. To do so, simply use a comma separated list. See <code>blocksize</code>.</p>
<dt><code>norandommap</code></p>
<dd> Normally <code>fio</code> will cover every block of the file when doing random I/O. If this parameter is given, a new offset will be chosen without looking at past I/O history. This parameter is mutually exclusive with <code>verify</code>.</p>
<dt><code>softrandommap</code><i></i>=bool</p>
<dd> See <code>norandommap</code>. If fio runs with the random block map enabled and it fails to allocate the map, if this option is set it will continue without a random block map. As coverage will not be as complete as with random maps, this option is disabled by default.</p>
<dt><code>random_generator</code><i></i>=str</p>
<dd> Fio supports the following engines for generating IO offsets for random IO:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>tausworthe</code></p>
<dd> Strong 2^88 cycle random number generator</p>
<dt><code>lfsr</code></p>
<dd> Linear feedback shift register generator</p>
<dt><code>tausworthe64</code></p>
<dd> Strong 64-bit 2^258 cycle random number generator</p>
<dt></dl>
</dl>
<dd></dl>
<p> Tausworthe is a strong random number generator, but it requires tracking on the side if we want to ensure that blocks are only read or written once. LFSR guarantees that we never generate the same offset twice, and it&#8217;s also less computationally expensive. It&#8217;s not a true random generator, however, though for IO purposes it&#8217;s typically good enough. LFSR only works with single block sizes, not with workloads that use multiple block sizes. If used with such a workload, fio may read or write some blocks multiple times.</p>
<dl>
<dt><code>nice</code><i></i>=int</p>
<dd> Run job with given nice value. See <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2).</p>
<dt><code>prio</code><i></i>=int</p>
<dd> Set I/O priority value of this job between 0 (highest) and 7 (lowest). See <code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1).</p>
<dt><code>prioclass</code><i></i>=int</p>
<dd> Set I/O priority class. See <code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1).</p>
<dt><code>thinktime</code><i></i>=int</p>
<dd> Stall job for given number of microseconds between issuing I/Os.</p>
<dt><code>thinktime_spin</code><i></i>=int</p>
<dd> Pretend to spend CPU time for given number of microseconds, sleeping the rest of the time specified by <code>thinktime</code>. Only valid if <code>thinktime</code> is set.</p>
<dt><code>thinktime_blocks</code><i></i>=int</p>
<dd> Only valid if thinktime is set &#8211; control how many blocks to issue, before waiting <code>thinktime</code> microseconds. If not set, defaults to 1 which will make fio wait <code>thinktime</code> microseconds after every block. This effectively makes any queue depth setting redundant, since no more than 1 IO will be queued before we have to complete it and do our thinktime. In other words, this setting effectively caps the queue depth if the latter is larger. Default: 1.</p>
<dt><code>rate</code><i></i>=int</p>
<dd> Cap bandwidth used by this job. The number is in bytes/sec, the normal postfix rules apply. You can use <code>rate</code>=500k to limit reads and writes to 500k each, or you can specify read and writes separately. Using <code>rate</code>=1m,500k would limit reads to 1MB/sec and writes to 500KB/sec. Capping only reads or writes can be done with <code>rate</code>=,500k or <code>rate</code>=500k,. The former will only limit writes (to 500KB/sec), the latter will only limit reads.</p>
<dt><code>ratemin</code><i></i>=int</p>
<dd> Tell <code>fio</code> to do whatever it can to maintain at least the given bandwidth. Failing to meet this requirement will cause the job to exit. The same format as <code>rate</code> is used for read vs write separation.</p>
<dt><code>rate_iops</code><i></i>=int</p>
<dd> Cap the bandwidth to this number of IOPS. Basically the same as rate, just specified independently of bandwidth. The same format as <code>rate</code> is used for read vs write separation. If <code>blocksize</code> is a range, the smallest block size is used as the metric.</p>
<dt><code>rate_iops_min</code><i></i>=int</p>
<dd> If this rate of I/O is not met, the job will exit. The same format as <code>rate</code> is used for read vs write separation.</p>
<dt><code>ratecycle</code><i></i>=int</p>
<dd> Average bandwidth for <code>rate</code> and <code>ratemin</code> over this number of milliseconds. Default: 1000ms.</p>
<dt><code>latency_target</code><i></i>=int</p>
<dd> If set, fio will attempt to find the max performance point that the given workload will run at while maintaining a latency below this target. The values is given in microseconds. See <code>latency_window</code> and <code>latency_percentile</code>.</p>
<dt><code>latency_window</code><i></i>=int</p>
<dd> Used with <code>latency_target</code> to specify the sample window that the job is run at varying queue depths to test the performance. The value is given in microseconds.</p>
<dt><code>latency_percentile</code><i></i>=float</p>
<dd> The percentage of IOs that must fall within the criteria specified by <code>latency_target</code> and <code>latency_window</code>. If not set, this defaults to 100.0, meaning that all IOs must be equal or below to the value set by <code>latency_target</code>.</p>
<dt><code>max_latency</code><i></i>=int</p>
<dd> If set, fio will exit the job if it exceeds this maximum latency. It will exit with an ETIME error.</p>
<dt><code>cpumask</code><i></i>=int</p>
<dd> Set CPU affinity for this job. <i>int</i> is a bitmask of allowed CPUs the job may run on. See <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2).</p>
<dt><code>cpus_allowed</code><i></i>=str</p>
<dd> Same as <code>cpumask</code>, but allows a comma-delimited list of CPU numbers.</p>
<dt><code>cpus_allowed_policy</code><i></i>=str</p>
<dd> Set the policy of how fio distributes the CPUs specified by <code>cpus_allowed</code> or <code>cpumask</code>. Two policies are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>shared</code></p>
<dd> All jobs will share the CPU set specified.</p>
<dt><code>split</code></p>
<dd> Each job will get a unique CPU from the CPU set.</dl>
</dl>
<p> <code>shared</code> is the default behaviour, if the option isn&#8217;t specified. If <code>split</code> is specified, then fio will assign one cpu per job. If not enough CPUs are given for the jobs listed, then fio will roundrobin the CPUs in the set.</dl>
</dl>
<dl>
<dt><code>numa_cpu_nodes</code><i></i>=str</p>
<dd> Set this job running on specified NUMA nodes&#8217; CPUs. The arguments allow comma delimited list of cpu numbers, A-B ranges, or &#8216;all&#8217;.</p>
<dt><code>numa_mem_policy</code><i></i>=str</p>
<dd> Set this job&#8217;s memory policy and corresponding NUMA nodes. Format of the arguments:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&lt;mode&gt;[:&lt;nodelist&gt;]</code></p>
<dd>
<dt><code>mode</code></p>
<dd> is one of the following memory policy:</p>
<dt><code>default, prefer, bind, interleave, local</code></p>
<dd>
<dt></dl>
</dl>
<dd> For <code>default</code> and <code>local</code> memory policy, no <code>nodelist</code> is needed to be specified. For <code>prefer</code>, only one node is allowed. For <code>bind</code> and <code>interleave</code>, <code>nodelist</code> allows comma delimited list of numbers, A-B ranges, or &#8216;all&#8217;.</p>
<dt><code>startdelay</code><i></i>=irange</p>
<dd> Delay start of job for the specified number of seconds. Supports all time suffixes to allow specification of hours, minutes, seconds and milliseconds &#8211; seconds are the default if a unit is omitted. Can be given as a range which causes each thread to choose randomly out of the range.</p>
<dt><code>runtime</code><i></i>=int</p>
<dd> Terminate processing after the specified number of seconds.</p>
<dt><code>time_based</code></p>
<dd> If given, run for the specified <code>runtime</code> duration even if the files are completely read or written. The same workload will be repeated as many times as <code>runtime</code> allows.</p>
<dt><code>ramp_time</code><i></i>=int</p>
<dd> If set, fio will run the specified workload for this amount of time before logging any performance numbers. Useful for letting performance settle before logging results, thus minimizing the runtime required for stable results. Note that the <code>ramp_time</code> is considered lead in time for a job, thus it will increase the total runtime if a special timeout or runtime is specified.</p>
<dt><code>invalidate</code><i></i>=bool</p>
<dd> Invalidate buffer-cache for the file prior to starting I/O. Default: true.</p>
<dt><code>sync</code><i></i>=bool</p>
<dd> Use synchronous I/O for buffered writes. For the majority of I/O engines, this means using O_SYNC. Default: false.</p>
<dt><code>iomem</code><i></i>=str, mem<i></i>=str</p>
<dd> Allocation method for I/O unit buffer. Allowed values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>malloc</code></p>
<dd> Allocate memory with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3).</p>
<dt><code>shm</code></p>
<dd> Use shared memory buffers allocated through <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2).</p>
<dt><code>shmhuge</code></p>
<dd> Same as <code>shm</code>, but use huge pages as backing.</p>
<dt><code>mmap</code></p>
<dd> Use <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for allocation. Uses anonymous memory unless a filename is given after the option in the format `:<i>file</i>&#8216;.</p>
<dt><code>mmaphuge</code></p>
<dd> Same as <code>mmap</code>, but use huge files as backing.</dl>
</dl>
<p> The amount of memory allocated is the maximum allowed <code>blocksize</code> for the job multiplied by <code>iodepth</code>. For <code>shmhuge</code> or <code>mmaphuge</code> to work, the system must have free huge pages allocated. <code>mmaphuge</code> also needs to have hugetlbfs mounted, and <i>file</i> must point there. At least on Linux, huge pages must be manually allocated. See <code>/proc/sys/vm/nr_hugehages</code> and the documentation for that. Normally you just need to echo an appropriate number, eg echoing 8 will ensure that the OS has 8 huge pages ready for use.</dl>
<dt><code>iomem_align</code><i></i>=int, mem_align<i></i>=int</p>
<dd> This indicates the memory alignment of the IO memory buffers. Note that the given alignment is applied to the first IO unit buffer, if using <code>iodepth</code> the alignment of the following buffers are given by the <code>bs</code> used. In other words, if using a <code>bs</code> that is a multiple of the page sized in the system, all buffers will be aligned to this value. If using a <code>bs</code> that is not page aligned, the alignment of subsequent IO memory buffers is the sum of the <code>iomem_align</code> and <code>bs</code> used.</p>
<dt><code>hugepage-size</code><i></i>=int</p>
<dd> Defines the size of a huge page. Must be at least equal to the system setting. Should be a multiple of 1MB. Default: 4MB.</p>
<dt><code>exitall</code></p>
<dd> Terminate all jobs when one finishes. Default: wait for each job to finish.</p>
<dt><code>bwavgtime</code><i></i>=int</p>
<dd> Average bandwidth calculations over the given time in milliseconds. Default: 500ms.</p>
<dt><code>iopsavgtime</code><i></i>=int</p>
<dd> Average IOPS calculations over the given time in milliseconds. Default: 500ms.</p>
<dt><code>create_serialize</code><i></i>=bool</p>
<dd> If true, serialize file creation for the jobs. Default: true.</p>
<dt><code>create_fsync</code><i></i>=bool</p>
<dd> <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) data file after creation. Default: true.</p>
<dt><code>create_on_open</code><i></i>=bool</p>
<dd> If true, the files are not created until they are opened for IO by the job.</p>
<dt><code>create_only</code><i></i>=bool</p>
<dd> If true, fio will only run the setup phase of the job. If files need to be laid out or updated on disk, only that will be done. The actual job contents are not executed.</p>
<dt><code>allow_file_create</code><i></i>=bool</p>
<dd> If true, fio is permitted to create files as part of its workload. This is the default behavior. If this option is false, then fio will error out if the files it needs to use don&#8217;t already exist. Default: true.</p>
<dt><code>allow_mounted_write</code><i></i>=bool</p>
<dd> If this isn&#8217;t set, fio will abort jobs that are destructive (eg that write) to what appears to be a mounted device or partition. This should help catch creating inadvertently destructive tests, not realizing that the test will destroy data on the mounted file system. Default: false.</p>
<dt><code>pre_read</code><i></i>=bool</p>
<dd> If this is given, files will be pre-read into memory before starting the given IO operation. This will also clear the <code>invalidate</code> flag, since it is pointless to pre-read and then drop the cache. This will only work for IO engines that are seekable, since they allow you to read the same data multiple times. Thus it will not work on eg network or splice IO.</p>
<dt><code>unlink</code><i></i>=bool</p>
<dd> Unlink job files when done. Default: false.</p>
<dt><code>loops</code><i></i>=int</p>
<dd> Specifies the number of iterations (runs of the same workload) of this job. Default: 1.</p>
<dt><code>verify_only</code><i></i>=bool</p>
<dd> Do not perform the specified workload, only verify data still matches previous invocation of this workload. This option allows one to check data multiple times at a later date without overwriting it. This option makes sense only for workloads that write data, and does not support workloads with the <code>time_based</code> option set.</p>
<dt><code>do_verify</code><i></i>=bool</p>
<dd> Run the verify phase after a write phase. Only valid if <code>verify</code> is set. Default: true.</p>
<dt><code>verify</code><i></i>=str</p>
<dd> Method of verifying file contents after each iteration of the job. Each verification method also implies verification of special header, which is written to the beginning of each block. This header also includes meta information, like offset of the block, block number, timestamp when block was written, etc. <code>verify</code>=str can be combined with <code>verify_pattern</code>=str option. The allowed values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>md5 crc16 crc32 crc32c crc32c-intel crc64 crc7 sha256 sha512 sha1 xxhash</code></p>
<dd> Store appropriate checksum in the header of each block. crc32c-intel is hardware accelerated SSE4.2 driven, falls back to regular crc32c if not supported by the system.</p>
<dt><code>meta</code></p>
<dd> This option is deprecated, since now meta information is included in generic verification header and meta verification happens by default. For detailed information see the description of the <code>verify</code>=str setting. This option is kept because of compatibility&#8217;s sake with old configurations. Do not use it.</p>
<dt><code>pattern</code></p>
<dd> Verify a strict pattern. Normally fio includes a header with some basic information and checksumming, but if this option is set, only the specific pattern set with <code>verify_pattern</code> is verified.</p>
<dt><code>null</code></p>
<dd> Pretend to verify. Used for testing internals.</dl>
</dl>
<p> This option can be used for repeated burn-in tests of a system to make sure that the written data is also correctly read back. If the data direction given is a read or random read, fio will assume that it should verify a previously written file. If the data direction includes any form of write, the verify will be of the newly written data.</dl>
<dt><code>verifysort</code><i></i>=bool</p>
<dd> If true, written verify blocks are sorted if <code>fio</code> deems it to be faster to read them back in a sorted manner. Default: true.</p>
<dt><code>verifysort_nr</code><i></i>=int</p>
<dd> Pre-load and sort verify blocks for a read workload.</p>
<dt><code>verify_offset</code><i></i>=int</p>
<dd> Swap the verification header with data somewhere else in the block before writing. It is swapped back before verifying.</p>
<dt><code>verify_interval</code><i></i>=int</p>
<dd> Write the verification header for this number of bytes, which should divide <code>blocksize</code>. Default: <code>blocksize</code>.</p>
<dt><code>verify_pattern</code><i></i>=str</p>
<dd> If set, fio will fill the io buffers with this pattern. Fio defaults to filling with totally random bytes, but sometimes it&#8217;s interesting to fill with a known pattern for io verification purposes. Depending on the width of the pattern, fio will fill 1/2/3/4 bytes of the buffer at the time(it can be either a decimal or a hex number). The verify_pattern if larger than a 32-bit quantity has to be a hex number that starts with either &quot;0x&quot; or &quot;0X&quot;. Use with <code>verify</code>=str. Also, verify_pattern supports %o format, which means that for each block offset will be written and then verifyied back, e.g.:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>verify_pattern</code>=%o</dl>
<p> Or use combination of everything: </p>
<dl>
<dt>
<dd> <code>verify_pattern</code>=0xff%o&quot;abcd&quot;-21</dl>
</dl>
<dt><code>verify_fatal</code><i></i>=bool</p>
<dd> If true, exit the job on the first observed verification failure. Default: false.</p>
<dt><code>verify_dump</code><i></i>=bool</p>
<dd> If set, dump the contents of both the original data block and the data block we read off disk to files. This allows later analysis to inspect just what kind of data corruption occurred. Off by default.</p>
<dt><code>verify_async</code><i></i>=int</p>
<dd> Fio will normally verify IO inline from the submitting thread. This option takes an integer describing how many async offload threads to create for IO verification instead, causing fio to offload the duty of verifying IO contents to one or more separate threads. If using this offload option, even sync IO engines can benefit from using an <code>iodepth</code> setting higher than 1, as it allows them to have IO in flight while verifies are running.</p>
<dt><code>verify_async_cpus</code><i></i>=str</p>
<dd> Tell fio to set the given CPU affinity on the async IO verification threads. See <code>cpus_allowed</code> for the format used.</p>
<dt><code>verify_backlog</code><i></i>=int</p>
<dd> Fio will normally verify the written contents of a job that utilizes verify once that job has completed. In other words, everything is written then everything is read back and verified. You may want to verify continually instead for a variety of reasons. Fio stores the meta data associated with an IO block in memory, so for large verify workloads, quite a bit of memory would be used up holding this meta data. If this option is enabled, fio will write only N blocks before verifying these blocks.</p>
<dt><code>verify_backlog_batch</code><i></i>=int</p>
<dd> Control how many blocks fio will verify if verify_backlog is set. If not set, will default to the value of <code>verify_backlog</code> (meaning the entire queue is read back and verified). If <code>verify_backlog_batch</code> is less than <code>verify_backlog</code> then not all blocks will be verified, if <code>verify_backlog_batch</code> is larger than <code>verify_backlog</code>, some blocks will be verified more than once.</p>
<dt><code>trim_percentage</code><i></i>=int</p>
<dd> Number of verify blocks to discard/trim.</p>
<dt><code>trim_verify_zero</code><i></i>=bool</p>
<dd> Verify that trim/discarded blocks are returned as zeroes.</p>
<dt><code>trim_backlog</code><i></i>=int</p>
<dd> Trim after this number of blocks are written.</p>
<dt><code>trim_backlog_batch</code><i></i>=int</p>
<dd> Trim this number of IO blocks.</p>
<dt><code>experimental_verify</code><i></i>=bool</p>
<dd> Enable experimental verification.</p>
<dt><code>verify_state_save</code><i></i>=bool</p>
<dd> When a job exits during the write phase of a verify workload, save its current state. This allows fio to replay up until that point, if the verify state is loaded for the verify read phase.</p>
<dt><code>verify_state_load</code><i></i>=bool</p>
<dd> If a verify termination trigger was used, fio stores the current write state of each thread. This can be used at verification time so that fio knows how far it should verify. Without this information, fio will run a full verification pass, according to the settings in the job file used.</p>
<dt><code>stonewall </code>, wait_for_previous</p>
<dd> Wait for preceding jobs in the job file to exit before starting this one. <code>stonewall</code> implies <code>new_group</code>.</p>
<dt><code>new_group</code></p>
<dd> Start a new reporting group. If not given, all jobs in a file will be part of the same reporting group, unless separated by a stonewall.</p>
<dt><code>numjobs</code><i></i>=int</p>
<dd> Number of clones (processes/threads performing the same workload) of this job. Default: 1.</p>
<dt><code>group_reporting</code></p>
<dd> If set, display per-group reports instead of per-job when <code>numjobs</code> is specified.</p>
<dt><code>thread</code></p>
<dd> Use threads created with <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) instead of processes created with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<dt><code>zonesize</code><i></i>=int</p>
<dd> Divide file into zones of the specified size in bytes. See <code>zoneskip</code>.</p>
<dt><code>zonerange</code><i></i>=int</p>
<dd> Give size of an IO zone. See <code>zoneskip</code>.</p>
<dt><code>zoneskip</code><i></i>=int</p>
<dd> Skip the specified number of bytes when <code>zonesize</code> bytes of data have been read.</p>
<dt><code>write_iolog</code><i></i>=str</p>
<dd> Write the issued I/O patterns to the specified file. Specify a separate file for each job, otherwise the iologs will be interspersed and the file may be corrupt.</p>
<dt><code>read_iolog</code><i></i>=str</p>
<dd> Replay the I/O patterns contained in the specified file generated by <code>write_iolog</code>, or may be a <code>blktrace</code> binary file.</p>
<dt><code>replay_no_stall</code><i></i>=int</p>
<dd> While replaying I/O patterns using <code>read_iolog</code> the default behavior attempts to respect timing information between I/Os. Enabling <code>replay_no_stall</code> causes I/Os to be replayed as fast as possible while still respecting ordering.</p>
<dt><code>replay_redirect</code><i></i>=str</p>
<dd> While replaying I/O patterns using <code>read_iolog</code> the default behavior is to replay the IOPS onto the major/minor device that each IOP was recorded from. Setting <code>replay_redirect</code> causes all IOPS to be replayed onto the single specified device regardless of the device it was recorded from.</p>
<dt><code>replay_align</code><i></i>=int</p>
<dd> Force alignment of IO offsets and lengths in a trace to this power of 2 value.</p>
<dt><code>replay_scale</code><i></i>=int</p>
<dd> Scale sector offsets down by this factor when replaying traces.</p>
<dt><code>per_job_logs</code><i></i>=bool</p>
<dd> If set, this generates bw/clat/iops log with per file private filenames. If not set, jobs with identical names will share the log filename. Default: true.</p>
<dt><code>write_bw_log</code><i></i>=str</p>
<dd> If given, write a bandwidth log of the jobs in this job file. Can be used to store data of the bandwidth of the jobs in their lifetime. The included fio_generate_plots script uses gnuplot to turn these text files into nice graphs. See <code>write_lat_log</code> for behaviour of given filename. For this option, the postfix is _bw.x.log, where x is the index of the job (1..N, where N is the number of jobs). If <code>per_job_logs</code> is false, then the filename will not include the job index.</p>
<dt><code>write_lat_log</code><i></i>=str</p>
<dd> Same as <code>write_bw_log</code>, but writes I/O completion latencies. If no filename is given with this option, the default filename of &quot;jobname_type.x.log&quot; is used, where x is the index of the job (1..N, where N is the number of jobs). Even if the filename is given, fio will still append the type of log. If <code>per_job_logs</code> is false, then the filename will not include the job index.</p>
<dt><code>write_iops_log</code><i></i>=str</p>
<dd> Same as <code>write_bw_log</code>, but writes IOPS. If no filename is given with this option, the default filename of &quot;jobname_type.x.log&quot; is used, where x is the index of the job (1..N, where N is the number of jobs). Even if the filename is given, fio will still append the type of log. If <code>per_job_logs</code> is false, then the filename will not include the job index.</p>
<dt><code>log_avg_msec</code><i></i>=int</p>
<dd> By default, fio will log an entry in the iops, latency, or bw log for every IO that completes. When writing to the disk log, that can quickly grow to a very large size. Setting this option makes fio average the each log entry over the specified period of time, reducing the resolution of the log. Defaults to 0.</p>
<dt><code>log_offset</code><i></i>=bool</p>
<dd> If this is set, the iolog options will include the byte offset for the IO entry as well as the other data values.</p>
<dt><code>log_compression</code><i></i>=int</p>
<dd> If this is set, fio will compress the IO logs as it goes, to keep the memory footprint lower. When a log reaches the specified size, that chunk is removed and compressed in the background. Given that IO logs are fairly highly compressible, this yields a nice memory savings for longer runs. The downside is that the compression will consume some background CPU cycles, so it may impact the run. This, however, is also true if the logging ends up consuming most of the system memory. So pick your poison. The IO logs are saved normally at the end of a run, by decompressing the chunks and storing them in the specified log file. This feature depends on the availability of zlib.</p>
<dt><code>log_store_compressed</code><i></i>=bool</p>
<dd> If set, and <code>log</code>_compression is also set, fio will store the log files in a compressed format. They can be decompressed with fio, using the <code>&#8211;inflate-log</code> command line parameter. The files will be stored with a <code>.fz</code> suffix.</p>
<dt><code>block_error_percentiles</code><i></i>=bool</p>
<dd> If set, record errors in trim block-sized units from writes and trims and output a histogram of how many trims it took to get to errors, and what kind of error was encountered.</p>
<dt><code>disable_lat</code><i></i>=bool</p>
<dd> Disable measurements of total latency numbers. Useful only for cutting back the number of calls to <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), as that does impact performance at really high IOPS rates. Note that to really get rid of a large amount of these calls, this option must be used with disable_slat and disable_bw as well.</p>
<dt><code>disable_clat</code><i></i>=bool</p>
<dd> Disable measurements of completion latency numbers. See <code>disable_lat</code>.</p>
<dt><code>disable_slat</code><i></i>=bool</p>
<dd> Disable measurements of submission latency numbers. See <code>disable_lat</code>.</p>
<dt><code>disable_bw_measurement</code><i></i>=bool</p>
<dd> Disable measurements of throughput/bandwidth numbers. See <code>disable_lat</code>.</p>
<dt><code>lockmem</code><i></i>=int</p>
<dd> Pin the specified amount of memory with <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2). Can be used to simulate a smaller amount of memory. The amount specified is per worker.</p>
<dt><code>exec_prerun</code><i></i>=str</p>
<dd> Before running the job, execute the specified command with <code><a href="/docs/linux/man/3-system/">system</a></code>(3).</p>
<dl>
<dt>
<dd> Output is redirected in a file called <code>jobname.prerun.txt</code></dl>
<dt><code>exec_postrun</code><i></i>=str</p>
<dd> Same as <code>exec_prerun</code>, but the command is executed after the job completes.</p>
<dl>
<dt>
<dd> Output is redirected in a file called <code>jobname.postrun.txt</code></dl>
<dt><code>ioscheduler</code><i></i>=str</p>
<dd> Attempt to switch the device hosting the file to the specified I/O scheduler.</p>
<dt><code>disk_util</code><i></i>=bool</p>
<dd> Generate disk utilization statistics if the platform supports it. Default: true.</p>
<dt><code>clocksource</code><i></i>=str</p>
<dd> Use the given clocksource as the base of timing. The supported options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>gettimeofday</code></p>
<dd> <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2)</p>
<dt><code>clock_gettime</code></p>
<dd> <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)</p>
<dt><code>cpu</code></p>
<dd> Internal CPU clock source</p>
<dt></dl>
</dl>
<dd></dl>
<p> <code>cpu</code> is the preferred clocksource if it is reliable, as it is very fast (and fio is heavy on time calls). Fio will automatically use this clocksource if it&#8217;s supported and considered reliable on the system it is running on, unless another clocksource is specifically set. For x86/x86-64 CPUs, this means supporting TSC Invariant.</p>
<dl>
<dt><code>gtod_reduce</code><i></i>=bool</p>
<dd> Enable all of the <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) reducing options (disable_clat, disable_slat, disable_bw) plus reduce precision of the timeout somewhat to really shrink the <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) call count. With this option enabled, we only do about 0.4% of the gtod() calls we would have done if all time keeping was enabled.</p>
<dt><code>gtod_cpu</code><i></i>=int</p>
<dd> Sometimes it&#8217;s cheaper to dedicate a single thread of execution to just getting the current time. Fio (and databases, for instance) are very intensive on <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) calls. With this option, you can set one CPU aside for doing nothing but logging current time to a shared memory location. Then the other threads/processes that run IO workloads need only copy that segment, instead of entering the kernel with a <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) call. The CPU set aside for doing these time calls will be excluded from other uses. Fio will manually clear it from the CPU mask of other jobs.</p>
<dt><code>ignore_error</code><i></i>=str</p>
<dd> Sometimes you want to ignore some errors during test in that case you can specify error list for each error type.<br />
 ignore_error=READ_ERR_LIST,WRITE_ERR_LIST,VERIFY_ERR_LIST<br />
 errors for given error type is separated with &#8216;:&#8217;. Error may be symbol (&#8216;ENOSPC&#8217;, &#8216;ENOMEM&#8217;) or an integer.<br />
 Example: ignore_error=EAGAIN,ENOSPC:122 .<br />
 This option will ignore EAGAIN from READ, and ENOSPC and 122(EDQUOT) from WRITE.</p>
<dt><code>error_dump</code><i></i>=bool</p>
<dd> If set dump every error even if it is non fatal, true by default. If disabled only fatal error will be dumped</p>
<dt><code>profile</code><i></i>=str</p>
<dd> Select a specific builtin performance test.</p>
<dt><code>cgroup</code><i></i>=str</p>
<dd> Add job to this control group. If it doesn&#8217;t exist, it will be created. The system must have a mounted cgroup blkio mount point for this to work. If your system doesn&#8217;t have it mounted, you can do so with: </p>
<p> # mount -t cgroup -o blkio none /cgroup</p>
<dt><code>cgroup_weight</code><i></i>=int</p>
<dd> Set the weight of the cgroup to this value. See the documentation that comes with the kernel, allowed values are in the range of 100..1000.</p>
<dt><code>cgroup_nodelete</code><i></i>=bool</p>
<dd> Normally fio will delete the cgroups it has created after the job completion. To override this behavior and to leave cgroups around after the job completion, set cgroup_nodelete=1. This can be useful if one wants to inspect various cgroup files after job completion. Default: false</p>
<dt><code>uid</code><i></i>=int</p>
<dd> Instead of running as the invoking user, set the user ID to this value before the thread/process does any work.</p>
<dt><code>gid</code><i></i>=int</p>
<dd> Set group ID, see <code>uid</code>.</p>
<dt><code>unit_base</code><i></i>=int</p>
<dd> Base unit for reporting. Allowed values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Use auto-detection (default).</p>
<dt><code>8</code></p>
<dd> Byte based.</p>
<dt><code>1</code></p>
<dd> Bit based.</dl>
</dl>
</dl>
<dl>
<dt><code>flow_id</code><i></i>=int</p>
<dd> The ID of the flow. If not specified, it defaults to being a global flow. See <code>flow</code>.</p>
<dt><code>flow</code><i></i>=int</p>
<dd> Weight in token-based flow control. If this value is used, then there is a <code>flow counter</code> which is used to regulate the proportion of activity between two or more jobs. fio attempts to keep this flow counter near zero. The <code>flow</code> parameter stands for how much should be added or subtracted to the flow counter on each iteration of the main I/O loop. That is, if one job has <code>flow=8</code> and another job has <code>flow=-1</code>, then there will be a roughly 1:8 ratio in how much one runs vs the other.</p>
<dt><code>flow_watermark</code><i></i>=int</p>
<dd> The maximum value that the absolute value of the flow counter is allowed to reach before the job must wait for a lower value of the counter.</p>
<dt><code>flow_sleep</code><i></i>=int</p>
<dd> The period of time, in microseconds, to wait after the flow watermark has been exceeded before retrying operations</p>
<dt><code>clat_percentiles</code><i></i>=bool</p>
<dd> Enable the reporting of percentiles of completion latencies.</p>
<dt><code>percentile_list</code><i></i>=float_list</p>
<dd> Overwrite the default list of percentiles for completion latencies and the block error histogram. Each number is a floating number in the range (0,100], and the maximum length of the list is 20. Use &#8216;:&#8217; to separate the numbers. For example, &#8211;percentile_list=99.5:99.9 will cause fio to report the values of completion latency below which 99.5% and 99.9% of the observed latencies fell, respectively.</dl>
<h3>Ioengine Parameters List</h3>
<p> Some parameters are only valid when a specific ioengine is in use. These are used identically to normal parameters, with the caveat that when used on the command line, they must come after the ioengine.</p>
<dl>
<dt><code>(cpu)cpuload</code><i></i>=int</p>
<dd> Attempt to use the specified percentage of CPU cycles.</p>
<dt><code>(cpu)cpuchunks</code><i></i>=int</p>
<dd> Split the load into cycles of the given time. In microseconds.</p>
<dt><code>(cpu)exit_on_io_done</code><i></i>=bool</p>
<dd> Detect when IO threads are done, then exit.</p>
<dt><code>(libaio)userspace_reap</code></p>
<dd> Normally, with the libaio engine in use, fio will use the io_getevents system call to reap newly returned events. With this flag turned on, the AIO ring will be read directly from user-space to reap events. The reaping mode is only enabled when polling for a minimum of 0 events (eg when iodepth_batch_complete=0).</p>
<dt><code>(net,netsplice)hostname</code><i></i>=str</p>
<dd> The host name or IP address to use for TCP or UDP based IO. If the job is a TCP listener or UDP reader, the hostname is not used and must be omitted unless it is a valid UDP multicast address.</p>
<dt><code>(net,netsplice)port</code><i></i>=int</p>
<dd> The TCP or UDP port to bind to or connect to. If this is used with <code>numjobs</code> to spawn multiple instances of the same job type, then this will be the starting port number since fio will use a range of ports.</p>
<dt><code>(net,netsplice)interface</code><i></i>=str</p>
<dd> The IP address of the network interface used to send or receive UDP multicast packets.</p>
<dt><code>(net,netsplice)ttl</code><i></i>=int</p>
<dd> Time-to-live value for outgoing UDP multicast packets. Default: 1</p>
<dt><code>(net,netsplice)nodelay</code><i></i>=bool</p>
<dd> Set TCP_NODELAY on TCP connections.</p>
<dt><code>(net,netsplice)protocol</code><i></i>=str, proto<i></i>=str</p>
<dd> The network protocol to use. Accepted values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>tcp</code></p>
<dd> Transmission control protocol</p>
<dt><code>tcpv6</code></p>
<dd> Transmission control protocol V6</p>
<dt><code>udp</code></p>
<dd> User datagram protocol</p>
<dt><code>udpv6</code></p>
<dd> User datagram protocol V6</p>
<dt><code>unix</code></p>
<dd> UNIX domain socket</dl>
</dl>
<p> When the protocol is TCP or UDP, the port must also be given, as well as the hostname if the job is a TCP listener or UDP reader. For unix sockets, the normal filename option should be used and the port is invalid.</dl>
<dt><code>(net,netsplice)listen</code></p>
<dd> For TCP network connections, tell fio to listen for incoming connections rather than initiating an outgoing connection. The hostname must be omitted if this option is used.</p>
<dt><code>(net,</code><i>pingpong)</i>=bool</p>
<dd> Normally a network writer will just continue writing data, and a network reader will just consume packets. If pingpong=1 is set, a writer will send its normal payload to the reader, then wait for the reader to send the same payload back. This allows fio to measure network latencies. The submission and completion latencies then measure local time spent sending or receiving, and the completion latency measures how long it took for the other end to receive and send back. For UDP multicast traffic pingpong=1 should only be set for a single reader when multiple readers are listening to the same address.</p>
<dt><code>(net,</code><i>window_size)</i>=int</p>
<dd> Set the desired socket buffer size for the connection.</p>
<dt><code>(net,</code><i>mss)</i>=int</p>
<dd> Set the TCP maximum segment size (TCP_MAXSEG).</p>
<dt><code>(e4defrag,donorname)</code><i></i>=str</p>
<dd> File will be used as a block donor (swap extents between files)</p>
<dt><code>(e4defrag,inplace)</code><i></i>=int</p>
<dd> Configure donor file block allocation strategy<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt>
<dd> <code>0(default)</code><i>:</i> Preallocate donor&#8217;s file on init</p>
<dl>
<dt><code>1:</code></p>
<dd> allocate space immediately inside defragment event, and free right after event</dl>
</dl>
<dt><code>(rbd)rbdname</code><i></i>=str</p>
<dd> Specifies the name of the RBD.</p>
<dt><code>(rbd)pool</code><i></i>=str</p>
<dd> Specifies the name of the Ceph pool containing the RBD.</p>
<dt><code>(rbd)clientname</code><i></i>=str</p>
<dd> Specifies the username (without the &#8216;client.&#8217; prefix) used to access the Ceph cluster.</p>
<dt><code>(mtd)skipbad</code><i></i>=bool</p>
<dd> Skip operations against known bad blocks.</dl>
<h2>OUTPUT</h2>
<p> While running, <code>fio</code> will display the status of the created jobs. For example:</p>
<dl>
<dt>
<dd>
<p> Threads: 1: [_r] [24.8% done] [ 13509/ 8334 kb/s] [eta 00h:01m:31s]</dl>
<p> The characters in the first set of brackets denote the current status of each threads. The possible values are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>P</code></p>
<dd> Setup but not started.</p>
<dt><code>C</code></p>
<dd> Thread created.</p>
<dt><code>I</code></p>
<dd> Initialized, waiting.</p>
<dt><code>R</code></p>
<dd> Running, doing sequential reads.</p>
<dt><code>r</code></p>
<dd> Running, doing random reads.</p>
<dt><code>W</code></p>
<dd> Running, doing sequential writes.</p>
<dt><code>w</code></p>
<dd> Running, doing random writes.</p>
<dt><code>M</code></p>
<dd> Running, doing mixed sequential reads/writes.</p>
<dt><code>m</code></p>
<dd> Running, doing mixed random reads/writes.</p>
<dt><code>F</code></p>
<dd> Running, currently waiting for <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2).</p>
<dt><code>V</code></p>
<dd> Running, verifying written data.</p>
<dt><code>E</code></p>
<dd> Exited, not reaped by main thread.</p>
<dt><code>&#8211;</code></p>
<dd> Exited, thread reaped.</dl>
</dl>
<p> The second set of brackets shows the estimated completion percentage of the current group. The third set shows the read and write I/O rate, respectively. Finally, the estimated run time of the job is displayed. </p>
<p> When <code>fio</code> completes (or is interrupted by Ctrl-C), it will show data for each thread, each group of threads, and each disk, in that order. </p>
<p> Per-thread statistics first show the threads client number, group-id, and error code. The remaining figures are as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>io</code></p>
<dd> Number of megabytes of I/O performed.</p>
<dt><code>bw</code></p>
<dd> Average data rate (bandwidth).</p>
<dt><code>runt</code></p>
<dd> Threads run time.</p>
<dt><code>slat</code></p>
<dd> Submission latency minimum, maximum, average and standard deviation. This is the time it took to submit the I/O.</p>
<dt><code>clat</code></p>
<dd> Completion latency minimum, maximum, average and standard deviation. This is the time between submission and completion.</p>
<dt><code>bw</code></p>
<dd> Bandwidth minimum, maximum, percentage of aggregate bandwidth received, average and standard deviation.</p>
<dt><code>cpu</code></p>
<dd> CPU usage statistics. Includes user and system time, number of context switches this thread went through and number of major and minor page faults.</p>
<dt><code>IO depths</code></p>
<dd> Distribution of I/O depths. Each depth includes everything less than (or equal) to it, but greater than the previous depth.</p>
<dt><code>IO issued</code></p>
<dd> Number of read/write requests issued, and number of short read/write requests.</p>
<dt><code>IO latencies</code></p>
<dd> Distribution of I/O completion latencies. The numbers follow the same pattern as <code>IO depths</code>.</dl>
</dl>
<p> The group statistics show:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>io</code></p>
<dd> Number of megabytes I/O performed.</p>
<dt><code>aggrb</code></p>
<dd> Aggregate bandwidth of threads in the group.</p>
<dt><code>minb</code></p>
<dd> Minimum average bandwidth a thread saw.</p>
<dt><code>maxb</code></p>
<dd> Maximum average bandwidth a thread saw.</p>
<dt><code>mint</code></p>
<dd> Shortest runtime of threads in the group.</p>
<dt><code>maxt</code></p>
<dd> Longest runtime of threads in the group.</dl>
</dl>
<p> Finally, disk statistics are printed with reads first:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ios</code></p>
<dd> Number of I/Os performed by all groups.</p>
<dt><code>merge</code></p>
<dd> Number of merges in the I/O scheduler.</p>
<dt><code>ticks</code></p>
<dd> Number of ticks we kept the disk busy.</p>
<dt><code>io_queue</code></p>
<dd> Total time spent in the disk queue.</p>
<dt><code>util</code></p>
<dd> Disk utilization.</dl>
</dl>
<p> It is also possible to get fio to dump the current output while it is running, without terminating the job. To do that, send fio the <code>USR1</code> signal.</p>
<h2>TERSE OUTPUT</h2>
<p> If the <code>&#8211;minimal</code> / <code>&#8211;append-terse</code> options are given, the results will be printed/appended in a semicolon-delimited format suitable for scripted use. A job description (if provided) follows on a new line. Note that the first number in the line is the version number. If the output has to be changed for some reason, this number will be incremented by 1 to signify that change. The fields are: </p>
<dl>
<dt>
<dd> <code>terse version, fio version, jobname, groupid, error</code> </p>
<p> Read status:</p>
<dl>
<dt>
<dd> <code>Total I/O </code>(KB), bandwidth (KB/s), IOPS, runtime (ms) </p>
<p> Submission latency:</p>
<dl>
<dt>
<dd> <code>min, max, mean, standard deviation</code></dl>
<p> Completion latency:</p>
<dl>
<dt>
<dd> <code>min, max, mean, standard deviation</code></dl>
<p> Completion latency percentiles (20 fields):</p>
<dl>
<dt>
<dd> <code>Xth percentile=usec</code></dl>
<p> Total latency:</p>
<dl>
<dt>
<dd> <code>min, max, mean, standard deviation</code></dl>
<p> Bandwidth:</p>
<dl>
<dt>
<dd> <code>min, max, aggregate percentage of total, mean, standard deviation</code></dl>
</dl>
<p> Write status:</p>
<dl>
<dt>
<dd> <code>Total I/O </code>(KB), bandwidth (KB/s), IOPS, runtime (ms) </p>
<p> Submission latency:</p>
<dl>
<dt>
<dd> <code>min, max, mean, standard deviation</code></dl>
<p> Completion latency:</p>
<dl>
<dt>
<dd> <code>min, max, mean, standard deviation</code></dl>
<p> Completion latency percentiles (20 fields):</p>
<dl>
<dt>
<dd> <code>Xth percentile=usec</code></dl>
<p> Total latency:</p>
<dl>
<dt>
<dd> <code>min, max, mean, standard deviation</code></dl>
<p> Bandwidth:</p>
<dl>
<dt>
<dd> <code>min, max, aggregate percentage of total, mean, standard deviation</code></dl>
</dl>
<p> CPU usage:</p>
<dl>
<dt>
<dd> <code>user, system, context switches, major page faults, minor page faults</code></dl>
<p> IO depth distribution:</p>
<dl>
<dt>
<dd> <code>&lt;=1, 2, 4, 8, 16, 32, &gt;=64</code></dl>
<p> IO latency distribution:</p>
<dl>
<dt>
<dd> Microseconds:</p>
<dl>
<dt>
<dd> <code>&lt;=2, 4, 10, 20, 50, 100, 250, 500, 750, 1000</code></dl>
<p> Milliseconds:</p>
<dl>
<dt>
<dd> <code>&lt;=2, 4, 10, 20, 50, 100, 250, 500, 750, 1000, 2000, &gt;=2000</code></dl>
</dl>
<p> Disk utilization (1 for each disk used):</p>
<dl>
<dt>
<dd> <code>name, read ios, write ios, read merges, write merges, read ticks, write ticks, read in-queue time, write in-queue time, disk utilization percentage</code></dl>
<p> Error Info (dependent on continue_on_error, default off):</p>
<dl>
<dt>
<dd> <code>total # errors, first error code </code></dl>
<p> <code>text description (if provided in config &#8211; appears on newline)</code></dl>
<h2>CLIENT / SERVER</h2>
<p> Normally you would run fio as a stand-alone application on the machine where the IO workload should be generated. However, it is also possible to run the frontend and backend of fio separately. This makes it possible to have a fio server running on the machine(s) where the IO workload should be running, while controlling it from another machine. </p>
<p> To start the server, you would do: </p>
<p> <code>fio &#8211;server=args</code> </p>
<p> on that machine, where args defines what fio listens to. The arguments are of the form &#8216;type:hostname or IP:port&#8217;. &#8216;type&#8217; is either &#8216;ip&#8217; (or ip4) for TCP/IP v4, &#8216;ip6&#8217; for TCP/IP v6, or &#8216;sock&#8217; for a local unix domain socket. &#8216;hostname&#8217; is either a hostname or IP address, and &#8216;port&#8217; is the port to listen to (only valid for TCP/IP, not a local socket). Some examples: </p>
<p> 1) fio &#8211;server </p>
<p>Start a fio server, listening on all interfaces on the default port&nbsp;<wbr>(8765). </p>
<p> 2) fio &#8211;server=ip:hostname,4444 </p>
<p>Start a fio server, listening on IP belonging to hostname and on port 4444. </p>
<p> 3) fio &#8211;server=ip6:::1,4444 </p>
<p>Start a fio server, listening on IPv6 localhost ::1 and on port 4444. </p>
<p> 4) fio &#8211;server=,4444 </p>
<p>Start a fio server, listening on all interfaces on port 4444. </p>
<p> 5) fio &#8211;server=1.2.3.4 </p>
<p>Start a fio server, listening on IP 1.2.3.4 on the default port. </p>
<p> 6) fio &#8211;server=sock:/tmp/fio.sock </p>
<p>Start a fio server, listening on the local socket&nbsp;<wbr>/tmp/fio.sock. </p>
<p> When a server is running, you can connect to it from a client. The client is run with: </p>
<p> fio &#8211;local-args &#8211;client=server &#8211;remote-args &lt;job file(s)&gt; </p>
<p> where &#8211;local-args are arguments that are local to the client where it is running, &#8216;server&#8217; is the connect string, and &#8211;remote-args and &lt;job file(s)&gt; are sent to the server. The &#8216;server&#8217; string follows the same format as it does on the server side, to allow IP/hostname/socket and port strings. You can connect to multiple clients as well, to do that you could run: </p>
<p> fio &#8211;client=server2 &#8211;client=server2 &lt;job file(s)&gt; </p>
<p> If the job file is located on the fio server, then you can tell the server to load a local file as well. This is done by using &#8211;remote-config: </p>
<p> fio &#8211;client=server &#8211;remote-config /path/to/file.fio </p>
<p> Then fio will open this local (to the server) job file instead of being passed one from the client. </p>
<p> If you have many servers (example: 100 VMs/containers), you can input a pathname of a file containing host IPs/names as the parameter value for the &#8211;client option. For example, here is an example &quot;host.list&quot; file containing 2 hostnames: </p>
<p> host1.your.dns.domain<br />
 host2.your.dns.domain </p>
<p> The fio command would then be: </p>
<p> fio &#8211;client=host.list &lt;job file&gt; </p>
<p> In this mode, you cannot input server-specific parameters or job files, and all servers receive the same job file. </p>
<p> In order to enable fio &#8211;client runs utilizing a shared filesystem from multiple hosts, fio &#8211;client now prepends the IP address of the server to the filename. For example, if fio is using directory /mnt/nfs/fio and is writing filename fileio.tmp, with a &#8211;client hostfile containing two hostnames h1 and h2 with IP addresses 192.168.10.120 and 192.168.10.121, then fio will create two files: </p>
<p> /mnt/nfs/fio/192.168.10.120.fileio.tmp<br />
 /mnt/nfs/fio/192.168.10.121.fileio.tmp </p>
<h2>AUTHORS</h2>
<p> <code>fio</code> was written by Jens Axboe &lt;jens.axboe [at] oracle.com&gt;, now Jens Axboe &lt;axboe [at] fb.com&gt;.<br />
 This man page was written by Aaron Carroll &lt;aaronc [at] cse.unsw.edu.au&gt; based on documentation by Jens Axboe.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the <code>fio</code> mailing list &lt;fio [at] vger.kernel.org&gt;. See <code>README</code>.</p>
<h2>SEE ALSO</h2>
<p> For further documentation see <code>HOWTO</code> and <code>README</code>.<br />
 Sample jobfiles are available in the <code>examples</code> directory. </p>
<h2>Index</h2>
