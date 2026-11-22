---

title: "asn1_print_structure(3)"
name: "asn1_print_structure"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_print_structure/"
description: "asn1_print_structure – API function"
---

<p> asn1_print_structure &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>void asn1_print_structure(FILE * </code><i>out</i><code>, asn1_node </code><i>structure</i><code>, const char * </code><i>name</i><code>, int </code><i>mode</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>FILE * out</dt>
<dd> pointer to the output file (e.g. stdout).</dd>
<dt>asn1_node structure</dt>
<dd> pointer to the structure that you want to visit.</dd>
<dt>const char * name</dt>
<dd> an element of the structure</dd>
<dt>int mode</dt>
<dd> specify how much of the structure to print, can be <code>ASN1_PRINT_NAME</code>, <code>ASN1_PRINT_NAME_TYPE</code>, <code>ASN1_PRINT_NAME_TYPE_VALUE</code>, or <code>ASN1_PRINT_ALL</code>.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Prints on the <i>out</i> file descriptor the structure&#8217;s tree starting from the <i>name</i> element inside the structure <i>structure</i> .</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2015 Free Software Foundation, Inc..<br/>
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libtasn1</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtasn1</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info libtasn1</code></dd></dl>
<p> should give you access to the complete manual. As an alternative you may obtain the manual from:</p>
<dl>
<dt>
</dt><dd> <code><a rel="nofollow" href="http://www.gnu.org/software/libtasn1/manual/">http://www.gnu.org/software/libtasn1/manual/</a></code></dd></dl>
