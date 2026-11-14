---
title: "mime(5)"
name: "mime"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mime/"
---

mime.types - mime type description file for cups

<h2>Description</h2>

The <i>mime.types</i> file defines the recognized file types. 

 Additional file types can be added to <i>mime.types</i> or (preferably) in additional files in the CUPS configuration directory with the extension &quot;.types&quot;. 

 Each line in the <i>mime.types</i> file is a comment, blank, or rule line. Comment lines start with the # character. Rule lines start with the MIME type name and are optionally followed by a series of file recognition rules that are used to automatically identify print and web files: 
 <pre> super/type rule [ ... ruleN]</pre>MIME type names are case-insensitive and are sorted in ascending alphanumeric order for the purposes of matching. See the &quot;TYPE MATCHING AND PRIORITY&quot; section for more information. 

 The rules may be grouped using parenthesis, joined using &quot;+&quot; for a logical AND and &quot;,&quot; or whitespace for a logical OR, and negated using &quot;!&quot;.

<h2>Rules</h2>

Rules take two forms - a filename extension by itself and functions with test values inside parenthesis. The following functions are available:
<dl><dt>match(&quot;pattern&quot;)
<dd>Pattern match on filename
<dt>ascii(offset,length)
<dd>True if bytes are valid printable ASCII (CR, NL, TAB, BS, 32-126)
<dt>printable(offset,length)
<dd>True if bytes are printable 8-bit chars (CR, NL, TAB, BS, 32-126, 128-254)
<dt>priority(number)
<dd>Specifies the relative priority of this MIME type. The default priority is 100. Larger values have higher priority while smaller values have lower priority.
<dt>string(offset,&quot;string&quot;)
<dd>True if bytes are identical to string
<dt>istring(offset,&quot;string&quot;)
<dd>True if a case-insensitive comparison of the bytes is identical
<dt>char(offset,value)
<dd>True if byte is identical
<dt>short(offset,value)
<dd>True if 16-bit integer is identical
<dt>int(offset,value)
<dd>True if 32-bit integer is identical
<dt>locale(&quot;string&quot;)
<dd>True if current locale matches string
<dt>contains(offset,range,&quot;string&quot;)
<dd>True if the range contains the string</dl>

<h2>String Constants</h2>

String constants can be specified inside quotes (&quot;&quot;) for strings containing whitespace and angle brackets (&lt;&gt;) for hexadecimal strings.

<h2>Type Matching And Priority</h2>

When CUPS needs to determine the MIME type of a given file, it checks every MIME type defined in the .types files. When two types have the same matching rules, the type chosen will depend on the type name and priority, with higher- priority types being used over lower-priority ones. If the types have the same priority, the type names are sorted alphanumerically in ascending order and the first type is chosen. 

 For example, if two types &quot;text/bar&quot; and &quot;text/foo&quot; are defined as matching the extension &quot;doc&quot;, normally the type &quot;text/bar&quot; will be chosen since its name is alphanumerically smaller than &quot;text/foo&quot;. However, if &quot;text/foo&quot; also defines a higher priority than &quot;text/bar&quot;, &quot;text/foo&quot; will be chosen instead.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-classes-conf/">classes.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a HREF="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-convs/">mime.convs</a>(5)</i>, <i><a HREF="/docs/linux/man/5-printers-conf/">printers.conf</a>(5)</i>, 
 <a rel="nofollow" HREF="http://localhost:631/help">http://localhost:631/help</a>

<h2>Copyright</h2>

Copyright 2007-2013 by Apple Inc.
