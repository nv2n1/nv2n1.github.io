---
title: "aoe-mkdevs(8)"
name: "aoe-mkdevs"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoe-mkdevs/"
description: "aoe-mkdevs – create special device files for aoe driver"
---

<p>aoe-mkdevs &#8211; create special device files for aoe driver</p>
<h2>Synopsis</h2>
<pre><code>aoe-mkdevs {device-dir}
env n_partitions=1 aoe-mkdevs {device-dir}</code></pre>
<h2>Description</h2>
<p>The <i>aoe-mkdevs</i> command is deprecated in favor of udev. Systems with udev do not need to use the <i>aoe-mkdevs</i> or <i>aoe-mkself</i> commands, because udev will create device nodes as needed. </p>
<p> Systems without udev use <i>aoe-mkdevs</i> to create the character special files necessary to control the aoe driver. The <i>aoe-mkdevs</i> command uses <i>aoe-mkshelf</i> to also create block special files. </p>
<p> The aoe drivers after version 49 support dynamic minor device numbers so that a greater number of devices can be supported. The <i>aoe-mkdevs</i> command is incompatible with dynamic device numbers. If your system lacks udev, and you are using an aoe driver version 50 or above, use the aoe_dyndevs=0 module option to force the aoe driver to use static device numbers. </p>
<p> If you are not using dynamic device numbers, and you built your aoe driver to support only one partition per device (whole-disk partitions), then the device files must match, and you should use the <i>n_partitions</i> environment variable described below.</p>
<h3>Arguments</h3>
<dl>
<dt><code>device-dir</code></p>
<dd>This should be the name of the directory where the special device files will be created.</dl>
<h2>Environment Variables</h2>
<p>If the <i>n_partitions</i> variable is set in the environment, it will override the default number of partitions per aoe disk, namely 16.</p>
<h2>Example</h2>
<p>In this example, the root user on a host named <i>nai</i> creates special files for using the aoe disks in shelf 7. After remembering that the driver doesn&#8217;t have partition support, this sysadmin gets rid of the mismatching device nodes and calls <i>aoe-mkdevs</i> again with <i>n_partitions</i> set to 1.</p>
<dl>
<dd>
<pre>nai:~# rm -rf /dev/etherd 
nai:~# aoe-mkdevs /dev/etherd
nai:~# ls /dev/etherd | wc -l
1603
nai:~# rm -rf /dev/etherd
nai:~# n_partitions=1 aoe-mkdevs /dev/etherd
nai:~# ls /dev/etherd | wc -l
103</pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-discover/">aoe-discover</a></i>(8), <i><a href="/docs/linux/man/8-aoe-interfaces/">aoe-interfaces</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkshelf/">aoe-mkshelf</a></i>(8), <i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), <i><a href="/docs/linux/man/8-aoetools/">aoetools</a></i>(8), <i><a href="/docs/linux/man/7-udev/">udev</a></i>(7).</p>
<h2>Author</h2>
<p>Ed L. Cashin (ecashin [at] coraid.com)</p>
