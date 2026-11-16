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
<p><i>ttyI</i><code>[</code><i>0-63</i><code>]</code> are emulated tty devices of the Linux <font SIZE="-1">ISDN</font> subsystem. These devices can be used in the same way as the traditional serial devices <i>ttySx.</i> The official major device numbers are <code>43</code> for <i>ttyI .</i> The minor device numbers start with <code>0</code> and end with <code>63</code>. The <font SIZE="-1">ISDN</font> tty devices are equipped with a modem emulation implementing a set of traditional and some special AT commands. This provides easy use together with almost all communication software that uses modem commands: <code><a href="/docs/linux/man/1-minicom/">minicom</a></code>(1), <code>seyon</code>(1), <code>XCept</code>(1), <code><a href="/docs/linux/man/8-uucico/">uucico</a></code>(8), <code><a href="/docs/linux/man/8-mgetty/">mgetty</a></code>(8), <code>dip</code>(8), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) and more. When enabled during kernel configuration, the emulator is capable of a reduced set of commands to support audio. To use audio features, an <font SIZE="-1">ISDN</font> card with a audio-capable low-level driver is needed. Currently the only audio-capable drivers are the teles and HiSax driver. The line disciplines are handled by the kernel so that SLIP, CSLIP and asynchronous PPP are possible. The port speed of the <font SIZE="-1">ISDN</font> tty devices is always 64000 bps. </p>
<h2>At Command Set</h2>
<p>The description of <code>AT commands</code> here does <code>not</code> cover audio related commands. For a description of audio related commands, see <code><a href="/docs/linux/man/4-isdn_audio/">isdn_audio</a></code>(4). The following <code>AT commands</code> are supported by <font SIZE="-1">ISDN</font> tty devices:</p>
<dl>
<dt><code>ATA</code></dt>
<dd>Answer an incoming call.</dd>
<dt><code>ATD</code><i>num</i></dt>
<dd>Dial number <i>num</i>. Allowed are digits [0-9] and the characters &quot;,&quot;, &quot;#&quot;, &quot;.&quot;, &quot;*&quot;, &quot;W&quot;, &quot;P&quot;, &quot;T&quot;, &quot;S&quot;, &quot;-&quot;. The characters are ignored except of &quot;S&quot; which indicates a SPV if it precedes the number (<code>only</code> German 1TR6 ISDN).</dd>
<dt><code>ATE0</code></dt>
<dd>Echo off.</dd>
<dt><code>ATE1</code></dt>
<dd>Echo on (default).</dd>
<dt><code>ATH</code></dt>
<dd>Hang up.</dd>
<dt><code>ATH0</code></dt>
<dd>Hang up.</dd>
<dt><code>ATH1</code></dt>
<dd>Off hook (ignored).</dd>
<dt><code>ATI</code></dt>
<dd>Return device Information (&quot;ISDN for Linux&#8230;&quot;).</dd>
<dt><code>ATI0</code></dt>
<dd>Return device Information (&quot;ISDN for Linux&#8230;&quot;).</dd>
<dt><code>ATI1</code></dt>
<dd>Return device Information (&quot;ISDN for Linux&#8230;&quot;).</dd>
<dt><code>ATI2</code></dt>
<dd>Return Statistics of last connection.</dd>
<dt><code>ATO</code></dt>
<dd>Return from command mode to online mode (data mode).</dd>
<dt><code>ATQ0</code></dt>
<dd>Enable result codes (default).</dd>
<dt><code>ATQ1</code></dt>
<dd>Disable result codes.</dd>
<dt><code>ATS</code><i>x</i><code>=</code><i>y</i></dt>
<dd>Set register <i>x</i> to value <i>y</i>.</dd>
<dt><code>ATS</code><i>x</i><code>?</code></dt>
<dd>Show content of register <i>x</i>.</dd>
<dt><code>ATS</code><i>x</i><code>.</code><i>y</i><code>=</code><i>z</i></dt>
<dd>Set register <i>x</i>, bit <i>y</i> to value <i>z</i></dd>
<dt><code>ATS</code><i>x</i><code>.</code><i>y</i><code>?</code></dt>
<dd>Show bit <i>y</i> of register <i>x</i>.</dd>
<dt><code>ATV0</code></dt>
<dd>Print result code as number.</dd>
<dt><code>ATV1</code></dt>
<dd>Print result code as text (default).</dd>
<dt><code>ATZ</code></dt>
<dd>Reset all registers and load profile values.</dd>
<dt><code>AT&amp;B</code><i>x</i></dt>
<dd>Set packet size of outgoing packets to value <i>x</i> (maximum 4000). The actual packet size depends on the hardware driver and may be smaller than <i>x</i> (e.g. with the teles driver). There will be <code>no</code> error message if the value is bigger than the hardware driver can process. However the size of the outgoing packets will be set correctly.</dd>
<dt><code>AT&amp;D2</code></dt>
<dd>DTR falling edge: hang up and return to command mode (default).</dd>
<dt><code>AT&amp;D3</code></dt>
<dd>DTR falling edge: hang up, return to command mode and reset all registers.</dd>
<dt><code>AT&amp;E</code><i>x</i></dt>
<dd>Set MSN (Euro-ISDN, EDSS1) or EAZ (German 1TR6) to value <i>x</i>. For MSNs, <i>x</i> is a string of digits representing the local phone number, while for EAZs <i>x</i> should be only the last digit of the Number.</dd>
<dt><code>AT&amp;F</code></dt>
<dd>Set all registers and profile to &quot;factory-defaults&quot;.</dd>
<dt><code>AT&amp;L</code><i>plist</i></dt>
<dd>Set list of phone numbers to listen on. <i>plist</i> is a list of wildcard patterns separated by semicolon. If this is set, it has precedence over the MSN set by AT&amp;E.</dd>
<dt><code>AT&amp;V</code></dt>
<dd>Show current register settings.</dd>
<dt><code>AT&amp;W0</code></dt>
<dd>Write registers and EAZ/MSN to profile. (You need to run <code><a href="/docs/linux/man/8-iprofd/">iprofd</a></code>(8) for making changes permanent.)</dd>
<dt><code>AT&amp;X0</code></dt>
<dd>Disable BTX-Mode (default).</dd>
<dt><code>AT&amp;X1</code></dt>
<dd>Enable BTX-Mode.</dd></dl>
<h2>Escape Sequence</h2>
<p>During a data connection, the driver can be set to command mode by typing in <i>delay</i><code>+++</code><i>delay</i>. The escape character (default &quot;+&quot;) may be set via register 2. The <i>delay</i> must be at least 1.5 seconds and between each escape character the pause must not exceed 0.5 seconds. <i>ATO</i> brings the modem emulation back to data mode.</p>
<h2>Registers</h2>
<dl>
<dt><code>0</code> (default 0)</dt>
<dd>Number of rings on which the &quot;modem&quot; will answer. (S0=0 will disable auto answering).</dd>
<dt><code>1</code> (default 0)</dt>
<dd>Counts and stores the number of rings from an incoming call.</dd>
<dt><code>2</code> (default 43 = &#8216;+&#8217;)</dt>
<dd>ASCII code of the escape character.</dd>
<dt><code>3</code> (default 13 = CR)</dt>
<dd>ASCII code of Carriage Return.</dd>
<dt><code>4</code> (default 10 = LF)</dt>
<dd>ASCII code of Line Feed.</dd>
<dt><code>5</code> (default 8 = BS)</dt>
<dd>ASCII code of Backspace.</dd>
<dt><code>6</code> (default 3)</dt>
<dd>Duration, in number of seconds, modem waits before dialling.</dd>
<dt><code>7</code> (default 60)</dt>
<dd>Wait time for carrier in seconds.</dd>
<dt><code>8</code> (default 2)</dt>
<dd>Pause time for comma (&#8216;,&#8217;) in dial command in seconds (ignored).</dd>
<dt><code>9</code> (default 6)</dt>
<dd>Carrier detect time in tenths of seconds (ignored).</dd>
<dt><code>10</code> (default 7)</dt>
<dd>Wait time until hangup after carrier loss in tenths of seconds (ignored).</dd>
<dt><code>11</code> (default 70)</dt>
<dd>Duration and delay in milliseconds for touch tone dialling (ignored).</dd>
<dt><code>12</code> (default 69)</dt>
<dd>Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</dd>
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
<dt><code>13</code> (default 4)</dt>
<dd>Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</dd>
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
<dt><code>14</code> (default 0)</dt>
<dd>Layer-2 protocol. </dd>
<p>&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>X75/LAPB with I-frames. </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>X75/LAPB with UI-frames. </p>
<p>&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>X75/LAPB with BUI-frames. </p>
<p>&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>HDLC. </p>
<p>&nbsp;<wbr>4&nbsp;<wbr>=&nbsp;<wbr>TRANSPARENT.<br />
 10 = Analog Modem. (only if hardware supports this)<br />
 11 = Fax G3. (only if hardware supports this)</p>
<dt><code>15</code> (default 0)</dt>
<dd>Layer-3 protocol.<br />
 0 = transparent<br />
 1 = transparent with audio features (e.g. DSP)<br />
 2 = Fax G3</dd>
<dt><code>16</code> (default 250)</dt>
<dd>Outgoing packet size / 16.</dd>
<dt><code>17</code></dt>
<dd>reserved.</dd>
<dt><code>18</code> (default 4)</dt>
<dd>Service-Octet-1 to accept or to be used on dial out.<br />
 Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</dd>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Service 1 (audio) when set.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Service 5 (BTX) when set.</p>
<p> 2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Service 7 (data) when set.</p>
<dl>
<dd>
</dd><dl>
<dd>Note: It is possible to set more than one bit. In this case, on outgoing calls, the most significant 1-bit is chosen to select the outgoing service octet. On incoming calls the selected services are accepted, contents of register 14 is ignored and the Layer-2-protocol is automatically set with the following values to match the service of the incoming call:</dd>
<dl>
<dd>
</dd><dl>
<dt>Incoming service <i>audio</i> (Reg. 20.0 = 1)</dt>
<dd>L2-protocol is set to 4 (TRANSPARENT).</dd>
<dt>Incoming service <i>BTX</i> (Reg. 20.1 = 1)</dt>
<dd>L2-protocol is set to 0 (X75/LAPB with I-frames).</dd>
<dt>Incoming service <i>date</i> (Reg. 20.2 = 1)</dt>
<dd>L2-protocol is set to 0 (X75/LAPB with I-frames).</dd></dl>
</dl>
</dl>
</dl>
<dt><code>19</code> (default 0)</dt>
<dd>Service-Octet-2 (ignored when using EDSS1).</dd>
<dt><code>20</code> (read only)</dt>
<dd>Service-Octet-1 of last incoming call. This bit-mapped register is set on incoming call (during RING). Mapping is the same like register 18.</dd>
<dt><code>21</code> (read only)</dt>
<dd>Bit-mapped register. Set on incoming call (during RING) to the value of octet 3 of calling party number Information Element (Numbering plan). See section <code>4.5.10</code> of <code>ITU Q.931</code>.</dd>
<dt><code>22</code> (read only)</dt>
<dd>Bit-mapped register. Set on incoming call (during RING) to the value of octet 3a of calling party number Information Element (Screening info). See section <code>4.5.10</code> of <code>ITU Q.931</code>.</dd>
<dt><code>23</code> (default 0)</dt>
<dd>Bit-mapped register.<br />
 Bit<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Description</dd>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Disable CPN extended RING.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Enable CPN extended RING.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Disable CPN extended FCON.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Enable CPN extended FCON.</p>
<dt></dt></dl>
<h2>Note</h2>
<dd>There used also be <i>cui</i> devices (major device number 44), but since the <i>cua</i> devices for regular tty devices are no longer supported in the kernel, these are also no longer supported for ISDN4linux.</dd>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;<br />
 modified by Paul Slootman &lt;paul [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-icnctrl/">icnctrl</a></code>(8), <code>telesctrl</code>(8), <code><a href="/docs/linux/man/4-isdninfo/">isdninfo</a></code>(4), <code><a href="/docs/linux/man/4-isdn_audio/">isdn_audio</a></code>(4), <code><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></code>(8). </p>
