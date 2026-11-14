---
title: "tk_getuid(3)"
name: "tk_getuid"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getuid/"
description: "Tk_GetUid, Tk_Uid – convert from string to unique identifier"
---

<p>Tk_GetUid, Tk_Uid &#8211; convert from string to unique identifier </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Uid
<code>Tk_GetUid</code>(<i>string</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>char <i>*string</i> (in) String for which the corresponding unique identifier is desired. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetUid</code> returns the unique identifier corresponding to <i>string</i>. Unique identifiers are similar to atoms in Lisp, and are used in Tk to speed up comparisons and searches. A unique identifier (type Tk_Uid) is a string pointer and may be used anywhere that a variable of type &#8220;char *&#8221; could be used. However, there is guaranteed to be exactly one unique identifier for any given string value. If <code>Tk_GetUid</code> is called twice, once with string <i>a</i> and once with string <i>b</i>, and if <i>a</i> and <i>b</i> have the same string value (strcmp(a, b) == 0), then <code>Tk_GetUid</code> will return exactly the same Tk_Uid value for each call (Tk_GetUid(a) == Tk_GetUid(b)). This means that variables of type Tk_Uid may be compared directly (x == y) without having to call <code>strcmp</code>. In addition, the return value from <code>Tk_GetUid</code> will have the same string value as its argument (strcmp(Tk_GetUid(a), a) == 0). </p>
<h2>Keywords</h2>
<p>atom, unique identifier</p>
