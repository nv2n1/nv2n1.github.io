---
title: "xmdomain(5)"
name: "xmdomain"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xmdomain/"
description: "xmdomain.cfg – xm domain config file format"
---

<p>xmdomain.cfg &#8211; xm domain config file format</p>
<h2>Synopsis</h2>
<pre> /etc/xen/myxendomain
 /etc/xen/myxendomain2
 /etc/xen/auto/myxenautostarted</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/1-xm/">xm</a></code>(1) program uses python executable config files to define domains to create from scratch. Each of these config files needs to contain a number of required options, and may specify many more. </p>
<p> Domain configuration files live in /etc/xen by default, if you store config files anywhere else the full path to the config file must be specified in the <i>xm create</i> command. </p>
<p> /etc/xen/auto is a special case. Domain config files in that directory will be started automatically at system boot if the xendomain init script is enabled. The contents of /etc/xen/auto should be symlinks to files in /etc/xen to allow <i>xm create</i> to be used without full paths. </p>
<p> Options are specified by <i>name = value</i> statements in the xmdomain.cfg files.</p>
<h2>Options</h2>
<p>The following lists the most commonly used options for a domain config file.</p>
<dl>
<dt><code>kernel</code></p>
<dd>The kernel image for the domain. The format of the parameter is the fully qualified path to the kernel image file, i.e. <i>/boot/vmlinuz-2.6.12-xenU</i>.</p>
<dt><code>ramdisk</code></p>
<dd>The initial ramdisk for the domain. The format of the parameter is the fully qualified path to the initrd, i.e. <i>/boot/initrd.gz</i>. On many Linux distros you will not need a ramdisk if using the default xen kernel.</p>
<dt><code>memory</code></p>
<dd>The amount of <font SIZE="-1">RAM</font>, in megabytes, to allocate to the domain when it starts. Allocating insufficient memory for a domain may produce extremely bizarre behavior. If there isn&#8217;t enough free memory left on the machine to fulfill this request, the domain will fail to start. </p>
<p> Xen does not support overcommit of memory, so the total memory of all guests (+ 64 <font SIZE="-1">MB</font> needed for Xen) must be less than or equal to the physical <font SIZE="-1">RAM</font> in the machine.</p>
<dt><code>name</code></p>
<dd>A unique name for the domain. Attempting to create two domains with the same name will cause an error.</p>
<dt><code>root</code></p>
<dd>Specifies the root device for the domain. This is required for Linux domains, and possibly other OSes.</p>
<dt><code>nics</code></p>
<dd>The number of network interfaces allocated to the domain on boot. It defaults to 1.</p>
<dt><code>disk</code></p>
<dd>An array of block device stanzas, in the form: </p>
<pre> disk = [ &quot;stanza1&quot;, &quot;stanza2&quot;, ... ]</pre>
<p>Each stanza has 3 terms, separated by commas, &#8220;backend-dev,frontend-dev,mode&#8221;.</p>
<dl>
<dd>
<dl>
<dt><i>backend-dev</i></p>
<dd>The device in the backend domain that will be exported to the guest (frontend) domain. Supported formats include: </p>
<p> <i>phy:device</i> &#8211; export the physical device listed. The device can be in symbolic form, as in sda7, or as the hex major/minor number, as in 0x301 (which is hda1). </p>
<p> <i>file://path/to/file</i> &#8211; export the file listed as a loopback device. This will take care of the loopback setup before exporting the device.</p>
<dt><i>frontend-dev</i></p>
<dd>How the device should appear in the guest domain. The device can be in symbolic form, as in sda7, or as the hex major/minor number, as in 0x301 (which is hda1).</p>
<dt><i>mode</i></p>
<dd>The access mode for the device. There are currently 2 valid options, <i>r</i> (read-only), <i>w</i> (read/write).</dl>
</dl>
<dl>
<dd></dl>
<dt><code>vif</code></p>
<dd>An array of virtual interface stanzas in the form: </p>
<pre> vif = [ &quot;stanza1&quot;, &quot;stanza2&quot;, ... ]</pre>
<p>Each stanza specifies a set of <i>name = value</i> options separated by commas, in the form: &#8220;name1=value1, name2=value2, &#8230;&#8221; </p>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dd>
<dl>
<dt><i>bridge</i></p>
<dd>The network bridge to be used for this device. This is especially needed if multiple bridges exist on the machine.</p>
<dt><i>mac</i></p>
<dd>The <font SIZE="-1">MAC</font> address for the virtual interface. If mac is not specified, one will be randomly chosen by xen with the 00:16:3e vendor id prefix.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>vfb</code></p>
<dd>A virtual frame buffer stanza in the form: </p>
<pre> vfb = [ &quot;stanza&quot; ]</pre>
<p>The stanza specifies a set of <i>name = value</i> options separated by commas, in the form: &#8220;name1=value1, name2=value2, &#8230;&#8221; </p>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dd>
<dl>
<dt><i>type</i></p>
<dd>There are currently two valid options: <i>vnc</i> starts a <font SIZE="-1">VNC</font> server that lets you connect an external <font SIZE="-1">VNC</font> viewer, and <i>sdl</i> starts an internal viewer.</p>
<dt><i>vncdisplay</i></p>
<dd>The <font SIZE="-1">VNC</font> display number to use, defaults to the domain <font SIZE="-1">ID</font>. The <font SIZE="-1">VNC</font> server listens on port 5900 + display number.</p>
<dt><i>vnclisten</i></p>
<dd>The listening address for the <font SIZE="-1">VNC</font> server, default 127.0.0.1.</p>
<dt><i>vncunused</i></p>
<dd>If non-zero, the <font SIZE="-1">VNC</font> server listens on the first unused port above 5900.</p>
<dt><i>vncpasswd</i></p>
<dd>Overrides the XenD configured default password.</p>
<dt><i>display</i></p>
<dd>Display to use for the internal viewer, defaults to environment variable <i></i><font SIZE="-1"><i>DISPLAY</i></font><i></i>.</p>
<dt><i>xauthority</i></p>
<dd>Authority file to use for the internal viewer, defaults to environment variable <i></i><font SIZE="-1"><i>XAUTHORITY</i></font><i></i>.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>Additional Options</h2>
<p>The following options are also supported in the config file, though are far more rarely used.</p>
<dl>
<dt><code>builder</code></p>
<dd>Which builder should be used to construct the domain. This defaults to the <i>linux</i> if not specified, which is the builder for paravirtualized Linux domains.</p>
<dt><code>cpu</code></p>
<dd>Specifies which <font SIZE="-1">CPU</font> the domain should be started on, where 0 specifies the first cpu, 1 the second, and so on. This defaults to -1, which means Xen is free to pick which <font SIZE="-1">CPU</font> to start on.</p>
<dt><code>cpus</code></p>
<dd>Specifies a list of CPUs on which the domains&#8217; VCPUs are allowed to execute upon. The syntax supports ranges (0-3), and negation, ^1. For instance: </p>
<pre> cpus = &quot;0-3,5,^1&quot;</pre>
<p>Will result in CPUs 0, 2, 3, 5 being available for use by the domain.</p>
<dt><code>extra</code></p>
<dd>Extra information to append to the end of the kernel parameter line. The format is a string, the contents of which can be anything that the kernel supports. For instance: </p>
<pre> extra = &quot;4&quot;</pre>
<p>Will cause the domain to boot to runlevel 4.</p>
<dt><code>nfs_server</code></p>
<dd>The <font SIZE="-1">IP</font> address of the <font SIZE="-1">NFS</font> server to use as the root device for the domain. In order to do this you&#8217;ll need to specify <i>root=/dev/nfs</i>, and specify <i>nfs_root</i>.</p>
<dt><code>nfs_root</code></p>
<dd>The directory on the <font SIZE="-1">NFS</font> server to be used as the root filesystem. Specified as a fully qualified path, i.e. <i>/full/path/to/root/dir</i>.</p>
<dt><code>vcpus</code></p>
<dd>The number of virtual cpus to allocate to the domain. In order to use this the xen kernel must be compiled with <font SIZE="-1">SMP</font> support. </p>
<p> This defaults to 1, meaning running the domain as a <font SIZE="-1">UP</font>.</dl>
<h2>Domain Shutdown Options</h2>
<p>There are 3 options which control domain shutdown (both planned and unplanned) under certain events. The 3 events currently captured are:</p>
<dl>
<dt><code>on_shutdown</code></p>
<dd>Triggered on either an <i>xm shutdown</i> or graceful shutdown from inside the DomU.</p>
<dt><code>on_reboot</code></p>
<dd>Triggered on either an <i>xm reboot</i> or graceful reboot from inside the DomU.</p>
<dt><code>on_crash</code></p>
<dd>Triggered when a DomU goes to the crashed state for any reason.</dl>
<p> All of them take one of 4 valid states listed below.</p>
<dl>
<dt><code>destroy</code></p>
<dd>The domain will be cleaned up completely. No attempt at respawning will occur. This is what a typical shutdown would look like.</p>
<dt><code>restart</code></p>
<dd>The domain will be restarted with the same name as the old domain. This is what a typical reboot would look like.</p>
<dt><code>preserve</code></p>
<dd>The domain will not be cleaned up at all. This is often useful for crash state domains which ensures that enough evidence is to debug the real issue.</p>
<dt><code>rename-restart</code></p>
<dd>The old domain will not be cleaned up, but will be renamed so a new domain can be restarted in it&#8217;s place. The old domain will be renamed with a suffix -1, -2, etc, and assigned a new random <font SIZE="-1">UUID</font>; the new domain will keep the original name and <font SIZE="-1">UUID</font>. The old domain will release the devices that it holds, so that the new one may take them.</dl>
<p> Additionally, the &#8220;on_crash&#8221; event can also take:</p>
<dl>
<dt><code>coredump-destroy</code></p>
<dd>Dump the crashed domain&#8217;s core and then destroy it.</p>
<dt><code>coredump-restart</code></p>
<dd>Dump the crashed domain&#8217;s core and then restart it.</dl>
<h2>Examples</h2>
<p>The following are quick examples of ways that domains might be configured. They should not be considered an exhaustive set.</p>
<dl>
<dt><i>A Loopback File as Root</i></p>
<dd>
<pre> kernel = &quot;/boot/vmlinuz-2.6-xenU&quot;
 memory = 128
 name = &quot;MyLinux&quot; 
 root = &quot;/dev/hda1 ro&quot;
 disk = [ &quot;file:/var/xen/mylinux.img,hda1,w&quot; ]</pre>
<p>This creates a domain called MyLinux with 128 <font SIZE="-1">MB</font> of memory using a default xen kernel, and the file /var/xen/mylinux.img loopback mounted at hda1, which is the root filesystem.</p>
<dt><i></i><font SIZE="-1"><i>NFS</i></font><i> Root</i></p>
<dd><font SIZE="-1">FIXME:</font> write me</p>
<dt><i></i><font SIZE="-1"><i>LVM</i></font><i> Root</i></p>
<dd><font SIZE="-1">FIXME:</font> write me</p>
<dt><i>Two Networks</i></p>
<dd><font SIZE="-1">FIXME:</font> write me</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xm/">xm</a></code>(1)</p>
<h2>Author</h2>
<pre> Sean Dague &lt;sean at dague dot net&gt;</pre>
<h2>Bugs</h2>
<p>Not all options are currently documented </p>
