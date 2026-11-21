---

title: "loggen(1)"
name: "loggen"
section: "1"
letter: "l"
url: "/docs/linux/man/1-loggen/"
description: "loggen – Generate syslog messages at a specified rate"
---

<dl>
<dt> <code>loggen</code> [options]<code>target</code> [port]</dt></dl>
<dd>NOTE: The loggen application is distributed with the syslog-ng system logging application, and is usually part of the syslog-ng package. The latest version of the syslog-ng application is available at m[blue]<code>the official syslog-ng website</code>m[]<font SIZE="-2">[1]</font>. </dd>
<p> This manual page is only an abstract; for the complete documentation of syslog-ng, see m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> The <code>loggen</code> application is tool to test and stress-test your syslog server and the connection to the server. It can send syslog messages to the server at a specified rate, using a number of connection types and protocols, including TCP, UDP, and unix domain sockets. The messages can be generated automatically (repeating the <i>PADD</i>string over and over), or read from a file or the standard input. </p>
<p> When <code>loggen</code> finishes sending the messages, it displays the following statistics: </p>
<dl>
<dt>
</dt><dd> &bull; <i>average rate</i>: Average rate the messages were sent in messages/second.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; <i>count</i>: The total number of messages sent.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; <i>time</i>: The time required to send the messages in seconds.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; <i>average message size</i>: The average size of the sent messages in bytes.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; <i>bandwidth</i>: The average bandwidth used for sending the messages in kilobytes/second.</dd></dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;active-connections &lt;number-of-connections&gt;</code></p>
<dl>
<dt>
</dt><dd> Number of connections <code>loggen</code> will use to send messages to the destination. This option is usable only when using TCP or TLS connections to the destination. Default value: 1 </dd>
<p> The <code>loggen</code> utility waits until every connection is established before starting to to send messages. See also the <i>&#8211;idle-connections</i> option.</dl>
<p> <code>&#8211;csv</code> or <code>-C</code></p>
<dl>
<dt>
</dt><dd> Send the statistics of the sent messages to stdout as CSV. This can be used for plotting the message rate.</dd></dl>
<p> <code>&#8211;dgram</code> or <code>-D</code></p>
<dl>
<dt>
</dt><dd> Use datagram socket (UDP or unix-dgram) to send the messages to the target. Requires the <i>&#8211;inet</i> option as well.</dd></dl>
<p> <code>&#8211;dont-parse</code> or <code>-d</code></p>
<dl>
<dt>
</dt><dd> Do not parse the lines read from the input files, send them as received.</dd></dl>
<p> <code>&#8211;help</code> or <code>-h</code></p>
<dl>
<dt>
</dt><dd> Display a brief help message.</dd></dl>
<p> <code>&#8211;idle-connections &lt;number-of-connections&gt;</code></p>
<dl>
<dt>
</dt><dd> Number of idle connections <code>loggen</code> will establish to the destination. Note that <code>loggen</code> will not send any messages on idle connections, but the connection is kept open using keep-alive messages. This option is usable only when using TCP or TLS connections to the destination. See also the <i>&#8211;active-connections</i> option. Default value: 0</dd></dl>
<p> <code>&#8211;inet</code> or <code>-i</code></p>
<dl>
<dt>
</dt><dd> Use the TCP (by default) or UDP (when used together with the <i>&#8211;dgram</i> option) protocol to send the messages to the target.</dd></dl>
<p> <code>&#8211;interval &lt;seconds&gt;</code> or <code>-I &lt;seconds&gt;</code></p>
<dl>
<dt>
</dt><dd> The number of seconds <code>loggen</code> will run. Default value: 10 </dd>
<p> Note that when the <i>&#8211;interval</i> and <i>&#8211;number</i> are used together, <code>loggen</code> will send messages until the period set in <i>&#8211;interval</i> expires or the amount of messages set in <i>&#8211;number</i> is reached, whichever happens first.</dl>
<p> <code>&#8211;ipv6</code> or <code>-6</code></p>
<dl>
<dt>
</dt><dd> Specify the destination using its IPv6 address. Note that the destination must have a real IPv6 address.</dd></dl>
<p> <code>&#8211;loop-reading</code> or <code>-l</code></p>
<dl>
<dt>
</dt><dd> Read the file specified in <i>&#8211;read-file</i> option in loop: loggen will start reading from the beginning of the file when it reaches the end of the file.</dd></dl>
<p> <code>&#8211;number &lt;number-of-messages&gt;</code> or <code>-n &lt;number-of-messages&gt;</code></p>
<dl>
<dt>
</dt><dd> Number of messages to generate. </dd>
<p> Note that when the <i>&#8211;interval</i> and <i>&#8211;number</i> are used together, <code>loggen</code> will send messages until the period set in <i>&#8211;interval</i> expires or the amount of messages set in <i>&#8211;number</i> is reached, whichever happens first.</dl>
<p> <code>&#8211;no-framing</code> or <code>-F</code></p>
<dl>
<dt>
</dt><dd> Do not use the framing of the IETF-syslog protocol style, even if the <i>syslog-proto</i> option is set.</dd></dl>
<p> <code>&#8211;quiet</code> or <code>-Q</code></p>
<dl>
<dt>
</dt><dd> Output statistics only when the execution of <code>loggen</code> is finished. If not set, the statistics are displayed every second.</dd></dl>
<p> <code>&#8211;rate &lt;message/second&gt;</code> or <code>-r &lt;message/second&gt;</code></p>
<dl>
<dt>
</dt><dd> The number of messages generated per second for every active connection. Default value: 1000</dd></dl>
<p> <code>&#8211;read-file &lt;filename&gt;</code> or <code>-R &lt;filename&gt;</code></p>
<dl>
<dt>
</dt><dd> Read the messages from a file and send them to the target. See also the <i>&#8211;skip-tokens</i> option. </dd>
<p> Specify <i>&#8211;</i> as the input file to read messages from the standard input (stdio). Note that when reading messages from the standard input, <code>loggen</code> can only use a single thread. The <i>-R &#8211;</i> parameters must be placed at end of command, like: <code>loggen 127.0.0.1 1061 &#8211;read-file &#8211;</code></dl>
<p>&nbsp;<wbr>&nbsp;<wbr>Send the given sdata&nbsp;<wbr>(e.g.&nbsp;<wbr>&quot;[test name=\&quot;value\&quot;])&nbsp;<wbr>in case of syslog-proto<br />
&nbsp;<wbr>&nbsp;<wbr>.PP <code>&#8211;sdata &lt;data-to-send&gt;</code> or <code>-p &lt;data-to-send&gt;</code></p>
<dl>
<dt>
</dt><dd> Send the argument of the <i>&#8211;sdata</i> option as the SDATA part of IETF-syslog (RFC5424 formatted) messages. Use it together with the <i>&#8211;syslog-proto</i> option. For example: <i>&#8211;sdata &quot;[test name=\&quot;value\&quot;]</i></dd></dl>
<p> <code>&#8211;size &lt;message-size&gt;</code> or <code>-s &lt;message-size&gt;</code></p>
<dl>
<dt>
</dt><dd> The size of a syslog message in bytes. Default value: 256. Minimum value: 127 bytes, maximum value: 8192 bytes.</dd></dl>
<p> <code>&#8211;skip-tokens &lt;number&gt;</code></p>
<dl>
<dt>
</dt><dd> Skip the specified number of space-separated tokens (words) at the beginning of every line. For example, if the messages in the file look like <i>foo bar message</i>, <i>&#8211;skip-tokens 2</i> skips the <i>foo bar</i> part of the line, and sends only the <i>message</i> part. Works only when used together with the <i>&#8211;read-file</i> parameter. Default value: 3</dd></dl>
<p> <code>&#8211;stream</code> or <code>-S</code></p>
<dl>
<dt>
</dt><dd> Use a stream socket (TCP or unix-stream) to send the messages to the target.</dd></dl>
<p> <code>&#8211;syslog-proto</code> or <code>-P</code></p>
<dl>
<dt>
</dt><dd> Use the new IETF-syslog message format as specified in RFC5424. By default, loggen uses the legacy BSD-syslog message format (as described in RFC3164). See also the <i>&#8211;no-framing</i> option.</dd></dl>
<p> <code>&#8211;unix &lt;/path/to/socket&gt;</code> or <code>-x &lt;/path/to/socket&gt;</code></p>
<dl>
<dt>
</dt><dd> Use a UNIX domain socket to send the messages to the target.</dd></dl>
<p> <code>&#8211;use-ssl</code> or <code>-U</code></p>
<dl>
<dt>
</dt><dd> Use an SSL-encrypted channel to send the messages to the target. Note that it is not possible to check the certificate of the target, or to perform mutual authentication.</dd></dl>
<p> <code>&#8211;version</code> or <code>-V</code></p>
<dl>
<dt>
</dt><dd> Display version number of syslog-ng.</dd></dl>
<h2>EXAMPLES</h2>
<p> The following command generates 100 messages per second for ten minutes, and sends them to port 2010 of the localhost via TCP. Each message is 300 bytes long. <code>loggen &#8211;size 300 &#8211;rate 100 &#8211;interval 600 127.0.0.1 2010</code>.PP The following command is similar to the one above, but uses the UDP protocol. <code>loggen &#8211;inet &#8211;dgram &#8211;size 300 &#8211;rate 100 &#8211;interval 600 127.0.0.1 2010</code>.PP Send a single message on TCP6 to the <i>::1</i> IPv6 address, port <i>1061</i>: <code>loggen &#8211;ipv6 &#8211;number 1 ::1 1061</code>.PP Send a single message on UDP6 to the <i>::1</i> IPv6 address, port <i>1061</i>: <code>loggen &#8211;ipv6 &#8211;dgram &#8211;number 1 ::1 1061</code>.PP Send a single message using a unix domain-socket: <code>loggen &#8211;unix &#8211;stream &#8211;number 1 &lt;/path/to/socket&gt;</code>.PP Read messages from the standard input (stdio) and send them to the localhost: <code>loggen 127.0.0.1 1061 &#8211;read-file &#8211;</code>.SH &quot;FILES&quot; </p>
<p> /home/algernon/install/syslog-ng/3.5/bin/loggen</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-syslog-ng-conf/">syslog-ng.conf</a></code>(5) </p>
<p> m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[2]</font> </p>
<p> If you experience any problems or need help with loggen or syslog-ng, visit the m[blue]<code>syslog-ng mailing list</code>m[]<font SIZE="-2">[3]</font> </p>
<p> m[blue]<code>The syslog-ng OSE 3.3 Administrator Guide</code>m[]<font SIZE="-2">[2]</font> </p>
<p> If you experience any problems or need help with syslog-ng, visit m[blue]<code>visit the syslog-ng wiki</code>m[]<font SIZE="-2">[4]</font> or the m[blue]<code>syslog-ng mailing list</code>m[]<font SIZE="-2">[3]</font>. </p>
<p> For news and notifications about of syslog-ng, visit the m[blue]<code>syslog-ng Insider Blog</code>m[]<font SIZE="-2">[5]</font>.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by the BalaBit Documentation Team &lt;documentation [at] balabit.com&gt;.</p>
<h2>COPYRIGHT</h2>
<h3></h3>
<p> The authors grant permission to copy, distribute and/or modify this manual page under the terms of the GNU General Public License Version 2 or newer (GPL v2+).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> the official syslog-ng website</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.balabit.com/network-security/syslog-ng/">http://www.balabit.com/network-security/syslog-ng/</a></dd></dl>
<dt> 2.</dt>
<dd> The syslog-ng Administrator Guide</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.balabit.com/support/documentation/">http://www.balabit.com/support/documentation/</a></dd></dl>
<dt> 3.</dt>
<dd> syslog-ng mailing list</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://lists.balabit.hu/mailman/listinfo/syslog-ng">https://lists.balabit.hu/mailman/listinfo/syslog-ng</a></dd></dl>
<dt> 4.</dt>
<dd> visit the syslog-ng wiki</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.balabit.com/wiki/syslog-ng-faq">http://www.balabit.com/wiki/syslog-ng-faq</a></dd></dl>
<dt> 5.</dt>
<dd> <code>syslog-ng Insider Blog</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://insider.blogs.balabit.com">http://insider.blogs.balabit.com</a></dd></dl>
</dl>
