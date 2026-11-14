---
title: "libguestfs-tools-conf(5)"
name: "libguestfs-tools-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libguestfs-tools-conf/"
description: "libguestfs-tools.conf – configuration file for guestfish, guestmount, virt-rescue"
---

<p>libguestfs-tools.conf &#8211; configuration file for guestfish, guestmount, virt-rescue</p>
<h2>Synopsis</h2>
<pre> /etc/libguestfs-tools.conf
 $XDG_CONFIG_DIRS/libguestfs/libguestfs-tools.conf
 $HOME/.libguestfs-tools.rc
 $XDG_CONFIG_HOME/libguestfs/libguestfs-tools.conf</pre>
<h2>Description</h2>
<p><i>libguestfs-tools.conf</i> (or <i></i>$HOME<i>/.libguestfs-tools.rc</i>) changes the defaults for the following programs only:</p>
<dl>
<dt>&bull;</p>
<dd><i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1)</p>
<dt>&bull;</p>
<dd><i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1)</p>
<dt>&bull;</p>
<dd><i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1)</dl>
<p> There is currently only one setting which is controlled by this file. Adding (or uncommenting): </p>
<pre><code>read_only = true;</code></pre>
<p> changes these programs so they act as if the <i>&#8211;ro</i> flag was given on the command line. You can use this to make the programs safe against accidental modification of a live guest (users would have to explicitly add the <i>&#8211;rw</i> flag to modify guests). This is not the default because it is not backwards compatible. See also &#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). Note that <code>the semicolon is required</code>. This file is parsed by the libconfig library. For more information about the format, see: <a rel="nofollow" href="http://www.hyperrealm.com/libconfig/libconfig_manual.html">http://www.hyperrealm.com/libconfig/libconfig_manual.html</a></p>
<h2>File Location</h2>
<p>The order of the configuration files being read is, by importance:</p>
<dl>
<dt>&bull;</p>
<dd><tt>$XDG_CONFIG_HOME</tt>/libguestfs/libguestfs-tools.conf (<tt>$XDG_CONFIG_HOME</tt> is <i></i>$HOME<i>/.config</i> if not set).</p>
<dt>&bull;</p>
<dd><tt>$HOME</tt>/.libguestfs-tools.rc</p>
<dt>&bull;</p>
<dd><tt>$XDG_CONFIG_DIRS</tt>/libguestfs/libguestfs-tools.conf (where <tt>$XDG_CONFIG_DIRS</tt> means any of the directories in that environment variable, or just <i>/etc/xdg</i> if not set)</p>
<dt>&bull;</p>
<dd>/etc/libguestfs-tools.conf</dl>
<p> This means local users can override the system configuration by copying the configuration file (or creating it anew) into <i></i>$XDG_CONFIG_HOME<i>/libguestfs/libguestfs-tools.conf</i>. </p>
<p> <i>/etc/libguestfs-tools.conf</i> and <i></i>$HOME<i>/.libguestfs-tools.rc</i> are the old non-XDG paths which are read for compatibility.</p>
<h2>See Also</h2>
<p>&#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/latest/.">http://standards.freedesktop.org/basedir-spec/latest/.</a></p>
<h2>Authors</h2>
<p>Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>Copyright</h2>
<p>Copyright (C) 2011-2016 Red Hat Inc.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>Bugs</h2>
<p>To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd>The version of libguestfs.</p>
<dt>&bull;</p>
<dd>Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd>Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd>Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
