---
title: "globus_tilde_user_expand(3)"
name: "globus_tilde_user_expand"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_tilde_user_expand/"
description: "globus_tilde_expand.h –"
---

<p>globus_tilde_expand.h &#8211; </p>
<p> Home Directory ~ expansion.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_types.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_TILDE_EXPAND</code><br />
 <i>Expand ~. </i><br />
 #define <code>GLOBUS_TILDE_USER_EXPAND</code><br />
 <i>Expand ~user. </i></p>
<h3>Functions</h3>
<p>int <code>globus_tilde_expand</code> (unsigned long options, <code>globus_bool_t</code> url_form, char *inpath, char **outpath)<br />
 <i>Expand ~ and/or ~user in path strings. </i></p>
<h2>Detailed Description</h2>
<p>Home Directory ~ expansion. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
