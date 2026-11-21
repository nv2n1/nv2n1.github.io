---
title: "cbootimage(1)"
name: "cbootimage"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cbootimage/"
description: "cbootimage – tegra BCT compiler"
---

<h2 class="name">NAME</h2>
<p> cbootimage &#8211; tegra BCT compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>cbootimage</code> [ <i>options</i> ] configfile [ <i>inputimage</i> ] <i>outputimage</i></p>
<h2>DESCRIPTION</h2>
<p> This program is used to create images suitable to place into the boot flash of a device using a Tegra SoC. There are two primary modes of operation of cbootimage: </p>
<dl>
<dt>step]</dt>
<dd> Compile a textual representation of a BCT into a binary image.</dd>
<dt>step]</dt>
<dd> Generate an entire boot image from a previously compiled BCT and a bootloader binary. </dd>
</dl>
<h3>Platforms supported</h3>
<dl>
<dt>&bull;</dt>
<dd> <code>Tegra20</code></dd>
<dt>&bull;</dt>
<dd> <code>Tegra30</code></dd>
<dt>&bull;</dt>
<dd> <code>Tegra114</code></dd>
<dt>&bull;</dt>
<dd> <code>Tegra124</code></dd>
<dt>&bull;</dt>
<dd> <code>Tegra132</code></dd>
<dt>&bull;</dt>
<dd> <code>Tegra210</code> </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>-gbct</code></dt>
<dd> Generate the new bct file from the given config file.</dd>
<dt><code>-h, &#8211;help, -?</code></dt>
<dd> Print help text and exit. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;debug</code></dt>
<dd> Output debugging information.</dd>
<dt><code>-o</code><i>odm_data</i></dt>
<dd> Specify the odm_data value (in hex).</dd>
<dt><code>-t, &#8211;tegra </code><i>NN</i></dt>
<dd> Select target device. Must be one of: 20, 30, 114, 124, 132, 210.</dd>
<dt><code>-s, &#8211;ssoc </code><i>tegraNN</i></dt>
<dd> Select target device. Must be one of: tegra20, tegra30, tegra114, tegra124, tegra32, tegra210.</dd>
<dt><code>-u &#8211;update</code></dt>
<dd> Copy input image data and update bct configs into new image file </dd>
</dl>
<h2>EXAMPLES</h2>
<p> To generate a bct file from a text description obtained either through <a href="/docs/linux/man/1-bct_dump/">bct_dump</a>(1) or cbootimage-configs: </p>
<pre>
$ cbootimage -gbct -t124 PM375_Hynix_2GB_H5TC4G63AFR_RDA_924MHz.bct.cfg PM375_Hynix_2GB_H5TC4G63AFR_RDA_924MHz.bct
New BCT file PM375_Hynix_2GB_H5TC4G63AFR_RDA_924MHz.bct has been successfully generated!
</pre>
<p> To generate a boot image file including the newly generated bct: </p>
<pre>
cbootimage -t124 jetson-tk1-emmc.img.cfg jetson-tk1-emmc.img
Image file jetson-tk1-emmc.img has been successfully generated!
</pre>
<h2>RETURN VALUE</h2>
<p> If any error occurs a non zero exit status is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tegrarcm/">tegrarcm</a>(1),</code><a href="/docs/linux/man/1-bct_dump/">bct_dump</a>(1) </p>
