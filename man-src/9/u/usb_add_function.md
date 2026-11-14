---
title: "usb_add_function(9)"
name: "usb_add_function"
section: "9"
letter: "u"
url: "/docs/linux/man/9-usb_add_function/"
description: "usb_add_function – add a function to a configuration"
---

<p>usb_add_function &#8211; add a function to a configuration</p>
<h2>Synopsis</h2>
<pre><code>int usb_add_function(struct usb_configuration *config, struct usb_function *function);</code></pre>
<h2>Arguments</h2>
<p><i>config</i></p>
<dl>
<dd>
<dd>the configuration</dl>
<p> <i>function</i></p>
<dl>
<dd>the function being added</dl>
<h2>Context</h2>
<p>single threaded during gadget setup</p>
<h2>Description</h2>
<p>After initialization, each configuration must have one or more functions added to it. Adding a function involves calling its <i>bind</i>() method to allocate resources such as interface and string identifiers and endpoints. </p>
<p> This function returns the value of the function&#8217;s <code>bind</code>, which is zero for success else a negative errno value.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
