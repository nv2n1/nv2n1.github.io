---
title: "ntfsclone(8)"
name: "ntfsclone"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsclone/"
description: "ntfsclone – Efficiently clone, image, restore or rescue an NTFS"
---

<p>ntfsclone &#8211; Efficiently clone, image, restore or rescue an NTFS</p>
<h2>Synopsis</h2>
<p><code>ntfsclone</code> [<i>OPTIONS</i>] <i>SOURCE</i><br />
 <code>ntfsclone &#8211;save-image</code> [<i>OPTIONS</i>] <i>SOURCE</i><br />
 <code>ntfsclone &#8211;restore-image</code> [<i>OPTIONS</i>] <i>SOURCE</i><br />
 <code>ntfsclone &#8211;metadata</code> [<i>OPTIONS</i>] <i>SOURCE</i></p>
<h2>Description</h2>
<p><code>ntfsclone</code> will efficiently clone (copy, save, backup, restore) or rescue an NTFS filesystem to a sparse file, image, device (partition) or standard output. It works at disk sector level and copies only the used data. Unused disk space becomes zero (cloning to sparse file), encoded with control codes (saving in special image format), left unchanged (cloning to a disk/partition) or filled with zeros (cloning to standard output). </p>
<p> <code>ntfsclone</code> can be useful to make backups, an exact snapshot of an NTFS filesystem and restore it later on, or for developers to test NTFS read/write functionality, troubleshoot/investigate users&#8217; issues using the clone without the risk of destroying the original filesystem. </p>
<p> The clone, if not using the special image format, is an exact copy of the original NTFS filesystem from sector to sector thus it can be also mounted just like the original NTFS filesystem. For example if you clone to a file and the kernel has loopback device and NTFS support then the file can be mounted as</p>
<dl>
<dd><code>mount -t ntfs -o loop ntfsclone.img /mnt/ntfsclone</code> </p>
</dl>
<h3>Windows Cloning</h3>
<p>If you want to copy, move or restore a system or boot partition to another computer, or to a different disk or partition (e.g. hda1-&gt;hda2, hda1-&gt;hdb1 or to a different disk sector offset) then you will need to take extra care. </p>
<p> Usually, Windows will not be able to boot, unless you copy, move or restore NTFS to the same partition which starts at the same sector on the same type of disk having the same BIOS legacy cylinder setting as the original partition and disk had. </p>
<p> The ntfsclone utility guarantees to make an exact copy of NTFS but it won&#8217;t deal with booting issues. This is by design: ntfsclone is a filesystem, not system utility. Its aim is only NTFS cloning, not Windows cloning. Hereby ntfsclone can be used as a very fast and reliable build block for Windows cloning but itself it&#8217;s not enough.</p>
<h3>Sparse Files</h3>
<p>A file is sparse if it has unallocated blocks (holes). The reported size of such files are always higher than the disk space consumed by them. The <code>du</code> command can tell the real disk space used by a sparse file. The holes are always read as zeros. All major Linux filesystem like, ext2, ext3, reiserfs, Reiser4, JFS and XFS, supports sparse files but for example the ISO 9600 CD-ROM filesystem doesn&#8217;t.</p>
<h3>Handling Large Sparse Files</h3>
<p>As of today Linux provides inadequate support for managing (tar, cp, gzip, gunzip, bzip2, bunzip2, cat, etc) large sparse files. The only main Linux filesystem having support for efficient sparse file handling is XFS by the XFS_IOC_GETBMAPX <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)<code>.</code> However none of the common utilities supports it. This means when you tar, cp, gzip, bzip2, etc a large sparse file they will always read the entire file, even if you use the &quot;sparse support&quot; options. </p>
<p> <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) compresses large sparse files much better than <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) but it does so also much slower. Moreover neither of them handles large sparse files efficiently during uncompression from disk space usage point of view. </p>
<p> At present the most efficient way, both speed and space-wise, to compress and uncompress large sparse files by common tools would be using <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) with the options <code>-S</code> (handle sparse files &quot;efficiently&quot;) and <code>-j</code> (filter the archive through bzip2). Although <code>tar</code> still reads and analyses the entire file, it doesn&#8217;t pass on the large data blocks having only zeros to filters and it also avoids writing large amount of zeros to the disk needlessly. But since <code>tar</code> can&#8217;t create an archive from the standard input, you can&#8217;t do this in-place by just reading <code>ntfsclone</code> standard output. Even more sadly, using the -S option results serious data loss since the end of 2004 and the GNU <code>tar</code> maintainers didn&#8217;t release fixed versions until the present day.</p>
<h3>The Special Image Format</h3>
<p>It&#8217;s also possible, actually it&#8217;s recommended, to save an NTFS filesystem to a special image format. Instead of representing unallocated blocks as holes, they are encoded using control codes. Thus, the image saves space without requiring sparse file support. The image format is ideal for streaming filesystem images over the network and similar, and can be used as a replacement for Ghost or Partition Image if it is combined with other tools. The downside is that you can&#8217;t mount the image directly, you need to restore it first. </p>
<p> To save an image using the special image format, use the <code>-s</code> or the <code>&#8211;save-image</code> option. To restore an image, use the <code>-r</code> or the <code>&#8211;restore-image</code> option. Note that you can restore images from standard input by using &#8216;-&#8216; as the <i>SOURCE</i> file.</p>
<h3>Metadata-only Cloning</h3>
<p>One of the features of <code>ntfsclone</code> is that, it can also save only the NTFS metadata using the option <code>-m</code> or <code>&#8211;metadata</code> and the clone still will be mountable. In this case all non-metadata file content will be lost and reading them back will result always zeros. </p>
<p> The metadata-only image can be compressed very well, usually to not more than 1-8 MB thus it&#8217;s easy to transfer for investigation, troubleshooting. </p>
<p> In this mode of ntfsclone, <code>NONE</code> of the user&#8217;s data is saved, including the resident user&#8217;s data embedded into metadata. All is filled with zeros. Moreover all the file timestamps, deleted and unused spaces inside the metadata are filled with zeros. Thus this mode is inappropriate for example for forensic analyses. This mode may be combined with <code>&#8211;save-image</code> to create a special image format file instead of a sparse file. </p>
<p> Please note, filenames are not wiped out. They might contain sensitive information, so think twice before sending such an image to anybody.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsclone</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212; .</code> Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v .</code> Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-o</code>, <code>&#8211;output</code> FILE</p>
<dd>Clone NTFS to the non-existent <i>FILE</i>. If <i>FILE</i> is &#8216;-&#8216; then clone to the standard output. This option cannot be used for creating a partition, use <code>&#8211;overwrite</code> for an existing partition.</p>
<dt><code>-O</code>, <code>&#8211;overwrite</code> FILE</p>
<dd>Clone NTFS to <i>FILE</i>, which can be an existing partition or a regular file which will be overwritten if it exists.</p>
<dt><code>-s</code>, <code>&#8211;save-image</code></p>
<dd>Save to the special image format. This is the most efficient way space and speed-wise if imaging is done to the standard output, e.g. for image compression, encryption or streaming through a network.</p>
<dt><code>-r</code>, <code>&#8211;restore-image</code></p>
<dd>Restore from the special image format specified by <i>SOURCE</i> argument. If the <i>SOURCE</i> is &#8216;-&#8216; then the image is read from the standard input.</p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Test the consistency of a saved image by simulating its restoring without writing anything. The NTFS data contained in the image is not tested. The option <code>&#8211;restore-image</code> must also be present, and the options <code>&#8211;output</code> and <code>&#8211;overwrite</code> must be omitted.</p>
<dt><code>&#8211;rescue</code></p>
<dd>Ignore disk read errors so disks having bad sectors, e.g. dying disks, can be rescued the most efficiently way, with minimal stress on them. Ntfsclone works at the lowest, sector level in this mode too thus more data can be rescued. The contents of the unreadable sectors are filled by character &#8216;?&#8217; and the beginning of such sectors are marked by &quot;BadSectoR
