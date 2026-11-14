---
title: "virt-sysprep(1)"
name: "virt-sysprep"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-sysprep/"
description: "virt-sysprep – Reset, unconfigure or customize a virtual machine so clones can be made"
---

<h2 class="name">NAME</h2>
<p> virt-sysprep &#8211; Reset, unconfigure or customize a virtual machine so clones can be made </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - sysprep[--options] - d domname virt - sysprep[--options] - a disk.img[-a disk.img...]
</code></pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;virt-sysprep&quot;</tt> on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently.</p>
<h2>DESCRIPTION</h2>
<p> Virt-sysprep can reset or unconfigure a virtual machine so that clones can be made from it. Steps in this process include removing <font SIZE="-1">SSH</font> host keys, removing persistent network <font SIZE="-1">MAC</font> configuration, and removing user accounts. Virt-sysprep can also customize a virtual machine, for instance by adding <font SIZE="-1">SSH</font> keys, users or logos. Each step can be enabled or disabled as required. </p>
<p> Virt-sysprep modifies the guest or disk image <i>in place</i>. The guest must be shut down. If you want to preserve the existing contents of the guest, <i>you must snapshot, copy or clone the disk first</i>. See &#8220;<font SIZE="-1">COPYING AND CLONING&#8221;</font> below. </p>
<p> You do <i>not</i> need to run virt-sysprep as root. In fact we&#8217;d generally recommend that you don&#8217;t. The time you might want to run it as root is when you need root in order to access the disk image, but even in this case it would be better to change the permissions on the disk image to be writable as the non-root user running virt-sysprep. </p>
<p> &#8220;Sysprep&#8221; stands for &#8220;system preparation&#8221; tool. The name comes from the Microsoft program <i>sysprep.exe</i> which is used to unconfigure Windows machines in preparation for cloning them. Having said that, virt-sysprep does <i>not</i> currently work on Microsoft Windows guests. We plan to support Windows sysprepping in a future version, and we already have code to do it.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>-a</code> file</p>
<dd>
<dt><code>&#8211;add</code> file</p>
<dd> Add <i>file</i> which should be a disk image from a virtual machine. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format</i> option.</p>
<dt><code>-a</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;add</code> <font SIZE="-1">URI</font></p>
<dd> Add a remote disk. The <font SIZE="-1">URI</font> format is compatible with guestfish. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all.</p>
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;dry-run</code></p>
<dd> Perform a read-only &#8220;dry run&#8221; on the guest. This runs the sysprep operation, but throws away any changes to the disk at the end.</p>
<dt><code>&#8211;enable</code> operations</p>
<dd> Choose which sysprep operations to perform. Give a comma-separated list of operations, for example: </p>
<pre>
 --enable ssh-hostkeys,udev-persistent-net
</pre>
<p> would enable <font SIZE="-1">ONLY </font><tt>&quot;ssh-hostkeys&quot;</tt> and <tt>&quot;udev-persistent-net&quot;</tt> operations. </p>
<p> If the <i>&#8211;enable</i> option is not given, then we default to trying most sysprep operations (see <i>&#8211;list-operations</i> to show which are enabled). </p>
<p> Regardless of the <i>&#8211;enable</i> option, sysprep operations are skipped for some guest types. </p>
<p> Use <i>&#8211;list-operations</i> to list operations supported by a particular version of virt-sysprep. </p>
<p> See &#8220;<font SIZE="-1">OPERATIONS&#8221;</font> below for a list and an explanation of each operation.</p>
<dt><code>&#8211;operation</code> operations</p>
<dd>
<dt><code>&#8211;operations</code> operations</p>
<dd> Choose which sysprep operations to perform. Give a comma-separated list of operations, for example: </p>
<pre>
 --operations ssh-hostkeys,udev-persistent-net
</pre>
<p> would enable <font SIZE="-1">ONLY </font><tt>&quot;ssh-hostkeys&quot;</tt> and <tt>&quot;udev-persistent-net&quot;</tt> operations. </p>
<p> <i>&#8211;operations</i> allows you to enable and disable any operation, including the default ones (which would be tried when specifying neither <i>&#8211;operations</i> nor <i>&#8211;enable</i>) and all the available ones; prepending a <tt>&quot;-&quot;</tt> in front of an operation name removes it from the list of enabled operations, while the meta-names <tt>&quot;defaults&quot;</tt> and <tt>&quot;all&quot;</tt> represent respectively the operations enabled by default and all the available ones. For example: </p>
<pre>
 --operations firewall-rules,defaults,-tmp-files
</pre>
<p> would enable the <tt>&quot;firewall-rules&quot;</tt> operation (regardless whether it is enabled by default), all the default ones, and disable the <tt>&quot;tmp-files&quot;</tt> operation. </p>
<p> <i>&#8211;operations</i> can be specified multiple times; the first time the set of enabled operations is empty, while any further <i>&#8211;operations</i> affects the operations enabled so far. </p>
<p> If the <i>&#8211;operations</i> option is not given, then we default to trying most sysprep operations (see <i>&#8211;list-operations</i> to show which are enabled). </p>
<p> Regardless of the <i>&#8211;operations</i> option, sysprep operations are skipped for some guest types. </p>
<p> Use <i>&#8211;list-operations</i> to list operations supported by a particular version of virt-sysprep. </p>
<p> See &#8220;<font SIZE="-1">OPERATIONS&#8221;</font> below for a list and an explanation of each operation.</p>
<dt><code>&#8211;format</code> raw|qcow2|..</p>
<dd>
<dt><code>&#8211;format</code> auto</p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format auto</i> switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 virt-sysprep --format raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-sysprep --format raw -a disk.img --format auto -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>&#8211;list-operations</code></p>
<dd> List the operations supported by the virt-sysprep program. </p>
<p> These are listed one per line, with one or more single-space-separated fields, eg: </p>
<pre>
 $ virt-sysprep --list-operations
 bash-history * Remove the bash history in the guest
 cron-spool * Remove user at-jobs and cron-jobs
 dhcp-client-state * Remove DHCP client leases
 dhcp-server-state * Remove DHCP server leases
 [etc]
</pre>
<p> The first field is the operation name, which can be supplied to <i>&#8211;enable</i>. The second field is a <tt>&quot;*&quot;</tt> character if the operation is enabled by default or blank if not. Subsequent fields on the same line are the description of the operation. </p>
<p> Before libguestfs 1.17.33 only the first (operation name) field was shown and all operations were enabled by default.</p>
<dt><code>&#8211;mount-options</code> mp:opts[;mp:opts;&#8230;]</p>
<dd> Set the mount options used when libguestfs opens the disk image. Note this has no effect on the guest. It is used when opening certain guests such as ones using the <font SIZE="-1">UFS </font>(<font SIZE="-1">BSD</font>) filesystem. </p>
<p> Use a semicolon-separated list of <tt>&quot;mountpoint:options&quot;</tt> pairs. You may need to quote this list to protect it from the shell. </p>
<p> For example: </p>
<pre>
 --mount-options &quot;/:noatime&quot;
</pre>
<p> will mount the root directory with <tt>&quot;notime&quot;</tt>. This example: </p>
<pre>
 --mount-options &quot;/:noatime;/var:rw,nodiratime&quot;
</pre>
<p> will do the same, plus mount <i>/var</i> with <tt>&quot;rw,nodiratime&quot;</tt>.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t print log messages. </p>
<p> To enable detailed logging of individual file operations, use <i>-x</i>.</p>
<dt><code>&#8211;network</code></p>
<dd>
<dt><code>&#8211;no-network</code></p>
<dd> Enable or disable network access from the guest during the installation. </p>
<p> In virt-sysprep, the network is <i>disabled</i> by default. You must use <i>&#8211;network</i> to enable it, in order that options such as <i>&#8211;install</i> or <i>&#8211;update</i> will work. </p>
<p> <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) has more information about the security advantages of disabling the network.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</p>
<dt><code>&#8211;chmod</code> <font SIZE="-1">PERMISSIONS:FILE </font>(see &quot;customize&quot; below)</p>
<dd> Change the permissions of <tt>&quot;FILE&quot;</tt> to <tt>&quot;PERMISSIONS&quot;</tt>. </p>
<p> <i>Note</i>: <tt>&quot;PERMISSIONS&quot;</tt> by default would be decimal, unless you prefix it with <tt>0</tt> to get octal, ie. use <tt>0700</tt> not <tt>700</tt>.</p>
<dt><code>&#8211;commands-from-file</code> <font SIZE="-1">FILENAME </font>(see &quot;customize&quot; below)</p>
<dd> Read the customize commands from a file, one (and its arguments) each line. </p>
<p> Each line contains a single customization command and its arguments, for example: </p>
<pre>
 delete /some/file
 install some-package
 password some-user:password:its-new-password
</pre>
<p> Empty lines are ignored, and lines starting with <tt>&quot;#&quot;</tt> are comments and are ignored as well. Furthermore, arguments can be spread across multiple lines, by adding a <tt>&quot;\&quot;</tt> (continuation character) at the of a line, for example </p>
<pre>
 edit /some/file:\
   s/^OPT=.*/OPT=ok/
</pre>
<p> The commands are handled in the same order as they are in the file, as if they were specified as <i>&#8211;delete /some/file</i> on the command line.</p>
<dt><code>&#8211;copy</code> <font SIZE="-1">SOURCE:DEST </font>(see &quot;customize&quot; below)</p>
<dd> Copy files or directories recursively inside the guest. </p>
<p> Wildcards cannot be used.</p>
<dt><code>&#8211;copy-in</code> <font SIZE="-1">LOCALPATH:REMOTEDIR </font>(see &quot;customize&quot; below)</p>
<dd> Copy local files or directories recursively into the disk image, placing them in the directory <tt>&quot;REMOTEDIR&quot;</tt> (which must exist). </p>
<p> Wildcards cannot be used.</p>
<dt><code>&#8211;delete</code> <font SIZE="-1">PATH </font>(see &quot;customize&quot; below)</p>
<dd> Delete a file from the guest. Or delete a directory (and all its contents, recursively). </p>
<p> You can use shell glob characters in the specified path. Be careful to escape glob characters from the host shell, if that is required. For example: </p>
<pre>
 virt-customize --delete '/var/log/*.log'.
</pre>
<p> See also: <i>&#8211;upload</i>, <i>&#8211;scrub</i>.</p>
<dt><code>&#8211;edit</code> <font SIZE="-1">FILE:EXPR </font>(see &quot;customize&quot; below)</p>
<dd> Edit <tt>&quot;FILE&quot;</tt> using the Perl expression <tt>&quot;EXPR&quot;</tt>. </p>
<p> Be careful to properly quote the expression to prevent it from being altered by the shell. </p>
<p> Note that this option is only available when Perl 5 is installed. </p>
<p> See &#8220;NON-INTERACTIVE <font SIZE="-1">EDITING&#8221;</font> in <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1).</p>
<dt><code>&#8211;firstboot</code> <font SIZE="-1">SCRIPT </font>(see &quot;customize&quot; below)</p>
<dd> Install <tt>&quot;SCRIPT&quot;</tt> inside the guest, so that when the guest first boots up, the script runs (as root, late in the boot process). </p>
<p> The script is automatically chmod +x after installation in the guest. </p>
<p> The alternative version <i>&#8211;firstboot-command</i> is the same, but it conveniently wraps the command up in a single line script for you. </p>
<p> You can have multiple <i>&#8211;firstboot</i> options. They run in the same order that they appear on the command line. </p>
<p> Please take a look at &#8220;<font SIZE="-1">FIRST BOOT SCRIPTS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for more information and caveats about the first boot scripts. </p>
<p> See also <i>&#8211;run</i>.</p>
<dt><code>&#8211;firstboot-command</code> &#8216;<font SIZE="-1">CMD+ARGS</font>&#8216; (see &quot;customize&quot; below)</p>
<dd> Run command (and arguments) inside the guest when the guest first boots up (as root, late in the boot process). </p>
<p> You can have multiple <i>&#8211;firstboot</i> options. They run in the same order that they appear on the command line. </p>
<p> Please take a look at &#8220;<font SIZE="-1">FIRST BOOT SCRIPTS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for more information and caveats about the first boot scripts. </p>
<p> See also <i>&#8211;run</i>.</p>
<dt><code>&#8211;firstboot-install</code> <font SIZE="-1">PKG,PKG.. </font>(see &quot;customize&quot; below)</p>
<dd> Install the named packages (a comma-separated list). These are installed when the guest first boots using the guest&#8217;s package manager (eg. apt, yum, etc.) and the guest&#8217;s network connection. </p>
<p> For an overview on the different ways to install packages, see &#8220;<font SIZE="-1">INSTALLING PACKAGES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1).</p>
<dt><code>&#8211;hostname</code> <font SIZE="-1">HOSTNAME </font>(see &quot;customize&quot; below)</p>
<dd> Set the hostname of the guest to <tt>&quot;HOSTNAME&quot;</tt>. You can use a dotted hostname.domainname (<font SIZE="-1">FQDN</font>) if you want.</p>
<dt><code>&#8211;install</code> <font SIZE="-1">PKG,PKG.. </font>(see &quot;customize&quot; below)</p>
<dd> Install the named packages (a comma-separated list). These are installed during the image build using the guest&#8217;s package manager (eg. apt, yum, etc.) and the host&#8217;s network connection. </p>
<p> For an overview on the different ways to install packages, see &#8220;<font SIZE="-1">INSTALLING PACKAGES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1). </p>
<p> See also <i>&#8211;update</i>, <i>&#8211;uninstall</i>.</p>
<dt><code>&#8211;keep-user-accounts</code> <font SIZE="-1">USERS </font>(see &quot;user-account&quot; below)</p>
<dd> The user accounts to be kept in the guest. The value of this option is a list of user names separated by comma, where specifying an user means it is going to be kept. For example: </p>
<pre>
 --keep-user-accounts mary
</pre>
<p> would keep the user account <tt>&quot;mary&quot;</tt>. </p>
<p> This option can be specified multiple times.</p>
<dt><code>&#8211;link</code> TARGET:LINK[:LINK..] (see &quot;customize&quot; below)</p>
<dd> Create symbolic link(s) in the guest, starting at <tt>&quot;LINK&quot;</tt> and pointing at <tt>&quot;TARGET&quot;</tt>.</p>
<dt><code>&#8211;mkdir</code> <font SIZE="-1">DIR </font>(see &quot;customize&quot; below)</p>
<dd> Create a directory in the guest. </p>
<p> This uses <tt>&quot;mkdir -p&quot;</tt> so any intermediate directories are created, and it also works if the directory already exists.</p>
<dt><code>&#8211;move</code> <font SIZE="-1">SOURCE:DEST </font>(see &quot;customize&quot; below)</p>
<dd> Move files or directories inside the guest. </p>
<p> Wildcards cannot be used.</p>
<dt><code>&#8211;no-logfile</code> (see &quot;customize&quot; below)</p>
<dd> Scrub <tt>&quot;builder.log&quot;</tt> (log file from build commands) from the image after building is complete. If you don&#8217;t want to reveal precisely how the image was built, use this option. </p>
<p> See also: &#8220;<font SIZE="-1">LOG FILE&#8221;</font>.</p>
<dt><code>&#8211;password</code> <font SIZE="-1">USER:SELECTOR </font>(see &quot;customize&quot; below)</p>
<dd> Set the password for <tt>&quot;USER&quot;</tt>. (Note this option does <i>not</i> create the user account). </p>
<p> See &#8220;<font SIZE="-1">USERS AND PASSWORDS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field, and also how to set up user accounts.</p>
<dt><code>&#8211;password-crypto</code> md5|sha256|sha512 (see &quot;customize&quot; below)</p>
<dd> When the virt tools change or set a password in the guest, this option sets the password encryption of that password to <tt>&quot;md5&quot;</tt>, <tt>&quot;sha256&quot;</tt> or <tt>&quot;sha512&quot;</tt>. </p>
<p> <tt>&quot;sha256&quot;</tt> and <tt>&quot;sha512&quot;</tt> require glibc ≥ 2.7 (check <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3) inside the guest). </p>
<p> <tt>&quot;md5&quot;</tt> will work with relatively old Linux guests (eg. <font SIZE="-1">RHEL 3</font>), but is not secure against modern attacks. </p>
<p> The default is <tt>&quot;sha512&quot;</tt> unless libguestfs detects an old guest that didn&#8217;t have support for <font SIZE="-1">SHA-512,</font> in which case it will use <tt>&quot;md5&quot;</tt>. You can override libguestfs by specifying this option. </p>
<p> Note this does not change the default password encryption used by the guest when you create new user accounts inside the guest. If you want to do that, then you should use the <i>&#8211;edit</i> option to modify <tt>&quot;/etc/sysconfig/authconfig&quot;</tt> (Fedora, <font SIZE="-1">RHEL</font>) or <tt>&quot;/etc/pam.d/common-password&quot;</tt> (Debian, Ubuntu).</p>
<dt><code>&#8211;remove-user-accounts</code> <font SIZE="-1">USERS </font>(see &quot;user-account&quot; below)</p>
<dd> The user accounts to be removed from the guest. The value of this option is a list of user names separated by comma, where specifying an user means it is going to be removed. For example: </p>
<pre>
 --remove-user-accounts bob,eve
</pre>
<p> would only remove the user accounts <tt>&quot;bob&quot;</tt> and <tt>&quot;eve&quot;</tt>. </p>
<p> This option can be specified multiple times.</p>
<dt><code>&#8211;root-password</code> <font SIZE="-1">SELECTOR </font>(see &quot;customize&quot; below)</p>
<dd> Set the root password. </p>
<p> See &#8220;<font SIZE="-1">USERS AND PASSWORDS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field, and also how to set up user accounts. </p>
<p> Note: In virt-builder, if you <i>don&#8217;t</i> set <i>&#8211;root-password</i> then the guest is given a <i>random</i> root password.</p>
<dt><code>&#8211;run</code> <font SIZE="-1">SCRIPT </font>(see &quot;customize&quot; below)</p>
<dd> Run the shell script (or any program) called <tt>&quot;SCRIPT&quot;</tt> on the disk image. The script runs virtualized inside a small appliance, chrooted into the guest filesystem. </p>
<p> The script is automatically chmod +x. </p>
<p> If libguestfs supports it then a limited network connection is available but it only allows outgoing network connections. You can also attach data disks (eg. <font SIZE="-1">ISO</font> files) as another way to provide data (eg. software packages) to the script without needing a network connection (<i>&#8211;attach</i>). You can also upload data files (<i>&#8211;upload</i>). </p>
<p> You can have multiple <i>&#8211;run</i> options. They run in the same order that they appear on the command line. </p>
<p> See also: <i>&#8211;firstboot</i>, <i>&#8211;attach</i>, <i>&#8211;upload</i>.</p>
<dt><code>&#8211;run-command</code> &#8216;<font SIZE="-1">CMD+ARGS</font>&#8216; (see &quot;customize&quot; below)</p>
<dd> Run the command and arguments on the disk image. The command runs virtualized inside a small appliance, chrooted into the guest filesystem. </p>
<p> If libguestfs supports it then a limited network connection is available but it only allows outgoing network connections. You can also attach data disks (eg. <font SIZE="-1">ISO</font> files) as another way to provide data (eg. software packages) to the script without needing a network connection (<i>&#8211;attach</i>). You can also upload data files (<i>&#8211;upload</i>). </p>
<p> You can have multiple <i>&#8211;run-command</i> options. They run in the same order that they appear on the command line. </p>
<p> See also: <i>&#8211;firstboot</i>, <i>&#8211;attach</i>, <i>&#8211;upload</i>.</p>
<dt><code>&#8211;script</code> <font SIZE="-1">SCRIPT </font>(see &quot;script&quot; below)</p>
<dd> Run the named <tt>&quot;SCRIPT&quot;</tt> (a shell script or program) against the guest. The script can be any program on the host. The script&#8217;s current directory will be the guest&#8217;s root directory. </p>
<p> <code>Note:</code> If the script is not on the <tt>$PATH</tt>, then you must give the full absolute path to the script.</p>
<dt><code>&#8211;scriptdir</code> <font SIZE="-1">SCRIPTDIR </font>(see &quot;script&quot; below)</p>
<dd> The mount point (an empty directory on the host) used when the <tt>&quot;script&quot;</tt> operation is enabled and one or more scripts are specified using <i>&#8211;script</i> parameter(s). </p>
<p> <code>Note:</code> <tt>&quot;SCRIPTDIR&quot;</tt> <code>must</code> be an absolute path. </p>
<p> If <i>&#8211;scriptdir</i> is not specified then a temporary mountpoint will be created.</p>
<dt><code>&#8211;scrub</code> <font SIZE="-1">FILE </font>(see &quot;customize&quot; below)</p>
<dd> Scrub a file from the guest. This is like <i>&#8211;delete</i> except that:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> It scrubs the data so a guest could not recover it.</p>
<dt>&bull;</p>
<dd> It cannot delete directories, only regular files.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;selinux-relabel</code> (see &quot;customize&quot; below)</p>
<dd> Relabel files in the guest so that they have the correct SELinux label. </p>
<p> This will attempt to relabel files immediately, but if the operation fails this will instead touch <i>/.autorelabel</i> on the image to schedule a relabel operation for the next time the image boots. </p>
<p> You should only use this option for guests which support SELinux.</p>
<dt><code>&#8211;sm-attach</code> <font SIZE="-1">SELECTOR </font>(see &quot;customize&quot; below)</p>
<dd> Attach to a pool using <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> See &#8220;SUBSCRIPTION-MANAGER&#8221; in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field.</p>
<dt><code>&#8211;sm-credentials</code> <font SIZE="-1">SELECTOR </font>(see &quot;customize&quot; below)</p>
<dd> Set the credentials for <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> See &#8220;SUBSCRIPTION-MANAGER&#8221; in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field.</p>
<dt><code>&#8211;sm-register</code> (see &quot;customize&quot; below)</p>
<dd> Register the guest using <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> This requires credentials being set using <i>&#8211;sm-credentials</i>.</p>
<dt><code>&#8211;sm-remove</code> (see &quot;customize&quot; below)</p>
<dd> Remove all the subscriptions from the guest using <tt>&quot;subscription-manager&quot;</tt>.</p>
<dt><code>&#8211;sm-unregister</code> (see &quot;customize&quot; below)</p>
<dd> Unregister the guest using <tt>&quot;subscription-manager&quot;</tt>.</p>
<dt><code>&#8211;ssh-inject</code> USER[:SELECTOR] (see &quot;customize&quot; below)</p>
<dd> Inject an ssh key so the given <tt>&quot;USER&quot;</tt> will be able to log in over ssh without supplying a password. The <tt>&quot;USER&quot;</tt> must exist already in the guest. </p>
<p> See &#8220;<font SIZE="-1">SSH KEYS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field. </p>
<p> You can have multiple <i>&#8211;ssh-inject</i> options, for different users and also for more keys for each user.</p>
<dt><code>&#8211;timezone</code> <font SIZE="-1">TIMEZONE </font>(see &quot;customize&quot; below)</p>
<dd> Set the default timezone of the guest to <tt>&quot;TIMEZONE&quot;</tt>. Use a location string like <tt>&quot;Europe/London&quot;</tt></p>
<dt><code>&#8211;touch</code> <font SIZE="-1">FILE </font>(see &quot;customize&quot; below)</p>
<dd> This command performs a <i><a href="/docs/linux/man/1-touch/">touch</a></i>(1)-like operation on <tt>&quot;FILE&quot;</tt>.</p>
<dt><code>&#8211;truncate</code> <font SIZE="-1">FILE </font>(see &quot;customize&quot; below)</p>
<dd> This command truncates <tt>&quot;FILE&quot;</tt> to a zero-length file. The file must exist already.</p>
<dt><code>&#8211;truncate-recursive</code> <font SIZE="-1">PATH </font>(see &quot;customize&quot; below)</p>
<dd> This command recursively truncates all files under <tt>&quot;PATH&quot;</tt> to zero-length.</p>
<dt><code>&#8211;uninstall</code> <font SIZE="-1">PKG,PKG.. </font>(see &quot;customize&quot; below)</p>
<dd> Uninstall the named packages (a comma-separated list). These are removed during the image build using the guest&#8217;s package manager (eg. apt, yum, etc.). Dependent packages may also need to be uninstalled to satisfy the request. </p>
<p> See also <i>&#8211;install</i>, <i>&#8211;update</i>.</p>
<dt><code>&#8211;update</code> (see &quot;customize&quot; below)</p>
<dd> Do the equivalent of <tt>&quot;yum update&quot;</tt>, <tt>&quot;apt-get upgrade&quot;</tt>, or whatever command is required to update the packages already installed in the template to their latest versions. </p>
<p> See also <i>&#8211;install</i>, <i>&#8211;uninstall</i>.</p>
<dt><code>&#8211;upload</code> <font SIZE="-1">FILE:DEST </font>(see &quot;customize&quot; below)</p>
<dd> Upload local file <tt>&quot;FILE&quot;</tt> to destination <tt>&quot;DEST&quot;</tt> in the disk image. File owner and permissions from the original are preserved, so you should set them to what you want them to be in the disk image. </p>
<p> <tt>&quot;DEST&quot;</tt> could be the final filename. This can be used to rename the file on upload. </p>
<p> If <tt>&quot;DEST&quot;</tt> is a directory name (which must already exist in the guest) then the file is uploaded into that directory, and it keeps the same name as on the local filesystem. </p>
<p> See also: <i>&#8211;mkdir</i>, <i>&#8211;delete</i>, <i>&#8211;scrub</i>.</p>
<dt><code>&#8211;write</code> <font SIZE="-1">FILE:CONTENT </font>(see &quot;customize&quot; below)</p>
<dd> Write <tt>&quot;CONTENT&quot;</tt> to <tt>&quot;FILE&quot;</tt>.</dl>
<h2>OPERATIONS</h2>
<p> If the <i>&#8211;enable</i>/<i>&#8211;operations</i> option is <i>not</i> given, then most sysprep operations are enabled. </p>
<p> Use <tt>&quot;virt-sysprep --list-operations&quot;</tt> to list all operations for your virt-sysprep binary. The ones which are enabled by default are marked with a <tt>&quot;*&quot;</tt> character. Regardless of the <i>&#8211;enable</i>/<i>&#8211;operations</i> options, sysprep operations are skipped for some guest types. </p>
<p> Operations can be individually enabled using the <i>&#8211;enable</i>/<i>&#8211;operations</i> options. Use a comma-separated list, for example: </p>
<pre>
 virt-sysprep --operations ssh-hostkeys,udev-persistent-net [etc..]
</pre>
<p> Future versions of virt-sysprep may add more operations. If you are using virt-sysprep and want predictable behaviour, specify only the operations that you want to have enabled. </p>
<p> <tt>&quot;*&quot;</tt> = enabled by default when no <i>&#8211;enable</i>/<i>&#8211;operations</i> option is given.</p>
<h3><code>abrt-data</code> *</h3>
<p> Remove the crash data generated by <font SIZE="-1">ABRT.</font> </p>
<p> Remove the automatically generated <font SIZE="-1">ABRT</font> crash data in <tt>&quot;/var/spool/abrt/&quot;</tt>.</p>
<h3><code>bash-history</code> *</h3>
<p> Remove the bash history in the guest. </p>
<p> Remove the bash history of user &#8220;root&#8221; and any other users who have a <tt>&quot;.bash_history&quot;</tt> file in their home directory. </p>
<p> <i>Notes on bash-history</i> </p>
<p> Currently this only looks in <tt>&quot;/root&quot;</tt> and <tt>&quot;/home/*&quot;</tt> for home directories, so users with home directories in other locations won&#8217;t have the bash history removed.</p>
<h3><code>blkid-tab</code> *</h3>
<p> Remove blkid tab in the guest.</p>
<h3><code>ca-certificates</code></h3>
<p> Remove <font SIZE="-1">CA</font> certificates in the guest.</p>
<h3><code>crash-data</code> *</h3>
<p> Remove the crash data generated by kexec-tools. </p>
<p> Remove the automatically generated kdump kernel crash data.</p>
<h3><code>cron-spool</code> *</h3>
<p> Remove user at-jobs and cron-jobs.</p>
<h3><code>customize</code> *</h3>
<p> Customize the guest. </p>
<p> Customize the guest by providing <i><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></i>(1) options for installing packages, editing files and so on.</p>
<h3><code>dhcp-client-state</code> *</h3>
<p> Remove <font SIZE="-1">DHCP</font> client leases.</p>
<h3><code>dhcp-server-state</code> *</h3>
<p> Remove <font SIZE="-1">DHCP</font> server leases.</p>
<h3><code>dovecot-data</code> *</h3>
<p> Remove Dovecot (mail server) data.</p>
<h3><code>firewall-rules</code></h3>
<p> Remove the firewall rules. </p>
<p> This removes custom firewall rules by removing <tt>&quot;/etc/sysconfig/iptables&quot;</tt> or custom firewalld configuration in <tt>&quot;/etc/firewalld/*/*&quot;</tt>. </p>
<p> Note this is <i>not</i> enabled by default since it may expose guests to exploits. Use with care.</p>
<h3><code>flag-reconfiguration</code></h3>
<p> Flag the system for reconfiguration. </p>
<p> For Linux guests, this touches <tt>&quot;/.unconfigured&quot;</tt>, which causes the first boot to interactively query the user for settings such as the root password and timezone.</p>
<h3><code>fs-uuids</code></h3>
<p> Change filesystem UUIDs. </p>
<p> On guests and filesystem types where this is supported, new random UUIDs are generated and assigned to filesystems. </p>
<p> <i>Notes on fs-uuids</i> </p>
<p> The fs-uuids operation is disabled by default because it does not yet find and update all the places in the guest that use the UUIDs. For example <tt>&quot;/etc/fstab&quot;</tt> or the bootloader. Enabling this operation is more likely than not to make your guest unbootable. </p>
<p> See: <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=991641">https://bugzilla.redhat.com/show_bug.cgi?id=991641</a></p>
<h3><code>kerberos-data</code></h3>
<p> Remove Kerberos data in the guest.</p>
<h3><code>logfiles</code> *</h3>
<p> Remove many log files from the guest. </p>
<p> On Linux the following files are removed: </p>
<pre>
 /etc/Pegasus/*.cnf
 /etc/Pegasus/*.crt
 /etc/Pegasus/*.csr
 /etc/Pegasus/*.pem
 /etc/Pegasus/*.srl
 /root/anaconda-ks.cfg
 /root/anaconda-post.log
 /root/initial-setup-ks.cfg
 /root/install.log
 /root/install.log.syslog
 /var/cache/fontconfig/*
 /var/cache/gdm/*
 /var/cache/man/*
 /var/lib/AccountService/users/*
 /var/lib/fprint/*
 /var/lib/logrotate.status
 /var/log/*.log*
 /var/log/BackupPC/LOG
 /var/log/ConsoleKit/*
 /var/log/anaconda.syslog
 /var/log/anaconda/*
 /var/log/apache2/*_log
 /var/log/apache2/*_log-*
 /var/log/apt/*
 /var/log/aptitude*
 /var/log/audit/*
 /var/log/btmp*
 /var/log/ceph/*.log
 /var/log/chrony/*.log
 /var/log/cron*
 /var/log/cups/*_log*
 /var/log/debug*
 /var/log/dmesg*
 /var/log/exim4/*
 /var/log/faillog*
 /var/log/firewalld*
 /var/log/gdm/*
 /var/log/glusterfs/*glusterd.vol.log
 /var/log/glusterfs/glusterfs.log
 /var/log/grubby*
 /var/log/httpd/*log
 /var/log/installer/*
 /var/log/jetty/jetty-console.log
 /var/log/journal/*
 /var/log/lastlog*
 /var/log/libvirt/libvirtd.log
 /var/log/libvirt/libxl/*.log
 /var/log/libvirt/lxc/*.log
 /var/log/libvirt/qemu/*.log
 /var/log/libvirt/uml/*.log
 /var/log/lightdm/*
 /var/log/mail/*
 /var/log/maillog*
 /var/log/messages*
 /var/log/ntp
 /var/log/ntpstats/*
 /var/log/ppp/connect-errors
 /var/log/rhsm/*
 /var/log/sa/*
 /var/log/secure*
 /var/log/setroubleshoot/*.log
 /var/log/spooler*
 /var/log/squid/*.log
 /var/log/syslog*
 /var/log/tallylog*
 /var/log/tuned/tuned.log
 /var/log/wtmp*
 /var/log/xferlog*
 /var/named/data/named.run
</pre>
<h3><code>lvm-uuids</code> *</h3>
<p> Change <font SIZE="-1">LVM2 PV</font> and <font SIZE="-1">VG</font> UUIDs. </p>
<p> On Linux guests that have <font SIZE="-1">LVM2</font> physical volumes (PVs) or volume groups (VGs), new random UUIDs are generated and assigned to those PVs and VGs.</p>
<h3><code>machine-id</code> *</h3>
<p> Remove the local machine <font SIZE="-1">ID.</font> </p>
<p> The machine <font SIZE="-1">ID</font> is usually generated from a random source during system installation and stays constant for all subsequent boots. Optionally, for stateless systems it is generated during runtime at boot if it is found to be empty.</p>
<h3><code>mail-spool</code> *</h3>
<p> Remove email from the local mail spool directory.</p>
<h3><code>net-hostname</code> *</h3>
<p> Remove <font SIZE="-1">HOSTNAME</font> in network interface configuration. </p>
<p> For Fedora and Red Hat Enterprise Linux, this is removed from <tt>&quot;ifcfg-*&quot;</tt> files.</p>
<h3><code>net-hwaddr</code> *</h3>
<p> Remove <font SIZE="-1">HWADDR </font>(hard-coded <font SIZE="-1">MAC</font> address) configuration. </p>
<p> For Fedora and Red Hat Enterprise Linux, this is removed from <tt>&quot;ifcfg-*&quot;</tt> files.</p>
<h3><code>pacct-log</code> *</h3>
<p> Remove the process accounting log files. </p>
<p> The system wide process accounting will store to the pacct log files if the process accounting is on.</p>
<h3><code>package-manager-cache</code> *</h3>
<p> Remove package manager cache.</p>
<h3><code>pam-data</code> *</h3>
<p> Remove the <font SIZE="-1">PAM</font> data in the guest.</p>
<h3><code>puppet-data-log</code> *</h3>
<p> Remove the data and log files of puppet.</p>
<h3><code>rh-subscription-manager</code> *</h3>
<p> Remove the <font SIZE="-1">RH</font> subscription manager files.</p>
<h3><code>rhn-systemid</code> *</h3>
<p> Remove the <font SIZE="-1">RHN</font> system <font SIZE="-1">ID.</font></p>
<h3><code>rpm-db</code> *</h3>
<p> Remove host-specific <font SIZE="-1">RPM</font> database files. </p>
<p> Remove host-specific <font SIZE="-1">RPM</font> database files and locks. <font SIZE="-1">RPM</font> will recreate these files automatically if needed.</p>
<h3><code>samba-db-log</code> *</h3>
<p> Remove the database and log files of Samba.</p>
<h3><code>script</code> *</h3>
<p> Run arbitrary scripts against the guest. </p>
<p> The <tt>&quot;script&quot;</tt> module lets you run arbitrary shell scripts or programs against the guest. </p>
<p> Note this feature requires <font SIZE="-1">FUSE</font> support. You may have to enable this in your host, for example by adding the current user to the <tt>&quot;fuse&quot;</tt> group, or by loading a kernel module. </p>
<p> Use one or more <i>&#8211;script</i> parameters to specify scripts or programs that will be run against the guest. </p>
<p> The script or program is run with its current directory being the guest&#8217;s root directory, so relative paths should be used. For example: <tt>&quot;rm etc/resolv.conf&quot;</tt> in the script would remove a Linux guest&#8217;s <font SIZE="-1">DNS</font> configuration file, but <tt>&quot;rm /etc/resolv.conf&quot;</tt> would (try to) remove the host&#8217;s file. </p>
<p> Normally a temporary mount point for the guest is used, but you can choose a specific one by using the <i>&#8211;scriptdir</i> parameter. </p>
<p> <code>Note:</code> This is different from <i>&#8211;firstboot</i> scripts (which run in the context of the guest when it is booting first time). <i>&#8211;script</i> scripts run on the host, not in the guest.</p>
<h3><code>smolt-uuid</code> *</h3>
<p> Remove the Smolt hardware <font SIZE="-1">UUID.</font></p>
<h3><code>ssh-hostkeys</code> *</h3>
<p> Remove the <font SIZE="-1">SSH</font> host keys in the guest. </p>
<p> The <font SIZE="-1">SSH</font> host keys are regenerated (differently) next time the guest is booted. </p>
<p> If, after cloning, the guest gets the same <font SIZE="-1">IP</font> address, ssh will give you a stark warning about the host key changing: </p>
<pre>
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
</pre>
<h3><code>ssh-userdir</code> *</h3>
<p> Remove &#8220;.ssh&#8221; directories in the guest. </p>
<p> Remove the <tt>&quot;.ssh&quot;</tt> directory of user &#8220;root&#8221; and any other users who have a <tt>&quot;.ssh&quot;</tt> directory in their home directory. </p>
<p> <i>Notes on ssh-userdir</i> </p>
<p> Currently this only looks in <tt>&quot;/root&quot;</tt> and <tt>&quot;/home/*&quot;</tt> for home directories, so users with home directories in other locations won&#8217;t have the ssh files removed.</p>
<h3><code>sssd-db-log</code> *</h3>
<p> Remove the database and log files of sssd.</p>
<h3><code>tmp-files</code> *</h3>
<p> Remove temporary files. </p>
<p> This removes temporary files under <tt>&quot;/tmp&quot;</tt> and <tt>&quot;/var/tmp&quot;</tt>.</p>
<h3><code>udev-persistent-net</code> *</h3>
<p> Remove udev persistent net rules. </p>
<p> Remove udev persistent net rules which map the guest&#8217;s existing <font SIZE="-1">MAC</font> address to a fixed ethernet device (eg. eth0). </p>
<p> After a guest is cloned, the <font SIZE="-1">MAC</font> address usually changes. Since the old <font SIZE="-1">MAC</font> address occupies the old name (eg. eth0), this means the fresh <font SIZE="-1">MAC</font> address is assigned to a new name (eg. eth1) and this is usually undesirable. Erasing the udev persistent net rules avoids this.</p>
<h3><code>user-account</code></h3>
<p> Remove the user accounts in the guest. </p>
<p> By default remove all the user accounts and their home directories. The &#8220;root&#8221; account is not removed. </p>
<p> See the <i>&#8211;remove-user-accounts</i> parameter for a way to specify how to remove only some users, or to not remove some others.</p>
<h3><code>utmp</code> *</h3>
<p> Remove the utmp file. </p>
<p> This file records who is currently logged in on a machine. In modern Linux distros it is stored in a ramdisk and hence not part of the virtual machine&#8217;s disk, but it was stored on disk in older distros.</p>
<h3><code>yum-uuid</code> *</h3>
<p> Remove the yum <font SIZE="-1">UUID.</font> </p>
<p> Yum creates a fresh <font SIZE="-1">UUID</font> the next time it runs when it notices that the original <font SIZE="-1">UUID</font> has been erased.</p>
<h2>COPYING AND CLONING</h2>
<p> Virt-sysprep can be used as part of a process of cloning guests, or to prepare a template from which guests can be cloned. There are many different ways to achieve this using the virt tools, and this section is just an introduction. </p>
<p> A virtual machine (when switched off) consists of two parts:</p>
<dl>
<dt><i>configuration</i></p>
<dd> The configuration or description of the guest. eg. The libvirt <font SIZE="-1">XML </font>(see <tt>&quot;virsh dumpxml&quot;</tt>), the running configuration of the guest, or another external format like <font SIZE="-1">OVF.</font> </p>
<p> Some configuration items that might need to be changed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> name</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">UUID</font></p>
<dt>&bull;</p>
<dd> path to block device(s)</p>
<dt>&bull;</p>
<dd> network card <font SIZE="-1">MAC</font> address</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><i>block device(s)</i></p>
<dd> One or more hard disk images, themselves containing files, directories, applications, kernels, configuration, etc. </p>
<p> Some things inside the block devices that might need to be changed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> hostname and other net configuration</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">UUID</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">SSH</font> host keys</p>
<dt>&bull;</p>
<dd> Windows unique security <font SIZE="-1">ID </font>(<font SIZE="-1">SID</font>)</p>
<dt>&bull;</p>
<dd> Puppet registration</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3><font SIZE="-1">COPYING THE BLOCK DEVICE</font></h3>
<p> Starting with an original guest, you probably wish to copy the guest block device and its configuration to make a template. Then once you are happy with the template, you will want to make many clones from it. </p>
<p>virt &#8211; sysprep |<br />
    v<br />
            original guest&#8211; &#8212; &#8212; &#8212; &gt; template &#8212; &#8212; &#8212; &#8212; &#8212; &gt;<br />
                                      \&#8211; &#8212; &#8212; &gt; cloned<br />
                                       \&#8211; &#8212;&gt;guests<br />
                                        \&#8211; &#8212; &gt;</p>
<p> You can, of course, just copy the block device on the host using <i><a href="/docs/linux/man/1-cp/">cp</a></i>(1) or <i><a href="/docs/linux/man/1-dd/">dd</a></i>(1). </p>
<p>dd dd<br />
        original guest&#8211; &#8212; &#8212; &#8212; &gt; template &#8212; &#8212; &#8212; &#8212; &#8212; &gt;<br />
                                      \&#8211; &#8212; &#8212; &gt; cloned<br />
                                       \&#8211; &#8212;&gt;guests<br />
                                        \&#8211; &#8212; &gt;</p>
<p> There are some smarter (and faster) ways too: </p>
<p>snapshot template &#8212; &#8212; &#8212; &#8212; &#8212; &gt;<br />
                            \&#8211; &#8212; &#8212; &gt; cloned<br />
                             \&#8211; &#8212;&gt;guests<br />
                              \&#8211; &#8212; &gt;</p>
<p> You may want to run virt-sysprep twice, once to reset the guest (to make a template) and a second time to customize the guest for a specific user: </p>
<p>virt &#8211; sysprep virt &#8211; sysprep(reset)(add user, keys, logos) | |<br />
    dd v dd v<br />
        original guest&#8211; &#8212; &gt; template &#8212; &#8212; &#8212; &#8212;&gt;copied&#8211; &#8212; &#8212; &gt; custom<br />
        template guest</p>
<dl>
<dt>&bull;</p>
<dd> Create a snapshot using qemu-img: </p>
<pre>
 qemu-img create -f qcow2 -o backing_file=original snapshot.qcow
</pre>
<p> The advantage is that you don&#8217;t need to copy the original (very fast) and only changes are stored (less storage required). </p>
<p> Note that writing to the backing file once you have created guests on top of it is not possible: you will corrupt the guests.</p>
<dt>&bull;</p>
<dd> Create a snapshot using <tt>&quot;lvcreate --snapshot&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Other ways to create snapshots include using filesystems-level tools (for filesystems such as btrfs). </p>
<p> Most Network Attached Storage (<font SIZE="-1">NAS</font>) devices can also create cheap snapshots from files or LUNs.</p>
<dt>&bull;</p>
<dd> Get your <font SIZE="-1">NAS</font> to duplicate the <font SIZE="-1">LUN. </font> Most <font SIZE="-1">NAS</font> devices can also duplicate LUNs very cheaply (they copy them on-demand in the background).</p>
<dt>&bull;</p>
<dd> Prepare your template using <i><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></i>(1). See below.</dl>
<h3>VIRT-CLONE</h3>
<p> A separate tool, <i><a href="/docs/linux/man/1-virt-clone/">virt-clone</a></i>(1), can be used to duplicate the block device and/or modify the external libvirt configuration of a guest. It will reset the name, <font SIZE="-1">UUID</font> and <font SIZE="-1">MAC</font> address of the guest in the libvirt <font SIZE="-1">XML.</font> </p>
<p> <i><a href="/docs/linux/man/1-virt-clone/">virt-clone</a></i>(1) does not use libguestfs and cannot look inside the disk image. This was the original motivation to write virt-sysprep.</p>
<h3><font SIZE="-1">SPARSIFY</font></h3>
<p>virt &#8211; sparsify<br />
            original guest&#8211; &#8212; &#8212; &#8212; &gt;<br />
    template</p>
<p> <i><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></i>(1) can be used to make the cloning template smaller, making it easier to compress and/or faster to copy. </p>
<p> Notice that since virt-sparsify also copies the image, you can use it to make the initial copy (instead of <tt>&quot;dd&quot;</tt>).</p>
<h3><font SIZE="-1">RESIZE</font></h3>
<pre><code>
virt - resize template -- -- -- -- -- &gt;
                            \-- -- -- &gt; cloned
                             \-- ---&gt;guests
                              \-- -- &gt;
</code></pre>
<p> If you want to give people cloned guests, but let them pick the size of the guest themselves (eg. depending on how much they are prepared to pay for disk space), then instead of copying the template, you can run <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1). Virt-resize performs a copy and resize, and thus is ideal for cloning guests from a template.</p>
<h2>FIRSTBOOT VS SCRIPT</h2>
<p> The two options <i>&#8211;firstboot</i> and <i>&#8211;script</i> both supply shell scripts that are run against the guest. However these two options are significantly different. </p>
<p> <i>&#8211;firstboot script</i> uploads the file <tt>&quot;script&quot;</tt> into the guest and arranges that it will run, in the guest, when the guest is next booted. (The script will only run once, at the &#8220;first boot&#8221;). </p>
<p> <i>&#8211;script script</i> runs the shell <tt>&quot;script&quot;</tt> <i>on the host</i>, with its current directory inside the guest filesystem. </p>
<p> If you needed, for example, to <tt>&quot;yum install&quot;</tt> new packages, then you <i>must not</i> use <i>&#8211;script</i> for this, since that would (a) run the <tt>&quot;yum&quot;</tt> command on the host and (b) wouldn&#8217;t have access to the same resources (repositories, keys, etc.) as the guest. Any command that needs to run on the guest <i>must</i> be run via <i>&#8211;firstboot</i>. </p>
<p> On the other hand if you need to make adjustments to the guest filesystem (eg. copying in files), then <i>&#8211;script</i> is ideal since (a) it has access to the host filesystem and (b) you will get immediate feedback on errors. </p>
<p> Either or both options can be used multiple times on the command line.</p>
<h2>SECURITY</h2>
<p> Although virt-sysprep removes some sensitive information from the guest, it does not pretend to remove all of it. You should examine the &#8220;<font SIZE="-1">OPERATIONS&#8221;</font> above and the guest afterwards. </p>
<p> Sensitive files are simply removed. The data they contained may still exist on the disk, easily recovered with a hex editor or undelete tool. The <i>&#8211;scrub</i> option can be used to scrub files instead of just deleting them. <i><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></i>(1) is another way to remove this content. See also the <i><a href="/docs/linux/man/1-scrub/">scrub</a></i>(1) command to get rid of deleted content in directory entries and inodes.</p>
<h3><font SIZE="-1">RANDOM SEED</font></h3>
<p> <i>(This section applies to Linux guests only)</i> </p>
<p> For supported guests, virt-sysprep writes a few bytes of randomness from the host into the guest&#8217;s random seed file. </p>
<p> If this is just done once and the guest is cloned from the same template, then each guest will start with the same entropy, and things like <font SIZE="-1">SSH</font> host keys and <font SIZE="-1">TCP</font> sequence numbers may be predictable. </p>
<p> Therefore you should arrange to add more randomness <i>after</i> cloning from a template too, which can be done by enabling just the customize module: </p>
<pre>
 cp template.img newguest.img
 virt-sysprep --enable customize -a newguest.img
</pre>
<h2>SELINUX</h2>
<p> For guests which make use of SELinux, special handling for them might be needed when using operations which create new files or alter existing ones. </p>
<p> For further details, see &#8220;<font SIZE="-1">SELINUX&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1).</p>
<h2>WINDOWS 8</h2>
<p> Windows 8 &#8220;fast startup&#8221; can prevent virt-sysprep from working. See &#8220;<font SIZE="-1">WINDOWS HIBERNATION AND WINDOWS 8 FAST STARTUP&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 on success, or 1 if there was an error.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>&quot;VIRT_TOOLS_DATA_DIR&quot;</p>
<dd> This can point to the directory containing data files used for Windows firstboot installation. </p>
<p> Normally you do not need to set this. If not set, a compiled-in default will be used (something like <i>/usr/share/virt-tools</i>). </p>
<p> This directory may contain the following files:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>rhsrvany.exe</i></p>
<dd> This is the RHSrvAny Windows binary, used to install a &#8220;firstboot&#8221; script in Windows guests. It is required if you intend to use the <i>&#8211;firstboot</i> or <i>&#8211;firstboot-command</i> options with Windows guests. </p>
<p> See also: <tt>&quot;<a rel="nofollow" href="https://github.com/rwmjones/rhsrvany">https://github.com/rwmjones/rhsrvany</a>&quot;</tt></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> For other environment variables, see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1), <i><a href="/docs/linux/man/1-virt-clone/">virt-clone</a></i>(1), <i><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></i>(1), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <i><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></i>(1), <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <i><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></i>(8), <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1), <i><a href="/docs/linux/man/1-scrub/">scrub</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="http://libvirt.org/.">http://libvirt.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a> </p>
<p> Wanlong Gao, Fujitsu Ltd.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2016 Red Hat Inc. </p>
<p> Copyright (C) 2012 Fujitsu Ltd.</p>
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
<dt><a href="#lbBT">COPYING AND CLONING</a></p>
<dd>
<dt><a href="#lbBY">FIRSTBOOT VS SCRIPT</a></p>
<dd>
<dt><a href="#lbBZ">SECURITY</a></p>
<dd>
<dt><a href="#lbCB">SELINUX</a></p>
<dd>
<dt><a href="#lbCC">WINDOWS 8</a></p>
<dd>
<dt><a href="#lbCD">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbCE">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbCF">SEE ALSO</a></p>
<dd>
<dt><a href="#lbCG">AUTHORS</a></p>
<dd>
<dt><a href="#lbCH">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbCI">LICENSE</a></p>
<dd>
<dt><a href="#lbCJ">BUGS</a></p>
<dd></dl>
