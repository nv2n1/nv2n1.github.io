---
title: "casper(7)"
name: "casper"
section: "7"
letter: "c"
url: "/docs/linux/man/7-casper/"
description: "casper – a hook for initramfs-tools to boot live systems."
---

<p>casper &#8211; a hook for initramfs-tools to boot live systems.</p>
<h2>Synopsis</h2>
<p><code>BOOT=casper</code> As kernel parameter boot prompt. </p>
<h2>Description</h2>
<p>Casper is a hook for initramfs-tools used to generate an initramfs capable to boot live systems as those created by make-live. This includes the Debian-Live isos, netboot tarballs, and usb stick images and Ubuntu live cds. At boot time it will look for a (read-only) media containing a &quot;/casper&quot; directory where a root filesystems (often a compressed squashfs) is stored. If found, it will create a writable environment, using unionfs, for debian like systems to boot from. </p>
<h2>Recognized Boot Options</h2>
<dl>
<dt><code>casper-getty</code></p>
<dd>This enables a special &quot;serial&quot; login shell (experimental).</p>
<dt><code>xdebconf</code></p>
<dd>uses xdebconfigurator, if present on the rootfs, to configure X instead of the standard procedure (experimental).</p>
<dt><code>hostname=</code><i>HOSTNAME</i><code> , userfullname=</code><i>USERFULLNAME</i><code> , username=</code><i>USERNAME</i></p>
<dd>Those parameters lets you override values read from the config file.</p>
<dt><code>{keyb|kbd-chooser/method}=</code><i>KEYBOARD</i><code> , {klayout|console-setup/layoutcode}=</code><i>LAYOUT</i><code> , {kvariant|console-setup/variantcode}=</code><i>VARIANT</i><code> , {kmodel|console-setup/modelcode}=</code><i>CODE</i><code> , koptions=</code><i>OPTIONS</i></p>
<dd>Configure the running keyboard as specified, if this one misses casper behaves as if &quot;keyb=us&quot; was specified. It will be interfered from &quot;locale=&quot; if locale is only 2 lowecase letters as a special case. You could also specify console layout, variant, code, and options (no defaults).</p>
<dt><code>ip=</code><i>IFACE,ADDRESS,NETMASK,GATEWAY</i><code>[</code><i>:IFACE,ADDRESS,NETMASK,GATEWAY</i><code>]*</code></p>
<dd>Let you specify the name(s) and the options of the interface(s) that should be configured at boot time. Do not specify this if you want to use dhcp (default).</p>
<dt><code>ip[=</code>frommedia<code>]</code></p>
<dd>If this variable is set, dhcp and static configuration are just skipped and the system will use the (must be) media-preconfigured /etc/network/interfaces instead.</p>
<dt><code>{live-media|bootfrom}=</code><i>DEVICE</i></p>
<dd>If you specify one of this two equivalent forms, casper will first try to find this device for the &quot;/casper&quot; directory where the read-only root filesystem should reside. If it did not find something usable, the normal scan for block devices is performed.</p>
<dt><code>live-media-offset=</code><i>BYTES</i></p>
<dd>This way you could tell casper that your image starts at offset BYTES in the above specified or autodiscovered device, this could be useful to hide the debian-live iso or image inside another iso or image, to create &quot;clean&quot; images.</p>
<dt><code>live-media-path=</code><i>PATH</i></p>
<dd>Sets the path to the live filesystem on the medium. By default, it is set to &quot;/casper&quot; and you should not change that unless you have customized your media accordingly.</p>
<dt><code>locale=</code><i>LOCALE</i><code> | debian-installer/locale=</code><i>LOCALE</i></p>
<dd>Configure the running locale as specified, if not present the live-media rootfs configured locale will be used and if also this one misses casper behave as &quot;locale=en_US.UTF-8&quot; was specified. If only 2 lowercase letter are specified (like &quot;it&quot;), the &quot;maybe wanted&quot; locale is generated (like it:IT.UTF-8), in this case if also &quot;keyb=&quot; is unspecified is set with those 2 lowercase letters (keyb=it).</p>
<dt><code>netboot[=</code>nfs<code>|</code>cifs<code>]</code></p>
<dd>This tells casper to perform a network mount. The parameter &quot;nfsroot=&quot; (with optional &quot;nfsopts=&quot;), should specify where is the location of the root filesystem. With no args, will try cifs first, and if it fails nfs.</p>
<dt><code>persistent</code></p>
<dd>Casper will look for persistent and snapshot partitions or files labeled &quot;casper-rw&quot;, &quot;home-rw&quot;, and files called &quot;casper-sn*&quot;, &quot;home-sn*&quot; and will try to, in order: mount as /cow the first, mount the second in /home, and just copy the contents of the latter in appropriate locations (snapshots). Snapshots will be tried to be updated on reboot/shutdown. Look at <a href="/docs/linux/man/1-casper-snapshot/">casper-snapshot</a>(1) for more informations.</p>
<dt><code>nopersistent</code></p>
<dd>disables the above mentioned &quot;persistent&quot; feature, useful if the bootloader (like syslinux) has been installed with persistent enabled.</p>
<dt><code>persistent-path=</code><i>PATH</i></p>
<dd>Casper will look for persistency files in the root directory of a partition. With this parameter, the path can be configured so that you can have multiple directories on the same partition to store persistency files.</p>
<dt><code>showmounts</code></p>
<dd>This parameter will make casper to show on &quot;/&quot; the ro filesystems (mostly compressed) on /casper. This is not enabled by default because could lead to problems by applications like &quot;mono&quot; which store binary paths on installation.</p>
<dt><code>textonly</code></p>
<dd>Start up to text-mode shell prompts, disabling the graphical user interface.</p>
<dt><code>todisk=</code><i>DEVICE</i></p>
<dd>Adding this parameter, casper will try to copy the entire read-only media to the specified device before mounting the root filesystem. It probably needs a lot of free space. Subsequent boots should then skip this step and just specify the &quot;live-media=DEVICE&quot; boot parameter with the same DEVICE used this time.</p>
<dt><code>toram</code></p>
<dd>Adding this parameter, casper will try to copy the whole read-only media to the computer&#8217;s RAM before mounting the root filesystem. This could need a lot of ram, according to the space used by the read-only media.</p>
<dt><code>{preseed/file|file}=</code><i>FILE</i></p>
<dd>A path to a file present on the rootfs could be used to preseed debconf database.</p>
<dt><code>preseed/allow-network=true</code></p>
<dd>Bring up the network while running <code>preseed/early_command</code>.</p>
<dt><code>package/question=</code><i>VALUE</i></p>
<dd>All debian installed packages could be preseeded from command-line that way, beware of blanks spaces, they will interfere with parsing, use a preseed file in this case.</p>
<dt><code>uuid=</code><i>UUID</i></p>
<dd>Check that the discovered medium matches <i>UUID</i> rather than the default UUID embedded in the initramfs.</p>
<dt><code>ignore_uuid</code></p>
<dd>Do not check that any UUID embedded in the initramfs matches the discovered medium. <code>casper</code> may be told to generate a UUID by setting CASPER_GENERATE_UUID=1 when building the initramfs.</p>
<dt><code>noprompt</code></p>
<dd>Do not prompt to eject the CD on reboot. </p>
</dl>
<h2>Files</h2>
<p><code>/etc/casper.conf</code> some variables can be configured via this config file.</p>
<h2>Bugs</h2>
<p><code>casper</code> works fully on amd64, i386 and ppc, it should also run on other archs. </p>
<h2>Homepage</h2>
<p>Debian Live project &lt;<a rel="nofollow" href="http://live.debian.net/">http://live.debian.net/</a>&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-casper-snapshot/">casper-snapshot</a>(1),</code><a href="/docs/linux/man/8-initramfs-tools/">initramfs-tools</a>(8),<code><a href="/docs/linux/man/8-make-live/">make-live</a>(8),</code><a href="/docs/linux/man/5-make-live-conf/">make-live.conf</a>(5) </p>
<h2>Author</h2>
<p>casper was written by Tollef Fog Heen &lt;tfheen [at] canonical.com&gt;, Matt Zimmerman &lt;mdz [at] canonical.com&gt;, and Marco Amadori &lt;marco.amadori [at] gmail.com&gt;.</p>
<dl>
<dt>This manual page was written by Marco Amadori &lt;marco.amadori [at] gmail.com&gt;,</p>
<dd>for the Debian project (but may be used by others). </p>
</dl>
