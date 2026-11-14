---
title: "ttyi(4)"
name: "ttyi"
section: "4"
letter: "t"
url: "/docs/linux/man/4-ttyi/"
description: "ttyI – ISDN character devices with modem emulator"
---

<p>ttyI &#8211; ISDN character devices with modem emulator</p>
<h2>Description</h2>
<p><i>ttyI</i><code>[</code><i>0-63</i><code>]</code> are emulated tty devices of the Linux <font SIZE="-1">ISDN</font> subsystem. These devices can be used in the same way as the traditional serial devices <i>ttySx.</i> The official major device numbers are <code>43</code> for <i>ttyI .</i> The minor device numbers start with <code>0</code> and end with <code>63</code>. The <font SIZE="-1">ISDN</font> tty devices are equipped with a modem emulation implementing a set of traditional and some special AT commands. This provides easy use together with almost all communication software that uses modem commands: <code><a href="/docs/linux/man/1-minicom/">minicom</a></code>(1), <code><a href="/docs/linux/man/1-seyon/">seyon</a></code>(1), <code><a href="/docs/linux/man/1-xcept/">XCept</a></code>(1), <code><a href="/docs/linux/man/8-uucico/">uucico</a></code>(8), <code><a href="/docs/linux/man/8-mgetty/">mgetty</a></code>(8), <code><a href="/docs/linux/man/8-dip/">dip</a></code>(8), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) and more. When enabled during kernel configuration, the emulator is capable of a reduced set of commands to support audio. To use audio features, an <font SIZE="-1">ISDN</font> card with a audio-capable low-level driver is needed. Currently the only audio-capable drivers are the teles and HiSax driver. The line disciplines are handled by the kernel so that SLIP, CSLIP and asynchronous PPP are possible. The port speed of the <font SIZE="-1">ISDN</font> tty devices is always 64000 bps. </p>
<h2>At Command Set</h2>
<p>The description of <code>AT commands</code> here does <code>not</code> cover audio related commands. For a description of audio related commands, see <code><a href="/docs/linux/man/4-isdn_audio/">isdn_audio</a></code>(4). The following <code>AT commands</code> are supported by <font SIZE="-1">ISDN</font> tty devices:</p>
<dl>
<dt><code>ATA</code></p>
<dd>Answer an incoming call.</p>
<dt><code>ATD</code><i>num</i></p>
<dd>Dial number <i>num</i>. Allowed are digits [0-9] and the characters &quot;,&quot;, &quot;#&quot;, &quot;.&quot;, &quot;*&quot;, &quot;W&quot;, &quot;P&quot;, &quot;T&quot;, &quot;S&quot;, &quot;-&quot;. The characters are ignored except of &quot;S&quot; which indicates a SPV if it precedes the number (<code>only</code> German 1TR6 ISDN).</p>
<dt><code>ATE0</code></p>
<dd>Echo off.</p>
<dt><code>ATE1</code></p>
<dd>Echo on (default).</p>
<dt><code>ATH</code></p>
<dd>Hang up.</p>
<dt><code>ATH0</code></p>
<dd>Hang up.</p>
<dt><code>ATH1</code></p>
<dd>Off hook (ignored).</p>
<dt><code>ATI</code></p>
<dd>Return device Information (&quot;ISDN for Linux&#8230;&quot;).</p>
<dt><code>ATI0</code></p>
<dd>Return device Information (&quot;ISDN for Linux&#8230;&quot;).</p>
<dt><code>ATI1</code></p>
<dd>Return device Information (&quot;ISDN for Linux&#8230;&quot;).</p>
<dt><code>ATI2</code></p>
<dd>Return Statistics of last connection.</p>
<dt><code>ATO</code></p>
<dd>Return from command mode to online mode (data mode).</p>
<dt><code>ATQ0</code></p>
<dd>Enable result codes (default).</p>
<dt><code>ATQ1</code></p>
<dd>Disable result codes.</p>
<dt><code>ATS</code><i>x</i><code>=</code><i>y</i></p>
<dd>Set register <i>x</i> to value <i>y</i>.</p>
<dt><code>ATS</code><i>x</i><code>?</code></p>
<dd>Show content of register <i>x</i>.</p>
<dt><code>ATS</code><i>x</i><code>.</code><i>y</i><code>=</code><i>z</i></p>
<dd>Set register <i>x</i>, bit <i>y</i> to value <i>z</i></p>
<dt><code>ATS</code><i>x</i><code>.</code><i>y</i><code>?</code></p>
<dd>Show bit <i>y</i> of register <i>x</i>.</p>
<dt><code>ATV0</code></p>
<dd>Print result code as number.</p>
<dt><code>ATV1</code></p>
<dd>Print result code as text (default).</p>
<dt><code>ATZ</code></p>
<dd>Reset all registers and load profile values.</p>
<dt><code>AT&amp;B</code><i>x</i></p>
<dd>Set packet size of outgoing packets to value <i>x</i> (maximum 4000). The actual packet size depends on the hardware driver and may be smaller than <i>x</i> (e.g. with the teles driver). There will be <code>no</code> error message if the value is bigger than the hardware driver can process. However the size of the outgoing packets will be set correctly.</p>
<dt><code>AT&amp;D2</code></p>
<dd>DTR falling edge: hang up and return to command mode (default).</p>
<dt><code>AT&amp;D3</code></p>
<dd>DTR falling edge: hang up, return to command mode and reset all registers.</p>
<dt><code>AT&amp;E</code><i>x</i></p>
<dd>Set MSN (Euro-ISDN, EDSS1) or EAZ (German 1TR6) to value <i>x</i>. For MSNs, <i>x</i> is a string of digits representing the local phone number, while for EAZs <i>x</i> should be only the last digit of the Number.</p>
<dt><code>AT&amp;F</code></p>
<dd>Set all registers and profile to &quot;factory-defaults&quot;.</p>
<dt><code>AT&amp;L</code><i>plist</i></p>
<dd>Set list of phone numbers to listen on. <i>plist</i> is a list of wildcard patterns separated by semicolon. If this is set, it has precedence over the MSN set by AT&amp;E.</p>
<dt><code>AT&amp;V</code></p>
<dd>Show current register settings.</p>
<dt><code>AT&amp;W0</code></p>
<dd>Write registers and EAZ/MSN to profile. (You need to run <code><a href="/docs/linux/man/8-iprofd/">iprofd</a></code>(8) for making changes permanent.)</p>
<dt><code>AT&amp;X0</code></p>
<dd>Disable BTX-Mode (default).</p>
<dt><code>AT&amp;X1</code></p>
<dd>Enable BTX-Mode.</dl>
<h2>Escape Sequence</h2>
<p>During a data connection, the driver can be set to command mode by typing in <i>delay</i><code>+++</code><i>delay</i>. The escape character (default &quot;+&quot;) may be set via register 2. The <i>delay</i> must be at least 1.5 seconds and between each escape character the pause must not exceed 0.5 seconds. <i>ATO</i> brings the modem emulation back to data mode.</p>
<h2>Registers</h2>
<dl>
<dt><code>0</code> (default 0)</p>
<dd>Number of rings on which the &quot;modem&quot; will answer. (S0=0 will disable auto answering).</p>
<dt><code>1</code> (default 0)</p>
<dd>Counts and stores the number of rings from an incoming call.</p>
<dt><code>2</code> (default 43 = &#8216;+&#8217;)</p>
<dd>ASCII code of the escape character.</p>
<dt><code>3</code> (default 13 = CR)</p>
<dd>ASCII code of Carriage Return.</p>
<dt><code>4</code> (default 10 = LF)</p>
<dd>ASCII code of Line Feed.</p>
<dt><code>5</code> (default 8 = BS)</p>
<dd>ASCII code of Backspace.</p>
<dt><code>6</code> (default 3)</p>
<dd>Duration, in number of seconds, modem waits before dialling.</p>
<dt><code>7</code> (default 60)</p>
<dd>Wait time for carrier in seconds.</p>
<dt><code>8</code> (default 2)</p>
<dd>Pause time for comma (&#8216;,&#8217;) in dial command in seconds (ignored).</p>
<dt><code>9</code> (default 6)</p>
<dd>Carrier detect time in tenths of seconds (ignored).</p>
<dt><code>10</code> (default 7)</p>
<dd>Wait time until hangup after carrier loss in tenths of seconds (ignored).</p>
<dt><code>11</code> (default 70)</p>
<dd>Duration and delay in milliseconds for touch tone dialling (ignored).</p>
<dt><code>12</code> (default 69)</p>
<dd>Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</p>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Suppress response messages.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Show response messages.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Response messages as text.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Numeric response messages.</p>
<p> 2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Echo off.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Echo on.</p>
<p> 3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = DCD always on.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = DCD follows carrier.</p>
<p> 4<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = CTS follows RTS.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Ignore RTS, CTS always on.</p>
<p> 5<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Low-edge on DTR: Hangup and return</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>to command mode.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Same as 0 but also resets all</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>registers.</p>
<p> 6<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = DSR always on.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = DSR on only if channel is available.</p>
<p> 7<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Cisco-PPP-flag-hack off.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Cisco-PPP-flag-hack on.</p>
<dt><code>13</code> (default 4)</p>
<dd>Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</p>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Use delayed sending of data.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Immediately send data.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = T.70 protocol off.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = T.70 protocol on.</p>
<p> 2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Don&#8217;t hangup on DTR low.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Hangup on DTR low.</p>
<p> 3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Standard response messages.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Extended response messages.</p>
<p> 4<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = CALLER NUMBER before every RING.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = CALLER NUMBER after first RING.</p>
<p> 5<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Disable extended T.70 protocol.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Enable extended T.70 protocol.</p>
<p> 6<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Disable RUNG message.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = RUNG on cancelled incoming call.</p>
<p> 7<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Disable display messages from net.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Enable disable messages from net.</p>
<dt><code>14</code> (default 0)</p>
<dd>Layer-2 protocol. </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>X75/LAPB with I-frames. </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>X75/LAPB with UI-frames. </p>
<p>&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>X75/LAPB with BUI-frames. </p>
<p>&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>HDLC. </p>
<p>&nbsp;<wbr>4&nbsp;<wbr>=&nbsp;<wbr>TRANSPARENT.<br />
 10 = Analog Modem. (only if hardware supports this)<br />
 11 = Fax G3. (only if hardware supports this)</p>
<dt><code>15</code> (default 0)</p>
<dd>Layer-3 protocol.<br />
 0 = transparent<br />
 1 = transparent with audio features (e.g. DSP)<br />
 2 = Fax G3</p>
<dt><code>16</code> (default 250)</p>
<dd>Outgoing packet size / 16.</p>
<dt><code>17</code></p>
<dd>reserved.</p>
<dt><code>18</code> (default 4)</p>
<dd>Service-Octet-1 to accept or to be used on dial out.<br />
 Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</p>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Service 1 (audio) when set.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Service 5 (BTX) when set.</p>
<p> 2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Service 7 (data) when set.</p>
<dl>
<dd>
<dl>
<dd>Note: It is possible to set more than one bit. In this case, on outgoing calls, the most significant 1-bit is chosen to select the outgoing service octet. On incoming calls the selected services are accepted, contents of register 14 is ignored and the Layer-2-protocol is automatically set with the following values to match the service of the incoming call:</p>
<dl>
<dd>
<dl>
<dt>Incoming service <i>audio</i> (Reg. 20.0 = 1)</p>
<dd>L2-protocol is set to 4 (TRANSPARENT).</p>
<dt>Incoming service <i>BTX</i> (Reg. 20.1 = 1)</p>
<dd>L2-protocol is set to 0 (X75/LAPB with I-frames).</p>
<dt>Incoming service <i>date</i> (Reg. 20.2 = 1)</p>
<dd>L2-protocol is set to 0 (X75/LAPB with I-frames).</dl>
</dl>
</dl>
</dl>
<dt><code>19</code> (default 0)</p>
<dd>Service-Octet-2 (ignored when using EDSS1).</p>
<dt><code>20</code> (read only)</p>
<dd>Service-Octet-1 of last incoming call. This bit-mapped register is set on incoming call (during RING). Mapping is the same like register 18.</p>
<dt><code>21</code> (read only)</p>
<dd>Bit-mapped register. Set on incoming call (during RING) to the value of octet 3 of calling party number Information Element (Numbering plan). See section <code>4.5.10</code> of <code>ITU Q.931</code>.</p>
<dt><code>22</code> (read only)</p>
<dd>Bit-mapped register. Set on incoming call (during RING) to the value of octet 3a of calling party number Information Element (Screening info). See section <code>4.5.10</code> of <code>ITU Q.931</code>.</p>
<dt><code>23</code> (default 0)</p>
<dd>Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</p>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Disable CPN extended RING.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Enable CPN extended RING.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Disable CPN extended FCON.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Enable CPN extended FCON.</p>
<dt></dl>
<h2>Note</h2>
<dd>There used also be <i>cui</i> devices (major device number 44), but since the <i>cua</i> devices for regular tty devices are no longer supported in the kernel, these are also no longer supported for ISDN4linux.</p>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;<br />
 modified by Paul Slootman &lt;paul [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-icnctrl/">icnctrl</a></code>(8), <code><a href="/docs/linux/man/8-telesctrl/">telesctrl</a></code>(8), <code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4), <code><a href="/docs/linux/man/4-isdn_audio/">isdn_audio</a></code>(4), <code><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></code>(8). </p>
