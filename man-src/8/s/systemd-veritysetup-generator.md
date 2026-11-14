---
title: "systemd-veritysetup-generator(8)"
name: "systemd-veritysetup-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-veritysetup-generator/"
description: "systemd-veritysetup-generator – Unit generator for verity protected block devices"
---

<p>systemd-veritysetup-generator &#8211; Unit generator for verity protected block devices</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-veritysetup-generator</p>
<h2>Description</h2>
<p>systemd-veritysetup-generator is a generator that translates kernel command line options configuring verity protected block devices into native systemd units early at boot and when configuration of the system manager is reloaded. This will create <code>systemd-veritysetup [at] .service</code>(8) units as necessary. </p>
<p> Currently, only a single verity device may be set up with this generator, backing the root file system of the OS. </p>
<p> systemd-veritysetup-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>Kernel Command Line</h2>
<p>systemd-veritysetup-generator understands the following kernel command line parameters: </p>
<p> <i>systemd.verity=</i>, <i>rd.systemd.verity=</i></p>
<dl>
<dd>Takes a boolean argument. Defaults to &quot;yes&quot;. If &quot;no&quot;, disables the generator entirely. <i>rd.systemd.verity=</i> is honored only by the initial RAM disk (initrd) while <i>systemd.verity=</i> is honored by both the host system and the initrd.</dl>
<p> <i>roothash=</i></p>
<dl>
<dd>Takes a root hash value for the root file system. Expects a hash value formatted in hexadecimal characters of the appropriate length (i.e. most likely 256 bit/64 characters, or longer). If not specified via <i>systemd.verity_root_data=</i> and <i>systemd.verity_root_hash=</i>, the hash and data devices to use are automatically derived from the specified hash value. Specifically, the data partition device is looked for under a GPT partition UUID derived from the first 128bit of the root hash, the hash partition device is looked for under a GPT partition UUID derived from the last 128bit of the root hash. Hence it is usually sufficient to specify the root hash to boot from a verity protected root file system, as device paths are automatically determined from it &#8212; as long as the partition table is properly set up.</dl>
<p> <i>systemd.verity_root_data=</i>, <i>systemd.verity_root_hash=</i></p>
<dl>
<dd>These two settings take block device paths as arguments and may be used to explicitly configure the data partition and hash partition to use for setting up the verity protection for the root file system. If not specified, these paths are automatically derived from the <i>roothash=</i> argument (see above).</dl>
<p> <i>systemd.verity_root_options=</i></p>
<dl>
<dd>Takes a comma-separated list of dm-verity options. Expects the following options <code>ignore-corruption</code>, <code>restart-on-corruption</code>, <code>ignore-zero-blocks</code>, <code>check-at-most-once</code>, <code>panic-on-corruption</code> and <code>root-hash-signature</code>. See <code><a href="/docs/linux/man/8-veritysetup/">veritysetup</a></code>(8) for more details.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code>systemd-veritysetup [at] .service</code>(8), <code><a href="/docs/linux/man/8-veritysetup/">veritysetup</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8) </p>
