---

title: "vscnprintf(9)"
name: "vscnprintf"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vscnprintf/"
description: "vscnprintf – Format a string and place it in a buffer"
---

<p>vscnprintf &#8211; Format a string and place it in a buffer </p>

<dl>
<dt><code>int vscnprintf(char&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, const char&nbsp;<wbr>*&nbsp;<wbr></code><i>fmt</i><code>, va_list&nbsp;<wbr></code><i>args</i><code>);</code></dt>
</dl>
<h2>ARGUMENTS</h2>
<p> <i>buf</i> </p>
<dl>
<dd>  </dd>
<dd> <p> The buffer to place the result into </p>
 </dd></dl>
<p> <i>size</i> </p>
<dl>
<dd> <p> The size of the buffer, including the trailing null space </p>
 </dd></dl>
<p> <i>fmt</i> </p>
<dl>
<dd> <p> The format string to use </p>
 </dd></dl>
<p> <i>args</i> </p>
<dl>
<dd> <p> Arguments for the format string </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p>The return value is the number of characters which have been written into the <i>buf</i> not including the trailing &#8216;\0&#8217;. If <i>size</i> is == 0 the function returns 0. </p>
<p>If you&#8217;re not already dealing with a va_list consider using <code>scnprintf</code>. </p>
<p>See the <code>vsnprintf</code> documentation for format string extensions over C99.  </p>
<h2>COPYRIGHT</h2>
<p> <br/>
 </p>
