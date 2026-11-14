---
title: "pk-device-rebind(1)"
name: "pk-device-rebind"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pk-device-rebind/"
description: "pk-device-rebind – Device software reloader"
---

<h2 class="name">NAME</h2>
<p> pk-device-rebind &#8211; Device software reloader </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pk-device-rebind</code> [<code>&#8211;help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>pk-device-rebind</code> command. </p>
<p> <code>pk-device-rebind</code> is the command line client for reloading devices after firmware has been installed.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Show extra debugging information.</dl>
<p> <code>&#8211;simulate</code></p>
<dl>
<dt>
<dd> Don&#8217;t actually poke the hardware, only simulate what would be done.</dl>
<h2>RETURN VALUES</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success, the device was reloaded</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Failed with miscellaneous internal error.</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> Arguments incorrect.</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> Failed to write to device.</dl>
<h2>SEE ALSO</h2>
<p> <code>packagekitd</code> (1). <code><a href="/docs/linux/man/1-udev/">udev</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Richard Hughes richard [at] hughsie.com.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Richard Hughes </p>
<h2>Index</h2>
