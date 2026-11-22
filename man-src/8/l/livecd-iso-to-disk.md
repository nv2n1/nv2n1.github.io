---
title: "livecd-iso-to-disk(8)"
name: "livecd-iso-to-disk"
section: "8"
letter: "l"
url: "/docs/linux/man/8-livecd-iso-to-disk/"
description: "livecd-iso-to-disk – installs bootable Live images onto USB/SD storage devices."
---

<p>livecd-iso-to-disk &#8211; installs bootable Live images onto USB/SD storage devices.</p>
<h2>Synopsis</h2>
<p><code>livecd-iso-to-disk</code> [&#8211;help] [&#8211;noverify] [&#8211;format] [&#8211;reset-mbr] [&#8211;efi] [&#8211;skipcopy] [&#8211;force] [&#8211;xo] [&#8211;xo-no-home] [&#8211;timeout &lt;time&gt;] [&#8211;totaltimeout &lt;time&gt;] [&#8211;extra-kernel-args &lt;args&gt;] [&#8211;multi] [&#8211;livedir &lt;dir&gt;] [&#8211;compress] [&#8211;skipcompress] [&#8211;swap-size-mb &lt;size&gt;] [&#8211;overlay-size-mb &lt;size&gt;] [&#8211;home-size-mb &lt;size&gt;] [&#8211;delete-home] [&#8211;crypted-home] [&#8211;unencrypted-home] [&#8211;updates updates.img] [&#8211;ks kickstart] &lt;source&gt; &lt;target device&gt; </p>
<p> Simplest </p>
<p> The script may be run in simplest form with just the two arguments: </p>
<p> <code>livecd-iso-to-disk</code> &lt;source&gt; &lt;target device&gt; </p>
<p> To execute the script to completion, you will need to run it with root user permissions. SYSLINUX must be installed on the computer running the installation script.</p>
<dl>
<dt>&lt;source&gt;</dt>
<dd>This may be the filesystem path to a LiveOS .iso image file, such as from a CD-ROM, DVD, or download. It could also be the device node reference for the mount point of another LiveOS filesystem, including the currently-running one (such as a booted Live CD/DVD/USB, where /dev/live references the running image device).</dd>
<dt>&lt;target device&gt;</dt>
<dd>This should be the device partition name for the attached, target device, such as /dev/sdb1 or /dev/sdc1. (Issue the df -Th command to get a listing of the mounted partitions, where you can confirm the filesystem types, available space, and device names.) Be careful to specify the correct device, or you may overwrite important data on another disk!</dd></dl>
<h2>Description</h2>
<p><code>livecd-iso-to-disk</code> installs a Live CD/DVD/USB image (LiveOS) onto a USB/SD storage device (or any storage partition that will boot with a SYSLINUX bootloader). The target storage device can then boot the installed operating system on systems that support booting via the USB or the SD interface. The script requires a LiveOS source image and a target storage device. The source image may be either a LiveOS .iso file, the currently-running LiveOS image, the device node reference for an attached device with an installed LiveOS image, or a file backed by a block device with an installed LiveOS image. If the operating system supports persistent overlays for saving system changes, a pre-sized overlay may be included with the installation. </p>
<p> Unless you request the &#8211;format option, the installation does not destroy data outside of the LiveOS, syslinux, &amp; EFI folders on your target device. This allows one to maintain other files on the target disk outside of the LiveOS filesystem. </p>
<p> LiveOS images provide embedded filesystems through the Device-mapper component of the Linux kernel. The embedded filesystems exist within files such as /LiveOS/squashfs.img (the default compressed storage) or /LiveOS/ext3fs.img (an uncompressed version) on the primary volume partition of the storage device. In use, these are read-only filesystems. Optionally, one may specify a persistent LiveOS overlay to hold image-change snapshots (that use write-once, difference-tracking storage) in the /LiveOS/overlay-&lt;device_id&gt; file, which, *one should note*, always grows in size due to the storage mechanism. (The fraction of allocated space that has been consumed by system activity and changes may be displayed by issuing the &#8216;dmsetup status&#8217; command in a terminal session of a running LiveOS image.) One way to conserve the unrecoverable, overlay file space, is to specify a persistent home folder for user files, which will be saved in a /LiveOS/home.img filesystem image file. This file space is encrypted by default, but is not compressed. (One may bypass encryption with the &#8211;unencrypted-home installation option.) Files in this home folder may be erased to recover and reuse their storage space. The home.img file is also convenient for backing up or swapping user account files.</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Displays usage information and exits.</dd>
<dt>&#8211;noverify</dt>
<dd>Disables the image validation process that occurs before the image is installed from the original Live CD .iso image. When this option is specified, the image is not verified before loading onto the target storage device.</dd>
<dt>&#8211;format</dt>
<dd>Formats the target device and creates an MS-DOS partition table (or GUID partition table, if the &#8211;efi option is passed).</dd>
<dt>&#8211;reset-mbr</dt>
<dd>Sets the Master Boot Record (MBR) of the target storage device to the mbr.bin file from the installation system&#8217;s syslinux directory. This may be helpful in recovering a damaged or corrupted device.</dd>
<dt>&#8211;efi</dt>
<dd>Creates a GUID partition table when &#8211;format is passed, and installs a hybrid Extensible Firmware Interface (EFI)/MBR bootloader on the disk. This is necessary for most Intel Macs.</dd>
<dt>&#8211;skipcopy</dt>
<dd>Skips the copying of the live image to the target device, bypassing the actions of the &#8211;format, &#8211;overlay-size-mb, &#8211;home-size-mb, &amp; &#8211;swap-size-mb options, if present on the command line. (The &#8211;skipcopy option may be used while testing the script, in order to avoid repeated and lengthy copy commands, or to repair boot configuration files on a previously installed device.)</dd>
<dt>&#8211;force</dt>
<dd>This option allows the installation script to bypass a delete confirmation dialog in the event that a pre-existing LiveOS directory is found on the target device.</dd>
<dt>&#8211;xo</dt>
<dd>Used to prepare an image for the OLPC XO-1 laptop with its compressed, JFFS2 filesystem. Do not use the following options with &#8211;xo:</dd>
<dl>
<dd>
</dd><dl>
<dd>&#8211;overlay-size-mb &lt;size&gt;, home-size-mb &lt;size&gt;, &#8211;delete-home, &#8211;compress</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<dt>&#8211;xo-no-home</dt>
<dd>Used together with the &#8211;xo option to prepare an image for an OLPC XO laptop with the home folder on an SD card instead of the internal flash storage.</dd>
<dt>&#8211;timeout</dt>
<dd>Modifies the bootloader&#8217;s timeout value, which indicates how long to pause at the boot: prompt before booting automatically. This overrides the value set during iso creation. Units are 1/10 s. The timeout is canceled when any key is pressed, the assumption being that the user will complete the command line. A timeout of zero will disable the timeout completely.</dd>
<dt>&#8211;totaltimeout</dt>
<dd>Adds a bootloader totaltimeout, which indicates how long to wait before booting automatically. This is used to force an automatic boot. This timeout cannot be canceled by the user. Units are 1/10 s.</dd>
<dt>&#8211;extra-kernel-args &lt;args&gt;</dt>
<dd>Specifies additional kernel arguments, &lt;args&gt;, that will be inserted into the syslinux and EFI boot configurations. Multiple arguments should be specified in one string, i.e., &#8211;extra-kernel-args &#8220;arg1 arg2 &#8230;&#8221;</dd>
<dt>&#8211;multi</dt>
<dd>Used when installing multiple image copies to signal configuration of the boot files for the image in the &#8211;livedir &lt;dir&gt; parameter.</dd>
<dt>&#8211;livedir &lt;dir&gt;</dt>
<dd>Used with multiple image installations to designate the directory &lt;dir&gt; for the particular image.</dd>
<dt>&#8211;compress (default state for the operating system files)</dt>
<dd>The default, compressed SquashFS filesystem image is copied on installation. This option has no effect when the source filesystem is already expanded.</dd>
<dt>&#8211;skipcompress (default option when &#8211;xo is specified)</dt>
<dd>Expands the source SquashFS image on installation into the read-only /LiveOS/ext3fs.img filesystem image file.</dd>
<dt>&#8211;swap-size-mb &lt;size&gt;</dt>
<dd>Sets up a swap file of &lt;size&gt; mebibytes (integer values only) on the target device.</dd>
<dt>&#8211;overlay-size-mb &lt;size&gt;</dt>
<dd>This option sets the overlay size in mebibytes (integer values only). The overlay makes persistent storage available to the live operating system, if the operating system supports it. The persistent LiveOS overlay holds image-change snapshots (using write-once, difference-tracking storage) in the /LiveOS/overlay-&lt;device_id&gt; file, which, *one should note*, always grows in size due to the storage mechanism. (The fraction of allocated space that has been consumed may be displayed by issuing the &#8216;dmsetup status&#8217; command in a terminal session of a running LiveOS installation.) One way to conserve the unrecoverable, overlay file space, is to specify a persistent home folder for user files, see &#8211;home-size-mb below. The target storage device must have enough free space for the image and the overlay. A maximum &lt;size&gt; of 4095 MiB is permitted for vfat-formatted devices. If there is insufficient room on your device, you will be given information to help in adjusting your settings.</dd>
<dt>&#8211;home-size-mb &lt;size&gt;</dt>
<dd>Sets the home directory size in mebibytes (integer values only). A persistent home directory will be made in the /LiveOS/home.img filesystem image file. This file space is encrypted by default, but not compressed (one may bypass encryption with the &#8211;unencrypted-home installation option). Files in this home folder may be erased to recover and reuse their storage space. The target storage device must have enough free space for the image, any overlay, and the home directory. Note that the &#8211;delete-home option must also be selected to replace an existing persistent home with a new, empty one. A maximum &lt;size&gt; of 4095 MiB is permitted for vfat-formatted devices. If there is insufficient room on your device, you will be given information to help in adjusting your settings.</dd>
<dt>&#8211;delete-home</dt>
<dd>To prevent unwitting deletion of user files, this option must be explicitly selected when the option &#8211;home-size-mb &lt;size&gt; is selected and there is an existing persistent home directory on the target device.</dd>
<dt>&#8211;crypted-home (default that only applies to new home-size-mb requests)</dt>
<dd>Specifies the default option to encrypt a new persistent home directory if &#8211;home-size-mb &lt;size&gt; is specified.</dd>
<dt>&#8211;unencrypted-home</dt>
<dd>Prevents the default option to encrypt a new persistent home directory.</dd>
<dt>&#8211;updates updates.img</dt>
<dd>Setup inst.updates to point to an updates image on the device. Anaconda uses this for testing updates to an iso without needing to make a new iso.</dd>
<dt>&#8211;ks kickstart</dt>
<dd>Setup inst.ks to point to an kickstart file on the device. Use this for automating installs on boot.</dd></dl>
<h2>Contributors</h2>
<p>David Zeuthen, Jeremy Katz, Douglas McClendon, Chris Curran and other contributors. See the AUTHORS file in the source distribution for the complete list of credits.</p>
<h2>Bugs</h2>
<p>Report bugs to the mailing list <tt>&quot;<a rel="nofollow" href="http://admin.fedoraproject.org/mailman/listinfo/livecd">http://admin.fedoraproject.org/mailman/listinfo/livecd</a>&quot;</tt> or directly to Bugzilla <tt>&quot;<a href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a>&quot;</tt> against the <tt>&quot;Fedora&quot;</tt> product, and the <tt>&quot;livecd-tools&quot;</tt> component.</p>
<h2>Copyright</h2>
<p>Copyright (C) Fedora Project 2008, 2009, 2010 and various contributors. This is free software. You may redistribute copies of it under the terms of the GNU General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p><tt>&quot;livecd-creator(1)&quot;</tt>, project website <tt>&quot;<a rel="nofollow" href="http://fedoraproject.org/wiki/FedoraLiveCD">http://fedoraproject.org/wiki/FedoraLiveCD</a>&quot;</tt> </p>
