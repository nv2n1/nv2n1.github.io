---
title: "globus_hashtable_iterators(3)"
name: "globus_hashtable_iterators"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_hashtable_iterators/"
description: "Iterators –"
---

<h2 class="name">NAME</h2>
<p> Iterators &#8211; </p>
<h3>Functions</h3>
<p> void * <code>globus_hashtable_first</code> (globus_hashtable_t *table)<br />
 <i>Initialize iterator to first hash table entry. </i><br />
 void * <code>globus_hashtable_next</code> (globus_hashtable_t *table)<br />
 <i>Increment hash table iterator. </i><br />
 void * <code>globus_hashtable_last</code> (globus_hashtable_t *table)<br />
 <i>Initialize iterator to last hash table entry. </i><br />
 void * <code>globus_hashtable_prev</code> (globus_hashtable_t *table)<br />
 <i>Decrement hash table iterator. </i></p>
<h2>Detailed Description</h2>
<p> The iterator is initially NULL until one of <code>globus_hashtable_first()</code> or <code>globus_hashtable_last()</code> has been called. All other calls have no effect on iterator except for <code>globus_hashtable_remove()</code>. If the iterator points at the entry being removed, the iterator is moved to the next entry. </p>
<p> Once an &#8216;end&#8217; has been reached with <code>globus_hashtable_next()</code> or <code>globus_hashtable_prev()</code>, the iterator must again be reset with <code>globus_hashtable_first()</code> or <code>globus_hashtable_last()</code> before being used.</p>
<h2>Function Documentation</h2>
<h3>void* globus_hashtable_first (globus_hashtable_t *table)</h3>
<p> Initialize iterator to first hash table entry. Set iterator to first entry and return datum, NULL if empty</p>
<h3>void* globus_hashtable_last (globus_hashtable_t *table)</h3>
<p> Initialize iterator to last hash table entry. Set iterator to last entry and return datum, NULL if empty</p>
<h3>void* globus_hashtable_next (globus_hashtable_t *table)</h3>
<p> Increment hash table iterator. Set iterator to next entry and return datum, NULL if at end</p>
<h3>void* globus_hashtable_prev (globus_hashtable_t *table)</h3>
<p> Decrement hash table iterator. Set iterator to the previous entry and return datum, NULL if at end</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
