---
title: "xkbinitcanonicalkeytypes(3)"
name: "xkbinitcanonicalkeytypes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbinitcanonicalkeytypes/"
description: "XkbInitCanonicalKeyTypes – Set the definitions of the canonical key types in a client map to their default values"
---

<p>XkbInitCanonicalKeyTypes &#8211; Set the definitions of the canonical key types in a client map to their default values </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbInitCanonicalKeyTypes</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>int </code><i>keypadVMod</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description containing client map to initialize</p>
<dt><i>&#8211; which</i></p>
<dd>mask of types to initialize</p>
<dt><i>&#8211; keypadVMod</i></p>
<dd>index of NumLock virtual modifier</dl>
<h2>Description</h2>
<p><i>XkbInitCanonicalKeyTypes </i> initializes the first XkbNumRequiredTypes key types of the keyboard specified by the <i>xkb </i> parameter to their default values. The <i>which </i> parameter specifies what canonical key types to initialize and is a bitwise inclusive OR of the following masks: XkbOneLevelMask, XkbTwoLevelMask, XkbAlphabeticMask, and XkbKeypadMask. Only those canonical types specified by the <i>which </i> mask are initialized. </p>
<p> If XkbKeypadMask is set in the <i>which </i> parameter, <i>XkbInitCanonicalKeyTypes </i> looks up the NumLock named virtual modifier to determine which virtual modifier to use when initializing the KEYPAD key type. If the NumLock virtual modifier does not exist, <i>XkbInitCanonicalKeyTypes </i> creates it. </p>
<p> <i>XkbInitCanonicalKeyTypes </i> normally returns Success. It returns BadAccess if the Xkb extension has not been properly initialized, and BadAccess if the xkb parameter is not valid.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbInitCanonicalKeyTypes </i> funtion return Success if the Xkb extension has been properly initialized and the xkb parameter is valid.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized </p>
</dl>
