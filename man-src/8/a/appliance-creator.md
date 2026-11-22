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
<p><code>appliance-creator</code> [OPTIONS]</p>
<h2>Description</h2>
<p><code>appliance-creator</code> creates pre-installed appliance images from kickstart files. Kickstart files contain the information about packages and configurations that are built into the image.</p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</dt>
<dd>Shows a help message and exits.</dd></dl>
<h2>Image Options</h2>
<p>These options define the created appliance image.</p>
<dl>
<dt>-c KSCFG, &#8211;config=KSCFG</dt>
<dd>Path to kickstart config file</dd>
<dt>-n NAME, &#8211;name=NAME</dt>
<dd>Name of appliance image to be created (default based on config name)</dd>
<dt>-f FORMAT, &#8211;format=FORMAT</dt>
<dd>Disk format, this will take any input that qemu-img convert will take (raw, qcow2, vmdk, &#8230;) Note: not all disk formats with work with all virt technologies.</dd>
<dt>&#8211;vmem=VMEM</dt>
<dd>Amount of virtual memory for appliance in MB (default: 512)</dd>
<dt>&#8211;vcpu=VCPU</dt>
<dd>Number of virtual cpus for appliance (default: 1)</dd>
<dt>&#8211;checksum</dt>
<dd>Generate a checksum for the created appliance</dd></dl>
<h2>System Directory Options</h2>
<p>These options define the way the created Appliance is packaged</p>
<dl>
<dt>-p PACKAGE, &#8211;package=PACKAGE</dt>
<dd>Package format, will package up output, disk images and meta into a package. Currently only &#8220;zip&#8221;, &#8220;zip.64&#8221;, &#8220;tar&#8221;, &#8220;tar.gz&#8221;, &#8220;tar.bz2&#8221; are supported. (default is &#8220;none&#8221;)</dd>
<dt>-i INCLUDE, &#8211;include=INCLUDE</dt>
<dd>path to a file or dir to include in the appliance package</dd>
<dt>-o OUTDIR, &#8211;outdir=OUTDIR</dt>
<dd>output directory</dd></dl>
<h2>System Directory Options</h2>
<p>These options define directories used on your system for creating the appliance image</p>
<dl>
<dt>-t TMPDIR, &#8211;tmpdir=TMPDIR</dt>
<dd>Temporary directory to use (default: /var/tmp)</dd>
<dt>&#8211;cache=CACHEDIR</dt>
<dd>Cache directory to use (default: private cache)</dd></dl>
<h2>Debugging options</h2>
<p>These options define extra options for debugging</p>
<dl>
<dt>-d, &#8211;debug</dt>
<dd>Output debugging information</dd>
<dt>-v, &#8211;verbose</dt>
<dd>Output verbose progress information</dd>
<dt>&#8211;logfile=FILE</dt>
<dd>Save debug information to FILE</dd></dl>
<h2>Examples</h2>
<p>Appliance Example </p>
<p> appliance-creator \<br/>
&nbsp;<wbr>-n ThinCrust &#8211;config /usr/share/doc/appliance-tools-%{version}/aos-rawhide.ks \ &#8211;cache=/var/tmp/act</p>
<h2>Contributors</h2>
<p>David Huff, Joey Boggs, Bryan kearney, Daniel P. Berrange, and a team of other contributors.</p>
<h2>Bugs</h2>
<p>Report bugs to the mailing list <tt>&quot;<a rel="nofollow" href="http://www.redhat.com/mailman/listinfo/thincrust-devel-list">http://www.redhat.com/mailman/listinfo/thincrust-devel-list</a>&quot;</tt> or directly to BugZilla <tt>&quot;<a href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a>&quot;</tt> against the <tt>&quot;Fedora&quot;</tt> product, and the <tt>&quot;appliance-tools&quot;</tt> component.</p>
<h2>Copyright</h2>
<p>Copyright (C) Fedora Project 2008, and various contributors. This is free software. You may redistribute copies of it under the terms of the GNU General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p><tt>&quot;<a href="/docs/linux/man/1-qemu-img/">qemu-img</a>(1)&quot;</tt>,<tt>&quot;virt-iamge(1),&quot;virt-iamge(5) project website &quot;<a rel="nofollow" href="http://thincrust.org/">http://thincrust.org/</a>&quot;&quot;&quot;</tt></p>
<h2>Pod Errors</h2>
<p>Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 138:</dt>
<dd>Unterminated C&lt;C&lt;&#8230;&gt;&gt; sequence </dd>
</dl>
