---
title: "tk_getdash(3)"
name: "tk_getdash"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getdash/"
description: "Tk_GetDash – convert from string to valid dash structure."
---

<p>Tk_GetDash &#8211; convert from string to valid dash structure. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetDash</code>(<i>interp, string, dashPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>const char * <i>string</i> (in) Textual value to be converted.</p>
<dd>Tk_Dash <i>*dashPtr</i> (out) Points to place to store the dash pattern value converted from <i>string</i>. </p>
</dl>
<h2>Description</h2>
<p>These procedure parses the string and fills in the result in the Tk_Dash structure. The string can be a list of integers or a character string containing only &#8220;<code>.,-_</code>&#8221; or spaces. If all goes well, <code>TCL_OK</code> is returned. If <i>string</i> does not have the proper syntax then <code>TCL_ERROR</code> is returned, an error message is left in the interpreter&#8217;s result, and nothing is stored at *<i>dashPtr</i>. </p>
<p> The first possible syntax is a list of integers. Each element represents the number of pixels of a line segment. Only the odd segments are drawn using the &#8220;outline&#8221; color. The other segments are drawn transparent. </p>
<p> The second possible syntax is a character list containing only 5 possible characters &#8220;<code>.,-_ </code>&#8221;. The space can be used to enlarge the space between other line elements, and can not occur as the first position in the string. Some examples:</p>
<dl COMPACT>
<dd>
<pre> -dash . = -dash {2 4}
 -dash - = -dash {6 4}
 -dash -. = -dash {6 4 2 4}
 -dash -.. = -dash {6 4 2 4 2 4}
 -dash {. } = -dash {2 8}
 -dash , = -dash {4 4}</pre>
</dl>
<p> The main difference of this syntax with the previous is that it is shape-conserving. This means that all values in the dash list will be multiplied by the line width before display. This assures that &#8220;.&#8221; will always be displayed as a dot and &#8220;-&#8221; always as a dash regardless of the line width. </p>
<p> On systems where only a limited set of dash patterns, the dash pattern will be displayed as the most close dash pattern that is available. For example, on Windows only the first 4 of the above examples are available. The last 2 examples will be displayed identically as the first one. </p>
<h2>Keywords</h2>
<p>dash, conversion</p>
