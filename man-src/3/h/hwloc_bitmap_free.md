---
title: "hwloc_bitmap_free(3)"
name: "hwloc_bitmap_free"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_bitmap_free/"
description: "hwlocality_bitmap – The bitmap API"
---

<h2 class="name">NAME</h2>
<p> hwlocality_bitmap &#8211; The bitmap API </p>
<h3>Macros</h3>
<p> #define <code>hwloc_bitmap_foreach_begin</code>(id, bitmap) </p>
<p> #define <code>hwloc_bitmap_foreach_end</code>() </p>
<h3>Typedefs</h3>
<p> typedef struct hwloc_bitmap_s * <code>hwloc_bitmap_t</code> </p>
<p> typedef const struct hwloc_bitmap_s * <code>hwloc_const_bitmap_t</code> </p>
<h3>Functions</h3>
<p> <code>hwloc_bitmap_t</code> <code>hwloc_bitmap_alloc</code> (void) </p>
<p> <code>hwloc_bitmap_t</code> <code>hwloc_bitmap_alloc_full</code> (void) </p>
<p> void <code>hwloc_bitmap_free</code> (<code>hwloc_bitmap_t</code> bitmap) </p>
<p> <code>hwloc_bitmap_t</code> <code>hwloc_bitmap_dup</code> (<code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> void <code>hwloc_bitmap_copy</code> (<code>hwloc_bitmap_t</code> dst, <code>hwloc_const_bitmap_t</code> src) </p>
<p> int <code>hwloc_bitmap_snprintf</code> (char *restrict buf, size_t buflen, <code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_asprintf</code> (char **strp, <code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_sscanf</code> (<code>hwloc_bitmap_t</code> bitmap, const char *restrict string) </p>
<p> int <code>hwloc_bitmap_list_snprintf</code> (char *restrict buf, size_t buflen, <code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_list_asprintf</code> (char **strp, <code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_list_sscanf</code> (<code>hwloc_bitmap_t</code> bitmap, const char *restrict string) </p>
<p> int <code>hwloc_bitmap_taskset_snprintf</code> (char *restrict buf, size_t buflen, <code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_taskset_asprintf</code> (char **strp, <code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_taskset_sscanf</code> (<code>hwloc_bitmap_t</code> bitmap, const char *restrict string) </p>
<p> void <code>hwloc_bitmap_zero</code> (<code>hwloc_bitmap_t</code> bitmap) </p>
<p> void <code>hwloc_bitmap_fill</code> (<code>hwloc_bitmap_t</code> bitmap) </p>
<p> void <code>hwloc_bitmap_only</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned id) </p>
<p> void <code>hwloc_bitmap_allbut</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned id) </p>
<p> void <code>hwloc_bitmap_from_ulong</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned long mask) </p>
<p> void <code>hwloc_bitmap_from_ith_ulong</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned i, unsigned long mask) </p>
<p> void <code>hwloc_bitmap_set</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned id) </p>
<p> void <code>hwloc_bitmap_set_range</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned begin, int end) </p>
<p> void <code>hwloc_bitmap_set_ith_ulong</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned i, unsigned long mask) </p>
<p> void <code>hwloc_bitmap_clr</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned id) </p>
<p> void <code>hwloc_bitmap_clr_range</code> (<code>hwloc_bitmap_t</code> bitmap, unsigned begin, int end) </p>
<p> void <code>hwloc_bitmap_singlify</code> (<code>hwloc_bitmap_t</code> bitmap) </p>
<p> unsigned long <code>hwloc_bitmap_to_ulong</code> (<code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> unsigned long <code>hwloc_bitmap_to_ith_ulong</code> (<code>hwloc_const_bitmap_t</code> bitmap, unsigned i) </p>
<p> int <code>hwloc_bitmap_isset</code> (<code>hwloc_const_bitmap_t</code> bitmap, unsigned id) </p>
<p> int <code>hwloc_bitmap_iszero</code> (<code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_isfull</code> (<code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_first</code> (<code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_next</code> (<code>hwloc_const_bitmap_t</code> bitmap, int prev) </p>
<p> int <code>hwloc_bitmap_last</code> (<code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_weight</code> (<code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> void <code>hwloc_bitmap_or</code> (<code>hwloc_bitmap_t</code> res, <code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<p> void <code>hwloc_bitmap_and</code> (<code>hwloc_bitmap_t</code> res, <code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<p> void <code>hwloc_bitmap_andnot</code> (<code>hwloc_bitmap_t</code> res, <code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<p> void <code>hwloc_bitmap_xor</code> (<code>hwloc_bitmap_t</code> res, <code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<p> void <code>hwloc_bitmap_not</code> (<code>hwloc_bitmap_t</code> res, <code>hwloc_const_bitmap_t</code> bitmap) </p>
<p> int <code>hwloc_bitmap_intersects</code> (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<p> int <code>hwloc_bitmap_isincluded</code> (<code>hwloc_const_bitmap_t</code> sub_bitmap, <code>hwloc_const_bitmap_t</code> super_bitmap) </p>
<p> int <code>hwloc_bitmap_isequal</code> (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<p> int <code>hwloc_bitmap_compare_first</code> (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<p> int <code>hwloc_bitmap_compare</code> (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2) </p>
<h2>Detailed Description</h2>
<p> The <code>hwloc_bitmap_t</code> type represents a set of objects, typically OS processors &#8212; which may actually be hardware threads (represented by <code>hwloc_cpuset_t</code>, which is a typedef for <code>hwloc_bitmap_t</code>) &#8212; or memory nodes (represented by <code>hwloc_nodeset_t</code>, which is also a typedef for <code>hwloc_bitmap_t</code>). </p>
<p> <i>Both CPU and node sets are always indexed by OS physical number.</i> </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> CPU sets and nodesets are described in <code>Object Sets (hwloc_cpuset_t and hwloc_nodeset_t)</code>.</dl>
<p> A bitmap may be of infinite size. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Several examples of using the bitmap API are available under the doc/examples/ directory in the source tree. Regression tests such as tests/hwloc/hwloc_bitmap*.c also make intensive use of this API.</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define hwloc_bitmap_foreach_begin(id, bitmap)</h3>
<p> Loop macro iterating on bitmap bitmap. The loop must start with <code>hwloc_bitmap_foreach_begin()</code> and end with <code>hwloc_bitmap_foreach_end()</code> followed by a terminating &#8216;;&#8217;. </p>
<p> index is the loop variable; it should be an unsigned int. The first iteration will set index to the lowest index in the bitmap. Successive iterations will iterate through, in order, all remaining indexes set in the bitmap. To be specific: each iteration will return a value for index such that hwloc_bitmap_isset(bitmap, index) is true. </p>
<p> The assert prevents the loop from being infinite if the bitmap is infinite.</p>
<h3>#define hwloc_bitmap_foreach_end()</h3>
<p> End of loop macro iterating on a bitmap. Needs a terminating &#8216;;&#8217;. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>hwloc_bitmap_foreach_begin()</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct hwloc_bitmap_s* <code>hwloc_bitmap_t</code></h3>
<p> Set of bits represented as an opaque pointer to an internal bitmap.</p>
<h3>typedef const struct hwloc_bitmap_s* <code>hwloc_const_bitmap_t</code></h3>
<p> a non-modifiable <code>hwloc_bitmap_t</code></p>
<h2>Function Documentation</h2>
<h3>void hwloc_bitmap_allbut (<code>hwloc_bitmap_t</code> bitmap, unsigned id)</h3>
<p> Fill the bitmap and clear the index id.</p>
<h3><code>hwloc_bitmap_t</code> hwloc_bitmap_alloc (void)</h3>
<p> Allocate a new empty bitmap. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A valid bitmap or NULL.</dl>
<p> The bitmap should be freed by a corresponding call to <code>hwloc_bitmap_free()</code>.</p>
<h3><code>hwloc_bitmap_t</code> hwloc_bitmap_alloc_full (void)</h3>
<p> Allocate a new full bitmap.</p>
<h3>void hwloc_bitmap_and (<code>hwloc_bitmap_t</code> res, <code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2)</h3>
<p> And bitmaps bitmap1 and bitmap2 and store the result in bitmap res. res can be the same as bitmap1 or bitmap2</p>
<h3>void hwloc_bitmap_andnot (<code>hwloc_bitmap_t</code> res, <code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2)</h3>
<p> And bitmap bitmap1 and the negation of bitmap2 and store the result in bitmap res. res can be the same as bitmap1 or bitmap2</p>
<h3>int hwloc_bitmap_asprintf (char ** strp, <code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Stringify a bitmap into a newly allocated string.</p>
<h3>void hwloc_bitmap_clr (<code>hwloc_bitmap_t</code> bitmap, unsigned id)</h3>
<p> Remove index id from bitmap bitmap.</p>
<h3>void hwloc_bitmap_clr_range (<code>hwloc_bitmap_t</code> bitmap, unsigned begin, int end)</h3>
<p> Remove indexes from begin to end in bitmap bitmap. If end is -1, the range is infinite.</p>
<h3>int hwloc_bitmap_compare (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2)</h3>
<p> Compare bitmaps bitmap1 and bitmap2 in lexicographic order. Lexicographic comparison of bitmaps, starting for their highest indexes. Compare last indexes first, then second, etc. The empty bitmap is considered lower than anything. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is different from the non-existing hwloc_bitmap_compare_last() which would only compare the highest index of each bitmap.</dl>
<h3>int hwloc_bitmap_compare_first (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2)</h3>
<p> Compare bitmaps bitmap1 and bitmap2 using their lowest index. Smaller least significant bit is smaller. The empty bitmap is considered higher than anything.</p>
<h3>void hwloc_bitmap_copy (<code>hwloc_bitmap_t</code> dst, <code>hwloc_const_bitmap_t</code> src)</h3>
<p> Copy the contents of bitmap src into the already allocated bitmap dst.</p>
<h3><code>hwloc_bitmap_t</code> hwloc_bitmap_dup (<code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Duplicate bitmap bitmap by allocating a new bitmap and copying bitmap contents. If bitmap is NULL, NULL is returned.</p>
<h3>void hwloc_bitmap_fill (<code>hwloc_bitmap_t</code> bitmap)</h3>
<p> Fill bitmap bitmap with all possible indexes (even if those objects don&#8217;t exist or are otherwise unavailable)</p>
<h3>int hwloc_bitmap_first (<code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Compute the first index (least significant bit) in bitmap bitmap. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 if no index is set.</dl>
<h3>void hwloc_bitmap_free (<code>hwloc_bitmap_t</code> bitmap)</h3>
<p> Free bitmap bitmap. If bitmap is NULL, no operation is performed.</p>
<h3>void hwloc_bitmap_from_ith_ulong (<code>hwloc_bitmap_t</code> bitmap, unsigned i, unsigned long mask)</h3>
<p> Setup bitmap bitmap from unsigned long mask used as i -th subset.</p>
<h3>void hwloc_bitmap_from_ulong (<code>hwloc_bitmap_t</code> bitmap, unsigned long mask)</h3>
<p> Setup bitmap bitmap from unsigned long mask.</p>
<h3>int hwloc_bitmap_intersects (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2)</h3>
<p> Test whether bitmaps bitmap1 and bitmap2 intersects.</p>
<h3>int hwloc_bitmap_isequal (<code>hwloc_const_bitmap_t</code> bitmap1, <code>hwloc_const_bitmap_t</code> bitmap2)</h3>
<p> Test whether bitmap bitmap1 is equal to bitmap bitmap2.</p>
<h3>int hwloc_bitmap_isfull (<code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Test whether bitmap bitmap is completely full.</p>
<h3>int hwloc_bitmap_isincluded (<code>hwloc_const_bitmap_t</code> sub_bitmap, <code>hwloc_const_bitmap_t</code> super_bitmap)</h3>
<p> Test whether bitmap sub_bitmap is part of bitmap super_bitmap.</p>
<h3>int hwloc_bitmap_isset (<code>hwloc_const_bitmap_t</code> bitmap, unsigned id)</h3>
<p> Test whether index id is part of bitmap bitmap.</p>
<h3>int hwloc_bitmap_iszero (<code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Test whether bitmap bitmap is empty.</p>
<h3>int hwloc_bitmap_last (<code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Compute the last index (most significant bit) in bitmap bitmap. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 if no index is bitmap, or if the index bitmap is infinite.</dl>
<h3>int hwloc_bitmap_list_asprintf (char ** strp, <code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Stringify a bitmap into a newly allocated list string.</p>
<h3>int hwloc_bitmap_list_snprintf (char *restrict buf, size_t buflen, <code>hwloc_const_bitmap_t</code> bitmap)</h3>
<p> Stringify a bitmap in the list format. Lists are comma-separated indexes or ranges. Ranges are dash separated indexes. The last range may not have a ending indexes if the bitmap is infinite. </p>
<p> Up to buflen characters may be written in buffer buf. </p>
<p> If buflen is 0, buf may safely be NULL. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of character that were actually written if not truncating, or that would have been written (not including the ending 
