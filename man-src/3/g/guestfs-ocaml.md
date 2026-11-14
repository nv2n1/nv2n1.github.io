---
title: "guestfs-ocaml(3)"
name: "guestfs-ocaml"
section: "3"
letter: "g"
url: "/docs/linux/man/3-guestfs-ocaml/"
description: "guestfs-ocaml – How to use libguestfs from OCaml"
---

<h2 class="name">NAME</h2>
<p> guestfs-ocaml &#8211; How to use libguestfs from OCaml </p>
<h2>SYNOPSIS</h2>
<p> Module style: </p>
<pre>
 let g = Guestfs.create () in
 Guestfs.add_drive_opts g ~format:&quot;raw&quot; ~readonly:true &quot;disk.img&quot;;
 Guestfs.launch g;
</pre>
<p> Object-oriented style: </p>
<pre><code>
let g = new Guestfs.guestfs() in
            g #add_drive_opts ~format : "raw" ~readonly : true "disk.img";
g #launch();
ocamlfind opt prog.ml - package guestfs - linkpkg - o prog or : ocamlopt - I + guestfs mlguestfs.cmxa prog.ml - o prog
</code></pre>
<h2>DESCRIPTION</h2>
<p> This manual page documents how to call libguestfs from the OCaml programming language. This page just documents the differences from the C <font SIZE="-1">API</font> and gives some examples. If you are not familiar with using libguestfs, you also need to read <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h3><font SIZE="-1">PROGRAMMING STYLES</font></h3>
<p> There are two different programming styles supported by the OCaml bindings. You can use a module style, with each C function mapped to an OCaml function: </p>
<p>int guestfs_set_verbose(guestfs_h *g, int flag);</p>
<p> becomes: </p>
<pre>
 val Guestfs.set_verbose : Guestfs.t -&gt; bool -&gt; unit
</pre>
<p> Alternately you can use an object-oriented style, calling methods on the class <tt>&quot;Guestfs.guestfs&quot;</tt>: </p>
<pre>
 method set_verbose : bool -&gt; unit
</pre>
<p> The object-oriented style is usually briefer, and the minor performance penalty isn&#8217;t noticeable in the general overhead of performing libguestfs functions.</p>
<h3><font SIZE="-1">CLOSING THE HANDLE</font></h3>
<p> The handle is closed when it is reaped by the garbage collector. Because libguestfs handles include a lot of state, it is also possible to close (and hence free) them explicitly by calling <tt>&quot;Guestfs.close&quot;</tt> or the <tt>&quot;#close&quot;</tt> method.</p>
<h3><font SIZE="-1">EXCEPTIONS</font></h3>
<p> Errors from libguestfs functions are mapped into the <tt>&quot;Guestfs.Error&quot;</tt> exception. This has a single parameter which is the error message (a string). </p>
<p> Calling any function/method on a closed handle raises <tt>&quot;Guestfs.Handle_closed&quot;</tt>. The single parameter is the name of the function that you called.</p>
<h2>EXAMPLE: CREATE A DISK IMAGE</h2>
<p>(*Example showing how to create a disk image.*)</p>
<p>    open Unix<br />
    open Printf</p>
<p>    let output = &#8220;disk.img&#8221;</p>
<p>    let() =<br />
        let g = new Guestfs.guestfs() in</p>
<p>                (*Create a raw &#8211; format sparse disk image, 512 MB in size.*)<br />
                    g #disk_create output &#8220;raw&#8221;(Int64.of_int(512 * 1024 * 1024));</p>
<p>(*Set the trace flag so that we can see each libguestfs call.*)<br />
    g #set_trace true;</p>
<p>(*Attach the disk image to libguestfs.*)<br />
    g #add_drive_opts ~format : &#8220;raw&#8221; ~readonly : false output;</p>
<p>(*Run the libguestfs back &#8211; end.*)<br />
    g #launch();</p>
<p>(*Get the list of devices.Because we only added one drive<br />
      *above,<br />
 we expect that this list should contain a single<br />
     *element.<br />
         *)<br />
    let devices = g #list_devices() in<br />
                  if Array.length devices&lt;&gt; 1 then<br />
                  failwith &#8220;error: expected a single device from list-devices&#8221;;</p>
<p>(*Partition the disk as one single MBR partition.*)<br />
    g #part_disk devices.(0) &#8220;mbr&#8221;;</p>
<p>(*Get the list of partitions.We expect a single element, which<br />
                                                             *is the partition we have just created.<br />
                                                                 *)<br />
    let partitions = g #list_partitions() in<br />
                     if Array.length partitions&lt;&gt; 1 then<br />
                     failwith &#8220;error: expected a single partition from list-partitions&#8221;;</p>
<p>(*Create a filesystem on the partition.*)<br />
    g #mkfs &#8220;ext4&#8221; partitions.(0);</p>
<p>(*Now mount the filesystem so that we can add files.*)<br />
    g #mount partitions.(0) &#8220;/&#8221;;</p>
<p>(*Create some files and directories.*)<br />
    g #touch &#8220;/empty&#8221;;<br />
let message = &#8220;Hello, world
&#8221; in<br />
    g #write &#8220;/hello&#8221; message;<br />
g #mkdir &#8220;/foo&#8221;;</p>
<p>(*This one uploads the local file / etc / resolv.conf into * the disk image.*)<br />
    g #upload &#8220;/etc/resolv.conf&#8221;<br />
              &#8220;/foo/resolv.conf&#8221;;</p>
<p>(*Because we wrote to the disk and we want to detect write<br />
     *errors,<br />
 call g #shutdown.You don&#8217;t need to do this:<br />
     *g #close will do it implicitly.<br />
         *)<br />
    g #shutdown();</p>
<p>(*Note also that handles are automatically closed if they are<br />
      *reaped by the garbage collector.You only need to call close<br />
          *if you want to close the handle right away.<br />
              *)<br />
    g #close()</p>
<h2>EXAMPLE: INSPECT A VIRTUAL MACHINE DISK IMAGE</h2>
<p>(*Example showing how to inspect a virtual machine disk.*)</p>
<p>    open Printf</p>
<p>    let disk =<br />
        if Array.length Sys.argv = 2 then<br />
                                   Sys.argv.(1) else failwith &#8220;usage: inspect_vm disk.img&#8221;</p>
<p>                                   let() =<br />
            let g = new Guestfs.guestfs() in</p>
<p>                    (*Attach the disk image read &#8211; only to libguestfs.*)<br />
                        g #add_drive_opts(*~format<br />
                                          : &#8220;raw&#8221; *) ~readonly : true disk;</p>
<p>(*Run the libguestfs back &#8211; end.*)<br />
    g #launch();</p>
<p>   (* Ask libguestfs to inspect for operating systems. *)<br />
   let roots = g#inspect_os () in<br />
   if Array.length roots = 0 then<br />
     failwith &#8220;inspect_vm: no operating systems found&#8221;;</p>
<p>   Array.iter(<br />
       fun root-&gt;printf &#8220;Root device: %s
&#8221; root;</p>
<p>       (*Print basic information about the operating system.*)<br />
           printf &#8221;  Product name: %s
&#8221;(g #inspect_get_product_name root);<br />
       printf &#8221;  Version:      %d.%d
&#8221;(g #inspect_get_major_version root)(g #inspect_get_minor_version root);<br />
       printf &#8221;  Type:         %s
&#8221;(g #inspect_get_type root);<br />
       printf &#8221;  Distro:       %s
&#8221;(g #inspect_get_distro root);</p>
<p>       (*Mount up the disks, like guestfish &#8211; i.* *Sort keys by length, shortest first, so that we end up *mounting the filesystems in the correct order.*)<br />
           let mps = g #inspect_get_mountpoints root in<br />
               let cmp(a, _)(b, _) =<br />
                   compare(String.length a)(String.length b) in<br />
                       let mps = List.sort cmp mps in<br />
                                     List.iter(<br />
                                         fun(mp, dev)-&gt;try g #mount_ro dev mp<br />
                                             with Guestfs.Error msg-&gt;eprintf &#8220;%s (ignored)
&#8221; msg) mps;</p>
<p>       (*If / etc / issue.net file exists, print up to 3 lines.*)<br />
           let filename = &#8220;/etc/issue.net&#8221; in if g #is_file filename then(<br />
               printf &#8220;&#8212; %s &#8212;
&#8221; filename;<br />
               let lines = g #head_n 3 filename in<br />
                               Array.iter print_endline lines);</p>
<p>       (*Unmount everything.*)<br />
           g #umount_all()) roots</p>
<h2>EXAMPLE: ENABLE DEBUGGING AND LOGGING</h2>
<pre><code>
(*Example showing how to enable debugging, and capture it into any
                                                   *custom logging system.
                                                       *)

    (*Events we are interested in.This bitmask covers all trace and
          *debug messages.
              *)
        let event_bitmask = [Guestfs.EVENT_LIBRARY;
                             Guestfs.EVENT_WARNING;
                             Guestfs.EVENT_APPLIANCE;
                             Guestfs.EVENT_TRACE]

    let rec main() =
        let g = new Guestfs.guestfs() in

                (*By default, debugging information is printed on stderr.To
                                  *capture it somewhere else you have to set up an event handler
                                      *which will be called back as debug messages are generated.To do
                                          *this use the event API.
                                              *
                                                  *For more information see EVENTS in guestfs(3)
                                                      .
                                                          *)
                    ignore(g #set_event_callback message_callback event_bitmask);

(*This is how debugging is enabled
 : **Setting the 'trace' flag in the handle means that each libguestfs
         *call is logged(name, parameters, return )
             .This flag is useful
                 *to see how libguestfs is being used by a program.
                     *
                         *Setting the 'verbose' flag enables a great deal of extra
                             *debugging throughout the system.This is useful if there is a
                                 *libguestfs error which you don't understand.
                                     *
                                         *Note that you should set the flags early on after creating the
                                             *handle.In particular if you set the verbose flag after launch
                                                 *then you won't see all messages.
                                                     *
                                                         *For more information see
 : *http
 : // libguestfs.org/guestfs-faq.1.html#debugging-libguestfs
 **Error messages raised by APIs are * not *debugging information,
 *and they are not affected by any of this.You may have to log * them separately.
                                                                     *)
    g #set_trace true;
g #set_verbose true;

(*Do some operations which will generate plenty of trace and debug
      *messages.
          *)
    g #add_drive "/dev/null";
g #launch();
g #close()

    (*This function is called back by libguestfs whenever a trace or
         *debug message is generated.*
             *For the classes of events we have registered above,
     'array' and
             *'array_len' will not be meaningful.Only 'buf' and 'buf_len' will * be interesting and these will contain the trace or
         debug message.*
             *This example simply redirects these messages to syslog,
     but
         *obviously you could do something more advanced here.
             *)
        and message_callback event event_handle buf array =
            if String.length buf &gt; 0 then(
                                       let event_name = Guestfs.event_to_string[event] in
                                                            Printf.printf "[%s] %S
%!" event_name buf)

                                       let() = main()
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-examples/">guestfs-examples</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-erlang/">guestfs-erlang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-golang/">guestfs-golang</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-java/">guestfs-java</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-lua/">guestfs-lua</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-perl/">guestfs-perl</a></i>(3), <i><a href="/docs/linux/man/3-guestfs-python/">guestfs-python</a></i>(3), <i><a href="/docs/linux/man/1-guestfs-recipes/">guestfs-recipes</a></i>(1), <i><a href="/docs/linux/man/3-guestfs-ruby/">guestfs-ruby</a></i>(3), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="http://caml.inria.fr/.">http://caml.inria.fr/.</a></p>
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
<dt><a href="#lbAH">EXAMPLE: CREATE A DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAI">EXAMPLE: INSPECT A VIRTUAL MACHINE DISK IMAGE</a></p>
<dd>
<dt><a href="#lbAJ">EXAMPLE: ENABLE DEBUGGING AND LOGGING</a></p>
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
