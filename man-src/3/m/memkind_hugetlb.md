---
title: "memkind_hugetlb(3)"
name: "memkind_hugetlb"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memkind_hugetlb/"
description: "memkind_hugetlb.h – hugetlb memory memkind operations. Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or re..."
---

<h2>NAME</h2>
<p> memkind_hugetlb.h &#8211; hugetlb memory memkind operations.<br />
 Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;memkind/internal/memkind_hugetlb.h&gt;
Link with - lmemkind int memkind_hugetlb_check_available_2mb(struct memkind *kind);

int memkind_hugetlb_check_available_1gb(struct memkind *kind);

int memkind_hugetlb_get_mmap_flags(struct memkind *kind, int *flags);

void memkind_hugetlb_init_once(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The hugetlb memory memkind operations enable memory kinds which use the Linux hugetlbfs file system. For more information about the hugetlbfs see link below.<br />
 <i><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/vm/hugetlbpage.txt">https://www.kernel.org/doc/Documentation/vm/hugetlbpage.txt</a></i> </p>
<p> <code>memkind_hugetlb_check_available_2mb</code>() Check if there are 2MB pages reserved in the default hugetlbfs. If the kind implements ops.get_mbind_nodemask(), then only the NUMA nodes set by the nodemask are checked, otherwise every NUMA node is checked. </p>
<p> <code>memkind_hugetlb_check_available_1gb</code>() Similar to memkind_hugetlb_check_available_2mb() except that the check is for 1GB pages instead of 2MB pages. </p>
<p> <code>memkind_hugetlb_get_mmap_flags</code>() Sets the flags for the <code>mmap</code>() system call such that the hugetlbfs is utilized for allocations. </p>
<p> <code>memkind_hugetlb_init_once</code>() This function initializes MEMKIND_HUGETLB kind and it should not be called more than once. <code>Note:</code> <code>memkind_hugetlb_init_once</code>() may reserve some extra memory.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2014 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3), <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3), <code><a href="/docs/linux/man/3-memkind_default/">memkind_default</a></code>(3), <code><a href="/docs/linux/man/3-memkind_gbtlb/">memkind_gbtlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hbw/">memkind_hbw</a></code>(3), <code><a href="/docs/linux/man/3-memkind_pmem/">memkind_pmem</a></code>(3), <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<h2>Index</h2>
