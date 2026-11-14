---
title: "milter-regex(8)"
name: "milter-regex"
section: "8"
letter: "m"
url: "/docs/linux/man/8-milter-regex/"
description: "milter-regex – sendmail milter plugin for regular expression filtering"
---

<p><code>milter-regex</code> &#8211; sendmail milter plugin for regular expression filtering</p>
<h2>Synopsis</h2>
<p>[-<code>d</code> ] [-<code>c </code><i>config</i> ] [-<code>j </code><i>dirname</i> ] [-<code>l </code><i>loglevel</i> ] [-<code>m </code><i>number</i> ] [-<code>p </code><i>pipe</i> ] [-<code>u </code><i>user</i> ]</p>
<h2>Description</h2>
<p>The plugin can be used with the milter API of <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) to filter mails using regular expressions matching SMTP envelope parameters and mail headers and body. The options are as follows:</p>
<dl>
<dt><code>-d</code></p>
<dd>Don&#8217;t detach from controlling terminal and produce verbose debug output on stdout.</p>
<dt><code>-c </code><i>config</i></p>
<dd>Use the specified configuration file instead of the default, /etc/mail/milter-regex.conf.</p>
<dt><code>-j </code><i>dirname</i></p>
<dd>Change root to the specified directory.</p>
<dt><code>-l </code><i>loglevel</i></p>
<dd>Only log messages up to and including the specified level. See <a href="/docs/linux/man/3-syslog/">syslog</a>(3) for the numerical values, e.g. LOG_INFO=6.</p>
<dt><code>-m </code><i>number</i></p>
<dd>Ignore mail body after the specified number of lines.</p>
<dt><code>-p </code><i>pipe</i></p>
<dd>Use the specified pipe to interface <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8). Default is unix:/var/spool/milter-regex/sock.</p>
<dt><code>-u </code><i>user</i></p>
<dd>Run as the specified user instead of the default, mregex. When is started as root, it calls <a href="/docs/linux/man/2-setuid/">setuid</a>(2) to drop privileges. The non-privileged user should have read access to the configuration file and read-write access to the pipe.</dl>
<h2>Sendmail Configuration</h2>
<p>The plugin needs to be registered in the <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) configuration, by adding the following lines to the .mc file </p>
<blockquote>
<pre>INPUT_MAIL_FILTER(`milter-regex',
 `S=unix:/var/spool/milter-regex/sock, T=S:30s;R:2m')</pre>
</blockquote>
<p> rebuilding /etc/mail/sendmail.cf from the .mc file using <a href="/docs/linux/man/1-m4/">m4</a>(1), and restarting <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8).</p>
<h2>Plugin Configuration</h2>
<p>The configuration file consists of rules that, when matched, cause <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) to reject mails. Emtpy lines and lines starting with # are ignored, as well as leading whitespace (blanks, tabs). Trailing backslashes can be used to wrap long rules into multiple lines. Each rule starts with one of the following commands:</p>
<dl>
<dt><code>reject &lt;message&gt;</code></p>
<dd>Subsequent rules cause the mail to be rejected with a permanent error consisting of the specified text part. The SMTP reply consists of the three-digit code 554 (RFC 2821 &quot;command rejected for policy reasons&quot;), the extended reply code 5.7.1 (RFC 1893 &quot;Permanent Failure&quot;, &quot;Security or Policy Status&quot;, &quot;Delivery not authorized, message refused&quot;) and the text part (which defaults to &quot;Command rejected&quot;, if not specified). This is a permanent failure, which causes the sender to remove the message from its queue without trying to retransmit, commonly generating a bounce message to the sender.</p>
<dt><code>tempfail &lt;message&gt;</code></p>
<dd>Subsequent matching rules cause the mail to be rejected with a temporary error consisting of the specified text part. The SMTP reply consists of the three-digit code 451 (RFC 2821 &quot;Requested action aborted: local error in processing&quot;), the extended reply code 4.7.1 (RFC 1893 &quot;Persistent Transient Failure&quot;, &quot;Security or Policy Status&quot;, &quot;Delivery not authorized, message refused&quot;) and the text part (which defaults to &quot;Please try again later&quot;, if not specified). This is a temporary failure, which causes the sender to keep the message in its queue and try to retransmit it, commonly for several days.</p>
<dt><code>discard</code></p>
<dd>Subsequent matching rules cause the mail to be accepted but then discarded silently. Note that <i>connect</i> and <i>helo</i> rules should not use <i>discard</i></p>
<dt><code>quarantine &lt;message&gt;</code></p>
<dd>Subsequent matching rules cause the mail to be quarantined in <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8).</p>
<dt><code>accept</code></p>
<dd>Subsequent matching rules cause the mail to be accepted without further rule evaluation. Can be used for whitelist criteria.</dl>
<p> A command is followed by one or more expressions, each causing the previous command to be executed when matched. The following expressions can be used:</p>
<dl>
<dt><code>connect &lt;hostname&gt; &lt;address&gt;</code></p>
<dd>Reject the connection if both the sender&#8217;s hostname and address match the specified regular expressions. The numerical address is either dotted-quad (IPv4) or coloned-hex (IPv6). The hostname is the result of a DNS reverse resolution of the numerical address (which <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) performs independantly of the milter plugin). When resolution fails, the hostname contains the numerical address in square brackets.</p>
<dt><code>helo &lt;name&gt;</code></p>
<dd>Reject the connection if the sender supplied HELO name matches the specified regular expression. Commonly, the sender supplies his fully-qualified hostname as HELO name.</p>
<dt><code>envfrom &lt;address&gt;</code></p>
<dd>Reject the mail if the sender supplied envelope MAIL FROM address matches the specified regular expression. Addresses commonly have the form &lt;user [at] host.doma.in&gt;.</p>
<dt><code>envrcpt &lt;address&gt;</code></p>
<dd>Reject the mail if the sender supplied envelope RCPT TO address matches the specified regular expression.</p>
<dt><code>header &lt;name&gt; &lt;value&gt;</code></p>
<dd>Reject the mail if a header matches the specified name and value. For instance, the header &quot;Subject: Test&quot; matches name Subject and value Test.</p>
<dt><code>body &lt;line&gt;</code></p>
<dd>Reject the mail if a body line matches the specified regular expression.</p>
<dt><code>macro &lt;name&gt; &lt;value&gt;</code></p>
<dd>Reject the mail if a sendmail macro value matches.</dl>
<p> The plugin regularly checks the configuration file for modification and reloads it automatically. Signals like SIGHUP will terminate the plugin, according to the milter signal handler. The plugin reacts to any kind of error, like syntax errors in the configuration file, by failing open, accepting all messages. When the plugin is not running, <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8) will accept all messages.</p>
<h2>Regular Expressions</h2>
<p>The regular expressions used in the configuration rules are enclosed in arbitrary delimiters, no further escaping is needed. </p>
<p> The first character of an argument is taken as the delimiter, and all subsequent characters up to the next occurance of the same delimiter are taken literally as the regular expression. Since the delimiter itself cannot be part of the regular expression (no escaping is supported), a delimiter must be chosen that doesn&#8217;t occur in the regular expression itself. Each argument can use a different delimiter, all characters except spaces and tabs are valid. </p>
<p> Two immediately adjacent delimiters form an empty regular expression, which always matches and requires no <a href="/docs/linux/man/3-regexec/">regexec</a>(3) call. This can be used in rules requiring multiple arguments, to match only some arguments. </p>
<p> See re_format7 for a detailed description of basic and extended regular expressions. </p>
<p> Optionally, the following flags can be used after the closing delimiter:</p>
<dl>
<dt><code>e</code></p>
<dd>Extended regular expression. This sets REG_EXTENDED for <a href="/docs/linux/man/3-regcomp/">regcomp</a>(3).</p>
<dt><code>i</code></p>
<dd>Ignore upper/lower case. This sets REG_ICASE.</p>
<dt><code>n</code></p>
<dd>Not matching. Reverses the matching result, i.e. the mail is rejected if the regular expression does not match.</dl>
<h2>Boolean Expressions</h2>
<p>A rule can consist of either a simple term or more complex expressions. A term has the form </p>
<pre>header /From/ /domain/i</pre>
<p>and expressions can be built combining terms with operators &quot;and&quot;, &quot;or&quot;, &quot;not&quot; and parentheses, as in </p>
<pre>header /From/ /domain/i and body /money/
( not header /From/ /domain/ ) and ( body /sex/ or body /fast/ )</pre>
<p>Operator precedence should not be relied on, instead parentheses should be used to resolve any ambiguities (they usually produce syntax errors from the parser).</p>
<h2>Macros</h2>
<p>Macros allow to store terms or expressions as a name, and $name can be used as term within other rules, expressions or macro definitions. Example: </p>
<pre>friends = header /^Received$/ /^from [^ ]*(ork.net|home.com)/e
attachments = header ,^Content-Type$, ,multipart/mixed, and \
 body ,^Content-Type: application/,
executables = $attachments and body ,name=&quot;.*.(pif|exe|scr)&quot;$,e
reject &quot;executable attachment from non-friends&quot;
$executables and not $friends</pre>
<p>Macro names must begin with a letter and may contain alphanumeric characters and punctuation characters. Reserved keywords (like &quot;reject&quot; or &quot;header&quot;) cannot be used as macro names. Macros must be defined before use, the definition must precede the use in the configuration file, read from top to bottom.</p>
<h2>Evaluation</h2>
<p>Rules are evaluated in the order specified in the configuration file, from top to bottom. When a rule matches, the corresponding action is taken, that is the last action specified before the matching rule. </p>
<p> The plugin evaluates the rules every time a line of mail (or envelope) is received. As soon as a rule matches, the action is taken immediately, possibly before the entire mail is received, even if further lines might possibly make other rules match, too. This means the first rule matching chronologically has precedence. </p>
<p> If evaluation for a line of mail makes two (or more) rules match, the rule that comes first in the configuration file has precedence. </p>
<p> Boolean expressions are short-circuit evaluated, that means &quot;a or b&quot; becomes true as soon as one of the terms is true and &quot;a and b&quot; becomes false as soon as one of the terms is false, even if the other term is not known, possibly because the relevant mail line has not been received yet.</p>
<h2>Examples</h2>
<pre># /etc/mail/milter-regex.conf example
# Accept anything encrypted, just to demonstrate sendmail macros
accept
macro /tls_version/ /TLSv/
tempfail &quot;Sender IP address not resolving&quot;
connect /\[.*\]/ //
reject &quot;Malformed HELO (not a domain, no dot)&quot;
helo /\./n
reject &quot;Malformed RCPT TO (not an email address, not &lt;.*@.*&gt;)&quot;
envrcpt /&lt;(.*@.*|Postmaster)&gt;/ein
reject &quot;HTML mail not accepted&quot;
# use comma as delimiter here, as / occurs within RE
header /^Content-type$/i ,^text/html,i
body ,^Content-type: text/html,i
# Swen worm
discard
header /^(TO|FROM|SUBJECT)$/e //
header /^Content-type$/i /boundary=&quot;Boundary_(ID_/i
header /^Content-type$/i /boundary=&quot;[a-z]*&quot;/
body ,^Content-type: audio/x-wav; name=&quot;[a-z]*\.[a-z]*&quot;,i
# Some nasty spammer
reject &quot;Business Corp spam, get lost&quot;
body /^Business Corp. for W.&amp; L. AG/i and \
 ( body /043.*317.*0285/ or body /0041.43.317.02.85/ )</pre>
<h2>Logging</h2>
<p>sends log messages to <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8) using <i>facility</i> daemon and, with increasing verbosity, <i>level</i> err, notice, info and debug. The following syslog.conf5 section can be used to log messages to a dedicated file: </p>
<pre>!milter-regex
daemon.err;daemon.notice /var/log/milter-regex</pre>
<h2>Grammar</h2>
<p>Syntax for in BNF: </p>
<pre>file = ( rule | macro ) file
rule = action expr-list
action = &quot;reject&quot; msg | &quot;tempfail&quot; msg | &quot;discard&quot; |
 &quot;quarantine&quot; msg | &quot;accept&quot;
msg = ( '&quot;' | &quot;'&quot; ) string ( '&quot;' | &quot;'&quot; )
expr-list = expr [ expr-list ]
expr = term | term &quot;and&quot; expr | term &quot;or&quot; expr | &quot;not&quot; term
term = '(' expr ')' | &quot;connect&quot; arg arg | &quot;helo&quot; arg |
 &quot;envfrom&quot; arg | &quot;envrcpt&quot; arg | &quot;header&quot; arg arg |
 &quot;body&quot; arg | &quot;macro&quot; arg arg | '$' name
arg = del regex del flags
del = '/' | ',' | '-' | ...
flags = [ 'e' ] [ 'i' ] [ 'n' ]
macro = name '=' expr</pre>
<h2>Files</h2>
<p>/etc/mail/milter-regex.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-mailstats/">mailstats</a>(1), <a href="/docs/linux/man/3-regex/">regex</a>(3), <a href="/docs/linux/man/3-syslog/">syslog</a>(3), syslog.conf5, re_format7, <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8), <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)</p>
<dl>
<dd><i>Simple Mail Transfer Protocol</i> RFC 2821</dl>
<dl>
<dd><i>Enhanced Mail System Status Codes</i> RFC 1893</dl>
<h2>History</h2>
<p>The first version of was written in 2003. Boolean expression evaluation was added in 2004.</p>
<h2>Authors</h2>
<p>Daniel Hartmeier Aq daniel [at] benzedrine.cx</p>
