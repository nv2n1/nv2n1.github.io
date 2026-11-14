---
title: "ip-macsec(8)"
name: "ip-macsec"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-macsec/"
description: "ip-macsec – MACsec device configuration"
---

<p>ip-macsec &#8211; MACsec device configuration</p>
<h2>Synopsis</h2>
<p><code>ip link add link </code><i>DEVICE</i><code> name </code><i>NAME</i><code> type macsec </code> [ [ <code>address</code><i> &lt;lladdr&gt;</i> ] <code>port</code><i> PORT</i> | <code>sci</code><i> &lt;u64&gt;</i> ] [ <code>cipher</code> { <code>default</code> | <code>gcm-aes-128</code> | gcm-aes-256 } ] [ <code>icvlen</code><i> ICVLEN</i> ] [ <code>encrypt</code> { <code>on</code> | <code>off</code> } ] [ <code>send_sci</code> { <code>on</code> | <code>off</code> } ] [ <code>end_station</code> { <code>on</code> | <code>off</code> } ] [ <code>scb</code> { <code>on</code> | <code>off</code> } ] [ <code>protect</code> { <code>on</code> | <code>off</code> } ] [ <code>replay</code> { <code>on</code> | <code>off</code> } ] [ <code>window</code><i> WINDOW</i> ] [ <code>validate</code> { <code>strict</code> | <code>check</code> | <code>disabled</code> } ] [ <code>encodingsa</code><i> SA</i> ] [ <code>offload</code> { <code>off</code> | <code>phy</code> | <code>mac</code> } ] <code>ip macsec add </code><i>DEV</i><code> tx sa</code> { <i>0..3</i> } [ <i>OPTS</i> ] <code>key</code><i> ID KEY</i><br />
 <code>ip macsec set </code><i>DEV</i><code> tx sa</code> { <i>0..3</i> } [ <i>OPTS</i> ]<br />
 <code>ip macsec del </code><i>DEV</i><code> tx sa</code> { <i>0..3</i> } <code>ip macsec add </code><i>DEV</i><code> rx </code><i>SCI</i> [<code> on </code>|<code> off </code>]<br />
 <code>ip macsec set </code><i>DEV</i><code> rx </code><i>SCI</i> [<code> on </code>|<code> off </code>]<br />
 <code>ip macsec del </code><i>DEV</i><code> rx </code><i>SCI</i> <code>ip macsec add </code><i>DEV</i><code> rx </code><i>SCI</i><code> sa</code> { <i>0..3</i> } [ <i>OPTS</i> ] <code>key</code><i> ID KEY</i><br />
 <code>ip macsec set </code><i>DEV</i><code> rx </code><i>SCI</i><code> sa</code> { <i>0..3</i> } [ <i>OPTS</i> ]<br />
 <code>ip macsec del </code><i>DEV</i><code> rx </code><i>SCI</i><code> sa</code> { <i>0..3</i> } <code>ip macsec offload </code><i>DEV</i> { <code>off</code> | <code>phy</code> | <code>mac</code> } <code>ip macsec show</code> [<i> DEV </i>] </p>
<pre><code>OPTS := [

pn {

    1..2^32-1 } ] [

on | off ]


SCI := {

    sci

    &lt;u64&gt; |

    port

    PORT

    address &lt;lladdr&gt;

}

PORT := { 1..2^16-1 }

</code></pre>
<h2>Description</h2>
<p>The <code>ip macsec</code> commands are used to configure transmit secure associations and receive secure channels and their secure associations on a MACsec device created with the <code>ip link add</code> command using the <i>macsec</i> type. </p>
<h2>Examples</h2>
<h3>Create a MACsec device on link eth0 (offload is disabled by default)</h3>
<pre># ip link add link eth0 macsec0 type macsec port 11 encrypt on</pre>
<h3>Configure a secure association on that device</h3>
<pre># ip macsec add macsec0 tx sa 0 pn 1024 on key 01 81818181818181818181818181818181</pre>
<h3>Configure a receive channel</h3>
<pre># ip macsec add macsec0 rx port 1234 address c6:19:52:8f:e6:a0</pre>
<h3>Configure a receive association</h3>
<pre># ip macsec add macsec0 rx port 1234 address c6:19:52:8f:e6:a0 sa 0 pn 1 on key 00 82828282828282828282828282828282</pre>
<h3>Display MACsec configuration</h3>
<pre># ip macsec show</pre>
<h3>Configure offloading on an interface</h3>
<pre># ip macsec offload macsec0 phy</pre>
<h3>Configure offloading upon MACsec device creation</h3>
<pre># ip link add link eth0 macsec0 type macsec port 11 encrypt on offload mac</pre>
<h2>Notes</h2>
<p>This tool can be used to configure the 802.1AE keys of the interface. Note that 802.1AE uses GCM-AES with a initialization vector (IV) derived from the packet number. The same key must not be used with the same IV more than once. Instead, keys must be frequently regenerated and distributed. This tool is thus mostly for debugging and testing, or in combination with a user-space application that reconfigures the keys. It is wrong to just configure the keys statically and assume them to work indefinitely. The suggested and standardized way for key management is 802.1X-2010, which is implemented by wpa_supplicant. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip-link/">ip-link</a></code>(8) <code><a href="/docs/linux/man/8-wpa_supplicant/">wpa_supplicant</a></code>(8)</p>
<h2>Author</h2>
<p>Sabrina Dubroca &lt;sd [at] queasysnail.net&gt;</p>
