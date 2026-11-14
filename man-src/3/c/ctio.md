---
title: "ctio(3)"
name: "ctio"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctio/"
description: "ctio, ruint8, ruint16, ruint32, ruint64, wuint8, wuint16, wuint32, wuint64, rsint8, rsint16, rsint32, rsint64, wsint8, wsint16, wsint32, wsint64, rfloat, rdouble, wfloat, wdouble – integer and floa..."
---

<h2>NAME</h2>
<p> ctio, ruint8, ruint16, ruint32, ruint64, wuint8, wuint16, wuint32, wuint64, rsint8, rsint16, rsint32, rsint64, wsint8, wsint16, wsint32, wsint64, rfloat, rdouble, wfloat, wdouble &#8211; integer and float operations</p>
<h2>SYNOPSIS</h2>
<pre><code>
var mod_ctype = require('ctype');
Number mod_ctype.ruint8(Buffer buf, String endian, Number offset);
</code></pre>
<pre>
<code>Number</code> <code>mod_ctype.ruint16</code>(<code>Buffer</code> <i>buf</i>, <code>String</code> <i>endian</i>, <code>Number</code> <i>offset</i>);
</pre>
<pre>
<code>Number</code> <code>mod_ctype.ruint32</code>(<code>Buffer</code> <i>buf</i>, <code>String</code> <i>endian</i>, <code>Number</code> <i>offset</i>);
</pre>
<p>Number[2] mod_ctype.ruint64(Buffer buf, String endian, Number offset);</p>
<pre>
<code>Number</code> <code>mod_ctype.rsint8</code>(<code>Buffer</code> <i>buf</i>, <code>String</code> <i>endian</i>, <code>Number</code> <i>offset</i>);
</pre>
<pre>
<code>Number</code> <code>mod_ctype.rsint16</code>(<code>Buffer</code> <i>buf</i>, <code>String</code> <i>endian</i>, <code>Number</code> <i>offset</i>);
</pre>
<pre>
<code>Number</code> <code>mod_ctype.rsint32</code>(<code>Buffer</code> <i>buf</i>, <code>String</code> <i>endian</i>, <code>Number</code> <i>offset</i>);
</pre>
<p>Number[2] mod_ctype.rsint64(Buffer buf, String endian, Number offset);</p>
<pre>
<code>Number</code> <code>mod_ctype.rfloat</code>(<code>Buffer</code> <i>buf</i>, <code>String</code> <i>endian</i>, <code>Number</code> <i>offset</i>);
</pre>
<pre>
<code>Number</code> <code>mod_ctype.rdouble</code>(<code>Buffer</code> <i>buf</i>, <code>String</code> <i>endian</i>, <code>Number</code> <i>offset</i>);
</pre>
<p>void mod_ctype.wuint8(Number value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wuint16(Number value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wuint32(Number value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wuint64(Number[2] value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wsint8(Number value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wsint16(Number value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wsint32(Number value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wsint64(Number[2] value, String endian, Buffer buf, Number offset);</p>
<p>void mod_ctype.wfloat(Number value, String endian, Buffer buf, Number offset);</p>
<pre><code>
void mod_ctype.wdouble(Number value, String endian, Buffer buf, Number offset);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The argument <i>buf</i> refers to a valid buffer (from calling new Buffer()). The argument <i>endian</i> is either the string &#8216;big&#8217; or &#8216;little&#8217; and controls whether the data in the buffer is interpreted as big or little endian. The argument <i>offset</i> indicates the starting index into the buffer to read or write. All functions ensure that starting at <i>offset</i> does not overflow the end of the buffer. The argument <i>value</i> is a Number that is the valid type for the specific function. All functions that take <i>value</i> as an argument, verify that the passed value is valid. </p>
<h3><code>ruint8()</code>, <code>ruint16()</code>, <code>ruint32()</code></h3>
<p> The <code>ruint8()</code>, <code>ruint16()</code>, and <code>ruint32()</code> functions read an 8, 16, and 32-bit unsigned value from <i>buf</i> and return it. The value read is influenced by the values of <i>offset</i> and endian<i>. </p>
<p> </i></p>
<h3><code>rsint8()</code>, <code>rsint16()</code>, <code>rsint32()</code></h3>
<p> The <code>ruint8()</code>, <code>ruint16()</code>, and <code>ruint32()</code> functions work just as <code>ruint8()</code>, <code>ruint16()</code>, and <code>ruint32()</code>, except they return signed integers. </p>
<h3><code>ruint64()</code>, <code>rsint64()</code></h3>
<p> The <code>ruint64()</code> and <code>rsint64()</code> functions read unsigned and signed 64 bit integers respectively from <code>buf</code>. Due to the limitations of ECMAScript&#8217;s <code>Number</code> type, they cannot be stored as one value without a loss of precision. Instead of returning the values as a single <code>Number</code>, the functions return an array of two numbers. The first entry always contains the upper 32-bits and the second value contains the lower 32-bits. The lossy transformation into a number would be <i>res[0]*Math.pow(2,32)+res[1]</i>. Note that, unless an entry is zero, both array entries are guaranteed to have the same sign. </p>
<h3><code>wuint8()</code>, <code>wuint16()</code>, <code>wuint32()</code></h3>
<p> The functions <code>wuint8()</code>, <code>wuint16()</code>, and <code>wuint32()</code> modify the contents of <code>buf</code> by writing an 8, 16, and 32-bit unsigned integer respectively to <code>buf</code>. It is illegal to pass a number that is not an integer within the domain of the integer size, for example, for <code>wuint8()</code> the valid range is <code>[0, 255]</code>. The value will be written in either big or little endian format based upon the value of <code>endian</code>. </p>
<h3><code>wsint8()</code>, <code>wsint16()</code>, <code>wsint32()</code></h3>
<p> The functions <code>wsint8()</code>, <code>wsint16()</code>, and <code>wsint32()</code> function identically to the functions <code>wuint8()</code>, <code>wuint16()</code>, and <code>wuint32()</code> except that they the valid domain for <code>value</code> is that of a signed number instead of an unsigned number. For example the <code>wsint8()</code> has a domain of <code>[-128, 127]</code>. </p>
<h3><code>wuint64()</code>, <code>wsint64()</code></h3>
<p> The functions <code>wuint64()</code> and <code>swint64()</code> write out 64-bit unsigned and signed integers to <code>buf</code>. The <code>value</code> argument must be in the same format as described in <code>ruint64()</code> and <code>rsint64()</code>. </p>
<h3><code>rfloat()</code>, <code>rdouble()</code></h3>
<p> The functions &quot;<code>rfloat()</code> and <code>rdouble()</code>&quot; work like the other read functions, except that they read a single precision and double precision IEEE-754 floating point value instead. </p>
<h3><code>wfloat()</code>, <code>wdouble()</code></h3>
<p> The functions &quot;<code>rfloat()</code> and <code>rdouble()</code>&quot; work like the other write functions, except that the domain for a float is that of a single precision 4 byte value. The domain for a double is any <code>Number</code> in ECMAScript, which is defined to be represented by a double. </p>
<h2>ATTRIBUTES</h2>
<p> See <code><a href="/docs/linux/man/5-attributes/">attributes</a></code>(5) for descriptions of the following attributes: </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>ATTRIBUTE TYPE</td>
<td ALIGN=center>ATTRIBUTE VALUE
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Interface Stability</td>
<td>Committed
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>MT-Level</td>
<td>See below.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Standard</td>
<td>Not standardized.
</td>
</tr>
</table>
</table>
<p> All functions are MT-safe in so far as there aren&#8217;t shared memory MT concerns in most node programs. If one where to concoct such an environment, these functions wouldn&#8217;t be MT-safe. </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
<dt><a href="#lbAM">ATTRIBUTES</a></p>
<dd>
<dt><a href="#lbAN">SEE ALSO</a></p>
<dd></dl>
