---
title: "idn2(1)"
name: "idn2"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idn2/"
description: "idn2 – Libidn2 Internationalized Domain Names conversion tool"
---

<h2>NAME</h2>
<p> <code>idn2</code> &#8211; Libidn2 Internationalized Domain Names conversion tool</p>
<h2>SYNOPSIS</h2>
<p> <code>idn2</code> [OPTION]&#8230; [STRINGS]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> idn2 tool converts DNS domains from UTF-8 to ASCII compatibile encoding (ACE) form, as used in the DNS protocol. The encoding format is the Internationalized Domain Name (IDNA2008/TR46) format. </p>
<p> All input strings are expected to be encoded in the locale charset. </p>
<p> To process a string that starts with <code>&#8211;</code>, for example <code>-foo</code>, use <code>&#8212;</code> to signal the end of parameters, as in <code>idn2 &#8211;quiet &#8212; -foo</code>. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Prints help and exits.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Prints version and exits.</dd>
<dt><code>-d, &#8211;decode</code></dt>
<dd> Decode an ACE name according to IDNA2008.</dd>
<dt><code>-l, &#8211;lookup</code></dt>
<dd> Encode to ACE according to IDNA2008 (the default).</dd>
<dt><code>-r, &#8211;register</code></dt>
<dd> Registers a label.</dd>
<dt><code>-T, &#8211;tr46t</code></dt>
<dd> Enable TR#46 transitional processing.</dd>
<dt><code>-N, &#8211;tr46nt</code></dt>
<dd> Enable TR#46 non-transitional processing (default).</dd>
<dt><code>&#8211;no-tr46</code></dt>
<dd> Disable TR#46 processing.</dd>
<dt><code>&#8211;usestd3asciirules</code></dt>
<dd> Enable STD3 ASCII rules.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Prints debugging information.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Silent operation.</dd></dl>
<h2>Author</h2>
<p> Written by Simon Josefsson.</p>
<h2>Reporting bugs</h2>
<p> Report bugs to the gitlab issue tracker of the project <i><a rel="nofollow" href="https://gitlab.com/libidn/libidn2/issues">https://gitlab.com/libidn/libidn2/issues</a></i>. </p>
