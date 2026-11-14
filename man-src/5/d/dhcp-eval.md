---
title: "dhcp-eval(5)"
name: "dhcp-eval"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dhcp-eval/"
description: "dhcp-eval – ISC DHCP conditional evaluation"
---

<p>dhcp-eval &#8211; ISC DHCP conditional evaluation</p>
<h2>Description</h2>
<p>The Internet Systems Consortium DHCP client and server both provide the ability to perform conditional behavior depending on the contents of packets they receive. The syntax for specifying this conditional behaviour is documented here.</p>
<h2>Reference: Conditional Behaviour</h2>
<p>Conditional behaviour may be specified using the if statement and the else or elsif statements or the switch and case statements. A conditional statement can appear anywhere that a regular statement (e.g., an option statement) can appear, and can enclose one or more such statements. </p>
<p> <code>CONDITIONAL BEHAVIOUR: IF</code> </p>
<p> A typical conditional if statement in a server might be: </p>
<pre>if option dhcp-user-class = &quot;accounting&quot; {
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
}</pre>
<p>On the client side, an example of conditional evaluation might be: </p>
<pre># example.org filters DNS at its firewall, so we have to use their DNS
# servers when we connect to their network. If we are not at
# example.org, prefer our own DNS server.
if not option domain-name = &quot;example.org&quot; {
 prepend domain-name-servers 127.0.0.1;
}</pre>
<p>The <code>if</code> statement and the <code>elsif</code> continuation statement both take boolean expressions as their arguments. That is, they take expressions that, when evaluated, produce a boolean result. If the expression evaluates to true, then the statements enclosed in braces following the <code>if</code> statement are executed, and all subsequent <code>elsif</code> and <code>else</code> clauses are skipped. Otherwise, each subsequent <code>elsif</code> clause&#8217;s expression is checked, until an elsif clause is encountered whose test evaluates to true. If such a clause is found, the statements in braces following it are executed, and then any subsequent <code>elsif</code> and <code>else</code> clauses are skipped. If all the <code>if</code> and <code>elsif</code> clauses are checked but none of their expressions evaluate true, then if there is an <code>else</code> clause, the statements enclosed in braces following the <code>else</code> are evaluated. Boolean expressions that evaluate to null are treated as false in conditionals. </p>
<p> <code>CONDITIONAL BEHAVIOUR: SWITCH</code> </p>
<p> The above example can be rewritten using a switch construct as well. </p>
<pre>switch (option dhcp-user-class) {
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
}</pre>
<p>The <code>switch</code> statement and the <code>case</code> statements can both be data expressions or numeric expressions. Within a switch statement they all must be the same type. The server evaluates the expression from the switch statement and then it evaluates the expressions from the case statements until it finds a match. </p>
<p> If it finds a match it starts executing statements from that case until the next break statement. If it doesn&#8217;t find a match it starts from the default statement and again proceeds to the next break statement. If there is no match and no default it does nothing.</p>
<h2>Boolean Expressions</h2>
<p>The following is the current list of boolean expressions that are supported by the DHCP distribution. </p>
<p> <i>data-expression-1 </i><code>=</code> <i>data-expression-2</i></p>
<dl>
<dd>The <code>=</code> operator compares the values of two data expressions, returning true if they are the same, false if they are not. If either the left-hand side or the right-hand side are null, the result is also null.</dl>
<p> <i>data-expression-1 </i><code>~=</code> <i>data-expression-2</i> <i>data-expression-1 </i><code>~~</code> <i>data-expression-2</i></p>
<dl>
<dd>The <code>~=</code> and <code>~~</code> operators (not available on all systems) perform extended <a href="/docs/linux/man/7-regex/">regex</a>(7) matching of the values of two data expressions, returning true if <i>data-expression-1</i> matches against the regular expression evaluated by <i>data-expression-2</i>, or false if it does not match or encounters some error. If either the left-hand side or the right-hand side are null or empty strings, the result is also false. The <code>~~</code> operator differs from the <code>~=</code> operator in that it is case-insensitive.</dl>
<p> <i>boolean-expression-1 </i><code>and</code> <i>boolean-expression-2</i> </p>
<dl>
<dd>The <code>and</code> operator evaluates to true if the boolean expression on the left-hand side and the boolean expression on the right-hand side both evaluate to true. Otherwise, it evaluates to false. If either the expression on the left-hand side or the expression on the right-hand side are null, the result is null.</dl>
<p> <i>boolean-expression-1 </i><code>or</code> <i>boolean-expression-2</i> </p>
<dl>
<dd>The <code>or</code> operator evaluates to true if either the boolean expression on the left-hand side or the boolean expression on the right-hand side evaluate to true. Otherwise, it evaluates to false. If either the expression on the left-hand side or the expression on the right-hand side are null, the result is null.</dl>
<p> <code>not </code><i>boolean-expression</i> </p>
<dl>
<dd>The <code>not</code> operator evaluates to true if <i>boolean-expression</i> evaluates to false, and returns false if <i>boolean-expression</i> evaluates to true. If <i>boolean-expression</i> evaluates to null, the result is also null.</dl>
<p> <code>exists </code><i>option-name</i> </p>
<dl>
<dd>The <code>exists</code> expression returns true if the specified option exists in the incoming DHCP packet being processed.</dl>
<p> <code>known</code> </p>
<dl>
<dd>The <code>known</code> expression returns true if the client whose request is currently being processed is known &#8211; that is, if there&#8217;s a host declaration for it.</dl>
<p> <code>static</code> </p>
<dl>
<dd>The <code>static</code> expression returns true if the lease assigned to the client whose request is currently being processed is derived from a static address assignment.</dl>
<h2>Data Expressions</h2>
<p>Several of the boolean expressions above depend on the results of evaluating data expressions. A list of these expressions is provided here. </p>
<p> <code>substring (</code><i>data-expr</i><code>, </code><i>offset</i><code>, </code><i>length</i><code>)</code> </p>
<dl>
<dd>The <code>substring</code> operator evaluates the data expression and returns the substring of the result of that evaluation that starts <i>offset</i> bytes from the beginning, continuing for <i>length</i> bytes. <i>Offset</i> and <i>length</i> are both numeric expressions. If <i>data-expr</i>, <i>offset</i> or <i>length</i> evaluate to null, then the result is also null. If <i>offset</i> is greater than or equal to the length of the evaluated data, then a zero-length data string is returned. If <i>length is greater then the remaining length of the evaluated data after offset</i>, then a data string containing all data from <i>offset</i> to the end of the evaluated data is returned.</dl>
<p> <code>suffix (</code><i>data-expr</i><code>, </code><i>length</i><code>)</code> </p>
<dl>
<dd>The <code>suffix</code> operator evaluates <i>data-expr</i> and returns the last <i>length</i> bytes of the result of that evaluation. <i>Length</i> is a numeric expression. If <i>data-expr</i> or <i>length</i> evaluate to null, then the result is also null. If <i>suffix</i> evaluates to a number greater than the length of the evaluated data, then the evaluated data is returned.</dl>
<p> <code>lcase (</code><i>data-expr</i><code>)</code> </p>
<dl>
<dd>The <code>lcase</code> function returns the result of evaluating <i>data-expr</i> converted to lower case. If <i>data-expr</i> evaluates to null, then the result is also null.</dl>
<p> <code>ucase (</code><i>data-expr</i><code>)</code> </p>
<dl>
<dd>The <code>ucase</code> function returns the result of evaluating <i>data-expr</i> converted to upper case. If <i>data-expr</i> evaluates to null, then the result is also null.</dl>
<p> <code>option </code><i>option-name</i> </p>
<dl>
<dd>The <code>option</code> operator returns the contents of the specified option in the packet to which the server is responding.</dl>
<p> <code>config-option </code><i>option-name</i> </p>
<dl>
<dd>The <code>config-option</code> operator returns the value for the specified option that the DHCP client or server has been configured to send.</dl>
<p> <code>gethostname()</code> </p>
<dl>
<dd>The <code>gethostname()</code> function returns a data string whose contents are a character string, the results of calling gethostname() on the local system with a size limit of 255 bytes (not including NULL terminator). This can be used for example to configure dhclient to send the local hostname without knowing the local hostname at the time dhclient.conf is written.</dl>
<p> <code>hardware</code> </p>
<dl>
<dd>The <code>hardware</code> operator returns a data string whose first element is the type of network interface indicated in packet being considered, and whose subsequent elements are client&#8217;s link-layer address. If there is no packet, or if the RFC2131 <i>hlen</i> field is invalid, then the result is null. Hardware types include ethernet (1), token-ring (6), and fddi (8). Hardware types are specified by the IETF, and details on how the type numbers are defined can be found in RFC2131 (in the ISC DHCP distribution, this is included in the doc/ subdirectory).</dl>
<p> <code>packet (</code><i>offset</i><code>, </code><i>length</i><code>)</code> </p>
<dl>
<dd>The <code>packet</code> operator returns the specified portion of the packet being considered, or null in contexts where no packet is being considered. <i>Offset</i> and <i>length</i> are applied to the contents packet as in the <code>substring</code> operator.</dl>
<p> <i>string</i> </p>
<dl>
<dd>A string, enclosed in quotes, may be specified as a data expression, and returns the text between the quotes, encoded in ASCII. The backslash (&#8216;\&#8217;) character is treated specially, as in C programming: &#8216;	&#8217; means TAB, &#8216;&#8217; means carriage return, &#8216;
&#8217; means newline, and &#8216;&#8217; means bell. Any octal value can be specified with &#8216;
nn&#8217;, where nnn is any positive octal number less than 0400. Any hexadecimal value can be specified with &#8216;
