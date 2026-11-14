---
title: "fcobjectsetbuild(3)"
name: "fcobjectsetbuild"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcobjectsetbuild/"
description: "FcObjectSetBuild, FcObjectSetVaBuild, FcObjectSetVapBuild – Build object set from args"
---

<p>FcObjectSetBuild, FcObjectSetVaBuild, FcObjectSetVapBuild &#8211; Build object set from args </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcObjectSet * FcObjectSetBuild (const char *</code><i>first</i><code>, &#8230;</code><i></i><code>); </p>
<p> FcObjectSet * FcObjectSetVaBuild (const char *</code><i>first</i><code>, va_list </code><i>va</i><code>); </p>
<p> void FcObjectSetVapBuild (FcObjectSet *</code><i>result</i><code>, const char *</code><i>first</i><code>, va_list </code><i>va</i><code>); </code></p>
<h2>Description</h2>
<p>These build an object set from a null-terminated list of property names. FcObjectSetVapBuild is a macro version of FcObjectSetVaBuild which returns the result in the <i>result</i> variable directly.</p>
