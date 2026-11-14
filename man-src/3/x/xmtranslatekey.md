---
title: "xmtranslatekey(3)"
name: "xmtranslatekey"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtranslatekey/"
description: "XmTranslateKey — The default keycode-to-keysym translator"
---

<p><code>XmTranslateKey</code> &#8212; The default keycode-to-keysym translator</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmTranslateKey</code>(
<code>Display *display</code>,
<code>KeyCode keycode</code>,
<code>Modifiers modifiers</code>,
<code>Modifiers *modifiers_return</code>,
<code>KeySym *keysym_return</code>);</pre>
<h2>Description</h2>
<p><code>XmTranslateKey</code> is the default <code>XtKeyProc</code> translation procedure for Motif applications. The function takes a keycode and modifiers and returns the corresponding keysym. </p>
<p> <code>XmTranslateKey</code> serves two main purposes: to enable new translators with expanded functionality to get the default Motif keycode-to-keysym translation in addition to whatever they add, and to reinstall the default translator. This function enables keysyms defined by the Motif virtual bindings to be used when an application requires its own XtKeyProc to be installed.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display that the keycode is from</p>
<dt><i>keycode</i></p>
<dd>Specifies the keycode to translate</p>
<dt><i>modifiers</i></p>
<dd>Specifies the modifier keys to be applied to the keycode</p>
<dt><i>modifiers_return</i></p>
<dd>Specifies a mask of the modifier keys actually used to generate the keysym (an AND of <i>modifiers</i> and any default modifiers applied by the currently registered translator)</p>
<dt><i>keysym_return</i></p>
<dd>Specifies a pointer to the resulting keysym</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
