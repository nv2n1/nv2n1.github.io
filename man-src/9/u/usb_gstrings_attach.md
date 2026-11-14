---
title: "usb_gstrings_attach(9)"
name: "usb_gstrings_attach"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_gstrings_attach/"
description: "usb_gstrings_attach – attach gadget strings to a cdev and assign ids"
---

<p>usb_gstrings_attach &#8211; attach gadget strings to a cdev and assign ids</p>
<h2>Synopsis</h2>
<pre><code>struct usb_string *usb_gstrings_attach(struct usb_composite_dev *cdev, struct usb_gadget_strings **sp, unsigned n_strings);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>the device whose string descriptor IDs are being allocated and attached.</dl>
<p> <i>sp</i></p>
<dl>
<dd>an array of usb_gadget_strings to attach.</dl>
<p> <i>n_strings</i></p>
<dl>
<dd>number of entries in each usb_strings array (sp[]-&gt;strings)</dl>
<h2>Description</h2>
<p>This function will create a deep copy of usb_gadget_strings and usb_string and attach it to the cdev. The actual string (usb_string.s) will not be copied but only a referenced will be made. The struct usb_gadget_strings array may contain multiple languages and should be NULL terminated. The -&gt;language pointer of each struct usb_gadget_strings has to contain the same amount of entries. For instance: sp[0] is en-US, sp[1] is es-ES. It is expected that the first usb_string entry of es-ES contains the translation of the first usb_string entry of en-US. Therefore both entries become the same id assign.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
