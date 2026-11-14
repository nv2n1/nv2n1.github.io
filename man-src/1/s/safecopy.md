---
title: "safecopy(1)"
name: "safecopy"
section: "1"
letter: "s"
url: "/docs/linux/man/1-safecopy/"
description: "safecopy – rescue data from a source that causes IO errors"
---

<h2 class="name">NAME</h2>
<p> <code>safecopy</code> &#8211; rescue data from a source that causes IO errors</p>
<h2>SYNOPSIS</h2>
<p> <code>safecopy</code> [<i>OPTION</i>]&#8230; <i>SOURCE DEST</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>safecopy</code> tries to get as much data from SOURCE as possible, even resorting to device specific low level operations if applicable. </p>
<p> This is achieved by identifying problematic or damaged areas, skipping over them and continuing reading afterwards. The corresponding area in the destination file is either skipped (on initial creation that means padded with zeros) or deliberately filled with a recognizable pattern to later find affected files on a corrupted device. </p>
<p> Safecopy uses an incremental algorithm to identify the exact beginning and end of bad areas, allowing the user to trade minimum accesses to bad areas for thorough data resurrection. </p>
<p> Multiple passes over the same file are possible, to first retrieve as much data from a device as possible with minimum harm, and then trying to retrieve some of the remaining data with increasingly aggressive read attempts. </p>
<p> For this to work, the source device or file has to be seekable. For unseekable devices (like tapes) you can try to use an external script to execute a controlled skip over the damaged part for you. </p>
<p> (For example by using &quot;mt seek&quot; and &quot;mt tell&quot; on an SCSI tape device) See the &quot;-S &lt;seekscript&gt;&quot; parameter for details. </p>
<p> Performance and success of this tool depend extremely on the device driver, firmware and underlying hardware. </p>
<p> Currently safecopy supports RAW access to CDROM drives to read data directly of a CD, bypassing some driver dependant error correction. This can speed up data retrieval from CDs and reduce system load during recovery, as well as increase the success rate. Safecopy uses the disc status syscall to determine sector size and addressing of CDs. This fails on mixed-mode or multi-session CDs, since the sector layout can change within the disk, but would still work on the the big majority of disks. Other disks can still be recovered using normal high level data access. Safecopy auto-detects the disk type involved during scan for disk and block size. </p>
<p> Some CD/DVD drives are known to cause the ATAPI bus to crash on errors, causing the device driver to freeze for times up to and beyond a minute per error. Try to avoid using such drives for media recovery. Using safecopys low level access features might help under some circumstances. </p>
<p> Some drives can read bad media better than others. Be sure to attempt data recovery of CDs and DVDs on several different drives and computers. You can use safecopys incremental recovery feature to read previously unreadable sectors only. </p>
<h2>RELIABILITY</h2>
<p> Data recovery from damaged media is a delicate task, in the worst case its success or failure can safe or ruin whole companies and seal affected peoples personal fate. It is paramount that any tools written for that purpose are reliable and trustworthy. </p>
<p> A user needs to know what exactly the software is doing to his hardware and data. The outcome of any operation needs to be both understandable and predictable. </p>
<p> An &quot;intelligent data resurrection wizard&quot; with unknown complex internal behaviour may be a nifty tool, but does not meet the above requirements of predictable outcome, nor will the user know in advance what is done to his data. </p>
<p> The operation sequence of safecopy has been kept relatively simple to assure this predictability. Unfortunately feature additions have risen the complexity and lead to undefined outcome in the past when include and exclude lists had been mixed, especially when mixing different block sizes. In the worst case this could have lead to overwritten data in the destination file on a later incremental run with the mark (-M) option. </p>
<p> From version 1.3 on, safecopy ships with a test suite that can be used to verify safecopys behaviour in a set of test cases, simulating the combination of bad blocks in input with different include and exclude lists, both with and without marking. Releases are only made if safecopy passes those test cases according to the specification. </p>
<p> This textual specification of behaviour of safecopy can be found in the file specification.txt shipped with safecopy. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;stage1</code></p>
<dd> Preset to rescue most of the data fast, using no retries and avoiding bad areas.</p>
<dt>
<dd> <code>Presets</code>: -f 10% -r 10% -R 1 -Z 0 -L 2 -M BaDbLoCk -o stage1.badblocks</p>
<dt><code>&#8211;stage2</code></p>
<dd> Preset to rescue more data, using no retries but searching for exact ends of bad areas.</p>
<dt>
<dd> <code>Presets</code>: -f 128* -r 1* -R 1 -Z 0 -L 2 -I stage1.badblocks -o stage2.badblocks</p>
<dt><code>&#8211;stage3</code></p>
<dd> Preset to rescue everything that can be rescued using maximum retries, head realignment tricks and low level access.</p>
<dt>
<dd> <code>Presets</code>: -f 1* -r 1* -R 4 -Z 1 -L 2 -I stage2.badblocks -o stage3.badblocks</dl>
<p> All stage presets can be overridden by individual options.</p>
<dl>
<dt><code>-b</code> &lt;<i>size</i>&gt;</p>
<dd> Blocksize for default read operations. Set this to the physical sectorsize of your media.</p>
<dt>
<dd> <code>Default</code>: 1*<br />
 Hardware block size if reported by OS, otherwise 4096</p>
<dt><code>-f</code> &lt;<i>size</i>&gt;</p>
<dd> Blocksize in bytes when skipping over badblocks. Higher settings put less strain on your hardware, but you might miss good areas in between two bad ones.</p>
<dt>
<dd> <code>Default</code>: 16*</p>
<dt><code>-r</code> &lt;<i>size</i>&gt;</p>
<dd> Resolution in bytes when searching for the exact beginning or end of a bad area. If you read data directly from a device there is no need to set this lower than the hardware blocksize. On mounted filesystems however, read blocks and physical blocks could be misaligned. Smaller values lead to very thorough attempts to read data at the edge of damaged areas, but increase the strain on the damaged media.</p>
<dt>
<dd> <code>Default</code>: 1*</p>
<dt><code>-R</code> &lt;<i>number</i>&gt;</p>
<dd> At least that many read attempts are made on the first bad block of a damaged area with minimum resolution. More retries can sometimes recover a weak sector, but at the cost of additional strain.</p>
<dt>
<dd> <code>Default</code>: 3</p>
<dt><code>-Z</code> &lt;<i>number</i>&gt;</p>
<dd> On each error, force seek the read head from start to end of the source device as often as specified. That takes time, creates additional strain and might not be supported by all devices or drivers.</p>
<dt>
<dd> <code>Default</code>: 1</p>
<dt><code>-L</code> &lt;<i>mode</i>&gt;</p>
<dd> Use low level device calls as specified:</p>
<dt>
<dd> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Do not use low level device calls</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Attempt low level device calls<br />
 for error recovery only<br />
 2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Always use low level device calls<br />
 if available</p>
<dt>
<dd> Supported low level features in this version are:</p>
<dt>
<dd> SYSTEM DEVICE TYPE FEATURE<br />
 Linux cdrom/dvd bus/device reset<br />
 Linux cdrom read sector in raw mode<br />
 Linux floppy controller reset, twaddle</p>
<dt>
<dd> <code>Default</code>: 1</p>
<dt><code>&#8211;sync</code></p>
<dd> Use synchronized read calls (disable driver buffering). Safecopy will use O_DIRECT if supported by the OS and O_SYNC otherwise.</p>
<dt>
<dd> <code>Default</code>: Asynchronous read buffering by the OS is allowed</p>
<dt><code>&#8211;forceopen</code></p>
<dd> Keep trying to reopen the source after a read errer useful for USB drives that go away temporarily.</p>
<dt>
<dd> <code>Warning</code>: This can cause safecopy to hang until aborted manually!</p>
<dt>
<dd> <code>Default</code>: Abort on fopen() error</p>
<dt><code>-s</code> &lt;<i>blocks</i>&gt;</p>
<dd> Start position where to start reading. Will correspond to position 0 in the destination file.</p>
<dt>
<dd> <code>Default</code>: block 0</p>
<dt><code>-l</code> &lt;<i>blocks</i>&gt;</p>
<dd> Maximum length of data to be read.</p>
<dt>
<dd> <code>Default</code>: Entire size of input file</p>
<dt><code>-I</code> &lt;<i>badblockfile</i>&gt;</p>
<dd> Incremental mode. Assume the target file already exists and has holes specified in the badblockfile. It will be attempted to retrieve more data from the listed blocks or from beyond the file size of the target file only.</p>
<dt>
<dd> <code>Warning</code>: Without this option, the destination file will be emptied prior to writing. Use -I /dev/null if you want to continue a previous run of safecopy without a badblock list.</p>
<dt>
<dd> <code>Implies</code>: -c 0 if -c is not specified</p>
<dt>
<dd> <code>Default</code>: none ( /dev/null if -c is given )</p>
<dt><code>-i</code> &lt;<i>bytes</i>&gt;</p>
<dd> Blocksize to interpret the badblockfile given with -I.</p>
<dt>
<dd> <code>Default</code>: Blocksize as specified by -b</p>
<dt><code>-c</code> &lt;<i>blocks</i>&gt;</p>
<dd> Continue copying at this position. This allows continuing if the output is a block device with a fixed size as opposed to a growable file, where safecopy cannot determine how far it already got. The blocksize used is the same as for the -I option.<br />
 -c 0 will continue at the current destination size.</p>
<dt>
<dd> <code>Implies</code>: -I /dev/null if -I is not specified</p>
<dt>
<dd> <code>Default</code>: none ( 0 if -I is given )</p>
<dt><code>-X</code> &lt;<i>badblockfile</i>&gt;</p>
<dd> Exclusion mode. If used together with -I, excluded blocks override included blocks. Safecopy will not read or write any data from areas covered by exclude blocks.</p>
<dt>
<dd> <code>Default</code>: none</p>
<dt><code>-x</code> &lt;<i>bytes</i>&gt;</p>
<dd> Blocksize to interpret the badblockfile given with -X.</p>
<dt>
<dd> <code>Default</code>: Blocksize as specified by -b</p>
<dt><code>-o</code> &lt;<i>badblockfile</i>&gt;</p>
<dd> Write a badblocks/e2fsck compatible bad block file.</p>
<dt>
<dd> <code>Default</code>: none</p>
<dt><code>-S</code> &lt;<i>seekscript</i>&gt;</p>
<dd> Use external script for seeking in input file. (Might be useful for tape devices and similar). Seekscript must be an executable that takes the number of blocks to be skipped as argv1 (1-64) the blocksize in bytes as argv2 and the current position (in bytes) as argv3. Return value needs to be the number of blocks successfully skipped, or 0 to indicate seek failure. The external seekscript will only be used if lseek() fails and we need to skip over data.</p>
<dt>
<dd> <code>Default</code>: none</p>
<dt><code>-M</code> &lt;<i>string</i>&gt;</p>
<dd> Mark unrecovered data with this string instead of skipping it. This helps in later finding corrupted files on rescued file system images. The default is to zero unreadable data on creation of output files, and leaving the data as it is on any later run.</p>
<dt>
<dd> <code>Warning</code>: When used in combination with incremental mode (-I) this may overwrite data in any block that occurs in the -I file. Blocks not in the -I file, or covered by the file specified with -X are save from being overwritten.</p>
<dt>
<dd> <code>Default</code>: none</p>
<dt><code>&#8211;debug</code> &lt;<i>level</i>&gt;</p>
<dd> Enable debug output. Level is a bit field, add values together for more information:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>program flow: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>IO control: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>badblock marking:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>4</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>seeking: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>8</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>incremental mode:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>16</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>exclude mode: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>32</p>
<p> or for all debug output:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>255</p>
<dt>
<dd> <code>Default</code>: 0</p>
<dt><code>-T</code> &lt;<i>timingfile</i>&gt;</p>
<dd> Write sector read timing information into this file for later analysis.</p>
<dt>
<dd> <code>Default</code>: none</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the program help text. </p>
</dl>
<h2>PARAMETERS</h2>
<p> valid parameters for <code>-f</code> <code>-r</code> <code>-b</code> <code>&lt;size&gt;</code> options are:</p>
<dl>
<dt><code>&lt;integer&gt;</code></p>
<dd> Amount in bytes &#8211; i.e. 1024</p>
<dt><code>&lt;percentage&gt;%</code></p>
<dd> Percentage of whole file/device size &#8211; e.g. 10%</p>
<dt><code>&lt;number&gt;*</code></p>
<dd> <code>-b</code> only, number times blocksize reported by OS</p>
<dt><code>&lt;number&gt;*</code></p>
<dd> <code>-f</code> and <code>-r</code> only, number times the value of <code>-b</code> </p>
</dl>
<h2>OUTPUT</h2>
<p> description of output symbols:</p>
<dl>
<dt><code>.</code></p>
<dd> Between 1 and 1024 blocks successfully read.</p>
<dt><code>_</code></p>
<dd> Read of block was incomplete. (possibly end of file) The blocksize is now reduced to read the rest.</p>
<dt><code>|/|</code></p>
<dd> Seek failed, source can only be read sequentially.</p>
<dt><code>&gt;</code></p>
<dd> Read failed, reducing blocksize to read partial data.</p>
<dt><code>!</code></p>
<dd> A low level error on read attempt of smallest allowed size leads to a retry attempt.</p>
<dt><code>[xx](+yy){</code></p>
<dd> Current block and number of bytes continuously read successfully up to this point.</p>
<dt><code>X</code></p>
<dd> Read failed on a block with minimum blocksize and is skipped. Unrecoverable error, destination file is padded with zeros. Data is now skipped until end of the unreadable area is reached.</p>
<dt><code>&lt;</code></p>
<dd> Successful read after the end of a bad area causes backtracking with smaller blocksizes to search for the first readable data.</p>
<dt><code>}[xx](+yy)</code></p>
<dd> current block and number of bytes of recent continuous unreadable data. </p>
</dl>
<h2>HOWTO</h2>
<p> How do I&#8230;</p>
<dl>
<dt>&#8211; resurrect a file from a mounted but damaged media, that copy will fail on:</p>
<dd> <code>safecopy</code> /path/to/problemfile ~/saved-file</p>
<dt>&#8211; create an filesystem image of a damaged disk/cdrom:</p>
<dd> <code>safecopy</code> /dev/device ~/diskimage</p>
<dt>&#8211; resurrect data as thoroughly as possible?</p>
<dd>
<dt>
<dd> <code>safecopy</code> source dest -f 1* -R 8 -Z 2<br />
 (assuming logical misalignment of blocks to sectors)</p>
<dt>
<dd> <code>safecopy</code> source dest -f 1* -r 1 -R 8 -Z 2</p>
<dt>&#8211; resurrect data as fast as possible, or</p>
<dd>
<dt>&#8211; resurrect data with low risk of damaging the media further:</p>
<dd> (you can use even higher values for -f and -r)</p>
<dt>
<dd> <code>safecopy</code> source dest -f 10% -R 0 -Z 0</p>
<dt>&#8211; resurrect some data fast, then read more data thoroughly later:</p>
<dd>
<dt>
<dd> <code>safecopy</code> source dest -f 10% -R 0 -Z 0 -o badblockfile<br />
 <code>safecopy</code> source dest -f 1* -R 8 -Z 2 -I badblockfile</p>
<dt>
<dd> <i>Alternate approach using the new preset features:</i></p>
<dt>
<dd> <code>safecopy</code> source dest &#8211;stage1</p>
<dt>
<dd> <code>safecopy</code> source dest &#8211;stage2</p>
<dt>
<dd> <code>safecopy</code> source dest &#8211;stage3</p>
<dt>&#8211; utilize some friends CD-ROM drives to complete the data from my damaged CD:</p>
<dd> <code>safecopy</code> /dev/mydrive imagefile &lt;someoptions&gt; -b &lt;myblocksize&gt; -o myblockfile<br />
 <code>safecopy</code> /dev/otherdrive imagefile &lt;someoptions&gt; -b &lt;otherblocksize&gt; -I myblockfile -i &lt;myblocksize&gt; -o otherblockfile<br />
 <code>safecopy</code> /dev/anotherdrive imagefile &lt;someoptions&gt; -b &lt;anotherblocksize&gt; -I otherblockfile -i &lt;otherblocksize&gt;</p>
<dt>&#8211; interrupt and later resume a data rescue operation:</p>
<dd> <code>safecopy</code> source dest<br />
 <code>&lt;CTRL+C&gt;</code> (safecopy aborts)<br />
 <code>safecopy</code> source dest -I /dev/null</p>
<dt>&#8211; interrupt and later resume a data rescue operation with correct badblocks output:</p>
<dd> <code>safecopy</code> source dest &lt;options&gt; -o badblockfile<br />
 <code>&lt;CTRL+C&gt;</code> (safecopy aborts)<br />
 <code>mv</code> badblockfile savedbadblockfile<br />
 <code>safecopy</code> source dest -I /dev/null -o badblockfile<br />
 <code>cat</code> badblockfile &gt;&gt;savedbadblockfile</p>
<dt>&#8211; interrupt and resume in incremental mode:</p>
<dd>
 (this needs a bit of bash scripting to get the correct badblock lists)<br />
 <code>safecopy</code> source dest &lt;options&gt; -o badblockfile1<br />
 <code>safecopy</code> source dest &lt;options&gt; -I badblockfile1 -o badblockfile2<br />
 <code>&lt;CTRL+C&gt;</code> (safecopy aborts)<br />
 latest=$( tail -n 1 badblockfile2 )<br />
 if [ -z $latest ]; then latest=-1; fi;<br />
 cat badblockfile1 | while read block; do<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[ $block -gt $latest ] &amp;&amp; echo $block &gt;&gt;badblockfile2;</p>
<p> done;<br />
 <code>safecopy</code> source dest &lt;options&gt; -I badblockfile2 -o badblockfile3</p>
<dt>&#8211; find the corrupted files on a partially successful rescued file system:</p>
<dd> <code>safecopy</code> /dev/filesystem image -M CoRrUpTeD<br />
 <code>fsck</code> image<br />
 <code>mount</code> -o loop image /mnt/mountpoint<br />
 <code>grep</code> -R /mnt/mountpoint &quot;CoRrUpTeD&quot;<br />
 (hint: this might not find all affected files if the unreadable parts are smaller in size than your marker string)</p>
<dt>&#8211; exclude the previously known badblocks list of a filesystem from filesystem image creation:</p>
<dd> <code>dumpe2fs</code> -b /dev/filesystem &gt;badblocklist<br />
 <code>safecopy</code> /dev/filesystem image -X badblocklist -x &lt;blocksize of your fs&gt;</p>
<dt>&#8211; create an image of a device that starts at X and is Y in size:</p>
<dd> <code>safecopy</code> /dev/filesystem -b &lt;bsize&gt; -s &lt;X/bsize&gt; -l &lt;Y/bsize&gt;</p>
<dt>&#8211; combine two partial images of rescued data without access to the actual (damaged) source data:</p>
<dd> (This is a bit tricky. You need to get badblocks lists for both files somehow to make safecopy know where the missing data is. If you used the -M (mark) feature you might be able to automatically compute these, however this feature is not provided by safecopy. Lets assume you have two badblocks files.</p>
<dt>
<dd> you have:<br />
 image1.dat<br />
 image1.badblocks (blocksize1)<br />
 image2.dat<br />
 image2.badblocks (blocksize2)</p>
<dt>
<dd> The file size of image1 needs to be greater or equal to that of image2. (If not, swap them) )</p>
<dt>
<dd> <code>cp</code> image2.dat combined.dat<br />
 <code>safecopy</code> image1.dat combined.dat -I image2.badblocks -i blocksize2 -X image1.badblocks -x blocksize1<br />
 (This gets you the combined data, but no output badblocklist. The resulting badblocks list would be the badblocks that are<br />
 a: in both badblocks lists, or<br />
 b: in image1.badblocks and beyond the file size of image2 It should be reasonably easy to solve this logic in a short shell script. One day this might be shipped with safecopy, until then consider this your chance to contribute to a random open source project.)</p>
<dt>&#8211; rescue data of a tape device:</p>
<dd> If the tape device driver supports lseek(), treat it as any file, otherwise utilize the &quot;-S&quot; option of safecopy with a to be self-written script to skip over the bad blocks. (for example using &quot;mt seek&quot;) Make sure your tape device doesn&#8217;t auto-rewind on close. Send me feedback if you had any luck doing so, so I can update this documentation. </p>
</dl>
<h2>FAQ</h2>
<dl>
<dt>Q:</p>
<dd> Why create this tool if there already is something like dd-rescue and other tools for that purpose?</p>
<dt>A:</p>
<dd> Because I didn&#8217;t know of dd(-)rescue when I started, and I felt like it. Also I think safecopy suits the needs of a user in data loss peril better due to more readable output and more understandable options than some of the other tools. (Then again I am biased. Compare them yourself) Meanwhile safecopy supports low level features other tools don&#8217;t.</dl>
<dl>
<dt>Q:</p>
<dd> What exactly does the -Z option do?</p>
<dt>A:</p>
<dd> Remember back in MS-DOS times when a floppy would make a &quot;neek nark&quot; sound 3 times every time when running into a read error? This happened when the BIOS or DOS disk driver moved the IO head to its boundaries to possibly correct small cylinder misalignment, before it tried again. Linux doesn&#8217;t do that by default, neither do common CDROM drives or drivers. Nevertheless forcing this behaviour can increase your chance of reading bad sectors from a CD __BIG__ time. (Unlike floppies where it usually has little effect)</dl>
<dl>
<dt>Q:</p>
<dd> Whats my best chance to resurrect a CD that has become unreadable?</p>
<dt>A:</p>
<dd> Try making a backup image on many different computers and drives. The abilities to read from bad media vary extremely. I have a 6 year old Lite On CDRW drive, that even reads deeply and purposely scratched CDs (as in with my key, to make it unreadable) flawlessly. A CDRW drive of the same age at work doesn&#8217;t read any data from that part of the CD at all, while most DVD and combo drives have bad blocks every couple hundred bytes. Make full use of safecopys RAW access features if applicable. (-L 2 option)</p>
<dt>
<dd> As a general guideline: -CDRW drives usually do better than read-only CD drives.<br />
 -CD only drives sometimes do better on CDs than DVD drives.<br />
 -PC drives are sometimes better than laptop ones.<br />
 -A drive with a clean lens does better than a dirtball.<br />
 -Cleaning up CDs helps.<br />
 -Unless you use chemicals.<br />
 -Using sticky tape on a CD will rip of the reflective layer permanently rendering the disk unreadable.</dl>
<dl>
<dt>Q:</p>
<dd> Whats my best chance to resurrect a floppy that became unreadable?</p>
<dt>A:</p>
<dd> Again try different floppy drives. Keep in mind that it might be easier to further damage data on a bad floppy than on a CD. (Don&#8217;t overdo read attempts)</dl>
<dl>
<dt>Q:</p>
<dd> What about BlueRay/HDDVD disks?</p>
<dt>A:</p>
<dd> Hell if I knew, but generally they should be similar to DVDs. It probably depends how the drives firmware acts up.</dl>
<dl>
<dt>Q:</p>
<dd> My hard drive suddenly has many bad sectors, what should I do?</p>
<dt>A:</p>
<dd> Speed is an essential factor when rescuing data from a bad hard drive. Accesses to bad areas or even just time running can further damage the drive and make formerly readable areas unreadable, be it due to temperature rise, damaged heads scratching still good parts of the surface, bearings degrading due to vibration, etc. Its advisable to shut the system down and remove the hard drive from the computer as soon as errors occur and as fast as possible without causing further damage.</p>
<dt>
<dd> (Don&#8217;t pull the plug! Press reset to force reboot and then power down via power button/ACPI)</p>
<dt>
<dd> Set up a rescue system with enough disk space to store all the data from the damaged drive (and possibly multiple copies of it). If you have an external hard drive case that connects via USB SATA or SCSI, allowing a hot plug of the drive into a running system, use it. This allows you to prepare everything without the need for the drive to power up and possibly BIOS or operating system involuntarily accessing it. You also get easier access to the drive to check temperature or noise during operation.</p>
<dt>
<dd> When you rescue data, rescue good data first before attempting to access bad sectors. Safecopy allows you to skip known problem sectors using a badblock exclude file (-X) which you might be able to retrieve from system logs or from the drive internal logs, via smartmontools or similar software. Be aware that you might possibly need to convert physical sector numbers into logical block numbers depending on your source.</p>
<dt>
<dd> Also you should tell safecopy to jump out of any problematic areas ASAP and continue somewhere else. Parameters &quot;-f 10% -r 10% -R 0 -Z 0&quot; would do the trick by making safecopy skip 10% of the device content and continue there without backtracking. You can always attempt to get the data in between later, first get the supposedly good data on the rest of the drive. Depending on the method of data recovery you plan on using, it may make sense to mark the bad data with the &quot;-M&quot; option. This allows you to later find files affected by data corruption more easily. Use the &quot;-o&quot; option to make safecopy write a badblock list with all blocks skipped or unreadable.</p>
<dt>
<dd> When safecopy is done with this first run, you can attempt a second go trying to get more data. Using smaller values for &quot;-f&quot; and allowing safecopy to backtrack for the end of the affected area &quot;-r 1*&quot;. Be sure to use incremental mode &quot;-I&quot; to only read the blocks skipped in the first run.</p>
<dt>
<dd> It may make sense to let the drive cool down between runs. Once you got all the data from the &quot;good&quot; areas of the drive you can risk more &quot;thorough&quot; access to it. Increase the numbers of retries &quot;-R&quot; in case of bad blocks, maybe together with a head realignment &quot;-Z 1&quot;. &quot;-f 1*&quot; would make safecopy try to read on every single block, not skipping over bad areas at all.</p>
<dt>
<dd> If your drive stops responding, power it down, let it cool down for a while, then try again.</p>
<dt>
<dd> (I heard from people who brought dead drives back to live for a short time by cooling them to low temperatures with ice-packs.)</p>
<dt>
<dd> <code>!!!</code> If the data is really important, go to a professional data recovery specialist right away, before doing further damage to the drive. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> safecopy returns 0 (zero) if there were no unrecoverable errors.<br />
 safecopy returns 1 if some data could not be recovered.<br />
 safecopy returns 2 in case the copying was aborted due to error or signal. </p>
<h2>AUTHORS</h2>
<p> safecopy and its manpage have been designed and written by CorvusCorax. </p>
<h2>BUGS</h2>
<p> Please use the project page on sourceforge &lt;<a rel="nofollow" href="http://www.sf.net/projects/safecopy">http://www.sf.net/projects/safecopy</a>&gt; to get in contact with project development if you encounter bugs or want to contribute to safecopy. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 CorvusCorax<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License version 2 or above. &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>SEE ALSO</h2>
<p> Programs with a similar scope are among others</p>
<dl>
<dt><i><a href="/docs/linux/man/1-ddrescue/">ddrescue</a></i>(1), <i><a href="/docs/linux/man/1-dd-rescue/">dd-rescue</a></i>(1), &#8230;</p>
<dd>
</dl>
<h2>Index</h2>
