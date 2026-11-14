---
title: "system-config-kickstart(8)"
name: "system-config-kickstart"
section: "8"
letter: "s"
url: "/docs/linux/man/8-system-config-kickstart/"
description: "system-config-kickstart – graphical interface for creating kickstart files"
---

<p>system-config-kickstart &#8211; graphical interface for creating kickstart files</p>
<h2>Synopsis</h2>
<p><code>system-config-kickstart</code> [KSFILE]</p>
<h2>Description</h2>
<p><code>system-config-kickstart</code> provides a simple method of creating a kickstart file that can be used to automate the installation process on Red Hat Enterprise Linux, Fedora, and derived distributions. If given, the program will take its initial settings from the KSFILE provided on the command line. This allows editing of existing kickstart files. Currently, this program has some serious limitations. For example, it cannot work with LVM nor do advanced RAID and BTRFS configurations. These are supported by kickstart, but the graphical program does not provide a way to set them up nor manipulate them in existing kickstart files. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print out program usage.</p>
<dt><code>&#8211;generate FILENAME</code></p>
<dd>Examine the system and create a kickstart file that more or less matches, writing the output to FILENAME.</p>
<dt><code>&#8211;display DISPLAY#</code></p>
<dd>Specify the X display to use. </p>
</dl>
<h2>Examples</h2>
<p>To run the program type: system-config-kickstart </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;.</p>
<h2>Authors</h2>
<pre>Chris Lumens &lt;clumens [at] redhat.com&gt;
Brent Fox &lt;bfox [at] redhat.com&gt;
Tammy Fox &lt;tfox [at] redhat.com&gt;</pre>
