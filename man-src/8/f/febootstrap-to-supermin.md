---
title: "febootstrap-to-supermin(8)"
name: "febootstrap-to-supermin"
section: "8"
letter: "f"
url: "/docs/linux/man/8-febootstrap-to-supermin/"
---

febootstrap-to-supermin - Convert febootstrap root to supermin appliance.

<h2>Synopsis</h2>

<pre> febootstrap-to-supermin DIR supermin.img hostfiles.txt</pre>

<h2>Description</h2>

<i>febootstrap-to-supermin</i> converts the filesystem created by <i><a HREF="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8) into a supermin appliance. The term ``supermin appliance'' is described in the documentation below. First you should be familiar with <i><a HREF="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8) and <i><a HREF="/docs/linux/man/8-febootstrap-to-initramfs/">febootstrap-to-initramfs</a></i>(8).

<h2>Parameters</h2>

<tt>&quot;DIR&quot;</tt> is the directory created by febootstrap (ie. the output of febootstrap and the input to this program). 

 <tt>&quot;supermin.img&quot;</tt> is the name of the supermin appliance that this program creates, and <tt>&quot;hostfiles.txt&quot;</tt> is the name of the list of hostfiles that this program creates. (ie. the outputs of this program).

<h2>Supermin Appliance</h2>

A supermin appliance is a very specialized, highly minimized appliance which can be reconstructed on-the-fly at runtime into an ordinary (initramfs) appliance. 

 The normal appliance is a self-contained Linux operating system, based on the Fedora/RHEL/CentOS Linux distro. So it contains a complete copy of all the libraries and programs needed, like kernel, libc, bash, coreutils etc etc. 

 The supermin appliance removes the kernel and all the executable libraries and programs from the appliance. That just leaves a skeleton of directories, config files and some data files, which is obviously massively smaller than the normal appliance. At runtime we rebuild the appliance on-the-fly from the libraries and programs on the host (eg. pulling in the real /lib/libc.so, the real /bin/bash etc.) 

 Although this process of rebuilding the appliance each time sounds slow, it turns out to be faster than using a prebuilt appliance. (Most of the saving comes from not compressing the appliance - it transpires that decompressing the appliance is the slowest part of the whole boot sequence). On my machine, a new appliance can be built in under a fifth of a second, and the boot time is several seconds shorter. 

 The big advantage of the supermin appliance for distributions like Fedora is that it gets security fixes automatically from the host, so there is no need to rebuild the whole appliance for a security update in some underlying library. 

 There are several <i>disadvantages</i>: 

 It won't work at all except in very narrow, controlled cases like the Fedora packaging case. We control the dependencies of the appliance RPM tightly to ensure that the required binaries are actually present on the host. 

 Furthermore there are certain unlikely changes in the packages on the host which could break a supermin appliance, eg. an updated library which depends on an additional data file. 

 Also supermin appliances are subjected to changes in the host kernel which might break compatibility with qemu --- these are, of course, real bugs in any case. 

 Lastly, supermin appliances really can't be moved between branches of distributions (eg. built on Fedora 12 and moved to Fedora 10) because they are not self-contained and they rely on certain libraries being around. You shouldn't do this anyway. 

 Use supermin appliances with caution.

<h3>ANATOMY OF A SUPERMIN APPLIANCE</h3>

A supermin appliance consists of two files:
<dl><dt>supermin.img
</dt><dd>The image file (conventionally called <tt>&quot;supermin.img&quot;</tt>, but you can call it anything you want) is the skeleton initramfs. This is like an initramfs built by <i><a HREF="/docs/linux/man/8-febootstrap-to-initramfs/">febootstrap-to-initramfs</a></i>(8), but all libraries and binaries are removed.
</dd><dt>hostfiles.txt
</dt><dd>This plain text file contains a list of files that we need to add back from the host at runtime. ie. It's the list of libraries and binaries that we removed when we constructed <tt>&quot;supermin.img&quot;</tt>. 
 This file usually contains wildcards. This is because we don't want the file to break on minor updates to libraries, so for example instead of listing 
 <pre> lib64/libreadline.so.6.1.2</pre>the file contains 
 <pre> lib64/libreadline.so.6.*</pre></dd></dl>

<h3>RECONSTRUCTING AN INITRAMFS FROM A SUPERMIN APPLIANCE</h3>

The program <i><a HREF="/docs/linux/man/8-febootstrap-supermin-helper/">febootstrap-supermin-helper</a></i>(8) can be used to reconstruct a full initramfs from <tt>&quot;supermin.img&quot;</tt> and <tt>&quot;hostfiles.txt&quot;</tt> (plus, naturally, the required programs and libraries in the host filesystem). 

 See that man page for details.

<h3>RESTRICTION: UNREADABLE BINARIES ON THE HOST</h3>

Some binaries on the host are not publically readable. For example: 

 <pre> $ ll /usr/libexec/pt_chown 
 -rws--x--x 1 root root 28418 2009-09-28 13:42 /usr/libexec/pt_chown
 $ ll /usr/bin/chsh 
 -rws--x--x 1 root root 18072 2009-10-05 16:28 /usr/bin/chsh</pre>These binaries cause a problem when reconstructing the supermin appliance, because we'd like to copy them into the final appliance, and usually that process is done as non-root. Currently the only solution is that you should remove these problematic binaries from the appliance.

<h2>Example</h2>

Create a basic Fedora directory and turn it into a supermin image. 

 <i></i><i>NB</i><i></i> You must only build ``Rawhide on Rawhide''. If using another Fedora branch, you must change <tt>&quot;rawhide&quot;</tt> below as appropriate, eg to <tt>&quot;fedora-12&quot;</tt>. 

 <pre> $ febootstrap rawhide /tmp/fedora
 $ febootstrap-to-supermin /tmp/fedora supermin.img hostfiles.txt</pre>Examine the resulting files: 

 <pre> $ cpio -itv &lt; supermin.img | less
 $ less hostfiles.txt</pre>Reconstruct the final kernel and initramfs. 

 <i></i><i>NB</i><i></i> The first time you run this, it will be slow because the required host files are not in cache. With a ``hot cache'' it should be lightning fast. Run it several times to get representative timings. 

 <pre> $ febootstrap-supermin-helper supermin.img hostfiles.txt \
 /tmp/kernel /tmp/initrd</pre>You would boot the final image like this, although in this example it probably won't work unless you add a <tt>&quot;/init&quot;</tt> file to the appliance (see the discussion in <i><a HREF="/docs/linux/man/8-febootstrap-to-initramfs/">febootstrap-to-initramfs</a></i>(8)). 

 <pre> $ qemu -m 1024 -kernel /tmp/kernel -initrd /tmp/initrd [etc...]</pre>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8), <i><a HREF="/docs/linux/man/8-febootstrap-to-initramfs/">febootstrap-to-initramfs</a></i>(8), <i><a HREF="/docs/linux/man/8-febootstrap-supermin-helper/">febootstrap-supermin-helper</a></i>(8).

<h2>Authors</h2>

Richard W.M. Jones &lt;rjones @ redhat . com&gt;

<h2>Copyright</h2>

(C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" HREF="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;. 

 This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

 You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
