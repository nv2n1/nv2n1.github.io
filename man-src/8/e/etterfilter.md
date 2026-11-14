---
title: "etterfilter(8)"
name: "etterfilter"
section: "8"
letter: "e"
url: "/docs/linux/man/8-etterfilter/"
description: "etterfilter NG-0.7.3 – Filter compiler for ettercap content filtering engine"
---

<p><code>etterfilter NG-0.7.3 &#8211; Filter compiler for ettercap content filtering engine</code> </p>
<h2>Synopsis</h2>
<p><code>etterfilter</code> [<i>OPTIONS</i>] <i>FILE</i> </p>
<h2>Description</h2>
<p>The etterfilter utility is used to compile source filter files into binary filter files that can be interpreted by the JIT interpreter in the <a href="/docs/linux/man/8-ettercap/">ettercap</a>(8) filter engine. You have to compile your filter scripts in order to use them in ettercap. All syntax/parse errors will be checked at compile time, so you will be sure to produce a correct binary filter for ettercap.</p>
<dl>
<dt><code>GENERAL OPTIONS</code></p>
<dd>
<dt><code>-o</code>, <code>&#8211;output &lt;FILE&gt;</code></p>
<dd>you can specify the output file for a source filter file. By default the output is filter.ef.</p>
<dt><code>-t</code>, <code>&#8211;test &lt;FILE&gt;</code></p>
<dd>you can analyze a compiled filter file with this option. etterfilter will print in a human readable form all the instructions contained in it. It is a sort of &quot;disassembler&quot; for binary filter files.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>prints some debug messages during the compilation. Use it more than once to increase the debug level ( etterfilter -ddd &#8230; ).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-w</code>, <code>&#8211;suppress-warnings</code></p>
<dd>Don&#8217;t exit on warnings. With this option the compiler will compile the script even if it contains warnings.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>STANDARD OPTIONS</code></p>
<dd>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print the version and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>prints the help screen with a short summary of the available options.</p>
<dt><code>SCRIPTS SYNTAX</code></p>
<dd>A script is a compound of instructions. It is executed sequentially and you can make branches with the &#8216;if&#8217; statements. &#8216;if&#8217; and &#8216;if/else&#8217; statements are the only supported. No loops are implemented. The syntax is almost like C code except that you have to put &#8216;if&#8217; blocks into graph parentheses &#8216;{&#8216; &#8216;}&#8217;, even if they contain only one instruction. NOTE: you have to put a space between the &#8216;if&#8217; and the &#8216;(&#8216;. You must not put the space between the function name and the &#8216;(&#8216;.  The conditions for an &#8216;if&#8217; statement can be either functions or comparisons. Two or more conditions can be linked together with logical operators like OR &#8216;||&#8217; and AND &#8216;&amp;&amp;&#8217;. </p>
<pre><code>Example:

ip.ttl += 5;
</code></pre>
<p> Pay attention to the operator precedence. You cannot use parentheses to group conditions, so be careful with the order. An AND at the beginning of a conditions block will exclude all the other tests if it is evaluated as false. The parsing is left-to-right, when an operator is found: if it is an AND and the previous condition is false, all the statement is evaluated as false; if it is an OR the parsing goes on even if the condition is false.  the former condition will match all udp or http traffic. The latter is wrong, because if the packet is not tcp, the whole condition block will be evaluated as false. If you want to make complex conditions, the best way is to split them into nested &#8216;if&#8217; blocks. Every instruction in a block must end with a semicolon &#8216;;&#8217;. Comparisons are implemented with the &#8216;==&#8217; operator and can be used to compare numbers, strings or ip addresses. An ip address MUST be enclosed within two single quotes (eg. &#8216;192.168.0.7&#8217;). You can also use the &#8216;less than&#8217; (&#8216;&lt;&#8216;), &#8216;greater than&#8217; (&#8216;&gt;&#8217;), &#8216;less or equal&#8217; (&#8216;&lt;=&#8217;) and &#8216;greater or equal&#8217; (&#8216;&gt;=&#8217;) operators. The lvalue of a comparison must be an offset (see later) Example:</p>
<p>ip.ttl += 5;<br />
 Assignments are implemented with the &#8216;=&#8217; operator and the lvalue can be an offset (see later). The rvalue can be a string, an integer or a hexadecimal value.  You can also use the &#8216;inc&#8217; and &#8216;dec&#8217; operations on the packet fields. The operators used are &#8216;+=&#8217; and &#8216;-=&#8217;. The rvalue can be an integer or a hexadecimal value. </p>
<pre><code>Example:

ip.ttl += 5;
</code></pre>
<dt><code>OFFSET DEFINITION</code></p>
<dd>An offset is identified by a virtual pointer. In short words, an offset is a pointer to the packet buffer. The virtual pointer is a tuple &lt;L, O, S&gt;, where L is the iso/osi level, O is the offset in that level and S is the size of the virtual pointer. You can make algebraic operations on a virtual pointer and the result is still an offset. Specifying &#8216;vp + n&#8217; will result in a new virtual pointer &lt;L, O+n, S&gt;. And this is perfectly legal, we have changed the internal offset of that level. Virtual pointers are in the form &#8216;name.field.subfield&#8217;. For example &#8216;ip.ttl&#8217; is the virtual pointer for the Time To Live field in the IP header of a packet. It will be translated as &lt;L=3, O=9, S=1&gt;. Indeed it is the 9th byte of level 3 and its size is 1 byte. &#8216;ip.ttl + 1&#8217; is the same as &#8216;ip.proto&#8217; since the 10th byte of the IP header is the protocol encapsulated in the IP packet. The list of all supported virtual pointers is in the file etterfilter.tbl. You can add your own virtual pointers by adding a new table or modifying the existing ones. Refer to the comments at the beginning of the file for the syntax of etterfilter.tbl file.</p>
<dt><code>SCRIPTS FUNCTIONS</code></p>
<dd>
<dt><code>search(</code><i>where</i>, <i>what</i>)</p>
<dd>this function searches the string &#8216;what&#8217; in the buffer &#8216;where&#8217;. The buffer can be either DATA.data or DECODED.data. The former is the payload at layer DATA (ontop TCP or UDP) as it is transmitted on the wire, the latter is the payload decoded/decrypted by dissectors.<br />
 So, if you want to search in an SSH connection, it is better to use &#8216;DECODED.data&#8217; since &#8216;data&#8217; will be encrypted.<br />
 The string &#8216;what&#8217; can be binary. You have to escape it. example:<br />
 search(DATA.data, &quot;ABC&quot;)</p>
<dt><code>regex(</code><i>where</i>, <i>regex</i>)</p>
<dd>this function will return true if the &#8216;regex&#8217; has matched the buffer &#8216;where&#8217;. The considerations about &#8216;DECODED.data&#8217; and &#8216;DATA.data&#8217; mentioned for the function &#8216;search&#8217; are the same for the regex function. NOTE: regex can be used only against a string buffer. example:<br />
 regex(DECODED.data, &quot;.*login.*&quot;)</p>
<dt><code>pcre_regex(</code><i>where</i>, <i>pcre_regex</i> &#8230; )</p>
<dd>this function will evaluate a perl compatible regular expression. You can match against both DATA and DECODED, but if your expression modifies the buffer, it makes sense to operate only on DATA. The function accepts 2 or 3 parameters depending on the operation you want. The two parameter form is used only to match a pattern. The three parameter form means that you want to make a substitution. In both cases, the second parameter is the search string.<br />
 You can use $n in the replacement string. These placeholders are referred to the groups created in the search string. (e.g. pcre_regex(DATA.data, &quot;^var1=([:digit:]*)&amp;var2=([:digit:]*)&quot;, &quot;var1=$2&amp;var2=$1&quot;) will swap the value of var1 and var2).<br />
 NOTE: The pcre support is optional in ettercap and will be enabled only if you have the libpcre installed. The compiler will warn you if you try to compile a filter that contains pcre expressions but you don&#8217;t have libpcre. Use the -w option to suppress the warning. example:<br />
 pcre_regex(DATA.data, &quot;.*foo$&quot;)<br />
 pcre_regex(DATA.data, &quot;([^ ]*) bar ([^ ]*)&quot;, &quot;foo $1 $2&quot;)</p>
<dt><code>replace(</code><i>what</i>, <i>with</i>)</p>
<dd>this function replaces the string &#8216;what&#8217; with the string &#8216;with&#8217;. They can be binary string and must be escaped. The replacement is always performed in DATA.data since is the only payload which gets forwarded. The &#8216;DECODED.data&#8217; buffer is used only internally and never reaches the wire. example:<br />
 replace(&quot;ethercap&quot;, &quot;ettercap&quot;)</p>
<dt><code>inject(</code><i>what</i>)</p>
<dd>this function injects the content of the file &#8216;what&#8217; after the packet being processed. It always injects in DATA.data. You can use it to replace the entire packet with a fake one using the drop() function right before the inject() command. In that case the filtering engine will drop the current packet and inject the fake one. example:<br />
 inject(&quot;./fake_packet&quot;)</p>
<dt><code>log(</code><i>what</i>, <i>where</i>)</p>
<dd>this function dumps in the file &#8216;where&#8217; the buffer &#8216;what&#8217;. No information is stored about the packet, only the payload is dumped. So you will see the stream in the file. If you want to log packets in a more enhanced mode, you need to use the ettercap -L option and analyze it with <a href="/docs/linux/man/8-etterlog/">etterlog</a>(8).<br />
 The file &#8216;where&#8217; must be writable to the user EC_UID (see <a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5)). example:<br />
 log(DECODED.data, &quot;/tmp/interesting.log&quot;)</p>
<dt><code>msg(</code><i>message</i>)</p>
<dd>this function displays a message to the user in the User Messages window. It is useful to let the user know whether a particular filter has been successful or not. example:<br />
 msg(&quot;Packet filtered successfully&quot;)</p>
<dt><code>drop()</code></p>
<dd>this function marks the packet &quot;to be dropped&quot;. The packet will not be forwarded to the real destination. example:<br />
 drop()</p>
<dt><code>kill()</code></p>
<dd>this function kills the connection that owns the matched packet. If it is a TCP connection, a RST is sent to both sides of the connection. If it is an UDP connection, an ICMP PORT UNREACHABLE is sent to the source of the packet. example:<br />
 kill()</p>
<dt><code>exec(</code><i>command</i>)</p>
<dd>this function executes a shell command. You have to provide the full path to the command since it is executed without any environment. There is no way to determine if the command was successful or not. Furthermore, it is executed asynchronously since it is forked by the main process. example:<br />
 exec(&quot;/bin/cat /tmp/foo &gt;&gt; /tmp/bar&quot;)</p>
<dt><code>exit()</code></p>
<dd>this function causes the filter engine to stop executing the code. It is useful to stop the execution of the script on some circumstance checked by an &#8216;if&#8217; statement. example:<br />
 exit() </p>
<h2>Examples</h2>
<p>Here are some examples of using etterfilter.</p>
<dl>
<dt><code>etterfilter filter.ecf -o filter.ef</code></p>
<dd>Compiles the source filter.ecf into a binary filter.ef </p>
<h2>Authors</h2>
<p>Alberto Ornaghi (ALoR) &lt;alor [at] users.sf.net&gt;<br />
 Marco Valleri (NaGA) &lt;naga [at] antifork.org&gt;</p>
<h2>See Also</h2>
<p><i>etter.filter.examples</i><br />
 <i><a href="/docs/linux/man/8-ettercap/">ettercap</a>(8)</i> <i><a href="/docs/linux/man/8-etterlog/">etterlog</a>(8)</i> <i><a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5)</i> <i><a href="/docs/linux/man/8-ettercap_curses/">ettercap_curses</a>(8)</i> <i><a href="/docs/linux/man/8-ettercap_plugins/">ettercap_plugins</a>(8)</i> </p>
