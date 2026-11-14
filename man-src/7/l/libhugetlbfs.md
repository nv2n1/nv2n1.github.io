---
title: "libhugetlbfs(7)"
name: "libhugetlbfs"
section: "7"
letter: "l"
url: "/docs/linux/man/7-libhugetlbfs/"
description: "libhugetlbfs – preload library to back text, data, malloc() or shared memory with hugepages"
---

<p>libhugetlbfs &#8211; preload library to back text, data, malloc() or shared memory with hugepages</p>
<h2>Synopsis</h2>
<p><code>export [environment options]</code><br />
 <code>[LD_PRELOAD=libhugetlbfs.so] target_application</code></p>
<h2>Description</h2>
<p><code>libhugetlbfs</code> is a library that can back application text, data, malloc() and shared memory with hugepages. This is of benefit to applications that use large amounts of address space and suffer a performance hit due to TLB misses. Wall-clock time or oprofile can be used to determine if there is a performance benefit from using <code>libhugetlbfs</code> or not. In all cases but shared memory, a hugetlbfs mount must exist and a hugepage pool defined for hugepages to be used. Some limited functionality is available for unmodified dynamically linked applications. By preloading the library, the library can back malloc() and shared memory, and text and data segments can be partially backed if they are large enough. For the effective backing of text and data with huge pages, the application must be linked to the library and the ELF segments correctly aligned using the ld helpers. Once linked, malloc or shared memory can still be backed but no pre-loading is required. See /usr/share/doc/libhugetlbfs/HOWTO and <a href="/docs/linux/man/1-ld-hugetlbfs/">ld.hugetlbfs</a>(1) for detailed instructions on relinking applications. For applications that are hugepage-aware and linked to the library <code>get_huge_pages()</code> can be used for the direct allocation of hugepage-backed regions. Unless otherwise specified, <code>libhugetlbfs</code> will use the default hugepage size to back memory regions. The default size is the value of Hugepagesize displayed in /proc/meminfo. The size can be specified in bytes or in kilobytes, megabytes, or gigabytes by appending K, M, or G respectively. It is an error to specify a invalid, unsupported, or otherwise unconfigured huge page size. Kernel 2.6.27 or later is required to specify any pagesize other than the default. See /usr/share/docs/libhugetlbfs/HOWTO for detailed instructions on how the library should be used, particularly when relinking the application. This manual page provides a brief synopsis of the environment variables as a quick reference. The following variables affect what memory regions are backed by hugepages. In all cases, the environment being unset implies the feature should remain disabled.</p>
<dl>
<dt><code>HUGETLB_DEFAULT_PAGE_SIZE=&lt;pagesize&gt;</code></p>
<dd>This sets the default hugepage size to be used by libhugetlbfs. If not set, libhugetlbfs will use the kernel&#8217;s default hugepage size.</p>
<dt><code>HUGETLB_MORECORE=[yes|&lt;pagesize&gt;]</code></p>
<dd>This enables the hugepage malloc() feature, instructing libhugetlbfs to override glibc&#8217;s normal morecore() function with a hugepage version and use it for malloc(). All application malloc() memory should come from hugepage memory until it runs out, it will then fallback to base pages. Note that applications that use custom allocators may not be able to back their heaps using hugepages and this environment variable. It may be necessary to modify the custom allocator to use <code>get_huge_pages()</code>.</p>
<dt><code>HUGETLB_SHM=yes</code></p>
<dd>When this environment variable is set, the SHM_HUGETLB flag is added to the shmget() call and the size parameter is aligned to back the shared memory segment with hugepages. In the event hugepages cannot be used, base pages will be used instead and a warning will be printed to explain the failure. The pagesize cannot be specified with this parameter. To change the kernels default hugepage size, use the pagesize= kernel boot parameter (2.6.26 or later required).</p>
<dt><code>HUGETLB_ELFMAP=[no|[R[&lt;=pagesize&gt;]:[W[&lt;=pagesize&gt;]]]</code></p>
<dd>If the application has been relinked (see the HOWTO for instructions), this environment variable determines whether read-only, read-write, both or no segments are backed by hugepages and what pagesize should be used. If the recommended relinking method has been used, then <code>hugeedit</code> can be used to automatically back the text or data by default.</p>
<dt><code>HUGETLB_FORCE_ELFMAP=yes</code></p>
<dd>Force the use of hugepages for text and data segments even if the application has not been relinked to align the ELF segments on a hugepage boundary. Partial segment remapping is not guaranteed to work and the segments must be large enough to contain at least one hugepage for the remapping to occur.  The following options affect how libhugetlbfs behaves.</p>
<dl>
<dt><code>HUGETLB_RESTRICT_EXE=e1:e2:&#8230;:eN</code></p>
<dd>By default, libhugetlbfs will act on any program that it is loaded with, either via LD_PRELOAD or by explicitly linking with -lhugetlbfs. There are situations in which it is desirable to restrict libhugetlbfs&#8217; actions to specific programs. For example, some ISV applications are wrapped in a series of scripts that invoke bash, python, and/or perl.<tt>&nbsp;<wbr>&nbsp;<wbr></tt>It is more<br />
 convenient to set the environment variables related to libhugetlbfs before invoking the wrapper scripts, yet this has the unintended and undesirable consequence of causing the script interpreters to use and consume hugepages. There is no obvious benefit to causing the script interpreters to use hugepages, and there is a clear disadvantage: fewer hugepages are available to the actual application. To address this scenario, set HUGETLB_RESTRICT_EXE to a colon-separated list of programs to which the other libhugetlbfs environment variables should apply. (If not set, libhugetlbfs will attempt to apply the requested actions to all programs.) For example, </p>
<pre><code>HUGETLB_RESTRICT_EXE=hpcc:long_hpcc</code></pre>
<p> will restrict libhugetlbfs&#8217; actions to programs named /home/fred/hpcc and /bench/long_hpcc but not /bin/hpcc_no.</p>
<dt><code>HUGETLB_MORECORE_SHRINK=yes</code></p>
<dd>By default, the hugepage heap does not shrink. Shrinking is enabled by setting this environment variable. It is disabled by default as glibc occasionally exhibits strange behaviour if it mistakes the heap returned by <code>libhugetlbfs</code> as a foreign brk().</p>
<dt><code>HUGETLB_NO_PREFAULT</code></p>
<dd>By default <code>libhugetlbfs</code> will prefault regions it creates to ensure they can be referenced without receiving a SIGKILL. On kernels older than 2.6.27, this was necessary as the system did not guarantee that future faults would succeed on regions mapped MAP_PRIVATE. Prefaulting impacts the performance of malloc() and can result in poor placement on NUMA systems. If it is known the hugepage pool is large enough to run the application or the kernel is 2.6.27 or later, this environment variable should be set.</p>
<dt><code>HUGETLB_NO_RESERVE=yes</code></p>
<dd>By default, the kernel will reserve huge pages at mmap() time to ensure that future faults will succeed. This avoids unexpected application failure at fault time but some applications depend on memory overcommit to create large sparse mappings. For this type of application, setting this environment variable will create huge page backed mappings without a reservation. Use this option with extreme care as in the event huge pages are not available when the mapping is used, the application will be killed. On older kernels, the use of this feature can trigger the OOM killer. Hence, even with this variable set, reservations may still be used for safety.</p>
<dt><code>HUGETLB_MORECORE_HEAPBASE=address</code></p>
<dd><code>libhugetlbfs</code> normally picks an address to use as the base of the heap for malloc() automatically. This environment variable fixes which address is used.</p>
<dt><code>HUGETLB_PATH=&lt;path&gt;</code></p>
<dd>The path to the hugetlbfs mount is automatically determined at run-time. In the event there are multiple mounts and the wrong one is being selected, use this option to select the correct one. This may be the case if an application-specific mount with a fixed quota has been created for example.</p>
<dt><code>HUGETLB_SHARE=1</code></p>
<dd>By default, <code>libhugetlbfs</code> uses unlinked hugetlbfs files to store remapped program segment data. If the same program is started multiple times using hugepage segments, multiple hugepages will be used to store the same program data. The reduce this wastage, setting this environment variable will share read-only segments between multiple invocations of a program at the cost of the memory being used whether the applications are running or not. It is also possible that a malicious application inferfere with other applications executable code. See the HOWTO for more detailed information on this topic.  The following options control the verbosity of <code>libhugetlbfs</code>.</p>
<dl>
<dt><code>HUGETLB_VERBOSE=&lt;level&gt;</code></p>
<dd>The default value for this is 1 and the range of the value is from 0 to 99. The higher the value, the more verbose the output is. 0 is quiet and 3 will output much debugging information.</p>
<dt><code>HUGETLB_DEBUG</code></p>
<dd>Once set, this will give very detailed output on what is happening in the library and run extra diagnostics. </p>
<h2>Files</h2>
<p>[DESTDIR|/usr/share]/doc/libhugetlbfs/HOWTO</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1),</i> <i><a href="/docs/linux/man/1-ld-hugetlbfs/">ld.hugetlbfs</a>(1),</i> <i><a href="/docs/linux/man/8-hugectl/">hugectl</a>(8),</i> <i><a href="/docs/linux/man/8-hugeedit/">hugeedit</a>(8),</i> <i><a href="/docs/linux/man/3-gethugepagesize/">gethugepagesize</a>(3),</i> <i><a href="/docs/linux/man/3-gethugepagesizes/">gethugepagesizes</a>(3),</i> <i><a href="/docs/linux/man/3-getpagesizes/">getpagesizes</a>(3),</i> <i><a href="/docs/linux/man/3-hugetlbfs_test_path/">hugetlbfs_test_path</a>(3),</i> <i><a href="/docs/linux/man/3-hugetlbfs_find_path/">hugetlbfs_find_path</a>(3),</i> <i><a href="/docs/linux/man/3-hugetlbfs_find_path_for_size/">hugetlbfs_find_path_for_size</a>(3),</i> <i><a href="/docs/linux/man/3-hugetlbfs_test_path/">hugetlbfs_test_path</a>(3),</i> <i><a href="/docs/linux/man/3-hugetlbfs_test_path_for_size/">hugetlbfs_test_path_for_size</a>(3),</i> <i><a href="/docs/linux/man/3-hugetlbfs_unlinked_fd/">hugetlbfs_unlinked_fd</a>(3),</i> <i><a href="/docs/linux/man/3-hugetlbfs_unlinked_fd_for_size/">hugetlbfs_unlinked_fd_for_size</a>(3),</i> <i><a href="/docs/linux/man/3-get_huge_pages/">get_huge_pages</a>(3),</i> <i><a href="/docs/linux/man/3-free_huge_pages/">free_huge_pages</a>(3)</i></p>
<h2>Authors</h2>
<p>libhugetlbfs was written by various people on the libhugetlbfs-devel mailing list.</p>
