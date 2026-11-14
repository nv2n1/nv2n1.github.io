---
title: "systemd-veritysetup(8)"
name: "systemd-veritysetup"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-veritysetup/"
description: "systemd-veritysetup [at] .service, systemd-veritysetup – Disk verity protection logic"
---

<p>systemd-veritysetup [at] .service, systemd-veritysetup &#8211; Disk verity protection logic</p>
<h2>Synopsis</h2>
<p>systemd-veritysetup [at] .service </p>
<p> /lib/systemd/systemd-veritysetup</p>
<h2>Description</h2>
<p>systemd-veritysetup [at] .service is a service responsible for setting up verity protection block devices. It should be instantiated for each device that requires verity protection. </p>
<p> At early boot and when the system manager configuration is reloaded kernel command line configuration for verity protected block devices is translated into systemd-veritysetup [at] .service units by <code><a href="/docs/linux/man/8-systemd-veritysetup-generator/">systemd-veritysetup-generator</a></code>(8). </p>
<p> systemd-veritysetup [at] .service calls <code>systemd-veritysetup</code>.</p>
<h2>Commands</h2>
<p>The following commands are understood by <code>systemd-veritysetup</code>: </p>
<p> <code>attach</code> <i>volume</i> <i>datadevice</i> <i>hashdevice</i> <i>roothash</i> [<i>option</i>&#8230;]</p>
<dl>
<dd>Create a block device <i>volume</i> using <i>datadevice</i> and <i>hashdevice</i> as the backing devices. <i>roothash</i> forms the root of the tree of hashes stored on <i>hashdevice</i>. See m[blue]<code>Kernel dm-verity</code>m[]<font SIZE="-2">[1]</font> documentation for details.</dl>
<p> <code>detach</code> <i>volume</i></p>
<dl>
<dd>Detach (destroy) the block device <i>volume</i>.</dl>
<p> <code>help</code></p>
<dl>
<dd>Print short information about command syntax.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-veritysetup-generator/">systemd-veritysetup-generator</a></code>(8), <code><a href="/docs/linux/man/8-veritysetup/">veritysetup</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Kernel dm-verity</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/verity.html">https://www.kernel.org/doc/html/latest/admin-guide/device-mapper/verity.html</a></dl>
