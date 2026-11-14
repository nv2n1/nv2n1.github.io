---
title: "stdfloat_denorm_style(3)"
name: "stdfloat_denorm_style"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfloat_denorm_style/"
description: "std::float_denorm_style – std::float_denorm_style"
---

<p>std::float_denorm_style &#8211; std::float_denorm_style</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;limits&gt;

enum float_denorm_style {

    denorm_indeterminate = -1,

    denorm_absent = 0,

    denorm_present = 1

};</code></pre>
<p>Enumeration constants of type std::float_denorm_style indicate support of subnormal values by floating-point types.<br />
Enumeration constants<br />
Name Definition<br />
std::denorm_indeterminate Support of subnormal values cannot be determined<br />
std::denorm_absent The type does not support subnormal values<br />
std::denorm_present The type allows subnormal values </p>
<h2>See also</h2>
<p>has_denorm identifies the denormalization style used by the floating-point type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
