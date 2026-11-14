---
title: "guestfs-python(3)"
name: "guestfs-python"
section: "3"
letter: "g"
url: "/docs/linux/man/3-guestfs-python/"
description: "guestfs-python – How to use libguestfs from Python"
---

<h2 class="name">NAME</h2>
<p> guestfs-python &#8211; How to use libguestfs from Python </p>
<h2>SYNOPSIS</h2>
<pre>
 import guestfs
 g = guestfs.GuestFS (python_return_dict=True)
 g.add_drive_opts (&quot;disk.img&quot;, format=&quot;raw&quot;, readonly=1)
 g.launch ()
</pre>
<h2>DESCRIPTION</h2>
<p> This manual page documents how to call libguestfs from the Python programming language. This page just documents the differences from the C <font SIZE="-1">API</font> and gives some examples. If you are not familiar with using libguestfs, you also need to read <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h3>python_return_dict=True</h3>
<p> All new code should construct the handle using: </p>
<pre>
 g = guestfs.GuestFS (python_return_dict=True)
</pre>
<p> This indicates that your program wants to receive Python dicts for methods in the <font SIZE="-1">API</font> that return hashtables. </p>
<p> In a future version of libguestfs, this will become the default.</p>
<h3><font SIZE="-1">EXCEPTIONS</font></h3>
<p> Errors from libguestfs functions are mapped into <tt>&quot;RuntimeException&quot;</tt> with a single string argument which is the error message.</p>
<h3><font SIZE="-1">MORE DOCUMENTATION</font></h3>
<p> Type: </p>
<pre>
 $ python
 &gt;&gt;&gt; import guestfs
 &gt;&gt;&gt; help (guestfs)
</pre>
<h3><font SIZE="-1">USING PYTHON BINDINGS IN A VIRTUALENV</font></h3>
<p> These bindings are <i>not</i> available in pypi owing to a licensing problem. See <a rel="nofollow" href="https://bugzilla.redhat.com/1075594">https://bugzilla.redhat.com/1075594</a> for current status. </p>
<p> However we do publish a Python distribution for selected stable versions of libguestfs in <a rel="nofollow" href="http://libguestfs.org/download/python.">http://libguestfs.org/download/python.</a> You can use it like this: </p>
<pre>
 pip install <a rel="nofollow" href="http://libguestfs.org/download/python/guestfs-1.XX.YY.tar.gz">http://libguestfs.org/download/python/guestfs-1.XX.YY.tar.gz</a>
</pre>
<h2>EXAMPLE 1: CREATE A DISK IMAGE</h2>
<pre><code>
#Example showing how to create a disk image.

import guestfs

    output = "disk.img"

#All new Python code should pass python_return_dict = True
#to the constructor.It indicates that your program wants
#to receive Python dicts for methods in the API that return
#hashtables.
    g = guestfs.GuestFS(python_return_dict = True)

#Create a raw - format sparse disk image, 512 MB in size.
                            g.disk_create(output, "raw", 512 * 1024 * 1024);

#Set the trace flag so that we can see each libguestfs call.
g.set_trace(1)

#Attach the disk image to libguestfs.
    g.add_drive_opts(output, format = "raw", readonly = 0)

#Run the libguestfs back - end.
        g.launch()

#Get the list of devices.Because we only added one drive
#above, we expect that this list should contain a single
#element.
            devices = g.list_devices()
                          assert(len(devices) == 1)

#Partition the disk as one single MBR partition.
                              g.part_disk(devices[0], "mbr")

#Get the list of partitions.We expect a single element, which
#is the partition we have just created.
                                  partitions = g.list_partitions()
                                                   assert(len(partitions) == 1)

#Create a filesystem on the partition.
                                                       g.mkfs("ext4", partitions[0])

#Now mount the filesystem so that we can add files.
                                                           g.mount(partitions[0], "/")

#Create some files and directories.
                                                               g.touch("/empty")
                                                                   message = "Hello, world
" g.write("/hello", message)
                                                                                 g.mkdir("/foo")

#This one uploads the local file / etc / resolv.conf into
#the disk image.
                                                                                     g.upload("/etc/resolv.conf", "/foo/resolv.conf")

#Because we wrote to the disk and we want to detect write
#errors, call g.shutdown.You don't need to do this:
#g.close will do it implicitly.
                                                                                         g.shutdown()

#Note also that handles are automatically closed if they are
#reaped by reference counting.You only need to call close
#if you want to close the handle right away.
                                                                                             g.close()
</code></pre>
<h2>EXAMPLE 2: INSPECT A VIRTUAL MACHINE DISK IMAGE</h2>
<pre><code>
#Example showing how to inspect a virtual machine disk.

import sys import guestfs

    assert(len(sys.argv) == 2)
               disk = sys.argv[1]

#All new Python code should pass python_return_dict = True
#to the constructor.It indicates that your program wants
#to receive Python dicts for methods in the API that return
#hashtables.
                               g = guestfs.GuestFS(python_return_dict = True)

#Attach the disk image read - only to libguestfs.
                                                       g.add_drive_opts(disk, readonly = 1)

#Run the libguestfs back - end.
                                                                                  g.launch()

#Ask libguestfs to inspect for operating systems.
                                                                                               roots = g.inspect_os() if len (roots) == 0 :raise(Error("inspect_vm: no operating systems found"))

                                                                                                   for root in roots:print "Root device: %s" % root

#Print basic information about the operating system.
                                                                                           print "  Product name: %s" %(g.inspect_get_product_name(root))
                                                                                                                            print "  Version:      %d.%d" %
                                                                                                                        (g.inspect_get_major_version(root),
                                                                                                                                                     g.inspect_get_minor_version(root))
                                                                                                                                                         print "  Type:         %s" %(g.inspect_get_type(root))
                                                                                                                                                                                          print "  Distro:       %s" %(g.inspect_get_distro(root))

#Mount up the disks, like guestfish - i.
#
#Sort keys by length, shortest first, so that we end up
#mounting the filesystems in the correct order.
                                                                                                                                                                                                                           mps = g.inspect_get_mountpoints(root)
                                                                                                                                                                                                                               def compare(a, b) : return len(a) - len(b) for device in sorted(mps.keys(), compare) : try :g.mount_ro(mps[device], device)
                                                                                                                                                                                                                                                                                                                                                       except RuntimeError as msg:print "%s (ignored)" % msg

#If / etc / issue.net file exists, print up to 3 lines.
                                                                                                                                                                                                                                                                                                                                          filename = "/etc/issue.net" if g.is_file(filename) :print "--- %s ---" % filename lines = g.head_n(3, filename) for line in lines:print line

#Unmount everything.
                                                                                                                                                                                                                                                                                                                                                                                                                                             g.umount_all()
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-examples/">guestfs-examples</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-erlang/">guestfs-erlang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-golang/">guestfs-golang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-java/">guestfs-java</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-lua/">guestfs-lua</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-ocaml/">guestfs-ocaml</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-perl/">guestfs-perl</a></i>(3), <i><a href="/docs/linux/man/1-guestfs-recipes/">guestfs-recipes</a></i>(1), <i><a href="/docs/linux/man/3-guestfs-ruby/">guestfs-ruby</a></i>(3), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010-2012 Red Hat Inc.</p>
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
<dt><a href="#lbAI">EXAMPLE 1: CREATE A DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAJ">EXAMPLE 2: INSPECT A VIRTUAL MACHINE DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAL">AUTHORS</a></p>
<dd>
<dt><a href="#lbAM">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAN">LICENSE</a></p>
<dd>
<dt><a href="#lbAO">BUGS</a></p>
<dd></dl>
