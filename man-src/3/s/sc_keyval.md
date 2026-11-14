---
title: "sc_keyval(3)"
name: "sc_keyval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_keyval/"
description: "sc::KeyVal –"
---

<p>sc::KeyVal &#8211; </p>
<p> The <code>KeyVal</code> class is designed to simplify the process of allowing a user to specify keyword/value associations to a C++ program.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;keyval.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::AggregateKeyVal</code>, <code>sc::AssignedKeyVal</code>, <code>sc::PrefixKeyVal</code>, and <code>sc::StringKeyVal</code>.</p>
<h3>Public Types</h3>
<p>enum { MaxKeywordLength =  256 }</p>
<p>enum KeyValError { OK, HasNoValue, WrongType, UnknownKeyword, OperationFailed }</p>
<p>Public Member Functions<br />
 int <code>exists</code> (const char *)<br />
 <i>This takes as its only argument a keyword. </i><br />
 int <code>count</code> (const char *=0)<br />
 <i>If the value of a keyword is an array, then return its length. </i><br />
 <code>Ref</code>&lt; <code>KeyValValue</code> &gt; <code>value</code> (const char *=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValue</code>())<br />
 <i>Return the value associated with the keyword. </i><br />
 int <code>booleanvalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValueboolean</code>())<br />
 <i>Returns the boolean value (0 = false, 1 = true) of key. </i><br />
 double <code>doublevalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValuedouble</code>())<br />
 <i>Returns the double value of key. </i><br />
 float <code>floatvalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValuefloat</code>())<br />
 <i>Returns the float value of key. </i><br />
 char <code>charvalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValuechar</code>())<br />
 <i>Returns the char value of key. </i><br />
 int <code>intvalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValueint</code>())<br />
 <i>Returns the int value of key. </i><br />
 size_t <code>sizevalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValuesize</code>())<br />
 <i>Returns the size_t value of key. </i><br />
 char * <code>pcharvalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValuepchar</code>())<br />
 <i>Returns a copy of the string representation of the key&#8217;s value. </i><br />
 std::string <code>stringvalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValuestring</code>())<br />
 <i>Returns a string representation of the key&#8217;s value. </i><br />
 <code>Ref</code>&lt; <code>DescribedClass</code> &gt; <code>describedclassvalue</code> (const char *key=0, const <code>KeyValValue</code> &amp;def=<code>KeyValValueRefDescribedClass</code>())<br />
 <i>Returns a reference to an object of type </i><code>DescribedClass</code>.<br />
 KeyValError <code>error</code> ()<br />
 <i>Return the current error condition. </i><br />
 const char * <code>errormsg</code> (KeyValError err)<br />
 <i>Return a textual representation of err. </i><br />
 const char * <code>errormsg</code> ()<br />
 <i>Return a textual representation of the current error. </i><br />
 virtual void <code>errortrace</code> (std::ostream &amp;fp=ExEnv::err0())<br />
 <i>Write a message to fp describing the error. </i><br />
 virtual void <code>dump</code> (std::ostream &amp;fp=ExEnv::err0())<br />
 <i>Write a message to fp describing the error. </i><br />
 virtual void <code>print_unseen</code> (std::ostream &amp;fp=ExEnv::out0())<br />
 <i>Print keywords that were never looked at, if possible. </i><br />
 virtual int <code>have_unseen</code> ()<br />
 <i>Return 1 if there were unseen keywords, 0 if there are none, or -1 this keyval doesn&#8217;t keep track of unseen keywords. </i><br />
 void <code>verbose</code> (int v)<br />
 <i>Control printing of assignments. </i><br />
 int <code>verbose</code> () const<br />
 <i>Returns nonzero if assignments are printed. </i> <code>Reading Vectors.</code><br />
 These members correspond to the above members, but take an additional integer argument, i, which is a vector index. This is equivalent to getting a value for a keyword named &#8216;&lt;i&gt;key&lt;/i&gt;:&lt;i&gt;i&lt;/i&gt;&#8217;. The routines that do not take key arguments get the value for the keyword named &#8216;&lt;i&gt;i&lt;/i&gt;&#8217;. int exists (const char *key, int i)</p>
<p>int count (const char *key, int i)</p>
<p>int booleanvalue (const char *key, int i, const KeyValValue &amp;def=KeyValValueboolean())</p>
<p>double doublevalue (const char *key, int i, const KeyValValue &amp;def=KeyValValuedouble())</p>
<p>float floatvalue (const char *key, int i, const KeyValValue &amp;def=KeyValValuefloat())</p>
<p>char charvalue (const char *key, int i, const KeyValValue &amp;def=KeyValValuechar())</p>
<p>int intvalue (const char *key, int i, const KeyValValue &amp;def=KeyValValueint())</p>
<p>size_t sizevalue (const char *key, int i, const KeyValValue &amp;def=KeyValValuesize())</p>
<p>char * pcharvalue (const char *key, int i, const KeyValValue &amp;def=KeyValValuepchar())</p>
<p>std::string stringvalue (const char *key, int i, const KeyValValue &amp;def=KeyValValuestring())</p>
<p>Ref&lt; DescribedClass &gt; describedclassvalue (const char *key, int, const KeyValValue &amp;def=KeyValValueRefDescribedClass())</p>
<p>int exists (int i)</p>
<p>int count (int i)</p>
<p>int booleanvalue (int i, const KeyValValue &amp;def=KeyValValueboolean())</p>
<p>double doublevalue (int i, const KeyValValue &amp;def=KeyValValuedouble())</p>
<p>float floatvalue (int i, const KeyValValue &amp;def=KeyValValuefloat())</p>
<p>char charvalue (int i, const KeyValValue &amp;def=KeyValValuechar())</p>
<p>int intvalue (int i, const KeyValValue &amp;def=KeyValValueint())</p>
<p>size_t sizevalue (int i, const KeyValValue &amp;def=KeyValValuesize())</p>
<p>char * pcharvalue (int i, const KeyValValue &amp;def=KeyValValuepchar())</p>
<p>std::string stringvalue (int i, const KeyValValue &amp;def=KeyValValuestring())</p>
<p>Ref&lt; DescribedClass &gt; describedclassvalue (int i, const KeyValValue &amp;def=KeyValValueRefDescribedClass()) <code>Reading 2D Arrays.</code><br />
 These members correspond to the above members, but take additional integer arguments, i and j, which is an array index. This is equivalent to getting a value for a keyword named &#8216;&lt;i&gt;key&lt;/i&gt;:&lt;i&gt;i&lt;/i&gt;:&lt;i&gt;j&lt;/i&gt;&#8217;. The routines that do not take key arguments get the value for the keyword named &#8216;&lt;i&gt;i&lt;/i&gt;:&lt;i&gt;j&lt;/i&gt;&#8217;. int exists (const char *, int, int)</p>
<p>int count (const char *, int, int)</p>
<p>int booleanvalue (const char *, int, int, const KeyValValue &amp;def=KeyValValueboolean())</p>
<p>double doublevalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValuedouble())</p>
<p>float floatvalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValuefloat())</p>
<p>char charvalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValuechar())</p>
<p>int intvalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValueint())</p>
<p>size_t sizevalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValuesize())</p>
<p>char * pcharvalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValuepchar())</p>
<p>std::string stringvalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValuestring())</p>
<p>Ref&lt; DescribedClass &gt; describedclassvalue (const char *key, int, int, const KeyValValue &amp;def=KeyValValueRefDescribedClass())</p>
<p>int exists (int i, int j)</p>
<p>int count (int i, int j)</p>
<p>int booleanvalue (int i, int j, const KeyValValue &amp;def=KeyValValueboolean())</p>
<p>double doublevalue (int i, int j, const KeyValValue &amp;def=KeyValValuedouble())</p>
<p>float floatvalue (int i, int j, const KeyValValue &amp;def=KeyValValuefloat())</p>
<p>char charvalue (int i, int j, const KeyValValue &amp;def=KeyValValuechar())</p>
<p>int intvalue (int i, int j, const KeyValValue &amp;def=KeyValValueint())</p>
<p>size_t sizevalue (int i, int j, const KeyValValue &amp;def=KeyValValuesize())</p>
<p>char * pcharvalue (int i, int j, const KeyValValue &amp;def=KeyValValuepchar())</p>
<p>std::string stringvalue (int i, int j, const KeyValValue &amp;def=KeyValValuestring())</p>
<p>Ref&lt; DescribedClass &gt; describedclassvalue (int i, int j, const KeyValValue &amp;def=KeyValValueRefDescribedClass()) <code>Reading 3D Arrays.</code><br />
 These members correspond to the above members, but can be used to read in arrays with more than two dimensions. The nindex argument is the number of indices in the array. It is followed by an int giving the value of each index. </p>
<pre><code>int Va_exists (const char *key, int nindex,...)



int Va_count (const char *key, int nindex,...)



int Va_booleanvalue (const char *key, int nindex,...)



double Va_doublevalue (const char *key, int nindex,...)



float Va_floatvalue (const char *key, int nindex,...)



char Va_charvalue (const char *key, int nindex,...)



int Va_intvalue (const char *key, int nindex,...)



size_t Va_sizevalue (const char *key, int nindex,...)



char * Va_pcharvalue (const char *key, int nindex,...)



std::string Va_stringvalue (const char *key, int nindex,...)



Ref&lt; DescribedClass &gt; Va_describedclassvalue (const char *key, int nindex,...)



Protected Member Functions
void seterror (KeyValError err)


Set the current error condition.


void seterror (KeyValValue::KeyValValueError err)


Set the current error condition.


virtual int key_exists (const char *)=0


Ultimately called by exists.


virtual int key_count (const char *=0)


Ultimately called by count.


virtual Ref&lt; KeyValValue &gt; key_value (const char *, const KeyValValue &amp;def)=0


Ultimately called by value.


virtual int key_booleanvalue (const char *, const KeyValValue &amp;def)


Ultimately called by booleanvalue.


virtual double key_doublevalue (const char *key, const KeyValValue &amp;def)


Ultimately called by doublevalue.


virtual float key_floatvalue (const char *key, const KeyValValue &amp;def)


Ultimately called by floatvalue.


virtual char key_charvalue (const char *key, const KeyValValue &amp;def)


Ultimately called by charvalue.


virtual int key_intvalue (const char *key, const KeyValValue &amp;def)


Ultimately called by intvalue.


virtual size_t key_sizevalue (const char *key, const KeyValValue &amp;def)


Ultimately called by sizevalue.


virtual char * key_pcharvalue (const char *key, const KeyValValue &amp;def)


Ultimately called by pcharvalue.


virtual std::string key_stringvalue (const char *key, const KeyValValue &amp;def)


Ultimately called by stringvalue.


virtual Ref&lt; DescribedClass &gt; key_describedclassvalue (const char *key, const KeyValValue &amp;def)


Ultimately called by describedclassvalue.



Protected Attributes
int verbose_



Friends</code></pre>
<p> class <code>AggregateKeyVal</code> </p>
<p> class <code>PrefixKeyVal</code></p>
<h2>Detailed Description</h2>
<p>The <code>KeyVal</code> class is designed to simplify the process of allowing a user to specify keyword/value associations to a C++ program. </p>
<p> A flexible input style and ease of use for the programmer is achieved with this method. Keywords are represented by null terminated character arrays. The keywords are organized hierarchially, in a manner similar to the way that many file systems are organized. One character is special, &#8216;:&#8217;, which is used to separate the various hierarchial labels, which are referred to as &#8216;segments&#8217;, in the keyword. </p>
<p> A convention for specifying arrays is provided by <code>KeyVal</code>. Each index of the array is given by appending a segment containing the character representation of the index. Thus, &#8216;array:3:4&#8217; would be a the keyword corresponding to fourth row and fifth column of &#8216;array&#8217;, since indexing starts at zero. </p>
<p> To allow the <code>KeyVal</code> class to have associations that can represent data for classes, the keyword can be associated with a class as well as a value. This permits polymorphic data to be unambiguously represented by keyword/value associations. Most use of <code>KeyVal</code> need not be concerned with this.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::KeyVal::count (const char * = 0)</h3>
<p>If the value of a keyword is an array, then return its length. If no arguments are given then the top level will be checked to see if it is an array and, if so, the number of elements will be counted.</p>
<h3>int sc::KeyVal::exists (const char *)</h3>
<p>This takes as its only argument a keyword. Returns 1 if the keyword has a value and 0 otherwise.</p>
<h3>virtual int sc::KeyVal::have_unseen () [virtual]</h3>
<p>Return 1 if there were unseen keywords, 0 if there are none, or -1 this keyval doesn&#8217;t keep track of unseen keywords. </p>
<p> Reimplemented in <code>sc::ParsedKeyVal</code>.</p>
<h3>char* sc::KeyVal::pcharvalue (const char * key = 0, const <code>KeyValValue</code> &amp; def = <code>KeyValValuepchar</code>())</h3>
<p>Returns a copy of the string representation of the key&#8217;s value. Storage for the copy is obtained with new.</p>
<h3>std::string sc::KeyVal::stringvalue (const char * key = 0, const <code>KeyValValue</code> &amp; def = <code>KeyValValuestring</code>())</h3>
<p>Returns a string representation of the key&#8217;s value.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
