---
title: "xtsetkeytranslator(3)"
name: "xtsetkeytranslator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetkeytranslator/"
description: "XtSetKeyTranslator, XtTranslateKeycode, XtRegisterCaseConverter, XtConvertCase – convert KeySym to KeyCodes"
---

<p>XtSetKeyTranslator, XtTranslateKeycode, XtRegisterCaseConverter, XtConvertCase &#8211; convert KeySym to KeyCodes </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtSetKeyTranslator(Display *<i>display</i>, XtKeyProc <i>proc</i>);</p>
<dd>void XtTranslateKeycode(Display *<i>display</i>, KeyCode <i>keycode</i>, Modifiers <i>modifiers</i>, Modifiers *<i>modifiers_return</i>, KeySym *<i>keysym_return</i>);</p>
<dd>void XtRegisterCaseConverter(Display *<i>display</i>, XtCaseProc <i>proc</i>, KeySym <i>start</i>, KeySym <i>stop</i>);</p>
<dd>void XtConvertCase(Display *<i>display</i>, KeySym <i>keysym</i>, KeySym *<i>lower_return</i>, KeySym *<i>upper_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display.</p>
<dt><i>keycode</i></p>
<dd>Specifies the KeyCode to translate.</p>
<dt><i>keysym</i></p>
<dd>Specifies the KeySym to convert.</p>
<dt><i>keysym_return</i></p>
<dd>Returns the resulting KeySym.</p>
<dt><i>lower_return</i></p>
<dd>Returns the lowercase equivalent of the KeySym.</p>
<dt><i>upper_return</i></p>
<dd>Returns the uppercase equivalent of the KeySym.</p>
<dt><i>modifiers</i></p>
<dd>Specifies the modifiers to the KeyCode.</p>
<dt><i>modifiers_return</i></p>
<dd>Returns a mask that indicates the modifiers actually used to generate the KeySym.</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to perform key translations or conversions.</p>
<dt><i>start</i></p>
<dd>Specifies the first KeySym for which this converter is valid.</p>
<dt><i>stop</i></p>
<dd>Specifies the last KeySym for which this converter is valid.</dl>
<h2>Description</h2>
<p>The <code>XtSetKeyTranslator</code> function sets the specified procedure as the current key translator. The default translator is <code>XtTranslateKey</code>, an <code>XtKeyProc</code> that uses Shift and Lock modifiers with the interpretations defined by the core protocol. It is provided so that new translators can call it to get default KeyCode-to-KeySym translations and so that the default translator can be reinstalled. </p>
<p> The <code>XtTranslateKeycode</code> function passes the specified arguments directly to the currently registered KeyCode to KeySym translator. </p>
<p> The <code>XtRegisterCaseConverter</code> registers the specified case converter. The start and stop arguments provide the inclusive range of KeySyms for which this converter is to be called. The new converter overrides any previous converters for KeySyms in that range. No interface exists to remove converters; you need to register an identity converter. When a new converter is registered, the Intrinsics refreshes the keyboard state if necessary. The default converter understands case conversion for all KeySyms defined in the core protocol. </p>
<p> The <code>XtConvertCase</code> function calls the appropriate converter and returns the results. A user-supplied <code>XtKeyProc</code> may need to use this function.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
