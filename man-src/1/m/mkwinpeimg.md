---
title: "mkwinpeimg(1)"
name: "mkwinpeimg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkwinpeimg/"
description: "mkwinpeimg – Make a customized bootable image of Windows PE"
---

<h2>NAME</h2>
<p> mkwinpeimg &#8211; Make a customized bootable image of Windows PE</p>
<h2>SYNOPSIS</h2>
<p> <code>mkwinpeimg</code> [<i>OPTIONS</i>] <i>IMAGE</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mkwinpeimg</code> is able to make a bootable image of Windows PE by taking files from a mounted Windows installation ISO image (Vista or later) or the mounted ISO image for the Windows Automated Installation Kit (WAIK) or the WAIK supplement. The <code>&#8211;windows-dir</code> and <code>&#8211;waik-dir</code> options are used to specify the locations of these mounted ISOs. You only need one or the other. The files that <code>mkwinpeimg</code> will retrieve are <i>boot.wim</i>, <i>bootmgr</i>, <i>boot.sdi</i>, and <i>bcd</i>. If making an ISO image, the file <i>etfsboot.com</i> is also retrieved. Microsoft owns the rights to these files and they are not distributed with wimlib. </p>
<p> <code>mkwinpeimg</code> can make two types of bootable images. The default is to make a bootable disk image. The image is not partitioned and is formatted into a FAT filesystem. <code><a href="/docs/linux/man/1-syslinux/">syslinux</a></code>(1) is required to make this type of image, as it is used to chainload <i>bootmgr</i>. Also, <code><a href="/docs/linux/man/1-mtools/">mtools</a></code>(1) is required so that the FAT filesystem can be created without root privileges. </p>
<p> The other type of bootable image that <code>mkwinpeimg</code> can make is a bootable ISO image. To make this type of image, give the <code>&#8211;iso</code> option. <code><a href="/docs/linux/man/1-mkisofs/">mkisofs</a></code>(1) is required to make this type of image. In <code>&#8211;iso</code> mode, you can specify <i>IMAGE</i> as &quot;-&quot; to write the ISO image to standard output. </p>
<p> If you make a disk image, you could put it on a USB drive, and if you make an ISO image, you could put it on a CD. In addition, both types of images can be loaded by the SYSLINUX or PXELINUX bootloaders using the MEMDISK module. </p>
<p> Windows PE itself is contained in the <i>boot.wim</i> file. <code>mkwinpeimg</code> can modify this file before embedding it in a bootable image. The most useful modification is to specify an executable or batch file for Windows PE to execute as soon as it starts up. Use the <code>&#8211;start-script</code> <i>FILE</i> option to specify such a file. You may also add arbitrary files to <i>boot.wim</i> by putting them in a directory, then specifying the <code>&#8211;overlay</code> <i>DIR</i> option. However, for more extensive modifications, consider modifying the <i>boot.wim</i> file separately using <code>wimlib-imagex mountrw</code> or <code>wimlib-imagex update</code>, then providing it to <code>mkwinpeimg</code> using the <code>&#8211;wim</code> option. </p>
<p> <code>mkwinpeimg</code> can also make only a modified <i>boot.wim</i>, rather than a bootable ISO or disk image, if the <code>&#8211;only-wim</code> option is given.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;iso</code></p>
<dd> Make an ISO image instead of a disk image.</p>
<dt><code>-o</code>, <code>&#8211;only-wim</code></p>
<dd> Make neither a disk image nor an ISO image; instead, only make a modified <i>boot.wim</i> file.</p>
<dt><code>-W</code>, <code>&#8211;windows-dir</code>=<i>DIR</i></p>
<dd> Use DIR as the location of the mounted Windows installation ISO image. If neither <code>&#8211;windows-dir</code> nor <code>&#8211;waik-dir</code> is specified, then the script looks for the mounted ISO in the following default locations: /mnt/windows, /mnt/windows7, /mnt/windows8, and /mnt/windows10.</p>
<dt><code>-A</code>, <code>&#8211;waik-dir</code>=<i>DIR</i></p>
<dd> Get the boot files and boot.wim from the ISO of the Windows Automated Installation Kit mounted on DIR instead of from a Windows installation ISO. This also works if the mounted ISO is for the WAIK supplement rather than the WAIK itself.</p>
<dt><code>-s</code>, <code>&#8211;start-script</code>=<i>FILE</i></p>
<dd> Add FILE to the root directory of Windows PE image and adjust \Windows\System32\winpeshl.ini to execute FILE when Windows PE starts up.</p>
<dt><code>-w</code>, <code>&#8211;wim</code>=<i>WIM</i></p>
<dd> Use WIM as the &quot;boot.wim&quot; file. This defaults to the appropriate WIM file from the Windows ISO, WAIK, or WAIK supplement.</p>
<dt><code>-O</code>, <code>&#8211;overlay</code>=<i>DIR</i></p>
<dd> Adds all the files in DIR to the Windows PE image.</p>
<dt><code>-t</code>, <code>&#8211;tmp-dir</code>=<i>DIR</i></p>
<dd> Use DIR for temporary files. Defaults to a directory made using &quot;mktemp -d&quot;.</p>
<dt><code>-a</code>, <code>&#8211;arch</code>=<i>ARCH</i></p>
<dd> Use the Windows PE version from the Windows Automated Installation Kit (or the WAIK supplement) that has the CPU architecture <i>ARCH</i>. Only valid with <code>&#8211;waik-dir</code>. Possible values: &quot;x86&quot; or &quot;amd64&quot;. Default is &quot;x86&quot;. Note: the WAIK also contains a Windows PE image for the ia64 (Itanium) architecture; however, this is not supported by this script.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Show version information.</dl>
<h2>EXAMPLES</h2>
<p> Create a bootable disk image of Windows PE from the Windows (Vista or later) installation media mounted on /media/windows:</p>
<dl>
<dt>
<dd>
<p> mkwinpeimg &#8211;windows-dir=/media/windows winpe.img</dl>
<p> Create a bootable ISO of Windows PE from the WAIK (or WAIK supplement) mounted on /media/waik, and add all the files in &quot;winpe_overlay&quot; to Windows PE&#8217;s filesystem:</p>
<dl>
<dt>
<dd>
<p> mkwinpeimg &#8211;iso &#8211;waik-dir=/media/waik &#8211;overlay=winpe_overlay winpe.iso</dl>
<p> Create a bootable image of Windows PE from the Windows installation media mounted on /media/windows, add and make it execute &quot;install.cmd&quot; when it starts up. In this example the image is created in the root directory of the TFTP server for network booting.</p>
<dl>
<dt>
<dd>
<p> mkwinpeimg &#8211;start-script=install.cmd &#8211;windows-dir=/media/windows /var/tftpboot/winpe.img</dl>
<h2>NOTES</h2>
<p> Microsoft&#8217;s licenses may limit the things that Windows PE can be used for, and they may limit your rights to redistribute customized versions of Windows PE.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to ebiggers3 [at] gmail.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) </p>
<h2>Index</h2>
