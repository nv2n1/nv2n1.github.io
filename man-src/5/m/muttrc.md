---
title: "muttrc(5)"
name: "muttrc"
section: "5"
letter: "m"
url: "/docs/linux/man/5-muttrc/"
description: "muttrc – Configuration file for the Mutt Mail User Agent"
---

<p>muttrc &#8211; Configuration file for the Mutt Mail User Agent</p>
<h2>Description</h2>
<p>A mutt configuration file consists of a series of &#8220;commands&#8221;. Each line of the file may contain one or more commands. When multiple commands are used, they must be separated by a semicolon (&#8220;<code>;</code>&#8220;). The hash mark, or pound sign (&#8220;<code>#</code>&#8220;), is used as a &#8220;comment&#8221; character. You can use it to annotate your initialization file. All text after the comment character to the end of the line is ignored. Single quotes (&#8220;<code>&#8216;</code>&#8220;) and double quotes (&#8220;<code>&quot;</code>&#8220;) can be used to quote strings which contain spaces or other special characters. The difference between the two types of quotes is similar to that of many popular shell programs, namely that a single quote is used to specify a literal string (one that is not interpreted for shell variables or quoting with a backslash [see next paragraph]), while double quotes indicate a string which should be evaluated. For example, backticks are evaluated inside of double quotes, but not single quotes. <code>\</code> quotes the next character, just as in shells such as bash and zsh. For example, if want to put quotes (&#8220;<code>&quot;</code>&#8220;) inside of a string, you can use &#8220;<code>\</code>&#8221; to force the next character to be a literal instead of interpreted character. &#8220;<code>\</code>&#8221; means to insert a literal &#8220;<code>\</code>&#8221; into the line. &#8220;<code>
</code>&#8221; and &#8220;<code></code>&#8221; have their usual C meanings of linefeed and carriage-return, respectively. A &#8220;<code>\</code>&#8221; at the end of a line can be used to split commands over multiple lines, provided that the split points don&#8217;t appear in the middle of command names. It is also possible to substitute the output of a Unix command in an initialization file. This is accomplished by enclosing the command in backticks (<code>`</code><i>command</i><code>`</code>). UNIX environment variables can be accessed like the way it is done in shells like sh and bash: Prepend the name of the variable by a dollar (&#8220;<code>$</code>&#8220;) sign. </p>
<h2>Commands</h2>
<pre><code>alias</code> [<code>-group</code> <i>name</i> [...]] <i>key</i> <i>address</i> [<code>,</code> <i>address</i> [ ... ]]
<code>unalias</code> [<code> * </code> | <i>key</i> ]</pre>
<dl>
<dd><code>alias</code> defines an alias <i>key</i> for the given addresses. Each <i>address</i> will be resolved into either an email address (user [at] example.com) or a named email address (User Name &lt;user [at] example.com&gt;). The address may be specified in either format, or in the format &#8220;user [at] example.com (User Name)&#8221;. <code>unalias</code> removes the alias corresponding to the given <i>key</i> or all aliases when &#8220;<code>*</code>&#8221; is used as an argument. The optional <code>-group</code> argument to <code>alias</code> causes the aliased address(es) to be added to the named <i>group</i>.</dl>
<pre><code>group</code> [<code>-group</code> <i>name</i>] [<code>-rx</code> <i>EXPR</i> [ <i>...</i> ]] [<code>-addr</code> <i>address</i> [ <i>...</i> ]]
<code>ungroup</code> [<code>-group</code> <i>name</i> ] [ <code>*</code> | [[<code>-rx</code> <i>EXPR</i> [ <i>...</i> ]] [<code>-addr</code> <i>address</i> [ <i>...</i> ]]]</pre>
<dl>
<dd><code>group</code> is used to directly add either addresses or regular expressions to the specified group or groups. The different categories of arguments to the <code>group</code> command can be in any order. The flags <i>-rx</i> and <i>-addr</i> specify what the following strings (that cannot begin with a hyphen) should be interpreted as: either a regular expression or an email address, respectively. <code>ungroup</code> is used to remove addresses or regular expressions from the specified group or groups. The syntax is similar to the <code>group</code> command, however the special character <code>*</code> can be used to empty a group of all of its contents.</p>
<dd>These address groups can also be created implicitly by the <code>alias</code>, <code>lists</code>, <code>subscribe</code> and <code>alternates</code> commands by specifying the optional <i>-group</i> option.</p>
<dd>Once defined, these address groups can be used in patterns to search for and limit the display to messages matching a group.</dl>
<pre><code>alternates</code> [<code>-group</code> <i>name</i>] <i>regexp</i> [ <i>regexp</i> [ ... ]]
<code>unalternates</code> [<code> * </code> | <i>regexp</i> [ <i>regexp</i> [ ... ]] ]</pre>
<dl>
<dd><code>alternates</code> is used to inform mutt about alternate addresses where you receive mail; you can use regular expressions to specify alternate addresses. This affects mutt&#8217;s idea about messages from you, and messages addressed to you. <code>unalternates</code> removes a regular expression from the list of known alternates. The <code>-group</code> flag causes all of the subsequent regular expressions to be added to the named group.</dl>
<pre><code>alternative_order</code> <i>type</i>[<code>/</code><i>subtype</i>] [ ... ]
<code>unalternative_order</code> [<code> * </code> | <i>type</i>/<i>subtype</i>] [...]</pre>
<dl>
<dd><code>alternative_order</code> command permits you to define an order of preference which is used by mutt to determine which part of a <code>multipart/alternative</code> body to display. A subtype of &#8220;<code>*</code>&#8221; matches any subtype, as does an empty subtype. <code>unalternative_order</code> removes entries from the ordered list or deletes the entire list when &#8220;<code>*</code>&#8221; is used as an argument.</dl>
<pre><code>auto_view</code> <i>type</i>[<code>/</code><i>subtype</i>] [ ... ]
<code>unauto_view</code> <i>type</i>[<code>/</code><i>subtype</i>] [ ... ]</pre>
<dl>
<dd>This commands permits you to specify that mutt should automatically convert the given MIME types to text/plain when displaying messages. For this to work, there must be a <code><a href="/docs/linux/man/5-mailcap/">mailcap</a></code>(5) entry for the given MIME type with the <code>copiousoutput</code> flag set. A subtype of &#8220;<code>*</code>&#8221; matches any subtype, as does an empty subtype.</dl>
<pre><code>mime_lookup</code> <i>type</i>[<code>/</code><i>subtype</i>] [ ... ]
<code>unmime_lookup</code> <i>type</i>[<code>/</code><i>subtype</i>] [ ... ]</pre>
<dl>
<dd>This command permits you to define a list of &quot;data&quot; MIME content types for which mutt will try to determine the actual file type from the file name, and not use a <code><a href="/docs/linux/man/5-mailcap/">mailcap</a></code>(5) entry given for the original MIME type. For instance, you may add the <code>application/octet-stream</code> MIME type to this list.</p>
<dt><code>bind</code> <i>map1,map2,&#8230;</i> <i>key</i> <i>function</i></p>
<dd>This command binds the given <i>key</i> for the given <i>map</i> or maps to the given <i>function</i>. Multiple maps may be specified by separating them with commas (no whitespace is allowed).</p>
<dd>Valid maps are: <code>generic</code>, <code>alias</code>, <code>attach</code>, <code>browser</code>, <code>editor</code>, <code>index</code>, <code>compose</code>, <code>pager</code>, <code>pgp</code>, <code>postpone</code>, <code>mix</code>.</p>
<dd>For more information on keys and functions, please consult the Mutt Manual. Note that the function name is to be specified without angle brackets.</p>
<dt><code>account-hook</code> [<code>!</code>]<i>regexp</i> <i>command</i></p>
<dd>This hook is executed whenever you access a remote mailbox. Useful to adjust configuration settings to different IMAP or POP servers.</p>
<dt><code>charset-hook</code> <i>alias</i> <i>charset</i></p>
<dd>This command defines an alias for a character set. This is useful to properly display messages which are tagged with a character set name not known to mutt.</p>
<dt><code>iconv-hook</code> <i>charset</i> <i>local-charset</i></p>
<dd>This command defines a system-specific name for a character set. This is useful when your system&#8217;s <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) implementation does not understand MIME character set names (such as <code>iso-8859-1</code>), but instead insists on being fed with implementation-specific character set names (such as <code>8859-1</code>). In this specific case, you&#8217;d put this into your configuration file:</p>
<dd><code>iconv-hook iso-8859-1 8859-1</code></p>
<dt><code>message-hook</code> [<code>!</code>]<i>pattern</i> <i>command</i></p>
<dd>Before mutt displays (or formats for replying or forwarding) a message which matches the given <i>pattern</i> (or, when it is preceded by an exclamation mark, does not match the <i>pattern</i>), the given <i>command</i> is executed. When multiple <code>message-hook</code>s match, they are executed in the order in which they occur in the configuration file.</p>
<dt><code>folder-hook</code> [<code>!</code>]<i>regexp</i> <i>command</i></p>
<dd>When mutt enters a folder which matches <i>regexp</i> (or, when <i>regexp</i> is preceded by an exclamation mark, does not match <i>regexp</i>), the given <i>command</i> is executed.</p>
<dd>When several <code>folder-hook</code>s match a given mail folder, they are executed in the order given in the configuration file.</p>
<dt><code>macro</code> <i>map</i> <i>key</i> <i>sequence</i> [ <i>description</i> ]</p>
<dd>This command binds the given <i>sequence</i> of keys to the given <i>key</i> in the given <i>map</i> or maps. For valid maps, see <code>bind</code>. To specify multiple maps, put only a comma between the maps.</dl>
<pre><code>color</code> <i>object</i> [ <i>attribute</i> ... ] <i>foreground</i> <i>background</i> [ <i>regexp</i> ]
<code>color</code> index [ <i>attribute</i> ... ] <i>foreground</i> <i>background</i> [ <i>pattern</i> ]
<code>color</code> compose <i>composeobject</i> [ <i>attribute</i> ... ] <i>foreground</i> <i>background</i>
<code>uncolor</code> index <i>pattern</i> [ <i>pattern</i> ... ]</pre>
<dl>
<dd>If your terminal supports color, these commands can be used to assign <i>foreground</i>/<i>background</i> combinations to certain objects. Valid objects are: <code>attachment</code>, <code>body</code>, <code>bold</code>, <code>error</code>, <code>header</code>, <code>hdrdefault</code>, <code>index</code>, <code>indicator</code>, <code>markers</code>, <code>message</code>, <code>normal</code>, <code>prompt</code>, <code>quoted</code>, <code>quoted</code><i>N</i>, <code>search</code>, <code>signature</code>, <code>status</code>, <code>tilde</code>, <code>tree</code>, <code>underline</code>. If the sidebar is enabled the following objects are also valid: <code>sidebar_divider</code>, <code>sidebar_flagged</code>, <code>sidebar_highlight</code>, <code>sidebar_indicator</code>, <code>sidebar_new</code>, <code>sidebar_spoolfile</code>. The <code>body</code> and <code>header</code> objects allow you to restrict the colorization to a regular expression. The <code>index</code> object permits you to select colored messages by pattern.</p>
<dd>Valid composeobjects include <code>header</code>, <code>security_encrypt</code>, <code>security_sign</code>, <code>security_both</code>, <code>security_none</code>.</p>
<dd>Valid colors include: <code>white</code>, <code>black</code>, <code>green</code>, <code>magenta</code>, <code>blue</code>, <code>cyan</code>, <code>yellow</code>, <code>red</code>, <code>default</code>, <code>color</code><i>N</i>.</p>
<dd>Valid attributes include: <code>none</code>, <code>bold</code>, <code>underline</code>, <code>reverse</code>, and <code>standout</code>.</dl>
<pre><code>mono</code> <i>object</i> <i>attribute</i> [ <i>regexp</i> ]
<code>mono</code> index <i>attribute</i> [ <i>pattern</i> ]</pre>
<dl>
<dd>For terminals which don&#8217;t support color, you can still assign attributes to objects.</p>
<dt>[<code>un</code>]<code>ignore</code> <i>pattern</i> [ <i>pattern</i> &#8230; ]</p>
<dd>The <code>ignore</code> command permits you to specify header fields which you usually don&#8217;t wish to see. Any header field whose tag <i>begins</i> with an &#8220;ignored&#8221; pattern will be ignored.</p>
<dd>The <code>unignore</code> command permits you to define exceptions from the above mentioned list of ignored headers.</dl>
<pre><code>lists</code> [<code>-group</code> <i>name</i>] <i>regexp</i> [ <i>regexp</i> ... ]
<code>unlists</code> <i>regexp</i> [ <i>regexp</i> ... ]
<code>subscribe</code> [<code>-group</code> <i>name</i>] <i>regexp</i> [ <i>regexp</i> ... ]
<code>unsubscribe</code> <i>regexp</i> [ <i>regexp</i> ... ]</pre>
<dl>
<dd>Mutt maintains two lists of mailing list address patterns, a list of subscribed mailing lists, and a list of known mailing lists. All subscribed mailing lists are known. Patterns use regular expressions.</p>
<dd>The <code>lists</code> command adds a mailing list address to the list of known mailing lists. The <code>unlists</code> command removes a mailing list from the lists of known and subscribed mailing lists. The <code>subscribe</code> command adds a mailing list to the lists of known and subscribed mailing lists. The <code>unsubscribe</code> command removes it from the list of subscribed mailing lists. The <code>-group</code> flag adds all of the subsequent regular expressions to the named group.</p>
<dt><code>mbox-hook</code> [<code>!</code>]<i>regexp</i> <i>mailbox</i></p>
<dd>When mutt changes to a mail folder which matches <i>regexp</i>, <i>mailbox</i> will be used as the &#8220;mbox&#8221; folder, i.e., read messages will be moved to that folder when the mail folder is left.</p>
<dd>The first matching <code>mbox-hook</code> applies.</dl>
<pre><code>mailboxes</code> <i>filename</i> [ <i>filename</i> ... ]
<code>unmailboxes</code> [ <code>*</code> | <i>filename</i> ... ]</pre>
<dl>
<dd>The <code>mailboxes</code> specifies folders which can receive mail and which will be checked for new messages. When changing folders, pressing space will cycle through folders with new mail. The <code>unmailboxes</code> command is used to remove a file name from the list of folders which can receive mail. If &quot;<code>*</code>&quot; is specified as the file name, the list is emptied.</dl>
<pre><code>my_hdr</code> <i>string</i>
<code>unmy_hdr</code> <i>field</i></pre>
<dl>
<dd>Using <code>my_hdr</code>, you can define headers which will be added to the messages you compose. <code>unmy_hdr</code> will remove the given user-defined headers.</p>
<dt><code>hdr_order</code> <i>header1</i> <i>header2</i> [ &#8230; ]</p>
<dd>With this command, you can specify an order in which mutt will attempt to present headers to you when viewing messages.</p>
<dt><code>save-hook</code> [<code>!</code>]<i>pattern</i> <i>filename</i></p>
<dd>When a message matches <i>pattern</i>, the default file name when saving it will be the given <i>filename</i>.</p>
<dt><code>fcc-hook</code> [<code>!</code>]<i>pattern</i> <i>filename</i></p>
<dd>When an outgoing message matches <i>pattern</i>, the default file name for storing a copy (fcc) will be the given <i>filename</i>.</p>
<dt><code>fcc-save-hook</code> [<code>!</code>]<i>pattern</i> <i>filename</i></p>
<dd>This command is an abbreviation for identical <code>fcc-hook</code> and <code>save-hook</code> commands.</p>
<dt><code>send-hook</code> [<code>!</code>]<i>pattern</i> <i>command</i></p>
<dd>When composing a message matching <i>pattern</i>, <i>command</i> is executed. When multiple <code>send-hook</code>s match, they are executed in the order in which they occur in the configuration file.</p>
<dt><code>send2-hook</code> [<code>!</code>]<i>pattern</i> <i>command</i></p>
<dd>Whenever a message matching <i>pattern</i> is changed (either by editing it or by using the compose menu), <i>command</i> is executed. When multiple <code>send2-hook</code>s match, they are executed in the order in which they occur in the configuration file. Possible applications include setting the $sendmail variable when a message&#8217;s from header is changed.</p>
<dd><code>send2-hook</code> execution is not triggered by use of <code>enter-command</code> from the compose menu.</p>
<dt><code>reply-hook</code> [<code>!</code>]<i>pattern</i> <i>command</i></p>
<dd>When replying to a message matching <i>pattern</i>, <i>command</i> is executed. When multiple <code>reply-hook</code>s match, they are executed in the order in which they occur in the configuration file, but all <code>reply-hook</code>s are matched and executed before <code>send-hook</code>s, regardless of their order in the configuration file.</p>
<dt><code>crypt-hook</code> <i>regexp</i> <i>key-id</i></p>
<dd>The crypt-hook command provides a method by which you can specify the ID of the public key to be used when encrypting messages to a certain recipient. The meaning of &quot;key ID&quot; is to be taken broadly: This can be a different e-mail address, a numerical key ID, or even just an arbitrary search string. You may use multiple <code>crypt-hook</code>s with the same <i>regexp</i>; multiple matching <code>crypt-hook</code>s result in the use of multiple <i>key-id</i>s for a recipient.</p>
<dt><code>index-format-hook</code> <i>name</i> [<code>!</code>]<i>pattern</i> <i>format-string</i></p>
<dd>This command is used to inject format strings dynamically into $index_format based on pattern matching against the current message.</p>
<dd>The $index_format expando <i>%@name@</i> specifies a placeholder for the injection. Index-format-hooks with the same <i>name</i> are matched using <i>pattern</i> against the current message. Matching is done in the order specified in the .muttrc, with the first match being used. The hook&#8217;s <i>format-string</i> is then substituted and evaluated.</dl>
<pre><code>open-hook</code> <i>regexp</i> &quot;<i>command</i>&quot;
<code>close-hook</code> <i>regexp</i> &quot;<i>command</i>&quot;
<code>append-hook</code> <i>regexp</i> &quot;<i>command</i>&quot;</pre>
<dl>
<dd>These commands provide a way to handle compressed folders. The given <code>regexp</code> specifies which folders are taken as compressed (e.g. &quot;<i>\.gz$</i>&quot;). The commands tell Mutt how to uncompress a folder (<code>open-hook</code>), compress a folder (<code>close-hook</code>) or append a compressed mail to a compressed folder (<code>append-hook</code>). The <i>command</i> string is the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) like format string, and it should accept two parameters: <code>%f</code>, which is replaced with the (compressed) folder name, and <code>%t</code> which is replaced with the name of the temporary folder to which to write.</p>
<dt><code>push</code> <i>string</i></p>
<dd>This command adds the named <i>string</i> to the keyboard buffer.</dl>
<pre><code>set</code> [<code>no</code>|<code>inv</code>|<code>&amp;</code>|<code>?</code>]<i>variable</i>[=<i>value</i>] [ ... ]
<code>toggle</code> <i>variable</i> [ ... ]
<code>unset</code> <i>variable</i> [ ... ]
<code>reset</code> <i>variable</i> [ ... ]</pre>
<dl>
<dd>These commands are used to set and manipulate configuration variables.</p>
<dd>Mutt knows four basic types of variables: boolean, number, string and quadoption. Boolean variables can be <code>set</code> (true), <code>unset</code> (false), or <code>toggle</code>d. Number variables can be assigned a positive integer value.</p>
<dd>String variables consist of any number of printable characters. Strings must be enclosed in quotes if they contain spaces or tabs. You may also use the &#8220;C&#8221; escape sequences <code>
</code> and <code>	</code> for newline and tab, respectively.</p>
<dd>Quadoption variables are used to control whether or not to be prompted for certain actions, or to specify a default action. A value of <code>yes</code> will cause the action to be carried out automatically as if you had answered yes to the question. Similarly, a value of <code>no</code> will cause the the action to be carried out as if you had answered &#8220;no.&#8221; A value of <code>ask-yes</code> will cause a prompt with a default answer of &#8220;yes&#8221; and <code>ask-no</code> will provide a default answer of &#8220;no.&#8221;</p>
<dd>The <code>reset</code> command resets all given variables to the compile time defaults. If you reset the special variable <code>all</code>, all variables will reset to their compile time defaults.</p>
<dt><code>source</code> <i>filename</i></p>
<dd>The given file will be evaluated as a configuration file.</dl>
<pre><code>spam</code> <i>pattern</i> <i>format</i>
<code>nospam</code> <i>pattern</i></pre>
<dl>
<dd>These commands define spam-detection patterns from external spam filters, so that mutt can sort, limit, and search on &#8220;spam tags&#8221; or &#8220;spam attributes&#8221;, or display them in the index. See the Mutt manual for details.</dl>
<pre><code>subjectrx</code> <i>pattern</i> <i>replacement</i>
<code>unsubjectrx</code> [ <code>*</code> | <i>pattern</i> ]</pre>
<dl>
<dd><code>subjectrx</code> specifies a regular expression <i>pattern</i> which, if detected in a message subject, causes the subject to be replaced with the <i>replacement</i> value. The <i>replacement</i> is subject to substitutions in the same way as for the <code>spam</code> command: %L for the text to the left of the match, %R for text to the right of the match, and %1 for the first subgroup in the match (etc). If you simply want to erase the match, set it to &#8220;%L%R&#8221;. Any number of <code>subjectrx</code> commands may coexist.</p>
<dd>Note this well: the <i>replacement</i> value replaces the entire subject, not just the match!</p>
<dd><code>unsubjectrx</code> removes a given <code>subjectrx</code> from the substitution list. If <code>*</code> is used as the pattern, all substitutions will be removed.</p>
<dt><code>unhook</code> [<code> * </code> | <i>hook-type</i> ]</p>
<dd>This command will remove all hooks of a given type, or all hooks when &#8220;<code>*</code>&#8221; is used as an argument. <i>hook-type</i> can be any of the <code>-hook</code> commands documented above.</dl>
<pre><code>mailto_allow</code> <i>header-field</i> [ ... ]
<code>unmailto_allow</code> [ <code>*</code> | <i>header-field</i> ... ]</pre>
<dl>
<dd>These commands allow the user to modify the list of allowed header fields in a <i>mailto:</i> URL that Mutt will include in the the generated message. By default the list contains only <code>subject</code> and <code>body</code>, as specified by RFC2368.</p>
<dt><code>echo</code> <i>message</i></p>
<dd>Prints <i>message</i> to the message window. After printing the message, echo will pause for the number of seconds specified by $sleep_time.</dl>
<h2>Patterns</h2>
<p>In various places with mutt, including some of the above mentioned <code>hook</code> commands, you can specify patterns to match messages.</p>
<h3>Constructing Patterns</h3>
<p>A simple pattern consists of an operator of the form &#8220;<code>~</code><i>character</i>&#8220;, possibly followed by a parameter against which mutt is supposed to match the object specified by this operator. For some <i>character</i>s, the <code>~</code> may be replaced by another character to alter the behavior of the match. These are described in the list of operators, below. </p>
<p> With some of these operators, the object to be matched consists of several e-mail addresses. In these cases, the object is matched if at least one of these e-mail addresses matches. You can prepend a hat (&#8220;<code>^</code>&#8220;) character to such a pattern to indicate that <i>all</i> addresses must match in order to match the object. </p>
<p> You can construct complex patterns by combining simple patterns with logical operators. Logical AND is specified by simply concatenating two simple patterns, for instance &#8220;~C mutt-dev ~s bug&#8221;. Logical OR is specified by inserting a vertical bar (&#8220;<code>|</code>&#8220;) between two patterns, for instance &#8220;~C mutt-dev | ~s bug&#8221;. Additionally, you can negate a pattern by prepending a bang (&#8220;<code>!</code>&#8220;) character. For logical grouping, use braces (&#8220;()&#8221;). Example: &#8220;!(~t mutt|~c mutt) ~f elkins&#8221;.</p>
<h3>Simple Patterns</h3>
<p>Mutt understands the following simple patterns: </p>
<dl>
<dt>~A</p>
<dd>all messages</p>
<dt>~b <i>EXPR</i></p>
<dd>messages which contain <i>EXPR</i> in the message body.</p>
<dt>=b <i>STRING</i></p>
<dd>If IMAP is enabled, like ~b but searches for <i>STRING</i> on the server, rather than downloading each message and searching it locally.</p>
<dt>~B <i>EXPR</i></p>
<dd>messages which contain <i>EXPR</i> in the whole message.</p>
<dt>=B <i>STRING</i></p>
<dd>If IMAP is enabled, like ~B but searches for <i>STRING</i> on the server, rather than downloading each message and searching it locally.</p>
<dt>~c <i>EXPR</i></p>
<dd>messages carbon-copied to <i>EXPR</i></p>
<dt>%c <i>GROUP</i></p>
<dd>messages carbon-copied to any member of <i>GROUP</i></p>
<dt>~C <i>EXPR</i></p>
<dd>messages either to: or cc: <i>EXPR</i></p>
<dt>%C <i>GROUP</i></p>
<dd>messages either to: or cc: to any member of <i>GROUP</i></p>
<dt>~d <i>MIN</i>&#8211;<i>MAX</i></p>
<dd>messages with &#8220;date-sent&#8221; in a Date range</p>
<dt>~D</p>
<dd>deleted messages</p>
<dt>~e <i>EXPR</i></p>
<dd>messages which contain <i>EXPR</i> in the &#8220;Sender&#8221; field</p>
<dt>%e <i>GROUP</i></p>
<dd>messages which contain a member of <i>GROUP</i> in the &#8220;Sender&#8221; field</p>
<dt>~E</p>
<dd>expired messages</p>
<dt>~f <i>EXPR</i></p>
<dd>messages originating from <i>EXPR</i></p>
<dt>%f <i>GROUP</i></p>
<dd>messages originating from any member of <i>GROUP</i></p>
<dt>~F</p>
<dd>flagged messages</p>
<dt>~g</p>
<dd>PGP signed messages</p>
<dt>~G</p>
<dd>PGP encrypted messages</p>
<dt>~h <i>EXPR</i></p>
<dd>messages which contain <i>EXPR</i> in the message header</p>
<dt>=h <i>STRING</i></p>
<dd>If IMAP is enabled, like ~h but searches for <i>STRING</i> on the server, rather than downloading each message and searching it locally. <i>STRING</i> must be of the form &#8220;header: substring&#8221;</p>
<dt>~H <i>EXPR</i></p>
<dd>messages with spam tags matching <i>EXPR</i></p>
<dt>~i <i>EXPR</i></p>
<dd>messages which match <i>EXPR</i> in the &#8220;Message-ID&#8221; field</p>
<dt>~k</p>
<dd>messages containing PGP key material</p>
<dt>~l</p>
<dd>messages addressed to a known mailing list (defined by either <code>subscribe</code> or <code>list</code>)</p>
<dt>~L <i>EXPR</i></p>
<dd>messages either originated or received by <i>EXPR</i></p>
<dt>%L <i>GROUP</i></p>
<dd>messages either originated or received by any member of <i>GROUP</i></p>
<dt>~m <i>MIN</i>&#8211;<i>MAX</i></p>
<dd>message in the range <i>MIN</i> to <i>MAX</i></p>
<dt>~M <i>EXPR</i></p>
<dd>messages which contain a mime Content-Type matching <i>EXPR</i></p>
<dt>~n <i>MIN</i>&#8211;<i>MAX</i></p>
<dd>messages with a score in the range <i>MIN</i> to <i>MAX</i></p>
<dt>~N</p>
<dd>new messages</p>
<dt>~O</p>
<dd>old messages</p>
<dt>~p</p>
<dd>messages addressed to you (consults $from, <code>alternates</code>, and local account/hostname information)</p>
<dt>~P</p>
<dd>messages from you (consults $from, <code>alternates</code>, and local account/hostname information)</p>
<dt>~Q</p>
<dd>messages which have been replied to</p>
<dt>~r <i>MIN</i>&#8211;<i>MAX</i></p>
<dd>messages with &#8220;date-received&#8221; in a Date range</p>
<dt>~R</p>
<dd>read messages</p>
<dt>~s <i>EXPR</i></p>
<dd>messages having <i>EXPR</i> in the &#8220;Subject&#8221; field.</p>
<dt>~S</p>
<dd>superseded messages</p>
<dt>~t <i>EXPR</i></p>
<dd>messages addressed to <i>EXPR</i></p>
<dt>~T</p>
<dd>tagged messages</p>
<dt>~u</p>
<dd>messages addressed to a subscribed mailing list (defined by <code>subscribe</code> commands)</p>
<dt>~U</p>
<dd>unread messages</p>
<dt>~v</p>
<dd>message is part of a collapsed thread.</p>
<dt>~V</p>
<dd>cryptographically verified messages</p>
<dt>~x <i>EXPR</i></p>
<dd>messages which contain <i>EXPR</i> in the &#8220;References&#8221; or &#8220;In-Reply-To&#8221; field</p>
<dt>~X <i>MIN</i>&#8211;<i>MAX</i></p>
<dd>messages with MIN &#8211; MAX attachments</p>
<dt>~y <i>EXPR</i></p>
<dd>messages which contain <i>EXPR</i> in the &#8220;X-Label&#8221; field</p>
<dt>~z <i>MIN</i>&#8211;<i>MAX</i></p>
<dd>messages with a size in the range <i>MIN</i> to <i>MAX</i></p>
<dt>~=</p>
<dd>duplicated messages (see $duplicate_threads)</p>
<dt>~$</p>
<dd>unreferenced message (requires threaded view)</p>
<dt>~(PATTERN)</p>
<dd>messages in threads containing messages matching a certain pattern, e.g. all threads containing messages from you: ~(~P)</p>
<dt>~&lt;(PATTERN)</p>
<dd>messages whose immediate parent matches PATTERN, e.g. replies to your messages: ~&lt;(~P)</p>
<dt>~&gt;(PATTERN)</p>
<dd>messages having an immediate child matching PATTERN, e.g. messages you replied to: ~&gt;(~P)</dl>
<p> In the above, <i>EXPR</i> is a regular expression. </p>
<p> With the <code>~d</code>, <code>~m</code>, <code>~n</code>, <code>~r</code>, <code>~X</code>, and <code>~z</code> operators, you can also specify ranges in the forms <code>&lt;</code><i>MAX</i>, <code>&gt;</code><i>MIN</i>, <i>MIN</i><code>&#8211;</code>, and <code>&#8211;</code><i>MAX</i>. </p>
<p> With the <code>~z</code> operator, the suffixes &#8220;K&#8221; and &#8220;M&#8221; are allowed to specify kilobyte and megabyte respectively. </p>
<p> The <code>~b</code>, <code>~B</code>, <code>~h</code>, <code>~M</code>, and <code>~X</code> operators require reading each message in, which can be much slower. </p>
<p> You can force Mutt to treat <i>EXPR</i> as a simple string instead of a regular expression by using = instead of ~ in the pattern name.</p>
<h3>Matching dates</h3>
<p>The <code>~d</code> and <code>~r</code> operators are used to match date ranges, which are interpreted to be given in your local time zone. </p>
<p> A date is of the form <i>DD</i>[<code>/</code><i>MM</i>[<code>/</code>[<i>cc</i>]<i>YY</i>]], that is, a two-digit date, optionally followed by a two-digit month, optionally followed by a year specifications. Omitted fields default to the current month and year. </p>
<p> Mutt understands either two or four digit year specifications. When given a two-digit year, mutt will interpret values less than 70 as lying in the 21st century (i.e., &#8220;38&#8221; means 2038 and not 1938, and &#8220;00&#8221; is interpreted as 2000), and values greater than or equal to 70 as lying in the 20th century. </p>
<p> Note that this behavior <i>is</i> Y2K compliant, but that mutt <i>does</i> have a Y2.07K problem. </p>
<p> If a date range consists of a single date, the operator in question will match that precise date. If the date range consists of a dash (&#8220;<code>&#8211;</code>&#8220;), followed by a date, this range will match any date before and up to the date given. Similarly, a date followed by a dash matches the date given and any later point of time. Two dates, separated by a dash, match any date which lies in the given range of time. </p>
<p> You can also modify any absolute date by giving an error range. An error range consists of one of the characters <code>+</code>, <code>&#8211;</code>, <code>*</code>, followed by a positive number, followed by one of the unit characters <code>y</code>, <code>m</code>, <code>w</code>, or <code>d</code>, specifying a unit of years, months, weeks, or days. <code>+</code> increases the maximum date matched by the given interval of time, <code>&#8211; </code> decreases the minimum date matched by the given interval of time, and <code>*</code> increases the maximum date and decreases the minimum date matched by the given interval of time. It is possible to give multiple error margins, which cumulate. Example: <code>1/1/2001-1w+2w*3d</code> </p>
<p> You can also specify offsets relative to the current date. An offset is specified as one of the characters <code>&lt;</code>, <code>&gt;</code>, <code>=</code>, followed by a positive number, followed by one of the unit characters <code>y</code>, <code>m</code>, <code>w</code>, <code>d</code>, <code>H</code>, <code>M</code>, or <code>S</code>. <code>&gt;</code> matches dates which are older than the specified amount of time, an offset which begins with the character <code>&lt; </code> matches dates which are more recent than the specified amount of time, and an offset which begins with the character <code>=</code> matches points of time which are precisely the given amount of time ago.</p>
<h2>Configuration Variables</h2>
<dl>
<dt><code>abort_noattach</code></p>
<dd>
<pre>Type: quadoption
Default: no</pre>
<dd>When the body of the message matches $abort_noattach_regexp and there are no attachments, this quadoption controls whether to abort sending the message. </p>
<dt><code>abort_noattach_regexp</code></p>
<dd>
<pre>Type: regular expression
Default: "attach"</pre>
<dd>Specifies a regular expression to match against the body of the message, to determine if an attachment was mentioned but mistakenly forgotten. If it matches, $abort_noattach will be consulted to determine if message sending will be aborted.</p>
<dd>Like other regular expressions in Mutt, the search is case sensitive if the pattern contains at least one upper case letter, and case insensitive otherwise. </p>
<dt><code>abort_nosubject</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>If set to <i>yes</i>, when composing messages and no subject is given at the subject prompt, composition will be aborted. If set to <i>no</i>, composing messages with no subject given at the subject prompt will never be aborted. </p>
<dt><code>abort_unmodified</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>If set to <i>yes</i>, composition will automatically abort after editing the message body if no changes are made to the file (this check only happens after the <i>first</i> edit of the file). When set to <i>no</i>, composition will never be aborted. </p>
<dt><code>alias_file</code></p>
<dd>
<pre>Type: path
Default: "~/.muttrc"</pre>
<dd>The default file in which to save aliases created by the &lt;create-alias&gt; function. Entries added to this file are encoded in the character set specified by $config_charset if it is <i>set</i> or the current character set otherwise.</p>
<dd><code>Note:</code> Mutt will not automatically source this file; you must explicitly use the &#8220;source&#8221; command for it to be executed in case this option points to a dedicated alias file.</p>
<dd>The default for this option is the currently used muttrc file, or &#8220;~/.muttrc&#8221; if no user muttrc was found. </p>
<dt><code>alias_format</code></p>
<dd>
<pre>Type: string
Default: "%4n %2f %t %-10a %r"</pre>
<dd>Specifies the format of the data displayed for the &#8220;alias&#8221; menu. The following <a href="/docs/linux/man/3-printf/">printf</a>(3)-style sequences are available:</p>
<dl>
<dd>
<dl>
<dt>%a</p>
<dd>alias name</p>
<dt>%f</p>
<dd>flags &#8211; currently, a &#8220;d&#8221; for an alias marked for deletion</p>
<dt>%n</p>
<dd>index number</p>
<dt>%r</p>
<dd>address which alias expands to</p>
<dt>%t</p>
<dd>character which indicates if the alias is tagged for inclusion</dl>
</dl>
<dt><code>allow_8bit</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls whether 8-bit data is converted to 7-bit using either Quoted- Printable or Base64 encoding when sending mail. </p>
<dt><code>allow_ansi</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Controls whether ANSI color codes in messages (and color tags in rich text messages) are to be interpreted. Messages containing these codes are rare, but if this option is <i>set</i>, their text will be colored accordingly. Note that this may override your color choices, and even present a security problem, since a message could include a line like </p>
<dd>
<pre>[-- PGP output follows ...</pre>
<dd>and give it the same color as your attachment color (see also $crypt_timestamp). </p>
<dt><code>arrow_cursor</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, an arrow (&#8220;-&gt;&#8221;) will be used to indicate the current entry in menus instead of highlighting the whole line. On slow network or modem links this will make response faster because there is less that has to be redrawn on the screen when moving to the next or previous entries in the menu. </p>
<dt><code>ascii_chars</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, Mutt will use plain ASCII characters when displaying thread and attachment trees, instead of the default <i>ACS</i> characters. </p>
<dt><code>askbcc</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, Mutt will prompt you for blind-carbon-copy (Bcc) recipients before editing an outgoing message. </p>
<dt><code>askcc</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, Mutt will prompt you for carbon-copy (Cc) recipients before editing the body of an outgoing message. </p>
<dt><code>assumed_charset</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This variable is a colon-separated list of character encoding schemes for messages without character encoding indication. Header field values and message body content without character encoding indication would be assumed that they are written in one of this list. By default, all the header fields and message body without any charset indication are assumed to be in &#8220;us-ascii&#8221;.</p>
<dd>For example, Japanese users might prefer this: </p>
<dd>
<pre>set assumed_charset="iso-2022-jp:euc-jp:shift_jis:utf-8"</pre>
<dd>However, only the first content is valid for the message body. </p>
<dt><code>attach_charset</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This variable is a colon-separated list of character encoding schemes for text file attachments. Mutt uses this setting to guess which encoding files being attached are encoded in to convert them to a proper character set given in $send_charset.</p>
<dd>If <i>unset</i>, the value of $charset will be used instead. For example, the following configuration would work for Japanese text handling: </p>
<dd>
<pre>set attach_charset="iso-2022-jp:euc-jp:shift_jis:utf-8"</pre>
<dd>Note: for Japanese users, &#8220;iso-2022-*&#8221; must be put at the head of the value as shown above if included. </p>
<dt><code>attach_format</code></p>
<dd>
<pre>Type: string
Default: "%u%D%I %t%4n %T%.40d%&gt; [%.7m/%.10M, %.6e%?C?, %C?, %s] "</pre>
<dd>This variable describes the format of the &#8220;attachment&#8221; menu. The following <a href="/docs/linux/man/3-printf/">printf</a>(3)-style sequences are understood:</p>
<dl>
<dd>
<dl>
<dt>%C</p>
<dd>charset</p>
<dt>%c</p>
<dd>requires charset conversion (&#8220;n&#8221; or &#8220;c&#8221;)</p>
<dt>%D</p>
<dd>deleted flag</p>
<dt>%d</p>
<dd>description (if none, falls back to %F)</p>
<dt>%e</p>
<dd>MIME content-transfer-encoding</p>
<dt>%F</p>
<dd>filename in content-disposition header (if none, falls back to %f)</p>
<dt>%f</p>
<dd>filename</p>
<dt>%I</p>
<dd>disposition (&#8220;I&#8221; for inline, &#8220;A&#8221; for attachment)</p>
<dt>%m</p>
<dd>major MIME type</p>
<dt>%M</p>
<dd>MIME subtype</p>
<dt>%n</p>
<dd>attachment number</p>
<dt>%Q</p>
<dd>&#8220;Q&#8221;, if MIME part qualifies for attachment counting</p>
<dt>%s</p>
<dd>size (see formatstrings-size)</p>
<dt>%t</p>
<dd>tagged flag</p>
<dt>%T</p>
<dd>graphic tree characters</p>
<dt>%u</p>
<dd>unlink (=to delete) flag</p>
<dt>%X</p>
<dd>number of qualifying MIME parts in this part and its children (please see the &#8220;attachments&#8221; section for possible speed effects)</p>
<dt>%&gt;X</p>
<dd>right justify the rest of the string and pad with character &#8220;X&#8221;</p>
<dt>%|X</p>
<dd>pad to the end of the line with character &#8220;X&#8221;</p>
<dt>%*X</p>
<dd>soft-fill with character &#8220;X&#8221; as pad</dl>
</dl>
<dd>For an explanation of &#8220;soft-fill&#8221;, see the $index_format documentation. </p>
<dt><code>attach_sep</code></p>
<dd>
<pre>Type: string
Default: "
"</pre>
<dd>The separator to add between attachments when operating (saving, printing, piping, etc) on a list of tagged attachments. </p>
<dt><code>attach_split</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If this variable is <i>unset</i>, when operating (saving, printing, piping, etc) on a list of tagged attachments, Mutt will concatenate the attachments and will operate on them as a single attachment. The $attach_sep separator is added after each attachment. When <i>set</i>, Mutt will operate on the attachments one by one. </p>
<dt><code>attribution</code></p>
<dd>
<pre>Type: string
Default: "On %d, %n wrote:"</pre>
<dd>This is the string that will precede a message which has been included in a reply. For a full listing of defined <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences see the section on $index_format. </p>
<dt><code>attribution_locale</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>The locale used by <a href="/docs/linux/man/3-strftime/">strftime</a>(3) to format dates in the attribution string. Legal values are the strings your system accepts for the locale environment variable $LC_TIME.</p>
<dd>This variable is to allow the attribution date format to be customized by recipient or folder using hooks. By default, Mutt will use your locale environment, so there is no need to set this except to override that default. </p>
<dt><code>auto_subscribe</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, Mutt assumes the presence of a List-Post header means the recipient is subscribed to the list. Unless the mailing list is in the &#8220;unsubscribe&#8221; or &#8220;unlist&#8221; lists, it will be added to the &#8220;subscribe&#8221; list. Parsing and checking these things slows header reading down, so this option is disabled by default. </p>
<dt><code>auto_tag</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, functions in the <i>index</i> menu which affect a message will be applied to all tagged messages (if there are any). When unset, you must first use the &lt;tag-prefix&gt; function (bound to &#8220;;&#8221; by default) to make the next function apply to all tagged messages. </p>
<dt><code>autocrypt</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, enables autocrypt, which provides passive encryption protection with keys exchanged via headers. See &#8220;autocryptdoc&#8221; for more details. (Autocrypt only) </p>
<dt><code>autocrypt_acct_format</code></p>
<dd>
<pre>Type: string
Default: "%4n %-30a %20p %10s"</pre>
<dd>This variable describes the format of the &#8220;autocrypt account&#8221; menu. The following <a href="/docs/linux/man/3-printf/">printf</a>(3)-style sequences are understood</p>
<dl>
<dd>
<dl>
<dt>%a</p>
<dd>email address</p>
<dt>%k</p>
<dd>gpg keyid</p>
<dt>%n</p>
<dd>current entry number</p>
<dt>%p</p>
<dd>prefer-encrypt flag</p>
<dt>%s</p>
<dd>status flag (active/inactive)</dl>
</dl>
<dd>(Autocrypt only) </p>
<dt><code>autocrypt_dir</code></p>
<dd>
<pre>Type: path
Default: "~/.mutt/autocrypt"</pre>
<dd>This variable sets where autocrypt files are stored, including the GPG keyring and sqlite database. See &#8220;autocryptdoc&#8221; for more details. (Autocrypt only) </p>
<dt><code>autocrypt_reply</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, replying to an autocrypt email automatically enables autocrypt in the reply. You may want to unset this if you&#8217;re using the same key for autocrypt as normal web-of-trust, so that autocrypt isn&#8217;t forced on for all encrypted replies. (Autocrypt only) </p>
<dt><code>autoedit</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i> along with $edit_headers, Mutt will skip the initial send-menu (prompting for subject and recipients) and allow you to immediately begin editing the body of your message. The send-menu may still be accessed once you have finished editing the body of your message.</p>
<dd><code>Note:</code> when this option is <i>set</i>, you cannot use send-hooks that depend on the recipients when composing a new (non-reply) message, as the initial list of recipients is empty.</p>
<dd>Also see $fast_reply. </p>
<dt><code>beep</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When this variable is <i>set</i>, mutt will beep when an error occurs. </p>
<dt><code>beep_new</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When this variable is <i>set</i>, mutt will beep whenever it prints a message notifying you of new mail. This is independent of the setting of the $beep variable. </p>
<dt><code>bounce</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>Controls whether you will be asked to confirm bouncing messages. If set to <i>yes</i> you don&#8217;t get asked if you want to bounce a message. Setting this variable to <i>no</i> is not generally useful, and thus not recommended, because you are unable to bounce messages. </p>
<dt><code>bounce_delivered</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When this variable is <i>set</i>, mutt will include Delivered-To headers when bouncing messages. Postfix users may wish to <i>unset</i> this variable. </p>
<dt><code>braille_friendly</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When this variable is <i>set</i>, mutt will place the cursor at the beginning of the current line in menus, even when the $arrow_cursor variable is <i>unset</i>, making it easier for blind persons using Braille displays to follow these menus. The option is <i>unset</i> by default because many visual terminals don&#8217;t permit making the cursor invisible. </p>
<dt><code>browser_abbreviate_mailboxes</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When this variable is <i>set</i>, mutt will abbreviate mailbox names in the browser mailbox list, using &#8216;~&#8217; and &#8216;=&#8217; shortcuts.</p>
<dd>The default &#8220;alpha&#8221; setting of $sort_browser uses locale-based sorting (using <a href="/docs/linux/man/3-strcoll/">strcoll</a>(3)), which ignores some punctuation. This can lead to some situations where the order doesn&#8217;t make intuitive sense. In those cases, it may be desirable to <i>unset</i> this variable. </p>
<dt><code>browser_sticky_cursor</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When this variable is <i>set</i>, the browser will attempt to keep the cursor on the same mailbox when performing various functions. These include moving up a directory, toggling between mailboxes and directory listing, creating/renaming a mailbox, toggling subscribed mailboxes, and entering a new mask. </p>
<dt><code>certificate_file</code></p>
<dd>
<pre>Type: path
Default: "~/.mutt_certificates"</pre>
<dd>This variable specifies the file where the certificates you trust are saved. When an unknown certificate is encountered, you are asked if you accept it or not. If you accept it, the certificate can also be saved in this file and further connections are automatically accepted.</p>
<dd>You can also manually add CA certificates in this file. Any server certificate that is signed with one of these CA certificates is also automatically accepted.</p>
<dd>Example: </p>
<dd>
<pre>set certificate_file=~/.mutt/certificates</pre>
<dt><code>change_folder_next</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When this variable is <i>set</i>, the &lt;change-folder&gt; function mailbox suggestion will start at the next folder in your &#8220;mailboxes&#8221; list, instead of starting at the first folder in the list. </p>
<dt><code>charset</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Character set your terminal uses to display and enter textual data. It is also the fallback for $send_charset.</p>
<dd>Upon startup Mutt tries to derive this value from environment variables such as $LC_CTYPE or $LANG.</p>
<dd><code>Note:</code> It should only be set in case Mutt isn&#8217;t able to determine the character set used correctly. </p>
<dt><code>check_mbox_size</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When this variable is <i>set</i>, mutt will use file size attribute instead of access time when checking for new mail in mbox and mmdf folders.</p>
<dd>This variable is <i>unset</i> by default and should only be enabled when new mail detection for these folder types is unreliable or doesn&#8217;t work.</p>
<dd>Note that enabling this variable should happen before any &#8220;mailboxes&#8221; directives occur in configuration files regarding mbox or mmdf folders because mutt needs to determine the initial new mail status of such a mailbox by performing a fast mailbox scan when it is defined. Afterwards the new mail status is tracked by file size changes. </p>
<dt><code>check_new</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd><code>Note:</code> this option only affects <i>maildir</i> and <i>MH</i> style mailboxes.</p>
<dd>When <i>set</i>, Mutt will check for new mail delivered while the mailbox is open. Especially with MH mailboxes, this operation can take quite some time since it involves scanning the directory and checking each file to see if it has already been looked at. If this variable is <i>unset</i>, no check for new mail is performed while the mailbox is open. </p>
<dt><code>collapse_unread</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>unset</i>, Mutt will not collapse a thread if it contains any unread messages. </p>
<dt><code>compose_format</code></p>
<dd>
<pre>Type: string
Default: "-- Mutt: Compose [Approx. msg size: %l Atts: %a]%&gt;-"</pre>
<dd>Controls the format of the status line displayed in the &#8220;compose&#8221; menu. This string is similar to $status_format, but has its own set of <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences:</p>
<dl>
<dd>
<dl>
<dt>%a</p>
<dd>total number of attachments</p>
<dt>%h</p>
<dd>local hostname</p>
<dt>%l</p>
<dd>approximate size (in bytes) of the current message (see formatstrings-size)</p>
<dt>%v</p>
<dd>Mutt version string</dl>
</dl>
<dd>See the text describing the $status_format option for more information on how to set $compose_format. </p>
<dt><code>config_charset</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>When defined, Mutt will recode commands in rc files from this encoding to the current character set as specified by $charset and aliases written to $alias_file from the current character set.</p>
<dd>Please note that if setting $charset it must be done before setting $config_charset.</p>
<dd>Recoding should be avoided as it may render unconvertable characters as question marks which can lead to undesired side effects (for example in regular expressions). </p>
<dt><code>confirmappend</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will prompt for confirmation when appending messages to an existing mailbox. </p>
<dt><code>confirmcreate</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will prompt for confirmation when saving messages to a mailbox which does not yet exist before creating it. </p>
<dt><code>connect_timeout</code></p>
<dd>
<pre>Type: number
Default: 30</pre>
<dd>Causes Mutt to timeout a network connection (for IMAP, POP or SMTP) after this many seconds if the connection is not able to be established. A negative value causes Mutt to wait indefinitely for the connection attempt to succeed. </p>
<dt><code>content_type</code></p>
<dd>
<pre>Type: string
Default: "text/plain"</pre>
<dd>Sets the default Content-Type for the body of newly composed messages. </p>
<dt><code>copy</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>This variable controls whether or not copies of your outgoing messages will be saved for later references. Also see $record, $save_name, $force_name and &#8220;fcc-hook&#8221;. </p>
<dt><code>count_alternatives</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, Mutt will recurse inside multipart/alternatives while performing attachment searching and counting (see attachments).</p>
<dd>Traditionally, multipart/alternative parts have simply represented different encodings of the main content of the email. Unfortunately, some mail clients have started to place email attachments inside one of alternatives. Setting this will allow Mutt to find and count matching attachments hidden there, and include them in the index via %X or through ~X pattern matching. </p>
<dt><code>crypt_autoencrypt</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Setting this variable will cause Mutt to always attempt to PGP encrypt outgoing messages. This is probably only useful in connection to the &#8220;send-hook&#8221; command. It can be overridden by use of the pgp menu, when encryption is not required or signing is requested as well. If $smime_is_default is <i>set</i>, then OpenSSL is used instead to create S/MIME messages and settings can be overridden by use of the smime menu instead. (Crypto only) </p>
<dt><code>crypt_autopgp</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>This variable controls whether or not mutt may automatically enable PGP encryption/signing for messages. See also $crypt_autoencrypt, $crypt_replyencrypt, $crypt_autosign, $crypt_replysign and $smime_is_default. </p>
<dt><code>crypt_autosign</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Setting this variable will cause Mutt to always attempt to cryptographically sign outgoing messages. This can be overridden by use of the pgp menu, when signing is not required or encryption is requested as well. If $smime_is_default is <i>set</i>, then OpenSSL is used instead to create S/MIME messages and settings can be overridden by use of the smime menu instead of the pgp menu. (Crypto only) </p>
<dt><code>crypt_autosmime</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>This variable controls whether or not mutt may automatically enable S/MIME encryption/signing for messages. See also $crypt_autoencrypt, $crypt_replyencrypt, $crypt_autosign, $crypt_replysign and $smime_is_default. </p>
<dt><code>crypt_confirmhook</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If set, then you will be prompted for confirmation of keys when using the <i>crypt-hook</i> command. If unset, no such confirmation prompt will be presented. This is generally considered unsafe, especially where typos are concerned. </p>
<dt><code>crypt_opportunistic_encrypt</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Setting this variable will cause Mutt to automatically enable and disable encryption, based on whether all message recipient keys can be located by Mutt.</p>
<dd>When this option is enabled, Mutt will enable/disable encryption each time the TO, CC, and BCC lists are edited. If $edit_headers is set, Mutt will also do so each time the message is edited.</p>
<dd>While this is set, encryption can&#8217;t be manually enabled/disabled. The pgp or smime menus provide a selection to temporarily disable this option for the current message.</p>
<dd>If $crypt_autoencrypt or $crypt_replyencrypt enable encryption for a message, this option will be disabled for that message. It can be manually re-enabled in the pgp or smime menus. (Crypto only) </p>
<dt><code>crypt_protected_headers_read</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When set, Mutt will display protected headers (&#8220;Memory Hole&#8221;) in the pager, and will update the index and header cache with revised headers. Protected headers are stored inside the encrypted or signed part of an an email, to prevent disclosure or tampering. For more information see <a rel="nofollow" href="https://github.com/autocrypt/memoryhole.">https://github.com/autocrypt/memoryhole.</a> Currently Mutt only supports the Subject header.</p>
<dd>Encrypted messages using protected headers often substitute the exposed Subject header with a dummy value (see $crypt_protected_headers_subject). Mutt will update its concept of the correct subject <code>after</code> the message is opened, i.e. via the &lt;display-message&gt; function. If you reply to a message before opening it, Mutt will end up using the dummy Subject header, so be sure to open such a message first. (Crypto only) </p>
<dt><code>crypt_protected_headers_save</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When $crypt_protected_headers_read is set, and a message with a protected Subject is opened, Mutt will save the updated Subject into the header cache by default. This allows searching/limiting based on the protected Subject header if the mailbox is re-opened, without having to re-open the message each time. However, for mbox/mh mailbox types, or if header caching is not set up, you would need to re-open the message each time the mailbox was reopened before you could see or search/limit on the protected subject again.</p>
<dd>When this variable is set, Mutt additionally saves the protected Subject back <code>in the clear-text message headers</code>. This provides better usability, but with the tradeoff of reduced security. The protected Subject header, which may have previously been encrypted, is now stored in clear-text in the message headers. Copying the message elsewhere, via Mutt or external tools, could expose this previously encrypted data. Please make sure you understand the consequences of this before you enable this variable. (Crypto only) </p>
<dt><code>crypt_protected_headers_subject</code></p>
<dd>
<pre>Type: string
Default: "Encrypted subject"</pre>
<dd>When $crypt_protected_headers_write is set, and the message is marked for encryption, this will be substituted into the Subject field in the message headers. To prevent a subject from being substituted, unset this variable, or set it to the empty string. (Crypto only) </p>
<dt><code>crypt_protected_headers_write</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When set, Mutt will generate protected headers (&#8220;Memory Hole&#8221;) for signed and encrypted emails. Protected headers are stored inside the encrypted or signed part of an an email, to prevent disclosure or tampering. For more information see <a rel="nofollow" href="https://github.com/autocrypt/memoryhole.">https://github.com/autocrypt/memoryhole.</a> Currently Mutt only supports the Subject header. (Crypto only) </p>
<dt><code>crypt_replyencrypt</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, automatically PGP or OpenSSL encrypt replies to messages which are encrypted. (Crypto only) </p>
<dt><code>crypt_replysign</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, automatically PGP or OpenSSL sign replies to messages which are signed.</p>
<dd><code>Note:</code> this does not work on messages that are encrypted <i>and</i> signed! (Crypto only) </p>
<dt><code>crypt_replysignencrypted</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, automatically PGP or OpenSSL sign replies to messages which are encrypted. This makes sense in combination with $crypt_replyencrypt, because it allows you to sign all messages which are automatically encrypted. This works around the problem noted in $crypt_replysign, that mutt is not able to find out whether an encrypted message is also signed. (Crypto only) </p>
<dt><code>crypt_timestamp</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, mutt will include a time stamp in the lines surrounding PGP or S/MIME output, so spoofing such lines is more difficult. If you are using colors to mark these lines, and rely on these, you may <i>unset</i> this setting. (Crypto only) </p>
<dt><code>crypt_use_gpgme</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This variable controls the use of the GPGME-enabled crypto backends. If it is <i>set</i> and Mutt was built with gpgme support, the gpgme code for S/MIME and PGP will be used instead of the classic code. Note that you need to set this option in .muttrc; it won&#8217;t have any effect when used interactively.</p>
<dd>Note that the GPGME backend does not support creating old-style inline (traditional) PGP encrypted or signed messages (see $pgp_autoinline). </p>
<dt><code>crypt_use_pka</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Controls whether mutt uses PKA (see <a rel="nofollow" href="http://www.g10code.de/docs/pka-intro.de.pdf)">http://www.g10code.de/docs/pka-intro.de.pdf)</a> during signature verification (only supported by the GPGME backend). </p>
<dt><code>crypt_verify_sig</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>If <i>&#8220;yes&#8221;</i>, always attempt to verify PGP or S/MIME signatures. If <i>&#8220;ask-*&#8221;</i>, ask whether or not to verify the signature. If <i>&#8220;no&#8221;</i>, never attempt to verify cryptographic signatures. (Crypto only) </p>
<dt><code>date_format</code></p>
<dd>
<pre>Type: string
Default: "!%a, %b %d, %Y at %I:%M:%S%p %Z"</pre>
<dd>This variable controls the format of the date printed by the &#8220;%d&#8221; sequence in $index_format. This is passed to the <a href="/docs/linux/man/3-strftime/">strftime</a>(3) function to process the date, see the man page for the proper syntax.</p>
<dd>Unless the first character in the string is a bang (&#8220;!&#8221;), the month and week day names are expanded according to the locale. If the first character in the string is a bang, the bang is discarded, and the month and week day names in the rest of the string are expanded in the <i>C</i> locale (that is in US English). </p>
<dt><code>default_hook</code></p>
<dd>
<pre>Type: string
Default: "~f %s !~P | (~P ~C %s)"</pre>
<dd>This variable controls how &#8220;message-hook&#8221;, &#8220;reply-hook&#8221;, &#8220;send-hook&#8221;, &#8220;send2-hook&#8221;, &#8220;save-hook&#8221;, and &#8220;fcc-hook&#8221; will be interpreted if they are specified with only a simple regexp, instead of a matching pattern. The hooks are expanded when they are declared, so a hook will be interpreted according to the value of this variable at the time the hook is declared.</p>
<dd>The default value matches if the message is either from a user matching the regular expression given, or if it is from you (if the from address matches &#8220;alternates&#8221;) and is to or cc&#8217;ed to a user matching the given regular expression. </p>
<dt><code>delete</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>Controls whether or not messages are really deleted when closing or synchronizing a mailbox. If set to <i>yes</i>, messages marked for deleting will automatically be purged without prompting. If set to <i>no</i>, messages marked for deletion will be kept in the mailbox. </p>
<dt><code>delete_untag</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If this option is <i>set</i>, mutt will untag messages when marking them for deletion. This applies when you either explicitly delete a message, or when you save it to another folder. </p>
<dt><code>digest_collapse</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If this option is <i>set</i>, mutt&#8217;s received-attachments menu will not show the subparts of individual messages in a multipart/digest. To see these subparts, press &#8220;v&#8221; on that menu. </p>
<dt><code>display_filter</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>When set, specifies a command used to filter messages. When a message is viewed it is passed as standard input to $display_filter, and the filtered message is read from the standard output. </p>
<dt><code>dotlock_program</code></p>
<dd>
<pre>Type: path
Default: "/usr/bin/mutt_dotlock"</pre>
<dd>Contains the path of the <a href="/docs/linux/man/8-mutt_dotlock/">mutt_dotlock</a>(8) binary to be used by mutt. </p>
<dt><code>dsn_notify</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This variable sets the request for when notification is returned. The string consists of a comma separated list (no spaces!) of one or more of the following: <i>never</i>, to never request notification, <i>failure</i>, to request notification on transmission failure, <i>delay</i>, to be notified of message delays, <i>success</i>, to be notified of successful transmission.</p>
<dd>Example: </p>
<dd>
<pre>set dsn_notify="failure,delay"</pre>
<dd><code>Note:</code> when using $sendmail for delivery, you should not enable this unless you are either using Sendmail 8.8.x or greater or a MTA providing a <a href="/docs/linux/man/1-sendmail/">sendmail</a>(1)-compatible interface supporting the -N option for DSN. For SMTP delivery, DSN support is auto-detected so that it depends on the server whether DSN will be used or not. </p>
<dt><code>dsn_return</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This variable controls how much of your message is returned in DSN messages. It may be set to either <i>hdrs</i> to return just the message header, or <i>full</i> to return the full message.</p>
<dd>Example: </p>
<dd>
<pre>set dsn_return=hdrs</pre>
<dd><code>Note:</code> when using $sendmail for delivery, you should not enable this unless you are either using Sendmail 8.8.x or greater or a MTA providing a <a href="/docs/linux/man/1-sendmail/">sendmail</a>(1)-compatible interface supporting the -R option for DSN. For SMTP delivery, DSN support is auto-detected so that it depends on the server whether DSN will be used or not. </p>
<dt><code>duplicate_threads</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>This variable controls whether mutt, when $sort is set to <i>threads</i>, threads messages with the same Message-Id together. If it is <i>set</i>, it will indicate that it thinks they are duplicates of each other with an equals sign in the thread tree. </p>
<dt><code>edit_headers</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This option allows you to edit the header of your outgoing messages along with the body of your message.</p>
<dd>Although the compose menu may have localized header labels, the labels passed to your editor will be standard RFC 2822 headers, (e.g. To:, Cc:, Subject:). Headers added in your editor must also be RFC 2822 headers, or one of the pseudo headers listed in &#8220;edit-header&#8221;. Mutt will not understand localized header labels, just as it would not when parsing an actual email.</p>
<dd><code>Note</code> that changes made to the References: and Date: headers are ignored for interoperability reasons. </p>
<dt><code>editor</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>This variable specifies which editor is used by mutt. It defaults to the value of the $VISUAL, or $EDITOR, environment variable, or to the string &#8220;vi&#8221; if neither of those are set.</p>
<dd>The $editor string may contain a <i>%s</i> escape, which will be replaced by the name of the file to be edited. If the <i>%s</i> escape does not appear in $editor, a space and the name to be edited are appended.</p>
<dd>The resulting string is then executed by running </p>
<dd>
<pre>sh -c 'string'</pre>
<dd>where <i>string</i> is the expansion of $editor described above. </p>
<dt><code>encode_from</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will quoted-printable encode messages when they contain the string &#8220;From &#8221; (note the trailing space) in the beginning of a line. This is useful to avoid the tampering certain mail delivery and transport agents tend to do with messages (in order to prevent tools from misinterpreting the line as a mbox message separator). </p>
<dt><code>entropy_file</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>The file which includes random data that is used to initialize SSL library functions. </p>
<dt><code>envelope_from_address</code></p>
<dd>
<pre>Type: e-mail address
Default: ""</pre>
<dd>Manually sets the <i>envelope</i> sender for outgoing messages. This value is ignored if $use_envelope_from is <i>unset</i>. </p>
<dt><code>error_history</code></p>
<dd>
<pre>Type: number
Default: 30</pre>
<dd>This variable controls the size (in number of strings remembered) of the error messages displayed by mutt. These can be shown with the &lt;error-history&gt; function. The history is cleared each time this variable is set. </p>
<dt><code>escape</code></p>
<dd>
<pre>Type: string
Default: "~"</pre>
<dd>Escape character to use for functions in the built-in editor. </p>
<dt><code>fast_reply</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, the initial prompt for recipients and subject are skipped when replying to messages, and the initial prompt for subject is skipped when forwarding messages.</p>
<dd><code>Note:</code> this variable has no effect when the $autoedit variable is <i>set</i>. </p>
<dt><code>fcc_attach</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>This variable controls whether or not attachments on outgoing messages are saved along with the main body of your message. </p>
<dt><code>fcc_before_send</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When this variable is <i>set</i>, FCCs will occur before sending the message. Before sending, the message cannot be manipulated, so it will be stored the exact same as sent: $fcc_attach and $fcc_clear will be ignored (using their default values).</p>
<dd>When <i>unset</i>, the default, FCCs will occur after sending. Variables $fcc_attach and $fcc_clear will be respected, allowing it to be stored without attachments or encryption/signing if desired. </p>
<dt><code>fcc_clear</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When this variable is <i>set</i>, FCCs will be stored unencrypted and unsigned, even when the actual message is encrypted and/or signed. (PGP only) </p>
<dt><code>flag_safe</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If set, flagged messages cannot be deleted. </p>
<dt><code>folder</code></p>
<dd>
<pre>Type: path
Default: "~/Mail"</pre>
<dd>Specifies the default location of your mailboxes. A &#8220;+&#8221; or &#8220;=&#8221; at the beginning of a pathname will be expanded to the value of this variable. Note that if you change this variable (from the default) value you need to make sure that the assignment occurs <i>before</i> you use &#8220;+&#8221; or &#8220;=&#8221; for any other variables since expansion takes place when handling the &#8220;mailboxes&#8221; command. </p>
<dt><code>folder_format</code></p>
<dd>
<pre>Type: string
Default: "%2C %t %N %F %2l %-8.8u %-8.8g %8s %d %f"</pre>
<dd>This variable allows you to customize the file browser display to your personal taste. This string is similar to $index_format, but has its own set of <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences:</p>
<dl>
<dd>
<dl>
<dt>%C</p>
<dd>current file number</p>
<dt>%d</p>
<dd>date/time folder was last modified</p>
<dt>%D</p>
<dd>date/time folder was last modified using $date_format.</p>
<dt>%f</p>
<dd>filename (&#8220;/&#8221; is appended to directory names, &#8220;@&#8221; to symbolic links and &#8220;*&#8221; to executable files)</p>
<dt>%F</p>
<dd>file permissions</p>
<dt>%g</p>
<dd>group name (or numeric gid, if missing)</p>
<dt>%l</p>
<dd>number of hard links</p>
<dt>%m</p>
<dd>number of messages in the mailbox *</p>
<dt>%n</p>
<dd>number of unread messages in the mailbox *</p>
<dt>%N</p>
<dd>N if mailbox has new mail, blank otherwise</p>
<dt>%s</p>
<dd>size in bytes (see formatstrings-size)</p>
<dt>%t</p>
<dd>&#8220;*&#8221; if the file is tagged, blank otherwise</p>
<dt>%u</p>
<dd>owner name (or numeric uid, if missing)</p>
<dt>%&gt;X</p>
<dd>right justify the rest of the string and pad with character &#8220;X&#8221;</p>
<dt>%|X</p>
<dd>pad to the end of the line with character &#8220;X&#8221;</p>
<dt>%*X</p>
<dd>soft-fill with character &#8220;X&#8221; as pad</dl>
</dl>
<dd>For an explanation of &#8220;soft-fill&#8221;, see the $index_format documentation.</p>
<dd>* = can be optionally printed if nonzero</p>
<dd>%m, %n, and %N only work for monitored mailboxes. %m requires $mail_check_stats to be set. %n requires $mail_check_stats to be set (except for IMAP mailboxes). </p>
<dt><code>followup_to</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls whether or not the &#8220;Mail-Followup-To:&#8221; header field is generated when sending mail. When <i>set</i>, Mutt will generate this field when you are replying to a known mailing list, specified with the &#8220;subscribe&#8221; or &#8220;lists&#8221; commands.</p>
<dd>This field has two purposes. First, preventing you from receiving duplicate copies of replies to messages which you send to mailing lists, and second, ensuring that you do get a reply separately for any messages sent to known lists to which you are not subscribed.</p>
<dd>The header will contain only the list&#8217;s address for subscribed lists, and both the list address and your own email address for unsubscribed lists. Without this header, a group reply to your message sent to a subscribed list will be sent to both the list and your address, resulting in two copies of the same email for you. </p>
<dt><code>force_name</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This variable is similar to $save_name, except that Mutt will store a copy of your outgoing message by the username of the address you are sending to even if that mailbox does not exist.</p>
<dd>Also see the $record variable. </p>
<dt><code>forward_attachments</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>When forwarding inline (i.e. $mime_forward <i>unset</i> or answered with &#8220;no&#8221; and $forward_decode <i>set</i>), attachments which cannot be decoded in a reasonable manner will be attached to the newly composed message if this quadoption is <i>set</i> or answered with &#8220;yes&#8221;. </p>
<dt><code>forward_attribution_intro</code></p>
<dd>
<pre>Type: string
Default: "----- Forwarded message from %f -----"</pre>
<dd>This is the string that will precede a message which has been forwarded in the main body of a message (when $mime_forward is unset). For a full listing of defined <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences see the section on $index_format. See also $attribution_locale. </p>
<dt><code>forward_attribution_trailer</code></p>
<dd>
<pre>Type: string
Default: "----- End forwarded message -----"</pre>
<dd>This is the string that will follow a message which has been forwarded in the main body of a message (when $mime_forward is unset). For a full listing of defined <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences see the section on $index_format. See also $attribution_locale. </p>
<dt><code>forward_decode</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls the decoding of complex MIME messages into text/plain when forwarding a message. The message header is also RFC2047 decoded. This variable is only used, if $mime_forward is <i>unset</i>, otherwise $mime_forward_decode is used instead. </p>
<dt><code>forward_decrypt</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls the handling of encrypted messages when forwarding a message. When <i>set</i>, the outer layer of encryption is stripped off. This variable is only used if $mime_forward is <i>set</i> and $mime_forward_decode is <i>unset</i>. (PGP only) </p>
<dt><code>forward_edit</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>This quadoption controls whether or not the user is automatically placed in the editor when forwarding messages. For those who always want to forward with no modification, use a setting of &#8220;no&#8221;. </p>
<dt><code>forward_format</code></p>
<dd>
<pre>Type: string
Default: "[%a: %s]"</pre>
<dd>This variable controls the default subject when forwarding a message. It uses the same format sequences as the $index_format variable. </p>
<dt><code>forward_quote</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, forwarded messages included in the main body of the message (when $mime_forward is <i>unset</i>) will be quoted using $indent_string. </p>
<dt><code>from</code></p>
<dd>
<pre>Type: e-mail address
Default: ""</pre>
<dd>When <i>set</i>, this variable contains a default from address. It can be overridden using &#8220;my_hdr&#8221; (including from a &#8220;send-hook&#8221;) and $reverse_name. This variable is ignored if $use_from is <i>unset</i>.</p>
<dd>This setting defaults to the contents of the environment variable $EMAIL. </p>
<dt><code>gecos_mask</code></p>
<dd>
<pre>Type: regular expression
Default: "^[^,]*"</pre>
<dd>A regular expression used by mutt to parse the GECOS field of a password entry when expanding the alias. The default value will return the string up to the first &#8220;,&#8221; encountered. If the GECOS field contains a string like &#8220;lastname, firstname&#8221; then you should set it to &#8220;.*&#8221;.</p>
<dd>This can be useful if you see the following behavior: you address an e-mail to user ID &#8220;stevef&#8221; whose full name is &#8220;Steve Franklin&#8221;. If mutt expands &#8220;stevef&#8221; to &#8220;&#8221;Franklin&#8221; stevef [at] foo.bar&#8221; then you should set the $gecos_mask to a regular expression that will match the whole name so mutt will expand &#8220;Franklin&#8221; to &#8220;Franklin, Steve&#8221;. </p>
<dt><code>hdrs</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>unset</i>, the header fields normally added by the &#8220;my_hdr&#8221; command are not created. This variable <i>must</i> be unset before composing a new message or replying in order to take effect. If <i>set</i>, the user defined header fields are added to every new message. </p>
<dt><code>header</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, this variable causes Mutt to include the header of the message you are replying to into the edit buffer. The $weed setting applies. </p>
<dt><code>header_cache</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>This variable points to the header cache database. If pointing to a directory Mutt will contain a header cache database file per folder, if pointing to a file that file will be a single global header cache. By default it is <i>unset</i> so no header caching will be used.</p>
<dd>Header caching can greatly improve speed when opening POP, IMAP MH or Maildir folders, see &#8220;caching&#8221; for details. </p>
<dt><code>header_cache_compress</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When mutt is compiled with qdbm, tokyocabinet, or kyotocabinet as header cache backend, this option determines whether the database will be compressed. Compression results in database files roughly being one fifth of the usual diskspace, but the decompression can result in a slower opening of cached folder(s) which in general is still much faster than opening non header cached folders. </p>
<dt><code>header_cache_pagesize</code></p>
<dd>
<pre>Type: number (long)
Default: 16384</pre>
<dd>When mutt is compiled with either gdbm or bdb4 as the header cache backend, this option changes the database page size. Too large or too small values can waste space, memory, or CPU time. The default should be more or less optimal for most use cases. </p>
<dt><code>header_color_partial</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, color header regexps behave like color body regexps: color is applied to the exact text matched by the regexp. When <i>unset</i>, color is applied to the entire header.</p>
<dd>One use of this option might be to apply color to just the header labels.</p>
<dd>See &#8220;color&#8221; for more details. </p>
<dt><code>help</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, help lines describing the bindings for the major functions provided by each menu are displayed on the first line of the screen.</p>
<dd><code>Note:</code> The binding will not be displayed correctly if the function is bound to a sequence rather than a single keystroke. Also, the help line may not be updated if a binding is changed while Mutt is running. Since this variable is primarily aimed at new users, neither of these should present a major problem. </p>
<dt><code>hidden_host</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will skip the host name part of $hostname variable when adding the domain part to addresses. This variable does not affect the generation of Message-IDs, and it will not lead to the cut-off of first-level domains. </p>
<dt><code>hide_limited</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will not show the presence of messages that are hidden by limiting, in the thread tree. </p>
<dt><code>hide_missing</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, mutt will not show the presence of missing messages in the thread tree. </p>
<dt><code>hide_thread_subject</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, mutt will not show the subject of messages in the thread tree that have the same subject as their parent or closest previously displayed sibling. </p>
<dt><code>hide_top_limited</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will not show the presence of messages that are hidden by limiting, at the top of threads in the thread tree. Note that when $hide_limited is <i>set</i>, this option will have no effect. </p>
<dt><code>hide_top_missing</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, mutt will not show the presence of missing messages at the top of threads in the thread tree. Note that when $hide_missing is <i>set</i>, this option will have no effect. </p>
<dt><code>history</code></p>
<dd>
<pre>Type: number
Default: 10</pre>
<dd>This variable controls the size (in number of strings remembered) of the string history buffer per category. The buffer is cleared each time the variable is set. </p>
<dt><code>history_file</code></p>
<dd>
<pre>Type: path
Default: "~/.mutthistory"</pre>
<dd>The file in which Mutt will save its history.</p>
<dd>Also see $save_history. </p>
<dt><code>history_remove_dups</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, all of the string history will be scanned for duplicates when a new entry is added. Duplicate entries in the $history_file will also be removed when it is periodically compacted. </p>
<dt><code>honor_disposition</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, Mutt will not display attachments with a disposition of &#8220;attachment&#8221; inline even if it could render the part to plain text. These MIME parts can only be viewed from the attachment menu.</p>
<dd>If <i>unset</i>, Mutt will render all MIME parts it can properly transform to plain text. </p>
<dt><code>honor_followup_to</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>This variable controls whether or not a Mail-Followup-To header is honored when group-replying to a message. </p>
<dt><code>hostname</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Specifies the fully-qualified hostname of the system mutt is running on containing the host&#8217;s name and the DNS domain it belongs to. It is used as the domain part (after &#8220;@&#8221;) for local email addresses as well as Message-Id headers.</p>
<dd>Its value is determined at startup as follows: the node&#8217;s hostname is first determined by the <a href="/docs/linux/man/3-uname/">uname</a>(3) function. The domain is then looked up using the <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2) and <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3) functions. If those calls are unable to determine the domain, the full value returned by uname is used. Optionally, Mutt can be compiled with a fixed domain name in which case a detected one is not used.</p>
<dd>Also see $use_domain and $hidden_host. </p>
<dt><code>idn_decode</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will show you international domain names decoded. Note: You can use IDNs for addresses even if this is <i>unset</i>. This variable only affects decoding. (IDN only) </p>
<dt><code>idn_encode</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will encode international domain names using IDN. Unset this if your SMTP server can handle newer (RFC 6531) UTF-8 encoded domains. (IDN only) </p>
<dt><code>ignore_linear_white_space</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This option replaces linear-white-space between encoded-word and text to a single space to prevent the display of MIME-encoded &#8220;Subject:&#8221; field from being divided into multiple lines. </p>
<dt><code>ignore_list_reply_to</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Affects the behavior of the &lt;reply&gt; function when replying to messages from mailing lists (as defined by the &#8220;subscribe&#8221; or &#8220;lists&#8221; commands). When <i>set</i>, if the &#8220;Reply-To:&#8221; field is set to the same value as the &#8220;To:&#8221; field, Mutt assumes that the &#8220;Reply-To:&#8221; field was set by the mailing list to automate responses to the list, and will ignore this field. To direct a response to the mailing list when this option is <i>set</i>, use the &lt;list-reply&gt; function; &lt;group-reply&gt; will reply to both the sender and the list. </p>
<dt><code>imap_authenticators</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This is a colon-delimited list of authentication methods mutt may attempt to use to log in to an IMAP server, in the order mutt should try them. Authentication methods are either &#8220;login&#8221; or the right side of an IMAP &#8220;AUTH=xxx&#8221; capability string, e.g. &#8220;digest-md5&#8221;, &#8220;gssapi&#8221; or &#8220;cram-md5&#8221;. This option is case-insensitive. If it&#8217;s <i>unset</i> (the default) mutt will try all available methods, in order from most-secure to least-secure.</p>
<dd>Example: </p>
<dd>
<pre>set imap_authenticators="gssapi:cram-md5:login"</pre>
<dd><code>Note:</code> Mutt will only fall back to other authentication methods if the previous methods are unavailable. If a method is available but authentication fails, mutt will not connect to the IMAP server. </p>
<dt><code>imap_check_subscribed</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will fetch the set of subscribed folders from your server on connection, and add them to the set of mailboxes it polls for new mail just as if you had issued individual &#8220;mailboxes&#8221; commands. </p>
<dt><code>imap_condstore</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will use the CONDSTORE extension (RFC 7162) if advertised by the server. Mutt&#8217;s current implementation is basic, used only for initial message fetching and flag updates.</p>
<dd>For some IMAP servers, enabling this will slightly speed up downloading initial messages. Unfortunately, Gmail is not one those, and displays worse performance when enabled. Your mileage may vary. </p>
<dt><code>imap_delim_chars</code></p>
<dd>
<pre>Type: string
Default: "/."</pre>
<dd>This contains the list of characters which you would like to treat as folder separators for displaying IMAP paths. In particular it helps in using the &#8220;=&#8221; shortcut for your <i>folder</i> variable. </p>
<dt><code>imap_fetch_chunk_size</code></p>
<dd>
<pre>Type: number (long)
Default: 0</pre>
<dd>When set to a value greater than 0, new headers will be downloaded in sets of this size. If you have a very large mailbox, this might prevent a timeout and disconnect when opening the mailbox, by sending a FETCH per set of this size instead of a single FETCH for all new headers. </p>
<dt><code>imap_headers</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Mutt requests these header fields in addition to the default headers (&#8220;Date:&#8221;, &#8220;From:&#8221;, &#8220;Sender:&#8221;, &#8220;Subject:&#8221;, &#8220;To:&#8221;, &#8220;Cc:&#8221;, &#8220;Message-Id:&#8221;, &#8220;References:&#8221;, &#8220;Content-Type:&#8221;, &#8220;Content-Description:&#8221;, &#8220;In-Reply-To:&#8221;, &#8220;Reply-To:&#8221;, &#8220;Lines:&#8221;, &#8220;List-Post:&#8221;, &#8220;X-Label:&#8221;) from IMAP servers before displaying the index menu. You may want to add more headers for spam detection.</p>
<dd><code>Note:</code> This is a space separated list, items should be uppercase and not contain the colon, e.g. &#8220;X-BOGOSITY X-SPAM-STATUS&#8221; for the &#8220;X-Bogosity:&#8221; and &#8220;X-Spam-Status:&#8221; header fields. </p>
<dt><code>imap_idle</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will attempt to use the IMAP IDLE extension to check for new mail in the current mailbox. Some servers (dovecot was the inspiration for this option) react badly to mutt&#8217;s implementation. If your connection seems to freeze up periodically, try unsetting this. </p>
<dt><code>imap_keepalive</code></p>
<dd>
<pre>Type: number
Default: 300</pre>
<dd>This variable specifies the maximum amount of time in seconds that mutt will wait before polling open IMAP connections, to prevent the server from closing them before mutt has finished with them. The default is well within the RFC-specified minimum amount of time (30 minutes) before a server is allowed to do this, but in practice the RFC does get violated every now and then. Reduce this number if you find yourself getting disconnected from your IMAP server due to inactivity. </p>
<dt><code>imap_list_subscribed</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This variable configures whether IMAP folder browsing will look for only subscribed folders or all folders. This can be toggled in the IMAP browser with the &lt;toggle-subscribed&gt; function. </p>
<dt><code>imap_login</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Your login name on the IMAP server.</p>
<dd>This variable defaults to the value of $imap_user. </p>
<dt><code>imap_oauth_refresh_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>The command to run to generate an OAUTH refresh token for authorizing your connection to your IMAP server. This command will be run on every connection attempt that uses the OAUTHBEARER authentication mechanism. See &#8220;oauth&#8221; for details. </p>
<dt><code>imap_pass</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Specifies the password for your IMAP account. If <i>unset</i>, Mutt will prompt you for your password when you invoke the &lt;imap-fetch-mail&gt; function or try to open an IMAP folder.</p>
<dd><code>Warning</code>: you should only use this option when you are on a fairly secure machine, because the superuser can read your muttrc even if you are the only one who can read the file. </p>
<dt><code>imap_passive</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, mutt will not open new IMAP connections to check for new mail. Mutt will only check for new mail over existing IMAP connections. This is useful if you don&#8217;t want to be prompted for user/password pairs on mutt invocation, or if opening the connection is slow. </p>
<dt><code>imap_peek</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, mutt will avoid implicitly marking your mail as read whenever you fetch a message from the server. This is generally a good thing, but can make closing an IMAP folder somewhat slower. This option exists to appease speed freaks. </p>
<dt><code>imap_pipeline_depth</code></p>
<dd>
<pre>Type: number
Default: 15</pre>
<dd>Controls the number of IMAP commands that may be queued up before they are sent to the server. A deeper pipeline reduces the amount of time mutt must wait for the server, and can make IMAP servers feel much more responsive. But not all servers correctly handle pipelined commands, so if you have problems you might want to try setting this variable to 0.</p>
<dd><code>Note:</code> Changes to this variable have no effect on open connections. </p>
<dt><code>imap_poll_timeout</code></p>
<dd>
<pre>Type: number
Default: 15</pre>
<dd>This variable specifies the maximum amount of time in seconds that mutt will wait for a response when polling IMAP connections for new mail, before timing out and closing the connection. Set to 0 to disable timing out. </p>
<dt><code>imap_qresync</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will use the QRESYNC extension (RFC 7162) if advertised by the server. Mutt&#8217;s current implementation is basic, used only for initial message fetching and flag updates.</p>
<dd>Note: this feature is currently experimental. If you experience strange behavior, such as duplicate or missing messages please file a bug report to let us know. </p>
<dt><code>imap_servernoise</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, mutt will display warning messages from the IMAP server as error messages. Since these messages are often harmless, or generated due to configuration problems on the server which are out of the users&#8217; hands, you may wish to suppress them at some point. </p>
<dt><code>imap_user</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>The name of the user whose mail you intend to access on the IMAP server.</p>
<dd>This variable defaults to your user name on the local machine. </p>
<dt><code>implicit_autoview</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If set to &#8220;yes&#8221;, mutt will look for a mailcap entry with the &#8220;copiousoutput&#8221; flag set for <i>every</i> MIME attachment it doesn&#8217;t have an internal viewer defined for. If such an entry is found, mutt will use the viewer defined in that entry to convert the body part to text form. </p>
<dt><code>include</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>Controls whether or not a copy of the message(s) you are replying to is included in your reply. </p>
<dt><code>include_encrypted</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Controls whether or not Mutt includes separately encrypted attachment contents when replying.</p>
<dd>This variable was added to prevent accidental exposure of encrypted contents when replying to an attacker. If a previously encrypted message were attached by the attacker, they could trick an unwary recipient into decrypting and including the message in their reply. </p>
<dt><code>include_onlyfirst</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Controls whether or not Mutt includes only the first attachment of the message you are replying. </p>
<dt><code>indent_string</code></p>
<dd>
<pre>Type: string
Default: "&gt; "</pre>
<dd>Specifies the string to prepend to each line of text quoted in a message to which you are replying. You are strongly encouraged not to change this value, as it tends to agitate the more fanatical netizens.</p>
<dd>The value of this option is ignored if $text_flowed is set, because the quoting mechanism is strictly defined for format=flowed.</p>
<dd>This option is a format string, please see the description of $index_format for supported <a href="/docs/linux/man/3-printf/">printf</a>(3)-style sequences. </p>
<dt><code>index_format</code></p>
<dd>
<pre>Type: string
Default: "%4C %Z %{%b %d} %-15.15L (%?l?%4l&amp;%4c?) %s"</pre>
<dd>This variable allows you to customize the message index display to your personal taste.</p>
<dd>&#8220;Format strings&#8221; are similar to the strings used in the C function <a href="/docs/linux/man/3-printf/">printf</a>(3) to format output (see the man page for more details). For an explanation of the %? construct, see the $status_format description. The following sequences are defined in Mutt:</p>
<dl>
<dd>
<dl>
<dt>%a</p>
<dd>address of the author</p>
<dt>%A</p>
<dd>reply-to address (if present; otherwise: address of author)</p>
<dt>%b</p>
<dd>filename of the original message folder (think mailbox)</p>
<dt>%B</p>
<dd>the list to which the letter was sent, or else the folder name (%b).</p>
<dt>%c</p>
<dd>number of characters (bytes) in the message (see formatstrings-size)</p>
<dt>%C</p>
<dd>current message number</p>
<dt>%d</p>
<dd>date and time of the message in the format specified by $date_format converted to sender&#8217;s time zone</p>
<dt>%D</p>
<dd>date and time of the message in the format specified by $date_format converted to the local time zone</p>
<dt>%e</p>
<dd>current message number in thread</p>
<dt>%E</p>
<dd>number of messages in current thread</p>
<dt>%f</p>
<dd>sender (address + real name), either From: or Return-Path:</p>
<dt>%F</p>
<dd>author name, or recipient name if the message is from you</p>
<dt>%H</p>
<dd>spam attribute(s) of this message</p>
<dt>%i</p>
<dd>message-id of the current message</p>
<dt>%l</p>
<dd>number of lines in the unprocessed message (may not work with maildir, mh, and IMAP folders)</p>
<dt>%L</p>
<dd>If an address in the &#8220;To:&#8221; or &#8220;Cc:&#8221; header field matches an address defined by the users &#8220;subscribe&#8221; command, this displays &#8220;To &lt;list-name&gt;&#8221;, otherwise the same as %F.</p>
<dt>%m</p>
<dd>total number of message in the mailbox</p>
<dt>%M</p>
<dd>number of hidden messages if the thread is collapsed.</p>
<dt>%N</p>
<dd>message score</p>
<dt>%n</p>
<dd>author&#8217;s real name (or address if missing)</p>
<dt>%O</p>
<dd>original save folder where mutt would formerly have stashed the message: list name or recipient name if not sent to a list</p>
<dt>%P</p>
<dd>progress indicator for the built-in pager (how much of the file has been displayed)</p>
<dt>%r</p>
<dd>comma separated list of &#8220;To:&#8221; recipients</p>
<dt>%R</p>
<dd>comma separated list of &#8220;Cc:&#8221; recipients</p>
<dt>%s</p>
<dd>subject of the message</p>
<dt>%S</p>
<dd>single character status of the message (&#8220;N&#8221;/&#8221;O&#8221;/&#8221;D&#8221;/&#8221;d&#8221;/&#8221;!&#8221;/&#8221;r&#8221;/&#8221;*&#8221;)</p>
<dt>%t</p>
<dd>&#8220;To:&#8221; field (recipients)</p>
<dt>%T</p>
<dd>the appropriate character from the $to_chars string</p>
<dt>%u</p>
<dd>user (login) name of the author</p>
<dt>%v</p>
<dd>first name of the author, or the recipient if the message is from you</p>
<dt>%X</p>
<dd>number of attachments (please see the &#8220;attachments&#8221; section for possible speed effects)</p>
<dt>%y</p>
<dd>&#8220;X-Label:&#8221; field, if present</p>
<dt>%Y</p>
<dd>&#8220;X-Label:&#8221; field, if present, and <i>(1)</i> not at part of a thread tree, <i>(2)</i> at the top of a thread, or <i>(3)</i> &#8220;X-Label:&#8221; is different from preceding message&#8217;s &#8220;X-Label:&#8221;.</p>
<dt>%Z</p>
<dd>a three character set of message status flags. the first character is new/read/replied flags (&#8220;n&#8221;/&#8221;o&#8221;/&#8221;r&#8221;/&#8221;O&#8221;/&#8221;N&#8221;). the second is deleted or encryption flags (&#8220;D&#8221;/&#8221;d&#8221;/&#8221;S&#8221;/&#8221;P&#8221;/&#8221;s&#8221;/&#8221;K&#8221;). the third is either tagged/flagged (&#8220;*&#8221;/&#8221;!&#8221;), or one of the characters listed in $to_chars.</p>
<dt>%@name@</p>
<dd>insert and evaluate format-string from the matching &#8220;index-format-hook&#8221; command</p>
<dt>%{fmt}</p>
<dd>the date and time of the message is converted to sender&#8217;s time zone, and &#8220;fmt&#8221; is expanded by the library function <a href="/docs/linux/man/3-strftime/">strftime</a>(3); a leading bang disables locales</p>
<dt>%[fmt]</p>
<dd>the date and time of the message is converted to the local time zone, and &#8220;fmt&#8221; is expanded by the library function <a href="/docs/linux/man/3-strftime/">strftime</a>(3); a leading bang disables locales</p>
<dt>%(fmt)</p>
<dd>the local date and time when the message was received. &#8220;fmt&#8221; is expanded by the library function <a href="/docs/linux/man/3-strftime/">strftime</a>(3); a leading bang disables locales</p>
<dt>%&lt;fmt&gt;</p>
<dd>the current local time. &#8220;fmt&#8221; is expanded by the library function <a href="/docs/linux/man/3-strftime/">strftime</a>(3); a leading bang disables locales.</p>
<dt>%&gt;X</p>
<dd>right justify the rest of the string and pad with character &#8220;X&#8221;</p>
<dt>%|X</p>
<dd>pad to the end of the line with character &#8220;X&#8221;</p>
<dt>%*X</p>
<dd>soft-fill with character &#8220;X&#8221; as pad</dl>
</dl>
<dd>Note that for mbox/mmdf, &#8220;%l&#8221; applies to the unprocessed message, and for maildir/mh, the value comes from the &#8220;Lines:&#8221; header field when present (the meaning is normally the same). Thus the value depends on the encodings used in the different parts of the message and has little meaning in practice.</p>
<dd>&#8220;Soft-fill&#8221; deserves some explanation: Normal right-justification will print everything to the left of the &#8220;%&gt;&#8221;, displaying padding and whatever lies to the right only if there&#8217;s room. By contrast, soft-fill gives priority to the right-hand side, guaranteeing space to display it and showing padding only if there&#8217;s still room. If necessary, soft-fill will eat text leftwards to make room for rightward text.</p>
<dd>Note that these expandos are supported in &#8220;save-hook&#8221;, &#8220;fcc-hook&#8221;, &#8220;fcc-save-hook&#8221;, and &#8220;index-format-hook&#8221;.</p>
<dd>They are also supported in the configuration variables $attribution, $forward_attribution_intro, $forward_attribution_trailer, $forward_format, $indent_string, $message_format, $pager_format, and $post_indent_string. </p>
<dt><code>ispell</code></p>
<dd>
<pre>Type: path
Default: "ispell"</pre>
<dd>How to invoke ispell (GNU&#8217;s spell-checking software). </p>
<dt><code>keep_flagged</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, read messages marked as flagged will not be moved from your spool mailbox to your $mbox mailbox, or as a result of a &#8220;mbox-hook&#8221; command. </p>
<dt><code>mail_check</code></p>
<dd>
<pre>Type: number
Default: 5</pre>
<dd>This variable configures how often (in seconds) mutt should look for new mail. Also see the $timeout variable. </p>
<dt><code>mail_check_recent</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will only notify you about new mail that has been received since the last time you opened the mailbox. When <i>unset</i>, Mutt will notify you if any new mail exists in the mailbox, regardless of whether you have visited it recently.</p>
<dd>When <i>$mark_old</i> is set, Mutt does not consider the mailbox to contain new mail if only old messages exist. </p>
<dt><code>mail_check_stats</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will periodically calculate message statistics of a mailbox while polling for new mail. It will check for unread, flagged, and total message counts. Because this operation is more performance intensive, it defaults to <i>unset</i>, and has a separate option, $mail_check_stats_interval, to control how often to update these counts.</p>
<dd>Message statistics can also be explicitly calculated by invoking the &lt;check-stats&gt; function. </p>
<dt><code>mail_check_stats_interval</code></p>
<dd>
<pre>Type: number
Default: 60</pre>
<dd>When $mail_check_stats is <i>set</i>, this variable configures how often (in seconds) mutt will update message counts. </p>
<dt><code>mailcap_path</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This variable specifies which files to consult when attempting to display MIME bodies not directly supported by Mutt. The default value is generated during startup: see the &#8220;mailcap&#8221; section of the manual. </p>
<dt><code>mailcap_sanitize</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, mutt will restrict possible characters in mailcap % expandos to a well-defined set of safe characters. This is the safe setting, but we are not sure it doesn&#8217;t break some more advanced MIME stuff.</p>
<dd><code>DON&#8217;T CHANGE THIS SETTING UNLESS YOU ARE REALLY SURE WHAT YOU ARE DOING!</code> </p>
<dt><code>maildir_header_cache_verify</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Check for Maildir unaware programs other than mutt having modified maildir files when the header cache is in use. This incurs one <a href="/docs/linux/man/2-stat/">stat</a>(2) per message every time the folder is opened (which can be very slow for NFS folders). </p>
<dt><code>maildir_trash</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, messages marked as deleted will be saved with the maildir trashed flag instead of unlinked. <code>Note:</code> this only applies to maildir-style mailboxes. Setting it will have no effect on other mailbox types. </p>
<dt><code>maildir_check_cur</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, mutt will poll both the new and cur directories of a maildir folder for new messages. This might be useful if other programs interacting with the folder (e.g. dovecot) are moving new messages to the cur directory. Note that setting this option may slow down polling for new messages in large folders, since mutt has to scan all cur messages. </p>
<dt><code>mark_macro_prefix</code></p>
<dd>
<pre>Type: string
Default: "'"</pre>
<dd>Prefix for macros created using mark-message. A new macro automatically generated with <i>&lt;mark-message&gt;a</i> will be composed from this prefix and the letter <i>a</i>. </p>
<dt><code>mark_old</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls whether or not mutt marks <i>new</i> <code>unread</code> messages as <i>old</i> if you exit a mailbox without reading them. With this option <i>set</i>, the next time you start mutt, the messages will show up with an &#8220;O&#8221; next to them in the index menu, indicating that they are old. </p>
<dt><code>markers</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls the display of wrapped lines in the internal pager. If set, a &#8220;+&#8221; marker is displayed at the beginning of wrapped lines.</p>
<dd>Also see the $smart_wrap variable. </p>
<dt><code>mask</code></p>
<dd>
<pre>Type: regular expression
Default: "!^\.[^.]"</pre>
<dd>A regular expression used in the file browser, optionally preceded by the <i>not</i> operator &#8220;!&#8221;. Only files whose names match this mask will be shown. The match is always case-sensitive. </p>
<dt><code>mbox</code></p>
<dd>
<pre>Type: path
Default: "~/mbox"</pre>
<dd>This specifies the folder into which read mail in your $spoolfile folder will be appended.</p>
<dd>Also see the $move variable. </p>
<dt><code>mbox_type</code></p>
<dd>
<pre>Type: folder magic
Default: mbox</pre>
<dd>The default mailbox type used when creating new folders. May be any of &#8220;mbox&#8221;, &#8220;MMDF&#8221;, &#8220;MH&#8221; and &#8220;Maildir&#8221;. This is overridden by the -m command-line option. </p>
<dt><code>menu_context</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>This variable controls the number of lines of context that are given when scrolling through menus. (Similar to $pager_context.) </p>
<dt><code>menu_move_off</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>unset</i>, the bottom entry of menus will never scroll up past the bottom of the screen, unless there are less entries than lines. When <i>set</i>, the bottom entry may move off the bottom. </p>
<dt><code>menu_scroll</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, menus will be scrolled up or down one line when you attempt to move across a screen boundary. If <i>unset</i>, the screen is cleared and the next or previous page of the menu is displayed (useful for slow links to avoid many redraws). </p>
<dt><code>message_cache_clean</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, mutt will clean out obsolete entries from the message cache when the mailbox is synchronized. You probably only want to set it every once in a while, since it can be a little slow (especially for large folders). </p>
<dt><code>message_cachedir</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>Set this to a directory and mutt will cache copies of messages from your IMAP and POP servers here. You are free to remove entries at any time.</p>
<dd>When setting this variable to a directory, mutt needs to fetch every remote message only once and can perform regular expression searches as fast as for local folders.</p>
<dd>Also see the $message_cache_clean variable. </p>
<dt><code>message_format</code></p>
<dd>
<pre>Type: string
Default: "%s"</pre>
<dd>This is the string displayed in the &#8220;attachment&#8221; menu for attachments of type message/rfc822. For a full listing of defined <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences see the section on $index_format. </p>
<dt><code>meta_key</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, forces Mutt to interpret keystrokes with the high bit (bit 8) set as if the user had pressed the Esc key and whatever key remains after having the high bit removed. For example, if the key pressed has an ASCII value of 0xf8, then this is treated as if the user had pressed Esc then &#8220;x&#8221;. This is because the result of removing the high bit from 0xf8 is 0x78, which is the ASCII character &#8220;x&#8221;. </p>
<dt><code>metoo</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>unset</i>, Mutt will remove your address (see the &#8220;alternates&#8221; command) from the list of recipients when replying to a message. </p>
<dt><code>mh_purge</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>unset</i>, mutt will mimic mh&#8217;s behavior and rename deleted messages to <i>,&lt;old file name&gt;</i> in mh folders instead of really deleting them. This leaves the message on disk but makes programs reading the folder ignore it. If the variable is <i>set</i>, the message files will simply be deleted.</p>
<dd>This option is similar to $maildir_trash for Maildir folders. </p>
<dt><code>mh_seq_flagged</code></p>
<dd>
<pre>Type: string
Default: "flagged"</pre>
<dd>The name of the MH sequence used for flagged messages. </p>
<dt><code>mh_seq_replied</code></p>
<dd>
<pre>Type: string
Default: "replied"</pre>
<dd>The name of the MH sequence used to tag replied messages. </p>
<dt><code>mh_seq_unseen</code></p>
<dd>
<pre>Type: string
Default: "unseen"</pre>
<dd>The name of the MH sequence used for unseen messages. </p>
<dt><code>mime_forward</code></p>
<dd>
<pre>Type: quadoption
Default: no</pre>
<dd>When <i>set</i>, the message you are forwarding will be attached as a separate message/rfc822 MIME part instead of included in the main body of the message. This is useful for forwarding MIME messages so the receiver can properly view the message as it was delivered to you. If you like to switch between MIME and not MIME from mail to mail, set this variable to &#8220;ask-no&#8221; or &#8220;ask-yes&#8221;.</p>
<dd>Also see $forward_decode and $mime_forward_decode. </p>
<dt><code>mime_forward_decode</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Controls the decoding of complex MIME messages into text/plain when forwarding a message while $mime_forward is <i>set</i>. Otherwise $forward_decode is used instead. </p>
<dt><code>mime_forward_rest</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>When forwarding multiple attachments of a MIME message from the attachment menu, attachments which cannot be decoded in a reasonable manner will be attached to the newly composed message if this option is <i>set</i>. </p>
<dt><code>mime_type_query_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This specifies a command to run, to determine the mime type of a new attachment when composing a message. Unless $mime_type_query_first is set, this will only be run if the attachment&#8217;s extension is not found in the mime.types file.</p>
<dd>The string may contain a &#8220;%s&#8221;, which will be substituted with the attachment filename. Mutt will add quotes around the string substituted for &#8220;%s&#8221; automatically according to shell quoting rules, so you should avoid adding your own. If no &#8220;%s&#8221; is found in the string, Mutt will append the attachment filename to the end of the string.</p>
<dd>The command should output a single line containing the attachment&#8217;s mime type.</p>
<dd>Suggested values are &#8220;xdg-mime query filetype&#8221; or &#8220;file -bi&#8221;. </p>
<dt><code>mime_type_query_first</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, the $mime_type_query_command will be run before the mime.types lookup. </p>
<dt><code>mix_entry_format</code></p>
<dd>
<pre>Type: string
Default: "%4n %c %-16s %a"</pre>
<dd>This variable describes the format of a remailer line on the mixmaster chain selection screen. The following <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences are supported:</p>
<dl>
<dd>
<dl>
<dt>%n</p>
<dd>The running number on the menu.</p>
<dt>%c</p>
<dd>Remailer capabilities.</p>
<dt>%s</p>
<dd>The remailer&#8217;s short name.</p>
<dt>%a</p>
<dd>The remailer&#8217;s e-mail address.</dl>
</dl>
<dt><code>mixmaster</code></p>
<dd>
<pre>Type: path
Default: "mixmaster"</pre>
<dd>This variable contains the path to the Mixmaster binary on your system. It is used with various sets of parameters to gather the list of known remailers, and to finally send a message through the mixmaster chain. </p>
<dt><code>move</code></p>
<dd>
<pre>Type: quadoption
Default: no</pre>
<dd>Controls whether or not Mutt will move read messages from your spool mailbox to your $mbox mailbox, or as a result of a &#8220;mbox-hook&#8221; command. </p>
<dt><code>narrow_tree</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This variable, when <i>set</i>, makes the thread tree narrower, allowing deeper threads to fit on the screen. </p>
<dt><code>net_inc</code></p>
<dd>
<pre>Type: number
Default: 10</pre>
<dd>Operations that expect to transfer a large amount of data over the network will update their progress every $net_inc kilobytes. If set to 0, no progress messages will be displayed.</p>
<dd>See also $read_inc, $write_inc and $net_inc. </p>
<dt><code>new_mail_command</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>If <i>set</i>, Mutt will call this command after a new message is received. See the $status_format documentation for the values that can be formatted into this command. </p>
<dt><code>pager</code></p>
<dd>
<pre>Type: path
Default: "builtin"</pre>
<dd>This variable specifies which pager you would like to use to view messages. The value &#8220;builtin&#8221; means to use the built-in pager, otherwise this variable should specify the pathname of the external pager you would like to use.</p>
<dd>Using an external pager may have some disadvantages: Additional keystrokes are necessary because you can&#8217;t call mutt functions directly from the pager, and screen resizes cause lines longer than the screen width to be badly formatted in the help menu.</p>
<dd>When using an external pager, also see $prompt_after which defaults <i>set</i>. </p>
<dt><code>pager_context</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>This variable controls the number of lines of context that are given when displaying the next or previous page in the internal pager. By default, Mutt will display the line after the last one on the screen at the top of the next page (0 lines of context).</p>
<dd>This variable also specifies the amount of context given for search results. If positive, this many lines will be given before a match, if 0, the match will be top-aligned. </p>
<dt><code>pager_format</code></p>
<dd>
<pre>Type: string
Default: "-%Z- %C/%m: %-20.20n %s%* -- (%P)"</pre>
<dd>This variable controls the format of the one-line message &#8220;status&#8221; displayed before each message in either the internal or an external pager. The valid sequences are listed in the $index_format section. </p>
<dt><code>pager_index_lines</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>Determines the number of lines of a mini-index which is shown when in the pager. The current message, unless near the top or bottom of the folder, will be roughly one third of the way down this mini-index, giving the reader the context of a few messages before and after the message. This is useful, for example, to determine how many messages remain to be read in the current thread. One of the lines is reserved for the status bar from the index, so a setting of 6 will only show 5 lines of the actual index. A value of 0 results in no index being shown. If the number of messages in the current folder is less than $pager_index_lines, then the index will only use as many lines as it needs. </p>
<dt><code>pager_stop</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, the internal-pager will <code>not</code> move to the next message when you are at the end of a message and invoke the &lt;next-page&gt; function. </p>
<dt><code>pgp_auto_decode</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, mutt will automatically attempt to decrypt traditional PGP messages whenever the user performs an operation which ordinarily would result in the contents of the message being operated on. For example, if the user displays a pgp-traditional message which has not been manually checked with the &lt;check-traditional-pgp&gt; function, mutt will automatically check the message for traditional pgp. </p>
<dt><code>pgp_autoinline</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This option controls whether Mutt generates old-style inline (traditional) PGP encrypted or signed messages under certain circumstances. This can be overridden by use of the pgp menu, when inline is not required. The GPGME backend does not support this option.</p>
<dd>Note that Mutt might automatically use PGP/MIME for messages which consist of more than a single MIME part. Mutt can be configured to ask before sending PGP/MIME messages when inline (traditional) would not work.</p>
<dd>Also see the $pgp_mime_auto variable.</p>
<dd>Also note that using the old-style PGP message format is <code>strongly</code> <code>deprecated</code>. (PGP only) </p>
<dt><code>pgp_check_exit</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, mutt will check the exit code of the PGP subprocess when signing or encrypting. A non-zero exit code means that the subprocess failed. (PGP only) </p>
<dt><code>pgp_check_gpg_decrypt_status_fd</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, mutt will check the status file descriptor output of $pgp_decrypt_command and $pgp_decode_command for GnuPG status codes indicating successful decryption. This will check for the presence of DECRYPTION_OKAY, absence of DECRYPTION_FAILED, and that all PLAINTEXT occurs between the BEGIN_DECRYPTION and END_DECRYPTION status codes.</p>
<dd>If <i>unset</i>, mutt will instead match the status fd output against $pgp_decryption_okay. (PGP only) </p>
<dt><code>pgp_clearsign_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This format is used to create an old-style &#8220;clearsigned&#8221; PGP message. Note that the use of this format is <code>strongly</code> <code>deprecated</code>.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_decode_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This format strings specifies a command which is used to decode application/pgp attachments.</p>
<dd>The PGP command formats have their own set of <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences:</p>
<dl>
<dd>
<dl>
<dt>%p</p>
<dd>Expands to PGPPASSFD=0 when a pass phrase is needed, to an empty string otherwise. Note: This may be used with a %? construct.</p>
<dt>%f</p>
<dd>Expands to the name of a file containing a message.</p>
<dt>%s</p>
<dd>Expands to the name of a file containing the signature part<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of a multipart/signed attachment when verifying it.</p>
<dt>%a</p>
<dd>The value of $pgp_sign_as if set, otherwise the value of $pgp_default_key.</p>
<dt>%r</p>
<dd>One or more key IDs (or fingerprints if available).</dl>
</dl>
<dd>For examples on how to configure these formats for the various versions of PGP which are floating around, see the pgp and gpg sample configuration files in the samples/ subdirectory which has been installed on your system alongside the documentation. (PGP only) </p>
<dt><code>pgp_decrypt_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to decrypt a PGP encrypted message.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_decryption_okay</code></p>
<dd>
<pre>Type: regular expression
Default: ""</pre>
<dd>If you assign text to this variable, then an encrypted PGP message is only considered successfully decrypted if the output from $pgp_decrypt_command contains the text. This is used to protect against a spoofed encrypted message, with multipart/encrypted headers but containing a block that is not actually encrypted. (e.g. simply signed and ascii armored text).</p>
<dd>Note that if $pgp_check_gpg_decrypt_status_fd is set, this variable is ignored. (PGP only) </p>
<dt><code>pgp_default_key</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This is the default key-pair to use for PGP operations. It will be used for encryption (see $postpone_encrypt and $pgp_self_encrypt).</p>
<dd>It will also be used for signing unless $pgp_sign_as is set.</p>
<dd>The (now deprecated) <i>pgp_self_encrypt_as</i> is an alias for this variable, and should no longer be used. (PGP only) </p>
<dt><code>pgp_encrypt_only_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to encrypt a body part without signing it.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_encrypt_sign_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to both sign and encrypt a body part.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_entry_format</code></p>
<dd>
<pre>Type: string
Default: "%4n %t%f %4l/0x%k %-4a %2c %u"</pre>
<dd>This variable allows you to customize the PGP key selection menu to your personal taste. This string is similar to $index_format, but has its own set of <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences:</p>
<dl>
<dd>
<dl>
<dt>%n</p>
<dd>number</p>
<dt>%k</p>
<dd>key id</p>
<dt>%u</p>
<dd>user id</p>
<dt>%a</p>
<dd>algorithm</p>
<dt>%l</p>
<dd>key length</p>
<dt>%f</p>
<dd>flags</p>
<dt>%c</p>
<dd>capabilities</p>
<dt>%t</p>
<dd>trust/validity of the key-uid association</p>
<dt>%[&lt;s&gt;]</p>
<dd>date of the key where &lt;s&gt; is an <a href="/docs/linux/man/3-strftime/">strftime</a>(3) expression</dl>
</dl>
<dd>(PGP only) </p>
<dt><code>pgp_export_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to export a public key from the user&#8217;s key ring.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_getkeys_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is invoked whenever Mutt needs to fetch the public key associated with an email address. Of the sequences supported by $pgp_decode_command, %r is the only <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequence used with this format. Note that in this case, %r expands to the email address, not the public key ID (the key ID is unknown, which is why Mutt is invoking this command). (PGP only) </p>
<dt><code>pgp_good_sign</code></p>
<dd>
<pre>Type: regular expression
Default: ""</pre>
<dd>If you assign a text to this variable, then a PGP signature is only considered verified if the output from $pgp_verify_command contains the text. Use this variable if the exit code from the command is 0 even for bad signatures. (PGP only) </p>
<dt><code>pgp_ignore_subkeys</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Setting this variable will cause Mutt to ignore OpenPGP subkeys. Instead, the principal key will inherit the subkeys&#8217; capabilities. <i>Unset</i> this if you want to play interesting key selection games. (PGP only) </p>
<dt><code>pgp_import_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to import a key from a message into the user&#8217;s public key ring.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_list_pubring_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to list the public key ring&#8217;s contents. The output format must be analogous to the one used by </p>
<dd>
<pre>gpg --list-keys --with-colons --with-fingerprint</pre>
<dd>This format is also generated by the mutt_pgpring utility which comes with mutt.</p>
<dd>Note: gpg&#8217;s fixed-list-mode option should not be used. It produces a different date format which may result in mutt showing incorrect key generation dates.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. Note that in this case, %r expands to the search string, which is a list of one or more quoted values such as email address, name, or keyid. (PGP only) </p>
<dt><code>pgp_list_secring_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to list the secret key ring&#8217;s contents. The output format must be analogous to the one used by: </p>
<dd>
<pre>gpg --list-keys --with-colons --with-fingerprint</pre>
<dd>This format is also generated by the mutt_pgpring utility which comes with mutt.</p>
<dd>Note: gpg&#8217;s fixed-list-mode option should not be used. It produces a different date format which may result in mutt showing incorrect key generation dates.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. Note that in this case, %r expands to the search string, which is a list of one or more quoted values such as email address, name, or keyid. (PGP only) </p>
<dt><code>pgp_long_ids</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, use 64 bit PGP key IDs, if <i>unset</i> use the normal 32 bit key IDs. NOTE: Internally, Mutt has transitioned to using fingerprints (or long key IDs as a fallback). This option now only controls the display of key IDs in the key selection menu and a few other places. (PGP only) </p>
<dt><code>pgp_mime_auto</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>This option controls whether Mutt will prompt you for automatically sending a (signed/encrypted) message using PGP/MIME when inline (traditional) fails (for any reason).</p>
<dd>Also note that using the old-style PGP message format is <code>strongly</code> <code>deprecated</code>. (PGP only) </p>
<dt><code>pgp_replyinline</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Setting this variable will cause Mutt to always attempt to create an inline (traditional) message when replying to a message which is PGP encrypted/signed inline. This can be overridden by use of the pgp menu, when inline is not required. This option does not automatically detect if the (replied-to) message is inline; instead it relies on Mutt internals for previously checked/flagged messages.</p>
<dd>Note that Mutt might automatically use PGP/MIME for messages which consist of more than a single MIME part. Mutt can be configured to ask before sending PGP/MIME messages when inline (traditional) would not work.</p>
<dd>Also see the $pgp_mime_auto variable.</p>
<dd>Also note that using the old-style PGP message format is <code>strongly</code> <code>deprecated</code>. (PGP only) </p>
<dt><code>pgp_retainable_sigs</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, signed and encrypted messages will consist of nested multipart/signed and multipart/encrypted body parts.</p>
<dd>This is useful for applications like encrypted and signed mailing lists, where the outer layer (multipart/encrypted) can be easily removed, while the inner multipart/signed part is retained. (PGP only) </p>
<dt><code>pgp_self_encrypt</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, PGP encrypted messages will also be encrypted using the key in $pgp_default_key. (PGP only) </p>
<dt><code>pgp_show_unusable</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, mutt will display non-usable keys on the PGP key selection menu. This includes keys which have been revoked, have expired, or have been marked as &#8220;disabled&#8221; by the user. (PGP only) </p>
<dt><code>pgp_sign_as</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>If you have a different key pair to use for signing, you should set this to the signing key. Most people will only need to set $pgp_default_key. It is recommended that you use the keyid form to specify your key (e.g. 0x00112233). (PGP only) </p>
<dt><code>pgp_sign_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to create the detached PGP signature for a multipart/signed PGP/MIME body part.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_sort_keys</code></p>
<dd>
<pre>Type: sort order
Default: address</pre>
<dd>Specifies how the entries in the pgp menu are sorted. The following are legal values:</p>
<dl>
<dd>
<dl>
<dt>address</p>
<dd>sort alphabetically by user id</p>
<dt>keyid</p>
<dd>sort alphabetically by key id</p>
<dt>date</p>
<dd>sort by key creation date</p>
<dt>trust</p>
<dd>sort by the trust of the key</dl>
</dl>
<dd>If you prefer reverse order of the above values, prefix it with &#8220;reverse-&#8220;. (PGP only) </p>
<dt><code>pgp_strict_enc</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, Mutt will automatically encode PGP/MIME signed messages as quoted-printable. Please note that unsetting this variable may lead to problems with non-verifyable PGP signatures, so only change this if you know what you are doing. (PGP only) </p>
<dt><code>pgp_timeout</code></p>
<dd>
<pre>Type: number (long)
Default: 300</pre>
<dd>The number of seconds after which a cached passphrase will expire if not used. (PGP only) </p>
<dt><code>pgp_use_gpg_agent</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, mutt expects a <a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a>(1) process will handle private key passphrase prompts. If <i>unset</i>, mutt will prompt for the passphrase and pass it via stdin to the pgp command.</p>
<dd>Note that as of version 2.1, GnuPG automatically spawns an agent and requires the agent be used for passphrase management. Since that version is increasingly prevalent, this variable now defaults <i>set</i>.</p>
<dd>Mutt works with a GUI or curses pinentry program. A TTY pinentry should not be used.</p>
<dd>If you are using an older version of GnuPG without an agent running, or another encryption program without an agent, you will need to <i>unset</i> this variable. (PGP only) </p>
<dt><code>pgp_verify_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to verify PGP signatures.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pgp_verify_key_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to verify key information from the key selection menu.</p>
<dd>This is a format string, see the $pgp_decode_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (PGP only) </p>
<dt><code>pipe_decode</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Used in connection with the &lt;pipe-message&gt; command. When <i>unset</i>, Mutt will pipe the messages without any preprocessing. When <i>set</i>, Mutt will weed headers and will attempt to decode the messages first. </p>
<dt><code>pipe_sep</code></p>
<dd>
<pre>Type: string
Default: "
"</pre>
<dd>The separator to add between messages when piping a list of tagged messages to an external Unix command. </p>
<dt><code>pipe_split</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Used in connection with the &lt;pipe-message&gt; function following &lt;tag-prefix&gt;. If this variable is <i>unset</i>, when piping a list of tagged messages Mutt will concatenate the messages and will pipe them all concatenated. When <i>set</i>, Mutt will pipe the messages one by one. In both cases the messages are piped in the current sorted order, and the $pipe_sep separator is added after each message. </p>
<dt><code>pop_auth_try_all</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, Mutt will try all available authentication methods. When <i>unset</i>, Mutt will only fall back to other authentication methods if the previous methods are unavailable. If a method is available but authentication fails, Mutt will not connect to the POP server. </p>
<dt><code>pop_authenticators</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This is a colon-delimited list of authentication methods mutt may attempt to use to log in to an POP server, in the order mutt should try them. Authentication methods are either &#8220;user&#8221;, &#8220;apop&#8221; or any SASL mechanism, e.g. &#8220;digest-md5&#8221;, &#8220;gssapi&#8221; or &#8220;cram-md5&#8221;. This option is case-insensitive. If this option is <i>unset</i> (the default) mutt will try all available methods, in order from most-secure to least-secure.</p>
<dd>Example: </p>
<dd>
<pre>set pop_authenticators="digest-md5:apop:user"</pre>
<dt><code>pop_checkinterval</code></p>
<dd>
<pre>Type: number
Default: 60</pre>
<dd>This variable configures how often (in seconds) mutt should look for new mail in the currently selected mailbox if it is a POP mailbox. </p>
<dt><code>pop_delete</code></p>
<dd>
<pre>Type: quadoption
Default: ask-no</pre>
<dd>If <i>set</i>, Mutt will delete successfully downloaded messages from the POP server when using the &lt;fetch-mail&gt; function. When <i>unset</i>, Mutt will download messages but also leave them on the POP server. </p>
<dt><code>pop_host</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>The name of your POP server for the &lt;fetch-mail&gt; function. You can also specify an alternative port, username and password, i.e.: </p>
<dd>
<pre>[pop[s]://][username[:password]@]popserver[:port]</pre>
<dd>where &#8220;[&#8230;]&#8221; denotes an optional part. </p>
<dt><code>pop_last</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If this variable is <i>set</i>, mutt will try to use the &#8220;LAST&#8221; POP command for retrieving only unread messages from the POP server when using the &lt;fetch-mail&gt; function. </p>
<dt><code>pop_oauth_refresh_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>The command to run to generate an OAUTH refresh token for authorizing your connection to your POP server. This command will be run on every connection attempt that uses the OAUTHBEARER authentication mechanism. See &#8220;oauth&#8221; for details. </p>
<dt><code>pop_pass</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Specifies the password for your POP account. If <i>unset</i>, Mutt will prompt you for your password when you open a POP mailbox.</p>
<dd><code>Warning</code>: you should only use this option when you are on a fairly secure machine, because the superuser can read your muttrc even if you are the only one who can read the file. </p>
<dt><code>pop_reconnect</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>Controls whether or not Mutt will try to reconnect to the POP server if the connection is lost. </p>
<dt><code>pop_user</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Your login name on the POP server.</p>
<dd>This variable defaults to your user name on the local machine. </p>
<dt><code>post_indent_string</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Similar to the $attribution variable, Mutt will append this string after the inclusion of a message which is being replied to. For a full listing of defined <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences see the section on $index_format. </p>
<dt><code>postpone</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>Controls whether or not messages are saved in the $postponed mailbox when you elect not to send immediately.</p>
<dd>Also see the $recall variable. </p>
<dt><code>postponed</code></p>
<dd>
<pre>Type: path
Default: "~/postponed"</pre>
<dd>Mutt allows you to indefinitely &#8220;postpone sending a message&#8221; which you are editing. When you choose to postpone a message, Mutt saves it in the mailbox specified by this variable.</p>
<dd>Also see the $postpone variable. </p>
<dt><code>postpone_encrypt</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, postponed messages that are marked for encryption will be self-encrypted. Mutt will first try to encrypt using the value specified in $pgp_default_key or $smime_default_key. If those are not set, it will try the deprecated $postpone_encrypt_as. (Crypto only) </p>
<dt><code>postpone_encrypt_as</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This is a deprecated fall-back variable for $postpone_encrypt. Please use $pgp_default_key or $smime_default_key. (Crypto only) </p>
<dt><code>preconnect</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>If <i>set</i>, a shell command to be executed if mutt fails to establish a connection to the server. This is useful for setting up secure connections, e.g. with <a href="/docs/linux/man/1-ssh/">ssh</a>(1). If the command returns a nonzero status, mutt gives up opening the server. Example: </p>
<dd>
<pre>set preconnect="ssh -f -q -L 1234:mailhost.net:143 mailhost.net \
sleep 20 &lt; /dev/null &gt; /dev/null"</pre>
<dd>Mailbox &#8220;foo&#8221; on &#8220;mailhost.net&#8221; can now be reached as &#8220;{localhost:1234}foo&#8221;.</p>
<dd>Note: For this example to work, you must be able to log in to the remote machine without having to enter a password. </p>
<dt><code>print</code></p>
<dd>
<pre>Type: quadoption
Default: ask-no</pre>
<dd>Controls whether or not Mutt really prints messages. This is set to &#8220;ask-no&#8221; by default, because some people accidentally hit &#8220;p&#8221; often. </p>
<dt><code>print_command</code></p>
<dd>
<pre>Type: path
Default: "lpr"</pre>
<dd>This specifies the command pipe that should be used to print messages. </p>
<dt><code>print_decode</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Used in connection with the &lt;print-message&gt; command. If this option is <i>set</i>, the message is decoded before it is passed to the external command specified by $print_command. If this option is <i>unset</i>, no processing will be applied to the message when printing it. The latter setting may be useful if you are using some advanced printer filter which is able to properly format e-mail messages for printing. </p>
<dt><code>print_split</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Used in connection with the &lt;print-message&gt; command. If this option is <i>set</i>, the command specified by $print_command is executed once for each message which is to be printed. If this option is <i>unset</i>, the command specified by $print_command is executed only once, and all the messages are concatenated, with a form feed as the message separator.</p>
<dd>Those who use the <a href="/docs/linux/man/1-enscript/">enscript</a>(1) program&#8217;s mail-printing mode will most likely want to <i>set</i> this option. </p>
<dt><code>prompt_after</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If you use an <i>external</i> $pager, setting this variable will cause Mutt to prompt you for a command when the pager exits rather than returning to the index menu. If <i>unset</i>, Mutt will return to the index menu when the external pager exits. </p>
<dt><code>query_command</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>This specifies the command Mutt will use to make external address queries. The string may contain a &#8220;%s&#8221;, which will be substituted with the query string the user types. Mutt will add quotes around the string substituted for &#8220;%s&#8221; automatically according to shell quoting rules, so you should avoid adding your own. If no &#8220;%s&#8221; is found in the string, Mutt will append the user&#8217;s query to the end of the string. See &#8220;query&#8221; for more information. </p>
<dt><code>query_format</code></p>
<dd>
<pre>Type: string
Default: "%4c %t %-25.25a %-25.25n %?e?(%e)?"</pre>
<dd>This variable describes the format of the &#8220;query&#8221; menu. The following <a href="/docs/linux/man/3-printf/">printf</a>(3)-style sequences are understood:</p>
<dl>
<dd>
<dl>
<dt>%a</p>
<dd>destination address</p>
<dt>%c</p>
<dd>current entry number</p>
<dt>%e</p>
<dd>extra information *</p>
<dt>%n</p>
<dd>destination name</p>
<dt>%t</p>
<dd>&#8220;*&#8221; if current entry is tagged, a space otherwise</p>
<dt>%&gt;X</p>
<dd>right justify the rest of the string and pad with &#8220;X&#8221;</p>
<dt>%|X</p>
<dd>pad to the end of the line with &#8220;X&#8221;</p>
<dt>%*X</p>
<dd>soft-fill with character &#8220;X&#8221; as pad</dl>
</dl>
<dd>For an explanation of &#8220;soft-fill&#8221;, see the $index_format documentation.</p>
<dd>* = can be optionally printed if nonzero, see the $status_format documentation. </p>
<dt><code>quit</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>This variable controls whether &#8220;quit&#8221; and &#8220;exit&#8221; actually quit from mutt. If this option is <i>set</i>, they do quit, if it is <i>unset</i>, they have no effect, and if it is set to <i>ask-yes</i> or <i>ask-no</i>, you are prompted for confirmation when you try to quit. </p>
<dt><code>quote_regexp</code></p>
<dd>
<pre>Type: regular expression
Default: "^([ 	]*[|&gt;:}#])+"</pre>
<dd>A regular expression used in the internal pager to determine quoted sections of text in the body of a message. Quoted text may be filtered out using the &lt;toggle-quoted&gt; command, or colored according to the &#8220;color quoted&#8221; family of directives.</p>
<dd>Higher levels of quoting may be colored differently (&#8220;color quoted1&#8221;, &#8220;color quoted2&#8221;, etc.). The quoting level is determined by removing the last character from the matched text and recursively reapplying the regular expression until it fails to produce a match.</p>
<dd>Match detection may be overridden by the $smileys regular expression. </p>
<dt><code>read_inc</code></p>
<dd>
<pre>Type: number
Default: 10</pre>
<dd>If set to a value greater than 0, Mutt will display which message it is currently on when reading a mailbox or when performing search actions such as search and limit. The message is printed after this many messages have been read or searched (e.g., if set to 25, Mutt will print a message when it is at message 25, and then again when it gets to message 50). This variable is meant to indicate progress when reading or searching large mailboxes which may take some time. When set to 0, only a single message will appear before the reading the mailbox.</p>
<dd>Also see the $write_inc, $net_inc and $time_inc variables and the &#8220;tuning&#8221; section of the manual for performance considerations. </p>
<dt><code>read_only</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, all folders are opened in read-only mode. </p>
<dt><code>realname</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This variable specifies what &#8220;real&#8221; or &#8220;personal&#8221; name should be used when sending messages.</p>
<dd>By default, this is the GECOS field from /etc/passwd. Note that this variable will <i>not</i> be used when the user has set a real name in the $from variable. </p>
<dt><code>recall</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>Controls whether or not Mutt recalls postponed messages when composing a new message.</p>
<dd>Setting this variable to <i>yes</i> is not generally useful, and thus not recommended. Note that the &lt;recall-message&gt; function can be used to manually recall postponed messages.</p>
<dd>Also see $postponed variable. </p>
<dt><code>record</code></p>
<dd>
<pre>Type: path
Default: "~/sent"</pre>
<dd>This specifies the file into which your outgoing messages should be appended. (This is meant as the primary method for saving a copy of your messages, but another way to do this is using the &#8220;my_hdr&#8221; command to create a &#8220;Bcc:&#8221; field with your email address in it.)</p>
<dd>The value of <i>$record</i> is overridden by the $force_name and $save_name variables, and the &#8220;fcc-hook&#8221; command. Also see $copy and $write_bcc. </p>
<dt><code>reflow_space_quotes</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>This option controls how quotes from format=flowed messages are displayed in the pager and when replying (with $text_flowed <i>unset</i>). When set, this option adds spaces after each level of quote marks, turning &#8220;&gt;&gt;&gt;foo&#8221; into &#8220;&gt; &gt; &gt; foo&#8221;.</p>
<dd><code>Note:</code> If $reflow_text is <i>unset</i>, this option has no effect. Also, this option does not affect replies when $text_flowed is <i>set</i>. </p>
<dt><code>reflow_text</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will reformat paragraphs in text/plain parts marked format=flowed. If <i>unset</i>, Mutt will display paragraphs unaltered from how they appear in the message body. See RFC3676 for details on the <i>format=flowed</i> format.</p>
<dd>Also see $reflow_wrap, and $wrap. </p>
<dt><code>reflow_wrap</code></p>
<dd>
<pre>Type: number
Default: 78</pre>
<dd>This variable controls the maximum paragraph width when reformatting text/plain parts when $reflow_text is <i>set</i>. When the value is 0, paragraphs will be wrapped at the terminal&#8217;s right margin. A positive value sets the paragraph width relative to the left margin. A negative value set the paragraph width relative to the right margin.</p>
<dd>Also see $wrap. </p>
<dt><code>reply_regexp</code></p>
<dd>
<pre>Type: regular expression
Default: "^(re([\[0-9\]+])*|aw):[ 	]*"</pre>
<dd>A regular expression used to recognize reply messages when threading and replying. The default value corresponds to the English &#8220;Re:&#8221; and the German &#8220;Aw:&#8221;. </p>
<dt><code>reply_self</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>unset</i> and you are replying to a message sent by you, Mutt will assume that you want to reply to the recipients of that message rather than to yourself.</p>
<dd>Also see the &#8220;alternates&#8221; command. </p>
<dt><code>reply_to</code></p>
<dd>
<pre>Type: quadoption
Default: ask-yes</pre>
<dd>If <i>set</i>, when replying to a message, Mutt will use the address listed in the Reply-to: header as the recipient of the reply. If <i>unset</i>, it will use the address in the From: header field instead. This option is useful for reading a mailing list that sets the Reply-To: header field to the list address and you want to send a private message to the author of a message. </p>
<dt><code>resolve</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, the cursor will be automatically advanced to the next (possibly undeleted) message whenever a command that modifies the current message is executed. </p>
<dt><code>resume_draft_files</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, draft files (specified by -H on the command line) are processed similarly to when resuming a postponed message. Recipients are not prompted for; send-hooks are not evaluated; no alias expansion takes place; user-defined headers and signatures are not added to the message. </p>
<dt><code>resume_edited_draft_files</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, draft files previously edited (via -E -H on the command line) will have $resume_draft_files automatically set when they are used as a draft file again.</p>
<dd>The first time a draft file is saved, mutt will add a header, X-Mutt-Resume-Draft to the saved file. The next time the draft file is read in, if mutt sees the header, it will set $resume_draft_files.</p>
<dd>This option is designed to prevent multiple signatures, user-defined headers, and other processing effects from being made multiple times to the draft file. </p>
<dt><code>reverse_alias</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This variable controls whether or not Mutt will display the &#8220;personal&#8221; name from your aliases in the index menu if it finds an alias that matches the message&#8217;s sender. For example, if you have the following alias: </p>
<dd>
<pre>alias juser abd30425 [at] somewhere.net (Joe User)</pre>
<dd>and then you receive mail which contains the following header: </p>
<dd>
<pre>From: abd30425 [at] somewhere.net</pre>
<dd>It would be displayed in the index menu as &#8220;Joe User&#8221; instead of &#8220;abd30425 [at] somewhere.net.&#8221; This is useful when the person&#8217;s e-mail address is not human friendly. </p>
<dt><code>reverse_name</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>It may sometimes arrive that you receive mail to a certain machine, move the messages to another machine, and reply to some the messages from there. If this variable is <i>set</i>, the default <i>From:</i> line of the reply messages is built using the address where you received the messages you are replying to <code>if</code> that address matches your &#8220;alternates&#8221;. If the variable is <i>unset</i>, or the address that would be used doesn&#8217;t match your &#8220;alternates&#8221;, the <i>From:</i> line will use your address on the current machine.</p>
<dd>Also see the &#8220;alternates&#8221; command and $reverse_realname. </p>
<dt><code>reverse_realname</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>This variable fine-tunes the behavior of the $reverse_name feature.</p>
<dd>When it is <i>unset</i>, Mutt will remove the real name part of a matching address. This allows the use of the email address without having to also use what the sender put in the real name field.</p>
<dd>When it is <i>set</i>, Mutt will use the matching address as-is.</p>
<dd>In either case, a missing real name will be filled in afterwards using the value of $realname. </p>
<dt><code>rfc2047_parameters</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When this variable is <i>set</i>, Mutt will decode RFC2047-encoded MIME parameters. You want to set this variable when mutt suggests you to save attachments to files named like: </p>
<dd>
<pre>=?iso-8859-1?Q?file=5F=E4=5F991116=2Ezip?=</pre>
<dd>When this variable is <i>set</i> interactively, the change won&#8217;t be active until you change folders.</p>
<dd>Note that this use of RFC2047&#8217;s encoding is explicitly prohibited by the standard, but nevertheless encountered in the wild.</p>
<dd>Also note that setting this parameter will <i>not</i> have the effect that mutt <i>generates</i> this kind of encoding. Instead, mutt will unconditionally use the encoding specified in RFC2231. </p>
<dt><code>save_address</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, mutt will take the sender&#8217;s full address when choosing a default folder for saving a mail. If $save_name or $force_name is <i>set</i> too, the selection of the Fcc folder will be changed as well. </p>
<dt><code>save_empty</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>unset</i>, mailboxes which contain no saved messages will be removed when closed (the exception is $spoolfile which is never removed). If <i>set</i>, mailboxes are never removed.</p>
<dd><code>Note:</code> This only applies to mbox and MMDF folders, Mutt does not delete MH and Maildir directories. </p>
<dt><code>save_history</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>This variable controls the size of the history (per category) saved in the $history_file file. </p>
<dt><code>save_name</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This variable controls how copies of outgoing messages are saved. When <i>set</i>, a check is made to see if a mailbox specified by the recipient address exists (this is done by searching for a mailbox in the $folder directory with the <i>username</i> part of the recipient address). If the mailbox exists, the outgoing message will be saved to that mailbox, otherwise the message is saved to the $record mailbox.</p>
<dd>Also see the $force_name variable. </p>
<dt><code>score</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When this variable is <i>unset</i>, scoring is turned off. This can be useful to selectively disable scoring for certain folders when the $score_threshold_delete variable and related are used. </p>
<dt><code>score_threshold_delete</code></p>
<dd>
<pre>Type: number
Default: -1</pre>
<dd>Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked for deletion by mutt. Since mutt scores are always greater than or equal to zero, the default setting of this variable will never mark a message for deletion. </p>
<dt><code>score_threshold_flag</code></p>
<dd>
<pre>Type: number
Default: 9999</pre>
<dd>Messages which have been assigned a score greater than or equal to this variable&#8217;s value are automatically marked &#8220;flagged&#8221;. </p>
<dt><code>score_threshold_read</code></p>
<dd>
<pre>Type: number
Default: -1</pre>
<dd>Messages which have been assigned a score equal to or lower than the value of this variable are automatically marked as read by mutt. Since mutt scores are always greater than or equal to zero, the default setting of this variable will never mark a message read. </p>
<dt><code>search_context</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>For the pager, this variable specifies the number of lines shown before search results. By default, search results will be top-aligned. </p>
<dt><code>send_charset</code></p>
<dd>
<pre>Type: string
Default: "us-ascii:iso-8859-1:utf-8"</pre>
<dd>A colon-delimited list of character sets for outgoing messages. Mutt will use the first character set into which the text can be converted exactly. If your $charset is not &#8220;iso-8859-1&#8221; and recipients may not understand &#8220;UTF-8&#8221;, it is advisable to include in the list an appropriate widely used standard character set (such as &#8220;iso-8859-2&#8221;, &#8220;koi8-r&#8221; or &#8220;iso-2022-jp&#8221;) either instead of or after &#8220;iso-8859-1&#8221;.</p>
<dd>In case the text cannot be converted into one of these exactly, mutt uses $charset as a fallback. </p>
<dt><code>send_multipart_alternative</code></p>
<dd>
<pre>Type: quadoption
Default: no</pre>
<dd>If <i>set</i>, Mutt will generate a multipart/alternative container and an alternative part using the filter script specified in $send_multipart_alternative_filter. See the section &#8220;MIME Multipart/Alternative&#8221; (alternative-order).</p>
<dd>Note that enabling multipart/alternative is not compatible with inline PGP encryption. Mutt will prompt to use PGP/MIME in that case. </p>
<dt><code>send_multipart_alternative_filter</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>This specifies a filter script, which will convert the main (composed) message of the email to an alternative format. The message will be piped to the filter&#8217;s stdin. The expected output of the filter is the generated mime type, e.g. text/html, followed by a blank line, and then the converted content. See the section &#8220;MIME Multipart/Alternative&#8221; (alternative-order). </p>
<dt><code>sendmail</code></p>
<dd>
<pre>Type: path
Default: "/usr/sbin/sendmail -oem -oi"</pre>
<dd>Specifies the program and arguments used to deliver mail sent by Mutt. Mutt expects that the specified program interprets additional arguments as recipient addresses. Mutt appends all recipients after adding a &#8212; delimiter (if not already present). Additional flags, such as for $use_8bitmime, $use_envelope_from, $dsn_notify, or $dsn_return will be added before the delimiter.</p>
<dd><code>See also:</code> $write_bcc. </p>
<dt><code>sendmail_wait</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>Specifies the number of seconds to wait for the $sendmail process to finish before giving up and putting delivery in the background.</p>
<dd>Mutt interprets the value of this variable as follows:</p>
<dl>
<dd>
<dl>
<dt>&gt;0</p>
<dd>number of seconds to wait for sendmail to finish before continuing</p>
<dt>0</p>
<dd>wait forever for sendmail to finish</p>
<dt>&lt;0</p>
<dd>always put sendmail in the background without waiting</dl>
</dl>
<dd>Note that if you specify a value other than 0, the output of the child process will be put in a temporary file. If there is some error, you will be informed as to where to find the output. </p>
<dt><code>shell</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>Command to use when spawning a subshell. By default, the user&#8217;s login shell from /etc/passwd is used. </p>
<dt><code>sidebar_delim_chars</code></p>
<dd>
<pre>Type: string
Default: "/."</pre>
<dd>This contains the list of characters which you would like to treat as folder separators for displaying paths in the sidebar.</p>
<dd>Local mail is often arranged in directories: `dir1/dir2/mailbox&#8217;. </p>
<dd>
<pre>set sidebar_delim_chars='/'</pre>
<dd>IMAP mailboxes are often named: `folder1.folder2.mailbox&#8217;. </p>
<dd>
<pre>set sidebar_delim_chars='.'</pre>
<dd><code>See also:</code> $sidebar_short_path, $sidebar_folder_indent, $sidebar_indent_string. </p>
<dt><code>sidebar_divider_char</code></p>
<dd>
<pre>Type: string
Default: "|"</pre>
<dd>This specifies the characters to be drawn between the sidebar (when visible) and the other Mutt panels. ASCII and Unicode line-drawing characters are supported. </p>
<dt><code>sidebar_folder_indent</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Set this to indent mailboxes in the sidebar.</p>
<dd><code>See also:</code> $sidebar_short_path, $sidebar_indent_string, $sidebar_delim_chars. </p>
<dt><code>sidebar_format</code></p>
<dd>
<pre>Type: string
Default: "%B%* %n"</pre>
<dd>This variable allows you to customize the sidebar display. This string is similar to $index_format, but has its own set of <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences:</p>
<dl>
<dd>
<dl>
<dt>%B</p>
<dd>Name of the mailbox</p>
<dt>%S</p>
<dd>* Size of mailbox (total number of messages)</p>
<dt>%N</p>
<dd>* Number of unread messages in the mailbox</p>
<dt>%n</p>
<dd>N if mailbox has new mail, blank otherwise</p>
<dt>%F</p>
<dd>* Number of Flagged messages in the mailbox</p>
<dt>%!</p>
<dd>&#8220;!&#8221; : one flagged message; &#8220;!!&#8221; : two flagged messages; &#8220;n!&#8221; : n flagged messages (for n &gt; 2). Otherwise prints nothing.</p>
<dt>%d</p>
<dd>* @ Number of deleted messages</p>
<dt>%L</p>
<dd>* @ Number of messages after limiting</p>
<dt>%t</p>
<dd>* @ Number of tagged messages</p>
<dt>%&gt;X</p>
<dd>right justify the rest of the string and pad with &#8220;X&#8221;</p>
<dt>%|X</p>
<dd>pad to the end of the line with &#8220;X&#8221;</p>
<dt>%*X</p>
<dd>soft-fill with character &#8220;X&#8221; as pad</dl>
</dl>
<dd>* = Can be optionally printed if nonzero @ = Only applicable to the current folder</p>
<dd>In order to use %S, %N, %F, and %!, $mail_check_stats must be <i>set</i>. When thus set, a suggested value for this option is &#8220;%B%?F? [%F]?%* %?N?%N/?%S&#8221;. </p>
<dt><code>sidebar_indent_string</code></p>
<dd>
<pre>Type: string
Default: " "</pre>
<dd>This specifies the string that is used to indent mailboxes in the sidebar. It defaults to two spaces.</p>
<dd><code>See also:</code> $sidebar_short_path, $sidebar_folder_indent, $sidebar_delim_chars. </p>
<dt><code>sidebar_new_mail_only</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When set, the sidebar will only display mailboxes containing new, or flagged, mail.</p>
<dd><code>See also:</code> sidebar_whitelist. </p>
<dt><code>sidebar_next_new_wrap</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When set, the &lt;sidebar-next-new&gt; command will not stop and the end of the list of mailboxes, but wrap around to the beginning. The &lt;sidebar-prev-new&gt; command is similarly affected, wrapping around to the end of the list. </p>
<dt><code>sidebar_relative_shortpath_indent</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When set, this option changes how $sidebar_short_path and $sidebar_folder_indent perform shortening and indentation: both will look at the previous sidebar entries and shorten/indent relative to the most recent parent.</p>
<dd>An example of this option set/unset for mailboxes listed in this order, with $sidebar_short_path=yes, $sidebar_folder_indent=yes, and $sidebar_indent_string=&#8221;→&#8221;:</p>
<dl>
<dd>
<dl>
<dt><code>mailbox</code></p>
<dd><code>set</code> <code>unset</code></p>
<dt>=a.b</p>
<dd>=a.b →b</p>
<dt>=a.b.c.d</p>
<dd>→c.d →→→d</p>
<dt>=a.b.e</p>
<dd>→e →→e</dl>
</dl>
<dd>The second line illustrates most clearly. With this option set, =a.b.c.d is shortened relative to =a.b, becoming c.d; it is also indented one place relative to =a.b. With this option unset =a.b.c.d is always shortened to the last part of the mailbox, d and is indented three places, with respect to $folder (represented by &#8216;=&#8217;).</p>
<dd>When set, the third line will also be indented and shortened relative to the first line. </p>
<dt><code>sidebar_short_path</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>By default the sidebar will show the mailbox&#8217;s path, relative to the $folder variable. Setting sidebar_shortpath=yes will shorten the names relative to the previous name. Here&#8217;s an example:</p>
<dl>
<dd>
<dl>
<dt><code>shortpath=no</code></p>
<dd><code>shortpath=yes</code> <code>shortpath=yes, folderindent=yes, indentstr=&#8221;..&#8221;</code></p>
<dt>fruit</p>
<dd>fruit fruit</p>
<dt>fruit.apple</p>
<dd>apple ..apple</p>
<dt>fruit.banana</p>
<dd>banana ..banana</p>
<dt>fruit.cherry</p>
<dd>cherry ..cherry</dl>
</dl>
<dd><code>See also:</code> $sidebar_delim_chars, $sidebar_folder_indent, $sidebar_indent_string. </p>
<dt><code>sidebar_sort_method</code></p>
<dd>
<pre>Type: sort order
Default: order</pre>
<dd>Specifies how to sort entries in the file browser. By default, the entries are sorted alphabetically. Valid values:</p>
<dl>
<dd>
<dl>
<dt>&#8211; alpha (alphabetically)</p>
<dd>
<dt>&#8211; count (all message count)</p>
<dd>
<dt>&#8211; flagged (flagged message count)</p>
<dd>
<dt>&#8211; name (alphabetically)</p>
<dd>
<dt>&#8211; new (unread message count)</p>
<dd>
<dt>&#8211; path (alphabetically)</p>
<dd>
<dt>&#8211; unread (unread message count)</p>
<dd>
<dt>&#8211; unsorted</p>
<dd></dl>
</dl>
<dd>You may optionally use the &#8220;reverse-&#8221; prefix to specify reverse sorting order (example: &#8220;set sort_browser=reverse-date&#8221;). </p>
<dt><code>sidebar_use_mailbox_shortcuts</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When set, sidebar mailboxes will be displayed with mailbox shortcut prefixes &#8220;=&#8221; or &#8220;~&#8221;.</p>
<dd>When unset, the sidebar will trim off a matching $folder prefix but otherwise not use mailbox shortcuts. </p>
<dt><code>sidebar_visible</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This specifies whether or not to show sidebar. The sidebar shows a list of all your mailboxes.</p>
<dd><code>See also:</code> $sidebar_format, $sidebar_width </p>
<dt><code>sidebar_width</code></p>
<dd>
<pre>Type: number
Default: 30</pre>
<dd>This controls the width of the sidebar. It is measured in screen columns. For example: sidebar_width=20 could display 20 ASCII characters, or 10 Chinese characters. </p>
<dt><code>sig_dashes</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, a line containing &#8220;&#8211; &#8221; (note the trailing space) will be inserted before your $signature. It is <code>strongly</code> recommended that you not <i>unset</i> this variable unless your signature contains just your name. The reason for this is because many software packages use &#8220;&#8211; 
&#8221; to detect your signature. For example, Mutt has the ability to highlight the signature in a different color in the built-in pager. </p>
<dt><code>sig_on_top</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, the signature will be included before any quoted or forwarded text. It is <code>strongly</code> recommended that you do not set this variable unless you really know what you are doing, and are prepared to take some heat from netiquette guardians. </p>
<dt><code>signature</code></p>
<dd>
<pre>Type: path
Default: "~/.signature"</pre>
<dd>Specifies the filename of your signature, which is appended to all outgoing messages. If the filename ends with a pipe (&#8220;|&#8221;), it is assumed that filename is a shell command and input should be read from its standard output. </p>
<dt><code>simple_search</code></p>
<dd>
<pre>Type: string
Default: "~f %s | ~s %s"</pre>
<dd>Specifies how Mutt should expand a simple search into a real search pattern. A simple search is one that does not contain any of the &#8220;~&#8221; pattern operators. See &#8220;patterns&#8221; for more information on search patterns.</p>
<dd>For example, if you simply type &#8220;joe&#8221; at a search or limit prompt, Mutt will automatically expand it to the value specified by this variable by replacing &#8220;%s&#8221; with the supplied string. For the default value, &#8220;joe&#8221; would be expanded to: &#8220;~f joe | ~s joe&#8221;. </p>
<dt><code>size_show_bytes</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, message sizes will display bytes for values less than 1 kilobyte. See formatstrings-size. </p>
<dt><code>size_show_fractions</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, message sizes will be displayed with a single decimal value for sizes from 0 to 10 kilobytes and 1 to 10 megabytes. See formatstrings-size. </p>
<dt><code>size_show_mb</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i>, message sizes will display megabytes for values greater than or equal to 1 megabyte. See formatstrings-size. </p>
<dt><code>size_units_on_left</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, message sizes units will be displayed to the left of the number. See formatstrings-size. </p>
<dt><code>sleep_time</code></p>
<dd>
<pre>Type: number
Default: 1</pre>
<dd>Specifies time, in seconds, to pause while displaying certain informational messages, while moving from folder to folder and after expunging messages from the current folder. The default is to pause one second, so a value of zero for this option suppresses the pause. </p>
<dt><code>smart_wrap</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls the display of lines longer than the screen width in the internal pager. If <i>set</i>, long lines are wrapped at a word boundary. If <i>unset</i>, lines are simply wrapped at the screen edge. Also see the $markers variable. </p>
<dt><code>smileys</code></p>
<dd>
<pre>Type: regular expression
Default: "(&gt;From )|(:[-^]?[][)(&gt;&lt;}{|/DP])"</pre>
<dd>The <i>pager</i> uses this variable to catch some common false positives of $quote_regexp, most notably smileys and not consider a line quoted text if it also matches $smileys. This mostly happens at the beginning of a line. </p>
<dt><code>smime_ask_cert_label</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>This flag controls whether you want to be asked to enter a label for a certificate about to be added to the database or not. It is <i>set</i> by default. (S/MIME only) </p>
<dt><code>smime_ca_location</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>This variable contains the name of either a directory, or a file which contains trusted certificates for use with OpenSSL. (S/MIME only) </p>
<dt><code>smime_certificates</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>Since for S/MIME there is no pubring/secring as with PGP, mutt has to handle storage and retrieval of keys by itself. This is very basic right now, and keys and certificates are stored in two different directories, both named as the hash-value retrieved from OpenSSL. There is an index file which contains mailbox-address keyid pairs, and which can be manually edited. This option points to the location of the certificates. (S/MIME only) </p>
<dt><code>smime_decrypt_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This format string specifies a command which is used to decrypt application/x-pkcs7-mime attachments.</p>
<dd>The OpenSSL command formats have their own set of <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences similar to PGP&#8217;s:</p>
<dl>
<dd>
<dl>
<dt>%f</p>
<dd>Expands to the name of a file containing a message.</p>
<dt>%s</p>
<dd>Expands to the name of a file containing the signature part<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of a multipart/signed attachment when verifying it.</p>
<dt>%k</p>
<dd>The key-pair specified with $smime_default_key</p>
<dt>%c</p>
<dd>One or more certificate IDs.</p>
<dt>%a</p>
<dd>The algorithm used for encryption.</p>
<dt>%d</p>
<dd>The message digest algorithm specified with $smime_sign_digest_alg.</p>
<dt>%C</p>
<dd>CA location: Depending on whether $smime_ca_location<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;points to a directory or file, this expands to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8220;-CApath&nbsp;$smime_ca_location&#8221;&nbsp;or&nbsp;&#8220;-CAfile&nbsp;$smime_ca_location&#8221;.</dl>
</dl>
<dd>For examples on how to configure these formats, see the smime.rc in the samples/ subdirectory which has been installed on your system alongside the documentation. (S/MIME only) </p>
<dt><code>smime_decrypt_use_default_key</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i> (default) this tells mutt to use the default key for decryption. Otherwise, if managing multiple certificate-key-pairs, mutt will try to use the mailbox-address to determine the key to use. It will ask you to supply a key, if it can&#8217;t find one. (S/MIME only) </p>
<dt><code>smime_default_key</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This is the default key-pair to use for S/MIME operations, and must be set to the keyid (the hash-value that OpenSSL generates) to work properly.</p>
<dd>It will be used for encryption (see $postpone_encrypt and $smime_self_encrypt).</p>
<dd>It will be used for decryption unless $smime_decrypt_use_default_key is <i>unset</i>.</p>
<dd>It will also be used for signing unless $smime_sign_as is set.</p>
<dd>The (now deprecated) <i>smime_self_encrypt_as</i> is an alias for this variable, and should no longer be used. (S/MIME only) </p>
<dt><code>smime_encrypt_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to create encrypted S/MIME messages.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_encrypt_with</code></p>
<dd>
<pre>Type: string
Default: "aes256"</pre>
<dd>This sets the algorithm that should be used for encryption. Valid choices are &#8220;aes128&#8221;, &#8220;aes192&#8221;, &#8220;aes256&#8221;, &#8220;des&#8221;, &#8220;des3&#8221;, &#8220;rc2-40&#8221;, &#8220;rc2-64&#8221;, &#8220;rc2-128&#8221;. (S/MIME only) </p>
<dt><code>smime_get_cert_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to extract X509 certificates from a PKCS7 structure.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_get_cert_email_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to extract the mail address(es) used for storing X509 certificates, and for verification purposes (to check whether the certificate was issued for the sender&#8217;s mailbox).</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_get_signer_cert_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to extract only the signers X509 certificate from a S/MIME signature, so that the certificate&#8217;s owner may get compared to the email&#8217;s &#8220;From:&#8221; field.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_import_cert_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to import a certificate via smime_keys.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_is_default</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>The default behavior of mutt is to use PGP on all auto-sign/encryption operations. To override and to use OpenSSL instead this must be <i>set</i>. However, this has no effect while replying, since mutt will automatically select the same application that was used to sign/encrypt the original message. (Note that this variable can be overridden by unsetting $crypt_autosmime.) (S/MIME only) </p>
<dt><code>smime_keys</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>Since for S/MIME there is no pubring/secring as with PGP, mutt has to handle storage and retrieval of keys/certs by itself. This is very basic right now, and stores keys and certificates in two different directories, both named as the hash-value retrieved from OpenSSL. There is an index file which contains mailbox-address keyid pair, and which can be manually edited. This option points to the location of the private keys. (S/MIME only) </p>
<dt><code>smime_pk7out_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to extract PKCS7 structures of S/MIME signatures, in order to extract the public X509 certificate(s).</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_self_encrypt</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, S/MIME encrypted messages will also be encrypted using the certificate in $smime_default_key. (S/MIME only) </p>
<dt><code>smime_sign_as</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>If you have a separate key to use for signing, you should set this to the signing key. Most people will only need to set $smime_default_key. (S/MIME only) </p>
<dt><code>smime_sign_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to created S/MIME signatures of type multipart/signed, which can be read by all mail clients.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. NOTE: %c and %k will default to $smime_sign_as if set, otherwise $smime_default_key. (S/MIME only) </p>
<dt><code>smime_sign_digest_alg</code></p>
<dd>
<pre>Type: string
Default: "sha256"</pre>
<dd>This sets the algorithm that should be used for the signature message digest. Valid choices are &#8220;md5&#8221;, &#8220;sha1&#8221;, &#8220;sha224&#8221;, &#8220;sha256&#8221;, &#8220;sha384&#8221;, &#8220;sha512&#8221;. (S/MIME only) </p>
<dt><code>smime_sign_opaque_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to created S/MIME signatures of type application/x-pkcs7-signature, which can only be handled by mail clients supporting the S/MIME extension.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_timeout</code></p>
<dd>
<pre>Type: number (long)
Default: 300</pre>
<dd>The number of seconds after which a cached passphrase will expire if not used. (S/MIME only) </p>
<dt><code>smime_verify_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to verify S/MIME signatures of type multipart/signed.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smime_verify_opaque_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This command is used to verify S/MIME signatures of type application/x-pkcs7-mime.</p>
<dd>This is a format string, see the $smime_decrypt_command command for possible <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences. (S/MIME only) </p>
<dt><code>smtp_authenticators</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>This is a colon-delimited list of authentication methods mutt may attempt to use to log in to an SMTP server, in the order mutt should try them. Authentication methods are any SASL mechanism, e.g. &#8220;digest-md5&#8221;, &#8220;gssapi&#8221; or &#8220;cram-md5&#8221;. This option is case-insensitive. If it is &#8220;unset&#8221; (the default) mutt will try all available methods, in order from most-secure to least-secure.</p>
<dd>Example: </p>
<dd>
<pre>set smtp_authenticators="digest-md5:cram-md5"</pre>
<dt><code>smtp_oauth_refresh_command</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>The command to run to generate an OAUTH refresh token for authorizing your connection to your SMTP server. This command will be run on every connection attempt that uses the OAUTHBEARER authentication mechanism. See &#8220;oauth&#8221; for details. </p>
<dt><code>smtp_pass</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Specifies the password for your SMTP account. If <i>unset</i>, Mutt will prompt you for your password when you first send mail via SMTP. See $smtp_url to configure mutt to send mail via SMTP.</p>
<dd><code>Warning</code>: you should only use this option when you are on a fairly secure machine, because the superuser can read your muttrc even if you are the only one who can read the file. </p>
<dt><code>smtp_url</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Defines the SMTP smarthost where sent messages should relayed for delivery. This should take the form of an SMTP URL, e.g.: </p>
<dd>
<pre>smtp[s]://[user[:pass]@]host[:port]</pre>
<dd>where &#8220;[&#8230;]&#8221; denotes an optional part. Setting this variable overrides the value of the $sendmail variable.</p>
<dd>Also see $write_bcc. </p>
<dt><code>sort</code></p>
<dd>
<pre>Type: sort order
Default: date</pre>
<dd>Specifies how to sort messages in the &#8220;index&#8221; menu. Valid values are:</p>
<dl>
<dd>
<dl>
<dt>&#8211; date or date-sent</p>
<dd>
<dt>&#8211; date-received</p>
<dd>
<dt>&#8211; from</p>
<dd>
<dt>&#8211; mailbox-order (unsorted)</p>
<dd>
<dt>&#8211; score</p>
<dd>
<dt>&#8211; size</p>
<dd>
<dt>&#8211; spam</p>
<dd>
<dt>&#8211; subject</p>
<dd>
<dt>&#8211; threads</p>
<dd>
<dt>&#8211; to</p>
<dd></dl>
</dl>
<dd>You may optionally use the &#8220;reverse-&#8221; prefix to specify reverse sorting order (example: &#8220;set sort=reverse-date-sent&#8221;). </p>
<dt><code>sort_alias</code></p>
<dd>
<pre>Type: sort order
Default: alias</pre>
<dd>Specifies how the entries in the &#8220;alias&#8221; menu are sorted. The following are legal values:</p>
<dl>
<dd>
<dl>
<dt>&#8211; address (sort alphabetically by email address)</p>
<dd>
<dt>&#8211; alias (sort alphabetically by alias name)</p>
<dd>
<dt>&#8211; unsorted (leave in order specified in .muttrc)</p>
<dd></dl>
</dl>
<dt><code>sort_aux</code></p>
<dd>
<pre>Type: sort order
Default: date</pre>
<dd>This provides a secondary sort for messages in the &#8220;index&#8221; menu, used when the $sort value is equal for two messages.</p>
<dd>When sorting by threads, this variable controls how threads are sorted in relation to other threads, and how the branches of the thread trees are sorted. This can be set to any value that $sort can, except &#8220;threads&#8221; (in that case, mutt will just use &#8220;date-sent&#8221;). You can also specify the &#8220;last-&#8221; prefix in addition to the &#8220;reverse-&#8221; prefix, but &#8220;last-&#8221; must come after &#8220;reverse-&#8220;. The &#8220;last-&#8221; prefix causes messages to be sorted against its siblings by which has the last descendant, using the rest of $sort_aux as an ordering. For instance, </p>
<dd>
<pre>set sort_aux=last-date-received</pre>
<dd>would mean that if a new message is received in a thread, that thread becomes the last one displayed (or the first, if you have &#8220;set sort=reverse-threads&#8221;.)</p>
<dd>Note: For reversed-threads $sort order, $sort_aux is reversed again (which is not the right thing to do, but kept to not break any existing configuration setting). </p>
<dt><code>sort_browser</code></p>
<dd>
<pre>Type: sort order
Default: alpha</pre>
<dd>Specifies how to sort entries in the file browser. By default, the entries are sorted alphabetically. Valid values:</p>
<dl>
<dd>
<dl>
<dt>&#8211; alpha (alphabetically)</p>
<dd>
<dt>&#8211; count</p>
<dd>
<dt>&#8211; date</p>
<dd>
<dt>&#8211; size</p>
<dd>
<dt>&#8211; unread</p>
<dd>
<dt>&#8211; unsorted</p>
<dd></dl>
</dl>
<dd>You may optionally use the &#8220;reverse-&#8221; prefix to specify reverse sorting order (example: &#8220;set sort_browser=reverse-date&#8221;). </p>
<dt><code>sort_re</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>This variable is only useful when sorting by threads with $strict_threads <i>unset</i>. In that case, it changes the heuristic mutt uses to thread messages by subject. With $sort_re <i>set</i>, mutt will only attach a message as the child of another message by subject if the subject of the child message starts with a substring matching the setting of $reply_regexp. With $sort_re <i>unset</i>, mutt will attach the message whether or not this is the case, as long as the non-$reply_regexp parts of both messages are identical. </p>
<dt><code>spam_separator</code></p>
<dd>
<pre>Type: string
Default: ","</pre>
<dd>This variable controls what happens when multiple spam headers are matched: if <i>unset</i>, each successive header will overwrite any previous matches value for the spam label. If <i>set</i>, each successive match will append to the previous, using this variable&#8217;s value as a separator. </p>
<dt><code>spoolfile</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>If your spool mailbox is in a non-default place where Mutt cannot find it, you can specify its location with this variable. Mutt will initially set this variable to the value of the environment variable $MAIL or $MAILDIR if either is defined. </p>
<dt><code>ssl_ca_certificates_file</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>This variable specifies a file containing trusted CA certificates. Any server certificate that is signed with one of these CA certificates is also automatically accepted. (GnuTLS only)</p>
<dd>Example: </p>
<dd>
<pre>set ssl_ca_certificates_file=/etc/ssl/certs/ca-certificates.crt</pre>
<dt><code>ssl_client_cert</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>The file containing a client certificate and its associated private key. </p>
<dt><code>ssl_force_tls</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If this variable is <i>set</i>, Mutt will require that all connections to remote servers be encrypted. Furthermore it will attempt to negotiate TLS even if the server does not advertise the capability, since it would otherwise have to abort the connection anyway. This option supersedes $ssl_starttls. </p>
<dt><code>ssl_min_dh_prime_bits</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>This variable specifies the minimum acceptable prime size (in bits) for use in any Diffie-Hellman key exchange. A value of 0 will use the default from the GNUTLS library. (GnuTLS only) </p>
<dt><code>ssl_starttls</code></p>
<dd>
<pre>Type: quadoption
Default: yes</pre>
<dd>If <i>set</i> (the default), mutt will attempt to use STARTTLS on servers advertising the capability. When <i>unset</i>, mutt will not attempt to use STARTTLS regardless of the server&#8217;s capabilities. </p>
<dt><code>ssl_use_sslv2</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i> , Mutt will use SSLv2 when communicating with servers that request it. <code>N.B. As of 2011, SSLv2 is considered insecure, and using is inadvisable. See <a rel="nofollow" href="https://tools.ietf.org/html/rfc6176">https://tools.ietf.org/html/rfc6176</a> .</code> (OpenSSL only) </p>
<dt><code>ssl_use_sslv3</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i> , Mutt will use SSLv3 when communicating with servers that request it. <code>N.B. As of 2015, SSLv3 is considered insecure, and using it is inadvisable. See <a rel="nofollow" href="https://tools.ietf.org/html/rfc7525">https://tools.ietf.org/html/rfc7525</a> .</code> </p>
<dt><code>ssl_use_tlsv1</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i> , Mutt will use TLSv1.0 when communicating with servers that request it. <code>N.B. As of 2015, TLSv1.0 is considered insecure, and using it is inadvisable. See <a rel="nofollow" href="https://tools.ietf.org/html/rfc7525">https://tools.ietf.org/html/rfc7525</a> .</code> </p>
<dt><code>ssl_use_tlsv1_1</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i> , Mutt will use TLSv1.1 when communicating with servers that request it. <code>N.B. As of 2015, TLSv1.1 is considered insecure, and using it is inadvisable. See <a rel="nofollow" href="https://tools.ietf.org/html/rfc7525">https://tools.ietf.org/html/rfc7525</a> .</code> </p>
<dt><code>ssl_use_tlsv1_2</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i> , Mutt will use TLSv1.2 when communicating with servers that request it. </p>
<dt><code>ssl_use_tlsv1_3</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i> , Mutt will use TLSv1.3 when communicating with servers that request it. </p>
<dt><code>ssl_usesystemcerts</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If set to <i>yes</i>, mutt will use CA certificates in the system-wide certificate store when checking if a server certificate is signed by a trusted CA. (OpenSSL only) </p>
<dt><code>ssl_verify_dates</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i> (the default), mutt will not automatically accept a server certificate that is either not yet valid or already expired. You should only unset this for particular known hosts, using the &lt;account-hook&gt; function. </p>
<dt><code>ssl_verify_host</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>If <i>set</i> (the default), mutt will not automatically accept a server certificate whose host name does not match the host used in your folder URL. You should only unset this for particular known hosts, using the &lt;account-hook&gt; function. </p>
<dt><code>ssl_verify_partial_chains</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>This option should not be changed from the default unless you understand what you are doing.</p>
<dd>Setting this variable to <i>yes</i> will permit verifying partial certification chains, i. e. a certificate chain where not the root, but an intermediate certificate CA, or the host certificate, are marked trusted (in $certificate_file), without marking the root signing CA as trusted.</p>
<dd>(OpenSSL 1.0.2b and newer only). </p>
<dt><code>ssl_ciphers</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Contains a colon-seperated list of ciphers to use when using SSL. For OpenSSL, see <a href="/docs/linux/man/1-ciphers/">ciphers</a>(1) for the syntax of the string.</p>
<dd>For GnuTLS, this option will be used in place of &#8220;NORMAL&#8221; at the start of the priority string. See <a href="/docs/linux/man/3-gnutls_priority_init/">gnutls_priority_init</a>(3) for the syntax and more details. (Note: GnuTLS version 2.1.7 or higher is required.) </p>
<dt><code>status_chars</code></p>
<dd>
<pre>Type: string
Default: "-*%A"</pre>
<dd>Controls the characters used by the &#8220;%r&#8221; indicator in $status_format. The first character is used when the mailbox is unchanged. The second is used when the mailbox has been changed, and it needs to be resynchronized. The third is used if the mailbox is in read-only mode, or if the mailbox will not be written when exiting that mailbox (You can toggle whether to write changes to a mailbox with the &lt;toggle-write&gt; operation, bound by default to &#8220;%&#8221;). The fourth is used to indicate that the current folder has been opened in attach- message mode (Certain operations like composing a new mail, replying, forwarding, etc. are not permitted in this mode). </p>
<dt><code>status_format</code></p>
<dd>
<pre>Type: string
Default: "-%r-Mutt: %f [Msgs:%?M?%M/?%m%?n? New:%n?%?o? Old:%o?%?d? Del:%d?%?F? Flag:%F?%?t? Tag:%t?%?p? Post:%p?%?b? Inc:%b?%?l? %l?]---(%s/%S)-%&gt;-(%P)---"</pre>
<dd>Controls the format of the status line displayed in the &#8220;index&#8221; menu. This string is similar to $index_format, but has its own set of <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequences:</p>
<dl>
<dd>
<dl>
<dt>%b</p>
<dd>number of mailboxes with new mail *</p>
<dt>%d</p>
<dd>number of deleted messages *</p>
<dt>%f</p>
<dd>the full pathname of the current mailbox</p>
<dt>%F</p>
<dd>number of flagged messages *</p>
<dt>%h</p>
<dd>local hostname</p>
<dt>%l</p>
<dd>size (in bytes) of the current mailbox (see formatstrings-size) *</p>
<dt>%L</p>
<dd>size (in bytes) of the messages shown (i.e., which match the current limit) (see formatstrings-size) *</p>
<dt>%m</p>
<dd>the number of messages in the mailbox *</p>
<dt>%M</p>
<dd>the number of messages shown (i.e., which match the current limit) *</p>
<dt>%n</p>
<dd>number of new messages in the mailbox *</p>
<dt>%o</p>
<dd>number of old unread messages *</p>
<dt>%p</p>
<dd>number of postponed messages *</p>
<dt>%P</p>
<dd>percentage of the way through the index</p>
<dt>%r</p>
<dd>modified/read-only/won&#8217;t-write/attach-message indicator, according to $status_chars</p>
<dt>%R</p>
<dd>number of read messages *</p>
<dt>%s</p>
<dd>current sorting mode ($sort)</p>
<dt>%S</p>
<dd>current aux sorting method ($sort_aux)</p>
<dt>%t</p>
<dd>number of tagged messages *</p>
<dt>%u</p>
<dd>number of unread messages *</p>
<dt>%v</p>
<dd>Mutt version string</p>
<dt>%V</p>
<dd>currently active limit pattern, if any *</p>
<dt>%&gt;X</p>
<dd>right justify the rest of the string and pad with &#8220;X&#8221;</p>
<dt>%|X</p>
<dd>pad to the end of the line with &#8220;X&#8221;</p>
<dt>%*X</p>
<dd>soft-fill with character &#8220;X&#8221; as pad</dl>
</dl>
<dd>For an explanation of &#8220;soft-fill&#8221;, see the $index_format documentation.</p>
<dd>* = can be optionally printed if nonzero</p>
<dd>Some of the above sequences can be used to optionally print a string if their value is nonzero. For example, you may only want to see the number of flagged messages if such messages exist, since zero is not particularly meaningful. To optionally print a string based upon one of the above sequences, the following construct is used:</p>
<dd>%?&lt;sequence_char&gt;?&lt;optional_string&gt;?</p>
<dd>where <i>sequence_char</i> is a character from the table above, and <i>optional_string</i> is the string you would like printed if <i>sequence_char</i> is nonzero. <i>optional_string</i> <code>may</code> contain other sequences as well as normal text, but you may <code>not</code> nest optional strings.</p>
<dd>Here is an example illustrating how to optionally print the number of new messages in a mailbox:</p>
<dd>%?n?%n new messages.?</p>
<dd>You can also switch between two strings using the following construct:</p>
<dd>%?&lt;sequence_char&gt;?&lt;if_string&gt;&amp;&lt;else_string&gt;?</p>
<dd>If the value of <i>sequence_char</i> is non-zero, <i>if_string</i> will be expanded, otherwise <i>else_string</i> will be expanded.</p>
<dd>You can force the result of any <a href="/docs/linux/man/3-printf/">printf</a>(3)-like sequence to be lowercase by prefixing the sequence character with an underscore (&#8220;_&#8221;) sign. For example, if you want to display the local hostname in lowercase, you would use: &#8220;%_h&#8221;.</p>
<dd>If you prefix the sequence character with a colon (&#8220;:&#8221;) character, mutt will replace any dots in the expansion by underscores. This might be helpful with IMAP folders that don&#8217;t like dots in folder names. </p>
<dt><code>status_on_top</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Setting this variable causes the &#8220;status bar&#8221; to be displayed on the first line of the screen rather than near the bottom. If $help is <i>set</i>, too it&#8217;ll be placed at the bottom. </p>
<dt><code>strict_threads</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>If <i>set</i>, threading will only make use of the &#8220;In-Reply-To&#8221; and &#8220;References:&#8221; fields when you $sort by message threads. By default, messages with the same subject are grouped together in &#8220;pseudo threads.&#8221;. This may not always be desirable, such as in a personal mailbox where you might have several unrelated messages with the subjects like &#8220;hi&#8221; which will get grouped together. See also $sort_re for a less drastic way of controlling this behavior. </p>
<dt><code>suspend</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>unset</i>, mutt won&#8217;t stop when the user presses the terminal&#8217;s <i>susp</i> key, usually &#8220;^Z&#8221;. This is useful if you run mutt inside an xterm using a command like &#8220;xterm -e mutt&#8221;. </p>
<dt><code>text_flowed</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will generate &#8220;format=flowed&#8221; bodies with a content type of &#8220;text/plain; format=flowed&#8221;. This format is easier to handle for some mailing software, and generally just looks like ordinary text. To actually make use of this format&#8217;s features, you&#8217;ll need support in your editor.</p>
<dd>The option only controls newly composed messages. Postponed messages, resent messages, and draft messages (via -H on the command line) will use the content-type of the source message.</p>
<dd>Note that $indent_string is ignored when this option is <i>set</i>. </p>
<dt><code>thorough_search</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Affects the ~b and ~h search operations described in section &#8220;patterns&#8221;. If <i>set</i>, the headers and body/attachments of messages to be searched are decoded before searching. If <i>unset</i>, messages are searched as they appear in the folder.</p>
<dd>Users searching attachments or for non-ASCII characters should <i>set</i> this value because decoding also includes MIME parsing/decoding and possible character set conversions. Otherwise mutt will attempt to match against the raw message received (for example quoted-printable encoded or with encoded headers) which may lead to incorrect search results. </p>
<dt><code>thread_received</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt uses the date received rather than the date sent to thread messages by subject. </p>
<dt><code>tilde</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, the internal-pager will pad blank lines to the bottom of the screen with a tilde (&#8220;~&#8221;). </p>
<dt><code>time_inc</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>Along with $read_inc, $write_inc, and $net_inc, this variable controls the frequency with which progress updates are displayed. It suppresses updates less than $time_inc milliseconds apart. This can improve throughput on systems with slow terminals, or when running mutt on a remote system.</p>
<dd>Also see the &#8220;tuning&#8221; section of the manual for performance considerations. </p>
<dt><code>timeout</code></p>
<dd>
<pre>Type: number
Default: 600</pre>
<dd>When Mutt is waiting for user input either idling in menus or in an interactive prompt, Mutt would block until input is present. Depending on the context, this would prevent certain operations from working, like checking for new mail or keeping an IMAP connection alive.</p>
<dd>This variable controls how many seconds Mutt will at most wait until it aborts waiting for input, performs these operations and continues to wait for input.</p>
<dd>A value of zero or less will cause Mutt to never time out. </p>
<dt><code>tmpdir</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>This variable allows you to specify where Mutt will place its temporary files needed for displaying and composing messages. If this variable is not set, the environment variable $TMPDIR is used. If $TMPDIR is not set then &#8220;/tmp&#8221; is used. </p>
<dt><code>to_chars</code></p>
<dd>
<pre>Type: string
Default: " +TCFL"</pre>
<dd>Controls the character used to indicate mail addressed to you. The first character is the one used when the mail is <i>not</i> addressed to your address. The second is used when you are the only recipient of the message. The third is when your address appears in the &#8220;To:&#8221; header field, but you are not the only recipient of the message. The fourth character is used when your address is specified in the &#8220;Cc:&#8221; header field, but you are not the only recipient. The fifth character is used to indicate mail that was sent by <i>you</i>. The sixth character is used to indicate when a mail was sent to a mailing-list you subscribe to. </p>
<dt><code>trash</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>If set, this variable specifies the path of the trash folder where the mails marked for deletion will be moved, instead of being irremediably purged.</p>
<dd>NOTE: When you delete a message in the trash folder, it is really deleted, so that you have a way to clean the trash. </p>
<dt><code>ts_icon_format</code></p>
<dd>
<pre>Type: string
Default: "M%?n?AIL&amp;ail?"</pre>
<dd>Controls the format of the icon title, as long as &#8220;$ts_enabled&#8221; is set. This string is identical in formatting to the one used by &#8220;$status_format&#8221;. </p>
<dt><code>ts_enabled</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Controls whether mutt tries to set the terminal status line and icon name. Most terminal emulators emulate the status line in the window title. </p>
<dt><code>ts_status_format</code></p>
<dd>
<pre>Type: string
Default: "Mutt with %?m?%m messages&amp;no messages?%?n? [%n NEW]?"</pre>
<dd>Controls the format of the terminal status line (or window title), provided that &#8220;$ts_enabled&#8221; has been set. This string is identical in formatting to the one used by &#8220;$status_format&#8221;. </p>
<dt><code>tunnel</code></p>
<dd>
<pre>Type: string
Default: ""</pre>
<dd>Setting this variable will cause mutt to open a pipe to a command instead of a raw socket. You may be able to use this to set up preauthenticated connections to your IMAP/POP3/SMTP server. Example: </p>
<dd>
<pre>set tunnel="ssh -q mailhost.net /usr/local/libexec/imapd"</pre>
<dd>Note: For this example to work you must be able to log in to the remote machine without having to enter a password.</p>
<dd>When set, Mutt uses the tunnel for all remote connections. Please see &#8220;account-hook&#8221; in the manual for how to use different tunnel commands per connection. </p>
<dt><code>uncollapse_jump</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, Mutt will jump to the next unread message, if any, when the current thread is <i>un</i>collapsed. </p>
<dt><code>uncollapse_new</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will automatically uncollapse any collapsed thread that receives a new message. When <i>unset</i>, collapsed threads will remain collapsed. the presence of the new message will still affect index sorting, though. </p>
<dt><code>use_8bitmime</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd><code>Warning:</code> do not set this variable unless you are using a version of sendmail which supports the -B8BITMIME flag (such as sendmail 8.8.x) or you may not be able to send mail.</p>
<dd>When <i>set</i>, Mutt will invoke $sendmail with the -B8BITMIME flag when sending 8-bit messages to enable ESMTP negotiation. </p>
<dt><code>use_domain</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will qualify all local addresses (ones without the &#8220;@host&#8221; portion) with the value of $hostname. If <i>unset</i>, no addresses will be qualified. </p>
<dt><code>use_envelope_from</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will set the <i>envelope</i> sender of the message. If $envelope_from_address is <i>set</i>, it will be used as the sender address. If <i>unset</i>, mutt will attempt to derive the sender from the &#8220;From:&#8221; header.</p>
<dd>Note that this information is passed to sendmail command using the -f command line switch. Therefore setting this option is not useful if the $sendmail variable already contains -f or if the executable pointed to by $sendmail doesn&#8217;t support the -f switch. </p>
<dt><code>use_from</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will generate the &#8220;From:&#8221; header field when sending messages. If <i>unset</i>, no &#8220;From:&#8221; header field will be generated unless the user explicitly sets one using the &#8220;my_hdr&#8221; command. </p>
<dt><code>use_ipv6</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, Mutt will look for IPv6 addresses of hosts it tries to contact. If this option is <i>unset</i>, Mutt will restrict itself to IPv4 addresses. Normally, the default should work. </p>
<dt><code>user_agent</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>When <i>set</i>, mutt will add a &#8220;User-Agent:&#8221; header to outgoing messages, indicating which version of mutt was used for composing them. </p>
<dt><code>visual</code></p>
<dd>
<pre>Type: path
Default: ""</pre>
<dd>Specifies the visual editor to invoke when the &#8220;~v&#8221; command is given in the built-in editor. </p>
<dt><code>wait_key</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls whether Mutt will ask you to press a key after an external command has been invoked by these functions: &lt;shell-escape&gt;, &lt;pipe-message&gt;, &lt;pipe-entry&gt;, &lt;print-message&gt;, and &lt;print-entry&gt; commands.</p>
<dd>It is also used when viewing attachments with &#8220;auto_view&#8221;, provided that the corresponding mailcap entry has a <i>needsterminal</i> flag, and the external program is interactive.</p>
<dd>When <i>set</i>, Mutt will always ask for a key. When <i>unset</i>, Mutt will wait for a key only if the external command returned a non-zero status. </p>
<dt><code>weed</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>When <i>set</i>, mutt will weed headers when displaying, forwarding, printing, or replying to messages. </p>
<dt><code>wrap</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>When set to a positive value, mutt will wrap text at $wrap characters. When set to a negative value, mutt will wrap text so that there are $wrap characters of empty space on the right side of the terminal. Setting it to zero makes mutt wrap at the terminal width.</p>
<dd>Also see $reflow_wrap. </p>
<dt><code>wrap_headers</code></p>
<dd>
<pre>Type: number
Default: 78</pre>
<dd>This option specifies the number of characters to use for wrapping an outgoing message&#8217;s headers. Allowed values are between 78 and 998 inclusive.</p>
<dd><code>Note:</code> This option usually shouldn&#8217;t be changed. RFC5233 recommends a line length of 78 (the default), so <code>please only change this setting when you know what you&#8217;re doing</code>. </p>
<dt><code>wrap_search</code></p>
<dd>
<pre>Type: boolean
Default: yes</pre>
<dd>Controls whether searches wrap around the end.</p>
<dd>When <i>set</i>, searches will wrap around the first (or last) item. When <i>unset</i>, incremental searches will not wrap. </p>
<dt><code>wrapmargin</code></p>
<dd>
<pre>Type: number
Default: 0</pre>
<dd>(DEPRECATED) Equivalent to setting $wrap with a negative value. </p>
<dt><code>write_bcc</code></p>
<dd>
<pre>Type: boolean
Default: no</pre>
<dd>Controls whether mutt writes out the &#8220;Bcc:&#8221; header when preparing messages to be sent. Some MTAs, such as Exim and Courier, do not strip the &#8220;Bcc:&#8221; header; so it is advisable to leave this unset unless you have a particular need for the header to be in the sent message.</p>
<dd>If mutt is set to deliver directly via SMTP (see $smtp_url), this option does nothing: mutt will never write out the &#8220;Bcc:&#8221; header in this case.</p>
<dd>Note this option only affects the sending of messages. Fcc&#8217;ed copies of a message will always contain the &#8220;Bcc:&#8221; header if one exists.</p>
<dd>On Debian systems, exim4 and postfix strip BCC headers by default. The above warning applies to exim3 users, see /etc/Muttrc. </p>
<dt><code>write_inc</code></p>
<dd>
<pre>Type: number
Default: 10</pre>
<dd>When writing a mailbox, a message will be printed every $write_inc messages to indicate progress. If set to 0, only a single message will be displayed before writing a mailbox.</p>
<dd>Also see the $read_inc, $net_inc and $time_inc variables and the &#8220;tuning&#8221; section of the manual for performance considerations. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), <code><a href="/docs/linux/man/5-mailcap/">mailcap</a></code>(5), <code><a href="/docs/linux/man/5-maildir/">maildir</a></code>(5), <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5), <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) </p>
<p> The Mutt Manual </p>
<p> The Mutt home page: <a rel="nofollow" href="http://www.mutt.org/">http://www.mutt.org/</a></p>
<h2>Author</h2>
<p>Michael Elkins, and others. Use &lt;mutt-dev [at] mutt.org&gt; to contact the developers.</p>
