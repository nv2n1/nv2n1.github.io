---
title: "selinux_file_context_cmp(3)"
name: "selinux_file_context_cmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_file_context_cmp/"
description: "selinux_file_context_cmp – Compare two SELinux security contexts excluding the ‘user’ component"
---

<p>selinux_file_context_cmp &#8211; Compare two SELinux security contexts excluding the &#8216;user&#8217; component</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int selinux_file_context_cmp(const char *a,

                             const char *b);</code></pre>
<h2>Description</h2>
<p><code>selinux_file_context_cmp</code>() compares two context strings excluding the user component with <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3) as shown in the <code>EXAMPLE</code> section. </p>
<p> This is useful as for most object contexts, the user component is not relevant.</p>
<h2>Return Value</h2>
<p>The return values follow the <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3) function, where:</p>
<dl>
<dd>0 if they are equal.</dl>
<dl>
<dd>1 if <i>a</i> is greater than <i>b</i></dl>
<dl>
<dd>-1 if <i>a</i> is less than <i>b</i></dl>
<h2>Errors</h2>
<p>None.</p>
<h2>Notes</h2>
<p>The contexts being compared do not specifically need to be file contexts.</p>
<h2>Example</h2>
<p>If context <i>a</i> is:</p>
<dl>
<dd>user_u:user_r:user_t:s0</dl>
<p> and context <i>b</i> is:</p>
<dl>
<dd>root:user_r:user_t:s0</dl>
<p> then the actual strings compared are:</p>
<dl>
<dd>:user_r:user_t:s0 and :user_r:user_t:s0</dl>
<p> Therefore they will match and <code>selinux_file_context_cmp</code>() will return zero.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
