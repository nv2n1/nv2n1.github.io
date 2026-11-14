---
title: "radixsort(3)"
name: "radixsort"
section: "3"
letter: "r"
url: "/docs/linux/man/3-radixsort/"
description: "radixsort sradixsort – radix sort"
---

<p><code>radixsort</code> <code>sradixsort</code> &#8211; radix sort</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In limits.h In bsd/stdlib.h Ft int Fn radixsort const unsigned char **base int nmemb const unsigned char *table unsigned endbyte Ft int Fn sradixsort const unsigned char **base int nmemb const unsigned char *table unsigned endbyte</p>
<h2>Description</h2>
<p>The Fn radixsort and Fn sradixsort functions are implementations of radix sort. </p>
<p> These functions sort an Fa nmemb element array of pointers to byte strings, with the initial member of which is referenced by Fa base . The byte strings may contain any values. End of strings is denoted by character which has same weight as user specified value Fa endbyte . Fa endbyte has to be between 0 and 255. </p>
<p> Applications may specify a sort order by providing the Fa table argument. If non- <code>NULL</code> Fa table must reference an array of <code>UCHAR_MAX</code> + 1 bytes which contains the sort weight of each possible byte value. The end-of-string byte must have a sort weight of 0 or 255 (for sorting in reverse order). More than one byte may have the same sort weight. The Fa table argument is useful for applications which wish to sort different characters equally, for example, providing a table with the same weights for A-Z as for a-z will result in a case-insensitive sort. If Fa table is NULL, the contents of the array are sorted in ascending order according to the <code>ASCII</code> order of the byte strings they reference and Fa endbyte has a sorting weight of 0. </p>
<p> The Fn sradixsort function is stable, that is, if two elements compare as equal, their order in the sorted array is unchanged. The Fn sradixsort function uses additional memory sufficient to hold Fa nmemb pointers. </p>
<p> The Fn radixsort function is not stable, but uses no additional memory. </p>
<p> These functions are variants of most-significant-byte radix sorting; in particular, see An D.E. Knuth Ns &#8216;s <i>&quot;Algorithm R&quot;</i> and section 5.2.5, exercise 10. They take linear time relative to the number of bytes in the strings.</p>
<h2>Return Values</h2>
<p>Rv -std radixsort</p>
<h2>Errors</h2>
<dt><code>Bq </code>Er EINVAL</p>
<dd>The value of the Fa endbyte element of Fa table is not 0 or 255.</dl>
<p> Additionally, the Fn sradixsort function may fail and set <i>errno</i> for any of the errors specified for the library routine <a href="/docs/linux/man/3-malloc/">malloc</a>(3).</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-sort/">sort</a>(1), <a href="/docs/linux/man/3-qsort/">qsort</a>(3) </p>
<dl>
<dd>Knuth, D.E. 1968 <i>&quot;The Art of Computer Programming&quot;</i> <i>&quot;Sorting and Searching&quot;</i> Vol. 3 pp. 170-178</dl>
<dl>
<dd>Paige, R. 1987 <i>&quot;Three Partition Refinement Algorithms&quot;</i> <i>&quot;SIAM J. Comput.&quot;</i> Vol. 16 No. 6</dl>
<dl>
<dd>McIlroy, P. 1993 <i>&quot;Engineering Radix Sort&quot;</i> <i>&quot;Computing Systems&quot;</i> Vol. 6:1 pp. 5-27</dl>
<h2>History</h2>
<p>The Fn radixsort function first appeared in BSD 4.4</p>
