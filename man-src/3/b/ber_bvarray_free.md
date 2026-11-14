---
title: "ber_bvarray_free(3)"
name: "ber_bvarray_free"
section: "3"
letter: "b"
url: "/docs/linux/man/3-ber_bvarray_free/"
description: "ber_int_t, ber_uint_t, ber_len_t, ber_slen_t, ber_tag_t, struct berval, BerValue, BerVarray, BerElement, ber_bvfree, ber_bvecfree, ber_bvecadd, ber_bvarray_free, ber_bvarray_add, ber_bvdup, ber_dup..."
---

<h2 class="name">NAME</h2>
<p> ber_int_t, ber_uint_t, ber_len_t, ber_slen_t, ber_tag_t, struct berval, BerValue, BerVarray, BerElement, ber_bvfree, ber_bvecfree, ber_bvecadd, ber_bvarray_free, ber_bvarray_add, ber_bvdup, ber_dupbv, ber_bvstr, ber_bvstrdup, ber_str2bv, ber_alloc_t, ber_init, ber_init2, ber_free &#8211; OpenLDAP LBER types and allocation functions </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LBER (liblber, -llber)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;lber.h&gt;</code> </p>
<pre><code>
typedef impl_tag_t ber_tag_t;
typedef impl_int_t ber_int_t;
typedef impl_uint_t ber_uint_t;
typedef impl_len_t ber_len_t;
typedef impl_slen_t ber_slen_t;
typedef struct berval {
    ber_len_t bv_len;
    char *bv_val;
} BerValue, *BerVarray;
typedef struct berelement BerElement;
</code></pre>
<p> <code>void ber_bvfree(struct berval *</code><i>bv</i><code>);</code> </p>
<p> <code>void ber_bvecfree(struct berval **</code><i>bvec</i><code>);</code> </p>
<p> <code>void ber_bvecadd(struct berval ***</code><i>bvec</i><code>, struct berval *</code><i>bv</i><code>);</code> </p>
<p> <code>void ber_bvarray_free(struct berval *</code><i>bvarray</i><code>);</code> </p>
<p> <code>void ber_bvarray_add(BerVarray *</code><i>bvarray</i><code>, BerValue *</code><i>bv</i><code>);</code> </p>
<p> <code>struct berval *ber_bvdup(const struct berval *</code><i>bv</i><code>);</code> </p>
<p> <code>struct berval *ber_dupbv(const struct berval *</code><i>dst</i><code>, struct berval *</code><i>src</i><code>);</code> </p>
<p> <code>struct berval *ber_bvstr(const char *</code><i>str</i><code>);</code> </p>
<p> <code>struct berval *ber_bvstrdup(const char *</code><i>str</i><code>);</code> </p>
<p> <code>struct berval *ber_str2bv(const char *</code><i>str</i><code>, ber_len_t </code><i>len</i><code>, int </code><i>dup</i><code>, struct berval *</code><i>bv</i><code>);</code> </p>
<p> <code>BerElement *ber_alloc_t(int </code><i>options</i><code>);</code> </p>
<p> <code>BerElement *ber_init(struct berval *</code><i>bv</i><code>);</code> </p>
<p> <code>void ber_init2(BerElement *</code><i>ber</i><code>, struct berval *</code><i>bv</i><code>, int </code><i>options</i><code>);</code> </p>
<p> <code>void ber_free(BerElement *</code><i>ber</i><code>, int </code><i>freebuf</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The following are the basic types and structures defined for use with the Lightweight BER library. </p>
<p> <code>ber_int_t</code> is a signed integer of at least 32 bits. It is commonly equivalent to <code>int</code>. <code>ber_uint_t</code> is the unsigned variant of <code>ber_int_t</code>. </p>
<p> <code>ber_len_t</code> is an unsigned integer of at least 32 bits used to represent a length. It is commonly equivalent to a <code>size_t</code>. <code>ber_slen_t</code> is the signed variant to <code>ber_len_t</code>. </p>
<p> <code>ber_tag_t</code> is an unsigned integer of at least 32 bits used to represent a BER tag. It is commonly equivalent to a <code>unsigned long</code>. </p>
<p> The actual definitions of the integral impl_TYPE_t types are platform specific. </p>
<p> <code>BerValue</code>, commonly used as <code>struct berval</code>, is used to hold an arbitrary sequence of octets. <code>bv_val</code> points to <code>bv_len</code> octets. <code>bv_val</code> is not necessarily terminated by a NULL (zero) octet. <code>ber_bvfree</code>() frees a BerValue, pointed to by <i>bv</i>, returned from this API. If <i>bv</i> is NULL, the routine does nothing. </p>
<p> <code>ber_bvecfree</code>() frees an array of BerValues (and the array), pointed to by <i>bvec</i>, returned from this API. If <i>bvec</i> is NULL, the routine does nothing. <code>ber_bvecadd</code>() appends the <i>bv</i> pointer to the <i>bvec</i> array. Space for the array is allocated as needed. The end of the array is marked by a NULL pointer. </p>
<p> <code>ber_bvarray_free</code>() frees an array of BerValues (and the array), pointed to by <i>bvarray</i>, returned from this API. If <i>bvarray</i> is NULL, the routine does nothing. <code>ber_bvarray_add</code>() appends the contents of the BerValue pointed to by <i>bv</i> to the <i>bvarray</i> array. Space for the new element is allocated as needed. The end of the array is marked by a BerValue with a NULL bv_val field. </p>
<p> <code>ber_bvdup</code>() returns a copy of a BerValue. The routine returns NULL upon error (e.g. out of memory). The caller should use <code>ber_bvfree</code>() to deallocate the resulting BerValue. <code>ber_dupbv</code>() copies a BerValue from <i>src</i> to <i>dst</i>. If <i>dst</i> is NULL a new BerValue will be allocated to hold the copy. The routine returns NULL upon error, otherwise it returns a pointer to the copy. If <i>dst</i> is NULL the caller should use <code>ber_bvfree</code>() to deallocate the resulting BerValue, otherwise <code>ber_memfree</code>() should be used to deallocate the <i>dst-&gt;bv_val</i>. (The <code>ber_bvdup</code>() function is internally implemented as ber_dupbv(NULL, bv). <code>ber_bvdup</code>() is provided only for compatibility with an expired draft of the LDAP C API; <code>ber_dupbv</code>() is the preferred interface.) </p>
<p> <code>ber_bvstr</code>() returns a BerValue containing the string pointed to by <i>str</i>. <code>ber_bvstrdup</code>() returns a BerValue containing a copy of the string pointed to by <i>str</i>. <code>ber_str2bv</code>() returns a BerValue containing the string pointed to by <i>str</i>, whose length may be optionally specified in <i>len</i>. If <i>dup</i> is non-zero, the BerValue will contain a copy of <i>str</i>. If <i>len</i> is zero, the number of bytes to copy will be determined by <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3), otherwise <i>len</i> bytes will be copied. If <i>bv</i> is non-NULL, the result will be stored in the given BerValue, otherwise a new BerValue will be allocated to store the result. NOTE: Both <code>ber_bvstr</code>() and <code>ber_bvstrdup</code>() are implemented as macros using <code>ber_str2bv</code>() in this version of the library. </p>
<p> <code>BerElement</code> is an opaque structure used to maintain state information used in encoding and decoding. <code>ber_alloc_t</code>() is used to create an empty BerElement structure. If <code>LBER_USE_DER</code> is specified for the <i>options</i> parameter then data lengths for data written to the BerElement will be encoded in the minimal number of octets required, otherwise they will always be written as four byte values. <code>ber_init</code>() creates a BerElement structure that is initialized with a copy of the data in its <i>bv</i> parameter. <code>ber_init2</code>() initializes an existing BerElement <i>ber</i> using the data in the <i>bv</i> parameter. The data is referenced directly, not copied. The <i>options</i> parameter is the same as for <code>ber_alloc_t</code>(). <code>ber_free</code>() frees a BerElement pointed to by <i>ber</i>. If <i>ber</i> is NULL, the routine does nothing. If <i>freebuf</i> is zero, the internal buffer is not freed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3), <code><a href="/docs/linux/man/3-lber-decode/">lber-decode</a></code>(3), <code><a href="/docs/linux/man/3-lber-memory/">lber-memory</a></code>(3) </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
