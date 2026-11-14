---
title: "livemedia-creator(1)"
name: "livemedia-creator"
section: "1"
letter: "l"
url: "/docs/linux/man/1-livemedia-creator/"
description: "livemedia-creator – Create live install media"
---

<h2>NAME</h2>
<p> livemedia-creator &#8211; Create live install media </p>
<h2>SYNOPSIS</h2>
<p> livemedia-creator [-h]<br />
&nbsp;<wbr>(&#8211;make-iso | &#8211;make-disk | &#8211;make-fsimage | &#8211;make-appliance | &#8211;make-ami | &#8211;make-tar | &#8211;make-pxe-live | &#8211;make-ostree-live)<br />
&nbsp;<wbr>[&#8211;iso ISO]&nbsp;<wbr>[&#8211;disk-image DISK_IMAGE]<br />
&nbsp;<wbr>[&#8211;fs-image FS_IMAGE]&nbsp;<wbr>[&#8211;ks KS]<br />
&nbsp;<wbr>[&#8211;image-name IMAGE_NAME]&nbsp;<wbr>[&#8211;image-only]<br />
&nbsp;<wbr>[&#8211;fs-label FS_LABEL]<br />
&nbsp;<wbr>[&#8211;compression]&nbsp;<wbr>[&#8211;compress-arg]<br />
&nbsp;<wbr>[&#8211;live-rootfs-size LIVE_ROOTFS_SIZE]<br />
&nbsp;<wbr>[&#8211;live-rootfs-keep-size LIVE_ROOTFS_KEEP_SIZE]<br />
&nbsp;<wbr>[&#8211;keep-image]&nbsp;<wbr>[&#8211;no-virt]&nbsp;<wbr>[&#8211;proxy PROXY]<br />
&nbsp;<wbr>[&#8211;anaconda-arg ANACONDA_ARGS]<br />
&nbsp;<wbr>[&#8211;armplatform ARMPLATFORM]&nbsp;<wbr>[&#8211;location LOCATION]<br />
&nbsp;<wbr>[&#8211;logfile LOGFILE]<br />
&nbsp;<wbr>[&#8211;lorax-templates LORAX_TEMPLATES]&nbsp;<wbr>[&#8211;tmp TMP]<br />
&nbsp;<wbr>[&#8211;resultdir RESULT_DIR]&nbsp;<wbr>[&#8211;app-name APP_NAME]<br />
&nbsp;<wbr>[&#8211;app-template APP_TEMPLATE]&nbsp;<wbr>[&#8211;app-file APP_FILE]<br />
&nbsp;<wbr>[&#8211;ram MEMORY]&nbsp;<wbr>[&#8211;vcpus VCPUS]&nbsp;<wbr>[&#8211;vnc VNC]<br />
&nbsp;<wbr>[&#8211;arch ARCH]&nbsp;<wbr>[&#8211;kernel-args KERNEL_ARGS]<br />
&nbsp;<wbr>[&#8211;dracut-arg DRACUT_ARGS]&nbsp;<wbr>[&#8211;title TITLE]<br />
&nbsp;<wbr>[&#8211;project PROJECT]&nbsp;<wbr>[&#8211;releasever RELEASEVER]<br />
&nbsp;<wbr>[&#8211;volid VOLID]&nbsp;<wbr>[&#8211;squashfs_args SQUASHFS_ARGS] </p>
<h2>DESCRIPTION</h2>
<p> livemedia-creator uses Anaconda, kickstart and Lorax to create bootable media that use the same install path as a normal system install. It can be used to make live isos, bootable (partitioned) disk images and filesystem images for use with virtualization. </p>
<p> The general idea is to use virt-install to install into a disk image and then use the disk image to create the bootable media. </p>
<p> livemedia-creator &#8211;help will describe all of the options available. At the minimum you need: </p>
<p> &#8211;make-iso to create a final bootable .iso &#8211;iso to specify the Anaconda install media to use with virt-install &#8211;ks is the kickstart to use to install the system </p>
<h2>OPTIONAL ARGUMENTS:</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show this help message and exit </p>
<dt><code>&#8211;make-iso</code></p>
<dd> Build a live iso </p>
<dt><code>&#8211;make-disk</code></p>
<dd> Build a partitioned disk image </p>
<dt><code>&#8211;make-fsimage</code></p>
<dd> Build a filesystem image </p>
<dt><code>&#8211;make-appliance</code></p>
<dd> Build an appliance image and XML description </p>
<dt><code>&#8211;make-ami</code></p>
<dd> Build an ami image </p>
<dt><code>&#8211;make-tar</code></p>
<dd> Build a tar of the root filesystem. Defaults to root.tar.xz </p>
<dt><code>&#8211;make-pxe-live</code></p>
<dd> Build a live pxe boot squashfs image </p>
<dt><code>&#8211;make-ostree-live</code></p>
<dd> Build a live pxe boot squashfs image of Atomic Host </p>
<dt><code>&#8211;iso ISO</code></p>
<dd> Anaconda installation .iso path to use for virt-install </p>
<dt><code>&#8211;disk-image DISK_IMAGE</code></p>
<dd> Path to disk image to use for creating final image </p>
<dt><code>&#8211;fs-image FS_IMAGE</code></p>
<dd> Path to existing filesystem image to use for creating final image. </p>
<dt><code>&#8211;qcow2</code></p>
<dd> Create qcow2 image instead of raw sparse image when making disk images. </p>
<dt><code>&#8211;qcow2-arg</code></p>
<dd> Arguments to pass to qemu-img. Pass once for each argument &gt;&gt;&gt;&gt;&gt;&gt;&gt; d04a99e&#8230; livemedia-creator: Add support for making tarfiles </p>
<dt><code>&#8211;compression</code></p>
<dd> Compression binary for make-tar. xz, lzma, gzip, and bzip2 are supported. xz is the default. </p>
<dt><code>&#8211;compress-arg</code></p>
<dd> Arguments to pass to compression. Pass once for each argument </p>
<dt><code>&#8211;ks KS</code></p>
<dd> Kickstart file defining the install. </p>
<dt><code>&#8211;image-name IMAGE_NAME</code></p>
<dd> Name of fs/disk image to create. Default is a random name. </p>
<dt><code>&#8211;image-only</code></p>
<dd> Exit after creating fs/disk image. </p>
<dt><code>&#8211;keep-image</code></p>
<dd> Keep raw disk image after .iso creation </p>
<dt><code>&#8211;no-virt</code></p>
<dd> Use Anaconda&#8217;s image install instead of virt-install </p>
<dt><code>&#8211;proxy PROXY</code></p>
<dd> proxy URL to use for the install </p>
<dt><code>&#8211;anaconda-arg ANACONDA_ARGS</code></p>
<dd> Additional argument to pass to anaconda (no-virt mode). Pass once for eachargument </p>
<dt><code>&#8211;armplatform ARMPLATFORM</code></p>
<dd> the platform to use when creating images for ARM, i.e., highbank, mvebu, omap,tegra, etc. </p>
<dt><code>&#8211;location LOCATION</code></p>
<dd> location of iso directory tree with initrd.img and vmlinuz. Used to run virt-install with a newer initrd than the iso. </p>
<dt><code>&#8211;logfile LOGFILE</code></p>
<dd> Path to logfile </p>
<dt><code>&#8211;lorax-templates LORAX_TEMPLATES</code></p>
<dd> Path to mako templates for lorax </p>
<dt><code>&#8211;tmp TMP</code></p>
<dd> Top level temporary directory </p>
<dt><code>&#8211;resultdir RESULT_DIR</code></p>
<dd> Directory to copy the resulting images and iso into. Defaults to the temporaryworking directory </p>
<dt><code>&#8211;title TITLE</code></p>
<dd> Substituted for @TITLE@ in bootloader config files </p>
<dt><code>&#8211;project PROJECT</code></p>
<dd> substituted for @PROJECT@ in bootloader config files </p>
<dt><code>&#8211;releasever RELEASEVER</code></p>
<dd> substituted for @VERSION@ in bootloader config files </p>
<dt><code>&#8211;volid VOLID</code></p>
<dd> volume id </p>
<dt><code>&#8211;squashfs_args SQUASHFS_ARGS</code></p>
<dd> additional squashfs args </p>
</dl>
<h2>APPLIANCE ARGUMENTS:</h2>
<dl>
<dt><code>&#8211;app-name APP_NAME</code></p>
<dd> Name of appliance to pass to template </p>
<dt><code>&#8211;app-template APP_TEMPLATE</code></p>
<dd> Path to template to use for appliance data. </p>
<dt><code>&#8211;app-file APP_FILE</code></p>
<dd> Appliance template results file. </p>
</dl>
<h2>PXE-LIVE ARGUMENTS:</h2>
<dl>
<dt><code>&#8211;live-rootfs-size</code></p>
<dd> Size of root filesystem of live image in GiB. By default approximate size of space used in root filesystem is used. </p>
<dt><code>&#8211;live-rootfs-keep-size</code></p>
<dd> Keep the size of original root filesystem (rounded down to GiB) in live image </p>
</dl>
<h2>VIRT-INSTALL ARGUMENTS:</h2>
<dl>
<dt><code>&#8211;ram MEMORY</code></p>
<dd> Memory to allocate for installer in megabytes. </p>
<dt><code>&#8211;vcpus VCPUS</code></p>
<dd> Passed to &#8211;vcpus command </p>
<dt><code>&#8211;vnc VNC</code></p>
<dd> Passed to &#8211;graphics command </p>
<dt><code>&#8211;arch ARCH</code></p>
<dd> Passed to &#8211;arch command </p>
<dt><code>&#8211;kernel-args KERNEL_ARGS</code></p>
<dd> Additional argument to pass to the installation kernel </p>
</dl>
<h2>DRACUT ARGUMENTS:</h2>
<dl>
<dt><code>&#8211;dracut-arg DRACUT_ARGS</code></p>
<dd> Argument to pass to dracut when rebuilding the initramfs. Pass this once foreach argument. NOTE: this overrides the default. </p>
</dl>
<h2>SEE ALSO</h2>
<p> Documentation in /usr/share/docs/lorax/README.livemedia-creator </p>
<h2>AUTHOR</h2>
<pre>
Brian C. Lane
</pre>
<h2>Index</h2>
