---
title: "fcvalueequal(3)"
name: "fcvalueequal"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcvalueequal/"
description: "FcValueEqual – Test two values for equality"
---

<p>FcValueEqual &#8211; Test two values for equality </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcValueEqual (FcValue </code><i>v_a</i><code>, FcValue </code><i>v_b</i><code>); </code></p>
<h2>Description</h2>
<p>Compares two values. Integers and Doubles are compared as numbers; otherwise the two values have to be the same type to be considered equal. Strings are compared ignoring case.</p>
