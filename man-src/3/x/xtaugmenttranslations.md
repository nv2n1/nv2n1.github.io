---
title: "xtaugmenttranslations(3)"
name: "xtaugmenttranslations"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtaugmenttranslations/"
description: "XtParseTranslationTable, XtAugmentTranslations, XtOverrideTranslations, XtUninstallTranslations – manage translation tables"
---

<p>XtParseTranslationTable, XtAugmentTranslations, XtOverrideTranslations, XtUninstallTranslations &#8211; manage translation tables </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtTranslations XtParseTranslationTable(const char *<i>table</i>);</p>
<dd>void XtAugmentTranslations(Widget <i>w</i>, XtTranslations <i>translations</i>);</p>
<dd>void XtOverrideTranslations(Widget <i>w</i>, XtTranslations <i>translations</i>);</p>
<dd>void XtUninstallTranslations(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>table</i></p>
<dd>Specifies the translation table to compile.</p>
<dt><i>translations</i></p>
<dd>Specifies the compiled translation table to merge in (must not be NULL).</p>
<dt><i>w</i></p>
<dd>Specifies the widget into which the new translations are to be merged or removed.</dl>
<h2>Description</h2>
<p>The <code>XtParseTranslationTable</code> function compiles the translation table into the opaque internal representation of type <code>XtTranslations</code>. Note that if an empty translation table is required for any purpose, one can be obtained by calling <code>XtParseTranslationTable</code> and passing an empty string. </p>
<p> The <code>XtAugmentTranslations</code> function nondestructively merges the new translations into the existing widget translations. If the new translations contain an event or event sequence that already exists in the widget&#8217;s translations, the new translation is ignored. </p>
<p> The <code>XtOverrideTranslations</code> function destructively merges the new translations into the existing widget translations. If the new translations contain an event or event sequence that already exists in the widget&#8217;s translations, the new translation is merged in and override the widget&#8217;s translation. </p>
<p> To replace a widget&#8217;s translations completely, use <code>XtSetValues</code> on the XtNtranslations resource and specify a compiled translation table as the value. </p>
<p> The <code>XtUninstallTranslations</code> function causes the entire translation table for widget to be removed.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddactions/">XtAppAddActions</a>(3), <a href="/docs/linux/man/3-xtcreatepopupshell/">XtCreatePopupShell</a>(3), <a href="/docs/linux/man/3-xtparseacceleratortable/">XtParseAcceleratorTable</a>(3), <a href="/docs/linux/man/3-xtpopup/">XtPopup</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
