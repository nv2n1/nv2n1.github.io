---
title: "hugectl(8)"
name: "hugectl"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hugectl/"
description: "hugectl – Control policy for backing text, data and malloc() with hugepages"
---

<p>hugectl &#8211; Control policy for backing text, data and malloc() with hugepages</p>
<h2>Synopsis</h2>
<p><code>hugectl [options] command {arguments}</code></p>
<h2>Description</h2>
<p><code>hugectl</code> runs processes with a specific policy for backing memory regions with hugepages. The use of hugepages benefit applications that use large amounts of address space and suffer a performance hit due to TLB misses. Policy is enforced by <code>libhugetlbfs</code> and <code>hugectl</code> configures the environment based on the options provided. Wall-clock time or oprofile can be used to determine if there is a performance benefit from using hugepages or not. To effectively back text/data, the target process must be relinked to align the ELF segments on a hugepage boundary. The library also supports more options for the control of memory regions than are exposed by the <code>hugectl</code> utility. See the <code>libhugetlbfs</code> manual page for more details. The following options affect what memory regions are backed by hugepages.</p>
<dl>
<dt><code>&#8211;text[=&lt;size&gt;],&#8211;data[=&lt;size&gt;],&#8211;bss[=&lt;size&gt;]</code></p>
<dd>Back the text, data or BSS segments with hugepages, optionally with pages of the specified size. To be effective, the process must be relinked as described in the HOWTO to align the ELF segments. It is possible to partially back segments using the HUGETLB_FORCE_ELMAP environment variable as described in the <code>libhugetlbfs</code> manual page.</p>
<dt><code>&#8211;heap[=&lt;size&gt;]</code></p>
<dd>Use the glibc morecore hook to back malloc() with hugepages, optionally with pages of the specified size. Note that this does not affect brk() segments and applications that use custom allocators potentially do not use hugepages for their heap even with this option specified.</p>
<dt><code>&#8211;shm</code></p>
<dd>This option overrides shmget() to back shared memory regions with hugepages if possible. Segment size requests will be aligned to fit to the default hugepage size region.</p>
<dt><code>&#8211;share-text</code></p>
<dd>Request that multiple application instances share text segments that are backed with huge pages. This option sets the environment variable HUGETLB_SHARE to 1.</p>
<dt><code>&#8211;thp</code></p>
<dd>Align heap regions to huge page size for promotion by khugepaged. For more information on transparent huge pages see linux-2.6/Documentation/transhuge.txt  The following options affect how <code>hugectl</code> behaves.</p>
<dl>
<dt><code>&#8211;no-preload</code></p>
<dd>Disable any pre-loading of the <code>libhugetlbfs</code> library. This may be necessary if only the heap is being backed by hugepages and the application is already linked against the library. <code>hugectl</code> may pre-load the library by mistake and this option prevents that.</p>
<dt><code>&#8211;force-preload</code></p>
<dd>Force pre-loading of the <code>libhugetlbfs</code> library. This option is used when the segments of the binary are aligned to the hugepage boundary of interest but the binary is not linked against libhugetlbfs. This is useful on PPC64 where binaries are aligned to 64K as required by the ABI and the kernel is using a 4K base pagesize.</p>
<dt><code>&#8211;no-reserve</code></p>
<dd>By default, huge pages are reserved at mmap() time so future faults will succeed. This avoids unexpected application but some applications depend on memory overcommit to create large sparse mappings. For this type of application, this switch will create huge page backed mappings without a reservation if the kernel is recent enough to make this operation safe. Use this option with extreme care as in the event huge pages are not available when the mapping is faulted, the application will be killed.</p>
<dt><code>&#8211;dry-run</code></p>
<dd>Instead of running the process, the <code>hugectl</code> utility will describe what environment variables it set for <code>libhugetlbfs</code>. This is useful if additional environment variables are to be set and a launcher shell script is being developed.</p>
<dt><code>&#8211;library-use-path</code></p>
<dd>By default, <code>hugectl</code> will use the version of <code>libhugetlbfs</code> it was installed with, even if this is not in the LD_LIBRARY_PATH environment. Using this option forces <code>hugectl</code> to use the version of <code>libhugetlbfs</code> installed in the library system path.</p>
<dt><code>&#8211;library-path &lt;path&gt;</code></p>
<dd>This option forces <code>hugectl</code> to use the <code>libhugetlbfs</code> libraries within the given prefix.  The following options affect the verbosity of libhugetlbfs.</p>
<dl>
<dt><code>&#8211;verbose &lt;level&gt;, -v</code></p>
<dd>The default value for the verbosity level is 1 and the range of the value can be set with &#8211;verbose from 0 to 99. The higher the value, the more verbose the library will be. 0 is quiet and 3 will output much debugging information. The verbosity level is increased by one each time -v is specified.</p>
<dt><code>-q</code></p>
<dd>The -q option will drecease the verbosity level by 1 each time it is specified to a minimum of 0. </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1),</i> <i><a href="/docs/linux/man/7-hugeadm/">hugeadm</a>(7),</i> <i><a href="/docs/linux/man/7-libhugetlbfs/">libhugetlbfs</a>(7)</i></p>
<h2>Authors</h2>
<p>libhugetlbfs was written by various people on the libhugetlbfs-devel mailing list.</p>
