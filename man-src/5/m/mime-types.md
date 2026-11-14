---
title: "mime-types(5)"
name: "mime-types"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mime-types/"
description: "mime.types – mime type description file for cups"
---

<p>mime.types &#8211; mime type description file for cups</p>
<h2>Description</h2>
<p>The <code>mime.types</code> file defines the recognized file types. </p>
<p> Additional file types are specified in files with the extension <i>.types</i> in the CUPS configuration directory. </p>
<p> Each line in the <code>mime.types</code> file is a comment, blank, or rule line. Comment lines start with the # character. Rule lines start with the MIME media type and are optionally followed by a series of file recognition rules: </p>
<pre> <i>mime/type </i>[ <i>rule </i>... <i>rule </i>]</pre>
<p>Rules can be extended over multiple lines using the backslash character (\): </p>
<pre> <i>mime/type </i>[ <i>really-really-really-long-rule </i>... <code>\
 </code><i>rule </i>]</pre>
<p>MIME media types specified by the <i>mime/type</i> field are case-insensitive and are sorted in ascending alphanumeric order for the purposes of matching. See the &quot;TYPE MATCHING AND PRIORITY&quot; section for more information. </p>
<p> The rules may be grouped using parenthesis, joined using &quot;+&quot; for a logical AND, joined using &quot;,&quot; or whitespace for a logical OR, and negated using &quot;!&quot;.</p>
<h3>Rules</h3>
<p>Rules take two forms &#8211; a filename extension by itself and functions with test values inside parenthesis. The following functions are available:</p>
<dl>
<dt><code>match(&quot;</code><i>pattern</i><code>&quot;)</code></p>
<dd>True if the filename matches the given shell wildcard <i>pattern</i>.</p>
<dt><code>ascii(</code><i>offset</i><code>,</code><i>length</i><code>)</code></p>
<dd>True if the <i>length</i> bytes starting at <i>offset</i> are valid printable ASCII (CR, NL, TAB, BS, 32-126).</p>
<dt><code>printable(</code><i>offset</i><code>,</code><i>length</i><code>)</code></p>
<dd>True if the <i>length</i> bytes starting at <i>offset</i> are printable 8-bit chars (CR, NL, TAB, BS, 32-126, 128-254).</p>
<dt><code>priority(</code><i>number</i><code>)</code></p>
<dd>Specifies the relative priority of this MIME media type. The default priority is 100. Larger values have higher priority while smaller values have lower priority.</p>
<dt><code>string(</code><i>offset</i><code>,&quot;</code><i>string</i><code>&quot;)</code></p>
<dd>True if the bytes starting at <i>offset</i> are identical to <i>string</i>.</p>
<dt><code>istring(</code><i>offset</i><code>,&quot;</code><i>string</i><code>&quot;)</code></p>
<dd>True if the bytes starting at <i>offset</i> match <i>string</i> without respect to case.</p>
<dt><code>char(</code><i>offset</i><code>,</code><i>value</i><code>)</code></p>
<dd>True if the byte at <i>offset</i> is identical to <i>value</i>.</p>
<dt><code>short(</code><i>offset</i><code>,</code><i>value</i><code>)</code></p>
<dd>True if the 16-bit big-endian integer at <i>offset</i> is identical to <i>value</i>.</p>
<dt><code>int(</code><i>offset</i><code>,</code><i>value</i><code>)</code></p>
<dd>True if the 32-bit big-endian integer at <i>offset</i> is identical to <i>value</i>.</p>
<dt><code>locale(&quot;</code><i>string</i><code>&quot;)</code></p>
<dd>True if current locale matches <i>string</i>.</p>
<dt><code>contains(</code><i>offset</i><code>,</code><i>range</i><code>,&quot;</code><i>string</i><code>&quot;)</code></p>
<dd>True if the bytes starting at <i>offset</i> for <i>range</i> bytes contains <i>string</i>.</dl>
<h3>String Constants</h3>
<p>String constants can be specified inside quotes (&quot;&quot;) for strings containing whitespace and angle brackets (&lt;&gt;) for hexadecimal strings.</p>
<h3>Type Matching And Priority</h3>
<p>When CUPS needs to determine the MIME media type of a given file, it checks every MIME media type defined in the <i>.types</i> files. When two or more types match a given file, the type chosen will depend on the type name and priority, with higher-priority types being used over lower-priority ones. If the types have the same priority, the type names are sorted alphanumerically in ascending order and the first type is chosen. </p>
<p> For example, if two types &quot;text/bar&quot; and &quot;text/foo&quot; are defined as matching the extension &quot;doc&quot;, normally the type &quot;text/bar&quot; will be chosen since its name is alphanumerically smaller than &quot;text/foo&quot;. However, if &quot;text/foo&quot; also defines a higher priority than &quot;text/bar&quot;, &quot;text/foo&quot; will be chosen instead.</p>
<h2>Files</h2>
<p><i>/etc/cups</i> &#8211; Typical CUPS configuration directory.</p>
<h2>Examples</h2>
<p>Define two MIME media types for raster data, with one being a subset with higher priority: </p>
<pre> application/vnd.cups-raster string(0,&quot;RaSt&quot;) string(0,&quot;tSaR&quot;) \
 string(0,&quot;RaS2&quot;) string(0,&quot;2SaR&quot;) \
 string(0,&quot;RaS3&quot;) string(0,&quot;3SaR&quot;)
 image/pwg-raster string(0,&quot;RaS2&quot;) + \
 string(4,PwgRaster&lt;00&gt;) priority(150)</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5), <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/8-cupsfilter/">cupsfilter</a></code>(8), <code><a href="/docs/linux/man/5-mime-convs/">mime.convs</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
