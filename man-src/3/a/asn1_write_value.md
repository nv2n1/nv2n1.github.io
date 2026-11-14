---
title: "asn1_write_value(3)"
name: "asn1_write_value"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_write_value/"
description: "asn1_write_value – API function"
---

<h2>NAME</h2>
<p> asn1_write_value &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_write_value(asn1_node </code><i>node_root</i><code>, const char * </code><i>name</i><code>, const void * </code><i>ivalue</i><code>, int </code><i>len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node node_root</p>
<dd> pointer to a structure</p>
<dt>const char * name</p>
<dd> the name of the element inside the structure that you want to set.</p>
<dt>const void * ivalue</p>
<dd> vector used to specify the value to set. If len is &gt;0, VALUE must be a two&#8217;s complement form integer. if len=0 *VALUE must be a null terminated string with an integer value.</p>
<dt>int len</p>
<dd> number of bytes of *value to use to set the value: value[0]..value[len-1] or 0 if value is a null terminated string</dl>
<h2>DESCRIPTION</h2>
<p> Set the value of one element inside a structure. </p>
<p> If an element is OPTIONAL and you want to delete it, you must use the value=NULL and len=0. Using &quot;pkix.asn&quot;: </p>
<p> result=asn1_write_value(cert, &quot;tbsCertificate.issuerUniqueID&quot;, NULL, 0); </p>
<p> Description for each type:</p>
<h2>INTEGER</h2>
<p> VALUE must contain a two&#8217;s complement form integer. </p>
<p> value[0]=0xFF , len=1 -&gt; integer=-1. value[0]=0xFF value[1]=0xFF , len=2 -&gt; integer=-1. value[0]=0x01 , len=1 -&gt; integer= 1. value[0]=0x00 value[1]=0x01 , len=2 -&gt; integer= 1. value=&quot;123&quot; , len=0 -&gt; integer= 123.</p>
<h2>ENUMERATED</h2>
<p> As INTEGER (but only with not negative numbers).</p>
<h2>BOOLEAN</h2>
<p> VALUE must be the null terminated string &quot;TRUE&quot; or &quot;FALSE&quot; and LEN != 0. </p>
<p> value=&quot;TRUE&quot; , len=1 -&gt; boolean=TRUE. value=&quot;FALSE&quot; , len=1 -&gt; boolean=FALSE. </p>
<p> OBJECT IDENTIFIER: VALUE must be a null terminated string with each number separated by a dot (e.g. &quot;1.2.3.543.1&quot;). LEN != 0. </p>
<p> value=&quot;1 2 840 10040 4 3&quot; , len=1 -&gt; OID=dsa-with-sha.</p>
<h2>UTCTIME</h2>
<p> VALUE must be a null terminated string in one of these formats: &quot;YYMMDDhhmmssZ&quot;, &quot;YYMMDDhhmmssZ&quot;, &quot;YYMMDDhhmmss+hh&#8217;mm&#8217;&quot;, &quot;YYMMDDhhmmss-hh&#8217;mm&#8217;&quot;, &quot;YYMMDDhhmm+hh&#8217;mm&#8217;&quot;, or &quot;YYMMDDhhmm-hh&#8217;mm&#8217;&quot;. LEN != 0. </p>
<p> value=&quot;9801011200Z&quot; , len=1 -&gt; time=Jannuary 1st, 1998 at 12h 00m Greenwich Mean Time</p>
<h2>GENERALIZEDTIME</h2>
<p> VALUE must be in one of this format: &quot;YYYYMMDDhhmmss.sZ&quot;, &quot;YYYYMMDDhhmmss.sZ&quot;, &quot;YYYYMMDDhhmmss.s+hh&#8217;mm&#8217;&quot;, &quot;YYYYMMDDhhmmss.s-hh&#8217;mm&#8217;&quot;, &quot;YYYYMMDDhhmm+hh&#8217;mm&#8217;&quot;, or &quot;YYYYMMDDhhmm-hh&#8217;mm&#8217;&quot; where ss.s indicates the seconds with any precision like &quot;10.1&quot; or &quot;01.02&quot;. LEN != 0 </p>
<p> value=&quot;2001010112001.12-0700&quot; , len=1 -&gt; time=Jannuary 1st, 2001 at 12h 00m 01.12s Pacific Daylight Time </p>
<p> OCTET STRING: VALUE contains the octet string and LEN is the number of octets. </p>
<p> value=&quot;$sh$x01$sh$x02$sh$x03&quot; , len=3 -&gt; three bytes octet string</p>
<h2>GENERALSTRING</h2>
<p> VALUE contains the generalstring and LEN is the number of octets. </p>
<p> value=&quot;$sh$x01$sh$x02$sh$x03&quot; , len=3 -&gt; three bytes generalstring </p>
<p> BIT STRING: VALUE contains the bit string organized by bytes and LEN is the number of bits. </p>
<p> value=&quot;$sh$xCF&quot; , len=6 -&gt; bit string=&quot;110011&quot; (six bits)</p>
<h2>CHOICE</h2>
<p> if NAME indicates a choice type, VALUE must specify one of the alternatives with a null terminated string. LEN != 0. Using &quot;pkix.asn&quot;: </p>
<p> result=asn1_write_value(cert, &quot;certificate1.tbsCertificate.subject&quot;, &quot;rdnSequence&quot;, 1);</p>
<h2>ANY</h2>
<p> VALUE indicates the der encoding of a structure. LEN != 0. </p>
<p> SEQUENCE OF: VALUE must be the null terminated string &quot;NEW&quot; and LEN != 0. With this instruction another element is appended in the sequence. The name of this element will be &quot;?1&quot; if it&#8217;s the first one, &quot;?2&quot; for the second and so on. </p>
<p> Using &quot;pkix.asn&quot;: </p>
<p> result=asn1_write_value(cert, &quot;certificate1.tbsCertificate.subject.rdnSequence&quot;, &quot;NEW&quot;, 1); </p>
<p> SET OF: the same as SEQUENCE OF. Using &quot;pkix.asn&quot;: </p>
<p> result=asn1_write_value(cert, &quot;tbsCertificate.subject.rdnSequence.?LAST&quot;, &quot;NEW&quot;, 1);</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if the value was set, <code>ASN1_ELEMENT_NOT_FOUND</code> if <i>name</i> is not a valid element, and <code>ASN1_VALUE_NOT_VALID</code> if <i>ivalue</i> has a wrong format.</p>
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
