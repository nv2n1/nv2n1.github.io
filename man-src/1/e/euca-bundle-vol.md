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
<p> euca-bundle-vol [-p PREFIX] [-d DIR]</p>
<dl>
<dt>[-r {i386,x86_64,armhf,ppc,ppc64,ppc64le}]</dt>
<dd> [-e PATH,&#8230;] [-i PATH,&#8230;] [-s MiB] [&#8211;no-filter] [&#8211;all] [&#8211;inherit | <code>&#8211;no-inherit]</code> [-v DIR] [-P {mbr,gpt,none}] [-S FILE] [&#8211;fstab FILE | <code>&#8211;generate-fstab]</code> [&#8211;grub-config FILE] [-k FILE] [-c FILE] [&#8211;ec2cert FILE] [-u ACCOUNT] [&#8211;kernel IMAGE] [&#8211;ramdisk IMAGE] [-B VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;] [&#8211;productcodes CODE1,CODE2,&#8230;] [&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<p> Prepare this machine&#8217;s filesystem for use in the cloud</p>
<h2>DESCRIPTION</h2>
<p> This command must be run as the superuser.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> PREFIX, <code>&#8211;prefix</code> PREFIX</dt>
<dd> the file name prefix to give the bundle&#8217;s files (default: image)</dd>
<dt><code>-d</code> DIR, <code>&#8211;destination</code> DIR</dt>
<dd> location to place the bundle&#8217;s files (default: dir named by TMPDIR, TEMP, or TMP environment variables, or otherwise <i>,/var/tmp/</i>)</dd>
<dt><code>-r</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}, <code>&#8211;arch</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}</dt>
<dd> the image&#8217;s architecture (required)</dd>
<dt><code>-e</code> PATH,&#8230;, <code>&#8211;exclude</code> PATH,&#8230;</dt>
<dd> comma-separated list of paths to exclude</dd>
<dt><code>-i</code> PATH,&#8230;, <code>&#8211;include</code> PATH,&#8230;</dt>
<dd> comma-separated list of paths to include</dd>
<dt><code>-s</code> MiB, <code>&#8211;size</code> MiB</dt>
<dd> size of the image to create (default: 10240 MiB)</dd>
<dt><code>&#8211;no-filter</code></dt>
<dd> do not filter out sensitive/system files</dd>
<dt><code>&#8211;all</code></dt>
<dd> include all filesystems regardless of type (default: only include local filesystems)</dd>
<dt><code>&#8211;inherit</code></dt>
<dd> use the metadata service to provide metadata for the bundle (this is the default)</dd>
<dt><code>&#8211;no-inherit</code></dt>
<dd> do not use the metadata service for bundle metadata</dd>
<dt><code>-v</code> DIR, <code>&#8211;volume</code> DIR</dt>
<dd> location of the volume from which to create the bundle (default: /)</dd>
<dt><code>-P</code> {mbr,gpt,none}, <code>&#8211;partition</code> {mbr,gpt,none}</dt>
<dd> the type of partition table to create (default: attempt to guess based on the existing disk)</dd>
<dt><code>-S</code> FILE, <code>&#8211;script</code> FILE</dt>
<dd> location of a script to run immediately before bundling. It will receive the volume&#8217;s mount point as its only argument.</dd>
<dt><code>&#8211;fstab</code> FILE</dt>
<dd> location of an <a href="/docs/linux/man/5-fstab/">fstab</a>(5) file to copy into the bundled image</dd>
<dt><code>&#8211;generate-fstab</code></dt>
<dd> automatically generate an <a href="/docs/linux/man/5-fstab/">fstab</a>(5) file for the bundled image</dd>
<dt><code>&#8211;grub-config</code> FILE</dt>
<dd> location of a GRUB 1 configuration file to copy to <i>,/boot/grub/menu.lst/</i> on the bundled image</dd>
<dt><code>-k</code> FILE, <code>&#8211;privatekey</code> FILE</dt>
<dd> file containing your private key to sign the bundle&#8217;s manifest with. This private key will also be required to unbundle the image in the future.</dd>
<dt><code>-c</code> FILE, <code>&#8211;cert</code> FILE</dt>
<dd> file containing your X.509 certificate</dd>
<dt><code>&#8211;ec2cert</code> FILE</dt>
<dd> file containing the cloud&#8217;s X.509 certificate</dd>
<dt><code>-u</code> ACCOUNT, <code>&#8211;user</code> ACCOUNT</dt>
<dd> your account ID</dd>
<dt><code>&#8211;kernel</code> IMAGE</dt>
<dd> ID of the kernel image to associate with this machine image</dd>
<dt><code>&#8211;ramdisk</code> IMAGE</dt>
<dd> ID of the ramdisk image to associate with this machine image</dd>
<dt><code>-B</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;, <code>&#8211;block-device-mappings</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;</dt>
<dd> block device mapping scheme with which to launch instances of this machine image</dd>
<dt><code>&#8211;productcodes</code> CODE1,CODE2,&#8230;</dt>
<dd> comma-separated list of product codes for the image</dd>
<dt><code>&#8211;progress</code></dt>
<dd> show progress (the default when run interactively)</dd>
<dt><code>&#8211;no-progress</code></dt>
<dd> do not show progress (the default when run noninteractively)</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
