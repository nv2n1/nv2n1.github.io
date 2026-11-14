---
title: "ntfsresize(8)"
name: "ntfsresize"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsresize/"
description: "ntfsresize – resize an NTFS filesystem without data loss"
---

<p>ntfsresize &#8211; resize an NTFS filesystem without data loss</p>
<h2>Synopsis</h2>
<p><code>ntfsresize</code> [<i>OPTIONS</i>] <code>&#8211;info(-mb-only)</code> <i>DEVICE</i><br />
 <code>ntfsresize</code> [<i>OPTIONS</i>] [<code>&#8211;size </code><i>SIZE</i>[<code>k</code>|<code>M</code>|<code>G</code>]] <i>DEVICE</i></p>
<h2>Description</h2>
<p>The <code>ntfsresize</code> program safely resizes Windows XP, Windows Server 2003, Windows 2000, Windows NT4 and Longhorn NTFS filesystems without data loss. All NTFS versions are supported, used by 32-bit and 64-bit Windows. <code>Defragmentation is NOT required prior to resizing</code> because the program can relocate any data if needed, without risking data integrity. </p>
<p> Ntfsresize can be used to shrink or enlarge any NTFS filesystem located on an unmounted <i>DEVICE</i> (usually a disk partition). The new filesystem will fit in a DEVICE whose desired size is <i>SIZE</i> bytes. The <i>SIZE</i> parameter may have one of the optional modifiers <code>k</code>, <code>M</code>, <code>G</code>, which means the <i>SIZE</i> parameter is given in kilo-, mega- or gigabytes respectively. <code>Ntfsresize</code> conforms to the SI, ATA, IEEE standards and the disk manufacturers by using k=10^3, M=10^6 and G=10^9. </p>
<p> If both <code>&#8211;info(-mb-only)</code> and <code>&#8211;size</code> are omitted then the NTFS filesystem will be enlarged to match the underlying <i>DEVICE</i> size. </p>
<p> To resize a filesystem on a partition, you must resize BOTH the filesystem and the partition by editing the partition table on the disk. Similarly to other command line filesystem resizers, <code>ntfsresize</code> doesn&#8217;t manipulate the size of the partitions, hence to do that you must use a disk partitioning tool as well, for example <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8). Alternatively you could use one of the many user friendly partitioners that uses <code>ntfsresize</code> internally, like Mandriva&#8217;s DiskDrake, QTParted, SUSE/Novell&#8217;s YaST Partitioner, IBM&#8217;s EVMS, GParted or Debian/Ubuntu&#8217;s Partman. </p>
<p> <code>IMPORTANT!</code> It&#8217;s a good practice making REGULAR BACKUPS of your valuable data, especially before using ANY partitioning tools. To do so for NTFS, you could use <code><a href="/docs/linux/man/8-ntfsclone/">ntfsclone</a></code>(8). Don&#8217;t forget to save the partition table as well!</p>
<h3>Shrinkage</h3>
<p>If you wish to shrink an NTFS partition, first use <code>ntfsresize</code> to shrink the size of the filesystem. Then you could use <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) to shrink the size of the partition by deleting the partition and recreating it with the smaller size. Do not make the partition smaller than the new size of NTFS otherwise you won&#8217;t be able to boot. If you did so notwithstanding then just recreate the partition to be as large as NTFS.</p>
<h3>Enlargement</h3>
<p>To enlarge an NTFS filesystem, first you must enlarge the size of the underlying partition. This can be done using <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) by deleting the partition and recreating it with a larger size. Make sure it will not overlap with another existing partition. You may enlarge upwards (first sector unchanged) or downwards (last sector unchanged), but you may not enlarge at both ends in a single step. If you merge two NTFS partitions, only one of them can be expanded to the merged partition. After you have enlarged the partition, you may use <code>ntfsresize</code> to enlarge the size of the filesystem.</p>
<h3>Partitioning</h3>
<p>When recreating the partition by a disk partitioning tool, make sure you create it at the same starting sector and with the same partition type as before. Otherwise you won&#8217;t be able to access your filesystem. Use the &#8216;u&#8217; fdisk command to switch to the reliable sector unit from the default cylinder one. </p>
<p> Also make sure you set the bootable flag for the partition if it existed before. Failing to do so you might not be able to boot your computer from the disk.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsresize</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd>By using this option ntfsresize will only check the device to ensure that it is ready to be resized. If not, it will print any errors detected. If the device is fine, nothing will be printed.</p>
<dt><code>-i</code>, <code>&#8211;info</code></p>
<dd>By using this option without <code>&#8211;expand</code>, ntfsresize will determine the theoretically smallest shrunken filesystem size supported. Most of the time the result is the space already used on the filesystem. Ntfsresize will refuse shrinking to a smaller size than what you got by this option and depending on several factors it might be unable to shrink very close to this theoretical size. Although the integrity of your data should be never in risk, it&#8217;s still strongly recommended to make a test run by using the <code>&#8211;no-action</code> option before real resizing. </p>
<p> Practically the smallest shrunken size generally is at around &quot;used space&quot; + (20-200 MB). Please also take into account that Windows might need about 50-100 MB free space left to boot safely. </p>
<p> If used in association with option <code>&#8211;expand</code>, ntfsresize will determine the smallest downwards expansion size and the possible increments to the size. These are exact byte counts which must not be rounded. This option may be used after the partition has been expanded provided the upper bound has not been changed. </p>
<p> This option never causes any changes to the filesystem, the partition is opened read-only.</p>
<dt><code>-m</code>, <code>&#8211;info-mb-only</code></p>
<dd>Like the info option, only print out the shrinkable size in MB. Print nothing if the shrink size is the same as the original size (in MB). This option cannot be used in association with option <code>&#8211;expand</code>.</p>
<dt><code>-s</code>, <code>&#8211;size</code> SIZE[<code>k</code>|<code>M</code>|<code>G</code>]</p>
<dd>Resize filesystem to fit in a partition whose size is <i>SIZE</i>[<code>k</code>|<code>M</code>|<code>G</code>] bytes by shifting its end and keeping its beginning unchanged. The filesystem size is set to be at least one sector smaller than the partition. The optional modifiers <code>k</code>, <code>M</code>, <code>G</code> mean the <i>SIZE</i> parameter is given in kilo-, mega- or gigabytes respectively. Conforming to standards, k=10^3, M=10^6 and G=10^9. ki=2^10, Mi=2^20 and Gi=2^30 are also allowed. Use this option with <code>&#8211;no-action</code> first.</p>
<dt><code>-x</code>, <code>&#8211;expand</code></p>
<dd>Expand the filesystem to the current partition size, shifting down its beginning and keeping its end unchanged. The metadata is recreated in the expanded space and no user data is relocated. This is incompatible with option -s (or &#8211;size) and can only be made if the expanded space is an exact multiple of the cluster size. It must also be large enough to hold the new metadata. </p>
<p> If the expansion is interrupted for some reason (power outage, etc), you may restart the resizing, as the original data and metadata have been kept unchanged. </p>
<p> Note : expanding a Windows system partition and filesystem downwards may lead to the registry or some files not matching the new system layout, or to some important files being located too far from the beginning of the partition, thus making Windows not bootable.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Forces ntfsresize to proceed with the resize operation either without prompting for an explicit acceptance, or if the filesystem is marked for consistency check. Double the option (-ff, &#8211;force &#8211;force) to avoid prompting even if the file system is marked for check. </p>
<p> Please note, ntfsresize always marks the filesystem for consistency check before a real resize operation and it leaves that way for extra safety. Thus if NTFS was marked by ntfsresize then it&#8217;s safe to use this option. If you need to resize several times without booting into Windows between each resizing steps then you must use this option.</p>
<dt><code>-n, &#8211;no-action</code></p>
<dd>Use this option to make a test run before doing the real resize operation. Volume will be opened read-only and <code>ntfsresize</code> displays what it would do if it were to resize the filesystem. Continue with the real resizing only if the test run passed.</p>
<dt><code>-b</code>, <code>&#8211;bad-sectors</code></p>
<dd>Support disks having hardware errors, bad sectors with those <code>ntfsresize</code> would refuse to work by default. </p>
<p> Prior using this option, it&#8217;s strongly recommended to make a backup by <code><a href="/docs/linux/man/8-ntfsclone/">ntfsclone</a></code>(8) using the &#8211;rescue option, then running &#8216;chkdsk /f /r volume:&#8217; on Windows from the command line. If the disk guarantee is still valid then replace it. It&#8217;s defected. Please also note, that no software can repair these type of hardware errors. The most what they can do is to work around the permanent defects. </p>
<p> This option doesn&#8217;t have any effect if the disk is flawless.</p>
<dt><code>-P</code>, <code>&#8211;no-progress-bar</code></p>
<dd>Don&#8217;t show progress bars.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>More output.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print the version number of <code>ntfsresize</code> and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display help and exit.</dl>
<h2>Exit Codes</h2>
<p>The exit code is 0 on success, non-zero otherwise.</p>
<h2>Known Issues</h2>
<p>No reliability problem is known. If you find a bug please send an email describing the problem to the development team at:<br />
 ntfs-3g-devel [at] lists.sf.net </p>
<p> There are a few very rarely met restrictions at present: filesystems having unknown bad sectors, relocation of the first MFT extent and resizing into the middle of a $MFTMirr extent aren&#8217;t supported yet. These cases are detected and resizing is restricted to a safe size or the closest safe size is displayed. </p>
<p> <code>Ntfsresize</code> schedules an NTFS consistency check and after the first boot into Windows you must see <code>chkdsk</code> running on a blue background. This is intentional and no need to worry about it. Windows may force a quick reboot after the consistency check. Moreover after repartitioning your disk and depending on the hardware configuration, the Windows message <code>System Settings Change</code> may also appear. Just acknowledge it and reboot again. </p>
<p> The disk geometry handling semantic (HDIO_GETGEO ioctl) has changed in an incompatible way in Linux 2.6 kernels and this triggered multitudinous partition table corruptions resulting in unbootable Windows systems, even if NTFS was consistent, if <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8) was involved in some way. This problem was often attributed to ntfsresize but in fact it&#8217;s completely independent of NTFS thus ntfsresize. Moreover ntfsresize never touches the partition table at all. By changing the &#8216;Disk Access Mode&#8217; to LBA in the BIOS makes booting work again, most of the time. You can find more information about this issue in the Troubleshooting section of the below referred Ntfsresize FAQ.</p>
<h2>Authors</h2>
<p><code>ntfsresize</code> was written by Szabolcs Szakacsits, with contributions from Anton Altaparmakov and Richard Russon. It was ported to ntfs-3g by Erik Larsson and Jean-Pierre Andre.</p>
<h2>Acknowledgement</h2>
<p>Many thanks to Anton Altaparmakov and Richard Russon for libntfs, the excellent documentation and comments, to Gergely Madarasz, Dewey M. Sasser and Miguel Lastra and his colleagues at the University of Granada for their continuous and highly valuable help, furthermore to Erik Meade, Martin Fick, Sandro Hawke, Dave Croal, Lorrin Nelson, Geert Hendrickx, Robert Bjorkman and Richard Burdick for beta testing the relocation support, to Florian Eyben, Fritz Oppliger, Richard Ebling, Sid-Ahmed Touati, Jan Kiszka, Benjamin Redelings, Christopher Haney, Ryan Durk, Ralf Beyer, Scott Hansen, Alan Evans for the valued contributions and to Theodore Ts&#8217;o whose <code><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></code>(8) man page originally formed the basis of this page.</p>
<h2>Availability</h2>
<p><code>ntfsresize</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8), <code><a href="/docs/linux/man/8-sfdisk/">sfdisk</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-evms/">evms</a></code>(8), <code><a href="/docs/linux/man/8-ntfsclone/">ntfsclone</a></code>(8), <code><a href="/docs/linux/man/8-mkntfs/">mkntfs</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
