---
title: "virt-inspector(1)"
name: "virt-inspector"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-inspector/"
description: "virt-inspector – Display operating system version and other information about a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-inspector &#8211; Display operating system version and other information about a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - inspector[--options] - d domname virt - inspector[--options] - a disk.img[-a disk.img...]
</code></pre>
<p> Old-style: </p>
<pre>
 virt-inspector domname
 virt-inspector disk.img [disk.img ...]
</pre>
<h2>DESCRIPTION</h2>
<p> <code>virt-inspector</code> examines a virtual machine or disk image and tries to determine the version of the operating system and other information about the virtual machine. </p>
<p> Virt-inspector produces <font SIZE="-1">XML</font> output for feeding into other programs. </p>
<p> In the normal usage, use <tt>&quot;virt-inspector -d domname&quot;</tt> where <tt>&quot;domname&quot;</tt> is the libvirt domain (see: <tt>&quot;virsh list --all&quot;</tt>). </p>
<p> You can also run virt-inspector directly on disk images from a single virtual machine. Use <tt>&quot;virt-inspector -a disk.img&quot;</tt>. In rare cases a domain has several block devices, in which case you should list several <i>-a</i> options one after another, with the first corresponding to the guest&#8217;s <i>/dev/sda</i>, the second to the guest&#8217;s <i>/dev/sdb</i> and so on. </p>
<p> You can also run virt-inspector on install disks, live CDs, bootable <font SIZE="-1">USB</font> keys and similar. </p>
<p> Virt-inspector can only inspect and report upon <i>one domain at a time</i>. To inspect several virtual machines, you have to run virt-inspector several times (for example, from a shell script for-loop). </p>
<p> Because virt-inspector needs direct access to guest images, it won&#8217;t normally work over remote libvirt connections. </p>
<p> All of the information available from virt-inspector is also available through the core libguestfs inspection <font SIZE="-1">API </font>(see &#8220;<font SIZE="-1">INSPECTION&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)). The same information can also be fetched using guestfish or via libguestfs bindings in many programming languages (see &#8220;<font SIZE="-1">GETTING INSPECTION DATA FROM THE LIBGUESTFS API&#8221;</font>).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>-a</code> file</p>
<dd>
<dt><code>&#8211;add</code> file</p>
<dd> Add <i>file</i> which should be a disk image from a virtual machine. If the virtual machine has multiple block devices, you must supply all of them with separate <i>-a</i> options. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option.</p>
<dt><code>-a</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;add</code> <font SIZE="-1">URI</font></p>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>-c </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;connect </code><font SIZE="-1"><code>URI</code></font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> Libvirt is only used if you specify a <tt>&quot;domname&quot;</tt> on the command line. If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all.</p>
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;echo-keys</code></p>
<dd> When prompting for keys and passphrases, virt-inspector normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</p>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> Specify the format of disk images given on the command line. If this is omitted then the format is autodetected from the content of the disk image. </p>
<p> If disk images are requested from libvirt, then this program asks libvirt for this information. In this case, the value of the format parameter is ignored. </p>
<p> If working with untrusted raw-format guest disk images, you should ensure the format is always specified.</p>
<dt><code>&#8211;keys-from-stdin</code></p>
<dd> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</p>
<dt><code>&#8211;xpath</code> query</p>
<dd> Perform an XPath query on the <font SIZE="-1">XML</font> on stdin, and print the result on stdout. In this mode virt-inspector simply runs an XPath query; all other inspection functions are disabled. See &#8220;<font SIZE="-1">XPATH QUERIES&#8221;</font> below for some examples.</dl>
<h2>OLD-STYLE COMMAND LINE ARGUMENTS</h2>
<p> Previous versions of virt-inspector allowed you to write either: </p>
<pre>
 virt-inspector disk.img [disk.img ...]
</pre>
<p> or </p>
<pre>
 virt-inspector guestname
</pre>
<p> whereas in this version you should use <i>-a</i> or <i>-d</i> respectively to avoid the confusing case where a disk image might have the same name as a guest. </p>
<p> For compatibility the old style is still supported.</p>
<h2>XML FORMAT</h2>
<p> The virt-inspector <font SIZE="-1">XML</font> is described precisely in a <font SIZE="-1">RELAX NG</font> schema file <i>virt-inspector.rng</i> which is supplied with libguestfs. This section is just an overview. </p>
<p> The top-level element is &lt;operatingsystems&gt;, and it contains one or more &lt;operatingsystem&gt; elements. You would only see more than one &lt;operatingsystem&gt; element if the virtual machine is multi-boot, which is vanishingly rare in real world VMs.</p>
<h3>&lt;operatingsystem&gt;</h3>
<p> In the &lt;operatingsystem&gt; tag are various optional fields that describe the operating system, its architecture, the descriptive &#8220;product name&#8221; string, the type of <font SIZE="-1">OS</font> and so on, as in this example: </p>
<pre>
 &lt;operatingsystems&gt;
   &lt;operatingsystem&gt;
     &lt;root&gt;/dev/sda2&lt;/root&gt;
     &lt;name&gt;windows&lt;/name&gt;
     &lt;arch&gt;i386&lt;/arch&gt;
     &lt;distro&gt;windows&lt;/distro&gt;
     &lt;product_name&gt;Windows 7 Enterprise&lt;/product_name&gt;
     &lt;product_variant&gt;Client&lt;/product_variant&gt;
     &lt;major_version&gt;6&lt;/major_version&gt;
     &lt;minor_version&gt;1&lt;/minor_version&gt;
     &lt;windows_systemroot&gt;/Windows&lt;/windows_systemroot&gt;
     &lt;format&gt;installed&lt;/format&gt;
</pre>
<p> In brief, &lt;name&gt; is the class of operating system (something like <tt>&quot;linux&quot;</tt> or <tt>&quot;windows&quot;</tt>), &lt;distro&gt; is the distribution (eg. <tt>&quot;fedora&quot;</tt> but many other distros are recognized) and &lt;arch&gt; is the guest architecture. The other fields are fairly self-explanatory, but because these fields are taken directly from the libguestfs inspection <font SIZE="-1">API</font> you can find precise information from &#8220;<font SIZE="-1">INSPECTION&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3). </p>
<p> The &lt;root&gt; element is the root filesystem device, but from the point of view of libguestfs (block devices may have completely different names inside the <font SIZE="-1">VM</font> itself).</p>
<h3>&lt;mountpoints&gt;</h3>
<p> Un*x-like guests typically have multiple filesystems which are mounted at various mountpoints, and these are described in the &lt;mountpoints&gt; element which looks like this: </p>
<pre>
 &lt;operatingsystems&gt;
   &lt;operatingsystem&gt;
     ...
     &lt;mountpoints&gt;
       &lt;mountpoint dev=&quot;/dev/vg_f13x64/lv_root&quot;&gt;/&lt;/mountpoint&gt;
       &lt;mountpoint dev=&quot;/dev/sda1&quot;&gt;/boot&lt;/mountpoint&gt;
     &lt;/mountpoints&gt;
</pre>
<p> As with &lt;root&gt;, devices are from the point of view of libguestfs, and may have completely different names inside the guest. Only mountable filesystems appear in this list, not things like swap devices.</p>
<h3>&lt;filesystems&gt;</h3>
<p> &lt;filesystems&gt; is like &lt;mountpoints&gt; but covers <i>all</i> filesystems belonging to the guest, including swap and empty partitions. (In the rare case of a multi-boot guest, it covers filesystems belonging to this <font SIZE="-1">OS</font> or shared with this <font SIZE="-1">OS</font> and other OSes). </p>
<p> You might see something like this: </p>
<pre>
 &lt;operatingsystems&gt;
   &lt;operatingsystem&gt;
     ...
     &lt;filesystems&gt;
       &lt;filesystem dev=&quot;/dev/vg_f13x64/lv_root&quot;&gt;
         &lt;type&gt;ext4&lt;/type&gt;
         &lt;label&gt;Fedora-13-x86_64&lt;/label&gt;
         &lt;uuid&gt;e6a4db1e-15c2-477b-ac2a-699181c396aa&lt;/uuid&gt;
       &lt;/filesystem&gt;
</pre>
<p> The optional elements within &lt;filesystem&gt; are the filesystem type, the label, and the <font SIZE="-1">UUID.</font></p>
<h3>&lt;applications&gt;</h3>
<p> The related elements &lt;package_format&gt;, &lt;package_management&gt; and &lt;applications&gt; describe applications installed in the virtual machine. </p>
<p> &lt;package_format&gt;, if present, describes the packaging system used. Typical values would be <tt>&quot;rpm&quot;</tt> and <tt>&quot;deb&quot;</tt>. </p>
<p> &lt;package_management&gt;, if present, describes the package manager. Typical values include <tt>&quot;yum&quot;</tt>, <tt>&quot;up2date&quot;</tt> and <tt>&quot;apt&quot;</tt> </p>
<p> &lt;applications&gt; lists the packages or applications installed. </p>
<pre>
 &lt;operatingsystems&gt;
   &lt;operatingsystem&gt;
     ...
     &lt;applications&gt;
       &lt;application&gt;
         &lt;name&gt;coreutils&lt;/name&gt;
         &lt;version&gt;8.5&lt;/version&gt;
         &lt;release&gt;1&lt;/release&gt;
       &lt;/application&gt;
</pre>
<p> The version and release fields may not be available for some types guests. Other fields are possible, see &#8220;guestfs_inspect_list_applications&#8221; in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h3>&lt;drive_mappings&gt;</h3>
<p> For operating systems like Windows which use drive letters, virt-inspector is able to find out how drive letters map to filesystems. </p>
<pre>
 &lt;operatingsystems&gt;
   &lt;operatingsystem&gt;
     ...
     &lt;drive_mappings&gt;
       &lt;drive_mapping name=&quot;C&quot;&gt;/dev/sda2&lt;/drive_mapping&gt;
       &lt;drive_mapping name=&quot;E&quot;&gt;/dev/sdb1&lt;/drive_mapping&gt;
     &lt;/drive_mappings&gt;
</pre>
<p> In the example above, drive C maps to the filesystem on the second partition on the first disk, and drive E maps to the filesystem on the first partition on the second disk. </p>
<p> Note that this only covers permanent local filesystem mappings, not things like network shares. Furthermore <font SIZE="-1">NTFS</font> volume mount points may not be listed here.</p>
<h3>&lt;icon&gt;</h3>
<p> Virt-inspector is sometimes able to extract an icon or logo for the guest. The icon is returned as base64-encoded <font SIZE="-1">PNG</font> data. Note that the icon can be very large and high quality. </p>
<p> &lt;operatingsystems&gt;<br />
   &lt;operatingsystem&gt;<br />
     &#8230;<br />
     &lt;icon&gt;<br />
       iVBORw0KGgoAAAANSUhEUgAAAGAAAABg[&#8230;&#8230;.]<br />
       [&#8230; many lines of base64 data &#8230;]<br />
     &lt;/icon&gt;</p>
<p> To display the icon, you have to extract it and convert the base64 data back to a binary file. Use an XPath query or simply an editor to extract the data, then use the coreutils <i><a href="/docs/linux/man/1-base64/">base64</a></i>(1) program to do the conversion back to a <font SIZE="-1">PNG</font> file: </p>
<pre>
 base64 -i -d &lt; icon.data &gt; icon.png
</pre>
<h3><font SIZE="-1">INSPECTING INSTALL DISKS, LIVE</font> CDs</h3>
<p> Virt-inspector can detect some operating system installers on install disks, live CDs, bootable <font SIZE="-1">USB</font> keys and more. </p>
<p> In this case the &lt;format&gt; tag will contain <tt>&quot;installer&quot;</tt> and other fields may be present to indicate a live <font SIZE="-1">CD,</font> network installer, or one part of a multipart <font SIZE="-1">CD. </font> For example: </p>
<pre>
 &lt;operatingsystems&gt;
   &lt;operatingsystem&gt;
     &lt;root&gt;/dev/sda&lt;/root&gt;
     &lt;name&gt;linux&lt;/name&gt;
     &lt;arch&gt;i386&lt;/arch&gt;
     &lt;distro&gt;ubuntu&lt;/distro&gt;
     &lt;product_name&gt;Ubuntu 10.10 &amp;quot;Maverick Meerkat&amp;quot;&lt;/product_name&gt;
     &lt;major_version&gt;10&lt;/major_version&gt;
     &lt;minor_version&gt;10&lt;/minor_version&gt;
     &lt;format&gt;installer&lt;/format&gt;
     &lt;live/&gt;
</pre>
<h2>XPATH QUERIES</h2>
<p> Virt-inspector includes built in support for running XPath queries. The reason for including XPath support directly in virt-inspector is simply that there are no good and widely available command line programs that can do XPath queries. The only good one is <i><a href="/docs/linux/man/1-xmlstarlet/">xmlstarlet</a></i>(1) and that is not available on Red Hat Enterprise Linux. </p>
<p> To perform an XPath query, use the <i>&#8211;xpath</i> option. Note that in this mode, virt-inspector simply reads <font SIZE="-1">XML</font> from stdin and outputs the query result on stdout. All other inspection features are disabled in this mode. </p>
<p> For example: </p>
<p>$ virt &#8211; inspector &#8211; d Guest | virt &#8211; inspector&#8211; xpath &#8216;//filesystems&#8217; &lt; filesystems &gt; &lt;filesystem dev = &#8220;/dev/vg_f13x64/lv_root&#8221;&gt;&lt;type&gt; ext4&lt;/ type&gt;[&#8230;] $ virt &#8211; inspector &#8211; d Guest |<br />
    virt &#8211; inspector&#8211; xpath &#8220;string(//filesystem[@dev=&#8217;/dev/sda1&#8242;]/type)&#8221; ext4 $ virt &#8211; inspector &#8211; d Guest |<br />
    virt &#8211; inspector&#8211; xpath &#8216;string(//icon)&#8217; | base64 &#8211; i &#8211; d | display &#8211; [ displays the guest icon, if there is one ]</p>
<h2>GETTING INSPECTION DATA FROM THE LIBGUESTFS API</h2>
<p> In early versions of libguestfs, virt-inspector was a large Perl script that contained many heuristics for inspecting guests. This had several problems: in order to do inspection from other tools (like guestfish) we had to call out to this Perl script; and it privileged Perl over other languages that libguestfs supports. </p>
<p> By libguestfs 1.8 we had rewritten the Perl code in C, and incorporated it all into the core libguestfs <font SIZE="-1">API </font>(<i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)). Now virt-inspector is simply a thin C program over the core C <font SIZE="-1">API. </font> All of the inspection information is available from all programming languages that libguestfs supports, and from guestfish. </p>
<p> For a description of the C inspection <font SIZE="-1">API,</font> read &#8220;<font SIZE="-1">INSPECTION&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3). </p>
<p> For example code using the C inspection <font SIZE="-1">API,</font> look for <i>inspect-vm.c</i> which ships with libguestfs. </p>
<p> <i>inspect-vm.c</i> has also been translated into other languages. For example, <i>inspect_vm.pl</i> is the Perl translation, and there are other translations for OCaml, Python, etc. See &#8220;<font SIZE="-1">USING LIBGUESTFS WITH OTHER PROGRAMMING LANGUAGES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) for a list of man pages which contain this example code.</p>
<h3><font SIZE="-1">GETTING INSPECTION DATA FROM GUESTFISH</font></h3>
<p> If you use the guestfish <i>-i</i> option, then the main C inspection <font SIZE="-1">API </font>&#8220;guestfs_inspect_os&#8221; in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) is called. This is equivalent to the guestfish command <tt>&quot;inspect-os&quot;</tt>. You can also call this guestfish command by hand. </p>
<p> <tt>&quot;inspect-os&quot;</tt> performs inspection on the current disk image, returning the list of operating systems found. Each <font SIZE="-1">OS</font> is represented by its root filesystem device. In the majority of cases, this command prints nothing (no OSes found), or a single root device, but beware that it can print multiple lines if there are multiple OSes or if there is an install <font SIZE="-1">CD</font> attached to the guest. </p>
<pre>
 $ guestfish --ro -a F15x32.img
 &gt;&lt;fs&gt; run
 &gt;&lt;fs&gt; inspect-os
 /dev/vg_f15x32/lv_root
</pre>
<p> Using the root device, you can fetch further information about the guest: </p>
<pre>
 &gt;&lt;fs&gt; inspect-get-type /dev/vg_f15x32/lv_root
 linux
 &gt;&lt;fs&gt; inspect-get-distro /dev/vg_f15x32/lv_root
 fedora
 &gt;&lt;fs&gt; inspect-get-major-version /dev/vg_f15x32/lv_root
 15
 &gt;&lt;fs&gt; inspect-get-product-name /dev/vg_f15x32/lv_root
 Fedora release 15 (Lovelock)
</pre>
<p> Limitations of guestfish make it hard to assign the root device to a variable (since guestfish doesn&#8217;t have variables), so if you want to do this reproducibly you are better off writing a script using one of the other languages that the libguestfs <font SIZE="-1">API</font> supports. </p>
<p> To list applications, you have to first mount up the disks: </p>
<pre>
 &gt;&lt;fs&gt; inspect-get-mountpoints /dev/vg_f15x32/lv_root
 /: /dev/vg_f15x32/lv_root
 /boot: /dev/vda1
 &gt;&lt;fs&gt; mount-ro /dev/vg_f15x32/lv_root /
 &gt;&lt;fs&gt; mount-ro /dev/vda1 /boot
</pre>
<p> and then call the inspect-list-applications <font SIZE="-1">API:</font> </p>
<pre><code>
&gt; &lt;fs&gt; inspect - list - applications / dev / vg_f15x32 / lv_root | head - 28
                                                                              [0] = {
    app_name : ConsoleKit
    app_display_name :
    app_epoch : 0
    app_version : 0.4.5
    app_release : 1.fc15
    app_install_path :
    app_trans_path :
    app_publisher :
    app_url :
    app_source_package :
    app_summary :
    app_description :
}
            [1] = {
                app_name : ConsoleKit - libs
                app_display_name :
                app_epoch : 0
                app_version : 0.4.5
                app_release : 1.fc15
                app_install_path :
                app_trans_path :
                app_publisher :
                app_url :
                app_source_package :
                app_summary :
                app_description :
            }
</code></pre>
<p> To display an icon for the guest, note that filesystems must also be mounted as above. You can then do: </p>
<pre>
 &gt;&lt;fs&gt; inspect-get-icon /dev/vg_f15x32/lv_root | display -
</pre>
<h2>OLD VERSIONS OF VIRT-INSPECTOR</h2>
<p> As described above, early versions of libguestfs shipped with a different virt-inspector program written in Perl (the current version is written in C). The <font SIZE="-1">XML</font> output of the Perl virt-inspector was different and it could also output in other formats like text. </p>
<p> The old virt-inspector is no longer supported or shipped with libguestfs. </p>
<p> To confuse matters further, in Red Hat Enterprise Linux 6 we ship two versions of virt-inspector with different names: </p>
<pre>
 virt-inspector     Old Perl version.
 virt-inspector2    New C version.
</pre>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <a rel="nofollow" href="http://www.w3.org/TR/xpath/,">http://www.w3.org/TR/xpath/,</a> <i><a href="/docs/linux/man/1-base64/">base64</a></i>(1), <i><a href="/docs/linux/man/1-xmlstarlet/">xmlstarlet</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<dl>
<dt>&bull;</p>
<dd> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<dt>&bull;</p>
<dd> Matthew Booth mbooth [at] redhat.com</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010-2012 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAO">XPATH QUERIES</a></p>
<dd>
<dt><a href="#lbAP">GETTING INSPECTION DATA FROM THE LIBGUESTFS API</a></p>
<dd>
<dt><a href="#lbAR">OLD VERSIONS OF VIRT-INSPECTOR</a></p>
<dd>
<dt><a href="#lbAS">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAT">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAU">AUTHORS</a></p>
<dd>
<dt><a href="#lbAV">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAW">LICENSE</a></p>
<dd>
<dt><a href="#lbAX">BUGS</a></p>
<dd></dl>
