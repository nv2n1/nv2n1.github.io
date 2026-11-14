---
title: "wodim(1)"
name: "wodim"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wodim/"
description: "wodim – write data to optical disk media"
---

<h2>NAME</h2>
<p> wodim &#8211; write data to optical disk media</p>
<h2>SYNOPSIS</h2>
<p> <code>wodim</code> [<i>options</i>] <i>track1</i>&#8230;<i>trackn</i></p>
<h2>NOTE</h2>
<p> There may be similarities and differences between this program and other disk recording application(s). See the <code>CREDITS</code> and <code>AUTHORS</code> sections below to learn about the origin of <code>wodim.</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>wodim</code> is used to record data or audio Compact Discs on an Orange Book CD-Recorder or to write DVD media on a DVD-Recorder. </p>
<p> The <i>device</i> is the device file or label offered by the operating system to access the recorder with SCSI GENERIC (sg) interface. Note that some operating systems may provide separate device nodes for block-oriented and sg access. For example, on older <i>Linux</i> systems, the sg access was available through <i>/dev/sg&#8230;</i> files while the block oriented access was done through associated (but not identical) <i>/dev/hd&#8230;</i> and <i>/dev/sr&#8230;</i> (or <i>/dev/scd&#8230;</i> ) files. </p>
<p> In any case, the user running <code>wodim</code> needs read and write access to the particular device file on a Linux system. It is recommended to be root or install the application as suid-root, because certain versions of Linux (kernel) limit the set of SCSI commands allowed for non-root users. Even if usage without root identity is possible in many cases, some device drivers still may fail, show unexplainable problems and generally the problems become harder to debug. The risk for buffer-underruns is also increased. See the <i>PROCESS SCHEDULING PRIORITY</i> section below for more details. </p>
<p> There is an alternative way of specifying the device, using the traditional SCSI descriptions in form of <i>devicetype:bus/target/lun</i> specification. However, the success of this method is not guaranteed since it requires an adaptation scheme for your architecture, and the numbers may vary depending on the hardware-internal numbering or on the order of hot-plug device detection. If your operating system does not provide a sufficient framework for keeping this numbers persistent, don&#8217;t rely on them. See <code>-scanbus</code> and <code>&#8211;devices</code> options below for details. </p>
<p> There are emulated SCSI compatible device systems, using the SCSI protocols transported over various hardware/media types. The most known examples is ATAPI (&quot;IDE burners&quot;) or USB storage (&quot;external USB case&quot;). If the pseudo-SCSI b/t/l device address specification is used instead of the native one, you need to prepend the &quot;devicetype:&quot; description to the emulated &quot;bus/target/lun&quot; device address. </p>
<p> If a file /etc/wodim.conf exists, the parameter to the <code>dev=</code> option may also be a drive name label in that file (see FILES section). </p>
<p> As a special exception, the device specification can be <i>-1</i> or just omitted, which invokes automatic guessing of an appropriate device for the selected operation. However, this guessing is not available everywhere and is not reliable; it is only available for the user&#8217;s convenience in simple environments. </p>
<p> In <i>Track At Once </i> mode, each <i>track</i> corresponds to a single file that contains the prepared data for that track. If the argument is `<code>&#8211;</code>&#8216;, standard input is used for that track. Only one track may be taken from <i>stdin</i>. In the other write modes, the direct file to track relation may not be implemented. In <code>-clone</code> mode, a single file contains all data for the whole disk. To allow DVD writing on platforms that do not implement large file support, <code>wodim</code> concatenates all file arguments to a single track when writing to DVD media. </p>
<h2>PROCESS SCHEDULING PRIORITY</h2>
<p> Wodim tries to get higher process priority using different methods. This is important because the burn process is usually a realtime task, no long delays should occur while transmitting fresh data to the recorder. This is especially important on systems with insufficient RAM where swapping can create delays of many seconds. </p>
<p> A possible workaround on underpowered systems is the use of the burnfree or similar feature, allowing the recorder to resume. </p>
<p> Root permissions are usually required to get higher process scheduling priority. </p>
<p> On <code>SVr4 </code> compliant systems, <code>wodim </code> uses the real time class to get the highest scheduling priority that is possible (higher than all kernel processes). On systems with <code>POSIX real time scheduling</code> wodim uses real time scheduling too, but may not be able to gain a priority that is higher than all kernel processes. </p>
<p> In order to be able to use the SCSI transport subsystem of the OS, run at highest priority and lock itself into core <code>wodim</code> either needs to be run as root, needs to be installed suid root or must be called via <code>RBACs</code> pfexec mechanism. </p>
<h2>GENERAL OPTIONS</h2>
<p> General options must be before any track file name or track option.</p>
<dl>
<dt><code>-version</code></p>
<dd> Print version information and exit.</p>
<dt><code>-v</code></p>
<dd> Increment the level of general verbosity by one. This is used e.g. to display the progress of the writing process.</p>
<dt><code>-V</code></p>
<dd> Increment the verbose level in respect of SCSI command transport by one. This helps to debug problems during the writing process, that occur in the CD/DVD-Recorder. If you get incomprehensible error messages you should use this flag to get more detailed output. <code>-VV</code> will show data buffer content in addition. Using <code>-V</code> or <code>-VV</code> slows down the process and may be the reason for a buffer underrun.</p>
<dt><code>debug=</code><i>#, </i><code>-d</code></p>
<dd> Set the misc debug value to # (with debug=#) or increment the misc debug level by one (with -d). If you specify <i>-dd,</i> this equals to <code>debug=</code><i>2.</i> This may help to find problems while opening a driver for libusal as well as with sector sizes and sector types. Using <code>-debug</code> slows down the process and may be the reason for a buffer underrun.</p>
<dt><code>kdebug=</code>#, <code>kd=</code>#</p>
<dd> Tell the <code>usal</code>-driver to modify the kernel debug value while SCSI commands are running.</p>
<dt><code>-silent</code>, <code>-s</code></p>
<dd> Do not print out a status report for failed SCSI commands.</p>
<dt><code>-force</code></p>
<dd> Force to continue on some errors. Be careful when using this option. <code>wodim</code> implements several checks that prevent you from doing unwanted things like damaging CD-RW media by improper drives. Many of the sanity checks are disabled when the <code>-force</code> option is used. </p>
<p> This option also implements some tricks that will allow you to blank bad CD-RW disks.</p>
<dt><code>-immed</code></p>
<dd> Tell wodim to set the <code>SCSI IMMED</code> flag in certain commands (load/eject/blank/close_track/close_session). This can be useful on broken systems with ATAPI harddisk and CD/DVD writer on the same bus or with SCSI systems that don&#8217;t use disconnect/reconnect. These systems will freeze while blanking or fixating a CD/DVD or while a DVD writer is filling up a session to the minimum amount (approx. 800 MB). Setting the <code>-immed</code> flag will request the command to return immediately while the operation proceeds in background, making the bus usable for the other devices and avoiding the system freeze. This is an experimental feature which may work or not, depending on the model of the CD/DVD writer. A correct solution would be to set up a correct cabling but there seem to be notebooks around that have been set up the wrong way by the manufacturer. As it is impossible to fix this problem in notebooks, the <code>-immed</code> option has been added. </p>
<p> A second experimental feature of the <code>-immed</code> flag is to tell wodim to try to wait short times while writing to the media. This is expected to free the IDE bus if the CD/DVD writer and the data source are connected to the same IDE cable. In this case, the CD/DVD writer would otherwise usually block the IDE bus for nearly all the time making it impossible to fetch data from the source drive. See also <code>minbuf=</code> and <code>-v</code> option. </p>
<p> Use both features at your own risk. If it turns out that it would make sense to have a separate option for the wait feature, write to the author and convince him.</p>
<dt><code>minbuf=</code><i>value</i></p>
<dd> The # <code>minbuf=</code> option allows to define the minimum drive buffer fill ratio for the experimental ATAPI wait mode that is intended to free the IDE bus to allow hard disk and CD/DVD writer to be on the same IDE cable. As the wait mode currently only works when the verbose option <code>-v</code> has been specified, <code>wodim</code> implies the verbose option in case the <code>-immed</code> or <code>minbuf=</code> option have been specified. Valid values for <code>minbuf= </code> are between 25 and 95 for 25%&#8230;95% minimum drive buffer fill ratio.</p>
<dt><code>-dummy</code></p>
<dd> The CD/DVD-Recorder will go through all steps of the recording process, but the laser is turned off during this procedure. It is recommended to run several tests before actually writing to a Compact Disk or Digital Versatile Disk, if the timing and load response of the system is not known.</p>
<dt><code>-clone</code></p>
<dd> Tells <code>wodim</code> to handle images created by <i>readom -clone</i>. The <code>-clone</code> may only be used in conjunction with with the <code>-raw96r</code> or with the <code>-raw16</code> option. Using <code>-clone</code> together with <code>-raw96r</code> is preferred as it allows to write all subchannel data. The option <code>-raw16</code> should only be used with drives that do not support to write in <code>-raw96r</code> mode.</p>
<dt><code>-dao</code></p>
<dd>
<dt><code>-sao</code></p>
<dd> Set <code>SAO (Session At Once)</code> mode which is usually called <code>Disk At Once </code>mode. This currently only works with MMC drives that support <code>Session At Once</code> mode. Note that wodim needs to know the size of each track in advance for this mode (see the <code>genisoimage -print-size</code> option and the <i>EXAMPLES</i> section for more information).</p>
<dt><code>-tao</code></p>
<dd> Set <code>TAO (Track At Once) writing mode.</code> This is the default write mode in previous <code>wodim</code> versions. With most drives, this write mode is required for multi session recording.</p>
<dt><code>-raw</code></p>
<dd> Set <code>RAW writing mode.</code> Using this option defaults to <code>-raw96r</code>. Note that wodim needs to know the size of each track in advance for this mode (see the <code>genisoimage -print-size</code> option and the <i>EXAMPLES</i> section for more information).</p>
<dt><code>-raw96r</code></p>
<dd> Select Set <code>RAW writing mode</code> with 2352 byte sectors plus 96 bytes of raw P-W subchannel data resulting in a sector size of 2448 bytes. This is the preferred raw writing mode as it gives best control over the CD writing process. If you find any problems with the layout of a disk or with sub channel content (e.g. wrong times on the display when playing the CD) and your drive supports to write in <code>-raw96r</code> or <code>-raw16</code> mode, you should give it a try. There are several CD writers with bad firmware that result in broken disks when writing in TAO or SAO mode. Writing data disks in raw mode needs significantly more CPU time than other write modes. If your CPU is too slow, this may result in buffer underruns. Note that wodim needs to know the size of each track in advance for this mode (see the <code>genisoimage -print-size</code> option and the <i>EXAMPLES</i> section for more information).</p>
<dt><code>-raw96p</code></p>
<dd> Select Set <code>RAW writing mode</code> with 2352 byte sectors plus 96 bytes of packed P-W subchannel data resulting in a sector size of 2448 bytes. This is the less preferred raw writing mode as only a few recorders support it and some of these recorders have bugs in the firmware implementation. Don&#8217;t use this mode if your recorder supports <code>-raw96r</code> or <code>-raw16</code>. Writing data disks in raw mode needs significantly more CPU time than other write modes. If your CPU is too slow, this may result in buffer underruns. Note that wodim needs to know the size of each track in advance for this mode (see the <code>genisoimage -print-size</code> option and the <i>EXAMPLES</i> section for more information).</p>
<dt><code>-raw16</code></p>
<dd> Select Set <code>RAW writing mode</code> with 2352 byte sectors plus 16 bytes of P-Q subchannel data resulting in a sector size of 2368 bytes. If a recorder does not support <code>-raw96r</code>, this is the preferred raw writing mode. It does not allow to write <i>CD-Text</i> or <i>CD+Graphics</i> but it is the only raw writing mode in cheap CD writers. As these cheap writers in most cases do not support <code>-dao</code> mode. Don&#8217;t use this mode if your recorder supports <code>-raw96r</code>. Writing data disks in raw mode needs significantly more CPU time than other write modes. If your CPU is too slow, this may result in buffer underruns. Note that wodim needs to know the size of each track in advance for this mode (see the <code>genisoimage -print-size</code> option and the <i>EXAMPLES</i> section for more information).</p>
<dt><code>-multi</code></p>
<dd> Allow multi session CDs to be made. This flag needs to be present on all sessions of a multi session disk, except you want to create a session that will be the last session on the media. The fixation will be done in a way that allows the CD/DVD-Recorder to append additional sessions later. This is done by generation a TOC with a link to the next program area. The so generated media is not 100% compatible to manufactured CDs (except for CDplus). Use only for recording of multi session CDs. If this option is present, the default track type is <code>CD-ROM XA mode 2 form 1</code> and the sector size is 2048 bytes. The XA sector subheaders will be created by the drive. The <i>Sony </i> drives have no hardware support for <code>CD-ROM XA mode 2 form 1</code>. You have to specify the <code>-data </code> option in order to create multi session disks on these drives. As long as wodim does not have a coder for converting data sectors to audio sectors, you need to force <code>CD-ROM</code> sectors by including the <code>-data</code> option if you like to record a multisession disk in SAO mode. Not all drives allow multisession CDs in SAO mode.</p>
<dt><code>-msinfo</code></p>
<dd> Retrieve multi session info in a form suitable for <code>genisoimage</code> and print it to standard output. See <code>msifile=</code> option for another version. </p>
<p> This option makes only sense with a CD that contains at least one closed session and is appendable (not finally closed yet). Some drives create error messages if you try to get the multi session info for a disk that is not suitable for this operation.</p>
<dt><code>msifile=</code>filename</p>
<dd> Like <code>-msinfo</code> option but also stores the multi session info in a file.</p>
<dt><code>-toc</code></p>
<dd> Retrieve and print out the table of content or PMA of a CD. With this option, <code>wodim</code> will work with CD-R drives and with CD-ROM drives.</p>
<dt><code>-atip</code></p>
<dd> Retrieve and print out the ATIP (absolute Time in Pre-groove) info of a CD/DVD recordable or CD/DVD re-writable media. With this option, <code>wodim</code> will try to retrieve the ATIP info. If the actual drive does not support to read the ATIP info, it may be that only a reduced set of information records or even nothing is displayed. Only a limited number of MMC compliant drives support to read the ATIP info. </p>
<p> If <code>wodim</code> is able to retrieve the lead-in start time for the first session, it will try to decode and print the manufacturer info from the media. DVD media does not have ATIP information but there is equivalent prerecorded information that is read out and printed.</p>
<dt><code>-fix</code></p>
<dd> The disk will only be fixated (i.e. a TOC for a CD-Reader will be written). This may be used, if for some reason the disk has been written but not fixated. This option currently does not work with old TEAC drives (CD-R50S and CD-R55S).</p>
<dt><code>-nofix</code></p>
<dd> Do not fixate the disk after writing the tracks. This may be used to create an audio disk in steps. An un-fixated disk can usually not be used on a non CD-writer type drive but there are audio CD players that will be able to play such a disk.</p>
<dt><code>-waiti</code></p>
<dd> Wait for input to become available on standard input before trying to open the SCSI driver. This allows <code>wodim</code> to read its input from a pipe even when writing additional sessions to a multi session disk. When writing another session to a multi session disk, <code>genisoimage </code> needs to read the old session from the device before writing output. This cannot be done if <code>wodim </code> opens the SCSI driver at the same time.</p>
<dt><code>-load</code></p>
<dd> Load the media and exit. This only works with a tray loading mechanism but seems to be useful when using the Kodak disk transporter.</p>
<dt><code>-lock</code></p>
<dd> Load the media, lock the door and exit. This only works with a tray loading mechanism but seems to be useful when using the Kodak disk transporter.</p>
<dt><code>-eject</code></p>
<dd> Eject disk after doing the work. Some devices (e.g. Philips) need to eject the medium before creating a new disk. Doing a -dummy test and immediately creating a real disk would not work on these devices.</p>
<dt><code>speed=</code>#</p>
<dd> Set the speed factor of the writing process to #. # is an integer, representing a multiple of the audio speed. This is about 150 KB/s for CD-ROM, about 172 KB/s for CD-Audio and about 1385 kB/s for DVD media. If no <i>speed</i> option is present, <code>wodim</code> will try to get a drive specific speed value from the file <code>/etc/wodim.conf</code> and if it cannot find one, it will try to get the speed value from the <code>CDR_SPEED</code> environment and later from the <code>CDR_SPEED=</code> entry in <code>/etc/wodim.conf</code>. If no speed value could be found, wodim uses a drive specific default speed. The default for all new (MMC compliant) drives is to use the maximum supported by the drive. If you use <i>speed=0</i> with a MMC compliant drive, <code>wodim</code> will switch to the lowest possible speed for drive and medium. If you are using an old (non MMC) drive that has problems with <i>speed=2 </i> or <i>speed=4</i>, you should try <i>speed=0</i>.</p>
<dt><code>blank=</code><i>type</i></p>
<dd> Blank a CD-RW and exit or blank a CD-RW before writing. The blanking type may be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt>help</p>
<dd> Display a list of possible blanking types.</p>
<dt>all</p>
<dd> Blank the entire disk. This may take a long time.</p>
<dt>fast</p>
<dd> Minimally blank the disk. This results in erasing the PMA, the TOC and the pregap.</p>
<dt>track</p>
<dd> Blank a track.</p>
<dt>unreserve</p>
<dd> Unreserve a reserved track.</p>
<dt>trtail</p>
<dd> Blank the tail of a track.</p>
<dt>unclose</p>
<dd> Unclose last session.</p>
<dt>session</p>
<dd> Blank the last session.</dl>
</dl>
<p> Not all drives support all blanking types. It may be necessary to use <code>blank=all</code> if a drive reports a specified command as being invalid. If used together with the <code>-force</code> flag, this option may be used to blank CD-RW disks that otherwise cannot be blanked. Note that you may need to specify <code>blank=</code><i>all</i> because some drives will not continue with certain types of bad CD-RW disks. Note also that <code>wodim</code> does its best if the <code>-force </code> flag is used but it finally depends on the drive&#8217;s firmware whether the blanking operation will succeed or not.</p>
<dt><code>-format</code></p>
<dd> Format a CD-RW/DVD-RW/DVD+RW disc. Formatting is currently only implemented for DVD+RW media. A &#8216;maiden&#8217; DVD+RW media needs to be formatted before you may write to it. However, as <code>wodim</code> autodetects the need for formatting in this case and auto formats the medium before it starts writing, the <code>-format</code> option is only needed if you like to forcibly reformat a DVD+RW medium.</p>
<dt><code>fs=</code>#</p>
<dd> Set the FIFO (ring buffer) size to #. You may use the same syntax as in <code><a href="/docs/linux/man/1-dd/">dd</a></code>(1), <code><a href="/docs/linux/man/1-sdd/">sdd</a></code>(1) or <code><a href="/docs/linux/man/1-star/">star</a></code>(1). The number representing the size is taken in bytes unless otherwise specified. If a number is followed directly by the letter `b&#8217;, `k&#8217;, `m&#8217;, `s&#8217; or `f&#8217;, the size is multiplied by 512, 1024, 1024*1024, 2048 or 2352. If the size consists of numbers separated by `x&#8217; or `*&#8217;, multiplication of the two numbers is performed. Thus <i>fs=10x63k</i> will specify a FIFO size of 630 kBytes. </p>
<p> The size specified by the <i>fs=</i> argument includes the shared memory that is needed for administration. This is at least one page of memory. If no <i>fs</i>= option is present, <code>wodim</code> will try to get the FIFO size value from the <code>CDR_FIFOSIZE</code> environment. The default FIFO size is currently 4 MB. </p>
<p> The FIFO is used to increase buffering for the real time writing process. It allows to run a pipe from <code>genisoimage</code> directly into <code>wodim</code>. If the FIFO is active and a pipe from <code>genisoimage</code> into <code>wodim</code> is used to create a CD, <code>wodim</code> will abort prior to do any modifications on the disk if <code>genisoimage </code> dies before it starts writing. The recommended FIFO size is between 4 and 128 MBytes. As a rule of thumb, the FIFO size should be at least equal to the size of the internal buffer of the CD/DVD-Recorder and no more than half of the physical amount of RAM available in the machine. If the FIFO size is big enough, the FIFO statistics will print a FIFO empty count of zero and the FIFO min fill is not below 20%. It is not wise to use too much space for the FIFO. If you need more than 8 MB to write a CD at a speed less than 20x from an image on a local file system on an idle machine, your machine is either underpowered, has hardware problems or is mis-configured. If you like to write DVDs or CDs at higher speed, it makes sense to use at least 16 MB for the FIFO. </p>
<p> On old and small machines, you need to be more careful with the FIFO size. If your machine has less than 256 MB of physical RAM, you should not set up a FIFO size that is more than 32 MB. The sun4c architecture (e.g. a Sparcstation-2) has only MMU page table entries for 16 MBytes per process. Using more than 14 MBytes for the FIFO may cause the operating system in this case to spend much time to constantly reload the MMU tables. Newer machines from Sun do not have this MMU hardware problem. I have no information on PC-hardware reflecting this problem. </p>
<p> Old Linux systems for non x86 platforms have broken definitions for the shared memory size. You need to fix them and rebuild the kernel or manually tell <code>wodim</code> to use a smaller FIFO. </p>
<p> If you have buffer underruns or similar problems (like a constantly empty drive buffer) and observe a zero <i>fifo empty count</i>, you have hardware problems that prevents the data from flowing fast enough from the kernel memory to the drive. The FIFO size in this case is sufficient, but you should check for a working DMA setup.</p>
<dt><code>ts=</code>#</p>
<dd> Set the maximum transfer size for a single SCSI command to #. The syntax for the <code>ts=</code> option is the same as for wodim fs=# or sdd bs=#. </p>
<p> If no <code>ts=</code> option has been specified, <code>wodim</code> defaults to a transfer size of 63 kB. If libusal gets lower values from the operating system, the value is reduced to the maximum value that is possible with the current operating system. Sometimes, it may help to further reduce the transfer size or to enhance it, but note that it may take a long time to find a better value by experimenting with the <code>ts=</code> option.</p>
<dt><code>dev=</code><i>target</i></p>
<dd> Sets the SCSI target for the CD/DVD-Recorder, see notes above. A typical device specification is <code>dev=</code><i>6,0</i> . A filename or virtual device name can be passed instead of the symbolic SCSI numbers. The correct device/filename in this case can be found in the system specific manuals of the target operating system. On a <i>FreeBSD</i> system without <i>CAM</i> support, you need to use the control device (e.g. <i>/dev/rcd0.ctl</i>). A correct device specification in this case may be <code>dev=</code><i>/dev/rcd0.ctl:@</i> . </p>
<p> On Linux and Windows 2000/XP, drives are accessible with their device (or drive) names or with the symbolic SCSI numbers (not recommended, mapping is not stable and could be completely removed in the future). </p>
<p> If no <i>dev</i> option is present, <code>wodim</code> will try to get the device from the <code>CDR_DEVICE</code> environment. </p>
<p> If the argument to the <code>dev=</code> option does not contain the characters &#8216;,&#8217;, &#8216;/&#8217;, &#8216;@&#8217; or &#8216;:&#8217;, it is interpreted as an label name that may be found in the file /etc/wodim.conf (see FILES section).</p>
<dt><code>gracetime=</code><i>#</i></p>
<dd> Set the grace time before starting to write to <i>#</i> seconds. Values below 2 seconds are not recommended to give the kernel or volume management a chance to learn the new state.</p>
<dt><code>timeout=</code><i>#</i></p>
<dd> Set the default SCSI command timeout value to <i>#</i> seconds. The default SCSI command timeout is the minimum timeout used for sending SCSI commands. If a SCSI command fails due to a timeout, you may try to raise the default SCSI command timeout above the timeout value of the failed command. If the command runs correctly with a raised command timeout, please report the better timeout value and the corresponding command to the author of the program. If no <i>timeout </i> option is present, a default timeout of 40 seconds is used.</p>
<dt><code>driver=</code><i>name</i></p>
<dd> Allows the user to manually select a driver for the device. The reason for the existence of the <code>driver=</code><i>name</i> option is to allow users to use <code>wodim</code> with drives that are similar to supported drives but not known directly by <code>wodim</code>. All drives made after 1997 should be MMC standard compliant and thus supported by one of the MMC drivers. It is most unlikely that <code>wodim</code> is unable to find the right driver automatically. Use this option with extreme care. If a wrong driver is used for a device, the possibility of creating corrupted disks is high. The minimum problem related to a wrong driver is that the <code>speed=</code> or <code>-dummy</code> will not work. </p>
<dl>
<dt>
<dd>
<p> The following driver names are supported:</p>
<dl>
<dt><code>help</code></p>
<dd> To get a list of possible drivers together with a short description.</p>
<dt><code>mmc_cd</code></p>
<dd> The generic SCSI-3/mmc CD-ROM driver is auto-selected whenever <code>wodim</code> finds a MMC compliant drive that does not identify itself to support writing at all, or that only identifies to support media or write modes not implemented in <code>wodim</code>.</p>
<dt><code>mmc_cd_dvd</code></p>
<dd> The generic SCSI-3/mmc CD/DVD driver is auto-selected whenever <code>wodim</code> finds a MMC-2 or MMC-3 compliant drive that seems to support more than one medium type and the tray is open or no medium could be found to select the right driver. This driver tries to close the tray, checks the medium found in the tray and then branches to the driver that matches the current medium.</p>
<dt><code>mmc_cdr</code></p>
<dd> The generic SCSI-3/mmc CD-R/CD-RW driver is auto-selected whenever <code>wodim</code> find a MMC compliant drive that only supports to write CDs or a multi system drive that contains a CD as the current medium.</p>
<dt><code>mmc_cdr_sony</code></p>
<dd> The generic SCSI-3/mmc CD-R/CD-RW driver is auto-selected whenever <code>wodim</code> would otherwise select the <code>mmc_cdr</code> driver but the device seems to be made by Sony. The <code>mmc_cdr_sony</code> is definitely needed for the Sony CDU 928 as this drive does not completely implement the MMC standard and some of the MMC SCSI commands have to be replaced by Sony proprietary commands. It seems that all Sony drives (even newer ones) still implement the Sony proprietary SCSI commands so it has not yet become a problem to use this driver for all Sony drives. If you find a newer Sony drive that does not work with this driver, please report.</p>
<dt><code>mmc_mdvd</code></p>
<dd> The generic SCSI-3/mmc-2 DVD-R/DVD-RW driver is auto-selected whenever <code>wodim</code> finds a MMC-2 or MMC-3 compliant drive that supports to write DVDs and an appropriate medium is loaded. Note that for unknown reason, the DVD-Plus alliance does not like that there is a simulation mode for DVD+R and DVD+RW media nor a way to erase DVD+RW media. DVD+R and DVD+RW only supports one write mode that is somewhere between Track At Once and Packet writing; this mode is selected in <code>wodim</code> via a the <code>-dao</code>/<code>-sao</code> option. As DVD+RW media needs to be formatted before its first use, <code>wodim</code> auto-detects this media state and performs a format before it starts to write. </p>
<p> Note: If you have any problems during burning DVDs using <code>wodim</code>, please consider <code>growisofs </code> from package <code>dvd+rw-tools</code>, which often works better in these cases.</p>
<dt><code>cw_7501</code></p>
<dd> The driver for Matsushita/Panasonic CW-7501 is auto-selected when <code>wodim</code> finds this old pre MMC drive. <code>wodim</code> supports all write modes for this drive type.</p>
<dt><code>kodak_pcd_600</code></p>
<dd> The driver for Kodak PCD-600 is auto-selected when <code>wodim</code> finds this old pre MMC drive which has been the first high speed (6x) CD writer for a long time. This drive behaves similar to the Philips CDD-521 drive.</p>
<dt><code>philips_cdd521</code></p>
<dd> The driver for Philips CDD-521 is auto-selected when <code>wodim</code> finds a Philips CDD-521 drive (which is the first CD writer ever made) or one of the other drives that are known to behave similar to this drive. All Philips CDD-521 or similar drives (see other drivers in this list) do not support Session At Once recording.</p>
<dt><code>philips_cdd521_old</code></p>
<dd> The driver for Philips old CDD-521 is auto-selected when <code>wodim</code> finds a Philips CDD-521 with very old firmware which has some known limitations.</p>
<dt><code>philips_cdd522</code></p>
<dd> The driver for Philips CDD-522 is auto-selected when <code>wodim</code> finds a Philips CDD-522 which is the successor of the 521 or one of its variants with Kodak label. <code>wodim</code> does not support Session At Once recording with these drives.</p>
<dt><code>philips_dumb</code></p>
<dd> The driver for Philips CDD-521 with pessimistic assumptions is never auto-selected. It may be used by hand with drives that behave similar to the Philips CDD-521.</p>
<dt><code>pioneer_dws114x</code></p>
<dd> The driver for Pioneer DW-S114X is auto-selected when <code>wodim</code> finds one of the old non MMC CD writers from Pioneer.</p>
<dt><code>plasmon_rf4100</code></p>
<dd> The driver for Plasmon RF 4100 is auto-selected when <code>wodim</code> finds this specific variant of the Philips CDD-521.</p>
<dt><code>ricoh_ro1060c</code></p>
<dd> The driver for Ricoh RO-1060C is auto-selected when <code>wodim</code> finds this drive. There is no real support for this drive yet.</p>
<dt><code>ricoh_ro1420c</code></p>
<dd> The driver for Ricoh RO-1420C is auto-selected when <code>wodim</code> finds a drive with this specific variant of the Philips CDD-521 command set.</p>
<dt><code>scsi2_cd</code></p>
<dd> The generic SCSI-2 CD-ROM driver is auto-selected whenever <code>wodim</code> finds a pre MMC drive that does not support writing or a pre MMC writer that is not supported by <code>wodim</code>.</p>
<dt><code>sony_cdu924</code></p>
<dd> The driver for Sony CDU-924 / CDU-948 is auto-selected whenever <code>wodim</code> finds one of the old pre MMC CD writers from Sony.</p>
<dt><code>teac_cdr50</code></p>
<dd> The driver for Teac CD-R50S, Teac CD-R55S, JVC XR-W2010, Pinnacle RCD-5020 is auto-selected whenever one of the drives is found that is known to the non MMC command set used by TEAC and JVC. Note that many drives from JVC will not work because they do not correctly implement the documented command set and JVC has been unwilling to fix or document the bugs. There is no support for the Session At Once write mode yet.</p>
<dt><code>tyuden_ew50</code></p>
<dd> The driver for Taiyo Yuden EW-50 is auto-selected when <code>wodim</code> finds a drive with this specific variant of the Philips CDD-521 command set.</p>
<dt><code>yamaha_cdr100</code></p>
<dd> The driver for Yamaha CDR-100 / CDR-102 is auto-selected when <code>wodim</code> finds one of the old pre MMC CD writers from Yamaha. There is no support for the Session At Once write mode yet.</p>
<dt><code>cdr_simul</code></p>
<dd> The simulation CD-R driver allows to run timing and speed tests with parameters that match the behavior of CD writers.</p>
<dt><code>dvd_simul</code></p>
<dd> The simulation DVD-R driver allows to run timing and speed tests with parameters that match the behavior of DVD writers.</dl>
<p> There are two special driver entries in the list: <code>cdr_simul</code> and <code>dvd_simul</code>. These driver entries are designed to make timing tests at any speed or timing tests for drives that do not support the <code>-dummy</code> option. The simulation drivers implement a drive with a buffer size of 1 MB that can be changed via the <code>CDR_SIMUL_BUFSIZE</code> environment variable. The simulation driver correctly simulates even a buffer underrun condition. If the <code>-dummy </code> option is present, the simulation is not aborted in case of a buffer underrun.</dl>
<dt><code>driveropts=</code><i>option list</i></p>
<dd> Set driver specific options. The options are specified a comma separated list. To get a list of valid options use <code>driveropts=</code><i>help</i> together with the <i>-checkdrive</i> option. If you like to set driver options without running a typical <code>wodim</code> task, you need to use the <code>-setdropts</code> option in addition, otherwise the command line parser in <code>wodim</code> will complain. Currently implemented driver options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>burnfree </code></p>
<dd> Turn the support for Buffer Underrun Free writing on. This only works for drives that support Buffer Underrun Free technology, which is available on most drives manufactured in this millennium. This may be called: <code>Sanyo BURN-Proof</code>, <code>Ricoh Just-Link</code>, <code>Yamaha Lossless-Link</code> or similar. </p>
<p> This option is deprecated and is mentioned here for documentation purposes only. The BURN-Free feature is enabled by default if the drive supports it. However, use of BURN-Free may cause decreased burning quality. Therefore it can be useful to disable it for certain purposes, eg. when creating a master copy for mass CD production.</p>
<dt><code>noburnfree </code></p>
<dd> Turn the support for Buffer Underrun Free writing off.</p>
<dt><code>varirec=</code><i>value</i></p>
<dd> Turn on the <code>Plextor VariRec</code> writing mode. The mandatory parameter <i>value</i> is the laser power offset and currently may be selected from -2, -1, 0, 1, 2. In addition, you need to set the write speed to 4 in order to allow <code>VariRec</code> to work.</p>
<dt><code>gigarec=</code><i>value</i></p>
<dd> Manage the <code>Plextor GigaRec</code> writing mode. The mandatory parameter <i>value</i> is the disk capacity ratio compared to normal recording and currently may be selected from 0.6, 0.7, 0.8, 1.0, 1.2, 1.3, 1.4. If values &lt; 1.0 are used, then the effect is similar to the <code>Yamaha Audio Master Q. R.</code> feature. If values &gt; 1.0 are used, then the disk capacity is increased. </p>
<p> Not all drives support all <code>GigaRec</code> values. When a drive uses the <code>GigaRec</code> feature, the write speed is limited to 8x.</p>
<dt><code>audiomaster</code></p>
<dd> Turn on the <code>Yamaha Audio Master Q. R.</code> feature which usually should result in high quality CDs that have less reading problems in Hi-Fi players. As this is implemented as a variant of the Session at Once write mode, it will only work if you select SAO write mode and there is no need to turn it off. The <code>Audio Master</code> mode will work with a limited speed but may also be used with data CDs. In <code>Audio Master</code> mode, the pits on the CD will be written larger then usual so the capacity of the medium is reduced when turning this feature on. A 74 minute CD will only have a capacity of 63 minutes if <code>Audio Master</code> is active and the capacity of a 80 minute CD will be reduced to 68 minutes.</p>
<dt><code>forcespeed</code></p>
<dd> Normally, modern drives know the highest possible speed for different media and may reduce the speed in order to grant best write quality. This technology may be called: <code>Plextor PowerRec</code>, <code>Ricoh Just-Speed</code>, <code>Yamaha Optimum Write Speed Control</code> or similar. Some drives (e.g. Plextor, Ricoh and Yamaha) allow to force the drive to use the selected speed even if the medium is so bad that the write quality would be poor. This option tells such a drive to force to use the selected speed regardless of the medium quality. </p>
<p> Use this option with extreme care and note that the drive should know better which medium will work at full speed. The default is to turn <code>forcespeed</code> off, regardless of the defaults of the drive.</p>
<dt><code>noforcespeed</code></p>
<dd> Turn off the <code>force speed</code> feature.</p>
<dt><code>speedread</code></p>
<dd> Some ultra high speed drives such as 48x and faster drives from Plextor limit the read speed for unknown media to e.g. 40x in order to avoid damaged disks and drives. Using this option tells the drive to read any media as fast as possible. Be very careful as this may cause the media to break in the drive while reading, resulting in a damaged media and drive!</p>
<dt><code>nospeedread</code></p>
<dd> Turn off unlimited read speed.</p>
<dt><code>singlesession</code></p>
<dd> Turn the drive into a single session only drive. This allows to read defective or non-compliant (illegal) media with extremely non-standard additional (broken/illegal) TOC entries in the TOC from the second or higher session. Some of these disks become usable if only the information from the first session is used. You need to enable Single Session mode before you insert the defective disk!</p>
<dt><code>nosinglesession</code></p>
<dd> Turn off single session mode. The drive will again behave as usual.</p>
<dt><code>hidecdr</code></p>
<dd> Hide the fact that a medium might be a recordable medium. This allows to make CD-Rs look like CD-ROMs and applications believe that the media in the drive is not a CD-R.</p>
<dt><code>nohidecdr</code></p>
<dd> Turn off hiding CD-R media.</p>
<dt><code>tattooinfo</code></p>
<dd> Use this option together with <code>-checkdrive</code> to retrieve the image size information for the <code>Yamaha DiskT@2</code> feature. The images always have a line length of 3744 pixel. Line number 0 (radius 0) is mapped to the center of the disk. If you know the inner and outer radius you will be able to create a pre distorted image that later may appear undistorted on the disk.</p>
<dt><code>tattoofile=</code><i>name</i></p>
<dd> Use this option together with <code>-checkdrive</code> to write an image prepared for the <code>Yamaha DiskT@2</code> feature to the medium. The file must be a file with raw image B&amp;W data (one byte per pixel) in a size as retrieved by a previous call to <code>tattoofile=</code><i>name</i> . If the size of the image equals the maximum possible size (3744 x 320 pixel), <code>wodim</code> will use the first part of the file. This first part then will be written to the leftover space on the CD. </p>
<p> Note that the image must be mirrored to be readable from the pick up side of the CD.</dl>
</dl>
<dt><code>-setdropts</code></p>
<dd> Set the driveropts specified by <code>driveropts=</code><i>option list</i><code>,</code> the <code>speed</code> of the drive and the <code>dummy</code> flag and exit. This allows wodim to set drive specific parameters that are not directly used by <code>wodim</code> like e.g. <code>single session mode</code>, <code>hide cdr</code> and similar. It is needed in case that <code>driveropts=</code><i>option list</i> should be called without planning to run a typical <code>wodim</code> task.</p>
<dt><code>-checkdrive</code></p>
<dd> Checks if a driver for the current drive is present and exit. If the drive is a known drive, <code>wodim</code> uses exit code 0.</p>
<dt><code>-prcap</code></p>
<dd> Print the drive capabilities for SCSI-3/mmc compliant drives as obtained from mode page 0x2A. Values marked with <i>kB</i> use 1000 bytes as kilo-byte, values marked with <i>KB</i> use 1024 bytes as Kilo-byte.</p>
<dt><code>-inq</code></p>
<dd> Do an inquiry for the drive, print the inquiry info and exit.</p>
<dt><code>-scanbus</code></p>
<dd> Scan all SCSI devices on all SCSI busses and print the inquiry strings. This option may be used to find SCSI address of the CD/DVD-Recorder on a system. If some device types are invisible, try using <code>dev=ATA:</code> or similar option to give a hint about the device type you are looking for. The numbers printed out as labels are computed by: <code>bus * 100 + target.</code> On platforms and device systems without persistent SCSI number management the results are not reliable. Use the .B &#8211;devices option instead.</p>
<dt><code>&#8211;devices</code></p>
<dd> Look for useable devices using the system specific functions, eg. probing with usual device nodes in /dev/*, and display the detections using symbolic device names in OS specific syntax.</p>
<dt><code>-reset</code></p>
<dd> Try to reset the SCSI bus where the CD recorder is located. This works not on all operating systems.</p>
<dt><code>-abort</code></p>
<dd> Try to send an <code>abort</code> sequence to the drive. If you use <code>wodim</code> only, this should never be needed; but other software may leave a drive in an unusable condition. Calling <code>wodim -reset</code> may be needed if a previous write has been interrupted and the software did not tell the drive that it will not continue to write.</p>
<dt><code>-overburn</code></p>
<dd> Allow <code>wodim </code> to write more than the official size of a medium. This feature is usually called <i>overburning</i> and depends on the fact that most blank media may hold more space than the official size. As the official size of the lead-out area on the disk is 90 seconds (6750 sectors) and a disk usually works if there are at least 150 sectors of lead out, all media may be overburned by at least 88 seconds (6600 sectors). Most CD recorders only do overburning in <code>SAO</code> or <code>RAW</code> mode. Known exceptions are TEAC CD-R50S, TEAC CD-R55S and the Panasonic CW-7502. Some drives do not allow to overburn as much as you might like and limit the size of a CD to e.g. 76 minutes. This problem may be circumvented by writing the CD in RAW mode because this way the drive has no chance to find the size before starting to burn. There is no guarantee that your drive supports overburning at all. Make a test to check if your drive implements the feature.</p>
<dt><code>-ignsize</code></p>
<dd> Ignore the known size of the medium. This option should be used with extreme care, it exists only for debugging purposes don&#8217;t use it for other reasons. It is not needed to write disks with more than the nominal capacity. This option implies <code>-overburn</code>.</p>
<dt><code>-useinfo</code></p>
<dd> Use <code>*.inf</code> files to overwrite audio options. If this option is used, the pregap size information is read from the <code>*.inf</code> file that is associated with the file that contains the audio data for a track. </p>
<p> If used together with the <code>-audio</code> option, <code>wodim</code> may be used to write audio CDs from a pipe from <code>icedax</code> if you call <code>wodim</code> with the <code>*.inf</code> files as track parameter list instead of using audio files. The audio data is read from <code>stdin</code> in this case. See <code>EXAMPLES</code> section below. <code>wodim</code> first verifies that <code>stdin</code> is not connected to a terminal and runs some heuristic consistency checks on the <code>*.inf</code> files and then sets the track lengths from the information in the <code>*.inf</code> files. </p>
<p> If you like to write from <code>stdin</code>, make sure that wodim is called with a large enough FIFO size, reduce the write speed to a value below the read speed of the source drive and switch the burn-free option for the recording drive on.</p>
<dt><code>defpregap=</code>#</p>
<dd> Set the default pre-gap size for all tracks except track number 1. This option currently only makes sense with the TEAC drive when creating track-at-once disks without the 2 second silence before each track.<br />
 This option may go away in future.</p>
<dt><code>-packet</code></p>
<dd> Set <code>Packet writing mode. </code> This is an experimental interface.</p>
<dt><code>pktsize=</code>#</p>
<dd> Set the packet size to #, forces fixed packet mode. This is an experimental interface.</p>
<dt><code>-noclose</code></p>
<dd> Do not close the current track, useful only when in packet writing mode. This is an experimental interface.</p>
<dt><code>mcn=</code><i>med_cat_nr</i></p>
<dd> Set the <code>Media Catalog Number</code> of the CD to <i>med_cat_nr</i>.</p>
<dt><code>-text</code></p>
<dd> Write CD-Text information based on information taken from a file that contains ascii information for the text strings. <code>wodim</code> supports CD-Text information based on the content of the <code>*.inf</code> files created by <code>icedax </code> and CD-Text information based on the content from a <code>CUE sheet</code> file. If a <code>CUE sheet</code> file contains both (binary CDTEXTFILE and text based SONGWRITER) entries, then the information based on the CDTEXTFILE entry will win. </p>
<p> You need to use the <code>-useinfo</code> option in addition in order to tell <code>wodim</code> to read the <code>*.inf</code> files or <code>cuefile=</code><i>filename</i> in order to tell <code>wodim</code> to read a <code>CUE sheet</code> file in addition. If you like to write your own CD-Text information, edit the <code>*.inf</code> files or the <code>CUE sheet</code> file with a text editor and change the fields that are relevant for CD-Text.</p>
<dt><code>textfile=</code><i>filename</i></p>
<dd> Write CD-Text based on information found in the binary file <i>filename</i>. This file must contain information in a data format defined in the SCSI-3 MMC-2 standard and in the Red Book. The four byte size header that is defined in the SCSI standard is optional and allows to make the recognition of correct data less ambiguous. This is the best option to be used to copy CD-Text data from existing CDs that already carry CD-Text information. To get data in a format suitable for this option use <code>wodim -vv -toc</code> to extract the information from disk. If both, <code>textfile=</code><i>filename</i> and CD-Text information from <code>*.inf</code> or <code>*.cue</code> files are present, <code>textfile=</code><i>filename</i> will overwrite the other information.</p>
<dt><code>cuefile=</code><i>filename</i></p>
<dd> Take all recording related information from a CDRWIN compliant <code>CUE sheet</code> file. No track files are allowed when this option is present and the option <code>-dao</code> is currently needed in addition. </p>
</dl>
<h2>TRACK OPTIONS</h2>
<p> Track options may be mixed with track file names.</p>
<dl>
<dt><code>isrc=</code><i>ISRC_number</i></p>
<dd> Set the <code>International Standard Recording Number</code> for the next track to <i>ISRC_number</i>.</p>
<dt><code>index=</code><i>list</i></p>
<dd> Sets an index list for the next track. In index list is a comma separated list of numbers that are counting from index 1. The first entry in this list must contain a 0, the following numbers must be an ascending list of numbers (counting in 1/75 seconds) that represent the start of the indices. An index list in the form: 0,7500,15000 sets index 1 to the start of the track, index 2 100 seconds from the start of the track and index 3 200 seconds from the start of the track.</p>
<dt><code>-audio</code></p>
<dd> If this flag is present, all subsequent tracks are written in <code>CD-DA </code> (similar to Red Book) audio format. The file with data for this tracks should contain stereo, 16-bit digital audio with 44100 samples/s. The byte order should be the following: MSB left, LSB left, MSB right, LSB right, MSB left and so on. The track should be a multiple of 2352 bytes. It is not possible to put the master image of an audio track on a raw disk because data will be read in multiple of 2352 bytes during the recording process. </p>
<p> If a filename ends in <i>.au</i> or <i>.wav</i> the file is considered to be a structured audio data file. <code>wodim</code> assumes that the file in this case is a Sun audio file or a Microsoft .WAV file and extracts the audio data from the files by skipping over the non-audio header information. In all other cases, wodim will only work correctly if the audio data stream does not have any header. Because many structured audio files do not have an integral number of blocks (1/75th second) in length, it is often necessary to specify the <code>-pad</code> option as well. <code>wodim</code> recognizes that audio data in a .WAV file is stored in Intel (little-endian) byte order, and will automatically byte-swap the data if the CD recorder requires big-endian data. <code>wodim</code> will reject any audio file that does not match the Red Book requirements of 16-bit stereo samples in PCM coding at 44100 samples/second. </p>
<p> Using other structured audio data formats as input to <code>wodim</code> will usually work if the structure of the data is the structure described above (raw pcm data in big-endian byte order). However, if the data format includes a header, you will hear a click at the start of a track.</p>
<dt><i> </i></p>
<dd> If neither <i>-data </i> nor <i>-audio</i> have been specified, <code>wodim</code> defaults to <i>-audio</i> for all filenames that end in <i>.au</i> or <i>.wav</i> and to <i>-data </i> for all other files.</p>
<dt><code>-swab</code></p>
<dd> If this flag is present, audio data is assumed to be in byte-swapped (little-endian) order. Some types of CD-Writers e.g. Yamaha, Sony and the new SCSI-3/mmc drives require audio data to be presented in little-endian order, while other writers require audio data to be presented in the big-endian (network) byte order normally used by the SCSI protocol. <code>wodim</code> knows if a CD-Recorder needs audio data in big- or little-endian order, and corrects the byte order of the data stream to match the needs of the recorder. You only need the <i>-swab </i> flag if your data stream is in Intel (little-endian) byte order. </p>
<p> Note that the verbose output of <code>wodim</code> will show you if swapping is necessary to make the byte order of the input data fit the required byte order of the recorder. <code>wodim</code> will not show you if the <i>-swab </i> flag was actually present for a track.</p>
<dt><code>-data</code></p>
<dd> If this flag is present, all subsequent tracks are written in <code>CD-ROM mode 1</code> (Yellow Book) format. The data size is a multiple of 2048 bytes. The file with track data should contain an <code>ISO-9660</code> or <code>Rock Ridge</code> filesystem image (see <code>genisoimage</code> for more details). If the track data is an <code>ufs</code> filesystem image, fragment size should be set to 2 KB or more to allow CD-drives with 2 KB sector size to be used for reading.</p>
<dt><i> </i></p>
<dd> <i>-data</i> is the default, if no other flag is present and the file does not appear to be of one of the well known audio file types.</p>
<dt><i> </i></p>
<dd> If neither <i>-data </i> nor <i>-audio</i> have been specified, <code>wodim</code> defaults to <i>-audio</i> for all filenames that end in <i>.au</i> or <i>.wav</i> and to <i>-data </i> for all other files.</p>
<dt><code>-mode2</code></p>
<dd> If this flag is present, all subsequent tracks are written in <code>CD-ROM mode 2</code> format. The data size is a multiple of 2336 bytes.</p>
<dt><code>-xa</code></p>
<dd> If this flag is present, all subsequent tracks are written in <code>CD-ROM XA mode 2 form 1</code> format. The data size is a multiple of 2048 bytes. The XA sector sub headers will be created by the drive. With this option, the write mode is the same as with the <code>-multi</code> option.</p>
<dt><code>-xa1</code></p>
<dd> If this flag is present, all subsequent tracks are written in <code>CD-ROM XA mode 2 form 1</code> format. The data size is a multiple of 2056 bytes. The XA sector sub headers are part of the user data and have to be supplied by the application that prepares the data to be written.</p>
<dt><code>-xa2</code></p>
<dd> If this flag is present, all subsequent tracks are written in <code>CD-ROM XA mode 2 form 2</code> format. The data is a multiple of 2324 bytes. The XA sector sub headers will be created by the drive.</p>
<dt><code>-xamix</code></p>
<dd> If this flag is present, all subsequent tracks are written in a way that allows a mix of <code>CD-ROM XA mode 2 form 1/2</code> format. The data size is a multiple of 2332 bytes. The XA sector sub headers are part of the user data and have to be supplied by the application that prepares the data to be written. The CRC and the P/Q parity ECC/EDC information (depending on the sector type) have to be supplied by the application that prepares the data to be written.</p>
<dt><code>-cdi</code></p>
<dd> If this flag is present, the TOC type for the disk is set to <code>CDI</code>. This only makes sense with XA disks.</p>
<dt><code>-isosize</code></p>
<dd> Use the <code>ISO-9660</code> file system size as the size of the next track. This option is needed if you want <code>wodim</code> to directly read the image of a track from a raw disk partition or from a <i>TAO </i> master CD. In the first case the option <code>-isosize</code> is needed to limit the size of the CD to the size of the ISO filesystem. In the second case the option <code>-isosize</code> is needed to prevent <code>wodim</code> from reading the two run out blocks that are appended by each CD-recorder in track at once mode. These two run out blocks cannot be read and would cause a buffer underrun that would cause a defective copy. Do not use this option on files created by <code>genisoimage</code> and in case <code>wodim</code> reads the track data from <i>stdin</i>. In the first case, you would prevent <code>wodim </code> from writing the amount of padding that has been appended by <code>genisoimage</code> and in the latter case, it will not work because <i>stdin</i> is not seekable. </p>
<p> If <code>-isosize</code> is used for a track, <code>wodim</code> will automatically add padding for this track as if the <code>-pad</code> option has been used but the amount of padding may be less than the padding written by <code>genisoimage</code>. Note that if you use <code>-isosize</code> on a track that contains Sparc boot information, the boot information will be lost. </p>
<p> Note also that this option cannot be used to determine the size of a file system if the multi session option is present.</p>
<dt><code>-pad</code></p>
<dd> If the track is a data track, 15 sectors of zeroed data will be added to the end of this and each subsequent data track. In this case, the <code>-pad </code> option is superseded by the <code>padsize=</code> option. It will remain however as a shorthand for <code>padsize=</code><i>15s.</i> If the <i>-pad </i> option refers to an audio track, <code>wodim </code> will pad the audio data to be a multiple of 2352 bytes. The audio data padding is done with binary zeroes which is equal to absolute silence. </p>
<p> <code>-pad </code> remains valid until disabled by <code>-nopad</code>.</p>
<dt><code>padsize=</code>#</p>
<dd> Set the amount of data to be appended as padding to the next track to #. Opposed to the behavior of the <code>-pad</code> option, the value for <i>padsize=</i> is reset to zero for each new track. wodim assumes a sector size of 2048 bytes for the <i>padsize=</i> option, independent from the real sector size and independent from the write mode. The megabytes mentioned in the verbose mode output however are counting the output sector size which is e.g. 2448 bytes when writing in RAW/RAW96 mode. See <code>fs</code>= option for possible arguments. To pad the equivalent of 20 minutes on a CD, you may write <code>padsize=</code>20x60x75s. Use this option if your CD-drive is not able to read the last sectors of a track or if you want to be able to read the CD on a <code>Linux </code> system with the ISO-9660 filesystem read ahead bug. If an empty file is used for track data, this option may be used to create a disk that is entirely made of padding. This may e.g. be used to find out how much overburning is possible with a specific media.</p>
<dt><code>-nopad</code></p>
<dd> Do not pad the following tracks &#8211; the default.</p>
<dt><code>-shorttrack</code></p>
<dd> Allow all subsequent tracks to violate the Red Book track length standard which requires a minimum track length of 4 seconds. This option is only useful when used in SAO or RAW mode. Not all drives support this feature. The drive must accept the resulting CUE sheet or support RAW writing.</p>
<dt><code>-noshorttrack</code></p>
<dd> Re-enforce the Red Book track length standard. Tracks must be at least 4 seconds.</p>
<dt><code>pregap=</code>#</p>
<dd> Set the pre-gap size for the next track. This option currently only makes sense with the TEAC drive when creating track-at-once disks without the 2 second silence before each track.<br />
 This option may go away in future.</p>
<dt><code>-preemp</code></p>
<dd> If this flag is present, all TOC entries for subsequent audio tracks will indicate that the audio data has been sampled with 50/15 microsec pre-emphasis. The data, however is not modified during the process of transferring from file to disk. This option has no effect on data tracks.</p>
<dt><code>-nopreemp</code></p>
<dd> If this flag is present, all TOC entries for subsequent audio tracks will indicate that the audio data has been mastered with linear data &#8211; this is the default.</p>
<dt><code>-copy</code></p>
<dd> If this flag is present, all TOC entries for subsequent audio tracks of the resulting CD will indicate that the audio data has permission to be copied without limit. This option has no effect on data tracks.</p>
<dt><code>-nocopy</code></p>
<dd> If this flag is present, all TOC entries for subsequent audio tracks of the resulting CD will indicate that the audio data has permission to be copied only once for personal use &#8211; this is the default.</p>
<dt><code>-scms</code></p>
<dd> If this flag is present, all TOC entries for subsequent audio tracks of the resulting CD will indicate that the audio data has no permission to be copied anymore.</p>
<dt><code>tsize=</code>#</p>
<dd> If the master image for the next track has been stored on a raw disk, use this option to specify the valid amount of data on this disk. If the image of the next track is stored in a regular file, the size of that file is taken to determine the length of this track. If the track contains an ISO 9660 filesystem image use the <i>-isosize</i> option to determine the length of that filesystem image.<br />
 In Disk at Once mode and with some drives that use the TEAC programming interface, even in Track at Once mode, <code>wodim</code> needs to know the size of each track before starting to write the disk. wodim now checks this and aborts before starting to write. If this happens you will need to run <code>genisoimage -print-size</code> before and use the output (with `s&#8217; appended) as an argument to the <code>tsize</code>= option of <code>wodim</code> (e.g. tsize=250000s).<br />
 See <code>fs</code>= option for possible arguments. </p>
</dl>
<h2>EXAMPLES</h2>
<p> For all examples below, it will be assumed that the CD/DVD-Recorder is connected to the primary SCSI bus of the machine. The SCSI target id is set to 2. </p>
<p> To record a pure CD-ROM at double speed, using data from the file <i>cdimage.raw</i>: </p>
<p>&nbsp;<wbr>wodim -v speed=2 dev=2,0 cdimage.raw </p>
<p> To create an image for a ISO 9660 filesystem with Rock Ridge extensions: </p>
<p>&nbsp;<wbr>genisoimage -R -o cdimage.raw&nbsp;<wbr>/home/joerg/master/tree </p>
<p> To check the resulting file before writing to CD on Solaris: </p>
<p>&nbsp;<wbr>mount -r -F fbk -o type=hsfs&nbsp;<wbr>/dev/fbk0:cdimage.raw&nbsp;<wbr>/mnt </p>
<p> On Linux: </p>
<p>&nbsp;<wbr>mount cdimage.raw -r -t iso9660 -o loop&nbsp;<wbr>/mnt </p>
<p> Go on with: </p>
<p>&nbsp;<wbr>ls -lR&nbsp;<wbr>/mnt </p>
<p>&nbsp;<wbr>umount&nbsp;<wbr>/mnt </p>
<p> If the overall speed of the system is sufficient and the structure of the filesystem is not too complex, wodim will run without creating an image of the ISO 9660 filesystem. Simply run the pipeline: </p>
<p>&nbsp;<wbr>genisoimage -R&nbsp;<wbr>/master/tree | wodim -v fs=6m speed=2 dev=2,0 &#8211; </p>
<p> The recommended minimum FIFO size for running this pipeline is 4 MBytes. As the default FIFO size is 4 MB, the <code>fs=</code> option needs only be present if you want to use a different FIFO size. If your system is loaded, you should run genisoimage in the real time class too. To raise the priority of <code>genisoimage</code> replace the command </p>
<p>&nbsp;<wbr>genisoimage -R&nbsp;<wbr>/master/tree<br />
 by </p>
<p>&nbsp;<wbr>priocntl -e -c RT -p 59 genisoimage -R&nbsp;<wbr>/master/tree </p>
<p> on Solaris and by </p>
<p>&nbsp;<wbr>nice &#8211;18 genisoimage -R&nbsp;<wbr>/master/tree </p>
<p> on systems that don&#8217;t have <code>UNIX International</code> compliant real-time scheduling. </p>
<p> wodim runs at priority 59 on Solaris, you should run genisoimage at no more than priority 58. On other systems, you should run genisoimage at no less than nice &#8211;18. </p>
<p> Creating a CD-ROM without file system image on disk has been tested on a Sparcstation-2 with a Yamaha CDR-400. It did work up to quad speed when the machine was not loaded. A faster machine may be able to handle quad speed also in the loaded case. </p>
<p> To record a pure CD-DA (audio) at single speed, with each track contained in a file named <i>track01.cdaudio</i>, <i>track02.cdaudio</i>, etc: </p>
<p>&nbsp;<wbr>wodim -v speed=1 dev=/dev/cdrw -audio track*.cdaudio </p>
<p> To check if it will be ok to use double speed for the example above. Use the dummy write option: </p>
<p>&nbsp;<wbr>wodim -v -dummy speed=2 dev=/dev/cdrw -audio track*.cdaudio </p>
<p> To record a mixed-mode CD with an ISO 9660 filesystem from <i>cdimage.raw</i> on the first track, the other tracks being audio tracks from the files <i>track01.cdaudio</i>, <i>track02.cdaudio</i>, etc: </p>
<p>&nbsp;<wbr>wodim -v dev=2,0 cdimage.raw -audio track*.cdaudio </p>
<p> To handle drives that need to know the size of a track before starting to write, first run </p>
<p>&nbsp;<wbr>genisoimage -R -q -print-size&nbsp;<wbr>/master/tree </p>
<p> and then run </p>
<p>&nbsp;<wbr>genisoimage -R&nbsp;<wbr>/master/tree | wodim speed=2 dev=2,0 tsize=XXXs &#8211; </p>
<p> where <i>XXX</i> is replaced by the output of the previous run of genisoimage. </p>
<p> To copy an audio CD in the most accurate way, first run </p>
<p>&nbsp;<wbr>icedax dev=/dev/cdrom -vall cddb=0 -B -Owav </p>
<p> and then run </p>
<p>&nbsp;<wbr>wodim dev=/dev/cdrw -v -dao -useinfo -text&nbsp;<wbr>&nbsp;<wbr>*.wav </p>
<p> This will try to copy track indices and to read CD-Text information from disk. If there is no CD-Text information, <code>icedax</code> will try to get the information from freedb.org instead. </p>
<p> To copy an audio CD from a pipe (without intermediate files), first run </p>
<p>&nbsp;<wbr>icedax dev=1,0 -vall cddb=0 -info-only </p>
<p> and then run </p>
<p>&nbsp;<wbr>icedax dev=1,0 -no-infofile -B -Oraw &#8211; |&nbsp;<wbr>\ </p>
<p>&nbsp;<wbr>wodim dev=2,0 -v -dao -audio -useinfo -text&nbsp;<wbr>*.inf </p>
<p> This will get all information (including track size info) from the <code>*.inf</code> files and then read the audio data from stdin. </p>
<p> If you like to write from <code>stdin</code>, make sure that wodim is called with a large enough FIFO size (e.g. <code>fs=128m</code>), reduce the write speed to a value below the read speed of the source drive (e.g. <code>speed=12</code>), and get a CD/DVD drive with BURN-Free feature if it is not available yet. </p>
<p> To set drive options without writing a CD (e.g. to switch a drive to single session mode), run </p>
<p>&nbsp;<wbr>wodim dev=1,0 -setdropts driveropts=singlesession </p>
<p> If you like to do this when no CD is in the drive, call </p>
<p>&nbsp;<wbr>wodim dev=1,0 -force -setdropts driveropts=singlesession </p>
<p> To copy a CD in clone mode, first read the master CD using: </p>
<p>&nbsp;<wbr>readom dev=b,t,l -clone f=somefile </p>
<p> or (in case the CD contains many sectors that are unreadable by intention) by calling: </p>
<p>&nbsp;<wbr>readom dev=1,0 -clone -nocorr f=somefile </p>
<p> will create the files <i>somefile</i> and <i>somefile.toc</i>. Then write the CD using: </p>
<p>&nbsp;<wbr>wodim dev=1,0 -raw96r -clone -v somefile </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>CDR_DEVICE</code></p>
<dd> This may either hold a device identifier that is suitable to the open call of the SCSI transport library or a label in the file /etc/wodim.conf.</p>
<dt><code>CDR_SPEED</code></p>
<dd> Sets the default speed value for writing (see also <code>speed=</code> option).</p>
<dt><code>CDR_FIFOSIZE</code></p>
<dd> Sets the default size of the FIFO (see also <code>fs=</code># option).</p>
<dt><code>CDR_FORCERAWSPEED</code></p>
<dd> If this environment variable is set, <code>wodim</code> will allow you to write at the full RAW encoding speed a single CPU supports. This will create high potential of buffer underruns. Use with care.</p>
<dt><code>CDR_FORCESPEED</code></p>
<dd> If this environment variable is set, <code>wodim</code> will allow you to write at the full DMA speed the system supports. There is no DMA reserve for reading the data that is to be written from disk. This will create high potential of buffer underruns. Use with care.</p>
<dt><code>RSH</code></p>
<dd> If the <code>RSH</code> environment is present, the remote connection will not be created via <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) but by calling the program pointed to by <code>RSH</code>. Use e.g. <code>RSH=</code>/usr/bin/ssh to create a secure shell connection. </p>
<p> Note that this forces <code>wodim</code> to create a pipe to the <code><a href="/docs/linux/man/1-rsh/">rsh</a>(1)</code> program and disallows <code>wodim</code> to directly access the network socket to the remote server. This makes it impossible to set up performance parameters and slows down the connection compared to a <code>root</code> initiated <code><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</code> connection.</p>
<dt><code>RSCSI</code></p>
<dd> If the <code>RSCSI</code> environment is present, the remote SCSI server will not be the program <code>/opt/schily/sbin/rscsi</code> but the program pointed to by <code>RSCSI</code>. Note that the remote SCSI server program name will be ignored if you log in using an account that has been created with a remote SCSI server program as login shell. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/wodim.conf</p>
<dd> Default values can be set for the following options in /etc/wodim.conf. For example: <font SIZE="-1">CDR_FIFOSIZE=8m</font> or <font SIZE="-1">CDR_SPEED=2</font></p>
<dl>
<dt>
<dd>
<dl>
<dt>CDR_DEVICE</p>
<dd> This may either hold a device identifier that is suitable to the open call of the SCSI transport library or a label in the file /etc/wodim.conf that allows to identify a specific drive on the system.</p>
<dt>CDR_SPEED</p>
<dd> Sets the default speed value for writing (see also <code>speed=</code> option).</p>
<dt>CDR_FIFOSIZE</p>
<dd> Sets the default size of the FIFO (see also <code>fs=</code># option).</p>
<dt>CDR_MAXFIFOSIZE</p>
<dd> Sets the maximum size of the FIFO (see also <code>fs=</code># option).</p>
<dt>Any other keyword (label) is an identifier (symbolic name) for a specific drive</p>
<dd> on the system. Such an identifier may not contain the characters &#8216;,&#8217;, &#8216;/&#8217;, &#8216;@&#8217; or &#8216;:&#8217;. </p>
<p> Each line that follows a label contains a whitespace separated list of items. Currently, four items are recognized: the drive&#8217;s target specification, the default speed that should be used for this drive, the default FIFO size that should be used for this drive and drive specific options. The values for <i>speed</i> and <i>fifosize</i> may be set to -1 to tell wodim to use the global defaults. <i>target</i> can be -1 to use the auto-guessing of the drive (see above). </p>
<p> The value for driveropts may be omitted or set to &quot;&quot; if no driveropts are used. A typical line may look this way: </p>
<p> plex760= 0,5,0<tt>&nbsp;<wbr></tt>12<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>50m<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>varirec=1</p>
<p> pioneer= /dev/hdd<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-1</p>
<p> This tells <code>wodim</code> that a drive named <i>plex760</i> is at scsibus 0, target 5, lun 0 and should be used with speed 12 and a FIFO size of 50 MB. It also uses some device specific parameter. A second drive may is accessible via the device file /dev/hdd and uses the default speed and the default FIFO size.</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-icedax/">icedax</a></code>(1), <code><a href="/docs/linux/man/1-readom/">readom</a></code>(1), <code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). </p>
<h2>NOTES</h2>
<p> On Solaris you need to stop the volume management if you like to use the USCSI fallback SCSI transport code. Even things like <code>wodim -scanbus</code> will not work if the volume management is running. </p>
<p> Disks made in <code>Track At Once </code> mode are not suitable as a master for direct mass production by CD manufacturers. You will need the <code>disk at once</code> option to record such disks. Nevertheless the disks made in <code>Track At Once </code> will normally be read in all CD players. Some old audio CD players however may produce a two second click between two audio tracks. </p>
<p> The minimal size of a track is 4 seconds or 300 sectors. If you write smaller tracks, the CD-Recorder will add dummy blocks. This is not an error, even though the SCSI-error message looks this way. </p>
<p> The Yamaha CDR-400 and all new SCSI-3/mmc conforming drives are supported in single and multi-session. </p>
<p> You should run several tests in all supported speeds of your drive with the <code>-dummy</code> option turned on if you are using <code>wodim</code> on an unknown system. Writing a CD is a real-time process. <code>NFS, CIFS</code> and other network file systems won&#8217;t always deliver constantly the needed data rates. If you want to use <code>wodim </code> with CD-images that are located on a <code>NFS</code> mounted filesystem, be sure that the FIFO size is big enough. If you want to make sure that buffer underruns are not caused by your source disk, you may use the command </p>
<p> <code> wodim -dummy dev=2,0 padsize=600m /dev/null</code> </p>
<p> to create a disk that is entirely made of dummy data. </p>
<p> There are also cases where you either need to be root or install <code>wodim </code> executable with suid-root permissions. First, if you are using a device manufactured before 1999 which requires a non-MMC driver, you should run <code>wodim</code> in dummy mode before writing data. If you find a problem doing this, please report it to the <code>cdrkit</code> maintainers (see below). </p>
<p> Second, certain functionality may be unusable because of Linux&#8217;s SCSI command filtering. When using <code>wodim</code> for anything except of pure data writing, you should also test the process in dummy mode and report trouble to the contact address below. </p>
<p> If you still want to run <code>wodim</code> with root permissions, you can set the permissions of the executable to suid-root. See the additional notes of your system/program distribution or README.suidroot which is part of the cdrkit source. </p>
<p> You should not connect old drives that do not support disconnect/reconnect to either the SCSI bus that is connected to the CD-Recorder or the source disk. </p>
<p> A Compact Disc can have no more than 99 tracks. </p>
<p> When creating a disc with both audio and data tracks, the data should be on track 1 otherwise you should create a CDplus disk which is a multi session disk with the first session containing the audio tracks and the following session containing the data track. </p>
<p> Many operating systems are not able to read more than a single data track, or need special software to do so. </p>
<p> If you have more information or SCSI command manuals for currently unsupported CD/DVD/BR/HD-DVD-Recorders, please contact the <code>cdrkit</code> maintainers (see below). </p>
<p> Many CD recorders have bugs and often require a firmware update to work correctly. If you experience problems which cannot be solved or explained by the notes above, please look for instructions on the homepage of the particular manufacturer. </p>
<p> Some bugs will force you to power cycle the device or to reboot the machine. </p>
<p> The FIFO percent output is computed just after a block of data has been written to the CD/DVD-Recorder. For this reason, there will never be 100% FIFO fill ratio while the FIFO is in streaming mode. </p>
<h2>DIAGNOSTICS</h2>
<p> You have 4 seconds to abort <code>wodim</code> start after you see the message: </p>
<p> Starting to write CD at speed %d in %s mode for %s session. In most shells you can do that by pressing Ctrl-C. </p>
<p> A typical error message for a SCSI command looks like: </p>
<dl>
<dt>
<dd>
<pre>
wodim: I/O error. test unit ready: scsi sendcmd: no error
CDB:  00 20 00 00 00 00
status: 0x2 (CHECK CONDITION)
Sense Bytes: 70 00 05 00 00 00 00 0A 00 00 00 00 25 00 00 00 00 00
Sense Key: 0x5 Illegal Request, Segment 0
Sense Code: 0x25 Qual 0x00 (logical unit not supported) Fru 0x0
Sense flags: Blk 0 (not valid)
cmd finished after 0.002s timeout 40s
</pre>
</dl>
<p> The first line gives information about the transport of the command. The text after the first colon gives the error text for the system call from the view of the kernel. It usually is: <code>I/O error</code> unless other problems happen. The next words contain a short description for the SCSI command that fails. The rest of the line tells you if there were any problems for the transport of the command over the SCSI bus. <code>fatal error</code> means that it was not possible to transport the command (i.e. no device present at the requested SCSI address). </p>
<p> The second line prints the SCSI command descriptor block for the failed command. </p>
<p> The third line gives information on the SCSI status code returned by the command, if the transport of the command succeeds. This is error information from the SCSI device. </p>
<p> The fourth line is a hex dump of the auto request sense information for the command. </p>
<p> The fifth line is the error text for the sense key if available, followed by the segment number that is only valid if the command was a <i>copy</i> command. If the error message is not directly related to the current command, the text <i>deferred error</i> is appended. </p>
<p> The sixth line is the error text for the sense code and the sense qualifier if available. If the type of the device is known, the sense data is decoded from tables in <i>scsierrs.c</i> . The text is followed by the error value for a field replaceable unit. </p>
<p> The seventh line prints the block number that is related to the failed command and text for several error flags. The block number may not be valid. </p>
<p> The eight line reports the timeout set up for this command and the time that the command really needed to complete. </p>
<p> The following message is not an error: </p>
<dl>
<dt>
<dd>
<pre>
Track 01: Total bytes read/written: 2048/2048 (1 sectors).
wodim: I/O error. flush cache: scsi sendcmd: no error
CDB:  35 00 00 00 00 00 00 00 00 00
status: 0x2 (CHECK CONDITION)
Sense Bytes: F0 00 05 80 00 00 27 0A 00 00 00 00 B5 00 00 00 00 00
Sense Key: 0x5 Illegal Request, Segment 0
Sense Code: 0xB5 Qual 0x00 (dummy data blocks added) Fru 0x0
Sense flags: Blk -2147483609 (valid)
cmd finished after 0.002s timeout 40s
</pre>
</dl>
<p> It simply notifies, that a track that is smaller than the minimum size has been expanded to 300 sectors.</p>
<h2>BUGS</h2>
<p> <code>netscsid</code> does not work properly and is generally unmaintained. It is probably not compatible with rscsi from <code>cdrtools</code> either. Good bugfixes are welcome, talk to Cdrkit maintainers. </p>
<p> <code>cuefile support is very limited, only one file is allowed. For volunteers,</code> see TODO file in the source. </p>
<p> <code>Specifying an audio file multiple times causes corruption of the second</code> track (effectively no data plus minimum padding). </p>
<p> Some of the bugs may be fixed in Joerg Schilling&#8217;s cdrtools. See there for details, URL attached below. </p>
<h2>CREDITS</h2>
<dl>
<dt>Joerg Schilling (schilling [at] fokus.fhg.de)</p>
<dd>
 For writing cdrecord and libscg which represent the most parts of wodim&#8217;s code.</dl>
<dl>
<dt>Bill Swartz<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(Bill_Swartz [at] twolf.com)</p>
<dd>
 For helping me with the TEAC driver support</p>
<dt>Aaron Newsome<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(aaron.d.newsome [at] wdc.com)</p>
<dd>
 For letting me develop Sony support on his drive</p>
<dt>Eric Youngdale<tt>&nbsp;<wbr>&nbsp;<wbr></tt>(eric [at] andante.jic.com)</p>
<dd>
 For supplying mkisofs</p>
<dt>Gadi Oxman<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(gadio [at] netvision.net.il)</p>
<dd>
 For tips on the ATAPI standard</p>
<dt>Finn Arne Gangstad<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(finnag [at] guardian.no)</p>
<dd>
 For the first FIFO implementation.</p>
<dt>Dave Platt<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(dplatt [at] feghoot.ml.org)</p>
<dd>
 For creating the experimental packet writing support,<br />
 the first implementation of CD-RW blanking support, the first .wav file decoder and many nice discussions on cdrecord.</p>
<dt>Chris P. Ross (cross [at] eng.us.uu.net)</p>
<dd>
 For the first implementation of a BSDI SCSI transport.</p>
<dt>Grant R. Guenther (grant [at] torque.net)</p>
<dd>
 For creating the first parallel port transport implementation for Linux.</p>
<dt>Kenneth D. Merry (ken [at] kdm.org)</p>
<dd>
 for providing the CAM port for FreeBSD together with Michael Smith (msmith [at] freebsd.org)</p>
<dt>Heiko Eiszfeldt (heiko [at] hexco.de)</p>
<dd> for making libedc_ecc available (needed to write RAW data sectors). </p>
</dl>
<h2>MAILING LISTS</h2>
<p> If you want to actively take part on the development of wodim, you may join the developer mailing list via this URL: </p>
<p> <code><a rel="nofollow" href="https://alioth.debian.org/mail/?group_id=31006">https://alioth.debian.org/mail/?group_id=31006</a></code> </p>
<p> The mail address of the list is: <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<h2>AUTHORS</h2>
<p> <code>wodim</code> is currently maintained as part of the cdrkit project by its developers. Most of the code and this manual page was originally written by: </p>
<pre>
Joerg Schilling
Seestr. 110
D-13353 Berlin
Germany
</pre>
<p> This application is derived from &quot;cdrecord&quot; as included in the cdrtools package [1] created by Joerg Schilling, who deserves most of the credit for its success. However, he is not involved into the development of this spinoff and therefore he shall not be held responsible for any problems caused by it. Do not refer to this application as &quot;cdrecord&quot;, do not try to get support for wodim by contacting the original authors. </p>
<p> Additional information can be found on:<br />
 <a rel="nofollow" href="https://alioth.debian.org/projects/debburn/">https://alioth.debian.org/projects/debburn/</a> </p>
<p> If you have support questions, send them to </p>
<p> <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<p> If you have definitely found a bug, send a mail to this list or to </p>
<p> <code>submit [at] bugs.debian.org</code> </p>
<p> writing at least a short description into the Subject and &quot;Package: cdrkit&quot; in the first line of the mail body.</p>
<h2>SOURCES</h2>
<p> [1] Cdrtools 2.01.01a08 from May 2006, <a rel="nofollow" href="http://cdrecord.berlios.de">http://cdrecord.berlios.de</a> </p>
<h2>Index</h2>
