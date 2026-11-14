---
title: "virt-dib(1)"
name: "virt-dib"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-dib/"
description: "virt-dib – Run diskimage-builder elements"
---

<h2 class="name">NAME</h2>
<p> virt-dib &#8211; Run diskimage-builder elements </p>
<h2>SYNOPSIS</h2>
<pre>
 virt-dib -B DIB-LIB [options] elements...
</pre>
<h2>DESCRIPTION</h2>
<p> Virt-dib is a tool for using the elements of <tt>&quot;diskimage-builder&quot;</tt> to build a new disk image, generate new ramdisks, etc. </p>
<p> Virt-dib is intended as safe replacement for <tt>&quot;diskimage-builder&quot;</tt> and its <tt>&quot;ramdisk-image-create&quot;</tt> mode, see &#8220;<font SIZE="-1">COMPARISON WITH</font> DISKIMAGE-BUILDER&#8221; for a quick comparison with usage of <tt>&quot;diskimage-builder&quot;</tt>. </p>
<p> <tt>&quot;diskimage-builder&quot;</tt> is part of the TripleO OpenStack project: <a rel="nofollow" href="https://wiki.openstack.org/wiki/TripleO.">https://wiki.openstack.org/wiki/TripleO.</a></p>
<h2>EXAMPLES</h2>
<h3>Build simple images of distributions</h3>
<pre>
 virt-dib \
   -B /path/to/diskimage-builder/lib \
   -p /path/to/diskimage-builder/elements \
   --envvar DIB_RELEASE=jessie \
   --name debian-jessie \
   debian vm
</pre>
<p> This builds a Debian Jessie (8.x) disk image, suitable for running as virtual machine, saved as <i>debian-jessie.qcow2</i>.</p>
<h3>Build ramdisks</h3>
<pre>
 virt-dib \
   -B /path/to/diskimage-builder/lib \
   -p /path/to/diskimage-builder/elements \
   --ramdisk \
   --name ramdisk \
   ubuntu deploy-ironic
</pre>
<p> This builds a ramdisk for the Ironic OpenStack component based on the Ubuntu distribution.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>-B</code> <font SIZE="-1">PATH</font></p>
<dd> Set the path to the library directory of <tt>&quot;diskimage-builder&quot;</tt>. This is usually the <i>lib</i> subdirectory in the sources and when installed, and <i>/usr/share/diskimage-builder/lib</i> when installed in <i>/usr</i>. </p>
<p> This parameter is <code>mandatory</code>, as virt-dib needs to provide it for the elements (as some of them might use scripts in it). Virt-dib itself does not make use of the library directory.</p>
<dt><code>&#8211;arch</code> <font SIZE="-1">ARCHITECTURE</font></p>
<dd> Use the specified architecture for the output image. The default value is the same as the host running virt-dib. </p>
<p> Right now this option does nothing more than setting the <tt>&quot;ARCH&quot;</tt> environment variable for the elements, and it&#8217;s up to them to produce an image for the requested architecture.</p>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>&#8211;debug</code> <font SIZE="-1">LEVEL</font></p>
<dd> Set the debug level to <tt>&quot;LEVEL&quot;</tt>, which is a non-negative integer number. The default is <tt>0</tt>. </p>
<p> This debug level is different than what <i>-x</i> and <i>-v</i> set, and it increases the debugging information printed out. Specifically, this sets the <tt>&quot;DIB_DEBUG_TRACE&quot;</tt>, and any value &gt; <tt>0</tt> enables tracing in the scripts executed.</p>
<dt><code>&#8211;drive</code> <font SIZE="-1">DISK</font></p>
<dd> Add the specified disk to be used as helper drive where to cache files of the elements, like disk images, distribution packages, etc. </p>
<p> See &#8220;<font SIZE="-1">HELPER DRIVE&#8221;</font>.</p>
<dt><code>-p</code> <font SIZE="-1">PATH</font></p>
<dd>
<dt><code>&#8211;element-path</code> <font SIZE="-1">PATH</font></p>
<dd> Add a new path with elements. Paths are used in the same order as the <i>-p</i> parameters appear, so a path specified first is looked first, and so on. </p>
<p> Obviously, it is recommended to add the path to the own elements of <tt>&quot;diskimage-builder&quot;</tt>, as most of the other elements will rely on them.</p>
<dt><code>&#8211;extra-packages</code> <font SIZE="-1">PACKAGE,&#8230;</font></p>
<dd> Install additional packages in the image being built. </p>
<p> This relies on the <tt>&quot;install-packages&quot;</tt> binary provided by the package management elements. </p>
<p> This option can be specified multiple times, each time with multiple packages separated by comma.</p>
<dt><code>&#8211;envvar</code> <font SIZE="-1">VARIABLE</font></p>
<dd>
<dt><code>&#8211;envvar</code> VARIABLE=VALUE</p>
<dd> Carry or set an environment variable for the elements. </p>
<p> See &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> below for more information on the interaction and usage of environment variables. </p>
<p> This option can be used in two ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;envvar</code> <font SIZE="-1">VARIABLE</font></p>
<dd> Carry the environment variable <tt>&quot;VARIABLE&quot;</tt>. If it is not set, nothing is exported to the elements.</p>
<dt><code>&#8211;envvar</code> VARIABLE=VALUE</p>
<dd> Set the environment variable <tt>&quot;VARIABLE&quot;</tt> with value <tt>&quot;VALUE&quot;</tt> for the elements, regardless whether an environment variable with the same name exists. </p>
<p> This can be useful to pass environment variable without exporting them in the environment where virt-dib runs.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;exclude-element</code> <font SIZE="-1">ELEMENT</font></p>
<dd> Ignore the specified element.</p>
<dt><code>&#8211;exclude-script</code> <font SIZE="-1">SCRIPT</font></p>
<dd> Ignore any element script named <tt>&quot;SCRIPT&quot;</tt>, whichever element it is in. </p>
<p> This can be useful in case some script does not run well with virt-dib, for example when they really need <tt>&quot;diskimage-builder&quot;</tt>&#8216;s environment.</p>
<dt><code>&#8211;formats</code> <font SIZE="-1">FORMAT,&#8230;</font></p>
<dd> Set the list of output formats, separating them with comma. </p>
<p> Supported formats are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;qcow2&quot; (enabled by default)</p>
<dd> <font SIZE="-1">QEMU</font>&#8216;s qcow2.</p>
<dt>&quot;raw&quot;</p>
<dd> Raw disk format.</p>
<dt>&quot;tar&quot;</p>
<dd> An uncompressed tarball.</p>
<dt>&quot;vhd&quot;</p>
<dd> <tt>&quot;Virtual Hard Disk&quot;</tt> disk image. This output format requires the <tt>&quot;vhd-util&quot;</tt> tool. </p>
<p> Please note that the version of <tt>&quot;vhd-util&quot;</tt> tool needs to be patched to support the <tt>&quot;convert&quot;</tt> subcommand, and to be bootable. The patch is available here: <a rel="nofollow" href="https://github.com/emonty/vhd-util/blob/master/debian/patches/citrix.">https://github.com/emonty/vhd-util/blob/master/debian/patches/citrix.</a></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;fs-type</code> <font SIZE="-1">FILESYSTEM</font></p>
<dd> Set the filesystem type to use for the root filesystem. The default is <tt>&quot;ext4&quot;</tt>. </p>
<p> See also &#8220;guestfs_filesystem_available&#8221; in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<dt><code>&#8211;image-cache</code> <font SIZE="-1">DIRECTORY</font></p>
<dd> Set the path in the host where cache the resources used by the elements of the <tt>&quot;extra-data.d&quot;</tt> phase. The default is <i>~/.cache/image-create</i>. </p>
<p> Please note that most of the resources fetched after <tt>&quot;extra-data&quot;</tt> will be cached in the helper drive specified with <i>&#8211;drive</i>; see also &#8220;<font SIZE="-1">HELPER DRIVE&#8221;</font>.</p>
<dt><code>&#8211;install-type</code> <font SIZE="-1">TYPE</font></p>
<dd> Specify the default installation type. Defaults to <tt>&quot;source&quot;</tt>. </p>
<p> Set to <tt>&quot;package&quot;</tt> to use package based installations by default.</p>
<dt><code>&#8211;machine-readable</code></p>
<dd> This option is used to make the output more machine friendly when being parsed by other programs. See &#8220;<font SIZE="-1">MACHINE READABLE OUTPUT&#8221;</font> below.</p>
<dt><code>-m</code> <font SIZE="-1">MB</font></p>
<dd>
<dt><code>&#8211;memsize</code> <font SIZE="-1">MB</font></p>
<dd> Change the amount of memory allocated to the appliance. Increase this if you find that the virt-dib execution runs out of memory. </p>
<p> The default can be found with this command: </p>
<pre>
 guestfish get-memsize
</pre>
<dt><code>&#8211;mkfs-options</code> &quot;OPTION STRING&quot;</p>
<dd> Add the specified options to <i><a href="/docs/linux/man/1-mkfs/">mkfs</a></i>(1), to be able to fine-tune the root filesystem creation. Note that this is not possible to override the filesystem type. </p>
<p> You should use <i>&#8211;mkfs-options</i> at most once. To pass multiple options, separate them with space, eg: </p>
<pre>
 virt-dib ... --mkfs-options '-O someopt -I foo'
</pre>
<dt><code>&#8211;network</code></p>
<dd>
<dt><code>&#8211;no-network</code></p>
<dd> Enable or disable network access from the guest during the installation. </p>
<p> Enabled is the default. Use <i>&#8211;no-network</i> to disable access. </p>
<p> The network only allows outgoing connections and has other minor limitations. See &#8220;<font SIZE="-1">NETWORK&#8221;</font> in <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1). </p>
<p> This does not affect whether the guest can access the network once it has been booted, because that is controlled by your hypervisor or cloud environment and has nothing to do with virt-dib. </p>
<p> If you use <i>&#8211;no-network</i>, then the environment variable <tt>&quot;DIB_OFFLINE&quot;</tt> is set to <tt>1</tt>, signaling the elements that they should use only cached resources when available. Note also that, unlike with <tt>&quot;diskimage-builder&quot;</tt> where elements may still be able to access to the network even with <tt>&quot;DIB_OFFLINE=&quot;</tt>, under virt-dib network will be fully unaccessible.</p>
<dt><code>&#8211;name</code> <font SIZE="-1">NAME</font></p>
<dd> Set the name of the output image file. The default is <tt>&quot;image&quot;</tt>. </p>
<p> According to the chosen name, there will be the following in the current directory:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>$NAME.ext</i></p>
<dd> For each output format, a disk image named after the outout image with the extension depending on the format; for example: <i></i>$NAME<i>.qcow2</i>, <i></i>$NAME<i>.raw</i>, etc. </p>
<p> Not applicable in ramdisk mode, see &#8220;<font SIZE="-1">RAMDISK BUILDING&#8221;</font>.</p>
<dt><i>$NAME.d</i></p>
<dd> A directory containing any files created by the elements, for example <i>dib-manifests</i> directory (created by the <tt>&quot;manifests&quot;</tt> element), ramdisks and kernels in ramdisk mode, and so on.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-delete-on-failure</code></p>
<dd> Don&#8217;t delete the output files on failure to build. You can use this to debug failures to run scripts. </p>
<p> The default is to delete the output file if virt-dib fails (or, for example, some script that it runs fails).</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t print ordinary progress messages.</p>
<dt><code>&#8211;qemu-img-options</code> option[,option,&#8230;]</p>
<dd> Pass <i>&#8211;qemu-img-options</i> option(s) to the <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1) command to fine-tune the output format. Options available depend on the output format (see <i>&#8211;formats</i>) and the installed version of the qemu-img program. </p>
<p> You should use <i>&#8211;qemu-img-options</i> at most once. To pass multiple options, separate them with commas, eg: </p>
<pre>
 virt-dib ... --qemu-img-options cluster_size=512,preallocation=metadata ...
</pre>
<dt><code>&#8211;ramdisk</code></p>
<dd> Set the ramdisk building mode. </p>
<p> See &#8220;<font SIZE="-1">RAMDISK BUILDING&#8221;</font>.</p>
<dt><code>&#8211;ramdisk-element</code> <font SIZE="-1">NAME</font></p>
<dd> Set the name for the additional element added in ramdisk building mode. The default is <tt>&quot;ramdisk&quot;</tt>. </p>
<p> See &#8220;<font SIZE="-1">RAMDISK BUILDING&#8221;</font>.</p>
<dt><code>&#8211;root-label</code> <font SIZE="-1">LABEL</font></p>
<dd> Set the label for the root filesystem in the created image. </p>
<p> Please note that some filesystems have different restrictions on the length of their labels; for example, on <tt>&quot;ext2/3/4&quot;</tt> filesystems labels cannot be longer than 16 characters, while on <tt>&quot;xfs&quot;</tt> they have at most 12 characters. </p>
<p> The default depends on the actual filesystem for the root partition (see <i>&#8211;fs-type</i>): on <tt>&quot;xfs&quot;</tt> is <tt>&quot;img-rootfs&quot;</tt>, while <tt>&quot;cloudimg-rootfs&quot;</tt> on any other filesystem.</p>
<dt><code>&#8211;size</code> <font SIZE="-1">SIZE</font></p>
<dd> Select the size of the output disk, where the size can be specified using common names such as <tt>&quot;32G&quot;</tt> (32 gigabytes) etc. The default size is <tt>&quot;5G&quot;</tt>. </p>
<p> To specify size in bytes, the number must be followed by the lowercase letter <i>b</i>, eg: <tt>&quot;--size 10737418240b&quot;</tt>. </p>
<p> See also <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1) for resizing partitions of an existing disk image.</p>
<dt><code>&#8211;skip-base</code></p>
<dd> Skip the inclusion of the <tt>&quot;base&quot;</tt> element.</p>
<dt><code>&#8211;smp</code> N</p>
<dd> Enable N ≥ 2 virtual CPUs for scripts to use.</p>
<dt><code>-u</code></p>
<dd> Do not compress resulting qcow2 images. The default is to compress them.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable debugging messages.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Unlike with <tt>&quot;diskimage-builder&quot;</tt>, the environment of the host is <code>not</code> inherited in the appliance when running most of the elements (i.e. all the ones different than <tt>&quot;extra-data.d&quot;</tt>). </p>
<p> To set environment for the elements being run, it is necessary to tell virt-dib to use them, with the option <i>&#8211;envvar</i>. Such option allows to selectively export environment variables when running the elements, and it is the preferred way to pass environment variables to the elements. </p>
<p> To recap: if you want the environment variable <tt>&quot;MYVAR&quot;</tt> (and its content) to be available to the elements, you can do either </p>
<pre>
 export MYVAR   # whichever is its value
 virt-dib ... --envvar MYVAR ...
</pre>
<p> or </p>
<pre>
 virt-dib ... --envvar MYVAR=value_of_it ...
</pre>
<h2>HELPER DRIVE</h2>
<p> Virt-dib runs most of the element in its own appliance, and thus not on the host. Because of this, there is no possibility for elements to cache resources directly on the host. </p>
<p> To solve this issue, virt-dib allows the usage of an helper drive where to store cached resources, like disk images, distribution packages, etc. While this means that there is a smaller space available for caching, at least it allows to limit the space on the host for caches, without assuming that elements will do that by themselves. </p>
<p> Currently this disk is either required to have a single partition on it, or the first partition on it will be used. A disk with the latter configuration can be easily created with <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) like the following: </p>
<pre>
 guestfish -N filename.img=fs:ext4:10G
</pre>
<p> The above will create a disk image called <i>filename.img</i>, 10G big, with a single partition of type ext4; see &#8220;<font SIZE="-1">PREPARED DISK IMAGES&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). </p>
<p> It is recommended for it to be ≥ 10G or even more, as elements will cache disk images, distribution packages, etc. As with any disk image, the helper disk can be easily resized using <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1) if more space in it is needed. </p>
<p> The drive can be accessed like any other disk image, for example using other tools of libguestfs such as <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1): </p>
<pre>
 guestfish -a filename.img -m /dev/sda1
</pre>
<p> If no helper drive is specified with <i>&#8211;drive</i>, all the resources cached during a virt-dib run will be discarded.</p>
<h3><font SIZE="-1">RESOURCES INSIDE THE DRIVE</font></h3>
<p> Inside the helper drive, it is possible to find the following resources:</p>
<dl>
<dt><i>/home</i></p>
<dd> This directory is set as <tt>&quot;HOME&quot;</tt> environment variable during the build. It contains mostly the image cache (saved as <i>/home/.cache/image-create</i>), and whichever other resource is cached in the home directory of the user running the various tools.</p>
<dt><i>/virt-dib-*.log</i></p>
<dd> These are the logs of the elements being run within the libguestfs appliance, which means all the hooks except <tt>&quot;extra-data.d&quot;</tt>.</dl>
<h2>RAMDISK BUILDING</h2>
<p> Virt-dib can emulate also <tt>&quot;ramdisk-image-create&quot;</tt>, which is a secondary operation mode of <tt>&quot;diskimage-builder&quot;</tt>. Instead of being a different tool name, virt-dib provides easy access to this mode using the <i>&#8211;ramdisk</i> switch. </p>
<p> In this mode:</p>
<dl>
<dt>&bull;</p>
<dd> there is an additional ramdisk element added (see <i>&#8211;ramdisk-element</i>)</p>
<dt>&bull;</p>
<dd> no image is produced (so <i>&#8211;formats</i> is ignored)</p>
<dt>&bull;</p>
<dd> <i></i>$NAME<i>.d</i> (see <i>&#8211;name</i>) will contain initrd, kernel, etc</dl>
<h2>TEMPORARY DIRECTORY</h2>
<p> Virt-dib uses the standard temporary directory used by libguestfs, see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3). </p>
<p> By default this location is <i>/tmp</i> (default value for <tt>&quot;TMPDIR&quot;</tt>), which on some systems may be on a tmpfs filesystem, and thus defaulting to a maximum size of <i>half</i> of physical <font SIZE="-1">RAM.</font> If virt-dib exceeds this, it may hang or exit early with an error. The solution is to point <tt>&quot;TMPDIR&quot;</tt> to a permanent location used as temporary location, for example: </p>
<pre>
 mkdir local-tmp
 env TMPDIR=$PWD/local-tmp virt-dib ...
 rm -rf local-tmp
</pre>
<h2>EXTRA DEPENDENCIES</h2>
<p> Because of virt-dib runs most of the elements in its own appliance, all the tools and libraries used by elements running outside the guest (typically <tt>&quot;root.d&quot;</tt>, <tt>&quot;block-device.d&quot;</tt>, and <tt>&quot;cleanup.d&quot;</tt>) need to be present in the appliance as well. In case they are not, scripts will fail mostly with a <tt>&quot;command not found&quot;</tt> error. </p>
<p> For tools and libraries packaged by the distribution, the easy solution is to tell libguestfs to include additional packages in the appliance. This is doable by e.g. creating a new file with the additional packages: </p>
<pre>
 # echo wget &gt; /usr/lib64/guestfs/supermin.d/dib-my-extra
</pre>
<p> The actual path to the <i>supermin.d</i> directory depends on the distribution; additional files can list more packages, each in its own line.</p>
<h2>COMPARISON WITH DISKIMAGE-BUILDER</h2>
<p> Virt-dib is intended as safe replacement for <tt>&quot;diskimage-builder&quot;</tt> and its <tt>&quot;ramdisk-image-create&quot;</tt> mode; the user-notable differences consist in:</p>
<dl>
<dt>&bull;</p>
<dd> the command line arguments; some of the arguments are the same as available in <tt>&quot;diskimage-builder&quot;</tt>, while some have different names: </p>
<pre><code>
disk - image - create virt - dib-- -- -- -- -- -- -- -- - -- -- -- -- -a ARCH-- arch ARCH-- image - size SIZE-- size SIZE-- max - online - resize SIZE doable using --mkfs - options - n-- skip - base - o IMAGENAME-- name IMAGENAME - p PACKAGE(S)-- extra - packages PACKAGE(S) - t FORMAT(S)-- formats FORMAT(S) - x-- debug N
</code></pre>
<dt>&bull;</p>
<dd> the location of non-image output files (like ramdisks and kernels)</p>
<dt>&bull;</p>
<dd> the way some of the cached resources are saved: using an helper drive, not directly on the disk where virt-dib is run</p>
<dt>&bull;</p>
<dd> the need to specify a target size for the output disk, as opposed to <tt>&quot;diskimage-builder&quot;</tt> calculating an optimal one</p>
<dt>&bull;</p>
<dd> the handling of environment variables, see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font>. </p>
<p> Furthermore, other than the libguestfs own environment variables (see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)), virt-dib does not read any other environment variable: this means that all the options and behaviour changes are specified solely using command line arguments</p>
<dt>&bull;</p>
<dd> extra tools needed on some out-of-chroot phases need to be available in the appliance, see &#8220;<font SIZE="-1">EXTRA DEPENDENCIES&#8221;</font>.</dl>
<p> Elements themselves should notice no difference in they way they are run; behaviour differences may due to wrong assumptions in elements, or not correct virt-dib emulation. </p>
<p> Known issues at the moment:</p>
<dl>
<dt>&bull;</p>
<dd> (none)</dl>
<h2>MACHINE READABLE OUTPUT</h2>
<p> The <i>&#8211;machine-readable</i> option can be used to make the output more machine friendly, which is useful when calling virt-dib from other programs, GUIs etc. </p>
<p> Use the option on its own to query the capabilities of the virt-dib binary. Typical output looks like this: </p>
<pre>
 $ virt-dib --machine-readable
 virt-dib
 output:qcow2
 output:tar
 output:raw
 output:vhd
</pre>
<p> A list of features is printed, one per line, and the program exits with status 0.</p>
<h2>TESTING</h2>
<p> Virt-dib has been tested with <tt>&quot;diskimage-builder&quot;</tt> (and its elements) ≥ 0.1.43; from time to time also with <tt>&quot;tripleo-image-elements&quot;</tt> and <tt>&quot;sahara-image-elements&quot;</tt>. </p>
<p> Previous versions may work, but it is not guaranteed.</p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Pino Toscano (<tt>&quot;ptoscano at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2015 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAL">RAMDISK BUILDING</a></p>
<dd>
<dt><a href="#lbAM">TEMPORARY DIRECTORY</a></p>
<dd>
<dt><a href="#lbAN">EXTRA DEPENDENCIES</a></p>
<dd>
<dt><a href="#lbAO">COMPARISON WITH DISKIMAGE-BUILDER</a></p>
<dd>
<dt><a href="#lbAP">MACHINE READABLE OUTPUT</a></p>
<dd>
<dt><a href="#lbAQ">TESTING</a></p>
<dd>
<dt><a href="#lbAR">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAS">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAT">AUTHOR</a></p>
<dd>
<dt><a href="#lbAU">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAV">LICENSE</a></p>
<dd>
<dt><a href="#lbAW">BUGS</a></p>
<dd></dl>
