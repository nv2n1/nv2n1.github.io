---
title: "sc_stringkeyval(3)"
name: "sc_stringkeyval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stringkeyval/"
description: "sc::StringKeyVal –"
---

<p>sc::StringKeyVal &#8211; </p>
<p> <code>StringKeyVal</code> is a base class for <code>KeyVal</code> implementations that store all values in a string format.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;keyval.h&gt;</code></pre>
<p> Inherits <code>sc::KeyVal</code>. Inherited by <code>sc::ParsedKeyVal</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual const char * stringrep (const char *key)=0</p>
<p>Returns the string representation of the value assigned to key.</p>
<p>virtual const char * classname (const char *)</p>
<p>Returns the name of the exact class of the object at the keyword.</p>
<p>virtual const char * truekeyword (const char *)</p>
<p>Returns a string which is the actual keyword if some sort of variable substitution takes place (needed to make multiple references to the same object work in input files). <code>Debugging.</code><br />
 See the parent class documentation for descriptions of these functions. </p>
<pre><code>virtual void errortrace (std::ostream &amp;fp=ExEnv::err0())


Write a message to fp describing the error.


virtual void dump (std::ostream &amp;fp=ExEnv::err0())


Write a message to fp describing the error.




Protected Member Functions</code></pre>
<p> int <code>key_exists</code> (const char *)<br />
 <i>Ultimately called by exists. </i><br />
 <code>Ref</code>&lt; <code>KeyValValue</code> &gt; <code>key_value</code> (const char *, const <code>KeyValValue</code> &amp;def)<br />
 <i>Ultimately called by value. </i></p>
<h2>Detailed Description</h2>
<p><code>StringKeyVal</code> is a base class for <code>KeyVal</code> implementations that store all values in a string format. </p>
<p> These are converted to other data types through <code>KeyValValue</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual const char* sc::StringKeyVal::classname (const char *) [virtual]</h3>
<p>Returns the name of the exact class of the object at the keyword. If no classname is assigned then 0 is returned. </p>
<p> Reimplemented in <code>sc::ParsedKeyVal</code>.</p>
<h3>virtual const char* sc::StringKeyVal::truekeyword (const char *) [virtual]</h3>
<p>Returns a string which is the actual keyword if some sort of variable substitution takes place (needed to make multiple references to the same object work in input files). </p>
<p> Reimplemented in <code>sc::ParsedKeyVal</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
