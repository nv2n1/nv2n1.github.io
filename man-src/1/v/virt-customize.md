---
title: "virt-customize(1)"
name: "virt-customize"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-customize/"
description: "virt-customize – Customize a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-customize &#8211; Customize a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - customize[-a disk.img[-a disk.img...] | -d domname][--attach ISOFILE][--attach - format FORMAT][-c URI | --connect URI][-n | --dry - run][--format FORMAT][-m MB | --memsize MB][--network | --no - network][-q | --quiet][--smp N][-v | --verbose][-x] [--chmod PERMISSIONS:FILE][--commands - from - file FILENAME] [--copy SOURCE:DEST] [--copy - in LOCALPATH:REMOTEDIR][--delete PATH] [--edit FILE:EXPR][--firstboot SCRIPT][--firstboot - command 'CMD+ARGS'][--firstboot - install PKG, PKG..][--hostname HOSTNAME][--install PKG, PKG..] [--link TARGET:LINK
           [:LINK..]][--mkdir DIR] [--move SOURCE:DEST] [--password USER:SELECTOR][--root - password SELECTOR][--run SCRIPT][--run - command 'CMD+ARGS'][--scrub FILE][--sm - attach SELECTOR][--sm - register][--sm - remove][--sm - unregister][--ssh - inject USER[:SELECTOR]][--truncate FILE][--truncate - recursive PATH][--timezone TIMEZONE][--touch FILE][--uninstall PKG, PKG..][--update] [--upload FILE:DEST] [--write FILE:CONTENT][--no - logfile][--password - crypto md5 | sha256 | sha512][--selinux - relabel][--sm - credentials SELECTOR] virt -
    customize[-V | --version]
</code></pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;virt-customize&quot;</tt> on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently.</p>
<h2>DESCRIPTION</h2>
<p> Virt-customize can customize a virtual machine (disk image) by installing packages, editing configuration files, and so on. </p>
<p> Virt-customize modifies the guest or disk image <i>in place</i>. The guest must be shut down. If you want to preserve the existing contents of the guest, <i>you must snapshot, copy or clone the disk first</i>. </p>
<p> You do <i>not</i> need to run virt-customize as root. In fact we&#8217;d generally recommend that you don&#8217;t. </p>
<p> Related tools include: <i><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></i>(1) and <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1).</p>
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
<dt><code>&#8211;attach</code> <font SIZE="-1">ISOFILE</font></p>
<dd> The given disk is attached to the libguestfs appliance. This is used to provide extra software repositories or other data for customization. </p>
<p> You probably want to ensure the volume(s) or filesystems in the attached disks are labelled (or use an <font SIZE="-1">ISO</font> volume name) so that you can mount them by label in your run-scripts: </p>
<pre>
 mkdir /tmp/mount
 mount LABEL=EXTRA /tmp/mount
</pre>
<p> You can have multiple <i>&#8211;attach</i> options, and the format can be any disk format (not just an <font SIZE="-1">ISO</font>).</p>
<dt><code>&#8211;attach-format</code> <font SIZE="-1">FORMAT</font></p>
<dd> Specify the disk format for the next <i>&#8211;attach</i> option. The <tt>&quot;FORMAT&quot;</tt> is usually <tt>&quot;raw&quot;</tt> or <tt>&quot;qcow2&quot;</tt>. Use <tt>&quot;raw&quot;</tt> for ISOs.</p>
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
<dt><code>&#8211;format</code> raw|qcow2|..</p>
<dd>
<dt><code>&#8211;format</code> auto</p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format auto</i> switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 virt-customize --format raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-customize --format raw -a disk.img --format auto -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>-m</code> <font SIZE="-1">MB</font></p>
<dd>
<dt><code>&#8211;memsize</code> <font SIZE="-1">MB</font></p>
<dd> Change the amount of memory allocated to <i>&#8211;run</i> scripts. Increase this if you find that <i>&#8211;run</i> scripts or the <i>&#8211;install</i> option are running out of memory. </p>
<p> The default can be found with this command: </p>
<pre>
 guestfish get-memsize
</pre>
<dt><code>&#8211;network</code></p>
<dd>
<dt><code>&#8211;no-network</code></p>
<dd> Enable or disable network access from the guest during the installation. </p>
<p> Enabled is the default. Use <i>&#8211;no-network</i> to disable access. </p>
<p> The network only allows outgoing connections and has other minor limitations. See &#8220;<font SIZE="-1">NETWORK&#8221;</font> in <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1). </p>
<p> If you use <i>&#8211;no-network</i> then certain other options such as <i>&#8211;install</i> will not work. </p>
<p> This does not affect whether the guest can access the network once it has been booted, because that is controlled by your hypervisor or cloud environment and has nothing to do with virt-customize. </p>
<p> Generally speaking you should <i>not</i> use <i>&#8211;no-network</i>. But here are some reasons why you might want to:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Because the libguestfs backend that you are using doesn&#8217;t support the network. (See: &#8220;<font SIZE="-1">BACKEND&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)).</p>
<dt>2.</p>
<dd> Any software you need to install comes from an attached <font SIZE="-1">ISO,</font> so you don&#8217;t need the network.</p>
<dt>3.</p>
<dd> You don&#8217;t want untrusted guest code trying to access your host network when running virt-customize. This is particularly an issue when you don&#8217;t trust the source of the operating system templates. (See &#8220;<font SIZE="-1">SECURITY&#8221;</font> below).</p>
<dt>4.</p>
<dd> You don&#8217;t have a host network (eg. in secure/restricted environments).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t print log messages. </p>
<p> To enable detailed logging of individual file operations, use <i>-x</i>.</p>
<dt><code>&#8211;smp</code> N</p>
<dd> Enable N ≥ 2 virtual CPUs for <i>&#8211;run</i> scripts to use.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h3>Customization options</h3>
<dl>
<dt><code>&#8211;chmod</code> <font SIZE="-1">PERMISSIONS:FILE</font></p>
<dd> Change the permissions of <tt>&quot;FILE&quot;</tt> to <tt>&quot;PERMISSIONS&quot;</tt>. </p>
<p> <i>Note</i>: <tt>&quot;PERMISSIONS&quot;</tt> by default would be decimal, unless you prefix it with <tt>0</tt> to get octal, ie. use <tt>0700</tt> not <tt>700</tt>.</p>
<dt><code>&#8211;commands-from-file</code> <font SIZE="-1">FILENAME</font></p>
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
<dt><code>&#8211;copy</code> <font SIZE="-1">SOURCE:DEST</font></p>
<dd> Copy files or directories recursively inside the guest. </p>
<p> Wildcards cannot be used.</p>
<dt><code>&#8211;copy-in</code> <font SIZE="-1">LOCALPATH:REMOTEDIR</font></p>
<dd> Copy local files or directories recursively into the disk image, placing them in the directory <tt>&quot;REMOTEDIR&quot;</tt> (which must exist). </p>
<p> Wildcards cannot be used.</p>
<dt><code>&#8211;delete</code> <font SIZE="-1">PATH</font></p>
<dd> Delete a file from the guest. Or delete a directory (and all its contents, recursively). </p>
<p> You can use shell glob characters in the specified path. Be careful to escape glob characters from the host shell, if that is required. For example: </p>
<pre>
 virt-customize --delete '/var/log/*.log'.
</pre>
<p> See also: <i>&#8211;upload</i>, <i>&#8211;scrub</i>.</p>
<dt><code>&#8211;edit</code> <font SIZE="-1">FILE:EXPR</font></p>
<dd> Edit <tt>&quot;FILE&quot;</tt> using the Perl expression <tt>&quot;EXPR&quot;</tt>. </p>
<p> Be careful to properly quote the expression to prevent it from being altered by the shell. </p>
<p> Note that this option is only available when Perl 5 is installed. </p>
<p> See &#8220;NON-INTERACTIVE <font SIZE="-1">EDITING&#8221;</font> in <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1).</p>
<dt><code>&#8211;firstboot</code> <font SIZE="-1">SCRIPT</font></p>
<dd> Install <tt>&quot;SCRIPT&quot;</tt> inside the guest, so that when the guest first boots up, the script runs (as root, late in the boot process). </p>
<p> The script is automatically chmod +x after installation in the guest. </p>
<p> The alternative version <i>&#8211;firstboot-command</i> is the same, but it conveniently wraps the command up in a single line script for you. </p>
<p> You can have multiple <i>&#8211;firstboot</i> options. They run in the same order that they appear on the command line. </p>
<p> Please take a look at &#8220;<font SIZE="-1">FIRST BOOT SCRIPTS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for more information and caveats about the first boot scripts. </p>
<p> See also <i>&#8211;run</i>.</p>
<dt><code>&#8211;firstboot-command</code> &#8216;<font SIZE="-1">CMD+ARGS</font>&#8216;</p>
<dd> Run command (and arguments) inside the guest when the guest first boots up (as root, late in the boot process). </p>
<p> You can have multiple <i>&#8211;firstboot</i> options. They run in the same order that they appear on the command line. </p>
<p> Please take a look at &#8220;<font SIZE="-1">FIRST BOOT SCRIPTS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for more information and caveats about the first boot scripts. </p>
<p> See also <i>&#8211;run</i>.</p>
<dt><code>&#8211;firstboot-install</code> <font SIZE="-1">PKG,PKG..</font></p>
<dd> Install the named packages (a comma-separated list). These are installed when the guest first boots using the guest&#8217;s package manager (eg. apt, yum, etc.) and the guest&#8217;s network connection. </p>
<p> For an overview on the different ways to install packages, see &#8220;<font SIZE="-1">INSTALLING PACKAGES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1).</p>
<dt><code>&#8211;hostname</code> <font SIZE="-1">HOSTNAME</font></p>
<dd> Set the hostname of the guest to <tt>&quot;HOSTNAME&quot;</tt>. You can use a dotted hostname.domainname (<font SIZE="-1">FQDN</font>) if you want.</p>
<dt><code>&#8211;install</code> <font SIZE="-1">PKG,PKG..</font></p>
<dd> Install the named packages (a comma-separated list). These are installed during the image build using the guest&#8217;s package manager (eg. apt, yum, etc.) and the host&#8217;s network connection. </p>
<p> For an overview on the different ways to install packages, see &#8220;<font SIZE="-1">INSTALLING PACKAGES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1). </p>
<p> See also <i>&#8211;update</i>, <i>&#8211;uninstall</i>.</p>
<dt><code>&#8211;link</code> TARGET:LINK[:LINK..]</p>
<dd> Create symbolic link(s) in the guest, starting at <tt>&quot;LINK&quot;</tt> and pointing at <tt>&quot;TARGET&quot;</tt>.</p>
<dt><code>&#8211;mkdir</code> <font SIZE="-1">DIR</font></p>
<dd> Create a directory in the guest. </p>
<p> This uses <tt>&quot;mkdir -p&quot;</tt> so any intermediate directories are created, and it also works if the directory already exists.</p>
<dt><code>&#8211;move</code> <font SIZE="-1">SOURCE:DEST</font></p>
<dd> Move files or directories inside the guest. </p>
<p> Wildcards cannot be used.</p>
<dt><code>&#8211;no-logfile</code></p>
<dd> Scrub <tt>&quot;builder.log&quot;</tt> (log file from build commands) from the image after building is complete. If you don&#8217;t want to reveal precisely how the image was built, use this option. </p>
<p> See also: &#8220;<font SIZE="-1">LOG FILE&#8221;</font>.</p>
<dt><code>&#8211;password</code> <font SIZE="-1">USER:SELECTOR</font></p>
<dd> Set the password for <tt>&quot;USER&quot;</tt>. (Note this option does <i>not</i> create the user account). </p>
<p> See &#8220;<font SIZE="-1">USERS AND PASSWORDS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field, and also how to set up user accounts.</p>
<dt><code>&#8211;password-crypto</code> md5|sha256|sha512</p>
<dd> When the virt tools change or set a password in the guest, this option sets the password encryption of that password to <tt>&quot;md5&quot;</tt>, <tt>&quot;sha256&quot;</tt> or <tt>&quot;sha512&quot;</tt>. </p>
<p> <tt>&quot;sha256&quot;</tt> and <tt>&quot;sha512&quot;</tt> require glibc ≥ 2.7 (check <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3) inside the guest). </p>
<p> <tt>&quot;md5&quot;</tt> will work with relatively old Linux guests (eg. <font SIZE="-1">RHEL 3</font>), but is not secure against modern attacks. </p>
<p> The default is <tt>&quot;sha512&quot;</tt> unless libguestfs detects an old guest that didn&#8217;t have support for <font SIZE="-1">SHA-512,</font> in which case it will use <tt>&quot;md5&quot;</tt>. You can override libguestfs by specifying this option. </p>
<p> Note this does not change the default password encryption used by the guest when you create new user accounts inside the guest. If you want to do that, then you should use the <i>&#8211;edit</i> option to modify <tt>&quot;/etc/sysconfig/authconfig&quot;</tt> (Fedora, <font SIZE="-1">RHEL</font>) or <tt>&quot;/etc/pam.d/common-password&quot;</tt> (Debian, Ubuntu).</p>
<dt><code>&#8211;root-password</code> <font SIZE="-1">SELECTOR</font></p>
<dd> Set the root password. </p>
<p> See &#8220;<font SIZE="-1">USERS AND PASSWORDS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field, and also how to set up user accounts. </p>
<p> Note: In virt-builder, if you <i>don&#8217;t</i> set <i>&#8211;root-password</i> then the guest is given a <i>random</i> root password.</p>
<dt><code>&#8211;run</code> <font SIZE="-1">SCRIPT</font></p>
<dd> Run the shell script (or any program) called <tt>&quot;SCRIPT&quot;</tt> on the disk image. The script runs virtualized inside a small appliance, chrooted into the guest filesystem. </p>
<p> The script is automatically chmod +x. </p>
<p> If libguestfs supports it then a limited network connection is available but it only allows outgoing network connections. You can also attach data disks (eg. <font SIZE="-1">ISO</font> files) as another way to provide data (eg. software packages) to the script without needing a network connection (<i>&#8211;attach</i>). You can also upload data files (<i>&#8211;upload</i>). </p>
<p> You can have multiple <i>&#8211;run</i> options. They run in the same order that they appear on the command line. </p>
<p> See also: <i>&#8211;firstboot</i>, <i>&#8211;attach</i>, <i>&#8211;upload</i>.</p>
<dt><code>&#8211;run-command</code> &#8216;<font SIZE="-1">CMD+ARGS</font>&#8216;</p>
<dd> Run the command and arguments on the disk image. The command runs virtualized inside a small appliance, chrooted into the guest filesystem. </p>
<p> If libguestfs supports it then a limited network connection is available but it only allows outgoing network connections. You can also attach data disks (eg. <font SIZE="-1">ISO</font> files) as another way to provide data (eg. software packages) to the script without needing a network connection (<i>&#8211;attach</i>). You can also upload data files (<i>&#8211;upload</i>). </p>
<p> You can have multiple <i>&#8211;run-command</i> options. They run in the same order that they appear on the command line. </p>
<p> See also: <i>&#8211;firstboot</i>, <i>&#8211;attach</i>, <i>&#8211;upload</i>.</p>
<dt><code>&#8211;scrub</code> <font SIZE="-1">FILE</font></p>
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
<dt><code>&#8211;selinux-relabel</code></p>
<dd> Relabel files in the guest so that they have the correct SELinux label. </p>
<p> This will attempt to relabel files immediately, but if the operation fails this will instead touch <i>/.autorelabel</i> on the image to schedule a relabel operation for the next time the image boots. </p>
<p> You should only use this option for guests which support SELinux.</p>
<dt><code>&#8211;sm-attach</code> <font SIZE="-1">SELECTOR</font></p>
<dd> Attach to a pool using <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> See &#8220;SUBSCRIPTION-MANAGER&#8221; in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field.</p>
<dt><code>&#8211;sm-credentials</code> <font SIZE="-1">SELECTOR</font></p>
<dd> Set the credentials for <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> See &#8220;SUBSCRIPTION-MANAGER&#8221; in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field.</p>
<dt><code>&#8211;sm-register</code></p>
<dd> Register the guest using <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> This requires credentials being set using <i>&#8211;sm-credentials</i>.</p>
<dt><code>&#8211;sm-remove</code></p>
<dd> Remove all the subscriptions from the guest using <tt>&quot;subscription-manager&quot;</tt>.</p>
<dt><code>&#8211;sm-unregister</code></p>
<dd> Unregister the guest using <tt>&quot;subscription-manager&quot;</tt>.</p>
<dt><code>&#8211;ssh-inject</code> USER[:SELECTOR]</p>
<dd> Inject an ssh key so the given <tt>&quot;USER&quot;</tt> will be able to log in over ssh without supplying a password. The <tt>&quot;USER&quot;</tt> must exist already in the guest. </p>
<p> See &#8220;<font SIZE="-1">SSH KEYS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) for the format of the <tt>&quot;SELECTOR&quot;</tt> field. </p>
<p> You can have multiple <i>&#8211;ssh-inject</i> options, for different users and also for more keys for each user.</p>
<dt><code>&#8211;timezone</code> <font SIZE="-1">TIMEZONE</font></p>
<dd> Set the default timezone of the guest to <tt>&quot;TIMEZONE&quot;</tt>. Use a location string like <tt>&quot;Europe/London&quot;</tt></p>
<dt><code>&#8211;touch</code> <font SIZE="-1">FILE</font></p>
<dd> This command performs a <i><a href="/docs/linux/man/1-touch/">touch</a></i>(1)-like operation on <tt>&quot;FILE&quot;</tt>.</p>
<dt><code>&#8211;truncate</code> <font SIZE="-1">FILE</font></p>
<dd> This command truncates <tt>&quot;FILE&quot;</tt> to a zero-length file. The file must exist already.</p>
<dt><code>&#8211;truncate-recursive</code> <font SIZE="-1">PATH</font></p>
<dd> This command recursively truncates all files under <tt>&quot;PATH&quot;</tt> to zero-length.</p>
<dt><code>&#8211;uninstall</code> <font SIZE="-1">PKG,PKG..</font></p>
<dd> Uninstall the named packages (a comma-separated list). These are removed during the image build using the guest&#8217;s package manager (eg. apt, yum, etc.). Dependent packages may also need to be uninstalled to satisfy the request. </p>
<p> See also <i>&#8211;install</i>, <i>&#8211;update</i>.</p>
<dt><code>&#8211;update</code></p>
<dd> Do the equivalent of <tt>&quot;yum update&quot;</tt>, <tt>&quot;apt-get upgrade&quot;</tt>, or whatever command is required to update the packages already installed in the template to their latest versions. </p>
<p> See also <i>&#8211;install</i>, <i>&#8211;uninstall</i>.</p>
<dt><code>&#8211;upload</code> <font SIZE="-1">FILE:DEST</font></p>
<dd> Upload local file <tt>&quot;FILE&quot;</tt> to destination <tt>&quot;DEST&quot;</tt> in the disk image. File owner and permissions from the original are preserved, so you should set them to what you want them to be in the disk image. </p>
<p> <tt>&quot;DEST&quot;</tt> could be the final filename. This can be used to rename the file on upload. </p>
<p> If <tt>&quot;DEST&quot;</tt> is a directory name (which must already exist in the guest) then the file is uploaded into that directory, and it keeps the same name as on the local filesystem. </p>
<p> See also: <i>&#8211;mkdir</i>, <i>&#8211;delete</i>, <i>&#8211;scrub</i>.</p>
<dt><code>&#8211;write</code> <font SIZE="-1">FILE:CONTENT</font></p>
<dd> Write <tt>&quot;CONTENT&quot;</tt> to <tt>&quot;FILE&quot;</tt>.</dl>
<h2>SELINUX</h2>
<p> For guests which make use of SELinux, special handling for them might be needed when using operations which create new files or alter existing ones. </p>
<p> For further details, see &#8220;<font SIZE="-1">SELINUX&#8221;</font> in <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1).</p>
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
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1), <i><a href="/docs/linux/man/1-virt-clone/">virt-clone</a></i>(1), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <i><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></i>(1), <i><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></i>(1), <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <i><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></i>(8), <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1), <i><a href="/docs/linux/man/1-scrub/">scrub</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="http://libvirt.org/.">http://libvirt.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2016 Red Hat Inc.</p>
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
