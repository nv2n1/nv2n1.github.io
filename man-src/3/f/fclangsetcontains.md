---
title: "fclangsetcontains(3)"
name: "fclangsetcontains"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsetcontains/"
description: "FcLangSetContains – check langset subset relation"
---

<p>FcLangSetContains &#8211; check langset subset relation </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcLangSetContains (const FcLangSet *</code><i>ls_a</i><code>, const FcLangSet *</code><i>ls_b</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcLangSetContains</code> returns FcTrue if <i>ls_a</i> contains every language in <i>ls_b</i>. <i>ls_a</i> will &#8216;contain&#8217; a language from <i>ls_b</i> if <i>ls_a</i> has exactly the language, or either the language or <i>ls_a</i> has no territory.</p>
