---
title: "systemd-cryptsetup-generator(8)"
name: "systemd-cryptsetup-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-cryptsetup-generator/"
description: "systemd-cryptsetup-generator – Unit generator for /etc/crypttab"
---

<p>systemd-cryptsetup-generator &#8211; Unit generator for /etc/crypttab</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-cryptsetup-generator</p>
<h2>Description</h2>
<p>systemd-cryptsetup-generator is a generator that translates /etc/crypttab into native systemd units early at boot and when configuration of the system manager is reloaded. This will create <code>systemd-cryptsetup [at] .service</code>(8) units as necessary. </p>
<p> systemd-cryptsetup-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>Kernel Command Line</h2>
<p>systemd-cryptsetup-generator understands the following kernel command line parameters: </p>
<p> <i>luks=</i>, <i>rd.luks=</i></p>
<dl>
<dd>Takes a boolean argument. Defaults to &quot;yes&quot;. If &quot;no&quot;, disables the generator entirely. <i>rd.luks=</i> is honored only by initial RAM disk (initrd) while <i>luks=</i> is honored by both the main system and the initrd.</dl>
<p> <i>luks.crypttab=</i>, <i>rd.luks.crypttab=</i></p>
<dl>
<dd>Takes a boolean argument. Defaults to &quot;yes&quot;. If &quot;no&quot;, causes the generator to ignore any devices configured in /etc/crypttab (<i>luks.uuid=</i> will still work however). <i>rd.luks.crypttab=</i> is honored only by initial RAM disk (initrd) while <i>luks.crypttab=</i> is honored by both the main system and the initrd.</dl>
<p> <i>luks.uuid=</i>, <i>rd.luks.uuid=</i></p>
<dl>
<dd>Takes a LUKS superblock UUID as argument. This will activate the specified device as part of the boot process as if it was listed in /etc/crypttab. This option may be specified more than once in order to set up multiple devices. <i>rd.luks.uuid=</i> is honored only by initial RAM disk (initrd) while <i>luks.uuid=</i> is honored by both the main system and the initrd. </p>
<p> If /etc/crypttab contains entries with the same UUID, then the name, keyfile and options specified there will be used. Otherwise, the device will have the name &quot;luks-UUID&quot;. </p>
<p> If /etc/crypttab exists, only those UUIDs specified on the kernel command line will be activated in the initrd or the real root.</dl>
<p> <i>luks.name=</i>, <i>rd.luks.name=</i></p>
<dl>
<dd>Takes a LUKS super block UUID followed by an &quot;=&quot; and a name. This implies <i>rd.luks.uuid=</i> or <i>luks.uuid=</i> and will additionally make the LUKS device given by the UUID appear under the provided name. </p>
<p> This parameter is the analogue of the first <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) field <i>volume-name</i>. </p>
<p> <i>rd.luks.name=</i> is honored only by initial RAM disk (initrd) while <i>luks.name=</i> is honored by both the main system and the initrd.</dl>
<p> <i>luks.data=</i>, <i>rd.luks.data=</i></p>
<dl>
<dd>Takes a LUKS super block UUID followed by a &quot;=&quot; and a block device specification for device hosting encrypted data. </p>
<p> For those entries specified with <i>rd.luks.uuid=</i> or <i>luks.uuid=</i>, the data device will be set to the one specified by <i>rd.luks.data=</i> or <i>luks.data=</i> of the corresponding UUID. </p>
<p> LUKS data device parameter is useful for specifying encrypted data devices with detached headers specified in <i>luks.options</i> entry containing &quot;header=&quot; argument. For example, <i>rd.luks.uuid=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40 <i>rd.luks.options=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40=header=/path/to/luks.hdr <i>rd.luks.data=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40=/dev/sdx. Hence, in this case, we will attempt to unlock LUKS device assembled from data device &quot;/dev/sdx&quot; and LUKS header (metadata) put in &quot;/path/to/luks.hdr&quot; file. This syntax is for now only supported on a per-device basis, i.e. you have to specify LUKS device UUID. </p>
<p> This parameter is the analogue of the second <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) field <i>encrypted-device</i>. </p>
<p> <i>rd.luks.data=</i> is honored only by initial RAM disk (initrd) while <i>luks.data=</i> is honored by both the main system and the initrd.</dl>
<p> <i>luks.key=</i>, <i>rd.luks.key=</i></p>
<dl>
<dd>Takes a password file name as argument or a LUKS super block UUID followed by a &quot;=&quot; and a password file name. </p>
<p> For those entries specified with <i>rd.luks.uuid=</i> or <i>luks.uuid=</i>, the password file will be set to the one specified by <i>rd.luks.key=</i> or <i>luks.key=</i> of the corresponding UUID, or the password file that was specified without a UUID. </p>
<p> It is also possible to specify an external device which should be mounted before we attempt to unlock the LUKS device. systemd-cryptsetup will use password file stored on that device. Device containing password file is specified by appending colon and a device identifier to the password file path. For example, <i>rd.luks.uuid=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40 <i>rd.luks.key=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40=/keyfile:LABEL=keydev. Hence, in this case, we will attempt to mount file system residing on the block device with label &quot;keydev&quot;. This syntax is for now only supported on a per-device basis, i.e. you have to specify LUKS device UUID. </p>
<p> This parameter is the analogue of the third <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) field <i>key-file</i>. </p>
<p> <i>rd.luks.key=</i> is honored only by initial RAM disk (initrd) while <i>luks.key=</i> is honored by both the main system and the initrd.</dl>
<p> <i>luks.options=</i>, <i>rd.luks.options=</i></p>
<dl>
<dd>Takes a LUKS super block UUID followed by an &quot;=&quot; and a string of options separated by commas as argument. This will override the options for the given UUID. </p>
<p> If only a list of options, without an UUID, is specified, they apply to any UUIDs not specified elsewhere, and without an entry in /etc/crypttab. </p>
<p> This parameter is the analogue of the fourth <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) field <i>options</i>. </p>
<p> It is possible to specify an external device which should be mounted before we attempt to unlock the LUKS device. systemd-cryptsetup will assemble LUKS device by combining data device specified in <i>luks.data</i> with detached LUKS header found in &quot;header=&quot; argument. For example, <i>rd.luks.uuid=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40 <i>rd.luks.options=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40=header=/luks.hdr:LABEL=hdrdev <i>rd.luks.data=</i>b40f1abf-2a53-400a-889a-2eccc27eaa40=/dev/sdx. Hence, in this case, we will attempt to mount file system residing on the block device with label &quot;hdrdev&quot;, and look for &quot;luks.hdr&quot; on that file system. Said header will be used to unlock (decrypt) encrypted data stored on /dev/sdx. This syntax is for now only supported on a per-device basis, i.e. you have to specify LUKS device UUID. </p>
<p> <i>rd.luks.options=</i> is honored only by initial RAM disk (initrd) while <i>luks.options=</i> is honored by both the main system and the initrd.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5), <code>systemd-cryptsetup [at] .service</code>(8), <code><a href="/docs/linux/man/1-systemd-cryptenroll/">systemd-cryptenroll</a></code>(1), <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8) </p>
