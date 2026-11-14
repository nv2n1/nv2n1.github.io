---
title: "guestfs-testing(1)"
name: "guestfs-testing"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-testing/"
description: "guestfs-testing – manual testing of libguestfs, you can help!"
---

<h2 class="name">NAME</h2>
<p> guestfs-testing &#8211; manual testing of libguestfs, you can help! </p>
<h2>DESCRIPTION</h2>
<p> This page has manual tests you can try on libguestfs. Everyone has a slightly different combination of platform, hardware and guests, so this testing is very valuable. Thanks for helping out! </p>
<p> Tests marked with a <code>*</code> (asterisk) can <code>destroy data</code> if you&#8217;re not careful. The others are safe and won&#8217;t modify anything. </p>
<p> These tests <code>require libguestfs ≥ 1.22</code>. </p>
<p> You can report bugs you find through this link: </p>
<p> <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> or post on the mailing list (registration is <code>not</code> required, but if you&#8217;re not registered then you&#8217;ll have to wait for a moderator to manually approve your message): </p>
<p> <a rel="nofollow" href="https://www.redhat.com/mailman/listinfo/libguestfs">https://www.redhat.com/mailman/listinfo/libguestfs</a></p>
<h2>TESTS</h2>
<h3>Run libguestfs-test-tool</h3>
<p> Run: </p>
<pre>
 libguestfs-test-tool
</pre>
<p> This command does a very simple, non-destructive test that basic libguestfs is functioning. You don&#8217;t need to run it as root. </p>
<p> If it <i>doesn&#8217;t</i> print <tt>&quot;===== TEST FINISHED OK =====&quot;</tt>, report it as a bug. It is very important that you include the <code>complete, unedited</code> output of <tt>&quot;libguestfs-test-tool&quot;</tt> in your bug report. See the &#8220;<font SIZE="-1">BUGS&#8221;</font> section at the end of this page.</p>
<h3>Check <font SIZE="-1">KVM</font> acceleration is being used.</h3>
<p> If your host has hardware virt acceleration, then with a hot cache libguestfs should be able to start up in a few seconds. Run the following command a few times: </p>
<pre>
 time guestfish -a /dev/null run
</pre>
<p> After a few runs, the time should settle down to a few seconds (under 3 seconds on fast 64 bit hardware). </p>
<p> If the command above does not work at all, use <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1).</p>
<h3>Check which version of libguestfs, qemu, libvirt, etc is being used.</h3>
<p> Look at the output of <tt>&quot;libguestfs-test-tool&quot;</tt> and check:</p>
<dl>
<dt>&bull;</p>
<dd> Which version of libguestfs is being used? Near the beginning of the output you&#8217;ll see a line like: </p>
<pre>
 library version: 1.22.0fedora=19,release=1.fc19,libvirt
</pre>
<dt>&bull;</p>
<dd> Is libvirt being used? You can tell the difference by looking for the backend: </p>
<pre>
 guestfs_get_backend: direct
</pre>
<p> or: </p>
<pre>
 guestfs_get_backend: libvirt
</pre>
<dt>&bull;</p>
<dd> Which version of qemu is being used? It may be printed out: </p>
<pre>
 libguestfs: qemu version 1.5
</pre>
<dt>&bull;</p>
<dd> Which kernel is being used? <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1) will try to pick the latest kernel installed on your machine. You can see the version in the appliance output, eg: </p>
<pre><code>
[0.000000] Linux version 3.9.2 - 200.fc18.x86_64 [...]
</code></pre>
</dl>
<h3>Try to open a local guest image with guestfish.</h3>
<p> You can use any guest disk image for this test. Make sure you use the <tt>&quot;--ro&quot;</tt> flag so that <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) will open the disk image read-only. </p>
<pre>
 guestfish --ro -a /path/to/disk.img -i
</pre>
<p> If the command is successful, it should print out the guest operating system name and put you at the guestfish <tt>&quot;&gt;&lt;fs&gt;&quot;</tt> prompt. You can use guestfish commands like <tt>&quot;ll /&quot;</tt> to look inside the disk image. To exit, type <tt>&quot;exit&quot;</tt>. </p>
<p> If you get an error, try enabling debugging (add <tt>&quot;-v&quot;</tt> to the command line). Also make sure that <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) succeeds.</p>
<h3>Try to open a remote guest image with guestfish.</h3>
<p> You may also have to disable libvirt by setting this: </p>
<pre>
 export LIBGUESTFS_BACKEND=direct
</pre>
<p> If you have a disk image available over <font SIZE="-1">HTTP/FTP,</font> try to open it. </p>
<pre>
 guestfish --ro -i --format=raw -a <a rel="nofollow" href="http://www.example.com/disk.img">http://www.example.com/disk.img</a>
</pre>
<p> For <font SIZE="-1">SSH</font> you will need to make sure that ssh-agent is set up so you don&#8217;t need a password to log in to the remote machine. Then a command similar to this should work: </p>
<pre>
 guestfish --ro -i --format=raw \
   -a <a href="ssh://remote.example.com/path/to/disk.img">ssh://remote.example.com/path/to/disk.img</a>
</pre>
<p> If you get an error, try enabling debugging (add <tt>&quot;-v&quot;</tt> to the command line). Also make sure that <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) succeeds.</p>
<h3>Run virt-alignment-scan on all your guests.</h3>
<p> Run <code><a href="/docs/linux/man/1-virt-alignment-scan/">virt-alignment-scan</a></code>(1) on guests or disk images: </p>
<pre>
 virt-alignment-scan -a /path/to/disk.img
</pre>
<p> or: </p>
<pre>
 virt-alignment-scan -d Guest
</pre>
<p> Does the alignment report match how the guest partitions are aligned?</p>
<h3>Run virt-cat on some files in guests.</h3>
<p> <code><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></code>(1) can display files from guests. For a Linux guest, try: </p>
<pre>
 virt-cat LinuxGuest /etc/passwd
</pre>
<p> A recent feature is support for Windows paths, for example: </p>
<pre>
 virt-cat WindowsGuest 'c:\windows\win.ini'
</pre>
<p> An even better test is if you have a Windows guest with multiple drives. Do <tt>&quot;D:&quot;</tt>, <tt>&quot;E:&quot;</tt> etc paths work correctly?</p>
<h3><code>*</code> Copy some files into a <code>shut off</code> guest.</h3>
<p> <code><a href="/docs/linux/man/1-virt-copy-in/">virt-copy-in</a></code>(1) can recursively copy files and directories into a guest or disk image. </p>
<pre>
 virt-copy-in -d Guest /etc /tmp
</pre>
<p> This should copy local directory <i>/etc</i> to <i>/tmp/etc</i> in the guest (recursively). If you boot the guest, can you see all of the copied files and directories? </p>
<p> Shut the guest down and try copying multiple files and directories: </p>
<pre>
 virt-copy-in -d Guest /home /etc/issue /tmp
</pre>
<h3>Copy some files out of a guest.</h3>
<p> <code><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></code>(1) can recursively copy files and directories out of a guest or disk image. </p>
<pre>
 virt-copy-out -d Guest /home .
</pre>
<p> Note the final space and period in the command is not a typo. </p>
<p> This should copy <i>/home</i> from the guest into the current directory.</p>
<h3>Run virt-df.</h3>
<p> <code><a href="/docs/linux/man/1-virt-df/">virt-df</a></code>(1) lists disk space. Run: </p>
<pre>
 virt-df
</pre>
<p> You can try comparing this to the results from <code><a href="/docs/linux/man/1-df/">df</a></code>(1) inside the guest, but there are some provisos:</p>
<dl>
<dt>&bull;</p>
<dd> The guest must be idle.</p>
<dt>&bull;</p>
<dd> The guest disks must be synched using <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1).</p>
<dt>&bull;</p>
<dd> Any action such as booting the guest will write log files causing the numbers to change.</dl>
<p> We don’t guarantee that the numbers will be identical even under these circumstances. They should be similar. It would indicate a bug if you saw greatly differing numbers.</p>
<h3>Try importing virt-df <font SIZE="-1">CSV</font> output into a spreadsheet or database.</h3>
<p> Run: </p>
<pre>
 virt-df --csv &gt; /tmp/report.csv
</pre>
<p> Now try to load this into your favorite spreadsheet or database. Are the results reproduced faithfully in the spreadsheet/database? </p>
<p> <a rel="nofollow" href="http://www.postgresql.org/docs/8.1/static/sql-copy.html">http://www.postgresql.org/docs/8.1/static/sql-copy.html</a> <a rel="nofollow" href="http://dev.mysql.com/doc/refman/5.1/en/load-data.html">http://dev.mysql.com/doc/refman/5.1/en/load-data.html</a></p>
<h3><code>*</code> Edit a file in a <code>shut off</code> guest.</h3>
<p> <code><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></code>(1) can edit files in guests. Try this command on a <font SIZE="-1">RHEL</font> or Fedora guest: </p>
<pre>
 virt-edit LinuxGuest /etc/sysconfig/network
</pre>
<p> On other Linux guests try editing other files such as: </p>
<pre>
 virt-edit LinuxGuest /etc/motd
</pre>
<p> Are the changes seen inside the guest when it is booted?</p>
<h3>Display the filesystems / partitions / LVs in a guest.</h3>
<p> <code><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></code>(1) can be used to display filesystems in a guest. Try this command on any disk image or guest: </p>
<pre>
 virt-filesystems -a /path/to/disk.img --all --long -h
</pre>
<p> or: </p>
<pre>
 virt-filesystems -d Guest --all --long -h
</pre>
<p> Do the results match what is seen in the guest?</p>
<h3>Run virt-inspector on all your guests.</h3>
<p> Use <code><a href="/docs/linux/man/1-virt-inspector/">virt-inspector</a></code>(1) to get a report on all of your guests or disk images: </p>
<pre>
 virt-inspector -a /path/to/disk.img | less
</pre>
<p> or: </p>
<pre>
 virt-inspector -d Guest | less
</pre>
<p> Do the results match what is actually in the guest? </p>
<p> If you have an unusual guest (a rare Linux distro, a very new version of Windows), does virt-inspector recognize it? If not, then it&#8217;s probably a bug.</p>
<h3>Try the auditing features of virt-ls on all your guests.</h3>
<p> List all setuid or setgid programs in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d Guest / | grep '^- [42]'
</pre>
<p> List all public-writable directories in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d Guest / | grep '^d ...7'
</pre>
<p> List all Unix domain sockets in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d Guest / | grep '^s'
</pre>
<p> List all regular files with filenames ending in ‘.png’: </p>
<pre>
 virt-ls -lR -d Guest / | grep -i '^-.*\.png$'
</pre>
<p> Display files larger than 10MB in home directories: </p>
<pre>
 virt-ls -lR -d Guest /home | awk '$3 &gt; 10*1024*1024'
</pre>
<p> Find everything modified in the last 7 days: </p>
<pre>
 virt-ls -lR -d Guest --time-days / | awk '$6 &lt;= 7'
</pre>
<p> Find regular files modified in the last 24 hours: </p>
<pre>
 virt-ls -lR -d Guest --time-days / | grep '^-' | awk '$6 &lt; 1'
</pre>
<p> Do the results match what is in the guest?</p>
<h3>Create a disk image from a tarball.</h3>
<p> Use <code><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></code>(1) to create a disk image from any tarball that you happen to have: </p>
<pre>
 virt-make-fs --partition=mbr --type=vfat /any/tarball.tar.gz output.img
</pre>
<p> Add ‘output.img’ as a raw disk to an existing guest. Check the guest can see the files. This test is particularly useful if you try it with a Windows guest. </p>
<p> Try other partitioning schemes, eg. <i>&#8211;partition=gpt</i>. </p>
<p> Try other filesystem formats, eg. <i>&#8211;type=ntfs</i>, <i>&#8211;type=ext2</i>.</p>
<h3><code>*</code> Run virt-rescue on a <code>shut off</code> disk image or guest.</h3>
<p> Use <code><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></code>(1) to examine, rescue or repair a <code>shut off</code> guest or disk image: </p>
<pre>
 virt-rescue -a /path/to/disk.img
</pre>
<p> or: </p>
<pre>
 virt-rescue -d Guest
</pre>
<p> Can you use ordinary shell commands to examine the guest?</p>
<h3><code>*</code> Resize your guests.</h3>
<p> Use <code><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></code>(1) to give a guest some more disk space. For example, if you have a disk image that is smaller than 30G, increase it to 30G by doing: </p>
<pre><code>
truncate - s 30G newdisk.img virt - filesystems - a / path / to / olddisk.img-- all-- long - h virt - resize / path / to / olddisk.img newdisk.img-- expand / dev / sda1 qemu - kvm - m 1024 - hda newdisk.img
</code></pre>
<p> Does the guest still boot? Try expanding other partitions.</p>
<h3><code>*</code> Sparsify a guest disk.</h3>
<p> Using <code><a href="/docs/linux/man/1-virt-sparsify/">virt-sparsify</a></code>(1), make a disk image more sparse: </p>
<pre>
 virt-sparsify /path/to/olddisk.img newdisk.img
</pre>
<p> Is <i>newdisk.img</i> still bootable after sparsifying? Is the resulting disk image smaller (use <tt>&quot;du&quot;</tt> to check)?</p>
<h3>Build and boot a guest</h3>
<p> Using <code><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></code>(1), choose a guest from the list: </p>
<pre>
 virt-builder -l
</pre>
<p> build it: </p>
<pre>
 virt-builder -o disk.img [os-version from list above]
</pre>
<p> and boot it: </p>
<pre>
 qemu-kvm -cpu host -m 2048 -drive file=disk.img,format=raw
</pre>
<p> Does it boot?</p>
<h3><code>*</code> Sysprep a <code>shut off</code> Linux guest.</h3>
<p> <code>Note</code> that this really will mess up an existing guest, so it&#8217;s better to clone the guest before trying this. </p>
<pre>
 virt-sysprep --hostname newhost.example.com -a /path/to/disk.img
</pre>
<p> Was the sysprep successful? After booting, what changes were made and were they successful?</p>
<h3>Dump the Windows Registry from your Windows guests.</h3>
<p> Use <code><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></code>(1) to dump out the Windows Registry from any Windows guests that you have. </p>
<pre>
 virt-win-reg --unsafe-printable-strings WindowsGuest 'HKLM\Software' |
   less
 virt-win-reg --unsafe-printable-strings WindowsGuest 'HKLM\System' |
   less
</pre>
<p> Does the output match running <tt>&quot;regedit&quot;</tt> inside the guest? </p>
<p> A recent feature is the ability to dump user registries, so try this, replacing <i>username</i> with the name of a local user in the guest: </p>
<pre>
 virt-win-reg --unsafe-printable-strings WindowsGuest 'HKEY_USERS
