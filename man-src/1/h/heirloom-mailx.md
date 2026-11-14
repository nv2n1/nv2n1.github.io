---
title: "heirloom-mailx(1)"
name: "heirloom-mailx"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heirloom-mailx/"
description: "mailx – send and receive Internet mail"
---

<h2 class="name">NAME</h2>
<p> mailx &#8211; send and receive Internet mail </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mailx</code> [<code>-BDdEFintv~</code>] [<code>-s</code><i>&nbsp;<wbr>subject</i>] [<code>-a</code><i>&nbsp;<wbr>attachment</i> ] [<code>-c</code><i>&nbsp;<wbr>cc-addr</i>] [<code>-b</code><i>&nbsp;<wbr>bcc-addr</i>] [<code>-r</code><i>&nbsp;<wbr>from-addr</i>] [<code>-h</code><i>&nbsp;<wbr>hops</i>] [<code>-A</code><i>&nbsp;<wbr>account</i>] [<code>-S</code><i>&nbsp;<wbr>variable</i>[<code>=</code><i>value</i>]] <i>to-addr</i> . . .</p>
<dt> <code>mailx</code> [<code>-BDdeEHiInNRv~</code>] [<code>-T</code><i>&nbsp;<wbr>name</i>] [<code>-A</code><i>&nbsp;<wbr>account</i>] [<code>-S</code><i>&nbsp;<wbr>variable</i>[<code>=</code><i>value</i>]] <code>-f</code> [<i>name</i>]</p>
<dt> <code>mailx</code> [<code>-BDdeEinNRv~</code>] [<code>-A</code><i>&nbsp;<wbr>account</i>] [<code>-S</code><i>&nbsp;<wbr>variable</i>[<code>=</code><i>value</i>]] [<code>-u</code><i>&nbsp;<wbr>user</i>]</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> <i>Mailx</i> is an intelligent mail processing system, which has</p>
<dd>a command syntax reminiscent of <i><a href="/docs/linux/man/1-ed/">ed</a></i>(1) with lines replaced by messages. It is based on Berkeley Mail 8.1, is intended to provide the functionality of the POSIX <code>mailx</code> command, and offers extensions for MIME, IMAP, POP3, SMTP, and S/MIME. <i>Mailx</i> provides enhanced features for interactive use, such as caching and disconnected operation for IMAP, message threading, scoring, and filtering. It is also usable as a mail batch language, both for sending and receiving mail. </p>
<p> The following options are accepted:</p>
<dl>
<dt><code>-A</code><i>&nbsp;<wbr>name</i></p>
<dd> Executes an <i>account</i> command (see below) for <i>name</i> after the startup files have been read.</p>
<dt><code>-a</code><i>&nbsp;<wbr>file</i></p>
<dd> Attach the given file to the message.</p>
<dt><code>-B</code></p>
<dd> Make standard input and standard output line-buffered.</p>
<dt><code>-b</code><i>&nbsp;<wbr>address</i></p>
<dd> Send blind carbon copies to list. List should be a comma-separated list of names.</p>
<dt><code>-c</code><i>&nbsp;<wbr>address</i></p>
<dd> Send carbon copies to list of users.</p>
<dt><code>-D</code></p>
<dd> Start in <i>disconnected</i> mode; see the description for the <i>disconnected</i> variable option.</p>
<dt><code>-d</code></p>
<dd> Enables debugging messages and disables the actual delivery of messages. Unlike <i>-v</i>, this option is intended for <i>mailx</i> development only.</p>
<dt><code>-e</code></p>
<dd> Just check if mail is present in the system mailbox. If yes, return an exit status of zero, else, a non-zero value.</p>
<dt><code>-E</code></p>
<dd> If an outgoing message does not contain any text in its first or only message part, do not send it but discard it silently, effectively setting the <i>skipemptybody</i> variable at program startup. This is useful for sending messages from scripts started by <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8).</p>
<dt><code>-f</code> [<i>file</i>]</p>
<dd> Read in the contents of the user&#8217;s mbox (or the specified file) for processing; when <i>mailx</i> is quit, it writes undeleted messages back to this file. The string <i>file</i> is handled as described for the <i>folder</i> command below.</p>
<dt><code>-F</code></p>
<dd> Save the message to send in a file named after the local part of the first recipient&#8217;s address.</p>
<dt><code>-H</code></p>
<dd> Print header summaries for all messages and exit.</p>
<dt><code>-h</code><i> hops</i></p>
<dd> Invoke sendmail with the specified hop count. This option has no effect when SMTP is used for sending mail.</p>
<dt><code>-i</code></p>
<dd> Ignore tty interrupt signals. This is particularly useful when using <i>mailx</i> on noisy phone lines.</p>
<dt><code>-I</code></p>
<dd> Shows the `Newsgroup:&#8217; or `Article-Id:&#8217; fields in the header summary. Only applicable in combination with <i>-f</i>.</p>
<dt><code>-n</code></p>
<dd> Inhibits reading /etc/nail.rc upon startup. This option should be activated for <i>mailx</i> scripts that are invoked on more than one machine, because the contents of that file may differ between them.</p>
<dt><code>-N</code></p>
<dd> Inhibits the initial display of message headers when reading mail or editing a mail folder.</p>
<dt><code>-q</code><i>&nbsp;<wbr>file</i></p>
<dd> Start the message with the contents of the specified file. May be given in send mode only.</p>
<dt><code>-r</code><i>&nbsp;<wbr>address</i></p>
<dd> Sets the <i>From</i> address. Overrides any <i>from</i> variable specified in environment or startup files. Tilde escapes are disabled. The <i>-r address</i> options are passed to the mail transfer agent unless SMTP is used. This option exists for compatibility only; it is recommended to set the <i>from</i> variable directly instead.</p>
<dt><code>-R</code></p>
<dd> Opens any folders read-only.</p>
<dt><code>-s</code><i>&nbsp;<wbr>subject</i></p>
<dd> Specify subject on command line (only the first argument after the <i>-s</i> flag is used as a subject; be careful to quote subjects containing spaces).</p>
<dt><code>-S</code><i>&nbsp;<wbr>variable</i>[<code>=</code><i>value</i>]</p>
<dd> Sets the internal option <i>variable</i> and, in case of a string option, assigns <i>value</i> to it.</p>
<dt><code>-T</code><i>&nbsp;<wbr>name</i></p>
<dd> Writes the `Message-Id:&#8217; and `Article-Id:&#8217; header fields of each message read in the file <i>name</i>. Implies <i>-I</i>. Compressed files are handled as described for the <i>folder</i> command below.</p>
<dt><code>-t</code></p>
<dd> The message to be sent is expected to contain a message header with `To:&#8217;, `Cc:&#8217;, or `Bcc:&#8217; fields giving its recipients. Recipients specified on the command line are ignored.</p>
<dt><code>-u</code><i>&nbsp;<wbr>user</i></p>
<dd> Reads the mailbox of the given user name.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. The details of delivery are displayed on the user&#8217;s terminal.</p>
<dt><code>-V</code></p>
<dd> Print <i>mailx</i>&#8216;s version and exit.</p>
<dt><code>-~</code></p>
<dd> Enable tilde escapes even if not in interactive mode.</dl>
<h3>Sending mail</h3>
<p> To send a message to one or more people, <i>mailx</i> can be invoked with arguments which are the names of people to whom the mail will be sent. The user is then expected to type in his message, followed by an `control-D&#8217; at the beginning of a line. The section below Replying to or originating mail, describes some features of <i>mailx</i> available to help when composing letters.</p>
<h3>Reading mail</h3>
<p> In normal usage <i>mailx</i> is given no arguments and checks the user&#8217;s mail out of the post office, then prints out a one line header of each message found. The current message is initially the first message (numbered 1) and can be printed using the print command which can be abbreviated `p&#8217;). The user can move among the messages much as he moves between lines in <i><a href="/docs/linux/man/1-ed/">ed</a></i>(1), with the commands `+&#8217; and `-&#8216; moving backwards and forwards, and simple numbers.</p>
<h3>Disposing of mail</h3>
<p> After examining a message the user can delete `d&#8217;) the message or reply `r&#8217;) to it. Deletion causes the <i>mailx</i> program to forget about the message. This is not irreversible; the message can be undeleted `u&#8217;) by giving its number, or the <i>mailx</i> session can be aborted by giving the exit `x&#8217;) command. Deleted messages will, however, usually disappear never to be seen again.</p>
<h3>Specifying messages</h3>
<p> Commands such as print and delete can be given a list of message numbers as arguments to apply to a number of messages at once. Thus `<i>delete 1 2</i>&#8216; deletes messages 1 and 2, while `<i>delete 1-5</i>&#8216; deletes messages 1 through 5. In sorted or threaded mode (see the <i>sort</i> and <i>thread</i> commands), `<i>delete 1-5</i>&#8216; deletes the messages that are located between (and including) messages 1 through 5 in the sorted/threaded order, as shown in the header summary. The following special message names exist:</p>
<dl>
<dt><code>:n</code></p>
<dd> All new messages.</p>
<dt><code>:o</code></p>
<dd> All old messages (any not in state read or new).</p>
<dt><code>:u</code></p>
<dd> All unread messages.</p>
<dt><code>:d</code></p>
<dd> All deleted messages (for the <i>undelete</i> command).</p>
<dt><code>:r</code></p>
<dd> All read messages.</p>
<dt><code>:f</code></p>
<dd> All `flagged&#8217; messages.</p>
<dt><code>:a</code></p>
<dd> All answered messages (cf. the <i>markanswered</i> variable).</p>
<dt><code>:t</code></p>
<dd> All messages marked as draft.</p>
<dt><code>:k</code></p>
<dd> All `killed&#8217; messages.</p>
<dt><code>:j</code></p>
<dd> All messages classified as junk.</p>
<dt><code>.</code></p>
<dd> The current message.</p>
<dt><code>;</code></p>
<dd> The message that was previously the current message.</p>
<dt><code>,</code></p>
<dd> The parent message of the current message, that is the message with the Message-ID given in the `In-Reply-To:&#8217; field or the last entry of the `References:&#8217; field of the current message.</p>
<dt><code>&#8211;</code></p>
<dd> The next previous undeleted message, or the next previous deleted message for the <i>undelete</i> command. In sorted/threaded mode, the next previous such message in the sorted/threaded order.</p>
<dt><code>+</code></p>
<dd> The next undeleted message, or the next deleted message for the <i>undelete</i> command. In sorted/threaded mode, the next such message in the sorted/threaded order.</p>
<dt><code>^</code></p>
<dd> The first undeleted message, or the first deleted message for the <i>undelete</i> command. In sorted/threaded mode, the first such message in the sorted/threaded order.</p>
<dt><code>$</code></p>
<dd> The last message. In sorted/threaded mode, the last message in the sorted/threaded order.</p>
<dt><code>&amp;</code><i>x</i></p>
<dd> In threaded mode, selects the message addressed with <i>x</i>, where <i>x</i> is any other message specification, and all messages from the thread that begins at it. Otherwise, it is identical to <i>x</i>. If <i>x</i> is omitted, the thread beginning with the current message is selected.</p>
<dt><code>*</code></p>
<dd> All messages.</p>
<dt><code>`</code></p>
<dd> All messages that were included in the message list for the previous command.</p>
<dt><code>/</code><i>string</i></p>
<dd> All messages that contain <i>string</i> in the subject field (case ignored). See also the <i>searchheaders</i> variable. If <i>string</i> is empty, the string from the previous specification of that type is used again.</p>
<dt><i>address</i></p>
<dd> All messages from <i>address</i>. By default, this is a case-sensitive search for the complete email address. If the <i>allnet</i> variable is set, only the local part of the addresses is evaluated for the comparison. Otherwise if the <i>showname</i> variable is set, a case-sensitive search for the complete real name of a sender is performed. The IMAP-style <code>(from&nbsp;<wbr></code><i>address)</i> expression can be used instead if substring matches are desired.</p>
<dt><code>(</code><i>criterion</i><code>)</code></p>
<dd> All messages that satisfy the given IMAP-style SEARCH <i>criterion</i>. This addressing mode is available with all types of folders; for folders not located on IMAP servers, or for servers unable to execute the SEARCH command, <i>mailx</i> will perform the search locally. Strings must be enclosed by double quotes `&quot;&#8217; in their entirety if they contain white space or parentheses; within the quotes, only backslash `\&#8217; is recognized as an escape character. All string searches are case-insensitive. When the description indicates that the `envelope&#8217; representation of an address field is used, this means that the search string is checked against both a list constructed as </p>
<pre>
<code>(&quot;</code><i>real name</i><code>&quot; &quot;</code><i>source-route</i><code>&quot; &quot;</code><i>local-part</i><code>&quot; &quot;</code><i>domain-part</i><code>&quot;)</code>
</pre>
<p> for each address, and the addresses without real names from the respective header field. Criteria can be nested using parentheses.</p>
<dt><code>(</code><i>criterion1 criterion2</i> &#8230; <i>criterionN</i><code>)</code></p>
<dd> All messages that satisfy all of the given criteria.</p>
<dt><code>(or</code><i> criterion1 criterion2</i><code>)</code></p>
<dd> All messages that satisfy either <i>criterion1</i> or <i>criterion2</i>, or both. To connect more than two criteria using `or&#8217;, (or) specifications have to be nested using additional parentheses, as with `(or a&nbsp;<wbr>(or b c))&#8217;; `(or a b c)&#8217; means ((a or b) and c). For a simple `or&#8217; operation of independent criteria on the lowest nesting level, it is possible to achieve similar effects by using three separate criteria, as with `(a)&nbsp;<wbr>(b)&nbsp;<wbr>(c)&#8217;.</p>
<dt><code>(not</code><i> criterion</i><code>)</code></p>
<dd> All messages that do not satisfy <i>criterion</i>.</p>
<dt><code>(bcc</code><i> string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in the `envelope&#8217; representation of the <i>Bcc:</i> field.</p>
<dt><code>(cc</code><i> string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in the `envelope&#8217; representation of the <i>Cc:</i> field.</p>
<dt><code>(from</code><i> string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in the `envelope&#8217; representation of the <i>From:</i> field.</p>
<dt><code>(subject</code><i> string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in the <i>Subject:</i> field.</p>
<dt><code>(to</code><i> string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in the `envelope&#8217; representation of the <i>To:</i> field.</p>
<dt><code>(header</code><i> name string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in the specified <i>Name:</i> field.</p>
<dt><code>(body</code><i> string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in their body.</p>
<dt><code>(text</code><i> string</i><code>)</code></p>
<dd> All messages that contain <i>string</i> in their header or body.</p>
<dt><code>(larger</code><i> size</i><code>)</code></p>
<dd> All messages that are larger than <i>size</i> (in bytes).</p>
<dt><code>(smaller</code><i> size</i><code>)</code></p>
<dd> All messages that are smaller than <i>size</i> (in bytes).</p>
<dt><code>(before</code><i> date</i><code>)</code></p>
<dd> All messages that were received before <i>date</i>; <i>date</i> must be in the form <i>d</i>[<i>d</i>]<code>&#8211;</code><i>mon</i><code>&#8211;</code><i>yyyy</i>, where <i>d</i>[<i>d</i>] is the day of the month as one or two digits, <i>mon</i> is the name of the month&#8212;one of `Jan&#8217;, `Feb&#8217;, `Mar&#8217;, `Apr&#8217;, `May&#8217;, `Jun&#8217;, `Jul&#8217;, `Aug&#8217;, `Sep&#8217;, `Oct&#8217;, `Nov&#8217;, or `Dec&#8217;, and <i>yyyy</i> is the year as four digits; e.g. &quot;30-Aug-2004&quot;.</p>
<dt><code>(on</code><i> date</i><code>)</code></p>
<dd> All messages that were received on the specified date.</p>
<dt><code>(since</code><i> date</i><code>)</code></p>
<dd> All messages that were received since the specified date.</p>
<dt><code>(sentbefore</code><i> date</i><code>)</code></p>
<dd> All messages that were sent on the specified date.</p>
<dt><code>(senton</code><i> date</i><code>)</code></p>
<dd> All messages that were sent on the specified date.</p>
<dt><code>(sentsince</code><i> date</i><code>)</code></p>
<dd> All messages that were sent since the specified date.</p>
<dt><code>()</code></p>
<dd> The same criterion as for the previous search. This specification cannot be used as part of another criterion. If the previous command line contained more than one independent criterion, the last of those criteria is used.</dl>
<p> A practical method to read a set of messages is to issue a <i>from</i> command with the search criteria first to check for appropriate messages, and to read each single message then by typing `<code>`</code>&#8216; repeatedly.</p>
<h3>Replying to or originating mail</h3>
<p> The <i>reply</i> command can be used to set up a response to a message, sending it back to the person who it was from. Text the user types in then, up to an end-of-file, defines the contents of the message. While the user is composing a message, <i>mailx</i> treats lines beginning with the character `~&#8217; specially. For instance, typing `~m&#8217; (alone on a line) will place a copy of the current message into the response right shifting it by a tabstop (see <i>indentprefix</i> variable, below). Other escapes will set up subject fields, add and delete recipients to the message, attach files to it and allow the user to escape to an editor to revise the message or to a shell to run some commands. (These options are given in the summary below.)</p>
<h3>Ending a mail processing session</h3>
<p> The user can end a <i>mailx</i> session with the quit (`q&#8217;) command. Messages which have been examined go to the user&#8217;s mbox file unless they have been deleted in which case they are discarded. Unexamined messages go back to the post office. (See the -f option above).</p>
<h3>Personal and systemwide distribution lists</h3>
<p> It is also possible to create a personal distribution lists so that, for instance, the user can send mail to `<i>cohorts</i>&#8216; and have it go to a group of people. Such lists can be defined by placing a line like </p>
<pre>
        <code>alias</code><i> cohorts bill ozalp jkf mark kridle [at] ucbcory</i>
</pre>
<p> in the file .mailrc in the user&#8217;s home directory. The current list of such aliases can be displayed with the alias command in <i>mailx</i>. System wide distribution lists can be created by editing /etc/aliases, see <i><a href="/docs/linux/man/5-aliases/">aliases</a></i>(5) and <i><a href="/docs/linux/man/8-sendmail/">sendmail</a></i>(8); these are kept in a different syntax. In mail the user sends, personal aliases will be expanded in mail sent to others so that they will be able to reply to the recipients. System wide aliases are not expanded when the mail is sent, but any reply returned to the machine will have the system wide alias expanded as all mail goes through sendmail.</p>
<h3>Recipient address specifications</h3>
<p> When an address is used to name a recipient (in any of To, Cc, or Bcc), names of local mail folders and pipes to external commands can also be specified; the message text is then written to them. The rules are: Any name which starts with a `<code>|</code>&#8216; character specifies a pipe, the command string following the `|&#8217; is executed and the message is sent to its standard input; any other name which contains a `<code>@</code>&#8216; character is treated as a mail address; any other name which starts with a `<code>+</code>&#8216; character specifies a folder name; any other name which contains a `<code>/</code>&#8216; character but no `<code>!</code>&#8216; or `<code>%</code>&#8216; character before also specifies a folder name; what remains is treated as a mail address. Compressed folders are handled as described for the <i>folder</i> command below.</p>
<h3>Network mail (Internet / ARPA, UUCP, Berknet)</h3>
<p> See <i><a href="/docs/linux/man/7-mailaddr/">mailaddr</a></i>(7) for a description of network addresses. <i>Mailx</i> has a number of options which can be set in the .mailrc file to alter its behavior; thus `<i>set askcc</i>&#8216; enables the askcc feature. (These options are summarized below).</p>
<h3>MIME types</h3>
<p> For any outgoing attachment, <i>mailx</i> tries to determine the content type. It does this by reading MIME type files whose lines have the following syntax: </p>
<pre>
        <i>type</i><code>/</code><i>subtype      extension </i>[<i>extension </i>. . .]
</pre>
<p> where type/subtype are strings describing the file contents, and extension is the part of a filename starting after the last dot. Any line not immediately beginning with an ASCII alphabetical character is ignored by <i>mailx</i>. If there is a match with the extension of the file to attach, the given type/subtype pair is used. Otherwise, or if the filename has no extension, the content types text/plain or application/octet-stream are used, the first for text or international text files, the second for any file that contains formatting characters other than newlines and horizontal tabulators.</p>
<h3>Character sets</h3>
<p> <i>Mailx</i> normally detects the character set of the terminal using the LC_CTYPE locale setting. If the locale cannot be used appropriately, the <i>ttycharset</i> variable should be set to provide an explicit value. When reading messages, their text is converted to the terminal character set if possible. Unprintable characters and illegal byte sequences are detected and replaced by Unicode substitute characters or question marks unless the <i>print-all-chars</i> is set at initialization time. </p>
<p> The character set for outgoing messages is not necessarily the same as the one used on the terminal. If an outgoing text message contains characters not representable in US-ASCII, the character set being used must be declared within its header. Permissible values can be declared using the <i>sendcharsets</i> variable, separated by commas; <i>mailx</i> tries each of the values in order and uses the first appropriate one. If the message contains characters that cannot be represented in any of the given character sets, the message will not be sent, and its text will be saved to the `dead.letter&#8217; file. Messages that contain NUL bytes are not converted. </p>
<p> Outgoing attachments are converted if they are plain text. If the <i>sendcharsets</i> variable contains more than one character set name, the <i>~@</i> tilde escape will ask for the character sets for individual attachments if it is invoked without arguments. </p>
<p> Best results are usually achieved when <i>mailx</i> is run in a UTF-8 locale on a UTF-8 capable terminal. In this setup, characters from various countries can be displayed, while it is still possible to use more simple character sets for sending to retain maximum compatibility with older mail clients.</p>
<h3>Commands</h3>
<p> Each command is typed on a line by itself, and may take arguments following the command word. The command need not be typed in its entirety &#8211; the first command which matches the typed prefix is used. For commands which take message lists as arguments, if no message list is given, then the next message forward which satisfies the command&#8217;s requirements is used. If there are no messages forward of the current message, the search proceeds backwards, and if there are no good messages at all, <i>mailx</i> types `<i>applicable messages</i>&#8216; and aborts the command. If the command begins with a <i>#</i> sign, the line is ignored. </p>
<p> The arguments to commands can be quoted, using the following methods:</p>
<dl>
<dt>&bull;</p>
<dd> An argument can be enclosed between paired double-quotes &quot;&quot; or single-quotes &#8221;; any white space, shell word expansion, or backslash characters within the quotes are treated literally as part of the argument. A double-quote will be treated literally within single-quotes and vice versa. These special properties of the quote marks occur only when they are paired at the beginning and end of the argument.</p>
<dt>&bull;</p>
<dd> A backslash outside of the enclosing quotes is discarded and the following character is treated literally as part of the argument.</p>
<dt>&bull;</p>
<dd> An unquoted backslash at the end of a command line is discarded and the next line continues the command.</dl>
<p> Filenames, where expected, are subjected to the following transformations, in sequence:</p>
<dl>
<dt>&bull;</p>
<dd> If the filename begins with an unquoted plus sign, and the <i>folder</i> variable is defined, the plus sign will be replaced by the value of the <i>folder</i> variable followed by a slash. If the <i>folder</i> variable is unset or is set to null, the filename will be unchanged.</p>
<dt>&bull;</p>
<dd> Shell word expansions are applied to the filename. If more than a single pathname results from this expansion and the command is expecting one file, an error results.</dl>
<p> The following commands are provided:</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> Print out the preceding message. If given a numeric argument n, goes to the n&#8217;th previous message and prints it.</p>
<dt><code>?</code></p>
<dd> Prints a brief summary of commands.</p>
<dt><code>!</code></p>
<dd> Executes the shell (see <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) and <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1)) command which follows.</p>
<dt><code>|</code></p>
<dd> A synonym for the <i>pipe</i> command.</p>
<dt><code>account</code></p>
<dd> (ac) Creates, selects or lists an email account. An account is formed by a group of commands, primarily of those to set variables. With two arguments, of which the second is a `{&#8216;, the first argument gives an account name, and the following lines create a group of commands for that account until a line containing a single `}&#8217; appears. With one argument, the previously created group of commands for the account name is executed, and a <i>folder</i> command is executed for the system mailbox or inbox of that account. Without arguments, the list of accounts and their contents are printed. As an example, </p>
<pre><code>
account myisp
{
    set folder = imaps : // mylogin@imap.myisp.example
                         set record = +Sent
                                          set from = "myname [at] myisp.example (My Name)" set smtp = smtp.myisp.example
}
</code></pre>
<p> creates an account named `myisp&#8217; which can later be selected by specifying `account myisp&#8217;.</p>
<dt><code>alias</code></p>
<dd> (a) With no arguments, prints out all currently-defined aliases. With one argument, prints out that alias. With more than one argument, creates a new alias or changes an old one.</p>
<dt><code>alternates</code></p>
<dd> (alt) The alternates command is useful if the user has accounts on several machines. It can be used to inform <i>mailx</i> that the listed addresses all belong to the invoking user. When he replies to messages, <i>mailx</i> will not send a copy of the message to any of the addresses listed on the alternates list. If the alternates command is given with no argument, the current set of alternate names is displayed.</p>
<dt><code>answered</code></p>
<dd> (ans) Takes a message list and marks each message as a having been answered. This mark has no technical meaning in the mail system; it just causes messages to be marked in the header summary, and makes them specially addressable.</p>
<dt><code>cache</code></p>
<dd> Only applicable to cached IMAP mailboxes; takes a message list and reads the specified messages into the IMAP cache.</p>
<dt><code>call</code></p>
<dd> Calls a macro (see the <i>define</i> command).</p>
<dt><code>cd</code></p>
<dd> Same as chdir.</p>
<dt><code>certsave</code></p>
<dd> Only applicable to S/MIME signed messages. Takes a message list and a file name and saves the certificates contained within the message signatures to the named file in both human-readable and PEM format. The certificates can later be used to send encrypted messages to the messages&#8217; originators by setting the <i>smime-encrypt-user [at] host</i> variable.</p>
<dt><code>chdir</code></p>
<dd> (ch) Changes the user&#8217;s working directory to that specified, if given. If no directory is given, then changes to the user&#8217;s login directory.</p>
<dt><code>classify</code></p>
<dd> (cl) Takes a list of messages and examines their contents for characteristics of junk mail using Bayesian filtering. Messages considered to be junk are then marked as such. The junk mail database is not changed.</p>
<dt><code>collapse</code></p>
<dd> (coll) Only applicable to threaded mode. Takes a message list and makes all replies to these messages invisible in header summaries, unless they are in state `new&#8217;.</p>
<dt><code>connect</code></p>
<dd> (conn) If operating in disconnected mode on an IMAP mailbox, switch to online mode and connect to the mail server while retaining the mailbox status. See the description of the <i>disconnected</i> variable for more information.</p>
<dt><code>copy</code></p>
<dd> (c) The copy command does the same thing that <i>save</i> does, except that it does not mark the messages it is used on for deletion when the user quits. Compressed files and IMAP mailboxes are handled as described for the <i>folder</i> command.</p>
<dt><code>Copy</code></p>
<dd> (C) Similar to <i>copy</i>, but saves the messages in a file named after the local part of the sender address of the first message.</p>
<dt><code>decrypt</code></p>
<dd> (dec) For unencrypted messages, this command is identical to <i>copy</i>. Encrypted messages are first decrypted, if possible, and then copied.</p>
<dt><code>Decrypt</code></p>
<dd> (Dec) Similar to <i>decrypt</i>, but saves the messages in a file named after the local part of the sender address of the first message.</p>
<dt><code>define</code></p>
<dd> (def) Defines a macro. A macro definition is a sequence of commands in the following form: </p>
<pre>
    <code>define</code> <i>name</i><code> {</code>
        <i>command1</i>
        <i>command2</i>
        ...
        <i>commandN</i>
    <code>}</code>
</pre>
<p> Once defined, a macro can be explicitly invoked using the <i>call</i> command, or can be implicitly invoked by setting the <i>folder-hook</i> or <i>folder-hook-fullname</i> variables.</p>
<dt><code>defines</code></p>
<dd> Prints the currently defined macros including their contents.</p>
<dt><code>delete</code></p>
<dd> (d) Takes a list of messages as argument and marks them all as deleted. Deleted messages will not be saved in mbox, nor will they be available for most other commands.</p>
<dt><code>discard</code></p>
<dd> Same as ignore.</p>
<dt><code>disconnect</code></p>
<dd> (disco) If operating in online mode on an IMAP mailbox, switch to disconnected mode while retaining the mailbox status. See the description of the <i>disconnected</i> variable for more information. A list of messages may optionally be given as argument; the respective messages are then read into the cache before the connection is closed. Thus `disco *&#8217; makes the entire current mailbox available for disconnected use.</p>
<dt><code>dp</code>&nbsp;<wbr>or<code>&nbsp;<wbr>dt</code></p>
<dd> Deletes the current message and prints the next message. If there is no next message, <i>mailx</i> says `<i>at EOF</i>&#8216;.</p>
<dt><code>draft</code></p>
<dd> Takes a message list and marks each message as a draft. This mark has no technical meaning in the mail system; it just causes messages to be marked in the header summary, and makes them specially addressable.</p>
<dt><code>echo</code></p>
<dd> Echoes its arguments, resolving special names as documented for the folder command. The escape sequences `<code></code>&#8216;, `<code></code>&#8216;, `<code>
