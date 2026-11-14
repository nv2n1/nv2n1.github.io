---
title: "cdk_draw(3)"
name: "cdk_draw"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_draw/"
description: "cdk_draw – Cdk Drawing Functions"
---

<h2 class="name">NAME</h2>
<p> cdk_draw &#8211; Cdk Drawing Functions </p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>

void boxWindow(
    WINDOW *window,
    chtype attr);
void attrbox(
    WINDOW *win,
    chtype tlc,
    chtype trc,
    chtype blc,
    chtype brc,
    chtype horz,
    chtype vert,
    chtype attr);
void drawObjBox(
    WINDOW *win,
    CDKOBJS *object);
void drawLine(
    WINDOW *window,
    int startx,
    int starty,
    int endx,
    int endy,
    chtype line);
void drawShadow(
    WINDOW *shadowWin);
void writeBlanks(
    WINDOW *window,
    int xpos,
    int ypos,
    int align,
    int start,
    int end);
void writeChar(
    WINDOW *window,
    int xpos,
    int ypos,
    char *string,
    int align,
    int start,
    int end);
void writeCharAttrib(
    WINDOW *window,
    int xpos,
    int ypos,
    char *string,
    chtype attr,
    int align,
    int start,
    int end);
void writeChtype(
    WINDOW *window,
    int xpos,
    int ypos,
    chtype *string,
    int align,
    int start,
    int end);
void writeChtypeAttrib(
    WINDOW *window,
    int xpos,
    int ypos,
    chtype *string,
    chtype attr,
    int align,
    int start,
    int end);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> These functions perform useful drawing and attribute operations.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>boxWindow</code></p>
<dd> draw a box with on the window <i>win</i>. Like <code>attrbox</code>, this function ORs <i>attr</i> with each character as it draws the box.</p>
<dt><code>attrbox</code></p>
<dd> draw a box with on the window <i>win</i> letting the caller define each element of the box.</p>
<dt>
<dd> The parameters <i>tlc</i>, <i>trc</i>, <i>blc</i>, <i>brc</i> are used for the top-left, top-right, bottom-left and bottom-right corners respectively. The parameters <i>horz</i> and <i>vert</i> are used for the horizontal and vertical sides of the box. Any of these parameters may be zero. In that case, the function skips the corresponding element of the box.</p>
<dt>
<dd> The function ORs <i>attr</i> with each character as it draws the box.</p>
<dt><code>drawObjBox</code></p>
<dd> Draw a box around the given window <i>win</i> using the <i>object</i>&#8216;s defined line-drawing characters.</p>
<dt><code>drawLine</code></p>
<dd> draw a line on the given window.</p>
<dt>
<dd> The parameters <i>starty</i>, <i>startx</i> are the starting coordinates. The parameters <i>endy</i>, <i>endx</i> are the ending coordinates. The function writes the data in <i>line</i> to each coordinate in that range including the start/end coordinates.</p>
<dt>
<dd> The function handles lines other than vertical or horizontal, but normally it is used for that, e.g., with <i>line</i> set to <code>ACS_HLINE</code> or <code>ACS_VLINE</code>.</p>
<dt><code>drawShadow</code></p>
<dd> draw a shadow on the right and bottom edges of a window.</p>
<dt><code>writeBlanks</code></p>
<dd> write a string of blanks, using <code>writeChar</code>. The parameters are passed to <code>writeChar</code> as is. There is no corresponding <code>writeBlanksAttrib</code> function.</p>
<dt><code>writeChar</code></p>
<dd> writes out a <code>char&nbsp;<wbr>*</code> string without adding attributes. The parameters are passed to <code>writeCharAttrib</code> as is.</p>
<dt><code>writeCharAttrib</code></p>
<dd> writes out a <code>char&nbsp;<wbr>*</code> string with the given attributes added. The string is written to the given <i>window</i>, using its relative screen coordinates <i>ypos</i> and <i>xpos</i>.</p>
<dt>
<dd> Compare with <code>writeChtypeAttrib</code>, which writes a <code>chtype&nbsp;<wbr>*</code> string.</p>
<dt>
<dd> The function ORs the attribute <i>attr</i> with each item from the string. For instance, it may be <code>A_BOLD</code>. The <i>align</i> parameter controls whether it is written horizontally (<code>HORIZONTAL</code>) or vertically (<code>VERTICAL</code>).</p>
<dt>
<dd> Finally, only a subset of the string is written. The function starts with the data from the <i>start</i> item of <i>string</i>, and ends before the <i>end</i> item. If <i>start</i> is greater than, or equal to <i>end</i>, no data is written.</p>
<dt><code>writeChtype</code></p>
<dd> writes out a <code>chtype&nbsp;<wbr>*</code> string without adding attributes. The parameters are passed to <code>writeChtypeAttrib</code> as is.</p>
<dt><code>writeChtypeAttrib</code></p>
<dd> writes out a <i>chtype&nbsp;<wbr>*</i> string with the given attributes added. The string is written to the given <i>window</i>, using its relative screen coordinates <i>ypos</i> and <i>xpos</i>. You would normally construct the string from a <i>char&nbsp;<wbr>*</i> string using <code>char2Chtype</code> (3).</p>
<dt>
<dd> The function ORs the attribute <i>attr</i> with each item from the string. For instance, it may be <code>A_BOLD</code>. The <i>align</i> parameter controls whether it is written horizontally (<code>HORIZONTAL</code>) or vertically (<code>VERTICAL</code>).</p>
<dt>
<dd> Finally, only a subset of the string is written. The function starts with the data from the <i>start</i> item of <i>string</i>, and ends before the <i>end</i> item. If <i>start</i> is greater than, or equal to <i>end</i>, no data is written.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_util/">cdk_util</a></code>(3) </p>
<h2>Index</h2>
