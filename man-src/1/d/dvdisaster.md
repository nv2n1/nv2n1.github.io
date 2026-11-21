---
title: "dvdisaster(1)"
name: "dvdisaster"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvdisaster/"
description: "DVDISASTER – data loss/scratch/aging protection for optical media"
---

<h2 class="name">NAME</h2>
<p> DVDISASTER &#8211; data loss/scratch/aging protection for optical media</p>
<h2>SYNOPSIS</h2>
<p> <code>dvdisaster</code> [<code>-r</code>|<code>-c</code>|<code>-f</code>|<code>-s</code>|<code>-t[q]</code>|<code>-u</code>] [<code>-d</code> <i>device</i>] [<code>-p</code> <i>prefix</i>] [<code>-i</code> <i>image</i>] [<code>-e</code> <i>eccfile</i>] [<code>-o</code> <i>file|image</i>] [<code>-a</code> <i>method-list</i>] [<code>-j</code> <i>n</i>] [<code>-n</code> <i>n%</i>] [<code>-m</code> <i>n</i>] [<code>-v</code>] [<code>-x</code> <i>n</i>] [<code>&#8211;adaptive-read</code>] [<code>&#8211;auto-suffix</code>] [<code>&#8211;cache-size</code> <i>n</i>] [<code>&#8211;dao</code>] [<code>&#8211;defective-dump</code> <i>d</i>] [<code>&#8211;driver</code> <i>d</i>] [<code>&#8211;eject</code>] [<code>&#8211;encoding-algorithm</code> <i>n</i>] [<code>&#8211;encoding-io-strategy</code> <i>n</i>] [<code>&#8211;fill-unreadable</code> <i>n</i>] [<code>&#8211;ignore-fatal-sense</code>] [<code>&#8211;ignore-iso-size</code>] [<code>&#8211;internal-rereads</code> <i>n</i>] [<code>&#8211;medium-info</code>] [<code>&#8211;old-ds-marker</code>] [<code>&#8211;prefetch-sectors</code> <i>n</i>] [<code>&#8211;raw-mode</code> <i>n</i>] [<code>&#8211;read-attempts</code> <i>n-m</i>] [<code>&#8211;read-medium</code> <i>n</i>] [<code>&#8211;read-raw</code>] [<code>&#8211;resource-file</code> <i>n</i>] [<code>&#8211;speed-warning</code> <i>n</i>] [<code>&#8211;spinup-delay</code> <i>n</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>DVDISASTER</code> provides a margin of safety against data loss on optical media caused by scratches or aging media. It creates error correction data which is used to recover unreadable sectors if the disc becomes damaged at a later time. </p>
<h2>TYPICAL USAGE</h2>
<dl>
<dt><code>dvdisaster</code> <code>-d</code> <i>/dev/hdc</i> <code>-s</code></dt>
<dd> Scans the medium in drive <i>/dev/hdc</i> for errors.</dd>
<dt><code>dvdisaster</code> <code>-d</code> <i>/dev/hdc</i> <code>-i</code> <i>medium.iso</i> <code>-r</code></dt>
<dd> Reads an image from drive <i>/dev/hdc</i> into the file <i>medium.iso</i>.</dd>
<dt><code>dvdisaster</code> <code>-d</code> <i>/dev/hdc</i> <code>-i</code> <i>medium.iso</i> <code>&#8211;read-raw</code> <code>-r</code></dt>
<dd> Creates an image as described above. Each sector&#8217;s integrity is verified by using its EDC and L-EC raw data. Only possible for CD media; otherwise the <code>&#8211;read-raw</code> option is silently ignored.</dd>
<dt><code>dvdisaster</code> <code>-d</code> <i>/dev/hdc</i> <code>-i</code> <i>medium.iso</i> <code>&#8211;read-attempts</code> <i>n-m</i> <code>-r</code></dt>
<dd> Creates an image as described above. Defective sectors are retried at least <i>n</i> times and at most <i>m</i> times. Recovery of defective CD media may improve when combined with <code>&#8211;read-raw</code>.</dd>
<dt><code>dvdisaster</code> <code>-d</code> <i>/dev/hdc</i> <code>-i</code> <i>medium.iso</i> <code>-e</code> <i>corr.ecc</i> <code>-r</code> <code>&#8211;adaptive-read</code></dt>
<dd> Uses the adaptive reading strategy to read an image from drive <i>/dev/hdc</i> into the file <i>medium.iso</i>. Reading will stop when enough data has been gathered to repair the image using the error correction file <i>corr.ecc</i>.</dd>
<dt><code>dvdisaster</code> <code>-i</code> <i>medium.iso</i> <code>-e</code> <i>corr.ecc</i> <code>-c</code></dt>
<dd> Creates an error correction file <i>corr.ecc</i> for the image <i>medium.iso</i>.</dd>
<dt><code>dvdisaster</code> <code>-i</code> <i>medium.iso</i> <code>-m</code><i>RS02</i> <code>-n</code> <i>350000</i> <code>-c</code></dt>
<dd> Augments the image <i>medium.iso</i> with error correction information, expanding the image to no more than <i>350000</i> sectors. If <code>-n</code> is omitted the image will be expanded to the smallest possible medium size (CD, DVD, DVD9). Note the missing blank between <code>-m</code> and <i>RS02</i>.</dd>
<dt><code>dvdisaster</code> <code>-i</code> <i>medium.iso</i> <code>-e</code> <i>corr.ecc</i> <code>-f</code></dt>
<dd> Repairs the image file <i>medium.iso</i> using the error correction file <i>corr.ecc</i>.</dd>
<dt><code>dvdisaster</code> <code>-i</code> <i>medium.iso</i> <code>-e</code> <i>corr.ecc</i> <code>-t</code></dt>
<dd> Verifies the image <i>medium.iso</i> with information from the error correction file <i>corr.ecc</i>.</dd>
<dt><code>NOTE:</code></dt>
<dd> Omit the <code>-e corr.ecc</code> options when working with augmented images in the examples above. </dd>
</dl>
<h2>OPTIONS</h2>
<p> Action selection (at least one action must be specified):</p>
<dl>
<dt><code>-r, &#8211;read</code></dt>
<dd> Read the medium image to hard disc. Use -rn-m to read a certain sector range, e.g. -r100-200.</dd>
<dt><code>-c, &#8211;create</code></dt>
<dd> Create .ecc information for the medium image.</dd>
<dt><code>-f, &#8211;fix</code></dt>
<dd> Try to fix medium image using .ecc information.</dd>
<dt><code>-s, &#8211;scan</code></dt>
<dd> Scan the medium for read errors.</dd>
<dt><code>-t, &#8211;test, -tq, &#8211;test=q</code></dt>
<dd> Test integrity of the .iso and .ecc files. When the &quot;q&quot; option is given, only information is output which can be gathered without fully scanning the files.</dd>
<dt><code>-u, &#8211;unlink</code></dt>
<dd> Delete .iso files (when other actions complete).</dd></dl>
<p> Drive and file specification:</p>
<dl>
<dt><code>-d, &#8211;device device</code></dt>
<dd> read from given device (default: /dev/cdrom).</dd>
<dt><code>-p, &#8211;prefix prefix</code></dt>
<dd> prefix of .iso/.ecc file (default: medium.* ).</dd>
<dt><code>-i, &#8211;image imagefile</code></dt>
<dd> name of image file (default: medium.iso).</dd>
<dt><code>-e, &#8211;ecc eccfile</code></dt>
<dd> name of parity file (default: medium.ecc).</dd>
<dt><code>-o, &#8211;ecc-target file|image</code></dt>
<dd> Specifies whether RS03 should create error correction files or augmented images (default: image).</dd>
<dt>
</dt><dd> Tweaking options (see manual before using!):</dd>
<dt><code>-a, &#8211;assume method1,method2,&#8230;</code></dt>
<dd> Assumes that the image is augmented with one of the given methods. This enables an exhaustive search for method signatures and might be helpful for detecting error correction information on damaged media. If the image does not contain the specified error correction information, a significant amount of CPU and I/O time may be wasted.</dd>
<dl>
<dt>
</dt><dd> Possible values are RS02 and RS03.</dd></dl>
<dt><code>-j, &#8211;jump n</code></dt>
<dd> jump n sectors forward after a read error (default: 16).</dd>
<dt><code>-n, &#8211;redundancy n[unit]</code></dt>
<dd> Error correction data redundancy. Allowed values depend on the method: </dd>
<dl>
<dt>
</dt><dd> RS01- and RS03-error correction files</dd>
<dl>
<dt>
</dt><dd> -n x&nbsp;<wbr>&nbsp;<wbr>creates error correction file with x roots.</dd></dl>
<dl>
<dt>
</dt><dd> -n x% creates error correction file with x percent redundancy.</dd></dl>
<dl>
<dt>
</dt><dd> -n xm creates error correction file of approx. x MiB size.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> RS01 error correction flles additionally support:</dd>
<dl>
<dt>
</dt><dd> -n normal &#8211; optimized codec for 14.3% redundancy/32 roots.</dd></dl>
<dl>
<dt>
</dt><dd> -n high&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; optimized codec for 33.5% redundancy/64 roots.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> RS02 images:</dd>
<dl>
<dt>
</dt><dd> -n CD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>augments image suitable for CD media.</dd></dl>
<dl>
<dt>
</dt><dd> -n DVD&nbsp;<wbr>&nbsp;<wbr>augments image suitable for DVD media.</dd></dl>
<dl>
<dt>
</dt><dd> -n DVD9 augments image suitable for DVD9 media.</dd></dl>
<dl>
<dt>
</dt><dd> -n BD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>augments image suitable for BD media.</dd></dl>
<dl>
<dt>
</dt><dd> -n BD2&nbsp;<wbr> augments image suitable for two layered BD media.</dd></dl>
<dl>
<dt>
</dt><dd> -n x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>augments image using approx. x sectors in total.</dd></dl>
<dl>
<dt>
</dt><dd> -n x%&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>augments image with approx. x% redundancy.</dd></dl>
<dl>
<dt>
</dt><dd> -n xr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>augments image with x roots error correction data.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> RS03 images:</dd>
<dl>
<dt>
</dt><dd> Setting the redundancy is not possible due to constraints in the format. The codec will automatically choose the size of the smallest fitting medium.</dd></dl>
</dl>
<dt><code>-m, &#8211;method n</code></dt>
<dd> lists/selects error correction methods (default: RS01).</dd>
<dl>
<dt>
</dt><dd> Possible values are RS01 and RS02.</dd></dl>
<dt><code>-v, &#8211;verbose n%</code></dt>
<dd> more diagnostic messages</dd>
<dt><code>-x, &#8211;threads n</code></dt>
<dd> Use n threads for encoding with the RS03 method. Use 2 or 4 threads for 2 or 4 core processors respectively. On larger machines save one core for housekeeping; e.g. use 7 threads on an eight core machine.</dd>
<dt><code>&#8211;adaptive-read</code></dt>
<dd> use optimized strategy for reading damaged media.</dd>
<dt><code>&#8211;auto-suffix</code></dt>
<dd> automatically add .iso and .ecc file suffixes.</dd>
<dt><code>&#8211;cache-size n</code></dt>
<dd> image cache size in MiB during -c mode (default: 32MiB).</dd>
<dt><code>&#8211;dao</code></dt>
<dd> assume DAO disc; do not trim image end.</dd>
<dt><code>&#8211;defective-dump d</code></dt>
<dd> Specifies the sub directory for storing incomplete raw sectors.</dd>
<dt><code>&#8211;driver d (Linux only)</code></dt>
<dd> Selects between the sg (SG_IO) driver (default setting) and the older cdrom (CDROM_SEND_PACKET) driver for accessing the optical drives. Both drivers should work equally well; however the cdrom driver is known to cause system failures on some ancient SCSI controllers. The older cdrom driver was the default upto and including dvdisaster 0.72.x; if the now pre-selected sg driver changes something to the worse for you please switch back to the older driver using &#8211;driver=cdrom.</dd>
<dt><code>&#8211;eject</code></dt>
<dd> eject medium after successful read.</dd>
<dt><code>&#8211;encoding-algorithm [32bit|64bit|SSE2|AltiVec]</code></dt>
<dd> This option affects the speed of generating RS03 error correction data. dvdisaster can either use a generic encoding algorithm using 32bit or 64bit wide operations running on the integer unit of the processor, or use processor specific extensions.</dd>
<dl>
<dt>
</dt><dd> Available extensions are SSE2 for x86 based processors and AltiVec on PowerPC processors. These extensions encode with 128bit wide operations and will usually provide the fastest encoding variant. The SSE2/AltiVec algorithms will automatically be selected if the processor supports them and nothing else is specified by this option.</dd></dl>
<dt><code>&#8211;encoding-io-strategy [readwrite|mmap]</code></dt>
<dd> This option controls how dvdisaster performs its disk I/O while creating error correction data with RS03. Try both options and see which performs best on your hardware setting.</dd>
<dl>
<dt>
</dt><dd> The &quot;readwrite&quot; option activates dvdisaster&#8217;s own I/O scheduler which reads and writes image data using normal file I/O. The advantage of this scheme is that dvdisaster knows exactly which data needs to be cached and preloaded; the disadvantage is that all data needs to be copied between the kernel and dvdisaster&#8217;s own buffers. Usually, this I/O scheme works best on slow storage with high latency and seek times; e.g. on all storage involving spinning platters. The &quot;mmap&quot; option uses the kernel&#8217;s memory mapping scheme for direct access to the image file. This has the advantage of minimal overhead, but may be adversely affected by poor caching and preloading decisions made by the kernel (since the kernel does not know what dvdisaster is going to do with the data). This scheme performs well when encoding in a RAM-based file system (such as /dev/shm on Linux) and on very fast media with low latency such as SSDs.</dd></dl>
<dt><code>&#8211;fill-unreadable n</code></dt>
<dd> fill unreadable sectors with byte n</dd>
<dt><code>&#8211;ignore-fatal-sense</code></dt>
<dd> continue reading after potentially fatal error condition.</dd>
<dt><code>&#8211;ignore-iso-size</code></dt>
<dd> By default getting the image size from the ISO/UDF filesystem is preferred over querying the drive as most drives report unreliable values.</dd>
<dl>
<dt>
</dt><dd> However in some rare cases the image size recorded in the ISO/UDF filesystem is wrong. Some Linux live CDs may have this problem. If you read back the ISO image from such CDs and its md5sum does not match the advertised one, try re-reading the image with this option turned on.</dd></dl>
<dl>
<dt>
</dt><dd> Do not blindly turn this option on as it will most likely create sub optimal or corrupted ISO images, especially if you plan to use the image for error correction data generation.</dd></dl>
<dt><code>&#8211;internal-rereads n</code></dt>
<dd> internal read attempts for defective CD media sectors (default: -1)</dd>
<dl>
<dt>
</dt><dd> The drive firmware usually retries unreadable sectors a few times before giving up and returning a read error. It is more efficient to set this to 0 or 1 and manage read attempts through the &#8211;read-attempts parameter. Most drives ignore this setting anyways. Use -1 to leave the drive at its default setting.</dd></dl>
<dt><code>&#8211;medium-info</code></dt>
<dd> Prints information about the currently inserted medium.</dd>
<dt><code>&#8211;old-ds-marker</code></dt>
<dd> Marks missing sectors in a manner which is compatible with dvdisaster 0.70 or older.</dd>
<dl>
<dt>
</dt><dd> The default marking method is recommended for dvdisaster 0.72 and later versions. However images marked with the current method can not be processed with older dvdisaster versions as missing sectors would not be recognized in the image. </dd>
<p> Do not process the same image with different settings for this option.</dl>
<dt><code>&#8211;prefetch-sectors n</code></dt>
<dd> number of sectors to preload during RS03 de-/encoding (default: 32)</dd>
<dl>
<dt>
</dt><dd> Using a value of n uses approx. n MiB of RAM.</dd></dl>
<dt><code>&#8211;raw-mode n</code></dt>
<dd> selects raw reading mode for CD media (default: 20)</dd>
<dl>
<dt>
</dt><dd> The recommended mode is 20, which makes the drive apply its built-in error correction to the best possible extent before transferring a defective sector. However some drives can only read defective sectors using mode 21, skipping the last stage of the internal error correction and returning the uncorrected sector instead.</dd></dl>
<dt><code>&#8211;read-attempts n-m</code></dt>
<dd> attempts n upto m reads of a defective sector.</dd>
<dt><code>&#8211;read-medium n</code></dt>
<dd> read the whole medium up to n times.</dd>
<dt><code>&#8211;read-raw</code></dt>
<dd> performs read in raw mode if possible.</dd>
<dt><code>&#8211;resource-file n</code></dt>
<dd> Specifies the path to the configuration file (default: $HOME/.dvdisaster)</dd>
<dt><code>&#8211;speed-warning n</code></dt>
<dd> print warning if speed changes by more than n percent.</dd>
<dt><code>&#8211;spinup-delay n</code></dt>
<dd> wait n seconds for drive to spin up.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>Documentation</code> DVDISASTER is documented by its own manual, installed in <i>/usr/share/doc/dvdisaster-0.79.5/html</i> </p>
<h2>AUTHOR</h2>
<p> DVDISASTER was written by Carsten Gnoerlich &lt;carsten [at] dvdisaster.com&gt;. </p>
<p> This manual page was written by Daniel Baumann &lt;daniel.baumann [at] panthera-systems.net&gt;, for the Debian project (but may be used by others). Since version 0.70 it is maintained by Carsten Gnoerlich. </p>
