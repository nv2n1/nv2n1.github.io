---
title: "aa_init(3)"
name: "aa_init"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aa_init/"
description: "aa_init – open the output display for AA-lib."
---

<h2>NAME</h2>
<p> aa_init &#8211; open the output display for AA-lib.</p>
<h2>SYNOPSIS</h2>
<p> <code> #include &lt;aalib.h&gt; </p>
<p> aa_context *aa_init<br />
 (<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const struct aa_driver *driver,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const struct aa_hardware_params *defparams,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const void *driverdata</p>
<p> ); </code></p>
<h2>PARAMETERS</h2>
<dl>
<dt><code>const struct aa_driver *driver</code></p>
<dd> Driver you want to use. Available drivers are listed in the NULL terminated aa_drivers array.</p>
<dt><code>const struct aa_hardware_params *defparams</code></p>
<dd> Hardware parameters you want. Use aa_defparams for default values.</p>
<dt><code>const void *driverdata</code></p>
<dd> This pointer is passed dirrectly to driver used to specify additional driver dependent parameters.</dl>
<h2>DESCRIPTION</h2>
<p> This is the most primitive AA-lib initialization function. Allows better control over the process than the easier to use aa_autoinit function. </p>
<p> Every AA-lib program ought to have call to aa_parseoptions before first call to aa_init.</p>
<h2>RETURNS</h2>
<p> Pointer to new AA-lib context or NULL if failed.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-save_d/">save_d</a>(3), <a href="/docs/linux/man/3-mem_d/">mem_d</a>(3), <a href="/docs/linux/man/3-aa_help/">aa_help</a>(3), <a href="/docs/linux/man/3-aa_formats/">aa_formats</a>(3), <a href="/docs/linux/man/3-aa_fonts/">aa_fonts</a>(3), <a href="/docs/linux/man/3-aa_dithernames/">aa_dithernames</a>(3), <a href="/docs/linux/man/3-aa_drivers/">aa_drivers</a>(3), <a href="/docs/linux/man/3-aa_kbddrivers/">aa_kbddrivers</a>(3), <a href="/docs/linux/man/3-aa_mousedrivers/">aa_mousedrivers</a>(3), <a href="/docs/linux/man/3-aa_kbdrecommended/">aa_kbdrecommended</a>(3), <a href="/docs/linux/man/3-aa_mouserecommended/">aa_mouserecommended</a>(3), <a href="/docs/linux/man/3-aa_displayrecommended/">aa_displayrecommended</a>(3), <a href="/docs/linux/man/3-aa_defparams/">aa_defparams</a>(3), <a href="/docs/linux/man/3-aa_defrenderparams/">aa_defrenderparams</a>(3), <a href="/docs/linux/man/3-aa_scrwidth/">aa_scrwidth</a>(3), <a href="/docs/linux/man/3-aa_scrheight/">aa_scrheight</a>(3), <a href="/docs/linux/man/3-aa_mmwidth/">aa_mmwidth</a>(3), <a href="/docs/linux/man/3-aa_mmheight/">aa_mmheight</a>(3), <a href="/docs/linux/man/3-aa_imgwidth/">aa_imgwidth</a>(3), <a href="/docs/linux/man/3-aa_imgheight/">aa_imgheight</a>(3), <a href="/docs/linux/man/3-aa_image/">aa_image</a>(3), <a href="/docs/linux/man/3-aa_text/">aa_text</a>(3), <a href="/docs/linux/man/3-aa_attrs/">aa_attrs</a>(3), <a href="/docs/linux/man/3-aa_currentfont/">aa_currentfont</a>(3), <a href="/docs/linux/man/3-aa_autoinit/">aa_autoinit</a>(3), <a href="/docs/linux/man/3-aa_autoinitkbd/">aa_autoinitkbd</a>(3), <a href="/docs/linux/man/3-aa_autoinitmouse/">aa_autoinitmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhi/">aa_recommendhi</a>(3), <a href="/docs/linux/man/3-aa_recommendlow/">aa_recommendlow</a>(3), <a href="/docs/linux/man/3-aa_initkbd/">aa_initkbd</a>(3), <a href="/docs/linux/man/3-aa_initmouse/">aa_initmouse</a>(3), <a href="/docs/linux/man/3-aa_close/">aa_close</a>(3), <a href="/docs/linux/man/3-aa_uninitkbd/">aa_uninitkbd</a>(3), <a href="/docs/linux/man/3-aa_uninitmouse/">aa_uninitmouse</a>(3), <a href="/docs/linux/man/3-aa_fastrender/">aa_fastrender</a>(3), <a href="/docs/linux/man/3-aa_render/">aa_render</a>(3), <a href="/docs/linux/man/3-aa_puts/">aa_puts</a>(3), <a href="/docs/linux/man/3-aa_printf/">aa_printf</a>(3), <a href="/docs/linux/man/3-aa_gotoxy/">aa_gotoxy</a>(3), <a href="/docs/linux/man/3-aa_hidecursor/">aa_hidecursor</a>(3), <a href="/docs/linux/man/3-aa_showcursor/">aa_showcursor</a>(3), <a href="/docs/linux/man/3-aa_getmouse/">aa_getmouse</a>(3), <a href="/docs/linux/man/3-aa_hidemouse/">aa_hidemouse</a>(3), <a href="/docs/linux/man/3-aa_showmouse/">aa_showmouse</a>(3), <a href="/docs/linux/man/3-aa_registerfont/">aa_registerfont</a>(3), <a href="/docs/linux/man/3-aa_setsupported/">aa_setsupported</a>(3), <a href="/docs/linux/man/3-aa_setfont/">aa_setfont</a>(3), <a href="/docs/linux/man/3-aa_getevent/">aa_getevent</a>(3), <a href="/docs/linux/man/3-aa_getkey/">aa_getkey</a>(3), <a href="/docs/linux/man/3-aa_resize/">aa_resize</a>(3), <a href="/docs/linux/man/3-aa_resizehandler/">aa_resizehandler</a>(3), <a href="/docs/linux/man/3-aa_parseoptions/">aa_parseoptions</a>(3), <a href="/docs/linux/man/3-aa_edit/">aa_edit</a>(3), <a href="/docs/linux/man/3-aa_createedit/">aa_createedit</a>(3), <a href="/docs/linux/man/3-aa_editkey/">aa_editkey</a>(3), <a href="/docs/linux/man/3-aa_putpixel/">aa_putpixel</a>(3), <a href="/docs/linux/man/3-aa_recommendhikbd/">aa_recommendhikbd</a>(3), <a href="/docs/linux/man/3-aa_recommendlowkbd/">aa_recommendlowkbd</a>(3), <a href="/docs/linux/man/3-aa_recommendhimouse/">aa_recommendhimouse</a>(3), <a href="/docs/linux/man/3-aa_recommendlowmouse/">aa_recommendlowmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhidisplay/">aa_recommendhidisplay</a>(3), <a href="/docs/linux/man/3-aa_recommendlowdisplay/">aa_recommendlowdisplay</a>(3) </p>
<h2>Index</h2>
