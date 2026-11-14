---
title: "ec2-converter(8)"
name: "ec2-converter"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ec2-converter/"
description: "ec2-converter, creates ready to bundle EC2 AMI disk images for Amazon’s EC2."
---

<p>ec2-converter, creates ready to bundle EC2 AMI disk images for Amazon&#8217;s EC2.</p>
<h2>Synopsis</h2>
<p><code>ec2-converter</code> [<font SIZE="-1">OPTIONS</font>]</p>
<h2>Description</h2>
<p><code>ec2-converter</code> creates creates ready to bundle <font SIZE="-1">EC2</font> <font SIZE="-1">AMI</font> disk images for Amazon&#8217;s <font SIZE="-1">EC2</font>.</p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd>Shows a help message and exits.</dl>
<h2>Image Options</h2>
<p>These options define the converted <font SIZE="-1">EC2</font> <font SIZE="-1">AMI</font> image.</p>
<dl>
<dt>-f <font SIZE="-1">IMAGEFILE</font> &#8211;imagefile=IMAGEFILE</p>
<dd>Image filename or directory to convert</p>
<dt>-n <font SIZE="-1">IMAGENAME</font>, &#8211;imagename=IMAGENAME</p>
<dd>Name of <font SIZE="-1">EC2</font> <font SIZE="-1">AMI</font> image to be created (default based on config name)</p>
<dt>&#8211;inputtype=INPUTTYPE</p>
<dd>Input image type valid options are: (loopbackfs, diskimage, directory)</p>
<dt>&#8211;ssh=(yes/no)</p>
<dd>Configure ssh to allow remote logins, default is yes,set to no if ssh is not installed</p>
<dt>&#8211;rpmcheck=(yes/no)</p>
<dd>Perform rpm package checks (curl/openssh-server), default is yes, set to no to override</dl>
<h2>System Directory Options</h2>
<p>These options define directories used on your system for creating the <font SIZE="-1">AMI</font> image</p>
<dl>
<dt>-t <font SIZE="-1">TMPDIR</font>, &#8211;tmpdir=TMPDIR</p>
<dd>Temporary directory to use (default: /var/tmp)</p>
<dt>&#8211;cache=CACHEDIR</p>
<dd>Cache directory to use (default: private cache)</dl>
<h2>Examples</h2>
<p>Convert a partitioned disk image created by appliance-creator </p>
<pre> ec2-converter -f testimage.raw --inputtype=diskimage</pre>
<p>Convert a loopback filesystem image </p>
<pre> ec2-converter -f /tmp/testimage.img --inputtype=loopbackfs</pre>
<p>Convert a directory containing a root filesystem </p>
<pre> ec2-converter -f /tmp/directory --inputtype=directory</pre>
<h2>Contributors</h2>
<p>Joey Boggs &lt;jboggs [at] redhat.com&gt;</p>
<h2>Bugs</h2>
<p>Report bugs to the mailing list <tt>&quot;<a rel="nofollow" href="http://www.redhat.com/mailman/listinfo/thincrust-devel-list">http://www.redhat.com/mailman/listinfo/thincrust-devel-list</a>&quot;</tt> or directly to BugZilla <tt>&quot;<a href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a>&quot;</tt> against the <tt>&quot;Fedora&quot;</tt> product, and the <tt>&quot;appliance-tools&quot;</tt> component.</p>
<h2>Copyright</h2>
<p>Copyright (C) Fedora Project 2008, and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is <font SIZE="-1">NO</font> <font SIZE="-1">WARRANTY</font>, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>project website <tt>&quot;<a rel="nofollow" href="http://thincrust.org/">http://thincrust.org/</a>&quot;</tt> </p>
