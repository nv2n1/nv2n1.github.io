---
title: "aa_fastrender(3)"
name: "aa_fastrender"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aa_fastrender/"
description: "aa_fastrender – simple and fast AA-lib rendering function."
---

<h2>NAME</h2>
<p> aa_fastrender &#8211; simple and fast AA-lib rendering function.</p>
<h2>SYNOPSIS</h2>
<p> <code> #include &lt;aalib.h&gt; </p>
<p> void aa_fastrender<br />
 (<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>aa_context *c,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int x1,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int y1,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int x2,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int y2</p>
<p> ); </code></p>
<h2>PARAMETERS</h2>
<dl>
<dt><code>aa_context *c</code></p>
<dd> Specifies the AA-lib context to operate on.</p>
<dt><code>int x1</code></p>
<dd> Column of top left coner of rendered area (in characters!).</p>
<dt><code>int y1</code></p>
<dd> Row of top left coner of rendered area.</p>
<dt><code>int x2</code></p>
<dd> Column of bottom right coner of rendered area.</p>
<dt><code>int y2</code></p>
<dd> Row of bottom right coner of rendered area.</dl>
<h2>DESCRIPTION</h2>
<p> This function does the trick of converting the emulated framebuffer into high quality ASCII-art. It is slightly faster and less flexible the aa_render function. </p>
<p> Note that to see the effect you need to call aa_flush too. </p>
<p> First call to this function may take a while, because the rendering tables are produced.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-save_d/">save_d</a>(3), <a href="/docs/linux/man/3-mem_d/">mem_d</a>(3), <a href="/docs/linux/man/3-aa_help/">aa_help</a>(3), <a href="/docs/linux/man/3-aa_formats/">aa_formats</a>(3), <a href="/docs/linux/man/3-aa_fonts/">aa_fonts</a>(3), <a href="/docs/linux/man/3-aa_dithernames/">aa_dithernames</a>(3), <a href="/docs/linux/man/3-aa_drivers/">aa_drivers</a>(3), <a href="/docs/linux/man/3-aa_kbddrivers/">aa_kbddrivers</a>(3), <a href="/docs/linux/man/3-aa_mousedrivers/">aa_mousedrivers</a>(3), <a href="/docs/linux/man/3-aa_kbdrecommended/">aa_kbdrecommended</a>(3), <a href="/docs/linux/man/3-aa_mouserecommended/">aa_mouserecommended</a>(3), <a href="/docs/linux/man/3-aa_displayrecommended/">aa_displayrecommended</a>(3), <a href="/docs/linux/man/3-aa_defparams/">aa_defparams</a>(3), <a href="/docs/linux/man/3-aa_defrenderparams/">aa_defrenderparams</a>(3), <a href="/docs/linux/man/3-aa_scrwidth/">aa_scrwidth</a>(3), <a href="/docs/linux/man/3-aa_scrheight/">aa_scrheight</a>(3), <a href="/docs/linux/man/3-aa_mmwidth/">aa_mmwidth</a>(3), <a href="/docs/linux/man/3-aa_mmheight/">aa_mmheight</a>(3), <a href="/docs/linux/man/3-aa_imgwidth/">aa_imgwidth</a>(3), <a href="/docs/linux/man/3-aa_imgheight/">aa_imgheight</a>(3), <a href="/docs/linux/man/3-aa_image/">aa_image</a>(3), <a href="/docs/linux/man/3-aa_text/">aa_text</a>(3), <a href="/docs/linux/man/3-aa_attrs/">aa_attrs</a>(3), <a href="/docs/linux/man/3-aa_currentfont/">aa_currentfont</a>(3), <a href="/docs/linux/man/3-aa_autoinit/">aa_autoinit</a>(3), <a href="/docs/linux/man/3-aa_autoinitkbd/">aa_autoinitkbd</a>(3), <a href="/docs/linux/man/3-aa_autoinitmouse/">aa_autoinitmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhi/">aa_recommendhi</a>(3), <a href="/docs/linux/man/3-aa_recommendlow/">aa_recommendlow</a>(3), <a href="/docs/linux/man/3-aa_init/">aa_init</a>(3), <a href="/docs/linux/man/3-aa_initkbd/">aa_initkbd</a>(3), <a href="/docs/linux/man/3-aa_initmouse/">aa_initmouse</a>(3), <a href="/docs/linux/man/3-aa_close/">aa_close</a>(3), <a href="/docs/linux/man/3-aa_uninitkbd/">aa_uninitkbd</a>(3), <a href="/docs/linux/man/3-aa_uninitmouse/">aa_uninitmouse</a>(3), <a href="/docs/linux/man/3-aa_render/">aa_render</a>(3), <a href="/docs/linux/man/3-aa_puts/">aa_puts</a>(3), <a href="/docs/linux/man/3-aa_printf/">aa_printf</a>(3), <a href="/docs/linux/man/3-aa_gotoxy/">aa_gotoxy</a>(3), <a href="/docs/linux/man/3-aa_hidecursor/">aa_hidecursor</a>(3), <a href="/docs/linux/man/3-aa_showcursor/">aa_showcursor</a>(3), <a href="/docs/linux/man/3-aa_getmouse/">aa_getmouse</a>(3), <a href="/docs/linux/man/3-aa_hidemouse/">aa_hidemouse</a>(3), <a href="/docs/linux/man/3-aa_showmouse/">aa_showmouse</a>(3), <a href="/docs/linux/man/3-aa_registerfont/">aa_registerfont</a>(3), <a href="/docs/linux/man/3-aa_setsupported/">aa_setsupported</a>(3), <a href="/docs/linux/man/3-aa_setfont/">aa_setfont</a>(3), <a href="/docs/linux/man/3-aa_getevent/">aa_getevent</a>(3), <a href="/docs/linux/man/3-aa_getkey/">aa_getkey</a>(3), <a href="/docs/linux/man/3-aa_resize/">aa_resize</a>(3), <a href="/docs/linux/man/3-aa_resizehandler/">aa_resizehandler</a>(3), <a href="/docs/linux/man/3-aa_parseoptions/">aa_parseoptions</a>(3), <a href="/docs/linux/man/3-aa_edit/">aa_edit</a>(3), <a href="/docs/linux/man/3-aa_createedit/">aa_createedit</a>(3), <a href="/docs/linux/man/3-aa_editkey/">aa_editkey</a>(3), <a href="/docs/linux/man/3-aa_putpixel/">aa_putpixel</a>(3), <a href="/docs/linux/man/3-aa_recommendhikbd/">aa_recommendhikbd</a>(3), <a href="/docs/linux/man/3-aa_recommendlowkbd/">aa_recommendlowkbd</a>(3), <a href="/docs/linux/man/3-aa_recommendhimouse/">aa_recommendhimouse</a>(3), <a href="/docs/linux/man/3-aa_recommendlowmouse/">aa_recommendlowmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhidisplay/">aa_recommendhidisplay</a>(3), <a href="/docs/linux/man/3-aa_recommendlowdisplay/">aa_recommendlowdisplay</a>(3) </p>
<h2>Index</h2>
