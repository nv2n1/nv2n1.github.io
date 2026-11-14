---
title: "iucode-tool(8)"
name: "iucode-tool"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iucode-tool/"
description: "iucode_tool – Tool to manipulate Intel® IA-32/X86-64 microcode bundles"
---

<p>iucode_tool &#8211; Tool to manipulate Intel&#174; IA-32/X86-64 microcode bundles</p>
<h2>Synopsis</h2>
<p><code>iucode_tool</code> [<i>options</i>] [[-t<i>type</i>] <i>filename</i>|<i>dirname</i>] &#8230;</p>
<h2>Description</h2>
<p><code>iucode_tool</code> is an utility that can load Intel&#174; processor microcode data from files in both text and binary microcode bundle formats. It can output a list of the microcodes in these files, merge them, upload them to the kernel (to upgrade the microcode in the system processor cores) or write some of them out to a file in binary format for later use. <code>iucode_tool</code> will load all microcodes in the specified files and directories to memory, in order to process them. Duplicated and outdated microcodes will be discarded. It can read microcode data from standard input (<i>stdin</i>), by specifying a file name of &#8220;-&#8221; (minus sign). Microcode data files are assumed to be in .dat text format if they have a .dat suffix, and to be in binary format otherwise. Standard input (<i>stdin</i>) is assumed to be in .dat text format. The <i>-t</i> option can be used to change the type of the files specified after it, including for <i>stdin</i>. If a directory is specified, all files whose names do not begin with a dot will be loaded, in unspecified order. Nested directories are skipped. Empty files and directories are ignored, and will be skipped. You can select which microcodes should be written out, listed or uploaded to the kernel using the <i>-S</i>, <i>-s</i>, <i>&#8211;date-before</i> and <i>&#8211;date-after</i> options. Should none of those options be specified, all microcodes will be selected. You can upload the selected microcodes to the kernel, write them out to a file (in binary format), to a Linux early initramfs archive, to per-processor-signature files in a directory, or to per-microcode files in a directory using the <i>-w</i>, <i>&#8211;write-earlyfw</i>, <i>-k</i>, <i>-K</i>, and <i>-W</i> options. <code>iucode_tool</code> will identify microcodes in its output and error messages using a &#8220;<i>n/k</i>&#8221; notation, where &#8220;<i>n</i>&#8221; is the bundle number, and &#8220;<i>k</i>&#8221; is the microcode number within that bundle. The output of the <i>&#8211;list-all</i> option when processing multiple input files is the best example of how it works. For more information about Intel processor microcodes, please read the included documentation and the Intel manuals listed in the <i>SEE ALSO</i> section. </p>
<h2>Options</h2>
<p><code>iucode_tool</code> accepts the following options: </p>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Inhibit usual output.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Print more information. Use more than once for added verbosity.</p>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd>List all available options and their meanings.</p>
<dt><code>&#8211;usage</code></p>
<dd>Show summary of options.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show version of program. </p>
<dt><code>-t </code><i>type</i></p>
<dd>Sets the file type of the following files. <i>type</i> can be:</p>
<dl>
<dd>
<dl>
<dt><code>b</code></p>
<dd>binary format. This is the same format used by the kernel driver and the BIOS/EFI, which is described in detail by the <i>Intel 64 and IA-32 Architectures Software Developer&#8217;s Manual, Volume 3A,</i> section 9.11.</p>
<dt><code>d</code></p>
<dd>Intel microcode .dat text format. This is the format normally used by Intel to distribute microcode data files.</p>
<dt><code>r</code></p>
<dd>recover microcode in binary format. Search uncompressed generic binary files for microcodes in Intel microcode binary format to recover. Note: It can find microcode that will not pass strict checks, and thus cause <code>iucode_tool</code> to exit if the <i>&#8211;no-strict-checks</i> or <i>&#8211;ignore-broken</i> options are not in effect.</p>
<dt><code>a</code></p>
<dd>(default) <code>iucode_tool</code> will use the suffix of the file name to select the file type: .dat text format for files that have a <i>.dat</i> suffix, and binary type otherwise. Note that for <i>stdin</i>, .dat text format is assumed.</dl>
</dl>
<dt><code>&#8211;downgrade</code></p>
<dd>When multiple versions of the microcode for a specific processor are available from different files, keep the one from the file loaded last, regardless of revision levels. Files are always loaded in the order they were specified in the command line. This option has no effect when just one file has been loaded. </p>
<dt><code>&#8211;no-downgrade</code></p>
<dd>When multiple versions of the microcode for a specific processor are available from different files, keep the one with the highest revision level. This is the default mode of operation. </p>
<dt><code>&#8211;strict-checks</code></p>
<dd>Perform strict checks on the microcode data. It will refuse to load microcodes and microcode data files with unexpected size and metadata. It will also refuse to load microcode entries that have the same metadata, but different payload. This is the default mode of operation. </p>
<dt><code>&#8211;no-strict-checks</code></p>
<dd>Perform less strict checks on the microcode data. Use only if you happen to come across a microcode data file that has microcodes with weird sizes or incorrect non-critical metadata (such as invalid dates), which you want to retain. If you just want to skip those, use the <i>&#8211;ignore-broken</i> option. </p>
<dt><code>&#8211;ignore-broken</code></p>
<dd>Skip broken microcode entries when loading a microcode data file, instead of aborting program execution. If the microcode entry has an unsupported format or had its header severely corrupted, all remaining data in the file will have to be ignored. In that case, using a file type of <i>recover microcode in binary format</i> (<i>-tr</i> option) is recommended, as it can skip over badly mangled microcode data. </p>
<dt><code>&#8211;no-ignore-broken</code></p>
<dd>Abort program execution if a broken microcode is found while loading a microcode data file. This is the default mode of operation. </p>
<dt><code>-s ! | [!]</code><i>signature</i><code>[,[</code><i>pf_mask</i><code>][,[</code><i>lt:</i><code>|</code><i>eq:</i><code>|</code><i>gt:</i><code>]</code><i>revision</i><code>]]</code></p>
<dd>Select microcodes by the specified <i>signature</i>, <i>processor flags mask</i> (<i>pf_mask</i>), and <i>revision</i>. </p>
<p> If the <i>processor flags mask</i> is specified, it will select only microcodes that are suitable for at least one of the processor flag combinations present in the mask. </p>
<p> If the <i>revision</i> is specified, optionally prefixed by one of the &#8220;<i>eq:</i>&#8220;, &#8220;<i>lt:</i>&#8221; or &#8220;<i>gt:</i>&#8221; operators, it will select only microcodes that have that same <i>revision</i> (if no operator, or if the &#8220;<i>eq:</i>&#8221; operator is used), or microcodes that have a <i>revision</i> that is less than (&#8220;<i>lt:</i>&#8221; operator), or greater than (&#8220;<i>gt:</i>&#8221; operator), the one specified. </p>
<p> Specify more than once to select more microcodes. This option can be combined with the <i>&#8211;scan-system</i> option to select more microcodes. If <i>signature</i> is prefixed with a &#8220;<i>!</i>&#8221; (exclamation mark), it will deselect microcodes instead. Ordering matters, with later <i>-s</i> options overriding earlier ones, including <i>&#8211;scan-system</i>. </p>
<p> When specifying <i>signature</i> and <i>pf_mask</i>, hexadecimal numbers must be prefixed with &#8220;<i>0x</i>&#8220;, and octal numbers with &#8220;<i>0</i>&#8220;. Decimal numbers must not have leading zeros, otherwise they would be interpreted as octal numbers. </p>
<p> The special notation <i>-s!</i> (with no <i>signature</i> parameter) instructs <code>iucode_tool</code> to require explicit inclusion of microcode signatures (using the non-negated form of <i>-s</i>, or using <i>&#8211;scan-system</i>). </p>
<dt><code>-S</code>, <code>&#8211;scan-system</code>[=<i>mode</i>]</p>
<dd>Select microcodes by scanning online processors on this system for their signatures. </p>
<p> This option can be used only once, and it can be combined with the <i>-s</i> option to select more microcodes. The microcodes selected by <i>&#8211;scan-system</i> can also be deselected by a later <i>-s&nbsp;!signature</i> option. </p>
<p> The optional <i>mode</i> argument (accepted only by the long version of the option) selects the strategy used to scan processors:</p>
<dl>
<dd>
<dl>
<dt><code>0</code> or <code>auto</code></p>
<dd>Currently the same as <code>fast</code>, but this might change in future versions if Intel ever deploys multi-signature systems that go beyond mixed-stepping. This is the default mode of operation, for backwards compatibility with previous versions of <code>iucode_tool</code>.</p>
<dt><code>1</code> or <code>fast</code></p>
<dd>Uses the cpuid instruction to detect the signature of the processor <code>iucode_tool</code> is running on, and selects all steppings for that processor&#8217;s type, family and model. Supports mixed-stepping systems.</p>
<dt><code>2</code> or <code>exact</code></p>
<dd>Uses kernel drivers to scan the signature of every online processor directly. This mode supports multi-signature systems. This scan mode will be slow on large systems with many processors, and likely requires special permissions (such as running as the root user). Should the scan fail for any reason, as a fail-safe measure, it will issue an warning and consider all possible steppings for every signature it did manage to scan successfully.</dl>
</dl>
<dt><code>&#8211;date-before</code>=<i>YYYY-MM-DD</i> and <code>&#8211;date-after</code>=<i>YYYY-MM-DD</i></p>
<dd>Limit the selected microcodes by a date range. The date must be given in ISO format, with four digits for the year and two digits for the month and day and &#8220;<i>&#8211;</i>&#8221; (minus sign) for the separator. Dates are not range-checked, so you can use <i>&#8211;date-after=2000-00-00</i> to select all microcodes dated since January 1st, 2000. </p>
<dt><code>&#8211;loose-date-filtering</code></p>
<dd>When a date range is specified, all revisions of the microcode will be considered for selection (ignoring just the date range, all other filters still apply) should any of the microcode&#8217;s revisions be within the date range. </p>
<dt><code>&#8211;strict-date-filtering</code></p>
<dd>When a date range is specified, select only microcodes which are within the date range. This is the default mode of operation. </p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>List selected microcode signatures to standard output (<i>stdout</i>).</p>
<dt><code>-L</code>, <code>&#8211;list-all</code></p>
<dd>List all microcode signatures while they&#8217;re being processed to standard output (<i>stdout</i>). </p>
<dt><code>-k</code>[<i>device</i>], <code>&#8211;kernel</code>[=<i>device</i>]</p>
<dd>Upload selected microcodes to the kernel. Optionally, the device path can be specified (default: <i>/dev/cpu/microcode</i>). This update method is deprecated: it will be removed eventually from the kernel and from iucode_tool.</p>
<dt><code>-K</code>[<i>directory</i>], <code>&#8211;write-firmware</code>[=<i>directory</i>]</p>
<dd>Write selected microcodes with the file names expected by the Linux kernel firmware loader. Optionally, the destination directory can be specified (default: <i>/lib/firmware/intel-ucode</i>). </p>
<dt><code>-w</code><i>file</i>, <code>&#8211;write-to</code>=<i>file</i></p>
<dd>Write selected microcodes to a file in binary format. </p>
<dt><code>&#8211;write-earlyfw</code>=<i>file</i></p>
<dd>Write selected microcodes to an early initramfs archive, which should be prepended to the regular initramfs to allow the kernel to update processor microcode very early during system boot. </p>
<dt><code>-W</code><i>directory</i>, <code>&#8211;write-named-to</code>=<i>directory</i></p>
<dd>Write selected microcodes to the specified directory, one microcode per file, in binary format. The file names reflect the microcode signature, processor flags mask and revision. </p>
<dt><code>&#8211;write-all-named-to</code>=<i>directory</i></p>
<dd>Write every microcode to the specified directory, one microcode per file, in binary format. The file names reflect the microcode signature, processor flags mask and revision. This is the only way to write out every revision of the same microcode. </p>
<dt><code>&#8211;overwrite</code></p>
<dd>Remove the destination file before writing, if it exists and is not a directory. The destination file is not overwritten in-place. Hardlinks will be severed, and any existing access permissions, ACLs and other extended attributes of the old destination file will be lost. </p>
<dt><code>&#8211;no-overwrite</code></p>
<dd>Abort if the destination file already exists. This is the default mode of operation. Do note that iucode_tool does not follow non-directory symlinks when writing files. </p>
<dt><code>&#8211;mini-earlyfw</code></p>
<dd>Optimize the early initramfs cpio container for minimal size. It will change the cpio block size to 16 bytes, and remove header entries for the parent directories of the microcode data file. As a result, the microcode data file will not be available to the regular initramfs, and tools might complain about the non-standard cpio block size. </p>
<p> This will typically reduce the early initramfs size by 736 bytes. </p>
<dt><code>&#8211;normal-earlyfw</code></p>
<dd>Optimize the early initramfs size for tool compatibility. This is the default mode of operation. The microcode data file will be available inside the regular initramfs as well. </p>
</dl>
<h2>Notes</h2>
<p><code>iucode_tool</code> reads all data to memory before doing any processing. It enforces a sanity limit of a maximum of 1GiB worth of binary microcode data per microcode data file. All informational and error messages are sent to standard error (<i>stderr</i>), while user-requested output (such as output generated by the list options) is sent to standard output (<i>stdout</i>). <code>iucode_tool</code> creates files with permissions 0644 (rw-r&#8211;r&#8211;), modified by the current umask. <code>iucode_tool</code>&#8216;s selected microcode listing and microcode output files are sorted first by <i>processor signature</i> (in ascending order), and then by <i>processor flags mask</i> (in descending order). When multiple revisions of a microcode are selected, the older ones will be skipped. Only the newest selected revision of a microcode (or the last one in load order when the <i>&#8211;downgrade</i> option is active) will be written to a file or uploaded to the kernel. Intel microcode data files, both in binary and text formats, can be concatenated to generate a bigger and still valid microcode data file. <code>iucode_tool</code> does not follow symlinks when writing microcode data files. It will either refuse to write the file and abort (default mode of operation), or (when the <i>&#8211;overwrite</i> option is active) it will remove the target symlink or file (and therefore breaking hardlinks) <i>before</i> writing the new file. <code>iucode_tool</code> does follow directory symlinks to locate the directory to write files into.</p>
<h3>Linux Notes</h3>
<p>Before Linux v4.4, the microcode update driver was split in two parts: the early microcode update driver (which gets microcode data from the initramfs) and the late microcode update driver, which could be a module and got microcode data from the firmware subsystem. The two drivers were unified in Linux v4.4. The microcode update driver needs to be present in the system at all times to ensure microcode updates are reapplied on resume from suspend and CPU hotplug. Do not unload the microcode module, unless you really know better. Since Linux v4.4, the late microcode driver cannot be a module anymore and will always be present in the system when enabled. Updating microcode early is safer. It can only be done at boot and it requires an initramfs, but it is strongly recommended: late microcode updates (which read microcode data from /lib/firmware) cannot safely change visible processor features. Early microcode updates are available since Linux v3.9. They can safely change visible processor features (such as the microcode updates that disabled Intel TSX instructions on Intel Haswell cores do). They require an uncompressed initramfs image with the microcode update data in <i>/kernel/x86/microcode/GenuineIntel.bin</i>. This uncompressed initramfs image must come before any compressed initramfs image(s), and it has an special name: <i>early initramfs</i>. The microcode update data inside the early initramfs image must be aligned to a 16-byte boundary due to a bug in several versions of the Linux kernel early microcode update driver. This requires special steps when creating the initramfs archive with the microcode data, and will be handled automatically by the <code>iucode_tool</code> <i>&#8211;write-earlyfw</i> option. Since Linux v4.2, it is also possible to build a kernel with the microcode update data as built-in firmware, using the CONFIG_FIRMWARE_IN_KERNEL facility. This feature is not yet mature as of Linux v4.2.8, v4.4.11, v4.5.5 and v4.6, and might not work in every case. The <i>/dev/cpu/microcode</i> update interface has been deprecated and should not be used. It has one special requirement: each write syscall must contain whole microcode(s). It can be accessed through <code>iucode_tool</code> <i>&#8211;kernel</i>. Up to Linux v3.5, late microcode updates were required to be triggered per-core, by writing the number 1 to <i>/sys/devices/system/cpu/*/microcode/reload</i> for every cpu. Depending on kernel version, you must either trigger it on every core to avoid a dangerous situation where some cores are using outdated microcode, or the kernel will accept the request only for the boot processor and use it to trigger an update on all system processor cores. Since Linux v3.6, the late microcode update driver has a new interface that explicitly triggers an update for every core at once when the number 1 is written to <i>/sys/devices/system/cpu/microcode/reload</i>. </p>
<h2>Examples</h2>
<h3>Updating files in <i>/lib/firmware/intel-ucode</i>:</h3>
<dl>
<dd>iucode_tool -K/lib/firmware/intel-ucode \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/lib/firmware/intel-ucode \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/tmp/file-with-new-microcodes.bin
</dl>
<h3>Processing several compressed files at once:</h3>
<dl>
<dd>zcat intel-microcode*.dat.gz | iucode_tool -l &#8211;</p>
<dd>zcat intel-microcode*.bin.gz | iucode_tool -l -tb &#8211;</dl>
<h3>Selecting microcodes and creating an early initramfs:</h3>
<dl>
<dd>iucode_tool &#8211;scan-system \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8211;write-earlyfw=/tmp/early.cpio \</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/lib/firmware/intel-ucode</p>
<dd>iucode_tool -s 0x106a5 -s 0x106a4 -l /lib/firmware/intel-ucode</dl>
<h3>Using the recovery loader to load and to update microcode in an early initramfs:</h3>
<dl>
<dd>iucode_tool -L -tr /boot/intel-ucode.img</p>
<dd>iucode_tool -Ll -S &#8211;write-earlyfw=/boot/intel-ucode.img.new \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-tr /boot/intel-ucode.img -tb /lib/firmware/intel-ucode &amp;&amp; \</p>
<p> mv /boot/intel-ucode.img.new /boot/intel-ucode.img </p>
<h2>Bugs</h2>
<p>Microcode with negative revision numbers is not special-cased, and will not be preferred over regular microcode. The <i>downgrade mode</i> should be used only for microcodes with the same <i>processor flags mask</i>. It cannot handle the corner cases where modifying a <i>processor flags mask</i> would be required to force the kernel to load a lower revision of a microcode, and <code>iucode_tool</code> will issue an warning when that happens. So far, this has not proved to be a relevant limitation as changes to the <i>processor flags mask</i> of post-launch, production microcode updates are very rare. The <i>loader version</i> microcode metadata field is ignored by <code>iucode_tool</code>. This shouldn&#8217;t cause problems as long as the same signature never needs more than a single type of loader. Files are not replaced atomically: if <code>iucode_tool</code> is interrupted while writing to a file, that file will be corrupted. </p>
<h2>See Also</h2>
<p><code>The Intel 64 and IA-32 Architectures Software Developer&#8217;s Manual, Volume 3A: System Programming Guide, Part 1</code> (order number 253668), section 9.11.</p>
<h2>Author</h2>
<p>Henrique de Moraes Holschuh &lt;hmh [at] hmh.eng.br&gt;</p>
