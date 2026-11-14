---
title: "sc_parsedkeyval(3)"
name: "sc_parsedkeyval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_parsedkeyval/"
description: "sc::ParsedKeyVal –"
---

<p>sc::ParsedKeyVal &#8211; </p>
<p> Converts textual information into keyword/value assocations.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;keyval.h&gt;</code></pre>
<p> Inherits <code>sc::StringKeyVal</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ParsedKeyVal</code> ()<br />
 <i>Create an empty </i><code>ParsedKeyVal</code>.<br />
 <code>ParsedKeyVal</code> (const char *file)<br />
 <i>Parse the given input file. </i><br />
 <code>ParsedKeyVal</code> (std::istream &amp;s)<br />
 <i>Read input from s. </i><br />
 <code>ParsedKeyVal</code> (<code>IPV2</code> *)<br />
 <i>Use the given IPV2* object. </i><br />
 <code>ParsedKeyVal</code> (const char *, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>This ctor is given a string which is used to form keywords that are sought in the keyval argument. </i><br />
 <code>~ParsedKeyVal</code> ()<br />
 <i>Cleanup, deleting the </i><code>IPV2</code> object.<br />
 void <code>read</code> (const char *)<br />
 <i>Read input data from the given filename. </i><br />
 void <code>read</code> (std::istream &amp;)<br />
 <i>Read input data from the given stream. </i><br />
 void <code>parse_string</code> (const char *)<br />
 <i>Read input data from the given string. </i> <code>Overrides of parent members.</code><br />
 See parent class documentation. </p>
<pre><code>const char * stringrep (const char *)


Returns the string representation of the value assigned to key.


const char * classname (const char *)


Returns the name of the exact class of the object at the keyword.


const char * truekeyword (const char *)


Returns a string which is the actual keyword if some sort of variable substitution takes place (needed to make multiple references to the same object work in input files).


void errortrace (std::ostream &amp;fp=ExEnv::err0())


Write a message to fp describing the error.


void dump (std::ostream &amp;fp=ExEnv::err0())


Write a message to fp describing the error.


void print_unseen (std::ostream &amp;fp=ExEnv::out0())


Print keywords that were never looked at, if possible.


int have_unseen ()


Return 1 if there were unseen keywords, 0 if there are none, or -1 this keyval doesn't keep track of unseen keywords.




Static Public Member Functions</code></pre>
<p> static void <code>cat_files</code> (const char *, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, std::ostream &amp;o)<br />
 <i>This is like the </i><code>ParsedKeyVal(const char*,const Ref&lt;KeyVal&gt;&amp;)</code> ctor, but writes the contents of the files to the given ostream.</p>
<h2>Detailed Description</h2>
<p>Converts textual information into keyword/value assocations. </p>
<p> The parsing is done with an <code>IPV2</code> object. The <code>keyval</code> for more information on the input format.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::ParsedKeyVal::ParsedKeyVal (<code>IPV2</code> *)</h3>
<p>Use the given IPV2* object. The new <code>ParsedKeyVal</code> takes wnership of the passed <code>IPV2</code> object.</p>
<h3>sc::ParsedKeyVal::ParsedKeyVal (const char *, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>This ctor is given a string which is used to form keywords that are sought in the keyval argument. The associated values are used to construct file names that are used to initialize the <code>ParsedKeyVal</code>. The keywords sought are string&#8217;dir&#8217; for the directory prefix and string&#8217;files&#8217; for an array of file names.</p>
<h2>Member Function Documentation</h2>
<h3>static void sc::ParsedKeyVal::cat_files (const char *, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, std::ostream &amp; o) [static]</h3>
<p>This is like the <code>ParsedKeyVal(const char*,const Ref&lt;KeyVal&gt;&amp;)</code> ctor, but writes the contents of the files to the given ostream.</p>
<h3>const char* sc::ParsedKeyVal::classname (const char *) [virtual]</h3>
<p>Returns the name of the exact class of the object at the keyword. If no classname is assigned then 0 is returned. </p>
<p> Reimplemented from <code>sc::StringKeyVal</code>.</p>
<h3>int sc::ParsedKeyVal::have_unseen () [virtual]</h3>
<p>Return 1 if there were unseen keywords, 0 if there are none, or -1 this keyval doesn&#8217;t keep track of unseen keywords. </p>
<p> Reimplemented from <code>sc::KeyVal</code>.</p>
<h3>const char* sc::ParsedKeyVal::truekeyword (const char *) [virtual]</h3>
<p>Returns a string which is the actual keyword if some sort of variable substitution takes place (needed to make multiple references to the same object work in input files). </p>
<p> Reimplemented from <code>sc::StringKeyVal</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
