---
title: "intel_error_decode(1)"
name: "intel_error_decode"
section: "1"
letter: "i"
url: "/docs/linux/man/1-intel_error_decode/"
description: "intel_error_decode – Decodes an Intel GPU dump automatically captured by the kernel at the time of an error."
---

<h2>NAME</h2>
<p> intel_error_decode &#8211; Decodes an Intel GPU dump automatically captured by the kernel at the time of an error.</p>
<h2>SYNOPSIS</h2>
<pre>
<code>intel_error_decode</code>
<code>intel_error_decode [ filename ]</code>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>intel_error_decode</code> is a tool that decodes the instructions and state of the GPU at the time of an error. It requires kernel 2.6.34 or newer, and either debugfs mounted on /sys/kernel/debug or /debug containing a current i915_error_state or you can pass a file containing a saved error.</p>
<h3>Options</h3>
<dl>
<dt><code>filename</code></p>
<dd> Decodes a previously saved error. </p>
</dl>
<h2>Index</h2>
