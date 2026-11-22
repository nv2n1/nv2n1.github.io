---
title: "wireless(7)"
name: "wireless"
section: "7"
letter: "w"
url: "/docs/linux/man/7-wireless/"
description: "wireless – Wireless Tools and Wireless Extensions"
---

<p>wireless &#8211; Wireless Tools and Wireless Extensions</p>
<h2>Synopsis</h2>
<p><code>iwconfig</code><br/>
 <code>iwpriv -a</code></p>
<h2>Description</h2>
<p>The <code>Wireless Extensions</code> is an API allowing you manipulate Wireless LAN networking interfaces. It is composed of a variety of tools and configuration files. It is documented in more detail in the Linux Wireless LAN Howto.<br/>
 The <code>Wireless Tools</code> are used to change the configuration of wireless LAN networking interfaces on the fly, to get their current configuration, to get statistics and diagnose them. They are described in their own man page, see below for references.<br/>
 <code>Wireless configuration</code> is specific to each Linux distribution. This man page will contain in the future the configuration procedure for a few common distributions. For the time being, check the file DISTRIBUTIONS.txt included with the Wireless Tools package.</p>
<h2>Debian 3.0</h2>
<p>In Debian 3.0 (and later) you can configure wireless LAN networking devices using the network configuration tool <code>ifupdown</code>(8).</p>
<dl>
<dt><code>File :</code></dt>
<dd><i>/etc/network/interfaces</i></dd>
<dt><code>Form :</code></dt>
<dd>wireless-<i>&lt;function&gt; &lt;value&gt;</i><br/>
 wireless-essid Home<br/>
 wireless-mode Ad-Hoc</dd>
<dt><code>See also :</code></dt>
<dd><i>/etc/network/if-pre-up.d/wireless-tools</i><br/>
 <i>/usr/share/doc/wireless-tools/README.Debian</i></dd></dl>
<h2>SuSE 8.0</h2>
<p>SuSE 8.0 (and later) has integrated wireless configuration in their network scripts.</p>
<dl>
<dt><code>Tool :</code></dt>
<dd><code>Yast2</code></dd>
<dt><code>File :</code></dt>
<dd><i>/etc/sysconfig/network/wireless</i><br/>
 <i>/etc/sysconfig/network/ifcfg-*</i></dd>
<dt><code>Form :</code></dt>
<dd>WIRELESS_<i>&lt;function&gt;</i>=<i>&lt;value&gt;</i><br/>
 WIRELESS_ESSID=&quot;Home&quot;<br/>
 WIRELESS_MODE=Ad-Hoc</dd>
<dt><code>See also :</code></dt>
<dd>man ifup<br/>
 info scpm</dd></dl>
<h2>Original Pcmcia Scripts</h2>
<p>If you are using the original configuration scripts from the Pcmcia package, you can use this method.</p>
<dl>
<dt><code>File :</code></dt>
<dd><i>/etc/pcmcia/wireless.opts</i></dd>
<dt><code>Form :</code></dt>
<dd>*,*,*,*) </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ESSID=&quot;Home&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MODE=&quot;Ad-Hoc&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;;;</p>
<dt><code>See also :</code></dt>
<dd><i>/etc/pcmcia/wireless</i><br/>
 File <i>PCMCIA.txt</i> part of Wireless Tools package</dd></dl>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com<br/>
 <i><a rel="nofollow" href="http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/">http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/</a></i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwlist/">iwlist</a></code>(8), <code><a href="/docs/linux/man/8-iwspy/">iwspy</a></code>(8), <code><a href="/docs/linux/man/8-iwpriv/">iwpriv</a></code>(8), <code><a href="/docs/linux/man/8-iwevent/">iwevent</a></code>(8). </p>
