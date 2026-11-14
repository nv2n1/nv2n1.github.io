---
title: "tk_canvastextinfo(3)"
name: "tk_canvastextinfo"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_canvastextinfo/"
description: "Tk_CanvasTextInfo – additional information for managing text items in canvases"
---

<p>Tk_CanvasTextInfo &#8211; additional information for managing text items in canvases </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_CanvasTextInfo *
<code>Tk_CanvasGetTextInfo</code>(<i>canvas</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Canvas <i>canvas</i> (in) A token that identifies a particular canvas widget. </p>
</dl>
<h2>Description</h2>
<p>Textual canvas items are somewhat more complicated to manage than other items, due to things like the selection and the input focus. <code>Tk_CanvasGetTextInfo</code> may be invoked by a type manager to obtain additional information needed for items that display text. The return value from <code>Tk_CanvasGetTextInfo</code> is a pointer to a structure that is shared between Tk and all the items that display text. The structure has the following form:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tk_CanvasTextInfo {
 Tk_3DBorder <i>selBorder</i>;
 int <i>selBorderWidth</i>;
 XColor *<i>selFgColorPtr</i>;
 Tk_Item *<i>selItemPtr</i>;
 int <i>selectFirst</i>;
 int <i>selectLast</i>;
 Tk_Item *<i>anchorItemPtr</i>;
 int <i>selectAnchor</i>;
 Tk_3DBorder <i>insertBorder</i>;
 int <i>insertWidth</i>;
 int <i>insertBorderWidth</i>;
 Tk_Item *<i>focusItemPtr</i>;
 int <i>gotFocus</i>;
 int <i>cursorOn</i>;
} Tk_CanvasTextInfo;</pre>
</dl>
<p> The <code>selBorder</code> field identifies a Tk_3DBorder that should be used for drawing the background under selected text. <i>selBorderWidth</i> gives the width of the raised border around selected text, in pixels. <i>selFgColorPtr</i> points to an XColor that describes the foreground color to be used when drawing selected text. <i>selItemPtr</i> points to the item that is currently selected, or NULL if there is no item selected or if the canvas does not have the selection. <i>selectFirst</i> and <i>selectLast</i> give the indices of the first and last selected characters in <i>selItemPtr</i>, as returned by the <i>indexProc</i> for that item. <i>anchorItemPtr</i> points to the item that currently has the selection anchor; this is not necessarily the same as <i>selItemPtr</i>. <i>selectAnchor</i> is an index that identifies the anchor position within <i>anchorItemPtr</i>. <i>insertBorder</i> contains a Tk_3DBorder to use when drawing the insertion cursor; <i>insertWidth</i> gives the total width of the insertion cursor in pixels, and <i>insertBorderWidth</i> gives the width of the raised border around the insertion cursor. <i>focusItemPtr</i> identifies the item that currently has the input focus, or NULL if there is no such item. <i>gotFocus</i> is 1 if the canvas widget has the input focus and 0 otherwise. <i>cursorOn</i> is 1 if the insertion cursor should be drawn in <i>focusItemPtr</i> and 0 if it should not be drawn; this field is toggled on and off by Tk to make the cursor blink. </p>
<p> The structure returned by <code>Tk_CanvasGetTextInfo</code> is shared between Tk and the type managers; typically the type manager calls <code>Tk_CanvasGetTextInfo</code> once when an item is created and then saves the pointer in the item&#8217;s record. Tk will update information in the Tk_CanvasTextInfo; for example, a <code>configure</code> widget command might change the <i>selBorder</i> field, or a <code>select</code> widget command might change the <i>selectFirst</i> field, or Tk might change <i>cursorOn</i> in order to make the insertion cursor flash on and off during successive redisplays. </p>
<p> Type managers should treat all of the fields of the Tk_CanvasTextInfo structure as read-only, except for <i>selItemPtr</i>, <i>selectFirst</i>, <i>selectLast</i>, and <i>selectAnchor</i>. Type managers may change <i>selectFirst</i>, <i>selectLast</i>, and <i>selectAnchor</i> to adjust for insertions and deletions in the item (but only if the item is the current owner of the selection or anchor, as determined by <i>selItemPtr</i> or <i>anchorItemPtr</i>). If all of the selected text in the item is deleted, the item should set <i>selItemPtr</i> to NULL to indicate that there is no longer a selection. </p>
<h2>Keywords</h2>
<p>canvas, focus, insertion cursor, selection, selection anchor, text</p>
