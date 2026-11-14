---
title: "guestfs-lua(3)"
name: "guestfs-lua"
section: "3"
letter: "g"
url: "/docs/linux/man/3-guestfs-lua/"
description: "guestfs-lua – How to use libguestfs from Lua"
---

<h2 class="name">NAME</h2>
<p> guestfs-lua &#8211; How to use libguestfs from Lua </p>
<h2>SYNOPSIS</h2>
<pre>
 local G = require &quot;guestfs&quot;
 g = G.create ()
 g:add_drive (&quot;test.img&quot;, { format = &quot;raw&quot;, readonly = true })
 g:launch ()
 devices = g:list_devices ()
 g:close ()
</pre>
<h2>DESCRIPTION</h2>
<p> This manual page documents how to call libguestfs from the Lua programming language. This page just documents the differences from the C <font SIZE="-1">API</font> and gives some examples. If you are not familiar with using libguestfs, you also need to read <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h3><font SIZE="-1">REQUIRING THE MODULE</font></h3>
<p> <tt>&quot;require &quot;guestfs&quot;&quot;</tt> returns the module, so you have to assign it to a local variable. Typical usage is: </p>
<pre>
 local G = require &quot;guestfs&quot;
</pre>
<p> (you can use any name you want instead of <tt>&quot;G&quot;</tt>, but in the examples in this man page we always use <tt>&quot;G&quot;</tt>).</p>
<h3><font SIZE="-1">OPENING AND CLOSING THE HANDLE</font></h3>
<p> To create a new handle, call: </p>
<pre>
 g = G.create ()
</pre>
<p> You can also use the optional arguments: </p>
<pre>
 g = G.create { environment = 0, close_on_exit = 0 }
</pre>
<p> to set the flags <tt>&quot;GUESTFS_CREATE_NO_ENVIRONMENT&quot;</tt> and/or <tt>&quot;GUESTFS_CREATE_NO_CLOSE_ON_EXIT&quot;</tt>. </p>
<p> The handle will be closed by the garbage collector, but you can also close it explicitly by doing: </p>
<pre>
 g:close ()
</pre>
<h3><font SIZE="-1">CALLING METHODS</font></h3>
<p> Use the ordinary Lua convention for calling methods on the handle. For example: </p>
<pre>
 g:set_verbose (true)
</pre>
<h3><font SIZE="-1">FUNCTIONS WITH OPTIONAL ARGUMENTS</font></h3>
<p> For functions that take optional arguments, the first arguments are the non-optional ones. The optional final argument is a table supplying the optional arguments. </p>
<pre>
 g:add_drive (&quot;test.img&quot;)
</pre>
<p> or: </p>
<pre>
 g:add_drive (&quot;test.img&quot;, { format = &quot;raw&quot;, readonly = true })
</pre>
<h3>64 <font SIZE="-1">BIT VALUES</font></h3>
<p> Currently 64 bit values must be passed as strings, and are returned as strings. This is because 32 bit Lua cannot handle 64 bit integers properly. We hope to come up with a better solution later.</p>
<h3><font SIZE="-1">ERRORS</font></h3>
<p> Most (but not all) errors are converted into objects (ie. tables) containing the following fields:</p>
<dl>
<dt>msg</p>
<dd> The error message (corresponding to &#8220;guestfs_last_error&#8221; in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)).</p>
<dt>code</p>
<dd> The <tt>&quot;errno&quot;</tt> (corresponding to &#8220;guestfs_last_errno&#8221; in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)).</dl>
<p> These objects also have <tt>&quot;__tostring&quot;</tt> functions attached to them so you can use <tt>&quot;tostring&quot;</tt> (or implicit conversion) to convert them into printable strings. </p>
<p> Note that the library also throws some errors as plain strings. You may need to check the type.</p>
<h3><font SIZE="-1">EVENTS</font></h3>
<p> Events can be registered by calling <tt>&quot;set_event_callback&quot;</tt>: </p>
<pre>
 eh = g:set_event_callback (cb, &quot;close&quot;)
</pre>
<p> or to register a single callback for multiple events make the second argument a list: </p>
<pre>
 eh = g:set_event_callback (cb, { &quot;appliance&quot;, &quot;library&quot;, &quot;trace&quot; })
</pre>
<p> A list of all valid event types (strings) is in the global variable <tt>&quot;G.event_all&quot;</tt>. </p>
<p> The callback (<tt>&quot;cb&quot;</tt>) is called with the following parameters: </p>
<pre><code>
function cb(g, event, eh, flags, buf, array)-- g is the guestfs handle
    -- event is a string which is the name of the event that fired
    -- flags is always zero
    -- buf is the data buffer(eg.log message etc)-- array is the array of 64 bit ints(eg.progress bar status etc)... end
</code></pre>
<p> You can also remove a callback using the event handle (<tt>&quot;eh&quot;</tt>) that was returned when you registered the callback: </p>
<pre>
 g:delete_event_callback (eh)
</pre>
<h2>EXAMPLE 1: CREATE A DISK IMAGE</h2>
<p>&#8211;Example showing how to create a disk image.</p>
<p>  local G = require &#8220;guestfs&#8221;</p>
<p>    local output = &#8220;disk.img&#8221;</p>
<p>    local g = G.create()</p>
<p>                  &#8212; Create a raw &#8211;<br />
              format sparse disk image,<br />
        512 MB in size.file = io.open(output, &#8220;w&#8221;)<br />
                                  file : seek(&#8220;set&#8221;, 512 * 1024 * 1024)<br />
                                             file : write(&#8216; &#8216;)<br />
                                                        file : close()</p>
<p>                                                                   &#8212; Set the trace flag so that we can see each libguestfs call.g : set_trace(true)</p>
<p>                                                                                                                                         &#8212; Attach the disk image to libguestfs.g : add_drive(output, {format = &#8220;raw&#8221;, readonly = false})</p>
<p>                                                                                                                                                                                        &#8212; Run the libguestfs back &#8211;<br />
                              end.g : launch()</p>
<p>                                          &#8212; Get the list of devices.Because we only added one drive&#8211; above,<br />
        we expect that this list should contain a single&#8211; element.devices = g : list_devices() if table.getn(devices) ~ = 1 then<br />
                                                                                                                               error &#8220;expected a single device from list-devices&#8221; end</p>
<p>                                                                                                                           &#8212; Partition the disk as one single MBR partition.g : part_disk(devices[1], &#8220;mbr&#8221;)</p>
<p>                                                                                                                                                                                     &#8212; Get the list of partitions.We expect a single element,<br />
        which&#8211; is the partition we have just created.partitions = g : list_partitions() if table.getn(partitions) ~ = 1 then<br />
                                                                                                                           error &#8220;expected a single partition from list-partitions&#8221; end</p>
<p>                                                                                                                       &#8212; Create a filesystem on the partition.g : mkfs(&#8220;ext4&#8221;, partitions[1])</p>
<p>                                                                                                                                                                       &#8212; Now mount the filesystem so that we can add files.g : mount(partitions[1], &#8220;/&#8221;)</p>
<p>                                                                                                                                                                                                                                    &#8212; Create some files and<br />
                                                                                                                       directories.g : touch(&#8220;/empty&#8221;)<br />
                                                                                                                                           message = &#8220;Hello, world
&#8221; g : write(&#8220;/hello&#8221;, message)<br />
                                                                                                                                                                              g : mkdir(&#8220;/foo&#8221;)</p>
<p>                                                                                                                                                                                      &#8212; This one uploads the local file /<br />
                                                                                                                                                                                  etc / resolv.conf into&#8211; the disk image.g : upload(&#8220;/etc/resolv.conf&#8221;, &#8220;/foo/resolv.conf&#8221;)</p>
<p>                                                                                                                                                                                                                                  &#8212; Because we wrote to the disk and<br />
                                                                                                                                                     we want to detect write&#8211; errors,<br />
        call g : shutdown.You don&#8217;t need to do this: &#8211;g : close will do it implicitly.g : shutdown()</p>
<p>                                                                                               &#8212; Note also that handles are automatically closed if they are<br />
                                                                                           &#8212; reaped by the garbage collector.You only need to call close<br />
                                                                                           &#8212; if you want to close the handle right away.g : close()</p>
<h2>EXAMPLE 2: INSPECT A VIRTUAL MACHINE DISK IMAGE</h2>
<pre><code>
 -- Example showing how to inspect a virtual machine disk.
 
 local G = require "guestfs"
 
 if table.getn (arg) == 1 then
    disk = arg[1]
 else
    error ("usage: inspect_vm disk.img")
 end
 
 local g = G.create ()
 
 -- Attach the disk image read-only to libguestfs.
 g:add_drive (disk, { -- format:"raw"
                      readonly = true })
 
 -- Run the libguestfs back-end.
 g:launch ()
 
 -- Ask libguestfs to inspect for operating systems.
 local roots = g:inspect_os ()
 if table.getn (roots) == 0 then
    error ("inspect_vm: no operating systems found")
 end
 
 for _, root in ipairs (roots) do
    print ("Root device: ", root)
 
    -- Print basic information about the operating system.
    print ("  Product name: ", g:inspect_get_product_name (root))
    print ("  Version:      ",
           g:inspect_get_major_version (root),
           g:inspect_get_minor_version (root))
    print ("  Type:         ", g:inspect_get_type (root))
    print ("  Distro:       ", g:inspect_get_distro (root))
 
    -- Mount up the disks, like guestfish -i.
    --
    -- Sort keys by length, shortest first, so that we end up
    -- mounting the filesystems in the correct order.
    mps = g:inspect_get_mountpoints (root)
    table.sort (mps,
                function (a, b)
                   return string.len (a) &lt; string.len (b)
                end)
    for mp,dev in pairs (mps) do
       pcall (function () g:mount_ro (dev, mp) end)
    end
 
    -- If /etc/issue.net file exists, print up to 3 lines.
    filename = "/etc/issue.net"
    if g:is_file (filename) then
       print ("--- ", filename, " ---")
       lines = g:head_n (3, filename)
       for _, line in ipairs (lines) do
          print (line)
       end
    end
 
    -- Unmount everything.
    g:umount_all ()
 end
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-examples/">guestfs-examples</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-erlang/">guestfs-erlang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-golang/">guestfs-golang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-java/">guestfs-java</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-ocaml/">guestfs-ocaml</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-perl/">guestfs-perl</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-python/">guestfs-python</a></i>(3), <i><a href="/docs/linux/man/1-guestfs-recipes/">guestfs-recipes</a></i>(1), <i><a href="/docs/linux/man/3-guestfs-ruby/">guestfs-ruby</a></i>(3), <a rel="nofollow" href="http://www.lua.org/,">http://www.lua.org/,</a> <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012 Red Hat Inc.</p>
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
<dt><a href="#lbAL">EXAMPLE 1: CREATE A DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAM">EXAMPLE 2: INSPECT A VIRTUAL MACHINE DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAN">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAO">AUTHORS</a></p>
<dd>
<dt><a href="#lbAP">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAQ">LICENSE</a></p>
<dd>
<dt><a href="#lbAR">BUGS</a></p>
<dd></dl>
