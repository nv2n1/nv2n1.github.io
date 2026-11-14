---
title: "waffle_feature_test_macros(7)"
name: "waffle_feature_test_macros"
section: "7"
letter: "w"
url: "/docs/linux/man/7-waffle_feature_test_macros/"
description: "waffle_feature_test_macros – Macros to control definitions exposed by Waffle’s headers"
---

<p>waffle_feature_test_macros &#8211; Macros to control definitions exposed by Waffle&#8217;s headers</p>
<h2>Synopsis</h2>
<pre><code>WAFFLE_API_VERSION</code>
<code>WAFFLE_API_EXPERIMENTAL</code></pre>
<h2>Description</h2>
<p>Waffle&#8217;s feature test macros allow the programmer to control the definitions that are exposed by Waffle&#8217;s headers when a program is compiled. Conversely, the macros allow the programmer to control which Waffle features a program&#8217;s source relies on. </p>
<p> In order to be effective, a feature test macro must be defined before including any header files. This can be done either in the compilation command (cc -DMACRO=value) or by defining the macro within the source code before including any headers.</p>
<h3>Specification of feature test macro requirements in manual pages</h3>
<p>When a function requires that a feature test macro be defined, the manual page docments it in the SYNOPSIS. When an enum or macro requires that a feature test macro be defined, the manual page documents it either in the SYNOPSIS or where the enum or macro first appears in the page.</p>
<h3>List of feature test macros</h3>
<p><code>WAFFLE_API_VERSION</code> (since waffle 1.3)</p>
<dl>
<dd>This macro controls the API version exposed by Waffle&#8217;s headers. The value ((<i>major</i> &lt;&lt; 8) | <i>minor</i>) exposes the API of Waffle <i>major</i>.<i>minor</i>. For example, the value 0x0103 exposes the API of Waffle 1.3. If this macro is undefined, then the headers expose the API of Waffle 1.2.</dl>
<p> <code>WAFFLE_API_EXPERIMENTAL</code></p>
<dl>
<dd>This macro exposes experimental features in Waffle&#8217;s headers. Experimental features may be altered or removed without notice and do not belong to Waffle&#8217;s stable API.</dl>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<dl>
<dd><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7)</dl>
<dl>
<dd><code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)</dl>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
