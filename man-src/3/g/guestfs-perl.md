---
title: "guestfs-perl(3)"
name: "guestfs-perl"
section: "3"
letter: "g"
url: "/docs/linux/man/3-guestfs-perl/"
description: "guestfs-perl – How to use libguestfs from Perl"
---

<h2 class="name">NAME</h2>
<p> guestfs-perl &#8211; How to use libguestfs from Perl </p>
<h2>SYNOPSIS</h2>
<pre><code>
use Sys::Guestfs;

my $g = Sys::Guestfs-&gt;new ();
$g-&gt;add_drive_opts('guest.img', format = &gt; 'raw');
$g-&gt;launch();
$g-&gt;mount('/dev/sda1', '/');
$g-&gt;touch('/hello');
$g-&gt;shutdown();
$g-&gt;close();
</code></pre>
<h2>DESCRIPTION</h2>
<p> This manual page documents how to call libguestfs from the Perl programming language. This page just documents the differences from the C <font SIZE="-1">API</font> and gives some examples. If you are not familiar with using libguestfs, you also need to read <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3). To read the full Perl <font SIZE="-1">API,</font> see <i><a href="/docs/linux/man/3-sys--guestfs/">Sys::Guestfs</a></i>(3).</p>
<h3><font SIZE="-1">ERRORS</font></h3>
<p> Errors from libguestfs functions turn into calls to <tt>&quot;croak&quot;</tt> (see <i><a href="/docs/linux/man/3-carp/">Carp</a></i>(3)).</p>
<h2>EXAMPLE 1: CREATE A DISK IMAGE</h2>
<p>#!/ usr / bin / env perl</p>
<p>#Example showing how to create a disk image.</p>
<p>use strict;<br />
use warnings;<br />
use Sys::Guestfs;</p>
<p>my $output = &#8220;disk.img&#8221;;</p>
<p>my $g = new Sys::Guestfs();</p>
<p>#Create a raw &#8211; format sparse disk image, 512 MB in size.<br />
$g-&gt;disk_create($output, &#8220;raw&#8221;, 512 * 1024 * 1024);</p>
<p>#Set the trace flag so that we can see each libguestfs call.<br />
$g-&gt;set_trace(1);</p>
<p>#Attach the disk image to libguestfs.<br />
$g-&gt;add_drive_opts($output, format = &gt; &#8220;raw&#8221;, readonly = &gt; 0);</p>
<p>#Run the libguestfs back &#8211; end.<br />
$g-&gt;launch();</p>
<p>#Get the list of devices.Because we only added one drive<br />
#above, we expect that this list should contain a single<br />
#element.<br />
my @devices = $g-&gt;list_devices();<br />
if (@devices != 1) {<br />
    die &#8220;error: expected a single device from list-devices&#8221;;<br />
}</p>
<p>#Partition the disk as one single MBR partition.<br />
$g-&gt;part_disk($devices[0], &#8220;mbr&#8221;);</p>
<p>#Get the list of partitions.We expect a single element, which<br />
#is the partition we have just created.<br />
my @partitions = $g-&gt;list_partitions();<br />
if (@partitions != 1) {<br />
    die &#8220;error: expected a single partition from list-partitions&#8221;;<br />
}</p>
<p>#Create a filesystem on the partition.<br />
$g-&gt;mkfs(&#8220;ext4&#8221;, $partitions[0]);</p>
<p>#Now mount the filesystem so that we can add files.<br />
$g-&gt;mount($partitions[0], &#8220;/&#8221;);</p>
<p>#Create some files and directories.<br />
$g-&gt;touch(&#8220;/empty&#8221;);<br />
my $message = &#8220;Hello, world
&#8221;;<br />
$g-&gt;write(&#8220;/hello&#8221;, $message);<br />
$g-&gt;mkdir(&#8220;/foo&#8221;);</p>
<p>#This one uploads the local file / etc / resolv.conf into<br />
#the disk image.<br />
$g-&gt;upload(&#8220;/etc/resolv.conf&#8221;, &#8220;/foo/resolv.conf&#8221;);</p>
<p>#Because we wrote to the disk and we want to detect write<br />
#errors, call $g-&gt;shutdown.You don&#8217;t need to do this:<br />
#$g-&gt;close will do it implicitly.<br />
$g-&gt;shutdown();</p>
<p>#Note also that handles are automatically closed if they are<br />
#reaped by reference counting.You only need to call close<br />
#if you want to close the handle right away.<br />
$g-&gt;close();</p>
<h2>EXAMPLE 2: INSPECT A VIRTUAL MACHINE DISK IMAGE</h2>
<pre><code>
#!/ usr / bin / env perl

#Example showing how to inspect a virtual machine disk.

use strict;
use warnings;
use Sys::Guestfs;

if (@ARGV &lt; 1) {
    die "usage: inspect_vm disk.img"
}

my $disk = $ARGV[0];

my $g = new Sys::Guestfs();

#Attach the disk image read - only to libguestfs.
#You could also add an optional format = &gt;... argument here.This is
#advisable since automatic format detection is insecure.
$g-&gt;add_drive_opts($disk, readonly = &gt; 1);

#Run the libguestfs back - end.
$g-&gt;launch();

#Ask libguestfs to inspect for operating systems.
my @roots = $g-&gt;inspect_os();
if (@roots == 0) {
    die "inspect_vm: no operating systems found";
}

 for
     my $root(@roots)
     {
         printf "Root device: %s
", $root;

#Print basic information about the operating system.
         printf "  Product name: %s
", $g-&gt;inspect_get_product_name($root);
         printf "  Version:      %d.%d
",
             $g-&gt;inspect_get_major_version($root),
             $g-&gt;inspect_get_minor_version($root);
         printf "  Type:         %s
", $g-&gt;inspect_get_type($root);
         printf "  Distro:       %s
", $g-&gt;inspect_get_distro($root);

#Mount up the disks, like guestfish - i.
#
#Sort keys by length, shortest first, so that we end up
#mounting the filesystems in the correct order.
         my % mps = $g-&gt;inspect_get_mountpoints($root);
         my @mps = sort{length $a &lt;=&gt; length $b}(keys % mps);
     for
         my $mp(@mps)
         {
             eval{$g-&gt;mount_ro($mps{$mp}, $mp)};
             if ($ @) {
                 print "$@ (ignored)
"
             }
         }

#If / etc / issue.net file exists, print up to 3 lines.
     my $filename = "/etc/issue.net";
     if ($g-&gt;is_file($filename)) {
         printf "--- %s ---
", $filename;
         my @lines = $g-&gt;head_n(3, $filename);
         print "$_
" foreach @lines;
     }

#Unmount everything.
     $g-&gt;umount_all()
     }
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-sys--guestfs/">Sys::Guestfs</a></i>(3), <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-examples/">guestfs-examples</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-erlang/">guestfs-erlang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-golang/">guestfs-golang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-java/">guestfs-java</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-lua/">guestfs-lua</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-ocaml/">guestfs-ocaml</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-python/">guestfs-python</a></i>(3), <i><a href="/docs/linux/man/1-guestfs-recipes/">guestfs-recipes</a></i>(1), <i><a href="/docs/linux/man/3-guestfs-ruby/">guestfs-ruby</a></i>(3), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2012 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This manual page contains examples which we hope you will use in your programs. The examples may be freely copied, modified and distributed for any purpose without any restrictions.</p>
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
<dt><a href="#lbAF">EXAMPLE 1: CREATE A DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAG">EXAMPLE 2: INSPECT A VIRTUAL MACHINE DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAH">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAI">AUTHORS</a></p>
<dd>
<dt><a href="#lbAJ">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAK">LICENSE</a></p>
<dd>
<dt><a href="#lbAL">BUGS</a></p>
<dd></dl>
