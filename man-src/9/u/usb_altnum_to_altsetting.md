---
title: "usb_altnum_to_altsetting(9)"
name: "usb_altnum_to_altsetting"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_altnum_to_altsetting/"
description: "usb_altnum_to_altsetting – get the altsetting structure with a given alternate setting number."
---

<p>usb_altnum_to_altsetting &#8211; get the altsetting structure with a given alternate setting number.</p>
<h2>Synopsis</h2>
<pre><code>struct usb_host_interface *usb_altnum_to_altsetting(const struct usb_interface *intf, unsigned int altnum);</code></pre>
<h2>Arguments</h2>
<p><i>intf</i></p>
<dl>
<dd>
<dd>the interface containing the altsetting in question</dl>
<p> <i>altnum</i></p>
<dl>
<dd>the desired alternate setting number</dl>
<h2>Description</h2>
<p>This searches the altsetting array of the specified interface for an entry with the correct bAlternateSetting value. </p>
<p> Note that altsettings need not be stored sequentially by number, so it would be incorrect to assume that the first altsetting entry in the array corresponds to altsetting zero. This routine helps device drivers avoid such mistakes. </p>
<p> Don&#8217;t call this function unless you are bound to the intf interface or you have locked the device!</p>
<h2>Return</h2>
<p>A pointer to the entry of the altsetting array of <i>intf</i> that has <i>altnum</i> as the alternate setting number. <code>NULL</code> if not found.</p>
<h2>Copyright</h2>
