---
title: "packet-utils(3)"
name: "packet-utils"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-utils/"
description: "packet.utils – Pktt utilities module"
---

<p>packet.utils &#8211; Pktt utilities module</p>
<h2>Description</h2>
<p>The Packet trace utilities module has classes which augment functionality of basic data types like displaying integers as their hex equivalent. It also includes an Enum base class which displays the integer as its string representation given by a mapping dictionary. There is also a class to be used as a base class for an RPC payload object. This module also includes some module variables to change how certain objects are displayed.</p>
<h2>Classes</h2>
<h3>class BitmapInval(exceptions.Exception)</h3>
<pre>Exception for an invalid bit number</pre>
<h3>class Enum(__builtin__.int)</h3>
<pre>Enum base object
This should only be used as a base class where the class attributes
should be initialized
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code>
Informal string representation, display value using the mapping
dictionary provided as a class attribute
<code>Static methods defined here:</code>
----------------------------
<code>__new__(cls, unpack)</code>
Constructor which checks if integer is a valid enum value</pre>
<h3>class EnumInval(exceptions.Exception)</h3>
<pre>Exception for an invalid enum value</pre>
<h3>class IntHex(__builtin__.int)</h3>
<pre>Integer object which is displayed in hex
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code></pre>
<h3>class LongHex(__builtin__.long)</h3>
<pre>Long integer object which is displayed in hex
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code></pre>
<h3>class RPCload(baseobj.BaseObj)</h3>
<pre>RPC load base object
This is used as a base class for an RPC payload object
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code>
Informal string representation
<code>rpc_str(self, name=None)</code>
Display RPC string</pre>
<h3>class StrHex(__builtin__.str)</h3>
<pre>String object which is displayed in hex
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code></pre>
<h2>Functions</h2>
<h3>bitmap_dict(unpack, bitmap, func_map, name_map=None)</h3>
<p>Returns a dictionary where the key is the bit number given by bitmap and the value is the decoded value by evaluating the function used for that specific bit number </p>
<dl>
<dd>
<dl>
<dt><code>unpack:</code></p>
<dd>Unpack object</p>
<dt><code>bitmap:</code></p>
<dd>Unsigned integer where a value must be decoded for every bit that is set, starting from the least significant bit</p>
<dt><code>func_map:</code></p>
<dd>Dictionary which maps a bit number to the function to be used for decoding the value for that bit number. The function must have the &quot;unpack&quot; object as the only argument</p>
<dt><code>name_map:</code></p>
<dd>Dictionary which maps a bit number to a bit name. If this is given the resulting dictionary will have a bit name for a key instead of the bit number</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
