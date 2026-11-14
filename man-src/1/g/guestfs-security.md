---
title: "guestfs-security(1)"
name: "guestfs-security"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-security/"
description: "guestfs-security – security of libguestfs"
---

<h2 class="name">NAME</h2>
<p> guestfs-security &#8211; security of libguestfs </p>
<h2>DESCRIPTION</h2>
<p> This manual page discusses security implications of using libguestfs, particularly with untrusted or malicious guests or disk images.</p>
<h2>REPORTING SECURITY PROBLEMS</h2>
<p> If you wish to privately report a security issue, please follow the Red Hat security procedure at <a rel="nofollow" href="https://access.redhat.com/security/team/contact">https://access.redhat.com/security/team/contact</a> </p>
<p> If the security problem is not so serious, you can simply file a bug (see &#8220;<font SIZE="-1">BUGS&#8221;</font> below), or send an email to our mailing list (<a rel="nofollow" href="https://www.redhat.com/mailman/listinfo/libguestfs">https://www.redhat.com/mailman/listinfo/libguestfs</a>). You do not need to subscribe to the mailing list to send email, but there will be a delay while the message is moderated.</p>
<h2>GENERAL ISSUES</h2>
<h3>Security of mounting filesystems</h3>
<p> You should never mount an untrusted guest filesystem directly on your host kernel (eg. using loopback or kpartx). </p>
<p> When you mount a filesystem, mistakes in the kernel filesystem (<font SIZE="-1">VFS</font>) can be escalated into exploits by attackers creating a malicious filesystem. These exploits are very severe for two reasons. Firstly there are very many filesystem drivers in the kernel, and many of them are infrequently used and not much developer attention has been paid to the code. Linux userspace helps potential crackers by detecting the filesystem type and automatically choosing the right <font SIZE="-1">VFS</font> driver, even if that filesystem type is unexpected. Secondly, a kernel-level exploit is like a local root exploit (worse in some ways), giving immediate and total access to the system right down to the hardware level. </p>
<p> These exploits can be present in the kernel for a very long time (<a rel="nofollow" href="https://lwn.net/Articles/538898/">https://lwn.net/Articles/538898/</a>). </p>
<p> Libguestfs provides a layered approach to protecting you from exploits: </p>
<pre><code>
untrusted filesystem-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --appliance kernel-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --qemu process running as non - root-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --sVirt[if using libvirt + SELinux]-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --host kernel
</code></pre>
<p> We run a Linux kernel inside a qemu virtual machine, usually running as a non-root user. The attacker would need to write a filesystem which first exploited the kernel, and then exploited either qemu virtualization (eg. a faulty qemu driver) or the libguestfs protocol, and finally to be as serious as the host kernel exploit it would need to escalate its privileges to root. Additionally if you use the libvirt back end and SELinux, sVirt is used to confine the qemu process. This multi-step escalation, performed by a static piece of data, is thought to be extremely hard to do, although we never say ‘never’ about security issues. </p>
<p> Callers can also reduce the attack surface by forcing the filesystem type when mounting (use &#8220;guestfs_mount_vfs&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)).</p>
<h3>General security considerations</h3>
<p> Be careful with any files or data that you download from a guest (by &#8220;download&#8221; we mean not just the &#8220;guestfs_download&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) command but any command that reads files, filenames, directories or anything else from a disk image). An attacker could manipulate the data to fool your program into doing the wrong thing. Consider cases such as:</p>
<dl>
<dt>&bull;</p>
<dd> the data (file etc) not being present</p>
<dt>&bull;</p>
<dd> being present but empty</p>
<dt>&bull;</p>
<dd> being much larger than normal</p>
<dt>&bull;</p>
<dd> containing arbitrary 8 bit data</p>
<dt>&bull;</p>
<dd> being in an unexpected character encoding</p>
<dt>&bull;</p>
<dd> containing homoglyphs.</dl>
<h3>Protocol security</h3>
<p> The protocol is designed to be secure, being based on <font SIZE="-1">RFC 4506</font> (<font SIZE="-1">XDR</font>) with a defined upper message size. However a program that uses libguestfs must also take care &#8211; for example you can write a program that downloads a binary from a disk image and executes it locally, and no amount of protocol security will save you from the consequences.</p>
<h3>Inspection security</h3>
<p> Parts of the inspection <font SIZE="-1">API</font> (see &#8220;<font SIZE="-1">INSPECTION&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)) return untrusted strings directly from the guest, and these could contain any 8 bit data. Callers should be careful to escape these before printing them to a structured file (for example, use <font SIZE="-1">HTML</font> escaping if creating a web page). </p>
<p> Guest configuration may be altered in unusual ways by the administrator of the virtual machine, and may not reflect reality (particularly for untrusted or actively malicious guests). For example we parse the hostname from configuration files like <i>/etc/sysconfig/network</i> that we find in the guest, but the guest administrator can easily manipulate these files to provide the wrong hostname. </p>
<p> The inspection <font SIZE="-1">API</font> parses guest configuration using two external libraries: Augeas (Linux configuration) and hivex (Windows Registry). Both are designed to be robust in the face of malicious data, although denial of service attacks are still possible, for example with oversized configuration files.</p>
<h3>Running untrusted guest commands</h3>
<p> Be very cautious about running commands from the guest. By running a command in the guest, you are giving <font SIZE="-1">CPU</font> time to a binary that you do not control, under the same user account as the library, albeit wrapped in qemu virtualization. More information and alternatives can be found in &#8220;<font SIZE="-1">RUNNING COMMANDS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3).</p>
<h2>HISTORICAL SECURITY ISSUES IN LIBGUESTFS</h2>
<h3><font SIZE="-1">CVE-2010-3851</font></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/642934">https://bugzilla.redhat.com/642934</a> </p>
<p> This security bug concerns the automatic disk format detection that qemu does on disk images. </p>
<p> A raw disk image is just the raw bytes, there is no header. Other disk images like qcow2 contain a special header. Qemu deals with this by looking for one of the known headers, and if none is found then assuming the disk image must be raw. </p>
<p> This allows a guest which has been given a raw disk image to write some other header. At next boot (or when the disk image is accessed by libguestfs) qemu would do autodetection and think the disk image format was, say, qcow2 based on the header written by the guest. </p>
<p> This in itself would not be a problem, but qcow2 offers many features, one of which is to allow a disk image to refer to another image (called the &#8220;backing disk&#8221;). It does this by placing the path to the backing disk into the qcow2 header. This path is not validated and could point to any host file (eg. &#8220;/etc/passwd&#8221;). The backing disk is then exposed through &#8220;holes&#8221; in the qcow2 disk image, which of course is completely under the control of the attacker. </p>
<p> In libguestfs this is rather hard to exploit except under two circumstances:</p>
<dl>
<dt>1.</p>
<dd> You have enabled the network or have opened the disk in write mode.</p>
<dt>2.</p>
<dd> You are also running untrusted code from the guest (see &#8220;<font SIZE="-1">RUNNING COMMANDS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)).</dl>
<p> The way to avoid this is to specify the expected disk format when adding disks (the optional <tt>&quot;format&quot;</tt> option to &#8220;guestfs_add_drive_opts&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)). You should always do this if the disk is raw format, and it’s a good idea for other cases too. (See also &#8220;<font SIZE="-1">DISK IMAGE FORMATS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)). </p>
<p> For disks added from libvirt using calls like &#8220;guestfs_add_domain&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), the format is fetched from libvirt and passed through. </p>
<p> For libguestfs tools, use the <i>&#8211;format</i> command line parameter as appropriate.</p>
<h3><font SIZE="-1">CVE-2011-4127</font></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/752375">https://bugzilla.redhat.com/752375</a> </p>
<p> This is a bug in the kernel which allowed guests to overwrite parts of the host’s drives which they should not normally have access to. </p>
<p> It is sufficient to update libguestfs to any version ≥ 1.16 which contains a change that mitigates the problem.</p>
<h3><font SIZE="-1">CVE-2012-2690</font></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/831117">https://bugzilla.redhat.com/831117</a> </p>
<p> Old versions of both virt-edit and the guestfish <tt>&quot;edit&quot;</tt> command created a new file containing the changes but did not set the permissions, etc of the new file to match the old one. The result of this was that if you edited a security sensitive file such as <i>/etc/shadow</i> then it would be left world-readable after the edit. </p>
<p> It is sufficient to update libguestfs to any version ≥ 1.16.</p>
<h3><font SIZE="-1">CVE-2013-2124</font></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/968306">https://bugzilla.redhat.com/968306</a> </p>
<p> This security bug was a flaw in inspection where an untrusted guest using a specially crafted file in the guest <font SIZE="-1">OS</font> could cause a double-free in the C library (denial of service). </p>
<p> It is sufficient to update libguestfs to a version that is not vulnerable: libguestfs ≥ 1.20.8, ≥ 1.22.2 or ≥ 1.23.2.</p>
<h3><font SIZE="-1">CVE-2013-4419</font></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/1016960">https://bugzilla.redhat.com/1016960</a> </p>
<p> When using the <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) <i>&#8211;remote</i> or guestfish <i>&#8211;listen</i> options, guestfish would create a socket in a known location (<i>/tmp/.guestfish-$UID/socket-$PID</i>). </p>
<p> The location has to be a known one in order for both ends to communicate. However no checking was done that the containing directory (<i>/tmp/.guestfish-$UID</i>) is owned by the user. Thus another user could create this directory and potentially hijack sockets owned by another user’s guestfish client or server. </p>
<p> It is sufficient to update libguestfs to a version that is not vulnerable: libguestfs ≥ 1.20.12, ≥ 1.22.7 or ≥ 1.24.</p>
<h3>Denial of service when inspecting disk images with corrupt btrfs volumes</h3>
<p> It was possible to crash libguestfs (and programs that use libguestfs as a library) by presenting a disk image containing a corrupt btrfs volume. </p>
<p> This was caused by a <font SIZE="-1">NULL</font> pointer dereference causing a denial of service, and is not thought to be exploitable any further. </p>
<p> See commit d70ceb4cbea165c960710576efac5a5716055486 for the fix. This fix is included in libguestfs stable branches ≥ 1.26.0, ≥ 1.24.6 and ≥ 1.22.8, and also in <font SIZE="-1">RHEL</font> ≥ 7.0. Earlier versions of libguestfs are not vulnerable.</p>
<h3><font SIZE="-1">CVE-2014-0191</font></h3>
<p> Libguestfs previously used unsafe libxml2 APIs for parsing libvirt <font SIZE="-1">XML.</font> These APIs defaulted to allowing network connections to be made when certain <font SIZE="-1">XML</font> documents were presented. Using a malformed <font SIZE="-1">XML</font> document it was also possible to exhaust all <font SIZE="-1">CPU,</font> memory or file descriptors on the machine. </p>
<p> Since the libvirt <font SIZE="-1">XML</font> comes from a trusted source (the libvirt daemon) it is not thought that this could have been exploitable. </p>
<p> This was fixed in libguestfs ≥ 1.27.9 and the fix was backported to stable versions ≥ 1.26.2, ≥ 1.24.9, ≥ 1.22.10 and ≥ 1.20.13.</p>
<h3>Shellshock (bash <font SIZE="-1">CVE-2014-6271</font>)</h3>
<p> This bash bug indirectly affects libguestfs. For more information see: <a rel="nofollow" href="https://www.redhat.com/archives/libguestfs/2014-September/msg00252.html">https://www.redhat.com/archives/libguestfs/2014-September/msg00252.html</a></p>
<h3><font SIZE="-1">CVE-2014-8484</font></h3>
<h3><font SIZE="-1">CVE-2014-8485</font></h3>
<p> These two bugs in binutils affect the <font SIZE="-1">GNU</font> <code><a href="/docs/linux/man/1-strings/">strings</a></code>(1) program, and thus the &#8220;guestfs_strings&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) and &#8220;guestfs_strings_e&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) APIs in libguestfs. Running strings on an untrusted file could cause arbitrary code execution (confined to the libguestfs appliance). </p>
<p> In libguestfs ≥ 1.29.5 and ≥ 1.28.3, libguestfs uses the <tt>&quot;strings&quot;</tt> <i>-a</i> option to avoid <font SIZE="-1">BFD</font> parsing on the file.</p>
<h3><font SIZE="-1">CVE-2015-5745</font></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/show_bug.cgi?id=1251157">https://bugzilla.redhat.com/show_bug.cgi?id=1251157</a> </p>
<p> This is not a vulnerability in libguestfs, but because we always give a virtio-serial port to each guest (since that is how guest-host communication happens), an escalation from the appliance to the host qemu process is possible. This could affect you if:</p>
<dl>
<dt>&bull;</p>
<dd> your libguestfs program runs untrusted programs out of the guest (using &#8220;guestfs_sh&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) etc), or</p>
<dt>&bull;</p>
<dd> another exploit was found in (for example) kernel filesystem code that allowed a malformed filesystem to take over the appliance.</dl>
<p> If you use sVirt to confine qemu, that would thwart some attacks.</p>
<h3>Permissions of <i>.ssh</i> and <i>.ssh/authorized_keys</i></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/1260778">https://bugzilla.redhat.com/1260778</a> </p>
<p> The tools <code><a href="/docs/linux/man/1-virt-customize/">virt-customize</a></code>(1), <code><a href="/docs/linux/man/1-virt-sysprep/">virt-sysprep</a></code>(1) and <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1) have an <i>&#8211;ssh-inject</i> option for injecting an <font SIZE="-1">SSH</font> key into virtual machine disk images. They may create a <i>~user/.ssh</i> directory and <i>~user/.ssh/authorized_keys</i> file in the guest to do this. </p>
<p> In libguestfs &lt; 1.31.5 and libguestfs &lt; 1.30.2, the new directory and file would get mode <tt>0755</tt> and mode <tt>0644</tt> respectively. However these permissions (especially for <i>~user/.ssh</i>) are wider than the permissions that OpenSSH uses. In current libguestfs, the directory and file are created with mode <tt>0700</tt> and mode <tt>0600</tt>.</p>
<h3><font SIZE="-1">CVE-2015-8869</font></h3>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/CVE-2015-8869">https://bugzilla.redhat.com/CVE-2015-8869</a> </p>
<p> This vulnerability in OCaml might affect virt tools written in the OCaml programming language. It affects only 64 bit platforms. Because this bug affects code generation it is difficult to predict which precise software could be affected, and therefore our recommendation is that you recompile libguestfs using a version of the OCaml compiler where this bug has been fixed (or ask your Linux distro to do the same).</p>
<h3><font SIZE="-1">CVE-2017-5208, CVE-2017-5331, CVE-2017-5332, CVE-2017-5333, CVE-2017-6009, CVE-2017-6010, CVE-2017-6011</font></h3>
<p> Multiple vulnerabilities in the <code><a href="/docs/linux/man/1-wrestool/">wrestool</a></code>(1) program in the <tt>&quot;icoutils&quot;</tt> package can be exploited for local code execution on the host. </p>
<p> When libguestfs inspection (see &#8220;Inspection security&#8221; above) detects a Windows <font SIZE="-1">XP</font> or Windows 7 guest and is asked to find an associated icon for the guest, it will download an untrusted file from the guest and run <tt>&quot;wrestool -x&quot;</tt> on that file. This can lead to local code execution on the host. Any disk image or guest can be crafted to look like a Windows guest to libguestfs inspection, so just because you do not have Windows guests does not help. </p>
<p> Any program calling the libguestfs <font SIZE="-1">API</font> <tt>&quot;guestfs_inspect_get_icon&quot;</tt> could be vulnerable. This includes <code><a href="/docs/linux/man/1-virt-inspector/">virt-inspector</a></code>(1) and <code><a href="/docs/linux/man/1-virt-manager/">virt-manager</a></code>(1). </p>
<p> The solution is to update to the non-vulnerable version of icoutils (at least 0.31.1).</p>
<h3><font SIZE="-1">CVE-2017-7244, CVE-2017-7245, CVE-2017-7246</font></h3>
<p> Multiple vulnerabilities in <font SIZE="-1">PCRE</font> could be exploited to crash libguestfs (ie. cause a denial of service) when performing inspection on an untrusted virtual machine. </p>
<p> The solution is to update to a version of <font SIZE="-1">PCRE</font> with these bugs fixed (upstream version ≥ 8.41).</p>
<h3><font SIZE="-1">CVE-2018-11806</font></h3>
<p> Vulnerabilities affecting qemu user networking (<font SIZE="-1">SLIRP</font>) allow a malicious filesystem image to take control of qemu and from there attack the host. </p>
<p> This affects libguestfs when the backend is set to <tt>&quot;direct&quot;</tt> <i>and</i> networking is enabled. </p>
<p> The direct backend is the default upstream, but not in some downstream Linux distributions including Fedora, Red Hat Enterprise Linux and CentOS. It might also have been selected if you set the <tt>&quot;LIBGUESTFS_BACKEND=direct&quot;</tt> environment variable or called <tt>&quot;guestfs_set_backend (g, &quot;direct&quot;)&quot;</tt>. </p>
<p> Networking is enabled automatically by some tools (eg. <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1)), or is enabled if your code called <tt>&quot;guestfs_set_network (g, 1)&quot;</tt> (which is not the default). </p>
<p> The libvirt backend is not affected. </p>
<p> The solution is to update qemu to a version containing the fix (see <a rel="nofollow" href="https://lists.gnu.org/archive/html/qemu-devel/2018-06/msg01012.html">https://lists.gnu.org/archive/html/qemu-devel/2018-06/msg01012.html</a>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-release-notes/">guestfs-release-notes</a></code>(1), <code><a href="/docs/linux/man/1-guestfs-testing/">guestfs-testing</a></code>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2019 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Lesser General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> Lesser General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA</font></p>
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
<dd> Run <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbBB">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBC">AUTHORS</a></p>
<dd>
<dt><a href="#lbBD">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbBE">LICENSE</a></p>
<dd>
<dt><a href="#lbBF">BUGS</a></p>
<dd></dl>
