---
title: "euca-bundle-vol(1)"
name: "euca-bundle-vol"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-bundle-vol/"
description: "euca-bundle-vol – Prepare this machine’s filesystem for use in the cloud"
---

<h2>NAME</h2>
<p> euca-bundle-vol &#8211; Prepare this machine&#8217;s filesystem for use in the cloud</p>
<h2>SYNOPSIS</h2>
<p> euca-bundle-vol [-p PREFIX] [-d DIR]</p>
<dl>
<dt>[-r {i386,x86_64,armhf,ppc,ppc64,ppc64le}]</p>
<dd> [-e PATH,&#8230;] [-i PATH,&#8230;] [-s MiB] [&#8211;no-filter] [&#8211;all] [&#8211;inherit | <code>&#8211;no-inherit]</code> [-v DIR] [-P {mbr,gpt,none}] [-S FILE] [&#8211;fstab FILE | <code>&#8211;generate-fstab]</code> [&#8211;grub-config FILE] [-k FILE] [-c FILE] [&#8211;ec2cert FILE] [-u ACCOUNT] [&#8211;kernel IMAGE] [&#8211;ramdisk IMAGE] [-B VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;] [&#8211;productcodes CODE1,CODE2,&#8230;] [&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Prepare this machine&#8217;s filesystem for use in the cloud</p>
<h2>DESCRIPTION</h2>
<p> This command must be run as the superuser.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PREFIX, <code>&#8211;prefix</code> PREFIX</p>
<dd> the file name prefix to give the bundle&#8217;s files (default: image)</p>
<dt><code>-d</code> DIR, <code>&#8211;destination</code> DIR</p>
<dd> location to place the bundle&#8217;s files (default: dir named by TMPDIR, TEMP, or TMP environment variables, or otherwise <i>,/var/tmp/</i>)</p>
<dt><code>-r</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}, <code>&#8211;arch</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}</p>
<dd> the image&#8217;s architecture (required)</p>
<dt><code>-e</code> PATH,&#8230;, <code>&#8211;exclude</code> PATH,&#8230;</p>
<dd> comma-separated list of paths to exclude</p>
<dt><code>-i</code> PATH,&#8230;, <code>&#8211;include</code> PATH,&#8230;</p>
<dd> comma-separated list of paths to include</p>
<dt><code>-s</code> MiB, <code>&#8211;size</code> MiB</p>
<dd> size of the image to create (default: 10240 MiB)</p>
<dt><code>&#8211;no-filter</code></p>
<dd> do not filter out sensitive/system files</p>
<dt><code>&#8211;all</code></p>
<dd> include all filesystems regardless of type (default: only include local filesystems)</p>
<dt><code>&#8211;inherit</code></p>
<dd> use the metadata service to provide metadata for the bundle (this is the default)</p>
<dt><code>&#8211;no-inherit</code></p>
<dd> do not use the metadata service for bundle metadata</p>
<dt><code>-v</code> DIR, <code>&#8211;volume</code> DIR</p>
<dd> location of the volume from which to create the bundle (default: /)</p>
<dt><code>-P</code> {mbr,gpt,none}, <code>&#8211;partition</code> {mbr,gpt,none}</p>
<dd> the type of partition table to create (default: attempt to guess based on the existing disk)</p>
<dt><code>-S</code> FILE, <code>&#8211;script</code> FILE</p>
<dd> location of a script to run immediately before bundling. It will receive the volume&#8217;s mount point as its only argument.</p>
<dt><code>&#8211;fstab</code> FILE</p>
<dd> location of an <a href="/docs/linux/man/5-fstab/">fstab</a>(5) file to copy into the bundled image</p>
<dt><code>&#8211;generate-fstab</code></p>
<dd> automatically generate an <a href="/docs/linux/man/5-fstab/">fstab</a>(5) file for the bundled image</p>
<dt><code>&#8211;grub-config</code> FILE</p>
<dd> location of a GRUB 1 configuration file to copy to <i>,/boot/grub/menu.lst/</i> on the bundled image</p>
<dt><code>-k</code> FILE, <code>&#8211;privatekey</code> FILE</p>
<dd> file containing your private key to sign the bundle&#8217;s manifest with. This private key will also be required to unbundle the image in the future.</p>
<dt><code>-c</code> FILE, <code>&#8211;cert</code> FILE</p>
<dd> file containing your X.509 certificate</p>
<dt><code>&#8211;ec2cert</code> FILE</p>
<dd> file containing the cloud&#8217;s X.509 certificate</p>
<dt><code>-u</code> ACCOUNT, <code>&#8211;user</code> ACCOUNT</p>
<dd> your account ID</p>
<dt><code>&#8211;kernel</code> IMAGE</p>
<dd> ID of the kernel image to associate with this machine image</p>
<dt><code>&#8211;ramdisk</code> IMAGE</p>
<dd> ID of the ramdisk image to associate with this machine image</p>
<dt><code>-B</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;, <code>&#8211;block-device-mappings</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;</p>
<dd> block device mapping scheme with which to launch instances of this machine image</p>
<dt><code>&#8211;productcodes</code> CODE1,CODE2,&#8230;</p>
<dd> comma-separated list of product codes for the image</p>
<dt><code>&#8211;progress</code></p>
<dd> show progress (the default when run interactively)</p>
<dt><code>&#8211;no-progress</code></p>
<dd> do not show progress (the default when run noninteractively)</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
