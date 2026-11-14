---
title: "asn1_read_value(3)"
name: "asn1_read_value"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_read_value/"
description: "asn1_read_value – API function"
---

<h2>NAME</h2>
<p> asn1_read_value &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_read_value(asn1_node </code><i>root</i><code>, const char * </code><i>name</i><code>, void * </code><i>ivalue</i><code>, int * </code><i>len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node root</p>
<dd> pointer to a structure.</p>
<dt>const char * name</p>
<dd> the name of the element inside a structure that you want to read.</p>
<dt>void * ivalue</p>
<dd> vector that will contain the element&#8217;s content, must be a pointer to memory cells already allocated (may be <code>NULL</code>).</p>
<dt>int * len</p>
<dd> number of bytes of *value: value[0]..value[len-1]. Initialy holds the sizeof value.</dl>
<h2>DESCRIPTION</h2>
<p> Returns the value of one element inside a structure. If an element is OPTIONAL and this returns <code>ASN1_ELEMENT_NOT_FOUND</code>, it means that this element wasn&#8217;t present in the der encoding that created the structure. The first element of a SEQUENCE_OF or SET_OF is named &quot;?1&quot;. The second one &quot;?2&quot; and so on. If the <i>root</i> provided is a node to specific sequence element, then the keyword &quot;?CURRENT&quot; is also acceptable and indicates the current sequence element of this node. </p>
<p> Note that there can be valid values with length zero. In these case this function will succeed and <i>len</i> will be zero.</p>
<h2>INTEGER</h2>
<p> VALUE will contain a two&#8217;s complement form integer. </p>
<p> integer=-1 -&gt; value[0]=0xFF , len=1. integer=1 -&gt; value[0]=0x01 , len=1.</p>
<h2>ENUMERATED</h2>
<p> As INTEGER (but only with not negative numbers).</p>
<h2>BOOLEAN</h2>
<p> VALUE will be the null terminated string &quot;TRUE&quot; or &quot;FALSE&quot; and LEN=5 or LEN=6. </p>
<p> OBJECT IDENTIFIER: VALUE will be a null terminated string with each number separated by a dot (i.e. &quot;1.2.3.543.1&quot;). </p>
<p> LEN = strlen(VALUE)+1</p>
<h2>UTCTIME</h2>
<p> VALUE will be a null terminated string in one of these formats: &quot;YYMMDDhhmmss+hh&#8217;mm&#8217;&quot; or &quot;YYMMDDhhmmss-hh&#8217;mm&#8217;&quot;. LEN=strlen(VALUE)+1.</p>
<h2>GENERALIZEDTIME</h2>
<p> VALUE will be a null terminated string in the same format used to set the value. </p>
<p> OCTET STRING: VALUE will contain the octet string and LEN will be the number of octets.</p>
<h2>GENERALSTRING</h2>
<p> VALUE will contain the generalstring and LEN will be the number of octets. </p>
<p> BIT STRING: VALUE will contain the bit string organized by bytes and LEN will be the number of bits.</p>
<h2>CHOICE</h2>
<p> If NAME indicates a choice type, VALUE will specify the alternative selected.</p>
<h2>ANY</h2>
<p> If NAME indicates an any type, VALUE will indicate the DER encoding of the structure actually used.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if value is returned, <code>ASN1_ELEMENT_NOT_FOUND</code> if <i>name</i> is not a valid element, <code>ASN1_VALUE_NOT_FOUND</code> if there isn&#8217;t any value for the element selected, and <code>ASN1_MEM_ERROR</code> if The value vector isn&#8217;t big enough to store the result, and in this case <i>len</i> will contain the number of bytes needed.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2015 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libtasn1</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtasn1</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info libtasn1</code></dl>
<p> should give you access to the complete manual. As an alternative you may obtain the manual from:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.gnu.org/software/libtasn1/manual/">http://www.gnu.org/software/libtasn1/manual/</a></code></dl>
<h2>Index</h2>
