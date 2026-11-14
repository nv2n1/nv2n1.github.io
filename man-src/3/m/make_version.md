---
title: "make_version(3)"
name: "make_version"
section: "3"
letter: "m"
url: "/docs/linux/man/3-make_version/"
description: "MAKE_VERSION – Create a 32 bit integer from the Allegro version"
---

<p>MAKE_VERSION &#8211; Create a 32 bit integer from the Allegro version</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Macro MAKE_VERSION(a, b, c)</code></p>
<h2>Description</h2>
<p>This macro can be used to check if some Allegro version is (binary) compatible with the current version. It is safe to use &gt; and &lt; to check if one version is more recent than another. The third number is ignored if the second number is even, so MAKE_VERSION(4, 2, 0) is equivalent to MAKE_VERSION(4, 2, 1). This is because of our version numbering policy since 4.0.0: the second number is even for stable releases, which must be ABI-compatible with earlier versions of the same series. This macro is mainly useful for addon packages and libraries. See the `ABI compatibility information&#8217; section of the manual for more detailed information. Example: </p>
<pre> /* Check if the current version is compatible with Allegro 4.2.0 */
 #if (MAKE_VERSION(4, 2, 0) &lt;= MAKE_VERSION(ALLEGRO_VERSION, \
 ALLEGRO_SUB_VERSION, ALLEGRO_WIP_VERSION))
 /* Allegro 4.2.0 compatibility */
 #else
 /* Work-around */
 #endif</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-allegro_version/">ALLEGRO_VERSION</a></code>(3), <code><a href="/docs/linux/man/3-allegro_sub_version/">ALLEGRO_SUB_VERSION</a></code>(3), <code><a href="/docs/linux/man/3-allegro_wip_version/">ALLEGRO_WIP_VERSION</a></code>(3)</p>
