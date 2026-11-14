---
title: "perl592delta(1)"
name: "perl592delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl592delta/"
description: "perl592delta – what is new for perl v5.9.2"
---

<h2 class="name">NAME</h2>
<p> perl592delta &#8211; what is new for perl v5.9.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.9.1 and the 5.9.2 development releases. See perl590delta and perl591delta for the differences between 5.8.0 and 5.9.1.</p>
<h2>Incompatible Changes</h2>
<h3>Packing and <font SIZE="-1">UTF-8</font> strings</h3>
<p> The semantics of <i>pack()</i> and <i>unpack()</i> regarding UTF-8-encoded data has been changed. Processing is now by default character per character instead of byte per byte on the underlying encoding. Notably, code that used things like <tt>&quot;pack(&quot;a*&quot;, $string)&quot;</tt> to see through the encoding of string will now simply get back the original <tt>$string</tt>. Packed strings can also get upgraded during processing when you store upgraded characters. You can get the old behaviour by using <tt>&quot;use bytes&quot;</tt>. </p>
<p> To be consistent with <i>pack()</i>, the <tt>&quot;C0&quot;</tt> in <i>unpack()</i> templates indicates that the data is to be processed in character mode, i.e. character by character; on the contrary, <tt>&quot;U0&quot;</tt> in <i>unpack()</i> indicates <font SIZE="-1">UTF-8</font> mode, where the packed string is processed in its UTF-8-encoded Unicode form on a byte by byte basis. This is reversed with regard to perl 5.8.X. </p>
<p> Moreover, <tt>&quot;C0&quot;</tt> and <tt>&quot;U0&quot;</tt> can also be used in <i>pack()</i> templates to specify respectively character and byte modes. </p>
<p> <tt>&quot;C0&quot;</tt> and <tt>&quot;U0&quot;</tt> in the middle of a pack or unpack format now switch to the specified encoding mode, honoring parens grouping. Previously, parens were ignored. </p>
<p> Also, there is a new <i>pack()</i> character format, <tt>&quot;W&quot;</tt>, which is intended to replace the old <tt>&quot;C&quot;</tt>. <tt>&quot;C&quot;</tt> is kept for unsigned chars coded as bytes in the strings internal representation. <tt>&quot;W&quot;</tt> represents unsigned (logical) character values, which can be greater than 255. It is therefore more robust when dealing with potentially UTF-8-encoded data (as <tt>&quot;C&quot;</tt> will wrap values outside the range 0..255, and not respect the string encoding). </p>
<p> In practice, that means that pack formats are now encoding-neutral, except <tt>&quot;C&quot;</tt>. </p>
<p> For consistency, <tt>&quot;A&quot;</tt> in <i>unpack()</i> format now trims all Unicode whitespace from the end of the string. Before perl 5.9.2, it used to strip only the classical <font SIZE="-1">ASCII</font> space characters.</p>
<h3>Miscellaneous</h3>
<p> The internal dump output has been improved, so that non-printable characters such as newline and backspace are output in <tt>&quot;
