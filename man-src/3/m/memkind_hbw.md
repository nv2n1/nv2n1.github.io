---
title: "memkind_hbw(3)"
name: "memkind_hbw"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memkind_hbw/"
description: "memkind_hbw.h – high bandwidth memory memkind operations. Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or..."
---

<h2>NAME</h2>
<p> memkind_hbw.h &#8211; high bandwidth memory memkind operations.<br />
 Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;memkind/internal/memkind_hbw.h&gt;
Link with - lmemkind int memkind_hbw_check_available(struct memkind *kind);

int memkind_hbw_hugetlb_check_available(struct memkind *kind);

int memkind_hbw_gbtlb_check_available(struct memkind *kind);

int memkind_hbw_get_mbind_nodemask(struct memkind *kind, unsigned long *nodemask, unsigned long maxnode);

int memkind_hbw_all_get_mbind_nodemask(struct memkind *kind, unsigned long *nodemask, unsigned long maxnode);

void memkind_hbw_init_once(void);

void memkind_hbw_hugetlb_init_once(void);

void memkind_hbw_preferred_init_once(void);

void memkind_hbw_preferred_hugetlb_init_once(void);

void memkind_hbw_interleave_init_once(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> High bandwidth memory memkind operations. </p>
<p> <code>memkind_hbw_check_available</code>() returns zero if library was able to detect heterogeneous NUMA node bandwidths. Returns <code>MEMKIND_UNAVAILABLE</code> if the detection mechanism failed. Detection mechanism can be also overridden by the environment variable <code>MEMKIND_HBW_NODES</code> as described in the <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3) man page. </p>
<p> <code>memkind_hbw_hugetlb_check_available</code>() In addition to checking for high bandwidth memory as is done by memkind_hbw_check_available (), this also checks for 2MB huge pages as is done by memkind_hugetlb_check_available_2mb(). </p>
<p> <code>memkind_hbw_gbtlb_check_available</code>() In addition to checking for high bandwidth memory as is done by memkind_hbw_check_available (), this also checks for 1GB huge pages as is done by memkind_hugetlb_check_available_1gb(). </p>
<p> <code>memkind_hbw_get_mbind_nodemask</code>() sets the <i>nodemask</i> bit to one that corresponds to the high bandwidth NUMA node that has the closest NUMA distance to the CPU of the calling process. All other bits up to <i>maxnode</i> are set to zero. The <i>nodemask</i> can be used in conjuction with the <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) system call. </p>
<p> <code>memkind_hbw_all_get_mbind_nodemask</code>() sets the <i>nodemask</i> bits to one that correspond to the all high bandwidth NUMA nodes in the system. All other bits up to <i>maxnode</i> are set to zero. The <i>nodemask</i> can be used in conjuction with the <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) system call. </p>
<p> <code>memkind_hbw_init_once</code>() This function initializes MEMKIND_HBW kind and it should not be called more than once. Note: <code>memkind_hbw_init_once</code>() may reserve some extra memory. </p>
<p> <code>memkind_hbw_hugetlb_init_once</code>() This function initializes MEMKIND_HBW_HUGETLB kind and it should not be called more than once. Note: <code>memkind_hbw_hugetlb_init_once</code>() may reserve some extra memory. </p>
<p> <code>memkind_hbw_preferred_init_once</code>() This function initializes MEMKIND_HBW_PREFERRED kind and it should not be called more than once. Note: <code>memkind_hbw_preferred_init_once</code>() may reserve some extra memory. </p>
<p> <code>memkind_hbw_preferred_hugetlb_init_once</code>() This function initializes MEMKIND_HBW_PREFERRED_HUGETLB kind and it should not be called more than once. Note: <code>memkind_hbw_preferred_hugetlb_init_once</code>() may reserve some extra memory. </p>
<p> <code>memkind_hbw_interleave_init_once</code>() This function initializes MEMKIND_HBW_INTERLEAVE kind and it should not be called more than once. Note: <code>memkind_hbw_interleave_init_once</code>() may reserve some extra memory.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2014 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3), <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3), <code><a href="/docs/linux/man/3-memkind_default/">memkind_default</a></code>(3), <code><a href="/docs/linux/man/3-memkind_gbtlb/">memkind_gbtlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hugetlb/">memkind_hugetlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_pmem/">memkind_pmem</a></code>(3), <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<h2>Index</h2>
