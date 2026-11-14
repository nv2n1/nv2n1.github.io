---
title: "ber_put_seq(3)"
name: "ber_put_seq"
section: "3"
letter: "b"
url: "/docs/linux/man/3-ber_put_seq/"
description: "ber_alloc_t, ber_flush, ber_flush2, ber_printf, ber_put_int, ber_put_enum, ber_put_ostring, ber_put_string, ber_put_null, ber_put_boolean, ber_put_bitstring, ber_start_seq, ber_start_set, ber_put_s..."
---

<h2 class="name">NAME</h2>
<p> ber_alloc_t, ber_flush, ber_flush2, ber_printf, ber_put_int, ber_put_enum, ber_put_ostring, ber_put_string, ber_put_null, ber_put_boolean, ber_put_bitstring, ber_start_seq, ber_start_set, ber_put_seq, ber_put_set &#8211; OpenLDAP LBER simplified Basic Encoding Rules library routines for encoding </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LBER (liblber, -llber)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;lber.h&gt;</code> </p>
<p> <code>BerElement *ber_alloc_t(int </code><i>options</i><code>);</code> </p>
<p> <code>int ber_flush(Sockbuf *</code><i>sb</i><code>, BerElement *</code><i>ber</i><code>, int </code><i>freeit</i><code>);</code> </p>
<p> <code>int ber_flush2(Sockbuf *</code><i>sb</i><code>, BerElement *</code><i>ber</i><code>, int </code><i>freeit</i><code>);</code> </p>
<p> <code>int ber_printf(BerElement *</code><i>ber</i><code>, const char *</code><i>fmt</i><code>, &#8230;);</code> </p>
<p> <code>int ber_put_int(BerElement *</code><i>ber</i><code>, ber_int_t </code><i>num</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_put_enum(BerElement *</code><i>ber</i><code>, ber_int_t </code><i>num</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_put_ostring(BerElement *</code><i>ber</i><code>, const char *</code><i>str</i><code>, ber_len_t </code><i>len</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_put_string(BerElement *</code><i>ber</i><code>, const char *</code><i>str</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_put_null(BerElement *</code><i>ber</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_put_boolean(BerElement *</code><i>ber</i><code>, ber_int_t </code><i>bool</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_put_bitstring(BerElement *</code><i>ber</i><code>, const char *</code><i>str</i><code>, ber_len_t </code><i>blen</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_start_seq(BerElement *</code><i>ber</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_start_set(BerElement *</code><i>ber</i><code>, ber_tag_t </code><i>tag</i><code>);</code> </p>
<p> <code>int ber_put_seq(BerElement *</code><i>ber</i><code>);</code> </p>
<p> <code>int ber_put_set(BerElement *</code><i>ber</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These routines provide a subroutine interface to a simplified implementation of the Basic Encoding Rules of ASN.1. The version of BER these routines support is the one defined for the LDAP protocol. The encoding rules are the same as BER, except that only definite form lengths are used, and bitstrings and octet strings are always encoded in primitive form. This man page describes the encoding routines in the lber library. See <code><a href="/docs/linux/man/3-lber-decode/">lber-decode</a></code>(3) for details on the corresponding decoding routines. Consult <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3) for information about types, allocators, and deallocators. </p>
<p> Normally, the only routines that need to be called by an application are <code>ber_alloc_t</code>() to allocate a BER element for encoding, <code>ber_printf</code>() to do the actual encoding, and <code>ber_flush2</code>() to actually write the element. The other routines are provided for those applications that need more control than <code>ber_printf</code>() provides. In general, these routines return the length of the element encoded, or -1 if an error occurred. </p>
<p> The <code>ber_alloc_t</code>() routine is used to allocate a new BER element. It should be called with an argument of LBER_USE_DER. </p>
<p> The <code>ber_flush2</code>() routine is used to actually write the element to a socket (or file) descriptor, once it has been fully encoded (using <code>ber_printf</code>() and friends). See <code><a href="/docs/linux/man/3-lber-sockbuf/">lber-sockbuf</a></code>(3) for more details on the Sockbuf implementation of the <i>sb</i> parameter. If the <i>freeit</i> parameter is non-zero, the supplied <i>ber</i> will be freed. If <i>LBER_FLUSH_FREE_ON_SUCCESS</i> is used, the <i>ber</i> is only freed when successfully flushed, otherwise it is left intact; if <i>LBER_FLUSH_FREE_ON_ERROR</i> is used, the <i>ber</i> is only freed when an error occurs, otherwise it is left intact; if <i>LBER_FLUSH_FREE_ALWAYS</i> is used, the <i>ber</i> is freed anyway. This function differs from the original <code><a href="/docs/linux/man/3-ber_flush/">ber_flush</a></code>(3) function, whose behavior corresponds to that indicated for <i>LBER_FLUSH_FREE_ON_SUCCESS</i>. Note that in the future, the behavior of <code><a href="/docs/linux/man/3-ber_flush/">ber_flush</a></code>(3) with <i>freeit</i> non-zero might change into that of <code><a href="/docs/linux/man/3-ber_flush2/">ber_flush2</a></code>(3) with <i>freeit</i> set to <i>LBER_FLUSH_FREE_ALWAYS</i>. </p>
<p> The <code>ber_printf</code>() routine is used to encode a BER element in much the same way that <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) works. One important difference, though, is that some state information is kept with the <i>ber</i> parameter so that multiple calls can be made to <code>ber_printf</code>() to append things to the end of the BER element. <code>Ber_printf</code>() writes to <i>ber</i>, a pointer to a BerElement such as returned by <code>ber_alloc_t</code>(). It interprets and formats its arguments according to the format string <i>fmt</i>. The format string can contain the following characters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>b</code></p>
<dd> Boolean. An ber_int_t parameter should be supplied. A boolean element is output.</p>
<dt><code>e</code></p>
<dd> Enumeration. An ber_int_t parameter should be supplied. An enumeration element is output.</p>
<dt><code>i</code></p>
<dd> Integer. An ber_int_t parameter should be supplied. An integer element is output.</p>
<dt><code>B</code></p>
<dd> Bitstring. A char * pointer to the start of the bitstring is supplied, followed by the number of bits in the bitstring. A bitstring element is output.</p>
<dt><code>n</code></p>
<dd> Null. No parameter is required. A null element is output.</p>
<dt><code>o</code></p>
<dd> Octet string. A char * is supplied, followed by the length of the string pointed to. An octet string element is output.</p>
<dt><code>O</code></p>
<dd> Octet string. A struct berval * is supplied. An octet string element is output.</p>
<dt><code>s</code></p>
<dd> Octet string. A null-terminated string is supplied. An octet string element is output, not including the trailing NULL octet.</p>
<dt><code>t</code></p>
<dd> Tag. A ber_tag_t specifying the tag to give the next element is provided. This works across calls.</p>
<dt><code>v</code></p>
<dd> Several octet strings. A null-terminated array of char *&#8217;s is supplied. Note that a construct like &#8216;{v}&#8217; is required to get an actual SEQUENCE OF octet strings.</p>
<dt><code>V</code></p>
<dd> Several octet strings. A null-terminated array of struct berval *&#8217;s is supplied. Note that a construct like &#8216;{V}&#8217; is required to get an actual SEQUENCE OF octet strings.</p>
<dt><code>W</code></p>
<dd> Several octet strings. An array of struct berval&#8217;s is supplied. The array is terminated by a struct berval with a NULL bv_val. Note that a construct like &#8216;{W}&#8217; is required to get an actual SEQUENCE OF octet strings.</p>
<dt><code>{</code></p>
<dd> Begin sequence. No parameter is required.</p>
<dt><code>}</code></p>
<dd> End sequence. No parameter is required.</p>
<dt><code>[</code></p>
<dd> Begin set. No parameter is required.</p>
<dt><code>]</code></p>
<dd> End set. No parameter is required.</dl>
</dl>
<p> The <code>ber_put_int</code>() routine writes the integer element <i>num</i> to the BER element <i>ber</i>. </p>
<p> The <code>ber_put_enum</code>() routine writes the enumeration element <i>num</i> to the BER element <i>ber</i>. </p>
<p> The <code>ber_put_boolean</code>() routine writes the boolean value given by <i>bool</i> to the BER element. </p>
<p> The <code>ber_put_bitstring</code>() routine writes <i>blen</i> bits starting at <i>str</i> as a bitstring value to the given BER element. Note that <i>blen</i> is the length <i>in bits</i> of the bitstring. </p>
<p> The <code>ber_put_ostring</code>() routine writes <i>len</i> bytes starting at <i>str</i> to the BER element as an octet string. </p>
<p> The <code>ber_put_string</code>() routine writes the null-terminated string (minus the terminating &#8216;&nbsp;<wbr>&#8216;) to the BER element as an octet string. </p>
<p> The <code>ber_put_null</code>() routine writes a NULL element to the BER element. </p>
<p> The <code>ber_start_seq</code>() routine is used to start a sequence in the BER element. The <code>ber_start_set</code>() routine works similarly. The end of the sequence or set is marked by the nearest matching call to <code>ber_put_seq</code>() or <code>ber_put_set</code>(), respectively.</p>
<h2>EXAMPLES</h2>
<p> Assuming the following variable declarations, and that the variables have been assigned appropriately, an lber encoding of the following ASN.1 object: </p>
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
<p> can be achieved like so: </p>
<pre><code>
int rc;
ber_int_t scope, ali, size, time, attrsonly;
char *dn, **attrs;
BerElement *ber;
/* ... fill in values ... */
ber = ber_alloc_t(LBER_USE_DER);
if (ber == NULL) {
    /* error */
}
rc = ber_printf(ber, "{siiiib{v}}", dn, scope, ali,
                size, time, attrsonly, attrs);
if (rc == -1) {
    /* error */
} else {
    /* success */
}
</code></pre>
<h2>ERRORS</h2>
<p> If an error occurs during encoding, generally these routines return -1. </p>
<h2>NOTES</h2>
<p> The return values for all of these functions are declared in the &lt;lber.h&gt; header file.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lber-decode/">lber-decode</a></code>(3), <code><a href="/docs/linux/man/3-lber-memory/">lber-memory</a></code>(3), <code><a href="/docs/linux/man/3-lber-sockbuf/">lber-sockbuf</a></code>(3), <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
