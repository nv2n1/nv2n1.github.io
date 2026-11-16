---
title: "xmcvtxmstringtoct(3)"
name: "xmcvtxmstringtoct"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcvtxmstringtoct/"
description: "XmCvtXmStringToCT — A compound string function that converts a compound string to compound text"
---

<p><code>XmCvtXmStringToCT</code> &#8212; A compound string function that converts a compound string to compound text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>char * XmCvtXmStringToCT</code>(
<code>XmString string</code>);</pre>
<h2>Description</h2>
<p><code>XmCvtXmStringToCT</code> converts a compound string to a (<code>char *</code>) string in compound text format. The application must call <code>XtAppInitialize</code> before calling this function. The converter uses the font list tag associated with a given compound string segment to select a compound text format for that segment. A registry defines a mapping between font list tags and compound text encoding formats. The converter uses the following algorithm for each compound string segment:</p>
<dl COMPACT>
<dt> 1.</dt>
<dd>If the compound string segment tag is mapped to <code>XmFONTLIST_DEFAULT_TAG</code> in the registry, the converter passes the text of the compound string segment to <code>XmbTextListToTextProperty</code> with an encoding style of <code>XCompoundTextStyle</code> and uses the resulting compound text for that segment.</dd>
<dt> 2.</dt>
<dd>If the compound string segment tag is mapped to an MIT registered charset in the registry, the converter creates the compound text for that segment using the charset (from the registry) and the text of the compound string segment as defined in the X Consortium Standard <i>Compound Text Encoding</i>.</dd>
<dt> 3.</dt>
<dd>If the compound string segment tag is mapped to a charset in the registry that is neither <code>XmFONTLIST_DEFAULT_TAG</code> nor an MIT registered charset, the converter creates the compound text for that segment using the charset (from the registry) and the text of the compound string segment as an &quot;extended segment&quot; with a variable number of octets per character.</dd>
<dt> 4.</dt>
<dd>If the compound string segment tag is not mapped in the registry, the result is implementation dependent.</dd>
<dt><i>string</i></dt>
<dd>Specifies a compound string to be converted to compound text.</dd></dl>
<h2>Return</h2>
<p>Returns a (<code>char *</code>) string in compound text format. This format is described in the X Consortium Standard <i>Compound Text Encoding</i>. The function allocates space to hold the returned string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XtFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcvtcttoxmstring/">XmCvtCTToXmString</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmmapsegmentencoding/">XmMapSegmentEncoding</a></code>(3), <code><a href="/docs/linux/man/3-xmregistersegmentencoding/">XmRegisterSegmentEncoding</a></code>(3), and <code>XmString</code>.</p>
