---
title: "aa_createedit(3)"
name: "aa_createedit"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aa_createedit/"
description: "aa_createedit – Simple interactive line editor provided as helper function."
---

<h2>NAME</h2>
<p> aa_createedit &#8211; Simple interactive line editor provided as helper function.</p>
<h2>SYNOPSIS</h2>
<p> <code> #include &lt;aalib.h&gt; </p>
<p> struct aa_edit *aa_createedit<br />
 (<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>aa_context *c,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int x,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int y,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int size,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>char *s,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int maxsize</p>
<p> ); </code></p>
<h2>PARAMETERS</h2>
<dl>
<dt><code>aa_context *c</code></p>
<dd> Specifies the AA-lib context to operate on.</p>
<dt><code>int x</code></p>
<dd> X coordinate of the edited text.</p>
<dt><code>int y</code></p>
<dd> Y coordinate of the edited text.</p>
<dt><code>int size</code></p>
<dd> Length of the editor window.</p>
<dt><code>char *s</code></p>
<dd> Buffer to edit (containing default value).</p>
<dt><code>int maxsize</code></p>
<dd> Size of the buffer.</dl>
<h2>DESCRIPTION</h2>
<p> You might use this function to input strings in AA-lib programs. This function initializes the aa_edit structure used by event-based editor. You might then call the aa_editkey function when key is pressed.</p>
<h2>RETURNS</h2>
<p> Pointer to edit context when succesfull and NULL on failure.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-save_d/">save_d</a>(3), <a href="/docs/linux/man/3-mem_d/">mem_d</a>(3), <a href="/docs/linux/man/3-aa_help/">aa_help</a>(3), <a href="/docs/linux/man/3-aa_formats/">aa_formats</a>(3), <a href="/docs/linux/man/3-aa_fonts/">aa_fonts</a>(3), <a href="/docs/linux/man/3-aa_dithernames/">aa_dithernames</a>(3), <a href="/docs/linux/man/3-aa_drivers/">aa_drivers</a>(3), <a href="/docs/linux/man/3-aa_kbddrivers/">aa_kbddrivers</a>(3), <a href="/docs/linux/man/3-aa_mousedrivers/">aa_mousedrivers</a>(3), <a href="/docs/linux/man/3-aa_kbdrecommended/">aa_kbdrecommended</a>(3), <a href="/docs/linux/man/3-aa_mouserecommended/">aa_mouserecommended</a>(3), <a href="/docs/linux/man/3-aa_displayrecommended/">aa_displayrecommended</a>(3), <a href="/docs/linux/man/3-aa_defparams/">aa_defparams</a>(3), <a href="/docs/linux/man/3-aa_defrenderparams/">aa_defrenderparams</a>(3), <a href="/docs/linux/man/3-aa_scrwidth/">aa_scrwidth</a>(3), <a href="/docs/linux/man/3-aa_scrheight/">aa_scrheight</a>(3), <a href="/docs/linux/man/3-aa_mmwidth/">aa_mmwidth</a>(3), <a href="/docs/linux/man/3-aa_mmheight/">aa_mmheight</a>(3), <a href="/docs/linux/man/3-aa_imgwidth/">aa_imgwidth</a>(3), <a href="/docs/linux/man/3-aa_imgheight/">aa_imgheight</a>(3), <a href="/docs/linux/man/3-aa_image/">aa_image</a>(3), <a href="/docs/linux/man/3-aa_text/">aa_text</a>(3), <a href="/docs/linux/man/3-aa_attrs/">aa_attrs</a>(3), <a href="/docs/linux/man/3-aa_currentfont/">aa_currentfont</a>(3), <a href="/docs/linux/man/3-aa_autoinit/">aa_autoinit</a>(3), <a href="/docs/linux/man/3-aa_autoinitkbd/">aa_autoinitkbd</a>(3), <a href="/docs/linux/man/3-aa_autoinitmouse/">aa_autoinitmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhi/">aa_recommendhi</a>(3), <a href="/docs/linux/man/3-aa_recommendlow/">aa_recommendlow</a>(3), <a href="/docs/linux/man/3-aa_init/">aa_init</a>(3), <a href="/docs/linux/man/3-aa_initkbd/">aa_initkbd</a>(3), <a href="/docs/linux/man/3-aa_initmouse/">aa_initmouse</a>(3), <a href="/docs/linux/man/3-aa_close/">aa_close</a>(3), <a href="/docs/linux/man/3-aa_uninitkbd/">aa_uninitkbd</a>(3), <a href="/docs/linux/man/3-aa_uninitmouse/">aa_uninitmouse</a>(3), <a href="/docs/linux/man/3-aa_fastrender/">aa_fastrender</a>(3), <a href="/docs/linux/man/3-aa_render/">aa_render</a>(3), <a href="/docs/linux/man/3-aa_puts/">aa_puts</a>(3), <a href="/docs/linux/man/3-aa_printf/">aa_printf</a>(3), <a href="/docs/linux/man/3-aa_gotoxy/">aa_gotoxy</a>(3), <a href="/docs/linux/man/3-aa_hidecursor/">aa_hidecursor</a>(3), <a href="/docs/linux/man/3-aa_showcursor/">aa_showcursor</a>(3), <a href="/docs/linux/man/3-aa_getmouse/">aa_getmouse</a>(3), <a href="/docs/linux/man/3-aa_hidemouse/">aa_hidemouse</a>(3), <a href="/docs/linux/man/3-aa_showmouse/">aa_showmouse</a>(3), <a href="/docs/linux/man/3-aa_registerfont/">aa_registerfont</a>(3), <a href="/docs/linux/man/3-aa_setsupported/">aa_setsupported</a>(3), <a href="/docs/linux/man/3-aa_setfont/">aa_setfont</a>(3), <a href="/docs/linux/man/3-aa_getevent/">aa_getevent</a>(3), <a href="/docs/linux/man/3-aa_getkey/">aa_getkey</a>(3), <a href="/docs/linux/man/3-aa_resize/">aa_resize</a>(3), <a href="/docs/linux/man/3-aa_resizehandler/">aa_resizehandler</a>(3), <a href="/docs/linux/man/3-aa_parseoptions/">aa_parseoptions</a>(3), <a href="/docs/linux/man/3-aa_edit/">aa_edit</a>(3), <a href="/docs/linux/man/3-aa_editkey/">aa_editkey</a>(3), <a href="/docs/linux/man/3-aa_putpixel/">aa_putpixel</a>(3), <a href="/docs/linux/man/3-aa_recommendhikbd/">aa_recommendhikbd</a>(3), <a href="/docs/linux/man/3-aa_recommendlowkbd/">aa_recommendlowkbd</a>(3), <a href="/docs/linux/man/3-aa_recommendhimouse/">aa_recommendhimouse</a>(3), <a href="/docs/linux/man/3-aa_recommendlowmouse/">aa_recommendlowmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhidisplay/">aa_recommendhidisplay</a>(3), <a href="/docs/linux/man/3-aa_recommendlowdisplay/">aa_recommendlowdisplay</a>(3) </p>
<h2>Index</h2>
