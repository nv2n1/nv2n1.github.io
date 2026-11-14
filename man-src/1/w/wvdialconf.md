---
title: "wvdialconf(1)"
name: "wvdialconf"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wvdialconf/"
description: "wvdialconf – build a configuration file for"
---

<h2 class="name">NAME</h2>
<p> wvdialconf &#8211; build a configuration file for <code></p>
<p><a href="/docs/linux/man/1-wvdial/">wvdial</a></code>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>wvdialconf</code> <i>/etc/wvdial.conf</i></p>
<h2>DESCRIPTION</h2>
<p> <code>wvdialconf</code> detects your modem, its maximum baud rate, and a good initialization string and generates or updates the <code><a href="/docs/linux/man/1-wvdial/">wvdial</a></code>(1) configuration file based on this information. </p>
<p> <code>wvdialconf</code> is completely non-interactive. You still need to edit <i>/etc/wvdial.conf</i> to specify the phone number, login name, and password of your internet account in order for <code><a href="/docs/linux/man/1-wvdial/">wvdial</a></code>(1) to work. </p>
<p> It is safe to run <code>wvdialconf</code> if a configuration file already exists. In that case, only the <i>Modem</i>, <i>Baud</i>, <i>Init</i>, and <i>Init2</i> options are changed in the <i>[Dialer Defaults]</i> section, and only if autodetection is successful.</p>
<h2>BUGS</h2>
<p> We&#8217;re willing to entertain the possibility. Let us know if you have any problems by sending an e-mail to <code>&lt;wvdial-list [at] lists.nit.ca&gt;</code>. </p>
<h2>DIAGNOSTICS</h2>
<p> An exit status of 0 means that a modem was detected and the configuration file was updated successfully. </p>
<p> Any other value means that something went wrong and the configuration file was unchanged.</p>
<h2>AUTHORS</h2>
<p> Dave Coombs and Avery Pennarun for Net Integration Technologies.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wvdial/">wvdial</a></code>(1), <code><a href="/docs/linux/man/5-wvdial-conf/">wvdial.conf</a></code>(5). </p>
<h2>Index</h2>
