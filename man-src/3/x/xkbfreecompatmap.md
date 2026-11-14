---
title: "xkbfreecompatmap(3)"
name: "xkbfreecompatmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreecompatmap/"
description: "XkbFreeCompatMap – Free an entire compatibility map or selected portions of one"
---

<p>XkbFreeCompatMap &#8211; Free an entire compatibility map or selected portions of one </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeCompatMap</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>Bool </code><i>free_map</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>Xkb description in which to free compatibility map</p>
<dt><i>&#8211; which</i></p>
<dd>mask of compatibility map components to free</p>
<dt><i>&#8211; free_map</i></p>
<dd>True =&gt; free XkbCompatMap structure itself</dl>
<h2>Description</h2>
<p><i>which </i> specifies the compatibility map components to be freed (see XkbGetCompatMap). <i>which </i> is an inclusive OR of the bits shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Compatibility Map Component Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask</td>
<td>Value</td>
<td>Affecting
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbSymInterpMask</td>
<td>(1&lt;&lt;0)</td>
<td>Symbol interpretations
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroupCompatMask</td>
<td>(1&lt;&lt;1)</td>
<td>Group maps
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllCompatMask</td>
<td>(0x3)</td>
<td>All compatibility map components
</td>
</tr>
</table>
<p> <i>free_map </i> indicates whether the XkbCompatMap structure itself should be freed. If <i>free_map </i> is True, <i>which </i> is ignored, all non-NULL compatibility map components are freed, and the <i>compat </i> field in the XkbDescRec referenced by <i>xkb </i> is set to NULL.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbCompatMapRec {
 XkbSymInterpretPtr sym_interpret; /* symbol based key semantics*/
 XkbModsRec groups[XkbNumKbdGroups]; /* group =&gt; modifier map */
 unsigned short num_si; /* # structures used in sym_interpret */
 unsigned short size_si; /* # structures allocated in sym_interpret */
 } XkbCompatMapRec, *XkbCompatMapPtr;</pre>
<p>The complete description of an Xkb keyboard is given by an XkbDescRec. The component structures in the XkbDescRec represent the major Xkb components outlined in Figure 1.1. </p>
<pre>typedef struct {
 struct _XDisplay * display; /* connection to X server */
 unsigned short flags; /* private to Xkb, do not modify */
 unsigned short device_spec; /* device of interest */
 KeyCode min_key_code; /* minimum keycode for device */
 KeyCode max_key_code; /* maximum keycode for device */
 XkbControlsPtr ctrls; /* controls */
 XkbServerMapPtr server; /* server keymap */
 XkbClientMapPtr map; /* client keymap */
 XkbIndicatorPtr indicators; /* indicator map */
 XkbNamesPtr names; /* names for all components */
 XkbCompatMapPtr compat; /* compatibility map */
 XkbGeometryPtr geom; /* physical geometry of keyboard */
} XkbDescRec, *XkbDescPtr;</pre>
<p>The <i>display </i> field points to an X display structure. The <i>flags field is private to the library: modifying </i> <i>flags </i> may yield unpredictable results. The <i>device_spec </i> field specifies the device identifier of the keyboard input device, or XkbUseCoreKeyboard, which specifies the core keyboard device. The <i>min_key_code</i> and <i>max_key_code </i> fields specify the least and greatest keycode that can be returned by the keyboard. The other fields specify structure components of the keyboard description and are described in detail in other sections of this document. Table 2 identifies the subsequent sections of this document that discuss the individual components of the XkbDescRec. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 2 XkbDescRec Component References
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbDescRec Field</td>
<td>For more info
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ctrls</td>
<td>Chapter 10
</td>
</tr>
<tr VALIGN=top>
<td>server</td>
<td>Chapter 16
</td>
</tr>
<tr VALIGN=top>
<td>map</td>
<td>Chapter 15
</td>
</tr>
<tr VALIGN=top>
<td>indicators</td>
<td>Chapter 8
</td>
</tr>
<tr VALIGN=top>
<td>names</td>
<td>Chapter 18
</td>
</tr>
<tr VALIGN=top>
<td>compat</td>
<td>Chapter 17
</td>
</tr>
<tr VALIGN=top>
<td>geom</td>
<td>Chapter 13
</td>
</tr>
</table>
<p> Each structure component has a corresponding mask bit that is used in function calls to indicate that the structure should be manipulated in some manner, such as allocating it or freeing it. These masks and their relationships to the fields in the XkbDescRec are shown in Table 3. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 3 Mask Bits for XkbDescRec
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask Bit</td>
<td>XkbDescRec Field</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>XkbControlsMask</td>
<td>ctrls</td>
<td>(1L&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td>XkbServerMapMask</td>
<td>server</td>
<td>(1L&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIClientMapMask</td>
<td>map</td>
<td>(1L&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIndicatorMapMask</td>
<td>indicators</td>
<td>(1L&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td>XkbNamesMask</td>
<td>names</td>
<td>(1L&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td>XkbCompatMapMask</td>
<td>compat</td>
<td>(1L&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td>XkbGeometryMask</td>
<td>geom</td>
<td>(1L&lt;&lt;6)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllComponentsMask</td>
<td>All Fields</td>
<td>(0x7f)
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetcompatmap/">XkbGetCompatMap</a></code>(3)</p>
