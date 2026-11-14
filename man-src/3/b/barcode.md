---
title: "barcode(3)"
name: "barcode"
section: "3"
letter: "b"
url: "/docs/linux/man/3-barcode/"
description: "barcode – a library to create and print bar codes"
---

<h2 class="name">NAME</h2>
<p> barcode &#8211; a library to create and print bar codes </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;barcode.h&gt;</code> </p>
<p> <code>struct Barcode_Item *Barcode_Create(char *</code><i>text</i><code>);</code><br />
 <code>int Barcode_Delete(struct Barcode_Item *</code><i>bc</i><code>);</code><br />
 <code>int Barcode_Encode(struct Barcode_Item *</code><i>bc</i><code>, int </code><i>flags</i><code>);</code><br />
 <code>int Barcode_Print(struct Barcode_Item *</code><i>bc</i><code>, FILE *</code><i>f</i><code>, int </code><i>flags</i><code>);</code><br />
 <code>int Barcode_Position(struct Barcode_Item *</code><i>bc</i><code>, int </code><i>wid</i><code>, int </code><i>hei</i><code>, int </code><i>xoff</i><code>, int </code><i>yoff</i><code> , double </code><i>scalef</i><code>);</code><br />
 <code>int Barcode_Encode_and_Print(char *</code><i>text</i><code>, FILE *</code><i>f</i><code>, int </code><i>wid</i><code>, int </code><i>hei</i><code>, int </code><i>xoff</i><code>, int </code><i>yoff</i><code>, int </code><i>flags</i><code>);</code><br />
 <code>int Barcode_Version(char *</code><i>versionname</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The barcode family of library functions is meant to ease creation of bar-code printouts. The information below is extracted from the texinfo file, which is the preferred source of information. </p>
<p> The functions included in the barcode library are declared in the header file barcode.h. They perform the following tasks:</p>
<dl>
<dt>struct Barcode_Item *Barcode_Create(char *text);</p>
<dd> The function creates a new barcode object to deal with a specified text string. It returns NULL in case of failure and a pointer to a barcode data structure in case of success.</p>
<dt>int Barcode_Delete(struct Barcode_Item *bc);</p>
<dd> Destroy a barcode object. Always returns 0 (success)</p>
<dt>int Barcode_Encode(struct Barcode_Item *bc, int flags);</p>
<dd> Encode the text included in the bc object. Valid flags are the encoding type (other flags are ignored) and BARCODE_NO_CHECKSUM (other flags are silently ignored); if the flag argument is zero, bc-&gt;flags will apply. The function returns 0 on success and -1 in case of error. After successful termination the data structure will host the description of the bar code and its textual representation, after a failure the error field will include the reason of the failure.</p>
<dt>int Barcode_Print(struct Barcode_Item *bc, FILE *f, int flags);</p>
<dd> Print the bar code described by bc to the specified file. Valid flags are the output type, BARCODE_NO_ASCII and BARCODE_OUT_NOHEADERS, other flags are ignored. If any of these flags is zero, it will be inherited from bc-&gt;flags which therefore takes precedence. The function returns 0 on success and -1 in case of error (with bc-&gt;error set accordingly). In case of success, the bar code is printed to the specified file, which won&#8217;t be closed after use.</p>
<dt>int Barcode_Position(struct Barcode_Item *bc, int wid, int hei, int xoff, int yoff, double scalef);</p>
<dd> The function is a shortcut to assign values to the data structure.</p>
<dt>int Barcode_Encode_and_Print(char *text, FILE *f, int wid, int hei, int xoff, int yoff, int flags);</p>
<dd> The function deals with the whole life of the barcode object by calling the other functions; it uses all the specified flags.</p>
<dt>int Barcode_Version(char *versionname);</p>
<dd> Returns the current version as an integer number of the form major * 10000 + minor * 100 + release. Therefore, version 1.03.5 will be returned as 10305 and version 0.53 as 5300. If the argument is non-null, it will be used to return the version number as a string. Note that the same information is available from two preprocessor macros: BARCODE_VERSION (the string) and BARCODE_VERSION_INT (the integer number). </p>
</dl>
<h2>Index</h2>
