---
title: "rlm_expr(5)"
name: "rlm_expr"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_expr/"
description: "rlm_expr – FreeRADIUS Module"
---

<p>rlm_expr &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_expr</i> module allows the server to perform limited mathematical calculations. This module is not called directly in any section, it is invoked through the dynamic expansion of strings. For example, some NAS boxes send a NAS-Port attribute which is a 32-bit number composed of port, card, and interface, all in different bytes. To see these attributes split into pieces, you can have an entry in the &#8216;users&#8217; file like:</p>
<dl>
<dd>
<pre>DEFAULT
<br>
 Vendor-Interface = `%{expr: %{NAS-Port} / (256 * 256)}`,
<br>
 Vendor-Card = `%{expr: (%{NAS-Port} / 256) %% 256}`,
<br>
 Vendor-Port = `%{expr: %{NAS-Port} %% 256}`
<br></pre>
</dl>
<p> where the attributes Vendor-Interface, Vendor-Card, and Vendor-Port are attributes created by either you or a vendor-supplied dictionary. The methematical operators supported by the expression module are:</p>
<dl>
<dt><code>+</code></p>
<dd>addition</p>
<dt><code>&#8211;</code></p>
<dd>subtraction</p>
<dt><code>/</code></p>
<dd>division</p>
<dt><code>%%</code></p>
<dd>modulo remainder</p>
<dt><code>*</code></p>
<dd>multiplication</p>
<dt><code>&amp;</code></p>
<dd>boolean AND</p>
<dt><code>|</code></p>
<dd>boolean OR</p>
<dt><code>()</code></p>
<dd>grouping of sub-expressions</dl>
<p> NOTE: The modulo remainder operator is &#8216;%%&#8217;, and not &#8216;%&#8217;. This is due to the &#8216;%&#8217; character being used as a special character for dynamic translation. NOTE: These operators do NOT have precedence. The parsing of the input string, and the calculation of the answer, is done strictly left to right. If you wish to order the expressions, you MUST group them into sub-expression, as shown in the previous example. All of the calculations are performed as unsigned 32-bit integers. </p>
<h2>Configuration</h2>
<dl>
<dd>
<pre>modules {
 ...
<br>
 expr {
<br>
 }
<br>
 ...
<br>
}
<br>
 ...
<br>
instantiate {
 ...
<br>
 expr
 ...
<br>
}
</dl></pre>
<h2>Sections</h2>
<p><code>instantiate</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
