---
title: "fcpatternbuild(3)"
name: "fcpatternbuild"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternbuild/"
description: "FcPatternBuild, FcPatternVaBuild, FcPatternVapBuild – Create patterns from arguments"
---

<p>FcPatternBuild, FcPatternVaBuild, FcPatternVapBuild &#8211; Create patterns from arguments </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcPattern * FcPatternBuild (FcPattern *</code><i>pattern</i><code>, &#8230;</code><i></i><code>); </p>
<p> FcPattern * FcPatternVaBuild (FcPattern *</code><i>pattern</i><code>, va_list </code><i>va</i><code>); </p>
<p> void FcPatternVapBuild (FcPattern *</code><i>result</i><code>, FcPattern *</code><i>pattern</i><code>, va_list </code><i>va</i><code>); </code></p>
<h2>Description</h2>
<p>Builds a pattern using a list of objects, types and values. Each value to be entered in the pattern is specified with three arguments:</p>
<dl COMPACT>
<dt>1.</p>
<dd>Object name, a string describing the property to be added.</p>
<dt>2.</p>
<dd>Object type, one of the FcType enumerated values</p>
<dt>3.</p>
<dd>Value, not an FcValue, but the raw type as passed to any of the FcPatternAdd&lt;type&gt; functions. Must match the type of the second argument.</dl>
<p> The argument list is terminated by a null object name, no object type nor value need be passed for this. The values are added to `pattern&#8217;, if `pattern&#8217; is null, a new pattern is created. In either case, the pattern is returned. Example </p>
<pre>pattern = FcPatternBuild (0, FC_FAMILY, FcTypeString, &quot;Times&quot;, (char *) 0);</pre>
<p>FcPatternVaBuild is used when the arguments are already in the form of a varargs value. FcPatternVapBuild is a macro version of FcPatternVaBuild which returns its result directly in the <i>result</i> variable.</p>
