---
title: "aa_puts(3)"
name: "aa_puts"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aa_puts/"
description: "aa_puts – output string to AA-lib output buffers."
---

<h2>NAME</h2>
<p> aa_puts &#8211; output string to AA-lib output buffers.</p>
<h2>SYNOPSIS</h2>
<p> <code> #include &lt;aalib.h&gt; </p>
<p> void aa_puts<br />
 (<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>aa_context *c,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int x,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int y,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>enum aa_attribute attr,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const char *s</p>
<p> ); </code></p>
<h2>PARAMETERS</h2>
<dl>
<dt><code>aa_context *c</code></p>
<dd> Specifies the AA-lib context to operate on.</p>
<dt><code>int x</code></p>
<dd> X coordinate of the first character.</p>
<dt><code>int y</code></p>
<dd> Y coordinate of the first character.</p>
<dt><code>enum aa_attribute attr</code></p>
<dd> Attribute to use. </p>
<p> Possible values for an <code>enum aa_attribute</code> are as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>AA_NORMAL</code></p>
<dd> Normal characters.</p>
<dt><code>AA_DIM</code></p>
<dd> Dark characters.</p>
<dt><code>AA_BOLD</code></p>
<dd> Bright characters.</p>
<dt><code>AA_BOLDFONT</code></p>
<dd> Characters rendered in bold font.</p>
<dt><code>AA_REVERSE</code></p>
<dd> Reversed (black on whilte) characters.</p>
<dt><code>AA_SPECIAL</code></p>
<dd> Render characters in a way easilly visible on the screen. The exact rendering is driver dependent, but this mode ought to be used to output texts you want to make easilly visible in the image.</dl>
</dl>
<dt><code>const char *s</code></p>
<dd> String to output.</dl>
<h2>DESCRIPTION</h2>
<p> Output given string to AA-lib output buffers. To see the effect you need to call aa_flush too.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-save_d/">save_d</a>(3), <a href="/docs/linux/man/3-mem_d/">mem_d</a>(3), <a href="/docs/linux/man/3-aa_help/">aa_help</a>(3), <a href="/docs/linux/man/3-aa_formats/">aa_formats</a>(3), <a href="/docs/linux/man/3-aa_fonts/">aa_fonts</a>(3), <a href="/docs/linux/man/3-aa_dithernames/">aa_dithernames</a>(3), <a href="/docs/linux/man/3-aa_drivers/">aa_drivers</a>(3), <a href="/docs/linux/man/3-aa_kbddrivers/">aa_kbddrivers</a>(3), <a href="/docs/linux/man/3-aa_mousedrivers/">aa_mousedrivers</a>(3), <a href="/docs/linux/man/3-aa_kbdrecommended/">aa_kbdrecommended</a>(3), <a href="/docs/linux/man/3-aa_mouserecommended/">aa_mouserecommended</a>(3), <a href="/docs/linux/man/3-aa_displayrecommended/">aa_displayrecommended</a>(3), <a href="/docs/linux/man/3-aa_defparams/">aa_defparams</a>(3), <a href="/docs/linux/man/3-aa_defrenderparams/">aa_defrenderparams</a>(3), <a href="/docs/linux/man/3-aa_scrwidth/">aa_scrwidth</a>(3), <a href="/docs/linux/man/3-aa_scrheight/">aa_scrheight</a>(3), <a href="/docs/linux/man/3-aa_mmwidth/">aa_mmwidth</a>(3), <a href="/docs/linux/man/3-aa_mmheight/">aa_mmheight</a>(3), <a href="/docs/linux/man/3-aa_imgwidth/">aa_imgwidth</a>(3), <a href="/docs/linux/man/3-aa_imgheight/">aa_imgheight</a>(3), <a href="/docs/linux/man/3-aa_image/">aa_image</a>(3), <a href="/docs/linux/man/3-aa_text/">aa_text</a>(3), <a href="/docs/linux/man/3-aa_attrs/">aa_attrs</a>(3), <a href="/docs/linux/man/3-aa_currentfont/">aa_currentfont</a>(3), <a href="/docs/linux/man/3-aa_autoinit/">aa_autoinit</a>(3), <a href="/docs/linux/man/3-aa_autoinitkbd/">aa_autoinitkbd</a>(3), <a href="/docs/linux/man/3-aa_autoinitmouse/">aa_autoinitmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhi/">aa_recommendhi</a>(3), <a href="/docs/linux/man/3-aa_recommendlow/">aa_recommendlow</a>(3), <a href="/docs/linux/man/3-aa_init/">aa_init</a>(3), <a href="/docs/linux/man/3-aa_initkbd/">aa_initkbd</a>(3), <a href="/docs/linux/man/3-aa_initmouse/">aa_initmouse</a>(3), <a href="/docs/linux/man/3-aa_close/">aa_close</a>(3), <a href="/docs/linux/man/3-aa_uninitkbd/">aa_uninitkbd</a>(3), <a href="/docs/linux/man/3-aa_uninitmouse/">aa_uninitmouse</a>(3), <a href="/docs/linux/man/3-aa_fastrender/">aa_fastrender</a>(3), <a href="/docs/linux/man/3-aa_render/">aa_render</a>(3), <a href="/docs/linux/man/3-aa_printf/">aa_printf</a>(3), <a href="/docs/linux/man/3-aa_gotoxy/">aa_gotoxy</a>(3), <a href="/docs/linux/man/3-aa_hidecursor/">aa_hidecursor</a>(3), <a href="/docs/linux/man/3-aa_showcursor/">aa_showcursor</a>(3), <a href="/docs/linux/man/3-aa_getmouse/">aa_getmouse</a>(3), <a href="/docs/linux/man/3-aa_hidemouse/">aa_hidemouse</a>(3), <a href="/docs/linux/man/3-aa_showmouse/">aa_showmouse</a>(3), <a href="/docs/linux/man/3-aa_registerfont/">aa_registerfont</a>(3), <a href="/docs/linux/man/3-aa_setsupported/">aa_setsupported</a>(3), <a href="/docs/linux/man/3-aa_setfont/">aa_setfont</a>(3), <a href="/docs/linux/man/3-aa_getevent/">aa_getevent</a>(3), <a href="/docs/linux/man/3-aa_getkey/">aa_getkey</a>(3), <a href="/docs/linux/man/3-aa_resize/">aa_resize</a>(3), <a href="/docs/linux/man/3-aa_resizehandler/">aa_resizehandler</a>(3), <a href="/docs/linux/man/3-aa_parseoptions/">aa_parseoptions</a>(3), <a href="/docs/linux/man/3-aa_edit/">aa_edit</a>(3), <a href="/docs/linux/man/3-aa_createedit/">aa_createedit</a>(3), <a href="/docs/linux/man/3-aa_editkey/">aa_editkey</a>(3), <a href="/docs/linux/man/3-aa_putpixel/">aa_putpixel</a>(3), <a href="/docs/linux/man/3-aa_recommendhikbd/">aa_recommendhikbd</a>(3), <a href="/docs/linux/man/3-aa_recommendlowkbd/">aa_recommendlowkbd</a>(3), <a href="/docs/linux/man/3-aa_recommendhimouse/">aa_recommendhimouse</a>(3), <a href="/docs/linux/man/3-aa_recommendlowmouse/">aa_recommendlowmouse</a>(3), <a href="/docs/linux/man/3-aa_recommendhidisplay/">aa_recommendhidisplay</a>(3), <a href="/docs/linux/man/3-aa_recommendlowdisplay/">aa_recommendlowdisplay</a>(3) </p>
<h2>Index</h2>
