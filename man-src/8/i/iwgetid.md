---
title: "iwgetid(8)"
name: "iwgetid"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iwgetid/"
description: "iwgetid – Report ESSID, NWID or AP/Cell Address of wireless network"
---

<p>iwgetid &#8211; Report ESSID, NWID or AP/Cell Address of wireless network</p>
<h2>Synopsis</h2>
<p><code>iwgetid </code><i>[interface]</i><code> [&#8211;raw] [&#8211;scheme] [&#8211;ap] [&#8211;freq]</code><br />
 <code> [&#8211;mode] [&#8211;protocol] [&#8211;channel]</code></p>
<h2>Description</h2>
<p><code>iwgetid</code> is used to find out the NWID, ESSID or AP/Cell Address of the wireless network that is currently used. The information reported is the same as the one shown by <code>iwconfig</code>, but <code>iwgetid</code> is easier to integrate in various scripts.<br />
 By default, <code>iwgetid</code> will print the <i>ESSID</i> of the device, and if the device doesn&#8217;t have any ESSID it will print its <i>NWID</i>.<br />
 The default formatting output is pretty-print.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;raw</code></p>
<dd>This option disables pretty-printing of the information. This option is orthogonal to the other options (except <code>&#8211;scheme</code>), so with the appropriate combination of options you can print the raw ESSID, AP Address or Mode.<br />
 This format is ideal when storing the result of iwgetid as a variable in <i>Shell</i> or <i>Perl</i> scripts or to pass the result as an argument on the command line of <code>iwconfig</code>.</p>
<dt><code>&#8211;scheme</code></p>
<dd>This option is similar to the previous one, it disables pretty-printing of the information and removes all characters that are not alphanumerics (like space, punctuation and control characters).<br />
 The resulting output is a valid Pcmcia scheme identifier (that may be used as an argument of the command <code>cardctl scheme</code>). This format is also ideal when using the result of iwgetid as a selector in <i>Shell</i> or <i>Perl</i> scripts, or as a file name.</p>
<dt><code>&#8211;ap</code></p>
<dd>Display the MAC address of the Wireless <i>Access Point</i> or the <i>Cell</i>.</p>
<dt><code>&#8211;freq</code></p>
<dd>Display the current <i>frequency</i> or <i>channel</i> used by the interface.</p>
<dt><code>&#8211;channel</code></p>
<dd>Display the current <i>channel</i> used by the interface. The channel is determined using the current frequency and the frequency list provided by the interface.</p>
<dt><code>&#8211;mode</code></p>
<dd>Display the current <i>mode</i> of the interface.</p>
<dt><code>&#8211;protocol</code></p>
<dd>Display the <i>protocol name</i> of the interface. This allows to identify all the cards that are compatible with each other and accept the same type of configuration.<br />
 This can also be used to <i>check Wireless Extension support</i> on the interface, as this is the only attribute that all drivers supporting Wireless Extension are mandated to support.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwspy/">iwspy</a></code>(8), <code><a href="/docs/linux/man/8-iwpriv/">iwpriv</a></code>(8). </p>
