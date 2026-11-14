---
title: "xmrendertable(3)"
name: "xmrendertable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertable/"
description: "XmRenderTable — Data type for a render table"
---

<p><code>XmRenderTable</code> &#8212; Data type for a render table</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
XmRenderTable</pre>
<h2>Description</h2>
<p><code>XmRenderTable</code> is the data type for a render table, which contains a table of renditions (<code>XmRendition</code>s). Each rendition consists of a set of attributes for rendering text, including a font or fontset, colors, tabs, and lines. Each rendition is identified with a tag. </p>
<p> When a compound string is displayed, for each segment in the string, the rendition used to render that string is formed as follows. If the segment has at least one rendition begin tag or if the list of tags formed by accumulating from previous segments the rendition begin tags and removing the rendition end tags is not empty, these tags are matched with renditions in the render table. The effective rendition used to render the segment is formed by successively merging each rendition found into the current rendition with non-<code>XmAS_IS</code> (<code>XmUNSPECIFIED_PIXEL</code> for color resources) values for resources in the rendition to be merged, thus replacing the corresponding values of the resources in the current rendition. Finally, if the resulting rendition still has resources with unspecified values and the segment has a locale or charset tag (these are optional and mutually exclusive) this tag is matched with a rendition in the render table, and the missing rendition values are filled in from that entry. </p>
<p> If no matching rendition is found for a particular tag, then the <code>XmNnoRenditionCallback</code> of the <code>XmDisplay</code> object is called and the render table is searched again for that tag. </p>
<p> If the resulting rendition does not specify a font or fontset, then for segments whose text type is <code>XmCHARSET_TEXT</code>, the render table will be searched for a rendition tagged with <code>XmFONTLIST_DEFAULT_TAG</code>, and if a matching rendition is found, it will be merged into the current rendition. If the resulting rendition contains no font or fontset, the <code>XmNnoFontCallback</code> will be called with the default rendition and &quot;&quot; as the font name. If no rendition matches or no font was found after the callback, then the first rendition in the render table will be merged into the current rendition. If this rendition still has no font, then the segment will not be rendered and a warning will be emitted. </p>
<p> For segments whose text type is <code>XmMULTIBYTE_TEXT</code> or <code>XmWIDECHAR_TEXT</code>, the render table will be searched for a rendition tagged with <code>_MOTIF_DEFAULT_LOCALE</code>, and, if a matching rendition is found, it will be merged into the current rendition. If the resulting rendition contains no font, the <code>XmNnoFontCallback</code> will be called with the default rendition and &quot;&quot; as the font name. An application can have this callback attempt to remedy this problem by calling <code>XmRenditionUpdate</code> on the input rendition to provide a font for the widget to use. This may be done by either providing an alternative font name to be loaded using the <code>XmNfontName</code> and <code>XmNfontType</code> resources or with an already loaded font using the <code>XmNfont</code> resource. If no rendition matches or no font was found after the callback, then the segment will not be rendered and a warning will be issued. </p>
<p> Render tables are specified in resource files with the following syntax: </p>
<pre><i>resource_spec</i>: [ <i>tag</i> [, <i>tag</i> ]* ]</pre>
<p>where <i>tag</i> is some string suitable for the <code>XmNtag</code> resource of a rendition. </p>
<p> If no tags are specified, then a render table will be created that is either empty or contains only a rendition with a tag of <code>_MOTIF_DEFAULT_LOCALE</code>. </p>
<p> Specific values for specific rendition resources are specified using the following syntax: </p>
<pre><i>resource_spec</i> [*|.] <i>rendition</i>[*|.] <i>resource_name</i>: <i>value</i></pre>
<p>where:</p>
<dl COMPACT>
<dt><i>resource_spec</i></p>
<dd>Specifies the render table.</p>
<dt><i>rendition</i></p>
<dd>Is either the class Rendition or a tag.</p>
<dt><i>resource_name</i></p>
<dd>Is either the class or name of a particular resource.</p>
<dt><i>value</i></p>
<dd>Is the specification of the value to be set.</dl>
<p> Any resource line that consists of just a resource name or class component with no rendition component or loose binding will be assumed to specify resource values for a rendition with a tag of <code>_MOTIF_DEFAULT_LOCALE</code>. In effect, this creates a default rendition in much the same way that specifying no fontlist tag for a fontlist resource causes the fontlist created to contain an entry tagged with <code>XmFONTLIST_DEFAULT_TAG</code>: </p>
<pre><i>resource_spec</i>.<i>resource_name</i>: <i>value</i></pre>
<p>For example, the following would set the <code>XmNrenderTable</code> resource of <code>label1</code> to a render table consisting of three renditions tagged with <code>_MOTIF_DEFAULT_LOCALE</code>, <i>bold</i>, and <i>oblique</i>, with values for resources set as described in the resource specifications. </p>
<pre><tt>*label1.renderTable: bold, oblique
*label1.renderTable.bold.renditionForeground: Green
*label1.renderTable.bold.fontName: *-*-*-bold-*-iso8859-1
*label1.renderTable.bold.fontType: FONT_IS_FONT
*label1.renderTable.oblique.renditionBackground: Red
*label1.renderTable.oblique.fontName: *-*-*-italic-*-iso8859-1
*label1.renderTable.oblique.fontType: FONT_IS_FONT
*label1.renderTable.oblique.underlineType: AS_IS
*label1.renderTable.fontName: fixed
*label1.renderTable.fontType: FONT_IS_FONT
*label1.renderTable.renditionForegound: black
*label1.renderTable*tabList: 1in, +1.5in, +3in</tt></pre>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendertableaddrenditions/">XmRenderTableAddRenditions</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablecopy/">XmRenderTableCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablecvtfromprop/">XmRenderTableCvtFromProp</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablecvttoprop/">XmRenderTableCvtToProp</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablefree/">XmRenderTableFree</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablegetrendition/">XmRenderTableGetRendition</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablegetrenditions/">XmRenderTableGetRenditions</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablegettags/">XmRenderTableGetTags</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertableremoverenditions/">XmRenderTableRemoveRenditions</a></code>(3), <code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
