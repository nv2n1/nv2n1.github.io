---
title: "veritytab(5)"
name: "veritytab"
section: "5"
letter: "v"
url: "/docs/linux/man/5-veritytab/"
description: "veritytab – Configuration for verity block devices"
---

<p>veritytab &#8211; Configuration for verity block devices</p>
<h2>Synopsis</h2>
<p>/etc/veritytab</p>
<h2>Description</h2>
<p>The /etc/veritytab file describes verity protected block devices that are set up during system boot. </p>
<p> Empty lines and lines starting with the &quot;#&quot; character are ignored. Each of the remaining lines describes one verity protected block device. Fields are delimited by white space. </p>
<p> Each line is in the form </p>
<dl>
<dd>
<pre><i>volume-name</i> <i>data-device</i> <i>hash-device</i> <i>roothash</i> <i>options</i></pre>
</dl>
<p> The first four fields are mandatory, the remaining one is optional. </p>
<p> The first field contains the name of the resulting verity volume; its block device is set up below /dev/mapper/. </p>
<p> The second field contains a path to the underlying block data device, or a specification of a block device via &quot;UUID=&quot; followed by the UUID. </p>
<p> The third field contains a path to the underlying block hash device, or a specification of a block device via &quot;UUID=&quot; followed by the UUID. </p>
<p> The fourth field is the &quot;roothash&quot; in hexadecimal. </p>
<p> The fifth field, if present, is a comma-delimited list of options. The following options are recognized: </p>
<p> <code>ignore-corruption</code>, <code>restart-on-corruption</code>, <code>panic-on-corruption</code></p>
<dl>
<dd>Defines what to do if a data verity problem is detected (data corruption). Without these options kernel fails the IO operation with I/O error. With &quot;&#8211;ignore-corruption&quot; option the corruption is only logged. With &quot;&#8211;restart-on-corruption&quot; or &quot;&#8211;panic-on-corruption&quot; the kernel is restarted (panicked) immediately. (You have to provide way how to avoid restart loops.)</dl>
<p> <code>ignore-zero-blocks</code></p>
<dl>
<dd>Instruct kernel to not verify blocks that are expected to contain zeroes and always directly return zeroes instead. WARNING: Use this option only in very specific cases. This option is available since Linux kernel version 4.5.</dl>
<p> <code>check-at-most-once</code></p>
<dl>
<dd>Instruct kernel to verify blocks only the first time they are read from the data device, rather than every time. WARNING: It provides a reduced level of security because only offline tampering of the data device&#8217;s content will be detected, not online tampering. This option is available since Linux kernel version 4.17.</dl>
<p> <code>root-hash-signature=</code></p>
<dl>
<dd>A base64 string encoding the root hash signature prefixed by &quot;base64:&quot; or a path to roothash signature file used to verify the root hash (in kernel). This feature requires Linux kernel version 5.4 or more recent.</dl>
<p> <code>_netdev</code></p>
<dl>
<dd>Marks this veritysetup device as requiring network. It will be started after the network is available, similarly to <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5) units marked with <code>_netdev</code>. The service unit to set up this device will be ordered between remote-fs-pre.target and remote-veritysetup.target, instead of veritysetup-pre.target and veritysetup.target. </p>
<p> Hint: if this device is used for a mount point that is specified in <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), the <code>_netdev</code> option should also be used for the mount point. Otherwise, a dependency loop might be created where the mount point will be pulled in by local-fs.target, while the service to configure the network is usually only started <i>after</i> the local file system has been mounted.</dl>
<p> <code>noauto</code></p>
<dl>
<dd>This device will not be added to veritysetup.target. This means that it will not be automatically enabled on boot, unless something else pulls it in. In particular, if the device is used for a mount point, it&#8217;ll be enabled automatically during boot, unless the mount point itself is also disabled with <code>noauto</code>.</dl>
<p> <code>nofail</code></p>
<dl>
<dd>This device will not be a hard dependency of veritysetup.target. It&#8217;ll still be pulled in and started, but the system will not wait for the device to show up and be enabled, and boot will not fail if this is unsuccessful. Note that other units that depend on the enabled device may still fail. In particular, if the device is used for a mount point, the mount point itself also needs to have the <code>nofail</code> option, or the boot will fail if the device is not enabled successfully.</dl>
<p> <code>x-initrd.attach</code></p>
<dl>
<dd>Setup this verity protected block device in the initramfs, similarly to <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5) units marked with <code>x-initrd.mount</code>. </p>
<p> Although it&#8217;s not necessary to mark the mount entry for the root file system with <code>x-initrd.mount</code>, <code>x-initrd.attach</code> is still recommended with the verity protected block device containing the root file system as otherwise systemd will attempt to detach the device during the regular system shutdown while it&#8217;s still in use. With this option the device will still be detached but later after the root file system is unmounted. </p>
<p> All other verity protected block devices that contain file systems mounted in the initramfs should use this option.</dl>
<p> At early boot and when the system manager configuration is reloaded, this file is translated into native systemd units by <code><a href="/docs/linux/man/8-systemd-veritysetup-generator/">systemd-veritysetup-generator</a></code>(8).</p>
<h2>Examples</h2>
<p><code>Example 1.&nbsp;/etc/veritytab example</code> </p>
<p> Set up two verity protected block devices. One using device blocks, another using files. </p>
<dl>
<dd>
<pre>usr PARTUUID=783e45ae-7aa3-484a-beef-a80ff9c19cbb PARTUUID=21dc1dfe-4c33-8b48-98a9-918a22eb3e37 36e3f740ad502e2c25e2a23d9c7c17bf0fdad2300b7580842d4b7ec1fb0fa263 auto
data /etc/data /etc/hash a5ee4b42f70ae1f46a08a7c92c2e0a20672ad2f514792730f5d49d7606ab8fdf auto</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code>systemd-veritysetup [at] .service</code>(8), <code><a href="/docs/linux/man/8-systemd-veritysetup-generator/">systemd-veritysetup-generator</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-veritysetup/">veritysetup</a></code>(8), </p>
