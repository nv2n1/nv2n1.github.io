---
title: "qemu-img(1)"
name: "qemu-img"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qemu-img/"
description: "qemu-img – QEMU disk image utility"
---

<h2 class="name">NAME</h2>
<p> qemu-img &#8211; QEMU disk image utility </p>
<h2>SYNOPSIS</h2>
<p> <code>qemu-img</code> [<i>standard</i> <i>options</i>] <i>command</i> [<i>command</i> <i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> qemu-img allows you to create, convert and modify images offline. It can handle all image formats supported by <font SIZE="-1">QEMU.</font> </p>
<p> <code>Warning:</code> Never use qemu-img to modify images in use by a running virtual machine or any other process; this may destroy the image. Also, be aware that querying an image that is being modified by another process may encounter inconsistent state.</p>
<h2>OPTIONS</h2>
<p> Standard options:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display this help and exit</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version information and exit</p>
<dt><code>-T, &#8211;trace [[enable=]</code><i>pattern</i><code>][,events=</code><i>file</i><code>][,file=</code><i>file</i><code>]</code></p>
<dd> Specify tracing options.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>[enable=]</code><i>pattern</i></p>
<dd> Immediately enable events matching <i>pattern</i> (either event name or a globbing pattern). This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend. To specify multiple events or patterns, specify the <code>-trace</code> option multiple times. </p>
<p> Use <tt>&quot;-trace help&quot;</tt> to print a list of names of trace points.</p>
<dt><code>events=</code><i>file</i></p>
<dd> Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events-all</i> file) per line; globbing patterns are accepted too. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend.</p>
<dt><code>file=</code><i>file</i></p>
<dd> Log output traces to <i>file</i>. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i> tracing backend.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> The following commands are supported:</p>
<dl>
<dt><code>amend [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-p] [-q] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] -o</code> <i>options</i><i>filename</i></p>
<dd>
<dt><code>bench [-c</code> <i>count</i><code>] [-d</code> <i>depth</i><code>] [-f</code> <i>fmt</i><code>] [&#8211;flush-interval=</code><i>flush_interval</i><code>] [-n] [&#8211;no-drain] [-o</code> <i>offset</i><code>] [&#8211;pattern=</code><i>pattern</i><code>] [-q] [-s</code> <i>buffer_size</i><code>] [-S</code> <i>step_size</i><code>] [-t</code> <i>cache</i><code>] [-w] [-U]</code> <i>filename</i></p>
<dd>
<dt><code>check [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-q] [-f</code> <i>fmt</i><code>] [&#8211;output=</code><i>ofmt</i><code>] [-r [leaks | all]] [-T</code> <i>src_cache</i><code>] [-U]</code> <i>filename</i></p>
<dd>
<dt><code>commit [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-q] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] [-b</code> <i>base</i><code>] [-d] [-p]</code> <i>filename</i></p>
<dd>
<dt><code>compare [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [-F</code> <i>fmt</i><code>] [-T</code> <i>src_cache</i><code>] [-p] [-q] [-s] [-U]</code> <i>filename1</i><i>filename2</i></p>
<dd>
<dt><code>convert [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [&#8211;target-image-opts] [-U] [-C] [-c] [-p] [-q] [-n] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] [-T</code> <i>src_cache</i><code>] [-O</code> <i>output_fmt</i><code>] [-B</code> <i>backing_file</i><code>] [-o</code> <i>options</i><code>] [-l</code> <i>snapshot_param</i><code>] [-S</code> <i>sparse_size</i><code>] [-m</code> <i>num_coroutines</i><code>] [-W] [&#8211;salvage]</code> <i>filename</i> <code>[</code><i>filename2</i> <code>[&#8230;]]</code> <i>output_filename</i></p>
<dd>
<dt><code>create [&#8211;object</code> <i>objectdef</i><code>] [-q] [-f</code> <i>fmt</i><code>] [-b</code> <i>backing_file</i><code>] [-F</code> <i>backing_fmt</i><code>] [-u] [-o</code> <i>options</i><code>]</code> <i>filename</i> <code>[</code><i>size</i><code>]</code></p>
<dd>
<dt><code>dd [&#8211;image-opts] [-U] [-f</code> <i>fmt</i><code>] [-O</code> <i>output_fmt</i><code>] [bs=</code><i>block_size</i><code>] [count=</code><i>blocks</i><code>] [skip=</code><i>blocks</i><code>] if=</code><i>input</i> <code>of=</code><i>output</i></p>
<dd>
<dt><code>info [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [&#8211;output=</code><i>ofmt</i><code>] [&#8211;backing-chain] [-U]</code> <i>filename</i></p>
<dd>
<dt><code>map [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [&#8211;output=</code><i>ofmt</i><code>] [-U]</code> <i>filename</i></p>
<dd>
<dt><code>measure [&#8211;output=</code><i>ofmt</i><code>] [-O</code> <i>output_fmt</i><code>] [-o</code> <i>options</i><code>] [&#8211;size</code> <i>N</i> <code>| [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [-l</code> <i>snapshot_param</i><code>]</code> <i>filename</i><code>]</code></p>
<dd>
<dt><code>snapshot [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-U] [-q] [-l | -a</code> <i>snapshot</i> <code>| -c</code> <i>snapshot</i> <code>| -d</code> <i>snapshot</i><code>]</code> <i>filename</i></p>
<dd>
<dt><code>rebase [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-U] [-q] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] [-T</code> <i>src_cache</i><code>] [-p] [-u] -b</code> <i>backing_file</i> <code>[-F</code> <i>backing_fmt</i><code>]</code> <i>filename</i></p>
<dd>
<dt><code>resize [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [&#8211;preallocation=</code><i>prealloc</i><code>] [-q] [&#8211;shrink]</code> <i>filename</i> <code>[+ | -]</code><i>size</i></p>
<dd></dl>
<p> Command parameters:</p>
<dl>
<dt><i>filename</i></p>
<dd> is a disk image filename</p>
<dt><i>fmt</i></p>
<dd> is the disk image format. It is guessed automatically in most cases. See below for a description of the supported disk formats.</p>
<dt><i>size</i></p>
<dd> is the disk image size in bytes. Optional suffixes <tt>&quot;k&quot;</tt> or <tt>&quot;K&quot;</tt> (kilobyte, 1024) <tt>&quot;M&quot;</tt> (megabyte, 1024k) and <tt>&quot;G&quot;</tt> (gigabyte, 1024M) and T (terabyte, 1024G) are supported. <tt>&quot;b&quot;</tt> is ignored.</p>
<dt><i>output_filename</i></p>
<dd> is the destination disk image filename</p>
<dt><i>output_fmt</i></p>
<dd> is the destination format</p>
<dt><i>options</i></p>
<dd> is a comma separated list of format specific options in a name=value format. Use <tt>&quot;-o ?&quot;</tt> for an overview of the options supported by the used format or see the format descriptions below for details.</p>
<dt><i>snapshot_param</i></p>
<dd> is param used for internal snapshot, format is &#8216;snapshot.id=[<font SIZE="-1">ID</font>],snapshot.name=[<font SIZE="-1">NAME</font>]&#8217; or &#8216;[<font SIZE="-1">ID_OR_NAME</font>]&#8217;</p>
<dt><code>&#8211;object</code> <i>objectdef</i></p>
<dd> is a <font SIZE="-1">QEMU</font> user creatable object definition. See the <tt><a href="/docs/linux/man/1-qemu/">qemu</a>(1)</tt> manual page for a description of the object properties. The most common object type is a <tt>&quot;secret&quot;</tt>, which is used to supply passwords and/or encryption keys.</p>
<dt><code>&#8211;image-opts</code></p>
<dd> Indicates that the source <i>filename</i> parameter is to be interpreted as a full option string, not a plain filename. This parameter is mutually exclusive with the <i>-f</i> parameter.</p>
<dt><code>&#8211;target-image-opts</code></p>
<dd> Indicates that the <i>output_filename</i> parameter(s) are to be interpreted as a full option string, not a plain filename. This parameter is mutually exclusive with the <i>-O</i> parameters. It is currently required to also use the <i>-n</i> parameter to skip image creation. This restriction may be relaxed in a future release.</p>
<dt><code>&#8211;force-share (-U)</code></p>
<dd> If specified, <tt>&quot;qemu-img&quot;</tt> will open the image in shared mode, allowing other <font SIZE="-1">QEMU</font> processes to open it in write mode. For example, this can be used to get the image information (with &#8216;info&#8217; subcommand) when the image is used by a running guest. Note that this could produce inconsistent results because of concurrent metadata changes, etc. This option is only allowed when opening images in read-only mode.</p>
<dt><code>&#8211;backing-chain</code></p>
<dd> will enumerate information about backing files in a disk image chain. Refer below for further description.</p>
<dt><code>-c</code></p>
<dd> indicates that target image must be compressed (qcow format only)</p>
<dt><code>-h</code></p>
<dd> with or without a command shows help and lists the supported formats</p>
<dt><code>-p</code></p>
<dd> display progress bar (compare, convert and rebase commands only). If the <i>-p</i> option is not used for a command that supports it, the progress is reported when the process receives a <tt>&quot;SIGUSR1&quot;</tt> or <tt>&quot;SIGINFO&quot;</tt> signal.</p>
<dt><code>-q</code></p>
<dd> Quiet mode &#8211; do not print any output (except errors). There&#8217;s no progress bar in case both <i>-q</i> and <i>-p</i> options are used.</p>
<dt><code>-S</code> <i>size</i></p>
<dd> indicates the consecutive number of bytes that must contain only zeros for qemu-img to create a sparse image during conversion. This value is rounded down to the nearest 512 bytes. You may use the common size suffixes like <tt>&quot;k&quot;</tt> for kilobytes.</p>
<dt><code>-t</code> <i>cache</i></p>
<dd> specifies the cache mode that should be used with the (destination) file. See the documentation of the emulator&#8217;s <tt>&quot;-drive cache=...&quot;</tt> option for allowed values.</p>
<dt><code>-T</code> <i>src_cache</i></p>
<dd> specifies the cache mode that should be used with the source file(s). See the documentation of the emulator&#8217;s <tt>&quot;-drive cache=...&quot;</tt> option for allowed values.</dl>
<p> Parameters to snapshot subcommand:</p>
<dl>
<dt><code>snapshot</code></p>
<dd> is the name of the snapshot to create, apply or delete</p>
<dt><code>-a</code></p>
<dd> applies a snapshot (revert disk to saved state)</p>
<dt><code>-c</code></p>
<dd> creates a snapshot</p>
<dt><code>-d</code></p>
<dd> deletes a snapshot</p>
<dt><code>-l</code></p>
<dd> lists all snapshots in the given image</dl>
<p> Parameters to compare subcommand:</p>
<dl>
<dt><code>-f</code></p>
<dd> First image format</p>
<dt><code>-F</code></p>
<dd> Second image format</p>
<dt><code>-s</code></p>
<dd> Strict mode &#8211; fail on different image size or sector allocation</dl>
<p> Parameters to convert subcommand:</p>
<dl>
<dt><code>-n</code></p>
<dd> Skip the creation of the target volume</p>
<dt><code>-m</code></p>
<dd> Number of parallel coroutines for the convert process</p>
<dt><code>-W</code></p>
<dd> Allow out-of-order writes to the destination. This option improves performance, but is only recommended for preallocated devices like host devices or other raw block devices.</p>
<dt><code>-C</code></p>
<dd> Try to use copy offloading to move data from source image to target. This may improve performance if the data is remote, such as with <font SIZE="-1">NFS</font> or iSCSI backends, but will not automatically sparsify zero sectors, and may result in a fully allocated target image depending on the host support for getting allocation information.</p>
<dt><code>&#8211;salvage</code></p>
<dd> Try to ignore I/O errors when reading. Unless in quiet mode (<tt>&quot;-q&quot;</tt>), errors will still be printed. Areas that cannot be read from the source will be treated as containing only zeroes.</dl>
<p> Parameters to dd subcommand:</p>
<dl>
<dt><code>bs=</code><i>block_size</i></p>
<dd> defines the block size</p>
<dt><code>count=</code><i>blocks</i></p>
<dd> sets the number of input blocks to copy</p>
<dt><code>if=</code><i>input</i></p>
<dd> sets the input file</p>
<dt><code>of=</code><i>output</i></p>
<dd> sets the output file</p>
<dt><code>skip=</code><i>blocks</i></p>
<dd> sets the number of input blocks to skip</dl>
<p> Command description:</p>
<dl>
<dt><code>amend [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-p] [-q] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] -o</code> <i>options</i><i>filename</i></p>
<dd> Amends the image format specific <i>options</i> for the image file <i>filename</i>. Not all file formats support this operation.</p>
<dt><code>bench [-c</code> <i>count</i><code>] [-d</code> <i>depth</i><code>] [-f</code> <i>fmt</i><code>] [&#8211;flush-interval=</code><i>flush_interval</i><code>] [-n] [&#8211;no-drain] [-o</code> <i>offset</i><code>] [&#8211;pattern=</code><i>pattern</i><code>] [-q] [-s</code> <i>buffer_size</i><code>] [-S</code> <i>step_size</i><code>] [-t</code> <i>cache</i><code>] [-w] [-U]</code> <i>filename</i></p>
<dd> Run a simple sequential I/O benchmark on the specified image. If <tt>&quot;-w&quot;</tt> is specified, a write test is performed, otherwise a read test is performed. </p>
<p> A total number of <i>count</i> I/O requests is performed, each <i>buffer_size</i> bytes in size, and with <i>depth</i> requests in parallel. The first request starts at the position given by <i>offset</i>, each following request increases the current position by <i>step_size</i>. If <i>step_size</i> is not given, <i>buffer_size</i> is used for its value. </p>
<p> If <i>flush_interval</i> is specified for a write test, the request queue is drained and a flush is issued before new writes are made whenever the number of remaining requests is a multiple of <i>flush_interval</i>. If additionally <tt>&quot;--no-drain&quot;</tt> is specified, a flush is issued without draining the request queue first. </p>
<p> If <tt>&quot;-n&quot;</tt> is specified, the native <font SIZE="-1">AIO</font> backend is used if possible. On Linux, this option only works if <tt>&quot;-t none&quot;</tt> or <tt>&quot;-t directsync&quot;</tt> is specified as well. </p>
<p> For write tests, by default a buffer filled with zeros is written. This can be overridden with a pattern byte specified by <i>pattern</i>.</p>
<dt><code>check [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-q] [-f</code> <i>fmt</i><code>] [&#8211;output=</code><i>ofmt</i><code>] [-r [leaks | all]] [-T</code> <i>src_cache</i><code>] [-U]</code> <i>filename</i></p>
<dd> Perform a consistency check on the disk image <i>filename</i>. The command can output in the format <i>ofmt</i> which is either <tt>&quot;human&quot;</tt> or <tt>&quot;json&quot;</tt>. The <font SIZE="-1">JSON</font> output is an object of <font SIZE="-1">QAPI</font> type <tt>&quot;ImageCheck&quot;</tt>. </p>
<p> If <tt>&quot;-r&quot;</tt> is specified, qemu-img tries to repair any inconsistencies found during the check. <tt>&quot;-r leaks&quot;</tt> repairs only cluster leaks, whereas <tt>&quot;-r all&quot;</tt> fixes all kinds of errors, with a higher risk of choosing the wrong fix or hiding corruption that has already occurred. </p>
<p> Only the formats <tt>&quot;qcow2&quot;</tt>, <tt>&quot;qed&quot;</tt> and <tt>&quot;vdi&quot;</tt> support consistency checks. </p>
<p> In case the image does not have any inconsistencies, check exits with <tt>0</tt>. Other exit codes indicate the kind of inconsistency found or if another error occurred. The following table summarizes all exit codes of the check subcommand:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Check completed, the image is (now) consistent</p>
<dt><code>1</code></p>
<dd> Check not completed because of internal errors</p>
<dt><code>2</code></p>
<dd> Check completed, image is corrupted</p>
<dt><code>3</code></p>
<dd> Check completed, image has leaked clusters, but is not corrupted</p>
<dt><code>63</code></p>
<dd> Checks are not supported by the image format</dl>
</dl>
<dl>
<dt>
<dd>
<p> If <tt>&quot;-r&quot;</tt> is specified, exit codes representing the image state refer to the state after (the attempt at) repairing it. That is, a successful <tt>&quot;-r all&quot;</tt> will yield the exit code 0, independently of the image state before.</dl>
<dt><code>commit [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-q] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] [-b</code> <i>base</i><code>] [-d] [-p]</code> <i>filename</i></p>
<dd> Commit the changes recorded in <i>filename</i> in its base image or backing file. If the backing file is smaller than the snapshot, then the backing file will be resized to be the same size as the snapshot. If the snapshot is smaller than the backing file, the backing file will not be truncated. If you want the backing file to match the size of the smaller snapshot, you can safely truncate it yourself once the commit operation successfully completes. </p>
<p> The image <i>filename</i> is emptied after the operation has succeeded. If you do not need <i>filename</i> afterwards and intend to drop it, you may skip emptying <i>filename</i> by specifying the <tt>&quot;-d&quot;</tt> flag. </p>
<p> If the backing chain of the given image file <i>filename</i> has more than one layer, the backing file into which the changes will be committed may be specified as <i>base</i> (which has to be part of <i>filename</i>&#8216;s backing chain). If <i>base</i> is not specified, the immediate backing file of the top image (which is <i>filename</i>) will be used. Note that after a commit operation all images between <i>base</i> and the top image will be invalid and may return garbage data when read. For this reason, <tt>&quot;-b&quot;</tt> implies <tt>&quot;-d&quot;</tt> (so that the top image stays valid).</p>
<dt><code>compare [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [-F</code> <i>fmt</i><code>] [-T</code> <i>src_cache</i><code>] [-p] [-q] [-s] [-U]</code> <i>filename1</i><i>filename2</i></p>
<dd> Check if two images have the same content. You can compare images with different format or settings. </p>
<p> The format is probed unless you specify it by <i>-f</i> (used for <i>filename1</i>) and/or <i>-F</i> (used for <i>filename2</i>) option. </p>
<p> By default, images with different size are considered identical if the larger image contains only unallocated and/or zeroed sectors in the area after the end of the other image. In addition, if any sector is not allocated in one image and contains only zero bytes in the second one, it is evaluated as equal. You can use Strict mode by specifying the <i>-s</i> option. When compare runs in Strict mode, it fails in case image size differs or a sector is allocated in one image and is not allocated in the second one. </p>
<p> By default, compare prints out a result message. This message displays information that both images are same or the position of the first different byte. In addition, result message can report different image size in case Strict mode is used. </p>
<p> Compare exits with <tt>0</tt> in case the images are equal and with <tt>1</tt> in case the images differ. Other exit codes mean an error occurred during execution and standard error output should contain an error message. The following table sumarizes all exit codes of the compare subcommand:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Images are identical</p>
<dt><code>1</code></p>
<dd> Images differ</p>
<dt><code>2</code></p>
<dd> Error on opening an image</p>
<dt><code>3</code></p>
<dd> Error on checking a sector allocation</p>
<dt><code>4</code></p>
<dd> Error on reading data</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>convert [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [&#8211;target-image-opts] [-U] [-C] [-c] [-p] [-q] [-n] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] [-T</code> <i>src_cache</i><code>] [-O</code> <i>output_fmt</i><code>] [-B</code> <i>backing_file</i><code>] [-o</code> <i>options</i><code>] [-l</code> <i>snapshot_param</i><code>] [-S</code> <i>sparse_size</i><code>] [-m</code> <i>num_coroutines</i><code>] [-W]</code> <i>filename</i> <code>[</code><i>filename2</i> <code>[&#8230;]]</code> <i>output_filename</i></p>
<dd> Convert the disk image <i>filename</i> or a snapshot <i>snapshot_param</i> to disk image <i>output_filename</i> using format <i>output_fmt</i>. It can be optionally compressed (<tt>&quot;-c&quot;</tt> option) or use any format specific options like encryption (<tt>&quot;-o&quot;</tt> option). </p>
<p> Only the formats <tt>&quot;qcow&quot;</tt> and <tt>&quot;qcow2&quot;</tt> support compression. The compression is read-only. It means that if a compressed sector is rewritten, then it is rewritten as uncompressed data. </p>
<p> Image conversion is also useful to get smaller image when using a growable format such as <tt>&quot;qcow&quot;</tt>: the empty sectors are detected and suppressed from the destination image. </p>
<p> <i>sparse_size</i> indicates the consecutive number of bytes (defaults to 4k) that must contain only zeros for qemu-img to create a sparse image during conversion. If <i>sparse_size</i> is 0, the source will not be scanned for unallocated or zero sectors, and the destination image will always be fully allocated. </p>
<p> You can use the <i>backing_file</i> option to force the output image to be created as a copy on write image of the specified base image; the <i>backing_file</i> should have the same content as the input&#8217;s base image, however the path, image format, etc may differ. </p>
<p> If a relative path name is given, the backing file is looked up relative to the directory containing <i>output_filename</i>. </p>
<p> If the <tt>&quot;-n&quot;</tt> option is specified, the target volume creation will be skipped. This is useful for formats such as <tt>&quot;rbd&quot;</tt> if the target volume has already been created with site specific options that cannot be supplied through qemu-img. </p>
<p> Out of order writes can be enabled with <tt>&quot;-W&quot;</tt> to improve performance. This is only recommended for preallocated devices like host devices or other raw block devices. Out of order write does not work in combination with creating compressed images. </p>
<p> <i>num_coroutines</i> specifies how many coroutines work in parallel during the convert process (defaults to 8).</p>
<dt><code>create [&#8211;object</code> <i>objectdef</i><code>] [-q] [-f</code> <i>fmt</i><code>] [-b</code> <i>backing_file</i><code>] [-F</code> <i>backing_fmt</i><code>] [-u] [-o</code> <i>options</i><code>]</code> <i>filename</i> <code>[</code><i>size</i><code>]</code></p>
<dd> Create the new disk image <i>filename</i> of size <i>size</i> and format <i>fmt</i>. Depending on the file format, you can add one or more <i>options</i> that enable additional features of this format. </p>
<p> If the option <i>backing_file</i> is specified, then the image will record only the differences from <i>backing_file</i>. No size needs to be specified in this case. <i>backing_file</i> will never be modified unless you use the <tt>&quot;commit&quot;</tt> monitor command (or qemu-img commit). </p>
<p> If a relative path name is given, the backing file is looked up relative to the directory containing <i>filename</i>. </p>
<p> Note that a given backing file will be opened to check that it is valid. Use the <tt>&quot;-u&quot;</tt> option to enable unsafe backing file mode, which means that the image will be created even if the associated backing file cannot be opened. A matching backing file must be created or additional options be used to make the backing file specification valid when you want to use an image created this way. </p>
<p> The size can also be specified using the <i>size</i> option with <tt>&quot;-o&quot;</tt>, it doesn&#8217;t need to be specified separately in this case.</p>
<dt><code>dd [&#8211;image-opts] [-U] [-f</code> <i>fmt</i><code>] [-O</code> <i>output_fmt</i><code>] [bs=</code><i>block_size</i><code>] [count=</code><i>blocks</i><code>] [skip=</code><i>blocks</i><code>] if=</code><i>input</i> <code>of=</code><i>output</i></p>
<dd> Dd copies from <i>input</i> file to <i>output</i> file converting it from <i>fmt</i> format to <i>output_fmt</i> format. </p>
<p> The data is by default read and written using blocks of 512 bytes but can be modified by specifying <i>block_size</i>. If count=<i>blocks</i> is specified dd will stop reading input after reading <i>blocks</i> input blocks. </p>
<p> The size syntax is similar to <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1)&#8217;s size syntax.</p>
<dt><code>info [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [&#8211;output=</code><i>ofmt</i><code>] [&#8211;backing-chain] [-U]</code> <i>filename</i></p>
<dd> Give information about the disk image <i>filename</i>. Use it in particular to know the size reserved on disk which can be different from the displayed size. If <font SIZE="-1">VM</font> snapshots are stored in the disk image, they are displayed too. </p>
<p> If a disk image has a backing file chain, information about each disk image in the chain can be recursively enumerated by using the option <tt>&quot;--backing-chain&quot;</tt>. </p>
<p> For instance, if you have an image chain like: </p>
<pre>
        base.qcow2 &lt;- snap1.qcow2 &lt;- snap2.qcow2
</pre>
<p> To enumerate information about each disk image in the above chain, starting from top to base, do: </p>
<pre>
        qemu-img info --backing-chain snap2.qcow2
</pre>
<p> The command can output in the format <i>ofmt</i> which is either <tt>&quot;human&quot;</tt> or <tt>&quot;json&quot;</tt>. The <font SIZE="-1">JSON</font> output is an object of <font SIZE="-1">QAPI</font> type <tt>&quot;ImageInfo&quot;</tt>; with <tt>&quot;--backing-chain&quot;</tt>, it is an array of <tt>&quot;ImageInfo&quot;</tt> objects. </p>
<p> <tt>&quot;--output=human&quot;</tt> reports the following information (for every image in the chain):</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>image</i></p>
<dd> The image file name</p>
<dt><i>file format</i></p>
<dd> The image format</p>
<dt><i>virtual size</i></p>
<dd> The size of the guest disk</p>
<dt><i>disk size</i></p>
<dd> How much space the image file occupies on the host file system (may be shown as 0 if this information is unavailable, e.g. because there is no file system)</p>
<dt><i>cluster_size</i></p>
<dd> Cluster size of the image format, if applicable</p>
<dt><i>encrypted</i></p>
<dd> Whether the image is encrypted (only present if so)</p>
<dt><i>cleanly shut down</i></p>
<dd> This is shown as <tt>&quot;no&quot;</tt> if the image is dirty and will have to be auto-repaired the next time it is opened in qemu.</p>
<dt><i>backing file</i></p>
<dd> The backing file name, if present</p>
<dt><i>backing file format</i></p>
<dd> The format of the backing file, if the image enforces it</p>
<dt><i>Snapshot list</i></p>
<dd> A list of all internal snapshots</p>
<dt><i>Format specific information</i></p>
<dd> Further information whose structure depends on the image format. This section is a textual representation of the respective <tt>&quot;ImageInfoSpecific*&quot;</tt> <font SIZE="-1">QAPI</font> object (e.g. <tt>&quot;ImageInfoSpecificQCow2&quot;</tt> for qcow2 images).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>map [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [&#8211;output=</code><i>ofmt</i><code>] [-U]</code> <i>filename</i></p>
<dd> Dump the metadata of image <i>filename</i> and its backing file chain. In particular, this commands dumps the allocation state of every sector of <i>filename</i>, together with the topmost file that allocates it in the backing file chain. </p>
<p> Two option formats are possible. The default format (<tt>&quot;human&quot;</tt>) only dumps known-nonzero areas of the file. Known-zero parts of the file are omitted altogether, and likewise for parts that are not allocated throughout the chain. <code>qemu-img</code> output will identify a file from where the data can be read, and the offset in the file. Each line will include four fields, the first three of which are hexadecimal numbers. For example the first line of: </p>
<pre>
        Offset          Length          Mapped to       File
        0               0x20000         0x50000         /tmp/overlay.qcow2
        0x100000        0x10000         0x95380000      /tmp/backing.qcow2
</pre>
<p> means that 0x20000 (131072) bytes starting at offset 0 in the image are available in /tmp/overlay.qcow2 (opened in <tt>&quot;raw&quot;</tt> format) starting at offset 0x50000 (327680). Data that is compressed, encrypted, or otherwise not available in raw format will cause an error if <tt>&quot;human&quot;</tt> format is in use. Note that file names can include newlines, thus it is not safe to parse this output format in scripts. </p>
<p> The alternative format <tt>&quot;json&quot;</tt> will return an array of dictionaries in <font SIZE="-1">JSON</font> format. It will include similar information in the <tt>&quot;start&quot;</tt>, <tt>&quot;length&quot;</tt>, <tt>&quot;offset&quot;</tt> fields; it will also include other more specific information:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> whether the sectors contain actual data or not (boolean field <tt>&quot;data&quot;</tt>; if false, the sectors are either unallocated or stored as optimized all-zero clusters);</p>
<dt>&#8211;</p>
<dd> whether the data is known to read as zero (boolean field <tt>&quot;zero&quot;</tt>);</p>
<dt>&#8211;</p>
<dd> in order to make the output shorter, the target file is expressed as a <tt>&quot;depth&quot;</tt>; for example, a depth of 2 refers to the backing file of the backing file of <i>filename</i>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> In <font SIZE="-1">JSON</font> format, the <tt>&quot;offset&quot;</tt> field is optional; it is absent in cases where <tt>&quot;human&quot;</tt> format would omit the entry or exit with an error. If <tt>&quot;data&quot;</tt> is false and the <tt>&quot;offset&quot;</tt> field is present, the corresponding sectors in the file are not yet in use, but they are preallocated. </p>
<p> For more information, consult <i>include/block/block.h</i> in <font SIZE="-1">QEMU</font>&#8216;s source code.</dl>
<dt><code>measure [&#8211;output=</code><i>ofmt</i><code>] [-O</code> <i>output_fmt</i><code>] [-o</code> <i>options</i><code>] [&#8211;size</code> <i>N</i> <code>| [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [-l</code> <i>snapshot_param</i><code>]</code> <i>filename</i><code>]</code></p>
<dd> Calculate the file size required for a new image. This information can be used to size logical volumes or <font SIZE="-1">SAN</font> LUNs appropriately for the image that will be placed in them. The values reported are guaranteed to be large enough to fit the image. The command can output in the format <i>ofmt</i> which is either <tt>&quot;human&quot;</tt> or <tt>&quot;json&quot;</tt>. The <font SIZE="-1">JSON</font> output is an object of <font SIZE="-1">QAPI</font> type <tt>&quot;BlockMeasureInfo&quot;</tt>. </p>
<p> If the size <i>N</i> is given then act as if creating a new empty image file using <code>qemu-img create</code>. If <i>filename</i> is given then act as if converting an existing image file using <code>qemu-img convert</code>. The format of the new file is given by <i>output_fmt</i> while the format of an existing file is given by <i>fmt</i>. </p>
<p> A snapshot in an existing image can be specified using <i>snapshot_param</i>. </p>
<p> The following fields are reported: </p>
<pre>
        required size: 524288
        fully allocated size: 1074069504
</pre>
<p> The <tt>&quot;required size&quot;</tt> is the file size of the new image. It may be smaller than the virtual disk size if the image format supports compact representation. </p>
<p> The <tt>&quot;fully allocated size&quot;</tt> is the file size of the new image once data has been written to all sectors. This is the maximum size that the image file can occupy with the exception of internal snapshots, dirty bitmaps, vmstate data, and other advanced image format features.</p>
<dt><code>snapshot [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-U] [-q] [-l | -a</code> <i>snapshot</i> <code>| -c</code> <i>snapshot</i> <code>| -d</code> <i>snapshot</i><code>]</code> <i>filename</i></p>
<dd> List, apply, create or delete snapshots in image <i>filename</i>.</p>
<dt><code>rebase [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-U] [-q] [-f</code> <i>fmt</i><code>] [-t</code> <i>cache</i><code>] [-T</code> <i>src_cache</i><code>] [-p] [-u] -b</code> <i>backing_file</i> <code>[-F</code> <i>backing_fmt</i><code>]</code> <i>filename</i></p>
<dd> Changes the backing file of an image. Only the formats <tt>&quot;qcow2&quot;</tt> and <tt>&quot;qed&quot;</tt> support changing the backing file. </p>
<p> The backing file is changed to <i>backing_file</i> and (if the image format of <i>filename</i> supports this) the backing file format is changed to <i>backing_fmt</i>. If <i>backing_file</i> is specified as &quot;&quot; (the empty string), then the image is rebased onto no backing file (i.e. it will exist independently of any backing file). </p>
<p> If a relative path name is given, the backing file is looked up relative to the directory containing <i>filename</i>. </p>
<p> <i>cache</i> specifies the cache mode to be used for <i>filename</i>, whereas <i>src_cache</i> specifies the cache mode for reading backing files. </p>
<p> There are two different modes in which <tt>&quot;rebase&quot;</tt> can operate:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Safe mode</code></p>
<dd> This is the default mode and performs a real rebase operation. The new backing file may differ from the old one and qemu-img rebase will take care of keeping the guest-visible content of <i>filename</i> unchanged. </p>
<p> In order to achieve this, any clusters that differ between <i>backing_file</i> and the old backing file of <i>filename</i> are merged into <i>filename</i> before actually changing the backing file. </p>
<p> Note that the safe mode is an expensive operation, comparable to converting an image. It only works if the old backing file still exists.</p>
<dt><code>Unsafe mode</code></p>
<dd> qemu-img uses the unsafe mode if <tt>&quot;-u&quot;</tt> is specified. In this mode, only the backing file name and format of <i>filename</i> is changed without any checks on the file contents. The user must take care of specifying the correct new backing file, or the guest-visible content of the image will be corrupted. </p>
<p> This mode is useful for renaming or moving the backing file to somewhere else. It can be used without an accessible old backing file, i.e. you can use it to fix an image whose backing file has already been moved/renamed.</dl>
</dl>
<dl>
<dt>
<dd>
<p> You can use <tt>&quot;rebase&quot;</tt> to perform a &#8220;diff&#8221; operation on two disk images. This can be useful when you have copied or cloned a guest, and you want to get back to a thin image on top of a template or base image. </p>
<p> Say that <tt>&quot;base.img&quot;</tt> has been cloned as <tt>&quot;modified.img&quot;</tt> by copying it, and that the <tt>&quot;modified.img&quot;</tt> guest has run so there are now some changes compared to <tt>&quot;base.img&quot;</tt>. To construct a thin image called <tt>&quot;diff.qcow2&quot;</tt> that contains just the differences, do: </p>
<pre>
        qemu-img create -f qcow2 -b modified.img diff.qcow2
        qemu-img rebase -b base.img diff.qcow2
</pre>
<p> At this point, <tt>&quot;modified.img&quot;</tt> can be discarded, since <tt>&quot;base.img + diff.qcow2&quot;</tt> contains the same information.</dl>
<dt><code>resize [&#8211;object</code> <i>objectdef</i><code>] [&#8211;image-opts] [-f</code> <i>fmt</i><code>] [&#8211;preallocation=</code><i>prealloc</i><code>] [-q] [&#8211;shrink]</code> <i>filename</i> <code>[+ | -]</code><i>size</i></p>
<dd> Change the disk image as if it had been created with <i>size</i>. </p>
<p> Before using this command to shrink a disk image, you <font SIZE="-1">MUST</font> use file system and partitioning tools inside the <font SIZE="-1">VM</font> to reduce allocated file systems and partition sizes accordingly. Failure to do so will result in data loss! </p>
<p> When shrinking images, the <tt>&quot;--shrink&quot;</tt> option must be given. This informs qemu-img that the user acknowledges all loss of data beyond the truncated image&#8217;s end. </p>
<p> After using this command to grow a disk image, you must use file system and partitioning tools inside the <font SIZE="-1">VM</font> to actually begin using the new space on the device. </p>
<p> When growing an image, the <tt>&quot;--preallocation&quot;</tt> option may be used to specify how the additional image area should be allocated on the host. See the format description in the <tt>&quot;NOTES&quot;</tt> section which values are allowed. Using this option may result in slightly more data being allocated than necessary.</dl>
<h2>NOTES</h2>
<p> Supported image file formats:</p>
<dl>
<dt><code>raw</code></p>
<dd> Raw disk image format (default). This format has the advantage of being simple and easily exportable to all other emulators. If your file system supports <i>holes</i> (for example in ext2 or ext3 on Linux or <font SIZE="-1">NTFS</font> on Windows), then only the written sectors will reserve space. Use <tt>&quot;qemu-img info&quot;</tt> to know the real size used by the image or <tt>&quot;ls -ls&quot;</tt> on Unix/Linux. </p>
<p> Supported options:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;preallocation&quot;</p>
<dd> Preallocation mode (allowed values: <tt>&quot;off&quot;</tt>, <tt>&quot;falloc&quot;</tt>, <tt>&quot;full&quot;</tt>). <tt>&quot;falloc&quot;</tt> mode preallocates space for image by calling <code>posix_fallocate()</code>. <tt>&quot;full&quot;</tt> mode preallocates space for image by writing data to underlying storage. This data may or may not be zero, depending on the storage location.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>qcow2</code></p>
<dd> <font SIZE="-1">QEMU</font> image format, the most versatile format. Use it to have smaller images (useful if your filesystem does not supports holes, for example on Windows), optional <font SIZE="-1">AES</font> encryption, zlib based compression and support of multiple <font SIZE="-1">VM</font> snapshots. </p>
<p> Supported options:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;compat&quot;</p>
<dd> Determines the qcow2 version to use. <tt>&quot;compat=0.10&quot;</tt> uses the traditional image format that can be read by any <font SIZE="-1">QEMU</font> since 0.10. <tt>&quot;compat=1.1&quot;</tt> enables image format extensions that only <font SIZE="-1">QEMU 1.1</font> and newer understand (this is the default). Amongst others, this includes zero clusters, which allow efficient copy-on-read for sparse images.</p>
<dt>&quot;backing_file&quot;</p>
<dd> File name of a base image (see <code>create</code> subcommand)</p>
<dt>&quot;backing_fmt&quot;</p>
<dd> Image format of the base image</p>
<dt>&quot;encryption&quot;</p>
<dd> If this option is set to <tt>&quot;on&quot;</tt>, the image is encrypted with 128-bit AES-CBC. </p>
<p> The use of encryption in qcow and qcow2 images is considered to be flawed by modern cryptography standards, suffering from a number of design problems:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> The AES-CBC cipher is used with predictable initialization vectors based on the sector number. This makes it vulnerable to chosen plaintext attacks which can reveal the existence of encrypted data.</p>
<dt>&#8211;</p>
<dd> The user passphrase is directly used as the encryption key. A poorly chosen or short passphrase will compromise the security of the encryption.</p>
<dt>&#8211;</p>
<dd> In the event of the passphrase being compromised there is no way to change the passphrase to protect data in any qcow images. The files must be cloned, using a different encryption passphrase in the new file. The original file must then be securely erased using a program like shred, though even this is ineffective with many modern storage technologies.</p>
<dt>&#8211;</p>
<dd> Initialization vectors used to encrypt sectors are based on the guest virtual sector number, instead of the host physical sector. When a disk image has multiple internal snapshots this means that data in multiple physical sectors is encrypted with the same initialization vector. With the <font SIZE="-1">CBC</font> mode, this opens the possibility of watermarking attacks if the attack can collect multiple sectors encrypted with the same <font SIZE="-1">IV</font> and some predictable data. Having multiple qcow2 images with the same passphrase also exposes this weakness since the passphrase is directly used as the key.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Use of qcow / qcow2 encryption is thus strongly discouraged. Users are recommended to use an alternative encryption technology such as the Linux dm-crypt / <font SIZE="-1">LUKS</font> system.</dl>
<dt>&quot;cluster_size&quot;</p>
<dd> Changes the qcow2 cluster size (must be between 512 and 2M). Smaller cluster sizes can improve the image file size whereas larger cluster sizes generally provide better performance.</p>
<dt>&quot;preallocation&quot;</p>
<dd> Preallocation mode (allowed values: <tt>&quot;off&quot;</tt>, <tt>&quot;metadata&quot;</tt>, <tt>&quot;falloc&quot;</tt>, <tt>&quot;full&quot;</tt>). An image with preallocated metadata is initially larger but can improve performance when the image needs to grow. <tt>&quot;falloc&quot;</tt> and <tt>&quot;full&quot;</tt> preallocations are like the same options of <tt>&quot;raw&quot;</tt> format, but sets up metadata also.</p>
<dt>&quot;lazy_refcounts&quot;</p>
<dd> If this option is set to <tt>&quot;on&quot;</tt>, reference count updates are postponed with the goal of avoiding metadata I/O and improving performance. This is particularly interesting with <code>cache=writethrough</code> which doesn&#8217;t batch metadata updates. The tradeoff is that after a host crash, the reference count tables must be rebuilt, i.e. on the next open an (automatic) <tt>&quot;qemu-img check -r all&quot;</tt> is required, which may take some time. </p>
<p> This option can only be enabled if <tt>&quot;compat=1.1&quot;</tt> is specified.</p>
<dt>&quot;nocow&quot;</p>
<dd> If this option is set to <tt>&quot;on&quot;</tt>, it will turn off <font SIZE="-1">COW</font> of the file. It&#8217;s only valid on btrfs, no effect on other file systems. </p>
<p> Btrfs has low performance when hosting a <font SIZE="-1">VM</font> image file, even more when the guest on the <font SIZE="-1">VM</font> also using btrfs as file system. Turning off <font SIZE="-1">COW</font> is a way to mitigate this bad performance. Generally there are two ways to turn off <font SIZE="-1">COW</font> on btrfs: a) Disable it by mounting with nodatacow, then all newly created files will be <font SIZE="-1">NOCOW.</font> b) For an empty file, add the <font SIZE="-1">NOCOW</font> file attribute. That&#8217;s what this option does. </p>
<p> Note: this option is only valid to new or empty files. If there is an existing file which is <font SIZE="-1">COW</font> and has data blocks already, it couldn&#8217;t be changed to <font SIZE="-1">NOCOW</font> by setting <tt>&quot;nocow=on&quot;</tt>. One can issue <tt>&quot;lsattr filename&quot;</tt> to check if the <font SIZE="-1">NOCOW</font> flag is set or not (Capital &#8216;C&#8217; is <font SIZE="-1">NOCOW</font> flag).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>Other</code></p>
<dd> <font SIZE="-1">QEMU</font> also supports various other image file formats for compatibility with older <font SIZE="-1">QEMU</font> versions or other hypervisors, including <font SIZE="-1">VMDK, VDI, VHD</font> (vpc), <font SIZE="-1">VHDX,</font> qcow1 and <font SIZE="-1">QED.</font> For a full list of supported formats see <tt>&quot;qemu-img --help&quot;</tt>. For a more detailed description of these formats, see the <font SIZE="-1">QEMU</font> Emulation User Documentation. </p>
<p> The main purpose of the block drivers for these formats is image conversion. For running VMs, it is recommended to convert the disk images to either raw or qcow2 in order to achieve good performance.</dl>
<h2>SEE ALSO</h2>
<p> The <font SIZE="-1">HTML</font> documentation of <font SIZE="-1">QEMU</font> for more precise information and Linux user mode emulator invocation.</p>
<h2>AUTHOR</h2>
<p> Fabrice Bellard </p>
<h2>Index</h2>
