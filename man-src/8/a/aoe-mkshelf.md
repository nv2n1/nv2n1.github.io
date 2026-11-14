---
title: "aoe-mkshelf(8)"
name: "aoe-mkshelf"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoe-mkshelf/"
description: "aoe-mkshelf – create special device files for one shelf address"
---

<p>aoe-mkshelf &#8211; create special device files for one shelf address</p>
<h2>Synopsis</h2>
<pre><code>aoe-mkshelf {device-dir} {shelf-address}
env n_partitions=1 aoe-mkshelf {device-dir} {shelf-address}</code></pre>
<h2>Description</h2>
<p>The <i>aoe-mkshelf</i> command is not needed on systems that have udev installed and is incompatible with aoe drivers that have the <i>aoe_dyndevs</i> module parameter set to 1. </p>
<p> Systems lacking udev and having an aoe driver that uses static minor device numbers can use <i>aoe-mkshelf</i> to create the block special files necessary to access the AoE devices with the given shelf address. </p>
<p> All aoe drivers prior to <i>aoe6-50</i> use static minor device numbers. Versions 50 and up use dynamic minor device numbers when the module parameter aoe_dyndevs=1 is set. </p>
<p> If you are using static minor device numbers and your aoe driver supports only one partition per device (whole-disk partitions), then the device files must match, and you should use the <i>n_partitions</i> environment variable described below.</p>
<h3>Arguments</h3>
<dl>
<dt><code>device-dir</code></p>
<dd>This should be the name of the directory where the block device files will be created.</p>
<dt><code>shelf-address</code></p>
<dd>This is the AoE major address, or shelf address, for which to create device nodes. For example, specifying a shelf address of 1 means that the e1.* device nodes will be created in <code>device-dir</code>.</dl>
<h2>Environment Variables</h2>
<p>If the <i>n_partitions</i> variable is set in the environment, it will override the default number of partitions per aoe disk, namely 16.</p>
<h2>Example</h2>
<p>In this example, the root user on a host named <i>nai</i> creates special files for using the aoe disks in shelf 7. Then he remembers that the driver doesn&#8217;t have partition support, so the command is called again with <i>n_partitions</i> set to 1.</p>
<dl>
<dd>
<pre>nai:~# aoe-mkshelf /dev/etherd 7
nai:~# ls /dev/etherd/e7.* | wc -l
160
nai:~# rm /dev/etherd/e7.* 
nai:~# n_partitions=1 aoe-mkshelf /dev/etherd 7
nai:~# ls /dev/etherd/e7.* | wc -l
10
nai:~# </pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-discover/">aoe-discover</a></i>(8), <i><a href="/docs/linux/man/8-aoe-interfaces/">aoe-interfaces</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkdevs/">aoe-mkdevs</a></i>(8), <i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), <i><a href="/docs/linux/man/8-aoetools/">aoetools</a></i>(8), <i><a href="/docs/linux/man/7-udev/">udev</a></i>(7).</p>
<h2>Author</h2>
<p>Ed L. Cashin (ecashin [at] coraid.com)</p>
