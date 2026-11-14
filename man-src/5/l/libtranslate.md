---
title: "libtranslate(5)"
name: "libtranslate"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libtranslate/"
description: "services.xml – libtranslate generic service definitions"
---

<p>services.xml &#8211; libtranslate generic service definitions</p>
<h2>Description</h2>
<p>The <i>services.xml</i> file contains translation service definitions for the libtranslate generic module. The generic module provides an abstract framework for supporting web-based translation services. When the generic module is initialized, it reads service definitions from the <i>services.xml</i> files located in <i>/usr/share/libtranslate</i> and <i>~/.libtranslate</i>, creates the services defined in these files, and makes them available to libtranslate. The <i>services.xml</i> file must be encoded in UTF-8, and conform to the <i>services.xml</i> Document Type Definition, located in <i>/usr/share/libtranslate/services.dtd</i>. </p>
<h2>Elements</h2>
<h3>services</h3>
<dl>
<dt>Description</p>
<dd>The services element is the root of the document, and may contains service definitions and language mappings. </p>
<dt>Children</p>
<dd>These elements may occur zero or more times in services: custom-language, service. </p>
</dl>
<h3>custom-language</h3>
<dl>
<dt>Description</p>
<dd>The custom-language element maps a RFC 3066 language tag to a language name. </p>
<dl>
<dd><code>Note</code> </p>
<p> Some RFC 3066 tag to name mappings are built into libtranslate and do not need to be added (see the Built-In RFC 3066 Tag to Name Mappings appendix in the libtranslate Reference Manual). </p>
</dl>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>tag</i> (required)</p>
<dd>The RFC 3066 language tag. </p>
<dt><i>name</i> (required)</p>
<dd>The language human-readable name. </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains custom-language: services. </p>
</dl>
<h3>service</h3>
<dl>
<dt>Description</p>
<dd>The service element defines a translation service. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>name</i> (required)</p>
<dd>The service symbolic name, encoded in ASCII. </p>
<dt><i>nick</i> (implied, default: <i>name</i>)</p>
<dd>The service human-readable name. </p>
<dt><i>max-chunk-len</i> (optional, default: 1000)</p>
<dd>The maximum length of an input chunk, in characters (0 means unlimited). </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains service: services. </p>
<dt>Children</p>
<dd>This element may occur zero or more times in service: group. </p>
</dl>
<h3>group</h3>
<dl>
<dt>Description</p>
<dd>The group element defines a translation group (a group represents a set of languages and translation methods). </p>
<dt>Parents</p>
<dd>This element contains group: service. </p>
<dt>Children</p>
<dd>These elements may occur zero or more times in group: language, http-header. </p>
<p> These elements may occur zero or one time in group: text-translation, web-page-translation. </p>
</dl>
<h3>language</h3>
<dl>
<dt>Description</p>
<dd>The language element adds a language to the list of languages supported by a group. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>tag</i> (required)</p>
<dd>The RFC 3066 language tag. </p>
<dt><i>service-tag</i> (implied, default: <i>tag</i>)</p>
<dd>The language service-specific tag. This tag is not exposed to libtranslate, but is available as <i>from</i> and <i>to</i> variables (see Variable Substitution). </p>
<dt><i>to</i> (optional, default: none)</p>
<dd>A comma-separated list of RFC 3066 language tags this language can be translated into. The special list element * means &quot;every language of this group but this one&quot;. </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains language: group. </p>
</dl>
<h3>http-header</h3>
<dl>
<dt>Description</p>
<dd>The http-header element adds a HTTP header to the list of headers that are set when a HTTP request is issued. </p>
<p> If the http-header element occurs inside a group element, the header is added for text and web page translations. </p>
<p> If it occurs inside a text-translation or web-page-translation element, the header is only added for a text or web page translation, respectively. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>name</i> (required)</p>
<dd>The HTTP header name. </p>
<dt><i>value</i> (required)</p>
<dd>The HTTP header value. </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>These elements contain http-header: group, text-translation, web-page-translation. </p>
</dl>
<h3>text-translation</h3>
<dl>
<dt>Description</p>
<dd>The presence of the text-translation element specifies that the group can translate text. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>url</i> (required)</p>
<dd>The URL to use for translating text. Variable substitution is performed on the URL (see Variable Substitution). </p>
<dt><i>post</i> (optional, default: none)</p>
<dd>If this attribute is present, a HTTP POST request is issued (using the attribute value as post data). Otherwise, a HTTP GET request is issued. Variable substitution is performed on the post data (see Variable Substitution). </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains text-translation: group. </p>
<dt>Children</p>
<dd>These element may occur zero or more times in text-translation: http-header, pre-marker, error-marker. </p>
<p> This element may occur zero or one time in text-translation: post-marker. </p>
</dl>
<h3>pre-marker</h3>
<dl>
<dt>Description</p>
<dd>The pre-marker element is used to extract the translated text from the response to a text translation request. </p>
<p> For each pre-marker element, the parser locates <i>text</i> in the server response. If <i>text</i> is found, the parser moves to the character following <i>text</i>. If it is not found, the translation fails. The translated text starts at the character following the last pre-marker match. If no pre-marker element is specified, the translated text starts at the first character of the server response. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>text</i> (required)</p>
<dd>The text to match. </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains pre-marker: text-translation. </p>
</dl>
<h3>post-marker</h3>
<dl>
<dt>Description</p>
<dd>The post-marker element is used to extract the translated text from the response to a text translation request. </p>
<p> If <i>text</i> can be located in the server response, the translated text ends at the character preceding <i>text</i>. Otherwise, the translation fails. If no post-marker element is specified, the translated text ends at the last character of the server response. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>text</i> (required)</p>
<dd>The text to match. </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains post-marker: text-translation. </p>
</dl>
<h3>error-marker</h3>
<dl>
<dt>Description</p>
<dd>The error-marker element is used to check if a text translation error has occurred. </p>
<p> If one or more error-marker elements are specified and the <i>text</i> of any of them can be located anywhere in the server response, the translation fails. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>text</i> (required)</p>
<dd>The text to match. </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains error-marker: text-translation. </p>
</dl>
<h3>web-page-translation</h3>
<dl>
<dt>Description</p>
<dd>The presence of the web-page-translation element specifies that the group can translate a web page. </p>
<p> If no http-header element is specified and if <i>post</i> is not specified, the generic module does not need to connect to the server. In this case, <i>url</i> is returned as the URL of the translated web page. Otherwise, the generic module connects to the server, issues a HTTP GET or POST request, saves the response to a local file, and returns a file:// URL pointing to that file. </p>
<dt>Attributes</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>url</i> (required)</p>
<dd>The URL to use for translating a web page. Variable substitution is performed on the URL (see Variable Substitution). </p>
<dt><i>post</i> (optional, default: none)</p>
<dd>If this attribute is present, a HTTP POST request is issued (using the attribute value as post data). Otherwise, a HTTP GET request is issued (or no request at all, see above). Variable substitution is performed on the post data (see Variable Substitution). </p>
</dl>
</dl>
<dd>
<dt>Parents</p>
<dd>This element contains web-page-translation: group. </p>
<dt>Children</p>
<dd>This element may occur zero or more times in web-page-translation: http-header. </p>
</dl>
<h2>Variable Substitution</h2>
<p>Variable substitution is performed at translation time on the <i>url</i> and <i>post</i> attributes of the text-translation and web-page-translation elements. </p>
<p> A variable has the syntax ${<i>varname</i>[:<i>modifiers</i>]}. </p>
<p> <i>varname</i> may be any of the following variables: </p>
<dl>
<dt><i>text</i> (text-translation only)</p>
<dd>The text to translate. </p>
<dt><i>url</i> (web-page-translation only)</p>
<dd>The URL of the web page to translate. </p>
<dt><i>from</i></p>
<dd>The source language service tag. </p>
<dt><i>to</i></p>
<dd>The destination language service tag. </p>
<dt><i>time</i></p>
<dd>The number of seconds since 0 hours, 0 minutes, 0 seconds, January 1, 1970, Coordinated Universal Time. </p>
</dl>
<p> <i>modifiers</i> is a comma-separated list of modifiers. Each modifier is applied (in the specified order) on the contents of the variable. A modifier has the syntax <i>name</i>[=<i>value</i>]. </p>
<p> <i>name</i> may be any of the following modifiers: </p>
<dl>
<dt>escape</p>
<dd>Escapes the unsafe characters in the variable using URI percent notation. </p>
<dt>charset</p>
<dd>Converts the variable from UTF-8 (the libtranslate character set) to the character set <i>value</i>. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/libtranslate/services.xml</i></p>
<dd></dl>
<p> The system-wide service definitions. </p>
<dl>
<dt><i>~/.libtranslate/services.xml</i></p>
<dd></dl>
<p> The user service definitions. </p>
<dl>
<dt><i>/usr/share/libtranslate/services.dtd</i></p>
<dd></dl>
<p> The <i>services.xml</i> Document Type Definition.</p>
<h2>See Also</h2>
<p>The libtranslate Reference Manual </p>
<h2>Author</h2>
<p>Jean-Yves Lefort.</p>
