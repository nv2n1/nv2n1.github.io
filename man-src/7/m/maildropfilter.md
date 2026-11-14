---
title: "maildropfilter(7)"
name: "maildropfilter"
section: "7"
letter: "m"
url: "/docs/linux/man/7-maildropfilter/"
description: "maildropfilter – maildrop’s filtering language"
---

<p>maildropfilter &#8211; maildrop&#8217;s filtering language</p>
<h2>Synopsis</h2>
<p>/etc/maildroprc, $HOME/.mailfilter, $HOME/.mailfilters/*, and friends&#8230;</p>
<h2>Description</h2>
<p>This manual page describes the language used by <code>maildrop</code> to filter E-mail messages. The mail filtering instructions are read from a file. The language is loosely structured, it is based on pattern matching. The language has a distinct lexical and syntactical structure, very similar to Perl&#8217;s, but it is important to note that it is not Perl, and is very different from Perl, in certain cases. If the filtering instructions do not exist, <code>maildrop</code> delivers the message to the default mailbox without doing any additional processing, making it indistinguishable from the usual mail delivery agent. It is important to note that <code>maildrop</code> reads and parses the filter file before doing anything. If there are any errors <code>maildrop</code> prints an error message, and terminates with the exit code set to <code>EX_TEMPFAIL</code>. A compliant mail transport agent should re-queue the message for a later delivery attempt. Hopefully, most simple syntax errors will not cause mail to be bounced back if the error is caught and fixed quickly.</p>
<h3>Environment</h3>
<p><code>maildrop</code> uses variables to access and manipulate messages. Variables are arbitrary text accessed by referring to the name of the variable, such as <i>HOME</i>, or <i>DEFAULT</i>. Text is placed into a variable by using an assignment statement, such as: </p>
<pre><code>FILE=&quot;IN.junk&quot;</code></pre>
<p> This statement puts the text &quot;IN.junk&quot; (without the quotes) into a variable whose name is <i>FILE</i>. Later, the contents of a variable are accessed by using the $ symbol and the name for the variable. For example:</p>
<dl>
<dd>
<pre>to $FILE</pre>
</dl>
<p> This will deliver the current message to the mailbox file (or a maildir directory) named &quot;IN.junk&quot;. <code>maildrop</code> initially creates variables from the environment variables of the operating system, UNLESS <code>maildrop</code> runs in delivery mode. Each operating system environment variable becomes a <code>maildrop</code> variable. When running in delivery mode, <code>maildrop</code> does not import the environment for security reasons, except for the environment variables that define the process locale (<i>LANG</i>, <i>LANGUAGE</i>, and <i>LC_</i><i>*</i>), which are still imported. In all cases <code>maildrop</code> resets the following variables to their default values: <i>HOME</i>, <i>DEFAULT</i>, <i>SHELL</i>, <i>PATH</i>, <i>LOCKEXT</i>, <i>LOCKREFRESH</i>, <i>LOCKSLEEP</i>, <i>LOCKTIMEOUT</i>, <i>MAILDIRQUOTA</i>, <i>SENDMAIL</i> and <i>LOGNAME</i>. There&#8217;s one exception to this rule which applies to the version of <code>maildrop</code> that comes with the m[blue]<code>Courier mail server</code>m[]<font SIZE="-2">[1]</font>. The following does not apply to the standalone version of <code>maildrop</code>: when running in delivery mode, if the <code>-d</code> flag was not used, or if it specifies the same userid as the one that&#8217;s running <code>maildrop</code>: the following variables are automatically imported from the environment: <i>HOME</i>, <i>SHELL</i>, <i>LOGNAME</i> and <i>MAILDIRQUOTA</i>. These environment variables are initialized by the Courier mail server prior to running <code>maildrop</code>. Additionally, the initial value for the <i>DEFAULT</i> maildrop variable is imported from the <i>MAILDROPDEFAULT</i> environment variable. This is because the Courier mail server overloads the DEFAULT environment variable to store the defaulted portion of the local mailbox address. See the m[blue]<code><a href="/docs/linux/man/5-dot-courier/">dot-courier</a></code>(5)m[]<font SIZE="-2">[2]</font> man page in the Courier mail server distribution. You can get the Courier mail server&#8217;s <i>DEFAULT</i> value by using the <code>import</code> command. Note, however, that this will clobber the old contents of <i>DEFAULT</i>, which is probably not what you want. The right way to do this would be something like this:</p>
<dl>
<dd>
<pre>SAVEDEFAULT=$DEFAULT
import DEFAULT
LOCALDEFAULT=$DEFAULT
DEFAULT=$SAVEDEFAULT</pre>
</dl>
<p> All internal variables are exported back as environment variables when <code>maildrop</code> runs an external command. Changes to internal variables, made by the filter file, are reflected in the exported environment.</p>
<h3>Lexical structure</h3>
<p>Most whitespace is generally ignored. The # character introduces a comment running to the end of the line, which is also ignored. Unlike other mail filters, <code>maildrop</code> parses the filter file before taking any action with the message. If there are syntax errors in the file, <code>maildrop</code> displays an error message, and returns <code>EX_TEMPFAIL</code>. That should cause the mail message to remain in the queue, and, hopefully allow the problem to be corrected, without bouncing any mail.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 In <code>maildrop</code>, the end of line is a lexical token. In order to continue a long statement on the next line, terminate the line with a backslash character.</dl>
<h3>Literal text</h3>
<p>Literal text in the <code>maildrop</code> filtering language is surrounded by either single or double quotes. In order to enter a single quote into a text literal surrounded by single quotes, or a double quote into a literal surrounded by double quotes, prefix it with a backslash character. Use two backslash characters characters to enter one backslash character in the text literal.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 A backslash followed by either a backslash, or a matching quote, is the only situation where the backslash character is actually removed, leaving only the following character in the actual text literal. If a backslash character is followed by any other character, the backslash is NOT removed.  Multiple text literals in a row are automatically concatenated, even if they use different quotes. For example:</p>
<dl>
<dd>
<pre>FOOBAR=&quot;Foo&quot;'bar'
SAVEDEFAULT=$DEFAULT
import DEFAULT
LOCALDEFAULT=$DEFAULT
DEFAULT=$SAVEDEFAULT</pre>
</dl>
<p> This sets the variable <i>FOOBAR</i> to the text &quot;Foobar&quot;.</p>
<h3>Variable substitution</h3>
<p>Variable substitution is performed on text literals that&#8217;s surrounded by double quotation marks. The &quot;$&quot; character, followed by a variable name, is replaced by that variable&#8217;s contents. MAILBOX=&quot;$HOME/Mailbox&quot; This sets the variable <i>MAILBOX</i> to the contents of the variable <i>HOME</i> followed by &quot;/Mailbox&quot;. Variable names must begin with an uppercase letter, a lowercase letter, or an underscore. Following that, all letters, digits, and underscores are taken as a variable name, and its contents replace the $ sign, and the variable name. It is possible to access variables whose name includes other characters, by using braces as follows: MAILBOX=&quot;${HOME-WORD}/Mailbox&quot; Inserts the contents of the <i>HOME-WORD</i> variable. If the variable does not exist, the empty text literal is used to replace the variable name. It is not possible to access variables whose names include the } character. If the $ character is not followed by a left brace, letter, or an underscore, the $ character remains unmolested in the text literal. A backslash followed by the $ character results in a $ character in the text literal, without doing any variable substitution. Variable substitution is not done in text literals which are surrounded by single quotes (apostrophes).</p>
<h3>Command line arguments</h3>
<p><code>maildrop</code> initializes special variables: <i>$1</i>, <i>$2</i>, and so on, with additional parameters specified on the <code>maildrop</code> command line. A filter file may use those variables just like any other variables.</p>
<h3>Predefined variables</h3>
<p>The following variables are automatically defined by <code>maildrop</code>. The default values for the following variables may be changed by the system administrator. For security reasons, the values of the following variables are always reset to their default values, and are never imported from the environment: <i>DEFAULT</i></p>
<dl>
<dd>The default mailbox to deliver the message to. If the filter file does not indicate a mailbox to deliver this message to, the message is delivered to this mailbox. The default mailbox is defined by the system administrator.</dl>
<p> <i>FROM</i></p>
<dl>
<dd>Message envelope sender. This is usually the same address as what appears in the From: header, but may not be. This information may or may not be available to <code>maildrop</code> on your system. The message envelope sender is usually specified with the <code>-f</code> option to <code>maildrop</code>. If the <code>-f</code> option is not given, <code>maildrop</code> looks for the Return-Path: header in the message. As the last resort, FROM defaults to &#8220;MAILER-DAEMON&#8221;. Note that <i>FROM</i> may be empty &#8211; the message envelope sender is empty for bounce messages.</dl>
<p> <i>HOME</i></p>
<dl>
<dd>Home directory of the user running <code>maildrop</code>.</dl>
<p> <i>HOSTNAME</i></p>
<dl>
<dd>Network name of the machine running maildrop. Obtained from <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3).</dl>
<p> <i>LOCKEXT</i></p>
<dl>
<dd>Extension for dot-lock files (default: .lock).</dl>
<p> <i>LOCKREFRESH</i></p>
<dl>
<dd>Refresh interval, in seconds, for dot-locks (default: 15). When <code>maildrop</code> dot-locks a mailbox, <code>maildrop</code> tries to refresh the lock periodically in order to keep other programs from removing a stale dot-lock. This is only required if a dot-lock exists for a prolonged period of time, which should be discouraged anyway.</dl>
<p> <i>LOCKSLEEP</i></p>
<dl>
<dd>Number of seconds to wait to try again to create a dot-lock file, if one already exists (default: 5).</dl>
<p> <i>LOCKTIMEOUT</i></p>
<dl>
<dd>Number of seconds to wait before removing a stale dot-lock file (default: 60). If a dot-lock file still exists after <i>LOCKTIMEOUT</i> seconds, <code>maildrop</code> assumes that the process holding the lock no longer exists, and the dot-lock file can be safely removed. After removing the dot-lock file, <code>maildrop</code> waits <i>LOCKSLEEP</i> seconds before trying to create its own dot-lock file, in order to avoid a race condition with another process which is also trying to remove the same stale dot-lock, at the same time.</dl>
<p> <i>LOGNAME</i></p>
<dl>
<dd>Name of the user to who the message is being delivered.</dl>
<p> <i>MAILDROP_OLD_REGEXP</i></p>
<dl>
<dd>Revert to using the old legacy pattern matching engine. Versions of <code>maildrop</code> prior to version 2.0 (included in the Courier mail server 0.51, and earlier), used a built-in pattern matching engine, instead of using the PCRE library (see the &#8220;Patterns&#8221; section). <code>maildrop</code> 1.x used a different syntax for patterns, which is no longer described in this manual page. The old pattern matching engine is still available, by setting <i>MAILDROP_OLD_REGEXP</i> to &#8220;1&#8221;. Setting this variable will use the legacy pattern matching engine for the rest of the <code>maildrop</code> recipe file. The pattern matching engine will be removed completely in a future version of maildrop. This setting provides for a transitional period of converting old recipes. <i>MAILDROP_OLD_REGEXP</i> can be set to &#8220;1&#8221; in the global maildroprc file, then reset to &#8220;0&#8221; in each individual <code>maildrop</code> recipe file, after it gets converted to the new syntax.</dl>
<p> <i>MAILFILTER</i></p>
<dl>
<dd>This is the name of the original filter file that was given to <code>maildrop</code> on the command line. This is mostly useful to -defaultfilter files, it allows them to obtain the m[blue]<code>value of the -M option</code>m[]<font SIZE="-2">[3]</font> specified on the command line.</dl>
<p> <i>PATH</i></p>
<dl>
<dd>Command execution path. <code>maildrop</code> resets PATH to the system default (usually /bin:/usr/bin:/usr/local/bin).</dl>
<p> <i>SENDMAIL</i></p>
<dl>
<dd>The mail delivery agent. When <code>maildrop</code> is instructed to deliver the message to a mailbox whose name begins with the ! character, this is interpreted as a request to forward the message. The <i>SENDMAIL</i> command is executed to forward the message.</dl>
<p> <i>SHELL</i></p>
<dl>
<dd>The login shell. The shell is used to execute all commands invoked by <code>maildrop</code>.</dl>
<p> <i>VERBOSE</i></p>
<dl>
<dd>Current Debug level (default: 0). Setting <i>VERBOSE</i> to progressive higher values, between 1 and 9, produces debugging output on standard error. <code>maildrop</code> ignores the <i>VERBOSE</i> variable in delivery mode (in order not to confuse the mail transport agent).</dl>
<p> <i>UMASK</i></p>
<dl>
<dd>The file creation mode mask, in octal. The default setting of 077 creates mailboxes that are readable and writable by the owner only. Use 007 to create mailboxes that are readable/writable by both owner and the group. Use 037 to create mailboxes that are readable by both owner and group, but writable by owner only. Permissions on existing mailboxes are not changed, this setting affects only new mailboxes. When delivering to maildirs this setting sets the permissions on new messages only. Access permissions on messages in maildirs are also affected by the permissions on the maildir directories.</dl>
<h3>Other special variables</h3>
<p>The following variables are automatically used by <code>maildrop</code> when the filter file is being processed: <i>EXITCODE</i></p>
<dl>
<dd>Return code for <code>maildrop</code>. When <code>maildrop</code> successfully delivers a message, it terminates with this exit code, which defaults to 0. When the <code>to</code> or the <code>cc</code> command is used to deliver the message to an external process, via a pipe, <code>maildrop</code> will set this variable to the exit code of the external process. Since <code>maildrop</code> immediately terminates after completing the <code>to</code> command this means that <code>maildrop</code>&#8216;s exit code will be the exit code of the external process. If the <code>to</code> command does not deliver the message to a process you must set <i>EXITCODE</i> before the <code>to</code> command, since <code>maildrop</code> terminates immediately after finishing the delivery.</dl>
<p> <i>FLAGS</i></p>
<dl>
<dd>The <i>FLAGS</i> variable is used only when delivering a message to a maildir, and may contain only the following letters: &#8220;D&#8221;, &#8220;F&#8221;, &#8220;R&#8221;, and &#8220;S&#8221;. They may appear in any order. When the message gets delivered to the maildir, the message will be marked with a draft, flag, replied, or seen, attribute, correspondingly. <i>FLAGS</i> must be set before the message is delivered to a maildir. The contents of <i>FLAGS</i> are ignored, when delivering on an mbox folder.</dl>
<p> <i>KEYWORDS</i></p>
<dl>
<dd>The <i>KEYWORDS</i> variable is used only when delivering a message to a maildir, and implements the optional IMAP keyword extension as implemented in the m[blue]<code>Courier IMAP server</code>m[]<font SIZE="-2">[1]</font>. It may be optionally initialized to contain a comma-separate list of keywords. The <code>to</code>, or the <code>cc</code> command, delivers the message to the maildir normally, but also associated the list of keywords in <i>KEYWORDS</i> with the newly delivered message. <i>KEYWORDS</i> must be set before the message is delivered to a maildir. The contents of <i>KEYWORDS</i> are ignored, when delivering on an mbox folder.</dl>
<p> <i>LINES</i></p>
<dl>
<dd>Number of lines in the current message. Note that this may be an approximation. It may or may not take into account the -A option. Use this as criteria for filtering, nothing more.</dl>
<p> <i>MAILDIRQUOTA</i></p>
<dl>
<dd>Set this variable in order to manually enforce a maximum size on ANY maildir where the message is delivered. This is an optional feature that must be enabled by the system administrator, see m[blue]<code><a href="/docs/linux/man/8-maildirquota/">maildirquota</a></code>(8)m[]<font SIZE="-2">[4]</font> for more information.</dl>
<p> <i>RETURNCODE</i></p>
<dl>
<dd>This variable is set when <code>maildrop</code> runs the m[blue]<code>xfilter</code>m[]<font SIZE="-2">[5]</font> command, or a command that&#8217;s specified within a pair of backtick characters ( command substitution ). The <i>RETURNCODE</i> variable will be set to the exit code of the command, after it completes.</dl>
<p> <i>SIZE</i></p>
<dl>
<dd>Number of bytes in the message. This may or may not include the -A option. Use this as a criteria for filtering, nothing more.</dl>
<h3>Unquoted text</h3>
<p>All text strings in filter files should be in single, or double quotes. However, for convenience sake, quotes can be omitted under certain circumstances. Text that includes ONLY letters, digits, and the following characters: _-.:/${}@ may appear without quotes. Note that this does not allow spaces, or backslashes to be entered, however the text is still variable-substituted, and the substituted text may contain other characters. Also, note that patterns (see below) begin with the slash character. Normally, anything that begins with the slash is interpreted as a pattern. However, text immediately after &#8220;VARIABLE=&#8221; is interpreted as a string even if it begins with a slash. This is why something like:</p>
<dl>
<dd>
<pre>MAILDIR=/var/mail</pre>
</dl>
<p> works as expected. Using quotes, though, is highly recommended. You must use quotes to set a variable to a lone slash, because an unquoted slash is interpreted as a division sign. Long double or singly-quoted text can be broken across multiple lines by ending the line with a lone backslash character, like this: TEXT=&quot;This is a long \<br />
text string&quot; The backslash, the newline, and all leading whitespace on the next line is removed, resulting in &quot;This is a long text string&quot;.</p>
<h3>Command substitution</h3>
<p>Text enclosed in back-tick characters is interpreted as a shell command. The shell command is executed as a child process by <code>maildrop</code>. Its output is used in place of the command. For example:</p>
<dl>
<dd>
<pre>DIR=`ls`</pre>
</dl>
<p> places the names of the files in the current directory into the DIR variable. The output of the command will have all newline characters replaced by spaces, and leading and trailing spaces will be stripped (multiple spaces are not removed, though). Also, the contents of the message being delivered is made available to the command on standard input.</p>
<h3>Patterns</h3>
<p>The pattern syntax in <code>maildrop</code> is similar to the <code>grep</code> command&#8217;s syntax, with some minor differences. A pattern takes the following form in the filter file:</p>
<dl>
<dd>
<pre>/<i>pattern</i>/:<i>options</i></pre>
</dl>
<p> <i>pattern</i> specifies the text to look for in the message, in the UTF-8 codeset. <i>pattern</i> must not begin with a space, otherwise the leading slash will then be interpreted as a division sign. If you must search for text that starts with a space, use something like &quot;/[ ] &#8230; /&quot;. The general syntax of <code>maildrop</code>&#8216;s patterns is described in the <code><a href="/docs/linux/man/3-pcrepattern/">pcrepattern</a></code>(3) manual page, with certain exceptions noted below. <code>maildrop</code> uses the m[blue]<code>PCRE</code>m[]<font SIZE="-2">[6]</font> library to implement pattern matching. Not all features in PCRE are available in <code>maildrop</code>, and the &#8220;options&#8221; part, which follows the pattern specification, changes the pattern matching further. Consult the <code><a href="/docs/linux/man/3-pcrepattern/">pcrepattern</a></code>(3) manual page for more information, but note the following exceptions:</p>
<dl>
<dd>&bull; Internal options settings are not supported (but see the &#8220;D&#8221; maildrop option, below). Do not include option settings in the <i>pattern</i>, doing so will lead to undefined results.</dl>
<dl>
<dd>&bull; Named subpatterns are not implemented. Numbered subpatterns are implemented, see &#8220;Pattern Match Results&#8221;, below.</dl>
<dl>
<dd>&bull; The search pattern gets executed not against the raw message text, but the message transcoded into a canonical UTF-8-based format. This process involves transcoding any non-UTF-8 message content into UTF-8. Additionally, message headers get converted into a canonical format before the search pattern gets executed. For structured headers with email addresses, the process involves removing extraneous punctuation, or adding missing ones (in situations where a missing punctuation character can be deduced). Additionally certain pre-RFC822 obsolete header formats get converted to canonical form. This means that header search patterns that include punctuation character may appear not to work against obviously-matching message text. Use &#8220;reformime -u &lt;message.txt&#8221;, with message.txt containing the sample message, to see exactly the actual text that gets searched by patterns.</dl>
<h3>Pattern options</h3>
<p>Following /<i>pattern</i>/, there may be an optional colon, followed by one. or more options. The following options may be specified in any order: h</p>
<dl>
<dd>Match this pattern against the message header.</dl>
<p> b</p>
<dl>
<dd>Match this pattern against the message body.</dl>
<p> D</p>
<dl>
<dd>This is a case sensitive match. Normally the patterns match either uppercase or lowercase text. /john/ will match &quot;John&quot;, &quot;john&quot;, or &quot;JOHN&quot;. Specify the D option for a case-sensitive search: lowercase letters in the pattern must match lowercase letters in the message; ditto for uppercase.</dl>
<p> If neither &#8216;h&#8217; or &#8216;b&#8217; is specified, the pattern is matched against the header only. Specifying the &#8216;b&#8217; option causes the pattern to be matched against the message body. Specifying both causes the pattern to be matched against the entire message. Normally, each line in the message gets matched against the pattern individually. When applying patterns to a header, multi-line headers (headers split on several lines by beginning each continuation line with whitespace) are silently combined into a single line, before the pattern is applied.</p>
<h3>MIME encoding</h3>
<p>The pattern must be a valid text string in the UTF-8 codeset, and <code>maildrop</code> should handle messages that use MIME encodings in other known character sets. Options that specify a message header search result in <code>maildrop</code> searching the initial message headers, and any headers of additional MIME sections, in a multipart MIME message. Options that specify a message body search will search through all &quot;text&quot; MIME content. For a MIME search to succeed, the message must be a well-formed MIME message (with a Mime-Version: 1.0 header).</p>
<h3>Weighted scoring</h3>
<p>Patterns are evaluated by <code>maildrop</code> as any other numerical expression. If a pattern is found, <code>maildrop</code>&#8216;s filter interprets the results of the pattern match as number 1, or true, for filtering purposes. If a pattern is not found the results of the pattern search is zero. Once a pattern is found, the search stops. Second, and subsequent occurrences of the same pattern are NOT searched for. <code>maildrop</code> can also do weighted scoring. In weighted scoring, multiple occurrences of the same pattern are used to calculate a numerical score. To use a weighted search, specify the pattern as follows:</p>
<dl>
<dd>
<pre>/<i>pattern</i>/:<i>options</i>,<i>xxx</i>,<i>yyy</i></pre>
</dl>
<p> where <i>xxx</i> and <i>yyy</i> are two numbers. <i>yyy</i> is optional &#8212; it will default to 1, if missing. The first occurrence of the pattern is evaluated as xxx. The second occurrence of the pattern is evaluated as xxx*yyy, the third as xxx*yyy*yyy, etc&#8230; All occurrences of the pattern are added up to calculate the final score.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 <code>maildrop</code> does not recognize multiple occurrences of the same pattern in the same line. Multiple occurences of the same pattern in one line count as one occurence.</dl>
<h3>Pattern Match Results</h3>
<p>After a pattern is successfully matched, the actual text that is matched is placed in the <i>MATCH</i> variable. For example:</p>
<dl>
<dd>
<pre>/^From:.*/</pre>
</dl>
<p> matches a line of the form:</p>
<dl>
<dd>
<pre>From: postmaster [at] localhost</pre>
</dl>
<p> Here the variable <i>MATCH</i> will be set to &quot;From: postmaster [at] localhost&quot;, which can be used in subsequent statements. If the pattern contains subpatterns, the portions of the text that match the first subpattern is placed in the <i>MATCH1</i> variable. The second subpattern, if any, is placed in <i>MATCH2</i>, and so on:</p>
<dl>
<dd>
<pre>/^From:\s+(.*)@(.*)/</pre>
</dl>
<p> matched against the same line will set <i>MATCH</i> to &#8220;From: postmaster [at] localhost&#8221;, <i>MATCH1</i> to &#8220;postmaster&#8221;, and <i>MATCH2</i> to &#8220;localhost&#8221;. Of course, in real world the &#8220;From:&#8221; header is usually much more complicated, and can&#8217;t be handled that easily. This is just an illustrative example.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Subpatterns are not processed in the foreach statement.</dl>
<h3>Conversion of maildrop 1.x patterns to 2.0</h3>
<p>Although the new PCRE-based pattern matching code in <code>maildrop</code> is completely different from the built-in pattern matching code in <code>maildrop</code> 1.x, very few changes will be required to convert recipes to the new syntax. The only major differences are:</p>
<dl>
<dd>&bull; The subexpression format has changed. Any pattern that uses subexpression needs to be converted. Additionally, references to <i>MATCH2</i> must be replaced with <i>MATCH1</i>, <i>MATCH3</i> to <i>MATCH2</i>, and so on. References to plain old <i>MATCH</i> will remain the same.</dl>
<dl>
<dd>&bull; The &#8220;w&#8221; pattern option is no longer possible, with PCRE. The very few recipes that use this option, if any actually exist, will have to be rewritten in some other fashion.</dl>
<h3>Expressions</h3>
<p>Although <code>maildrop</code> evaluates expressions numerically, results of expressions are stored as text literals. When necessary, text literals are converted to numbers, then the results of a mathematical operation is converted back into a text literal.<br />
 <font SIZE="+1"> <code>Operators</code></p>
<dl>
<dd>The following operators carry their usual meaning, and are listed in order from lowest precedence, to the highest:</p>
<dl>
<dd></font></p>
<pre>||
&amp;&amp;
&lt; &lt;= &gt; &gt;= == != lt le gt ge eq ne
|
&amp;
+ -
* /
=~ /<i>pattern</i>/
/<i>pattern</i>/ ! ~ <i>function()</i></pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Variable assignment</code></p>
<dl>
<dd>
<dl>
<dd></font></p>
<pre>VARIABLE=<i>expression</i></pre>
</dl>
<p> Assigns the result of the expression to <i>VARIABLE</i> (note no leading $ in front of variable).</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If <i>VARIABLE</i> is NOT surrounded by quotes, then it may contain only letters, numbers, underscores, dashes, and a selected few other characters. In order to initialize a variable whose name contains non-standard punctuation marks, surround the name of the variable with quotes.<br />
 <font SIZE="+1"> <code>cc &#8211; deliver a copy of the message</code></p>
<dl>
<dd>
<dl>
<dd></font></p>
<pre>cc <i>expression</i></pre>
</dl>
<p> The <code>cc</code> statement is very similar to the <code>to</code> statement, except that after delivering the message <code>maildrop</code> continues to process the filter file, unlike the <code>to</code> statement which immediately terminates <code>maildrop</code> after the delivery is complete. Essentially, the message is carbon copied to the given mailbox, and may be delivered again to another mailbox by another <code>cc</code> or <code>to</code> statement. m[blue]<code>See the to</code> statementm[]<font SIZE="-2">[7]</font> for more details. When <code>cc</code> is used to deliver a message to a process <code>maildrop</code> will set the <i>EXITCODE</i> variable to the process&#8217;s exit code.</dl>
<p> <font SIZE="+1"> <code>dotlock &#8211; create a manual dot-lock</code></p>
<dl>
<dd>
<dl>
<dd></font></p>
<pre>dotlock <i>expression</i> {
 ...
}</pre>
</dl>
<p> <code>maildrop</code> automatically creates a lock when a message is delivered to a mailbox. Depending upon your system configuration, <code>maildrop</code> will use either dot-locks, or the flock() system call. The <code>dotlock</code> statement creates an explicit dot-lock file. Use the m[blue]<code>flock</code> statementm[]<font SIZE="-2">[8]</font> to create an explicit flock() lock. The <i>expression</i> is a filename that should be used as a lock file. <code>maildrop</code> creates the indicated dot-lock, executes the filtering instructions contained within the { &#8230; } block, and removes the lock. The expression <i>must</i> be the name of the dot-lock file itself, <i>NOT</i> the name of the mailbox file you want to lock.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 With manual locking, it is possible to deadlock multiple <code>maildrop</code> processes (or any other processes that try to claim the same locks). No deadlock detection is possible with dot-locks, and since <code>maildrop</code> automatically refreshes all of its dot-locks regularly, they will never go stale. You&#8217;ll have <code>maildrop</code> processes hanging in limbo, until their watchdog timers go off, aborting the mail delivery.<br />
 <font SIZE="+1"> <code>echo &#8211; output diagnostic information</code></p>
<dl>
<dd>
<dl>
<dd></font></p>
<pre>echo <i>expression</i></pre>
</dl>
<p> <code>maildrop</code> will print the given text. This is usually used when <code>maildrop</code> runs in embedded mode, but can be used for debugging purposes. Normally, a newline is printed after the text. If text is terminated with a 
