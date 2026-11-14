---
title: "xtappaddactions(3)"
name: "xtappaddactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappaddactions/"
description: "XtAppAddActions – register an action table"
---

<p>XtAppAddActions &#8211; register an action table </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppAddActions(XtAppContext <i>app_context</i>, XtActionList <i>actions</i>, Cardinal <i>num_actions</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>actions</i></p>
<dd>Specifies the action table to register.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of entries in this action table.</dl>
<h2>Description</h2>
<p>The <code>XtAppAddActions</code> function adds the specified action table and registers it with the translation manager.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtparsetranslationtable/">XtParseTranslationTable</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
