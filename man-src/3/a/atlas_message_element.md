---
title: "atlas_message_element(3)"
name: "atlas_message_element"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_message_element/"
description: "Atlas::Message::Element – Multi-type container."
---

<p>Atlas::Message::Element &#8211; Multi-type container. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Element.h">Element.h</a>&gt; </p>
<h3>Classes</h3>
<p>class <code>DataType</code> </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>TYPE_NONE</code>, <code>TYPE_INT</code>, <code>TYPE_FLOAT</code>, <code>TYPE_PTR</code>, <code>TYPE_STRING</code>, <code>TYPE_MAP</code>, <code>TYPE_LIST</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Element</code> ()<br />
 <i>Construct an empty object. </i><br />
 <code>Element</code> (const <code>Element</code> &amp;obj)<br />
 <i>Copy an existing object. </i><br />
 <code>Element</code> (int v)<br />
 <i>Set type to int, and value to v. </i><br />
 <code>Element</code> (bool v)<br />
 <i>Set type to int, and value to v. </i><br />
 <code>Element</code> (IntType v)<br />
 <i>Set type to int, and value to v. </i><br />
 <code>Element</code> (float v)<br />
 <i>Set type to double, and value to v. </i><br />
 <code>Element</code> (FloatType v)<br />
 <i>Set type to double, and value to v. </i><br />
 <code>Element</code> (PtrType v)<br />
 <i>Set type to PtrType, and value to v. </i><br />
 <code>Element</code> (const char *v)<br />
 <i>Set type to std::string, and value to v. </i><br />
 <code>Element</code> (const StringType &amp;v)<br />
 <i>Set type to std::string, and value to v. </i><br />
 <code>Element</code> (const MapType &amp;v)<br />
 <i>Set type to MapType, and value to v. </i><br />
 <code>Element</code> (const ListType &amp;v)<br />
 <i>Set type to ListType, and value to v. </i><br />
 <code>Element</code> &amp; <code>operator=</code> (const <code>Element</code> &amp;obj)<br />
 <i>overload assignment operator ! </i><br />
 <code>Element</code> &amp; <code>operator=</code> (int v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (bool v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (IntType v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (float v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (FloatType v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (PtrType v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (const char *v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (const StringType &amp;v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (const MapType &amp;v) </p>
<p> <code>Element</code> &amp; <code>operator=</code> (const ListType &amp;v) </p>
<p> bool <code>operator==</code> (const <code>Element</code> &amp;o) const<br />
 <i>Check for equality with another </i><code>Element</code>.<br />
 template&lt;class C &gt; bool <code>operator!=</code> (C c) const<br />
 <i>Check for inequality with anything we can check equality with. </i><br />
 bool <code>operator==</code> (IntType v) const<br />
 <i>Check for equality with a int. </i><br />
 bool <code>operator==</code> (FloatType v) const<br />
 <i>Check for equality with a double. </i><br />
 bool <code>operator==</code> (PtrType v) const<br />
 <i>Check for equality with a pointer. </i><br />
 bool <code>operator==</code> (const char *v) const<br />
 <i>Check for equality with a const char *. </i><br />
 bool <code>operator==</code> (const StringType &amp;v) const<br />
 <i>Check for equality with a std::string. </i><br />
 bool <code>operator==</code> (const MapType &amp;v) const<br />
 <i>Check for equality with a MapType. </i><br />
 bool <code>operator==</code> (const ListType &amp;v) const<br />
 <i>Check for equality with a ListType. </i><br />
 Type <code>getType</code> () const<br />
 <i>Get the current type. </i><br />
 bool <code>isNone</code> () const<br />
 <i>Check whether the current type is nothing. </i><br />
 bool <code>isInt</code> () const<br />
 <i>Check whether the current type is int. </i><br />
 bool <code>isFloat</code> () const<br />
 <i>Check whether the current type is double. </i><br />
 bool <code>isPtr</code> () const<br />
 <i>Check whether the current type is pointer. </i><br />
 bool <code>isNum</code> () const<br />
 <i>Check whether the current type is numeric. </i><br />
 bool <code>isString</code> () const<br />
 <i>Check whether the current type is std::string. </i><br />
 bool <code>isMap</code> () const<br />
 <i>Check whether the current type is MapType. </i><br />
 bool <code>isList</code> () const<br />
 <i>Check whether the current type is ListType. </i><br />
 IntType <code>asInt</code> () const throw (WrongTypeException)<br />
 <i>Retrieve the current value as a int. </i><br />
 IntType <code>Int</code> () const </p>
<p> FloatType <code>asFloat</code> () const throw (WrongTypeException)<br />
 <i>Retrieve the current value as a double. </i><br />
 FloatType <code>Float</code> () const </p>
<p> PtrType <code>asPtr</code> () const throw (WrongTypeException)<br />
 <i>Retrieve the current value as a pointer. </i><br />
 PtrType <code>Ptr</code> () const </p>
<p> FloatType <code>asNum</code> () const throw (WrongTypeException)<br />
 <i>Retrieve the current value as a number. </i><br />
 const std::string &amp; <code>asString</code> () const throw (WrongTypeException)<br />
 <i>Retrieve the current value as a const std::string reference. </i><br />
 std::string &amp; <code>asString</code> () throw (WrongTypeException)<br />
 <i>Retrieve the current value as a non-const std::string reference. </i><br />
 const StringType &amp; <code>String</code> () const </p>
<p> StringType &amp; <code>String</code> () </p>
<p> const MapType &amp; <code>asMap</code> () const throw (WrongTypeException)<br />
 <i>Retrieve the current value as a const MapType reference. </i><br />
 MapType &amp; <code>asMap</code> () throw (WrongTypeException)<br />
 <i>Retrieve the current value as a non-const MapType reference. </i><br />
 const MapType &amp; <code>Map</code> () const </p>
<p> MapType &amp; <code>Map</code> () </p>
<p> const ListType &amp; <code>asList</code> () const throw (WrongTypeException)<br />
 <i>Retrieve the current value as a const ListType reference. </i><br />
 ListType &amp; <code>asList</code> () throw (WrongTypeException)<br />
 <i>Retrieve the current value as a non-const ListType reference. </i><br />
 const ListType &amp; <code>List</code> () const </p>
<p> ListType &amp; <code>List</code> () </p>
<h3>Static Public Member Functions</h3>
<p>static const char * <code>typeName</code> (Type) </p>
<h3>Protected Attributes</h3>
<p>Type <code>t</code> </p>
<p> union { </p>
<p> IntType <code>i</code> </p>
<p> FloatType <code>f</code> </p>
<p> void * <code>p</code> </p>
<p> DataType&lt; StringType &gt; * <code>s</code> </p>
<p> DataType&lt; MapType &gt; * <code>m</code> </p>
<p> DataType&lt; ListType &gt; * <code>l</code> </p>
<p> }; </p>
<h2>Detailed Description</h2>
<p>Multi-type container. </p>
<p> FIXME: Document this </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Stefanus Du Toit &lt;sdt [at] gmx.net&gt;</dl>
<p> Changes: </p>
<p> 2003/04/02 Al Riddcoh &lt;alriddoch [at] zepler.org&gt; Add in some assignment operators for efficiency 2002/11/07 Al Riddcoh &lt;alriddoch [at] zepler.org&gt; Changed the name to <code>Element</code> as Object is a stupid name for a class. 2000/08/05 Karsten-O. Laux &lt;klaux [at] rhrk.uni-kl.de&gt; Changed the members to pointers which only get created when really needed. This is a major speedup for passing Object as parameter or when copying it. Because copying of unused members is omitted. All pointers are stored as a union, so we save memory ! Changed IntType to long and added convinience Constructors for float, int and bool </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
