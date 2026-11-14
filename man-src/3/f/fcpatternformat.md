---
title: "fcpatternformat(3)"
name: "fcpatternformat"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternformat/"
description: "FcPatternFormat – Format a pattern into a string according to a format specifier"
---

<p>FcPatternFormat &#8211; Format a pattern into a string according to a format specifier </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcPatternFormat (FcPattern *</code><i>pat</i><code>, const FcChar8 *</code><i>format</i><code>); </code></p>
<h2>Description</h2>
<p>Converts given pattern <i>pat</i> into text described by the format specifier <i>format</i>. The return value refers to newly allocated memory which should be freed by the caller using free(), or NULL if <i>format</i> is invalid. </p>
<p> The format is loosely modeled after printf-style format string. The format string is composed of zero or more directives: ordinary characters (not &quot;%&quot;), which are copied unchanged to the output stream; and tags which are interpreted to construct text from the pattern in a variety of ways (explained below). Special characters can be escaped using backslash. C-string style special characters like 
 and  are also supported (this is useful when the format string is not a C string literal). It is advisable to always escape curly braces that are meant to be copied to the output as ordinary characters. </p>
<p> Each tag is introduced by the character &quot;%&quot;, followed by an optional minimum field width, followed by tag contents in curly braces ({}). If the minimum field width value is provided the tag will be expanded and the result padded to achieve the minimum width. If the minimum field width is positive, the padding will right-align the text. Negative field width will left-align. The rest of this section describes various supported tag contents and their expansion. </p>
<p> A <i>simple</i> tag is one where the content is an identifier. When simple tags are expanded, the named identifier will be looked up in <i>pattern</i> and the resulting list of values returned, joined together using comma. For example, to print the family name and style of the pattern, use the format &quot;%{family} %{style}
&quot;. To extend the family column to forty characters use &quot;%-40{family}%{style}
&quot;. </p>
<p> Simple tags expand to list of all values for an element. To only choose one of the values, one can index using the syntax &quot;%{elt[idx]}&quot;. For example, to get the first family name only, use &quot;%{family[0]}&quot;. </p>
<p> If a simple tag ends with &quot;=&quot; and the element is found in the pattern, the name of the element followed by &quot;=&quot; will be output before the list of values. For example, &quot;%{weight=}&quot; may expand to the string &quot;weight=80&quot;. Or to the empty string if <i>pattern</i> does not have weight set. </p>
<p> If a simple tag starts with &quot;:&quot; and the element is found in the pattern, &quot;:&quot; will be printed first. For example, combining this with the =, the format &quot;%{:weight=}&quot; may expand to &quot;:weight=80&quot; or to the empty string if <i>pattern</i> does not have weight set. </p>
<p> If a simple tag contains the string &quot;:-&quot;, the rest of the the tag contents will be used as a default string. The default string is output if the element is not found in the pattern. For example, the format &quot;%{:weight=:-123}&quot; may expand to &quot;:weight=80&quot; or to the string &quot;:weight=123&quot; if <i>pattern</i> does not have weight set. </p>
<p> A <i>count</i> tag is one that starts with the character &quot;#&quot; followed by an element name, and expands to the number of values for the element in the pattern. For example, &quot;%{#family}&quot; expands to the number of family names <i>pattern</i> has set, which may be zero. </p>
<p> A <i>sub-expression</i> tag is one that expands a sub-expression. The tag contents are the sub-expression to expand placed inside another set of curly braces. Sub-expression tags are useful for aligning an entire sub-expression, or to apply converters (explained later) to the entire sub-expression output. For example, the format &quot;%40&#123;&#123;%{family} %{style}}}&quot; expands the sub-expression to construct the family name followed by the style, then takes the entire string and pads it on the left to be at least forty characters. </p>
<p> A <i>filter-out</i> tag is one starting with the character &quot;-&quot; followed by a comma-separated list of element names, followed by a sub-expression enclosed in curly braces. The sub-expression will be expanded but with a pattern that has the listed elements removed from it. For example, the format &quot;%{-size,pixelsize{sub-expr}}&quot; will expand &quot;sub-expr&quot; with <i>pattern</i> sans the size and pixelsize elements. </p>
<p> A <i>filter-in</i> tag is one starting with the character &quot;+&quot; followed by a comma-separated list of element names, followed by a sub-expression enclosed in curly braces. The sub-expression will be expanded but with a pattern that only has the listed elements from the surrounding pattern. For example, the format &quot;%{+family,familylang{sub-expr}}&quot; will expand &quot;sub-expr&quot; with a sub-pattern consisting only the family and family lang elements of <i>pattern</i>. </p>
<p> A <i>conditional</i> tag is one starting with the character &quot;?&quot; followed by a comma-separated list of element conditions, followed by two sub-expression enclosed in curly braces. An element condition can be an element name, in which case it tests whether the element is defined in pattern, or the character &quot;!&quot; followed by an element name, in which case the test is negated. The conditional passes if all the element conditions pass. The tag expands the first sub-expression if the conditional passes, and expands the second sub-expression otherwise. For example, the format &quot;%{?size,dpi,!pixelsize{pass}{fail}}&quot; will expand to &quot;pass&quot; if <i>pattern</i> has size and dpi elements but no pixelsize element, and to &quot;fail&quot; otherwise. </p>
<p> An <i>enumerate</i> tag is one starting with the string &quot;[]&quot; followed by a comma-separated list of element names, followed by a sub-expression enclosed in curly braces. The list of values for the named elements are walked in parallel and the sub-expression expanded each time with a pattern just having a single value for those elements, starting from the first value and continuing as long as any of those elements has a value. For example, the format &quot;%{[]family,familylang{%{family} (%{familylang})
}}&quot; will expand the pattern &quot;%{family} (%{familylang})
&quot; with a pattern having only the first value of the family and familylang elements, then expands it with the second values, then the third, etc. </p>
<p> As a special case, if an enumerate tag has only one element, and that element has only one value in the pattern, and that value is of type FcLangSet, the individual languages in the language set are enumerated. </p>
<p> A <i>builtin</i> tag is one starting with the character &quot;=&quot; followed by a builtin name. The following builtins are defined:</p>
<dl COMPACT>
<dt><code>unparse</code></p>
<dd>Expands to the result of calling FcNameUnparse() on the pattern.</p>
<dt><code>fcmatch</code></p>
<dd>Expands to the output of the default output format of the fc-match command on the pattern, without the final newline.</p>
<dt><code>fclist</code></p>
<dd>Expands to the output of the default output format of the fc-list command on the pattern, without the final newline.</p>
<dt><code>fccat</code></p>
<dd>Expands to the output of the default output format of the fc-cat command on the pattern, without the final newline.</p>
<dt><code>pkgkit</code></p>
<dd>Expands to the list of PackageKit font() tags for the pattern. Currently this includes tags for each family name, and each language from the pattern, enumerated and sanitized into a set of tags terminated by newline. Package management systems can use these tags to tag their packages accordingly. For example, the format &quot;%{+family,style{%{=unparse}}}
&quot; will expand to an unparsed name containing only the family and style element values from <i>pattern</i>.</dl>
<p> The contents of any tag can be followed by a set of zero or more <i>converter</i>s. A converter is specified by the character &quot;|&quot; followed by the converter name and arguments. The following converters are defined:</p>
<dl COMPACT>
<dt><code>basename</code></p>
<dd>Replaces text with the results of calling FcStrBasename() on it.</p>
<dt><code>dirname</code></p>
<dd>Replaces text with the results of calling FcStrDirname() on it.</p>
<dt><code>downcase</code></p>
<dd>Replaces text with the results of calling FcStrDowncase() on it.</p>
<dt><code>shescape</code></p>
<dd>Escapes text for one level of shell expansion. (Escapes single-quotes, also encloses text in single-quotes.)</p>
<dt><code>cescape</code></p>
<dd>Escapes text such that it can be used as part of a C string literal. (Escapes backslash and double-quotes.)</p>
<dt><code>xmlescape</code></p>
<dd>Escapes text such that it can be used in XML and HTML. (Escapes less-than, greater-than, and ampersand.)</p>
<dt><code>delete(</code><i>chars</i><code>)</code></p>
<dd>Deletes all occurrences of each of the characters in <i>chars</i> from the text. FIXME: This converter is not UTF-8 aware yet.</p>
<dt><code>escape(</code><i>chars</i><code>)</code></p>
<dd>Escapes all occurrences of each of the characters in <i>chars</i> by prepending it by the first character in <i>chars</i>. FIXME: This converter is not UTF-8 aware yet.</p>
<dt><code>translate(</code><i>from</i><code>,</code><i>to</i><code>)</code></p>
<dd>Translates all occurrences of each of the characters in <i>from</i> by replacing them with their corresponding character in <i>to</i>. If <i>to</i> has fewer characters than <i>from</i>, it will be extended by repeating its last character. FIXME: This converter is not UTF-8 aware yet. For example, the format &quot;%{family|downcase|delete( )}
&quot; will expand to the values of the family element in <i>pattern</i>, lower-cased and with spaces removed.</dl>
<h2>Since</h2>
<p>version 2.9.0</p>
