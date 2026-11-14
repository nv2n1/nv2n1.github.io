---
title: "etterlog(8)"
name: "etterlog"
section: "8"
letter: "e"
url: "/docs/linux/man/8-etterlog/"
description: "etterlog NG-0.7.3 – Log analyzer for ettercap log files"
---

<p><code>etterlog NG-0.7.3 &#8211; Log analyzer for ettercap log files</code> </p>
<h2>Synopsis</h2>
<p><code>etterlog</code> [<i>OPTIONS</i>] <i>FILE</i> </p>
<h2>Description</h2>
<p>Etterlog is the log analyzer for logfiles created by ettercap. It can handle both compressed (created with -Lc) or uncompressed logfiles. With this tool you can manipulate binary files as you like and you can print data in different ways all the times you want (in contrast with the previous logging system which was used to dump in a single static manner).<br />
 You will be able to dump traffic from only one connection of your choice, from only one or more hosts, print data in hex, ascii, binary etc&#8230; TIP: All unuseful messages are printed to stderr, so you can save the output from etterlog with the following command:</p>
<dl>
<dt><i>etterlog [options] logfile &gt; outfile</i></p>
<dd>Thus you can dump for example a binary file from an ftp connection if you print the data in binary mode, without headers and selecting only the ftp server as the source of the communication.</p>
<dt><code>GENERAL OPTIONS</code></p>
<dd>
<dt><code>-a</code>, <code>&#8211;analyze</code></p>
<dd>Analyze a log file and display some interesting statistics.</p>
<dt><code>-c</code>, <code>&#8211;connections</code></p>
<dd>Parse the log file and print a table of unique connections (port to port). This option can be used only on LOG_PACKET logfiles. On LOG_INFO logfiles it is useless. TIP: you can search for a particular host by using the following command: etterlog -c logfile.ecp | grep 10.0.0.1</p>
<dt><code>-f</code>, <code>&#8211;filter &lt;TARGET&gt;</code></p>
<dd>Print only packets coming from or going to TARGET. The TARGET specification is the same as in ettercap.<br />
 <i>TARGET</i> is in the form <i>MAC/IPs/PORTs</i>. Omitting one or more of its parts will be equivalent to set them to ANY. If the log type is LOG_INFO the target is used to display hosts matching the mac, ip and having the specified port(s) open. For example the target //80 will display only information about hosts with a running web server.</p>
<dt><code>-r</code>, <code>&#8211;reverse</code></p>
<dd>Reverse the matching in the TARGET selection. It means not(TARGET). All but the selected TARGET.</p>
<dt><code>-t</code>, <code>&#8211;proto &lt;PROTO&gt;</code></p>
<dd>Sniff only PROTO packets (default is TCP + UDP). This option is only useful in &quot;simple&quot; mode. If you start ettercap in interactive mode both TCP and UDP are sniffed.<br />
 PROTO can be &quot;tcp&quot;, &quot;udp&quot; or &quot;all&quot; for both.</p>
<dt><code>-F</code>, <code>&#8211;filcon &lt;CONNECTION&gt;</code></p>
<dd>Print packets belonging only to this CONNECTION.<br />
 CONNECTION is in the form PROTO:SOURCE:DEST. SOURCE and DEST are in the form IP:PORT. example: etterlog -F TCP:10.0.0.23:3318:198.182.196.56:80</p>
<dt><code>-s</code>, <code>&#8211;only-source</code></p>
<dd>Display only packets that are sent by the source of the selected CONNECTION. This option makes sense only in conjunction with the -F option. TIP: if you want to save a file transferred in an HTTP or FTP connection, you can use the following command: etterlog -B -s -n -F TCP:10.0.0.1:20:10.0.0.2:35426 logfile.ecp &gt; example.tar.gz<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-d</code>, <code>&#8211;only-dest</code></p>
<dd>Same as &#8211;only-source but it filters on the destination host.</p>
<dt><code>-n</code>, <code>&#8211;no-headers</code></p>
<dd>Do not print the header of each packet. This option is useful if you want to save a file in binary format (-B option). Without the headers you can redirect the output to a file and you will get the original stream. NOTE: the time stamp in the header is in the form: Thu Mar 27 23:03:31 2003 [169396], the value in the square brackets is expressed in microseconds</p>
<dt><code>-m</code>, <code>&#8211;show-mac</code></p>
<dd>In the headers show also the mac addresses corresponding to the ip addresses.</p>
<dt><code>-k</code>, <code>&#8211;color</code></p>
<dd>If used in conjunction with -F it displays the source and dest of the connection using different colors. If used with a LOG_INFO file it prints LAN hosts in green, REMOTE hosts in blue and GATEWAYS in red.</p>
<dt><code>-l</code>, <code>&#8211;only-local</code></p>
<dd>Used displaying an INFO file, it displays information only about local hosts.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-L</code>, <code>&#8211;only-remote</code></p>
<dd>Used displaying an INFO file, it displays information only about remote hosts.</p>
<dt><code>SEARCH OPTIONS</code></p>
<dd>
<dt><code>-e</code>, <code>&#8211;regex &lt;REGEX&gt;</code></p>
<dd>Display only packets matching the regex &lt;REGEX&gt;.<br />
 If this option is used agains a LOG_PACKET logfile, the regex is executed on the payload of the packet. If the type is LOG_INFO, the regex is executed on all the fields of the host profile (OS, banners, service and ethernet adapter).<br />
 NOTE: the regex is compiled with the REG_ICASE flag (case insensitive).</p>
<dt><code>-u</code>, <code>&#8211;user &lt;USER&gt;</code></p>
<dd>Display information about this user. The search is performed over all the user/pass couples collected across all hosts.</p>
<dt><code>-p</code>, <code>&#8211;passwords</code></p>
<dd>Print only the collected account information for each host. This prevents the huge profile output. It can be used in conjunction with the -u option to filter the users. An asterisk &#8216;*&#8217; used in front of an account represents a failed login attempt.</p>
<dt><code>-i</code>, <code>&#8211;show-client</code></p>
<dd>Show the client ip address when displaying the collected users and passwords. It may be useful when ACLs are in place.</p>
<dt><code>-I</code>, <code>&#8211;client &lt;IP&gt;</code></p>
<dd>Show passwords only coming from a specific &lt;IP&gt;. This is useful to view all the usernames and passwords of a client.</p>
<dt><code>EDITING OPTIONS</code></p>
<dd>
<dt><code>-C</code>, <code>&#8211;concat</code></p>
<dd>Use this option to concatenate two (or more) files into one single file. This is useful if you have collected ettercap log files from multiple sources and want to have an unified report. The output file must be specified with the -o option and the input files are listed as normal arguments. example:<br />
 etterlog -C -o outfile input1 input2 input3</p>
<dt><code>-o</code>, <code>&#8211;outfile &lt;FILE&gt;</code></p>
<dd>specifies the output file for a concatenation.</p>
<dt><code>VISUALIZATION METHOD</code></p>
<dd>&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-B</code>, <code>&#8211;binary</code></p>
<dd>Print data as they are, in binary form. Useful to dump binary data to a file (as described above).</p>
<dt><code>-X</code>, <code>&#8211;hex</code></p>
<dd>Print the packets in hex format. example: the string &quot;HTTP/1.1 304 Not Modified&quot; becomes: 0000: 4854 5450 2f31 2e31 2033 3034 204e 6f74 HTTP/1.1 304 Not<br />
 0010: 204d 6f64 6966 6965 64 Modified<br />
&nbsp;<wbr></p>
<dt><code>-A</code>, <code>&#8211;ascii</code></p>
<dd>Print only &quot;printable&quot; characters, the others are displayed as dots &#8216;.&#8217;</p>
<dt><code>-T</code>, <code>&#8211;text</code></p>
<dd>Print only the &quot;printable&quot; characters and skip the others.</p>
<dt><code>-E</code>, <code>&#8211;ebcdic</code></p>
<dd>Convert an EBCDIC text to ASCII.</p>
<dt><code>-H</code>, <code>&#8211;html</code></p>
<dd>Strip all html tags from the text. A tag is every string between &#8216;&lt;&#8216; and &#8216;&gt;&#8217;. example: &lt;title&gt;This is the title&lt;/title&gt;, but the following &lt;string&gt; will not be displayed. This is the title, but the following will not be displayed.</p>
<dt><code>-U</code>, <code>&#8211;utf8 &lt;encoding&gt;</code></p>
<dd>Print the packets in UTF-8 format. The &lt;encoding&gt; parameter specifies the encoding to be used while performing the conversion. Use the `iconv &#8211;list` command to obtain a list of all supported encodings.</p>
<dt><code>-Z</code>, <code>&#8211;zero</code></p>
<dd>Print always the void string. i.e. print only header information and no packet content will be printed.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-x</code>, <code>&#8211;xml</code></p>
<dd>Print the host information in xml form, so you can parse it with your favourite program. The DTD associated with the xml output is in share/etterlog.dtd<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>STANDARD OPTIONS</code></p>
<dd>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print the version and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print the help screen with a short summary of the available options. </p>
<h2>Examples</h2>
<p>Here are some examples of using etterlog.</p>
<dl>
<dt><code>etterlog -k -l dump.eci</code></p>
<dd>Displays information about local hosts in different colors.</p>
<dt><code>etterlog -X dump.ecp</code></p>
<dd>Prints packets in HEX mode with full headers.</p>
<dt><code>etterlog -c dump.ecp</code></p>
<dd>Displays the list of connections logged in the file.</p>
<dt><code>etterlog -Akn -F TCP:10.0.0.1:13423:213.203.143.52:6666 dump.ecp</code></p>
<dd>Displays the IRC traffic made by 10.0.0.1 in ASCII mode, without headers information and in colored mode.</p>
<dt><code>etterlog -H -t tcp -f //80 dump.ecp</code></p>
<dd>Dumps all HTTP traffic and strips html tags.</p>
<dt><code>etterlog -Z -r -f /10.0.0.2/22 dump.ecp</code></p>
<dd>Displays only the headers of all connections except ssh on host 10.0.0.2</p>
<dt><code>etterlog -A -e &#8216;user&#8217; -f //110 dump.ecp</code></p>
<dd>Displays only POP packets containing the &#8216;user&#8217; regexp (case insensitive).</p>
<dt><code>etterlog -u root dump.eci</code></p>
<dd>Displays information about all the accounts of the user &#8216;root&#8217;.</p>
<dt><code>etterlog -e Apache dump.eci</code></p>
<dd>Displays information about all the hosts running &#8216;Apache&#8217;.</p>
<dt><code>etterlog -e Linux dump.eci</code></p>
<dd>Displays information about all the hosts with the &#8216;Linux&#8217; operating system.</p>
<dt><code>etterlog -t tcp -f //110 dump.eci</code></p>
<dd>Displays information about all the hosts with the tcp port 110 open.</p>
<dt><code>etterlog -t udp dump.eci</code></p>
<dd>Displays information about all the hosts with at least one UDP port open.</p>
<dt><code>etterlog -B -s -n -F TCP:10.0.0.1:20:10.0.0.2:35426 logfile.ecp &gt; example.tar.gz</code></p>
<dd>Dumps in binary form the data sent by 10.0.0.1 over the data port of FTP. Since the headers are omitted, you will get the file as it was. </p>
<h2>Authors</h2>
<p>Alberto Ornaghi (ALoR) &lt;alor [at] users.sf.net&gt;<br />
 Marco Valleri (NaGA) &lt;naga [at] antifork.org&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ettercap/">ettercap</a>(8)</i> <i><a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8)</i> <i><a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5)</i> <i><a href="/docs/linux/man/8-ettercap_curses/">ettercap_curses</a>(8)</i> <i><a href="/docs/linux/man/8-ettercap_plugins/">ettercap_plugins</a>(8)</i> </p>
