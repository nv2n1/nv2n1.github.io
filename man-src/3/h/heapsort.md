---
title: "heapsort(3)"
name: "heapsort"
section: "3"
letter: "h"
url: "/docs/linux/man/3-heapsort/"
description: "heapsort , mergesort – sort functions"
---

<h2 class="name">NAME</h2>
<p> <code>heapsort , mergesort</code> &#8211; sort functions </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In bsd/stdlib.h Ft int Fo heapsort Fa void *base Fa size_t nmemb Fa size_t size Fa int *comparconst void *, const void * Fc Ft int Fo mergesort Fa void *base Fa size_t nmemb Fa size_t size Fa int *comparconst void *, const void * Fc</p>
<h2>DESCRIPTION</h2>
<p> The Fn heapsort function is a modified selection sort. The Fn mergesort function is a modified merge sort with exponential search intended for sorting data with pre-existing order. </p>
<p> The Fn heapsort function sorts an array of Fa nmemb objects, the initial member of which is pointed to by Fa base . The size of each object is specified by Fa size . The Fn mergesort function behaves similarly, but <i>requires</i> that Fa size be greater than &#8220;sizeof(void *) / 2&#8221; </p>
<p> The contents of the array Fa base are sorted in ascending order according to a comparison function pointed to by Fa compar , which requires two arguments pointing to the objects being compared. </p>
<p> The comparison function must return an integer less than, equal to, or greater than zero if the first argument is considered to be respectively less than, equal to, or greater than the second. </p>
<p> The algorithm implemented by Fn heapsort is <i>not</i> stable, that is, if two members compare as equal, their order in the sorted array is undefined. The Fn mergesort algorithm is stable. </p>
<p> The Fn heapsort function is an implementation of An J.W.J. William Ns &#8216;s &#8220;heapsort&#8221; algorithm, a variant of selection sorting; in particular, see An D.E. Knuth Ns &#8216;s <i>&quot;Algorithm H&quot; .</i> <code>Heapsort</code> takes O N lg N worst-case time. Its <i>only</i> advantage over Fn qsort is that it uses almost no additional memory; while Fn qsort does not allocate memory, it is implemented using recursion. </p>
<p> The function Fn mergesort requires additional memory of size Fa nmemb * Fa size bytes; it should be used only when space is not at a premium. The Fn mergesort function is optimized for data with pre-existing order; its worst case time is O N lg N; its best case is O N. </p>
<p> Normally, Fn qsort is faster than Fn mergesort is faster than Fn heapsort . Memory availability and pre-existing order in the data can make this untrue.</p>
<h2>RETURN VALUES</h2>
<p> Rv -std heapsort mergesort</p>
<h2>ERRORS</h2>
<p> The Fn heapsort and Fn mergesort functions succeed unless:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The Fa size argument is zero, or, the Fa size argument to Fn mergesort is less than &#8220;sizeof(void *) / 2&#8221;</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The Fn heapsort or Fn mergesort functions were unable to allocate memory.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sort/">sort</a>(1), <a href="/docs/linux/man/3-radixsort/">radixsort</a>(3)</p>
<dl>
<dt>
<dd> Williams, J.W.J 1964 <i>&quot;Heapsort&quot;</i> <i>&quot;Communications of the ACM&quot;</i> 7:1 pp. 347-348</dl>
<dl>
<dt>
<dd> Knuth, D.E. 1968 <i>&quot;The Art of Computer Programming&quot;</i> Vol. 3 <i>&quot;Sorting and Searching&quot;</i> pp. 114-123, 145-149</dl>
<dl>
<dt>
<dd> McIlroy, P.M. <i>&quot;Optimistic Sorting and Information Theoretic Complexity&quot;</i> <i>&quot;Fourth Annual ACM-SIAM Symposium on Discrete Algorithms&quot;</i> January 1992</dl>
<dl>
<dt>
<dd> Bentley, J.L. McIlroy, M.D. <i>&quot;Engineering a Sort Function&quot;</i> <i>&quot;Software&#8211;Practice and Experience&quot;</i> Vol. 23(11) pp. 1249-1265 November 1993</dl>
<h2>Index</h2>
