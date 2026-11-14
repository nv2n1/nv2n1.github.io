---
title: "initramfs-tools(8)"
name: "initramfs-tools"
section: "8"
letter: "i"
url: "/docs/linux/man/8-initramfs-tools/"
description: "initramfs-tools – an introduction to writing scripts for mkinitramfs"
---

<p>initramfs-tools &#8211; an introduction to writing scripts for mkinitramfs</p>
<h2>Description</h2>
<p>initramfs-tools has one main script and two different sets of subscripts which will be used during different phases of execution. Each of these will be discussed separately below with the help of an imaginary tool which performs a frobnication of a lvm partition prior to mounting the root partition. </p>
<h2>Kernel Command Line</h2>
<p>The root filesystem used by the kernel is specified by the boot loader as always. The traditional <code>root=/dev/sda1</code> style device specification is allowed. If a label is used, as in <code>root=LABEL=rootPart</code> the initrd will search all available devices for a filesystem with the appropriate label, and mount that device as the root filesystem. <code>root=UUID=uuidnumber</code> will mount the partition with that UUID as the root filesystem.</p>
<h3>Standard</h3>
<dl>
<dt><i> init= &quot;&lt;path to real init&gt;&quot;</p>
<dd>the binary to hand over execution to on the root fs after the initramfs scripts are done. </p>
<dt></i><i> root= &quot;&lt;path to blockdevice&gt;&quot;</p>
<dd>the device node to mount as the root file system. The recommended usage is to specify the UUID as followed &quot;root=UUID=xxx&quot;. </p>
<dt></i><i> rootfstype</p>
<dd>set the root file system type. </p>
<dt></i><i> rootdelay</p>
<dd>set delay in seconds. Determines how long mountroot waits for root to appear. The default is 180 seconds. </p>
<dt></i><i> rootflags</p>
<dd>set the file system mount option string. </p>
<dt></i><i> loop= &quot;&lt;path to image&gt;&quot;</p>
<dd>path within the original root file system to loop-mount and use as the real root file system. </p>
<dt></i><i> loopfstype</p>
<dd>set the loop file system type, if applicable. </p>
<dt></i><i> loopflags</p>
<dd>set the loop file system mount option string, if applicable. </p>
<dt></i><i> nfsroot</p>
<dd>can be either &quot;auto&quot; to try to get the relevant information from DHCP or a string of the form NFSSERVER:NFSPATH or NFSSERVER:NFSPATH:NFSOPTS. Use root=/dev/nfs for NFS to kick to in. NFSOPTS can be looked up in <a href="/docs/linux/man/5-nfs/">nfs</a>(5)</i>. </p>
<dt><i> ip</p>
<dd>tells how to configure the ip address. Allows one to specify an different NFS server than the DHCP server. See Documentation/filesystems/nfsroot.txt in any recent Linux source for details. Optional parameter for NFS root. </p>
<dt></i><i> BOOTIF</p>
<dd>is a mac address in pxelinux format with leading &quot;01-&quot; and &quot;-&quot; as separations. pxelinux passes mac address of network card used to PXE boot on with this bootarg. </p>
<dt></i><i> boot</p>
<dd>either local or NFS (affects which initramfs scripts are run, see the &quot;Subdirectories&quot; section under boot scripts). </p>
<dt></i><i> resume</p>
<dd>The resume hook tries to autodetect the resume partition and uses the first swap partition as valid guess. It is possible to set the RESUME variable in /etc/initramfs-tools/conf.d/resume. The boot variable noresume overrides it. </p>
<dt></i><i> resume_offset</p>
<dd>Specify the offset from the partition given by &quot;resume=&quot; at which the swap header of the swap file is located. </p>
<dt></i><i> quiet</p>
<dd>reduces the amount of text output to the console during boot. </p>
<dt></i><i> ro</p>
<dd>mounts the rootfs read-only. </p>
<dt></i><i> rw</p>
<dd>mounts the rootfs read-write. </p>
<dt></i><i> blacklist</p>
<dd>disables load of specific modules. Use blacklist=module1,module2,module3 bootparameter. </p>
</dl>
<p> </i></p>
<h3>Debug</h3>
<dl>
<dt><i> panic</p>
<dd>sets an timeout on panic. panic=&lt;sec&gt; is a documented security feature: it disables the debug shell. </p>
<dt></i><i> debug</p>
<dd>generates lots of output. It writes a log to /run/initramfs/initramfs.debug. Instead when invoked with an arbitrary argument output is written to console. Use for example &quot;debug=vc&quot;. </p>
<dt></i><i> break</p>
<dd>spawns a shell in the initramfs image at the chosen phase (top, modules, premount, mount, mountroot, bottom, init) before actually executing the corresponding scripts (see the &quot;Boot scripts&quot; section) or action. Multiple phases may be specified, delimited by commas. The default, if no phase is specified, is &quot;premount&quot;. Beware that if both &quot;panic&quot; and &quot;break&quot; are present, initramfs will not spawn any shells but reboot instead. </p>
<dt></i><i> netconsole</p>
<dd>loads netconsole linux modules with the chosen args. </p>
<dt></i><i> all_generic_ide</p>
<dd>loads generic IDE/ATA chipset support on boot. </p>
</dl>
<p> </i></p>
<h2>Scripts</h2>
<p>Valid boot and hook scripts names consist solely of alphabetics, numerics, dashes and underscores. Other scripts are discarded.</p>
<h3>Configuration hook scripts</h3>
<p>These are used to override the user configuration where necessary, for example to force use of busybox instead of klibc utilities.</p>
<h3>Hook scripts</h3>
<p>These are used when an initramfs image is created and not included in the image itself. They can however cause files to be included in the image. Hook scripts are executed under errexit. Thus a hook script can abort the mkinitramfs build on possible errors (exitcode != 0).</p>
<h3>Boot scripts</h3>
<p>These are included in the initramfs image and normally executed during kernel boot in the early user-space before the root partition has been mounted.</p>
<h2>Configuration Hook Scripts</h2>
<p>Configuration hook scripts can be found in /usr/share/initramfs-tools/conf-hooks.d. They are sourced by mkinitramfs after the configuration files in /etc and before running any hook scripts. They can override any of the variables documented in <i><a href="/docs/linux/man/5-initramfs-conf/">initramfs.conf</a></i>(5), but this should be done only if absolutely necessary. For example, if a package&#8217;s boot script requires commands not provided by klibc-utils, it should also install a configuration hook that sets <code>BUSYBOX=y</code>.</p>
<h2>Hook Scripts</h2>
<p>Hooks can be found in two places: /usr/share/initramfs-tools/hooks and /etc/initramfs-tools/hooks. They are executed during generation of the initramfs-image and are responsible for including all the necessary components in the image itself. No guarantees are made as to the order in which the different scripts are executed unless the prereqs are setup in the script. Please notice that PREREQ is only honored inside a single directory. So first the scripts in /usr/share/initramfs-tools are ordered according to their PREREQ values and executed. Then all scripts in /etc/initramfs-tools are ordered according to <code>their</code> PREREQ values and executed. This mean that currently there is no possibility to have a local script (/etc/initramfs-tools) get executed before one from the package (/usr/share/initramfs-tools). </p>
<p> If a hook script requires configuration beyond the exported variables listed below, it should read a private configuration file that is separate from the /etc/initramfs-tools directory. It <i>must not</i> read initramfs-tools configuration files directly.</p>
<h3>Header</h3>
<p>In order to support prereqs, each script should begin with the following lines: </p>
<dl>
<dd>
<pre>#!/bin/sh
PREREQ=&quot;&quot;
prereqs()
{
 echo &quot;$PREREQ&quot;
}
case $1 in
prereqs)
 prereqs
 exit 0
 ;;
esac
. /usr/share/initramfs-tools/hook-functions
# Begin real processing below this line</pre>
</dl>
<p> For example, if you are writing a new hook script which relies on lvm, the line starting with PREREQ should be changed to PREREQ=&quot;lvm&quot; which will ensure that the lvm hook script is run before your custom script.</p>
<h3>Help functions</h3>
<p>/usr/share/initramfs-tools/hook-functions contains a number of functions which deal with some common tasks in a hook script:</p>
<dl>
<dt><i></p>
<dd>manual_add_modules adds a module (and any modules which it depends on) to the initramfs image.</p>
<dl>
<dd></i><code>Example:</code> manual_add_modules isofs</dl>
<dt><i></p>
<dd>add_modules_from_file reads a file containing a list of modules (one per line) to be added to the initramfs image. The file can contain comments (lines starting with #) and arguments to the modules by writing the arguments on the same line as the name of the module.</p>
<dl>
<dd></i><code>Example:</code> add_modules_from_file /tmp/modlist</dl>
<dt><i></p>
<dd>force_load adds a module (and its dependencies) to the initramfs image and also unconditionally loads the module during boot. Also supports passing arguments to the module by listing them after the module name.</p>
<dl>
<dd></i><code>Example:</code> force_load cdrom debug=1</dl>
<dt><i></p>
<dd>copy_modules_dir copies an entire module directory from /lib/modules/KERNELVERSION/ into the initramfs image.</p>
<dl>
<dd></i><code>Example:</code> copy_modules_dir kernel/drivers/ata</dl>
</dl>
<h3>Including binaries</h3>
<p>If you need to copy binaries to the initramfs module, a command like this should be used: </p>
<dl>
<dd>copy_exec /sbin/mdadm /sbin</dl>
<p> mkinitramfs will automatically detect which libraries the executable depends on and copy them to the initramfs. This means that most executables, unless compiled with klibc, will automatically include glibc in the image which will increase its size by several hundred kilobytes.</p>
<h3>Including a system firmware preimage (early initramfs)</h3>
<p>If you need to prepend data to the initramfs image, you need to prepare it in a file, and call the <i>prepend_earlyinitramfs</i> function. The file can be disposed of as soon as the function returns. </p>
<p> <code>Example:</code> </p>
<pre>TEMP_FILE=$(mktemp ...)
 ...
prepend_earlyinitramfs ${TEMP_FILE}
rm -f ${TEMP_FILE}</pre>
<h3>Exported variables</h3>
<p>mkinitramfs sets several variables for the hook scripts environment. </p>
<dl>
<dt><i> MODULESDIR</p>
<dd>corresponds to the linux modules dir.</p>
<dt></i><i> version</p>
<dd>is the $(uname -r) linux version against mkinitramfs is run.</p>
<dt></i><i> CONFDIR</p>
<dd>is the path of the used initramfs-tools configurations.</p>
<dt></i><i> DESTDIR</p>
<dd>is the root path of the newly build initramfs.</p>
<dt></i><i> DPKG_ARCH</p>
<dd>allows arch specific hook additions.</p>
<dt></i><i> verbose</p>
<dd>corresponds to the verbosity of the update-initramfs run.</p>
<dt></i><i> BUSYBOX, MODULES</p>
<dd>are as described in <a href="/docs/linux/man/5-initramfs-conf/">initramfs.conf</a></i>(5).</p>
<dt><i> BUSYBOXDIR</p>
<dd>is the directory where busybox utilities should be installed from, or empty if busybox is not being used. </p>
</dl>
<p> </i></p>
<h2>Boot Scripts</h2>
<p>Similarly to hook scripts, boot scripts can be found in two places /usr/share/initramfs-tools/scripts/ and /etc/initramfs-tools/scripts/. There are a number of subdirectories to these two directories which control the boot stage at which the scripts are executed.</p>
<h3>Header</h3>
<p>Like for hook scripts, there are no guarantees as to the order in which the different scripts in one subdirectory (see &quot;Subdirectories&quot; below) are executed. In order to define a certain order, a similar header as for hook scripts should be used: </p>
<dl>
<dd>
<pre>#!/bin/sh
PREREQ=&quot;&quot;
prereqs()
{
 echo &quot;$PREREQ&quot;
}
case $1 in
prereqs)
 prereqs
 exit 0
 ;;
esac</pre>
</dl>
<p> Where PREREQ is modified to list other scripts in the same subdirectory if necessary.</p>
<h3>Help functions</h3>
<p>A number of functions (mostly dealing with output) are provided to boot scripts in <i>/scripts/functions</i> : </p>
<dl>
<dt><i></p>
<dd>log_success_msg Logs a success message</p>
<dl>
<dd></i><code>Example:</code> log_success_msg &quot;Frobnication successful&quot;</dl>
<dt><i></p>
<dd>log_failure_msg Logs a failure message</p>
<dl>
<dd></i><code>Example:</code> log_failure_msg &quot;Frobnication component froobz missing&quot;</dl>
<dt><i></p>
<dd>log_warning_msg Logs a warning message</p>
<dl>
<dd></i><code>Example:</code> log_warning_msg &quot;Only partial frobnication possible&quot;</dl>
<dt><i></p>
<dd>log_begin_msg Logs a message that some processing step has begun </p>
<dt></i><i></p>
<dd>log_end_msg Logs a message that some processing step is finished</p>
<dl>
<dd></i><code>Example:</code> </p>
<dl>
<dd>
<pre>log_begin_msg &quot;Frobnication begun&quot;
# Do something
log_end_msg</pre>
</dl>
</dl>
<dt><i></p>
<dd>panic Logs an error message and executes a shell in the initramfs image to allow the user to investigate the situation.</p>
<dl>
<dd></i><code>Example:</code> panic &quot;Frobnication failed&quot;</dl>
<dt><i></p>
<dd>add_mountroot_fail_hook Registers the script as able to provide possible further information, in the event that the root device cannot be found. See the example script in the initramfs-tools examples directory for more information.</p>
<dl>
<dd></i><code>Example:</code> add_mountroot_fail_hook</dl>
</dl>
<h3>Subdirectories</h3>
<p>Both /usr/share/initramfs-tools/scripts and /etc/initramfs-tools/scripts contains the following subdirectories. </p>
<dl>
<dt><i></p>
<dd>init-top the scripts in this directory are the first scripts to be executed after sysfs and procfs have been mounted. It also runs the udev hook for populating the /dev tree (udev will keep running until init-bottom). </p>
<dt></i><i></p>
<dd>init-premount happens after modules specified by hooks and /etc/initramfs-tools/modules have been loaded. </p>
<dt></i><i></p>
<dd>local-top OR nfs-top After these scripts have been executed, the root device node is expected to be present (local) or the network interface is expected to be usable (NFS). </p>
<dt></i><i></p>
<dd>local-block These scripts are called with the name of a local block device. After these scripts have been executed, that device node should be present. If the local-top or local-block scripts fail to create the wanted device node, the local-block scripts will be called periodically to try again. </p>
<dt></i><i></p>
<dd>local-premount OR nfs-premount are run after the sanity of the root device has been verified (local) or the network interface has been brought up (NFS), but before the actual root fs has been mounted. </p>
<dt></i><i></p>
<dd>local-bottom OR nfs-bottom are run after the rootfs has been mounted (local) or the NFS root share has been mounted. </p>
<dt></i><i></p>
<dd>init-bottom are the last scripts to be executed before procfs and sysfs are moved to the real rootfs and execution is turned over to the init binary which should now be found in the mounted rootfs. udev is stopped. </p>
</dl>
<p> </i></p>
<h3>Boot parameters</h3>
<dl>
<dt><i></p>
<dd>/conf/param.conf allows boot scripts to change exported variables that are listed on top of init. Write the new values to it. It will be sourced after an boot script run if it exists. </p>
</dl>
<p> </i></p>
<h2>Examples</h2>
<h3>Hook script</h3>
<p>An example hook script would look something like this (and would usually be placed in /etc/initramfs-tools/hooks/frobnicate):</p>
<dl>
<dd>
<pre>#!/bin/sh
# Example frobnication hook script
PREREQ=&quot;lvm&quot;
prereqs()
{
 echo &quot;$PREREQ&quot;
}
case $1 in
prereqs)
 prereqs
 exit 0
 ;;
esac
. /usr/share/initramfs-tools/hook-functions
# Begin real processing below this line
if [ ! -x &quot;/sbin/frobnicate&quot; ]; then
 exit 0
fi
force_load frobnicator interval=10
cp /sbin/frobnicate &quot;${DESTDIR}/sbin&quot;
exit 0</pre>
</dl>
<h3>Boot script</h3>
<p>An example boot script would look something like this (and would usually be placed in /etc/initramfs-tools/scripts/local-top/frobnicate):</p>
<dl>
<dd>
<pre>#!/bin/sh
# Example frobnication boot script
PREREQ=&quot;lvm&quot;
prereqs()
{
 echo &quot;$PREREQ&quot;
}
case $1 in
prereqs)
 prereqs
 exit 0
 ;;
esac
. /scripts/functions
# Begin real processing below this line
if [ ! -x &quot;/sbin/frobnicate&quot; ]; then
 panic &quot;Frobnication executable not found&quot;
fi
if [ ! -e &quot;/dev/mapper/frobb&quot; ]; then
 panic &quot;Frobnication device not found&quot;
fi
log_begin_msg &quot;Starting frobnication&quot;
/sbin/frobnicate &quot;/dev/mapper/frobb&quot; || panic &quot;Frobnication failed&quot;
log_end_msg
exit 0</pre>
</dl>
<h3>Exported variables</h3>
<p>init sets several variables for the boot scripts environment.</p>
<dl>
<dt><i> ROOT</p>
<dd>corresponds to the root boot option. Advanced boot scripts like cryptsetup or live-initramfs need to play tricks. Otherwise keep it alone.</p>
<dt></i><i> ROOTDELAY, ROOTFLAGS, ROOTFSTYPE, IP</p>
<dd>corresponds to the rootdelay, rootflags, rootfstype or ip boot option. Use of ROOTDELAY is deprecated; you should implement a local-block</i> boot script rather than delaying or polling.</p>
<dt><i> DPKG_ARCH</p>
<dd>allows arch specific boot actions.</p>
<dt></i><i> blacklist, panic, quiet, resume, noresume, resume_offset</p>
<dd>set according relevant boot option.</p>
<dt></i><i> break</p>
<dd>Useful for manual intervention during setup and coding an boot script.</p>
<dt></i><i> REASON</p>
<dd>Argument passed to the panic</i> helper function. Use to find out why you landed in the initramfs shell.</p>
<dt><i> init</p>
<dd>passes the path to <a href="/docs/linux/man/8-init/">init</a>(8) usually /sbin/init.</p>
<dt></i><i> readonly</p>
<dd>is the default for mounting the root corresponds to the ro bootarg. Overridden by rw bootarg.</p>
<dt></i><i> rootmnt</p>
<dd>is the path where root gets mounted usually /root.</p>
<dt></i><i> debug</p>
<dd>indicates that a debug log is captured for further investigation. </p>
<h2>Kernel Hooks</h2>
<p>initramfs-tools includes hook scripts that are called by kernel packages on installation and removal, so that an initramfs is automatically created, updated or deleted as necessary. The hook scripts do nothing if the environment variable <code>INITRD</code> is set to <code>No</code>. This will be the case for kernel packages built with <code>make deb-pkg</code> and with <code>CONFIG_BLK_DEV_INITRD</code> not set in the kernel config, or built with <code>make-kpkg</code> and not using the <code>&#8211;initrd</code> option.</p>
<h2>Debug</h2>
<p>It is easy to check the generated initramfs for its content. One may need to double-check if it contains the relevant binaries, libs or modules:</p>
<dl>
<dd>
<pre>lsinitramfs /boot/initrd.img-3.16-3-amd64</pre>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/run/initramfs/fsck.log</i></p>
<dd>Log of fsck commands run within the initramfs, with their output.</p>
<dt><i>/run/initramfs/fsck-root</i></p>
<dd>Exists only if fsck ran successfully for the root filesystem.</p>
<dt><i>/run/initramfs/fsck-usr</i></p>
<dd>Exists only if fsck ran successfully for the <i>/usr</i> filesystem. </p>
</dl>
<h2>Author</h2>
<p>The initramfs-tools are written by Maximilian Attems &lt;maks [at] debian.org&gt;, Jeff Bailey &lt;jbailey [at] raspberryginger.com&gt; and numerous others. </p>
<p> This manual was written by David H&auml;rdeman &lt;david [at] hardeman.nu&gt;, updated by Maximilian Attems &lt;maks [at] debian.org&gt;.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-initramfs-conf/">initramfs.conf</a></i>(5), <i><a href="/docs/linux/man/8-mkinitramfs/">mkinitramfs</a></i>(8), <i><a href="/docs/linux/man/8-update-initramfs/">update-initramfs</a></i>(8), <i><a href="/docs/linux/man/8-lsinitramfs/">lsinitramfs</a></i>(8). </p>
