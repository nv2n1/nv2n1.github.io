---
title: "appliance-creator(8)"
name: "appliance-creator"
section: "8"
letter: "a"
url: "/docs/linux/man/8-appliance-creator/"
description: "appliance-creator, creates pre-installed appliance images and meta-data."
---

<p>appliance-creator, creates pre-installed appliance images and meta-data.</p>
<h2>Synopsis</h2>
<p><code>appliance-creator</code> [<font SIZE="-1">OPTIONS</font>]</p>
<h2>Description</h2>
<p><code>appliance-creator</code> creates pre-installed appliance images from kickstart files. Kickstart files contain the information about packages and configurations that are built into the image.</p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd>Shows a help message and exits.</dl>
<h2>Image Options</h2>
<p>These options define the created appliance image.</p>
<dl>
<dt>-c <font SIZE="-1">KSCFG</font>, &#8211;config=KSCFG</p>
<dd>Path to kickstart config file</p>
<dt>-n <font SIZE="-1">NAME</font>, &#8211;name=NAME</p>
<dd>Name of appliance image to be created (default based on config name)</p>
<dt>-f <font SIZE="-1">FORMAT</font>, &#8211;format=FORMAT</p>
<dd>Disk format, this will take any input that qemu-img convert will take (raw, qcow2, vmdk, &#8230;) Note: not all disk formats with work with all virt technologies.</p>
<dt>&#8211;vmem=VMEM</p>
<dd>Amount of virtual memory for appliance in <font SIZE="-1">MB</font> (default: 512)</p>
<dt>&#8211;vcpu=VCPU</p>
<dd>Number of virtual cpus for appliance (default: 1)</p>
<dt>&#8211;checksum</p>
<dd>Generate a checksum for the created appliance</dl>
<h2>System Directory Options</h2>
<p>These options define the way the created Appliance is packaged</p>
<dl>
<dt>-p <font SIZE="-1">PACKAGE</font>, &#8211;package=PACKAGE</p>
<dd>Package format, will package up output, disk images and meta into a package. Currently only &#8220;zip&#8221;, &#8220;zip.64&#8221;, &#8220;tar&#8221;, &#8220;tar.gz&#8221;, &#8220;tar.bz2&#8221; are supported. (default is &#8220;none&#8221;)</p>
<dt>-i <font SIZE="-1">INCLUDE</font>, &#8211;include=INCLUDE</p>
<dd>path to a file or dir to include in the appliance package</p>
<dt>-o <font SIZE="-1">OUTDIR</font>, &#8211;outdir=OUTDIR</p>
<dd>output directory</dl>
<h2>System Directory Options</h2>
<p>These options define directories used on your system for creating the appliance image</p>
<dl>
<dt>-t <font SIZE="-1">TMPDIR</font>, &#8211;tmpdir=TMPDIR</p>
<dd>Temporary directory to use (default: /var/tmp)</p>
<dt>&#8211;cache=CACHEDIR</p>
<dd>Cache directory to use (default: private cache)</dl>
<h2>Debugging options</h2>
<p>These options define extra options for debugging</p>
<dl>
<dt>-d, &#8211;debug</p>
<dd>Output debugging information</p>
<dt>-v, &#8211;verbose</p>
<dd>Output verbose progress information</p>
<dt>&#8211;logfile=FILE</p>
<dd>Save debug information to <font SIZE="-1">FILE</font></dl>
<h2>Examples</h2>
<p>Appliance Example </p>
<p> appliance-creator \<br />
&nbsp;<wbr>-n ThinCrust &#8211;config /usr/share/doc/appliance-tools-%{version}/aos-rawhide.ks \ &#8211;cache=/var/tmp/act</p>
<h2>Contributors</h2>
<p>David Huff, Joey Boggs, Bryan kearney, Daniel P. Berrange, and a team of other contributors.</p>
<h2>Bugs</h2>
<p>Report bugs to the mailing list <tt>&quot;<a rel="nofollow" href="http://www.redhat.com/mailman/listinfo/thincrust-devel-list">http://www.redhat.com/mailman/listinfo/thincrust-devel-list</a>&quot;</tt> or directly to BugZilla <tt>&quot;<a href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a>&quot;</tt> against the <tt>&quot;Fedora&quot;</tt> product, and the <tt>&quot;appliance-tools&quot;</tt> component.</p>
<h2>Copyright</h2>
<p>Copyright (C) Fedora Project 2008, and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is <font SIZE="-1">NO</font> <font SIZE="-1">WARRANTY</font>, to the extent permitted by law.</p>
<h2>See Also</h2>
<p><tt>&quot;<a href="/docs/linux/man/1-qemu-img/">qemu-img</a>(1)&quot;</tt>,<tt>&quot;<a href="/docs/linux/man/1-virt-iamge/">virt-iamge</a>(1),&quot;<a href="/docs/linux/man/5-virt-iamge/">virt-iamge</a>(5) project website &quot;<a rel="nofollow" href="http://thincrust.org/">http://thincrust.org/</a>&quot;&quot;&quot;</tt></p>
<h2>Pod Errors</h2>
<p>Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 138:</p>
<dd>Unterminated C&lt;C&lt;&#8230;&gt;&gt; sequence </p>
</dl>
