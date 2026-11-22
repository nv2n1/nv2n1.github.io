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
<p><code>ec2-converter</code> [OPTIONS]</p>
<h2>Description</h2>
<p><code>ec2-converter</code> creates creates ready to bundle EC2 AMI disk images for Amazon&#8217;s EC2.</p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</dt>
<dd>Shows a help message and exits.</dd></dl>
<h2>Image Options</h2>
<p>These options define the converted EC2 AMI image.</p>
<dl>
<dt>-f IMAGEFILE &#8211;imagefile=IMAGEFILE</dt>
<dd>Image filename or directory to convert</dd>
<dt>-n IMAGENAME, &#8211;imagename=IMAGENAME</dt>
<dd>Name of EC2 AMI image to be created (default based on config name)</dd>
<dt>&#8211;inputtype=INPUTTYPE</dt>
<dd>Input image type valid options are: (loopbackfs, diskimage, directory)</dd>
<dt>&#8211;ssh=(yes/no)</dt>
<dd>Configure ssh to allow remote logins, default is yes,set to no if ssh is not installed</dd>
<dt>&#8211;rpmcheck=(yes/no)</dt>
<dd>Perform rpm package checks (curl/openssh-server), default is yes, set to no to override</dd></dl>
<h2>System Directory Options</h2>
<p>These options define directories used on your system for creating the AMI image</p>
<dl>
<dt>-t TMPDIR, &#8211;tmpdir=TMPDIR</dt>
<dd>Temporary directory to use (default: /var/tmp)</dd>
<dt>&#8211;cache=CACHEDIR</dt>
<dd>Cache directory to use (default: private cache)</dd></dl>
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
<p>Copyright (C) Fedora Project 2008, and various contributors. This is free software. You may redistribute copies of it under the terms of the GNU General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>project website <tt>&quot;<a rel="nofollow" href="http://thincrust.org/">http://thincrust.org/</a>&quot;</tt> </p>
