---
title: "sc_keyvalvalue(3)"
name: "sc_keyvalvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_keyvalvalue/"
description: "sc::KeyValValue –"
---

<p>sc::KeyValValue &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::KeyValValueboolean</code>, <code>sc::KeyValValuechar</code>, <code>sc::KeyValValuedouble</code>, <code>sc::KeyValValuefloat</code>, <code>sc::KeyValValueint</code>, <code>sc::KeyValValuepchar</code>, <code>sc::KeyValValueRefDescribedClass</code>, <code>sc::KeyValValuesize</code>, <code>sc::KeyValValueString</code>, and <code>sc::KeyValValuestring</code>.</p>
<h3>Public Types</h3>
<p>enum <code>KeyValValueError</code> { <code>OK</code>, <code>WrongType</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>KeyValValue (const KeyValValue &amp;)



virtual KeyValValue::KeyValValueError doublevalue (double &amp;) const



virtual KeyValValue::KeyValValueError booleanvalue (int &amp;) const



virtual KeyValValue::KeyValValueError floatvalue (float &amp;) const



virtual KeyValValue::KeyValValueError charvalue (char &amp;) const



virtual KeyValValue::KeyValValueError intvalue (int &amp;) const



virtual KeyValValue::KeyValValueError sizevalue (size_t &amp;) const



virtual KeyValValue::KeyValValueError pcharvalue (const char *&amp;) const



virtual KeyValValue::KeyValValueError stringvalue (std::string &amp;) const



virtual KeyValValue::KeyValValueError describedclassvalue (Ref&lt; DescribedClass &gt; &amp;) const



virtual void print (std::ostream &amp;o=ExEnv::out0()) const
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
