---
title: "brlapi_writearguments_t(3)"
name: "brlapi_writearguments_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_writearguments_t/"
description: "brlapi_writeArguments_t –"
---

<p>brlapi_writeArguments_t &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;brlapi.h&gt;</p>
<h3>Data Fields</h3>
<p>int <code>displayNumber</code> </p>
<p> unsigned int <code>regionBegin</code> </p>
<p> unsigned int <code>regionSize</code> </p>
<p> char * <code>text</code> </p>
<p> int <code>textSize</code> </p>
<p> unsigned char * <code>andMask</code> </p>
<p> unsigned char * <code>orMask</code> </p>
<p> int <code>cursor</code> </p>
<p> char * <code>charset</code> </p>
<h2>Detailed Description</h2>
<p>Structure containing arguments to be given to <code>brlapi_write()</code></p>
<h2>Field Documentation</h2>
<h3>unsigned char* brlapi_writeArguments_t::andMask</h3>
<p>And attributes; applied first</p>
<h3>char* brlapi_writeArguments_t::charset</h3>
<p>Text charset. NULL means it is assumed to be 8bits, and the same as the server&#8217;s. &#8221; means current locale&#8217;s charset. If no locale was selected, defaults to NULL&#8217;s meaning.</p>
<h3>int brlapi_writeArguments_t::cursor</h3>
<p><code>BRLAPI_CURSOR_LEAVE</code> == don&#8217;t touch, <code>BRLAPI_CURSOR_OFF</code> == turn off, 1 = 1st char of display, &#8230;</p>
<h3>int brlapi_writeArguments_t::displayNumber</h3>
<p>Display number <code>BRLAPI_DISPLAY_DEFAULT</code> == unspecified</p>
<h3>unsigned char* brlapi_writeArguments_t::orMask</h3>
<p>Or attributes; applied <i>after</i> ANDing</p>
<h3>unsigned int brlapi_writeArguments_t::regionBegin</h3>
<p>Region of display to update, 1st character of display is 1</p>
<h3>unsigned int brlapi_writeArguments_t::regionSize</h3>
<p>Number of characters held in text, andMask and orMask.</p>
<h3>char* brlapi_writeArguments_t::text</h3>
<p>Text to display, must hold as many characters as the region fields expresses.</p>
<h3>int brlapi_writeArguments_t::textSize</h3>
<p>Size of text in bytes. If -1, strlen() is used for computing it. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
