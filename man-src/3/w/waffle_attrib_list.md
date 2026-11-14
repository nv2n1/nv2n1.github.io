---
title: "waffle_attrib_list(3)"
name: "waffle_attrib_list"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_attrib_list/"
description: "waffle_attrib_list, waffle_attrib_list_length, waffle_attrib_list_get, waffle_attrib_list_get_with_default, waffle_attrib_list_update – Utilities for attribute lists"
---

<p>waffle_attrib_list, waffle_attrib_list_length, waffle_attrib_list_get, waffle_attrib_list_get_with_default, waffle_attrib_list_update &#8211; Utilities for attribute lists</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

bool waffle_attrib_list_length(const int32_t attrib_list[]);

bool waffle_attrib_list_get(const int32_t attrib_list[], int32_t key, int32_t *value);

bool waffle_attrib_list_get_with_default(const int32_t attrib_list[], int32_t key, int32_t *value, int32_t default_value);

bool waffle_attrib_list_update(int32_t attrib_list[], int32_t key, int32_t *value);</code></pre>
<h2>Description</h2>
<dd>An attribute list is a zero-terminated list of <code>int32_t</code> key/value pairs or a null pointer. A null pointer is interpreted as an empty list, whose only member is the terminal zero. For concrete examples of attribute lists, see the &quot;Examples&quot; section in <code><a href="/docs/linux/man/3-waffle_config/">waffle_config</a></code>(3). </p>
<p> All attribute list functions can be called before waffle has been successfully initialized with <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3). </p>
<p> <code>waffle_attrib_list_length()</code></p>
<dl>
<dd>Return the number of key/value pairs in the list.</dl>
<p> <code>waffle_attrib_list_get()</code></p>
<dl>
<dd>Get the <i>value</i> associated with <i>key</i>. If the list does not contain the <i>key</i>, then <i>value</i> is not dereferenced. Return true if and only if the list contains the <i>key</i>.</dl>
<p> <code>waffle_attrib_list_get_with_default()</code></p>
<dl>
<dd>Equivalent to <code>waffle_attrib_list_get()</code> except that if the list does not contain the <i>key</i> then <i>value</i> is set to a <i>default_value</i>.</dl>
<p> <code>waffle_attrib_list_update()</code></p>
<dl>
<dd>Update the <i>value</i> associated with <i>key</i>. If the list does not contain the <i>key</i> then the list is not modified. Return true if and only if the list contains the <i>key</i>.</dl>
<h2>Errors</h2>
<p>All attribute list functions set the error code to <code>WAFFLE_NO_ERROR</code> and can be called before waffle has been successfully initialized with <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3). </p>
<p> See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes.</p>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7)</p>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
