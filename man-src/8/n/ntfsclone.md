---

title: "ntfsclone(8)"
name: "ntfsclone"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsclone/"
description: "ntfsclone – Efficiently clone, image, restore or rescue an NTFS"
---

<p>ntfsclone &#8211; Efficiently clone, image, restore or rescue an NTFS </p>

<p> <code>ntfsclone</code> [<i>OPTIONS</i>] <i>SOURCE</i> <br />
 <code>ntfsclone --save-image</code> [<i>OPTIONS</i>] <i>SOURCE</i> <br />
 <code>ntfsclone --restore-image</code> [<i>OPTIONS</i>] <i>SOURCE</i> <br />
 <code>ntfsclone --metadata</code> [<i>OPTIONS</i>] <i>SOURCE</i>  </p>
<h2>DESCRIPTION</h2>
<p> <code>ntfsclone</code> will efficiently clone (copy, save, backup, restore) or rescue an NTFS filesystem to a sparse file, image, device (partition) or standard output. It works at disk sector level and copies only the used data. Unused disk space becomes zero (cloning to sparse file), encoded with control codes (saving in special image format), left unchanged (cloning to a disk/partition) or filled with zeros (cloning to standard output). </p>
<p> <code>ntfsclone</code> can be useful to make backups, an exact snapshot of an NTFS filesystem and restore it later on, or for developers to test NTFS read/write functionality, troubleshoot/investigate users&#8217; issues using the clone without the risk of destroying the original filesystem. </p>
<p>The clone, if not using the special image format, is an exact copy of the original NTFS filesystem from sector to sector thus it can be also mounted just like the original NTFS filesystem. For example if you clone to a file and the kernel has loopback device and NTFS support then the file can be mounted as </p>
<dl>
<dd> <p> <code>mount -t ntfs -o loop ntfsclone.img /mnt/ntfsclone</code> </p>
 </dd></dl>
<h3>Windows Cloning</h3>
<p> If you want to copy, move or restore a system or boot partition to another computer, or to a different disk or partition (e.g. hda1-&gt;hda2, hda1-&gt;hdb1 or to a different disk sector offset) then you will need to take extra care. </p>
<p>Usually, Windows will not be able to boot, unless you copy, move or restore NTFS to the same partition which starts at the same sector on the same type of disk having the same BIOS legacy cylinder setting as the original partition and disk had. </p>
<p>The ntfsclone utility guarantees to make an exact copy of NTFS but it won&#8217;t deal with booting issues. This is by design: ntfsclone is a filesystem, not system utility. Its aim is only NTFS cloning, not Windows cloning. Hereby ntfsclone can be used as a very fast and reliable build block for Windows cloning but itself it&#8217;s not enough.  </p>
<h3>Sparse Files</h3>
<p> A file is sparse if it has unallocated blocks (holes). The reported size of such files are always higher than the disk space consumed by them. The <code>du</code> command can tell the real disk space used by a sparse file. The holes are always read as zeros. All major Linux filesystem like, ext2, ext3, reiserfs, Reiser4, JFS and XFS, supports sparse files but for example the ISO 9600 CD-ROM filesystem doesn&#8217;t.  </p>
<h3>Handling Large Sparse Files</h3>
<p> As of today Linux provides inadequate support for managing (tar, cp, gzip, gunzip, bzip2, bunzip2, cat, etc) large sparse files. The only main Linux filesystem having support for efficient sparse file handling is XFS by the XFS_IOC_GETBMAPX <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)<code>.</code> However none of the common utilities supports it. This means when you tar, cp, gzip, bzip2, etc a large sparse file they will always read the entire file, even if you use the &quot;sparse support&quot; options. </p>
<p> <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) compresses large sparse files much better than <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) but it does so also much slower. Moreover neither of them handles large sparse files efficiently during uncompression from disk space usage point of view. </p>
<p>At present the most efficient way, both speed and space-wise, to compress and uncompress large sparse files by common tools would be using <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) with the options <code>-S</code> (handle sparse files &quot;efficiently&quot;) and <code>-j</code> (filter the archive through bzip2). Although <code>tar</code> still reads and analyses the entire file, it doesn&#8217;t pass on the large data blocks having only zeros to filters and it also avoids writing large amount of zeros to the disk needlessly. But since <code>tar</code> can&#8217;t create an archive from the standard input, you can&#8217;t do this in-place by just reading <code>ntfsclone</code> standard output. Even more sadly, using the -S option results serious data loss since the end of 2004 and the GNU <code>tar</code> maintainers didn&#8217;t release fixed versions until the present day.  </p>
<h3>The Special Image Format</h3>
<p> It&#8217;s also possible, actually it&#8217;s recommended, to save an NTFS filesystem to a special image format. Instead of representing unallocated blocks as holes, they are encoded using control codes. Thus, the image saves space without requiring sparse file support. The image format is ideal for streaming filesystem images over the network and similar, and can be used as a replacement for Ghost or Partition Image if it is combined with other tools. The downside is that you can&#8217;t mount the image directly, you need to restore it first. </p>
<p>To save an image using the special image format, use the <code>-s</code> or the <code>--save-image</code> option. To restore an image, use the <code>-r</code> or the <code>--restore-image</code> option. Note that you can restore images from standard input by using &#8216;-&#8216; as the <i>SOURCE</i> file.  </p>
<h3>Metadata-only Cloning</h3>
<p> One of the features of <code>ntfsclone</code> is that, it can also save only the NTFS metadata using the option <code>-m</code> or <code>--metadata</code> and the clone still will be mountable. In this case all non-metadata file content will be lost and reading them back will result always zeros. </p>
<p>The metadata-only image can be compressed very well, usually to not more than 1-8 MB thus it&#8217;s easy to transfer for investigation, troubleshooting. </p>
<p>In this mode of ntfsclone, <code>NONE</code> of the user&#8217;s data is saved, including the resident user&#8217;s data embedded into metadata. All is filled with zeros. Moreover all the file timestamps, deleted and unused spaces inside the metadata are filled with zeros. Thus this mode is inappropriate for example for forensic analyses. This mode may be combined with <code>--save-image</code> to create a special image format file instead of a sparse file. </p>
<p>Please note, filenames are not wiped out. They might contain sensitive information, so think twice before sending such an image to anybody.  </p>
<h2>OPTIONS</h2>
<p> Below is a summary of all the options that <code>ntfsclone</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>-</code> and the long name is preceded by <code>-- .</code> Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v .</code> Long named options can be abbreviated to any unique prefix of their name. </p>
<dl>
<dt><code>-o</code>, <code>--output</code> FILE</dt>
<dd> <p> Clone NTFS to the non-existent <i>FILE</i>. If <i>FILE</i> is &#8216;-&#8216; then clone to the standard output. This option cannot be used for creating a partition, use <code>--overwrite</code> for an existing partition. </p>
 </dd>
<dt><code>-O</code>, <code>--overwrite</code> FILE</dt>
<dd> <p> Clone NTFS to <i>FILE</i>, which can be an existing partition or a regular file which will be overwritten if it exists. </p>
 </dd>
<dt><code>-s</code>, <code>--save-image</code></dt>
<dd> <p> Save to the special image format. This is the most efficient way space and speed-wise if imaging is done to the standard output, e.g. for image compression, encryption or streaming through a network. </p>
 </dd>
<dt><code>-r</code>, <code>--restore-image</code></dt>
<dd> <p> Restore from the special image format specified by <i>SOURCE</i> argument. If the <i>SOURCE</i> is &#8216;-&#8216; then the image is read from the standard input. </p>
 </dd>
<dt><code>-n</code>, <code>--no-action</code></dt>
<dd> <p> Test the consistency of a saved image by simulating its restoring without writing anything. The NTFS data contained in the image is not tested. The option <code>--restore-image</code> must also be present, and the options <code>--output</code> and <code>--overwrite</code> must be omitted. </p>
 </dd>
<dt><code>--rescue</code></dt>
<dd> <p> Ignore disk read errors so disks having bad sectors, e.g. dying disks, can be rescued the most efficiently way, with minimal stress on them. Ntfsclone works at the lowest, sector level in this mode too thus more data can be rescued. The contents of the unreadable sectors are filled by character &#8216;?&#8216; and the beginning of such sectors are marked by &quot;BadSectoR\0&quot;. </p>
 </dd>
<dt><code>-m</code>, <code>--metadata</code></dt>
<dd> <p> Clone <code>ONLY METADATA</code> (for NTFS experts). Only cloning to a (sparse) file is allowed, unless used the option <code>--save-image</code> is also used. You can&#8217;t metadata-only clone to a device. </p>
 </dd>
<dt><code>--ignore-fs-check</code></dt>
<dd> <p> Ignore the result of the filesystem consistency check. This option is allowed to be used only with the <code>--metadata</code> option, for the safety of user&#8217;s data. The clusters which cause the inconsistency are saved too. </p>
 </dd>
<dt><code>-t</code>, <code>--preserve-timestamps</code></dt>
<dd> <p> Do not wipe the timestamps, to be used only with the <code>--metadata</code> option. </p>
 </dd>
<dt><code>--full-logfile</code></dt>
<dd> <p> Include the Windows log file in the copy. This is only useful for extracting metadata, saving or cloning a file system which was not properly unmounted from Windows. </p>
 </dd>
<dt><code>--new-serial</code>, or</dt>
<dd>  </dd>
<dt><code>--new-half-serial</code></dt>
<dd> <p> Set a new random serial number to the clone. The serial number is a 64 bit number used to identify the device during the mounting process, so it has to be changed to enable the original file system and the clone to be mounted at the same time on the same computer. </p>
<p>The option <code>--new-half-serial</code> only changes the upper part of the serial number, keeping the lower part which is used by Windows unchanged. </p>
<p>The options <code>--new-serial</code> and <code>--new-half-serial</code> can only be used when cloning a file system of restoring from an image. </p>
<p>The serial number is not the volume UUID used by Windows to locate files which have been moved to another volume. </p>
 </dd>
<dt><code>-f</code>, <code>--force</code></dt>
<dd> <p> Forces ntfsclone to proceed if the filesystem is marked &quot;dirty&quot; for consistency check. </p>
 </dd>
<dt><code>-q</code>, <code>--quiet</code></dt>
<dd> <p> Do not display any progress-bars during operation. </p>
 </dd>
<dt><code>-h</code>, <code>--help</code></dt>
<dd> <p> Show a list of options with a brief description of each one. </p>
 </dd></dl>
<h2>EXIT CODES</h2>
<p> The exit code is 0 on success, non-zero otherwise.  </p>
<h2>EXAMPLES</h2>
<p> Clone NTFS on /dev/hda1 to /dev/hdc1: </p>
<dl>
<dd> <p> <code>ntfsclone --overwrite /dev/hdc1 /dev/hda1</code> </p>
 </dd></dl>
<p> Save an NTFS to a file in the special image format: </p>
<dl>
<dd> <p> <code>ntfsclone --save-image --output backup.img /dev/hda1</code> </p>
 </dd></dl>
<p> Restore an NTFS from a special image file to its original partition: </p>
<dl>
<dd> <p> <code>ntfsclone --restore-image --overwrite /dev/hda1 backup.img</code> </p>
 </dd></dl>
<p> Save an NTFS into a compressed image file: </p>
<dl>
<dd> <p> <code>ntfsclone --save-image -o - /dev/hda1 | gzip -c &gt; backup.img.gz</code> </p>
 </dd></dl>
<p> Restore an NTFS volume from a compressed image file: </p>
<dl>
<dd> <p> <code>gunzip -c backup.img.gz | \\</code> <br />
 <code>ntfsclone --restore-image --overwrite /dev/hda1 -</code> </p>
 </dd></dl>
<p> Backup an NTFS volume to a remote host, using ssh. Please note, that ssh may ask for a password! </p>
<dl>
<dd> <p> <code>ntfsclone --save-image --output - /dev/hda1 | \\</code> <br />
 <code>gzip -c | ssh host &#8216;cat &gt; backup.img.gz&#8217;</code> </p>
 </dd></dl>
<p> Restore an NTFS volume from a remote host via ssh. Please note, that ssh may ask for a password! </p>
<dl>
<dd> <p> <code>ssh host &#8216;cat backup.img.gz&#8217; | gunzip -c | \\</code> <br />
 <code>ntfsclone --restore-image --overwrite /dev/hda1 -</code> </p>
 </dd></dl>
<p> Stream an image file from a web server and restore it to a partition: </p>
<dl>
<dd> <p> <code>wget -qO - <a rel="nofollow" href="http://server/backup.img">http://server/backup.img</a> | \\</code> <br />
 <code>ntfsclone --restore-image --overwrite /dev/hda1 -</code> </p>
 </dd></dl>
<p> Clone an NTFS volume to a non-existent file: </p>
<dl>
<dd> <p> <code>ntfsclone --output ntfs-clone.img /dev/hda1</code> </p>
 </dd></dl>
<p> Pack NTFS metadata for NTFS experts. Please note that bzip2 runs very long but results usually at least 10 times smaller archives than gzip on a sparse file. </p>
<dl>
<dd> <p> <code>ntfsclone --metadata --output ntfsmeta.img /dev/hda1</code> <br />
 <code>bzip2 ntfsmeta.img</code> </p>
<p>Or, outputting to a compressed image : <br />
 <code>ntfsclone -mst --output - /dev/hda1 | bzip2 &gt; ntfsmeta.bz2</code> </p>
 </dd></dl>
<p> Unpacking NTFS metadata into a sparse file: </p>
<dl>
<dd> <p> <code>bunzip2 -c ntfsmeta.img.bz2 | \\</code> <br />
 <code>cp --sparse=always /proc/self/fd/0 ntfsmeta.img</code> </p>
 </dd></dl>
<h2>KNOWN ISSUES</h2>
<p> There are no known problems with <code>ntfsclone</code>. If you think you have found a problem then please send an email describing it to the development team: ntfs-3g-devel [at] lists.sf.net </p>
<p>Sometimes it might appear ntfsclone froze if the clone is on ReiserFS and even CTRL-C won&#8217;t stop it. This is not a bug in ntfsclone, however it&#8217;s due to ReiserFS being extremely inefficient creating large sparse files and not handling signals during this operation. This ReiserFS problem was improved in kernel 2.4.22. XFS, JFS and ext3 don&#8217;t have this problem.  </p>
<h2>AUTHORS</h2>
<p> <code>ntfsclone</code> was written by Szabolcs Szakacsits with contributions from Per Olofsson (special image format support) and Anton Altaparmakov. It was ported to ntfs-3g by Erik Larsson and Jean-Pierre Andre.  </p>
<h2>AVAILABILITY</h2>
<p> <code>ntfsclone</code> is part of the <code>ntfs-3g</code> package and is available at: <br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a>  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ntfsresize/">ntfsresize</a></code>(8) <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) <code><a href="/docs/linux/man/8-xfs_copy/">xfs_copy</a></code>(8) <code><a href="/docs/linux/man/8-debugreiserfs/">debugreiserfs</a></code>(8) <code><a href="/docs/linux/man/8-e2image/">e2image</a></code>(8) </p>
