---
title: "virt-builder(1)"
name: "virt-builder"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-builder/"
description: "virt-builder – Build virtual machine images quickly"
---

<h2 class="name">NAME</h2>
<p> virt-builder &#8211; Build virtual machine images quickly </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - builder os - version[-o | --output DISKIMAGE][--size SIZE][--format raw | qcow2][--arch ARCHITECTURE][--attach ISOFILE] [--chmod PERMISSIONS:FILE][--commands - from - file FILENAME] [--copy SOURCE:DEST] [--copy - in LOCALPATH:REMOTEDIR][--delete PATH] [--edit FILE:EXPR][--firstboot SCRIPT][--firstboot - command 'CMD+ARGS'][--firstboot - install PKG, PKG..][--hostname HOSTNAME][--install PKG, PKG..] [--link TARGET:LINK
                        [:LINK..]][--mkdir DIR] [--move SOURCE:DEST] [--password USER:SELECTOR][--root - password SELECTOR][--run SCRIPT][--run - command 'CMD+ARGS'][--scrub FILE][--sm - attach SELECTOR][--sm - register][--sm - remove][--sm - unregister][--ssh - inject USER[:SELECTOR]][--truncate FILE][--truncate - recursive PATH][--timezone TIMEZONE][--touch FILE][--uninstall PKG, PKG..][--update] [--upload FILE:DEST] [--write FILE:CONTENT][--no - logfile][--password - crypto md5 | sha256 | sha512][--selinux - relabel][--sm - credentials SELECTOR] virt -
        builder - l |
    --list[--long][--list - format short | long | json] virt - builder-- notes os - version virt - builder-- print - cache virt - builder-- cache - all - templates virt - builder-- delete - cache virt - builder-- get - kernel DISKIMAGE[--format raw | qcow2][--output OUTPUTDIR]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Virt-builder is a tool for quickly building new virtual machines. You can build a variety of VMs for local or cloud use, usually within a few minutes or less. Virt-builder also has many ways to customize these VMs. Everything is run from the command line and nothing requires root privileges, so automation and scripting is simple. </p>
<p> Note that virt-builder does not install guests from scratch. It takes cleanly prepared, digitally signed <font SIZE="-1">OS</font> templates and customizes them. This approach is used because it is much faster, but if you need to do fresh installs you may want to look at <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1) and <i><a href="/docs/linux/man/1-oz-install/">oz-install</a></i>(1). </p>
<p> The easiest way to get started is by looking at the examples in the next section.</p>
<h2>EXAMPLES</h2>
<h3>List the virtual machines available</h3>
<pre>
 virt-builder --list
</pre>
<p> will list out the operating systems available to install. A selection of freely redistributable OSes is available as standard. You can add your own too (see below). </p>
<p> After choosing a guest from the list, you may want to see if there are any installation notes: </p>
<pre>
 virt-builder --notes fedora-20
</pre>
<h3>Build a virtual machine</h3>
<pre>
 virt-builder fedora-20
</pre>
<p> will build a Fedora 20 image for the same architecture as virt-builder (so running it from an i386 installation will try to build an i386 image, if available). This will have all default configuration (minimal size, no user accounts, random root password, only the bare minimum installed software, etc.). </p>
<p> You <i>do not</i> need to run this command as root. </p>
<p> The first time this runs it has to download the template over the network, but this gets cached (see &#8220;<font SIZE="-1">CACHING&#8221;</font>). </p>
<p> The name of the output file is derived from the template name, so above it will be <i>fedora-20.img</i>. You can change the output filename using the <i>-o</i> option: </p>
<pre>
 virt-builder fedora-20 -o mydisk.img
</pre>
<p> You can also use the <i>-o</i> option to write to existing devices or logical volumes. </p>
<pre>
 virt-builder fedora-20 --format qcow2
</pre>
<p> As above, but write the output in qcow2 format to <i>fedora-20.qcow2</i>. </p>
<pre>
 virt-builder fedora-20 --size 20G
</pre>
<p> As above, but the output size will be 20 <font SIZE="-1">GB. </font> The guest <font SIZE="-1">OS</font> is resized as it is copied to the output (automatically, using <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1)). </p>
<pre>
 virt-builder fedora-20 --arch i386
</pre>
<p> As above, but using an i386 template, if available.</p>
<h3>Setting the root password</h3>
<pre>
 virt-builder fedora-20 --root-password file:/tmp/rootpw
</pre>
<p> Create a Fedora 20 image. The root password is taken from the file <i>/tmp/rootpw</i>. </p>
<p> Note if you <i>don&#8217;t</i> set <i>&#8211;root-password</i> then the guest is given a <i>random</i> root password. </p>
<p> You can also create user accounts. See &#8220;<font SIZE="-1">USERS AND PASSWORDS&#8221;</font> below.</p>
<h3>Set the hostname</h3>
<pre>
 virt-builder fedora-20 --hostname virt.example.com
</pre>
<p> Set the hostname to <tt>&quot;virt.example.com&quot;</tt>.</p>
<h3>Installing software</h3>
<p> To install packages from the ordinary (guest) software repository (eg. yum or apt): </p>
<pre>
 virt-builder fedora-20 --install &quot;inkscape,@Xfce Desktop&quot;
</pre>
<p> (In Fedora, <tt>&quot;@&quot;</tt> is used to install groups of packages. On Debian you would install a meta-package instead.) </p>
<p> To update the core packages to the latest version: </p>
<pre>
 virt-builder debian-7 --update
</pre>
<p> For guests which use SELinux, like Fedora and Red Hat Enterprise Linux, you may need to do SELinux relabelling after installing or updating packages (see &#8220;<font SIZE="-1">SELINUX&#8221;</font> below): </p>
<pre>
 virt-builder fedora-20 --update --selinux-relabel
</pre>
<h3>Customizing the installation</h3>
<p> There are many options that let you customize the installation. These include: <i>&#8211;run</i>/<i>&#8211;run-command</i>, which run a shell script or command while the disk image is being generated and lets you add or edit files that go into the disk image. <i>&#8211;firstboot</i>/<i>&#8211;firstboot-command</i>, which let you add scripts/commands that are run the first time the guest boots. <i>&#8211;edit</i> to edit files. <i>&#8211;upload</i> to upload files. </p>
<p> For example: </p>
<pre>
 cat &lt;&lt;'EOF' &gt; /tmp/yum-update.sh
 yum -y update
 EOF
 
 virt-builder fedora-20 --firstboot /tmp/yum-update.sh
</pre>
<p> or simply: </p>
<pre>
 virt-builder fedora-20 --firstboot-command 'yum -y update'
</pre>
<p> which makes the <i><a href="/docs/linux/man/8-yum/">yum</a></i>(8) <tt>&quot;update&quot;</tt> command run once the first time the guest boots. </p>
<p> Or: </p>
<pre>
 virt-builder fedora-20 \
   --edit '/etc/yum.conf:
             s/gpgcheck=1/gpgcheck=0/'
</pre>
<p> which edits <i>/etc/yum.conf</i> inside the disk image (during disk image creation, long before boot). </p>
<p> You can combine these options, and have multiple options of all types.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>&#8211;arch</code> <font SIZE="-1">ARCHITECTURE</font></p>
<dd> Use the specified architecture for the output image. This means there must be sources providing the requested template for the requested architecture. </p>
<p> See also &#8220;<font SIZE="-1">ARCHITECTURE&#8221;</font>.</p>
<dt><code>&#8211;attach</code> <font SIZE="-1">ISOFILE</font></p>
<dd> During the customization phase, the given disk is attached to the libguestfs appliance. This is used to provide extra software repositories or other data for customization. </p>
<p> You probably want to ensure the volume(s) or filesystems in the attached disks are labelled (or use an <font SIZE="-1">ISO</font> volume name) so that you can mount them by label in your run-scripts: </p>
<pre>
 mkdir /tmp/mount
 mount LABEL=EXTRA /tmp/mount
</pre>
<p> You can have multiple <i>&#8211;attach</i> options, and the format can be any disk format (not just an <font SIZE="-1">ISO</font>). </p>
<p> See also: <i>&#8211;run</i>, &#8220;Installing packages at build time from a side repository&#8221;, <i><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></i>(1), <i><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></i>(1).</p>
<dt><code>&#8211;attach-format</code> <font SIZE="-1">FORMAT</font></p>
<dd> Specify the disk format for the next <i>&#8211;attach</i> option. The <tt>&quot;FORMAT&quot;</tt> is usually <tt>&quot;raw&quot;</tt> or <tt>&quot;qcow2&quot;</tt>. Use <tt>&quot;raw&quot;</tt> for ISOs.</p>
<dt><code>&#8211;cache</code> <font SIZE="-1">DIR</font></p>
<dd>
<dt><code>&#8211;no-cache</code></p>
<dd> <i>&#8211;cache</i> <font SIZE="-1">DIR</font> sets the directory to use/check for cached template files. If not set, defaults to either <i></i>$XDG_CACHE_HOME<i>/virt-builder/</i> or <i></i>$HOME<i>/.cache/virt-builder/</i>. </p>
<p> <i>&#8211;no-cache</i> disables template caching.</p>
<dt><code>&#8211;cache-all-templates</code></p>
<dd> Download all templates to the cache and then exit. See &#8220;<font SIZE="-1">CACHING&#8221;</font>. </p>
<p> Note this doesn&#8217;t cache everything. More templates might be uploaded. Also this doesn&#8217;t cache packages (the <i>&#8211;install</i>, <i>&#8211;update</i> options).</p>
<dt><code>&#8211;check-signature</code></p>
<dd>
<dt><code>&#8211;no-check-signature</code></p>
<dd> Check/don&#8217;t check the digital signature of the <font SIZE="-1">OS</font> template. The default is to check the signature and exit if it is not correct. Using <i>&#8211;no-check-signature</i> bypasses this check. </p>
<p> See also <i>&#8211;fingerprint</i>.</p>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>&#8211;curl</code> <font SIZE="-1">CURL</font></p>
<dd> Specify an alternate <i><a href="/docs/linux/man/1-curl/">curl</a></i>(1) binary. You can also use this to add curl parameters, for example to disable https certificate checks: </p>
<p>virt &#8211; builder&#8211; curl &#8220;curl &#8211;insecure&#8221;[&#8230;]</p>
<dt><code>&#8211;delete-cache</code></p>
<dd> Delete the template cache. See &#8220;<font SIZE="-1">CACHING&#8221;</font>.</p>
<dt><code>&#8211;no-delete-on-failure</code></p>
<dd> Don&#8217;t delete the output file on failure to build. You can use this to debug failures to run scripts. See &#8220;<font SIZE="-1">DEBUGGING BUILDS&#8221;</font> for ways to debug images. </p>
<p> The default is to delete the output file if virt-builder fails (or, for example, some script that it runs fails).</p>
<dt><code>&#8211;fingerprint</code> &#8216;<font SIZE="-1">AAAA BBBB &#8230;</font>&#8216;</p>
<dd> Check that the index and templates are signed by the key with the given fingerprint. (The fingerprint is a long string, usually written as 10 groups of 4 hexadecimal digits). </p>
<p> You can give this option multiple times. If you have multiple source URLs, then you can have either no fingerprint, one fingerprint or multiple fingerprints. If you have multiple, then each must correspond 1-1 with a source <font SIZE="-1">URL.</font></p>
<dt><code>&#8211;format</code> qcow2</p>
<dd>
<dt><code>&#8211;format</code> raw</p>
<dd> For ordinary builds, this selects the output format. The default is <i>raw</i>. </p>
<p> With <i>&#8211;get-kernel</i> this specifies the input format. </p>
<p> To create an old-style qcow2 file (for compatibility with <font SIZE="-1">RHEL 6</font> or very old qemu &lt; 1.1), after running virt-builder, use this command: </p>
<pre>
 qemu-img amend -f qcow2 -o compat=0.10 output.qcow2
</pre>
<dt><code>&#8211;get-kernel</code> <font SIZE="-1">IMAGE</font></p>
<dd> This option extracts the kernel and initramfs from a previously built disk image called <tt>&quot;IMAGE&quot;</tt> (in fact it works for any <font SIZE="-1">VM</font> disk image, not just ones built using virt-builder). </p>
<p> The kernel and initramfs are written to the current directory, unless you also specify the <i>&#8211;output</i> <tt>&quot;outputdir&quot;</tt> <code>directory</code> name. </p>
<p> The format of the disk image is automatically detected unless you specify it by using the <i>&#8211;format</i> option. </p>
<p> In the case where the guest contains multiple kernels, the one with the highest version number is chosen. To extract arbitrary kernels from the disk image, see <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). To extract the entire <i>/boot</i> directory of a guest, see <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1).</p>
<dt><code>&#8211;gpg</code> <font SIZE="-1">GPG</font></p>
<dd> Specify an alternate <i><a href="/docs/linux/man/1-gpg/">gpg</a></i>(1) (<font SIZE="-1">GNU</font> Privacy Guard) binary. You can also use this to add gpg parameters, for example to specify an alternate home directory: </p>
<p>virt &#8211; builder&#8211; gpg &#8220;gpg &#8211;homedir /tmp&#8221;[&#8230;]</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;list</code></p>
<dd>
<dt><code>&#8211;list &#8211;list-format</code> format</p>
<dd>
<dt><code>&#8211;list &#8211;long</code></p>
<dd> List available templates. </p>
<p> It is possible to choose with <i>&#8211;list-format</i> the output format for the list templates:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>short</code></p>
<dd> The default format, prints only the template identifier and, next to it, its short description.</p>
<dt><code>long</code></p>
<dd> Prints a textual list with the details of the available sources, followed by the details of the available templates.</p>
<dt><code>json</code></p>
<dd> Prints a <font SIZE="-1">JSON</font> object with the details of the available sources and the details of the available templates. </p>
<p> The <tt>&quot;version&quot;</tt> key in the main object represents the &#8220;compatibility version&#8221;, and it is bumped every time the resulting <font SIZE="-1">JSON</font> output is incompatible with the previous versions (for example the structure has changed, or non-optional keys are no more present).</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>&#8211;long</i> is a shorthand for the <tt>&quot;long&quot;</tt> format. </p>
<p> See also: <i>&#8211;source</i>, <i>&#8211;notes</i>, &#8220;<font SIZE="-1">SOURCES OF TEMPLATES&#8221;</font>.</dl>
<dt><code>&#8211;machine-readable</code></p>
<dd> This option is used to make the output more machine friendly when being parsed by other programs. See &#8220;<font SIZE="-1">MACHINE READABLE OUTPUT&#8221;</font> below.</p>
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
<p> This does not affect whether the guest can access the network once it has been booted, because that is controlled by your hypervisor or cloud environment and has nothing to do with virt-builder. </p>
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
<dd> You don&#8217;t want untrusted guest code trying to access your host network when running virt-builder. This is particularly an issue when you don&#8217;t trust the source of the operating system templates. (See &#8220;<font SIZE="-1">SECURITY&#8221;</font> below).</p>
<dt>4.</p>
<dd> You don&#8217;t have a host network (eg. in secure/restricted environments).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-sync</code></p>
<dd> Do not sync the output file on exit. </p>
<p> Virt-builder fsync&#8217;s the output file or disk image when it exits. </p>
<p> The reason is that qemu/KVM&#8217;s default caching mode is <tt>&quot;none&quot;</tt> or <tt>&quot;directsync&quot;</tt>, both of which bypass the host page cache. Therefore these would not work correctly if you immediately started the guest after running virt-builder &#8211; they would not see the complete output file. (Note that you should not use these caching modes &#8211; they are fundamentally broken for this and other reasons.) </p>
<p> If you are not using these broken caching modes, you can use <i>&#8211;no-sync</i> to avoid this unnecessary sync and gain considerable extra performance.</p>
<dt><code>&#8211;notes</code> os-version</p>
<dd> List any notes associated with this guest, then exit (this does not do the install).</p>
<dt><code>-o</code> filename</p>
<dd>
<dt><code>&#8211;output</code> filename</p>
<dd> Write the output to <i>filename</i>. If you don&#8217;t specify this option, then the output filename is generated by taking the <tt>&quot;os-version&quot;</tt> string and adding <tt>&quot;.img&quot;</tt> (for raw format) or <tt>&quot;.qcow2&quot;</tt> (for qcow2 format). </p>
<p> Note that the output filename could be a device, partition or logical volume. </p>
<p> When used with <i>&#8211;get-kernel</i>, this option specifies the output directory.</p>
<dt><code>&#8211;print-cache</code></p>
<dd> Print information about the template cache. See &#8220;<font SIZE="-1">CACHING&#8221;</font>.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t print ordinary progress messages.</p>
<dt><code>&#8211;size</code> <font SIZE="-1">SIZE</font></p>
<dd> Select the size of the output disk, where the size can be specified using common names such as <tt>&quot;32G&quot;</tt> (32 gigabytes) etc. </p>
<p> Virt-builder will resize filesystems inside the disk image automatically. </p>
<p> If the size is not specified, then one of two things happens. If the output is a file, then the size is the same as the template. If the output is a device, partition, etc then the size of that device is used. </p>
<p> To specify size in bytes, the number must be followed by the lowercase letter <i>b</i>, eg: <tt>&quot;--size 10737418240b&quot;</tt>.</p>
<dt><code>&#8211;smp</code> N</p>
<dd> Enable N ≥ 2 virtual CPUs for <i>&#8211;run</i> scripts to use.</p>
<dt><code>&#8211;source</code> <font SIZE="-1">URL</font></p>
<dd> Set the source <font SIZE="-1">URL</font> to look for indexes. </p>
<p> You can give this option multiple times to specify multiple sources. </p>
<p> See also &#8220;<font SIZE="-1">SOURCES OF TEMPLATES&#8221;</font> below. </p>
<p> Note that you should not point <i>&#8211;source</i> to sources that you don&#8217;t trust (unless the source is signed by someone you do trust). See also the <i>&#8211;no-network</i> option.</p>
<dt><code>&#8211;no-warn-if-partition</code></p>
<dd> Do not emit a warning if the output device is a partition. This warning avoids a common user error when writing to a <font SIZE="-1">USB</font> key or external drive, when you should normally write to the whole device (<i>&#8211;output /dev/sdX</i>), not to a partition on the device (<i>&#8211;output /dev/sdX1</i>). Use this option to <i>suppress</i> this warning.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable debug messages and/or produce verbose output. </p>
<p> When reporting bugs, use this option and attach the complete output to your bug report.</p>
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
<p> Please take a look at &#8220;<font SIZE="-1">FIRST BOOT SCRIPTS&#8221;</font> for more information and caveats about the first boot scripts. </p>
<p> See also <i>&#8211;run</i>.</p>
<dt><code>&#8211;firstboot-command</code> &#8216;<font SIZE="-1">CMD+ARGS</font>&#8216;</p>
<dd> Run command (and arguments) inside the guest when the guest first boots up (as root, late in the boot process). </p>
<p> You can have multiple <i>&#8211;firstboot</i> options. They run in the same order that they appear on the command line. </p>
<p> Please take a look at &#8220;<font SIZE="-1">FIRST BOOT SCRIPTS&#8221;</font> for more information and caveats about the first boot scripts. </p>
<p> See also <i>&#8211;run</i>.</p>
<dt><code>&#8211;firstboot-install</code> <font SIZE="-1">PKG,PKG..</font></p>
<dd> Install the named packages (a comma-separated list). These are installed when the guest first boots using the guest&#8217;s package manager (eg. apt, yum, etc.) and the guest&#8217;s network connection. </p>
<p> For an overview on the different ways to install packages, see &#8220;<font SIZE="-1">INSTALLING PACKAGES&#8221;</font>.</p>
<dt><code>&#8211;hostname</code> <font SIZE="-1">HOSTNAME</font></p>
<dd> Set the hostname of the guest to <tt>&quot;HOSTNAME&quot;</tt>. You can use a dotted hostname.domainname (<font SIZE="-1">FQDN</font>) if you want.</p>
<dt><code>&#8211;install</code> <font SIZE="-1">PKG,PKG..</font></p>
<dd> Install the named packages (a comma-separated list). These are installed during the image build using the guest&#8217;s package manager (eg. apt, yum, etc.) and the host&#8217;s network connection. </p>
<p> For an overview on the different ways to install packages, see &#8220;<font SIZE="-1">INSTALLING PACKAGES&#8221;</font>. </p>
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
<p> See &#8220;<font SIZE="-1">USERS AND PASSWORDS&#8221;</font> for the format of the <tt>&quot;SELECTOR&quot;</tt> field, and also how to set up user accounts.</p>
<dt><code>&#8211;password-crypto</code> md5|sha256|sha512</p>
<dd> When the virt tools change or set a password in the guest, this option sets the password encryption of that password to <tt>&quot;md5&quot;</tt>, <tt>&quot;sha256&quot;</tt> or <tt>&quot;sha512&quot;</tt>. </p>
<p> <tt>&quot;sha256&quot;</tt> and <tt>&quot;sha512&quot;</tt> require glibc ≥ 2.7 (check <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3) inside the guest). </p>
<p> <tt>&quot;md5&quot;</tt> will work with relatively old Linux guests (eg. <font SIZE="-1">RHEL 3</font>), but is not secure against modern attacks. </p>
<p> The default is <tt>&quot;sha512&quot;</tt> unless libguestfs detects an old guest that didn&#8217;t have support for <font SIZE="-1">SHA-512,</font> in which case it will use <tt>&quot;md5&quot;</tt>. You can override libguestfs by specifying this option. </p>
<p> Note this does not change the default password encryption used by the guest when you create new user accounts inside the guest. If you want to do that, then you should use the <i>&#8211;edit</i> option to modify <tt>&quot;/etc/sysconfig/authconfig&quot;</tt> (Fedora, <font SIZE="-1">RHEL</font>) or <tt>&quot;/etc/pam.d/common-password&quot;</tt> (Debian, Ubuntu).</p>
<dt><code>&#8211;root-password</code> <font SIZE="-1">SELECTOR</font></p>
<dd> Set the root password. </p>
<p> See &#8220;<font SIZE="-1">USERS AND PASSWORDS&#8221;</font> for the format of the <tt>&quot;SELECTOR&quot;</tt> field, and also how to set up user accounts. </p>
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
<p> See &#8220;SUBSCRIPTION-MANAGER&#8221; for the format of the <tt>&quot;SELECTOR&quot;</tt> field.</p>
<dt><code>&#8211;sm-credentials</code> <font SIZE="-1">SELECTOR</font></p>
<dd> Set the credentials for <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> See &#8220;SUBSCRIPTION-MANAGER&#8221; for the format of the <tt>&quot;SELECTOR&quot;</tt> field.</p>
<dt><code>&#8211;sm-register</code></p>
<dd> Register the guest using <tt>&quot;subscription-manager&quot;</tt>. </p>
<p> This requires credentials being set using <i>&#8211;sm-credentials</i>.</p>
<dt><code>&#8211;sm-remove</code></p>
<dd> Remove all the subscriptions from the guest using <tt>&quot;subscription-manager&quot;</tt>.</p>
<dt><code>&#8211;sm-unregister</code></p>
<dd> Unregister the guest using <tt>&quot;subscription-manager&quot;</tt>.</p>
<dt><code>&#8211;ssh-inject</code> USER[:SELECTOR]</p>
<dd> Inject an ssh key so the given <tt>&quot;USER&quot;</tt> will be able to log in over ssh without supplying a password. The <tt>&quot;USER&quot;</tt> must exist already in the guest. </p>
<p> See &#8220;<font SIZE="-1">SSH KEYS&#8221;</font> for the format of the <tt>&quot;SELECTOR&quot;</tt> field. </p>
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
<h2>REFERENCE</h2>
<h3><font SIZE="-1">INSTALLING PACKAGES</font></h3>
<p> There are several approaches to installing packages or applications in the guest which have different trade-offs. </p>
<p> <i>Installing packages at build time</i> </p>
<p> If the guest <font SIZE="-1">OS</font> you are installing is similar to the host <font SIZE="-1">OS </font>(eg. both are Linux), and if libguestfs supports network connections, then you can use <i>&#8211;install</i> to install packages like this: </p>
<pre>
 virt-builder fedora-20 --install inkscape
</pre>
<p> This uses the guest&#8217;s package manager and the host&#8217;s network connection. </p>
<p> <i>Updating packages at build time</i> </p>
<p> To update the core set of packages in the template at build time: </p>
<pre>
 virt-builder fedora-20 --update
</pre>
<p> Most of the templates that ship with virt-builder come with a very minimal selection of packages (known as a &#8220;<font SIZE="-1">JEOS&#8221;</font> or &#8220;Just Enough Operating System&#8221;), which are up to date at the time the template is created, but could be out of date by the time you come to install an <font SIZE="-1">OS</font> from the template. This option updates those template packages. </p>
<p> <i>Installing packages at first boot</i> </p>
<p> Another option is to install the packages when the guest first boots: </p>
<pre>
 virt-builder fedora-20 --firstboot-install inkscape
</pre>
<p> This uses the guest&#8217;s package manager and the guest&#8217;s network connection. </p>
<p> The downsides are that it will take the guest a lot longer to boot first time, and there&#8217;s nothing much you can do if package installation fails (eg. if a network problem means the guest can&#8217;t reach the package repositories). </p>
<p> <i>Installing packages at build time from a side repository</i> </p>
<p> If the software you want to install is not available in the main package repository of the guest, then you can add a side repository. Usually this is presented as an <font SIZE="-1">ISO </font>(<font SIZE="-1">CD</font> disk image) file containing extra packages. </p>
<p> You can create the disk image using either <i><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></i>(1) or <i><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></i>(1). For genisoimage, use a command like this: </p>
<pre>
 genisoimage -o extra-packages.iso -R -J -V EXTRA cdcontents/
</pre>
<p> Create a script that mounts the <font SIZE="-1">ISO</font> and sets up the repository. For yum, create /tmp/install.sh containing: </p>
<pre>
 mkdir /tmp/mount
 mount LABEL=EXTRA /tmp/mount
 
 cat &lt;&lt;'EOF' &gt; /etc/yum.repos.d/extra.repo
 [extra]
 name=extra
 baseurl=file:///tmp/mount
 enabled=1
 EOF
 
 yum -y install famousdatabase
</pre>
<p> For apt, create /tmp/install.sh containing: </p>
<pre>
 mkdir /tmp/mount
 mount LABEL=EXTRA /tmp/mount
 
 apt-cdrom -d=/tmp/mount add
 apt-get -y install famousdatabase
</pre>
<p> Use the <i>&#8211;attach</i> option to attach the <font SIZE="-1">CD /</font> disk image and the <i>&#8211;run</i> option to run the script: </p>
<pre>
 virt-builder fedora-20 \
   --attach extra-packages.iso \
   --run /tmp/install.sh
</pre>
<h3><font SIZE="-1">USERS AND PASSWORDS</font></h3>
<p> The <i>&#8211;root-password</i> option is used to change the root password (otherwise a random password is used). This option takes a password <tt>&quot;SELECTOR&quot;</tt> in one of the following formats:</p>
<dl>
<dt><code>&#8211;root-password</code> file:FILENAME</p>
<dd> Read the root password from <tt>&quot;FILENAME&quot;</tt>. The whole first line of this file is the replacement password. Any other lines are ignored. You should create the file with mode 0600 to ensure no one else can read it.</p>
<dt><code>&#8211;root-password</code> password:PASSWORD</p>
<dd> Set the root password to the literal string <tt>&quot;PASSWORD&quot;</tt>. </p>
<p> <code>Note: this is not secure</code> since any user on the same machine can see the cleartext password using <i><a href="/docs/linux/man/1-ps/">ps</a></i>(1).</p>
<dt><code>&#8211;root-password</code> random</p>
<dd> Choose a random password, which is printed on stdout. The password has approximately 120 bits of randomness. </p>
<p> This is the default.</p>
<dt><code>&#8211;root-password</code> disabled</p>
<dd> The root account password is disabled. This is like putting <tt>&quot;*&quot;</tt> in the password field.</p>
<dt><code>&#8211;root-password</code> locked:file:FILENAME</p>
<dd>
<dt><code>&#8211;root-password</code> locked:password:PASSWORD</p>
<dd>
<dt><code>&#8211;root-password</code> locked:random</p>
<dd> The root account is locked, but a password is placed on the account. If first unlocked (using <tt>&quot;passwd -u&quot;</tt>) then logins will use the given password.</p>
<dt><code>&#8211;root-password</code> locked</p>
<dd>
<dt><code>&#8211;root-password</code> locked:disabled</p>
<dd> The root account is locked <i>and</i> password is disabled.</dl>
<p> <i>Creating user accounts</i> </p>
<p> To create user accounts, use the <i><a href="/docs/linux/man/8-useradd/">useradd</a></i>(8) command with &#8211;firstboot-command like this: </p>
<pre>
 virt-builder --firstboot-command \
    'useradd -m -p &quot;&quot; rjones ; chage -d 0 rjones'
</pre>
<p> The above command will create an <tt>&quot;rjones&quot;</tt> account with no password, and force the user to set a password when they first log in. There are other ways to manage passwords, see <i><a href="/docs/linux/man/8-useradd/">useradd</a></i>(8) for details.</p>
<h3><font SIZE="-1">KEYBOARD LAYOUT</font></h3>
<p> Because there are so many different ways to set the keyboard layout in Linux distributions, virt-builder does not yet attempt to have a simple command line option. This section describes how to set the keyboard for some common Linux distributions. </p>
<p> <i>Keyboard layout with systemd</i> </p>
<p> For distros that use systemd <tt>&quot;localectl&quot;</tt>, use a command like this: </p>
<pre>
 virt-builder fedora-20 \
   --firstboot-command 'localectl set-keymap uk'
</pre>
<p> See <i><a href="/docs/linux/man/1-localectl/">localectl</a></i>(1) and <a rel="nofollow" href="https://www.happyassassin.net/2013/11/23/keyboard-layouts-in-fedora-20-and-previously/">https://www.happyassassin.net/2013/11/23/keyboard-layouts-in-fedora-20-and-previously/</a> for more details. </p>
<p> <i>Keyboard layout using /etc/sysconfig/keyboard</i> </p>
<p> For <font SIZE="-1">RHEL</font> ≤ 6, Fedora ≤ 18 and similar, upload or modify the keyboard configuration file using the <i>&#8211;upload</i>, <i>&#8211;write</i> or <i>&#8211;edit</i> options. For example: </p>
<pre>
 virt-builder centos-6 \
   --edit '/etc/sysconfig/keyboard: s/^KEYTABLE=.*/KEYTABLE=&quot;uk&quot;/'
</pre>
<p> The format of this file can be found documented in many places online. </p>
<p> <i>Keyboard layout with Debian-derived distros</i> </p>
<p> For Debian-derived distros using <i>/etc/default/keyboard</i>, upload or modify the keyboard file using the <i>&#8211;upload</i>, <i>&#8211;write</i> or <i>&#8211;edit</i> options. For example: </p>
<pre>
 virt-builder debian-7 \
   --edit '/etc/default/keyboard: s/^XKBLAYOUT=.*/XKBLAYOUT=&quot;gb&quot;/'
</pre>
<p> See <a rel="nofollow" href="https://wiki.debian.org/Keyboard.">https://wiki.debian.org/Keyboard.</a></p>
<h3><font SIZE="-1">LANGUAGE</font></h3>
<p> Most Linux distributions support multiple locale settings so that you can have guest messages printed in another language such as Russian. </p>
<p> However there is no single setting which controls this, since extra packages may need to be installed to support console and X fonts, and keyboard input methods. The packages required, and their configuration is highly distro-specific, and it is outside the scope of virt-builder to do this. </p>
<p> This section contains examples for some common Linux distributions. </p>
<p> <i>Setting Japanese in Fedora 20</i> </p>
<p>virt &#8211; builder fedora &#8211; 20 &#8211;size 20G &#8211;update&#8211; install @japanese &#8211; support&#8211; install @xfce&#8211; install xorg &#8211; x11 &#8211; server &#8211; Xorg, xorg &#8211; x11 &#8211; drivers, rsyslog&#8211; link / usr / lib / systemd / system / graphical.target : / etc / systemd / system / default.target&#8211; firstboot &#8211; command &#8216;localectl set-locale LANG=ja_JP.utf8&#8217; &#8211;firstboot &#8211; command &#8216;localectl set-keymap jp&#8217; &#8211;firstboot &#8211; command &#8216;systemctl isolate graphical.target&#8217;</p>
<p> <i>Setting Japanese in Debian 7 (Wheezy)</i> </p>
<p> Note that although this enables Japanese in the text console too, it is unlikely that you will see properly rendered Japanese there. However Japanese is properly rendered in X applications and terminals. </p>
<p>pkgs = locales, xfce4,<br />
    ibus, ibus &#8211; anthy,<br />
    ttf &#8211; sazanami &#8211; gothic, ttf &#8211; sazanami &#8211; mincho,<br />
    fonts &#8211; takao &#8211; mincho,<br />
    xfonts &#8211; intl &#8211; japanese, xfonts &#8211; intl &#8211; japanese &#8211; big,<br />
    iceweasel &#8211; l10n &#8211; ja, manpages &#8211; ja</p>
<p>                                          virt &#8211;<br />
                               builder debian &#8211; 7 &#8211;size 20G &#8211;install $pkgs&#8211; edit &#8216;/etc/inittab: s,^#([1-9].*respawn.*/sbin/getty.*),$1,&#8217; &#8211;edit &#8216;/etc/locale.gen: s,^#\s*ja,ja,&#8217; &#8211;write &#8216;/etc/default/locale:LANG=&#8221;ja_JP.UTF-8&#8243;&#8216; &#8211;run &#8211; command &#8220;locale-gen&#8221;</p>
<h3><font SIZE="-1">LOG FILE</font></h3>
<p> Scripts and package installation that runs at build time (<i>&#8211;run</i>, <i>&#8211;run-command</i>, <i>&#8211;install</i>, <i>&#8211;update</i>, but <i>not</i> firstboot) is logged in one of the following locations:</p>
<dl>
<dt><i>/tmp/builder.log</i></p>
<dd> On Linux, <font SIZE="-1">BSD</font> and other guests.</p>
<dt><i>C:\Tempuilder.log</i></p>
<dd> On Windows, <font SIZE="-1">DOS</font> guests.</p>
<dt><i>/builder.log</i></p>
<dd> If <i>/tmp</i> or <i>C:\Temp</i> is missing.</dl>
<p> If you don&#8217;t want the log file to appear in the final image, then use the <i>&#8211;no-logfile</i> command line option.</p>
<h3><font SIZE="-1">SSH KEYS</font></h3>
<p> The <i>&#8211;ssh-inject</i> option is used to inject ssh keys for users in the guest, so they can login without supplying a password. </p>
<p> The <tt>&quot;SELECTOR&quot;</tt> part of the option value is optional; in this case, <i>&#8211;ssh-inject</i> <tt>&quot;USER&quot;</tt> means that we look in the <i>current</i> user&#8217;s <i>~/.ssh</i> directory to find the default public <font SIZE="-1">ID</font> file. That key is uploaded. &#8220;default public <font SIZE="-1">ID&#8221;</font> is the <i>default_ID_file</i> file described in <i><a href="/docs/linux/man/1-ssh-copy-id/">ssh-copy-id</a></i>(1). </p>
<p> If specified, the <tt>&quot;SELECTOR&quot;</tt> can be in one of the following formats:</p>
<dl>
<dt><code>&#8211;ssh-inject</code> USER:file:FILENAME</p>
<dd> Read the ssh key from <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>. <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i> is usually a <i>.pub</i> file.</p>
<dt><code>&#8211;ssh-inject</code> USER:string:KEY_STRING</p>
<dd> Use the specified <tt>&quot;KEY_STRING&quot;</tt>. <tt>&quot;KEY_STRING&quot;</tt> is usually a public string like <i>ssh-rsa </i><font SIZE="-1"><i>AAAA&#8230;.</i></font><i> user [at] localhost</i>.</dl>
<p> In any case, the <i>~USER/.ssh</i> directory and the <i>~USER/.ssh/authorized_keys</i> file will be created if not existing already.</p>
<h3><font SIZE="-1">FIRST BOOT SCRIPTS</font></h3>
<p> The <i>&#8211;firstboot</i> and <i>&#8211;firstboot-command</i> options allow you to execute commands at the first boot of the guest. To do so, an init script for the guest init system is installed, which takes care of running all the added scripts and commands. </p>
<p> Supported operating systems are:</p>
<dl>
<dt>Linux</p>
<dd> Init systems supported are: systemd, System-V init (known also as sysvinit), and Upstart (using the System-V scripts). </p>
<p> Note that usually init scripts run as root, but with a more limited environment than what could be available from a normal shell: for example, <tt>$HOME</tt> may be unset or empty. </p>
<p> The output of the first boot scripts is available in the guest as <i>~root/virt-sysprep-firstboot.log</i>.</p>
<dt>Windows</p>
<dd> <i>rhsrvany.exe</i>, available from sources at <a rel="nofollow" href="https://github.com/rwmjones/rhsrvany,">https://github.com/rwmjones/rhsrvany,</a> is installed to run the first boot scripts. It is required, and the setup of first boot scripts will fail if it is not present. </p>
<p> <i>rhsrvany.exe</i> is copied from the location pointed to by the <tt>&quot;VIRT_TOOLS_DATA_DIR&quot;</tt> environment variable; if not set, a compiled-in default will be used (something like <i>/usr/share/virt-tools</i>). </p>
<p> The output of the first boot scripts is available in the guest as <i>C:\Program Files\Red Hat\Firstboot\log.txt</i>.</dl>
<h3>SUBSCRIPTION-MANAGER</h3>
<p> It is possible to automate the registration and attaching of the system using <tt>&quot;subscription-manager&quot;</tt>. This is typical on Red Hat Enterprise Linux guests. There are few options which ease this process, avoid executing commands manually and exposing passwords on command line. </p>
<p> <i>&#8211;sm-register</i> starts the registration process, and requires <i>&#8211;sm-credentials</i> to be specified; the format of the <tt>&quot;SELECTOR&quot;</tt> of <i>&#8211;sm-credentials</i> is one of the following formats:</p>
<dl>
<dt><code>&#8211;sm-credentials</code> USER:file:FILENAME</p>
<dd> Read the password for the specified <tt>&quot;USER&quot;</tt> from <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>.</p>
<dt><code>&#8211;sm-credentials</code> USER:password:PASSWORD</p>
<dd> Use the literal string <tt>&quot;PASSWORD&quot;</tt> for the specified <tt>&quot;USER&quot;</tt>.</dl>
<p> <i>&#8211;sm-attach</i> attaches the system to subscriptions; the format of its <tt>&quot;SELECTOR&quot;</tt> is one of the following:</p>
<dl>
<dt><code>&#8211;sm-attach</code> auto</p>
<dd> <tt>&quot;subscription-manager&quot;</tt> attaches to the best-fitting subscriptions for the system.</p>
<dt><code>&#8211;sm-attach</code> file:FILENAME</p>
<dd> Read the pool <font SIZE="-1">ID</font> from <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>.</p>
<dt><code>&#8211;sm-attach</code> pool:POOL</p>
<dd> Use the literal string <tt>&quot;POOL&quot;</tt> as pool <font SIZE="-1">ID.</font></dl>
<p> <i>&#8211;sm-remove</i> removes all the subscriptions from the guest, while <i>&#8211;sm-unregister</i> completely unregister the system.</p>
<h3><font SIZE="-1">INSTALLATION PROCESS</font></h3>
<p> When you invoke virt-builder, installation proceeds as follows:</p>
<dl>
<dt>&bull;</p>
<dd> The template image is downloaded. </p>
<p> If the template image is present in the cache, the cached version is used instead. (See &#8220;<font SIZE="-1">CACHING&#8221;</font>).</p>
<dt>&bull;</p>
<dd> The template signature is checked.</p>
<dt>&bull;</p>
<dd> The template is uncompressed to a tmp file.</p>
<dt>&bull;</p>
<dd> The template image is resized into the destination, using <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1).</p>
<dt>&bull;</p>
<dd> Extra disks are attached (<i>&#8211;attach</i>).</p>
<dt>&bull;</p>
<dd> A new random seed is generated for the guest.</p>
<dt>&bull;</p>
<dd> Guest customization is performed, in the order specified on the command line.</p>
<dt>&bull;</p>
<dd> SELinux relabelling is done (<i>&#8211;selinux-relabel</i>).</dl>
<h3><font SIZE="-1">IMPORTING THE DISK IMAGE</font></h3>
<p> <i>Importing into libvirt</i> </p>
<p> Import the disk image into libvirt using <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1) <i>&#8211;import</i> option. </p>
<p>virt &#8211; install&#8211; import&#8211; name guest&#8211; ram 2048 &#8211;disk path = disk.img, format = raw&#8211; os &#8211; variant fedora20</p>
<p> Notes:</p>
<dl>
<dt>1.</p>
<dd> You <i>must</i> specify the correct format. The format is <tt>&quot;raw&quot;</tt> unless you used virt-builder&#8217;s <i>&#8211;format</i> option.</p>
<dt>2.</p>
<dd> <i>&#8211;os-variant</i> is highly recommended, because it will present optimum devices to enable the guest to run most efficiently. To get a list of all variants, do: </p>
<pre>
 osinfo-query os
</pre>
<p> The above tool is provided by libosinfo package.</p>
<dt>3.</p>
<dd> You can run virt-install as root or non-root. Each works slightly differently because libvirt manages a different set of virtual machines for each user. In particular virt-manager normally shows the root-owned VMs, whereas Boxes shows the user-owned VMs, and other tools probably work differently as well.</dl>
<p> <i>Importing into OpenStack</i> </p>
<p> Import the image into Glance (the OpenStack image store) by doing: </p>
<p>glance image &#8211; create&#8211; name fedora &#8211; 20 &#8211; image&#8211; file fedora &#8211; 20.img &#8211;disk &#8211; format raw&#8211; container &#8211; format bare&#8211; is &#8211; public True</p>
<p> The <i>&#8211;file</i> parameter is the virt-builder-generated disk image. It should match virt-builder&#8217;s <i>&#8211;output</i> option. The <i>&#8211;disk-format</i> parameter should match virt-builder&#8217;s <i>&#8211;format</i> option (or <tt>&quot;raw&quot;</tt> if you didn&#8217;t use that option). The <i>&#8211;container-format</i> should always be <tt>&quot;bare&quot;</tt> since virt-builder doesn&#8217;t put images into containers. </p>
<p> You can use the <tt>&quot;glance image-show </tt>fedora-20-image<tt>&quot;</tt> command to display the properties of the image. </p>
<p> To boot up an instance of your image on a Nova compute node, do: </p>
<pre>
 nova boot fedora-20-server --image fedora-20-image \
   --flavor m1.medium
</pre>
<p> Use <tt>&quot;nova flavor-list&quot;</tt> to list possible machine flavors. Use <tt>&quot;nova list&quot;</tt> to list running instances. </p>
<p> <i>Booting directly using qemu or </i><font SIZE="-1"><i>KVM</i></font><i></i> </p>
<p> The qemu command line is not very stable or easy to use, hence libvirt should be used if possible. However a command line similar to the following could be used to boot the virtual machine: </p>
<pre>
 qemu-system-x86_64 \
   -machine accel=kvm:tcg \
   -cpu host \
   -m 2048 \
   -drive file=disk.img,format=raw,if=virtio
</pre>
<p> As with libvirt, it is very important that the correct format is chosen. It will be <tt>&quot;raw&quot;</tt> unless the <i>&#8211;format</i> option was used.</p>
<h3><font SIZE="-1">CONFIGURATION MANAGEMENT</font></h3>
<p> <i>Puppet</i> </p>
<p> To enable the Puppet agent in a guest, install the package, point the configuration at your Puppetmaster, and ensure the agent runs at boot. </p>
<p> A typical virt-builder command would be: </p>
<p>virt &#8211; builder fedora &#8211; 20 &#8211;hostname client.example.com&#8211; update&#8211; install puppet&#8211; edit &#8216;/etc/puppet/puppet.conf: s / ^\[agent\] / [agent]
 server = puppetmaster.example.com / &#8216; \<br />
   &#8211;run-command &#8216; systemctl enable puppet&#8217; \<br />
   &#8211;selinux-relabel</p>
<p> The precise instructions vary according to the Linux distro. For further information see: <a rel="nofollow" href="http://docs.puppetlabs.com/guides/installation.htm">http://docs.puppetlabs.com/guides/installation.htm</a></p>
<h3><font SIZE="-1">DEBUGGING BUILDS</font></h3>
<p> If virt-builder itself fails, then enable debugging (<i>-v</i>) and report a bug (see &#8220;<font SIZE="-1">BUGS&#8221;</font> below). </p>
<p> If virt-builder fails because some script or package it is installing fails, try using <i>&#8211;no-delete-on-failure</i> to preserve the output file, and continue reading this section. </p>
<p> If virt-builder is successful but the image doesn&#8217;t work, here are some things to try:</p>
<dl>
<dt>Use virt-rescue</p>
<dd> Run <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1) on the disk image: </p>
<pre>
 virt-rescue -a disk.img
</pre>
<p> This gives you a rescue shell. You can mount the filesystems from the disk image on <i>/sysroot</i> and examine them using ordinary Linux commands. You can also chroot into the guest to reinstall the bootloader. The virt-rescue man page has a lot more information and examples.</p>
<dt>Use guestfish</p>
<dd> Run <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) on the disk image: </p>
<pre>
 guestfish -a disk.img -i
</pre>
<p> Use guestfish commands like <tt>&quot;ll /directory&quot;</tt> and <tt>&quot;cat /file&quot;</tt> to examine directories and files.</p>
<dt>Use guestmount</p>
<dd> Mount the disk image safely on the host using <font SIZE="-1">FUSE</font> and <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1): </p>
<pre>
 mkdir /tmp/mp
 guestmount -a disk.img -i /tmp/mp
 cd /tmp/mp
</pre>
<p> To unmount the disk image do: </p>
<pre>
 fusermount -u /tmp/mp
</pre>
<dt>Add a serial console</p>
<dd> If the guest hangs during boot, it can be helpful to add a serial console to the guest, and direct kernel messages to the serial console. Adding the serial console will involve looking at the documentation for your hypervisor. To direct kernel messages to the serial console, add the following on the kernel command line: </p>
<pre>
 console=tty0 console=ttyS0,115200
</pre>
</dl>
<h3><font SIZE="-1">SOURCES OF TEMPLATES</font></h3>
<p> virt-builder reads the available sources from configuration files, with the <i>.conf</i> extension and located in the following paths:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>$XDG_CONFIG_HOME</tt>/virt-builder/repos.d/ (<tt>$XDG_CONFIG_HOME</tt> is <i></i>$HOME<i>/.config</i> if not set).</p>
<dt>&bull;</p>
<dd> <tt>$XDG_CONFIG_DIRS</tt>/virt-builder/repos.d/ (where <tt>$XDG_CONFIG_DIRS</tt> means any of the directories in that environment variable, or just <i>/etc/xdg</i> if not set)</dl>
<p> Each <i>.conf</i> file in those paths has a simple text format like the following: </p>
<pre>
 [libguestfs.org]
 uri=<a rel="nofollow" href="http://libguestfs.org/download/builder/index.asc">http://libguestfs.org/download/builder/index.asc</a>
 gpgkey=file:///etc/xdg/virt-builder/repos.d/libguestfs.gpg
</pre>
<p> The part in square brackets is the repository identifier, which is used as unique identifier. </p>
<p> The following fields can appear:</p>
<dl>
<dt>&quot;uri=URI&quot;</p>
<dd> The <font SIZE="-1">URI</font> of the index file which this repository refers to. </p>
<p> This field is required.</p>
<dt>&quot;gpgkey=URI&quot;</p>
<dd> This optional field represents the <font SIZE="-1">URI </font>(although only <i>file://</i> URIs are accepted) of the key used to sign the index file. If not present, the index file referred by <i>uri=..</i> is not signed.</p>
<dt>&quot;proxy=MODE&quot;</p>
<dd> This optional field specifies the proxy mode, to be used when downloading the index file of this repository. The possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>no</code>, <code>off</code></p>
<dd> No proxy is being used at all, even overriding the system configuration.</p>
<dt><code>system</code></p>
<dd> The proxy used is the system one.</p>
<dt><i>anything else</i></p>
<dd> Specifies the actual proxy configuration to be used, overriding the system configuration.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If not present, the assumed value is to respect the proxy settings of the system (i.e. as if <code>system</code> would be specified).</dl>
<dt>&quot;format=FORMAT&quot;</p>
<dd> This optional field specifies the format of the repository. The possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>native</code></p>
<dd> The native format of the <tt>&quot;virt-builder&quot;</tt> repository. See also &#8220;Creating and signing the index file&#8221; below.</p>
<dt><code>simplestreams</code></p>
<dd> The <font SIZE="-1">URI</font> represents the root of a Simple Streams v1.0 tree of metadata. </p>
<p> For more information about Simple Streams, see also <a rel="nofollow" href="https://launchpad.net/simplestreams.">https://launchpad.net/simplestreams.</a></dl>
</dl>
<dl>
<dt>
<dd>
<p> If not present, the assumed value is <tt>&quot;native&quot;</tt>.</dl>
</dl>
<p> For serious virt-builder use, you may want to create your own repository of templates. </p>
<p> <i>Libguestfs.org repository</i> </p>
<p> Out of the box, virt-builder downloads the file <a rel="nofollow" href="http://libguestfs.org/download/builder/index.asc">http://libguestfs.org/download/builder/index.asc</a> which is an index of available templates plus some information about each one, wrapped up in a digital signature. The command <tt>&quot;virt-builder --list&quot;</tt> lists out the information in this index file. </p>
<p> The templates hosted on libguestfs.org were created using shell scripts, kickstart files and preseed files which can be found in the libguestfs source tree, in <tt>&quot;builder/website&quot;</tt>. </p>
<p> <i>Setting up the repository</i> </p>
<p> You can set up your own site containing an index file and some templates, and then point virt-builder at the site by creating a <i>.conf</i> file pointing to it. </p>
<p> Note that if your index is signed, you will need to properly fill <i>gpgkey=..</i> in your <i>.conf</i> file, making sure to deploy also the <font SIZE="-1">GPG</font> key file. </p>
<pre>
 virt-builder --source <a rel="nofollow" href="https://example.com/builder/index.asc">https://example.com/builder/index.asc</a> \
    --fingerprint 'AAAA BBBB ...' \
    --list
</pre>
<p> You can host this on any web or <font SIZE="-1">FTP</font> server, or a local or network filesystem. </p>
<p> <i>Setting up a </i><font SIZE="-1"><i>GPG</i></font><i> key</i> </p>
<p> If you don&#8217;t have a GnuPG key, you will need to set one up. (Strictly speaking this is optional, but if your index and template files are not signed then virt-builder users will have to use the <i>&#8211;no-check-signature</i> flag every time they use virt-builder.) </p>
<p> To create a key, see the <font SIZE="-1">GPG</font> manual <a rel="nofollow" href="http://www.gnupg.org/gph/en/manual.html.">http://www.gnupg.org/gph/en/manual.html.</a> </p>
<p> Export your <font SIZE="-1">GPG</font> public key: </p>
<pre>
 gpg --export -a &quot;you [at] example.com&quot; &gt; pubkey
</pre>
<p> <i>Create the templates</i> </p>
<p> There are many ways to create the templates. For example you could clone existing guests (see <i><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></i>(1)), or you could install a guest by hand (<i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1)). To see how the templates were created for virt-builder, look at the scripts in <tt>&quot;builder/website&quot;</tt> </p>
<p> For best results when compressing the templates, use the following xz options (see <i><a href="/docs/linux/man/1-nbdkit-xz-plugin/">nbdkit-xz-plugin</a></i>(1) for further explanation): </p>
<pre>
 xz --best --block-size=16777216 disk
</pre>
<p> <i>Creating and signing the index file</i> </p>
<p> The index file has a simple text format (shown here without the digital signature): </p>
<p>[fedora &#8211; 18] name = Fedora® 18 osinfo = fedora18<br />
    arch = x86_64<br />
        file = fedora &#8211; 18.xz checksum[sha512] = &#8230; format = raw<br />
                   size = 6442450944 compressed_size = 148947524 expand = / dev / sda3</p>
<p>                                                                                      [fedora &#8211; 19] name = Fedora® 19 osinfo = fedora19<br />
                                                                              arch = x86_64<br />
                                                                                  file = fedora &#8211; 19.xz checksum[sha512] = &#8230; revision = 3 format = raw<br />
                                                                                             size = 4294967296 compressed_size = 172190964 expand = / dev / sda3</p>
<p> The part in square brackets is the <tt>&quot;os-version&quot;</tt>, which is the same string that is used on the virt-builder command line to build that <font SIZE="-1">OS.</font> </p>
<p> After preparing the <tt>&quot;index&quot;</tt> file in the correct format, clearsign it using the following command: </p>
<pre>
 gpg --clearsign --armor index
</pre>
<p> This will create the final file called <i>index.asc</i> which can be uploaded to the server (and is the <i>uri=..</i> <font SIZE="-1">URL</font>). As noted above, signing the index file is optional, but recommended. </p>
<p> The following fields can appear:</p>
<dl>
<dt>&quot;name=NAME&quot;</p>
<dd> The user-friendly name of this template. This is displayed in the <i>&#8211;list</i> output but is otherwise not significant.</p>
<dt>&quot;osinfo=ID&quot;</p>
<dd> This optional field maps the operating system to the associated libosinfo <font SIZE="-1">ID. </font> Virt-builder does not use it (yet).</p>
<dt>&quot;arch=ARCH&quot;</p>
<dd> The architecture of the operating system installed within the template. This field is required.</p>
<dt>&quot;file=PATH&quot;</p>
<dd> The path (relative to the index) of the xz-compressed template. </p>
<p> Note that absolute paths or URIs are <code>not</code> permitted here. This is because virt-builder has a &#8220;same origin&#8221; policy for templates so they cannot come from other servers.</p>
<dt>&quot;sig=PATH&quot;</p>
<dd> <code>This option is deprecated</code>. Use the checksum field instead. </p>
<p> The path (relative to the index) of the <font SIZE="-1">GPG</font> detached signature of the xz file. </p>
<p> Note that absolute paths or URIs are <code>not</code> permitted here. This is because virt-builder has a &#8220;same origin&#8221; policy for templates so they cannot come from other servers. </p>
<p> The file can be created as follows: </p>
<pre>
 gpg --detach-sign --armor -o disk.xz.sig disk.xz
</pre>
<dt>&quot;checksum[sha512]=7b882fe9b82eb0fef&#8230;&quot;</p>
<dd> The <font SIZE="-1">SHA-512</font> checksum of the <code>compressed</code> file is checked after it is downloaded. To work out the signature, do: </p>
<pre>
 sha512sum disk.xz
</pre>
<p> Note if you use this, you don&#8217;t need to sign the file, ie. don&#8217;t use <tt>&quot;sig&quot;</tt>. This option overrides <tt>&quot;sig&quot;</tt>.</p>
<dt>&quot;checksum=7b882fe9b82eb0fef&#8230;&quot;</p>
<dd> <tt>&quot;checksum&quot;</tt> is an alias for <tt>&quot;checksum[sha512]&quot;</tt>. </p>
<p> If you need to interoperate with virt-builder = 1.24.0 then you have to use <tt>&quot;checksum&quot;</tt> because that version would give a parse error with square brackets and numbers in the key of a field. This is fixed in virt-builder ≥ 1.24.1.</p>
<dt>&quot;revision=N&quot;</p>
<dd> The revision is an integer which is used to control the template cache. Increasing the revision number causes clients to download the template again even if they have a copy in the cache. </p>
<p> The revision number is optional. If omitted it defaults to <tt>1</tt>.</p>
<dt>&quot;format=raw&quot;</p>
<dd>
<dt>&quot;format=qcow2&quot;</p>
<dd> Specify the format of the disk image (before it was compressed). If not given, the format is autodetected, but generally it is better to be explicit about the intended format. </p>
<p> Note this is the source format, which is different from the <i>&#8211;format</i> option (requested output format). Virt-builder does on-the-fly conversion from the source format to the requested output format.</p>
<dt>&quot;size=NNN&quot;</p>
<dd> The virtual size of the image in bytes. This is the size of the image when uncompressed. If using a non-raw format such as qcow2 then it means the virtual disk size, not the size of the qcow2 file. </p>
<p> This field is required. </p>
<p> Virt-builder also uses this as the minimum size that users can request via the <i>&#8211;size</i> option, or as the default size if there is no <i>&#8211;size</i> option.</p>
<dt>&quot;compressed_size=NNN&quot;</p>
<dd> The compressed size of the disk image in bytes. This is just used for information (when using <i>&#8211;list &#8211;long</i>).</p>
<dt>&quot;expand=/dev/sdaX&quot;</p>
<dd> When expanding the image to its final size, instruct <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1) to expand the named partition in the guest image to fill up all available space. This works like the virt-resize <i>&#8211;expand</i> option. </p>
<p> You should usually put the device name of the guest&#8217;s root filesystem here. </p>
<p> It&#8217;s a good idea to use this, but not required. If the field is omitted then virt-resize will create an extra partition at the end of the disk to cover the free space, which is much less user-friendly.</p>
<dt>&quot;lvexpand=/dev/VolGroup/LogVol&quot;</p>
<dd> When expanding the image to its final size, instruct <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1) to expand the named logical volume in the guest image to fill up all available space. This works like the virt-resize <i>&#8211;lv-expand</i> option. </p>
<p> If the guest uses <font SIZE="-1">LVM2</font> you should usually put the <font SIZE="-1">LV</font> of the guest&#8217;s root filesystem here. If the guest does not use <font SIZE="-1">LVM2</font> or its root filesystem is not on an <font SIZE="-1">LV,</font> don&#8217;t use this option.</p>
<dt>&quot;notes=NOTES&quot;</p>
<dd> Any notes that go with this image, especially notes describing what packages are in the image, how the image was prepared, and licensing information. </p>
<p> This information is shown in the <i>&#8211;notes</i> and <i>&#8211;list</i> <i>&#8211;long</i> modes. </p>
<p> You can use multi-line notes here by indenting each new line with at least one character of whitespace (even on blank lines): </p>
<pre>
 notes=This image was prepared using
  the following kickstart script:
                                &lt;-- one space at beginning of line
  part /boot --fstype ext3
  ...
</pre>
<dt>&quot;hidden=true&quot;</p>
<dd> Using the hidden flag prevents the template from being listed by the <i>&#8211;list</i> option (but it is still installable). This is used for test images.</p>
<dt>&quot;aliases=ALIAS1 ALIAS2 &#8230;&quot;</p>
<dd> This optional field specifies a list of aliases, separated by spaces, for the image. For example, an alias could be used to always point to the latest version of a certain image, leaving the old versions available in the index instead of updating the same image (see the <tt>&quot;revision&quot;</tt> field).</dl>
<p> <i>Running virt-builder against multiple sources</i> </p>
<p> It is possible to use multiple sources with virt-builder. The recommended way is to deploy <i>.conf</i> files pointing to the index files. Another way is to specify the sources using multiple <i>&#8211;source</i> and/or <i>&#8211;fingerprint</i> options: </p>
<pre>
 virt-builder \
   --source <a rel="nofollow" href="http://example.com/s1/index.asc">http://example.com/s1/index.asc</a> \
   --source <a rel="nofollow" href="http://example.com/s2/index.asc">http://example.com/s2/index.asc</a>
</pre>
<p> You can provide N or 1 fingerprints. In the case where you provide N fingerprints, N = number of sources and there is a 1-1 correspondence between each source and each fingerprint: </p>
<p>virt &#8211; builder&#8211; source http: //example.com/s1/index.asc &#8211;fingerprint &#8216;0123 &#8230;&#8217; \<br />
   &#8211;source http://example.com/s2/index.asc &#8211;fingerprint &#8216;9876 &#8230;&#8217;</p>
<p> In the case where you provide 1 fingerprint, the same fingerprint is used for all sources. </p>
<p> You <tt>&quot;must&quot;</tt> provide at least 1 fingerprint. </p>
<p> <i>Licensing of templates</i> </p>
<p> You should be aware of the licensing of images that you distribute. For open source guests, provide a link to the source code in the <tt>&quot;notes&quot;</tt> field and comply with other requirements (eg. around trademarks). </p>
<p> <i>Formal specification of the index file</i> </p>
<p> The index file format has a formal specification defined by the flex scanner and bison parser used to parse the file. This can be found in the following files in the libguestfs source tree: </p>
<pre>
 builder/index-scan.l
 builder/index-parse.y
</pre>
<p> A tool called <i><a href="/docs/linux/man/1-virt-index-validate/">virt-index-validate</a></i>(1) is available to validate the index file to ensure it is correct. </p>
<p> Note that the parser and tool can work on either the signed or unsigned index file (ie. <i>index</i> or <i>index.asc</i>). </p>
<p> The index is always encoded in <font SIZE="-1">UTF-8.</font></p>
<h3><font SIZE="-1">CACHING</font></h3>
<p> <i>Caching templates</i> </p>
<p> Since the templates are usually very large, downloaded templates are cached in the user&#8217;s home directory. </p>
<p> The location of the cache is <i></i>$XDG_CACHE_HOME<i>/virt-builder/</i> or <i></i>$HOME<i>/.cache/virt-builder</i>. </p>
<p> You can print out information about the cache directory, including which guests are currently cached, by doing: </p>
<pre>
 virt-builder --print-cache
</pre>
<p> The cache can be deleted if you want to save space by doing: </p>
<pre>
 virt-builder --delete-cache
</pre>
<p> You can download all (current) templates to the local cache by doing: </p>
<pre>
 virt-builder --cache-all-templates
</pre>
<p> To disable the template cache, use <i>&#8211;no-cache</i>. </p>
<p> Only templates are cached. The index and detached digital signatures are not cached. </p>
<p> <i>Caching packages</i> </p>
<p> Virt-builder uses <i><a href="/docs/linux/man/1-curl/">curl</a></i>(1) to download files and it also uses the current <tt>&quot;http_proxy&quot;</tt> (etc) settings when installing packages (<i>&#8211;install</i>, <i>&#8211;update</i>). </p>
<p> You may therefore want to set those environment variables in order to maximize the amount of local caching that happens. See &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> and <i><a href="/docs/linux/man/1-curl/">curl</a></i>(1). </p>
<p> <i>Local mirrors</i> </p>
<p> To increase both speed and reliability of installing packages, you can set up a local mirror of the target distribution, and point the guest package manager at that. </p>
<p> Because of the order in which each phase of installation happens, you cannot use <i>&#8211;write</i> (to point the package manager at a repo) followed by <i>&#8211;install</i> (to install from that repo). The <i>&#8211;write</i> and <i>&#8211;install</i> steps run in the opposite order, regardless of their order on the command line. You have to do this using <i>&#8211;run-command</i> instead of <i>&#8211;install</i>. </p>
<p> Using a local mirror with Fedora </p>
<p> To install a Fedora guest using a local mirror: </p>
<pre><code>
virt - builder fedora - 20 --edit '/etc/yum.repos.d/fedora.repo: s{.*baseurl =.*}
{
    baseurl = http : // example.com/mirror/};
                     s{.*metalink =.*} {};
    ' \
   --edit ' /
            etc / yum.repos.d / fedora -
        updates.repo : s{.*baseurl =.*}
    {
        baseurl = http : // example.com/mirror-updates/};
                         s{.*metalink =.*} {};
        ' \
   --run-command ' yum -
            y update ' \
   --run-command ' yum -
            y install pkg1 pkg2...'
</code></pre>
<p> Using a local mirror with Debian </p>
<p> Assuming that you are using <tt>&quot;apt-proxy&quot;</tt> to mirror the repository, you should create a new <i>sources.list</i> file to point to your proxy (see <a rel="nofollow" href="https://help.ubuntu.com/community/AptProxy)">https://help.ubuntu.com/community/AptProxy)</a> and then do: </p>
<pre>
 virt-builder debian-7 \
   --upload sources.list:/etc/apt/sources.list \
   --run-command 'apt-get -y update' \
   --run-command 'apt-get -y install pkg1 pkg2 ...'
</pre>
<h3><font SIZE="-1">DIGITAL SIGNATURES</font></h3>
<p> Virt-builder uses <font SIZE="-1">GNU</font> Privacy Guard (GnuPG or gpg) to verify that the index and templates have not been tampered with. </p>
<p> The source points to an index file, which is optionally signed. </p>
<p> Virt-builder downloads the index and checks that the signature is valid and the signer&#8217;s fingerprint matches the specified fingerprint (ie. the one specified in <i>gpgkey=..</i> in the <i>.conf</i>, or with <i>&#8211;fingerprint</i>, in that order). </p>
<p> For checking against the built-in public key/fingerprint, this requires importing the public key into the user&#8217;s local gpg keyring (that&#8217;s just the way that gpg works). </p>
<p> When a template is downloaded, its signature is checked in the same way. </p>
<p> Although the signatures are optional, if you don&#8217;t have them then virt-builder users will have to use <i>&#8211;no-check-signature</i> on the command line. This prevents an attacker from replacing the signed index file with an unsigned index file and having virt-builder silently work without checking the signature. In any case it is highly recommended that you always create signed index and templates.</p>
<h3><font SIZE="-1">ARCHITECTURE</font></h3>
<p> Virt-builder can build a guest for any architecture no matter what the host architecture is. For example an x86-64 guest on an <font SIZE="-1">ARM</font> host. </p>
<p> However certain options may not work, specifically options that require running commands in the guest during the build process: <i>&#8211;install</i>, <i>&#8211;update</i>, <i>&#8211;run</i>, <i>&#8211;run-command</i>. You may need to replace these with their firstboot-equivalents. </p>
<p> An x86-64 host building 32 bit i686 guests should work without any special steps.</p>
<h3><font SIZE="-1">SECURITY</font></h3>
<p> Virt-builder does not need to run as root (in fact, should not be run as root), and doesn&#8217;t use setuid, <tt>&quot;sudo&quot;</tt> or any similar mechanism. </p>
<p> <i>&#8211;install</i>, <i>&#8211;update</i>, <i>&#8211;run</i> and <i>&#8211;run-command</i> are implemented using an appliance (a small virtual machine) so these commands do not run on the host. If you are using the libguestfs libvirt backend and have SELinux enabled then the virtual machine is additionally encapsulated in an SELinux container (sVirt). </p>
<p> However these options will have access to the host&#8217;s network and since the template may contain untrusted code, the code might try to access host network resources which it should not. You can use <i>&#8211;no-network</i> to prevent this. </p>
<p> Firstboot commands run in the context of the guest when it is booted, and so the security of your hypervisor / cloud should be considered. </p>
<p> Virt-builder injects a random seed into every guest which it builds. This helps to ensure that <font SIZE="-1">TCP</font> sequence numbers, UUIDs, ssh host keys etc are truly random when the guest boots. </p>
<p> You should check digital signatures and not ignore any signing errors.</p>
<h3><font SIZE="-1">CLONES</font></h3>
<p> If you wish to create many new guests of the same type, it is tempting to run virt-builder once and then copy the output file. You should <code>not</code> do this. You should run virt-builder once for each new guest you need. </p>
<p> The reason is that each clone needs to have (at least) a separate random seed, and possibly other unique features (such as filesystem UUIDs) in future versions of virt-builder. </p>
<p> Another thing you should <i>not</i> do is to boot the guest, then clone the booted disk image. The reason is that some guests create unique machine IDs, <font SIZE="-1">SSH</font> host keys and so on at first boot, and you would not want clones to have duplicate identities. </p>
<p> See also: <i><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></i>(1).</p>
<h3><font SIZE="-1">PERFORMANCE</font></h3>
<p> The most important aspect of getting good performance is caching. Templates gets downloaded into the cache the first time they are used, or if you use the <i>&#8211;cache-all-templates</i> option. See &#8220;<font SIZE="-1">CACHING&#8221;</font> above for further information. </p>
<p> Packages required for the <i>&#8211;install</i> and <i>&#8211;update</i> options are downloaded using the host network connection. Setting the <tt>&quot;http_proxy&quot;</tt>, <tt>&quot;https_proxy&quot;</tt> and <tt>&quot;ftp_proxy&quot;</tt> environment variables to point to a local web cache may ensure they only need to be downloaded once. You can also try using a local package repository, although this can be complex to set up and varies according to which Linux distro you are trying to install. </p>
<p> <i>Using &#8211;no-sync</i> </p>
<p> Use <i>&#8211;no-sync</i>. However read the caveats in the &#8220;<font SIZE="-1">OPTIONS&#8221;</font> section above, since this can cause disk corruption if not used correctly. </p>
<p> <i>Skipping virt-resize</i> </p>
<p> Virt-builder can skip the virt-resize step under certain conditions. This makes virt-builder much faster. The conditions are:</p>
<dl>
<dt>&bull;</p>
<dd> the output must be a regular file (not a block device), <code>and</code></p>
<dt>&bull;</p>
<dd> the user did <code>not</code> use the <i>&#8211;size</i> option, <code>and</code></p>
<dt>&bull;</p>
<dd> the output format is the same as the template format (usually raw).</dl>
<p> <i>pxzcat</i> </p>
<p> Virt-builder uses an internal implementation of pxzcat (parallel xzcat) if liblzma was found at build time. If liblzma was not found at build time, regular <tt>&quot;xzcat&quot;</tt> is used which is single-threaded. </p>
<p> <i>User-Mode Linux</i> </p>
<p> You can use virt-builder with the User-Mode Linux (<font SIZE="-1">UML</font>) backend. This may be faster when running virt-builder inside a virtual machine (eg. in the cloud). </p>
<p> To enable the <font SIZE="-1">UML</font> backend, read the instructions in &#8220;USER-MODE <font SIZE="-1">LINUX BACKEND&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3). </p>
<p> Currently you have to use the <i>&#8211;no-network</i> option. This should be fixed in a future version. </p>
<p> The qcow2 output format is not supported by <font SIZE="-1">UML. </font> You can only create raw-format guests.</p>
<h3><font SIZE="-1">SELINUX</font></h3>
<p> Guests which use SELinux (such as Fedora and Red Hat Enterprise Linux) require that each file has a correct SELinux label. </p>
<p> Virt-builder does not know how to give new files a label, so there are two possible strategies it can use to ensure correct labelling:</p>
<dl>
<dt>Using <i>&#8211;selinux-relabel</i></p>
<dd> This runs <i><a href="/docs/linux/man/8-setfiles/">setfiles</a></i>(8) just before finalizing the guest, which sets SELinux labels correctly in the disk image. </p>
<p> This is the recommended method.</p>
<dt><i>&#8211;touch</i> <i>/.autorelabel</i></p>
<dd> Guest templates may already contain a file called <i>/.autorelabel</i> or you may touch it. </p>
<p> For guests that use SELinux, this causes <i><a href="/docs/linux/man/8-restorecon/">restorecon</a></i>(8) to run at first boot. Guests will reboot themselves once the first time you use them, which is normal and harmless.</dl>
<p> Please note that if your guest uses SELinux, and you are doing operations on it which might create new files or change existing ones, you are recommended to use <i>&#8211;selinux-relabel</i>. This will help in making sure that files have the right SELinux labels.</p>
<h2>MACHINE READABLE OUTPUT</h2>
<p> The <i>&#8211;machine-readable</i> option can be used to make the output more machine friendly, which is useful when calling virt-builder from other programs, GUIs etc. </p>
<p> Use the option on its own to query the capabilities of the virt-builder binary. Typical output looks like this: </p>
<pre>
 $ virt-builder --machine-readable
 virt-builder
 arch
 config-file
 customize
 json-list
 pxzcat
</pre>
<p> A list of features is printed, one per line, and the program exits with status 0.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> For other environment variables which affect all libguestfs programs, see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<dl>
<dt>&quot;http_proxy&quot;</p>
<dd>
<dt>&quot;https_proxy&quot;</p>
<dd>
<dt>&quot;no_proxy&quot;</p>
<dd> Set the proxy for downloads. These environment variables (and more) are actually interpreted by <i><a href="/docs/linux/man/1-curl/">curl</a></i>(1), not virt-builder.</p>
<dt>&quot;HOME&quot;</p>
<dd> Used to determine the location of the template cache, and the location of the user&#8217; sources. See &#8220;<font SIZE="-1">CACHING&#8221;</font> and &#8220;<font SIZE="-1">SOURCES OF TEMPLATES&#8221;</font>.</p>
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
<dt>&quot;XDG_CACHE_HOME&quot;</p>
<dd> Used to determine the location of the template cache. See &#8220;<font SIZE="-1">CACHING&#8221;</font>.</p>
<dt>&quot;XDG_CONFIG_HOME&quot;</p>
<dd> Used to determine the location of the user&#8217; sources. See &#8220;<font SIZE="-1">SOURCES OF TEMPLATES&#8221;</font>.</p>
<dt>&quot;XDG_CONFIG_DIRS&quot;</p>
<dd> Used to determine the location of the system sources. See &#8220;<font SIZE="-1">SOURCES OF TEMPLATES&#8221;</font>.</dl>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1), <i><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></i>(1), <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <i><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></i>(1), <i><a href="/docs/linux/man/1-oz-install/">oz-install</a></i>(1), <i><a href="/docs/linux/man/1-gpg/">gpg</a></i>(1), <i><a href="/docs/linux/man/1-curl/">curl</a></i>(1), <i><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></i>(1), <i><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2013 Red Hat Inc.</p>
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
<dt><a href="#lbBI">MACHINE READABLE OUTPUT</a></p>
<dd>
<dt><a href="#lbBJ">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbBK">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbBL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBM">AUTHOR</a></p>
<dd>
<dt><a href="#lbBN">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbBO">LICENSE</a></p>
<dd>
<dt><a href="#lbBP">BUGS</a></p>
<dd></dl>
