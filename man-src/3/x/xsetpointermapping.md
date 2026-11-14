---
title: "xsetpointermapping(3)"
name: "xsetpointermapping"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetpointermapping/"
description: "XSetPointerMapping, XGetPointerMapping – manipulate pointer settings"
---

<p>XSetPointerMapping, XGetPointerMapping &#8211; manipulate pointer settings </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetPointerMapping(Display *<i>display</i>, unsigned char <i>map</i>[], int <i>nmap</i>);</p>
<dd>int XGetPointerMapping(Display *<i>display</i>, unsigned char <i>map_return</i>[], int <i>nmap</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>map</i></p>
<dd>Specifies the mapping list.</p>
<dt><i>map_return</i></p>
<dd>Returns the mapping list.</p>
<dt><i>nmap</i></p>
<dd>Specifies the number of items in the mapping list.</dl>
<h2>Description</h2>
<p>The <code>XSetPointerMapping</code> function sets the mapping of the pointer. If it succeeds, the X server generates a <code>MappingNotify</code> event, and <code>XSetPointerMapping</code> returns <code>MappingSuccess</code>. Element map[i] defines the logical button number for the physical button i+1. The length of the list must be the same as <code>XGetPointerMapping</code> would return, or a <code>BadValue</code> error results. A zero element disables a button, and elements are not restricted in value by the number of physical buttons. However, no two elements can have the same nonzero value, or a <code>BadValue</code> error results. If any of the buttons to be altered are logically in the down state, <code>XSetPointerMapping</code> returns <code>MappingBusy</code>, and the mapping is not changed. </p>
<p> <code>XSetPointerMapping</code> can generate a <code>BadValue</code> error. </p>
<p> The <code>XGetPointerMapping</code> function returns the current mapping of the pointer. Pointer buttons are numbered starting from one. <code>XGetPointerMapping</code> returns the number of physical buttons actually on the pointer. The nominal mapping for a pointer is map[i]=i+1. The nmap argument specifies the length of the array where the pointer mapping is returned, and only the first nmap elements are returned in map_return.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangekeyboardcontrol/">XChangeKeyboardControl</a>(3), <a href="/docs/linux/man/3-xchangekeyboardmapping/">XChangeKeyboardMapping</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
