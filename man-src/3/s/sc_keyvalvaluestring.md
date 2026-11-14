---
title: "sc_keyvalvaluestring(3)"
name: "sc_keyvalvaluestring"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_keyvalvaluestring/"
description: "sc::KeyValValueString –"
---

<p>sc::KeyValValueString &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::KeyValValue</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Storage</code> { <code>Copy</code>, <code>Steal</code>, <code>Use</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>KeyValValueString (const char *, KeyValValueString::Storage s=KeyValValueString::Use)



KeyValValueString (char *, KeyValValueString::Storage s=KeyValValueString::Use)



KeyValValueString (const KeyValValueString &amp;)



KeyValValue::KeyValValueError doublevalue (double &amp;) const



KeyValValue::KeyValValueError booleanvalue (int &amp;) const



KeyValValue::KeyValValueError floatvalue (float &amp;) const



KeyValValue::KeyValValueError charvalue (char &amp;) const



KeyValValue::KeyValValueError intvalue (int &amp;) const



KeyValValue::KeyValValueError sizevalue (size_t &amp;) const



KeyValValue::KeyValValueError pcharvalue (const char *&amp;) const



KeyValValue::KeyValValueError stringvalue (std::string &amp;) const



void print (std::ostream &amp;o=ExEnv::out0()) const
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
