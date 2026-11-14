---
title: "ber_first_element(3)"
name: "ber_first_element"
section: "3"
letter: "b"
url: "/docs/linux/man/3-ber_first_element/"
description: "ber_get_next, ber_skip_tag, ber_peek_tag, ber_scanf, ber_get_int, ber_get_enum, ber_get_stringb, ber_get_stringa, ber_get_stringal, ber_get_stringbv, ber_get_null, ber_get_boolean, ber_get_bitstrin..."
---

<h2 class="name">NAME</h2>
<p> ber_get_next, ber_skip_tag, ber_peek_tag, ber_scanf, ber_get_int, ber_get_enum, ber_get_stringb, ber_get_stringa, ber_get_stringal, ber_get_stringbv, ber_get_null, ber_get_boolean, ber_get_bitstring, ber_first_element, ber_next_element &#8211; OpenLDAP LBER simplified Basic Encoding Rules library routines for decoding </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LBER (liblber, -llber)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;lber.h&gt;</code> </p>
<p> <code>ber_tag_t ber_get_next(Sockbuf *</code><i>sb</i><code>, ber_len_t *</code><i>len</i><code>, BerElement *</code><i>ber</i><code>);</code> </p>
<p> <code>ber_tag_t ber_skip_tag(BerElement *</code><i>ber</i><code>, ber_len_t *</code><i>len</i><code>);</code> </p>
<p> <code>ber_tag_t ber_peek_tag(BerElement *</code><i>ber</i><code>, ber_len_t *</code><i>len</i><code>);</code> </p>
<p> <code>ber_tag_t ber_scanf(BerElement *</code><i>ber</i><code>, const char *</code><i>fmt</i><code>, &#8230;);</code> </p>
<p> <code>ber_tag_t ber_get_int(BerElement *</code><i>ber</i><code>, ber_int_t *</code><i>num</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_enum(BerElement *</code><i>ber</i><code>, ber_int_t *</code><i>num</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_stringb(BerElement *</code><i>ber</i><code>, char *</code><i>buf</i><code>, ber_len_t *</code><i>len</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_stringa(BerElement *</code><i>ber</i><code>, char **</code><i>buf</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_stringal(BerElement *</code><i>ber</i><code>, struct berval **</code><i>bv</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_stringbv(BerElement *</code><i>ber</i><code>, struct berval *</code><i>bv</i><code>, int </code><i>alloc</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_null(BerElement *</code><i>ber</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_boolean(BerElement *</code><i>ber</i><code>, ber_int_t *</code><i>bool</i><code>);</code> </p>
<p> <code>ber_tag_t ber_get_bitstringa(BerElement *</code><i>ber</i><code>, char **</code><i>buf</i><code>, ber_len_t *</code><i>blen</i><code>);</code> </p>
<p> <code>ber_tag_t ber_first_element(BerElement *</code><i>ber</i><code>, ber_len_t *</code><i>len</i><code>, char **</code><i>cookie</i><code>);</code> </p>
<p> <code>ber_tag_t ber_next_element(BerElement *</code><i>ber</i><code>, ber_len_t *</code><i>len</i><code>, const char *</code><i>cookie</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These routines provide a subroutine interface to a simplified implementation of the Basic Encoding Rules of ASN.1. The version of BER these routines support is the one defined for the LDAP protocol. The encoding rules are the same as BER, except that only definite form lengths are used, and bitstrings and octet strings are always encoded in primitive form. This man page describes the decoding routines in the lber library. See <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3) for details on the corresponding encoding routines. Consult <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3) for information about types, allocators, and deallocators. </p>
<p> Normally, the only routines that need to be called by an application are <code>ber_get_next</code>() to get the next BER element and <code>ber_scanf</code>() to do the actual decoding. In some cases, <code>ber_peek_tag</code>() may also need to be called in normal usage. The other routines are provided for those applications that need more control than <code>ber_scanf</code>() provides. In general, these routines return the tag of the element decoded, or LBER_ERROR if an error occurred. </p>
<p> The <code>ber_get_next</code>() routine is used to read the next BER element from the given Sockbuf, <i>sb</i>. It strips off and returns the leading tag, strips off and returns the length of the entire element in <i>len</i>, and sets up <i>ber</i> for subsequent calls to <code>ber_scanf</code>() et al to decode the element. See <code><a href="/docs/linux/man/3-lber-sockbuf/">lber-sockbuf</a></code>(3) for details of the Sockbuf implementation of the <i>sb</i> parameter. </p>
<p> The <code>ber_scanf</code>() routine is used to decode a BER element in much the same way that <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3) works. It reads from <i>ber</i>, a pointer to a BerElement such as returned by <code>ber_get_next</code>(), interprets the bytes according to the format string <i>fmt</i>, and stores the results in its additional arguments. The format string contains conversion specifications which are used to direct the interpretation of the BER element. The format string can contain the following characters.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>a</code></p>
<dd> Octet string. A char ** should be supplied. Memory is allocated, filled with the contents of the octet string, null-terminated, and returned in the parameter. The caller should free the returned string using <code>ber_memfree</code>().</p>
<dt><code>A</code></p>
<dd> Octet string. A variant of &quot;<code>a</code>&quot;. A char ** should be supplied. Memory is allocated, filled with the contents of the octet string, null-terminated, and returned in the parameter, unless a zero-length string would result; in that case, the arg is set to NULL. The caller should free the returned string using <code>ber_memfree</code>().</p>
<dt><code>s</code></p>
<dd> Octet string. A char * buffer should be supplied, followed by a pointer to a ber_len_t initialized to the size of the buffer. Upon return, the null-terminated octet string is put into the buffer, and the ber_len_t is set to the actual size of the octet string.</p>
<dt><code>O</code></p>
<dd> Octet string. A struct ber_val ** should be supplied, which upon return points to a dynamically allocated struct berval containing the octet string and its length. The caller should free the returned structure using <code>ber_bvfree</code>().</p>
<dt><code>o</code></p>
<dd> Octet string. A struct ber_val * should be supplied, which upon return contains the dynamically allocated octet string and its length. The caller should free the returned octet string using <code>ber_memfree</code>().</p>
<dt><code>m</code></p>
<dd> Octet string. A struct ber_val * should be supplied, which upon return contains the octet string and its length. The string resides in memory assigned to the BerElement, and must not be freed by the caller.</p>
<dt><code>b</code></p>
<dd> Boolean. A pointer to a ber_int_t should be supplied.</p>
<dt><code>e</code></p>
<dd> Enumeration. A pointer to a ber_int_t should be supplied.</p>
<dt><code>i</code></p>
<dd> Integer. A pointer to a ber_int_t should be supplied.</p>
<dt><code>B</code></p>
<dd> Bitstring. A char ** should be supplied which will point to the dynamically allocated bits, followed by a ber_len_t *, which will point to the length (in bits) of the bitstring returned.</p>
<dt><code>n</code></p>
<dd> Null. No parameter is required. The element is simply skipped if it is recognized.</p>
<dt><code>v</code></p>
<dd> Sequence of octet strings. A char *** should be supplied, which upon return points to a dynamically allocated null-terminated array of char *&#8217;s containing the octet strings. NULL is returned if the sequence is empty. The caller should free the returned array and octet strings using <code>ber_memvfree</code>().</p>
<dt><code>V</code></p>
<dd> Sequence of octet strings with lengths. A struct berval *** should be supplied, which upon return points to a dynamically allocated null-terminated array of struct berval *&#8217;s containing the octet strings and their lengths. NULL is returned if the sequence is empty. The caller should free the returned structures using <code>ber_bvecfree</code>().</p>
<dt><code>W</code></p>
<dd> Sequence of octet strings with lengths. A BerVarray * should be supplied, which upon return points to a dynamically allocated array of struct berval&#8217;s containing the octet strings and their lengths. The array is terminated by a struct berval with a NULL bv_val string pointer. NULL is returned if the sequence is empty. The caller should free the returned structures using <code>ber_bvarray_free</code>().</p>
<dt><code>M</code></p>
<dd> Sequence of octet strings with lengths. This is a generalized form of the previous three formats. A void ** (ptr) should be supplied, followed by a ber_len_t * (len) and a ber_len_t (off). Upon return (ptr) will point to a dynamically allocated array whose elements are all of size (*len). A struct berval will be filled starting at offset (off) in each element. The strings in each struct berval reside in memory assigned to the BerElement and must not be freed by the caller. The array is terminated by a struct berval with a NULL bv_val string pointer. NULL is returned if the sequence is empty. The number of elements in the array is also stored in (*len) on return. The caller should free the returned array using <code>ber_memfree</code>().</p>
<dt><code>l</code></p>
<dd> Length of the next element. A pointer to a ber_len_t should be supplied.</p>
<dt><code>t</code></p>
<dd> Tag of the next element. A pointer to a ber_tag_t should be supplied.</p>
<dt><code>T</code></p>
<dd> Skip element and return its tag. A pointer to a ber_tag_t should be supplied.</p>
<dt><code>x</code></p>
<dd> Skip element. The next element is skipped.</p>
<dt><code>{</code></p>
<dd> Begin sequence. No parameter is required. The initial sequence tag and length are skipped.</p>
<dt><code>}</code></p>
<dd> End sequence. No parameter is required and no action is taken.</p>
<dt><code>[</code></p>
<dd> Begin set. No parameter is required. The initial set tag and length are skipped.</p>
<dt><code>]</code></p>
<dd> End set. No parameter is required and no action is taken.</dl>
</dl>
<p> The <code>ber_get_int</code>() routine tries to interpret the next element as an integer, returning the result in <i>num</i>. The tag of whatever it finds is returned on success, LBER_ERROR (-1) on failure. </p>
<p> The <code>ber_get_stringb</code>() routine is used to read an octet string into a preallocated buffer. The <i>len</i> parameter should be initialized to the size of the buffer, and will contain the length of the octet string read upon return. The buffer should be big enough to take the octet string value plus a terminating NULL byte. </p>
<p> The <code>ber_get_stringa</code>() routine is used to dynamically allocate space into which an octet string is read. The caller should free the returned string using <code>ber_memfree().</code> </p>
<p> The <code>ber_get_stringal</code>() routine is used to dynamically allocate space into which an octet string and its length are read. It takes a struct berval **, and returns the result in this parameter. The caller should free the returned structure using <code>ber_bvfree().</code> </p>
<p> The <code>ber_get_stringbv</code>() routine is used to read an octet string and its length into the provided struct berval *. If the <i>alloc</i> parameter is zero, the string will reside in memory assigned to the BerElement, and must not be freed by the caller. If the <i>alloc</i> parameter is non-zero, the string will be copied into dynamically allocated space which should be returned using <code>ber_memfree</code>(). </p>
<p> The <code>ber_get_null</code>() routine is used to read a NULL element. It returns the tag of the element it skips over. </p>
<p> The <code>ber_get_boolean</code>() routine is used to read a boolean value. It is called the same way that <code>ber_get_int</code>() is called. </p>
<p> The <code>ber_get_enum</code>() routine is used to read a enumeration value. It is called the same way that <code>ber_get_int</code>() is called. </p>
<p> The <code>ber_get_bitstringa</code>() routine is used to read a bitstring value. It takes a char ** which will hold the dynamically allocated bits, followed by an ber_len_t *, which will point to the length (in bits) of the bitstring returned. The caller should free the returned string using <code>ber_memfree</code>(). </p>
<p> The <code>ber_first_element</code>() routine is used to return the tag and length of the first element in a set or sequence. It also returns in <i>cookie</i> a magic cookie parameter that should be passed to subsequent calls to ber_next_element(), which returns similar information.</p>
<h2>EXAMPLES</h2>
<p> Assume the variable <i>ber</i> contains a lightweight BER encoding of the following ASN.1 object: </p>
<pre><code>
AlmostASearchRequest : = SEQUENCE
{
    baseObject DistinguishedName,
        scope ENUMERATED{
            baseObject(0),
            singleLevel(1),
            wholeSubtree(2)},
        derefAliases ENUMERATED{
            neverDerefaliases(0),
            derefInSearching(1),
            derefFindingBaseObj(2),
            alwaysDerefAliases(3)},
        sizelimit INTEGER(0..65535),
        timelimit INTEGER(0..65535),
        attrsOnly BOOLEAN,
        attributes SEQUENCE OF AttributeType
}
</code></pre>
<p> The element can be decoded using <code>ber_scanf</code>() as follows. </p>
<pre><code>
ber_int_t scope, deref, size, time, attrsonly;
char *dn, **attrs;
ber_tag_t tag;
tag = ber_scanf(ber, "{aeeiib{v}}",
                &amp;dn, &amp;scope, &amp;deref,
                &amp;size, &amp;time, &amp;attrsonly, &amp;attrs);
if (tag == LBER_ERROR) {
    /* error */
} else {
    /* success */
}
ber_memfree(dn);
ber_memvfree(attrs);
</code></pre>
<h2>ERRORS</h2>
<p> If an error occurs during decoding, generally these routines return LBER_ERROR ((ber_tag_t)-1). </p>
<h2>NOTES</h2>
<p> The return values for all of these functions are declared in the <code>&lt;lber.h&gt;</code> header file. Some routines may dynamically allocate memory which must be freed by the caller using supplied deallocation routines.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3), <code><a href="/docs/linux/man/3-lber-memory/">lber-memory</a></code>(3), <code><a href="/docs/linux/man/3-lber-sockbuf/">lber-sockbuf</a></code>(3), <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
