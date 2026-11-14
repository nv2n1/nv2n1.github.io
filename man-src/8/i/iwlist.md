---
title: "iwlist(8)"
name: "iwlist"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iwlist/"
description: "iwlist – Get more detailed wireless information from a wireless interface"
---

<p>iwlist &#8211; Get more detailed wireless information from a wireless interface</p>
<h2>Synopsis</h2>
<p><code>iwlist [</code><i>interface</i><code>] scanning</code><br />
 <code>iwlist [</code><i>interface</i><code>] frequency</code><br />
 <code>iwlist [</code><i>interface</i><code>] rate</code><br />
 <code>iwlist [</code><i>interface</i><code>] keys</code><br />
 <code>iwlist [</code><i>interface</i><code>] power</code><br />
 <code>iwlist [</code><i>interface</i><code>] txpower</code><br />
 <code>iwlist [</code><i>interface</i><code>] retry</code><br />
 <code>iwlist [</code><i>interface</i><code>] event</code><br />
 <code>iwlist [</code><i>interface</i><code>] auth</code><br />
 <code>iwlist [</code><i>interface</i><code>] wpakeys</code><br />
 <code>iwlist [</code><i>interface</i><code>] genie</code><br />
 <code>iwlist [</code><i>interface</i><code>] modulation</code><br />
 <code>iwlist &#8211;help</code><br />
 <code>iwlist &#8211;version</code></p>
<h2>Description</h2>
<p><code>Iwlist</code> is used to display some additional information from a wireless network interface that is not displayed by <i><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></i>(8). The main argument is used to select a category of information, <code>iwlist</code> displays in detailed form all information related to this category, including information already shown by <i><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></i>(8).</p>
<h2>Parameters</h2>
<dl>
<dt><code>scan</code>[ning]</p>
<dd>Give the list of Access Points and Ad-Hoc cells in range, and optionally a whole bunch of information about them (ESSID, Quality, Frequency, Mode&#8230;). The type of information returned depends on what the card supports.<br />
 Triggering scanning is a privileged operation (<i>root</i> only) and normal users can only read left-over scan results. By default, the way scanning is done (the scope of the scan) is dependant on the card and card settings.<br />
 This command takes optional arguments, however most drivers will ignore those. The option <code>essid</code> is used to specify a scan on a specific ESSID. With some card/driver, this enables to see hidden networks. The option <code>last</code> does not trigger a scan and read left-over scan results.</p>
<dt><code>freq</code>[uency]/<code>channel</code></p>
<dd>Give the list of available frequencies in the device and the number of defined channels. Please note that usually the driver returns the total number of channels and only the frequencies available in the present locale, so there is no one-to-one mapping between frequencies displayed and channel numbers.</p>
<dt><code>rate</code>/<code>bit</code>[rate]</p>
<dd>List the bit-rates supported by the device.</p>
<dt><code>keys</code>/<code>enc</code>[ryption]</p>
<dd>List the encryption key sizes supported and list all the encryption keys set in the device.</p>
<dt><code>power</code></p>
<dd>List the various Power Management attributes and modes of the device.</p>
<dt><code>txpower</code></p>
<dd>List the various Transmit Powers available on the device.</p>
<dt><code>retry</code></p>
<dd>List the transmit retry limits and retry lifetime on the device.</p>
<dt><code>ap</code>/<code>accesspoint</code>/<code>peers</code></p>
<dd>Give the list of Access Points in range, and optionally the quality of link to them. This feature is <code>obsolete</code> and now deprecated in favor of scanning support (above), and most drivers don&#8217;t support it.<br />
 Some drivers may use this command to return a specific list of Peers or Access Points, such as the list of Peers associated/registered with the card. See your driver documentation for details.</p>
<dt><code>event</code></p>
<dd>List the wireless events supported by the device.</p>
<dt><code>auth</code></p>
<dd>List the WPA authentication parameters currently set.</p>
<dt><code>wpa</code>[keys]</p>
<dd>List all the WPA encryption keys set in the device.</p>
<dt><code>genie</code></p>
<dd>List the Generic Information Elements set in the device (used for WPA support).</p>
<dt><code>modu</code>[lation]</p>
<dd>List the modulations supported by the device and the modulations currently enabled.</p>
<dt><code>&#8211;version</code></p>
<dd>Display the version of the tools, as well as the recommended and current Wireless Extensions version for the tool and the various wireless interfaces.</p>
<dt><code>&#8211;help</code></p>
<dd>Display short help message.</dl>
<h2>Files</h2>
<p><i>/proc/net/wireless</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwspy/">iwspy</a></code>(8). <code><a href="/docs/linux/man/8-iwevent/">iwevent</a></code>(8), <code><a href="/docs/linux/man/8-iwpriv/">iwpriv</a></code>(8), <code><a href="/docs/linux/man/7-wireless/">wireless</a></code>(7). </p>
