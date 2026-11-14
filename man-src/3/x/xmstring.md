---
title: "xmstring(3)"
name: "xmstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstring/"
description: "XmString — Data type for a compound string"
---

<p><code>XmString</code> &#8212; Data type for a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmString</code> is the data type for a compound string. Compound strings consist of a sequence of components, including, but not limited to, the following:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_SEPARATOR</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_TAB</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_LAYOUT_POP</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_DIRECTION</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_LAYOUT_PUSH</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_CHARSET</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_FONTLIST_ELEMENT_TAG</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_LOCALE</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_LOCALE_TEXT</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_TAG</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_TEXT</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_END</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_RENDITION_BEGIN</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_RENDITION_END</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_UNKNOWN</code></p>
<dt> &bull;</p>
<dd><code>XmSTRING_COMPONENT_WIDECHAR_TEXT</code></dl>
<p> and also a rendition tags table, text, and text component. When a compound string is displayed, the rendition tags and the direction are used to determine how to display the text. </p>
<p> Calling <code>XtGetValues</code> for a resource whose type is <code>XmString</code> yields a copy of the compound string resource value. The application is responsible for using <code>XmStringFree</code> to free the memory allocated for the copy. </p>
<p> Please see the <code>XmStringComponentType</code> reference page for more detail about compound string components, and for a description of the order in which the components should appear in a compound string. Refer to the <code>XmRenderTable</code> reference page for a description of the algorithm that associates the rendition tags used for displaying a compound string text component with a rendition in a render table.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmparsemapping/">XmParseMapping</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingcreate/">XmParseMappingCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingfree/">XmParseMappingFree</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappinggetvalues/">XmParseMappingGetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingsetvalues/">XmParseMappingSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetablefree/">XmParseTableFree</a></code>(3), <code><a href="/docs/linux/man/3-xmstringbaseline/">XmStringBaseline</a></code>(3), <code><a href="/docs/linux/man/3-xmstringbytecompare/">XmStringByteCompare</a></code>(3), <code><a href="/docs/linux/man/3-xmstringbytestreamlength/">XmStringByteStreamLength</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcompare/">XmStringCompare</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcomponentcreate/">XmStringComponentCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcomponenttype/">XmStringComponentType</a></code>(3), <code><a href="/docs/linux/man/3-xmstringconcat/">XmStringConcat</a></code>(3), <code><a href="/docs/linux/man/3-xmstringconcatandfree/">XmStringConcatAndFree</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcopy/">XmStringCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreatelocalized/">XmStringCreateLocalized</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreateltor/">XmStringCreateLtoR</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreatesimple/">XmStringCreateSimple</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdirection/">XmStringDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdirectioncreate/">XmStringDirectionCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdirectiontodirection/">XmStringDirectionToDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdraw/">XmStringDraw</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdrawimage/">XmStringDrawImage</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdrawunderline/">XmStringDrawUnderline</a></code>(3), <code><a href="/docs/linux/man/3-xmstringempty/">XmStringEmpty</a></code>(3), <code><a href="/docs/linux/man/3-xmstringextent/">XmStringExtent</a></code>(3), <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3), <code><a href="/docs/linux/man/3-xmstringfreecontext/">XmStringFreeContext</a></code>(3), <code><a href="/docs/linux/man/3-xmstringgenerate/">XmStringGenerate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringgetltor/">XmStringGetLtoR</a></code>(3), <code><a href="/docs/linux/man/3-xmstringgetnextcomponent/">XmStringGetNextComponent</a></code>(3), <code><a href="/docs/linux/man/3-xmstringgetnextsegment/">XmStringGetNextSegment</a></code>(3), <code><a href="/docs/linux/man/3-xmstringgetnexttriple/">XmStringGetNextTriple</a></code>(3), <code><a href="/docs/linux/man/3-xmstringhassubstring/">XmStringHasSubstring</a></code>(3), <code><a href="/docs/linux/man/3-xmstringheight/">XmStringHeight</a></code>(3), <code><a href="/docs/linux/man/3-xmstringinitcontext/">XmStringInitContext</a></code>(3), <code><a href="/docs/linux/man/3-xmstringisvoid/">XmStringIsVoid</a></code>(3), <code><a href="/docs/linux/man/3-xmstringlength/">XmStringLength</a></code>(3), <code><a href="/docs/linux/man/3-xmstringlinecount/">XmStringLineCount</a></code>(3), <code><a href="/docs/linux/man/3-xmstringnconcat/">XmStringNConcat</a></code>(3), <code><a href="/docs/linux/man/3-xmstringncopy/">XmStringNCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmstringparsetext/">XmStringParseText</a></code>(3), <code><a href="/docs/linux/man/3-xmstringpeeknextcomponent/">XmStringPeekNextComponent</a></code>(3), <code><a href="/docs/linux/man/3-xmstringpeeknexttriple/">XmStringPeekNextTriple</a></code>(3), <code><a href="/docs/linux/man/3-xmstringputrendition/">XmStringPutRendition</a></code>(3), <code><a href="/docs/linux/man/3-xmstringsegmentcreate/">XmStringSegmentCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringseparatorcreate/">XmStringSeparatorCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringtable/">XmStringTable</a></code>(3), <code><a href="/docs/linux/man/3-xmstringtableparsestringarray/">XmStringTableParseStringArray</a></code>(3), <code><a href="/docs/linux/man/3-xmstringtableproposetablist/">XmStringTableProposeTablist</a></code>(3), <code><a href="/docs/linux/man/3-xmstringtabletoxmstring/">XmStringTableToXmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringtableunparse/">XmStringTableUnparse</a></code>(3), <code><a href="/docs/linux/man/3-xmstringtoxmstringtable/">XmStringToXmStringTable</a></code>(3), <code><a href="/docs/linux/man/3-xmstringunparse/">XmStringUnparse</a></code>(3), <code><a href="/docs/linux/man/3-xmstringwidth/">XmStringWidth</a></code>(3), <code><a href="/docs/linux/man/3-xmcvtxmstringtobytestream/">XmCvtXmStringToByteStream</a></code>(3), <code><a href="/docs/linux/man/3-xmcvtxmstringtoct/">XmCvtXmStringToCT</a></code>(3), <code><a href="/docs/linux/man/3-xmcvtcttoxmstring/">XmCvtCTToXmString</a></code>(3), and <code><a href="/docs/linux/man/3-xmcvtbytestreamtoxmstring/">XmCvtByteStreamToXmString</a></code>(3).</p>
