---
title: "tcpick(8)"
name: "tcpick"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpick/"
description: "tcpick – tcp stream sniffer and connection tracker"
---

<p>tcpick &#8211; tcp stream sniffer and connection tracker</p>
<h2>Synopsis</h2>
<p><code>tcpick </code> [<code> -a </code>] [<code> -n </code>] [<code> -C </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -e </code><i>count</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -i </code><i>interface </i>|<code> -r </code><i> file </i>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -X </code><i>timeout</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -D </code> ] [<code> -F1 </code>|<code> -F2 </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -yH </code>|<code> -yP </code>|<code> -yR </code>|<code> -yU </code>|<code> -yx </code>|<code> -yX </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -bH </code>|<code> -bP </code>|<code> -bR </code>|<code> -bU </code>|<code> -bx </code>|<code> -bX </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -wH[ub] </code>|<code> -wP[ub] </code>|<code> -wR[ub] </code>|<code> -wU[ub] </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -v </code> [<i> verbosity </i>]] [<code> -S </code>] [<code> -h </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> &#8211;separator </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -T </code>|<code> -Tf </code> [<i> number </i>]] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -E </code>|<code> -Ef </code> [<i> number </i>]] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> -Pc </code> | <code> -Ps </code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<i> &quot;filter&quot; </i>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code> &#8211;help </code>] [<code> &#8211;version </code>] </p>
<h2>Description</h2>
<p><code>tcpick</code> is a textmode sniffer libpcap-based that can track tcp streams and saves the data captured in different files, each for every connection, or displays them in the terminal in different formats (hexdump, printable charachters, raw&#8230;) Useful for picking files in a passive way. It is useful to keep track of what users of a network are doing, and is usable with textmode tools like grep, sed, awk. Happy data hunting :-) </p>
<h2>Base Options</h2>
<dl>
<dt><code>-i &#8211;interface </code><i>interface</i></p>
<dd>listen on selected interface, (i.e. <i>ppp0</i> or <i>eth0</i>). If option <code>-i</code> is omitted, tcpick is able to select the first open interface (usually a ethernet card).</p>
<dt><code>-r &#8211;readfile</code></p>
<dd>reads raw packets from a file written with <code>tcpdump -w</code> instead of using a network device.</p>
<dt><code> &quot;filter&quot; </code></p>
<dd>This is the filter for the capturer engine. You can set it in the same way of setting the <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)</code> filter. Read <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1) manpage for other explanations.</p>
<dt><code>-a</code></p>
<dd>Displays host names instead of ip addresses. Warning: for every new ip grabbed a dns query will be generated! Use it carefully on high-traffic network devices!</p>
<dt><code>-C &#8211;colors</code></p>
<dd>Uses terminal colors: very nice! It should help you to read the output of tcpick</p>
<dt><code>-D </code><i>number</i> <code>&#8211;dirs</code> <i>number</i></p>
<dd>Create directories to store sniffed sessions. When a directory contains <i>number</i> sessions, a new one will be created.</p>
<dt><code>-e </code><i>count</i></p>
<dd>Exits when <i>count</i> packets have been sniffed</p>
<dt><code>-E </code><i>number</i></p>
<dd>Exit when <i>number</i> sniffed connections are detected as &quot;CLOSED&quot;</p>
<dt><code>-Ef </code><i>number</i></p>
<dd>Exit when <code>the first</code> <i>number</i> connections are detected as &quot;CLOSED&quot;</p>
<dt><code>-F1 -F2 &#8211;filenaming 1|2</code></p>
<dd>Choose the filenaming system.<br />
 <code> -F1 </code>: tcpick_<code>clientip</code>_<code>serverip</code>.<code>side</code>.dat<br />
 (side means <code>clnt</code>, <code>serv</code> or <code>both</code>)<br />
 <code> -F2 </code>: tcpick_<code>connectionnumber</code>_<code>clientip</code>_<code>serverip</code>.<code>side</code>.dat</p>
<dt><code>-h</code></p>
<dd>Shows source and destination ip and port; shows tcp flags as letters.</p>
<dt><code>&#8211;help</code></p>
<dd>Displays a short help summary</p>
<dt><code>-p</code></p>
<dd><i>Don&#8217;t</i> put the network interface in promiscuous mode. Note that the interface might be in promiscuous mode for some other reason.</p>
<dt><code>-S</code></p>
<dd>Suppresses the &quot;status of the connection&quot; banner.</p>
<dt><code>&#8211;separator</code></p>
<dd>Add a separator for the payloads displayed.</p>
<dt><code>-t</code></p>
<dd>Adds timestamp in <code>hour:minutes:seconds:microseconds</code> format</p>
<dt><code>-td</code></p>
<dd>Like <code>-tFP with date timestamp in day-month-year</code> format </p>
<dt><code>-T </code><i>number</i></p>
<dd>Track <i>number</i> connections. It could be very useful on a high-traffic network device. If <i>number</i> is not specified, it will be set to <code>1</code>.</p>
<dt><code>-Tf </code><i>number</i></p>
<dd>Track <code>only the first</code> <i>number</i> connections; the following will be discarded. If <i>number</i> is not specified, it will be set to <code>1</code>.</p>
<dt><code>-v </code><i>verbosity</i></p>
<dd>Quite unuseful, yet. Set verbosity level. Actually there are not really many extra messages to display, this means it is enabled by default (<code>-v1</code>). Set verbosity level to <code>0</code> to suppress extra messages (<code>-v0</code>) except error messages. Set verbosity level to <code>5</code> to display debug messages (<code>-v5</code>). There are not other verbosity levels.</p>
<dt><code>-X </code><i>timeout</i></p>
<dd>Connections are considered <code>EXPIRED</code> when there is no traffic for at least <i>timeout</i> seconds. Default is 600.</p>
<dt><code>&#8211;version</code></p>
<dd>Displays the tcpick version </p>
</dl>
<h2>Display The Data In The Tcp Packets</h2>
<p>These options are prefixed by <code>-y</code> and are useful to display in various ways the content of the packet sniffed (the data, called payload), once it arrives at the listening interface. In that way the tcp duplicates will be not discarded and the packets will not be reordered, but displayed &quot;as is&quot;. If you want a fully acknowledged stream, see the <code>-w</code> and <code>-b</code> set of options.</p>
<dl>
<dt><code>-yH</code></p>
<dd>View data in hexadecimal-spaced mode (for the hexdump see <code>-yx</code> and <code>-yX</code> options.</p>
<dt><code>-yP</code></p>
<dd>Shows data contained in the tcp packets. Non-printable charachters are transformed in dots: &quot;<code>.</code>&quot;. Newline character is preserved. This is the best way, in my opinion to show data like HTTP requests, IRC communication, SMTP stuff and so on.</p>
<dt><code>-yR</code></p>
<dd>Displays all kind of charachters, printable and non printable. If something binary is transmitted, the effect will probably be like watching with &quot;<code>cat</code>&quot; at a gzipped file.</p>
<dt><code>-yx</code></p>
<dd>Shows all data after the header in hexadecimal dump of 16 bytes per line.</p>
<dt><code>-yX</code></p>
<dd>Shows all data after the header in hexadecimal and ascii dump with 16 bytes per line.</p>
<dt><code>-yU</code></p>
<dd>Shows all data after the header, but <code>U</code>nprintable charachters are displayed as hexadecimal values between a &quot;&lt;&quot; and a &quot;&gt;&quot; symbol. </p>
</dl>
<h2>Rebuild And Write The Tcp Stream To File</h2>
<p>The prefix for these options is <code>-w</code>. The TCP stream that has been sniffed with these options will be written to file named:<br />
 <i>client_&lt;ip_client&gt;_&lt;ip_server&gt;_&lt;port_server&gt;.tcpick</i> and<br />
 <i>server_&lt;ip_client&gt;_&lt;ip_server&gt;_&lt;port_server&gt;.tcpick</i><br />
 With the <code>u</code> flag of the <code>-w</code> option (i.e. <code>-wRu</code>) both client and server data will be written to a unique file named in that way:<br />
 <i>&lt;ip_client&gt;_&lt;ip_server&gt;_&lt;port_server&gt;.tcpick</i><br />
 If you use the additional flag <code>b</code> of the <code>-w</code> option (i.e. <code>-wPub</code>), in the file will be written this banner: </p>
<p> <code>[client|server] offset before:offset after (lenght of rebuilded segment)</code> </p>
<p> to distinguish between client and server data.<br />
 The flow is rebuilded, reordered and the duplicates are dropped. In that way it is possible to sniff entire files transmitted via ftp without data corruption (you can see this with md5sum). If no argument is given to <code>-w</code> the data will be written like <code>-wR</code> You can decide to write only client or server data by setting the flag<br />
&nbsp;<wbr><code>C</code>&nbsp;<wbr>(output only client data)&nbsp;<wbr>and&nbsp;<wbr><code>S</code>&nbsp;<wbr>(output only server data) to the <code>-w</code> set. </p>
<dl>
<dt><code>-wR</code></p>
<dd>This is the preferred option: data will be written without any changes. Useful for sniffing binary or compressed files.<br />
 (<code>-wRC</code> only the client, <code>-wRS</code> only the server)</p>
<dt><code>-wP</code></p>
<dd>Unprintable charachters are written like dots.<br />
 (<code>-wPC</code> only the client, <code>-wPS</code> only the server)</p>
<dt><code>-wU</code></p>
<dd><code>U</code>nprintable charachters are displayed as hexadecimal values between a &quot;&lt;&quot; and a &quot;&gt;&quot; symbol.<br />
 (<code>-wPC</code> only the client, <code>-wPS</code> only the server)</p>
<dt><code>-wH</code></p>
<dd>The flow is written in hexadecimal-spaced mode.<br />
 (<code>-wHC</code> only the client, <code>-wHS</code> only the server) </p>
</dl>
<h2>Display The Rebuilded Tcp Stream</h2>
<p>The prefix for these options is <code>-b</code>. This set of options is very useful if you want to redirect the sniffed flow to anoter program with a pipe, and there should be no data corruption. Of course the most useful is <code>-bR</code> to show the data as they are (raw). A very useful feature is the flag <code>C</code> (output only client data) and <code>S</code> (output only server data). I.e.: <code>-bRC</code> will display only the data from the client in raw mode; in that way you can put them in a file with a pipe redirection. </p>
<p> The sub-options are quite the same of the <code>-y</code> set, so you have:</p>
<dl>
<dt><code> -bH </code> hex-spaced</p>
<dd>(<code>-bHC</code> only the client, <code>-bHS</code> only the server)</p>
<dt><code> -bP </code> unprintable displayed as dots</p>
<dd>(<code>-bPC</code> only the client, <code>-bPS</code> only the server)</p>
<dt><code> -bR </code> raw mode</p>
<dd>(<code>-bRC</code> only the client, <code>-bRS</code> only the server)</p>
<dt><code> -bU </code> unprintable as &lt;hex&gt;.</p>
<dd>(<code>-bUC</code> only the client, <code>-bUS</code> only the server)</p>
<dt><code> -bx </code> hexdump</p>
<dd>(<code>-bxC</code> only the client, <code>-bxS</code> only the server)</p>
<dt><code> -bU </code> hexdump + ascii</p>
<dd>(<code>-bXC</code> only the client, <code>-bXS</code> only the server)</p>
<dt><code> -PC &#8211;pipe client </code></p>
<dd>This is an alias for <code>-bRC -S -v0 -Tf1 -Ef1</code>. With this option you are able to track only the first connection (<code>-T1</code>) matched by tcpick and data are displayed as raw. Only data from the client are put on stdout. All messages and banners are suppressed, except error messages (<code>-S -v0</code>), so this option is particulary useful to download an entire fully rebuilded and acknowledged connection.</p>
<dt><code> -PS &#8211;pipe server </code></p>
<dd>This is an alias for <code>-bRS -S -v0 -Tf1 -Ef1</code>. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt>how to display the connection status:</p>
<dd><code> # tcpick -i eth0 -C</code></p>
<dt>display the payload and packet headers:</p>
<dd><code> # tcpick -i eth0 -C -yP -h -a</code></p>
<dt>display client data only of the first smtp connection:</p>
<dd><code> # tcpick -i eth0 -C -bCU -T1 &quot;port 25&quot;</code></p>
<dt>download a file passively:</p>
<dd><code> # tcpick -i eth0 -wR &quot;port ftp-data&quot;</code></p>
<dt>log http data in unique files (client and server mixed together):</p>
<dd><code> # tcpick -i eth0 &quot;port 80&quot; -wRub</code></p>
<dt>redirect the first connection to a software:</p>
<dd><code> # tcpick -i eth0 &#8211;pipe client &quot;port 80&quot; | gzip &gt; http_response.gz</code><br />
 <code> # tcpick -i eth0 &#8211;pipe server &quot;port 25&quot; | nc foobar.net 25</code> </p>
<h2>Mailing-List</h2>
<p>Address: <i>&lt;tcpick-project[a]lists.sourceforge.net&gt;</i><br />
 Archive: <i><a rel="nofollow" href="http://sourceforge.net/mailarchive/forum.php?forum=tcpick-project">http://sourceforge.net/mailarchive/forum.php?forum=tcpick-project</a></i><br />
 Subscribe: <i><a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/tcpick-project">http://lists.sourceforge.net/lists/listinfo/tcpick-project</a></i><br />
 If you have new ideas, patches, feature requests or simply need help, don&#8217;t wait! I will be grateful if you send a message to the mailing list (even if you want to say what you liked most on tcpick).</p>
<h2>Tcpick Website</h2>
<p>The tcpick website is at <i><a rel="nofollow" href="http://tcpick.sf.net">http://tcpick.sf.net</a></i>.<br />
 You can find the project page here: <i><a rel="nofollow" href="http://sourceforge.net/projects/tcpick">http://sourceforge.net/projects/tcpick</a></i> kindly hosted by the sourceforge team.</p>
<h2>Authors</h2>
<p>Please check <code>AUTHORS</code> file.</p>
<h2>Bugs</h2>
<p>Tcpick is an experimental software, and maybe some bugs are described in the <code>KNOWN-BUGS</code> file.<br />
 On some versions of MacOSX Segmentation Fault happens and connections aren&#8217;t tracked properly.<br />
 If you find any other bug, please write to the tcpick mailing list. </p>
<h2>See Also</h2>
<p>Other nice packet/data sniffers:<br />
 tcpdump, ngrep, tcptrack, ettercap, ethereal, snort </p>
<h2>License</h2>
<p>This program is <code>free software</code>; you can redistribute it and/or modify it under the terms of the <code>GNU General Public License</code> as published by the Free Software Foundation; either version 2 of the License, or (at you option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <code> WITHOUT ANY WARRANTY</code>; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111, USA.</p>
