---
title: "page_cache_next_hole(9)"
name: "page_cache_next_hole"
section: "9"
letter: "p"
url: "/docs/linux/man/9-page_cache_next_hole/"
description: "page_cache_next_hole – find the next hole (not-present entry)"
---

<p>page_cache_next_hole &#8211; find the next hole (not-present entry)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pgoff_t page_cache_next_hole(struct address_space&nbsp;<wbr>*&nbsp;<wbr></code><i>mapping</i><code>, pgoff_t&nbsp;<wbr></code><i>index</i><code>, unsigned long&nbsp;<wbr></code><i>max_scan</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>mapping</dl>
<p> <i>index</i></p>
<dl>
<dd>index</dl>
<p> <i>max_scan</i></p>
<dl>
<dd>maximum range to search</dl>
<h2>Description</h2>
<p>Search the set [index, min(index+max_scan-1, MAX_INDEX)] for the lowest indexed hole.</p>
<h2>Return</h2>
<p>the index of the hole if found, otherwise returns an index outside of the set specified (in which case &#8216;return &#8211; index &gt;= max_scan&#8217; will be true). In rare cases of index wrap-around, 0 will be returned. </p>
<p> page_cache_next_hole may be called under rcu_read_lock. However, like radix_tree_gang_lookup, this will not atomically search a snapshot of the tree at a single point in time. For example, if a hole is created at index 5, then subsequently a hole is created at index 10, page_cache_next_hole covering both indexes may return 10 if called under rcu_read_lock.</p>
<h2>Copyright</h2>
