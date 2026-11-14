---
title: "iok(1)"
name: "iok"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iok/"
description: "iok– Indic Onscreen Keyboard"
---

<h2>NAME</h2>
<p> <code>iok</code>&#8211; Indic Onscreen Keyboard</p>
<h2>SYNOPSIS</h2>
<p> <code>iok</code> [<code>-a</code>] [<code>-h</code>] [<code>-d</code> <i>1</i>] [<code>-n</code> <i>LANGCODE</i>]</p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr>Indic Onscreen Keyboard currently shows Inscript and Inscript2 keymaps for 22 official Indian languages. The languages are Assamese, Bengali, Bodo, Dogri, Gujarati, Hindi, Kannada, Kokani, Maithili, Malayalam, Manipuri, Marathi, Nepali, Oriya, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu.<br />
&nbsp;<wbr>The iok application runs in default and advanced mode. In default mode, iok starts by loading Inscript2 keymap of the current locale. If keymap is not installed or available then iok shows keymap list in the default mode. User can then select any keymap from keymap list if he want to write using it.<br />
&nbsp;<wbr>&nbsp;<wbr>In the advanced mode, iok allows to open non-supported keymaps. If keymap can be parsed by iok then it will be showed in iok UI otherwise it will show error message that iok can&#8217;t load this keymap. Advanced mode also allows to create custom keymap by either swapping or re-assigning character mappings in the existing loaded keymap in iok.<br />
&nbsp;<wbr>&nbsp;<wbr>Another feature iok supports is Drag and Drop. This will allow user to swap character mappings using mouse.<br />
&nbsp;<wbr>&nbsp;<wbr>The keymap list shows Inscript and Inscript2 keymaps from location /usr/share/m17n and ~/.m17n.d path. </p>
<p> To start iok in normal mode from console, use following command iok </p>
<p> To start iok in advanced mode from console, use following command iok -a </p>
<p> To start iok in any supported Inscript2 keymap (say in Marathi) use following command iok -n mr </p>
<p> As Inscript2 keymap naming also uses language script code for some languages, command to open those keymaps is like this iok -n pa-guru where pa is a isocode name for the Punjabi language and guru is a language script code name in which keymap is written. </p>
<p> To use Drag and Drop feature of iok, start iok from console as iok -d 1 The Draft version of Inscript2 keymaps are available at <a rel="nofollow" href="https://fedorahosted.org/inscript2/">https://fedorahosted.org/inscript2/</a> </p>
<p> This project is available at <a rel="nofollow" href="http://fedorahosted.org/iok/">http://fedorahosted.org/iok/</a> or <a href="http://iok.sourceforge.net">http://iok.sourceforge.net</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> It shows the menus and combo box in iok UI</p>
<dt><code>-h</code></p>
<dd> It show the help</p>
<dt><code>-d</code><i> 1</i></p>
<dd> This will enable Drag and Drop feature only for the single iok invocation. Otherwise iok has disabled Drag and Drop by default.</p>
<dt><code>-n</code><i> LANGCODE</i></p>
<dd> In the place of LANGCODE,you need to specify a particular language code. Shows iok UI for that particular language. This will also requires language script code. e.g. for Bodo, Dogri, Kokani, Nepali, Sindhi use its langcode and &quot;-deva&quot; as a language script code. </p>
<p> To start iok using Kokani keymap, run &quot;iok -n kok-deva&quot;</dl>
<h2>AUTHOR</h2>
<p> Suji A &lt;suji87.msc [at] gmail.com&gt; , Parag &lt;pnemade [at] fedoraproject.org&gt; </p>
<h2>Index</h2>
