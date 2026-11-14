---
title: "hwloc_bitmap_dup(3)"
name: "hwloc_bitmap_dup"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_bitmap_dup/"
---

<h2 class="name">NAME</h2>
 

 hwlocality_bitmap - The bitmap API 

<h3>Macros</h3>

 

 
 #define <b>hwloc_bitmap_foreach_begin</b>(id, bitmap) 
 
 #define <b>hwloc_bitmap_foreach_end</b>() 

<h3>Typedefs</h3>

 

 
 typedef struct hwloc_bitmap_s * <b>hwloc_bitmap_t</b> 
 
 typedef const struct hwloc_bitmap_s * <b>hwloc_const_bitmap_t</b> 

<h3>Functions</h3>

 

 
 <b>hwloc_bitmap_t</b> <b>hwloc_bitmap_alloc</b> (void) 
 
 <b>hwloc_bitmap_t</b> <b>hwloc_bitmap_alloc_full</b> (void) 
 
 void <b>hwloc_bitmap_free</b> (<b>hwloc_bitmap_t</b> bitmap) 
 
 <b>hwloc_bitmap_t</b> <b>hwloc_bitmap_dup</b> (<b>hwloc_const_bitmap_t</b> bitmap) 
 
 void <b>hwloc_bitmap_copy</b> (<b>hwloc_bitmap_t</b> dst, <b>hwloc_const_bitmap_t</b> src) 
 
 int <b>hwloc_bitmap_snprintf</b> (char *restrict buf, size_t buflen, <b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_asprintf</b> (char **strp, <b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_sscanf</b> (<b>hwloc_bitmap_t</b> bitmap, const char *restrict string) 
 
 int <b>hwloc_bitmap_list_snprintf</b> (char *restrict buf, size_t buflen, <b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_list_asprintf</b> (char **strp, <b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_list_sscanf</b> (<b>hwloc_bitmap_t</b> bitmap, const char *restrict string) 
 
 int <b>hwloc_bitmap_taskset_snprintf</b> (char *restrict buf, size_t buflen, <b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_taskset_asprintf</b> (char **strp, <b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_taskset_sscanf</b> (<b>hwloc_bitmap_t</b> bitmap, const char *restrict string) 
 
 void <b>hwloc_bitmap_zero</b> (<b>hwloc_bitmap_t</b> bitmap) 
 
 void <b>hwloc_bitmap_fill</b> (<b>hwloc_bitmap_t</b> bitmap) 
 
 void <b>hwloc_bitmap_only</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned id) 
 
 void <b>hwloc_bitmap_allbut</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned id) 
 
 void <b>hwloc_bitmap_from_ulong</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned long mask) 
 
 void <b>hwloc_bitmap_from_ith_ulong</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned i, unsigned long mask) 
 
 void <b>hwloc_bitmap_set</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned id) 
 
 void <b>hwloc_bitmap_set_range</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned begin, int end) 
 
 void <b>hwloc_bitmap_set_ith_ulong</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned i, unsigned long mask) 
 
 void <b>hwloc_bitmap_clr</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned id) 
 
 void <b>hwloc_bitmap_clr_range</b> (<b>hwloc_bitmap_t</b> bitmap, unsigned begin, int end) 
 
 void <b>hwloc_bitmap_singlify</b> (<b>hwloc_bitmap_t</b> bitmap) 
 
 unsigned long <b>hwloc_bitmap_to_ulong</b> (<b>hwloc_const_bitmap_t</b> bitmap) 
 
 unsigned long <b>hwloc_bitmap_to_ith_ulong</b> (<b>hwloc_const_bitmap_t</b> bitmap, unsigned i) 
 
 int <b>hwloc_bitmap_isset</b> (<b>hwloc_const_bitmap_t</b> bitmap, unsigned id) 
 
 int <b>hwloc_bitmap_iszero</b> (<b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_isfull</b> (<b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_first</b> (<b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_next</b> (<b>hwloc_const_bitmap_t</b> bitmap, int prev) 
 
 int <b>hwloc_bitmap_last</b> (<b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_weight</b> (<b>hwloc_const_bitmap_t</b> bitmap) 
 
 void <b>hwloc_bitmap_or</b> (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 
 
 void <b>hwloc_bitmap_and</b> (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 
 
 void <b>hwloc_bitmap_andnot</b> (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 
 
 void <b>hwloc_bitmap_xor</b> (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 
 
 void <b>hwloc_bitmap_not</b> (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap) 
 
 int <b>hwloc_bitmap_intersects</b> (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 
 
 int <b>hwloc_bitmap_isincluded</b> (<b>hwloc_const_bitmap_t</b> sub_bitmap, <b>hwloc_const_bitmap_t</b> super_bitmap) 
 
 int <b>hwloc_bitmap_isequal</b> (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 
 
 int <b>hwloc_bitmap_compare_first</b> (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 
 
 int <b>hwloc_bitmap_compare</b> (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2) 

<h2>Detailed Description</h2>

 

 The <b>hwloc_bitmap_t</b> type represents a set of objects, typically OS processors -- which may actually be hardware threads (represented by <b>hwloc_cpuset_t</b>, which is a typedef for <b>hwloc_bitmap_t</b>) -- or memory nodes (represented by <b>hwloc_nodeset_t</b>, which is also a typedef for <b>hwloc_bitmap_t</b>). 

 <i>Both CPU and node sets are always indexed by OS physical number.</i> 

 <b>Note:</b>
<dl>
<dt>
<dd> CPU sets and nodesets are described in <b>Object Sets (hwloc_cpuset_t and hwloc_nodeset_t)</b>.</dl>
 

 A bitmap may be of infinite size. 

 <b>Note:</b>
<dl>
<dt>
<dd> Several examples of using the bitmap API are available under the doc/examples/ directory in the source tree. Regression tests such as tests/hwloc/hwloc_bitmap*.c also make intensive use of this API.</dl>
 

 

<h2>Macro Definition Documentation</h2>

 

<h3>#define hwloc_bitmap_foreach_begin(id, bitmap)</h3>

 

 

 Loop macro iterating on bitmap bitmap. The loop must start with <b>hwloc_bitmap_foreach_begin()</b> and end with <b>hwloc_bitmap_foreach_end()</b> followed by a terminating ';'. 

 index is the loop variable; it should be an unsigned int. The first iteration will set index to the lowest index in the bitmap. Successive iterations will iterate through, in order, all remaining indexes set in the bitmap. To be specific: each iteration will return a value for index such that hwloc_bitmap_isset(bitmap, index) is true. 

 The assert prevents the loop from being infinite if the bitmap is infinite.

<h3>#define hwloc_bitmap_foreach_end()</h3>

 

 

 End of loop macro iterating on a bitmap. Needs a terminating ';'. 

 <b>See also:</b>
<dl>
<dt>
<dd> <b>hwloc_bitmap_foreach_begin()</b></dl>
 

 

<h2>Typedef Documentation</h2>

 

<h3>typedef struct hwloc_bitmap_s* <b>hwloc_bitmap_t</b></h3>

 

 

 Set of bits represented as an opaque pointer to an internal bitmap.

<h3>typedef const struct hwloc_bitmap_s* <b>hwloc_const_bitmap_t</b></h3>

 

 

 a non-modifiable <b>hwloc_bitmap_t</b>

<h2>Function Documentation</h2>

 

<h3>void hwloc_bitmap_allbut (<b>hwloc_bitmap_t</b> bitmap, unsigned id)</h3>

 

 

 Fill the bitmap and clear the index id.

<h3><b>hwloc_bitmap_t</b> hwloc_bitmap_alloc (void)</h3>

 

 

 Allocate a new empty bitmap. 

 <b>Returns:</b>
<dl>
<dt>
<dd> A valid bitmap or NULL.</dl>
 

 The bitmap should be freed by a corresponding call to <b>hwloc_bitmap_free()</b>.

<h3><b>hwloc_bitmap_t</b> hwloc_bitmap_alloc_full (void)</h3>

 

 

 Allocate a new full bitmap.

<h3>void hwloc_bitmap_and (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 And bitmaps bitmap1 and bitmap2 and store the result in bitmap res. res can be the same as bitmap1 or bitmap2

<h3>void hwloc_bitmap_andnot (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 And bitmap bitmap1 and the negation of bitmap2 and store the result in bitmap res. res can be the same as bitmap1 or bitmap2

<h3>int hwloc_bitmap_asprintf (char ** strp, <b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Stringify a bitmap into a newly allocated string.

<h3>void hwloc_bitmap_clr (<b>hwloc_bitmap_t</b> bitmap, unsigned id)</h3>

 

 

 Remove index id from bitmap bitmap.

<h3>void hwloc_bitmap_clr_range (<b>hwloc_bitmap_t</b> bitmap, unsigned begin, int end)</h3>

 

 

 Remove indexes from begin to end in bitmap bitmap. If end is -1, the range is infinite.

<h3>int hwloc_bitmap_compare (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 Compare bitmaps bitmap1 and bitmap2 in lexicographic order. Lexicographic comparison of bitmaps, starting for their highest indexes. Compare last indexes first, then second, etc. The empty bitmap is considered lower than anything. 

 <b>Note:</b>
<dl>
<dt>
<dd> This is different from the non-existing hwloc_bitmap_compare_last() which would only compare the highest index of each bitmap.</dl>
 

 

<h3>int hwloc_bitmap_compare_first (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 Compare bitmaps bitmap1 and bitmap2 using their lowest index. Smaller least significant bit is smaller. The empty bitmap is considered higher than anything.

<h3>void hwloc_bitmap_copy (<b>hwloc_bitmap_t</b> dst, <b>hwloc_const_bitmap_t</b> src)</h3>

 

 

 Copy the contents of bitmap src into the already allocated bitmap dst.

<h3><b>hwloc_bitmap_t</b> hwloc_bitmap_dup (<b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Duplicate bitmap bitmap by allocating a new bitmap and copying bitmap contents. If bitmap is NULL, NULL is returned.

<h3>void hwloc_bitmap_fill (<b>hwloc_bitmap_t</b> bitmap)</h3>

 

 

 Fill bitmap bitmap with all possible indexes (even if those objects don't exist or are otherwise unavailable)

<h3>int hwloc_bitmap_first (<b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Compute the first index (least significant bit) in bitmap bitmap. 

 <b>Returns:</b>
<dl>
<dt>
<dd> -1 if no index is set.</dl>
 

 

<h3>void hwloc_bitmap_free (<b>hwloc_bitmap_t</b> bitmap)</h3>

 

 

 Free bitmap bitmap. If bitmap is NULL, no operation is performed.

<h3>void hwloc_bitmap_from_ith_ulong (<b>hwloc_bitmap_t</b> bitmap, unsigned i, unsigned long mask)</h3>

 

 

 Setup bitmap bitmap from unsigned long mask used as i -th subset.

<h3>void hwloc_bitmap_from_ulong (<b>hwloc_bitmap_t</b> bitmap, unsigned long mask)</h3>

 

 

 Setup bitmap bitmap from unsigned long mask.

<h3>int hwloc_bitmap_intersects (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 Test whether bitmaps bitmap1 and bitmap2 intersects.

<h3>int hwloc_bitmap_isequal (<b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 Test whether bitmap bitmap1 is equal to bitmap bitmap2.

<h3>int hwloc_bitmap_isfull (<b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Test whether bitmap bitmap is completely full.

<h3>int hwloc_bitmap_isincluded (<b>hwloc_const_bitmap_t</b> sub_bitmap, <b>hwloc_const_bitmap_t</b> super_bitmap)</h3>

 

 

 Test whether bitmap sub_bitmap is part of bitmap super_bitmap.

<h3>int hwloc_bitmap_isset (<b>hwloc_const_bitmap_t</b> bitmap, unsigned id)</h3>

 

 

 Test whether index id is part of bitmap bitmap.

<h3>int hwloc_bitmap_iszero (<b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Test whether bitmap bitmap is empty.

<h3>int hwloc_bitmap_last (<b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Compute the last index (most significant bit) in bitmap bitmap. 

 <b>Returns:</b>
<dl>
<dt>
<dd> -1 if no index is bitmap, or if the index bitmap is infinite.</dl>
 

 

<h3>int hwloc_bitmap_list_asprintf (char ** strp, <b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Stringify a bitmap into a newly allocated list string.

<h3>int hwloc_bitmap_list_snprintf (char *restrict buf, size_t buflen, <b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Stringify a bitmap in the list format. Lists are comma-separated indexes or ranges. Ranges are dash separated indexes. The last range may not have a ending indexes if the bitmap is infinite. 

 Up to buflen characters may be written in buffer buf. 

 If buflen is 0, buf may safely be NULL. 

 <b>Returns:</b>
<dl>
<dt>
<dd> the number of character that were actually written if not truncating, or that would have been written (not including the ending \0).</dl>
 

 

<h3>int hwloc_bitmap_list_sscanf (<b>hwloc_bitmap_t</b> bitmap, const char *restrict string)</h3>

 

 

 Parse a list string and stores it in bitmap bitmap.

<h3>int hwloc_bitmap_next (<b>hwloc_const_bitmap_t</b> bitmap, int prev)</h3>

 

 

 Compute the next index in bitmap bitmap which is after index prev. If prev is -1, the first index is returned. 

 <b>Returns:</b>
<dl>
<dt>
<dd> -1 if no index with higher index is bitmap.</dl>
 

 

<h3>void hwloc_bitmap_not (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Negate bitmap bitmap and store the result in bitmap res. res can be the same as bitmap

<h3>void hwloc_bitmap_only (<b>hwloc_bitmap_t</b> bitmap, unsigned id)</h3>

 

 

 Empty the bitmap bitmap and add bit id.

<h3>void hwloc_bitmap_or (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 Or bitmaps bitmap1 and bitmap2 and store the result in bitmap res. res can be the same as bitmap1 or bitmap2

<h3>void hwloc_bitmap_set (<b>hwloc_bitmap_t</b> bitmap, unsigned id)</h3>

 

 

 Add index id in bitmap bitmap.

<h3>void hwloc_bitmap_set_ith_ulong (<b>hwloc_bitmap_t</b> bitmap, unsigned i, unsigned long mask)</h3>

 

 

 Replace i -th subset of bitmap bitmap with unsigned long mask.

<h3>void hwloc_bitmap_set_range (<b>hwloc_bitmap_t</b> bitmap, unsigned begin, int end)</h3>

 

 

 Add indexes from begin to end in bitmap bitmap. If end is -1, the range is infinite.

<h3>void hwloc_bitmap_singlify (<b>hwloc_bitmap_t</b> bitmap)</h3>

 

 

 Keep a single index among those set in bitmap bitmap. May be useful before binding so that the process does not have a chance of migrating between multiple logical CPUs in the original mask.

<h3>int hwloc_bitmap_snprintf (char *restrict buf, size_t buflen, <b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Stringify a bitmap. Up to buflen characters may be written in buffer buf. 

 If buflen is 0, buf may safely be NULL. 

 <b>Returns:</b>
<dl>
<dt>
<dd> the number of character that were actually written if not truncating, or that would have been written (not including the ending \0).</dl>
 

 

<h3>int hwloc_bitmap_sscanf (<b>hwloc_bitmap_t</b> bitmap, const char *restrict string)</h3>

 

 

 Parse a bitmap string and stores it in bitmap bitmap.

<h3>int hwloc_bitmap_taskset_asprintf (char ** strp, <b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Stringify a bitmap into a newly allocated taskset-specific string.

<h3>int hwloc_bitmap_taskset_snprintf (char *restrict buf, size_t buflen, <b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Stringify a bitmap in the taskset-specific format. The taskset command manipulates bitmap strings that contain a single (possible very long) hexadecimal number starting with 0x. 

 Up to buflen characters may be written in buffer buf. 

 If buflen is 0, buf may safely be NULL. 

 <b>Returns:</b>
<dl>
<dt>
<dd> the number of character that were actually written if not truncating, or that would have been written (not including the ending \0).</dl>
 

 

<h3>int hwloc_bitmap_taskset_sscanf (<b>hwloc_bitmap_t</b> bitmap, const char *restrict string)</h3>

 

 

 Parse a taskset-specific bitmap string and stores it in bitmap bitmap.

<h3>unsigned long hwloc_bitmap_to_ith_ulong (<b>hwloc_const_bitmap_t</b> bitmap, unsigned i)</h3>

 

 

 Convert the i -th subset of bitmap bitmap into unsigned long mask.

<h3>unsigned long hwloc_bitmap_to_ulong (<b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Convert the beginning part of bitmap bitmap into unsigned long mask.

<h3>int hwloc_bitmap_weight (<b>hwloc_const_bitmap_t</b> bitmap)</h3>

 

 

 Compute the 'weight' of bitmap bitmap (i.e., number of indexes that are in the bitmap). 

 <b>Returns:</b>
<dl>
<dt>
<dd> the number of indexes that are in the bitmap.</dl>
 

 

<h3>void hwloc_bitmap_xor (<b>hwloc_bitmap_t</b> res, <b>hwloc_const_bitmap_t</b> bitmap1, <b>hwloc_const_bitmap_t</b> bitmap2)</h3>

 

 

 Xor bitmaps bitmap1 and bitmap2 and store the result in bitmap res. res can be the same as bitmap1 or bitmap2

<h3>void hwloc_bitmap_zero (<b>hwloc_bitmap_t</b> bitmap)</h3>

 

 

 Empty the bitmap bitmap.

<h2>Author</h2>

 

 Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. 

<h2>Index</h2>



<dt><a HREF="#lbAM">Function Documentation</a>
<dd>


<dt><a HREF="#lbCG">Author</a>
<dd></dl>
