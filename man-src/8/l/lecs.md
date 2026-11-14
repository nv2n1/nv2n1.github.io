---
title: "lecs(8)"
name: "lecs"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lecs/"
description: "les, bus – ATM LAN Emulation service demons"
---

<p>les, bus &#8211; ATM LAN Emulation service demons</p>
<h2>Synopsis</h2>
<p><code>lecs</code> [<code>-l&nbsp;<wbr></code><i>listen_address</i>] [<code>-f&nbsp;<wbr></code><i>configuration_file</i>] [<code>-d&nbsp;<wbr>]</code></p>
<h2>Description</h2>
<p>LE Service consists of three components: LAN Emulation Configuration Server (<code>lecs</code>), LAN Emulation Server ( <code><a href="/docs/linux/man/8-les/">les</a>(8)</code>) and Broadcast and Unknown Server (<code><a href="/docs/linux/man/8-bus/">bus</a>(8)</code>). </p>
<p> <code>Lecs</code> implements the distribution of LECs to different emulated LANs. This is done by giving different LAN Emulation Server ATM addresses to LECs. Distribution is based on <code>lecs</code>&#8216;s configuration database and information provided by the LE client. It is not required that a <code>lecs</code> exists for all emulated LANs. It is possible to bypass this configuration phase by directly telling ATM address of the <code><a href="/docs/linux/man/8-les/">les</a>(8)</code> to the LEC. </p>
<p> Configuration file example for <code>lecs</code>: </p>
<pre># Our ATM address (should be included to differentiate us from 
# e.g. LEC)
# Must be before ELAN definitions
470023000000030300010002010020ea000ae905
# ELAN name is inside brackets.
# Parameters below are for Ethernet type LE (Linux &amp; almost all 
# other LE clients)
[tut-lane1]
# Address of the LES
LES:=470023000000030300010002010020ea000ae901
# 802_3 or 802_5 (802_3 = Ethernet)
Type:=802_3
# 1515, 4544, 9234 or 18190 (1516= Ethernet)
Max_Frame:=1516
# ATM address for hosts that are guided to this ELAN. 
# Wildcard is x or X.
470023000000030300010002010020ea0005aax0
470023000000030000010002010020ea0005bx00
47.002300000003030001000201.00603E2FDX23.00
470023000000030300010002010020ea000Xxx00
DEFAULT
# Another ELAN, which has empty name
[asdf]
# This directive sets this elan as the default i.e. it will be
# included if LEC's configure request could not be matched to 
# other ELANs
#DEFAULT
LES= 470023000000030300010002010020ea000ae902
Type=Ethernet</pre>
<p>Rules for finding ELAN definitions using information provided in LE_CONFIGURE_REQUEST and the configuration file are as follows: </p>
<pre>1. Find an entry where ELAN-NAME matches exactly and an 
 ATM address of the LEC is found in ELAN definition. 
 These are to match exactly with the information given in 
 LE_CONFIGURE_REQUEST. If ELAN-NAME is found, but ATM 
 address doesn't match then reject with reason &quot;Permission 
 denied&quot;.
2. Search for first ELAN which matches in type of emulated LAN, 
 maximum frame size and ATM address of the LEC.
3. If matching ELAN was not found, return default ELAN 
 definitions.
4. No match, so request is rejected with reason &quot;No 
 Configuration&quot;.</pre>
<p><code>SIGHUP</code> restarts the server.</p>
<h2>Options</h2>
<dl>
<dt>
<dt><code>-d</code></p>
<dd>
<dd>Reads the configuration file, dumps its contents and exits.</p>
<dt><code>-l&nbsp;<wbr></code><i>listen_address</i></p>
<dd>Use the <i>listen_address</i> to where wait connections.</p>
<dt><code>-f&nbsp;<wbr></code><i>configuration_file</i></p>
<dd>Use the specified configuration file instead of <code>.lecs_conf</code>.</dl>
<h2>Files</h2>
<dl>
<dt><code>.lecs_conf</code></p>
<dd>configuration file</dl>
<h2>Bugs</h2>
<p>Undocumented.</p>
<h2>Author</h2>
<p>Marko Kiiskila, TUT &lt;carnil [at] cs.tut.fi&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-les/">les</a>(8), <a href="/docs/linux/man/8-atmsigd/">atmsigd</a>(8), <a href="/docs/linux/man/8-zeppelin/">zeppelin</a>(8) </p>
