---

title: "virt-p2v-make-disk(1)"
name: "virt-p2v-make-disk"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-p2v-make-disk/"
description: "virt-p2v-make-disk – Build the virt-p2v disk using virt-builder"
---

<p> virt-p2v-make-disk &#8211; Build the virt-p2v disk using virt-builder </p>
<h2>SYNOPSIS</h2>
<pre>
 virt-p2v-make-disk -o /dev/sdX [os-version]
</pre>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) converts a physical machine to run virtualized on KVM, managed by libvirt, OpenStack, oVirt, Red Hat Enterprise Virtualisation (RHEV), or one of the other targets supported by <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<p> virt-p2v-make-disk is a script which creates a bootable disk image or USB key containing virt-p2v. It uses <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) to do this, and is just a small shell script around virt-builder. </p>
<p> The required <i>-o</i> parameter specifies where the output should go, for example to a USB key (eg. <tt>&quot;-o /dev/sdX&quot;</tt>) or to a file. If you pass a device name, then <code>the existing contents of the device will be erased</code>.</p>
<h3>os-version parameter</h3>
<p> The optional <tt>&quot;os-version&quot;</tt> parameter is the base Linux distro to use for the operating system on the ISO.  If you don&#8217;t set this parameter, the script tries to choose a suitable default for you. Most users should <i>not</i> use the <tt>&quot;os-version&quot;</tt> parameter. </p>
<p> The base OS selected for virt-p2v is not related in any way to the OS of the physical machine that you are trying to convert. </p>
<p> To list possible <tt>&quot;os-version&quot;</tt> combinations, do: </p>
<pre>
 virt-builder -l
</pre>
<h2>EXAMPLES</h2>
<p> Write a virt-p2v bootable USB key on <i>/dev/sdX</i> (any existing content on <i>/dev/sdX</i> is erased): </p>
<pre>
 virt-p2v-make-disk -o /dev/sdX
</pre>
<p> Write a virt-p2v bootable virtual disk image, and boot it under qemu: </p>
<pre>
 virt-p2v-make-disk -o /var/tmp/p2v.img
 qemu-kvm -m 1024 -boot c \
   -drive file=/var/tmp/p2v.img,if=virtio,index=0 \
   -drive file=/var/tmp/guest.img,if=virtio,index=1
</pre>
<p> where <i>/var/tmp/guest.img</i> would be the disk image of some guest that you want to convert (for testing only).</p>
<h2>ADDING EXTRA PACKAGES</h2>
<p> You can install extra packages using the <i>&#8211;install</i> option. This can be useful for making a more fully-featured virt-p2v disk with extra tools for debugging and troubleshooting. Give a list of packages, separated by commas. For example: </p>
<pre>
 virt-p2v-make-disk -o /var/tmp/p2v.img --install tcpdump,traceroute
</pre>
<h2>ADDING AN SSH IDENTITY</h2>
<p> You can inject an SSH identity (private key) file to the image using the <i>&#8211;inject-ssh-identity</i> option. </p>
<p> First create a key pair. It must have an empty passphrase: </p>
<pre>
 ssh-keygen -t rsa -N '' -f id_rsa
</pre>
<p> This creates a private key (<tt>&quot;id_rsa&quot;</tt>) and a public key (<tt>&quot;id_rsa.pub&quot;</tt>) pair. The public key should be appended to the <tt>&quot;authorized_keys&quot;</tt> file on the virt-v2v conversion server (usually to <tt>&quot;/root/.ssh/authorized_keys&quot;</tt>). </p>
<p> The private key should be injected into the disk image and then discarded: </p>
<pre>
 virt-p2v-make-disk [...] --inject-ssh-identity id_rsa
 rm id_rsa
</pre>
<p> When booting virt-p2v, specify the URL of the injected file like this: </p>
<pre><code>
 │         User name: [root_____________________________] │
 │                                                        │
 │          Password: [    &lt;leave this field blank&gt;     ] │
 │                                                        │
 │  SSH Identity URL: [file:///var/tmp/id_rsa___________] │
</code></pre>
<p> or if using the kernel command line, add: </p>
<pre>
 p2v.identity=file:///var/tmp/id_rsa
</pre>
<p> For more information, see &#8220;SSH IDENTITIES&#8221; in <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display help.</dd>
<dt><code>&#8211;inject-ssh-identity</code> id_rsa</dt>
<dd> Add an SSH identity (private key) file into the image. See &#8220;ADDING AN SSH IDENTITY&#8221; above.</dd>
<dt><code>&#8211;install</code> pkg,pkg,&#8230;</dt>
<dd> Add extra packages to the image. See &#8220;ADDING EXTRA PACKAGES&#8221; above.</dd>
<dt><code>&#8211;no-warn-if-partition</code></dt>
<dd> Normally you should not write to a partition on a USB drive (ie. don&#8217;t use <tt>&quot;-o /dev/sdX1&quot;</tt>, use <tt>&quot;-o /dev/sdX&quot;</tt> to make a bootable USB drive). If you do this, virt-builder prints a warning. This option suppresses that warning.</dd>
<dt><code>-o</code> OUTPUT</dt>
<dd>
</dd><dt><code>&#8211;output</code> OUTPUT</dt>
<dd> Write output to <tt>&quot;OUTPUT&quot;</tt>, which can be a local file or block device. <code>The existing contents of the device will be erased</code>.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Enable verbose output. Use this if you need to debug problems with the script or if you are filing a bug.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>$libexecdir/virt-p2v</i></dt>
<dd> The <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1) binary which is copied into the bootable disk image. </dd>
<p> The location of the binary can be changed by setting the <tt>&quot;VIRT_P2V_DATA_DIR&quot;</tt> environment variable.</p>
<dt><i>$datadir/virt-p2v/issue</i></dt>
<dd>
</dd><dt><i>$datadir/virt-p2v/launch-virt-p2v.in</i></dt>
<dd>
</dd><dt><i>$datadir/virt-p2v/p2v.service</i></dt>
<dd> Various data files that are copied into the bootable disk image. </dd>
<p> The location of these files can be changed by setting the <tt>&quot;VIRT_P2V_DATA_DIR&quot;</tt> environment variable.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>&quot;VIRT_P2V_DATA_DIR&quot;</dt>
<dd> The directory where virt-p2v-make-disk looks for data files (see &#8220;FILES&#8221; above). If not set, a compiled-in location is used.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v/">virt-p2v</a></i>(1), <i><a href="/docs/linux/man/1-virt-p2v-make-kickstart/">virt-p2v-make-kickstart</a></i>(1), <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</dt>
<dd> The version of libguestfs.</dd>
<dt>&bull;</dt>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</dd>
<dt>&bull;</dt>
<dd> Describe the bug accurately and give a way to reproduce it.</dd>
<dt>&bull;</dt>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </dd>
</dl>
