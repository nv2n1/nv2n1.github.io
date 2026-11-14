---
title: "xmreptypevalidvalue(3)"
name: "xmreptypevalidvalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmreptypevalidvalue/"
description: "XmRepTypeValidValue — A representation type manager function that tests the validity of a numerical value of a representation type resource"
---

<p><code>XmRepTypeValidValue</code> &#8212; A representation type manager function that tests the validity of a numerical value of a representation type resource</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RepType.h&gt;
<code>Boolean XmRepTypeValidValue</code>(
<code>XmRepTypeId rep_type_id</code>,
<code>unsigned char test_value</code>,
<code>Widget enable_default_warning</code>);</pre>
<h2>Description</h2>
<p><code>XmRepTypeValidValue</code> tests the validity of a numerical value for a given representation type resource. The function generates a default warning message if the value is invalid and the <i>enable_default_warning</i> argument is non-NULL.</p>
<dl COMPACT>
<dt><i>rep_type_id</i></p>
<dd>Specifies the identification number of the representation type.</p>
<dt><i>test_value</i></p>
<dd>Specifies the numerical value to test.</p>
<dt><i>enable_default_warning</i></p>
<dd>Specifies the ID of the widget that contains a default warning message. If this parameter is NULL, no default warning message is generated and the application must provide its own error handling.</dl>
<h2>Return</h2>
<p>Returns True if the specified value is valid; otherwise, returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmreptypegetid/">XmRepTypeGetId</a></code>(3) and <code><a href="/docs/linux/man/3-xmreptyperegister/">XmRepTypeRegister</a></code>(3).</p>
