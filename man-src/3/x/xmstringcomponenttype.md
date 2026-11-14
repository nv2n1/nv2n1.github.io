---
title: "xmstringcomponenttype(3)"
name: "xmstringcomponenttype"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringcomponenttype/"
description: "XmStringComponentType — Data type for compound string components"
---

<p><code>XmStringComponentType</code> &#8212; Data type for compound string components</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmStringComponentType</code> is the data type specifying compound string component types. A compound string component identifies some part of a compound string, and can have a value and length. A compound string component can be one of the following types. These component types are grouped according to their length and value types. </p>
<p> The following components have values of NULL and lengths of 0 (zero).</p>
<dl COMPACT>
<dt><code>XmSTRING_COMPONENT_SEPARATOR</code></p>
<dd>This component usually maps to a newline or carriage return in displayed text.</p>
<dt><code>XmSTRING_COMPONENT_TAB</code></p>
<dd>This component may be thought of as a text component containing only a single tab.</p>
<dt><code>XmSTRING_COMPONENT_LAYOUT_POP</code></p>
<dd>The layout direction is kept on a stack, with the current direction kept on top of the stack. When this component is read, the most recently read layout direction is popped off the stack and replaced by the direction immediately before it.</p>
<dt><code>XmSTRING_COMPONENT_END</code></p>
<dd>This component marks the end of a compound string. No other components should follow. If an application does not place an <code>XmSTRING_COMPONENT_END</code> component at the end of an <code>XmString</code>, Motif automatically does it for the application.</dl>
<p> The following component has a value of <code>XmDirection</code> and the length of that direction.</p>
<dl COMPACT>
<dt><code>XmSTRING_COMPONENT_LAYOUT_PUSH</code></p>
<dd>The layout direction is kept on a stack, with the current direction kept on top of the stack. This component replaces the current layout direction, and causes another to be pushed onto the top of this stack.</dl>
<p> The following component has a value of <code>XmStringDirection</code> and the length of that direction.</p>
<dl COMPACT>
<dt><code>XmSTRING_COMPONENT_DIRECTION</code></p>
<dd>This component sets the string direction by overriding the previous string direction.</dl>
<p> The following components have values of type <code>char *</code> or some equivalent type, and the lengths of these types.</p>
<dl COMPACT>
<dt><code>XmSTRING_COMPONENT_LOCALE_TEXT</code></p>
<dd>This component contains the multibyte text of a compound string.</p>
<dt><code>XmSTRING_COMPONENT_WIDECHAR_TEXT</code></p>
<dd>This component contains the widechar text of a compound string.</p>
<dt><code>XmSTRING_COMPONENT_TEXT</code></p>
<dd>This component contains the charset text of a compound string. Note that a compound string cannot contain both charset and locale (multibyte or widechar) text.</p>
<dt><code>XmSTRING_COMPONENT_RENDITION_BEGIN</code></p>
<dd>This component marks the beginning of a new rendition. All text following this component will be rendered using this rendition as the primary one. If there is already a rendition in effect, it is kept in memory and used to fill in any unspecified values in the primary rendition. Renditions are kept until a corresponding <code>XmSTRING_COMPONENT_RENDITION_END</code> component is encountered.</p>
<dt><code>XmSTRING_COMPONENT_RENDITION_END</code></p>
<dd>This component signifies that the specified rendition will no longer be used to render text, and will not be available to fill in unspecified values of newer renditions.</p>
<dt><code>XmSTRING_COMPONENT_UNKNOWN</code></p>
<dd>This component type signifies that the component contents belong to an unknown component type.</p>
<dt><code>XmSTRING_COMPONENT_LOCALE</code></p>
<dd>Use this component to specify the locale in which an internationalized application is to execute. The only valid character string for this component is <code>_MOTIF_DEFAULT_LOCALE</code>.</p>
<dt><code>XmSTRING_COMPONENT_TAG</code></p>
<dd>For charset text, this is the tag of the font to be used to display the text. This tag is sometimes referred to as the charset tag or the fontlist tag.</p>
<dt><code>XmSTRING_COMPONENT_CHARSET</code></p>
<dd>This component is obsolete and remains for compatibility with previous releases. It has been replaced by <code>XmSTRING_COMPONENT_TAG</code>.</p>
<dt><code>XmSTRING_COMPONENT_FONTLIST_ELEMENT_TAG</code></p>
<dd>This component is obsolete and remains for compatibility with previous releases. It has been replaced by <code>XmSTRING_COMPONENT_TAG</code>.</dl>
<p> Some compound string components depend on values defined in other components. The <code>XmSTRING_COMPONENT_TAB</code> component definition, for example, depends on information in the <code>XmSTRING_COMPONENT_RENDITION_BEGIN</code>. To account for these dependencies, a typical compound string will have its member components in the following order: </p>
<pre>[
 [ <code>XmSTRING_COMPONENT_LAYOUT_PUSH</code> ]
 [ <code>XmSTRING_COMPONENT_RENDITION_BEGIN</code> ]*
 [ <code>XmSTRING_COMPONENT_TAG</code> | <code>XmSTRING_COMPONENT_LOCALE</code> ]
 [ <code>XmSTRING_COMPONENT_TAB</code> ]*
 [ <code>XmSTRING_COMPONENT_DIRECTION</code> ]
 [ <code>XmSTRING_COMPONENT_TEXT</code> |
 <code>XmSTRING_COMPONENT_LOCALE_TEXT</code> |
 <code>XmSTRING_COMPONENT_WIDECHAR_TEXT</code> ]
 [ <code>XmSTRING_COMPONENT_RENDITION_END</code> ]*
 [ <code>XmSTRING_COMPONENT_LAYOUT_POP</code> ]
 [ <code>XmSTRING_COMPONENT_SEPARATOR</code> ]
]*
<code>XmSTRING_COMPONENT_END</code></pre>
