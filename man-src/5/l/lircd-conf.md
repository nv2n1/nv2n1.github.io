---
title: "lircd-conf(5)"
name: "lircd-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lircd-conf/"
description: "lircd.conf – lirc main configuration file"
---

<p>lircd.conf &#8211; lirc main configuration file</p>
<h2>Description</h2>
<p>The file has two purposes: to provide timing information to the driver so it can decode the data to button presses, and to provide a mapping from button presses to key symbols used by <a href="/docs/linux/man/8-lircd/">lircd</a>(8). </p>
<p> The basic structure is a list of remote blocks. Whitespace and line breaks are used as delimiters. </p>
<p> If the comment character (#) appears as the first character on a line the rest of the line is ignored.</p>
<h2>Remote Blocks</h2>
<p>Remote blocks are either normal or raw. </p>
<p> Normal remote blocks begin with <code>begin remote</code> and ends with <code>end remote.</code> The first part of the block describes the basic properties of the remote, see REMOTE DESCRIPTION SECTION. Following this is a codes section, which is delimited by <code>begin codes</code> and <code>end codes.</code> </p>
<p> Each line in a codes section contains the name of a button on the remote followed by a hexidecimal data value matching the data part of the IR frame (see REMOTE DESCRIPTION SECTION). You may not assign the same name to two buttons in the same remote section. </p>
<p> Raw remote blocks are identical to normal blocks besides the codes section which is a list of button descriptions enclosed by <code>begin raw_codes</code> and <code>end raw_codes.</code> </p>
<p> A raw button description begins with the parameter <code>name</code> followed by the name of the button. The button description ends with the next button description or the end of the raw_codes block. The lines in between is a list of decimal numbers describing the signal sent by that button. The first number indicates the duration of the first pulse in microseconds. The second number indicates the duration of the space which follows it. Pulse and space durations alternate for as long as is necessary. The last duration should represent a pulse.</p>
<h2>Remote Description Section</h2>
<p>Each line in this section contains a parameter followed by the value or values that should be assigned to that parameter. Parameters are optional unless otherwise stated. </p>
<p> All values are decimal integers that are either dimensionless or have units of microseconds unless otherwise stated. Hexidecimal numbers should be prefixed by 0x. If the remote does not have a particular &quot;feature,&quot; then the line may be omitted. The button code is sent just after the pre signal and just before the post signal. </p>
<p> Some parameters describe the bits in the IR protocol. The frame is normally defined like</p>
<dl>
<dd>|header|plead|pre data|pre|data|post|post data|ptrail|foot|gap|</dl>
<p> where most parameters defaults to 0. Some parameters change the overall frame layout e. g., the repeat parameter. </p>
<dl>
<dt><code>include &#8221;&lt;path&gt;&#8221;</code></p>
<dd>Include the given path using normal <i>include</i> semantics. If the path is relative, it&#8217;s interpreted relative to the main lircd.conf file. &lt;path&gt; must be enclosed in double quotes. It can contain a <a href="/docs/linux/man/3-glob/">glob</a>(3) pattern in which case all matching files are included.</p>
<dt><code>manual_sort &lt;1|0&gt;</code></p>
<dd>Normally, lircd tries to sort multiple remotes so the one which decodes fastest are used first. Setting manual_sort to 1 in any remote disables this and uses the remotes in the order they are listed in lircd.conf or as the alphanumerically sorted filenames in lircd.conf.d.</p>
<dt><code>name &lt;remote name&gt;</code></p>
<dd>The unique name assigned to the remote control (may not contain whitespace). Within a single file all names must be unique. Parameter is mandatory.</p>
<dt><code>flags &lt;flag1&gt;&lt;|flag2&gt;&#8230;</code></p>
<dd>Flags are special text strings which describe various properties of the remote and determine the semantics of some of the following fields. Multiple flags should be separated by the pipe(|) symbol. See FLAGS.</p>
<dt><code>driver &lt;driver name&gt;</code></p>
<dd>For lirccode drivers which does not have timing information the optional driver attribute names the driver which is required to use this remote.</p>
<dt><code>bits &lt;number of data bits&gt;</code></p>
<dd>The number of data bits in the hexidecimal codes which describe each button (decimal integer).</p>
<dt><code>eps &lt;relative error tolerance&gt;</code></p>
<dd>The relative error tolerance for received signals in percent. By default, irrecord set this to 30 (i. e., 30%).</p>
<dt><code>aeps &lt;absolute error tolerance&gt;</code></p>
<dd>The absolute error tolerance for received signals (microseconds). The default is the hardcoded driver dependent resolution value. By default irrecord sets this to 100.</p>
<dt><code>header &lt;phead&gt; &lt;shead&gt;</code></p>
<dd>The initial pulse and space sent (microseconds).</p>
<dt><code>three &lt;pthree&gt; &lt;sthree&gt;</code></p>
<dd>Only used by RC-MM remotes</p>
<dt><code>two &lt;ptwo&gt; &lt;stwo&gt;</code></p>
<dd>Only used by RC-MM remotes</p>
<dt><code>one &lt;pone&gt; &lt;sone&gt;</code></p>
<dd>The pulse and space lengths representing a one.</p>
<dt><code>zero &lt;pzero&gt; &lt;szero&gt;</code></p>
<dd>The pulse and space lengths representing a zero.</p>
<dt><code>ptrail &lt;trailing pulse&gt;</code></p>
<dd>A trailing pulse, immediately following the post_data.</p>
<dt><code>plead &lt;leading pulse&gt;</code></p>
<dd>A leading pulse, immediately after the header.</p>
<dt><code>foot &lt;pfoot&gt; &lt;sfoot&gt;</code></p>
<dd>A pulse and space, immediately following the trailing pulse.</p>
<dt><code>repeat &lt;prepeat&gt; &lt;srepeat&gt;</code></p>
<dd>A pulse and space that replaces everything between leading pulse and the trailing pulse, whenever a signal is repeated. The foot is not sent, and the header is not sent unless the REPEAT_HEADER flag is present.</p>
<dt><code>pre_data_bits &lt;number of pre_data_bits&gt;</code></p>
<dd>The number of bits in the pre_data code.</p>
<dt><code>pre_data &lt;hexidecimal number&gt;</code></p>
<dd>Hexidecimal code indicating the sequence of ones and zeros immediately following the leading pulse.</p>
<dt><code>post_data_bits &lt;number of post data bits&gt;</code></p>
<dd>The number of bits in the post_data code.</p>
<dt><code>post_data &lt;hexidecimal number&gt;</code></p>
<dd>Hexidecimal code indicating the sequence of ones and zeros immediately following the post signal.</p>
<dt><code>pre &lt;ppre&gt; &lt;spre&gt;</code></p>
<dd>A pulse and space immediately following the pre_data.</p>
<dt><code>post &lt;ppost&gt; &lt;spost&gt;</code></p>
<dd>A pulse and space immediately following the button code.</p>
<dt><code>gap &lt;gap length&gt;</code></p>
<dd>A (typically long) space which follows the trailing pulse.</p>
<dt><code>repeat_gap &lt;repeat_gap length&gt;</code></p>
<dd>A gap immediately following the trailing pulse, and preceding a repetition of the same code that&#8217;s due to a the same press of the button.</p>
<dt><code>min_repeat &lt;minimum number of repetitions&gt;</code></p>
<dd>The minimum times a signal is repeated when sent. Note that 0 means the signal is sent only once. Not used when receiving.</p>
<dt><code>toggle_bit &lt;bit to toggle&gt;</code></p>
<dd>A bit of the pre_data, code, or post_data that is toggled between one and zero each time a button is pressed. This parameter is obsoleted by toggle_bit_mask and should be used in new configs.</p>
<dt><code>toggle_bit_mask &lt;hexadecimal mask&gt;</code></p>
<dd>Bits which are toggled between one and zero each time a button is pressed. The mask is applied to the concatenated value of pre data &#8211; data &#8211; post_data.</p>
<dt><code>repeat_mask &lt;mask&gt;</code></p>
<dd>Mask defines which bits are inverted for repeats.</p>
<dt><code>frequency &lt;hertz&gt;</code></p>
<dd>Remote carrier frequency, defaults to 38000.</p>
<dt><code>duty_cycle &lt;on time&gt;</code></p>
<dd>The percentage of time during a pulse that infrared light is being sent (default is 50). </p>
</dl>
<h2>Flags</h2>
<p>Flags are values set in the flags parameter.</p>
<dl>
<dt><code>RC5</code></p>
<dd>The remote uses the RC5 protocol.</p>
<dt><code>RC6</code></p>
<dd>The remote uses the RC6 protocol.</p>
<dt><code>RCMM</code></p>
<dd>The remote uses the RC-MM protocol (transmitting not supported).</p>
<dt><code>SHIFT_ENC</code></p>
<dd>Obsolete flag, now a synonym for RC5. The position of the pulse (before or after the space) determines whether the bit is a one or a zero.</p>
<dt><code>SPACE_ENC</code></p>
<dd>A one and a zero can be distinguished by the length of the spaces, used by the NEC protocol and others.</p>
<dt><code>REVERSE</code></p>
<dd>Reverses the bit order of the pre_data, the post_data and the codes (e.g., 0x123 becomes 0xC48). If this flag is present, the least significant bit is sent first.</p>
<dt><code>NO_HEAD_REP</code></p>
<dd>The header is not sent when a signal (the button is held down) is repeated even though there is no special repeat code.</p>
<dt><code>NO_FOOT_REP</code></p>
<dd>The foot is not sent when a signal is repeated (the button is held down) even though there is no special repeat code .</p>
<dt><code>CONST_LENGTH</code></p>
<dd>The total signal length is always constant. The gap length now represents the length of the entire signal, and the actual gap at the end of the signal is adjusted accordingly.</p>
<dt><code>RAW_CODES</code></p>
<dd>The codes are in raw format.</p>
<dt><code>REPEAT_HEADER</code></p>
<dd>Send the header when the signal is repeated even though the remote has a special repeat code.</dl>
<h2>Disclaimer</h2>
<p>LIRC was designed to collect IR data and save it in a private, compact, yet human readable format with the purpose of being able to re-transmit (or re-recognize) these signals. It was not designed with the goal of providing a well documented and tested configuration file format that could be used e.g., to generate arbitrary IR signals or to convert them to other formats. The configuration file should thus not be considered a public interface to LIRC. </p>
<p> This manpage should be understood with this in mind. It was authored by reading the code of LIRC, and does not constitute an authoritative specification of the behavior of LIRC and its configuration file. Also, some less commonly used flags and parameters are not documented.</p>
<h2>See Also</h2>
<dl>
<dt><a href="/docs/linux/man/8-lircd/">lircd</a>(8)</p>
<dd>
<dt><a href="/docs/linux/man/1-irrecord/">irrecord</a>(1)</p>
<dd>
<dt><a rel="nofollow" href="http://en.wikipedia.org/wiki/RC-5">http://en.wikipedia.org/wiki/RC-5</a></p>
<dd>
<dt><a rel="nofollow" href="http://www.sbprojects.com/knowledge/ir/">http://www.sbprojects.com/knowledge/ir/</a></p>
<dd>
