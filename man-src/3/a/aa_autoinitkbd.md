---
title: "aa_autoinitkbd(3)"
name: "aa_autoinitkbd"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aa_autoinitkbd/"
description: "aa_autoinitkbd – easy to use AA-lib keyboard initialization function."
---

<h2>NAME</h2>
<p> aa_autoinitkbd &#8211; easy to use AA-lib keyboard initialization function.</p>
<h2>SYNOPSIS</h2>
<p> <code> #include &lt;aalib.h&gt; </p>
<p> int aa_autoinitkbd<br />
 (<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>struct aa_context *context,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int mode</p>
<p> ); </code></p>
<h2>PARAMETERS</h2>
<dl>
<dt><code>struct aa_context *context</code></p>
<dd> Specifies the AA-lib context to operate on.</p>
<dt><code>int mode</code></p>
<dd> Mask of extra features you request. Can contain AA_SENDRELEASE if you are interested in release events too.</dl>
<h2>DESCRIPTION</h2>
<p> Attempts to find available keyboard driver supporting the specified mode. First attempts to initialize the recommended drivers and then in order drivers available in the aa_kbddrivers array (all regular output drivers compiled into AA-lib). </p>
<p> Every AA-lib program ought to have call to aa_parseoptions before first call to aa_init.</p>
<h2>RETURNS</h2>
<p> 1 when succesfull or 0 on failure.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-save_d/">save_d</a>(3), <a href="/docs/linux/man/3-mem_d/">mem_d</a>(3), <a href="/docs/linux/man/3-aa_help/">aa_help</a>(3), <a href="/docs/linux/man/3-aa_formats/">aa_formats</a>(3), <a href="/docs/linux/man/3-aa_fonts/">aa_fonts</a>(3), <a href="/docs/linux/man/3-aa_dithernames/">aa_dithernames</a>(3), <a href="/docs/linux/man/3-aa_drivers/">aa_drivers</a>(3), <a href="/docs/linux/man/3-aa_kbddrivers/">aa_kbddrivers</a>(3), <a href="/docs/linux/man/3-aa_mousedrivers/">aa_mousedrivers</a>(3), <a href="/docs/linux/man/3-aa_kbdrecommended/">aa_kbdrecommended</a>(3), <a href="/docs/linux/man/3-aa_mouserecommended/">aa_mouserecommended</a>(3), <a href="/docs/linux/man/3-aa_displayrecommended/">aa_displayrecommended</a>(3), <a href="/docs/linux/man/3-aa_defparams/">aa_defparams</a>(3), <a href="/docs/linux/man/3-aa_defrenderparams/">aa_defrenderparams</a>(3), <a href="/docs/linux/man/3-aa_scrwidth/">aa_scrwidth</a>(3), <a href="/docs/linux/man/3-aa_scrheight/">aa_scrheight</a>(3), <a href="/docs/linux/man/3-aa_mmwidth/">aa_mmwidth</a>(3), <a href="/docs/linux/man/3-aa_mmheight/">aa_mmheight</a>(3), <a href="/docs/linux/man/3-aa_imgwidth/">aa_imgwidth</a>(3), <a href="/docs/linux/man/3-aa_imgheight/">aa_imgheight</a>(3), <a href="/docs/linux/man/3-aa_image/">aa_image</a>(3), <a href="/docs/linux/man/3-aa_text/">aa_text</a>(3), <a href="/docs/linux/man/3-aa_attrs/">aa_attrs</a>(3), <a href="/docs/linux/man/3-aa_currentfont/">aa_currentfont</a>(3), <a href="/docs/linux/man/3-aa_autoinit/">aa_autoinit</a>(3), <a href="/docs/linux/man/3-aa_autoinitmouse/">aa_autoinitmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhi/">aa_recommendhi</a>(3), <a href="/docs/linux/man/3-aa_recommendlow/">aa_recommendlow</a>(3), <a href="/docs/linux/man/3-aa_init/">aa_init</a>(3), <a href="/docs/linux/man/3-aa_initkbd/">aa_initkbd</a>(3), <a href="/docs/linux/man/3-aa_initmouse/">aa_initmouse</a>(3), <a href="/docs/linux/man/3-aa_close/">aa_close</a>(3), <a href="/docs/linux/man/3-aa_uninitkbd/">aa_uninitkbd</a>(3), <a href="/docs/linux/man/3-aa_uninitmouse/">aa_uninitmouse</a>(3), <a href="/docs/linux/man/3-aa_fastrender/">aa_fastrender</a>(3), <a href="/docs/linux/man/3-aa_render/">aa_render</a>(3), <a href="/docs/linux/man/3-aa_puts/">aa_puts</a>(3), <a href="/docs/linux/man/3-aa_printf/">aa_printf</a>(3), <a href="/docs/linux/man/3-aa_gotoxy/">aa_gotoxy</a>(3), <a href="/docs/linux/man/3-aa_hidecursor/">aa_hidecursor</a>(3), <a href="/docs/linux/man/3-aa_showcursor/">aa_showcursor</a>(3), <a href="/docs/linux/man/3-aa_getmouse/">aa_getmouse</a>(3), <a href="/docs/linux/man/3-aa_hidemouse/">aa_hidemouse</a>(3), <a href="/docs/linux/man/3-aa_showmouse/">aa_showmouse</a>(3), <a href="/docs/linux/man/3-aa_registerfont/">aa_registerfont</a>(3), <a href="/docs/linux/man/3-aa_setsupported/">aa_setsupported</a>(3), <a href="/docs/linux/man/3-aa_setfont/">aa_setfont</a>(3), <a href="/docs/linux/man/3-aa_getevent/">aa_getevent</a>(3), <a href="/docs/linux/man/3-aa_getkey/">aa_getkey</a>(3), <a href="/docs/linux/man/3-aa_resize/">aa_resize</a>(3), <a href="/docs/linux/man/3-aa_resizehandler/">aa_resizehandler</a>(3), <a href="/docs/linux/man/3-aa_parseoptions/">aa_parseoptions</a>(3), <a href="/docs/linux/man/3-aa_edit/">aa_edit</a>(3), <a href="/docs/linux/man/3-aa_createedit/">aa_createedit</a>(3), <a href="/docs/linux/man/3-aa_editkey/">aa_editkey</a>(3), <a href="/docs/linux/man/3-aa_putpixel/">aa_putpixel</a>(3), <a href="/docs/linux/man/3-aa_recommendhikbd/">aa_recommendhikbd</a>(3), <a href="/docs/linux/man/3-aa_recommendlowkbd/">aa_recommendlowkbd</a>(3), <a href="/docs/linux/man/3-aa_recommendhimouse/">aa_recommendhimouse</a>(3), <a href="/docs/linux/man/3-aa_recommendlowmouse/">aa_recommendlowmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhidisplay/">aa_recommendhidisplay</a>(3), <a href="/docs/linux/man/3-aa_recommendlowdisplay/">aa_recommendlowdisplay</a>(3) </p>
<h2>Index</h2>
