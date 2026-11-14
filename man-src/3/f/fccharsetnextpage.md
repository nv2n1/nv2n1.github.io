---
title: "fccharsetnextpage(3)"
name: "fccharsetnextpage"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetnextpage/"
description: "FcCharSetNextPage – Continue enumerating charset contents"
---

<p>FcCharSetNextPage &#8211; Continue enumerating charset contents </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar32 FcCharSetNextPage (const FcCharSet *</code><i>a</i><code>, FcChar32[FC_CHARSET_MAP_SIZE] </code><i>map</i><code>, FcChar32 *</code><i>next</i><code>); </code></p>
<h2>Description</h2>
<p>Builds an array of bits in <i>map</i> marking the Unicode coverage of <i>a</i> for page containing <i>*next</i> (see the <code>FcCharSetFirstPage</code> description for details). <i>*next</i> is set to contains the base code point for the next page in <i>a</i>. Returns the base of code point for the page, or FC_CHARSET_DONE if <i>a</i> does not contain <i>*next</i>.</p>
