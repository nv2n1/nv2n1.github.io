---
title: "kissparms(8)"
name: "kissparms"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kissparms/"
description: "kissparms – Configure KISS TNCs."
---

<p>kissparms &#8211; Configure KISS TNCs.</p>
<h2>Synopsis</h2>
<p><code>kissparms [-c crc-type] -p &lt;port&gt; [-f y|n] [-h hw] [-l txtail] [-r pers] [-s slot] [-t txd] [-e feclevel] [-v] [-x] [-X raw] </code></p>
<h2>Description</h2>
<p><code>Kissparms</code> is used to dynamically configure KISS TNCs that have been setup for AX.25 use by <code>kissattach.</code> This program uses the packet interface to allow it to communicate with the KISS TNC without interrupting the AX.25 data stream. Therefore the KISS parameters may be set at any time during the operation of the AX.25 port. </p>
<p> A full description of the KISS protocol can be found in the ARRL 6th Computer Networking Conference papers pp 38-43. While use of the Tx Tail value is now deprecated, it has been included to satisfy the requirements of users of old TNC firmware. </p>
<p> Although this utility was originally designed for controlling KISS TNCs connected to a serial port, it is used by a number of other Linux packet radio devices such as the Z8530 SCC driver for controlling their parameters in exactly the same manner. Therefore <code>kissparms</code> functionality extends to more than KISS TNCs.</p>
<h2>Options</h2>
<dl>
<dt><code>-c crc-type</code></dt>
<dd>Sets the crc-type to use. For e.g. kernel mkiss: 0 = auto, 1 = none, 2 = flexnet, 3 = smack</dd>
<dt><code>-p port</code></dt>
<dd>Sets the port that is being configured.</dd>
<dt><code>-f y|n</code></dt>
<dd>This sets the TNC into either full duplex &#8220;y&#8221;, or half duplex &#8220;n&#8221; mode.</dd>
<dt><code>-h hardware</code></dt>
<dd>This is used to set hardware specific parameters.</dd>
<dt><code>-e FEC error correction level</code></dt>
<dd>Sets the FEC error correction level in a DSP card based modem (KISS parameter 8). Larger correction level means better noise resistance, but slower throughput on a good connection. This is an experimental feature found in a QPSK modem for the Motorola DSP56001 based DSP4 and EVM cards only.</dd>
<dt><code>-l txtail</code></dt>
<dd>Sets the TX Tail time in milliseconds. Note that the command to the TNC only operates in steps of ten milliseconds, so only use values like 10, 20 etc.</dd>
<dt><code>-r persist</code></dt>
<dd>Sets the persist value. This parameter is scaled to the range 0 to 255.</dd>
<dt><code>-s slottime</code></dt>
<dd>Sets the slottime in milliseconds. Note that the command to the TNC only operates in steps of ten milliseconds, so only use values like 10, 20 etc.</dd>
<dt><code>-t txdelay</code></dt>
<dd>Sets the TX Delay in milliseconds. Note that the command to the TNC only operates in steps of ten milliseconds, so only use values like 10, 20 etc.</dd>
<dt><code>-v</code></dt>
<dd>Display the version.</dd>
<dt><code>-x</code></dt>
<dd>Takes the TNC out of KISS mode back into &#8220;normal&#8221; mode. This command is manufacturer specific but works in many cases. This option overrides all options except the port number.</dd>
<dt><code>-X</code><i>raw</i></dt>
<dd>Sends the specified raw value to the kiss driver.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
