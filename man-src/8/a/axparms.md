---
title: "axparms(8)"
name: "axparms"
section: "8"
letter: "a"
url: "/docs/linux/man/8-axparms/"
description: "axparms – Configure AX.25 interfaces."
---

<p>axparms &#8211; Configure AX.25 interfaces.</p>
<h2>Synopsis</h2>
<p><code>axparms &#8211;assoc|&#8211;forward|&#8211;route|&#8211;setcall|&#8211;version &#8230;</code></p>
<h2>Description</h2>
<p>The <code>axparms</code> command is designed to be a multi-function command that allows miscellaneous commands to be issued to the Linux AX.25 protocol layer. It includes the functionality of <code>axassociate</code> and <code>axsetcall</code> which this command superceedes. The different modes of the command are chosen by the first argument. Sunsequent arguments depend upon this argument and so no generalised command format can be given.</p>
<h2>&#8211;assoc Argument</h2>
<p>The format of this option is: </p>
<pre><code>axparms --assoc &lt;callsign&gt; &lt;username&gt;</code>
<br>
<code>axparms --assoc &lt;callsign&gt; delete</code>
<br>
<code>axparms --assoc policy [default|deny]</code>
<br>
<code>axparms --assoc show</code></pre>
<p>This option mainpulates the kernel uid/callsign mapping table, allowing callsigns to be associated and dis-associated with a user. The <code>policy</code> option permits the superuser to have all other uid&#8217;s either default to the actual port name, or to block traffic. </p>
<p> At power up the table is blank and the policy is &#8216;default&#8217;, which is thus backward compatible.</p>
<h2>&#8211;forward Argument</h2>
<p>Allows the use of many receivers with one transmitter, known as packet forwarding in many systems. The format of this command is: </p>
<pre><code>axparms --forward &lt;portfrom&gt; &lt;portto&gt;</code>
<br>
<code>axparms --forward &lt;portfrom&gt; delete</code></pre>
<p>Any packets to be transmitted on port portfrom will be transmitted on port portto. This will stay in force until the second form of the command is issued which will remove the association.</p>
<h2>&#8211;route Argument</h2>
<p>This option allows the internal AX.25 routing table to be manipulated. This table is available for reading in /proc/net/ax25_route, and will be built up dynamically by stations heard. However it is possible to add, delete and list entries via this option. </p>
<p> The formats of this option are: </p>
<pre><code>axparms --route add &lt;port&gt; &lt;callsign&gt; [&lt;digis&gt;] [--ipmode V|D]</code>
<br>
<code>axparms --route del &lt;port&gt; &lt;callsign&gt;</code></pre>
<p><code>axparms &#8211;route list</code> </p>
<p> Routes added via this command will not be removed from the internal routing table when they are lqoldrq as normal entries are. The <code>&#8211;ipmode</code> option sets mode vc or mode datagram for this destination. </p>
<p> If the &lt;callsign&gt; argument is set to lqdefaultrq then this will set the default route for all outgoing AX.25 connections which will be used when there is no specific route to the required destination.</p>
<h2>&#8211;setcall Argument</h2>
<p>The format of this option is: </p>
<p> <code>axparms &#8211;setcall &lt;interface&gt; &lt;callsign&gt;</code> </p>
<p> This changes the callsign associated at the given physical ax25 interface. </p>
<p> Cave: The interface name is not the symbolic port name from axports, but the real interface name (from <a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8)): ax0, ax1, .., sp0, .., bpq0, &#8230; etc.. </p>
<p> The change is permanent as long as the interface exists, or another lqaxparms &#8211;setcallrq is issued. </p>
<p> The interface has to exist already in order to use this option; it may be in state UP or DOWN.</p>
<h2>&#8211;version Argument</h2>
<p>This option displays the version of the AX.25 utilities that <code>axparms</code> belongs to.</p>
<h2>Files</h2>
<p>/proc/net/ax25_bpqether<br />
 /proc/net/ax25_calls<br />
 /etc/ax25/axports</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-call/">call</a></code>(1), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/8-axctl/">axctl</a></code>(8), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5).</p>
<h2>Authors</h2>
<pre>Alan Cox GW4PTS &lt;alan [at] cymru.net&gt;
<br>
Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;
<br>
Joerg Reuter DL1BKE &lt;jreuter [at] poboxes.com&gt;</pre>
