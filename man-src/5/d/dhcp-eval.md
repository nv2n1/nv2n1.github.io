---

title: "dhcp-eval(5)"
name: "dhcp-eval"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dhcp-eval/"
description: "dhcp-eval – ISC DHCP conditional evaluation"
---

<p>dhcp-eval &#8211; ISC DHCP conditional evaluation </p>
<p> The Internet Systems Consortium DHCP client and server both provide the ability to perform conditional behavior depending on the contents of packets they receive. The syntax for specifying this conditional behaviour is documented here.  </p>
<h2>REFERENCE: CONDITIONAL BEHAVIOUR</h2>
<p> Conditional behaviour may be specified using the if statement and the else or elsif statements or the switch and case statements. A conditional statement can appear anywhere that a regular statement (e.g., an option statement) can appear, and can enclose one or more such statements. </p>
<p> <code>CONDITIONAL BEHAVIOUR: IF</code> </p>
<p>A typical conditional if statement in a server might be: </p>
<pre><code>if option dhcp-user-class = &quot;accounting&quot; {
  max-lease-time 17600;
  option domain-name &quot;accounting.example.org&quot;;
  option domain-name-servers ns1.accounting.example.org,
                             ns2.accounting.example.org;
} elsif option dhcp-user-class = &quot;sales&quot; {
  max-lease-time 17600;
  option domain-name &quot;sales.example.org&quot;;
  option domain-name-servers ns1.sales.example.org,
                             ns2.sales.example.org;
} elsif option dhcp-user-class = &quot;engineering&quot; {
  max-lease-time 17600;
  option domain-name &quot;engineering.example.org&quot;;
  option domain-name-servers ns1.engineering.example.org,
                             ns2.engineering.example.org;
} else {
  max-lease-time 600;
  option domain-name &quot;misc.example.org&quot;;
  option domain-name-servers ns1.misc.example.org,
                             ns2.misc.example.org;
}
</code></pre>
<p>On the client side, an example of conditional evaluation might be: </p>
<pre><code># example.org filters DNS at its firewall, so we have to use their DNS
# servers when we connect to their network. If we are not at
# example.org, prefer our own DNS server.
if not option domain-name = &quot;example.org&quot; {
  prepend domain-name-servers 127.0.0.1;
}
</code></pre>
<p>The <code>if</code> statement and the <code>elsif</code> continuation statement both take boolean expressions as their arguments. That is, they take expressions that, when evaluated, produce a boolean result. If the expression evaluates to true, then the statements enclosed in braces following the <code>if</code> statement are executed, and all subsequent <code>elsif</code> and <code>else</code> clauses are skipped. Otherwise, each subsequent <code>elsif</code> clause&#8217;s expression is checked, until an elsif clause is encountered whose test evaluates to true. If such a clause is found, the statements in braces following it are executed, and then any subsequent <code>elsif</code> and <code>else</code> clauses are skipped. If all the <code>if</code> and <code>elsif</code> clauses are checked but none of their expressions evaluate true, then if there is an <code>else</code> clause, the statements enclosed in braces following the <code>else</code> are evaluated. Boolean expressions that evaluate to null are treated as false in conditionals. </p>
<p> <code>CONDITIONAL BEHAVIOUR: SWITCH</code> </p>
<p>The above example can be rewritten using a switch construct as well. </p>
<pre><code>switch (option dhcp-user-class) {
  case &quot;accounting&quot;:
    max-lease-time 17600;
    option domain-name &quot;accounting.example.org&quot;;
    option domain-name-servers ns1.accounting.example.org,
                               ns2.accounting.example.org;
  case &quot;sales&quot;:
    max-lease-time 17600;
    option domain-name &quot;sales.example.org&quot;;
    option domain-name-servers ns1.sales.example.org,
                               ns2.sales.example.org;
    break;
  case &quot;engineering&quot;:
    max-lease-time 17600;
    option domain-name &quot;engineering.example.org&quot;;
    option domain-name-servers ns1.engineering.example.org,
                               ns2.engineering.example.org;
    break;
  default:
    max-lease-time 600;
    option domain-name &quot;misc.example.org&quot;;
    option domain-name-servers ns1.misc.example.org,
                               ns2.misc.example.org;
    break;
}
</code></pre>
<p>The <code>switch</code> statement and the <code>case</code> statements can both be data expressions or numeric expressions. Within a switch statement they all must be the same type. The server evaluates the expression from the switch statement and then it evaluates the expressions from the case statements until it finds a match. </p>
<p>If it finds a match it starts executing statements from that case until the next break statement. If it doesn&#8217;t find a match it starts from the default statement and again proceeds to the next break statement. If there is no match and no default it does nothing. </p>
<h2>BOOLEAN EXPRESSIONS</h2>
<p> The following is the current list of boolean expressions that are supported by the DHCP distribution. </p>
<p> <i>data-expression-1 </i><code>=</code> <i>data-expression-2</i> </p>
<dl>
<dd> <p>The <code>=</code> operator compares the values of two data expressions, returning true if they are the same, false if they are not. If either the left-hand side or the right-hand side are null, the result is also null. </p>
 </dd></dl>
<p> <i>data-expression-1 </i><code>~=</code> <i>data-expression-2</i> <i>data-expression-1 </i><code>~~</code> <i>data-expression-2</i> </p>
<dl>
<dd> <p>The <code>~=</code> and <code>~~</code> operators (not available on all systems) perform extended <a href="/docs/linux/man/7-regex/">regex</a>(7) matching of the values of two data expressions, returning true if <i>data-expression-1</i> matches against the regular expression evaluated by <i>data-expression-2</i>, or false if it does not match or encounters some error. If either the left-hand side or the right-hand side are null or empty strings, the result is also false. The <code>~~</code> operator differs from the <code>~=</code> operator in that it is case-insensitive. </p>
 </dd></dl>
<p> <i>boolean-expression-1 </i><code>and</code> <i>boolean-expression-2</i> </p>
<dl>
<dd> <p> The <code>and</code> operator evaluates to true if the boolean expression on the left-hand side and the boolean expression on the right-hand side both evaluate to true. Otherwise, it evaluates to false. If either the expression on the left-hand side or the expression on the right-hand side are null, the result is null. </p>
 </dd></dl>
<p> <i>boolean-expression-1 </i><code>or</code> <i>boolean-expression-2</i> </p>
<dl>
<dd> <p> The <code>or</code> operator evaluates to true if either the boolean expression on the left-hand side or the boolean expression on the right-hand side evaluate to true. Otherwise, it evaluates to false. If either the expression on the left-hand side or the expression on the right-hand side are null, the result is null. </p>
 </dd></dl>
<p> <code>not </code><i>boolean-expression</i> </p>
<dl>
<dd> <p> The <code>not</code> operator evaluates to true if <i>boolean-expression</i> evaluates to false, and returns false if <i>boolean-expression</i> evaluates to true. If <i>boolean-expression</i> evaluates to null, the result is also null. </p>
 </dd></dl>
<p> <code>exists </code><i>option-name</i> </p>
<dl>
<dd> <p> The <code>exists</code> expression returns true if the specified option exists in the incoming DHCP packet being processed. </p>
 </dd></dl>
<p> <code>known</code> </p>
<dl>
<dd> <p> The <code>known</code> expression returns true if the client whose request is currently being processed is known - that is, if there&#8217;s a host declaration for it. </p>
 </dd></dl>
<p> <code>static</code> </p>
<dl>
<dd> <p> The <code>static</code> expression returns true if the lease assigned to the client whose request is currently being processed is derived from a static address assignment. </p>
 </dd></dl>
<h2>DATA EXPRESSIONS</h2>
<p> Several of the boolean expressions above depend on the results of evaluating data expressions. A list of these expressions is provided here. </p>
<p> <code>substring (</code><i>data-expr</i><code>, </code><i>offset</i><code>, </code><i>length</i><code>)</code> </p>
<dl>
<dd> <p> The <code>substring</code> operator evaluates the data expression and returns the substring of the result of that evaluation that starts <i>offset</i> bytes from the beginning, continuing for <i>length</i> bytes. <i>Offset</i> and <i>length</i> are both numeric expressions. If <i>data-expr</i>, <i>offset</i> or <i>length</i> evaluate to null, then the result is also null. If <i>offset</i> is greater than or equal to the length of the evaluated data, then a zero-length data string is returned. If <i>length is greater then the remaining length of the evaluated data after offset</i>, then a data string containing all data from <i>offset</i> to the end of the evaluated data is returned. </p>
 </dd></dl>
<p> <code>suffix (</code><i>data-expr</i><code>, </code><i>length</i><code>)</code> </p>
<dl>
<dd> <p> The <code>suffix</code> operator evaluates <i>data-expr</i> and returns the last <i>length</i> bytes of the result of that evaluation. <i>Length</i> is a numeric expression. If <i>data-expr</i> or <i>length</i> evaluate to null, then the result is also null. If <i>suffix</i> evaluates to a number greater than the length of the evaluated data, then the evaluated data is returned. </p>
 </dd></dl>
<p> <code>lcase (</code><i>data-expr</i><code>)</code> </p>
<dl>
<dd> <p> The <code>lcase</code> function returns the result of evaluating <i>data-expr</i> converted to lower case. If <i>data-expr</i> evaluates to null, then the result is also null. </p>
 </dd></dl>
<p> <code>ucase (</code><i>data-expr</i><code>)</code> </p>
<dl>
<dd> <p> The <code>ucase</code> function returns the result of evaluating <i>data-expr</i> converted to upper case. If <i>data-expr</i> evaluates to null, then the result is also null. </p>
 </dd></dl>
<p> <code>option </code><i>option-name</i> </p>
<dl>
<dd> <p> The <code>option</code> operator returns the contents of the specified option in the packet to which the server is responding. </p>
 </dd></dl>
<p> <code>config-option </code><i>option-name</i> </p>
<dl>
<dd> <p> The <code>config-option</code> operator returns the value for the specified option that the DHCP client or server has been configured to send. </p>
 </dd></dl>
<p> <code>gethostname()</code> </p>
<dl>
<dd> <p> The <code>gethostname()</code> function returns a data string whose contents are a character string, the results of calling gethostname() on the local system with a size limit of 255 bytes (not including NULL terminator). This can be used for example to configure dhclient to send the local hostname without knowing the local hostname at the time dhclient.conf is written. </p>
 </dd></dl>
<p> <code>hardware</code> </p>
<dl>
<dd> <p> The <code>hardware</code> operator returns a data string whose first element is the type of network interface indicated in packet being considered, and whose subsequent elements are client&#8217;s link-layer address. If there is no packet, or if the RFC2131 <i>hlen</i> field is invalid, then the result is null. Hardware types include ethernet (1), token-ring (6), and fddi (8). Hardware types are specified by the IETF, and details on how the type numbers are defined can be found in RFC2131 (in the ISC DHCP distribution, this is included in the doc/ subdirectory). </p>
 </dd></dl>
<p> <code>packet (</code><i>offset</i><code>, </code><i>length</i><code>)</code> </p>
<dl>
<dd> <p> The <code>packet</code> operator returns the specified portion of the packet being considered, or null in contexts where no packet is being considered. <i>Offset</i> and <i>length</i> are applied to the contents packet as in the <code>substring</code> operator. </p>
 </dd></dl>
<p> <i>string</i> </p>
<dl>
<dd> <p> A string, enclosed in quotes, may be specified as a data expression, and returns the text between the quotes, encoded in ASCII. The backslash (&#8216;\&#8216;) character is treated specially, as in C programming: &#8216;\t&#8217; means TAB, &#8216;\r&#8217; means carriage return, &#8216;\n&#8217; means newline, and &#8216;\b&#8217; means bell. Any octal value can be specified with &#8216;\nnn&#8217;, where nnn is any positive octal number less than 0400. Any hexadecimal value can be specified with &#8216;\xnn&#8217;, where nn is any positive hexadecimal number less than or equal to 0xff. </p>
 </dd></dl>
<p> <i>colon-separated hexadecimal list</i> </p>
<dl>
<dd> <p> A list of hexadecimal octet values, separated by colons, may be specified as a data expression. </p>
 </dd></dl>
<p> <code>concat (</code><i>data-expr1</i><code>, ..., </code><i>data-exprN</i><code>)</code> </p>
<dl>
<dd> <p> The expressions are evaluated, and the results of each evaluation are concatenated in the sequence that the subexpressions are listed. If any subexpression evaluates to null, the result of the concatenation is null. </p>
 </dd></dl>
<p> <code>reverse (</code><i>numeric-expr1</i><code>, </code><i>data-expr2</i><code>)</code> </p>
<dl>
<dd> <p> The two expressions are evaluated, and then the result of evaluating the data expression is reversed in place, using hunks of the size specified in the numeric expression. For example, if the numeric expression evaluates to four, and the data expression evaluates to twelve bytes of data, then the reverse expression will evaluate to twelve bytes of data, consisting of the last four bytes of the input data, followed by the middle four bytes, followed by the first four bytes. </p>
 </dd></dl>
<p> <code>leased-address</code> </p>
<dl>
<dd> <p> In any context where the client whose request is being processed has been assigned an IP address, this data expression returns that IP address. In any context where the client whose request is being processed has not been assigned an ip address, if this data expression is found in executable statements executed on that client&#8217;s behalf, a log message indicating &quot;there is no lease associated with this client&quot; is syslogged to the debug level (this is considered dhcpd.conf debugging information). </p>
 </dd></dl>
<p> <code>binary-to-ascii (</code><i>numeric-expr1</i><code>, </code><i>numeric-expr2</i><code>,</code> <i>data-expr1</i><code>,</code> <i>data-expr2</i><code>)</code> </p>
<dl>
<dd> <p> Converts the result of evaluating data-expr2 into a text string containing one number for each element of the result of evaluating data-expr2. Each number is separated from the other by the result of evaluating data-expr1. The result of evaluating numeric-expr1 specifies the base (2 through 16) into which the numbers should be converted. The result of evaluating numeric-expr2 specifies the width in bits of each number, which may be either 8, 16 or 32. </p>
<p>As an example of the preceding three types of expressions, to produce the name of a PTR record for the IP address being assigned to a client, one could write the following expression: </p>
 </dd></dl>
<pre><code>        concat (binary-to-ascii (10, 8, &quot;.&quot;,
                                 reverse (1, leased-address)),
                &quot;.in-addr.arpa.&quot;);
</code></pre>
<p> <code>encode-int (</code><i>numeric-expr</i><code>, </code><i>width</i><code>)</code> </p>
<dl>
<dd> <p> Numeric-expr is evaluated and encoded as a data string of the specified width, in network byte order (most significant byte first). If the numeric expression evaluates to the null value, the result is also null. </p>
 </dd></dl>
<p> <code>pick-first-value (</code><i>data-expr1</i> [ ... <i>expr</i>n ] <code>)</code> </p>
<dl>
<dd> <p> The pick-first-value function takes any number of data expressions as its arguments. Each expression is evaluated, starting with the first in the list, until an expression is found that does not evaluate to a null value. That expression is returned, and none of the subsequent expressions are evaluated. If all expressions evaluate to a null value, the null value is returned. </p>
 </dd></dl>
<p> <code>host-decl-name</code> </p>
<dl>
<dd> <p> The host-decl-name function returns the name of the host declaration that matched the client whose request is currently being processed, if any. If no host declaration matched, the result is the null value. </p>
 </dd></dl>
<h2>NUMERIC EXPRESSIONS</h2>
<p> Numeric expressions are expressions that evaluate to an integer. In general, the maximum size of such an integer should not be assumed to be representable in fewer than 32 bits, but the precision of such integers may be more than 32 bits. </p>
<p>In addition to the following operators several standard math functions are available. They are: </p>
<pre><code>operation symbol
add + subtract - divide / multiply * modulus % bitwise and &amp; bitwise or | bitwise xor ^ 
</code></pre>
<p> <code>extract-int (</code><i>data-expr</i><code>, </code><i>width</i><code>)</code> </p>
<dl>
<dd> <p> The <code>extract-int</code> operator extracts an integer value in network byte order from the result of evaluating the specified data expression. Width is the width in bits of the integer to extract. Currently, the only supported widths are 8, 16 and 32. If the evaluation of the data expression doesn&#8217;t provide sufficient bits to extract an integer of the specified size, the null value is returned. </p>
 </dd></dl>
<p> <code>lease-time</code> </p>
<dl>
<dd> <p> The duration of the current lease - that is, the difference between the current time and the time that the lease expires. </p>
 </dd></dl>
<p> <i>number</i> </p>
<dl>
<dd> <p> Any number between zero and the maximum representable size may be specified as a numeric expression. </p>
 </dd></dl>
<p> <code>client-state</code> </p>
<dl>
<dd> <p> The current state of the client instance being processed. This is only useful in DHCP client configuration files. Possible values are: </p>
 </dd>
<dl>
<dt><i>&bull;</i></dt>
<dd> <p> Booting - DHCP client is in the INIT state, and does not yet have an IP address. The next message transmitted will be a DHCPDISCOVER, which will be broadcast. </p>
 </dd>
<dt><i>&bull;</i></dt>
<dd> <p> Reboot - DHCP client is in the INIT-REBOOT state. It has an IP address, but is not yet using it. The next message to be transmitted will be a DHCPREQUEST, which will be broadcast. If no response is heard, the client will bind to its address and move to the BOUND state. </p>
 </dd>
<dt><i>&bull;</i></dt>
<dd> <p> Select - DHCP client is in the SELECTING state - it has received at least one DHCPOFFER message, but is waiting to see if it may receive other DHCPOFFER messages from other servers. No messages are sent in the SELECTING state. </p>
 </dd>
<dt><i>&bull;</i></dt>
<dd> <p> Request - DHCP client is in the REQUESTING state - it has received at least one DHCPOFFER message, and has chosen which one it will request. The next message to be sent will be a DHCPREQUEST message, which will be broadcast. </p>
 </dd>
<dt><i>&bull;</i></dt>
<dd> <p> Bound - DHCP client is in the BOUND state - it has an IP address. No messages are transmitted in this state. </p>
 </dd>
<dt><i>&bull;</i></dt>
<dd> <p> Renew - DHCP client is in the RENEWING state - it has an IP address, and is trying to contact the server to renew it. The next message to be sent will be a DHCPREQUEST message, which will be unicast directly to the server. </p>
 </dd>
<dt><i>&bull;</i></dt>
<dd> <p> Rebind - DHCP client is in the REBINDING state - it has an IP address, and is trying to contact any server to renew it. The next message to be sent will be a DHCPREQUEST, which will be broadcast. </p>
 </dd></dl>
</dl>
<h2>REFERENCE: ACTION EXPRESSIONS</h2>
<p> <code>log (</code><i>priority</i><code>, </code><i>data-expr</i><code>)</code> </p>
<dl>
<dd> <p>Logging statements may be used to send information to the standard logging channels. A logging statement includes an optional priority (<code>fatal</code>, <code>error</code>, <code>info</code>, or <code>debug</code>), and a data expression. </p>
<p>Logging statements take only a single data expression argument, so if you want to output multiple data values, you will need to use the <code>concat</code> operator to concatenate them. </p>
 </dd></dl>
<p> <code>execute (</code><i>command-path</i><code> [, </code><i>data-expr1</i><code>, ... </code><i>data-exprN</i><code>]);</code> </p>
<dl>
<dd> <p>The <code>execute</code> statement runs an external command. The first argument is a string literal containing the name or path of the command to run. The other arguments, if present, are either string literals or data- expressions which evaluate to text strings, to be passed as command-line arguments to the command. </p>
<p> <code>execute</code> is synchronous; the program will block until the external command being run has finished. Please note that lengthy program execution (for example, in an &quot;on commit&quot; in dhcpd.conf) may result in bad performance and timeouts. Only external applications with very short execution times are suitable for use. </p>
<p>Passing user-supplied data to an external application might be dangerous. Make sure the external application checks input buffers for validity. Non-printable ASCII characters will be converted into dhcpd.conf language octal escapes (&quot;\nnn&quot;), make sure your external command handles them as such. </p>
<p>It is possible to use the execute statement in any context, not only on events. If you put it in a regular scope in the configuration file you will execute that command every time a scope is evaluated. </p>
 </dd></dl>
<p> <code>parse-vendor-option;</code> </p>
<dl>
<dd> <p>The <code>parse-vendor-option</code> statement attempts to parse a vendor option (code 43). It is only useful while processing a packet on the server and requires that the administrator has already used the <code>vendor-option-space</code> statement to select a valid vendor space. </p>
<p>This functionality may be used if the server needs to take different actions depending on the values the client placed in the vendor option and the sub-options are not at fixed locations. It is handled as an action to allow an administrator to examine the incoming options and choose the correct vendor space. </p>
 </dd></dl>
<h2>REFERENCE: DYNAMIC DNS UPDATES</h2>
<p>See the dhcpd.conf and dhclient.conf man pages for more information about DDNS.  </p>
<h2>SEE ALSO</h2>
<p> dhcpd.conf(5), dhcpd.leases(5), dhclient.conf(5), <a href="/docs/linux/man/5-dhcp-options/">dhcp-options</a>(5), <a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), <a href="/docs/linux/man/8-dhclient/">dhclient</a>(8), RFC2132, RFC2131.  </p>
<h2>AUTHOR</h2>
<p> Information about Internet Systems Consortium can be found at <code><a rel="nofollow" href="https://www.isc.org.">https://www.isc.org.</a></code> </p>
