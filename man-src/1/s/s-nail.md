---

title: "s-nail(1)"
name: "s-nail"
section: "1"
letter: "s"
url: "/docs/linux/man/1-s-nail/"
description: "S-nail [v14.9.23] – send and receive Internet mail"
---

<p> <code>S-nail [v14.9.23]</code> - send and receive Internet mail </p>
<p> <code>s-nail</code> [-<code>DdEFinv~#</code> ] [-<code>: </code><i>spec</i> ] [-<code>A </code><i>account</i> ] [: <code>-a </code><i>attachment </i><code>:</code> ] [: <code>-b </code><i>bcc-addr </i><code>:</code> ] [: <code>-C </code><i>field: body </i><code>:</code> ] [: <code>-c </code><i>cc-addr </i><code>:</code> ] [-<code>M </code><i>type | -</i><code>m </code><i>file | -</i><code>q </code><i>file | -</i><code>t</code> ] [-<code>r </code><i>from-addr</i> ] [: <code>-S&nbsp; </code><i>var </i>[<code>= </code><i>value </i><code>: </code>] ] [-<code>s </code><i>subject</i> ] [: <code>-T </code><i>field: addr </i><code>:</code> ] [: <code>-X </code><i>cmd </i><code>:</code> ] [: <code>-Y </code><i>cmd </i><code>:</code> ] [-<code>.</code> ] : <i>to-addr </i><code>:</code> [-<code>-~ : </code><i>mta-option </i><code>:</code> ] </p>
<p> <br />
<code>s-nail</code> [-<code>DdEeHiNnRv~#</code> ] [-<code>: </code><i>spec</i> ] [-<code>A </code><i>account</i> ] [: <code>-C </code><i>field: body </i><code>:</code> ] [-<code>L </code><i>spec</i> ] [-<code>r </code><i>from-addr</i> ] [: <code>-S&nbsp; </code><i>var </i>[<code>= </code><i>value </i><code>: </code>] ] [-<code>u </code><i>user</i> ] [: <code>-X </code><i>cmd </i><code>:</code> ] [: <code>-Y </code><i>cmd </i><code>:</code> ] [-<code>-~ : </code><i>mta-option </i><code>:</code> ] <br />
<code>s-nail</code> [-<code>DdEeHiNnRv~#</code> ] [-<code>: </code><i>spec</i> ] [-<code>A </code><i>account</i> ] [: <code>-C </code><i>field: body </i><code>:</code> ] -<code>f</code> [-<code>L </code><i>spec</i> ] [-<code>r </code><i>from-addr</i> ] [: <code>-S&nbsp; </code><i>var </i>[<code>= </code><i>value </i><code>: </code>] ] [: <code>-X </code><i>cmd </i><code>:</code> ] [: <code>-Y </code><i>cmd </i><code>:</code> ] [<i>file</i> ] [-<code>-~ : </code><i>mta-option </i><code>:</code> ] </p>
<p> <br />
<code>s-nail</code> -<code>h | --help</code> <br />
<code>s-nail</code> -<code>V | --version</code>  </p>
<blockquote><p> <code>Note:</code> S-nail (S-nail) will see major changes in v15.0 (circa 2022). Some backward incompatibilities cannot be avoided. Sx COMMANDS change to Sx Shell-style argument quoting , and shell metacharacters will become (more) meaningful. Some commands accept new syntax today via <code>wysh</code> ( Sx Command modifiers ) Behaviour is flagged [v15-compat] and [no v15-compat], <code>set ting</code> <i>v15-compat</i> ( Sx INTERNAL VARIABLES will choose new behaviour when applicable; giving it a value makes <code>wysh</code> an implied default. [Obsolete] flags what will vanish. </p>
<p> <code>Warning!</code> <i>v15-compat</i> (with value) will be a default in v14.10.0! </p>
</blockquote>
<p> S-nail provides a simple and friendly environment for sending and receiving mail. It is intended to provide the functionality of the POSIX <a href="/docs/linux/man/1-mailx/">mailx</a>(1) command, but is MIME capable and optionally offers extensions for line editing, S/MIME, SMTP and POP3, among others. S-nail divides incoming mail into its constituent messages and allows the user to deal with them in any order. It offers many Sx COMMANDS and Sx INTERNAL VARIABLES for manipulating messages and sending mail. It provides the user simple editing capabilities to ease the composition of outgoing messages, and increasingly powerful and reliable non-interactive scripting capabilities.  </p>
<h3>Options</h3>
<dl>
<dt><code>-: </code><i>spec , -</i><code>-resource-files =..</code></dt>
<dd> <p> Controls loading of (as via <code>source</code> Sx Resource files : <i>spec</i> is parsed case-insensitively, the letter `s&#8217; corresponds to the system wide s-nail.rc `u&#8217; the user&#8217;s personal file ~/.mailrc The (original) system wide resource is also compiled-in, accessible via `x&#8217; The letters `-&#8216; and `/&#8216; disable usage of resource files. Order matters, default is `su&#8217; This option overrides -<code>n</code> </p>
 </dd>
<dt><code>-A </code><i>name , -</i><code>-account =..</code></dt>
<dd> <p> Activate user <code>account</code> <i>name</i> after program startup is complete (resource files loaded, only -<code>X</code> commands are to be executed), and switch to its Sx primary system mailbox (most likely the <i>inbox )</i> If activation fails the program e <code>xit s if used non-interactively, or if any of</code> <i>errexit</i> or <i>posix</i> are set. </p>
 </dd>
<dt><code>-a </code><i>file </i>[<i>=input-charset </i>[<i>#output-charset </i>] ] </dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;Fl Fl attach Ns&nbsp;=.. (Send mode) Attach <i>file</i> For (Compose mode) opportunities refer to <code>~@</code> and <code>~^</code> <i>file</i> is subject to tilde expansion (see Sx Filename transformations and <code>folder )</code> if it is not accessible but contains a `=&#8216; character, anything before the last `=&#8216; will be used as the filename, anything thereafter as a character set specification, as shown. </p>
<p> If only an input character set is specified, the input side is fixed, and no character set conversion will be applied; an empty or the special string hyphen-minus `-&#8216; is taken for <i>ttycharset</i> (the default). If an output character set has also been specified the desired conversion is performed immediately, not considering file type and content, except for an empty string or hyphen-minus `-&#8216; , which select the default conversion algorithm (see Sx Character sets ) : no immediate conversion is performed, <i>file</i> and its contents will be MIME-classified ( Sx HTML mail and MIME attachments , The mime.types files) first --- only the latter mode is available unless <i>features</i> includes `,+iconv,&#8216; </p>
 </dd>
<dt><code>-B</code></dt>
<dd> <p> ([Obsolete]: S-nail will always use line-buffered output, to gain line-buffered input even in batch mode enable batch mode via -<code># .</code> </p>
 </dd>
<dt><code>-b </code><i>addr , -</i><code>-bcc =..</code></dt>
<dd> <p> (Send mode) Send a blind carbon copy to recipient <i>addr</i> The option may be used multiple times. Also see the section Sx On sending mail, and non-interactive mode . </p>
 </dd>
<dt><code>-C </code><i>field: body , -</i><code>-custom-header =..</code></dt>
<dd> <p> Create a custom header which persists for an entire session. A custom header consists of the field name followed by a colon `:&#8216; and the field content body, for example `-C&#8217; Blah: Neminem laede; imo omnes, quantum potes, juva . Standard header field names cannot be overwritten by custom headers. Runtime adjustable custom headers are available via the variable <i>customhdr</i> and in (Compose mode) <code>~^</code> one of the Sx COMMAND ESCAPES , as well as <code>digmsg</code> are the most flexible and powerful options to manage message headers. This option may be used multiple times. </p>
 </dd>
<dt><code>-c </code><i>addr , -</i><code>-cc =..</code></dt>
<dd> <p> (Send mode) Just like -<code>b</code> except it places the argument in the list of carbon copies. </p>
 </dd>
<dt><code>-D , --disconnected</code></dt>
<dd> <p> [Option] Startup with <i>disconnected</i> <code>set</code> </p>
 </dd>
<dt><code>-d , --debug</code></dt>
<dd> <p> Enter a debug-only sandbox mode by setting the internal variable <i>debug</i> the same can be achieved via `-<code>S</code> &#8216; Va debug or `<code>set</code> &#8216; Va debug . Also see -<code>v</code> </p>
 </dd>
<dt><code>-E , --discard-empty-messages</code></dt>
<dd> <p> (Send mode) <code>set</code> <i>skipemptybody</i> and thus discard messages with an empty message part body, successfully. </p>
 </dd>
<dt><code>-e , --check-and-exit</code></dt>
<dd> <p> Just check if mail is present (in the system <i>inbox</i> or the one specified via -<code>f )</code> if yes, return an exit status of zero, a non-zero value otherwise. To restrict the set of mails to consider in this evaluation a message specification can be added with the option -<code>L</code> Quickrun: does not open an interactive session. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> (Send mode) Save the message to send in a file named after the local part of the first recipient&#8217;s address (instead of in <i>record </i><code>).</code> </p>
 </dd>
<dt><code>-f , --file</code></dt>
<dd> <p> Read in the contents of the user&#8217;s Sx secondary mailbox <code>MBOX</code> (or the specified file) for processing; when S-nail is quit, it writes undeleted messages back to this file (but be aware of the <i>hold</i> option). The optional <i>file</i> argument will undergo some special Sx Filename transformations (as via <code>folder )</code> Note that <i>file</i> is not an argument to the flag -<code>f</code> but is instead taken from the command line after option processing has been completed. In order to use a <i>file</i> that starts with a hyphen-minus, prefix with a relative path, as in `./-hyphenbox.mbox&#8217; </p>
 </dd>
<dt><code>-H , --header-summary</code></dt>
<dd> <p> Display a summary of <code>headers</code> for the given <code>folder</code> (depending on -<code>u</code> <i>inbox</i> or <code>MAIL</code> or as specified via -<code>f )</code> then exit. A configurable summary view is available via the option -<code>L</code> This mode does not honour <i>showlast</i> Quickrun: does not open an interactive session. </p>
 </dd>
<dt><code>-h , --help</code></dt>
<dd> <p> Show a brief usage summary; use -<code>-long-help</code> for a list long options. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> <code>set</code> <i>ignore</i> to ignore tty interrupt signals. </p>
 </dd>
<dt><code>-L </code><i>spec , -</i><code>-search =..</code></dt>
<dd> <p> Display a summary of <code>headers</code> of all messages that match the given <i>spec</i> in the <code>folder</code> found by the same algorithm used by -<code>H</code> then exit. See the section Sx Specifying messages for the format of <i>spec</i> This mode does not honour <i>showlast</i> </p>
<p> If the -<code>e</code> option has been given in addition no header summary is produced, but S-nail will instead indicate via its exit status whether <i>spec</i> matched any messages ( `0&#8217; or not ( `1&#8217; ); note that any verbose output is suppressed in this mode and must instead be enabled explicitly (see -<code>v )</code> Quickrun: does not open an interactive session. </p>
 </dd>
<dt><code>-M </code><i>type</i></dt>
<dd> <p> (Send mode) Will flag standard input with the MIME `Content-Type:&#8216; set to the given known <i>type</i> ( Sx HTML mail and MIME attachments , The mime.types files and use it as the main message body. [v15 behaviour may differ] Using this option will bypass processing of <i>message-inject-head</i> and <i>message-inject-tail</i> Also see -<code>q , m , t</code> </p>
 </dd>
<dt><code>-m </code><i>file</i></dt>
<dd> <p> (Send mode) MIME classify the specified <i>file</i> and use it as the main message body. [v15 behaviour may differ] Using this option will bypass processing of <i>message-inject-head</i> and <i>message-inject-tail</i> Also see -<code>q , M , t</code> </p>
 </dd>
<dt><code>-N , --no-header-summary</code></dt>
<dd> <p> inhibit the initial display of message headers when reading mail or editing a mailbox <code>folder</code> by calling <code>unset</code> for the internal variable <i>header</i> </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Standard flag that inhibits reading the system wide s-nail.rc upon startup. The option -<code>:</code> allows more control over the startup sequence; also see Sx Resource files . </p>
 </dd>
<dt><code>-q </code><i>file , -</i><code>-quote-file =..</code></dt>
<dd> <p> (Send mode) Initialize the message body with the contents of <i>file</i> which may be standard input `-&#8216; only in non-interactive context. Also see -<code>M , m , t</code> </p>
 </dd>
<dt><code>-R , --read-only</code></dt>
<dd> <p> Any mailbox <code>folder</code> aka <code>folder</code> opened will be in read-only mode. </p>
 </dd>
<dt><code>-r </code><i>from-addr , -</i><code>-from-address =..</code></dt>
<dd> <p> The RFC 5321 reverse-path used for relaying and delegating messages to its destination(s), for example to report delivery errors, is normally derived from the address which appears in the <i>from</i> header (or, if that contains multiple addresses, in <i>sender )</i> A file-based aka local executable <i>mta</i> (Mail-Transfer-Agent), however, instead uses the local identity of the initiating user. </p>
<p> When this command line option is used the given single addressee <i>from-addr</i> will be assigned to the internal variable <i>from</i> but in addition the command line option -<code>f </code><i>from-addr</i> will be passed to a file-based <i>mta</i> whenever a message is sent. Shall <i>from-addr</i> include a user name the address components will be separated and the name part will be passed to a file-based <i>mta</i> individually via -<code>F </code><i>name</i> Even though not a recipient the `shquote&#8217; <i>expandaddr</i> flag is supported. </p>
<p> If an empty string is passed as <i>from-addr</i> then the content of the variable <i>from</i> (or, if that contains multiple addresses, <i>sender</i> will be evaluated and used for this purpose whenever the file-based <i>mta</i> is contacted. By default, without -<code>r</code> that is, neither -<code>f</code> nor -<code>F</code> command line options are used when contacting a file-based MTA, unless this automatic deduction is enforced by <code>set ting the internal variable</code> <i>r-option-implicit</i> </p>
<p> Remarks: many default installations and sites disallow overriding the local user identity like this unless either the MTA has been configured accordingly or the user is member of a group with special privileges. Passing an invalid address will cause an error. </p>
 </dd>
<dt><code>-S </code><i>var </i>[= <code>value , --set =..</code> ] </dt>
<dd> <p> <code>set</code> (or, with a prefix string `no&#8217; , as documented in Sx INTERNAL VARIABLES , <code>unset</code> <i>var </i><code>iable and optionally assign</code> <i>value</i> if supported; [v15 behaviour may differ] the entire expression is evaluated as if specified within dollar-single-quotes (see Sx Shell-style argument quoting ) if the internal variable <i>v15-compat</i> is set. If the operation fails the program will exit if any of <i>errexit</i> or <i>posix</i> are set. Settings established via -<code>S</code> cannot be changed from within Sx Resource files or an account switch initiated by -<code>A</code> They will become mutable again before commands registered via -<code>X</code> are executed. </p>
 </dd>
<dt><code>-s </code><i>subject , -</i><code>-subject =..</code></dt>
<dd> <p> (Send mode) Specify the subject of the message to be sent. Newline (NL) and carriage-return (CR) bytes are invalid and will be normalized to space (SP) characters. </p>
 </dd>
<dt><code>-T </code><i>field: addr , -</i><code>-target =..</code></dt>
<dd> <p> (Send mode) Add <i>addr</i> to the list of receivers targeted by <i>field</i> for now supported are only `bcc&#8217; , `cc&#8217; , `fcc&#8217; , and `to&#8217; Field and body (address) are separated by a colon `:&#8216; and optionally blank (space, tabulator) characters. The `shquote&#8217; <i>expandaddr</i> flag is supported. <i>addr</i> is parsed like a message header address line, as if it would be part of a template message fed in via -<code>t</code> and the same modifier suffix is supported. This option may be used multiple times. </p>
 </dd>
<dt><code>-t , --template</code></dt>
<dd> <p> (Send mode) The text message given (on standard input) is expected to contain, separated from the message body by an empty line, one or multiple plain text message headers. [v15 behaviour may differ] Readily prepared MIME mail messages cannot be passed. Headers can span multiple consecutive lines if follow lines start with any amount of whitespace. A line starting with the number sign `#&#8216; in the first column is ignored. Message recipients can be given via the message headers `To:&#8216; , `Cc:&#8216; , `Bcc:&#8216; (the `?single&#8217; modifier enforces treatment as a single addressee, for example `To?single:&#8216; exa, &lt;m@ple&gt; ) or `Fcc:&#8216; , they will be added to any recipients specified on the command line, and are likewise subject to <i>expandaddr</i> validity checks. If a message subject is specified via `Subject:&#8216; then it will be used in favour of one given on the command line. </p>
<p> More optional headers are `Reply-To:&#8216; (possibly overriding <i>reply-to )</i> `Sender:&#8216; ( <i>sender</i> `From:&#8216; ( <i>from</i> and / or option -<code>r )</code> `Message-ID:&#8216; , `In-Reply-To:&#8216; , `References:&#8216; and `Mail-Followup-To:&#8216; , by default created automatically dependent on message context, will be used if specified (a special address massage will however still occur for the latter). Any other custom header field (also see -<code>C</code> <i>customhdr</i> and <code>~^</code> is passed through entirely unchanged, and in conjunction with the options -<code>~</code> or -<code>#</code> it is possible to embed Sx COMMAND ESCAPES . Also see -<code>M , m , q</code> </p>
 </dd>
<dt><code>-u </code><i>user , -</i><code>-inbox-of =..</code></dt>
<dd> <p> Initially read the Sx primary system mailbox of <i>user</i> appropriate privileges presumed; effectively identical to `-<code>f</code> &#8216; Ns &nbsp;%user . </p>
 </dd>
<dt><code>-V , --version</code></dt>
<dd> <p> Show S-nails <i>version</i> and exit. The command <code>version</code> will also show the list of <i>features</i> `$&#8216; s-nail -:/ -Xversion -Xx . </p>
 </dd>
<dt><code>-v , --verbose</code></dt>
<dd> <p> <code>set s the internal variable</code> <i>verbose</i> to enable logging of informational context messages. (Increases level of verbosity when used multiple times.) Also see -<code>d</code> </p>
 </dd>
<dt><code>-X </code><i>cmd , -</i><code>-startup-cmd =..</code></dt>
<dd> <p> Add the given (or multiple for a multiline argument) <i>cmd</i> to a list of commands to be executed before normal operation starts. The commands will be evaluated as a unit, just as via <code>source</code> Correlates with -<code>#</code> and <i>errexit</i> </p>
 </dd>
<dt><code>-Y </code><i>cmd , -</i><code>-cmd =..</code></dt>
<dd> <p> Add the given (or multiple for a multiline argument) <i>cmd</i> to a list of commands to be executed after normal operation has started. The commands will be evaluated successively in the given order, and as if given on the program&#8217;s standard input --- before interactive prompting begins in interactive mode, after standard input has been consumed otherwise. </p>
 </dd>
<dt><code>-~ , --enable-cmd-escapes</code></dt>
<dd> <p> Enable Sx COMMAND ESCAPES in (Compose mode) even in non-interactive use cases. This can for example be used to automatically format the composed message text before sending the message: </p>
<blockquote><pre><code>$ ( echo 'line one. Word. Word2.';\
    echo '~| /usr/bin/fmt -tuw66' ) |\
  LC_ALL=C s-nail -d~:/ -Sttycharset=utf-8 bob [at] exam.ple
</code></pre>
</blockquote>
 </dd>
<dt><code>-# , --batch-mode</code></dt>
<dd> <p> Enables batch mode: standard input is made line buffered, the complete set of (interactive) commands is available, processing of Sx COMMAND ESCAPES is enabled in Sx Compose mode , and diverse Sx INTERNAL VARIABLES are adjusted for batch necessities, exactly as if done via -<code>S</code> <i>emptystart</i> no <i>errexit</i> no <i>header</i> no <i>posix</i> <i>quiet</i> <i>sendwait</i> <i>typescript-mode</i> as well as <code>MAIL</code> <code>MBOX</code> and <i>inbox</i> (the latter three to /dev/null ) Also, the values of <code>COLUMNS</code> and <code>LINES</code> are looked up, and acted upon. The following prepares an email message in a batched dry run: </p>
<blockquote><pre><code>$ for name in bob alice [at] exam.ple lisa [at] exam.ple; do
    printf 'mail %s\n~s ubject\nText\n~.\n' &quot;${name}&quot;
  done |
  LC_ALL=C s-nail -#:x -Smta=test \
    -X'alias bob bob [at] exam.ple'
</code></pre>
</blockquote>
 </dd>
<dt><code>-. , --end-options</code></dt>
<dd> <p> This flag forces termination of option processing in order to prevent ``option injection&#8217;&#8216; (attacks). It also forcefully puts S-nail into send mode, see Sx On sending mail, and non-interactive mode . </p>
 </dd></dl>
<p> If the setting of <i>expandargv</i> allows their recognition all <i>mta-option</i> arguments given at the end of the command line after a `--&#8216; separator will be passed through to a file-based <i>mta</i> (Mail-Transfer-Agent) and persist for the entire session. <i>expandargv</i> constraints do not apply to the content of <i>mta-arguments</i> Command line receiver address handling supports the `shquote&#8217; constraint of <i>expandaddr</i> for more please see Sx On sending mail, and non-interactive mode . </p>
<blockquote><pre><code>$ s-nail -#:/ -X 'addrcodec enc Hey, ho &lt;silver@go&gt;' -Xx
</code></pre>
</blockquote>
<h3>A starter</h3>
<p> S-nail is a direct descendant of BSD Mail, itself a successor to the Research UNIX mail which ``was there from the start&#8217;&#8216; according to Sx HISTORY . It thus represents the user side of the UNIX mail system, whereas the system side (Mail-Transfer-Agent, MTA) was traditionally taken by sendmail(8) (and most MTAs provide a binary of this name for compatibility reasons). If the [Option]al SMTP <i>mta</i> is included in the <i>features</i> of S-nail then the system side is not a mandatory precondition for mail delivery. </p>
<p> S-nail strives for compliance with the POSIX <a href="/docs/linux/man/1-mailx/">mailx</a>(1) standard, but <i>posix</i> one of the Sx INTERNAL VARIABLES , or its Sx ENVIRONMENT Ns al equivalent <code>POSIXLY_CORRECT</code> needs to be set to adjust behaviour to be almost on par. Almost, because there is one important difference: POSIX Sx Shell-style argument quoting is ([v15 behaviour may differ] increasingly) used instead of the Sx Old-style argument quoting that the standard documents, which is believed to be a feature. The builtin as well as the (default) global s-nail.rc Sx Resource files already bend the standard imposed settings a bit. </p>
<p> For example, <i>hold</i> and <i>keepsave</i> are <code>set</code> in order to suppress the automatic moving of messages to the Sx secondary mailbox <code>MBOX</code> that would otherwise occur (see Sx Message states ) , and <i>keep</i> to not remove empty system MBOX mailbox files (or all empty such files in <i>posix</i> mode) to avoid mangling of file permissions when files eventually get recreated. </p>
<p> To enter interactive mode even if the initial mailbox is empty <i>emptystart</i> is set, <i>editheaders</i> to allow editing of headers as well as <i>fullnames</i> to not strip down addresses in Sx Compose mode , and <i>quote</i> to include the message that is being responded to when <code>reply ing, which is indented by an</code> <i>indentprefix</i> that also deviates from standard imposed settings. <i>mime-counter-evidence</i> is fully enabled, too. It sets <i>followup-to-honour</i> and <i>reply-to-honour</i> to comply with reply address desires. </p>
<p> Credentials and other settings are easily addressable by grouping them via <code>account</code> The file mode creation mask can be managed with <i>umask</i> Files and shell pipe output can be <code>source d for</code> <code>eval uation, also during startup from within the</code> Sx Resource files . Informational context can be available by <code>set ting</code> <i>verbose</i> or <i>debug</i> (as via -<code>v , d )</code>  </p>
<h3>On sending mail, and non-interactive mode</h3>
<p> To send a message to one or more people, using a local or built-in <i>mta</i> (Mail-Transfer-Agent) transport to actually deliver the generated mail message, S-nail can be invoked with arguments which are the names of people to whom the mail will be sent, and the command line options -<code>b</code> and -<code>c</code> can be used to add (blind) carbon copy receivers: </p>
<blockquote><pre><code># Via test MTA
$ echo Hello, world | s-nail -:/ -Smta=test -s test $LOGNAME
# Viasendmail(1) MTA
$ &lt;/dev/null s-nail -:x -s test $LOGNAME
# Debug dry-run mode:
$ &lt;/dev/null LC_ALL=C s-nail -d -:/ \
   -Sttycharset=utf8 -Sfullnames \
   -b bcc [at] exam.ple -c cc [at] exam.ple -. \
   '(Lovely) Bob &lt;bob [at] exam.ple&gt;' eric [at] exam.ple
# With SMTP (no real sending due to -d debug dry-run)
$ LC_ALL=C s-nail -d -:/ -Sv15-compat -Sttycharset=utf8 \
    -S mta=smtps://mylogin@exam.ple:465 -Ssmtp-auth=none \
    -S from=scriptreply [at] exam.ple \
    -a /etc/mail.rc --end-options \
    eric [at] exam.ple &lt; /tmp/letter.txt
</code></pre>
</blockquote>
<p> Email addresses and plain user names are subject to <code>alternates</code> filtering, names only are first expanded through <code>alias</code> and <i>mta-aliases</i> An address in angle brackets consisting only of a valid local user `&lt;name&gt;&#8216; will be converted to a fully qualified address if either <i>hostname</i> is not set, or set to a non-empty value; if set to the empty value the conversion is left up to the <i>mta</i> By setting <i>expandaddr</i> fine-grained control of recipient address types other than user names and network addresses is possible. Recipients are classified as follows: any name that starts with a vertical bar `|&#8216; character specifies a command pipe - the command string following the `|&#8216; is executed and the message is sent to its standard input; likewise, any name that consists only of hyphen-minus `-&#8216; or starts with the character solidus `/&#8216; or the character sequence dot solidus `./&#8216; is treated as a file, regardless of the remaining content. Any other name which contains a commercial at `@&#8216; character is a network address; Any other name which starts with a plus sign `+&#8216; character is a mailbox name; Any other name which contains a solidus `/&#8216; character but no exclamation mark `!&#8216; or percent sign `%&#8216; character before is also a mailbox name; What remains is treated as a network address. This classification can be avoided by using a `Fcc:&#8216; header, see Sx Compose mode . </p>
<blockquote><pre><code>$ echo bla | s-nail -Sexpandaddr -s test ./mbox.mbox
$ echo bla | s-nail -Sexpandaddr -s test '|cat &gt;&gt; ./mbox.mbox'
$ echo safe | LC_ALL=C \
    s-nail -:/ -Smta=test -Sv15-compat -Sttycharset=utf8 \
      --set mime-force-sendout --set fullnames \
      -S expandaddr=fail,-all,+addr,failinvaddr -s test \
      --end-options 'Imagine John &lt;cold [at] turk.ey&gt;'
</code></pre>
</blockquote>
<p> Before messages are sent they undergo editing in Sx Compose mode . But many settings are static and can be set more generally. The envelope sender address for example is defined by <i>from</i> explicitly defining an originating <i>hostname</i> may be desirable, especially with the built-in SMTP Mail-Transfer-Agent <i>mta</i> Sx Character sets for outgoing message and MIME part content are configurable via <i>sendcharsets</i> whereas input data is assumed to be in <i>ttycharset</i> Message data will be passed over the wire in a <i>mime-encoding</i> and MIME parts aka attachments need a <code>mimetype</code> usually taken out of Sx The mime.types files . Saving copies of sent messages in a <i>record</i> mailbox may be desirable - as for most mailbox <code>folder</code> targets Sx Filename transformations will be performed. </p>
<p> For the purpose of arranging a complete environment of settings that can be switched to with a single command or command line option there are <code>account s</code> Alternatively a flat configuration could be possible, making use of so-called variable chains which automatically pick `USER [at] HOST&#8217; or `HOST&#8217; context-dependent variants some variables support: for example addressing `<code>Folder</code> &#8216; Ns pop3://yaa [at] exam.ple would find <i>pop3-no-apop-yaa [at] exam.ple</i> <i>pop3-no-apop-exam.ple</i> and <i>pop3-no-apop</i> in order. For more please see Sx On URL syntax and credential lookup and Sx INTERNAL VARIABLES . </p>
<p> To avoid environmental noise scripts should create a script-local environment, ideally with the command line options -<code>:</code> to disable configuration files in conjunction with repetitions of -<code>S</code> to specify variables: </p>
<blockquote><pre><code>$ env LC_ALL=C s-nail -:/ \
    -Sv15-compat \
    -Sttycharset=utf-8 -Smime-force-sendout \
    -Sexpandaddr=fail,-all,failinvaddr \
    -S mta=smtps://mylogin@exam.ple:465 -Ssmtp-auth=login \
    -S from=scriptreply [at] exam.ple \
    -s 'Subject to go' -a attachment_file \
    -Sfullnames -. \
    'Recipient 1 &lt;rec1 [at] exam.ple&gt;' rec2 [at] exam.ple \
    &lt; content_file
</code></pre>
</blockquote>
<p> As shown, scripts producing messages can ``fake&#8217;&#8216; a locale environment, the above specifies the all-compatible 7-bit clean <code>LC_ALL</code> ``C&#8217;&#8216; but will nonetheless take and send UTF-8 in the message text by using <i>ttycharset</i> If character set conversion is compiled in ( <i>features</i> includes the term `,+iconv,&#8216; ) invalid (according to <i>ttycharset</i> character input data would normally cause errors; setting <i>mime-force-sendout</i> will instead, as a last resort, classify the input as binary data, and therefore allow message creation to be successful. (Such content can then be inspected either by installing a <i>pipe-TYPE/SUBTYPE</i> handler for `application/octet-stream&#8217; , or possibly automatically through <i>mime-counter-evidence )</i> </p>
<p> In interactive mode, introduced soon, messages can be sent by calling the <code>mail</code> command with a list of recipient addresses: </p>
<blockquote><pre><code>$ s-nail -:/ -Squiet -Semptystart -Sfullnames -Smta=test
&quot;/var/spool/mail/user&quot;: 0 messages
? mail &quot;Recipient 1 &lt;rec1 [at] exam.ple&gt;&quot;, rec2 [at] exam.ple
...
? # Will do the right thing (tm)
? m rec1 [at] exam.ple rec2 [at] exam.ple
</code></pre>
</blockquote>
<h3>Compose mode</h3>
<p> If standard input is a terminal rather than the message to be sent, the user is expected to type in the message contents. In compose mode lines beginning with the character `~&#8216; (in fact the value of <i>escape</i> are special - these are so-called Sx COMMAND ESCAPES which can be used to read in files, process shell commands, add and edit attachments and more. For example <code>~v</code> or <code>~e</code> will start the <code>VISUAL</code> text <code>EDITOR</code> respectively, to revise the message in its current state, <code>~h</code> allows editing of the most important message headers, with the potent <code>~^</code> custom headers can be created, for example (more specifically than with -<code>C</code> and <i>customhdr )</i> [Option]ally <code>~?</code> gives an overview of most other available command escapes. </p>
<p> To create file-carbon-copies the special recipient header `Fcc:&#8216; may be used as often as desired, for example via <code>~^</code> Its entire value (or body in standard terms) is interpreted as a <code>folder</code> target, after having been subject to Sx Filename transformations : this is the only way to create a file-carbon-copy without introducing an ambiguity regarding the interpretation of the address, file names with leading vertical bars or commercial ats can be used. Like all other recipients `Fcc:&#8216; is subject to the checks of <i>expandaddr</i> Any local file and pipe command addressee honours the setting of <i>mbox-fcc-and-pcc</i> </p>
<p> Once finished with editing the command escape <code>~.</code> (see there) will call hooks, insert automatic injections and receivers, leave compose mode and send the message once it is completed. Aborting letter composition is possible with either of <code>~x</code> or <code>~q</code> the latter of which will save the message in the file denoted by <code>DEAD</code> unless no <i>save</i> is set. And unless <i>ignoreeof</i> is set the effect of <code>~.</code> can also be achieved by typing end-of-transmission (EOT) via `control-D&#8217; ( `^D&#8217; at the beginning of an empty line, and <code>~q</code> is always reachable by typing end-of-text (ETX) twice via `control-C&#8217; ( `^C&#8217; ). </p>
<p> The compose mode hooks <i>on-compose-enter , on-compose-splice , on-compose-leave</i> and <i>on-compose-cleanup</i> may be set to <code>define d macros and provide reliable and increasingly powerful mechanisms to</code> perform automated message adjustments dependent on message context, for example addition of message signatures ( <i>message-inject-head , message-inject-tail</i> or creation of additional receiver lists (also by setting <i>autocc , autobcc )</i> To achieve that the command <code>digmsg</code> may be used in order to query and adjust status of message(s). The splice hook can also make use of Sx COMMAND ESCAPES . ([v15 behaviour may differ] The compose mode hooks work for <code>forward , mail , reply</code> and variants; <code>resend</code> and <code>Resend</code> only provide the hooks <i>on-resend-enter</i> and <i>on-resend-cleanup</i> which are pretty restricted due to the nature of the operation.)  </p>
<h3>On reading mail, and more on interactive mode</h3>
<p> When invoked without addressees S-nail enters interactive mode in which mails may be read. When used like that the user&#8217;s system <i>inbox</i> (for more on mailbox types please see the command <code>folder</code> is read in and a one line header of each message therein is displayed if the variable <i>header</i> is set. The visual style of this summary of <code>headers</code> can be adjusted through the variable <i>headline</i> and the possible sorting criterion via <i>autosort</i> Scrolling through <i>screen </i><code>fuls of</code> <code>headers</code> can be performed with the command <code>z</code> If the initially opened mailbox is empty S-nail will instead exit immediately (after displaying a message) unless the variable <i>emptystart</i> is set. </p>
<p> At the <i>prompt</i> the command <code>list</code> will give a listing of all available commands and <code>help</code> will [Option]ally give a summary of some common ones. If the [Option]al documentation strings are available (see <i>features</i> one can type `help&#8217; X (or `?X&#8217; and see the actual expansion of `X&#8217; and what its purpose is, i.e., commands can be abbreviated (note that POSIX defines some abbreviations, so that the alphabetical order of commands does not necessarily relate to the abbreviations; it is however possible to define overwrites with <code>commandalias )</code> These commands can also produce a more <i>verbose</i> output. </p>
<p> Messages are given numbers (starting at 1) which uniquely identify messages; the current message - the ``dot&#8217;&#8216; - will either be the first new message, or the first unread message, or the first message of the mailbox; the internal variable <i>showlast</i> will instead cause usage of the last message for this purpose. The command <code>headers</code> will display a <i>screen </i><code>ful of header summaries containing the</code> ``dot&#8217;&#8216; whereas <code>from</code> will display only the summaries of the given messages, defaulting to the ``dot&#8217;&#8216; </p>
<p> Message content can be displayed with the command <code>type</code> ( `t&#8217; alias <code>print )</code> Here the variable <i>crt</i> controls whether and when S-nail will use the configured <code>PAGER</code> for display instead of directly writing to the user terminal <i>screen</i> the sole difference to the command <code>more</code> which will always use the <code>PAGER</code> The command <code>top</code> will instead only show the first <i>toplines</i> of a message (maybe even compressed if <i>topsqueeze</i> is set). Message display experience may improve by setting and adjusting <i>mime-counter-evidence</i> and also see Sx HTML mail and MIME attachments . </p>
<p> By default the current message ( ``dot&#8217;&#8216; is displayed, but like with many other commands it is possible to give a fancy message specification (see Sx Specifying messages ) , for example `t:u&#8217; will display all unread messages, `t.&#8216; will display the ``dot&#8217;&#8216; `t&#8217; 1 5 will type the messages 1 and 5, `t&#8217; 1-5 will type the messages 1 through 5, and `t-&#8216; and `t+&#8216; will display the previous and the next message, respectively. The command <code>search</code> (a more substantial alias for <code>from</code> will display a header summary of the given message specification list instead of their content; the following will search for subjects: </p>
<blockquote><p> <code>? from &quot;&#8216;@Some subject to search for&#8217;&quot;</code> </p>
</blockquote>
<p> In the default setup all header fields of a message will be <code>type d, but fields can be white- or blacklisted for a variety of</code> applications by using the command <code>headerpick</code> e.g., to restrict their display to a very restricted set for <code>type</code> `<code>headerpick</code> &#8216; Cd type retain Ar from to cc subject . In order to display all header fields of a message regardless of currently active ignore or retain lists, use the commands <code>Type</code> and <code>Top</code> <code>Show</code> will show the raw message content. Note that historically the global s-nail.rc not only adjusts the list of displayed headers, but also sets <i>crt</i> ([v15 behaviour may differ] A yet somewhat restricted) Reliable scriptable message inspection is available via <code>digmsg</code> </p>
<p> Dependent upon the configuration a line editor (see the section Sx On terminal control and line editor ) aims at making the user experience with the many Sx COMMANDS a bit nicer. When reading the system <i>inbox</i> or when -<code>f</code> (or <code>folder</code> specified a mailbox explicitly prefixed with the special `%:&#8216; modifier (to propagate it to a Sx primary system mailbox ) , then messages which have been read (see&nbsp; Sx Message states will be automatically moved to a Sx secondary mailbox , the user&#8217;s <code>MBOX</code> file, when the mailbox is left, either by changing the active mailbox or by quitting S-nail - this automatic moving from a system- or primary- to the secondary mailbox is not performed when the variable <i>hold</i> is set. Messages can also be explicitly <code>move d to other mailboxes, whereas</code> <code>copy</code> keeps the original message. <code>write</code> can be used to write out data content of specific parts of messages. </p>
<p> After examining a message the user can <code>reply `r&#8217; </code> to the sender and all recipients (which will also be placed in `To:&#8216; unless <i>recipients-in-cc</i> is set), or <code>Reply `R&#8217; </code> exclusively to the sender(s). To comply with with the receivers desired reply address the Sx quadoption Ns s <i>followup-to-honour</i> and <i>reply-to-honour</i> should usually be set. The commands <code>Lreply</code> and <code>Lfollowup</code> know how to apply a special addressee massage, see Sx Mailing lists . Dependent on the presence and value of <i>quote</i> the message being replied to will be included in a quoted form. <code>forward ing a message will allow editing the new message: the original message</code> will be contained in the message body, adjusted according to <code>headerpick</code> It is possible to <code>resend</code> or <code>Resend</code> messages: the former will add a series of `Resent-&#8216; headers, whereas the latter will not; different to newly created messages editing is not possible and no copy will be saved even with <i>record</i> unless the additional variable <i>record-resent</i> is set. When sending, replying or forwarding messages comments and full names will be stripped from recipient addresses unless the internal variable <i>fullnames</i> is set. </p>
<p> Of course messages can be <code>delete `d&#8217; </code> and they can spring into existence again via <code>undelete</code> or when the S-nail session is ended via the <code>exit</code> or <code>xit</code> commands to perform a quick program termation. To end a mail processing session regularly and perform a full program exit one may issue the command <code>quit</code> It will, among others, move read messages to the Sx secondary mailbox <code>MBOX</code> as necessary, discard deleted messages in the current mailbox, and update the [Option]al (see <i>features</i> line editor <i>history-file</i> By the way, whenever the main event loop is about to look out for the next input line it will trigger the hook <i>on-main-loop-tick</i>  </p>
<h3>HTML mail and MIME attachments</h3>
<p> HTML-only messages become more and more common, and many messages come bundled with a bouquet of MIME (Multipurpose Internet Mail Extensions) parts and attachments. To get a notion of MIME types there is a built-in default set, onto which the content of Sx The mime.types files will be added (as configured and allowed by <i>mimetypes-load-control )</i> Types can also become registered and listed with the command <code>mimetype</code> To improve interaction with the faulty MIME part declarations of real life <i>mime-counter-evidence</i> will allow verification of the given assertion, and the possible provision of an alternative, better MIME type. Note plain text parts will always be preferred in `multipart/alternative&#8217; MIME messages unless <i>mime-alternative-favour-rich</i> is set. </p>
<p> Whereas a simple HTML-to-text filter for displaying HTML messages is [Option]ally supported (indicated by `,+filter-html-tagsoup,&#8216; in <i>features )</i> MIME types other than plain text cannot be handled directly. To deal with specific non-text MIME types or file extensions programs need to be registered which either prepare (re-)integrable plain text versions of their input (a mode which is called <code>copiousoutput )</code> or display the content externally, for example in a graphical window: the latter type is only considered by and for the command <code>mimeview</code> </p>
<p> To install a handler program for a MIME type an according <i>pipe-TYPE/SUBTYPE</i> variable needs to be set; to define a handler for a file extension <i>pipe-EXTENSION</i> can be used - these handlers take precedence. [Option]ally mail user agent configuration is supported (see Sx The Mailcap files ) , and will be queried for display or quote handlers after the former ones. Type-markers registered via <code>mimetype</code> are the last possible source for information how to handle a MIME type. </p>
<p> For example, to display HTML messages integrated via the text browsers <a href="/docs/linux/man/1-lynx/">lynx</a>(1) or <a href="/docs/linux/man/1-elinks/">elinks</a>(1), register a MathML MIME type and enable its plain text display, and to open PDF attachments in an external PDF viewer, asynchronously and with some other magic attached: </p>
<blockquote><pre><code>? if &quot;$features&quot; !% ,+filter-html-tagsoup,
? #set pipe-text/html='?* elinks -force-html -dump 1'
? set pipe-text/html='?* lynx -stdin -dump -force_html'
? # Display HTML as plain text instead
? #set pipe-text/html=?t
? endif
? mimetype ?t application/mathml+xml mathml
? wysh set pipe-application/pdf='?&amp;=? \
    trap &quot;rm -f \&quot;${MAILX_FILENAME_TEMPORARY}\&quot;&quot; EXIT;\
    trap &quot;trap \&quot;\&quot; INT QUIT TERM; exit 1&quot; INT QUIT TERM;\
    mupdf &quot;${MAILX_FILENAME_TEMPORARY}&quot;'
? define showhtml {
? \localopts yes
? \set mime-alternative-favour-rich pipe-text/html=?h?
? \type &quot;$@&quot;
? }
? \commandalias html \\call showhtml
</code></pre>
</blockquote>
<h3>Mailing lists</h3>
<p> Known or subscribed-to mailing lists may be flagged in the summary of <code>headers</code> ( <i>headline</i> format character `%L&#8217; ) , and will gain special treatment when sending mails: the variable <i>followup-to-honour</i> will ensure that a `Mail-Followup-To:&#8216; header is honoured when a message is being replied to ( <code>reply</code> <code>followup</code> <code>Lreply</code> <code>Lfollowup )</code> and <i>followup-to</i> controls creation of this header when creating <code>mail s, if the necessary user setup</code> ( from , sender ) is available; then, it may also be created automatically, for example when list-replying via <code>Lreply</code> or <code>Lfollowup</code> when <code>followup</code> or <code>reply</code> is used and the messages `Mail-Followup-To:&#8216; is honoured etc. </p>
<p> The commands <code>mlist</code> and <code>mlsubscribe</code> manage S-nails notion of which addresses are mailing lists. With the [Option]al regular expression support any address which contains any of the magic regular expression characters `(&#8216; ^[*+?|$ ; see re_format7 or <a href="/docs/linux/man/7-regex/">regex</a>(7), dependent on the host system) will be compiled and used as one, possibly matching many addresses. It is not possible to escape the ``magic&#8217;&#8216; in order to match special characters as-is, bracket expressions must be used, for example `<code>search</code> &#8216; Li @subject@&#8216;[[]open bracket&#8217; . </p>
<blockquote><pre><code>? set followup-to followup-to-honour=ask-yes \
    reply-to-honour=ask-yes
? mlist a1 [at] b1.c1 a2 [at] b2.c2 '.*@lists\.c3$'
? mlsubscribe a4 [at] b4.c4 exact [at] lists.c3
</code></pre>
</blockquote>
<p> Known and subscribed lists differ in that for the latter the <i>user </i><code>s address is not part of a generated</code> `Mail-Followup-To:&#8216; There are exceptions, for example if multiple lists are addressed and not all have the subscription attribute. When replying to a message its list address ( `List-Post:&#8216; header) is automatically and temporarily treated like a known <code>mlist</code> dependent on the variable <i>reply-to-honour</i> an existing `Reply-To:&#8216; is used instead (if it is a single address on the same domain as `List-Post:&#8216; ) in order to accept a list administrator&#8217;s wish that is supposed to have been manifested like that. </p>
<p> For convenience and compatibility with mail programs that do not honour the non-standard M-F-T, an automatic user entry in the carbon-copy `Cc:&#8216; address list of generated message can be created by setting <i>followup-to-add-cc</i> This entry will be added whenever the user will be placed in the `Mail-Followup-To:&#8216; list, and is not a regular addressee already. <i>reply-to-swap-in</i> tries to deal with the address rewriting that many mailing-lists nowadays perform to work around DKIM / DMARC etc. standard imposed problems.  </p>
<h3>Signed and encrypted messages with S/MIME</h3>
<p> [Option] S/MIME provides two central mechanisms: message signing and message encryption. A signed message contains some data in addition to the regular text. The data can be used to verify that the message has been sent using a valid certificate, that the sender address matches that in the certificate, and that the message text has not been altered. Signing a message does not change its regular text; it can be read regardless of whether the recipients software is able to handle S/MIME. It is thus usually possible to sign all outgoing messages if so desired. </p>
<p> Encryption, in contrast, makes the message text invisible for all people except those who have access to the secret decryption key. To encrypt a message, the specific recipients public encryption key must be known. It is therefore not possible to send encrypted mail to people unless their key has been retrieved from either previous communication or public key directories. Because signing is performed with private keys, and encryption with public keys, messages should always be signed before being encrypted. </p>
<p> A central concept to S/MIME is that of the certification authority (CA). A CA is a trusted institution that issues certificates. For each of these certificates it can be verified that it really originates from the CA, provided that the CA&#8217;s own certificate is previously known. A set of CA certificates is usually delivered and installed together with the cryptographical library that is used on the local system. Therefore reasonable security for S/MIME on the Internet is provided if the source that provides that library installation is trusted. It is also possible to use a specific pool of trusted certificates. If this is desired, <i>smime-ca-no-defaults</i> should be set to avoid using the default certificate pool, and <i>smime-ca-file</i> and/or <i>smime-ca-dir</i> should be pointed to a trusted pool of certificates. A certificate cannot be more secure than the method its CA certificate has been retrieved with. </p>
<p> This trusted pool of certificates is used by the command <code>verify</code> to ensure that the given S/MIME messages can be trusted. If so, verified sender certificates that were embedded in signed messages can be saved locally with the command <code>certsave</code> and used by S-nail to encrypt further communication with these senders: </p>
<blockquote><pre><code>? certsave FILENAME
? set smime-encrypt-USER [at] HOST=FILENAME \
    smime-cipher-USER [at] HOST=AES256
</code></pre>
</blockquote>
<p> To sign outgoing messages, in order to allow receivers to verify the origin of these messages, a personal S/MIME certificate is required. S-nail supports password-protected personal certificates (and keys), see <i>smime-sign-cert</i> The section Sx On URL syntax and credential lookup gives an overview of the possible sources of user credentials, and Sx S/MIME step by step shows examplarily how a private S/MIME certificate can be obtained. In general, if such a private key plus certificate ``pair&#8217;&#8216; is available, all that needs to be done is to set some variables: </p>
<blockquote><pre><code>? set smime-sign-cert=ME [at] exam.ple.paired \
    smime-sign-digest=SHA512 \
    smime-sign from=myname [at] my.host
</code></pre>
</blockquote>
<p> Variables of interest for S/MIME in general are <i>smime-ca-dir</i> <i>smime-ca-file</i> <i>smime-ca-flags</i> <i>smime-ca-no-defaults</i> <i>smime-crl-dir</i> <i>smime-crl-file</i> For S/MIME signing of interest are <i>smime-sign</i> <i>smime-sign-cert</i> <i>smime-sign-include-certs</i> and <i>smime-sign-digest</i> Additional variables of interest for S/MIME en- and decryption: <i>smime-cipher</i> and <i>smime-encrypt-USER [at] HOST</i> Variables of secondary interest may be <i>content-description-smime-message</i> and <i>content-description-smime-signature</i> S/MIME is available if `,+smime,&#8216; is included in <i>features</i> </p>
<p> [v15 behaviour may differ] Note that neither S/MIME signing nor encryption applies to message subjects or other header fields yet. Thus they may not contain sensitive information for encrypted messages, and cannot be trusted even if the message content has been verified. When sending signed messages, it is recommended to repeat any important header information in the message text.  </p>
<h3>On URL syntax and credential lookup</h3>
<p> For accessing protocol-specific resources Uniform Resource Locators (URL, RFC 3986) have become omnipresent. Here they are expected in a ``normalized&#8217;&#8216; variant, not used in data exchange, but only meant as a compact, easy-to-use way of defining and representing information in a well-known notation; as such they do not conform to any real standard. Optional parts are placed in brackets `[]&#8216; , optional either because there also exist other ways to define the information, or because the part is protocol specific. `/path&#8217; for example is used by the [Option]al Maildir <code>folder</code> type and the IMAP protocol, but not by POP3. If `USER&#8217; and `PASSWORD&#8217; are included in an URL server specification, URL percent encoded (RFC 3986) forms are needed, generable with <code>urlcodec</code> </p>
<blockquote><p> <code>PROTOCOL://[USER[:PASSWORD]@]server[:port][/path]</code> </p>
</blockquote>
<p> Often Sx INTERNAL VARIABLES exist in multiple versions, called ``variable chains&#8217;&#8216; in this document: the plain `variable&#8217; as well as `variable-HOST&#8217; and `variable-USER [at] HOST&#8217; If a port was specified `HOST&#8217; really means `server:port&#8217; , not `server&#8217; And this `USER&#8217; is never in URL percent encoded form. For example, whether the hypothetical `<a href="smtp://wings%3Aof@a.dove'">smtp://wings%3Aof@a.dove&#8217;</a> including user and password was used, or whether it was `<a href="smtp://a.dove'">smtp://a.dove&#8217;</a> and it came from a different source, to lookup the chain <i>tls-config-pairs</i> first `tls-config-pairs-wings:of [at] a.dove&#8217; is looked up, then `tls-config-pairs-a.dove&#8217; , before finally looking up the plain variable. </p>
<p> The logic to collect (an <code>account s) credential information is as follows:</code> </p>
<ul>
<li> <p> A user is always required. If no `USER&#8217; has been given in the URL the variables <i>user-HOST</i> and <i>user</i> are looked up. Afterwards, when enforced by the [Option]al variables <i>netrc-lookup-HOST</i> or <i>netrc-lookup</i> Sx The .netrc file of the user will be searched for a `HOST&#8217; specific entry which provides a `login&#8217; name: only unambiguous entries are used (one possible matching entry for `HOST&#8217; ) . </p>
<p> If there is still no `USER&#8217; then the verified <code>LOGNAME</code> known to be a valid user on the current host, is used.  </li>
<li>  Authentication: unless otherwise noted the chain <i>PROTOCOL-auth-USER [at] HOST , PROTOCOL-auth-HOST , PROTOCOL-auth</i> is checked, falling back to a protocol-specific default as necessary.  </li>
<li>  If no `PASSWORD&#8217; has been given in the URL, then if the `USER&#8217; has been found through the [Option]al <i>netrc-lookup</i> that may have also provided the password. Otherwise the chain <i>password-USER [at] HOST , password-HOST , password</i> is looked up. </p>
<p> Thereafter the (now complete) [Option]al chain <i>netrc-lookup-USER [at] HOST , netrc-lookup-HOST , netrc-lookup</i> is checked, if set the <code>netrc</code> cache is searched for a password only (multiple user accounts for a single machine may exist as well as a fallback entry without user but with a password). </p>
<p> If at that point there is still no password available, but the (protocols&#8217;) chosen authentication type requires a password, then in interactive mode the user will be prompted on the terminal.  </li>
</ul>
 </p>
<p> <code>Note:</code> S/MIME verification works relative to the values found in the `From:&#8216; (or `Sender:&#8216; ) header field(s), which means the values of <i>smime-sign , smime-sign-cert , smime-sign-include-certs</i> and <i>smime-sign-digest</i> will not be looked up using the `USER&#8217; and `HOST&#8217; chains from above, but instead use the corresponding values from the message that is being worked on. If no address matches we assume and use the setting of <i>from</i> In unusual cases multiple and different `USER&#8217; and `HOST&#8217; combinations may therefore be involved - on the other hand those unusual cases become possible. The usual case is as short as: </p>
<blockquote><pre><code>set mta=smtp://USER:PASS@HOST smtp-use-starttls \
    smime-sign smime-sign-cert=+smime.pair \
    from=myname [at] my.host
</code></pre>
</blockquote>
<p> The section Sx EXAMPLES contains complete example configurations.  </p>
<h3>Encrypted network communication</h3>
<p> [Option] SSL (Secure Sockets Layer) aka its successor TLS (Transport Layer Security) are protocols which aid in securing communication by providing a safely initiated and encrypted network connection. A central concept of TLS are certificates: as part of each network connection setup a (set of) certificates will be exchanged through which the identity of the network peer can be cryptographically verified; if possible the TLS/SNI (ServerNameIndication) extension will be enabled to allow servers fine-grained control over the certificates being used. A locally installed pool of trusted certificates will then be inspected, and verification will succeed if it contains a(n in)direct signer of the presented certificate(s). </p>
<p> The local pool of trusted so-called CA (Certification Authority) certificates is usually delivered with and used along the TLS library. A custom pool of trusted certificates can be selected by pointing <i>tls-ca-file</i> and/or (with special preparation) <i>tls-ca-dir</i> to the desired location; setting <i>tls-ca-no-defaults</i> in addition will avoid additional inspection of the default pool. A certificate cannot be more secure than the method its CA certificate has been retrieved with. For inspection or other purposes, the certificate of a server (as seen when connecting to it) can be fetched with the command <code>tls</code> (port can usually be the protocol name, too, and <i>tls-verify</i> is taken into account here): </p>
<blockquote><pre><code>$ s-nail -vX 'tls certchain SERVER-URL[:PORT]; x'
</code></pre>
</blockquote>
<p> A local pool of CA certificates is not strictly necessary, however, server certificates can also be verified via their fingerprint. For this a message digest will be calculated and compared against the variable chain <i>tls-fingerprint</i> and verification will succeed if the fingerprint matches. The message digest (algorithm) can be configured via the variable chain <i>tls-fingerprint-digest</i> <code>tls</code> can again be used: </p>
<blockquote><pre><code>$ s-nail -X 'wysh set verbose; tls fingerprint SERVER-URL[:PORT]; x'
</code></pre>
</blockquote>
<p> It depends on the used protocol whether encrypted communication is possible, and which configuration steps have to be taken to enable it. Some protocols, like POP3S, are implicitly encrypted, others, like POP3, can upgrade a plain text connection if so requested. For example, to use the `STLS&#8217; that POP3 offers (a member of) the variable (chain) <i>pop3-use-starttls</i> needs to be set, with convenience via <code>shortcut</code> </p>
<blockquote><pre><code>shortcut encpop1 pop3s://pop1.exam.ple
shortcut encpop2 pop3://pop2.exam.ple
set pop3-use-starttls-pop2.exam.ple
set mta=smtps://smtp.exam.ple:465set mta=smtp://smtp.exam.ple smtp-use-starttls
</code></pre>
</blockquote>
<p> Normally that is all there is to do, given that TLS libraries try to provide safe defaults, plenty of knobs however exist to adjust settings. For example certificate verification settings can be fine-tuned via <i>tls-ca-flags</i> and the TLS configuration basics are accessible via <i>tls-config-pairs</i> for example to control protocol versions or cipher lists. In the past hints on how to restrict the set of protocols to highly secure ones were indicated, but as of the time of this writing the list of protocols or ciphers may need to become relaxed in order to be able to connect to some servers; the following example allows connecting to a ``Lion&#8217;&#8216; that uses OpenSSL 0.9.8za from June 2014 (refer to Sx INTERNAL VARIABLES for more on variable chains): </p>
<blockquote><pre><code>wysh set tls-config-pairs-lion [at] exam.ple='MinProtocol=TLSv1.1,\
    CipherString=TLSv1.2:!aNULL:!eNULL:\
      ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:\
      DHE-RSA-AES256-SHA:@STRENGTH'
</code></pre>
</blockquote>
<p> The OpenSSL program ciphers(1) should be referred to when creating a custom cipher list. Variables of interest for TLS in general are <i>tls-ca-dir</i> <i>tls-ca-file</i> <i>tls-ca-flags</i> <i>tls-ca-no-defaults</i> <i>tls-config-file</i> <i>tls-config-module</i> <i>tls-config-pairs</i> <i>tls-crl-dir</i> <i>tls-crl-file</i> <i>tls-rand-file</i> as well as <i>tls-verify</i> Also see <i>tls-features</i> TLS is available if `+tls&#8217; is included in <i>features</i>  </p>
<h3>Character sets</h3>
<p> [Option] The user&#8217;s locale environment is detected by looking at the <code>LC_ALL</code> environment variable. The internal variable <i>ttycharset</i> will be set to the detected terminal character set accordingly, and will thus show up in the output of commands like <code>set</code> and <code>varshow</code> This character set will be targeted when trying to display data, and user input data is expected to be in this character set, too. </p>
<p> When creating messages their character input data is classified. 7-bit clean text data and attachments will be classified as <i>charset-7bit</i> 8-bit data will [Option]ally be converted into members of <i>sendcharsets</i> until a character set conversion succeeds. <i>charset-8bit</i> is the implied default last member of this list. If no 8-bit character set is capable to represent input data, no message will be sent, and its text will optionally be <i>save </i><code>d</code> in <code>DEAD</code> If that is not acceptable, for example in script environments, <i>mime-force-sendout</i> can be set to force sending of non-convertible data as `application/octet-stream&#8217; classified binary content instead: like this receivers still have the option to inspect message content (for example via <i>mime-counter-evidence )</i> If the [Option]al character set conversion is not available ( <i>features</i> misses `,+iconv,&#8216; ) , <i>ttycharset</i> is the only supported character set for non 7-bit clean data, and it is simply assumed it can be used to exchange 8-bit messages. </p>
<p> <i>ttycharset</i> may also be given an explicit value to send mail in a completely ``faked&#8217;&#8216; locale environment, which can be used to generate and send for example 8-bit UTF-8 input data in a pure 7-bit US-ASCII `LC_ALL=C&#8217; environment (an example of this can be found in the section Sx On sending mail, and non-interactive mode ) . Due to lack of programming interfaces reading mail will not really work as expected in a faked environment: whereas <i>ttycharset</i> might be addressable, any output will be made safely printable, as via <code>vexpr</code> <code>makeprint</code> according to the actual locale environment, which is not affected by <i>ttycharset.</i> </p>
<p> Classifying 7-bit clean data as <i>charset-7bit</i> is a problem if the input character set ( <i>ttycharset</i> is a multibyte character set that is itself 7-bit clean. For example, the Japanese character set ISO-2022-JP is, but is capable to encode the rich set of Japanese Kanji, Hiragana and Katakana characters: in order to notify receivers of this character set the mail message must be MIME encoded so that the character set ISO-2022-JP can be advertised, otherwise an invalid email message would result! To achieve this, the variable <i>charset-7bit</i> can be set to ISO-2022-JP. (Today a better approach regarding email is the usage of UTF-8, which uses 8-bit bytes for non-US-ASCII data.) </p>
<p> When replying to a message and the variable <i>reply-in-same-charset</i> is set, the character set of the message being replied to is tried first as a target character set (still being a subject of <code>charsetalias</code> filtering, however). Another opportunity is <i>sendcharsets-else-ttycharset</i> to reflect the user&#8217;s locale environment automatically, it will treat <i>ttycharset</i> as an implied member of (an unset) <i>sendcharsets</i> </p>
<p> [Option] When reading messages, their text data is converted into <i>ttycharset</i> as necessary in order to display them on the user&#8217;s terminal. Unprintable characters and invalid byte sequences are detected and replaced by substitution characters. Character set mappings for source character sets can be established with <code>charsetalias</code> which may be handy to work around faulty or incomplete character set catalogues (one could for example add a missing LATIN1 to ISO-8859-1 mapping), or to enforce treatment of one character set as another one ( ``interpret LATIN1 as CP1252&#8217;&#8216; Also see <i>charset-unknown-8bit</i> to deal with another hairy aspect of message interpretation. </p>
<p> In general, if a message saying ``cannot convert from a to b&#8217;&#8216; appears, either some characters are not appropriate for the currently selected (terminal) character set, or the needed conversion is not supported by the system. In the first case, it is necessary to set an appropriate <code>LC_CTYPE</code> locale and/or the variable <i>ttycharset</i> The best results are usually achieved when running in a UTF-8 locale on a UTF-8 capable terminal, in which case the full Unicode spectrum of characters is available. In this setup characters from various countries can be displayed, while it is still possible to use more simple character sets for sending to retain maximum compatibility with older mail clients. </p>
<p> On the other hand the POSIX standard defines a locale-independent 7-bit ``portable character set&#8217;&#8216; that should be used when overall portability is an issue, the even more restricted subset named ``portable filename character set&#8217;&#8216; consists of A-Z, a-z, 0-9, period `.&#8216; , underscore `_&#8216; and hyphen-minus `-&#8216;  </p>
<h3>Message states</h3>
<p> S-nail differentiates in between several message states; the current state will be reflected in the summary of <code>headers</code> if the <i>attrlist</i> of the configured <i>headline</i> allows, and Sx Specifying messages dependent on their state is possible. When operating on the system <i>inbox</i> or in any other Sx primary system mailbox , special actions, like the automatic moving of messages to the Sx secondary mailbox <code>MBOX</code> may be applied when the mailbox is left (also implicitly by program termination, unless the command <code>exit</code> was used) - however, because this may be irritating to users which are used to ``more modern&#8217;&#8216; mail-user-agents, the provided global s-nail.rc template sets the internal <i>hold</i> and <i>keepsave</i> variables in order to suppress this behaviour. </p>
<dl>
<dt><code>`new&#8217; </code></dt>
<dd> <p> Message has neither been viewed nor moved to any other state. Such messages are retained even in the Sx primary system mailbox . </p>
 </dd>
<dt><code>`unread&#8217; </code></dt>
<dd> <p> Message has neither been viewed nor moved to any other state, but the message was present already when the mailbox has been opened last: Such messages are retained even in the Sx primary system mailbox . </p>
 </dd>
<dt><code>`read&#8217; </code></dt>
<dd> <p> The message has been processed by one of the following commands: <code>~f</code> <code>~m</code> <code>~F</code> <code>~M</code> <code>copy</code> <code>mbox</code> <code>next</code> <code>pipe </code> <code>Print</code> <code>print</code> <code>top</code> <code>Type</code> <code>type</code> <code>undelete</code> The commands <code>dp</code> and <code>dt</code> will always try to automatically ``step&#8217;&#8216; and <code>type</code> the ``next&#8217;&#8216; logical message, and may thus mark multiple messages as read, the <code>delete</code> command will do so if the internal variable <i>autoprint</i> is set. </p>
<p> Except when the <code>exit</code> command is used, messages that are in a Sx primary system mailbox and are in `read&#8217; state when the mailbox is left will be saved in the Sx secondary mailbox <code>MBOX</code> unless the internal variable <i>hold</i> it set. </p>
 </dd>
<dt><code>`deleted&#8217; </code></dt>
<dd> <p> The message has been processed by one of the following commands: <code>delete</code> <code>dp</code> <code>dt</code> Only <code>undelete</code> can be used to access such messages. </p>
 </dd>
<dt><code>`preserved&#8217; </code></dt>
<dd> <p> The message has been processed by a <code>preserve</code> command and it will be retained in its current location. </p>
 </dd>
<dt><code>`saved&#8217; </code></dt>
<dd> <p> The message has been processed by one of the following commands: <code>save</code> or <code>write</code> Unless when the <code>exit</code> command is used, messages that are in a Sx primary system mailbox and are in `saved&#8217; state when the mailbox is left will be deleted; they will be saved in the Sx secondary mailbox <code>MBOX</code> when the internal variable <i>keepsave</i> is set. </p>
 </dd></dl>
<p> In addition to these message states, flags which otherwise have no technical meaning in the mail system except allowing special ways of addressing them when Sx Specifying messages can be set on messages. These flags are saved with messages and are thus persistent, and are portable between a set of widely used MUAs. </p>
<dl>
<dt><code>answered</code></dt>
<dd> <p> Mark messages as having been answered. </p>
 </dd>
<dt><code>draft</code></dt>
<dd> <p> Mark messages as being a draft. </p>
 </dd>
<dt><code>flag</code></dt>
<dd> <p> Mark messages which need special attention. </p>
 </dd></dl>
<h3>Specifying messages</h3>
<p> [Only new quoting rules] <code>COMMANDS</code> which take Sx Message list arguments , such as <code>search</code> <code>type</code> <code>copy</code> and <code>delete</code> can perform actions on a number of messages at once. Specifying invalid messages, or using illegal syntax, will cause errors to be reported through the Sx INTERNAL VARIABLES <i>!</i> <i>^ERR</i> and companions, as well as the command exit status <i>?</i> </p>
<p> For example, `delete&#8217; 1 2 deletes the messages 1 and 2, whereas `delete&#8217; 1-5 will delete the messages 1 through 5. In sorted or threaded mode (see the <code>sort</code> command), `delete&#8217; 1-5 will delete the messages that are located between (and including) messages 1 through 5 in the sorted/threaded order, as shown in the <code>headers</code> summary. </p>
<p> Errors can for example be <i>^ERR </i><code>-BADMSG</code> when requesting an invalid message, <i>^ERR </i><code>-NOMSG</code> if no applicable message can be found, <i>^ERR </i><code>-CANCELED</code> for missing informational data (mostly thread-related). <i>^ERR </i><code>-INVAL</code> for invalid syntax as well as <i>^ERR </i><code>-IO</code> for input/output errors can happen. The following special message names exist: </p>
<dl>
<dt><i>.</i></dt>
<dd> <p> The current message, the so-called ``dot&#8217;&#8216; </p>
 </dd>
<dt><i>;</i></dt>
<dd> <p> The message that was previously the current message; needs to be quoted. </p>
 </dd>
<dt><i>,</i></dt>
<dd> <p> The parent message of the current message, that is the message with the Message-ID given in the `In-Reply-To:&#8216; field or the last entry of the `References:&#8216; field of the current message. </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> The previous undeleted message, or the previous deleted message for the <code>undelete</code> command; In <code>sort ed or</code> `thread&#8217; Ns ed mode, the previous such message in the according order. </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> The next undeleted message, or the next deleted message for the <code>undelete</code> command; In <code>sort ed or</code> `thread&#8217; Ns ed mode, the next such message in the according order. </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> The first undeleted message, or the first deleted message for the <code>undelete</code> command; In <code>sort ed or</code> `thread&#8217; Ns ed mode, the first such message in the according order. </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> The last message; In <code>sort ed or</code> `thread&#8217; Ns ed mode, the last such message in the according order. Needs to be quoted. </p>
 </dd>
<dt><i>&amp; </i><i>x</i></dt>
<dd> <p> In `thread&#8217; Ns ed <code>sort</code> mode, selects the message addressed with <i>x</i> where <i>x</i> is any other message specification, and all messages from the thread that begins at it. Otherwise it is identical to <i>x</i> If <i>x</i> is omitted, the thread beginning with the current message is selected. </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> All messages. </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> All messages that were included in the Sx Message list arguments of the previous command; needs to be quoted. (A convenient way to read all new messages is to select them via `from&#8217; :n , as below, and then to read them in order with the default command --- <code>next</code> --- simply by successively typing ``&#8216; ; for this to work <i>showlast</i> must be set.) </p>
 </dd>
<dt><i>x-y</i></dt>
<dd> <p> An inclusive range of message numbers. Selectors that may also be used as endpoints include any of <i>.;-+^$</i> </p>
 </dd>
<dt><i>address</i></dt>
<dd> <p> A case-insensitive ``any substring matches&#8217;&#8216; search against the `From:&#8216; header, which will match addresses (too) even if <i>showname</i> is set (and POSIX says ``any address as shown in a header summary shall be matchable in this form )&#8216;&#8216; However, if the <i>allnet</i> variable is set, only the local part of the address is evaluated for the comparison, not ignoring case, and the setting of <i>showname</i> is completely ignored. For finer control and match boundaries use the `@&#8216; search expression. </p>
 </dd>
<dt><i>/ </i><i>string</i></dt>
<dd> <p> All messages that contain <i>string</i> in the subject field (case ignored according to locale). See also the <i>searchheaders</i> variable. If <i>string</i> is empty, the string from the previous specification of that type is used again. </p>
 </dd>
<dt>[<i>@ </i><i>name-list </i><i>@ </i><i>expr</i> ] </dt>
<dd>  </dd>
<dd> <p> All messages that contain the given case-insensitive search <i>expr </i><code>ession; If </code>the [Option]al regular expression support is available <i>expr</i> will be interpreted as (an extended) one if any of the Sx magic regular expression characters is seen. If the optional <i>@ </i><i>name-list</i> part is missing the search is restricted to the subject field body, but otherwise <i>name-list</i> specifies a comma-separated list of header fields to search, for example </p>
<blockquote><p> <code>&#8216;@to,from,cc [at] Someone i ought to know&#8217;</code> </p>
</blockquote>
<p> In order to search for a string that includes a `@&#8216; (commercial at) character the <i>name-list</i> is effectively non-optional, but may be given as the empty string. Also, specifying an empty search <i>expr </i><code>ession will effectively test for existence of the given header fields.</code> Some special header fields may be abbreviated: `f&#8217; , `t&#8217; , `c&#8217; , `b&#8217; and `s&#8217; will match `From&#8217; , `To , &#8216; `Cc , &#8216; `Bcc&#8217; and `Subject&#8217; , respectively and case-insensitively. [Option]ally, and just like <i>expr</i> <i>name-list</i> will be interpreted as (an extended) regular expression if any of the Sx magic regular expression characters is seen. </p>
<p> The special names `header&#8217; or `&lt;&#8216; can be used to search in (all of) the header(s) of the message, and the special names `body&#8217; or `&gt;&#8216; and `text&#8217; or `=&#8216; will perform full text searches - whereas the former searches only the body, the latter also searches the message header ([v15 behaviour may differ] this mode yet brute force searches over the entire decoded content of messages, including administrativa strings). </p>
<p> This specification performs full text comparison, but even with regular expression support it is almost impossible to write a search expression that safely matches only a specific address domain. To request that the body content of the header is treated as a list of addresses, and to strip those down to the plain email address which the search expression is to be matched against, prefix the effective <i>name-list</i> with a tilde `~&#8216; : </p>
<blockquote><p> <code>&#8216;@~f,c@@a\.safe\.domain\.match$&#8216;</code> </p>
</blockquote>
 </dd>
<dt><i>:c</i></dt>
<dd> <p> All messages of state or with matching condition `c&#8217; , where `c&#8217; is one or multiple of the following colon modifiers: </p>
 </dd>
<dl>
<dt><i>a</i></dt>
<dd> <p> <code>answered</code> messages (cf. the variable <i>markanswered )</i> </p>
 </dd>
<dt><i>d</i></dt>
<dd> <p> `deleted&#8217; messages (for the <code>undelete</code> and <code>from</code> commands only). </p>
 </dd>
<dt><i>f</i></dt>
<dd> <p> <code>flag ged messages.</code> </p>
 </dd>
<dt><i>L</i></dt>
<dd> <p> Messages with receivers that match <code>mlsubscribe d addresses.</code> </p>
 </dd>
<dt><i>l</i></dt>
<dd> <p> Messages with receivers that match <code>mlist ed addresses.</code> </p>
 </dd>
<dt><i>n</i></dt>
<dd> <p> `new&#8217; messages. </p>
 </dd>
<dt><i>o</i></dt>
<dd> <p> Old messages (any not in state `read&#8217; or `new&#8217; ) . </p>
 </dd>
<dt><i>r</i></dt>
<dd> <p> `read&#8217; messages. </p>
 </dd>
<dt><i>S</i></dt>
<dd> <p> [Option] Messages with unsure spam classification (see Sx Handling spam ) . </p>
 </dd>
<dt><i>s</i></dt>
<dd> <p> [Option] Messages classified as spam. </p>
 </dd>
<dt><i>t</i></dt>
<dd> <p> Messages marked as <code>draft</code> </p>
 </dd>
<dt><i>u</i></dt>
<dd> <p> `unread&#8217; messages. </p>
 </dd></dl>
<p> [Option] IMAP-style SEARCH expressions may also be used. These consist of keywords and criterions, and because Sx Message list arguments are split into tokens according to Sx Shell-style argument quoting it is necessary to quote the entire IMAP search expression in order to ensure that it remains a single token. This addressing mode is available with all types of mailbox <code>folder s; S-nail will perform the search locally as necessary.</code> Strings must be enclosed by double quotation marks `&#8216; in their entirety if they contain whitespace or parentheses; within the quotes, only reverse solidus `\&#8216; is recognized as an escape character. All string searches are case-insensitive. When the description indicates that the ``envelope&#8217;&#8216; representation of an address field is used, this means that the search string is checked against both a list constructed as </p>
<blockquote><pre><code>'(&quot;name&quot; &quot;source&quot; &quot;local-part&quot; &quot;domain-part&quot;)'
</code></pre>
</blockquote>
<p> for each address, and the addresses without real names from the respective header field. These search expressions can be nested using parentheses, see below for examples. </p>
<dl>
<dt><i>( criterion</i></dt>
<dd> <p> All messages that satisfy the given <i>criterion</i> </p>
 </dd>
<dt><i>( criterion1 criterion2 ... criterionN</i></dt>
<dd> <p> All messages that satisfy all of the given criteria. </p>
 </dd>
<dt><i>( or criterion1 criterion2</i></dt>
<dd> <p> All messages that satisfy either <i>criterion1</i> or <i>criterion2</i> or both. To connect more than two criteria using `or&#8217; specifications have to be nested using additional parentheses, as with `(or&#8217; a (or b c)) , since `(or&#8217; a b c) really means `((a&#8217; or b) and c) . For a simple `or&#8217; operation of independent criteria on the lowest nesting level, it is possible to achieve similar effects by using three separate criteria, as with `(a)&#8216; (b) (c) . </p>
 </dd>
<dt><i>( not criterion</i></dt>
<dd> <p> All messages that do not satisfy <i>criterion</i> </p>
 </dd>
<dt><i>( bcc &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in the envelope representation of the `Bcc:&#8216; field. </p>
 </dd>
<dt><i>( cc &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in the envelope representation of the `Cc:&#8216; field. </p>
 </dd>
<dt><i>( from &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in the envelope representation of the `From:&#8216; field. </p>
 </dd>
<dt><i>( subject &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in the `Subject:&#8216; field. </p>
 </dd>
<dt><i>( to &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in the envelope representation of the `To:&#8216; field. </p>
 </dd>
<dt><i>( header name &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in the specified `Name:&#8216; field. </p>
 </dd>
<dt><i>( body &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in their body. </p>
 </dd>
<dt><i>( text &quot; </i><i>string </i><i>&quot;</i></dt>
<dd> <p> All messages that contain <i>string</i> in their header or body. </p>
 </dd>
<dt><i>( larger size</i></dt>
<dd> <p> All messages that are larger than <i>size</i> (in bytes). </p>
 </dd>
<dt><i>( smaller size</i></dt>
<dd> <p> All messages that are smaller than <i>size</i> (in bytes). </p>
 </dd>
<dt><i>( before date</i></dt>
<dd> <p> All messages that were received before <i>date</i> which must be in the form `d[d]-mon-yyyy&#8217; , where `d&#8217; denotes the day of the month as one or two digits, `mon&#8217; is the name of the month - one of `Jan&#8217; Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec , and `yyyy&#8217; is the year as four digits, for example `28-Dec-2012&#8217; </p>
 </dd>
<dt><i>( on date</i></dt>
<dd> <p> All messages that were received on the specified date. </p>
 </dd>
<dt><i>( since date</i></dt>
<dd> <p> All messages that were received since the specified date. </p>
 </dd>
<dt><i>( sentbefore date</i></dt>
<dd> <p> All messages that were sent on the specified date. </p>
 </dd>
<dt><i>( senton date</i></dt>
<dd> <p> All messages that were sent on the specified date. </p>
 </dd>
<dt><i>( sentsince date</i></dt>
<dd> <p> All messages that were sent since the specified date. </p>
 </dd>
<dt><i>()</i></dt>
<dd> <p> The same criterion as for the previous search. This specification cannot be used as part of another criterion. If the previous command line contained more than one independent criterion then the last of those criteria is used. </p>
 </dd></dl>
<h3>On terminal control and line editor</h3>
<p> [Option] Terminal control through one of the standard UNIX libraries, Lb libtermcap or Lb libterminfo , may be available. For the <code>TERM inal defined in the environment interactive usage aspects, for example</code> Sx Coloured display , and insight of cursor and function keys for the Mailx-Line-Editor (MLE), will be enhanced or enabled. Library interaction can be disabled on a per-invocation basis via <i>termcap-disable</i> whereas the internal variable <i>termcap</i> is always used as a preferred source of terminal capabilities. (For a usage example see the Sx FAQ entry Sx Not &quot;defunctional&quot;, but the editor key does not work . ) </p>
<p> [Option] The built-in Mailx-Line-Editor (MLE) should work in all environments which comply to the ISO C standard St -isoC-amd1 , and will support wide glyphs if possible (the necessary functionality had been removed from ISO C, but was included in St -xpg4 ) . Usage of a line editor in interactive mode can be prevented by setting <i>line-editor-disable</i> Especially if the [Option]al terminal control support is missing setting entries in <i>termcap</i> will help shall the MLE misbehave, see there for more. The MLE can support a little bit of <code>colour</code> </p>
<p> [Option] If the <code>history</code> feature is available then input from line editor prompts will be saved in a history list that can be searched in and be expanded from. Such saving can be prevented by prefixing input with any amount of whitespace. Aspects of history, like allowed content and maximum size, as well as whether history shall be saved persistently, can be configured with the internal variables <i>history-file</i> <i>history-gabby</i> <i>history-gabby-persist</i> and <i>history-size</i> There also exists the macro hook <i>on-history-addition</i> which can be used to apply finer control on what enters history. </p>
<p> The MLE supports a set of editing and control commands. By default (as) many (as possible) of these will be assigned to a set of single-letter control codes, which should work on any terminal (and can be generated by holding the ``control&#8217;&#8216; key while pressing the key of desire, for example `control-D&#8217; ) . If the [Option]al <code>bind</code> command is available then the MLE commands can also be accessed freely by assigning the command name, which is shown in parenthesis in the list below, to any desired key-sequence, and the MLE will instead and also use <code>bind</code> to establish its built-in key bindings (more of them if the [Option]al terminal control is available), an action which can then be suppressed completely by setting <i>line-editor-no-defaults</i> Sx Shell-style argument quoting notation is used in the following: </p>
<dl>
<dt><code>`\cA&#8217; </code></dt>
<dd> <p> Go to the start of the line ( <code>mle-go-home</code> </p>
 </dd>
<dt><code>`\cB&#8217; </code></dt>
<dd> <p> Move the cursor backward one character ( <code>mle-go-bwd</code> </p>
 </dd>
<dt><code>`\cC&#8217; </code></dt>
<dd> <p> <a href="/docs/linux/man/3-raise/">raise</a>(3) `SIGINT&#8217; ( <code>mle-raise-int</code> </p>
 </dd>
<dt><code>`\cD&#8217; </code></dt>
<dd> <p> Forward delete the character under the cursor; quits S-nail if used on the empty line unless the internal variable <i>ignoreeof</i> is set ( <code>mle-del-fwd</code> </p>
 </dd>
<dt><code>`\cE&#8217; </code></dt>
<dd> <p> Go to the end of the line ( <code>mle-go-end</code> </p>
 </dd>
<dt><code>`\cF&#8217; </code></dt>
<dd> <p> Move the cursor forward one character ( <code>mle-go-fwd</code> </p>
 </dd>
<dt><code>`\cG&#8217; </code></dt>
<dd> <p> Cancel current operation, full reset. If there is an active history search or tabulator expansion then this command will first reset that, reverting to the former line content; thus a second reset is needed for a full reset in this case ( <code>mle-reset</code> </p>
 </dd>
<dt><code>`\cH&#8217; </code></dt>
<dd> <p> Backspace: backward delete one character ( <code>mle-del-bwd</code> </p>
 </dd>
<dt><code>`\cI&#8217; </code></dt>
<dd> <p> [Only new quoting rules] Horizontal tabulator: try to expand the word before the cursor, supporting the usual Sx Filename transformations ( <code>mle-complete</code> this is affected by <code>mle-quote-rndtrip</code> and <i>line-editor-cpl-word-breaks )</i> </p>
 </dd>
<dt><code>`\cJ&#8217; </code></dt>
<dd> <p> Newline: commit the current line ( <code>mle-commit</code> </p>
 </dd>
<dt><code>`\cK&#8217; </code></dt>
<dd> <p> Cut all characters from the cursor to the end of the line ( <code>mle-snarf-end</code> </p>
 </dd>
<dt><code>`\cL&#8217; </code></dt>
<dd> <p> Repaint the line ( <code>mle-repaint</code> </p>
 </dd>
<dt><code>`\cN&#8217; </code></dt>
<dd> <p> [Option] Go to the next history entry ( <code>mle-hist-fwd</code> </p>
 </dd>
<dt><code>`\cO&#8217; </code></dt>
<dd> <p> ([Option]ally context-dependent) Invokes the command <code>dt</code> </p>
 </dd>
<dt><code>`\cP&#8217; </code></dt>
<dd> <p> [Option] Go to the previous history entry ( <code>mle-hist-bwd</code> </p>
 </dd>
<dt><code>`\cQ&#8217; </code></dt>
<dd> <p> Toggle roundtrip mode shell quotes, where produced, on and off ( <code>mle-quote-rndtrip</code> This setting is temporary, and will be forgotten once the command line is committed; also see <code>shcodec</code> </p>
 </dd>
<dt><code>`\cR&#8217; </code></dt>
<dd> <p> [Option] Complete the current line from (the remaining) older history entries ( <code>mle-hist-srch-bwd</code> </p>
 </dd>
<dt><code>`\cS&#8217; </code></dt>
<dd> <p> [Option] Complete the current line from (the remaining) newer history entries ( <code>mle-hist-srch-fwd</code> </p>
 </dd>
<dt><code>`\cT&#8217; </code></dt>
<dd> <p> Paste the snarf buffer ( <code>mle-paste</code> </p>
 </dd>
<dt><code>`\cU&#8217; </code></dt>
<dd> <p> The same as `\cA&#8217; followed by `\cK&#8217; ( <code>mle-snarf-line</code> </p>
 </dd>
<dt><code>`\cV&#8217; </code></dt>
<dd> <p> Prompts for a Unicode character (hexadecimal number without prefix, see <code>vexpr</code> to be inserted ( <code>mle-prompt-char</code> Note this command needs to be assigned to a single-letter control code in order to become recognized and executed during input of a key-sequence (only three single-letter control codes can be used for that shortcut purpose); this control code is then special-treated and thus cannot be part of any other sequence (because it will trigger the <code>mle-prompt-char</code> function immediately). </p>
 </dd>
<dt><code>`\cW&#8217; </code></dt>
<dd> <p> Cut the characters from the one preceding the cursor to the preceding word boundary ( <code>mle-snarf-word-bwd</code> </p>
 </dd>
<dt><code>`\cX&#8217; </code></dt>
<dd> <p> Move the cursor forward one word boundary ( <code>mle-go-word-fwd</code> </p>
 </dd>
<dt><code>`\cY&#8217; </code></dt>
<dd> <p> Move the cursor backward one word boundary ( <code>mle-go-word-bwd</code> </p>
 </dd>
<dt><code>`\cZ&#8217; </code></dt>
<dd> <p> <a href="/docs/linux/man/3-raise/">raise</a>(3) `SIGTSTP&#8217; ( <code>mle-raise-tstp</code> </p>
 </dd>
<dt><code>`\c[&#8216; </code></dt>
<dd> <p> Escape: reset a possibly used multibyte character input state machine and [Option]ally a lingering, incomplete key binding ( <code>mle-cancel</code> This command needs to be assigned to a single-letter control code in order to become recognized and executed during input of a key-sequence (only three single-letter control codes can be used for that shortcut purpose). This control code may also be part of a multi-byte sequence, but if a sequence is active and the very control code is currently also an expected input, then the active sequence takes precedence and will consume the control code. </p>
 </dd>
<dt><code>`\c\&#8216; </code></dt>
<dd> <p> ([Option]ally context-dependent) Invokes the command `<code>z</code> &#8216; Ns + . </p>
 </dd>
<dt><code>`\c]&#8216; </code></dt>
<dd> <p> ([Option]ally context-dependent) Invokes the command `<code>z</code> &#8216; Ns $ . </p>
 </dd>
<dt><code>`\c^&#8216; </code></dt>
<dd> <p> ([Option]ally context-dependent) Invokes the command `<code>z</code> &#8216; Ns 0 . </p>
 </dd>
<dt><code>`\c_&#8216; </code></dt>
<dd> <p> Cut the characters from the one after the cursor to the succeeding word boundary ( <code>mle-snarf-word-fwd</code> </p>
 </dd>
<dt><code>`\c?&#8216; </code></dt>
<dd> <p> Backspace: <code>mle-del-bwd</code> </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> <code>mle-bell</code> ring the audible bell. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> [Option] <code>mle-clear-screen</code> move the cursor home and clear the screen. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> <code>mle-fullreset</code> different to <code>mle-reset</code> this will immediately reset a possibly active search etc. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> <code>mle-go-screen-bwd</code> move the cursor backward one screen width. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> <code>mle-go-screen-fwd</code> move the cursor forward one screen width. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> <code>mle-raise-quit:</code> <a href="/docs/linux/man/3-raise/">raise</a>(3) `SIGQUIT&#8217; </p>
 </dd></dl>
<h3>Coloured display</h3>
<p> [Option] Colours and font attributes through ANSI a.k.a. ISO 6429 SGR (select graphic rendition) escape sequences are optionally supported. Usage of colours and font attributes solely depends upon the capability of the detected terminal type ( <code>TERM</code> and as fine-tuned through <i>termcap</i> Colours and font attributes can be managed with the multiplexer command <code>colour</code> and <code>uncolour</code> removes the given mappings. Setting <i>colour-disable</i> suppresses usage of colour and font attribute sequences, while leaving established mappings unchanged. </p>
<p> Whether actually applicable colour and font attribute sequences should also be generated when output is going to be paged through the external <code>PAGER</code> (also see <i>crt </i><code>) depends upon the setting of</code> <i>colour-pager</i> because pagers usually need to be configured in order to support ISO escape sequences. Knowledge of some widely used pagers is however built-in, and in a clean environment it is often enough to simply set <i>colour-pager</i> please refer to that variable for more on this topic. </p>
<p> It might make sense to conditionalize colour setup on interactive mode via <code>if</code> ( `terminal&#8217; indeed means ``interactive )&#8216;&#8216; </p>
<blockquote><pre><code>if terminal &amp;&amp; &quot;$features&quot; =% ,+colour,
  colour iso view-msginfo ft=bold,fg=green
  colour iso view-header ft=bold,fg=red (from|subject) # regex
  colour iso view-header fg=red
  uncolour iso view-header from,subject
  colour iso view-header ft=bold,fg=magenta,bg=cyan
  colour 256 view-header ft=bold,fg=208,bg=230 &quot;subject,from&quot;
  colour mono view-header ft=bold
  colour mono view-header ft=bold,ft=reverse subject,from
endif
</code></pre>
</blockquote>
<h3>Handling spam</h3>
<p> [Option] S-nail can make use of several spam interfaces for the purpose of identification of, and, in general, dealing with spam messages. A precondition of most commands in order to function is that the <i>spam-interface</i> variable is set to one of the supported interfaces. Sx Specifying messages that have been identified as spam is possible via their (volatile) `is-spam&#8217; state by using the `<i>:s</i> &#8216; and `<i>:S</i> &#8216; specifications, and their <i>attrlist</i> entries will be used when displaying the <i>headline</i> in the summary of <code>headers</code> </p>
<ul>
<li> <p> <code>spamrate</code> rates the given messages and sets their `is-spam&#8217; flag accordingly. If the spam interface offers spam scores these can be shown in <i>headline</i> by using the format `%$&#8216;  </li>
<li>  <code>spamham</code> <code>spamspam</code> and <code>spamforget</code> will interact with the Bayesian filter of the chosen interface and learn the given messages as ``ham&#8217;&#8216; or ``spam&#8217;&#8216; respectively; the last command can be used to cause ``unlearning&#8217;&#8216; of messages; it adheres to their current `is-spam&#8217; state and thus reverts previous teachings.  </li>
<li>  <code>spamclear</code> and <code>spamset</code> will simply set and clear, respectively, the mentioned volatile `is-spam&#8217; message flag, without any interface interaction.  </li>
</ul>
 </p>
<p> The <a href="/docs/linux/man/1-spamassassin/">spamassassin</a>(1) based <i>spam-interface</i> `spamc&#8217; requires a running instance of the <a href="/docs/linux/man/1-spamd/">spamd</a>(1) server in order to function, started with the option -<code>-allow-tell</code> shall Bayesian filter learning be possible. </p>
<blockquote><pre><code>$ spamd -i localhost:2142 -i /tmp/.spamsock -d [-L] [-l]
$ spamd --listen=localhost:2142 --listen=/tmp/.spamsock \
    --daemonize [--local] [--allow-tell]
</code></pre>
</blockquote>
<p> Thereafter S-nail can make use of these interfaces: </p>
<blockquote><pre><code>$ s-nail -Sspam-interface=spamc -Sspam-maxsize=500000 \
    -Sspamc-command=/usr/local/bin/spamc \
    -Sspamc-arguments=&quot;-U /tmp/.spamsock&quot; -Sspamc-user=
or
$ s-nail -Sspam-interface=spamc -Sspam-maxsize=500000 \
    -Sspamc-command=/usr/local/bin/spamc \
    -Sspamc-arguments=&quot;-d localhost -p 2142&quot; -Sspamc-user=
</code></pre>
</blockquote>
<p> Using the generic filter approach allows usage of programs like <a href="/docs/linux/man/1-bogofilter/">bogofilter</a>(1). Here is an example, requiring it to be accessible via <code>PATH</code> </p>
<blockquote><pre><code>$ s-nail -Sspam-interface=filter -Sspam-maxsize=500000 \
    -Sspamfilter-ham=&quot;bogofilter -n&quot; \
    -Sspamfilter-noham=&quot;bogofilter -N&quot; \
    -Sspamfilter-nospam=&quot;bogofilter -S&quot; \
    -Sspamfilter-rate=&quot;bogofilter -TTu 2&gt;/dev/null&quot; \
    -Sspamfilter-spam=&quot;bogofilter -s&quot; \
    -Sspamfilter-rate-scanscore=&quot;1;^(.+)$&quot;
</code></pre>
</blockquote>
<p> Because messages must exist on local storage in order to be scored (or used for Bayesian filter training), it is possibly a good idea to perform the local spam check last. Spam can be checked automatically when opening specific folders by setting a specialized form of the internal variable <i>folder-hook</i> </p>
<blockquote><pre><code>define spamdelhook {
  # Server side DCC
  spamset (header x-dcc-brand-metrics &quot;bulk&quot;)
  # Server-sidespamassassin(1)
  spamset (header x-spam-flag &quot;YES&quot;)
  del :s # TODO we HAVE to be able to do `spamrate :u ! :sS'
  move :S +maybe-spam
  spamrate :u
  del :s
  move :S +maybe-spam
}
set folder-hook-SOMEFOLDER=spamdelhook
</code></pre>
</blockquote>
<p> See also the documentation for the variables <i>spam-interface , spam-maxsize</i> <i>spamc-command , spamc-arguments , spamc-user</i> <i>spamfilter-ham , spamfilter-noham , spamfilter-nospam ,</i> <br />
&nbsp;<wbr>&nbsp;spamfilter-rate and <i>spamfilter-rate-scanscore</i>  </p>
<h2>COMMANDS</h2>
<p> S-nail reads input in lines. An unquoted reverse solidus `\&#8216; at the end of a command line ``escapes&#8217;&#8216; the newline character: it is discarded and the next line of input is used as a follow-up line, with all leading whitespace removed; once an entire line is completed, the whitespace characters <code>space , tabulator , newline</code> as well as those defined by the variable <i>ifs</i> are removed from the beginning and end. Placing any whitespace characters at the beginning of a line will prevent a possible addition of the command line to the [Option]al <code>history</code> </p>
<p> The beginning of such input lines is then scanned for the name of a known command: command names may be abbreviated, in which case the first command that matches the given prefix will be used. Sx Command modifiers may prefix a command in order to modify its behaviour. A name may also be a <code>commandalias</code> which will become expanded until no more expansion is possible. Once the command that shall be executed is known, the remains of the input line will be interpreted according to command-specific rules, documented in the following. </p>
<p> This behaviour is different to the <a href="/docs/linux/man/1-sh/">sh</a>(1) ell, which is a programming language with syntactic elements of clearly defined semantics, and therefore capable to sequentially expand and evaluate individual elements of a line. `?&#8216; set one=value two=$one for example will never possibly assign value to one, because the variable assignment is performed no sooner but by the command ( <code>set</code> long after the expansion happened. </p>
<p> A list of all commands in lookup order is dumped by the command <code>list</code> [Option]ally the command <code>help</code> (or <code>? )</code> when given an argument, will show a documentation string for the command matching the expanded argument, as in `?t&#8217; , which should be a shorthand of `?type&#8217; ; with these documentation strings both commands support a more <i>verbose</i> listing mode which includes the argument type of the command and other information which applies; a handy suggestion might thus be: </p>
<blockquote><pre><code>? define __xv {
  # Before v15: need to enablesh(1)ell-style on _entire_ line!
  localopts yes;wysh set verbose;ignerr eval &quot;${@}&quot;;return ${?}
}
? commandalias xv '\call __xv'
? xv help set
</code></pre>
</blockquote>
<h3>Command modifiers</h3>
<p> Commands may be prefixed by none to multiple command modifiers. Some command modifiers can be used with a restricted set of commands only, the <i>verbose</i> version of <code>list</code> will ([Option]ally) show which modifiers apply. </p>
<ul>
<li> <p> The modifier reverse solidus <code>\</code> to be placed first, prevents <code>commandalias</code> expansions on the remains of the line, for example `\echo&#8217; will always evaluate the command <code>echo</code> even if an (command)alias of the same name exists. <code>commandalias</code> content may itself contain further command modifiers, including an initial reverse solidus to prevent further expansions.  </li>
<li>  The modifier <code>ignerr</code> indicates that any error generated by the following command should be ignored by the state machine and not cause a program exit with enabled <i>errexit</i> or for the standardized exit cases in <i>posix</i> mode. <i>?</i> one of the Sx INTERNAL VARIABLES , will be set to the real exit status of the command regardless.  </li>
<li>  <code>local</code> will alter the called command to apply changes only temporarily, local to block-scope, and can thus only be used inside of a <code>define d macro or an</code> <code>account</code> definition. Specifying it implies the modifier <code>wysh</code> Local variables will not be inherited by macros deeper in the <code>call</code> chain, and all local settings will be garbage collected once the local scope is left. To record and unroll changes in the global scope use the command <code>localopts</code>  </li>
<li>  <code>scope</code> does yet not implement any functionality.  </li>
<li>  <code>u</code> does yet not implement any functionality.  </li>
<li>  Some commands support the <code>vput</code> modifier: if used, they expect the name of a variable, which can itself be a variable, i.e., shell expansion is applied, as their first argument, and will place their computation result in it instead of the default location (it is usually written to standard output). </p>
<p> The given name will be tested for being a valid <a href="/docs/linux/man/1-sh/">sh</a>(1) variable name, and may therefore only consist of upper- and lowercase characters, digits, and the underscore; the hyphen-minus may be used as a non-portable extension; digits may not be used as first, hyphen-minus may not be used as last characters. In addition the name may either not be one of the known Sx INTERNAL VARIABLES , or must otherwise refer to a writable (non-boolean) value variable. The actual put operation may fail nonetheless, for example if the variable expects a number argument only a number will be accepted. Any error during these operations causes the command as such to fail, and the error number <i>!</i> will be set to <i>^ERR </i><code>-NOTSUP</code> the exit status <i>?</i> should be set to `-1&#8217; , but some commands deviate from the latter, which is documented.  </li>
<li>  Last, but not least, the modifier <code>wysh</code> can be used for some old and established commands to choose the new Sx Shell-style argument quoting rules over the traditional Sx Old-style argument quoting . This modifier is implied if <i>v15-compat</i> is set to a non-empty value.  </li>
</ul>
 </p>
<h3>Old-style argument quoting</h3>
<p> [v15 behaviour may differ] This section documents the traditional and POSIX standardized style of quoting non-message list arguments to commands which expect this type of arguments: whereas still used by the majority of such commands, the new Sx Shell-style argument quoting may be available even for those via <code>wysh</code> one of the Sx Command modifiers . Nonetheless care must be taken, because only new commands have been designed with all the capabilities of the new quoting rules in mind, which can, for example generate control characters. </p>
<ul>
<li> <p> An argument can be enclosed between paired double-quotes `argument&#8217; or single-quotes `&#8216;argument&#8217;&#8216; ; any whitespace, shell word expansion, or reverse solidus characters (except as described next) within the quotes are treated literally as part of the argument. A double-quote will be treated literally within single-quotes and vice versa. Inside such a quoted string the actually used quote character can be used nonetheless by escaping it with a reverse solidus `\&#8216; , as in `y\ou&#8217;  </li>
<li>  An argument that is not enclosed in quotes, as above, can usually still contain space characters if those spaces are reverse solidus escaped, as in `you\&#8216; are .  </li>
<li>  A reverse solidus outside of the enclosing quotes is discarded and the following character is treated literally as part of the argument.  </li>
</ul>
 </p>
<h3>Shell-style argument quoting</h3>
<p> <a href="/docs/linux/man/1-sh/">sh</a>(1) ell-style, and therefore POSIX standardized, argument parsing and quoting rules are used by most commands. [v15 behaviour may differ] Most new commands only support these new rules and are flagged [Only new quoting rules], some elder ones can use them with the command modifier <code>wysh</code> in the future only this type of argument quoting will remain. </p>
<p> A command line is parsed from left to right and an input token is completed whenever an unquoted, otherwise ignored, metacharacter is seen. Metacharacters are vertical bar <code>|</code> ampersand <code>&amp;</code> semicolon <code>;</code> as well as all characters from the variable <i>ifs</i> and / or <code>space , tabulator , newline</code> The additional metacharacters left and right parenthesis <code>( , )</code> and less-than and greater-than signs <code>&lt; ,</code> that the <a href="/docs/linux/man/1-sh/">sh</a>(1) supports are not used, and are treated as ordinary characters: for one these characters are a vivid part of email addresses, and it seems highly unlikely that their function will become meaningful to S-nail. </p>
<blockquote><p> <code>Compatibility note:</code> [v15 behaviour may differ] Please note that even many new-style commands do not yet honour <i>ifs</i> to parse their arguments: whereas the <a href="/docs/linux/man/1-sh/">sh</a>(1) ell is a language with syntactic elements of clearly defined semantics, S-nail parses entire input lines and decides on a per-command base what to do with the rest of the line. This also means that whenever an unknown command is seen all that S-nail can do is cancellation of the processing of the remains of the line. </p>
<p> It also often depends on an actual subcommand of a multiplexer command how the rest of the line should be treated, and until v15 we are not capable to perform this deep inspection of arguments. Nonetheless, at least the following commands which work with positional parameters fully support <i>ifs</i> for an almost shell-compatible field splitting: <code>call , call_if , read , vpospar , xcall</code> </p>
</blockquote>
<p> Any unquoted number sign `#&#8216; at the beginning of a new token starts a comment that extends to the end of the line, and therefore ends argument processing. An unquoted dollar sign `$&#8216; will cause variable expansion of the given name, which must be a valid <a href="/docs/linux/man/1-sh/">sh</a>(1) ell-style variable name (see <code>vput )</code> Sx INTERNAL VARIABLES as well as Sx ENVIRONMENT (shell) variables can be accessed through this mechanism, brace enclosing the name is supported (i.e., to subdivide a token). </p>
<p> Whereas the metacharacters <code>space , tabulator , newline</code> only complete an input token, vertical bar <code>|</code> ampersand <code>&amp;</code> and semicolon <code>;</code> also act as control operators and perform control functions. For now supported is semicolon <code>;</code> which terminates a single command, therefore sequencing the command line and making the remainder of the line a subject to reevaluation. With sequencing, multiple command argument types and quoting rules may therefore apply to a single line, which can become problematic before v15: e.g., the first of the following will cause surprising results. </p>
<blockquote><p> <code>? echo one; set verbose; echo verbose=$verbose.</code> </p>
</blockquote>
<blockquote><p> <code>? echo one; wysh set verbose; echo verbose=$verbose.</code> </p>
</blockquote>
<p> Quoting is a mechanism that will remove the special meaning of metacharacters and reserved words, and will prevent expansion. There are four quoting mechanisms: the escape character, single-quotes, double-quotes and dollar-single-quotes: </p>
<ul>
<li> <p> The literal value of any character can be preserved by preceding it with the escape character reverse solidus `\&#8216;  </li>
<li>  Arguments which are enclosed in `&#8216;single-quotes&#8217;&#8216; retain their literal value. A single-quote cannot occur within single-quotes.  </li>
<li>  The literal value of all characters enclosed in `&quot;double-quotes&quot;&#8216; is retained, with the exception of dollar sign `$&#8216; , which will cause variable expansion, as above, backquote (grave accent) ``&#8216; , (which not yet means anything special), reverse solidus `\&#8216; , which will escape any of the characters dollar sign `$&#8216; (to prevent variable expansion), backquote (grave accent) ``&#8216; , double-quote `&quot;&#8216; (to prevent ending the quote) and reverse solidus `\&#8216; (to prevent escaping, i.e., to embed a reverse solidus character as-is), but has no special meaning otherwise.  </li>
<li>  Arguments enclosed in `$&#8216;dollar-single-quotes&#8217;&#8216; extend normal single quotes in that reverse solidus escape sequences are expanded as follows: </p>
<dl>
<dt><code>`\a&#8217; </code></dt>
<dd> <p> bell control character (ASCII and ISO-10646 BEL). </p>
 </dd>
<dt><code>`\b&#8217; </code></dt>
<dd> <p> backspace control character (ASCII and ISO-10646 BS). </p>
 </dd>
<dt><code>`\E&#8217; </code></dt>
<dd> <p> escape control character (ASCII and ISO-10646 ESC). </p>
 </dd>
<dt><code>`\e&#8217; </code></dt>
<dd> <p> the same. </p>
 </dd>
<dt><code>`\f&#8217; </code></dt>
<dd> <p> form feed control character (ASCII and ISO-10646 FF). </p>
 </dd>
<dt><code>`\n&#8217; </code></dt>
<dd> <p> line feed control character (ASCII and ISO-10646 LF). </p>
 </dd>
<dt><code>`\r&#8217; </code></dt>
<dd> <p> carriage return control character (ASCII and ISO-10646 CR). </p>
 </dd>
<dt><code>`\t&#8217; </code></dt>
<dd> <p> horizontal tabulator control character (ASCII and ISO-10646 HT). </p>
 </dd>
<dt><code>`\v&#8217; </code></dt>
<dd> <p> vertical tabulator control character (ASCII and ISO-10646 VT). </p>
 </dd>
<dt><code>`\\&#8216; </code></dt>
<dd> <p> emits a reverse solidus character. </p>
 </dd>
<dt><code>`\&#8216;&#8216; </code></dt>
<dd> <p> single quote. </p>
 </dd>
<dt><code>`\&#8216; </code></dt>
<dd> <p> double quote (escaping is optional). </p>
 </dd>
<dt><code>`\NNN&#8217; </code></dt>
<dd> <p> eight-bit byte with the octal value `NNN&#8217; (one to three octal digits), optionally prefixed by an additional `0&#8217; A 0 byte will suppress further output for the quoted argument. </p>
 </dd>
<dt><code>`\xHH&#8217; </code></dt>
<dd> <p> eight-bit byte with the hexadecimal value `HH&#8217; (one or two hexadecimal characters, no prefix, see <code>vexpr )</code> A 0 byte will suppress further output for the quoted argument. </p>
 </dd>
<dt><code>`\UHHHHHHHH&#8217; </code></dt>
<dd> <p> the Unicode / ISO-10646 character with the hexadecimal codepoint value `HHHHHHHH&#8217; (one to eight hexadecimal characters) --- note that Unicode defines the maximum codepoint ever to be supported as `0x10FFFF&#8217; (in planes of `0xFFFF&#8217; characters each). This escape is only supported in locales that support Unicode (see Sx Character sets ) , in other cases the sequence will remain unexpanded unless the given code point is ASCII compatible or (if the [Option]al character set conversion is available) can be represented in the current locale. The character NUL will suppress further output for the quoted argument. </p>
 </dd>
<dt><code>`\uHHHH&#8217; </code></dt>
<dd> <p> Identical to `\UHHHHHHHH&#8217; except it takes only one to four hexadecimal characters. </p>
 </dd>
<dt><code>`\cX&#8217; </code></dt>
<dd> <p> Emits the non-printable (ASCII and compatible) C0 control codes 0 (NUL) to 31 (US), and 127 (DEL). Printable representations of ASCII control codes can be created by mapping them to a different, visible part of the ASCII character set. Adding the number 64 achieves this for the codes 0 to 31, here 7 (BEL): `7&#8217; + 64 = 71 = G . The real operation is a bitwise logical XOR with 64 (bit 7 set, see <code>vexpr )</code> thus also covering code 127 (DEL), which is mapped to 63 (question mark): `?&nbsp;vexpr&nbsp;^&nbsp;127 64&#8217; </p>
<p> Whereas historically circumflex notation has often been used for visualization purposes of control codes, as in `^G&#8217; , the reverse solidus notation has been standardized: `\cG&#8217; Some control codes also have standardized (ISO-10646, ISO C) aliases, as shown above ( `\a&#8217; `\n&#8217; , `\t&#8217; etc) : whenever such an alias exists it will be used for display purposes. The control code NUL ( `\c@&#8216; a non-standard extension) will suppress further output for the remains of the token (which may extend beyond the current quote), or, depending on the context, the remains of all arguments for the current command. </p>
 </dd>
<dt><code>`\$NAME&#8217; </code></dt>
<dd> <p> Non-standard extension: expand the given variable name, as above. Brace enclosing the name is supported. </p>
 </dd>
<dt><code>`\`{command}&#8216; </code></dt>
<dd> <p> Not yet supported, just to raise awareness: Non-standard extension. </p>
 </dd>
 </li>
</dl>
<p> Caveats: </p>
<blockquote><pre><code>? echo 'Quotes '${HOME}' and 'tokens&quot; differ!&quot;# no comment
? echo Quotes ${HOME} and tokens differ! # comment
? echo Don&quot;'&quot;t you worry$'\x21' The sun shines on us. $'\u263A'
</code></pre>
</blockquote>
<h3>Message list arguments</h3>
<p> Many commands operate on message list specifications, as documented in Sx Specifying messages . The argument input is first split into individual tokens via Sx Shell-style argument quoting , which are then interpreted as the mentioned specifications. If no explicit message list has been specified, many commands will search for and use the next message forward that satisfies the commands&#8217; requirements, and if there are no messages forward of the current message, the search proceeds backwards; if there are no good messages at all to be found, an error message is shown and the command is aborted. The <i>verbose</i> output of the command <code>list</code> will indicate whether a command searches for a default message, or not.  </p>
<h3>Raw data arguments for codec commands</h3>
<p> A special set of commands, which all have the string ``codec&#8217;&#8216; in their name, like <code>addrcodec</code> <code>shcodec</code> <code>urlcodec</code> take raw string data as input, which means that the content of the command input line is passed completely unexpanded and otherwise unchanged: like this the effect of the actual codec is visible without any noise of possible shell quoting rules etc., i.e., the user can input one-to-one the desired or questionable data. To gain a level of expansion, the entire command line can be <code>eval uated first, for example</code> </p>
<blockquote><pre><code>? vput shcodec res encode /usr/Sch&ouml;nes Wetter/heute.txt
? echo $res
$'/usr/Sch\u00F6nes Wetter/heute.txt'
? shcodec d $res
$'/usr/Sch\u00F6nes Wetter/heute.txt'
? eval shcodec d $res
/usr/Sch&ouml;nes Wetter/heute.txt
</code></pre>
</blockquote>
<h3>Filename transformations</h3>
<p> Filenames, where expected, and unless documented otherwise, are subsequently subject to the following filename transformations, in sequence: </p>
<ul>
<li> <p> If the given name is a registered <code>shortcut</code> it will be replaced with the expanded shortcut. This step is mostly taken for <code>folder s only.</code>  </li>
<li>  The filename is matched against the following patterns or strings. But for plus <i>+file</i> <i>folder</i> expansion this step is mostly taken for <code>folder s only.</code> </p>
<dl>
<dt><i>file ...</i></dt>
<dd> <p> (Number sign) is expanded to the previous file. </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> (Percent sign) is replaced by the invoking user&#8217;s primary system mailbox, which either is the (itself expandable) <i>inbox</i> if that is set, the standardized absolute pathname indicated by <code>MAIL</code> if that is set, or a built-in compile-time default otherwise. When opening a <code>folder</code> the used name is actively checked for being a primary mailbox, first against <i>inbox</i> then against <code>MAIL</code> </p>
 </dd>
<dt><i>%user</i></dt>
<dd> <p> Expands to the primary system mailbox of <i>user</i> (and never the value of <i>inbox</i> regardless of its actual setting). </p>
 </dd>
<dt><i>file ...</i></dt>
<dd> <p> (Ampersand) is replaced with the invoking user&#8217;s secondary mailbox, the <code>MBOX</code> </p>
 </dd>
<dt><i>+file</i></dt>
<dd> <p> Refers to a <i>file</i> in the <i>folder</i> directory (if that variable is set). </p>
 </dd>
<dt><i>%:filespec</i></dt>
<dd> <p> Expands to the same value as <i>filespec</i> but has special meaning when used with, for example, the command <code>folder</code> the file will be treated as a primary system mailbox by, among others, the <code>mbox</code> and <code>save</code> commands, meaning that messages that have been read in the current session will be moved to the <code>MBOX</code> mailbox instead of simply being flagged as read. </p>
 </dd>
 </li>
</dl>
<li> <p> Meta expansions may be applied to the resulting filename, as allowed by the operation and applicable to the resulting access protocol (also see Sx On URL syntax and credential lookup ) . For the file-protocol, a leading tilde `~&#8216; character will be replaced by the expansion of <code>HOME</code> except when followed by a valid user name, in which case the home directory of the given user is used instead. </p>
<p> A shell expansion as if specified in double-quotes (see Sx Shell-style argument quoting ) may be applied, so that any occurrence of `$VARIABLE&#8217; (or `${VARIABLE}&#8216; ) will be replaced by the expansion of the variable, if possible; Sx INTERNAL VARIABLES as well as Sx ENVIRONMENT (shell) variables can be accessed through this mechanism. </p>
<p> Shell pathname wildcard pattern expansions ( <a href="/docs/linux/man/7-glob/">glob</a>(7) may be applied as documented. If the fully expanded filename results in multiple pathnames and the command is expecting only one file, an error results. </p>
<p> In interactive context, in order to allow simple value acceptance (via ``ENTER )&#8216;&#8216; arguments will usually be displayed in a properly quoted form, so a file `diet\&#8216; is \curd.txt may be displayed as `&#8216;diet\&#8216; is \curd.txt&#8217; .  </li>
</ul>
 </p>
<h3>Commands</h3>
<p> The following commands are available: </p>
<dl>
<dt><code>!</code></dt>
<dd> <p> Executes the <code>SHELL</code> command which follows, replacing unescaped exclamation marks with the previously executed command if the internal variable <i>bang</i> is set. This command supports <code>vput</code> as documented in Sx Command modifiers , and manages the error number <i>!</i> A 0 or positive exit status <i>?</i> reflects the exit status of the command, negative ones that an error happened before the command was executed, or that the program did not exit cleanly, but maybe due to a signal: the error number is <i>^ERR </i><code>-CHILD</code> then. </p>
<p> In conjunction with the <code>vput</code> modifier the following special cases exist: a negative exit status occurs if the collected data could not be stored in the given variable, which is a <i>^ERR </i><code>-NOTSUP</code> error that should otherwise not occur. <i>^ERR </i><code>-CANCELED</code> indicates that no temporary file could be created to collect the command output at first glance. In case of catchable out-of-memory situations <i>^ERR </i><code>-NOMEM</code> will occur and S-nail will try to store the empty string, just like with all other detected error conditions. </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> The comment-command causes the entire line to be ignored. <code>Note:</code> this really is a normal command which&#8217; purpose is to discard its arguments, not a ``comment-start&#8217;&#8216; indicating special character, which means that for example trailing comments on a line are not possible (except for commands which use Sx Shell-style argument quoting ) . </p>
 </dd>
<dt><code>+</code></dt>
<dd> <p> Goes to the next message in sequence and types it (like ``ENTER )&#8216;&#8216; </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Display the preceding message, or the n&#8217;th previous message if given a numeric argument n. </p>
 </dd>
<dt><code>=</code></dt>
<dd> <p> Shows the message number of the current message (the ``dot&#8217;&#8216; when used without arguments, that of the given list otherwise. Output numbers will be separated from each other with the first character of <i>ifs</i> and followed by the first character of <i>if-ws</i> if that is not empty and not identical to the first. If that results in no separation at all a <code>space</code> character is used. This command supports <code>vput</code> (see Sx Command modifiers ) , and manages the error number <i>!</i> </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> [Option] Show a brief summary of commands. [Option] Given an argument a synopsis for the command in question is shown instead; commands can be abbreviated in general and this command can be used to see the full expansion of an abbreviation including the synopsis, try, for example `?h&#8217; , `?hel&#8217; and `?help&#8217; and see how the output changes. To avoid that aliases are resolved the modifier <code>\</code> can be prepended to the argument, but note it must be quoted. This mode also supports a more <i>verbose</i> output, which will provide the information documented for <code>list</code> </p>
 </dd>
<dt><code>|</code></dt>
<dd> <p> A synonym for the <code>pipe</code> command. </p>
 </dd>
<dt><code>account , unaccount</code></dt>
<dd> <p> (ac, una) Creates, selects or lists (an) account(s). Accounts are special incarnations of <code>define d</code> macros and group commands and variable settings which together usually arrange the environment for the purpose of creating an email account. Different to normal macros settings which are covered by <code>localopts</code> - here by default enabled! - will not be reverted before the <code>account</code> is changed again. The special account `null&#8217; (case-insensitive) always exists, and all but it can be deleted by the latter command, and in one operation with the special name `*&#8216; Also for all but it a possibly set <i>on-account-cleanup</i> hook is called once they are left, also for program exit. </p>
<p> Without arguments a listing of all defined accounts is shown. With one argument the given account is activated: the system <i>inbox</i> of that account will be activated (as via <code>folder )</code> a possibly installed <i>folder-hook</i> will be run, and the internal variable <i>account</i> will be updated. The two argument form behaves identical to defining a macro as via <code>define</code> Important settings for accounts include <i>folder , from , hostname , inbox , mta , password</i> and <i>user</i> ( Sx On URL syntax and credential lookup ) as well as things like <i>tls-config-pairs</i> ( Sx Encrypted network communication ) and protocol specifics like <i>imap-auth , pop3-auth , smtp-auth</i> </p>
<blockquote><pre><code>account myisp {
  set folder=~/mail inbox=+syste.mbox record=+sent.mbox
  set from='(My Name) myname [at] myisp.example'
  set mta=smtp://mylogin@smtp.myisp.example}
</code></pre>
</blockquote>
 </dd>
<dt><code>addrcodec</code></dt>
<dd> <p> Perform email address codec transformations on raw-data argument, rather according to email standards (RFC 5322; [v15 behaviour may differ] will furtherly improve). Supports <code>vput</code> (see Sx Command modifiers ) , and manages the error number <i>!</i> The first argument must be either <i>[+[+[+]]]e[ncode]</i> <i>d[ecode]</i> <i>s[kin]</i> or <i>skinl[ist]</i> and specifies the operation to perform on the rest of the line. </p>
<p> Decoding will show how a standard-compliant MUA will display the given argument, which should be an email address. Please be aware that most MUAs have difficulties with the address standards, and vary wildly when (comments) in parenthesis, ``double-quoted&#8217;&#8216; strings, or quoted-pairs, as below, become involved. [v15 behaviour may differ] S-nail currently does not perform decoding when displaying addresses. </p>
<p> Skinning is identical to decoding but only outputs the plain address, without any string, comment etc. components. Another difference is that it may fail with the error number <i>!</i> set to <i>^ERR </i><code>-INVAL</code> if decoding fails to find a(n) (valid) email address, in which case the unmodified input will be output again. </p>
<p> <i>skinlist</i> first performs a skin operation, and thereafter checks a valid address for whether it is a registered mailing list (see <code>mlist</code> and <code>mlsubscribe )</code> eventually reporting that state in the error number <i>!</i> as <i>^ERR </i><code>-EXIST</code> (This state could later become overwritten by an I/O error, though.) </p>
<p> Encoding supports four different modes, lesser automated versions can be chosen by prefixing one, two or three plus signs: the standard imposes a special meaning on some characters, which thus have to be transformed to so-called quoted-pairs by pairing them with a reverse solidus `\&#8216; in order to remove the special meaning; this might change interpretation of the entire argument from what has been desired, however! Specify one plus sign to remark that parenthesis shall be left alone, two for not turning double quotation marks into quoted-pairs, and three for also leaving any user-specified reverse solidus alone. The result will always be valid, if a successful exit status is reported ([v15 behaviour may differ] the current parser fails this assertion for some constructs). [v15 behaviour may differ] Addresses need to be specified in between angle brackets `&lt;&#8216; , `&gt;&#8216; if the construct becomes more difficult, otherwise the current parser will fail; it is not smart enough to guess right. </p>
<blockquote><pre><code>? addrc enc &quot;Hey, you&quot;,&lt;diet [at] exam.ple&gt;\ out\ there
&quot;\&quot;Hey, you\&quot;, \\ out\\ there&quot; &lt;diet [at] exam.ple&gt;
? addrc d &quot;\&quot;Hey, you\&quot;, \\ out\\ there&quot; &lt;diet [at] exam.ple&gt;
&quot;Hey, you&quot;, \ out\ there &lt;diet [at] exam.ple&gt;
? addrc s &quot;\&quot;Hey, you\&quot;, \\ out\\ there&quot; &lt;diet [at] exam.ple&gt;
diet [at] exam.ple
</code></pre>
</blockquote>
 </dd>
<dt><code>alias , unalias</code></dt>
<dd> <p> [Only new quoting rules](a, una) Define or list, and remove, respectively, address aliases, which are a method of creating personal distribution lists that map a single name to none to multiple receivers, to be expanded after Sx Compose mode is left; the expansion correlates with <i>metoo</i> The latter command removes all given aliases, the special name asterisk `*&#8216; will remove all existing aliases. When used without arguments the former shows a list of all currently known aliases, with one argument only the target(s) of the given one. When given two arguments, hyphen-minus `-&#8216; being the first, the target(s) of the second is/are expanded recursively. </p>
<p> In all other cases the given alias is newly defined, or will be appended to: arguments must either be themselves valid alias names, or any other address type (see Sx On sending mail, and non-interactive mode ) . Recursive expansion of aliases can be prevented by prefixing the desired argument with the modifier reverse solidus <code>\</code> A valid alias name conforms to <i>mta-aliases</i> syntax, but follow-up characters can also be the number sign `#&#8216; , colon `:&#8216; , commercial at `@,&#8216; exclamation mark `!&#8216; , period `.&#8216; as well as ``any character that has the high bit set&#8217;&#8216; The dollar sign `$&#8216; may be the last character. The number sign `#&#8216; may need Sx Shell-style argument quoting . </p>
<p> [v15 behaviour may differ] Unfortunately the colon is currently not supported, as it interferes with normal address parsing rules. [v15 behaviour may differ] Such high bit characters will likely cause warnings at the moment for the same reasons why colon is unsupported; also, in the future locale dependent character set validity checks will be performed. </p>
<blockquote><pre><code>? alias cohorts bill jkf mark kridle [at] ucbcory ~/cohorts.mbox
? alias mark mark [at] exam.ple
? set mta-aliases=/etc/aliases
</code></pre>
</blockquote>
 </dd>
<dt><code>alternates , unalternates</code></dt>
<dd> <p> [Only new quoting rules] (alt) Manage a list of alternate addresses or names of the active user, members of which will be removed from recipient lists (except one). There is a set of implicit alternates which is formed of the values of <code>LOGNAME</code> <i>from</i> <i>sender</i> and <i>reply-to</i> <i>from</i> will not be used if <i>sender</i> is set. The latter command removes the given list of alternates, the special name `*&#8216; will discard all existing alternate names. </p>
<p> The former command manages the error number <i>!</i> It shows the current set of alternates when used without arguments; in this mode only it also supports <code>vput</code> (see Sx Command modifiers ) . Otherwise the given arguments (after being checked for validity) are appended to the list of alternate names; in <i>posix</i> mode they replace that list instead. </p>
 </dd>
<dt><code>answered , unanswered</code></dt>
<dd> <p> Take a message lists and mark each message as (not) having been answered. Messages will be marked answered when being <code>reply d</code> to automatically if the <i>markanswered</i> variable is set. See the section Sx Message states . </p>
 </dd>
<dt><code>bind , unbind</code></dt>
<dd> <p> [Option][Only new quoting rules] The bind command extends the MLE (see Sx On terminal control and line editor ) with freely configurable key bindings. The latter command removes from the given context the given key binding, both of which may be specified as a wildcard `*&#8216; , so that `unbind&#8217; * * will remove all bindings of all contexts. Due to initialization order unbinding will not work for built-in key bindings upon program startup, however: please use <i>line-editor-no-defaults</i> for this purpose instead. </p>
<p> With zero arguments, or with a context name the former command shows all key bindings (of the given context; an asterisk `*&#8216; will iterate over all contexts); a more verbose listing will be produced if either of <i>debug</i> or <i>verbose</i> are set. With two or more arguments a specific binding is shown, or (re)established: the first argument is the context to which the binding shall apply, the second argument is a comma-separated list of the ``keys&#8217;&#8216; which form the binding. Further arguments will be joined to form the expansion, and cause the binding to be created or updated. To indicate that a binding shall not be auto-committed, but that the expansion shall instead be furtherly editable by the user, a commercial at `@&#8216; (that will be removed) can be placed last in the expansion, from which leading and trailing whitespace will finally be removed. Reverse solidus cannot be used as the last character of expansion. An empty expansion will be rejected. </p>
<p> Contexts define when a binding applies, i.e., a binding will not be seen unless the context for which it is defined for is currently active. This is not true for the shared binding `base&#8217; , which is the foundation for all other bindings and as such always applies, its bindings, however, only apply secondarily. The available contexts are the shared `base&#8217; , the `default&#8217; context which is used in all not otherwise documented situations, and `compose&#8217; , which applies only to Sx Compose mode . </p>
<p> Bindings are specified as a comma-separated list of byte-sequences, where each list entry corresponds to one ``key&#8217;&#8216; (press). Byte sequence boundaries will be forcefully terminated after <i>bind-inter-byte-timeout</i> milliseconds, whereas key sequences can be timed out via <i>bind-inter-key-timeout</i> A list entry may, indicated by a leading colon character `:&#8216; , also refer to the name of a terminal capability; several dozen names are compiled in and may be specified either by their <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5), or, if existing, by their <a href="/docs/linux/man/5-termcap/">termcap</a>(5) name, regardless of the actually used [Option]al terminal control library. But any capability may be used, as long as the name is resolvable by the [Option]al control library, or was defined via the internal variable <i>termcap</i> Input sequences are not case-normalized, an exact match is required to update or remove a binding. It is advisable to use an initial escape or other control character (like `\cA&#8217; ) for user (as opposed to purely terminal capability based) bindings in order to avoid ambiguities; it also reduces search time. Examples: </p>
<blockquote><pre><code>? bind base a,b echo one
? bind base $'\E',d mle-snarf-word-fwd # Esc(ape)
? bind base $'\E',$'\c?' mle-snarf-word-bwd # Esc,Delete
? bind default $'\cA',:khome,w 'echo Editable binding@'
? bind default a,b,c rm -irf / @ # Also editable
? bind default :kf1 File %
? bind compose :kf1 ~v
</code></pre>
</blockquote>
<p> Note that the entire comma-separated list is first parsed (over) as a shell-token with whitespace as the field separator, then parsed and expanded for real with comma as the field separator, therefore whitespace needs to be properly quoted, see Sx Shell-style argument quoting . Using Unicode reverse solidus escape sequences renders a binding defunctional if the locale does not support Unicode (see Sx Character sets ) , and using terminal capabilities does so if no (corresponding) terminal control support is (currently) available. Adding, deleting or modifying a key binding invalidates the internal prebuilt lookup tree, it will be recreated as necessary: this process will be visualized in most <i>verbose</i> as well as in <i>debug</i> mode. </p>
<p> The following terminal capability names are built-in and can be used in <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5) or (if available) the two-letter <a href="/docs/linux/man/5-termcap/">termcap</a>(5) notation. See the respective manual for a list of capabilities. The program <a href="/docs/linux/man/1-infocmp/">infocmp</a>(1) can be used to show all the capabilities of <code>TERM</code> or the given terminal type; using the -<code>x</code> flag will also show supported (non-standard) extensions. </p>
 </dd>
<dl>
<dt><code>kbs &nbsp;or kb</code></dt>
<dd> <p> Backspace. </p>
 </dd>
<dt><code>kdch1 &nbsp;or kD</code></dt>
<dd> <p> Delete character. </p>
 </dd>
<dt><code>kDC &nbsp;or *4</code></dt>
<dd> <p> --- shifted variant. </p>
 </dd>
<dt><code>kel &nbsp;or kE</code></dt>
<dd> <p> Clear to end of line. </p>
 </dd>
<dt><code>kext &nbsp;or @9</code></dt>
<dd> <p> Exit. </p>
 </dd>
<dt><code>kich1 &nbsp;or kI</code></dt>
<dd> <p> Insert character. </p>
 </dd>
<dt><code>kIC &nbsp;or #3</code></dt>
<dd> <p> --- shifted variant. </p>
 </dd>
<dt><code>khome &nbsp;or kh</code></dt>
<dd> <p> Home. </p>
 </dd>
<dt><code>kHOM &nbsp;or #2</code></dt>
<dd> <p> --- shifted variant. </p>
 </dd>
<dt><code>kend &nbsp;or @7</code></dt>
<dd> <p> End. </p>
 </dd>
<dt><code>knp &nbsp;or kN</code></dt>
<dd> <p> Next page. </p>
 </dd>
<dt><code>kpp &nbsp;or kP</code></dt>
<dd> <p> Previous page. </p>
 </dd>
<dt><code>kcub1 &nbsp;or kl</code></dt>
<dd> <p> Left cursor (with more modifiers: see below). </p>
 </dd>
<dt><code>kLFT &nbsp;or #4</code></dt>
<dd> <p> --- shifted variant. </p>
 </dd>
<dt><code>kcuf1 &nbsp;or kr</code></dt>
<dd> <p> Right cursor (ditto). </p>
 </dd>
<dt><code>kRIT &nbsp;or %i</code></dt>
<dd> <p> --- shifted variant. </p>
 </dd>
<dt><code>kcud1 &nbsp;or kd</code></dt>
<dd> <p> Down cursor (ditto). </p>
 </dd>
<dt><code>kDN</code></dt>
<dd> <p> --- shifted variant (only terminfo). </p>
 </dd>
<dt><code>kcuu1 &nbsp;or ku</code></dt>
<dd> <p> Up cursor (ditto). </p>
 </dd>
<dt><code>kUP</code></dt>
<dd> <p> --- shifted variant (only terminfo). </p>
 </dd>
<dt><code>kf0 &nbsp;or k0</code></dt>
<dd> <p> Function key 0. Add one for each function key up to <code>kf9</code> and <code>k9</code> respectively. </p>
 </dd>
<dt><code>kf10 &nbsp;or k;</code></dt>
<dd> <p> Function key 10. </p>
 </dd>
<dt><code>kf11 &nbsp;or F1</code></dt>
<dd> <p> Function key 11. Add one for each function key up to <code>kf19</code> and <code>F9</code> respectively. </p>
 </dd></dl>
<p> Some terminals support key-modifier combination extensions, e.g., `Alt+Shift+xy&#8217; For example, the delete key, <code>kdch1</code> in its shifted variant, the name is mutated to <code>kDC</code> then a number is appended for the states `Alt&#8217; ( <code>kDC3</code> `Shift+Alt&#8217; ( <code>kDC4</code> `Control&#8217; ( <code>kDC5</code> `Shift+Control&#8217; ( <code>kDC6</code> `Alt+Control&#8217; ( <code>kDC7</code> finally `Shift+Alt+Control&#8217; ( <code>kDC8</code> The same for the left cursor key, <code>kcub1</code> <code>KLFT , KLFT3 , KLFT4 , KLFT5 , KLFT6 , KLFT7 , KLFT8</code> </p>
<dt><code>call</code></dt>
<dd> <p> [Only new quoting rules] Calls the given macro, which must have been created via <code>define</code> (see there for more), otherwise an <i>^ERR </i><code>-NOENT</code> error occurs. Calling macros recursively will at some time excess the stack size limit, causing a hard program abortion; if recursively calling a macro is the last command of the current macro, consider to use the command <code>xcall</code> which will first release all resources of the current macro before replacing the current macro with the called one. </p>
 </dd>
<dt><code>call_if</code></dt>
<dd> <p> Identical to <code>call</code> if the given macro has been created via <code>define</code> but does not fail nor warn if the macro does not exist. </p>
 </dd>
<dt><code>cd</code></dt>
<dd> <p> Synonym for <code>chdir</code> </p>
 </dd>
<dt><code>certsave</code></dt>
<dd> <p> [Option] Only applicable to S/MIME signed messages. Takes an optional message list and a filename and saves the certificates contained within the message signatures to the named file in both human-readable and PEM format. The certificates can later be used to send encrypted messages to the respective message senders by setting <i>smime-encrypt-USER [at] HOST</i> variables. </p>
 </dd>
<dt><code>charsetalias , uncharsetalias</code></dt>
<dd> <p> [Only new quoting rules] Manage alias mappings for (conversion of) Sx Character sets . Alias processing is not performed for Sx INTERNAL VARIABLES , for example <i>charset-8bit</i> and mappings are ineffective if character set conversion is not available ( <i>features</i> does not announce `,+iconv,&#8216; ) . Expansion happens recursively for cases where aliases point to other aliases (built-in loop limit: 8). </p>
<p> The latter command deletes all aliases given as arguments, or all at once when given the asterisk `*&#8216; The former shows the list of all currently defined aliases if used without arguments, or the target of the given single argument; when given two arguments, hyphen-minus `-&#8216; being the first, the second is instead expanded recursively. In all other cases the given arguments are treated as pairs of character sets and their desired target alias name, creating new or updating already existing aliases. </p>
 </dd>
<dt><code>chdir</code></dt>
<dd> <p> [Only new quoting rules](ch) Change the working directory to <code>HOME</code> or the given argument. Synonym for <code>cd</code> </p>
 </dd>
<dt><code>collapse , uncollapse</code></dt>
<dd> <p> Only applicable to `thread&#8217; Ns ed <code>sort</code> mode. Takes a message list and makes all replies to these messages invisible in header summaries, except for `new&#8217; messages and the ``dot&#8217;&#8216; Also when a message with collapsed replies is displayed, all of these are automatically uncollapsed. The latter command undoes collapsing. </p>
 </dd>
<dt><code>colour , uncolour</code></dt>
<dd> <p> [Option][Only new quoting rules] Manage colour mappings of and for a Sx Coloured display . Without arguments the former shows all currently defined mappings. Otherwise a colour type is expected (case-insensitively), it must be one of `256&#8217; for 256-colour terminals, `8&#8217; , `ansi&#8217; or `iso&#8217; for the standard 8-colour ANSI / ISO 6429 colour palette, and `1&#8217; or `mono&#8217; for monochrome terminals, which only support (some) font attributes. Without further arguments the list of all currently defined mappings of the given type is shown (here the special `all&#8217; or `*&#8216; also show all currently defined mappings). </p>
<p> Otherwise the second argument defines the mappable slot, the third argument a (comma-separated list of) colour and font attribute specification(s), and the optionally supported fourth argument can be used to specify a precondition: if conditioned mappings exist they are tested in (creation) order unless a (case-insensitive) match has been found, and the default mapping (if any has been established) will only be chosen as a last resort. The types of available preconditions depend on the mappable slot, the following of which exist: </p>
<p> Mappings prefixed with `mle-&#8216; are used for the [Option]al built-in Mailx-Line-Editor (MLE, see Sx On terminal control and line editor ) and do not support preconditions. </p>
 </dd>
<dl>
<dt><i>mle-position</i></dt>
<dd> <p> This mapping is used for the position indicator that is visible when a line cannot be fully displayed on the screen. </p>
 </dd>
<dt><i>mle-prompt</i></dt>
<dd> <p> Used for the <i>prompt</i> </p>
 </dd>
<dt><i>mle-error</i></dt>
<dd> <p> Used for the occasionally appearing error indicator that is joined onto <i>prompt</i> [v15 behaviour may differ] Also used for error messages written on standard error . </p>
 </dd></dl>
<p> Mappings prefixed with `sum-&#8216; are used in header summaries, and they all understand the preconditions `dot&#8217; (the current message) and `older&#8217; for elder messages (only honoured in conjunction with <i>datefield-markout-older )</i> </p>
<dl>
<dt><i>sum-dotmark</i></dt>
<dd> <p> This mapping is used for the ``dotmark&#8217;&#8216; that can be created with the `%&gt;&#8216; or `%&lt;&#8216; formats of the variable <i>headline</i> </p>
 </dd>
<dt><i>sum-header</i></dt>
<dd> <p> For the complete header summary line except the ``dotmark&#8217;&#8216; and the thread structure. </p>
 </dd>
<dt><i>sum-thread</i></dt>
<dd> <p> For the thread structure which can be created with the `%i&#8217; format of the variable <i>headline</i> </p>
 </dd></dl>
<p> Mappings prefixed with `view-&#8216; are used when displaying messages. </p>
<dl>
<dt><i>view-from_</i></dt>
<dd> <p> This mapping is used for so-called `From_&#8216; lines, which are MBOX file format specific header lines (also see <i>mbox-rfc4155 )</i> </p>
 </dd>
<dt><i>view-header</i></dt>
<dd> <p> For header lines. A comma-separated list of headers to which the mapping applies may be given as a precondition; if the [Option]al regular expression support is available then if any of the Sx magic regular expression characters is seen the precondition will be evaluated as (an extended) one. </p>
 </dd>
<dt><i>view-msginfo</i></dt>
<dd> <p> For the introductional message info line. </p>
 </dd>
<dt><i>view-partinfo</i></dt>
<dd> <p> For MIME part info lines. </p>
 </dd></dl>
<p> The following (case-insensitive) colour definitions and font attributes are understood, multiple of which can be specified in a comma-separated list: </p>
<dl>
<dt><i>ft=</i></dt>
<dd> <p> a font attribute: `bold&#8217; , `reverse&#8217; or `underline&#8217; It is possible (and often applicable) to specify multiple font attributes for a single mapping. </p>
 </dd>
<dt><i>fg=</i></dt>
<dd> <p> foreground colour attribute, in order (numbers 0 - 7) `black&#8217; , `red&#8217; , `green&#8217; , `brown&#8217; , `blue&#8217; , `magenta&#8217; , `cyan&#8217; or `white&#8217; To specify a 256-colour mode a decimal number colour specification in the range 0 to 255, inclusive, is supported, and interpreted as follows: </p>
 </dd>
<dl>
<dt><code>0 - 7</code></dt>
<dd> <p> the standard ISO 6429 colours, as above. </p>
 </dd>
<dt><code>8 - 15</code></dt>
<dd> <p> high intensity variants of the standard colours. </p>
 </dd>
<dt><code>16 - 231</code></dt>
<dd> <p> 216 colours in tuples of 6. </p>
 </dd>
<dt><code>232 - 255</code></dt>
<dd> <p> grayscale from black to white in 24 steps. </p>
 </dd></dl>
<blockquote><pre><code>#!/bin/sh -
fg() { printf &quot;\033[38;5;${1}m($1)&quot;; }
bg() { printf &quot;\033[48;5;${1}m($1)&quot;; }
i=0
while [ $i -lt 256 ]; do fg $i; i=$(($i + 1)); done
printf &quot;\033[0m\n&quot;
i=0
while [ $i -lt 256 ]; do bg $i; i=$(($i + 1)); done
printf &quot;\033[0m\n&quot;
</code></pre>
</blockquote>
<dt><i>bg=</i></dt>
<dd> <p> background colour attribute (see <code>fg=</code> for possible values). </p>
 </dd></dl>
<p> The command <code>uncolour</code> will remove for the given colour type (the special type `*&#8216; selects all) the given mapping; if the optional precondition argument is given only the exact tuple of mapping and precondition is removed. The special name `*&#8216; will remove all mappings (no precondition allowed), thus `uncolour&#8217; * * will remove all established mappings. </p>
<dt><code>commandalias , uncommandalias</code></dt>
<dd> <p> [Only new quoting rules] Define or list, and remove, respectively, command aliases. An (command)alias can be used everywhere a normal command can be used, but always takes precedence: any arguments that are given to the command alias are joined onto the alias expansion, and the resulting string forms the command line that is, in effect, executed. The latter command removes all given aliases, the special name asterisk `*&#8216; will remove all existing aliases. When used without arguments the former shows a list of all currently known aliases, with one argument only the expansion of the given one. </p>
<p> With two or more arguments a command alias is defined or updated: the first argument is the name under which the remaining command line should be accessible, the content of which can be just about anything. An alias may itself expand to another alias, but to avoid expansion loops further expansion will be prevented if an alias refers to itself or if an expansion depth limit is reached. Explicit expansion prevention is available via reverse solidus <code>\</code> one of the Sx Command modifiers . </p>
<blockquote><pre><code>? commandalias xx
s-nail: `commandalias': no such alias: xx
? commandalias xx echo hello,
? commandalias xx
commandalias xx 'echo hello,'
? xx
hello,
? xx world
hello, world
</code></pre>
</blockquote>
 </dd>
<dt><code>Copy</code></dt>
<dd> <p> (C) Similar to <code>copy</code> but copy the messages to a file named after the local part of the sender of the first message instead of taking a filename argument; <i>outfolder</i> is inspected to decide on the actual storage location. </p>
 </dd>
<dt><code>copy</code></dt>
<dd> <p> (c) Copy messages to the named file and do not mark them as being saved; otherwise identical to <code>save</code> </p>
 </dd>
<dt><code>csop</code></dt>
<dd> <p> [Only new quoting rules] A multiplexer command which provides C-style string operations on 8-bit bytes without a notion of locale settings and character sets, effectively assuming ASCII data. For numeric and other operations refer to <code>vexpr</code> <code>vput</code> one of the Sx Command modifiers , is supported. The error result is `-1&#8217; for usage errors and numeric results, the empty string otherwise; missing data errors, as for unsuccessful searches, result in the <i>!</i> error number being set to <i>^ERR </i><code>-NODATA</code> Where the question mark `?&#8216; modifier suffix is supported, a case-insensitive (ASCII mapping) operation mode is supported; the keyword `case&#8217; is optional so that `find?&#8216; and `find?case&#8217; are identical. </p>
 </dd>
<dl>
<dt><code>length</code></dt>
<dd> <p> Queries the length of the given argument. </p>
 </dd>
<dt><code>hash , hash32</code></dt>
<dd> <p> Calculates a hash value of the given argument. The latter will return a 32-bit result regardless of host environment. `?&#8216; modifier suffix is supported. These use Chris Torek&#8217;s hash algorithm, the resulting hash value is bit mixed as shown by Bret Mulvey. </p>
 </dd>
<dt><code>find</code></dt>
<dd> <p> Search for the second in the first argument. Shows the resulting 0-based offset shall it have been found. `?&#8216; modifier suffix is supported. </p>
 </dd>
<dt><code>substring</code></dt>
<dd> <p> Creates a substring of its first argument. The optional second argument is the 0-based starting offset, a negative one counts from the end; the optional third argument specifies the length of the desired result, a negative length leaves off the given number of bytes at the end of the original string; by default the entire string is used. This operation tries to work around faulty arguments (set <i>verbose</i> for error logs), but reports them via the error number <i>!</i> as <i>^ERR </i><code>-OVERFLOW</code> </p>
 </dd>
<dt><code>trim</code></dt>
<dd> <p> Trim away whitespace characters from both ends of the argument. </p>
 </dd>
<dt><code>trim-front</code></dt>
<dd> <p> Trim away whitespace characters from the begin of the argument. </p>
 </dd>
<dt><code>trim-end</code></dt>
<dd> <p> Trim away whitespace characters from the end of the argument. </p>
 </dd></dl>
<dt><code>cwd</code></dt>
<dd> <p> Show the name of the current working directory, as reported by <a href="/docs/linux/man/3-getcwd/">getcwd</a>(3). Supports <code>vput</code> (see Sx Command modifiers ) . The return status is tracked via <i>?</i> </p>
 </dd>
<dt><code>Decrypt</code></dt>
<dd> <p> [Option] For unencrypted messages this command is identical to <code>Copy</code> Encrypted messages are first decrypted, if possible, and then copied. </p>
 </dd>
<dt><code>decrypt</code></dt>
<dd> <p> [Option] For unencrypted messages this command is identical to <code>copy</code> Encrypted messages are first decrypted, if possible, and then copied. </p>
 </dd>
<dt><code>define , undefine</code></dt>
<dd> <p> The latter command deletes the given macro, the special name `*&#8216; will discard all existing macros. Deletion of (a) macro(s) can be performed from within running (a) macro(s), including self-deletion. Without arguments the former command prints the current list of macros, including their content, otherwise it defines a macro, replacing an existing one of the same name as applicable. </p>
<p> A defined macro can be invoked explicitly by using the <code>call</code> <code>call_if</code> and <code>xcall</code> commands, or implicitly if a macro hook is triggered, for example a <i>folder-hook</i> Execution of a macro body can be stopped from within by calling <code>return</code> </p>
<p> Temporary macro block-scope variables can be created or deleted with the <code>local</code> command modifier in conjunction with the commands <code>set</code> and <code>unset</code> respectively. To enforce unrolling of changes made to (global) Sx INTERNAL VARIABLES the command <code>localopts</code> can be used instead; its covered scope depends on how (i.e., ``as what&#8217;&#8216; normal macro, folder hook, hook, <code>account</code> switch) the macro is invoked. </p>
<p> Inside a <code>call ed macro, the given positional parameters are implicitly local</code> to the macro&#8217;s scope, and may be accessed via the variables <i>*</i> <i>@</i> <i>#</i> and <i>1</i> and any other positive unsigned decimal number less than or equal to <i>#</i> Positional parameters can be <code>shift ed, or become completely replaced, removed etc. via</code> <code>vpospar</code> A helpful command for numeric computation and string evaluations is <code>vexpr</code> <code>csop</code> offers C-style byte string operations. </p>
<blockquote><pre><code>define name {
  command1
  command2
  ...
  commandN
}
define exmac {
  echo Parameter 1 of ${#} is ${1}, all: ${*} / ${@}
  return 1000 0
}
call exmac Hello macro exmac!
echo ${?}/${!}/${^ERRNAME}
</code></pre>
</blockquote>
 </dd>
<dt><code>delete , undelete</code></dt>
<dd> <p> (d, u) Marks the given message list as being or not being `deleted&#8217; , respectively; if no argument has been specified then the usual search for a visible message is performed, as documented for Sx Message list arguments , showing only the next input prompt if the search fails. Deleted messages will neither be saved in the Sx secondary mailbox <code>MBOX</code> nor will they be available for most other commands. If the <i>autoprint</i> variable is set, the new ``dot&#8217;&#8216; or the last message restored, respectively, is automatically <code>type d; also see</code> <code>dp</code> <code>dt</code> </p>
 </dd>
<dt><code>digmsg</code></dt>
<dd> <p> [Only new quoting rules] Digging (information out of) messages is possible through <code>digmsg</code> objects, which can be <code>create d for the given message number; in</code> Sx Compose mode the hyphen-minus `-&#8216; will instead open the message that is being composed. If a hyphen-minus is given as the optional third argument then output will be generated on the standard output channel instead of being subject to consumption by the <code>readall</code> (or <code>read</code> and <code>readsh</code> command(s). Note: output must be consumed before normal processing can continue; for <code>digmsg</code> objects this means each command output has to be read until the end of file (EOF) state occurs. </p>
<p> The objects may be <code>remove d again by giving the same identifier used for creation;</code> this step could be omitted: objects will be automatically closed when the active <code>folder</code> (mailbox) or the compose mode is left, respectively. In all other use cases the second argument is an object identifier, and the third and all following arguments are interpreted as via <code>~^</code> (see Sx COMMAND ESCAPES ) : </p>
<blockquote><pre><code>? vput = msgno; digmsg create $msgno
? digmsg $msgno header list; readall x; echon $x
210 Subject From To Message-ID References In-Reply-To
? digmsg $msgno header show Subject;readall x;echon $x
212 Subject
'Hello, world'
? digmsg remove $msgno
</code></pre>
</blockquote>
 </dd>
<dt><code>discard</code></dt>
<dd> <p> (di) Identical to <code>ignore</code> Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>dp , dt</code></dt>
<dd> <p> Delete the given messages and automatically <code>type</code> the new ``dot&#8217;&#8216; if one exists, regardless of the setting of <i>autoprint</i> </p>
 </dd>
<dt><code>dotmove</code></dt>
<dd> <p> Move the ``dot&#8217;&#8216; up or down by one message when given `+&#8216; or `-&#8216; argument, respectively. </p>
 </dd>
<dt><code>draft , undraft</code></dt>
<dd> <p> Take message lists and mark each given message as being draft, or not being draft, respectively, as documented in the section Sx Message states . </p>
 </dd>
<dt><code>echo</code></dt>
<dd> <p> [Only new quoting rules](ec) Print the given strings, equivalent to the shell utility <a href="/docs/linux/man/1-echo/">echo</a>(1), that is, Sx Shell-style argument quoting expansion is performed and, different to the otherwise identical <code>echon</code> a trailing newline is echoed. <code>vput</code> as documented in Sx Command modifiers is supported, and the error number <i>!</i> is managed: if data is stored in a variable then the return value reflects the length of the result string in case of success and is `-1&#8217; on error. </p>
<p> <code>Remarks:</code> this command traditionally (in BSD Mail) also performed Sx Filename transformations , which is standard incompatible and hard to handle because quoting transformation patterns is not possible; the subcommand <code>file-expand</code> of <code>vexpr</code> can be used to expand filenames. </p>
 </dd>
<dt><code>echoerr</code></dt>
<dd> <p> [Only new quoting rules] Identical to <code>echo</code> but the message is written to standard error, and prefixed by <i>log-prefix</i> Also see <code>echoerrn</code> In interactive sessions the [Option]al message ring queue for <code>errors</code> will be used instead, if available and <code>vput</code> was not used. </p>
 </dd>
<dt><code>echon</code></dt>
<dd> <p> [Only new quoting rules] Identical to <code>echo</code> but does not write or store a trailing newline. </p>
 </dd>
<dt><code>echoerrn</code></dt>
<dd> <p> [Only new quoting rules] Identical to <code>echoerr</code> but does not write or store a trailing newline. </p>
 </dd>
<dt><code>edit</code></dt>
<dd> <p> (e) Point the text <code>EDITOR</code> at each message from the given list in turn. Modified contents are discarded unless the <i>writebackedited</i> variable is set, and are not used unless the mailbox can be written to and the editor returns a successful exit status. <code>visual</code> can be used instead for a more display oriented editor. </p>
 </dd>
<dt><code>elif</code></dt>
<dd> <p> Part of the <code>if</code> (see there for more), <code>elif , else , endif</code> conditional --- if the condition of a preceding <code>if</code> was false, check the following condition and execute the following block if it evaluates true. </p>
 </dd>
<dt><code>else</code></dt>
<dd> <p> (el) Part of the <code>if</code> (see there for more), <code>elif , else , endif</code> conditional --- if none of the conditions of the preceding <code>if</code> and <code>elif</code> commands was true, the <code>else</code> block is executed. </p>
 </dd>
<dt><code>endif</code></dt>
<dd> <p> (en) Marks the end of an <code>if</code> (see there for more), <code>elif , else , endif</code> conditional execution block. </p>
 </dd>
<dt><code>environ</code></dt>
<dd> <p> [Only new quoting rules] There is a strict separation in between Sx INTERNAL VARIABLES and the program Sx ENVIRONMENT , which is inherited by child processes. Some variables of the latter are however vivid for program operation, their purpose is known, therefore they have been integrated transparently into handling of the former, as accessible via <code>set</code> and <code>unset</code> To integrate any other environment variable, and/or to export internal variables into the process environment where they normally are not, a <code>link</code> needs to become established with this command, for example </p>
<blockquote><p> <code>environ link PERL5LIB TZ</code> </p>
</blockquote>
<p> Afterwards changing such variables with <code>set</code> will cause automatic updates of the environment, too. Sufficient system support provided (it was in BSD as early as 1987, and is standardized since Y2K) removing such variables with <code>unset</code> will remove them also from the environment, but in any way the knowledge they ever have been <code>link ed will be lost.</code> This implies that <code>localopts</code> may cause loss of such links. </p>
<p> The subcommand <code>unlink</code> removes an existing link without otherwise touching variables, the <code>set</code> and <code>unset</code> subcommands are identical to <code>set</code> and <code>unset</code> but additionally update the program environment accordingly; removing a variable breaks any freely established <code>link</code> </p>
 </dd>
<dt><code>errors</code></dt>
<dd> <p> [Option] As console user interfaces at times scroll error messages by too fast and/or out of scope, data can additionally be sent to an error queue manageable by this command: <i>show</i> or no argument will display and clear the queue, <i>clear</i> will only clear it. As the queue becomes filled with <i>errors-limit</i> entries the eldest entries are being dropped. There are also the variables <i>^ERRQUEUE-COUNT</i> and <i>^ERRQUEUE-EXISTS</i> </p>
 </dd>
<dt><code>eval</code></dt>
<dd> <p> [Only new quoting rules] Construct a command by concatenating the arguments, separated with a single space character, and then evaluate the result. This command passes through the exit status <i>?</i> and error number <i>!</i> of the evaluated command; also see <code>call</code> </p>
<blockquote><pre><code>define xxx {
  echo &quot;xxx arg &lt;$1&gt;&quot;
  shift
  if $# -gt 0
    \xcall xxx &quot;$@&quot;
  endif
}
define yyy {
  eval &quot;$@ ' ball&quot;
}
call yyy '\call xxx' &quot;b\$'\t'u ' &quot;
call xxx arg &lt;b u&gt;
call xxx arg &lt; &gt;
call xxx arg &lt;ball&gt;
</code></pre>
</blockquote>
 </dd>
<dt><code>exit</code></dt>
<dd> <p> (ex or x) Exit from S-nail without changing the active mailbox and skip any saving of messages in the Sx secondary mailbox <code>MBOX</code> as well as a possibly tracked line editor <i>history-file</i> A possibly set <i>on-account-cleanup</i> will be invoked, however. The optional status number argument will be passed through to <a href="/docs/linux/man/3-exit/">exit</a>(3). [v15 behaviour may differ] For now it can happen that the given status will be overwritten, later this will only occur if a later error needs to be reported onto an otherwise success indicating status. </p>
 </dd>
<dt><code>File</code></dt>
<dd> <p> (Fi) Like <code>folder</code> but open the mailbox read-only. </p>
 </dd>
<dt><code>file</code></dt>
<dd> <p> (fi) See <code>folder</code> </p>
 </dd>
<dt><code>filetype , unfiletype</code></dt>
<dd> <p> [Only new quoting rules] Define, list, and remove, respectively, file handler hooks, which provide (shell) commands that enable S-nail to load and save MBOX files from and to files with the registered file extensions, as shown and described for <code>folder</code> The extensions are used case-insensitively, yet the auto-completion feature of for example <code>folder</code> will only work case-sensitively. An intermediate temporary file will be used to store the expanded data. The latter command will remove hooks for all given extensions, asterisk `*&#8216; will remove all existing handlers. </p>
<p> When used without arguments the former shows a list of all currently defined file hooks, with one argument the expansion of the given alias. Otherwise three arguments are expected, the first specifying the file extension for which the hook is meant, and the second and third defining the load- and save commands to deal with the file type, respectively, both of which must read from standard input and write to standard output. Changing hooks will not affect already opened mailboxes ([v15 behaviour may differ] except below). [v15 behaviour may differ] For now too much work is done, and files are oftened read in twice where once would be sufficient: this can cause problems if a filetype is changed while such a file is opened; this was already so with the built-in support of .gz etc. in Heirloom, and will vanish in v15. [v15 behaviour may differ] For now all handler strings are passed to the <code>SHELL for evaluation purposes; in the future a</code> `!&#8216; prefix to load and save commands may mean to bypass this shell instance: placing a leading space will avoid any possible misinterpretations. </p>
<blockquote><pre><code>? filetype bz2 'bzip2 -dc' 'bzip2 -zc' \
    gz 'gzip -dc' 'gzip -c' xz 'xz -dc' 'xz -zc' \
    zst 'zstd -dc' 'zstd -19 -zc' \
    zst.pgp 'gpg -d | zstd -dc' 'zstd -19 -zc | gpg -e'
? set record=+sent.zst.pgp
</code></pre>
</blockquote>
 </dd>
<dt><code>flag , unflag</code></dt>
<dd> <p> Take message lists and mark the messages as being flagged, or not being flagged, respectively, for urgent/special attention. See the section Sx Message states . </p>
 </dd>
<dt><code>Folder</code></dt>
<dd> <p> (Fold) Like <code>folder</code> but open the mailbox read-only. </p>
 </dd>
<dt><code>folder</code></dt>
<dd> <p> (fold) Open a new, or show status information of the current mailbox. If an argument is given, changes (such as deletions) will be written out, a new mailbox will be opened, the internal variables <i>mailbox-resolved</i> and <i>mailbox-display</i> will be updated, a set according <i>folder-hook</i> is executed, and optionally a summary of <code>headers</code> is displayed if the variable <i>header</i> is set. </p>
<p> Sx Filename transformations will be applied to the <i>name</i> argument, and `protocol://&#8216; prefixes are, i.e., URL (see Sx On URL syntax and credential lookup ) syntax is understood, as in `<a href="mbox:///tmp/somefolder'">mbox:///tmp/somefolder&#8217;</a> If a protocol prefix is used the mailbox type is fixated, otherwise opening none-existing <code>folders</code> uses the protocol defined in <i>newfolders</i> </p>
<p> For the protocols <i>mbox</i> and <i>file</i> (MBOX database), as well as <i>eml</i> (electronic mail message [v15 behaviour may differ] read-only) the list of all registered <code>filetype s is traversed to check whether hooks shall be used to load (and save)</code> data from (and to) the given <i>name</i> Changing hooks will not affect already opened mailboxes. For example, the following creates hooks for the <a href="/docs/linux/man/1-gzip/">gzip</a>(1) compression tool and a combined compressed and encrypted format: </p>
<blockquote><pre><code>? filetype \
    gzip 'gzip -dc' 'gzip -c' \
    zst.pgp 'gpg -d | zstd -dc' 'zstd -19 -zc | gpg -e'
</code></pre>
</blockquote>
<p> For historic reasons <code>filetype s provide limited (case-sensitive) auto-completion capabilities.</code> For example `mbox.gz&#8217; will be found for `?&#8216; file mbox , provided that corresponding handlers are installed. It will neither find `mbox.GZ&#8217; nor `mbox.Gz however, &#8216; but an explicit `?&#8216; file mbox.GZ will find and use the handler for `gz&#8217; [v15 behaviour may differ] The latter mode can only be used for MBOX files. </p>
<p> EML files consist of only one mail message, [v15 behaviour may differ] and can only be opened read-only. When reading MBOX files tolerant POSIX rules are used by default. Invalid message boundaries that can be found quite often in historic MBOX files will be complained about (even more with <i>debug )</i> in this case the method described for <i>mbox-rfc4155</i> can be used to create a valid MBOX database from the invalid input. </p>
<p> MBOX databases and EML files will always be protected via file-region locks ( <a href="/docs/linux/man/2-fcntl/">fcntl</a>(2) during file operations to protect against concurrent modifications. [Option] An MBOX <i>inbox</i> ( <code>MAIL</code> or Sx primary system mailbox will also be protected by so-called dotlock files, the traditional way of mail spool file locking: for any file `x&#8217; a lock file `x.lock&#8217; will be created during the synchronization, in the same directory and with the same user and group identities as the file of interest --- as necessary created by an external privileged dotlock helper. <i>dotlock-disable</i> disables dotlock files. Also see Sx FAQ : Sx Howto handle stale dotlock files . </p>
<p> [Option] If no protocol has been fixated, and <i>name</i> refers to a directory with the subdirectories `tmp&#8217; , `new&#8217; and `cur&#8217; , then it is treated as a folder in ``Maildir&#8217;&#8216; format. The maildir format stores each message in its own file, and has been designed so that file locking is not necessary when reading or writing files. </p>
<p> [Option]ally URLs can be used to access network resources, securely via Sx Encrypted network communication , if so supported. Network communication socket timeouts are configurable via <i>socket-connect-timeout</i> All network traffic may be proxied over a SOCKS server via <i>socks-proxy</i> </p>
<blockquote><p> <code>[v15-compat] protocol://[user[:password]@]host[:port][/path]</code> </p>
</blockquote>
<blockquote><p> <code>[no v15-compat] protocol://[user@]host[:port][/path]</code> </p>
</blockquote>
<p> [Option]ally supported network protocols are <i>pop3</i> (POP3) and <i>pop3s</i> (POP3 with TLS encrypted transport), <i>imap</i> and <i>imaps</i> The <i>[/path]</i> part is valid only for IMAP; there it defaults to <i>INBOX</i> Network URLs require a special encoding as documented in the section Sx On URL syntax and credential lookup . </p>
 </dd>
<dt><code>folders</code></dt>
<dd> <p> Lists the names of all folders below the given argument or <i>folder</i> For file-based protocols <code>LISTER</code> will be used for display purposes. </p>
 </dd>
<dt><code>Followup , followup</code></dt>
<dd> <p> (Compose mode)(F,fo) Similar to <code>Reply</code> and <code>reply</code> respectively, but save the message in a file named after the local part of the (first) recipient&#8217;s address, possibly overwriting <i>record</i> and honouring <i>outfolder</i> Also see <code>Copy</code> and <code>Save</code> </p>
 </dd>
<dt><code>Forward</code></dt>
<dd> <p> (Compose mode) Similar to <code>forward</code> but saves the message in a file named after the local part of the recipient&#8217;s address (instead of in <i>record </i><code>).</code> </p>
 </dd>
<dt><code>forward</code></dt>
<dd> <p> (Compose mode) Take a message list and the address of a recipient, subject to <i>fullnames</i> to whom the messages are sent. The text of the original message is included in the new one, enclosed by the values of <i>forward-inject-head</i> and <i>forward-inject-tail</i> <i>content-description-forwarded-message</i> is inspected. The list of included headers can be filtered with the `forward&#8217; slot of the white- and blacklisting command <code>headerpick</code> Only the first part of a multipart message is included but for <i>forward-as-attachment</i> </p>
<p> This may generate the errors <i>^ERR </i><code>-DESTADDRREQ</code> if no receiver has been specified, or was rejected by <i>expandaddr</i> policy, <i>^ERR </i><code>-IO</code> if an I/O error occurs, <i>^ERR </i><code>-NOTSUP</code> if a necessary character set conversion fails, and <i>^ERR </i><code>-INVAL</code> for other errors. It can also fail with errors of Sx Specifying messages . Any error stops processing of further messages. </p>
 </dd>
<dt><code>from</code></dt>
<dd> <p> (f) Takes a list of message specifications and displays a summary of their message headers, exactly as via <code>headers</code> making the first message of the result the new ``dot&#8217;&#8216; (the last message if <i>showlast</i> is set). An alias of this command is <code>search</code> Also see Sx Specifying messages . </p>
 </dd>
<dt><code>Fwd</code></dt>
<dd> <p> [Obsolete] Alias for <code>Forward</code> </p>
 </dd>
<dt><code>fwd</code></dt>
<dd> <p> [Obsolete] Alias for <code>forward</code> </p>
 </dd>
<dt><code>fwdignore</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>fwdretain</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>ghost , unghost</code></dt>
<dd> <p> [Obsolete] Replaced by <code>commandalias</code> <code>uncommandalias</code> </p>
 </dd>
<dt><code>headerpick , unheaderpick</code></dt>
<dd> <p> [Only new quoting rules] Multiplexer command to manage white- and blacklisting selections of header fields for a variety of applications. Without arguments the set of contexts that have settings is displayed. When given arguments, the first argument is the context to which the command applies, one of (case-insensitive) `type&#8217; for display purposes (for example <code>type )</code> `save&#8217; for selecting which headers shall be stored persistently when <code>save</code> <code>copy</code> <code>move</code> or even <code>decrypt ing messages (note that MIME related etc. header fields should not be</code> ignored in order to not destroy usability of the message in this case), `forward&#8217; for stripping down messages when <code>forward ing message (has no effect if</code> <i>forward-as-attachment</i> is set), and `top&#8217; for defining user-defined set of fields for the command <code>top</code> </p>
<p> The current settings of the given context are displayed if it is the only argument. A second argument denotes the type of restriction that is to be chosen, it may be (a case-insensitive prefix of) `retain&#8217; or `ignore&#8217; for white- and blacklisting purposes, respectively. Establishing a whitelist suppresses inspection of the corresponding blacklist. </p>
<p> If no further argument is given the current settings of the given type will be displayed, otherwise the remaining arguments specify header fields, which [Option]ally may be given as regular expressions, to be added to the given type. The special wildcard field (asterisk, `*&#8216; ) will establish a (fast) shorthand setting which covers all fields. </p>
<p> The latter command always takes three or more arguments and can be used to remove selections, i.e., from the given context, the given type of list, all the given headers will be removed, the special argument `*&#8216; will remove all headers. </p>
 </dd>
<dt><code>headers</code></dt>
<dd> <p> (h) Show the current group of headers, the size of which depends on the variable <i>screen</i> in interactive mode, and the format of which can be defined with <i>headline</i> If a message-specification is given the group of headers containing the first message therein is shown and the message at the top of the screen becomes the new ``dot&#8217;&#8216; the last message is targeted if <i>showlast</i> is set. </p>
 </dd>
<dt><code>help</code></dt>
<dd> <p> (hel) A synonym for <code>?</code> </p>
 </dd>
<dt><code>history</code></dt>
<dd> <p> [Option] Without arguments or when given <code>show</code> all history entries are shown (this mode also supports a more <i>verbose</i> output). <code>load</code> will replace the list of entries with the content of <i>history-file</i> and <code>save</code> will dump all entries to said file, replacing former content, and <code>clear</code> will delete all entries. The argument can also be a signed decimal <i>NUMBER</i> which will select and evaluate the respective history entry, and move it to the top of the history; a negative number is used as an offset to the current command so that `-1&#8217; will select the last command, the history top, whereas <code>delete</code> will delete all given entries ( <i>:NUMBER:</i> Also see Sx On terminal control and line editor . </p>
 </dd>
<dt><code>hold</code></dt>
<dd> <p> (ho, also <code>preserve</code> Takes a message list and marks each message therein to be saved in the user&#8217;s system <i>inbox</i> instead of in the Sx secondary mailbox <code>MBOX</code> Does not override the <code>delete</code> command. S-nail deviates from the POSIX standard with this command, because a <code>next</code> command issued after <code>hold</code> will display the following message, not the current one. </p>
 </dd>
<dt><code>if</code></dt>
<dd> <p> (i) Part of the <code>if , elif , else , endif</code> conditional execution construct --- if the given condition is true then the encapsulated block is executed. The POSIX standard only supports the (case-insensitive) conditions `r&#8217; Ns eceive and `s&#8217; Ns end, the remaining are non-portable extensions. [v15 behaviour may differ] In conjunction with the <code>wysh</code> command prefix(es) Sx Shell-style argument quoting and more test operators are available. </p>
<blockquote><pre><code>if receive
  commands ...
else
  commands ...
endif
</code></pre>
</blockquote>
<p> Further (case-insensitive) one-argument conditions are `t&#8217; Ns erminal which evaluates to true in interactive terminal sessions (running with standard input or standard output attached to a terminal, and none of the ``quickrun&#8217;&#8216; command line options -<code>e</code> -<code>H</code> and -<code>L</code> have been used), as well as any boolean value (see Sx INTERNAL VARIABLES for textual boolean representations) to mark an enwrapped block as ``never execute&#8217;&#8216; or ``always execute&#8217;&#8216; (Remarks: condition syntax errors skip all branches until <code>endif .</code> </p>
<p> [no v15-compat] and without <code>wysh</code> It is possible to check Sx INTERNAL VARIABLES as well as Sx ENVIRONMENT variables for existence or compare their expansion against a user given value or another variable by using the `$&#8216; ( ``variable next&#8217;&#8216; conditional trigger character; a variable on the right hand side may be signalled using the same mechanism. Variable names may be enclosed in a pair of matching braces. When this mode has been triggered, several operators are available ([v15-compat] and <code>wysh</code> they are always available, and there is no trigger: variables will have been expanded by the shell-compatible parser before the <code>if</code> etc. command sees them). </p>
<p> [v15-compat] Two argument conditions. Variables can be tested for existence and expansion: `-N&#8217; will test whether the given variable exists, so that `-N&#8217; editalong will evaluate to true when <i>editalong</i> is set, whereas `-Z&#8217; editalong will if it is not. `-n&#8217; $editalong will be true if the variable is set and expands to a non-empty string, `-z&#8217; $&#8216;\$editalong&#8217; only if the expansion is empty, whether the variable exists or not. The remaining conditions take three arguments. </p>
<p> Integer operators treat the arguments on the left and right hand side of the operator as integral numbers and compare them arithmetically. It is an error if any of the operands is not a valid integer, an empty argument (which implies it had been quoted) is treated as if it were 0. Via the question mark `?&#8216; modifier suffix a saturated operation mode is available where numbers will linger at the minimum or maximum possible value, instead of overflowing (or trapping), the keyword `saturated&#8217; is optional, `==?&#8216; , `==?satu&#8217; and `==?saturated&#8217; are therefore identical. Available operators are `-lt&#8217; (less than), `-le&#8217; (less than or equal to), `-eq&#8217; (equal), `-ne&#8217; (not equal), `-ge&#8217; (greater than or equal to), and `-gt&#8217; (greater than). </p>
<p> String and regular expression data operators compare the left and right hand side according to their textual content. Unset variables are treated as the empty string. Via the question mark `?&#8216; modifier suffix a case-insensitive operation mode is available, the keyword `case&#8217; is optional, `==?&#8216; and `==?case&#8217; are identical. </p>
<p> Available string operators are `&lt;&#8216; (less than), `&lt;=&#8216; (less than or equal to), `==&#8216; (equal), `!=&#8216; (not equal), `&gt;=&#8216; (greater than or equal to), `&gt;&#8216; (greater than), `=%&#8216; (is substring of) and `!%&#8216; (is not substring of). By default these operators work on bytes and (therefore) do not take into account character set specifics. If the case-insensitivity modifier has been used, case is ignored according to the rules of the US-ASCII encoding, i.e., bytes are still compared. </p>
<p> When the [Option]al regular expression support is available, the additional string operators `=~&#8216; and `!~&#8216; can be used. They treat the right hand side as an extended regular expression that is matched according to the active locale (see Sx Character sets ) , i.e., character sets should be honoured correctly. </p>
<p> Conditions can be joined via AND-OR lists (where the AND operator is `&amp;&amp;&#8216; and the OR operator is `||&#8216; ) , which have equal precedence and will be evaluated with left associativity, thus using the same syntax that is known for the <a href="/docs/linux/man/1-sh/">sh</a>(1). It is also possible to form groups of conditions and lists by enclosing them in pairs of brackets `[...&nbsp;] ,&#8216; which may be interlocked within each other, and also be joined via AND-OR lists. </p>
<p> The results of individual conditions and entire groups may be modified via unary operators: the unary operator `!&#8216; will reverse the result. </p>
<blockquote><pre><code>wysh set v15-compat=yes # with value: automatic &quot;wysh&quot;!
if -N debug;echo *debug* set;else;echo not;endif
if &quot;$ttycharset&quot; == UTF-8 || &quot;$ttycharset&quot; ==?cas UTF8
  echo ttycharset is UTF-8, the former case-sensitive!
endif
set t1=one t2=one
if [ &quot;${t1}&quot; == &quot;${t2}&quot; ]
  echo These two variables are equal
endif
if &quot;$features&quot; =% ,+regex, &amp;&amp; &quot;$TERM&quot; =~?case ^xterm.*
  echo ..in an X terminal
endif
if [ [ true ] &amp;&amp; [ [ &quot;${debug}&quot; != '' ] || \
    [ &quot;$verbose&quot; != '' ] ] ]
  echo Noisy, noisy
endif
if true &amp;&amp; [ -n &quot;$debug&quot; || -n &quot;${verbose}&quot; ]
  echo Left associativity, as is known from the shell
endif
</code></pre>
</blockquote>
 </dd>
<dt><code>ignore</code></dt>
<dd> <p> (ig) Identical to <code>discard</code> Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>list</code></dt>
<dd> <p> Shows the names of all available commands, in command lookup order. [Option] In conjunction with a set variable <i>verbose</i> additional information will be provided for each command: the argument type will be indicated, the documentation string will be shown, and the set of command flags will show up: </p>
 </dd>
<dl>
<dt><code>``local&#8217;&#8216; </code></dt>
<dd> <p> command supports the command modifier <code>local</code> </p>
 </dd>
<dt><code>``vput&#8217;&#8216; </code></dt>
<dd> <p> command supports the command modifier <code>vput</code> </p>
 </dd>
<dt><code>`*!*&#8216; </code></dt>
<dd> <p> the error number is tracked in <i>!</i> </p>
 </dd>
<dt><code>`needs-box&#8217; </code></dt>
<dd> <p> whether the command needs an active mailbox, a <code>folder</code> </p>
 </dd>
<dt><code>`ok:&#8216; </code></dt>
<dd> <p> indicators whether command is ... </p>
 </dd>
<dl>
<dt><code>`batch/interactive&#8217; </code></dt>
<dd> <p> usable in interactive or batch mode ( -<code>#</code> </p>
 </dd>
<dt><code>`send-mode&#8217; </code></dt>
<dd> <p> usable in send mode. </p>
 </dd>
<dt><code>`subprocess&#8217; </code></dt>
<dd> <p> allowed to be used when running in a subprocess instance, for example from within a macro that is called via <i>on-compose-splice</i> </p>
 </dd></dl>
<dt><code>`not&#8217; </code></dt>
<dd> <p> ok: indicators whether command is not ... </p>
 </dd>
<dl>
<dt><code>`compose&#8217; </code></dt>
<dd> <p> mode available in Sx Compose mode. </p>
 </dd>
<dt><code>`startup&#8217; </code></dt>
<dd> <p> available during program startup, like in Sx Resource files . </p>
 </dd></dl>
<dt><code>`gabby&#8217; </code></dt>
<dd> <p> The command produces <i>history-gabby</i> <code>history</code> entries. </p>
 </dd></dl>
<dt><code>localopts</code></dt>
<dd> <p> Enforce change localization of <code>environ</code> (linked) Sx ENVIRONMENT as well as (global) Sx INTERNAL VARIABLES , meaning that their state will be reverted to the former one once the ``covered scope&#8217;&#8216; is left. Just like the command modifier <code>local</code> which provides block-scope localization for some commands (instead), it can only be used inside of macro definition blocks introduced by <code>account</code> or <code>define</code> The covered scope of an <code>account</code> is left once a different account is activated, and some macros, notably <i>folder-hook </i><code>s</code> use their own specific notion of covered scope, here it will be extended until the folder is left again. </p>
<p> This setting stacks up: i.e., if `macro1&#8217; enables change localization and calls `macro2&#8217; , which explicitly resets localization, then any value changes within `macro2&#8217; will still be reverted when the scope of `macro1&#8217; is left. (Caveats: if in this example `macro2&#8217; changes to a different <code>account</code> which sets some variables that are already covered by localizations, their scope will be extended, and in fact leaving the <code>account</code> will (thus) restore settings in (likely) global scope which actually were defined in a local, macro private context!) </p>
<p> This command takes one or two arguments, the optional first one specifies an attribute that may be one of <code>scope</code> which refers to the current scope and is thus the default, <code>call</code> which causes any macro that is being <code>call ed to be started with localization enabled by default, as well as</code> <code>call-fixate</code> which (if enabled) disallows any called macro to turn off localization: like this it can be ensured that once the current scope regains control, any changes made in deeper levels have been reverted. The latter two are mutually exclusive, and neither affects <code>xcall</code> The (second) argument is interpreted as a boolean (string, see Sx INTERNAL VARIABLES ) and states whether the given attribute shall be turned on or off. </p>
<blockquote><pre><code>define temporary_settings {
  set possibly_global_option1
  localopts on
  set localized_option1
  set localized_option2
  localopts scope off
  set possibly_global_option2
}
</code></pre>
</blockquote>
 </dd>
<dt><code>Lfollowup , Lreply</code></dt>
<dd> <p> (Compose mode) Reply to messages that come in via known ( <code>mlist</code> or subscribed ( <code>mlsubscribe</code> mailing lists, or pretend to do so (see Sx Mailing lists ) : on top of the usual <code>followup</code> and <code>reply</code> respectively, functionality this will actively resort and even remove message recipients in order to generate a message that is supposed to be sent to a mailing list. For example it will also implicitly generate a `Mail-Followup-To:&#8216; header if that seems useful, regardless of the setting of the variable <i>followup-to</i> For more documentation please refer to Sx On sending mail, and non-interactive mode . </p>
<p> This may generate the errors <i>^ERR </i><code>-DESTADDRREQ</code> if no receiver has been specified, <i>^ERR </i><code>-PERM</code> if some addressees where rejected by <i>expandaddr</i> <i>^ERR </i><code>-IO</code> if an I/O error occurs, <i>^ERR </i><code>-NOTSUP</code> if a necessary character set conversion fails, and <i>^ERR </i><code>-INVAL</code> for other errors. It can also fail with errors of Sx Specifying messages . Occurrence of some of the errors depend on the value of <i>expandaddr</i> Any error stops processing of further messages. </p>
 </dd>
<dt><code>Mail</code></dt>
<dd> <p> (Compose mode) Similar to <code>mail</code> but saves the message in a file named after the local part of the first recipient&#8217;s address (instead of in <i>record </i><code>).</code> </p>
 </dd>
<dt><code>mail</code></dt>
<dd> <p> (Compose mode)(m) Takes a (list of) recipient address(es) as (an) argument(s), or asks on standard input if none were given; then collects the remaining mail content and sends it out. Unless the internal variable <i>fullnames</i> is set recipient addresses will be stripped from comments, names etc. For more documentation please refer to Sx On sending mail, and non-interactive mode . </p>
<p> This may generate the errors <i>^ERR </i><code>-DESTADDRREQ</code> if no receiver has been specified, <i>^ERR </i><code>-PERM</code> if some addressees where rejected by <i>expandaddr</i> <i>^ERR </i><code>-NOTSUP</code> if multiple messages have been specified, <i>^ERR </i><code>-IO</code> if an I/O error occurs, <i>^ERR </i><code>-NOTSUP</code> if a necessary character set conversion fails, and <i>^ERR </i><code>-INVAL</code> for other errors. It can also fail with errors of Sx Specifying messages . Occurrence of some of the errors depend on the value of <i>expandaddr</i> </p>
 </dd>
<dt><code>mailcap</code></dt>
<dd> <p> [Option] When used without arguments or if <i>show</i> has been given the content of Sx The Mailcap files cache is shown, (re-)initializing it first (as necessary. If the argument is <i>load</i> then the cache will only be (re-)initialized, and <i>clear</i> will remove its contents. Note that S-nail will try to load the files only once, use `<code>mailcap</code> &#8216; Ns &nbsp;clear to unlock further attempts. Loading and parsing can be made more <i>verbose</i> </p>
 </dd>
<dt><code>mbox</code></dt>
<dd> <p> (mb) The given message list is to be sent to the Sx secondary mailbox <code>MBOX</code> when S-nail is quit; this is the default action unless the variable <i>hold</i> is set. [v15 behaviour may differ] This command can only be used in a Sx primary system mailbox . </p>
 </dd>
<dt><code>mimetype , unmimetype</code></dt>
<dd> <p> [Only new quoting rules] Without arguments the content of the MIME type cache will displayed; a more verbose listing will be produced if either of <i>debug</i> or <i>verbose</i> are set. When given arguments they will be joined, interpreted as shown in Sx The mime.types files (also see Sx HTML mail and MIME attachments ) , and the resulting entry will be added (prepended) to the cache. In any event MIME type sources are loaded first as necessary - <i>mimetypes-load-control</i> can be used to fine-tune which sources are actually loaded. </p>
<p> The latter command deletes all specifications of the given MIME type, thus `?&#8216; unmimetype text/plain will remove all registered specifications for the MIME type `text/plain&#8217; The special name `*&#8216; will discard all existing MIME types, just as will `reset&#8217; , but which also reenables cache initialization via <i>mimetypes-load-control</i> </p>
 </dd>
<dt><code>mimeview</code></dt>
<dd> <p> [v15 behaviour may differ] Only available in interactive mode, this command allows execution of external MIME type handlers which do not integrate into the normal <code>type</code> output (see Sx HTML mail and MIME attachments ) . ([v15 behaviour may differ] No syntax to directly address parts, this restriction may vanish.) The user will be asked for each non-text part of the given message in turn whether the registered handler shall be used to display the part. </p>
 </dd>
<dt><code>mlist , unmlist</code></dt>
<dd> <p> [Only new quoting rules] Manage the list of known Sx Mailing lists ; subscriptions are controlled via <code>mlsubscribe</code> The latter command deletes all given arguments, or all at once when given the asterisk `*&#8216; The former shows the list of all currently known lists if used without arguments, otherwise the given arguments will become known. [Option] In the latter case, arguments which contain any of the Sx magic regular expression characters will be interpreted as one, possibly matching many addresses; these will be sequentially matched via linked lists instead of being looked up in a dictionary. </p>
 </dd>
<dt><code>mlsubscribe , unmlsubscribe</code></dt>
<dd> <p> Building upon the command pair <code>mlist , unmlist</code> but only managing the subscription attribute of mailing lists. (The former will also create not yet existing mailing lists.) </p>
 </dd>
<dt><code>Move</code></dt>
<dd> <p> Similar to <code>move</code> but move the messages to a file named after the local part of the sender of the first message instead of taking a filename argument; <i>outfolder</i> is inspected to decide on the actual storage location. </p>
 </dd>
<dt><code>move</code></dt>
<dd> <p> Acts like <code>copy</code> but marks the messages for deletion if they were transferred successfully. </p>
 </dd>
<dt><code>More</code></dt>
<dd> <p> Like <code>more</code> but also displays header fields which would not pass the <code>headerpick</code> selection, and all MIME parts. Identical to <code>Page</code> </p>
 </dd>
<dt><code>more</code></dt>
<dd> <p> Invokes the <code>PAGER</code> on the given messages, even in non-interactive mode and as long as the standard output is a terminal. Identical to <code>page</code> </p>
 </dd>
<dt><code>mtaaliases</code></dt>
<dd> <p> [Option] When used without arguments or if <i>show</i> has been given the content of the <i>mta-aliases</i> cache is shown, (re-)initializing it first (as necessary). If the argument is <i>load</i> then the cache will only be (re-)initialized, and <i>clear</i> will remove its contents. </p>
 </dd>
<dt><code>netrc</code></dt>
<dd> <p> [Option] When used without arguments, or when the argument was <i>show</i> the content of the ~/.netrc cache is shown, initializing it as necessary. If the argument is <i>load</i> then the cache will be (re)loaded, whereas <i>clear</i> removes it. Loading and parsing can be made more <i>verbose</i> <i>lookup</i> will query the cache for the URL given as the second argument ( `[USER@]HOST&#8217; ). See <i>netrc-lookup</i> <i>netrc-pipe</i> and the section Sx On URL syntax and credential lookup ; the section Sx The .netrc file documents the file format in detail. </p>
 </dd>
<dt><code>newmail</code></dt>
<dd> <p> Checks for new mail in the current folder without committing any changes before. If new mail is present, a message is shown. If the <i>header</i> variable is set, the headers of each new message are also shown. This command is not available for all mailbox types. </p>
 </dd>
<dt><code>next</code></dt>
<dd> <p> (n) (like `+&#8216; or ``ENTER&#8217;&#8216; Goes to the next message in sequence and types it. With an argument list, types the next matching message. </p>
 </dd>
<dt><code>New</code></dt>
<dd> <p> Same as <code>Unread</code> </p>
 </dd>
<dt><code>new</code></dt>
<dd> <p> Same as <code>unread</code> </p>
 </dd>
<dt><code>noop</code></dt>
<dd> <p> If the current folder is accessed via a network connection, a ``NOOP&#8217;&#8216; command is sent, otherwise no operation is performed. </p>
 </dd>
<dt><code>Page</code></dt>
<dd> <p> Like <code>page</code> but also displays header fields which would not pass the <code>headerpick</code> selection, and all MIME parts. Identical to <code>More</code> </p>
 </dd>
<dt><code>page</code></dt>
<dd> <p> Invokes the <code>PAGER</code> on the given messages, even in non-interactive mode and as long as the standard output is a terminal. Identical to <code>more</code> </p>
 </dd>
<dt><code>Pipe</code></dt>
<dd> <p> Like <code>pipe</code> but also pipes header fields which would not pass the <code>headerpick</code> selection, and all parts of MIME `multipart/alternative&#8217; messages. </p>
 </dd>
<dt><code>pipe</code></dt>
<dd> <p> (pi) Takes an optional message list and shell command (that defaults to <i>cmd )</i> and pipes the messages through the command. If the <i>page</i> variable is set, every message is followed by a formfeed character. </p>
 </dd>
<dt><code>preserve</code></dt>
<dd> <p> (pre) A synonym for <code>hold</code> </p>
 </dd>
<dt><code>Print</code></dt>
<dd> <p> (P) Alias for <code>Type</code> </p>
 </dd>
<dt><code>print</code></dt>
<dd> <p> (p) Research UNIX equivalent of <code>type</code> </p>
 </dd>
<dt><code>quit</code></dt>
<dd> <p> (q) Terminates the session, saving all undeleted, unsaved messages in the current Sx secondary mailbox <code>MBOX</code> preserving all messages marked with <code>hold</code> or <code>preserve</code> or never referenced in the system <i>inbox</i> and removing all other messages from the Sx primary system mailbox . If new mail has arrived during the session, the message ``You have new mail&#8217;&#8216; will be shown. If given while editing a mailbox file with the command line option -<code>f</code> then the edit file is rewritten. A return to the shell is effected, unless the rewrite of edit file fails, in which case the user can escape with the exit command. The optional status number argument will be passed through to <a href="/docs/linux/man/3-exit/">exit</a>(3). [v15 behaviour may differ] For now it can happen that the given status will be overwritten, later this will only occur if a later error needs to be reported onto an otherwise success indicating status. </p>
 </dd>
<dt><code>read</code></dt>
<dd> <p> [Only new quoting rules] Read a line from standard input, or the channel set active via <code>readctl</code> and assign the data, which will be split as indicated by <i>ifs</i> to the given variables. The variable names are checked by the same rules as documented for <code>vput</code> and the same error codes will be seen in <i>!</i> the exit status <i>?</i> indicates the number of bytes read, it will be `-1&#8217; with the error number <i>!</i> set to <i>^ERR </i><code>-BADF</code> in case of I/O errors, or <i>^ERR </i><code>-NONE</code> upon End-Of-File. If there are more fields than variables, assigns successive fields to the last given variable. If there are less fields than variables, assigns the empty string to the remains. </p>
<blockquote><pre><code>? read a b c
   H e l l o
? echo &quot;&lt;$a&gt; &lt;$b&gt; &lt;$c&gt;&quot;
&lt;H&gt; &lt;e&gt; &lt;l l o&gt;
? wysh set ifs=:; read a b c;unset ifs
hey2.0,:&quot;'you &quot;,:world!:mars.:
? echo $?/$^ERRNAME / &lt;$a&gt;&lt;$b&gt;&lt;$c&gt;
0/NONE / &lt;hey2.0,&gt;&lt;&quot;'you &quot;,&gt;&lt;world!:mars.:&gt;&lt;&gt;&lt;&gt;
</code></pre>
</blockquote>
 </dd>
<dt><code>readsh</code></dt>
<dd> <p> [Only new quoting rules] Like <code>read</code> but splits on shell token boundaries (see Sx Shell-style argument quoting ) rather than at <i>ifs</i> [v15 behaviour may differ] Could become a <code>commandalias</code> maybe `read&#8217; --tokenize -- . </p>
 </dd>
<dt><code>readall</code></dt>
<dd> <p> [Only new quoting rules] Read anything from standard input, or the channel set active via <code>readctl</code> and assign the data to the given variable. The variable name is checked by the same rules as documented for <code>vput</code> and the same error codes will be seen in <i>!</i> the exit status <i>?</i> indicates the number of bytes read, it will be `-1&#8217; with the error number <i>!</i> set to <i>^ERR </i><code>-BADF</code> in case of I/O errors, or <i>^ERR </i><code>-NONE</code> upon End-Of-File. [v15 behaviour may differ] The input data length is restricted to 31-bits. </p>
 </dd>
<dt><code>readctl</code></dt>
<dd> <p> [Only new quoting rules] Manages input channels for <code>read</code> <code>readsh</code> and <code>readall</code> to be used to avoid complicated or impracticable code, like calling <code>read</code> from within a macro in non-interactive mode. Without arguments, or when the first argument is <code>show</code> a listing of all known channels is printed. Channels can otherwise be <code>create d, and existing channels can be</code> <code>set</code> active and <code>remove d by giving the string used for creation.</code> </p>
<p> The channel name is expected to be a file descriptor number, or, if parsing the numeric fails, an input file name that undergoes Sx Filename transformations . For example (this example requires a modern shell): </p>
<blockquote><pre><code>$ printf 'echon &quot;hey, &quot;\nread a\nyou\necho $a' |\
  s-nail -R#
hey, you
$ LC_ALL=C printf 'echon &quot;hey, &quot;\nread a\necho $a' |\
  LC_ALL=C 6&lt;&lt;&lt; 'you' s-nail -R#X'readctl create 6'
hey, you
</code></pre>
</blockquote>
 </dd>
<dt><code>remove</code></dt>
<dd> <p> [Only new quoting rules] Removes the named files or directories. If a name refers to a mailbox, say a Maildir mailbox, then a mailbox type specific removal will be performed, deleting the complete mailbox. In interactive mode the user is asked for confirmation. </p>
 </dd>
<dt><code>rename</code></dt>
<dd> <p> [Only new quoting rules] Takes the name of an existing folder and the name for the new folder and renames the first to the second one. Sx Filename transformations including shell pathname wildcard pattern expansions ( <a href="/docs/linux/man/7-glob/">glob</a>(7) are performed on both arguments. Both folders must be of the same type. </p>
 </dd>
<dt><code>Reply , Respond</code></dt>
<dd> <p> (Compose mode)(R) Identical to <code>reply</code> except that it replies to only the sender of each message of the given list, by using the first message as the template to quote, for the `Subject:&#8216; etc.; setting <i>flipr</i> will exchange this command with <code>reply</code> </p>
 </dd>
<dt><code>reply , respond</code></dt>
<dd> <p> (Compose mode)(r) Take a message (list) and group-respond (to each in turn) by addressing the sender and all recipients, subject to <i>fullnames</i> and <code>alternates</code> processing. <i>followup-to</i> <i>followup-to-honour</i> <i>reply-to-honour</i> as well as <i>recipients-in-cc</i> influence response behaviour. <i>quote</i> as well as <i>quote-as-attachment</i> configure whether responded-to message shall be quoted etc., <i>content-description-quote-attachment</i> may be used. Setting <i>flipr</i> will exchange this command with <code>Reply</code> The command <code>Lreply</code> offers special support for replying to mailing lists. For more documentation please refer to Sx On sending mail, and non-interactive mode . </p>
<p> This may generate the errors <i>^ERR </i><code>-DESTADDRREQ</code> if no receiver has been specified, or was rejected by <i>expandaddr</i> policy, <i>^ERR </i><code>-IO</code> if an I/O error occurs, <i>^ERR </i><code>-NOTSUP</code> if a necessary character set conversion fails, and <i>^ERR </i><code>-INVAL</code> for other errors. It can also fail with errors of Sx Specifying messages . Any error stops processing of further messages. </p>
 </dd>
<dt><code>Resend</code></dt>
<dd> <p> Like <code>resend</code> but does not add any header lines. This is not a way to hide the sender&#8217;s identity, but useful for sending a message again to the same recipients. </p>
 </dd>
<dt><code>resend</code></dt>
<dd> <p> Takes a list of messages and a name, and sends each message to the given addressee, which is subject to <i>fullnames</i> `Resent-From:&#8216; and related header fields are prepended to the new copy of the message. Saving in <i>record</i> is only performed if <i>record-resent</i> is set. [v15 behaviour may differ](Compose mode) is not entered, the only supported hooks are <i>on-resend-enter</i> and <i>on-resend-cleanup</i> </p>
<p> This may generate the errors <i>^ERR </i><code>-DESTADDRREQ</code> if no receiver has been specified, or was rejected by <i>expandaddr</i> policy, <i>^ERR </i><code>-IO</code> if an I/O error occurs, <i>^ERR </i><code>-NOTSUP</code> if a necessary character set conversion fails, and <i>^ERR </i><code>-INVAL</code> for other errors. It can also fail with errors of Sx Specifying messages . Any error stops processing of further messages. </p>
 </dd>
<dt><code>retain</code></dt>
<dd> <p> (ret) Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>return</code></dt>
<dd> <p> Only available inside of a <code>define d macro or an</code> <code>account</code> this command returns control of execution to the outer scope. The two optional parameters are positive decimal numbers and default to 0: the first specifies the 32-bit return value (stored in <i>?</i> [v15 behaviour may differ] and later extended to 64-bit), the second the 32-bit error number (stored in <i>! )</i> As documented for <i>?</i> a non-0 exit status may cause the program to exit. </p>
 </dd>
<dt><code>Save</code></dt>
<dd> <p> (S) Similar to <code>save,</code> but saves the messages in a file named after the local part of the sender of the first message instead of taking a filename argument; <i>outfolder</i> is inspected to decide on the actual storage location. </p>
 </dd>
<dt><code>save</code></dt>
<dd> <p> (s) Takes a message list and a filename and appends each message in turn to the end of the file. Sx Filename transformations including shell pathname wildcard pattern expansions ( <a href="/docs/linux/man/7-glob/">glob</a>(7) is performed on the filename. If no filename is given, the Sx secondary mailbox <code>MBOX</code> is used. The filename in quotes, followed by the generated character count is echoed on the user&#8217;s terminal. If editing a Sx primary system mailbox the messages are marked for deletion. To filter the saved header fields to the desired subset use the `save&#8217; slot of the white- and blacklisting command <code>headerpick</code> Also see <code>Copy</code> </p>
 </dd>
<dt><code>savediscard</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>saveignore</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>saveretain</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>search</code></dt>
<dd> <p> Takes a message specification (list) and displays a header summary of all matching messages, as via <code>headers</code> This command is an alias of <code>from</code> Also see Sx Specifying messages . </p>
 </dd>
<dt><code>seen</code></dt>
<dd> <p> Takes a message list and marks all messages as having been read. </p>
 </dd>
<dt><code>set , unset</code></dt>
<dd> <p> (se, [Only new quoting rules] uns) The latter command will delete all given global variables, or only block-scope local ones if the <code>local</code> command modifier has been used. The former, when used without arguments, will show all currently known variables, being more verbose if either of <i>debug</i> or <i>verbose</i> is set. Remarks: this list mode will not automatically link-in (known) Sx ENVIRONMENT variables, this only happens for explicit addressing, examples are <code>varshow</code> using a variable in an <code>if</code> condition or a string passed to <code>echo</code> explicit <code>set ting, as well as some program-internal use cases (look-ups).</code> </p>
<p> Otherwise the given variables (and arguments) are set or adjusted. Arguments are of the form `name=value&#8217; (no space before or after `=&#8216; ) , or plain `name&#8217; if there is no value, i.e., a boolean variable. If a name begins with `no&#8217; , as in `set&#8217; nosave , the effect is the same as invoking the <code>unset</code> command with the remaining part of the variable ( `unset&#8217; save ). [v15 behaviour may differ] In conjunction with the <code>wysh</code> (or&nbsp; <code>local</code> command prefix(es) Sx Shell-style argument quoting can be used to quote arguments as necessary. [v15 behaviour may differ] Otherwise quotation marks may be placed around any part of the assignment statement to quote blanks or tabs. </p>
<p> When operating in global scope any `name&#8217; that is known to map to an environment variable will automatically cause updates in the program environment (unsetting a variable in the environment requires corresponding system support) --- use the command <code>environ</code> for further environmental control. If the command modifier <code>local</code> has been used to enforce local scoping then the given user variables will be garbage collected when the local scope is left; for Sx INTERNAL VARIABLES , however, <code>local</code> behaves the same as if <code>localopts</code> would have been set (temporarily), which means that changes are inherited by deeper scopes. Also see <code>varshow</code> and the sections Sx INTERNAL VARIABLES and Sx ENVIRONMENT . </p>
<blockquote><pre><code>? wysh set indentprefix=' -&gt; '
? wysh set atab=$' ' aspace=' ' zero=0
</code></pre>
</blockquote>
 </dd>
<dt><code>shcodec</code></dt>
<dd> <p> Apply shell quoting rules to the given raw-data arguments. Supports <code>vput</code> (see Sx Command modifiers ) . The first argument specifies the operation: <i>[+]e[ncode]</i> or <i>d[ecode]</i> cause shell quoting to be applied to the remains of the line, and expanded away thereof, respectively. If the former is prefixed with a plus-sign, the quoted result will not be roundtrip enabled, and thus can be decoded only in the very same environment that was used to perform the encode; also see <code>mle-quote-rndtrip</code> If the coding operation fails the error number <i>!</i> is set to <i>^ERR </i><code>-CANCELED</code> and the unmodified input is used as the result; the error number may change again due to output or result storage errors. </p>
 </dd>
<dt><code>shell</code></dt>
<dd> <p> [Only new quoting rules] (sh) Invokes an interactive version of the shell, and returns its exit status. </p>
 </dd>
<dt><code>shortcut , unshortcut</code></dt>
<dd> <p> [Only new quoting rules] Manage the file- or pathname shortcuts as documented for <code>folder</code> The latter command deletes all shortcuts given as arguments, or all at once when given the asterisk `*&#8216; The former shows the list of all currently defined shortcuts if used without arguments, the target of the given with a single argument. Otherwise arguments are treated as pairs of shortcuts and their desired expansion, creating new or updating already existing ones. </p>
 </dd>
<dt><code>shift</code></dt>
<dd> <p> [Only new quoting rules] Shift the positional parameter stack (starting at <i>1</i> by the given number (which must be a positive decimal), or 1 if no argument has been given. It is an error if the value exceeds the number of positional parameters. If the given number is 0, no action is performed, successfully. The stack as such can be managed via <code>vpospar</code> Note this command will fail in <code>account</code> and hook macros unless the positional parameter stack has been explicitly created in the current context via <code>vpospar</code> </p>
 </dd>
<dt><code>show</code></dt>
<dd> <p> Like <code>type</code> but performs neither MIME decoding nor decryption, so that the raw message text is shown. </p>
 </dd>
<dt><code>size</code></dt>
<dd> <p> (si) Shows the size in characters of each message of the given message list. </p>
 </dd>
<dt><code>sleep</code></dt>
<dd> <p> [Only new quoting rules] Sleep for the specified number of seconds (and optionally milliseconds), by default interruptible. If a third argument is given the sleep will be uninterruptible, otherwise the error number <i>!</i> will be set to <i>^ERR </i><code>-INTR</code> if the sleep has been interrupted. The command will fail and the error number will be <i>^ERR </i><code>-OVERFLOW</code> if the given duration(s) overflow the time datatype, and <i>^ERR </i><code>-INVAL</code> if the given durations are no valid integers. </p>
 </dd>
<dt><code>sort , unsort</code></dt>
<dd> <p> The latter command disables sorted or threaded mode, returns to normal message order and, if the <i>header</i> variable is set, displays a header summary. The former command shows the current sorting criterion when used without an argument, but creates a sorted representation of the current folder otherwise, and changes the <code>next</code> command and the addressing modes such that they refer to messages in the sorted order. Message numbers are the same as in regular mode. If the <i>header</i> variable is set, a header summary in the new order is also displayed. Automatic folder sorting can be enabled by setting the <i>autosort</i> variable, as in `set&#8217; autosort=thread . Possible sorting criterions are: </p>
 </dd>
<dl>
<dt><i>date</i></dt>
<dd> <p> Sort the messages by their `Date:&#8216; field, that is by the time they were sent. </p>
 </dd>
<dt><i>from</i></dt>
<dd> <p> Sort messages by the value of their `From:&#8216; field, that is by the address of the sender. If the <i>showname</i> variable is set, the sender&#8217;s real name (if any) is used. </p>
 </dd>
<dt><i>size</i></dt>
<dd> <p> Sort the messages by their size. </p>
 </dd>
<dt><code>spam</code></dt>
<dd> <p> [Option] Sort the message by their spam score, as has been classified by <code>spamrate</code> </p>
 </dd>
<dt><i>status</i></dt>
<dd> <p> Sort the messages by their message status. </p>
 </dd>
<dt><i>subject</i></dt>
<dd> <p> Sort the messages by their subject. </p>
 </dd>
<dt><i>thread</i></dt>
<dd> <p> Create a threaded display. </p>
 </dd>
<dt><i>to</i></dt>
<dd> <p> Sort messages by the value of their `To:&#8216; field, that is by the address of the recipient. If the <i>showname</i> variable is set, the recipient&#8217;s real name (if any) is used. </p>
 </dd></dl>
<dt><code>source</code></dt>
<dd> <p> [Only new quoting rules] (so) The source command reads commands from the given file. Sx Filename transformations will be applied. If the given expanded argument ends with a vertical bar `|&#8216; then the argument will instead be interpreted as a shell command and S-nail will read the output generated by it. Dependent on the settings of <i>posix</i> and <i>errexit</i> and also dependent on whether the command modifier <code>ignerr</code> had been used, encountering errors will stop sourcing of the given input. [v15 behaviour may differ] Note that <code>source</code> cannot be used from within macros that execute as <i>folder-hook </i><code>s</code> or <code>account s</code> i.e., it can only be called from macros that were <code>call ed</code> </p>
 </dd>
<dt><code>source_if</code></dt>
<dd> <p> [Only new quoting rules] The difference to <code>source</code> (beside not supporting pipe syntax aka shell command input) is that this command will not generate an error nor warn if the given file argument cannot be opened successfully. </p>
 </dd>
<dt><code>spamclear</code></dt>
<dd> <p> [Option] Takes a list of messages and clears their `is-spam&#8217; flag. </p>
 </dd>
<dt><code>spamforget</code></dt>
<dd> <p> [Option] Takes a list of messages and causes the <i>spam-interface</i> to forget it has ever used them to train its Bayesian filter. Unless otherwise noted the `is-spam&#8217; flag of the message is inspected to chose whether a message shall be forgotten to be ``ham&#8217;&#8216; or ``spam&#8217;&#8216; </p>
 </dd>
<dt><code>spamham</code></dt>
<dd> <p> [Option] Takes a list of messages and informs the Bayesian filter of the <i>spam-interface</i> that they are ``ham&#8217;&#8216; This also clears the `is-spam&#8217; flag of the messages in question. </p>
 </dd>
<dt><code>spamrate</code></dt>
<dd> <p> [Option] Takes a list of messages and rates them using the configured <i>spam-interface</i> without modifying the messages, but setting their `is-spam&#8217; flag as appropriate; because the spam rating headers are lost the rate will be forgotten once the mailbox is left. Refer to the manual section Sx Handling spam for the complete picture of spam handling in S-nail. </p>
 </dd>
<dt><code>spamset</code></dt>
<dd> <p> [Option] Takes a list of messages and sets their `is-spam&#8217; flag. </p>
 </dd>
<dt><code>spamspam</code></dt>
<dd> <p> [Option] Takes a list of messages and informs the Bayesian filter of the <i>spam-interface</i> that they are ``spam&#8217;&#8216; This also sets the `is-spam&#8217; flag of the messages in question. </p>
 </dd>
<dt><code>thread</code></dt>
<dd> <p> [Obsolete] The same as `sort&#8217; thread (consider using a `commandalias&#8217; as necessary). </p>
 </dd>
<dt><code>tls</code></dt>
<dd> <p> [Only new quoting rules] TLS information and management command multiplexer to aid in Sx Encrypted network communication , mostly available only if the term `,+sockets,&#8216; is included in <i>features</i> Commands support <code>vput</code> if so documented (see Sx Command modifiers ) . The result that is shown in case of errors is always the empty string, errors can be identified via the error number <i>!</i> For example, string length overflows are caught and set <i>!</i> to <i>^ERR </i><code>-OVERFLOW</code> The TLS configuration is honoured, especially <i>tls-verify</i> </p>
<blockquote><pre><code>? vput tls result fingerprint pop3s://ex.am.ple
? echo $?/$!/$^ERRNAME: $result
</code></pre>
</blockquote>
 </dd>
<dl>
<dt><code>certchain</code></dt>
<dd> <p> Show the complete verified peer certificate chain. Includes informational fields in conjunction with <i>verbose</i> </p>
 </dd>
<dt><code>certificate</code></dt>
<dd> <p> Show only the peer certificate, without any signers. Includes informational fields in conjunction with <i>verbose</i> </p>
 </dd>
<dt><code>fingerprint</code></dt>
<dd> <p> Show the <i>tls-fingerprint-digest </i><code>ed fingerprint of the certificate of the given HOST</code> ( `server:port&#8217; where the port defaults to the HTTPS port, 443). <i>tls-fingerprint</i> is actively ignored for the runtime of this command. </p>
 </dd></dl>
<dt><code>Top</code></dt>
<dd> <p> Like <code>top</code> but always uses the <code>headerpick</code> `type&#8217; slot for white- and blacklisting header fields. </p>
 </dd>
<dt><code>top</code></dt>
<dd> <p> (to) Takes a message list and types out the first <i>toplines</i> lines of each message on the user&#8217;s terminal. Unless a special selection has been established for the `top&#8217; slot of the <code>headerpick</code> command, the only header fields that are displayed are `From:&#8216; , `To:&#8216; , `Cc:&#8216; , and `Subject:&#8216; <code>Top</code> will always use the `type&#8217; <code>headerpick</code> selection instead. It is possible to apply compression to what is displayed by setting <i>topsqueeze</i> Messages are decrypted and converted to the terminal character set if necessary. </p>
 </dd>
<dt><code>touch</code></dt>
<dd> <p> (tou) Takes a message list and marks the messages for saving in the Sx secondary mailbox <code>MBOX</code> S-nail deviates from the POSIX standard with this command, as a following <code>next</code> command will display the following message instead of the current one. </p>
 </dd>
<dt><code>Type</code></dt>
<dd> <p> (T) Like <code>type</code> but also displays header fields which would not pass the <code>headerpick</code> selection, and all visualizable parts of MIME `multipart/alternative&#8217; messages. </p>
 </dd>
<dt><code>type</code></dt>
<dd> <p> (t) Takes a message list and types out each message on the user&#8217;s terminal. The display of message headers is selectable via <code>headerpick</code> For MIME multipart messages, all parts with a content type of `text&#8217; , all parts which have a registered MIME type handler (see Sx HTML mail and MIME attachments ) which produces plain text output, and all `message&#8217; parts are shown, others are hidden except for their headers. Messages are decrypted and converted to the terminal character set if necessary. The command <code>mimeview</code> can be used to display parts which are not displayable as plain text. </p>
 </dd>
<dt><code>unaccount</code></dt>
<dd> <p> See <code>account</code> </p>
 </dd>
<dt><code>unalias</code></dt>
<dd> <p> (una) See <code>alias</code> </p>
 </dd>
<dt><code>unanswered</code></dt>
<dd> <p> See <code>answered</code> </p>
 </dd>
<dt><code>unbind</code></dt>
<dd> <p> See <code>bind</code> </p>
 </dd>
<dt><code>uncollapse</code></dt>
<dd> <p> See <code>collapse</code> </p>
 </dd>
<dt><code>uncolour</code></dt>
<dd> <p> See <code>colour</code> </p>
 </dd>
<dt><code>undefine</code></dt>
<dd> <p> See <code>define</code> </p>
 </dd>
<dt><code>undelete</code></dt>
<dd> <p> See <code>delete</code> </p>
 </dd>
<dt><code>undraft</code></dt>
<dd> <p> See <code>draft</code> </p>
 </dd>
<dt><code>unflag</code></dt>
<dd> <p> See <code>flag</code> </p>
 </dd>
<dt><code>unfwdignore</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>unfwdretain</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>unignore</code></dt>
<dd> <p> Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>unmimetype</code></dt>
<dd> <p> See <code>mimetype</code> </p>
 </dd>
<dt><code>unmlist</code></dt>
<dd> <p> See <code>mlist</code> </p>
 </dd>
<dt><code>unmlsubscribe</code></dt>
<dd> <p> See <code>mlsubscribe</code> </p>
 </dd>
<dt><code>Unread</code></dt>
<dd> <p> Same as <code>unread</code> </p>
 </dd>
<dt><code>unread</code></dt>
<dd> <p> Takes a message list and marks each message as not having been read. </p>
 </dd>
<dt><code>unretain</code></dt>
<dd> <p> Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>unsaveignore</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>unsaveretain</code></dt>
<dd> <p> [Obsolete] Superseded by the multiplexer <code>headerpick</code> </p>
 </dd>
<dt><code>unset</code></dt>
<dd> <p> [Only new quoting rules] (uns) See <code>set</code> </p>
 </dd>
<dt><code>unshortcut</code></dt>
<dd> <p> See <code>shortcut</code> </p>
 </dd>
<dt><code>unsort</code></dt>
<dd> <p> See <code>short</code> </p>
 </dd>
<dt><code>unthread</code></dt>
<dd> <p> [Obsolete] Same as <code>unsort</code> </p>
 </dd>
<dt><code>urlcodec</code></dt>
<dd> <p> Perform URL percent codec operations on the raw-data argument, rather according to RFC 3986. The first argument specifies the operation: <i>e[ncode]</i> or <i>d[ecode]</i> perform plain URL percent en- and decoding, respectively. <i>p[ath]enc[ode]</i> and <i>p[ath]dec[ode]</i> perform a slightly modified operation which should be better for pathnames: it does not allow a tilde `~&#8216; , and will neither accept hyphen-minus `-&#8216; nor dot `.&#8216; as an initial character. The remains of the line form the URL data which is to be converted. This is a character set agnostic operation, and it may thus decode bytes which are invalid in the current <i>ttycharset</i> </p>
<p> Supports <code>vput</code> (see Sx Command modifiers ) , and manages the error number <i>!</i> If the coding operation fails the error number <i>!</i> is set to <i>^ERR </i><code>-CANCELED</code> and the unmodified input is used as the result; the error number may change again due to output or result storage errors. [v15 behaviour may differ] This command does not know about URLs beside what is documented. ( <code>vexpr</code> offers a <code>makeprint</code> subcommand, shall the URL be displayed.) </p>
 </dd>
<dt><code>varshow</code></dt>
<dd> <p> [Only new quoting rules] This command produces the same output as the listing mode of <code>set</code> including <i>verbose </i><code>ity adjustments, but only for the given variables.</code> </p>
 </dd>
<dt><code>verify</code></dt>
<dd> <p> [Option] Takes a message list and verifies each message. If a message is not a S/MIME signed message, verification will fail for it. The verification process checks if the message was signed using a valid certificate, if the message sender&#8217;s email address matches one of those contained within the certificate, and if the message content has been altered. </p>
 </dd>
<dt><code>version</code></dt>
<dd> <p> Shows the <i>version</i> and <i>features</i> of S-nail, optionally in a more <i>verbose</i> form which also includes the build and running system environment. This command supports <code>vput</code> (see Sx Command modifiers ) . </p>
 </dd>
<dt><code>vexpr</code></dt>
<dd> <p> [Only new quoting rules] A multiplexer command which offers signed 64-bit numeric calculations, as well as other, mostly string-based operations. C-style byte string operations are available via <code>csop</code> The first argument defines the number, type, and meaning of the remaining arguments. An empty number argument is treated as 0. Supports <code>vput</code> (see Sx Command modifiers ) . The result shown in case of errors is `-1&#8217; for usage errors and numeric operations, the empty string otherwise; ``soft&#8217;&#8216; errors, like when a search operation failed, will also set the <i>!</i> error number to <i>^ERR </i><code>-NODATA</code> Except when otherwise noted numeric arguments are parsed as signed 64-bit numbers, and errors will be reported in the error number <i>!</i> as the numeric error <i>^ERR </i><code>-RANGE</code> </p>
<p> Numeric operations work on one or two signed 64-bit integers. Numbers prefixed with `0x&#8217; or `0X&#8217; are interpreted as hexadecimal (base 16) numbers, whereas `0&#8217; indicates octal (base 8), and `0b&#8217; as well as `0B&#8217; denote binary (base 2) numbers. It is possible to use any base in between 2 and 36, inclusive, with the `BASE#number&#8217; notation, where the base is given as an unsigned decimal number, so `16#AFFE&#8217; is a different way of specifying a hexadecimal number. Unsigned interpretation of a number can be enforced by prefixing an `u&#8217; (case-insensitively), as in `u-110&#8217; ; this is not necessary for power-of-two bases (2, 4, 8, 16 and 32), which will be interpreted as unsigned by default, but it still makes a difference regarding overflow detection and overflow constant. It is possible to enforce signed interpretation by (instead) prefixing a `s&#8217; (case-insensitively). The number sign notation uses a permissive parse mode and as such supports complicated conditions out of the box: </p>
<blockquote><pre><code>? wysh set ifs=:;read i;unset ifs;echo $i;vexpr pb 2 10#$i
   -009
&lt; -009&gt;
0b1001
</code></pre>
</blockquote>
<p> One integer is expected by assignment (equals sign `=&#8216; ) , which does nothing but parsing the argument, thus detecting validity and possible overflow conditions, unary not (tilde `~&#8216; ) , which creates the bitwise complement, and unary plus and minus. Two integers are used by addition (plus sign `+&#8216; ) , subtraction (hyphen-minus `-&#8216; ) , multiplication (asterisk `*&#8216; ) , division (solidus `/&#8216; ) and modulo (percent sign `%&#8216; ) , as well as for the bitwise operators logical or (vertical bar `|&#8216; , to be quoted) , bitwise and (ampersand `&amp;&#8216; , to be quoted) , bitwise xor (circumflex `^&#8216; ) , the bitwise signed left- and right shifts ( `&lt;&lt;&#8216; `&gt;&gt;&#8216; ) , as well as for the unsigned right shift `&gt;&gt;&gt;&#8216; </p>
<p> Another numeric operation is <code>pbase</code> which takes a number base in between 2 and 36, inclusive, and will act on the second number given just the same as what equals sign `=&#8216; does, but the number result will be formatted in the base given, as a signed 64-bit number unless unsigned interpretation of the input number had been forced (with an u prefix). </p>
<p> Numeric operations support a saturated mode via the question mark `?&#8216; modifier suffix; the keyword `saturated&#8217; is optional, `+?&#8216; , `+?satu&#8217; , and `+?saturated&#8217; are therefore identical. In saturated mode overflow errors and division and modulo by zero are no longer reported via the exit status, but the result will linger at the minimum or maximum possible value, instead of overflowing (or trapping). This is true also for the argument parse step. For the bitwise shifts, the saturated maximum is 63. Any caught overflow will be reported via the error number <i>!</i> as <i>^ERR </i><code>-OVERFLOW</code> </p>
<blockquote><pre><code>? vput vexpr res -? +1 -9223372036854775808
? echo $?/$!/$^ERRNAME:$res
0/75/OVERFLOW:-9223372036854775808
</code></pre>
</blockquote>
<p> Character set agnostic string functions have no notion of locale settings and character sets. </p>
 </dd>
<dl>
<dt><code>date-utc</code></dt>
<dd> <p> Outputs the current date and time in UTC (Coordinated Universal Time) with values named such that `vput&#8217; vexpr x date-utc; eval wysh set $x creates accessible variables. </p>
 </dd>
<dt><code>date-stamp-utc</code></dt>
<dd> <p> Outputs a RFC 3339 internet date/time format of UTC. </p>
 </dd>
<dt><code>epoch</code></dt>
<dd> <p> The seconds and nanoseconds since the Unix epoch (1970-01-01T00:00:00) named `epoch_sec&#8217; and `epoch_nsec&#8217; such that `vput&#8217; vexpr x epoch; eval wysh set $x creates accessible variables. </p>
 </dd>
<dt><code>file-expand</code></dt>
<dd> <p> Performs the usual Sx Filename transformations on its argument. </p>
 </dd>
<dt><code>file-stat , file-lstat</code></dt>
<dd> <p> Perform the usual Sx Filename transformations on the argument, then call <a href="/docs/linux/man/2-stat/">stat</a>(2) and <a href="/docs/linux/man/2-lstat/">lstat</a>(2), respectively, and output values such that `vput&#8217; vexpr x file-stat FILE; eval wysh set $x creates accessible variables. The variable `st_type&#8217; uses solidus `/&#8216; to denote directories, commercial at `@&#8216; for links, number sign `#&#8216; for block devices, percent sign `%&#8216; for for character devices, vertical bar `|&#8216; for FIFOs, equal sign `=&#8216; for sockets, and the period `.&#8216; for the rest. </p>
 </dd>
<dt><code>random</code></dt>
<dd> <p> Generates a random string of the given length, or of <code>PATH_MAX</code> bytes (a constant from /usr/include if the value 0 is given; the random string will be base64url encoded according to RFC 4648, and thus be usable as a (portable) filename. </p>
 </dd></dl>
<p> String operations work, sufficient support provided, according to the active user&#8217;s locale encoding and character set (see Sx Character sets ) . Where the question mark `?&#8216; modifier suffix is supported, a case-insensitive operation mode is available; the keyword `case&#8217; is optional, `regex?&#8216; and `regex?case&#8217; are therefore identical. </p>
<dl>
<dt><code>makeprint</code></dt>
<dd> <p> (One-way) Converts the argument to something safely printable on the terminal. </p>
 </dd>
<dt><code>regex</code></dt>
<dd> <p> [Option] A string operation that will try to match the first argument with the regular expression given as the second argument. `?&#8216; modifier suffix is supported. If the optional third argument has been given then instead of showing the match offset a replacement operation is performed: the third argument is treated as if specified within dollar-single-quote (see Sx Shell-style argument quoting ) , and any occurrence of a positional parameter, for example <i>0 , 1</i> etc. is replaced with the according match group of the regular expression: </p>
<blockquote><pre><code>? vput vexpr res regex bananarama \
    (.*)NanA(.*) '\${1}au\$2'
? echo $?/$!/$^ERRNAME:$res:
1/61/NODATA::
? vput vexpr res regex?case bananarama \
    (.*)NanA(.*) '\${1}uauf\$2'
? echo $?/$!/$^ERRNAME:$res:
0/0/NONE:bauauframa:
</code></pre>
</blockquote>
 </dd></dl>
<dt><code>vpospar</code></dt>
<dd> <p> [Only new quoting rules] Manage the positional parameter stack (see <i>1 , # , * ,</i> as well as <code>shift )</code> If the first argument is `clear&#8217; , then the positional parameter stack of the current context, or the global one, if there is none, is cleared. If it is `set&#8217; , then the remaining arguments will be used to (re)create the stack, if the parameter stack size limit is excessed an <i>^ERR </i><code>-OVERFLOW</code> error will occur. </p>
<p> If the first argument is `quote&#8217; , a round-trip capable representation of the stack contents is created, with each quoted parameter separated from each other with the first character of <i>ifs</i> and followed by the first character of <i>if-ws</i> if that is not empty and not identical to the first. If that results in no separation at all a <code>space</code> character is used. This mode supports <code>vput</code> (see Sx Command modifiers ) . I.e., the subcommands `set&#8217; and `quote&#8217; can be used (in conjunction with <code>eval</code> to (re)create an argument stack from and to a single variable losslessly. </p>
<blockquote><pre><code>? vpospar set hey, &quot;'you &quot;, world!
? echo $#: &lt;${1}&gt;&lt;${2}&gt;&lt;${3}&gt;
? vput vpospar x quote
? vpospar clear
? echo $#: &lt;${1}&gt;&lt;${2}&gt;&lt;${3}&gt;
? eval vpospar set ${x}
? echo $#: &lt;${1}&gt;&lt;${2}&gt;&lt;${3}&gt;
</code></pre>
</blockquote>
 </dd>
<dt><code>visual</code></dt>
<dd> <p> (v) Takes a message list and invokes the <code>VISUAL</code> display editor on each message. Modified contents are discarded unless the <i>writebackedited</i> variable is set, and are not used unless the mailbox can be written to and the editor returns a successful exit status. <code>edit</code> can be used instead for a less display oriented editor. </p>
 </dd>
<dt><code>write</code></dt>
<dd> <p> (w) For conventional messages the body without all headers is written. The original message is never marked for deletion in the originating mail folder. The output is decrypted and converted to its native format as necessary. If the output file exists, the text is appended. If a message is in MIME multipart format its first part is written to the specified file as for conventional messages, handling of the remains depends on the execution mode. No special handling of compressed files is performed. </p>
<p> In interactive mode the user is consecutively asked for the filenames of the processed parts. For convenience saving of each part may be skipped by giving an empty value, the same result as writing it to /dev/null Shell piping the part content by specifying a leading vertical bar `|&#8216; character for the filename is supported. Other user input undergoes the usual Sx Filename transformations , including shell pathname wildcard pattern expansions ( <a href="/docs/linux/man/7-glob/">glob</a>(7) and shell variable expansion for the message as such, not the individual parts, and contents of the destination file are overwritten if the file previously existed. Character set conversion to <i>ttycharset</i> is performed when saving text data. </p>
<p> [v15 behaviour may differ] In non-interactive mode any part which does not specify a filename is ignored, and suspicious parts of filenames of the remaining parts are URL percent encoded (as via <code>urlcodec</code> to prevent injection of malicious character sequences, resulting in a filename that will be written into the current directory. Existing files will not be overwritten, instead the part number or a dot are appended after a number sign `#&#8216; to the name until file creation succeeds (or fails due to other reasons). </p>
 </dd>
<dt><code>xcall</code></dt>
<dd> <p> [Only new quoting rules] The sole difference to <code>call</code> is that the new macro is executed in place of the current one, which will not regain control: all resources of the current macro will be released first. This implies that any setting covered by <code>localopts</code> will be forgotten and covered variables will become cleaned up. If this command is not used from within a <code>call ed macro it will silently be (a more expensive variant of)</code> <code>call</code> </p>
 </dd>
<dt><code>xit</code></dt>
<dd> <p> (x) A synonym for <code>exit</code> </p>
 </dd>
<dt><code>z</code></dt>
<dd> <p> [Only new quoting rules] S-nail presents message headers in <i>screen </i><code>fuls as described under the</code> <code>headers</code> command. Without arguments this command scrolls to the next window of messages, likewise if the argument is `+&#8216; An argument of `-&#8216; scrolls to the last, `^&#8216; scrolls to the first, and `$&#8216; to the last <i>screen</i> of messages. A number argument prefixed by `+&#8216; or `-&#8216; indicates that the window is calculated in relation to the current position, and a number without a prefix specifies an absolute position. </p>
 </dd>
<dt><code>Z</code></dt>
<dd> <p> [Only new quoting rules] Similar to <code>z</code> but scrolls to the next or previous window that contains at least one `new&#8217; or <code>flag ged message.</code> </p>
 </dd></dl>
<h2>COMMAND ESCAPES</h2>
<p> Command escapes are available in Sx Compose mode during interactive usage, when explicitly requested via -<code>~</code> and in batch mode ( -<code>#</code> They perform special functions, like editing headers of the message being composed, calling normal Sx COMMANDS , yielding a shell, etc. Command escapes are only recognized at the beginning of lines, and consist of an escape followed by a command character. The default <i>escape</i> character is the tilde `~&#8216; </p>
<p> Unless otherwise documented command escapes ensure proper updates of the error number <i>!</i> and the exit status <i>?</i> The variable <i>errexit</i> controls whether a failed operation errors out message compose mode and causes program exit. Escapes may be prefixed by none to multiple single character command modifiers, interspersed whitespace is ignored: </p>
<ul>
<li> <p> An effect equivalent to the command modifier <code>ignerr</code> can be achieved with hyphen-minus `-&#8216; , overriding <i>errexit</i>  </li>
<li>  The modifier dollar `$&#8216; <code>eval uates the remains of the line; also see</code> Sx Shell-style argument quoting . [v15 behaviour may differ] For now the entire input line is evaluated as a whole; to avoid that control operators like semicolon <code>;</code> are interpreted unintentionally, they must be quoted.  </li>
</ul>
 </p>
<p> Addition of the command line to the [Option]al history can be prevented by placing whitespace directly after <i>escape</i> The [Option]al key <code>bind ings support a compose mode specific context.</code> The following command escapes are supported: </p>
<dl>
<dt><code>~~ </code><i>string</i></dt>
<dd> <p> Insert the string of text in the message prefaced by a single `~&#8216; (If the escape character has been changed, that character must be doubled instead.) </p>
 </dd>
<dt><code>~! </code><i>command</i></dt>
<dd> <p> Execute the indicated shell <i>command</i> which follows, replacing unescaped exclamation marks with the previously executed command if the internal variable <i>bang</i> is set, then return to the message. </p>
 </dd>
<dt><code>~.</code></dt>
<dd> <p> End compose mode and send the message. The hooks <i>on-compose-splice-shell</i> and <i>on-compose-splice</i> in order, will be called when set, after which, in interactive mode <i>askatend</i> (leading to <i>askcc , askbcc</i> and <i>askattach</i> will be checked as well as <i>asksend</i> after which a set <i>on-compose-leave</i> hook will be called, <i>autocc</i> and <i>autobcc</i> will be joined in if set, finally a given <i>message-inject-tail</i> will be incorporated, after which the compose mode is left. </p>
 </dd>
<dt><code>~: </code><i>S-nail-command </i><code>&nbsp;or ~_ </code><i>S-nail-command</i></dt>
<dd> <p> Can be used to execute Sx COMMANDS (which are allowed in compose mode). </p>
 </dd>
<dt><code>~&lt; </code><i>filename</i></dt>
<dd> <p> Identical to <code>~r</code> </p>
 </dd>
<dt><code>~&lt;! </code><i>command</i></dt>
<dd> <p> <i>command</i> is executed using the shell. Its standard output is inserted into the message. </p>
 </dd>
<dt><code>~?</code></dt>
<dd> <p> [Option] Write a summary of command escapes. </p>
 </dd>
<dt><code>~@ </code>[<i>filename...</i> ] </dt>
<dd> <p> Append or edit the list of attachments. Does not manage the error number <i>!</i> and the exit status <i>?</i> (please use <code>~^</code> if error handling is necessary). The append mode expects a list of <i>filename</i> arguments as shell tokens (see Sx Shell-style argument quoting ; token-separating commas are ignored, too), to be interpreted as documented for the command line option -<code>a</code> with the message number exception as below. </p>
<p> Without <i>filename</i> arguments the attachment list is edited, entry by entry; if a filename is left empty, that attachment is deleted from the list; once the end of the list is reached either new attachments may be entered or the session can be quit by committing an empty ``new&#8217;&#8216; attachment. In non-interactive mode or in batch mode ( -<code>#</code> the list of attachments is effectively not edited but instead recreated; again, an empty input ends list creation. </p>
<p> For all modes, if a given filename solely consists of the number sign `#&#8216; followed by either a valid message number of the currently active mailbox, or by a period `.&#8216; , referring to the current message of the active mailbox, the so-called ``dot&#8217;&#8216; then the given message is attached as a `message/rfc822&#8217; MIME message part. The number sign must be quoted to avoid misinterpretation as a shell comment character. </p>
 </dd>
<dt><code>~| </code><i>command</i></dt>
<dd> <p> Pipe the message text through the specified filter command. If the command gives no output or terminates abnormally, retain the original text of the message. The command <a href="/docs/linux/man/1-fmt/">fmt</a>(1) is often used as a rejustifying filter. </p>
<p> If the first character of the command is a vertical bar, then the entire message including header fields is subject to the filter command, so `~||&#8216; echo Fcc: /tmp/test; cat will prepend a file-carbon-copy message header. Also see <code>~e , ~v</code> </p>
 </dd>
<dt><code>~^ </code><i>cmd </i>[<i>subcmd </i>[<i>arg3 </i>[<i>arg4</i> ] ] ] </dt>
<dd> <p> Inspect and modify the message using the semantics of <code>digmsg</code> therefore arguments are evaluated according to Sx Shell-style argument quoting . Error number <i>!</i> and exit status <i>?</i> are not managed: errors are handled via the protocol, and hard errors like I/O failures cannot be handled. </p>
<p> The protocol consists of command lines followed by (a) response line(s). The first field of the response line represents a status code which specifies whether a command was successful or not, whether result data is to be expected, and if, the format of the result data. Response data will be shell quoted as necessary for consumption by <code>readsh</code> or <code>eval</code> and <code>vpospar</code> to name a few. Error status code lines may optionally contain additional context: </p>
 </dd>
<dl>
<dt><code>`210&#8217; </code></dt>
<dd> <p> Status ok; the remains of the line are the result. </p>
 </dd>
<dt><code>`211&#8217; </code></dt>
<dd> <p> Status ok; the rest of the line is optionally used for more status. What follows are lines of result addresses, terminated by an empty line. All the input, including the empty line, must be consumed before further commands can be issued. Address lines consist of two token, first the plain network address, e.g., `bob [at] exam.ple&#8217; , followed by the (quoted) full address as known: `&#8216;(Lovely)&#8216; Bob &lt;bob [at] exam.ple&gt;&#8216; . Non-network addresses use the first field to indicate the type (hyphen-minus `-&#8216; for files, vertical bar `|&#8216; for pipes, and number sign `#&#8216; for names which will undergo <code>alias</code> processing) instead, the actual value will be in the second field. </p>
 </dd>
<dt><code>`212&#8217; </code></dt>
<dd> <p> Status ok; the rest of the line is optionally used for more status. What follows are lines of furtherly unspecified (quoted) string content, terminated by an empty line. All the input, including the empty line, must be consumed before further commands can be issued. </p>
 </dd>
<dt><code>`500&#8217; </code></dt>
<dd> <p> Syntax error; invalid command. </p>
 </dd>
<dt><code>`501&#8217; </code></dt>
<dd> <p> Syntax error or otherwise invalid parameters or arguments. </p>
 </dd>
<dt><code>`505&#8217; </code></dt>
<dd> <p> Error: an argument fails verification. For example an invalid address has been specified (also see <i>expandaddr )</i> or an attempt was made to modify anything in S-nail&#8217;s own namespace, or a modifying subcommand has been used on a read-only message. </p>
 </dd>
<dt><code>`506&#8217; </code></dt>
<dd> <p> Error: an otherwise valid argument is rendered invalid due to context. For example, a second address is added to a header which may consist of a single address only. </p>
 </dd></dl>
<p> If a command indicates failure then the message will have remained unmodified. Most commands can fail with `500&#8217; if required arguments are missing, or excessive arguments have been given (false command usage). ([v15 behaviour may differ] The latter does not yet occur regularly, because as stated in Sx Shell-style argument quoting our argument parser is not yet smart enough to work on subcommand base; for example one might get excess argument error for a three argument subcommand that receives four arguments, but not for a four argument subcommand which receives six arguments: here excess will be joined.) The following (case-insensitive) commands are supported: </p>
<dl>
<dt><code>attachment</code></dt>
<dd> <p> This command allows listing, removal and addition of message attachments. The second argument specifies the subcommand to apply, one of: </p>
 </dd>
<dl>
<dt><code>attribute</code></dt>
<dd> <p> This uses the same search mechanism as described for <code>remove</code> and prints any known attributes of the first found attachment via `212&#8217; upon success or `501&#8217; if no such attachment can be found. The attributes are written as lines with a keyword and a value token. </p>
 </dd>
<dt><code>attribute-at</code></dt>
<dd> <p> This uses the same search mechanism as described for <code>remove-at</code> and is otherwise identical to <code>attribute</code> </p>
 </dd>
<dt><code>attribute-set</code></dt>
<dd> <p> This uses the same search mechanism as described for <code>remove</code> and will set the attribute given as the fourth to the value given as the fifth token argument. If the value is an empty token, then the given attribute is removed, or reset to a default value if existence of the attribute is crucial. </p>
<p> It returns via `210&#8217; upon success, with the index of the found attachment following, `505&#8217; for message attachments or if the given keyword is invalid, and `501&#8217; if no such attachment can be found. The following keywords may be used (case-insensitively): </p>
 </dd>
<dl>
<dt><code>`filename&#8217; </code></dt>
<dd> <p> Sets the filename of the MIME part, i.e., the name that is used for display and when (suggesting a name for) saving (purposes). </p>
 </dd>
<dt><code>`content-description&#8217; </code></dt>
<dd> <p> Associate some descriptive information to the attachment&#8217;s content, used in favour of the plain filename by some MUAs. </p>
 </dd>
<dt><code>`content-id&#8217; </code></dt>
<dd> <p> May be used for uniquely identifying MIME entities in several contexts; this expects a special reference address format as defined in RFC 2045 and generates a `505&#8217; upon address content verification failure. </p>
 </dd>
<dt><code>`content-type&#8217; </code></dt>
<dd> <p> Defines the media type/subtype of the part, which is managed automatically, but can be overwritten. </p>
 </dd>
<dt><code>`content-disposition&#8217; </code></dt>
<dd> <p> Automatically set to the string `attachment&#8217; </p>
 </dd></dl>
<dt><code>attribute-set-at</code></dt>
<dd> <p> This uses the same search mechanism as described for <code>remove-at</code> and is otherwise identical to <code>attribute-set</code> </p>
 </dd>
<dt><code>insert</code></dt>
<dd> <p> Adds the attachment given as the third argument, specified exactly as documented for the command line option -<code>a</code> and supporting the message number extension as documented for <code>~@</code> This reports `210&#8217; upon success, with the index of the new attachment following, `505&#8217; if the given file cannot be opened, `506&#8217; if an on-the-fly performed character set conversion fails, otherwise `501&#8217; is reported; this is also reported if character set conversion is requested but not available. </p>
 </dd>
<dt><code>list</code></dt>
<dd> <p> List all attachments via `212&#8217; , or report `501&#8217; if no attachments exist. This command is the default command of <code>attachment</code> if no second argument has been given. </p>
 </dd>
<dt><code>remove</code></dt>
<dd> <p> This will remove the attachment given as the third argument, and report `210&#8217; upon success or `501&#8217; if no such attachment can be found. If there exists any path component in the given argument, then an exact match of the path which has been used to create the attachment is used directly, but if only the basename of that path matches then all attachments are traversed to find an exact match first, and the removal occurs afterwards; if multiple basenames match, a `506&#8217; error occurs. Message attachments are treated as absolute pathnames. </p>
<p> If no path component exists in the given argument, then all attachments will be searched for `filename=&#8216; parameter matches as well as for matches of the basename of the path which has been used when the attachment has been created; multiple matches result in a `506&#8217; </p>
 </dd>
<dt><code>remove-at</code></dt>
<dd> <p> This will interpret the third argument as a number and remove the attachment at that list position (counting from one!), reporting `210&#8217; upon success or `505&#8217; if the argument is not a number or `501&#8217; if no such attachment exists. </p>
 </dd></dl>
<dt><code>header</code></dt>
<dd> <p> This command allows listing, inspection, and editing of message headers. Header name case is not normalized, so that case-insensitive comparison should be used when matching names. The second argument specifies the subcommand to apply, one of: </p>
 </dd>
<dl>
<dt><code>insert</code></dt>
<dd> <p> Create a new or an additional instance of the header given in the third argument, with the header body content as given in the fourth token. It may return `501&#8217; if the third argument specifies a free-form header field name that is invalid, or if body content extraction fails to succeed, `505&#8217; if any extracted address does not pass syntax and/or security checks or on S-nail namespace violations, and `506&#8217; to indicate prevention of excessing a single-instance header --- note that `Subject:&#8216; can be appended to (a space separator will be added automatically first). `To:&#8216; , `Cc:&#8216; and `Bcc:&#8216; support the `?single&#8217; modifier to enforce treatment as a single addressee, for example `header&#8217; insert To?single: &#8216;exa, &lt;m@ple&gt;&#8216; ; the word `single&#8217; is optional. </p>
<p> `210&#8217; is returned upon success, followed by the name of the header and the list position of the newly inserted instance. The list position is always 1 for single-instance header fields. All free-form header fields are managed in a single list; also see <i>customhdr</i> </p>
 </dd>
<dt><code>list</code></dt>
<dd> <p> Without a third argument a list of all yet existing headers is given via `210&#8217; ; this command is the default command of <code>header</code> if no second argument has been given. A third argument restricts output to the given header only, which may fail with `501&#8217; if no such field is defined. </p>
 </dd>
<dt><code>remove</code></dt>
<dd> <p> This will remove all instances of the header given as the third argument, reporting `210&#8217; upon success, `501&#8217; if no such header can be found, and `505&#8217; on S-nail namespace violations. </p>
 </dd>
<dt><code>remove-at</code></dt>
<dd> <p> This will remove from the header given as the third argument the instance at the list position (counting from one!) given with the fourth argument, reporting `210&#8217; upon success or `505&#8217; if the list position argument is not a number or on S-nail namespace violations, and `501&#8217; if no such header instance exists. </p>
 </dd>
<dt><code>show</code></dt>
<dd> <p> Shows the content of the header given as the third argument. Dependent on the header type this may respond with `211&#8217; or `212&#8217; ; any failure results in `501&#8217; </p>
 </dd></dl>
<p> In compose-mode read-only access to optional pseudo headers in the S-nail private namespace is available: </p>
<dl>
<dt><code>`Mailx-Command:&#8216; </code></dt>
<dd> <p> The name of the command that generates the message, one of `forward&#8217; , `Lreply&#8217; , `mail&#8217; , `Reply&#8217; , `reply&#8217; , `resend&#8217; This pseudo header always exists (in compose-mode). </p>
 </dd>
<dt><code>`Mailx-Raw-To:&#8216; </code></dt>
<dd>  </dd>
<dt><code>`Mailx-Raw-Cc:&#8216; </code></dt>
<dd>  </dd>
<dt><code>`Mailx-Raw-Bcc:&#8216; </code></dt>
<dd> <p> Represent the frozen initial state of these headers before any transformation ( <code>alias</code> <code>alternates</code> <i>recipients-in-cc</i> etc.) took place. </p>
 </dd>
<dt><code>`Mailx-Orig-Sender:&#8216; </code></dt>
<dd>  </dd>
<dt><code>`Mailx-Orig-From:&#8216; </code></dt>
<dd>  </dd>
<dt><code>`Mailx-Orig-To:&#8216; </code></dt>
<dd>  </dd>
<dt><code>`Mailx-Orig-Cc:&#8216; </code></dt>
<dd>  </dd>
<dt><code>`Mailx-Orig-Bcc:&#8216; </code></dt>
<dd> <p> The values of said headers of the original message which has been addressed by any of <code>reply , forward , resend</code> The sender field is special as it is filled in with the sole sender according to RFC 5322 rules, it may thus be equal to the from field. </p>
 </dd></dl>
<dt><code>help , ?</code></dt>
<dd> <p> Show an abstract of the above commands via `211&#8217; </p>
 </dd>
<dt><code>version</code></dt>
<dd> <p> This command will print the protocol version via `210&#8217; </p>
 </dd></dl>
<dt><code>~A</code></dt>
<dd> <p> The same as `<code>~i</code> &#8216; Ns Va Sign . </p>
 </dd>
<dt><code>~a</code></dt>
<dd> <p> The same as `<code>~i</code> &#8216; Ns Va sign . </p>
 </dd>
<dt><code>~b </code><i>name ...</i></dt>
<dd> <p> Add the given names to the list of blind carbon copy recipients. </p>
 </dd>
<dt><code>~c </code><i>name ...</i></dt>
<dd> <p> Add the given names to the list of carbon copy recipients. </p>
 </dd>
<dt><code>~d</code></dt>
<dd> <p> Read the file specified by the <code>DEAD</code> variable into the message. </p>
 </dd>
<dt><code>~e</code></dt>
<dd> <p> Invoke the text <code>EDITOR</code> on the message collected so far, then return to compose mode. <code>~v</code> can be used for a more display oriented editor, and <code>~| |</code> offers a pipe-based editing approach. </p>
 </dd>
<dt><code>~F </code><i>messages</i></dt>
<dd> <p> Read the named messages into the message being sent, including all message headers and MIME parts, and honouring <i>forward-add-cc</i> as well as <i>forward-inject-head</i> and <i>forward-inject-tail</i> If no messages are specified, read in the current message, the ``dot&#8217;&#8216; </p>
 </dd>
<dt><code>~f </code><i>messages</i></dt>
<dd> <p> Read the named messages into the message being sent. If no messages are specified, read in the current message, the ``dot&#8217;&#8216; Strips down the list of header fields according to the `forward&#8217; (with <i>posix</i> `type&#8217; ) white- and blacklist selection of <code>headerpick</code> and honours <i>forward-add-cc</i> as well as <i>forward-inject-head</i> and <i>forward-inject-tail</i> For MIME multipart messages, only the first displayable part is included. </p>
 </dd>
<dt><code>~H</code></dt>
<dd> <p> In interactive mode, edit the message header fields `From:&#8216; , `Reply-To:&#8216; and `Sender:&#8216; by typing each one in turn and allowing the user to edit the field. The default values for these fields originate from the <i>from , reply-to</i> and <i>sender</i> variables. In non-interactive mode this sets <i>^ERR </i><code>-NOTTY</code> </p>
 </dd>
<dt><code>~h</code></dt>
<dd> <p> In interactive mode, edit the message header fields `To:&#8216; , `Cc:&#8216; , `Bcc:&#8216; and `Subject:&#8216; by typing each one in turn and allowing the user to edit the field. In non-interactive mode this sets <i>^ERR </i><code>-NOTTY</code> </p>
 </dd>
<dt><code>~I </code><i>variable</i></dt>
<dd> <p> Insert the value of the specified variable into the message. The message remains unaltered if the variable is unset or empty. Any embedded character sequences `\t&#8217; horizontal tabulator and `\n&#8217; line feed are expanded in <i>posix</i> mode; otherwise the expansion should occur at <code>set</code> time ([v15 behaviour may differ] by using the command modifier <i>wysh )</i> </p>
 </dd>
<dt><code>~i </code><i>variable</i></dt>
<dd> <p> Like <code>~I</code> but appends a newline character. </p>
 </dd>
<dt><code>~M </code><i>messages</i></dt>
<dd> <p> Read the named messages into the message being sent, indented by <i>indentprefix</i> If no messages are specified, read the current message, the ``dot&#8217;&#8216; Honours <i>forward-add-cc</i> as well as <i>forward-inject-head</i> and <i>forward-inject-tail</i> </p>
 </dd>
<dt><code>~m </code><i>messages</i></dt>
<dd> <p> Read the named messages into the message being sent, indented by <i>indentprefix</i> If no messages are specified, read the current message, the ``dot&#8217;&#8216; Strips down the list of header fields according to the `type&#8217; white- and blacklist selection of <code>headerpick</code> Honours <i>forward-add-cc</i> as well as <i>forward-inject-head</i> and <i>forward-inject-tail</i> For MIME multipart messages, only the first displayable part is included. </p>
 </dd>
<dt><code>~p</code></dt>
<dd> <p> Display the message collected so far, prefaced by the message header fields and followed by the attachment list, if any. </p>
 </dd>
<dt><code>~Q</code></dt>
<dd> <p> Read in the given / current message(s) using the algorithm of <i>quote</i> (except that is implicitly assumed, even if not set), honouring <i>quote-add-cc</i> </p>
 </dd>
<dt><code>~q</code></dt>
<dd> <p> Abort the message being sent, copying it to the file specified by the <code>DEAD</code> variable if <i>save</i> is set. </p>
 </dd>
<dt><code>~R </code><i>filename</i></dt>
<dd> <p> Identical to <code>~r</code> but indent each line that has been read by <i>indentprefix</i> </p>
 </dd>
<dt><code>~r </code><i>filename </i>[<i>HERE-delimiter</i> ] </dt>
<dd> <p> Read the named file, object to Sx Filename transformations excluding shell globs and variable expansions, into the message; if <i>filename</i> is the hyphen-minus `-&#8216; then standard input is used (for pasting, for example). Only in this latter mode <i>HERE-delimiter</i> may be given: if it is data will be read in until the given <i>HERE-delimiter</i> is seen on a line by itself, and encountering EOF is an error; the <i>HERE-delimiter</i> is a required argument in non-interactive mode; if it is single-quote quoted then the pasted content will not be expanded, [v15 behaviour may differ] otherwise a future version of S-nail may perform shell-style expansion on the content. </p>
 </dd>
<dt><code>~s </code><i>string</i></dt>
<dd> <p> Cause the named string to become the current subject field. Newline (NL) and carriage-return (CR) bytes are invalid and will be normalized to space (SP) characters. </p>
 </dd>
<dt><code>~t </code><i>name ...</i></dt>
<dd> <p> Add the given name(s) to the direct recipient list. </p>
 </dd>
<dt><code>~U </code><i>messages</i></dt>
<dd> <p> Read in the given / current message(s) excluding all headers, indented by <i>indentprefix</i> Honours <i>forward-add-cc</i> as well as <i>forward-inject-head</i> and <i>forward-inject-tail</i> </p>
 </dd>
<dt><code>~u </code><i>messages</i></dt>
<dd> <p> Read in the given / current message(s), excluding all headers. Honours <i>forward-add-cc</i> as well as <i>forward-inject-head</i> and <i>forward-inject-tail</i> </p>
 </dd>
<dt><code>~v</code></dt>
<dd> <p> Invoke the <code>VISUAL</code> editor on the message collected so far, then return to compose mode. <code>~e</code> can be used for a less display oriented editor, and <code>~| |</code> offers a pipe-based editing approach. </p>
 </dd>
<dt><code>~w </code><i>filename</i></dt>
<dd> <p> Write the message onto the named file, which is object to the usual Sx Filename transformations . If the file exists, the message is appended to it. </p>
 </dd>
<dt><code>~x</code></dt>
<dd> <p> Same as <code>~q</code> except that the message is not saved at all. </p>
 </dd></dl>
<h2>INTERNAL VARIABLES</h2>
<p> Internal S-nail variables are controlled via the <code>set</code> and <code>unset</code> commands; prefixing a variable name with the string `no&#8217; and calling <code>set</code> has the same effect as using <code>unset</code> `unset&#8217; crt and `set&#8217; nocrt do the same thing. <code>varshow</code> will give more insight on the given variable(s), and <code>set</code> when called without arguments, will show a listing of all variables. Both commands support a more <i>verbose</i> listing mode. Some well-known variables will also become inherited from the program Sx ENVIRONMENT implicitly, others can be imported explicitly with the command <code>environ</code> and henceforth share said properties. </p>
<p> Two different kinds of internal variables exist, and both of which can also form chains. There are boolean variables, which can only be in one of the two states ``set&#8217;&#8216; and ``unset&#8217;&#8216; and value variables with a(n optional) string value. For the latter proper quoting is necessary upon assignment time, the introduction of the section Sx COMMANDS documents the supported quoting rules. </p>
<blockquote><pre><code>? wysh set one=val\ 1 two=&quot;val 2&quot; \
    three='val &quot;3&quot;' four=$'val \'4\''; \
    varshow one two three four; \
    unset one two three four
</code></pre>
</blockquote>
<p> Dependent upon the actual option string values may become interpreted as colour names, command specifications, normal text, etc. They may be treated as numbers, in which case decimal values are expected if so documented, but otherwise any numeric format and base that is valid and understood by the <code>vexpr</code> command may be used, too. </p>
<p> There also exists a special kind of string value, the ``boolean string&#8217;&#8216; which must either be a decimal integer (in which case `0&#8217; is false and `1&#8217; and any other value is true) or any of the (case-insensitive) strings `off&#8217; , `no&#8217; , `n&#8217; and `false&#8217; for a false boolean and `on&#8217; , `yes&#8217; , `y&#8217; and `true&#8217; for a true boolean; a special kind of boolean string is the ``quadoption&#8217;&#8216; it can optionally be prefixed with the (case-insensitive) term `ask-&#8216; , as in `ask-yes&#8217; ; in interactive mode the user will be prompted, otherwise the actual boolean is used. </p>
<p> Variable chains extend a plain `variable&#8217; with `variable-HOST&#8217; and `variable-USER [at] HOST&#8217; variants. Here `HOST&#8217; will be converted to all lowercase when looked up (but not when the variable is set or unset!), [Option]ally IDNA converted, and indeed means `server:port&#8217; if a `port&#8217; had been specified in the contextual Uniform Resource Locator URL, see Sx On URL syntax and credential lookup . Even though this mechanism is based on URLs no URL percent encoding may be applied to neither of `USER&#8217; nor `HOST&#8217; , variable chains need to be specified using raw data; the mentioned section contains examples. Variables which support chains are explicitly documented as such, and S-nail treats the base name of any such variable special, meaning that users should not create custom names like `variable-xyz&#8217; in order to avoid false classifications and treatment of such variables.  </p>
<h3>Initial settings</h3>
<p> The standard POSIX 2008/Cor 2-2016 mandates the following initial variable settings: no <i>allnet</i> no <i>append</i> <i>asksub</i> no <i>askbcc</i> no <i>autoprint</i> no <i>bang</i> no <i>cmd</i> no <i>crt</i> no <i>debug</i> no <i>dot</i> <i>escape</i> set to `~&#8216; , no <i>flipr</i> no <i>folder</i> <i>header</i> no <i>hold</i> no <i>ignore</i> no <i>ignoreeof</i> no <i>keep</i> no <i>keepsave</i> no <i>metoo</i> no <i>outfolder</i> no <i>page</i> <i>prompt</i> set to `?&nbsp;&#8216; , no <i>quiet</i> no <i>record</i> <i>save</i> no <i>sendwait</i> no <i>showto</i> no <i>Sign</i> no <i>sign</i> <i>toplines</i> set to `5&#8217; </p>
<p> However, S-nail has built-in some initial (and some default) settings which (may) diverge, others may become adjusted by one of the Sx Resource files . Displaying the former is accomplished via <code>set</code> `$&#8216; s-nail -:/ -v -Xset -Xx . In general this implementation sets (and has extended the meaning of) <i>sendwait</i> and does not support the no <i>onehop</i> variable - use command line options or <i>mta-arguments</i> to pass options through to a <i>mta</i> The default global resource file sets, among others, the variables <i>hold</i> <i>keep</i> and <i>keepsave</i> establishes a default <code>headerpick</code> selection etc., and should thus be taken into account.  </p>
<h3>Variables</h3>
<dl>
<dt><i>?</i></dt>
<dd> <p> (Read-only) The exit status of the last command, or the <code>return</code> value of the macro <code>call ed last.</code> This status has a meaning in the state machine: in conjunction with <i>errexit</i> any non-0 exit status will cause a program exit, and in <i>posix</i> mode any error while loading (any of the) resource files will have the same effect. <code>ignerr</code> one of the Sx Command modifiers , can be used to instruct the state machine to ignore errors. </p>
 </dd>
<dt><i>!</i></dt>
<dd> <p> (Read-only) The current error number ( <a href="/docs/linux/man/3-errno/">errno</a>(3)) which is set after an error occurred; it is also available via <i>^ERR</i> and the error name and documentation string can be queried via <i>^ERRNAME</i> and <i>^ERRDOC</i> [v15 behaviour may differ] This machinery is new and the error number is only really usable if a command explicitly states that it manages the variable <i>!</i> for others errno will be used in case of errors, or <i>^ERR </i><code>-INVAL</code> if that is 0: it thus may or may not reflect the real error. The error number may be set with the command <code>return</code> </p>
 </dd>
<dt><i>^</i></dt>
<dd> <p> (Read-only) This is a multiplexer variable which performs dynamic expansion of the requested state or condition, of which there are: </p>
 </dd>
<dl>
<dt><i>^ERR , ^ERRDOC , ^ERRNAME</i></dt>
<dd> <p> The number, documentation, and name of the current <a href="/docs/linux/man/3-errno/">errno</a>(3), respectively, which is usually set after an error occurred. The documentation is an [Option], the name is used if not available. [v15 behaviour may differ] This machinery is new and is usually reliable only if a command explicitly states that it manages the variable <i>!</i> which is effectively identical to <i>^ERR</i> Each of those variables can be suffixed with a hyphen minus followed by a name or number, in which case the expansion refers to the given error. Note this is a direct mapping of (a subset of) the system error values: </p>
<blockquote><pre><code>define work {
  eval echo \$1: \$^ERR-$1:\
    \$^ERRNAME-$1: \$^ERRDOC-$1
  vput vexpr i + &quot;$1&quot; 1
  if [ $i -lt 16 ]
    \xcall work $i
  end
}
call work 0
</code></pre>
</blockquote>
 </dd>
<dt><i>^ERRQUEUE-COUNT , ^ERRQUEUE-EXISTS</i></dt>
<dd> <p> The number of messages in the [Option]al queue of <code>errors</code> and a string indicating queue state: empty or (translated) ``ERROR&#8217;&#8216; Always 0 and the empty string, respectively, unless <i>features</i> includes `,+errors,&#8216; </p>
 </dd></dl>
<dt><i>*</i></dt>
<dd> <p> (Read-only) Expands all positional parameters (see <i>1 )</i> separated by the first character of the value of <i>ifs</i> [v15 behaviour may differ] The special semantics of the equally named special parameter of the <a href="/docs/linux/man/1-sh/">sh</a>(1) are not yet supported. </p>
 </dd>
<dt><i>@</i></dt>
<dd> <p> (Read-only) Expands all positional parameters (see <i>1 )</i> separated by a space character. If placed in double quotation marks, each positional parameter is properly quoted to expand to a single parameter again. </p>
 </dd>
<dt><i>#</i></dt>
<dd> <p> (Read-only) Expands to the number of positional parameters, i.e., the size of the positional parameter stack in decimal. </p>
 </dd>
<dt><i>0</i></dt>
<dd> <p> (Read-only) Inside the scope of a <code>define d and</code> <code>call ed macro this expands to the name of the calling macro, or to the empty</code> string if the macro is running from top-level. For the [Option]al regular expression search and replace operator of <code>vexpr</code> this expands to the entire matching expression. It represents the program name in global context. </p>
 </dd>
<dt><i>1</i></dt>
<dd> <p> (Read-only) Access of the positional parameter stack. All further parameters can be accessed with this syntax, too, `2&#8217; , `3&#8217; etc.; positional parameters can be shifted off the stack by calling <code>shift</code> The parameter stack contains, for example, the arguments of a <code>call ed</code> <code>define d macro, the matching groups of the [Option]al regular expression search</code> and replace expression of <code>vexpr</code> and can be explicitly created or overwritten with the command <code>vpospar</code> </p>
 </dd>
<dt><i>account</i></dt>
<dd> <p> (Read-only) Is set to the active <code>account</code> </p>
 </dd>
<dt><i>add-file-recipients</i></dt>
<dd> <p> (Boolean) When file or pipe recipients have been specified, mention them in the corresponding address fields of the message instead of silently stripping them from their recipient list. By default such addressees are not mentioned. </p>
 </dd>
<dt><i>allnet</i></dt>
<dd> <p> (Boolean) Causes only the local part to be evaluated when comparing addresses. </p>
 </dd>
<dt><i>append</i></dt>
<dd> <p> (Boolean) Causes messages saved in the Sx secondary mailbox <code>MBOX</code> to be appended to the end rather than prepended. This should always be set. </p>
 </dd>
<dt><i>askatend</i></dt>
<dd> <p> (Boolean) Causes the prompts for `Cc:&#8216; and `Bcc:&#8216; lists to appear after the message has been edited. </p>
 </dd>
<dt><i>askattach</i></dt>
<dd> <p> (Boolean) If set, S-nail asks an interactive user for files to attach at the end of each message; An empty line finalizes the list. </p>
 </dd>
<dt><i>askcc</i></dt>
<dd> <p> (Boolean) Causes the interactive user to be prompted for carbon copy recipients (at the end of each message if <i>askatend</i> or <i>bsdcompat</i> are set). </p>
 </dd>
<dt><i>askbcc</i></dt>
<dd> <p> (Boolean) Causes the interactive user to be prompted for blind carbon copy recipients (at the end of each message if <i>askatend</i> or <i>bsdcompat</i> are set). </p>
 </dd>
<dt><i>asksend</i></dt>
<dd> <p> (Boolean) Causes the interactive user to be prompted for confirmation to send the message or reenter compose mode after having been shown a preliminary envelope summary. </p>
 </dd>
<dt><i>asksign</i></dt>
<dd> <p> (Boolean)[Option] Causes the interactive user to be prompted if the message is to be signed at the end of each message. The <i>smime-sign</i> variable is ignored when this variable is set. </p>
 </dd>
<dt><i>asksub</i></dt>
<dd> <p> (Boolean) Causes S-nail to prompt the interactive user for the subject upon entering compose mode unless a subject already exists. </p>
 </dd>
<dt><i>attrlist</i></dt>
<dd> <p> A sequence of characters to display in the `attribute&#8217; column of the <i>headline</i> as shown in the display of <code>headers</code> each for one type of messages (see Sx Message states ) , with the default being `NUROSPMFAT+-$~&#8216; or `NU&nbsp;*HMFAT+-$~&#8216; if the <i>bsdflags</i> variable is set, in the following order: </p>
 </dd>
<dl>
<dt><code>`N&#8217; </code></dt>
<dd> <p> new. </p>
 </dd>
<dt><code>`U&#8217; </code></dt>
<dd> <p> unread but old. </p>
 </dd>
<dt><code>`R&#8217; </code></dt>
<dd> <p> new but read. </p>
 </dd>
<dt><code>`O&#8217; </code></dt>
<dd> <p> read and old. </p>
 </dd>
<dt><code>`S&#8217; </code></dt>
<dd> <p> saved. </p>
 </dd>
<dt><code>`P&#8217; </code></dt>
<dd> <p> preserved. </p>
 </dd>
<dt><code>`M&#8217; </code></dt>
<dd> <p> mboxed. </p>
 </dd>
<dt><code>`F&#8217; </code></dt>
<dd> <p> flagged. </p>
 </dd>
<dt><code>`A&#8217; </code></dt>
<dd> <p> answered. </p>
 </dd>
<dt><code>`T&#8217; </code></dt>
<dd> <p> draft. </p>
 </dd>
<dt><code>`+&#8216; </code></dt>
<dd> <p> [v15 behaviour may differ] start of a (collapsed) thread in threaded mode (see <i>autosort</i> <code>thread )</code> </p>
 </dd>
<dt><code>`-&#8216; </code></dt>
<dd> <p> [v15 behaviour may differ] an uncollapsed thread in threaded mode; only used in conjunction with -<code>L</code> </p>
 </dd>
<dt><code>`$&#8216; </code></dt>
<dd> <p> classified as spam. </p>
 </dd>
<dt><code>`~&#8216; </code></dt>
<dd> <p> classified as possible spam. </p>
 </dd></dl>
<dt><i>autobcc</i></dt>
<dd> <p> Specifies a list of recipients to which a blind carbon copy of each outgoing message will be sent automatically. </p>
 </dd>
<dt><i>autocc</i></dt>
<dd> <p> Specifies a list of recipients to which a carbon copy of each outgoing message will be sent automatically. </p>
 </dd>
<dt><i>autocollapse</i></dt>
<dd> <p> (Boolean) Causes threads to be collapsed automatically when .Ql thread Ns ed <code>sort</code> mode is entered (see the <code>collapse</code> command). </p>
 </dd>
<dt><i>autoprint</i></dt>
<dd> <p> (Boolean) Enable automatic <code>type ing of a(n existing)</code> ``successive&#8217;&#8216; message after <code>delete</code> and <code>undelete</code> commands: the message that becomes the new ``dot&#8217;&#8216; is shown automatically, as via <code>dp</code> or <code>dt</code> </p>
 </dd>
<dt><i>autosort</i></dt>
<dd> <p> Causes sorted mode (see the <code>sort</code> command) to be entered automatically with the value of this variable as sorting method when a folder is opened, for example `set&#8217; autosort=thread . </p>
 </dd>
<dt><i>bang</i></dt>
<dd> <p> (Boolean) Enables the substitution of all not (reverse-solidus) escaped exclamation mark `!&#8216; characters by the contents of the last executed command for the <code>!</code> shell escape command and <code>~!</code> one of the compose mode Sx COMMAND ESCAPES . If this variable is not set no reverse solidus stripping is performed. </p>
 </dd>
<dt><i>bind-timeout</i></dt>
<dd> <p> [Obsolete] Predecessor of <i>bind-inter-byte-timeout</i> [v15 behaviour may differ] Setting this automatically sets the successor. </p>
 </dd>
<dt><i>bind-inter-byte-timeout</i></dt>
<dd> <p> [Option] Terminals may generate multi-byte sequences for special function keys, for example, but these sequences may not become read as a unit. And multi-byte sequences can be defined freely via <code>bind</code> This variable specifies the timeout in milliseconds that the MLE (see Sx On terminal control and line editor ) waits for more bytes to arrive unless it considers a sequence ``complete&#8217;&#8216; The default is 200, the maximum is about 10 seconds. In the following example the comments state which sequences are affected by this timeout: </p>
<blockquote><pre><code>? bind base abc echo 0 # abc
? bind base ab,c echo 1 # ab
? bind base abc,d echo 2 # abc
? bind base ac,d echo 3 # ac
? bind base a,b,c echo 4
? bind base a,b,c,d echo 5
? bind base a,b,cc,dd echo 6 # cc and dd
</code></pre>
</blockquote>
 </dd>
<dt><i>bind-inter-key-timeout</i></dt>
<dd> <p> [Option] Multi-key <code>bind</code> sequences do not time out by default. If this variable is set, then the current key sequence is forcefully terminated once the timeout (in milliseconds) triggers. The value should be (maybe significantly) larger than <i>bind-inter-byte-timeout</i> but may not excess the maximum, too. </p>
 </dd>
<dt><i>bsdcompat</i></dt>
<dd> <p> (Boolean) Sets some cosmetical features to traditional BSD style; has the same affect as setting <i>askatend</i> and all other variables prefixed with `bsd&#8217; ; it also changes the behaviour of <i>emptystart</i> (which does not exist in BSD). </p>
 </dd>
<dt><i>bsdflags</i></dt>
<dd> <p> (Boolean) Changes the letters shown in the first column of a header summary to traditional BSD style. </p>
 </dd>
<dt><i>bsdheadline</i></dt>
<dd> <p> (Boolean) Changes the display of columns in a header summary to traditional BSD style. </p>
 </dd>
<dt><i>bsdmsgs</i></dt>
<dd> <p> (Boolean) Changes some informational messages to traditional BSD style. </p>
 </dd>
<dt><i>bsdorder</i></dt>
<dd> <p> (Boolean) Causes the `Subject:&#8216; field to appear immediately after the `To:&#8216; field in message headers and with the <code>~h</code> Sx COMMAND ESCAPES . </p>
 </dd>
<dt><i>build-cc , build-ld , build-os , build-rest</i></dt>
<dd> <p> (Read-only) The build environment, including the compiler, the linker, the operating system S-nail has been build for, usually taken from <a href="/docs/linux/man/1-uname/">uname</a>(1) via `uname&#8217; -s , and then lowercased, as well as all the possibly interesting rest of the configuration and build environment. This information is also available in the <i>verbose</i> output of the command <code>version</code> </p>
 </dd>
<dt><i>charset-7bit</i></dt>
<dd> <p> The value that should appear in the `charset=&#8216; parameter of `Content-Type:&#8216; MIME header fields when no character set conversion of the message data was performed. This defaults to US-ASCII, and the chosen character set should be US-ASCII compatible. </p>
 </dd>
<dt><i>charset-8bit</i></dt>
<dd> <p> [Option] The default 8-bit character set that is used as an implicit last member of the variable <i>sendcharsets</i> This defaults to UTF-8 if character set conversion capabilities are available, and to ISO-8859-1 otherwise (unless the operating system environment is known to always and exclusively support UTF-8 locales), in which case the only supported character set is <i>ttycharset</i> and this variable is effectively ignored. </p>
 </dd>
<dt><i>charset-unknown-8bit</i></dt>
<dd> <p> [Option] RFC 1428 specifies conditions when internet mail gateways shall ``upgrade&#8217;&#8216; the content of a mail message by using a character set with the name `unknown-8bit&#8217; Because of the unclassified nature of this character set S-nail will not be capable to convert this character set to any other character set. If this variable is set any message part which uses the character set `unknown-8bit&#8217; is assumed to really be in the character set given in the value, otherwise the (final) value of <i>charset-8bit</i> is used for this purpose. </p>
<p> This variable will also be taken into account if a MIME type (see Sx The mime.types files ) of a MIME message part that uses the `binary&#8217; character set is forcefully treated as text. </p>
 </dd>
<dt><i>cmd</i></dt>
<dd> <p> The default value for the <code>pipe</code> command. </p>
 </dd>
<dt><i>colour-disable</i></dt>
<dd> <p> (Boolean)[Option] Forcefully disable usage of colours. Also see the section Sx Coloured display . </p>
 </dd>
<dt><i>colour-pager</i></dt>
<dd> <p> (Boolean)[Option] Whether colour shall be used for output that is paged through <code>PAGER</code> Note that pagers may need special command line options, for example <a href="/docs/linux/man/1-less/">less</a>(1) requires the option -<code>R</code> and <a href="/docs/linux/man/1-lv/">lv</a>(1) the option -<code>c</code> in order to support colours. Often doing manual adjustments is unnecessary since S-nail may perform adjustments dependent on the value of the environment variable <code>PAGER</code> (see there for more). </p>
 </dd>
<dt><i>contact-mail , contact-web</i></dt>
<dd> <p> (Read-only) Addresses for contact per email and web, respectively, for bug reports, suggestions, or anything else regarding S-nail. The former can be used directly: `?&#8216; Ns Ic eval Ns Ic mail Ns $contact-mail . </p>
 </dd>
<dt><i>content-description-forwarded-message</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;content-description-quote-attachment ,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;content-description-smime-message ,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;content-description-smime-signature [Option](partially) Strings which will be placed in according `Content-Description:&#8216; headers if non-empty. They all have default values, for example `Forwarded&#8217; message . </p>
 </dd>
<dt><i>crt</i></dt>
<dd> <p> In a(n interactive) terminal session, then if this valued variable is set it will be used as a threshold to determine how many lines the given output has to span before it will be displayed via the configured <code>PAGER</code> Usage of the <code>PAGER</code> can be forced by setting this to the value `0&#8217; , setting it without a value will deduce the current height of the terminal screen to compute the threshold (see <code>LINES</code> <i>screen</i> and <a href="/docs/linux/man/1-stty/">stty</a>(1)). [v15 behaviour may differ] At the moment this uses the count of lines of the message in wire format, which, dependent on the <i>mime-encoding</i> of the message, is unrelated to the number of display lines. (The software is old and historically the relation was a given thing.) </p>
 </dd>
<dt><i>customhdr</i></dt>
<dd> <p> Define a set of custom headers to be injected into newly composed or forwarded messages. A custom header consists of the field name followed by a colon `:&#8216; and the field content body. Standard header field names cannot be overwritten by a custom header, with the exception of `Comments:&#8216; and `Keywords:&#8216; Different to the command line option -<code>C</code> the variable value is interpreted as a comma-separated list of custom headers: to include commas in header bodies they need to become escaped with reverse solidus `\&#8216; Headers can be managed more freely in Sx Compose mode via <code>~^</code> </p>
<blockquote><p> <code>? set customhdr=&#8216;Hdr1: Body1-1\, Body1-2, Hdr2: Body2&#8217;</code> </p>
</blockquote>
 </dd>
<dt><i>datefield</i></dt>
<dd> <p> Controls the appearance of the `%d&#8217; date and time format specification of the <i>headline</i> variable, that is used, for example, when viewing the summary of <code>headers</code> If unset, then the local receiving date is used and displayed unformatted, otherwise the message sending `Date:&#8216; It is possible to assign a <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format string and control formatting, but embedding newlines via the `%n&#8217; format is not supported, and will result in display errors. The default is `%Y-%m-%d&#8217; %H:%M , and also see <i>datefield-markout-older</i> </p>
 </dd>
<dt><i>datefield-markout-older</i></dt>
<dd> <p> Only used in conjunction with <i>datefield</i> Can be used to create a visible distinction of messages dated more than a day in the future, or older than six months, a concept comparable to the -<code>l</code> option of the POSIX utility <a href="/docs/linux/man/1-ls/">ls</a>(1). If set to the empty string, then the plain month, day and year of the `Date:&#8216; will be displayed, but a <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format string to control formatting can be assigned. The default is `%Y-%m-%d&#8217; </p>
 </dd>
<dt><i>debug</i></dt>
<dd> <p> (Boolean) (Almost) Enter a debug-only sandbox mode which generates many log messages, disables the actual delivery of messages, and also implies no <i>record</i> as well as no <i>save</i> Also see <i>verbose</i> </p>
 </dd>
<dt><i>disposition-notification-send</i></dt>
<dd> <p> (Boolean)[Option] Emit a `Disposition-Notification-To:&#8216; header (RFC 3798) with the message. This requires the <i>from</i> variable to be set. </p>
 </dd>
<dt><i>dot</i></dt>
<dd> <p> (Boolean) When dot is set, a period `.&#8216; on a line by itself during message input in (interactive or batch -<code>#</code> Sx Compose mode will be treated as end-of-message (in addition to the normal end-of-file condition). This behaviour is implied in <i>posix</i> mode with a set <i>ignoreeof</i> </p>
 </dd>
<dt><i>dotlock-disable</i></dt>
<dd> <p> (Boolean)[Option] Disable creation of Sx dotlock files for MBOX databases. </p>
 </dd>
<dt><i>dotlock-ignore-error</i></dt>
<dd> <p> [Obsolete](Boolean)[Option] Ignore failures when creating Sx dotlock files . Please use <i>dotlock-disable</i> instead. </p>
 </dd>
<dt><i>editalong</i></dt>
<dd> <p> If this variable is set then the editor is started automatically when a message is composed in interactive mode. If the value starts with the letter `v&#8217; then this acts as if <code>~v</code> otherwise as if <code>~e</code> (see&nbsp; Sx COMMAND ESCAPES had been specified. The <i>editheaders</i> variable is implied for this automatically spawned editor session. </p>
 </dd>
<dt><i>editheaders</i></dt>
<dd> <p> (Boolean) When a message is edited while being composed, its header is included in the editable text. </p>
 </dd>
<dt><i>emptystart</i></dt>
<dd> <p> (Boolean) When entering interactive mode S-nail normally writes ``<code>mail for user</code> &#8216;&#8216; and exits immediately if a mailbox is empty or does not exist. If this variable is set S-nail starts even with an empty or non-existent mailbox (the latter behaviour furtherly depends upon <i>bsdcompat</i> though). </p>
 </dd>
<dt><i>errexit</i></dt>
<dd> <p> (Boolean) Let each command with a non-0 exit status, including every <code>call ed macro which</code> <code>return s a non-0 status, cause a program exit unless prefixed by</code> <code>ignerr</code> (see Sx Command modifiers ) . This also affects Sx COMMAND ESCAPES , but which use a different modifier for ignoring the error. Please refer to the variable <i>?</i> for more on this topic. </p>
 </dd>
<dt><i>errors-limit</i></dt>
<dd> <p> [Option] Maximum number of entries in the <code>errors</code> queue. </p>
 </dd>
<dt><i>escape</i></dt>
<dd> <p> The first character of this value defines the escape character for Sx COMMAND ESCAPES in Sx Compose mode . The default value is the character tilde `~&#8216; If set to the empty string, command escapes are disabled. </p>
 </dd>
<dt><i>expandaddr</i></dt>
<dd> <p> If unset only user name and email address recipients are allowed Sx On sending mail, and non-interactive mode . If set without value all possible recipient types will be accepted. A value is parsed as a comma-separated list of case-insensitive strings, and if that contains `restrict&#8217; behaviour equals the former except when in interactive mode or if Sx COMMAND ESCAPES were enabled via -<code>~</code> or -<code>#</code> in which case it equals the latter, allowing all address types. `restrict&#8217; really acts like `restrict,-all,+name,+addr&#8217; , so care for ordering issues must be taken. </p>
<p> Recipient types can be added and removed with a plus sign `+&#8216; or hyphen-minus `-&#8216; prefix, respectively. By default invalid or disallowed types are filtered out and cause a warning, hard send errors need to be enforced by including `fail&#8217; The value `all&#8217; covers all types, `fcc&#8217; whitelists `Fcc:&#8216; header targets regardless of other settings, `file&#8217; file targets (it includes `fcc&#8217; ) , `pipe&#8217; command pipeline targets, `name&#8217; user names still unexpanded after <code>alias</code> and <i>mta-aliases</i> processing and thus left for expansion by the <i>mta</i> (invalid for the built-in SMTP one), and `addr&#8217; network addresses. Targets are interpreted in the given order, so that `restrict,fail,+file,-all,+addr&#8217; will cause hard errors for any non-network address recipient address unless running interactively or having been started with the option -<code>~</code> or -<code>#</code> in the latter case(s) any type may be used. </p>
<p> User name receivers addressing valid local users can be expanded to fully qualified network addresses (also see <i>hostname</i> by including `nametoaddr&#8217; in the list. Historically invalid recipients were stripped off without causing errors, this can be changed by making `failinvaddr&#8217; an entry of the list (it really acts like `failinvaddr,+addr&#8217; ) . Likewise, `domaincheck&#8217; (really&nbsp; `domaincheck,+addr&#8217; compares address domain names against a whitelist and strips off ( `fail&#8217; for hard errors) addressees which fail this test; the domain name `localhost&#8217; and the non-empty value of <i>hostname</i> (the real hostname otherwise) are always whitelisted, <i>expandaddr-domaincheck</i> can be set to extend this list. Finally some address providers (for example -<code>b , c</code> and all other command line recipients) will be evaluated as if specified within dollar-single-quotes (see Sx Shell-style argument quoting ) if the value list contains the string `shquote&#8217; </p>
 </dd>
<dt><i>expandaddr-domaincheck</i></dt>
<dd> <p> Can be set to a comma-separated list of domain names which should be whitelisted for the evaluation of the `domaincheck&#8217; mode of <i>expandaddr</i> IDNA encoding is not automatically performed, <code>addrcodec</code> can be used to prepare the domain (of an address). </p>
 </dd>
<dt><i>expandargv</i></dt>
<dd> <p> Unless this variable is set additional <i>mta</i> (Mail-Transfer-Agent) arguments from the command line, as can be given after a -<code>-</code> separator, results in a program termination with failure status. The same can be accomplished by using the special (case-insensitive) value `fail&#8217; A lesser strict variant is the otherwise identical `restrict&#8217; , which does accept such arguments in interactive mode, or if tilde commands were enabled explicitly by using one of the command line options -<code>~</code> or -<code>#</code> The empty value will allow unconditional usage. </p>
 </dd>
<dt><i>features</i></dt>
<dd> <p> (Read-only) String giving a list of optional features. Features are preceded with a plus sign `+&#8216; if they are available, with a hyphen-minus `-&#8216; otherwise. To ease substring matching the string starts and ends with a comma. The output of the command <code>version</code> includes this information in a more pleasant output. </p>
 </dd>
<dt><i>flipr</i></dt>
<dd> <p> (Boolean) This setting reverses the meanings of a set of reply commands, turning the lowercase variants, which by default address all recipients included in the header of a message ( <code>reply , respond , followup</code> into the uppercase variants, which by default address the sender only ( <code>Reply , Respond , Followup</code> and vice versa. </p>
 </dd>
<dt><i>folder</i></dt>
<dd> <p> The default path under which mailboxes are to be saved: filenames that begin with the plus sign `+&#8216; will have the plus sign replaced with the value of this variable if set, otherwise the plus sign will remain unchanged when doing Sx Filename transformations ; also see <code>folder</code> for more on this topic, and know about standard imposed implications of <i>outfolder</i> The value supports a subset of transformations itself, and if the non-empty value does not start with a solidus `/&#8216; , then the value of <code>HOME</code> will be prefixed automatically. Once the actual value is evaluated first, the internal variable <i>folder-resolved</i> will be updated for caching purposes. </p>
 </dd>
<dt><i>folder-hook-FOLDER , folder-hook</i></dt>
<dd> <p> Names a <code>define d</code> macro which will be called whenever a <code>folder</code> is opened. The macro will also be invoked when new mail arrives, but message lists for commands executed from the macro only include newly arrived messages then. <code>localopts</code> are activated by default in a folder hook, causing the covered settings to be reverted once the folder is left again. </p>
<p> The specialized form will override the generic one if `FOLDER&#8217; matches the file that is opened. Unlike other folder specifications, the fully expanded name of a folder, without metacharacters, is used to avoid ambiguities. However, if the mailbox resides under <i>folder</i> then the usual `+&#8216; specification is tried in addition, so that if <i>folder</i> is ``mail&#8217;&#8216; (and thus relative to the user&#8217;s home directory) then /home/usr1/mail/sent will be tried as `folder-hook-/home/usr1/mail/sent&#8217; first, but then followed by `folder-hook-+sent&#8217; </p>
 </dd>
<dt><i>folder-resolved</i></dt>
<dd> <p> (Read-only) Set to the fully resolved path of <i>folder</i> once that evaluation has occurred; rather internal. </p>
 </dd>
<dt><i>followup-to</i></dt>
<dd> <p> (Boolean) Controls whether a `Mail-Followup-To:&#8216; header is generated when sending messages to known mailing lists. The user as determined via <i>from</i> (or, if that contains multiple addresses, <i>sender</i> will be placed in there if any list addressee is not a subscribed list. Also see <i>followup-to-honour</i> and the commands <code>mlist , mlsubscribe , reply</code> and <code>Lreply</code> </p>
 </dd>
<dt><i>followup-to-add-cc</i></dt>
<dd> <p> (Boolean) Controls whether the user will be added to the messages&#8217; `Cc:&#8216; list in addition to placing an entry in `Mail-Followup-To:&#8216; (see <i>followup-to )</i> </p>
 </dd>
<dt><i>followup-to-honour</i></dt>
<dd> <p> Controls whether a `Mail-Followup-To:&#8216; header is honoured when group-replying to a message via <code>reply</code> or <code>Lreply</code> This is a Sx quadoption ; if set without a value it defaults to ``yes&#8217;&#8216; and see <i>followup-to</i> </p>
 </dd>
<dt><i>forward-add-cc</i></dt>
<dd> <p> (Boolean) Whether senders of messages forwarded via <code>~F , ~f , ~m , ~U</code> or <code>~u</code> shall be made members of the carbon copies `Cc:&#8216; list. </p>
 </dd>
<dt><i>forward-as-attachment</i></dt>
<dd> <p> (Boolean) Original messages are normally sent as inline text with the <code>forward</code> command, and only the first part of a multipart message is included. With this setting enabled messages are sent as unmodified MIME `message/rfc822&#8217; attachments with all of their parts included. </p>
 </dd>
<dt><i>forward-inject-head , forward-inject-tail</i></dt>
<dd> <p> The strings to put before and after the text of a message with the <code>forward</code> command, respectively. The former defaults to `--------&#8216; Original Message --------\n . Special format directives in these strings will be expanded if possible, and if so configured the output will be folded according to <i>quote-fold</i> for more please refer to <i>quote-inject-head</i> Injections will not be performed by <code>forward</code> if the variable <i>forward-as-attachment</i> is set --- the Sx COMMAND ESCAPES <code>~F , ~f , ~M , ~m , ~U , ~u</code> always inject. </p>
 </dd>
<dt><i>from</i></dt>
<dd> <p> The address (or a list of addresses) to put into the `From:&#8216; field of the message header, quoting RFC 5322: the author(s) of the message, that is, the mailbox(es) of the person(s) or system(s) responsible for the writing of the message. According to that RFC setting the <i>sender</i> variable is required if <i>from</i> contains more than one address. [v15 behaviour may differ] Please expect automatic management of the <i>from</i> and <i>sender</i> relationship. Dependent on the context these addresses are handled as if they were in the list of <code>alternates</code> </p>
<p> If a file-based MTA is used, then <i>from</i> (or, if that contains multiple addresses, <i>sender</i> can nonetheless be used as the envelope sender address at the MTA protocol level (the RFC 5321 reverse-path), either via the -<code>r</code> command line option (without argument; see there for more), or by setting <i>r-option-implicit</i> </p>
<p> If the machine&#8217;s hostname is not valid at the Internet (for example at a dialup machine), then either this variable or <i>hostname</i> ([v15-compat] a SMTP-based <i>mta</i> adds even more fine-tuning capabilities with <i>smtp-hostname</i> have to be set: if so the message and MIME part related unique ID fields `Message-ID:&#8216; and `Content-ID:&#8216; will be created (except when disallowed by <i>message-id-disable</i> or <i>stealthmua )</i> </p>
 </dd>
<dt><i>fullnames</i></dt>
<dd> <p> (Boolean) Due to historical reasons comments and name parts of email addresses are removed by default when sending mail, replying to or forwarding a message. If this variable is set such stripping is not performed. </p>
 </dd>
<dt><i>fwdheading</i></dt>
<dd> <p> [Obsolete] Predecessor of <i>forward-inject-head</i> </p>
 </dd>
<dt><i>header</i></dt>
<dd> <p> (Boolean) Causes the header summary to be written at startup and after commands that affect the number of messages or the order of messages in the current <code>folder</code> Unless in <i>posix</i> mode a header summary will also be displayed on folder changes. The command line option -<code>N</code> can be used to set no <i>header</i> </p>
 </dd>
<dt><i>headline</i></dt>
<dd> <p> A format string to use for the summary of <code>headers</code> Format specifiers in the given string start with a percent sign `%&#8216; and may be followed by an optional decimal number indicating the field width --- if that is negative, the field is to be left-aligned. Names and addresses are subject to modifications according to <i>showname</i> and <i>showto</i> Valid format specifiers are: </p>
 </dd>
<dl>
<dt><code>`%%&#8216; </code></dt>
<dd> <p> A plain percent sign. </p>
 </dd>
<dt><code>`%&gt;&#8216; </code></dt>
<dd> <p> ``Dotmark&#8217;&#8216; a space character but for the current message ( ``dot&#8217;&#8216; for which it expands to `&gt;&#8216; (dependent on <i>headline-plain )</i> </p>
 </dd>
<dt><code>`%&lt;&#8216; </code></dt>
<dd> <p> ``Dotmark&#8217;&#8216; a space character but for the current message ( ``dot&#8217;&#8216; for which it expands to `&lt;&#8216; (dependent on <i>headline-plain )</i> </p>
 </dd>
<dt><code>`%$&#8216; </code></dt>
<dd> <p> [Option] The spam score of the message, as has been classified via the command <code>spamrate</code> Shows only a replacement character if there is no spam support. </p>
 </dd>
<dt><code>`%a&#8217; </code></dt>
<dd> <p> Message attribute character (status flag); the actual content can be adjusted by setting <i>attrlist</i> </p>
 </dd>
<dt><code>`%d&#8217; </code></dt>
<dd> <p> The date found in the `Date:&#8216; header of the message when <i>datefield</i> is set (the default), otherwise the date when the message was received. Formatting can be controlled by assigning a <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format string to <i>datefield</i> (and <i>datefield-markout-older )</i> </p>
 </dd>
<dt><code>`%e&#8217; </code></dt>
<dd> <p> The indenting level in `thread&#8217; Ns ed <code>sort</code> mode. </p>
 </dd>
<dt><code>`%f&#8217; </code></dt>
<dd> <p> The address of the message sender. </p>
 </dd>
<dt><code>`%i&#8217; </code></dt>
<dd> <p> The message thread tree structure. (Note that this format does not support a field width, and honours <i>headline-plain .</i> </p>
 </dd>
<dt><code>`%L&#8217; </code></dt>
<dd> <p> Mailing list status: is the addressee of the message a known `l&#8217; ( <code>mlist</code> or `L&#8217; <code>mlsubscribe d mailing list?</code> The letter `P&#8217; announces the presence of a RFC 2369 `List-Post:&#8216; header, which makes a message a valuable target of <code>Lreply</code> </p>
 </dd>
<dt><code>`%l&#8217; </code></dt>
<dd> <p> The number of lines of the message, if available. </p>
 </dd>
<dt><code>`%m&#8217; </code></dt>
<dd> <p> Message number. </p>
 </dd>
<dt><code>`%o&#8217; </code></dt>
<dd> <p> The number of octets (bytes) in the message, if available. </p>
 </dd>
<dt><code>`%S&#8217; </code></dt>
<dd> <p> Message subject (if any) in double quotes. </p>
 </dd>
<dt><code>`%s&#8217; </code></dt>
<dd> <p> Message subject (if any). </p>
 </dd>
<dt><code>`%t&#8217; </code></dt>
<dd> <p> The position in threaded/sorted order. </p>
 </dd>
<dt><code>`%U&#8217; </code></dt>
<dd> <p> The value 0 except in an IMAP mailbox, where it expands to the UID of the message. </p>
 </dd></dl>
<p> The default is `%&gt;%a%m%-18f&nbsp;%16d&nbsp;%4l/%-5o&nbsp;%i%-s ,&#8216; or `%&gt;%a%m%20-f&nbsp;<wbr>&nbsp;%16d&nbsp;%3l/%-5o&nbsp;%i%-S&#8217; if <i>bsdcompat</i> is set. Also see <i>attrlist</i> <i>headline-plain</i> and <i>headline-bidi</i> </p>
<dt><i>headline-bidi</i></dt>
<dd> <p> Bidirectional text requires special treatment when displaying headers, because numbers (in dates or for file sizes etc.) will not affect the current text direction, in effect resulting in ugly line layouts when arabic or other right-to-left text is to be displayed. On the other hand only a minority of terminals is capable to correctly handle direction changes, so that user interaction is necessary for acceptable results. Note that extended host system support is required nonetheless, e.g., detection of the terminal character set is one precondition; and this feature only works in an Unicode (i.e., UTF-8) locale. </p>
<p> In general setting this variable will cause S-nail to encapsulate text fields that may occur when displaying <i>headline</i> (and some other fields, like dynamic expansions in <i>prompt</i> with special Unicode control sequences; it is possible to fine-tune the terminal support level by assigning a value: no value (or any value other than `1&#8217; , `2&#8217; and `3&#8217; ) will make S-nail assume that the terminal is capable to properly deal with Unicode version 6.3, in which case text is embedded in a pair of U+2068 (FIRST STRONG ISOLATE) and U+2069 (POP DIRECTIONAL ISOLATE) characters. In addition no space on the line is reserved for these characters. </p>
<p> Weaker support is chosen by using the value `1&#8217; (Unicode 6.3, but reserve the room of two spaces for writing the control sequences onto the line). The values `2&#8217; and `3&#8217; select Unicode 1.1 support (U+200E, LEFT-TO-RIGHT MARK); the latter again reserves room for two spaces in addition. </p>
 </dd>
<dt><i>headline-plain</i></dt>
<dd> <p> (Boolean) On Unicode (UTF-8) aware terminals enhanced graphical symbols are used by default for certain entries of <i>headline</i> If this variable is set only basic US-ASCII symbols will be used. </p>
 </dd>
<dt><i>history-file</i></dt>
<dd> <p> [Option] The (expandable) location of a permanent <code>history</code> file for the MLE line editor ( Sx On terminal control and line editor ) Also see <i>history-size</i> </p>
 </dd>
<dt><i>history-gabby</i></dt>
<dd> <p> [Option] Add more entries to the MLE <code>history</code> as is normally done. A comma-separated list of case-insensitive strings can be used to fine-tune which gabby entries shall be allowed. If it contains `errors&#8217; , erroneous commands will also be added. `all&#8217; adds all optional entries, and is the fallback chattiness identifier of <i>on-history-addition</i> </p>
 </dd>
<dt><i>history-gabby-persist</i></dt>
<dd> <p> (Boolean)[Option] The <i>history-gabby</i> entries will not be saved in persistent storage unless this variable is set. The knowledge of whether a persistent entry was gabby is not lost. Also see <i>history-file</i> </p>
 </dd>
<dt><i>history-size</i></dt>
<dd> <p> [Option] Setting this variable imposes a limit on the number of concurrent <code>history</code> entries. If set to the value 0 then no further history entries will be added, and loading and incorporation of the <i>history-file</i> upon program startup can also be suppressed by doing this. Runtime changes will not be reflected before the <code>history</code> is saved or loaded (again). </p>
 </dd>
<dt><i>hold</i></dt>
<dd> <p> (Boolean) This setting controls whether messages are held in the system <i>inbox</i> and it is set by default. </p>
 </dd>
<dt><i>hostname</i></dt>
<dd> <p> Used instead of the value obtained from uname(3) and <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3) as the hostname when expanding local addresses, for example in `From:&#8216; (also see Sx On sending mail, and non-interactive mode , for expansion of addresses that have a valid user-, but no domain name in angle brackets). If either of <i>from</i> or this variable is set the message and MIME part related unique ID fields `Message-ID:&#8216; and `Content-ID:&#8216; will be created (except when disallowed by <i>message-id-disable</i> or <i>stealthmua )</i> If the [Option]al IDNA support is available (see <i>idna-disable</i> variable assignment is aborted when a necessary conversion fails. </p>
<p> Setting it to the empty string will cause the normal hostname to be used, but nonetheless enables creation of said ID fields. [v15-compat] in conjunction with the built-in SMTP <i>mta</i> <i>smtp-hostname</i> also influences the results: one should produce some test messages with the desired combination of <i>hostname</i> and/or <i>from</i> <i>sender</i> etc. first. </p>
 </dd>
<dt><i>idna-disable</i></dt>
<dd> <p> (Boolean)[Option] Can be used to turn off the automatic conversion of domain names according to the rules of IDNA (internationalized domain names for applications). Since the IDNA code assumes that domain names are specified with the <i>ttycharset</i> character set, an UTF-8 locale charset is required to represent all possible international domain names (before conversion, that is). </p>
 </dd>
<dt><i>ifs</i></dt>
<dd> <p> The input field separator that is used ([v15 behaviour may differ] by some functions) to determine where to split input data. </p>
 </dd>
<dl>
<dt><code>1.</code></dt>
<dd> <p> Unsetting is treated as assigning the default value, `&#8216; \t\n . </p>
 </dd>
<dt><code>2.</code></dt>
<dd> <p> If set to the empty value, no field splitting will be performed. </p>
 </dd>
<dt><code>3.</code></dt>
<dd> <p> If set to a non-empty value, all whitespace characters are extracted and assigned to the variable <i>ifs-ws</i> </p>
 </dd></dl>
<dl>
<dt><code>a.</code></dt>
<dd> <p> <i>ifs-ws</i> will be ignored at the beginning and end of input. Diverging from POSIX shells default whitespace is removed in addition, which is owed to the entirely different line content extraction rules. </p>
 </dd>
<dt><code>b.</code></dt>
<dd> <p> Each occurrence of a character of <i>ifs</i> will cause field-splitting, any adjacent <i>ifs-ws</i> characters will be skipped. </p>
 </dd></dl>
<dt><i>ifs-ws</i></dt>
<dd> <p> (Read-only) Automatically deduced from the whitespace characters in <i>ifs</i> </p>
 </dd>
<dt><i>ignore</i></dt>
<dd> <p> (Boolean) Ignore interrupt signals from the terminal while entering messages; instead echo them as `@&#8216; characters and discard the current line. </p>
 </dd>
<dt><i>ignoreeof</i></dt>
<dd> <p> (Boolean) Ignore end-of-file conditions ( `control-D&#8217; in Sx Compose mode on message input and in interactive command input. If set an interactive command input session can only be left by explicitly using one of the commands <code>exit</code> and <code>quit</code> and message input in compose mode can only be terminated by entering a period `.&#8216; on a line by itself or by using the <code>~.</code> Sx COMMAND ESCAPES ; Setting this implies the behaviour that <i>dot</i> describes in <i>posix</i> mode. </p>
 </dd>
<dt><i>inbox</i></dt>
<dd> <p> If this is set to a non-empty string it will specify the user&#8217;s Sx primary system mailbox , overriding <code>MAIL</code> and the system-dependent default, and (thus) be used to replace `%&#8216; when doing Sx Filename transformations ; also see <code>folder</code> for more on this topic. The value supports a subset of transformations itself. </p>
 </dd>
<dt><i>indentprefix</i></dt>
<dd> <p> String used by the <code>~m , ~M</code> and <code>~R</code> Sx COMMAND ESCAPES and by the <i>quote</i> option for indenting messages, in place of the POSIX mandated default tabulator character `\t&#8217; Also see <i>quote-chars</i> </p>
 </dd>
<dt><i>keep</i></dt>
<dd> <p> (Boolean) If set, an empty Sx primary system mailbox file is not removed. Note that, in conjunction with <i>posix</i> mode any empty file will be removed unless this variable is set. This may improve the interoperability with other mail user agents when using a common folder directory, and prevents malicious users from creating fake mailboxes in a world-writable spool directory. [v15 behaviour may differ] Only local regular (MBOX) files are covered, Maildir and other mailbox types will never be removed, even if empty. </p>
 </dd>
<dt><i>keep-content-length</i></dt>
<dd> <p> (Boolean) When (editing messages and) writing MBOX mailbox files S-nail can be told to keep the `Content-Length:&#8216; and `Lines:&#8216; header fields that some MUAs generate by setting this variable. Since S-nail does neither use nor update these non-standardized header fields (which in itself shows one of their conceptual problems), stripping them should increase interoperability in between MUAs that work with with same mailbox files. Note that, if this is not set but <i>writebackedited</i> as below, is, a possibly performed automatic stripping of these header fields already marks the message as being modified. [v15 behaviour may differ] At some future time S-nail will be capable to rewrite and apply an <i>mime-encoding</i> to modified messages, and then those fields will be stripped silently. </p>
 </dd>
<dt><i>keepsave</i></dt>
<dd> <p> (Boolean) When a message is saved it is usually discarded from the originating folder when S-nail is quit. This setting causes all saved message to be retained. </p>
 </dd>
<dt><i>line-editor-cpl-word-breaks</i></dt>
<dd> <p> [Option] List of bytes which are used by the <code>mle-complete</code> tabulator completion to decide where word boundaries exist, by default `&#8216;@=;|:&#8216; [v15 behaviour may differ] This mechanism is yet restricted. </p>
 </dd>
<dt><i>line-editor-disable</i></dt>
<dd> <p> (Boolean) Turn off any line editing capabilities (from S-nails POW, see Sx On terminal control and line editor for more). </p>
 </dd>
<dt><i>line-editor-no-defaults</i></dt>
<dd> <p> (Boolean)[Option] Do not establish any default key binding. </p>
 </dd>
<dt><i>log-prefix</i></dt>
<dd> <p> Error log message prefix string ( `s-nail:&#8216; ). </p>
 </dd>
<dt><i>mailbox-display</i></dt>
<dd> <p> (Read-only) The name of the current mailbox ( <code>folder</code> possibly abbreviated for display purposes. </p>
 </dd>
<dt><i>mailbox-resolved</i></dt>
<dd> <p> (Read-only) The fully resolved path of the current mailbox. </p>
 </dd>
<dt><i>mailcap-disable</i></dt>
<dd> <p> (Boolean)[Option] Turn off consideration of MIME type handlers from, and implicit loading of Sx The Mailcap files . </p>
 </dd>
<dt><i>mailx-extra-rc</i></dt>
<dd> <p> An additional startup file that is loaded as the last of the Sx Resource files . Use this file for commands that are not understood by other POSIX <a href="/docs/linux/man/1-mailx/">mailx</a>(1) implementations, i.e., mostly anything which is not covered by Sx Initial settings . </p>
 </dd>
<dt><i>markanswered</i></dt>
<dd> <p> (Boolean) When a message is replied to and this variable is set, it is marked as having been <code>answered</code> See the section Sx Message states . </p>
 </dd>
<dt><i>mbox-fcc-and-pcc</i></dt>
<dd> <p> (Boolean) By default all file and pipe message receivers (see <i>expandaddr</i> will be fed valid MBOX database entry message data (see <code>folder</code> <i>mbox-rfc4155 )</i> and existing file targets will become extended in compliance to RFC 4155. If this variable is unset then a plain standalone RFC 5322 message will be written, and existing file targets will be overwritten. </p>
 </dd>
<dt><i>mbox-rfc4155</i></dt>
<dd> <p> (Boolean) When opening MBOX mailbox databases, and in order to achieve compatibility with old software, the very tolerant POSIX standard rules for detecting message boundaries (so-called `From_&#8216; lines) are used instead of the stricter rules from the standard RFC 4155. This behaviour can be switched by setting this variable. </p>
<p> This may temporarily be handy when S-nail complains about invalid `From_&#8216; lines when opening a MBOX: in this case setting this variable and re-opening the mailbox in question may correct the result. If so, copying the entire mailbox to some other file, as in `copy&#8217; * SOME-FILE , will perform proper, all-compatible `From_&#8216; quoting for all detected messages, resulting in a valid MBOX mailbox. ([v15 behaviour may differ] The better and non-destructive approach is to re-encode invalid messages, as if it would be created anew, instead of mangling the `From_&#8216; lines; this requires the structural code changes of the v15 rewrite.) Finally the variable can be unset again: </p>
<blockquote><pre><code>define mboxfix {
  localopts yes; wysh set mbox-rfc4155;\
    wysh File &quot;${1}&quot;; copy * &quot;${2}&quot;
}
call mboxfix /tmp/bad.mbox /tmp/good.mbox
</code></pre>
</blockquote>
 </dd>
<dt><i>memdebug</i></dt>
<dd> <p> (Boolean) Internal development variable. (Keeps memory debug enabled even if <i>debug</i> is not set.) </p>
 </dd>
<dt><i>message-id-disable</i></dt>
<dd> <p> (Boolean) By setting this variable the generation of `Message-ID:&#8216; and `Content-ID:&#8216; message and MIME part headers can be completely suppressed, effectively leaving this task up to the <i>mta</i> (Mail-Transfer-Agent) or the SMTP server. Note that according to RFC 5321 a SMTP server is not required to add this field by itself, so it should be ensured that it accepts messages without `Message-ID&#8217; </p>
 </dd>
<dt><i>message-inject-head</i></dt>
<dd> <p> A string to put at the beginning of each new message, followed by a newline. [Obsolete] The escape sequences tabulator `\t&#8217; and newline `\n&#8217; are understood (use the <code>wysh</code> prefix when <code>set ting the variable(s) instead).</code> </p>
 </dd>
<dt><i>message-inject-tail</i></dt>
<dd> <p> A string to put at the end of each new message, followed by a newline. [Obsolete] The escape sequences tabulator `\t&#8217; and newline `\n&#8217; are understood (use the <code>wysh</code> prefix when <code>set ting the variable(s) instead).</code> Also see <i>on-compose-leave</i> </p>
 </dd>
<dt><i>metoo</i></dt>
<dd> <p> (Boolean) Usually, when an <code>alias</code> expansion contains the sender, the sender is removed from the expansion. Setting this option suppresses these removals. Note that a set <i>metoo</i> also causes a `-m&#8217; option to be passed through to the <i>mta</i> (Mail-Transfer-Agent); though most of the modern MTAs no longer document this flag, no MTA is known which does not support it (for historical compatibility). </p>
 </dd>
<dt><i>mime-allow-text-controls</i></dt>
<dd> <p> (Boolean) When sending messages, each part of the message is MIME-inspected in order to classify the `Content-Type:&#8216; and `Content-Transfer-Encoding:&#8216; (see <i>mime-encoding</i> that is required to send this part over mail transport, i.e., a computation rather similar to what the <a href="/docs/linux/man/1-file/">file</a>(1) command produces when used with the `--mime&#8217; option. </p>
<p> This classification however treats text files which are encoded in UTF-16 (seen for HTML files) and similar character sets as binary octet-streams, forcefully changing any `text/plain&#8217; or `text/html&#8217; specification to `application/octet-stream&#8217; : If that actually happens a yet unset charset MIME parameter is set to `binary&#8217; , effectively making it impossible for the receiving MUA to automatically interpret the contents of the part. </p>
<p> If this variable is set, and the data was unambiguously identified as text data at first glance (by a `.txt&#8217; or `.html&#8217; file extension), then the original `Content-Type:&#8216; will not be overwritten. </p>
 </dd>
<dt><i>mime-alternative-favour-rich</i></dt>
<dd> <p> (Boolean) If this variable is set then rich MIME alternative parts (e.g., HTML) will be preferred in favour of included plain text versions when displaying messages, provided that a handler exists which produces output that can be (re)integrated into S-nail&#8217;s normal visual display. </p>
 </dd>
<dt><i>mime-counter-evidence</i></dt>
<dd> <p> Normally the `Content-Type:&#8216; field is used to decide how to handle MIME parts. Some MUAs, however, do not use Sx The mime.types files (also see Sx HTML mail and MIME attachments ) or a similar mechanism to correctly classify content, but specify an unspecific MIME type ( `application/octet-stream&#8217; even for plain text attachments. If this variable is set then S-nail will try to re-classify such MIME message parts, if possible, for example via a possibly existing attachment filename. A non-empty value may also be given, in which case a number is expected, actually a carrier of bits, best specified as a binary value, like `0b1111&#8217; </p>
 </dd>
<ul>
<li> <p> If bit two is set (counting from 1, decimal 2) then the detected <code>mimetype</code> will be carried along with the message and be used for deciding which MIME handler is to be used, for example; when displaying such a MIME part the part-info will indicate the overridden content-type by showing a plus sign `+&#8216;  </li>
<li>  If bit three is set (decimal 4) then the counter-evidence is always produced and a positive result will be used as the MIME type, even forcefully overriding the parts given MIME type.  </li>
<li>  If bit four is set (decimal 8) as a last resort the actual content of `application/octet-stream&#8217; parts will be inspected, so that data which looks like plain text can be treated as such. This mode is even more relaxed when data is to be displayed to the user or used as a message quote (data consumers which mangle data for display purposes, which includes masking of control characters, for example).  </li>
</ul>
 </p>
<dt><i>mime-encoding</i></dt>
<dd> <p> The MIME `Content-Transfer-Encoding&#8217; to use in outgoing text messages and message parts, where applicable (7-bit clean text messages are without an encoding if possible): </p>
 </dd>
<dl>
<dt><code>`8bit&#8217; </code></dt>
<dd> <p> (Or&nbsp; `8b&#8217; 8-bit transport effectively causes the raw data be passed through unchanged, but may cause problems when transferring mail messages over channels that are not ESMTP (RFC 1869) compliant. Also, several input data constructs are not allowed by the specifications and may cause a different transfer-encoding to be used. By established rules and popular demand occurrences of `^From_&#8216; (see <i>mbox-rfc4155</i> will be MBOXO quoted (prefixed with greater-than sign `&gt;&#8216; ) instead of causing a non-destructive encoding like `quoted-printable&#8217; to be chosen, unless context (like message signing) requires otherwise. </p>
 </dd>
<dt><code>`quoted-printable&#8217; </code></dt>
<dd> <p> (Or&nbsp; `qp&#8217; Quoted-printable encoding is 7-bit clean and has the property that ASCII characters are passed through unchanged, so that an english message can be read as-is; it is also acceptable for other single-byte locales that share many characters with ASCII, for example ISO-8859-1. The encoding will cause a large overhead for messages in other character sets: for example it will require up to twelve (12) bytes to encode a single UTF-8 character of four (4) bytes. It is the default encoding. </p>
 </dd>
<dt><code>`base64&#8217; </code></dt>
<dd> <p> (Or&nbsp; `b64&#8217; This encoding is 7-bit clean and will always be used for binary data. This encoding has a constant input:output ratio of 3:4, regardless of the character set of the input data it will encode three bytes of input to four bytes of output. This transfer-encoding is not human readable without performing a decoding step. </p>
 </dd></dl>
<dt><i>mime-force-sendout</i></dt>
<dd> <p> (Boolean)[Option] Whenever it is not acceptable to fail sending out messages because of non-convertible character content this variable may be set. It will, as a last resort, classify the part content as `application/octet-stream&#8217; Please refer to the section Sx Character sets for the complete picture of character set conversion, and Sx HTML mail and MIME attachments for how to internally or externally handle part content. </p>
 </dd>
<dt><i>mimetypes-load-control</i></dt>
<dd> <p> Can be used to control which of Sx The mime.types files are loaded: if the letter `u&#8217; is part of the option value, then the user&#8217;s personal ~/.mime.types file will be loaded (if it exists); likewise the letter `s&#8217; controls loading of the system wide /etc/mime.types directives found in the user file take precedence, letter matching is case-insensitive. If this variable is not set S-nail will try to load both files. Incorporation of the S-nail-built-in MIME types cannot be suppressed, but they will be matched last (the order can be listed via <code>mimetype )</code> </p>
<p> More sources can be specified by using a different syntax: if the value string contains an equals sign `=&#8216; then it is instead parsed as a comma-separated list of the described letters plus `f=FILENAME&#8217; pairs; the given filenames will be expanded and loaded, and their content may use the extended syntax that is described in the section Sx The mime.types files . Directives found in such files always take precedence (are prepended to the MIME type cache). </p>
 </dd>
<dt><i>mta</i></dt>
<dd> <p> Select an alternate Mail-Transfer-Agent by either specifying the full pathname of an executable (a `file://&#8216; prefix may be given), or [Option]ally a SMTP aka SUBMISSION protocol URL [v15-compat]: </p>
<blockquote><p> <code>submissions://[user[:password]@]server[:port]</code> </p>
</blockquote>
<p> ([no v15-compat]: `[<a href="smtp://]server[:port]'">smtp://]server[:port]&#8216;</a> The default has been chosen at compile time. MTA data transfers are always performed in asynchronous child processes, and without supervision unless either the <i>sendwait</i> or the <i>verbose</i> variable is set. Also see <i>mta-bcc-ok</i> [Option]ally expansion of <a href="/docs/linux/man/5-aliases/">aliases</a>(5) can be performed by setting <i>mta-aliases</i> </p>
<p> For testing purposes there is the `test&#8217; pseudo-MTA, which dumps to standard output or optionally to a file, and honours <i>mbox-fcc-and-pcc</i> </p>
<blockquote><pre><code>$ echo text | s-nail -:/ -Smta=test -s ubject ex [at] am.ple
$ &lt;/dev/null s-nail -:/ -Smta=test://./xy ex [at] am.ple
</code></pre>
</blockquote>
<p> For a file-based MTA it may be necessary to set <i>mta-argv0</i> in in order to choose the right target of a modern mailwrapper(8) environment. It will be passed command line arguments from several possible sources: from the variable <i>mta-arguments</i> if set, from the command line if given and the variable <i>expandargv</i> allows their use. Argument processing of the MTA will be terminated with a -<code>-</code> separator. </p>
<p> The otherwise occurring implicit usage of the following MTA command line arguments can be disabled by setting the boolean variable <i>mta-no-default-arguments</i> (which will also disable passing -<code>-</code> to the MTA): -<code>i</code> (for not treating a line with only a dot `.&#8216; character as the end of input), -<code>m</code> (shall the variable <i>metoo</i> be set) and -<code>v</code> (if the <i>verbose</i> variable is set); in conjunction with the -<code>r</code> command line option or <i>r-option-implicit</i> -<code>f</code> as well as possibly -<code>F</code> will (not) be passed. </p>
<p> [Option]ally S-nail can send mail over SMTP aka SUBMISSION network connections to a single defined smart host by setting this variable to a SMTP or SUBMISSION URL (see Sx On URL syntax and credential lookup ) . An authentication scheme can be specified via the variable chain <i>smtp-auth</i> Encrypted network connections are [Option]ally available, the section Sx Encrypted network communication should give an overview and provide links to more information on this. Note that with some mail providers it may be necessary to set the <i>smtp-hostname</i> variable in order to use a specific combination of <i>from</i> <i>hostname</i> and <i>mta</i> Network communication socket timeouts are configurable via <i>socket-connect-timeout</i> All generated network traffic may be proxied over a SOCKS <i>socks-proxy</i> it can be logged by setting <i>verbose</i> twice. The following SMTP variants may be used: </p>
 </dd>
<ul>
<li> <p> The plain SMTP protocol (RFC 5321) that normally lives on the server port 25 and requires setting the <i>smtp-use-starttls</i> variable to enter a TLS encrypted session state. Assign a value like [v15-compat] `<a href="smtp://[user[:password]@]server[:port]'">smtp://[user[:password]@]server[:port]&#8216;</a> ([no v15-compat] `<a href="smtp://server[:port]'">smtp://server[:port]&#8216;</a> ) to choose this protocol.  </li>
<li>  The so-called SMTPS which is supposed to live on server port 465 and is automatically TLS secured. Unfortunately it never became a standardized protocol and may thus not be supported by your hosts network service database - in fact the port number has already been reassigned to other protocols! </p>
<p> SMTPS is nonetheless a commonly offered protocol and thus can be chosen by assigning a value like [v15-compat] `<a href="smtps://[user[:password]@]server[:port]'">smtps://[user[:password]@]server[:port]&#8216;</a> ([no v15-compat] `<a href="smtps://server[:port]'">smtps://server[:port]&#8216;</a> ) ; due to the mentioned problems it is usually necessary to explicitly specify the port as `:465&#8217; , however.  </li>
<li>  The SUBMISSION protocol (RFC 6409) lives on server port 587 and is identically to the SMTP protocol from S-nail&#8217;s point of view; it requires setting <i>smtp-use-starttls</i> to enter a TLS secured session state; e.g., [v15-compat] `submission://[user[:password]@]server[:port]&#8216;  </li>
<li>  The SUBMISSIONS protocol (RFC 8314) that lives on server port 465 and is TLS secured by default. It can be chosen by assigning a value like [v15-compat] `submissions://[user[:password]@]server[:port]&#8216; Due to the problems mentioned for SMTPS above and the fact that SUBMISSIONS is new and a successor that lives on the same port as the historical engineering mismanagement named SMTPS, it is usually necessary to explicitly specify the port as `:465&#8217;  </li>
</ul>
 </p>
<dt><i>mta-aliases</i></dt>
<dd> <p> [Option] If set to a path pointing to a text file in valid MTA (Postfix) <a href="/docs/linux/man/5-aliases/">aliases</a>(5) format, the file is loaded and cached (manageable with <code>mtaaliases )</code> and henceforth plain `name&#8217; (see <i>expandaddr</i> message receiver names are recursively expanded as a last expansion step, after the distribution lists which can be created with <code>alias</code> Constraints on aliases5 content support: only local addresses (names) which are valid usernames ( `[a-z_][a-z0-9_-]*[$]?&#8216; are treated as expandable aliases, and [v15 behaviour may differ] `:include:/file/name&#8217; directives are not supported. By including `-name&#8217; in <i>expandaddr</i> it can be asserted that only expanded names (mail addresses) are passed through to the MTA. </p>
 </dd>
<dt><i>mta-arguments</i></dt>
<dd> <p> Arguments to pass through to a file-based <i>mta</i> (Mail-Transfer-Agent), parsed according to Sx Shell-style argument quoting into an array of arguments which will be joined onto MTA options from other sources, for example `?&#8216; wysh set mta-arguments=&#8216;-t -X /tmp/my log&#8217; . </p>
 </dd>
<dt><i>mta-no-default-arguments</i></dt>
<dd> <p> (Boolean) Avoids passing standard command line options to a file-based <i>mta</i> (please see there). </p>
 </dd>
<dt><i>mta-no-receiver-arguments</i></dt>
<dd> <p> (Boolean) By default all receiver addresses will be passed as command line options to a file-based <i>mta</i> Setting this variable disables this behaviour to aid those MTAs which employ special treatment of such arguments. Doing so can make it necessary to pass a -<code>t</code> via <i>mta-arguments</i> to testify the MTA that it should use the passed message as a template. </p>
 </dd>
<dt><i>mta-argv0</i></dt>
<dd> <p> Many systems use a so-called mailwrapper(8) environment to ensure compatibility with <a href="/docs/linux/man/1-sendmail/">sendmail</a>(1). This works by inspecting the name that was used to invoke the mail delivery system. If this variable is set then the mailwrapper (the program that is actually executed when calling the file-based <i>mta</i> will treat its contents as that name. </p>
 </dd>
<dt><i>mta-bcc-ok</i></dt>
<dd> <p> (Boolean) In violation of RFC 5322 some MTAs do not remove `Bcc:&#8216; header lines from transported messages after having noted the respective receivers for addressing purposes. (The MTAs Exim and Courier for example require the command line option -<code>t</code> to enforce removal.) Unless this is set corresponding receivers are addressed by protocol-specific means or MTA command line options only, the header itself is stripped before being sent over the wire. </p>
 </dd>
<dt><i>netrc-lookup-USER [at] HOST , netrc-lookup-HOST , netrc-lookup</i></dt>
<dd> <p> (Boolean)[v15-compat][Option] Used to control usage of the user&#8217;s ~/.netrc file for lookup of account credentials, as documented in the section Sx On URL syntax and credential lookup and for the command <code>netrc</code> the section Sx The .netrc file documents the file format. Also see <i>netrc-pipe</i> </p>
 </dd>
<dt><i>netrc-pipe</i></dt>
<dd> <p> [v15-compat][Option] When ~/.netrc is loaded (see <code>netrc</code> and <i>netrc-lookup</i> then S-nail will read the output of a shell pipe instead of the user&#8217;s ~/.netrc file if this variable is set (to the desired shell command). This can be used to, for example, store ~/.netrc in encrypted form: `?&#8216; set netrc-pipe=&#8216;gpg -qd ~/.netrc.pgp&#8217; . </p>
 </dd>
<dt><i>newfolders</i></dt>
<dd> <p> [Option] If this variable has the value `maildir&#8217; , newly created local folders will be in Maildir instead of MBOX format. </p>
 </dd>
<dt><i>newmail</i></dt>
<dd> <p> Checks for new mail in the current folder each time the prompt is shown. A Maildir folder must be re-scanned to determine if new mail has arrived. If this variable is set to the special value `nopoll&#8217; then a Maildir folder will not be rescanned completely, but only timestamp changes are detected. Maildir folders are [Option]al. </p>
 </dd>
<dt><i>outfolder</i></dt>
<dd> <p> (Boolean) Causes a non-absolute filename specified in <i>record</i> as well as the sender-based filenames of the <code>Copy</code> <code>Save</code> <code>Followup</code> and <code>followup</code> commands to be interpreted relative to the <i>folder</i> directory rather than relative to the current directory. </p>
 </dd>
<dt><i>on-account-cleanup-ACCOUNT , on-account-cleanup</i></dt>
<dd> <p> Macro hook which will be called once an <code>account</code> is left, as the very last step before unrolling per-account <code>localopts</code> This hook is run even in case of fatal errors, including those generated by switching to the account as such, and it is advisable to perform only absolutely necessary actions, like cleaning up <code>alternates</code> for example. The specialized form is used in favour of the generic one if found. </p>
 </dd>
<dt><i>on-compose-cleanup</i></dt>
<dd> <p> Macro hook which will be called after the message has been sent (or not, in case of failures), as the very last step before unrolling compose mode <code>localopts</code> This hook is run even in case of fatal errors, and it is advisable to perform only absolutely necessary actions, like cleaning up <code>alternates</code> for example. </p>
<p> For compose mode hooks that may affect the message content please see <i>on-compose-enter , on-compose-leave , on-compose-splice</i> [v15 behaviour may differ] This hook exists because <code>alias , alternates , commandalias , shortcut</code> to name a few, are neither covered by <code>localopts</code> nor by <code>local</code> changes applied in compose mode will continue to be in effect thereafter. </p>
 </dd>
<dt><i>on-compose-enter , on-compose-leave</i></dt>
<dd> <p> Macro hooks which will be called once compose mode is entered, and after composing has been finished, respectively; the exact order of the steps taken is documented for <code>~.</code> one of the Sx COMMAND ESCAPES . Context about the message being worked on can be queried via <code>digmsg</code> <code>localopts</code> are enabled for these hooks, and changes on variables will be forgotten after the message has been sent. <i>on-compose-cleanup</i> can be used to perform other necessary cleanup steps. </p>
<p> Here is an example that injects a signature via <i>message-inject-tail</i> instead using <i>on-compose-splice</i> to simply inject the file of desire via <code>~&lt;</code> or <code>~&lt;!</code> may be a better approach. </p>
<blockquote><pre><code>define t_ocl {
  vput ! i cat ~/.mysig
  if $? -eq 0
     vput csop message-inject-tail trim-end $i
  end
  # Alternatively
  readctl create ~/.mysig
  if $? -eq 0
    readall i
    if $? -eq 0
      vput csop message-inject-tail trim-end $i
    end
    readctl remove ~/.mysig
  end
}
set on-compose-leave=t_ocl
</code></pre>
</blockquote>
 </dd>
<dt><i>on-compose-splice , on-compose-splice-shell</i></dt>
<dd> <p> These hooks run once the normal compose mode is finished, but before the <i>on-compose-leave</i> macro hook is called etc. Both hooks will be executed in a subprocess, with their input and output connected to S-nail such that they can act as if they would be an interactive user. The difference in between them is that the latter is a <code>SHELL</code> command, whereas the former is a normal <code>define d macro, but which is restricted to a small set of commands (the</code> <i>verbose</i> output of for example <code>list</code> will indicate said capability). <code>localopts</code> are enabled for these hooks (in the parent process), causing any setting to be forgotten after the message has been sent; <i>on-compose-cleanup</i> can be used to perform other cleanup as necessary. </p>
<p> During execution of these hooks S-nail will temporarily forget whether it has been started in interactive mode, (a restricted set of) Sx COMMAND ESCAPES will always be available, and for guaranteed reproducibilities sake <i>escape</i> and <i>ifs</i> will be set to their defaults. The compose mode command <code>~^</code> has been especially designed for scriptability (via these hooks). The first line the hook will read on its standard input is the protocol version of said command escape, currently ``0 0 2&#8217;&#8216; backward incompatible protocol changes have to be expected. </p>
<p> Care must be taken to avoid deadlocks and other false control flow: if both involved processes wait for more input to happen at the same time, or one does not expect more input but the other is stuck waiting for consumption of its output, etc. There is no automatic synchronization of the hook: it will not be stopped automatically just because it, e.g., emits `~x&#8217; The hooks will however receive a termination signal if the parent enters an error condition. [v15 behaviour may differ] Protection against and interaction with signals is not yet given; it is likely that in the future these scripts will be placed in an isolated session, which is signalled in its entirety as necessary. </p>
<blockquote><pre><code>define ocs_signature {
  read version
  echo '~&lt; ~/.mysig' # '~&lt;! fortune pathtofortunefile'
}
set on-compose-splice=ocs_signature
wysh set on-compose-splice-shell=$'\
  read version;\
  printf &quot;hello $version! Headers: &quot;;\
  echo \'~^header list\';\
  read status result;\
  echo &quot;status=$status result=$result&quot;;\
  '
define ocsm {
  read version
  echo Splice protocol version is $version
  echo '~^h l'; read hl; vput csop es subs &quot;${hl}&quot; 0 1
  if &quot;$es&quot; != 2
    echoerr 'Cannot read header list'; echo '~x'; xit
  endif
  if &quot;$hl&quot; !%?case ' cc'
    echo '~^h i cc &quot;Diet is your &lt;mirr.or&gt;&quot;'; read es;\
      vput csop es substring &quot;${es}&quot; 0 1
    if &quot;$es&quot; != 2
      echoerr 'Cannot insert Cc: header'; echo '~x'
      # (no xit, macro finishes anyway)
    endif
  endif
}
set on-compose-splice=ocsm
</code></pre>
</blockquote>
 </dd>
<dt><i>on-history-addition</i></dt>
<dd> <p> This hook will be called if an entry is about to be added to the <code>history</code> of the MLE, as documented in Sx On terminal control and line editor . It will be called with three arguments: the first is the name of the input context (see <code>bind )</code> the second is either an empty string or the matching <i>history-gabby</i> type, and the third being the complete command line to be added. The entry will not be added to history if the hook uses a non-0 <code>return</code> [v15 behaviour may differ] A future version will give the expanded command name as the third argument, followed by the tokenized command line as parsed in the remaining arguments, the first of which is the original unexpanded command name; i.e., one may do `<code>shift</code> &#8216; Ns 4 and will then be able to access the positional parameters as usual via <i>* , # , 1</i> etc. </p>
 </dd>
<dt><i>on-main-loop-tick</i></dt>
<dd> <p> This hook will be called whenever the program&#8217;s main event loop is about to read the next input line. Note variable and other changes it performs are not scoped as via <code>localopts</code> </p>
 </dd>
<dt><i>on-program-exit</i></dt>
<dd> <p> This hook will be called when the program exits, whether via <code>exit</code> or <code>quit</code> or because the send mode is done. <code>Note:</code> this runs late and so terminal settings etc. are already teared down. </p>
 </dd>
<dt><i>on-resend-cleanup</i></dt>
<dd> <p> [v15 behaviour may differ] Identical to <i>on-compose-cleanup</i> but is only triggered by <code>resend</code> </p>
 </dd>
<dt><i>on-resend-enter</i></dt>
<dd> <p> [v15 behaviour may differ] Identical to <i>on-compose-enter</i> but is only triggered by <code>resend</code> currently there is no <code>digmsg</code> support, for example. </p>
 </dd>
<dt><i>page</i></dt>
<dd> <p> (Boolean) If set, each message feed through the command given for <code>pipe</code> is followed by a formfeed character `\f&#8217; </p>
 </dd>
<dt><i>password-USER [at] HOST , password-HOST , password</i></dt>
<dd> <p> [v15-compat] Variable chain that sets a password, which is used in case none has been given in the protocol and account-specific URL; as a last resort S-nail will ask for a password on the user&#8217;s terminal if the authentication method requires a password. Specifying passwords in a startup file is generally a security risk; the file should be readable by the invoking user only. </p>
 </dd>
<dt><i>password-USER [at] HOST</i></dt>
<dd> <p> [no v15-compat] (see the chain above for [v15-compat]) Set the password for `USER&#8217; when connecting to `HOST&#8217; If no such variable is defined for a host, the user will be asked for a password on standard input. Specifying passwords in a startup file is generally a security risk; the file should be readable by the invoking user only. </p>
 </dd>
<dt><i>piperaw</i></dt>
<dd> <p> (Boolean) Send messages to the <code>pipe</code> command without performing MIME and character set conversions. </p>
 </dd>
<dt><i>pipe-EXTENSION</i></dt>
<dd> <p> Identical to <i>pipe-TYPE/SUBTYPE</i> except that `EXTENSION&#8217; (normalized to lowercase using character mappings of the ASCII charset) denotes a file extension, for example `xhtml&#8217; Handlers registered using this method take precedence. </p>
 </dd>
<dt><i>pipe-TYPE/SUBTYPE</i></dt>
<dd> <p> A MIME message part identified as `TYPE/SUBTYPE&#8217; (case-insensitive, normalized to lowercase using character mappings of the ASCII charset) is displayed or quoted, its text is filtered through the value of this variable interpreted as a shell command. Unless noted only parts displayable as inline plain text (see <code>copiousoutput</code> are covered, other MIME parts will only be considered by and for <code>mimeview</code> </p>
<p> The special value question mark `?&#8216; forces interpretation of the message part as plain text, for example `set&#8217; pipe-application/xml=? . (This can also be achieved by adding a MIME type-marker via <code>mimetype .</code> [Option]ally MIME type handlers may be defined via Sx The Mailcap files to which should be referred to for documentation of flags like <code>copiousoutput</code> Question mark is indeed a trigger character to indicate flags that adjust behaviour and usage of the rest of the value, the shell command, for example: </p>
<blockquote><pre><code>? set pipe-X/Y='?!++=? vim ${MAILX_FILENAME_TEMPORARY}'
</code></pre>
</blockquote>
 </dd>
<dl>
<dt><code>`*&#8216; </code></dt>
<dd> <p> The command output can be reintegrated into this MUA&#8217;s normal processing: <code>copiousoutput</code> Implied when using a plain `&#8216; </p>
 </dd>
<dt><code>`#&#8216; </code></dt>
<dd> <p> Only use this handler for display, not for quoting a message: <code>x-mailx-noquote</code> </p>
 </dd>
<dt><code>`&amp;&#8216; </code></dt>
<dd> <p> Run the command asynchronously, do not wait for the handler to exit: <code>x-mailx-async</code> The standard output of the command will go to /dev/null </p>
 </dd>
<dt><code>`!&#8216; </code></dt>
<dd> <p> The command must be run on an interactive terminal, the terminal will temporarily be released for it to run: <code>needsterminal</code> </p>
 </dd>
<dt><code>`+&#8216; </code></dt>
<dd> <p> Request creation of a zero-sized temporary file, the absolute pathname of which will be made accessible via the environment variable <code>MAILX_FILENAME_TEMPORARY</code> <code>x-mailx-tmpfile</code> If given twice then the file will be unlinked automatically by S-nail when the command loop is entered again at latest: <code>x-mailx-tmpfile-unlink</code> it is an error to use automatic deletion in conjunction with <code>x-mailx-async</code> </p>
 </dd>
<dt><code>`=&#8216; </code></dt>
<dd> <p> Normally the MIME part content is passed to the handler via standard input; with this the data will instead be written into <code>MAILX_FILENAME_TEMPORARY</code> ( <code>x-mailx-tmpfile-fill</code> the creation of which is implied; in order to cause automatic deletion of the temporary file two plus signs `++&#8216; still have to be used. </p>
 </dd>
<dt><code>`t&#8217; </code></dt>
<dd> <p> Text type-marker: display this as normal plain text (for type-markers: Sx The mime.types files ) . Identical to only giving plain `?&#8216; , implies <code>copiousoutput</code> </p>
 </dd>
<dt><code>`h&#8217; </code></dt>
<dd> <p> [Option] HTML type-marker: display via built-in HTML-to-text filter. Implies <code>copiousoutput</code> </p>
 </dd>
<dt><code>`?&#8216; </code></dt>
<dd> <p> To avoid ambiguities with normal shell command content another question mark can be used to forcefully terminate interpretation of remaining characters. (Any character not in this list will have the same effect.) </p>
 </dd></dl>
<p> Some information about the MIME part to be displayed is embedded into the environment of the shell command: </p>
<dl>
<dt><code>MAILX_CONTENT</code></dt>
<dd> <p> The MIME content-type of the part, if known, the empty string otherwise. </p>
 </dd>
<dt><code>MAILX_CONTENT_EVIDENCE</code></dt>
<dd> <p> If <i>mime-counter-evidence</i> includes the carry-around-bit (2), then this will be set to the detected MIME content-type; not only then identical to <code>MAILX_CONTENT</code> otherwise. </p>
 </dd>
<dt><code>MAILX_EXTERNAL_BODY_URL</code></dt>
<dd> <p> MIME parts of type `message/external-body&#8217; access-type=url will store the access URL in this variable, it is empty otherwise. URL targets should not be activated automatically, without supervision. </p>
 </dd>
<dt><code>MAILX_FILENAME</code></dt>
<dd> <p> The filename, if any is set, the empty string otherwise. </p>
 </dd>
<dt><code>MAILX_FILENAME_GENERATED</code></dt>
<dd> <p> A random string. </p>
 </dd>
<dt><code>MAILX_FILENAME_TEMPORARY</code></dt>
<dd> <p> If temporary file creation has been requested through the command prefix this variable will be set and contain the absolute pathname of the temporary file. </p>
 </dd></dl>
<dt><i>pop3-auth-USER [at] HOST , pop3-auth-HOST , pop3-auth</i></dt>
<dd> <p> [Option][v15-compat] Variable chain that sets the POP3 authentication method. Supported are the default `plain&#8217; , [v15-compat] `oauthbearer&#8217; (see Sx FAQ entry Sx But, how about XOAUTH2 / OAUTHBEARER? ) , as well as [v15-compat] `external&#8217; and `externanon&#8217; for TLS secured connections which pass a client certificate via <i>tls-config-pairs</i> There may be the [Option]al method [v15-compat] `gssapi&#8217; `externanon&#8217; does not need any user credentials, `external&#8217; and `gssapi&#8217; need a <i>user</i> the remains also require a <i>password</i> `externanon&#8217; solely builds upon the credentials passed via a client certificate, and is usually the way to go since tested servers do not actually follow RFC 4422, and fail if additional credentials are actually passed. Unless <i>pop3-no-apop</i> is set the `plain&#8217; method will [Option]ally be replaced with APOP if possible (see there). </p>
 </dd>
<dt><i>pop3-bulk-load-USER [at] HOST , pop3-bulk-load-HOST , pop3-bulk-load</i></dt>
<dd> <p> (Boolean)[Option] When accessing a POP3 server S-nail loads the headers of the messages, and only requests the message bodies on user request. For the POP3 protocol this means that the message headers will be downloaded twice. If this variable is set then S-nail will download only complete messages from the given POP3 server(s) instead. </p>
 </dd>
<dt><i>pop3-keepalive-USER [at] HOST , pop3-keepalive-HOST , pop3-keepalive</i></dt>
<dd> <p> [Option] POP3 servers close the connection after a period of inactivity; the standard requires this to be at least 10 minutes, but practical experience may vary. Setting this variable to a numeric value greater than `0&#8217; causes a `NOOP&#8217; command to be sent each value seconds if no other operation is performed. </p>
 </dd>
<dt><i>pop3-no-apop-USER [at] HOST , pop3-no-apop-HOST , pop3-no-apop</i></dt>
<dd> <p> (Boolean)[Option] Unless this variable is set the MD5 based `APOP&#8217; authentication method will be used instead of a chosen `plain&#8217; <i>pop3-auth</i> when connecting to a POP3 server that advertises support. The advantage of `APOP&#8217; is that only a single packet is sent for the user/password tuple. (Originally also that the password is not sent in clear text over the wire, but for one MD5 does not any longer offer sufficient security, and then today transport is almost ever TLS secured.) Note that <i>pop3-no-apop-HOST</i> requires [v15-compat]. </p>
 </dd>
<dt><i>pop3-use-starttls-USER [at] HOST , pop3-use-starttls-HOST , pop3-use-starttls</i></dt>
<dd> <p> (Boolean)[Option] Causes S-nail to issue a `STLS&#8217; command to make an unencrypted POP3 session TLS encrypted. This functionality is not supported by all servers, and is not used if the session is already encrypted by the POP3S method. Note that <i>pop3-use-starttls-HOST</i> requires [v15-compat]. </p>
 </dd>
<dt><i>posix</i></dt>
<dd> <p> (Boolean) This flag enables POSIX mode, which changes behaviour of S-nail where that deviates from standardized behaviour. It is automatically squared with the environment variable <code>POSIXLY_CORRECT</code> changing the one will adjust the other. The following behaviour is covered and enforced by this mechanism: </p>
 </dd>
<ul>
<li> <p> In non-interactive mode, any error encountered while loading resource files during program startup will cause a program exit, whereas in interactive mode such errors will stop loading of the currently loaded (stack of) file(s, i.e., recursively). These exits can be circumvented on a per-command base by using <code>ignerr</code> one of the Sx Command modifiers , for each command which shall be allowed to fail.  </li>
<li>  <code>alternates</code> will replace the list of alternate addresses instead of appending to it. In addition alternates will only be honoured for any sort of message <code>reply</code> and for aliases.  </li>
<li>  The variable inserting Sx COMMAND ESCAPES <code>~A</code> <code>~a</code> <code>~I</code> and <code>~i</code> will expand embedded character sequences `\t&#8217; horizontal tabulator and `\n&#8217; line feed. [v15 behaviour may differ] For compatibility reasons this step will always be performed.  </li>
<li>  Reading in messages via <code>~f</code> ( Sx COMMAND ESCAPES will use the `type&#8217; not the `forward&#8217; <code>headerpick</code> selection.  </li>
<li>  Upon changing the active <code>folder</code> no summary of <code>headers</code> will be displayed even if <i>header</i> is set.  </li>
<li>  Setting <i>ignoreeof</i> implies the behaviour described by <i>dot</i>  </li>
<li>  The variable <i>keep</i> is extended to cover any empty mailbox, not only empty Sx primary system mailbox Ns es: they will be removed when they are left in empty state otherwise.  </li>
<li>  Each command has an exit <i>?</i> and error <i>!</i> status that overwrites that of the last command. In POSIX mode the program exit status will signal failure regardless unless all messages were successfully sent out to the <i>mta</i> also see <i>sendwait</i>  </li>
</ul>
 </p>
<dt><i>print-alternatives</i></dt>
<dd> <p> (Boolean) When a MIME message part of type `multipart/alternative&#8217; is displayed and it contains a subpart of type `text/plain&#8217; , other parts are normally discarded. Setting this variable causes all subparts to be displayed, just as if the surrounding part was of type `multipart/mixed&#8217; </p>
 </dd>
<dt><i>prompt</i></dt>
<dd> <p> The string used as a prompt in interactive mode. Whenever the variable is evaluated the value is treated as if specified within dollar-single-quotes (see Sx Shell-style argument quoting ) . This (post-assignment, i.e., second) expansion can be used to embed status information, for example <i>?</i> <i>!</i> <i>account</i> or <i>mailbox-display</i> </p>
<p> In order to embed characters which should not be counted when calculating the visual width of the resulting string, enclose the characters of interest in a pair of reverse solidus escaped brackets: `\[\E[0m\]&#8216; ; a slot for coloured prompts is also available with the [Option]al command <code>colour</code> Prompting may be prevented by setting this to the null string (aka `set&#8217; noprompt ) . </p>
 </dd>
<dt><i>prompt2</i></dt>
<dd> <p> This string is used for secondary prompts, but is otherwise identical to <i>prompt</i> The default is `..&nbsp;&#8216; </p>
 </dd>
<dt><i>quiet</i></dt>
<dd> <p> (Boolean) Suppresses the printing of the version when first invoked. </p>
 </dd>
<dt><i>quote</i></dt>
<dd> <p> If set messages processed by variants of <code>followup</code> and <code>reply</code> will start with the original message, lines of which prefixed by <i>indentprefix</i> taking into account <i>quote-chars</i> and <i>quote-fold</i> No headers will be quoted when set without value or for `noheading&#8217; , for `headers&#8217; the `type&#8217; <code>headerpick</code> selection will be included in the quote, `allbodies&#8217; embeds the (body) contents of all MIME parts, and `allheaders&#8217; also includes all headers. The quoted message will be enclosed by the expansions of <i>quote-inject-head</i> and <i>quote-inject-tail</i> Also see <i>quote-add-cc</i> <i>quote-as-attachment</i> and <code>~Q</code> one of the Sx COMMAND ESCAPES . </p>
 </dd>
<dt><i>quote-add-cc</i></dt>
<dd> <p> (Boolean) Whether senders of messages quoted via <code>~Q</code> shall be made members of the carbon copies `Cc:&#8216; list. </p>
 </dd>
<dt><i>quote-as-attachment</i></dt>
<dd> <p> (Boolean) Add the original message in its entirety as a `message/rfc822&#8217; MIME attachment when replying to a message. Note this works regardless of the setting of <i>quote</i> </p>
 </dd>
<dt><i>quote-chars</i></dt>
<dd> <p> Can be set to a string consisting of non-whitespace ASCII characters which shall be treated as quotation leaders, the default being `&gt;|}:&#8216; </p>
 </dd>
<dt><i>quote-fold</i></dt>
<dd> <p> [Option] Can be set in addition to <i>indentprefix</i> and creates a more fancy quotation in that leading quotation characters ( <i>quote-chars</i> are compressed and overlong lines are folded. <i>quote-fold</i> can be set to either one, two or three (space separated) numeric values, which are interpreted as the maximum (goal) and the minimum line length, respectively, in a spirit rather equal to the <a href="/docs/linux/man/1-fmt/">fmt</a>(1) program, but line- instead of paragraph-based. The third value is used as the maximum line length instead of the first if no better break point can be found; it is ignored unless it is larger than the minimum and smaller than the maximum. If not set explicitly the minimum will reflect the goal algorithmically. The goal cannot be smaller than the length of <i>indentprefix</i> plus some additional pad; necessary adjustments take place silently. </p>
 </dd>
<dt><i>quote-inject-head , quote-inject-tail</i></dt>
<dd> <p> The strings to put before and after the text of a <i>quote </i><code>d message, if non-empty, and respectively.</code> The former defaults to `%f&#8217; wrote:\n\n . Special format directives will be expanded if possible, and if so configured the output will be folded according to <i>quote-fold</i> Format specifiers in the given strings start with a percent sign `%&#8216; and expand values of the original message, unless noted otherwise. Note that names and addresses are not subject to the setting of <i>showto</i> Valid format specifiers are: </p>
 </dd>
<dl>
<dt><code>`%%&#8216; </code></dt>
<dd> <p> A plain percent sign. </p>
 </dd>
<dt><code>`%a&#8217; </code></dt>
<dd> <p> The address(es) of the sender(s). </p>
 </dd>
<dt><code>`%d&#8217; </code></dt>
<dd> <p> The date found in the `Date:&#8216; header of the message when <i>datefield</i> is set (the default), otherwise the date when the message was received. Formatting can be controlled by assigning a <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format string to <i>datefield</i> (and <i>datefield-markout-older )</i> </p>
 </dd>
<dt><code>`%f&#8217; </code></dt>
<dd> <p> The full name(s) (name and address, as given) of the sender(s). </p>
 </dd>
<dt><code>`%i&#8217; </code></dt>
<dd> <p> The `Message-ID:&#8216; </p>
 </dd>
<dt><code>`%n&#8217; </code></dt>
<dd> <p> The real name(s) of the sender(s) if there is one and <i>showname</i> allows usage, the address(es) otherwise. </p>
 </dd>
<dt><code>`%r&#8217; </code></dt>
<dd> <p> The senders real name(s) if there is one, the address(es) otherwise. </p>
 </dd></dl>
<dt><i>r-option-implicit</i></dt>
<dd> <p> (Boolean) Setting this option evaluates the contents of <i>from</i> (or, if that contains multiple addresses, <i>sender</i> and passes the results onto the used (file-based) MTA as described for the -<code>r</code> option (empty argument case). </p>
 </dd>
<dt><i>recipients-in-cc</i></dt>
<dd> <p> (Boolean) When doing a <code>reply</code> the original `From:&#8216; and `To:&#8216; as well as addressees which possibly came in via `Reply-To:&#8216; and `Mail-Followup-To:&#8216; are by default merged into the new `To:&#8216; If this variable is set a sensitive algorithm tries to place in `To:&#8216; only the sender of the message being replied to, others are placed in `Cc:&#8216; </p>
 </dd>
<dt><i>record</i></dt>
<dd> <p> Unless this variable is defined, no copies of outgoing mail will be saved. If defined it gives the pathname, subject to the usual Sx Filename transformations , of a folder where all new, replied-to or forwarded messages are saved: when saving to this folder fails the message is not sent, but instead <i>save </i><code>d to</code> <code>DEAD</code> The standard defines that relative (fully expanded) paths are to be interpreted relative to the current directory ( <code>cwd</code> to force interpretation relative to <i>folder</i> <i>outfolder</i> needs to be set in addition. </p>
 </dd>
<dt><i>record-files</i></dt>
<dd> <p> (Boolean) If this variable is set the meaning of <i>record</i> will be extended to cover messages which target only file and pipe recipients (see <i>expandaddr )</i> These address types will not appear in recipient lists unless <i>add-file-recipients</i> is also set. </p>
 </dd>
<dt><i>record-resent</i></dt>
<dd> <p> (Boolean) If this variable is set the meaning of <i>record</i> will be extended to also cover the <code>resend</code> and <code>Resend</code> commands. </p>
 </dd>
<dt><i>reply-in-same-charset</i></dt>
<dd> <p> (Boolean) If this variable is set S-nail first tries to use the same character set of the original message for replies. If this fails, the mechanism described in Sx Character sets is evaluated as usual. </p>
 </dd>
<dt><i>reply-strings</i></dt>
<dd> <p> Can be set to a comma-separated list of (case-insensitive according to ASCII rules) strings which shall be recognized in addition to the built-in strings as `Subject:&#8216; reply message indicators - built-in are `Re:&#8216; , which is mandated by RFC 5322, as well as the german `Aw:&#8216; , `Antw:&#8216; , and the `Wg:&#8216; which often has been seen in the wild; I.e., the separating colon has to be specified explicitly. </p>
 </dd>
<dt><i>reply-to</i></dt>
<dd> <p> A list of addresses to put into the `Reply-To:&#8216; field of the message header. Members of this list are handled as if they were in the <code>alternates</code> list. </p>
 </dd>
<dt><i>replyto</i></dt>
<dd> <p> [Obsolete] Variant of <i>reply-to</i> </p>
 </dd>
<dt><i>reply-to-honour</i></dt>
<dd> <p> Controls whether a `Reply-To:&#8216; header is honoured when replying to a message via <code>reply</code> or <code>Lreply</code> This is a Sx quadoption ; if set without a value it defaults to ``yes&#8217;&#8216; </p>
 </dd>
<dt><i>reply-to-swap-in</i></dt>
<dd> <p> Standards like DKIM and (in conjunction with) DMARC caused many Sx Mailing lists to use sender address rewriting in the style of `Name&#8217; via List &lt;list [at] address&gt; , where the original sender address often being placed in `Reply-To:&#8216; If this is set and a `Reply-To:&#8216; exists, and consists of only one addressee (!), then that is used in place of the pretended sender. This works independently from <i>reply-to-honour</i> The optional value, a comma-separated list of strings, offers more fine-grained control on when swapping shall be used; for now supported is <i>mlist</i> here swapping occurs if the sender is a mailing-list as defined by <code>mlist</code> </p>
 </dd>
<dt><i>rfc822-body-from_</i></dt>
<dd> <p> (Boolean) This variable can be used to force displaying a so-called `From_&#8216; line for messages that are embedded into an envelope mail via the `message/rfc822&#8217; MIME mechanism, for more visual convenience, also see <i>mbox-rfc4155</i> </p>
 </dd>
<dt><i>save</i></dt>
<dd> <p> (Boolean) Enable saving of (partial) messages in <code>DEAD</code> upon interrupt or delivery error. </p>
 </dd>
<dt><i>screen</i></dt>
<dd> <p> The number of lines that represents a ``screenful&#8217;&#8216; of lines, used in <code>headers</code> summary display, <code>from</code> <code>search ing, message</code> <code>top line display and scrolling via</code> <code>z</code> If this variable is not set S-nail falls back to a calculation based upon the detected terminal window size and the baud rate: the faster the terminal, the more will be shown. Overall screen dimensions and pager usage is influenced by the environment variables <code>COLUMNS</code> and <code>LINES</code> and the variable <i>crt</i> </p>
 </dd>
<dt><i>searchheaders</i></dt>
<dd> <p> (Boolean) Expand message list specifiers in the form `/x:y&#8217; to all messages containing the substring ``y&#8217;&#8216; in the header field `x&#8217; The string search is case insensitive. </p>
 </dd>
<dt><i>sendcharsets</i></dt>
<dd> <p> [Option] A comma-separated list of character set names that can be used in outgoing internet mail. The value of the variable <i>charset-8bit</i> is automatically appended to this list of character sets. If no character set conversion capabilities are compiled into S-nail then the only supported charset is <i>ttycharset</i> Also see <i>sendcharsets-else-ttycharset</i> and refer to the section Sx Character sets for the complete picture of character set conversion in S-nail. </p>
 </dd>
<dt><i>sendcharsets-else-ttycharset</i></dt>
<dd> <p> (Boolean)[Option] If this variable is set, but <i>sendcharsets</i> is not, then S-nail acts as if <i>sendcharsets</i> had been set to the value of the variable <i>ttycharset</i> In effect this combination passes through the message data in the character set of the current locale encoding: therefore mail message text will be (assumed to be) in ISO-8859-1 encoding when send from within a ISO-8859-1 locale, and in UTF-8 encoding when send from within an UTF-8 locale. </p>
<p> The 8-bit fallback <i>charset-8bit</i> never comes into play as <i>ttycharset</i> is implicitly assumed to be 8-bit and capable to represent all files the user may specify (as is the case when no character set conversion support is available in S-nail and the only supported character set is <i>ttycharset</i> see Sx Character sets ) . This might be a problem for scripts which use the suggested `LC_ALL=C&#8217; setting, since in this case the character set is US-ASCII by definition, so that it is better to also override <i>ttycharset</i> then; and/or do something like the following in the resource file: </p>
<blockquote><pre><code># Avoid ASCII &quot;propagates to 8-bit&quot; when scripting
\if ! t &amp;&amp; &quot;$LC_ALL&quot; != C &amp;&amp; &quot;$LC_CTYPE&quot; != C
  \set sendcharsets-else-ttycharset
\end
</code></pre>
</blockquote>
 </dd>
<dt><i>sender</i></dt>
<dd> <p> An address that is put into the `Sender:&#8216; field of outgoing messages, quoting RFC 5322: the mailbox of the agent responsible for the actual transmission of the message. This field should normally not be used unless the <i>from</i> field contains more than one address, on which case it is required. [v15 behaviour may differ] Please expect automatic management of the <i>from</i> and <i>sender</i> relationship. Dependent on the context this address is handled as if it were in the list of <code>alternates</code> Also see -<code>r</code> <i>r-option-implicit</i> </p>
 </dd>
<dt><i>sendmail</i></dt>
<dd> <p> [Obsolete] Predecessor of <i>mta</i> </p>
 </dd>
<dt><i>sendmail-arguments</i></dt>
<dd> <p> [Obsolete] Predecessor of <i>mta-arguments</i> </p>
 </dd>
<dt><i>sendmail-no-default-arguments</i></dt>
<dd> <p> [Obsolete](Boolean) Predecessor of <i>mta-no-default-arguments</i> </p>
 </dd>
<dt><i>sendmail-progname</i></dt>
<dd> <p> [Obsolete] Predecessor of <i>mta-argv0</i> </p>
 </dd>
<dt><i>sendwait</i></dt>
<dd> <p> Sending messages to the chosen <i>mta</i> or to command-pipe receivers (see Sx On sending mail, and non-interactive mode ) will be performed asynchronously. This means that only startup errors of the respective program will be recognizable, but no delivery errors. Also, no guarantees can be made as to when the respective program will actually run, as well as to when they will have produced output. </p>
<p> If this variable is set then child program exit is waited for, and its exit status code is used to decide about success. Remarks: in conflict with the POSIX standard this variable is built-in to be initially set. Another difference is that it can have a value, which is interpreted as a comma-separated list of case-insensitive strings naming specific subsystems for which synchronousness shall be ensured (only). Possible values are `mta&#8217; for <i>mta</i> delivery, and `pcc&#8217; for command-pipe receivers. </p>
 </dd>
<dt><i>showlast</i></dt>
<dd> <p> (Boolean) This setting causes S-nail to start at the last message instead of the first one when opening a mail folder, as well as with <code>from</code> and <code>headers</code> </p>
 </dd>
<dt><i>showname</i></dt>
<dd> <p> (Boolean) Causes S-nail to use the sender&#8217;s real name instead of the plain address in the header field summary and in message specifications. </p>
 </dd>
<dt><i>showto</i></dt>
<dd> <p> (Boolean) Causes the recipient of the message to be shown in the header summary if the message was sent by the user. </p>
 </dd>
<dt><i>Sign</i></dt>
<dd> <p> The value backing <code>~A</code> one of the Sx COMMAND ESCAPES . Also see <i>message-inject-tail</i> <i>on-compose-leave</i> and <i>on-compose-splice</i> </p>
 </dd>
<dt><i>sign</i></dt>
<dd> <p> The value backing <code>~a</code> one of the Sx COMMAND ESCAPES . Also see <i>message-inject-tail</i> <i>on-compose-leave</i> and <i>on-compose-splice</i> </p>
 </dd>
<dt><i>signature</i></dt>
<dd> <p> [Obsolete] Please use <i>on-compose-splice</i> or <i>on-compose-splice-shell</i> or <i>on-compose-leave</i> and (if necessary) <i>message-inject-tail</i> instead! </p>
 </dd>
<dt><i>skipemptybody</i></dt>
<dd> <p> (Boolean) If an outgoing message has an empty first or only message part, do not send, but discard it, successfully (also see the command line option -<code>E )</code> </p>
 </dd>
<dt><i>smime-ca-dir , smime-ca-file</i></dt>
<dd> <p> [Option] Specify the location of trusted CA certificates in PEM (Privacy Enhanced Mail) for the purpose of verification of S/MIME signed messages. <i>tls-ca-dir</i> documents the necessary preparation steps to use the former. The set of CA certificates which are built into the TLS library can be explicitly turned off by setting <i>smime-ca-no-defaults</i> and further fine-tuning is possible via <i>smime-ca-flags</i> </p>
 </dd>
<dt><i>smime-ca-flags</i></dt>
<dd> <p> [Option] Can be used to fine-tune behaviour of the X509 CA certificate storage, and the certificate verification that is used. The actual values and their meanings are documented for <i>tls-ca-flags</i> </p>
 </dd>
<dt><i>smime-ca-no-defaults</i></dt>
<dd> <p> (Boolean)[Option] Do not load the default CA locations that are built into the used to TLS library to verify S/MIME signed messages. </p>
 </dd>
<dt><i>smime-cipher-USER [at] HOST , smime-cipher</i></dt>
<dd> <p> [Option] Specifies the cipher to use when generating S/MIME encrypted messages (for the specified account). RFC 5751 mandates a default of `aes128&#8217; (AES-128 CBC). Possible values are (case-insensitive and) in decreasing cipher strength: `aes256&#8217; (AES-256 CBC), `aes192&#8217; (AES-192 CBC), `aes128&#8217; (AES-128 CBC), `des3&#8217; (DES EDE3 CBC, 168 bits; default if `aes128&#8217; is not available) and `des&#8217; (DES CBC, 56 bits). </p>
<p> The actually available cipher algorithms depend on the cryptographic library that S-nail uses. [Option] Support for more cipher algorithms may be available through dynamic loading via EVP_get_cipherbyname3 (OpenSSL) if S-nail has been compiled to support this. </p>
 </dd>
<dt><i>smime-crl-dir</i></dt>
<dd> <p> [Option] Specifies a directory that contains files with CRLs in PEM format to use when verifying S/MIME messages. </p>
 </dd>
<dt><i>smime-crl-file</i></dt>
<dd> <p> [Option] Specifies a file that contains a CRL in PEM format to use when verifying S/MIME messages. </p>
 </dd>
<dt><i>smime-encrypt-USER [at] HOST</i></dt>
<dd> <p> [Option] If this variable is set, messages send to the given receiver are encrypted before sending. The value of the variable must be set to the name of a file that contains a certificate in PEM format. </p>
<p> If a message is sent to multiple recipients, each of them for whom a corresponding variable is set will receive an individually encrypted message; other recipients will continue to receive the message in plain text unless the <i>smime-force-encryption</i> variable is set. It is recommended to sign encrypted messages, i.e., to also set the <i>smime-sign</i> variable. <i>content-description-smime-message</i> will be inspected for messages which become encrypted. </p>
 </dd>
<dt><i>smime-force-encryption</i></dt>
<dd> <p> (Boolean)[Option] Causes S-nail to refuse sending unencrypted messages. </p>
 </dd>
<dt><i>smime-sign</i></dt>
<dd> <p> (Boolean)[Option] S/MIME sign outgoing messages with the user&#8217;s ( <i>from</i> private key and include the users certificate as a MIME attachment. Signing a message enables a recipient to verify that the sender used a valid certificate, that the email addresses in the certificate match those in the message header and that the message content has not been altered. It does not change the message text, and people will be able to read the message as usual. <i>content-description-smime-signature</i> will be inspected. Also see <i>smime-sign-cert , smime-sign-include-certs</i> and <i>smime-sign-digest</i> </p>
 </dd>
<dt><i>smime-sign-cert-USER [at] HOST , smime-sign-cert</i></dt>
<dd> <p> [Option] Points to a file in PEM format. For the purpose of signing and decryption this file needs to contain the user&#8217;s private key, followed by his certificate. </p>
<p> For message signing `USER [at] HOST&#8217; is always derived from the value of <i>from</i> (or, if that contains multiple addresses, <i>sender )</i> For the purpose of encryption the recipients public encryption key (certificate) is expected; the command <code>certsave</code> can be used to save certificates of signed messages (the section Sx Signed and encrypted messages with S/MIME gives some details). This mode of operation is usually driven by the specialized form. </p>
<p> When decrypting messages the account is derived from the recipient fields ( `To:&#8216; and `Cc:&#8216; ) of the message, which are searched for addresses for which such a variable is set. S-nail always uses the first address that matches, so if the same message is sent to more than one of the user addresses using different encryption keys, decryption might fail. </p>
<p> Password-encrypted keys may be used for signing and decryption. Automated password lookup is possible via the ``pseudo-hosts&#8217;&#8216; `USER [at] HOST.smime-cert-key&#8217; for the private key, and `USER [at] HOST.smime-cert-cert&#8217; for the certificate stored in the same file. For example, the hypothetical address `bob [at] exam.ple&#8217; could be driven with a private key / certificate pair path defined in <i>smime-sign-cert-bob [at] exam.ple</i> and the needed passwords would then be looked up as `bob [at] exam.ple.smime-cert-key&#8217; and `bob [at] exam.ple.smime-cert-cert&#8217; When decrypting the value of <i>from</i> will be tried as a fallback to provide the necessary `USER [at] HOST&#8217; To include intermediate certificates, use <i>smime-sign-include-certs</i> The possible password sources are documented in Sx On URL syntax and credential lookup . </p>
 </dd>
<dt><i>smime-sign-digest-USER [at] HOST , smime-sign-digest</i></dt>
<dd> <p> [Option] Specifies the message digest to use when signing S/MIME messages. Please remember that for this use case `USER [at] HOST&#8217; refers to the variable <i>from</i> (or, if that contains multiple addresses, <i>sender )</i> The available algorithms depend on the used cryptographic library, but at least one usable built-in algorithm is ensured as a default. If possible the standard RFC 5751 will be violated by using `SHA512&#8217; instead of the mandated `SHA1&#8217; due to security concerns. This variable is ignored for very old (released before 2010) cryptographic libraries which do not offer the necessary interface: it will be logged if that happened. </p>
<p> S-nail will try to add built-in support for the following message digests, names are case-insensitive: `BLAKE2b512&#8217; , `BLAKE2s256&#8217; , `SHA3-512&#8217; , `SHA3-384&#8217; , `SHA3-256&#8217; , `SHA3-224&#8217; , as well as the widely available `SHA512&#8217; , `SHA384&#8217; , `SHA256&#8217; , `SHA224&#8217; , and the proposed insecure `SHA1&#8217; , finally `MD5&#8217; More digests may [Option]ally be available through dynamic loading via the OpenSSL function EVP_get_digestbyname3. </p>
 </dd>
<dt><i>smime-sign-include-certs-USER [at] HOST , smime-sign-include-certs</i></dt>
<dd> <p> [Option] If used, this is supposed to a consist of a comma-separated list of files, each of which containing a single certificate in PEM format to be included in the S/MIME message in addition to the <i>smime-sign-cert</i> certificate. This can be used to include intermediate certificates of the certificate authority, in order to allow the receiver&#8217;s S/MIME implementation to perform a verification of the entire certificate chain, starting from a local root certificate, over the intermediate certificates, down to the <i>smime-sign-cert</i> Even though top level certificates may also be included in the chain, they will not be used for the verification on the receiver&#8217;s side. </p>
<p> For the purpose of the mechanisms involved here, `USER [at] HOST&#8217; refers to the content of the internal variable <i>from</i> (or, if that contains multiple addresses, <i>sender )</i> The pseudo-host `USER [at] HOST.smime-include-certs&#8217; will be used for performing password lookups for these certificates, shall they have been given one, therefore the lookup can be automated via the mechanisms described in Sx On URL syntax and credential lookup . </p>
 </dd>
<dt><i>smime-sign-message-digest-USER [at] HOST , smime-sign-message-digest</i></dt>
<dd> <p> [Obsolete][Option] Predecessor(s) of <i>smime-sign-digest</i> </p>
 </dd>
<dt><i>smtp</i></dt>
<dd> <p> [Obsolete][Option] To use the built-in SMTP transport, specify a SMTP URL in <i>mta</i> [v15 behaviour may differ] For compatibility reasons a set <i>smtp</i> is used in preference of <i>mta</i> </p>
 </dd>
<dt><i>smtp-auth-USER [at] HOST , smtp-auth-HOST , smtp-auth</i></dt>
<dd> <p> [Option] Variable chain that controls the SMTP <i>mta</i> authentication method, possible values are `none&#8217; ([no v15-compat] default), `plain&#8217; ([v15-compat] default), `login&#8217; , [v15-compat] `oauthbearer&#8217; (see Sx FAQ entry Sx But, how about XOAUTH2 / OAUTHBEARER? ) as well as [v15-compat] `external&#8217; and `externanon&#8217; for TLS secured connections which pass a client certificate via <i>tls-config-pairs</i> There may be the [Option]al methods `cram-md5&#8217; and `gssapi&#8217; `none&#8217; and `externanon&#8217; do not need any user credentials, `external&#8217; and `gssapi&#8217; require a user name, and all other methods require a <i>user</i> name and a <i>password</i> `externanon&#8217; solely builds upon the credentials passed via a client certificate, and is usually the way to go since tested servers do not actually follow RFC 4422 aka RFC 4954, and fail if additional credentials are passed. Also see <i>mta</i> Note that <i>smtp-auth-HOST</i> is [v15-compat]. ([no v15-compat] Requires <i>smtp-auth-password</i> and <i>smtp-auth-user</i> Note for <i>smtp-auth-USER [at] HOST</i> may override dependent on sender address in the variable <i>from .</i> </p>
 </dd>
<dt><i>smtp-auth-password</i></dt>
<dd> <p> [Option][no v15-compat] Sets the global fallback password for SMTP authentication. If the authentication method requires a password, but neither <i>smtp-auth-password</i> nor a matching <i>smtp-auth-password-USER [at] HOST</i> can be found, S-nail will ask for a password on the user&#8217;s terminal. </p>
 </dd>
<dt><i>smtp-auth-password-USER [at] HOST</i></dt>
<dd> <p> [no v15-compat] Overrides <i>smtp-auth-password</i> for specific values of sender addresses, dependent upon the variable <i>from</i> </p>
 </dd>
<dt><i>smtp-auth-user</i></dt>
<dd> <p> [Option][no v15-compat] Sets the global fallback user name for SMTP authentication. If the authentication method requires a user name, but neither <i>smtp-auth-user</i> nor a matching <i>smtp-auth-user-USER [at] HOST</i> can be found, S-nail will ask for a user name on the user&#8217;s terminal. </p>
 </dd>
<dt><i>smtp-auth-user-USER [at] HOST</i></dt>
<dd> <p> [no v15-compat] Overrides <i>smtp-auth-user</i> for specific values of sender addresses, dependent upon the variable <i>from</i> </p>
 </dd>
<dt><i>smtp-hostname</i></dt>
<dd> <p> [Option][v15-compat] Normally S-nail uses the variable <i>from</i> to derive the necessary `USER [at] HOST&#8217; information in order to issue a `MAIL&#8217; FROM:&lt;&gt; SMTP <i>mta</i> command. Setting <i>smtp-hostname</i> can be used to use the `USER&#8217; from the SMTP account ( <i>mta</i> or the <i>user</i> variable chain) and the given `HOST&#8217; ( <i>hostname</i> if the empty string is given, or the local hostname as a last resort). This often allows using an address that is itself valid but hosted by a provider other than from which (in <i>from</i> the message is sent. Setting this variable also influences generated `Message-ID:&#8216; and `Content-ID:&#8216; header fields. If the [Option]al IDNA support is available (see <i>idna-disable</i> variable assignment is aborted when a necessary conversion fails. </p>
 </dd>
<dt><i>smtp-use-starttls-USER [at] HOST , smtp-use-starttls-HOST , smtp-use-starttls</i></dt>
<dd> <p> (Boolean)[Option] Causes S-nail to issue a `STARTTLS&#8217; command to make an SMTP <i>mta</i> session TLS encrypted, i.e., to enable transport layer security. </p>
 </dd>
<dt><i>socket-connect-timeout</i></dt>
<dd> <p> [Option] A positive number that defines the timeout to wait for establishing a socket connection before forcing <i>^ERR </i><code>-TIMEDOUT</code> </p>
 </dd>
<dt><i>socks-proxy-USER [at] HOST , socks-proxy-HOST , socks-proxy</i></dt>
<dd> <p> [Option] If set to the URL of a SOCKS5 server then all network activities are proxied through it, except for the single DNS name lookup necessary to resolve the proxy URL (unnecessary when given an already resolved IP address). It is automatically squared with the environment variable <code>SOCKS5_PROXY</code> changing the one will adjust the other. This example creates a local SOCKS5 proxy on port 10000 that forwards to the machine `HOST&#8217; (with identity `USER&#8217; ) , and from which actual network traffic happens: </p>
<blockquote><pre><code>$ ssh -D 10000 USER [at] HOST
$ s-nail -Ssocks-proxy=[socks5://]localhost:10000
# or =localhost:10000; no local DNS: =127.0.0.1:10000
</code></pre>
</blockquote>
 </dd>
<dt><i>spam-interface</i></dt>
<dd> <p> [Option] In order to use any of the spam-related commands (like <code>spamrate</code> the desired spam interface must be defined by setting this variable. Please refer to the manual section Sx Handling spam for the complete picture of spam handling in S-nail. All or none of the following interfaces may be available: </p>
 </dd>
<dl>
<dt><code>`spamc&#8217; </code></dt>
<dd> <p> Interaction with <a href="/docs/linux/man/1-spamc/">spamc</a>(1) from the <a href="/docs/linux/man/1-spamassassin/">spamassassin</a>(1) ( Lk <a rel="nofollow" href="http://spamassassin.apache.org">http://spamassassin.apache.org</a> SpamAssassin suite. Different to the generic filter interface S-nail will automatically add the correct arguments for a given command and has the necessary knowledge to parse the program&#8217;s output. A default value for <i>spamc-command</i> will have been compiled into the S-nail binary if <a href="/docs/linux/man/1-spamc/">spamc</a>(1) has been found in <code>PATH</code> during compilation. Shall it be necessary to define a specific connection type (rather than using a configuration file for that), the variable <i>spamc-arguments</i> can be used as in for example `-d&#8217; server.example.com -p 783 . It is also possible to specify a per-user configuration via <i>spamc-user</i> Note that this interface does not inspect the `is-spam&#8217; flag of a message for the command <code>spamforget</code> </p>
 </dd>
<dt><code>`filter&#8217; </code></dt>
<dd> <p> generic spam filter support via freely configurable hooks. This interface is meant for programs like <a href="/docs/linux/man/1-bogofilter/">bogofilter</a>(1) and requires according behaviour in respect to the hooks&#8217; exit status for at least the command <code>spamrate</code> ( `0&#8217; meaning a message is spam, `1&#8217; for non-spam, `2&#8217; for unsure and any other return value indicating a hard error); since the hooks can include shell code snippets diverting behaviour can be intercepted as necessary. The hooks are <i>spamfilter-ham , spamfilter-noham , spamfilter-nospam ,</i> <br />
&nbsp;<wbr>&nbsp;spamfilter-rate and <i>spamfilter-spam</i> the manual section Sx Handling spam contains examples for some programs. The process environment of the hooks will have the variable <code>MAILX_FILENAME_GENERATED</code> set. Note that spam score support for <code>spamrate</code> is not supported unless the [Option]tional regular expression support is available and the <i>spamfilter-rate-scanscore</i> variable is set. </p>
 </dd></dl>
<dt><i>spam-maxsize</i></dt>
<dd> <p> [Option] Messages that exceed this size will not be passed through to the configured <i>spam-interface</i> If unset or 0, the default of 420000 bytes is used. </p>
 </dd>
<dt><i>spamc-command</i></dt>
<dd> <p> [Option] The path to the <a href="/docs/linux/man/1-spamc/">spamc</a>(1) program for the `spamc&#8217; <i>spam-interface</i> Note that the path is not expanded, but used ``as is&#8217;&#8216; A fallback path will have been compiled into the S-nail binary if the executable had been found during compilation. </p>
 </dd>
<dt><i>spamc-arguments</i></dt>
<dd> <p> [Option] Even though S-nail deals with most arguments for the `spamc&#8217; <i>spam-interface</i> automatically, it may at least sometimes be desirable to specify connection-related ones via this variable, for example `-d&#8217; server.example.com -p 783 . </p>
 </dd>
<dt><i>spamc-user</i></dt>
<dd> <p> [Option] Specify a username for per-user configuration files for the `spamc&#8217; <i>spam-interface</i> If this is set to the empty string then S-nail will use the name of the current <i>user</i> </p>
 </dd>
<dt><i>spamfilter-ham , spamfilter-noham</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;spamfilter-nospam , spamfilter-rate , spamfilter-spam [Option] Command and argument hooks for the `filter&#8217; <i>spam-interface</i> The manual section Sx Handling spam contains examples for some programs. </p>
 </dd>
<dt><i>spamfilter-rate-scanscore</i></dt>
<dd> <p> [Option] Because of the generic nature of the `filter&#8217; <i>spam-interface</i> spam scores are not supported for it by default, but if the [Option]nal regular expression support is available then setting this variable can be used to overcome this restriction. It is interpreted as follows: first a number (digits) is parsed that must be followed by a semicolon `;&#8216; and an extended regular expression. Then the latter is used to parse the first output line of the <i>spamfilter-rate</i> hook, and, in case the evaluation is successful, the group that has been specified via the number is interpreted as a floating point scan score. </p>
 </dd>
<dt><i>ssl-ca-dir-USER [at] HOST , ssl-ca-dir-HOST , ssl-ca-dir ,<br />
&nbsp;<wbr>&nbsp;ssl-ca-file-USER [at] HOST , ssl-ca-file-HOST , ssl-ca-file</i></dt>
<dd> <p> [Obsolete][Option] Predecessors of <i>tls-ca-file</i> <i>tls-ca-dir</i> </p>
 </dd>
<dt><i>ssl-ca-flags-USER [at] HOST , ssl-ca-flags-HOST , ssl-ca-flags</i></dt>
<dd> <p> [Obsolete][Option] Predecessor of <i>tls-ca-flags</i> </p>
 </dd>
<dt><i>ssl-ca-no-defaults-USER [at] HOST , ssl-ca-no-defaults-HOST ,<br />
&nbsp;<wbr>&nbsp;ssl-ca-no-defaults</i></dt>
<dd> <p> [Obsolete](Boolean)[Option] Predecessor of <i>tls-ca-no-defaults</i> </p>
 </dd>
<dt><i>ssl-cert-USER [at] HOST , ssl-cert-HOST , ssl-cert</i></dt>
<dd> <p> [Obsolete][Option] Please use the <code>Certificate</code> slot of <i>tls-config-pairs</i> </p>
 </dd>
<dt><i>ssl-cipher-list-USER [at] HOST , ssl-cipher-list-HOST , ssl-cipher-list</i></dt>
<dd> <p> [Obsolete][Option] Please use the <code>CipherString</code> slot of <i>tls-config-pairs</i> </p>
 </dd>
<dt><i>ssl-config-file</i></dt>
<dd> <p> [Obsolete][Option] Predecessor of <i>tls-config-file</i> </p>
 </dd>
<dt><i>ssl-config-module-USER [at] HOST , ssl-config-module-HOST ,<br />
&nbsp;<wbr>&nbsp;ssl-config-module</i></dt>
<dd> <p> [Obsolete][Option] Predecessor of <i>tls-config-module</i> </p>
 </dd>
<dt><i>ssl-config-pairs-USER [at] HOST , ssl-config-pairs-HOST , ssl-config-pairs</i></dt>
<dd> <p> [Obsolete][Option] Predecessor of <i>tls-config-pairs</i> </p>
 </dd>
<dt><i>ssl-crl-dir , ssl-crl-file</i></dt>
<dd> <p> [Obsolete][Option] Predecessors of <i>tls-crl-dir</i> <i>tls-crl-file</i> </p>
 </dd>
<dt><i>ssl-curves-USER [at] HOST , ssl-curves-HOST , ssl-curves</i></dt>
<dd> <p> [Obsolete][Option] Please use the <code>Curves</code> slot of <i>tls-config-pairs</i> </p>
 </dd>
<dt><i>ssl-features</i></dt>
<dd> <p> [Obsolete][Option](Read-only) Predecessor of <i>tls-features</i> </p>
 </dd>
<dt><i>ssl-key-USER [at] HOST , ssl-key-HOST , ssl-key</i></dt>
<dd> <p> [Obsolete][Option] Please use the <code>PrivateKey</code> slot of <i>tls-config-pairs</i> </p>
 </dd>
<dt><i>ssl-method-USER [at] HOST , ssl-method-HOST , ssl-method</i></dt>
<dd> <p> [Obsolete][Option] Please use the <code>Protocol</code> slot of <i>tls-config-pairs</i> </p>
 </dd>
<dt><i>ssl-protocol-USER [at] HOST , ssl-protocol-HOST , ssl-protocol</i></dt>
<dd> <p> [Obsolete][Option] Please use the <code>Protocol</code> slot of <i>tls-config-pairs</i> </p>
 </dd>
<dt><i>ssl-rand-file</i></dt>
<dd> <p> [Obsolete][Option] Predecessor of <i>tls-rand-file</i> </p>
 </dd>
<dt><i>ssl-verify-USER [at] HOST , ssl-verify-HOST , ssl-verify</i></dt>
<dd> <p> [Obsolete][Option] Predecessor of <i>tls-verify</i> </p>
 </dd>
<dt><i>stealthmua</i></dt>
<dd> <p> If only set without an assigned value, then this setting inhibits the generation of the `Message-ID:&#8216; , `Content-ID:&#8216; and `User-Agent:&#8216; header fields that include obvious references to S-nail. There are two pitfalls associated with this: First, the message id of outgoing messages is not known anymore. Second, an expert may still use the remaining information in the header to track down the originating mail user agent. If set to the value `noagent&#8217; , then the mentioned `Message-ID:&#8216; and `Content-ID:&#8216; suppression does not occur. </p>
 </dd>
<dt><i>system-mailrc</i></dt>
<dd> <p> (Read-only) The compiled in path of the system wide initialization file one of the Sx Resource files : s-nail.rc </p>
 </dd>
<dt><i>termcap</i></dt>
<dd> <p> ([Option]) This specifies a comma-separated list of Lb libterminfo and/or Lb libtermcap capabilities (see Sx On terminal control and line editor , escape commas with reverse solidus `\&#8216; ) to be used to overwrite or define entries. <code>Note</code> this variable will only be queried once at program startup and can thus only be specified in resource files or on the command line. It will always be inspected, regardless of whether <i>features</i> denotes termcap/terminfo library support via `,+termcap,&#8216; </p>
<p> String capabilities form `cap=value&#8217; pairs and are expected unless noted otherwise. Numerics have to be notated as `cap#number&#8217; where the number is expected in normal decimal notation. Finally, booleans do not have any value but indicate a true or false state simply by being defined or not; this indeed means that S-nail does not support undefining an existing boolean. String capability values will undergo some expansions before use: for one notations like `^LETTER&#8217; stand for `control-LETTER&#8217; , and for clarification purposes `\E&#8217; can be used to specify `escape&#8217; (the control notation `^[&#8216; could lead to misreadings when a left bracket follows, which it does for the standard CSI sequence); finally three letter octal sequences, as in `\061&#8217; , are supported. To specify that a terminal supports 256-colours, and to define sequences that home the cursor and produce an audible bell, one might write: </p>
<blockquote><pre><code>? set termcap='Co#256,home=\E[H,bel=^G'
</code></pre>
</blockquote>
<p> The following terminal capabilities are or may be meaningful for the operation of the built-in line editor or S-nail in general: </p>
 </dd>
<dl>
<dt><code>am</code></dt>
<dd> <p> <code>auto_right_margin</code> boolean which indicates if the right margin needs special treatment; the <code>xenl</code> capability is related, for more see <code>COLUMNS</code> This capability is only used when backed by library support. </p>
 </dd>
<dt><code>clear &nbsp;or cl</code></dt>
<dd> <p> <code>clear_screen</code> clear the screen and home cursor. (Will be simulated via <code>ho</code> plus <code>cd .</code> </p>
 </dd>
<dt><code>colors &nbsp;or Co </code><code>max_colors</code></dt>
<dd> <p> numeric capability specifying the maximum number of colours. Note that S-nail does not actually care about the terminal beside that, but always emits ANSI / ISO 6429 escape sequences; also see <code>colour</code> </p>
 </dd>
<dt><code>cr</code></dt>
<dd> <p> <code>carriage_return</code> move to the first column in the current row. The default built-in fallback is `\r&#8217; </p>
 </dd>
<dt><code>cub1 &nbsp;or le</code></dt>
<dd> <p> <code>cursor_left</code> move the cursor left one space (non-destructively). The default built-in fallback is `\b&#8217; </p>
 </dd>
<dt><code>cuf1 &nbsp;or nd</code></dt>
<dd> <p> <code>cursor_right</code> move the cursor right one space (non-destructively). The default built-in fallback is `\E[C&#8217; , which is used by most terminals. Less often occur `\EC&#8217; and `\EOC&#8217; </p>
 </dd>
<dt><code>ed &nbsp;or cd</code></dt>
<dd> <p> <code>clr_eos</code> clear the screen. </p>
 </dd>
<dt><code>el &nbsp;or ce</code></dt>
<dd> <p> <code>clr_eol</code> clear to the end of line. (Will be simulated via <code>ch</code> plus repetitions of space characters.) </p>
 </dd>
<dt><code>home &nbsp;or ho</code></dt>
<dd> <p> <code>cursor_home</code> home cursor. </p>
 </dd>
<dt><code>hpa &nbsp;or ch</code></dt>
<dd> <p> <code>column_address</code> move the cursor (to the given column parameter) in the current row. (Will be simulated via <code>cr</code> plus <code>nd .</code> </p>
 </dd>
<dt><code>rmcup &nbsp;or te &nbsp;/ smcup &nbsp;or ti</code></dt>
<dd> <p> <code>exit_ca_mode</code> and <code>enter_ca_mode</code> respectively: exit and enter the alternative screen ca-mode, effectively turning S-nail into a fullscreen application. This must be enabled explicitly by setting <i>termcap-ca-mode</i> </p>
 </dd>
<dt><code>smkx &nbsp;or ks &nbsp;/ rmkx &nbsp;or ke</code></dt>
<dd> <p> <code>keypad_xmit</code> and <code>keypad_local</code> respectively: enable and disable the keypad. This is always enabled if available, because it seems even keyboards without keypads generate other key codes for, e.g., cursor keys in that case, and only if enabled we see the codes that we are interested in. </p>
 </dd>
<dt><code>xenl &nbsp;or xn</code></dt>
<dd> <p> <code>eat_newline_glitch</code> boolean which indicates whether a newline written in the last column of an <code>auto_right_margin</code> indicating terminal is ignored. With it the full terminal width is available even on autowrap terminals. This will be inspected even without `,+termcap,&#8216; <i>features</i> </p>
 </dd></dl>
<p> Many more capabilities which describe key-sequences are documented for <code>bind</code> </p>
<dt><i>termcap-ca-mode</i></dt>
<dd> <p> [Option] Allow usage of the <code>exit_ca_mode</code> and <code>enter_ca_mode</code> <i>termcap </i><code>abilities in order to enter an alternative exclusive screen, the</code> so-called ca-mode; this usually requires special configuration of the <code>PAGER</code> also dependent on the value of <i>crt</i> <code>Note</code> this variable will only be queried once at program startup and can thus only be specified in resource files or on the command line. </p>
 </dd>
<dt><i>termcap-disable</i></dt>
<dd> <p> [Option] Disable any interaction with a terminal control library. If set only some generic fallback built-ins and possibly the content of <i>termcap</i> describe the terminal to S-nail. <code>Note</code> this variable will only be queried once at program startup and can thus only be specified in resource files or on the command line. </p>
 </dd>
<dt><i>tls-ca-dir-USER [at] HOST , tls-ca-dir-HOST , tls-ca-dir ,<br />
&nbsp;<wbr>&nbsp;tls-ca-file-USER [at] HOST , tls-ca-file-HOST , tls-ca-file</i></dt>
<dd> <p> [Option] Directory and file, respectively, for pools of trusted CA certificates in PEM (Privacy Enhanced Mail) format, for the purpose of verification of TLS server certificates. Concurrent use is possible, the file is loaded once needed first, the directory lookup is performed anew as a last resort whenever necessary. The CA certificate pool built into the TLS library can be disabled via <i>tls-ca-no-defaults</i> further fine-tuning is possible via <i>tls-ca-flags</i> The directory search requires special filename conventions, please see SSL_CTX_load_verify_locations3 and verify(1) (or c_rehash1). </p>
 </dd>
<dt><i>tls-ca-flags-USER [at] HOST , tls-ca-flags-HOST , tls-ca-flags</i></dt>
<dd> <p> [Option] Can be used to fine-tune behaviour of the X509 CA certificate storage, and the certificate verification that is used (also see <i>tls-verify )</i> The value is expected to consist of a comma-separated list of configuration directives, with any intervening whitespace being ignored. The directives directly map to flags that can be passed to X509_STORE_set_flags3, which are usually defined in a file openssl/x509_vfy.h and the availability of which depends on the used TLS library version: a directive without mapping is ignored (error log subject to <i>debug )</i> Directives currently understood (case-insensitively) include: </p>
 </dd>
<dl>
<dt><code>no-alt-chains</code></dt>
<dd> <p> If the initial chain is not trusted, do not attempt to build an alternative chain. Setting this flag will make OpenSSL certificate verification match that of older OpenSSL versions, before automatic building and checking of alternative chains has been implemented; also see <code>trusted-first</code> </p>
 </dd>
<dt><code>no-check-time</code></dt>
<dd> <p> Do not check certificate/CRL validity against current time. </p>
 </dd>
<dt><code>partial-chain</code></dt>
<dd> <p> By default partial, incomplete chains which cannot be verified up to the chain top, a self-signed root certificate, will not verify. With this flag set, a chain succeeds to verify if at least one signing certificate of the chain is in any of the configured trusted stores of CA certificates. The OpenSSL manual page SSL_CTX_load_verify_locations3 gives some advise how to manage your own trusted store of CA certificates. </p>
 </dd>
<dt><code>strict</code></dt>
<dd> <p> Disable workarounds for broken certificates. </p>
 </dd>
<dt><code>trusted-first</code></dt>
<dd> <p> Try building a chain using issuers in the trusted store first to avoid problems with server-sent legacy intermediate certificates. Newer versions of OpenSSL support alternative chain checking and enable it by default, resulting in the same behaviour; also see <code>no-alt-chains</code> </p>
 </dd></dl>
<dt><i>tls-ca-no-defaults-USER [at] HOST , tls-ca-no-defaults-HOST ,<br />
&nbsp;<wbr>&nbsp;tls-ca-no-defaults</i></dt>
<dd> <p> (Boolean)[Option] Do not load the default CA locations that are built into the used to TLS library to verify TLS server certificates. </p>
 </dd>
<dt><i>tls-config-file</i></dt>
<dd> <p> [Option] If this variable is set CONF_modules_load_file3 (if announced via `,+modules-load-file,&#8216; in <i>tls-features</i> is used to allow resource file based configuration of the TLS library. This happens once the library is used first, which may also be early during startup (logged with <i>verbose )</i> If a non-empty value is given then the given file, after performing Sx Filename transformations , will be used instead of the TLS libraries global default, and it is an error if the file cannot be loaded. The application name will always be passed as `s-nail&#8217; Some TLS libraries support application-specific configuration via resource files loaded like this, please see <i>tls-config-module</i> </p>
 </dd>
<dt><i>tls-config-module-USER [at] HOST , tls-config-module-HOST ,<br />
&nbsp;<wbr>&nbsp;tls-config-module</i></dt>
<dd> <p> [Option] If file based application-specific configuration via <i>tls-config-file</i> is available, announced as `,+ctx-config,&#8216; by <i>tls-features</i> indicating availability of SSL_CTX_config3, then, it becomes possible to use a central TLS configuration file for all programs, including s-nail, for example </p>
<blockquote><pre><code># Register a configuration section for s-nail
s-nail = mailx_master
# The top configuration section creates a relation
# in between dynamic SSL configuration and an actual
# program specific configuration section
[mailx_master]
ssl_conf = mailx_tls_config
# And that program specific configuration section now
# can map diverse tls-config-module names to sections,
# as in: tls-config-module=account_xy
[mailx_tls_config]
account_xy = mailx_account_xy
account_yz = mailx_account_yz
[mailx_account_xy]
MinProtocol = TLSv1.2
Curves=P-521
[mailx_account_yz]
CipherString = TLSv1.2:!aNULL:!eNULL:
MinProtocol = TLSv1.1
Options = Bugs
</code></pre>
</blockquote>
 </dd>
<dt><i>tls-config-pairs-USER [at] HOST , tls-config-pairs-HOST , tls-config-pairs</i></dt>
<dd> <p> [Option] The value of this variable chain will be interpreted as a comma-separated list of directive/value pairs. Directives and values need to be separated by equals signs `=&#8216; , any whitespace surrounding pair members is removed. Keys are (usually) case-insensitive. Different to when placing these pairs in a <i>tls-config-module</i> section of a <i>tls-config-file</i> commas `,&#8216; need to be escaped with a reverse solidus `\&#8216; when included in pairs; also different: if the equals sign `=&#8216; is preceded with an asterisk `*&#8216; Sx Filename transformations will be performed on the value; it is an error if these fail. Unless proper support is announced by <i>tls-features</i> ( `,+conf-ctx,&#8216; only the keys below are supported, otherwise the pairs will be used directly as arguments to the function SSL_CONF_cmd3. </p>
 </dd>
<dl>
<dt><code>Certificate</code></dt>
<dd> <p> Filename of a TLS client certificate (chain) required by some servers. Fallback support via SSL_CTX_use_certificate_chain_file3. Sx Filename transformations are performed. <code>PrivateKey</code> will be set to the same value if not initialized explicitly. Some services support so-called `external&#8217; authentication if a TLS client certificate was successfully presented during connection establishment ( ``connecting is authenticating&#8217;&#8216; </p>
 </dd>
<dt><code>CipherString</code></dt>
<dd> <p> A list of ciphers for TLS connections, see ciphers(1). By default no list of ciphers is set, resulting in a <code>Protocol - specific list of ciphers (the protocol standards define lists of</code> acceptable ciphers; possibly cramped by the used TLS library). Fallback support via SSL_CTX_set_cipher_list3. </p>
 </dd>
<dt><code>Ciphersuites</code></dt>
<dd> <p> A list of ciphers used for TLSv1.3 connections, see ciphers(1). These will be joined onto the list of ciphers from <code>CipherString</code> Available if <i>tls-features</i> announces `,+ctx-set-ciphersuites,&#8216; , as necessary via SSL_CTX_set_ciphersuites3. </p>
 </dd>
<dt><code>Curves</code></dt>
<dd> <p> A list of supported elliptic curves, if applicable. By default no curves are set. Fallback support via SSL_CTX_set1_curves_list3, if available. </p>
 </dd>
<dt><code>MaxProtocol , MinProtocol</code></dt>
<dd> <p> The maximum and minimum supported TLS versions, respectively. Available if <i>tls-features</i> announces `,+ctx-set-maxmin-proto,&#8216; , as necessary via SSL_CTX_set_max_proto_version3 and SSL_CTX_set_min_proto_version3; these fallbacks use an internal parser which understands the strings `SSLv3&#8217; , `TLSv1&#8217; , `TLSv1.1&#8217; , `TLSv1.2&#8217; , `TLSv1.3&#8217; , and the special value `None&#8217; , which disables the given limit. </p>
 </dd>
<dt><code>Options</code></dt>
<dd> <p> Various flags to set. Fallback via SSL_CTX_set_options3, in which case any other value but (exactly) `Bugs&#8217; results in an error. </p>
 </dd>
<dt><code>PrivateKey</code></dt>
<dd> <p> Filename of the private key in PEM format of a TLS client certificate. If unset, the value of <code>Certificate</code> is used. Sx Filename transformations are performed. Fallback via SSL_CTX_use_PrivateKey_file3. </p>
 </dd>
<dt><code>Protocol</code></dt>
<dd> <p> The used TLS protocol. If <i>tls-features</i> announces `,+conf-ctx,&#8216; or `ctx-set-maxmin-proto&#8217; then using <code>MaxProtocol</code> and <code>MinProtocol</code> is preferable. Fallback is SSL_CTX_set_options3, driven via an internal parser which understands the strings `SSLv3&#8217; , `TLSv1&#8217; , `TLSv1.1&#8217; , `TLSv1.2&#8217; , `TLSv1.3&#8217; , and the special value `ALL&#8217; Multiple protocols may be given as a comma-separated list, any whitespace is ignored, an optional plus sign `+&#8216; prefix enables, a hyphen-minus `-&#8216; prefix disables a protocol, so that `-ALL,&#8216; TLSv1.2 enables only the TLSv1.2 protocol. </p>
 </dd></dl>
<dt><i>tls-crl-dir , tls-crl-file</i></dt>
<dd> <p> [Option] Specify a directory / a file, respectively, that contains a CRL in PEM format to use when verifying TLS server certificates. </p>
 </dd>
<dt><i>tls-features</i></dt>
<dd> <p> [Option](Read-only) This expands to a comma-separated list of the TLS library identity and optional features. To ease substring matching the string starts and ends with a comma. Currently supported identities are `libressl&#8217; (LibreSSL) , `libssl-0x30000&#8217; (OpenSSL v3.0.0 series), `libssl-0x10100&#8217; (OpenSSL v1.1.x series) and `libssl-0x10000&#8217; (elder OpenSSL series, other clones). Optional features are preceded with a plus sign `+&#8216; when available, and with a hyphen-minus `-&#8216; otherwise. </p>
<p> Currently known features are `conf-ctx&#8217; ( <i>tls-config-pairs</i> `ctx-config&#8217; ( <i>tls-config-module</i> `ctx-set-ciphersuites&#8217; ( <code>Ciphersuites</code> slot of <i>tls-config-pairs )</i> `ctx-set-maxmin-proto&#8217; ( <i>tls-config-pairs</i> `modules-load-file&#8217; ( <i>tls-config-file</i> and `tls-rand-file&#8217; ( <i>tls-rand-file</i> </p>
 </dd>
<dt><i>tls-fingerprint-USER [at] HOST , tls-fingerprint-HOST , tls-fingerprint</i></dt>
<dd> <p> [Option] It is possible to replace the verification of the connection peer certificate against the entire local pool of CAs (for more see Sx Encrypted network communication ) with the comparison against a precalculated certificate message digest, the so-called fingerprint, to be specified as the used <i>tls-fingerprint-digest</i> This fingerprint can for example be calculated with `<code>tls</code> &#8216; Ns &nbsp;fingerprint HOST . </p>
 </dd>
<dt><i>tls-fingerprint-digest-USER [at] HOST , tls-fingerprint-digest-HOST</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;tls-fingerprint-digest [Option] The message digest to be used when creating TLS certificate fingerprints, the defaults, if available, in test order, being `BLAKE2s256&#8217; , `SHA256&#8217; For the complete list of digest algorithms refer to <i>smime-sign-digest</i> </p>
 </dd>
<dt><i>tls-rand-file</i></dt>
<dd> <p> [Option] If <i>tls-features</i> announces `,+tls-rand-file,&#8216; then this will be queried to find a file with random entropy data which can be used to seed the P(seudo)R(andom)N(umber)G(enerator), see RAND_load_file3. The default filename ( RAND_file_name3 normally ~/.rnd will be used if this variable is not set or empty, or if the Sx Filename transformations fail. Shall seeding the PRNG have been successful, RAND_write_file3 will be called to update the entropy. Remarks: libraries which do not announce this feature seed the PRNG by other means. </p>
 </dd>
<dt><i>tls-verify-USER [at] HOST , tls-verify-HOST , tls-verify</i></dt>
<dd> <p> [Option] Variable chain that sets the action to be performed if an error occurs during TLS server certificate validation against the specified or default trust stores <i>tls-ca-dir</i> <i>tls-ca-file</i> or the TLS library built-in defaults (unless usage disallowed via <i>tls-ca-no-defaults )</i> and as fine-tuned via <i>tls-ca-flags</i> Valid (case-insensitive) values are `strict&#8217; (fail and close connection immediately), `ask&#8217; (ask whether to continue on standard input), `warn&#8217; (show a warning and continue), `ignore&#8217; (do not perform validation). The default is `ask&#8217; </p>
 </dd>
<dt><i>toplines</i></dt>
<dd> <p> If defined, gives the number of lines of a message to be displayed with the command <code>top</code> if unset, the first five lines are printed, if set to 0 the variable <i>screen</i> is inspected. If the value is negative then its absolute value will be used for unsigned right shifting (see <code>vexpr</code> the <i>screen</i> height. </p>
 </dd>
<dt><i>topsqueeze</i></dt>
<dd> <p> (Boolean) If set then the <code>top</code> command series will strip adjacent empty lines and quotations. </p>
 </dd>
<dt><i>ttycharset</i></dt>
<dd> <p> The character set of the terminal S-nail operates on, and the one and only supported character set that S-nail can use if no character set conversion capabilities have been compiled into it, in which case it defaults to ISO-8859-1. Otherwise it defaults to UTF-8. Sufficient locale support provided the default will be preferably deduced from the locale environment if that is set (for example <code>LC_CTYPE</code> see there for more); runtime locale changes will be reflected by <i>ttycharset</i> except during the program startup phase and if -<code>S</code> had been used to freeze the given value. Refer to the section Sx Character sets for the complete picture about character sets. </p>
 </dd>
<dt><i>typescript-mode</i></dt>
<dd> <p> (Boolean) A special multiplex variable that disables all variables and settings which result in behaviour that interferes with running S-nail in <a href="/docs/linux/man/1-script/">script</a>(1); it sets <i>colour-disable</i> <i>line-editor-disable</i> and (before startup completed only) <i>termcap-disable</i> Unsetting it does not restore the former state of the covered settings. </p>
 </dd>
<dt><i>umask</i></dt>
<dd> <p> For a safe-by-default policy the process file mode creation mask <a href="/docs/linux/man/2-umask/">umask</a>(2) will be set to `0077&#8217; on program startup after the resource files have been loaded, and unless this variable is set. By assigning this an empty value the active setting will not be changed, otherwise the given value will be made the new file mode creation mask. Child processes inherit the file mode creation mask of their parent. </p>
 </dd>
<dt><i>user-HOST , user</i></dt>
<dd> <p> [v15-compat] Variable chain that sets a global fallback user name, used in case none has been given in the protocol and account-specific URL. This variable defaults to the name of the user who runs S-nail. </p>
 </dd>
<dt><i>v15-compat</i></dt>
<dd> <p> Enable upward compatibility with S-nail version 15.0 in respect to which configuration options are available and how they are handled. If set to a non-empty value the command modifier <code>wysh</code> is implied and thus enforces Sx Shell-style argument quoting over Sx Old-style argument quoting for all commands which support both. This manual uses [v15-compat] and [no v15-compat] to refer to the new and the old way of doing things, respectively. </p>
 </dd>
<dt><i>verbose</i></dt>
<dd> <p> Verbose mode enables logging of informational context messages. Historically a (Boolean) variable, this can either be set multiple times (what the command line option -<code>v</code> uses), or be assigned a numeric value in order to increase verbosity. Assigning the value 0 disables verbosity and thus (almost) equals <code>unset</code> The maximum number is 3. Also see <i>debug</i> </p>
 </dd>
<dt><i>version , version-date</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;version-hexnum , version-major , version-minor , version-update (Read-only) S-nail version information: the first variable is a string with the complete version identification, the second the release date in ISO 8601 notation without time. The third is a 32-bit hexadecimal number with the upper 8 bits storing the major, followed by the minor and update version numbers which occupy 12 bits each. The latter three variables contain only decimal digits: the major, minor and update version numbers. The output of the command <code>version</code> will include this information. </p>
 </dd>
<dt><i>writebackedited</i></dt>
<dd> <p> If this variable is set messages modified using the <code>edit</code> or <code>visual</code> commands are written back to the current folder when it is quit; it is only honoured for writable folders in MBOX format, though. Note that the editor will be pointed to the raw message content in that case, i.e., neither MIME decoding nor decryption will have been performed, and proper <i>mbox-rfc4155</i> `From_&#8216; quoting of newly added or edited content is also left as an exercise to the user. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> The term ``environment variable&#8217;&#8216; should be considered an indication that these variables are either standardized as vivid parts of process environments, or that they are commonly found in there. The process environment is inherited from the <a href="/docs/linux/man/1-sh/">sh</a>(1) once S-nail is started, and unless otherwise explicitly noted handling of the following variables transparently integrates into that of the Sx INTERNAL VARIABLES from S-nail&#8217;s point of view. This means they can be managed via <code>set</code> and <code>unset</code> causing automatic program environment updates (to be inherited by newly created child processes). </p>
<p> In order to integrate other environment variables equally they need to be imported (linked) with the command <code>environ</code> This command can also be used to set and unset non-integrated environment variables from scratch, sufficient system support provided. The following example, applicable to a POSIX shell, sets the <code>COLUMNS</code> environment variable for S-nail only, and beforehand exports the <code>EDITOR</code> in order to affect any further processing in the running shell: </p>
<blockquote><pre><code>$ EDITOR=&quot;vim -u ${HOME}/.vimrc&quot;
$ export EDITOR
$ COLUMNS=80 s-nail -R
</code></pre>
</blockquote>
<dl>
<dt><code>COLUMNS</code></dt>
<dd> <p> The user&#8217;s preferred width in column positions for the terminal screen. Queried and used once on program startup in interactive or batch ( -<code>#</code> mode, actively managed for child processes and the MLE (see Sx On terminal control and line editor ) in interactive mode thereafter. Non-interactive mode always uses, and the fallback default is a compile-time constant, by default 80 columns. If in batch mode <code>COLUMNS</code> and <code>LINES</code> are both set but not both are usable (empty, not a number, or 0) at program startup, then the real terminal screen size will be (tried to be) determined once. (Normally the <a href="/docs/linux/man/1-sh/">sh</a>(1) manages these variables, and unsets them for pipe specifications etc.) </p>
 </dd>
<dt><code>DEAD</code></dt>
<dd> <p> The name of the (mailbox) <code>folder</code> to use for saving aborted messages if <i>save</i> is set; this defaults to ~/dead.letter If the variable <i>debug</i> is set no output will be generated, otherwise the contents of the file will be replaced. Except shell globs Sx Filename transformations (also see <code>folder</code> will be performed. </p>
 </dd>
<dt><code>EDITOR</code></dt>
<dd> <p> Pathname of the text editor to use for the <code>edit</code> command and <code>~e</code> (see&nbsp; Sx COMMAND ESCAPES ) <code>VISUAL</code> is used for a more display oriented editor. </p>
 </dd>
<dt><code>HOME</code></dt>
<dd> <p> The user&#8217;s home directory. This variable is only used when it resides in the process environment. The calling user&#8217;s home directory will be used instead if this directory does not exist, is not accessible or cannot be read; it will always be used for the root user. (No test for being writable is performed to allow usage by non-privileged users within read-only jails, but dependent on settings this directory is a default write target for, for example, <code>DEAD</code> <code>MBOX</code> and more.) </p>
 </dd>
<dt><code>LC_ALL , LC_CTYPE , LANG</code></dt>
<dd> <p> [Option] The (names in lookup order of the) <a href="/docs/linux/man/7-locale/">locale</a>(7) (and / or see <a href="/docs/linux/man/3-setlocale/">setlocale</a>(3)) which indicates the used Sx Character sets . Runtime changes trigger automatic updates of the entire locale system, which includes updating <i>ttycharset</i> (except during startup if the variable has been frozen via -<code>S )</code> </p>
 </dd>
<dt><code>LINES</code></dt>
<dd> <p> The user&#8217;s preferred number of lines for the terminal screen. The behaviour is as described for <code>COLUMNS</code> yet the compile-time constant used in non-interactive mode and as a fallback defaults to 24 (lines). </p>
 </dd>
<dt><code>LISTER</code></dt>
<dd> <p> Pathname of the directory lister to use in the <code>folders</code> command when operating on local mailboxes. Default is <a href="/docs/linux/man/1-ls/">ls</a>(1) (path search through <code>SHELL )</code> </p>
 </dd>
<dt><code>LOGNAME</code></dt>
<dd> <p> Upon startup S-nail will actively ensure that this variable refers to the name of the user who runs S-nail, in order to be able to pass a verified name to any newly created child process. </p>
 </dd>
<dt><code>MAIL</code></dt>
<dd> <p> Is used as the user&#8217;s Sx primary system mailbox unless <i>inbox</i> is set. If the environmental fallback is also not set, a built-in compile-time default is used. This is assumed to be an absolute pathname. </p>
 </dd>
<dt><code>MAILCAPS</code></dt>
<dd> <p> [Option] Override the default path search of Sx The Mailcap files : any existing file therein will be loaded in sequence, appending any content to the list of MIME type handler directives. The RFC 1524 standard imposed default value is assigned otherwise: `~/.mailcap:/etc/mailcap:/usr/etc/mailcap:/usr/local/etc/mailcap&#8217; (The default value is a compile-time [Option].) </p>
 </dd>
<dt><code>MAILRC</code></dt>
<dd> <p> Is used as a startup file instead of ~/.mailrc if set. In order to avoid side-effects from configuration files scripts should either set this variable to /dev/null or the -<code>:</code> command line option should be used. </p>
 </dd>
<dt><code>MAILX_NO_SYSTEM_RC</code></dt>
<dd> <p> If this variable is set then reading of s-nail.rc (aka <i>system-mailrc</i> at startup is inhibited, i.e., the same effect is achieved as if S-nail had been started up with the option -<code>:</code> (and according argument) or -<code>n</code> This variable is only used when it resides in the process environment. </p>
 </dd>
<dt><code>MBOX</code></dt>
<dd> <p> The name of the user&#8217;s Sx secondary mailbox file. A logical subset of the special Sx Filename transformations (also see <code>folder</code> are supported. The default is ~/mbox Traditionally this MBOX is used as the file to save messages from the Sx primary system mailbox that have been read. Also see Sx Message states . </p>
 </dd>
<dt><code>NETRC</code></dt>
<dd> <p> [v15-compat][Option] This variable overrides the default location of the user&#8217;s ~/.netrc file. </p>
 </dd>
<dt><code>PAGER</code></dt>
<dd> <p> Pathname of the program to use for backing the command <code>more</code> and when the <i>crt</i> variable enforces usage of a pager for output. The default paginator is <a href="/docs/linux/man/1-more/">more</a>(1) (path search through <code>SHELL )</code> </p>
<p> S-nail inspects the contents of this variable: if its contains the string ``less&#8217;&#8216; then a non-existing environment variable <code>LESS</code> will be set to (the portable) `RI&#8217; , likewise for ``lv&#8217;&#8216; <code>LV</code> will optionally be set to `-c&#8217; Also see <i>colour-pager</i> </p>
 </dd>
<dt><code>PATH</code></dt>
<dd> <p> A colon-separated list of directories that is searched by the shell when looking for commands, for example `/bin:/usr/bin:/usr/local/bin&#8217; </p>
 </dd>
<dt><code>POSIXLY_CORRECT</code></dt>
<dd> <p> This environment entry is automatically squared with <i>posix</i> </p>
 </dd>
<dt><code>SHELL</code></dt>
<dd> <p> The shell to use for the commands <code>!</code> <code>shell</code> the <code>~!</code> Sx COMMAND ESCAPES and when starting subprocesses. A default shell is used if this environment variable is not defined. </p>
 </dd>
<dt><code>SOCKS5_PROXY</code></dt>
<dd> <p> This environment entry is automatically squared with <i>socks-proxy</i> </p>
 </dd>
<dt><code>SOURCE_DATE_EPOCH</code></dt>
<dd> <p> Specifies a time in seconds since the Unix epoch (1970-01-01) to be used in place of the current time. This variable is looked up upon program startup, and its existence will switch S-nail to a reproducible mode ( Lk <a rel="nofollow" href="https://reproducible-builds.org">https://reproducible-builds.org</a> which uses deterministic random numbers, a special fixated pseudo <code>LOGNAME</code> and more. This operation mode is used for development and by software packagers. [v15 behaviour may differ] Currently an invalid setting is only ignored, rather than causing a program abortion. </p>
<blockquote><p> <code>$ SOURCE_DATE_EPOCH=`date +%s` s-nail</code> </p>
</blockquote>
 </dd>
<dt><code>TERM</code></dt>
<dd> <p> [Option] The terminal type for which output is to be prepared. For extended colour and font control please refer to Sx Coloured display , and for terminal management in general to Sx On terminal control and line editor . </p>
 </dd>
<dt><code>TMPDIR</code></dt>
<dd> <p> Except for the root user this variable defines the directory for temporary files to be used instead of /tmp (or the given compile-time constant) if set, existent, accessible as well as read- and writable. This variable is only used when it resides in the process environment, but S-nail will ensure at startup that this environment variable is updated to contain a usable temporary directory. </p>
 </dd>
<dt><code>USER</code></dt>
<dd> <p> Identical to <code>LOGNAME</code> (see there), but this variable is not standardized, should therefore not be used, and is only corrected if already set. </p>
 </dd>
<dt><code>VISUAL</code></dt>
<dd> <p> Pathname of the text editor to use for the <code>visual</code> command and <code>~v</code> (see&nbsp; Sx COMMAND ESCAPES ) <code>EDITOR</code> is used for a less display oriented editor. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.mailcap , /etc/mailcap </code></dt>
<dd> <p> [Option] Personal and system-wide MIME type handler definition files, see Sx The Mailcap files . (The shown names are part of the RFC 1524 standard search path <code>MAILCAPS .</code> </p>
 </dd>
<dt><code>~/.mailrc , s-nail.rc </code></dt>
<dd> <p> User-specific and system-wide files giving initial commands, the Sx Resource files . (The used filenames come from <i>MAILRC</i> and <i>system-mailrc</i> respectively.) </p>
 </dd>
<dt><code>~/mbox </code></dt>
<dd> <p> The default value for <code>MBOX</code> </p>
 </dd>
<dt><code>~/.mime.types , /etc/mime.types </code></dt>
<dd> <p> Personal and system-wide MIME types, see Sx The mime.types files . </p>
 </dd>
<dt><code>~/.netrc </code></dt>
<dd> <p> [v15-compat][Option] The default location of the user&#8217;s .netrc file - the section Sx The .netrc file documents the file format. The used path can be set via <code>NETRC</code> </p>
 </dd>
<dt><code>/dev/null </code></dt>
<dd> <p> The data sink <a href="/docs/linux/man/4-null/">null</a>(4). </p>
 </dd>
<dt><code>~/.rnd </code></dt>
<dd> <p> [Option] Possible location for persistent random entropy seed storage, see <i>tls-rand-file</i> </p>
 </dd></dl>
<h3>Resource files</h3>
<p> Upon startup S-nail reads in several resource files, in order: </p>
<dl>
<dt><code>s-nail.rc </code></dt>
<dd> <p> System wide initialization file ( <i>system-mailrc</i> Reading of this file can be suppressed, either by using the -<code>:</code> (and according argument) or -<code>n</code> command line options, or by setting the Sx ENVIRONMENT variable <code>MAILX_NO_SYSTEM_RC</code> </p>
 </dd>
<dt><code>~/.mailrc </code></dt>
<dd> <p> File giving initial commands. A different file can be chosen by setting the Sx ENVIRONMENT variable <code>MAILRC</code> Reading of this file can be suppressed with the -<code>:</code> command line option. </p>
 </dd>
<dt><i>mailx-extra-rc</i></dt>
<dd> <p> Defines a startup file to be read after all other resource files. It can be used to specify settings that are not understood by other <a href="/docs/linux/man/1-mailx/">mailx</a>(1) implementations, for example. </p>
 </dd></dl>
<p> The content of these files is interpreted as follows: </p>
<ul>
<li> <p> The whitespace characters space, tabulator and newline, as well as those defined by the variable <i>ifs</i> are removed from the beginning and end of input lines.  </li>
<li>  Empty lines are ignored.  </li>
<li>  Any other line is interpreted as a command. It may be spread over multiple input lines if the newline character is ``escaped&#8217;&#8216; by placing a reverse solidus character `\&#8216; as the last character of the line; whereas any leading whitespace of follow lines is ignored, trailing whitespace before a escaped newline remains in the input.  </li>
<li>  If the line (content) starts with the number sign `#&#8216; then it is a comment-command and also ignored. (The comment-command is a real command, which does nothing, and therefore the usual follow lines mechanism applies!)  </li>
</ul>
 </p>
<p> Errors while loading these files are subject to the settings of <i>errexit</i> and <i>posix</i> More files with syntactically equal content can be <code>source ed</code> The following, saved in a file, would be an examplary content: </p>
<blockquote><pre><code> # This line is a comment command. And y\
    es, it is really continued here.
set debug \
    verbose
    set editheaders
</code></pre>
</blockquote>
<h3>The mime.types files</h3>
<p> As stated in Sx HTML mail and MIME attachments S-nail needs to learn about MIME (Multipurpose Internet Mail Extensions) media types in order to classify message and attachment content. One source for them are mime.types files, the loading of which can be controlled by setting the variable <i>mimetypes-load-control</i> Another is the command <code>mimetype</code> which also offers access to S-nails MIME type cache. mime.types files have the following syntax: </p>
<blockquote><pre><code>type/subtype extension [extension ...]
# For example text/html html htm
</code></pre>
</blockquote>
<p> where `type/subtype&#8217; define the MIME media type, as standardized in RFC 2046: `type&#8217; is used to declare the general type of data, while the `subtype&#8217; specifies a specific format for that type of data. One or multiple filename `extension&#8217; Ns s, separated by whitespace, can be bound to the media type format. Comments may be introduced anywhere on a line with a number sign `#&#8216; , causing the remaining line to be discarded. S-nail also supports an extended, non-portable syntax in especially crafted files, which can be loaded via the alternative value syntax of <i>mimetypes-load-control</i> and prepends an optional `type-marker&#8217; : </p>
<blockquote><p> <code>[type-marker ]type/subtype extension [extension ...]</code> </p>
</blockquote>
<p> The following type markers are supported: </p>
<dl>
<dt><i>?</i></dt>
<dd> <p> Treat message parts with this content as plain text. </p>
 </dd>
<dt><i>?t</i></dt>
<dd> <p> The same as plain <i>?</i> </p>
 </dd>
<dt><i>?h</i></dt>
<dd> <p> Treat message parts with this content as HTML tagsoup. If the [Option]al HTML-tagsoup-to-text converter is not available treat the content as plain text instead. </p>
 </dd>
<dt><i>?H</i></dt>
<dd> <p> Likewise <i>?h</i> but instead of falling back to plain text require an explicit content handler to be defined. </p>
 </dd>
<dt><i>?q</i></dt>
<dd> <p> If no handler can be found a text message is displayed which says so. This can be annoying, for example signatures serve a contextual purpose, their content is of no use by itself. This marker will avoid displaying the text message. </p>
 </dd></dl>
<p> Further reading: for sending messages: <code>mimetype</code> <i>mime-allow-text-controls</i> <i>mimetypes-load-control</i> For reading etc. messages: Sx HTML mail and MIME attachments , Sx The Mailcap files , <code>mimetype</code> <i>mime-counter-evidence</i> <i>mimetypes-load-control</i> <i>pipe-TYPE/SUBTYPE</i> <i>pipe-EXTENSION</i>  </p>
<h3>The Mailcap files</h3>
<p> [Option] RFC 1524 defines a ``User Agent Configuration Mechanism&#8217;&#8216; to be used to inform mail user agent programs about the locally installed facilities for handling various data formats, i.e., about commands and how they can be used to display, edit et cetera MIME part contents, as well as a default path search that includes multiple possible locations of resource files, and the <code>MAILCAPS</code> environment variable to overwrite that. Handlers found from doing the path search will be cached, the command <code>mailcap</code> operates on that cache, and the variable <i>mailcap-disable</i> will suppress automatic loading, and usage of any mailcap handlers. Sx HTML mail and MIME attachments gives a general overview of how MIME types are handled. </p>
<p> ``Mailcap&#8217;&#8216; files consist of a set of newline separated entries. Comment lines start with a number sign `#&#8216; (in the first column!) and are ignored. Empty lines are ignored. All other lines are interpreted as mailcap entries. An entry definition may be split over multiple lines by placing the reverse solidus character `\&#8216; last in all but the final line. The standard does not specify how leading whitespace of successive lines is to be treated, therefore they are retained. </p>
<p> ``Mailcap&#8217;&#8216; entries consist of a number of semicolon `;&#8216; separated fields. The first two fields are mandatory and must occur in the specified order, the remaining fields are optional and may appear in any order. Leading and trailing whitespace of field content is ignored (removed). The reverse solidus `\&#8216; character can be used to escape any following character including semicolon and itself in the content of the second field, and in value parts of any optional key/value field. </p>
<p> The first field defines the MIME `TYPE/SUBTYPE&#8217; the entry is about to handle (case-insensitively). If the subtype is specified as an asterisk `*&#8216; the entry is meant to match all subtypes of the named type, e.g., `audio/*&#8216; would match any audio type. The second field is the <code>view</code> shell command used to display MIME parts of the given type. </p>
<p> Data consuming shell commands will be fed message (MIME part) data on standard input unless one or more instances of the (unquoted) string `%s&#8217; are used: these formats will be replaced with a temporary file(name) that has been prefilled with the parts data. Data producing shell commands are expected to generata data on their standard output unless that format is used. In all cases any given `%s&#8217; format is replaced with a properly shell quoted filename. When a command requests a temporary file via `%s&#8217; then that will be removed again, as if the <code>x-mailx-tmpfile</code> and <code>x-mailx-tmpfile-fill</code> flags had been set; unless the command requests <code>x-mailx-async</code> the <code>x-mailx-tmpfile-unlink</code> flag is also implied; see below for more. </p>
<p> Optional fields define single-word flags (case-insensitive), or key / value pairs consisting of a case-insensitive keyword, an equals sign `=&#8216; , and a shell command; whitespace surrounding the equals sign is removed. Optional fields include the following: </p>
<dl>
<dt><code>compose</code></dt>
<dd> <p> A program that can be used to compose a new body or body part in the given format. (Currently unused.) </p>
 </dd>
<dt><code>composetyped</code></dt>
<dd> <p> Similar to the <code>compose</code> field, but is to be used when the composing program needs to specify the `Content-type:&#8216; header field to be applied to the composed data. (Currently unused.) </p>
 </dd>
<dt><code>copiousoutput</code></dt>
<dd> <p> A flag field which indicates that the output of the <code>view</code> command is integrable into S-nails normal visual display. It is mutually exclusive with <code>needsterminal</code> </p>
 </dd>
<dt><code>description</code></dt>
<dd> <p> A textual description that describes this type of data. The text may optionally be enclosed within double quotation marks `&#8216; </p>
 </dd>
<dt><code>edit</code></dt>
<dd> <p> A program that can be used to edit a body or body part in the given format. (Currently unused.) </p>
 </dd>
<dt><code>nametemplate</code></dt>
<dd> <p> This field specifies a filename format for the `%s&#8217; format used in the shell command fields, in which `%s&#8217; will be replaced by a random string. (The filename is also stored in and passed to subprocesses via <code>MAILX_FILENAME_TEMPORARY .</code> The standard says this is ``only expected to be relevant in environments&#8217;&#8216; <br />
&nbsp;<wbr>&nbsp;where filename extensions are meaningful , and so this field is ignored unless the `%s&#8217; is a prefix, optionally followed by (ASCII) alphabetic and numeric characters, the underscore and the period. For example, to specify that a JPG file is to be passed to an image viewer with a name ending in `.jpg&#8217; , `nametemplate=%s.jpg&#8217; can be used. </p>
 </dd>
<dt><code>needsterminal</code></dt>
<dd> <p> This flag field indicates that the given shell command must be run on an interactive terminal. S-nail will temporarily release the terminal to the given command in interactive mode, in non-interactive mode this entry will be entirely ignored; this flag implies <code>x-mailx-noquote</code> </p>
 </dd>
<dt><code>print</code></dt>
<dd> <p> A program that can be used to print a message or body part in the given format. (Currently unused.) </p>
 </dd>
<dt><code>test</code></dt>
<dd> <p> Specifies a program to be run to test some condition, for example, the machine architecture, or the window system in use, to determine whether or not this mailcap entry applies. If the test fails, a subsequent mailcap entry should be sought; also see <code>x-mailx-test-once</code> Standard I/O of the test program is redirected from and to /dev/null and the format `%s&#8217; is not supported (the data does not yet exist). </p>
 </dd>
<dt><code>textualnewlines</code></dt>
<dd> <p> A flag field which indicates that this type of data is line-oriented and that, if encoded in `base64&#8217; , all newlines should be converted to canonical form (CRLF) before encoding, and will be in that form after decoding. (Currently unused.) </p>
 </dd>
<dt><code>x11-bitmap</code></dt>
<dd> <p> Names a file, in X11 bitmap (xbm) format, which points to an appropriate icon to be used to visually denote the presence of this kind of data. This field is not used by S-nail. </p>
 </dd>
<dt><code>x-mailx-async</code></dt>
<dd> <p> Extension flag field that denotes that the given <code>view</code> command shall be executed asynchronously, without blocking S-nail. Cannot be used in conjunction with <code>needsterminal</code> the standard output of the command will go to /dev/null </p>
 </dd>
<dt><code>x-mailx-noquote</code></dt>
<dd> <p> An extension flag field that indicates that even a <code>copiousoutput</code> <code>view</code> command shall not be used when <i>quote </i><code>ing messages, as it would by default.</code> </p>
 </dd>
<dt><code>x-mailx-test-once</code></dt>
<dd> <p> Extension flag which denotes whether the given <code>test</code> command shall be evaluated once only with its exit status being cached. This is handy if some global unchanging condition is to be queried, like ``running under the X Window System&#8217;&#8216; </p>
 </dd>
<dt><code>x-mailx-tmpfile</code></dt>
<dd> <p> Extension flag field that requests creation of a zero-sized temporary file, the name of which is to be placed in the environment variable <code>MAILX_FILENAME_TEMPORARY</code> It is an error to use this flag with commands that include a `%s&#8217; format (because that is implemented by means of this temporary file). </p>
 </dd>
<dt><code>x-mailx-tmpfile-fill</code></dt>
<dd> <p> Normally the MIME part content is passed to the handler via standard input; if this flag is set then the data will instead be written into the implied <code>x-mailx-tmpfile</code> In order to cause deletion of the temporary file you will have to set <code>x-mailx-tmpfile-unlink</code> explicitly! It is an error to use this flag with commands that include a `%s&#8217; format. </p>
 </dd>
<dt><code>x-mailx-tmpfile-unlink</code></dt>
<dd> <p> Extension flag field that requests that the temporary file shall be deleted automatically when the command loop is entered again at latest. It is an error to use this flag with commands that include a `%s&#8217; format, or in conjunction with <code>x-mailx-async</code> <code>x-mailx-tmpfile</code> is implied. </p>
 </dd>
<dt><code>x-mailx-last-resort</code></dt>
<dd> <p> An extension flag that indicates that this handler shall only be used as a last resort, when no other source (see Sx HTML mail and MIME attachments ) provides a MIME handler. </p>
 </dd>
<dt><code>x-mailx-ignore</code></dt>
<dd> <p> An extension that enforces that this handler is not used at all. </p>
 </dd></dl>
<p> The standard includes the possibility to define any number of additional fields, prefixed by `x-&#8216; Flag fields apply to the entire ``Mailcap&#8217;&#8216; entry --- in some unusual cases, this may not be desirable, but differentiation can be accomplished via separate entries, taking advantage of the fact that subsequent entries are searched if an earlier one does not provide enough information. For example, if a <code>view</code> command needs to specify the <code>needsterminal</code> flag, but the <code>compose</code> command shall not, the following will help out the latter: </p>
<blockquote><pre><code>application/postscript; ps-to-terminal %s; needsterminal
application/postscript; ps-to-terminal %s; compose=idraw %s
</code></pre>
</blockquote>
<p> In value parts of command fields any occurrence of the format string `%t&#8217; will be replaced by the `TYPE/SUBTYPE&#8217; specification. Any named parameter from a messages&#8217; `Content-type:&#8216; field may be embedded into the command line using the format `%{&#8216; followed by the parameter name and a closing brace `}&#8216; character. The entire parameter should appear as a single command line argument, regardless of embedded spaces, shell quoting will be performed by the RFC 1524 processor, thus: </p>
<blockquote><pre><code># Message
Content-type: multipart/mixed; boundary=42
# Mailcap file
multipart/*; /usr/local/bin/showmulti \
  %t %{boundary} ; composetyped = /usr/local/bin/makemulti
# Executed shell command
/usr/local/bin/showmulti multipart/mixed 42
</code></pre>
</blockquote>
<p> Note that S-nail does not support handlers for multipart MIME parts as shown in this example (as of today). It does not support the additional formats `%n&#8217; and `%F&#8217; An example file, also showing how to properly deal with the expansion of `%s&#8217; , which includes any quotes that are necessary to make it a valid shell argument by itself and thus will cause undesired behaviour when placed in additional user-provided quotes: </p>
<blockquote><pre><code># Comment line
text/richtext; richtext %s; copiousoutput
text/x-perl; perl -cWT %s; nametemplate = %s.pl
# Exit EX_TEMPFAIL=75 on signal
application/pdf; \
  infile=%s\; \
    trap &quot;rm -f ${infile}&quot; EXIT\; \
    trap &quot;exit 75&quot; INT QUIT TERM\; \
    mupdf &quot;${infile}&quot;; \
  test = [ -n &quot;${DISPLAY}&quot; ]; \
  nametemplate = %s.pdf; x-mailx-async
application/pdf; pdftotext -layout - -; copiousoutput
application/*; echo &quot;This is \\&quot;%t\\&quot; but \
    is 50 \% Greek to me&quot; \; &lt; %s head -c 512 | cat -vet; \
  copiousoutput; x-mailx-noquote; x-mailx-last-resort
</code></pre>
</blockquote>
<p> Further reading: Sx HTML mail and MIME attachments , Sx The mime.types files , <code>mimetype</code> <code>MAILCAPS</code> <i>mime-counter-evidence</i> <i>pipe-TYPE/SUBTYPE</i> <i>pipe-EXTENSION</i>  </p>
<h3>The .netrc file</h3>
<p> User credentials for machine accounts (see Sx On URL syntax and credential lookup ) can be placed in the .netrc file, which will be loaded and cached when requested by <i>netrc-lookup</i> The default location ~/.netrc may be overridden by the <code>NETRC</code> environment variable. As long as syntax constraints are honoured the file source may be replaced with the output of the shell command set in <i>netrc-pipe</i> to load an encrypted file, for example. The cache can be managed with the command <code>netrc</code> </p>
<p> The file consists of space, tabulator or newline separated tokens. This parser implements a superset of the original BSD syntax, but users should nonetheless be aware of portability glitches, shall their .netrc be usable across multiple programs and platforms: </p>
<ul>
<li> <p> BSD only supports double quotation marks, for example `password&#8217; pass with spaces .  </li>
<li>  BSD (only?) supports escaping of single characters via a reverse solidus (a space could be escaped via `\&nbsp;&#8216; ) , in- as well as outside of a quoted string. This method is assumed to be present, and will actively be used to quote double quotation marks `&#8216; and reverse solidus `\&#8216; characters inside the <code>login</code> and <code>password</code> tokens, for example for display purposes.  </li>
<li>  BSD does not require a final quotation mark of the last user input token.  </li>
<li>  The original BSD (Berknet) parser also supported a format which allowed tokens to be separated with commas - whereas at least Hewlett-Packard still seems to support this syntax, this parser does not!  </li>
<li>  As a non-portable extension some widely-used programs support shell-style comments: if an input line starts, after any amount of whitespace, with a number sign `#&#8216; , then the rest of the line is ignored.  </li>
<li>  Whereas other programs may require that the .netrc file is accessible by only the user if it contains a <code>password</code> token for any other <code>login</code> than ``anonymous&#8217;&#8216; this parser will always require these strict permissions.  </li>
</ul>
 </p>
<p> Of the following list of supported tokens this parser uses (and caches) <code>machine</code> <code>login</code> and <code>password</code> An existing <code>default</code> entry will not be used. </p>
<dl>
<dt><code>machine </code><i>name</i></dt>
<dd> <p> The hostname of the entries&#8217; machine, lowercase-normalized before use. Any further file content, until either end-of-file or the occurrence of another <code>machine</code> or a <code>default</code> first-class token is bound (only related) to the machine <i>name</i> </p>
<p> As an extension that should not be the cause of any worries this parser supports a single wildcard prefix for <i>name</i> </p>
<blockquote><pre><code>machine *.example.com login USER password PASS
machine pop3.example.com login USER password PASS
machine smtp.example.com login USER password PASS
</code></pre>
</blockquote>
<p> which would match `xy.example.com&#8217; as well as `pop3.example.com&#8217; , but neither `example.com&#8217; nor `local.smtp.example.com&#8217; In the example neither `pop3.example.com&#8217; nor `smtp.example.com&#8217; will be matched by the wildcard, since the exact matches take precedence (it is however faster to specify it the other way around). </p>
 </dd>
<dt><code>default</code></dt>
<dd> <p> This is the same as <code>machine</code> except that it is a fallback entry that is used shall none of the specified machines match; only one default token may be specified, and it must be the last first-class token. </p>
 </dd>
<dt><code>login </code><i>name</i></dt>
<dd> <p> The user name on the remote machine. </p>
 </dd>
<dt><code>password </code><i>string</i></dt>
<dd> <p> The user&#8217;s password on the remote machine. </p>
 </dd>
<dt><code>account </code><i>string</i></dt>
<dd> <p> Supply an additional account password. This is merely for FTP purposes. </p>
 </dd>
<dt><code>macdef </code><i>name</i></dt>
<dd> <p> Define a macro. A macro is defined with the specified <i>name</i> it is formed from all lines beginning with the next line and continuing until a blank line is (consecutive newline characters are) encountered. (Note that <code>macdef</code> entries cannot be utilized by multiple machines, too, but must be defined following the <code>machine</code> they are intended to be used with.) If a macro named <i>init</i> exists, it is automatically run as the last step of the login process. This is merely for FTP purposes. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<h3>An example configuration</h3>
<blockquote><pre><code># This example assumes v15.0 compatibility mode
set v15-compat
# Request strict TLL transport layer security checks
set tls-verify=strict
# Where are the up-to-date TLS certificates?
# (Since we manage up-to-date ones explicitly, do not use any,
# possibly outdated, default certificates shipped with OpenSSL)
#set tls-ca-dir=/etc/ssl/certs
set tls-ca-file=/etc/ssl/certs/ca-certificates.crt
set tls-ca-no-defaults
#set tls-ca-flags=partial-chain
wysh set smime-ca-file=&quot;${tls-ca-file}&quot; \
  smime-ca-no-defaults #smime-ca-flags=&quot;${tls-ca-flags}&quot;
# This could be outsourced to a central configuration file via
# tls-config-file plus tls-config-module if the used library allows.
# CipherString: explicitly define the list of ciphers, which may
# improve security, especially with protocols older than TLS v1.2.
# Seeciphers(1). Possibly best to only use tls-config-pairs-HOST
# (or -USER [at] HOST), as necessary, again..
# Note that TLSv1.3 uses Ciphersuites= instead, which will join
# with CipherString (if protocols older than v1.3 are allowed)
# Curves: especially with TLSv1.3 curves selection may be desired.
# MinProtocol,MaxProtocol: do not use protocols older than TLS v1.2.
# Change this only when the remote server does not support it:
# maybe use chain support via tls-config-pairs-HOST / -USER [at] HOST
# to define such explicit exceptions, then, e.g.,
# MinProtocol=TLSv1.1
if &quot;$tls-features&quot; =% ,+ctx-set-maxmin-proto,
  wysh set tls-config-pairs='\
      CipherString=TLSv1.2:!aNULL:!eNULL:@STRENGTH,\
      Curves=P-521:P-384:P-256,\
      MinProtocol=TLSv1.1'
else
  wysh set tls-config-pairs='\
      CipherString=TLSv1.2:!aNULL:!eNULL:@STRENGTH,\
      Curves=P-521:P-384:P-256,\
      Protocol=-ALL\,+TLSv1.1 \, +TLSv1.2\, +TLSv1.3'
endif
# Essential setting: select allowed character sets
set sendcharsets=utf-8,iso-8859-1
# A very kind option: when replying to a message, first try to
# use the same encoding that the original poster used herself!
set reply-in-same-charset
# When replying, do not merge From: and To: of the original message
# into To:. Instead old From: -&gt; new To:, old To: -&gt; merge Cc:.
set recipients-in-cc
# When sending messages, wait until the Mail-Transfer-Agent finishs.
# Only like this you will be able to see errors reported through the
# exit status of the MTA (including the built-in SMTP one)!
set sendwait
# Only use built-in MIME types, nomime.types(5) files
set mimetypes-load-control
# Default directory where we act in (relative to $HOME)
set folder=mail
# A leading &quot;+&quot; (often) means: under *folder*
# *record* is used to save copies of sent messages
set MBOX=+mbox.mbox DEAD=+dead.txt \
  record=+sent.mbox record-files record-resent
# Make &quot;file mymbox&quot; and &quot;file myrec&quot; go to..
shortcut mymbox %:+mbox.mbox myrec +sent.mbox
# Not really optional, e.g., for S/MIME
set from='Your Name &lt;address [at] exam.ple&gt;'
# It may be necessary to set hostname and/or smtp-hostname
# if the &quot;SERVER&quot; of mta and &quot;domain&quot; of from do not match.
# The `urlencode' command can be used to encode USER and PASS
set mta=(smtps?|submissions?)://[USER[:PASS]@]SERVER[:PORT] \
  smtp-auth=login/plain... \
  smtp-use-starttls
# Never refuse to start into interactive mode, and more
set emptystart \
  colour-pager crt= \
  followup-to followup-to-honour=ask-yes fullnames \
  history-file=+.s-nailhist history-size=-1 history-gabby \
  mime-counter-evidence=0b1111 \
  prompt='?\$?!\$!/\$^ERRNAME[\$account#\$mailbox-display]? ' \
  reply-to-honour=ask-yes \
  umask=
# Only include the selected header fields when typing messages
headerpick type retain from_ date from to cc subject \
  message-id mail-followup-to reply-to
# ...when forwarding messages
headerpick forward retain subject date from to cc
# ...when saving message, etc.
#headerpick save ignore ^Original-.*$ ^X-.*$
# Some mailing lists
mlist '@xyz-editor\.xyz$' '@xyzf\.xyz$'
mlsubscribe '^xfans [at] xfans\.xyz$'
# Handle a few file extensions (to store MBOX databases)
filetype bz2 'bzip2 -dc' 'bzip2 -zc' \
  gz 'gzip -dc' 'gzip -c' xz 'xz -dc' 'xz -zc' \
  zst 'zstd -dc' 'zstd -19 -zc' \
  zst.pgp 'gpg -d | zstd -dc' 'zstd -19 -zc | gpg -e'
# A real life example of a very huge free mail provider
# Instead of directly placing content inside `account',
# we `define' a macro: like that we can switch &quot;accounts&quot;
# from within *on-compose-splice*, for example!
define XooglX {
  set folder=~/spool/XooglX inbox=+syste.mbox sent=+sent
  set from='Your Name &lt;address [at] examp.ple&gt;'
  set pop3-no-apop-pop.gmXil.com
  shortcut pop %:pop3s://pop.gmXil.com
  shortcut imap %:imaps://imap.gmXil.com  # Or, entirely IMAP based setup
  #set folder=imaps://imap.gmail.com record=&quot;+[Gmail]/Sent Mail&quot; \
  # imap-cache=~/spool/cache
  set mta=smtp://USER:PASS@smtp.gmXil.com smtp-use-starttls
  # Alternatively:
  set mta=smtps://USER:PASS@smtp.gmail.com:465}
account XooglX {
  \call XooglX
}
# Here is a pretty large one which does not allow sending mails
# if there is a domain name mismatch on the SMTP protocol level,
# which would bite us if the value of from does not match, e.g.,
# for people who have a sXXXXeforge project and want to speak
# with the mailing list under their project account (in from),
# still sending the message through their normal mail provider
define XandeX {
  set folder=~/spool/XandeX inbox=+syste.mbox sent=+sent
  set from='Your Name &lt;address [at] exam.ple&gt;'
  shortcut pop %:pop3s://pop.yaXXex.com
  shortcut imap %:imaps://imap.yaXXex.com  set mta=smtps://USER:PASS@smtp.yaXXex.com:465 \
    hostname=yaXXex.com smtp-hostname=
}
account XandeX {
  \call Xandex
}
# Create some new commands so that, e.g., `ls /tmp' will..
commandalias lls '!ls ${LS_COLOUR_FLAG} -aFlrS'
commandalias llS '!ls ${LS_COLOUR_FLAG} -aFlS'
set pipe-message/external-body='?* echo $MAILX_EXTERNAL_BODY_URL'
# We do not supportgpg(1) directly yet. But simple --clearsign'd
# message parts can be dealt with as follows:
define V {
  localopts yes
  wysh set pipe-text/plain=$'?*#++=?\
    &lt; &quot;${MAILX_FILENAME_TEMPORARY}&quot; awk \
        -v TMPFILE=&quot;${MAILX_FILENAME_TEMPORARY}&quot; \'\
      BEGIN{done=0}\
      /^-----BEGIN PGP SIGNED MESSAGE-----/,/^$/ {\
        if(done++ != 0)\
          next;\
        print &quot;--- GPG --verify ---&quot;;\
        system(&quot;gpg --verify &quot; TMPFILE &quot; 2&gt;&amp;1&quot;);\
        print &quot;--- GPG --verify ---&quot;;\
        print &quot;&quot;;\
        next;\
      }\
      /^-----BEGIN PGP SIGNATURE-----/,\
          /^-----END PGP SIGNATURE-----/{\
        next;\
      }\
      {print}\
    \''
    print
}
commandalias V '\'call V
</code></pre>
</blockquote>
<p> When storing passwords in ~/.mailrc appropriate permissions should be set on this file with `$&#8216; chmod 0600 ~/.mailrc . If the [Option]al <i>netrc-lookup</i> is available user credentials can be stored in the central ~/.netrc file instead; e.g., here is a different version of the example account that sets up SMTP and POP3: </p>
<blockquote><pre><code>define XandeX {
  set folder=~/spool/XandeX inbox=+syste.mbox sent=+sent
  set from='Your Name &lt;address [at] exam.ple&gt;'
  set netrc-lookup
  # Load an encrypted ~/.netrc by uncommenting the next line
  #set netrc-pipe='gpg -qd ~/.netrc.pgp'
  set mta=smtps://smtp.yXXXXx.ru:465 \
      smtp-hostname= hostname=yXXXXx.com
  set pop3-keepalive=240 pop3-no-apop-pop.yXXXXx.ru
  commandalias xp fi pop3s://pop.yXXXXx.ru
}
account XandeX {
  \call XandeX
}
</code></pre>
</blockquote>
<p> and, in the ~/.netrc file: </p>
<blockquote><pre><code>machine *.yXXXXx.ru login USER password PASS
</code></pre>
</blockquote>
<p> This configuration should now work just fine: </p>
<blockquote><p> <code>$ echo text | s-nail -dvv -AXandeX -s Subject user [at] exam.ple</code> </p>
</blockquote>
<h3>S/MIME step by step</h3>
<p> [Option] The first thing that is needed for Sx Signed and encrypted messages with S/MIME is a personal certificate, and a private key. The certificate contains public information, in particular a name and email address(es), and the public key that can be used by others to encrypt messages for the certificate holder (the owner of the private key), and to <code>verify</code> signed messages generated with that certificate(&#8216;s private key). Whereas the certificate is included in each signed message, the private key must be kept secret. It is used to decrypt messages that were previously encrypted with the public key, and to sign messages. </p>
<p> For personal use it is recommended to get a S/MIME certificate from one of the major CAs on the Internet. Many CAs offer such certificates for free. Usually offered is a combined certificate and private key in PKCS#12 format which S-nail does not accept directly. To convert it to PEM format, the following shell command can be used; please read on for how to use these PEM files. </p>
<blockquote><pre><code>$ openssl pkcs12 -in cert.p12 -out certpem.pem -clcerts -nodes
$ # Alternatively
$ openssl pkcs12 -in cert.p12 -out cert.pem -clcerts -nokeys
$ openssl pkcs12 -in cert.p12 -out key.pem -nocerts -nodes
</code></pre>
</blockquote>
<p> There is also Lk <a rel="nofollow" href="https://www.CAcert.org">https://www.CAcert.org</a> which issues client and server certificates to members of their community for free; their root certificate ( Lk <a rel="nofollow" href="https://www.cacert.org/certs/root.crt">https://www.cacert.org/certs/root.crt</a> is often not in the default set of trusted CA root certificates, though, which means their root certificate has to be downloaded separately, and needs to be part of the S/MIME certificate validation chain by including it in <i>smime-ca-dir</i> or as a vivid member of the <i>smime-ca-file</i> But let us take a step-by-step tour on how to setup S/MIME with a certificate from CAcert.org despite this situation! </p>
<p> First of all you will have to become a member of the CAcert.org community, simply by registrating yourself via the web interface. Once you are, create and verify all email addresses you want to be able to create signed and encrypted messages for/with using the corresponding entries of the web interface. Now ready to create S/MIME certificates, so let us create a new ``client certificate&#8217;&#8216; ensure to include all email addresses that should be covered by the certificate in the following web form, and also to use your name as the ``common name&#8217;&#8216; </p>
<p> Create a private key and a certificate request on your local computer (please see the manual pages of the used commands for more in-depth knowledge on what the used arguments etc. do): </p>
<blockquote><p> <code>$ openssl req -nodes -newkey rsa:4096 -keyout key.pem -out creq.pem</code> </p>
</blockquote>
<p> Afterwards copy-and-paste the content of ``creq.pem&#8217;&#8216; into the certificate-request (CSR) field of the web form on the CAcert.org website (you may need to unfold some ``advanced options&#8217;&#8216; to see the corresponding text field). This last step will ensure that your private key (which never left your box) and the certificate belong together (through the public key that will find its way into the certificate via the certificate-request). You are now ready and can create your CAcert certified certificate. Download and store or copy-and-paste it as ``pub.crt&#8217;&#8216; </p>
<p> Yay. In order to use your new S/MIME setup a combined private key/public key (certificate) file has to be created: </p>
<blockquote><p> <code>$ cat key.pem pub.crt &gt; ME [at] HERE.com.paired</code> </p>
</blockquote>
<p> This is the file S-nail will work with. If you have created your private key with a passphrase then S-nail will ask you for it whenever a message is signed or decrypted, unless this operation has been automated as described in Sx Signed and encrypted messages with S/MIME . Set the following variables to henceforth use S/MIME (setting <i>smime-ca-file</i> is of interest for verification only): </p>
<blockquote><pre><code>? set smime-ca-file=ALL-TRUSTED-ROOT-CERTS-HERE \
    smime-sign-cert=ME [at] HERE.com.paired \
    smime-sign-digest=SHA512 \
    smime-sign from=myname [at] my.host
</code></pre>
</blockquote>
<h3>Using CRLs with S/MIME or TLS</h3>
<p> [Option] Certification authorities (CAs) issue certificate revocation lists (CRLs) on a regular basis. These lists contain the serial numbers of certificates that have been declared invalid after they have been issued. Such usually happens because the private key for the certificate has been compromised, because the owner of the certificate has left the organization that is mentioned in the certificate, etc. To seriously use S/MIME or TLS verification, an up-to-date CRL is required for each trusted CA. There is otherwise no method to distinguish between valid and invalidated certificates. S-nail currently offers no mechanism to fetch CRLs, nor to access them on the Internet, so they have to be retrieved by some external mechanism. </p>
<p> S-nail accepts CRLs in PEM format only; CRLs in DER format must be converted, like, e.g.: </p>
<blockquote><p> <code>$ openssl crl -inform DER -in crl.der -out crl.pem</code> </p>
</blockquote>
<p> To tell S-nail about the CRLs, a directory that contains all CRL files (and no other files) must be created. The <i>smime-crl-dir</i> or <i>tls-crl-dir</i> variables, respectively, must then be set to point to that directory. After that, S-nail requires a CRL to be present for each CA that is used to verify a certificate.  </p>
<h2>FAQ</h2>
<p> In general it is a good idea to turn on <i>debug</i> ( -<code>d</code> and / or <i>verbose</i> ( -<code>v</code> twice) if something does not work well. Very often a diagnostic message can be produced that leads to the problems&#8217; solution.  </p>
<h3>S-nail shortly hangs on startup</h3>
<p> This can have two reasons, one is the necessity to wait for a file lock and cannot be helped, the other being that S-nail calls the function <a href="/docs/linux/man/2-uname/">uname</a>(2) in order to query the nodename of the box (sometimes the real one is needed instead of the one represented by the internal variable <i>hostname )</i> One may have varying success by ensuring that the real hostname and `localhost&#8217; have entries in /etc/hosts or, more generally, that the name service is properly setup - and does <a href="/docs/linux/man/1-hostname/">hostname</a>(1) return the expected value? Does this local hostname have a domain suffix? RFC 6762 standardized the link-local top-level domain `.local&#8217; , try again after adding an (additional) entry with this extension.  </p>
<h3>I cannot login to Google mail (via OAuth)</h3>
<p> Since 2014 some free service providers classify programs as ``less secure&#8217;&#8216; unless they use a special authentication method (OAuth 2.0) which was not standardized for non-HTTP protocol authentication token query until August 2015 (RFC 7628). </p>
<p> Different to Kerberos / GSSAPI, which is developed since the mid of the 1980s, where a user can easily create a local authentication ticket for her- and himself with the locally installed <a href="/docs/linux/man/1-kinit/">kinit</a>(1) program, that protocol has no such local part but instead requires a world-wide-web query to create or fetch a token; since there is no local cache this query would have to be performed whenever S-nail is invoked (in interactive sessions situation may differ). </p>
<p> S-nail does not directly support OAuth. It, however, supports XOAUTH2 / OAUTHBEARER, see Sx But, how about XOAUTH2 / OAUTHBEARER? If that is not used it is necessary to declare S-nail a ``less secure app&#8217;&#8216; (on the providers account web page) in order to read and send mail. However, it also seems possible to take the following steps instead: </p>
<ol>
<li> <p> give the provider the number of a mobile phone,  </li>
<li>  enable ``2-Step Verification&#8217;&#8216;  </li>
<li>  create an application specific password (16 characters), and  </li>
<li>  use that special password instead of the real Google account password in S-nail (for more on that see the section Sx On URL syntax and credential lookup ) .  </li>
</ol>
 </p>
<h3>But, how about XOAUTH2 / OAUTHBEARER?</h3>
<p> Following up Sx I cannot login to Google mail (via OAuth) one OAuth-based authentication method is available: the OAuth 2.0 bearer token usage as standardized in RFC 6750 (according SASL mechanism in RFC 7628), also known as XOAUTH2 and OAUTHBEARER, allows fetching a temporary access token via the web that can locally be used as a <i>password</i> The protocol is simple and extendable, token updates or even password changes via a simple TLS secured server login would be possible in theory, but today a web browser and an external support tool are prerequisites for using this authentication method. The token times out and must be periodically refreshed via the web. </p>
<p> Some hurdles must be taken before being able to use this method. Using GMail as an example, an application (that is a name) must be registered, for which credentials, a ``client ID&#8217;&#8216; and a ``client secret&#8217;&#8216; need to be created and saved locally (in a secure way). These initial configuration steps can be performed at Lk <a rel="nofollow" href="https://console.developers.google.com/apis/credentials">https://console.developers.google.com/apis/credentials</a> . Thereafter a refresh token can be requested; a python program to do this for GMail accounts is Lk <a rel="nofollow" href="https://github.com/google/gmail-oauth2-tools/raw/master/python/oauth2.py">https://github.com/google/gmail-oauth2-tools/raw/master/python/oauth2.py</a> : </p>
<blockquote><pre><code>$ python oauth2.py --user=EMAIL \
  --client-id=THE-ID --client-secret=THE-SECRET \
  --generate_oauth2_token
To authorize token, visit this url and follow the directions:https://accounts.google.com/o/oauth2/auth?client_id=...  Enter verification code: ...
  Refresh Token: ...
  Access Token: ...
  Access Token Expiration Seconds: 3600
$ # Of which the last three are actual token responses.
$ # Thereafter access tokens can regularly be refreshed
$ # via the created refresh token (read on)
</code></pre>
</blockquote>
<p> The generated refresh token must also be saved locally (securely). The procedure as a whole can be read at Lk <a rel="nofollow" href="https://github.com/google/gmail-oauth2-tools/wiki/OAuth2DotPyRunThrough">https://github.com/google/gmail-oauth2-tools/wiki/OAuth2DotPyRunThrough</a> . Since periodic timers are not yet supported, keeping an access token up-to-date (from within S-nail) can only be performed via the hook <i>on-main-loop-tick</i> or (for sending only) <i>on-compose-enter</i> (for more on authentication please see the section Sx On URL syntax and credential lookup ) : </p>
<blockquote><pre><code>set on-main-loop-tick=o-m-l-t on-compose-enter=o-c-e
define o-m-l-t {
  xcall update_access_token
}
define o-c-e {
  xcall update_access_token
}
set access_token_=0
define update_access_token {
  local set i epoch_sec epoch_nsec
  vput vexpr i epoch
  eval set $i # set epoch_sec/_nsec of vexpr epoch
  vput vexpr i + $access_token_ 2100
  if $epoch_sec -ge $i
    vput ! password python oauth2.py --user=EMAIL \
        --client-id=THE-ID --client-secret=THE-SECRET \
        --refresh-token=THE-REFRESH-TOKEN |\
      sed '1b PASS;d; :PASS s/^.\{1,\}:\(.\{1,\}\)$/\1/'
    vput csop password trim &quot;$password&quot;
    if -n &quot;$verbose&quot;
      echo password is &lt;$password&gt;
    endif
    set access_token_=$epoch_sec
  endif
}
</code></pre>
</blockquote>
<h3>Not "defunctional", but the editor key does not work</h3>
<p> Two thinkable situations: the first is a shadowed sequence; setting <i>debug</i> or the most possible <i>verbose</i> mode, causes a printout of the <code>bind</code> tree after that is built; being a cache, this happens only upon startup or after modifying bindings. </p>
<p> Or second, terminal libraries (see Sx On terminal control and line editor, <code>bind</code> <i>termcap</i> may report different codes than the terminal really sends, rendering bindings dysfunctional because expected and received data do not match; the <i>verbose</i> listing of <code>bind ings will show the byte sequences that are expected.</code> (One common source of problems is that the --- possibly even non-existing --- keypad is not turned on, and the resulting layout reports the keypad control codes for the normal keyboard keys.) </p>
<p> To overcome the situation use for example the program <a href="/docs/linux/man/1-cat/">cat</a>(1) with its option -<code>v</code> if available, to see the byte sequences which are actually produced by keypresses, and use the variable <i>termcap</i> to make S-nail aware of them. The terminal this is typed on produces some unexpected sequences, here for an example the shifted home key: </p>
<blockquote><pre><code>? set verbose
? bind*
# 1B 5B=[ 31=1 3B=; 32=2 48=H
  bind base :kHOM z0
? x
$ cat -v
^[[H
$ s-nail -v -Stermcap='kHOM=\E[H'
? bind*
# 1B 5B=[ 48=H
  bind base :kHOM z0
</code></pre>
</blockquote>
<h3>Can S-nail git-send-email?</h3>
<p> Yes. Put (at least parts of) the following in your ~/.gitconfig </p>
<blockquote><pre><code>[sendemail]
smtpserver = /usr/bin/s-nail
smtpserveroption = -t
#smtpserveroption = -Sexpandaddr
smtpserveroption = -Athe-account-you-need
##
suppresscc = all
suppressfrom = false
assume8bitEncoding = UTF-8
#to = /tmp/OUT
confirm = always
chainreplyto = true
multiedit = false
thread = true
quiet = true
annotate = true
</code></pre>
</blockquote>
<p> Newer <a href="/docs/linux/man/1-git/">git</a>(1) versions (v2.33.0) added the option <code>sendmailCmd</code> Patches can also be send directly, for example: </p>
<blockquote><pre><code>$ git format-patch -M --stdout HEAD^ |
  s-nail -A the-account-you-need -t RECEIVER
</code></pre>
</blockquote>
<h3>Howto handle stale dotlock files</h3>
<p> <code>folder</code> sometimes fails to open MBOX mail databases because creation of Sx dotlock files is impossible due to existing but unowned lock files. S-nail does not offer an option to deal with those files, because it is considered a site policy what counts as unowned, and what not. The site policy is usually defined by administrator(s), and expressed in the configuration of a locally installed MTA (for example Postfix `stale_lock_time=500s&#8217; ) . Therefore the suggestion: </p>
<blockquote><pre><code>$ &lt;/dev/null s-nail -s 'MTA: be no frog, handle lock' $LOGNAME
</code></pre>
</blockquote>
<p> By sending a mail to yourself the local MTA can use its normal queue mechanism to try the delivery multiple times, finally decide a lock file has become stale, and remove it.  </p>
<h2>IMAP CLIENT</h2>
<p> [Option]ally there is IMAP client support available. This part of the program is obsolete and will vanish in v15 with the large MIME and I/O layer rewrite, because it uses old-style blocking I/O and makes excessive use of signal based long code jumps. Support can hopefully be readded later based on a new-style I/O, with SysV signal handling. In fact the IMAP support had already been removed from the codebase, but was reinstantiated on user demand: in effect the IMAP code is at the level of S-nail v14.8.16 (with <code>imapcodec</code> being the sole exception), and should be treated with some care. </p>
<p> IMAP uses the `<a href="imap://'">imap://&#8216;</a> and `<a href="imaps://'">imaps://&#8216;</a> protocol prefixes, and an IMAP-based <i>folder</i> may be used. IMAP URLs (paths) undergo inspections and possible transformations before use (and the command <code>imapcodec</code> can be used to manually apply them to any given argument). Hierarchy delimiters are normalized, a step which is configurable via the <i>imap-delim</i> variable chain, but defaults to the first seen delimiter otherwise. S-nail supports internationalised IMAP names, and en- and decodes the names from and to the <i>ttycharset</i> as necessary and possible. If a mailbox name is expanded (see Sx Filename transformations ) to an IMAP mailbox, all names that begin with `+&#8216; then refer to IMAP mailboxes below the <i>folder</i> target box, while folder names prefixed by `@&#8216; refer to folders below the hierarchy base, so the following will list all folders below the current one when in an IMAP mailbox: `folders&#8217; @ . </p>
<p> Note: some IMAP servers do not accept the creation of mailboxes in the hierarchy base, but require that they are created as subfolders of `INBOX&#8217; - with such servers a folder name of the form </p>
<blockquote><p> <code><a href="imaps://mylogin@imap.myisp.example/INBOX.">imaps://mylogin@imap.myisp.example/INBOX.</a></code> </p>
</blockquote>
<p> should be used (the last character is the server&#8217;s hierarchy delimiter). The following IMAP-specific commands exist: </p>
<dl>
<dt><code>cache</code></dt>
<dd> <p> Only applicable to cached IMAP mailboxes; takes a message list and reads the specified messages into the IMAP cache. </p>
 </dd>
<dt><code>connect</code></dt>
<dd> <p> If operating in disconnected mode on an IMAP mailbox, switch to online mode and connect to the mail server while retaining the mailbox status. See the description of the <i>disconnected</i> variable for more information. </p>
 </dd>
<dt><code>disconnect</code></dt>
<dd> <p> If operating in online mode on an IMAP mailbox, switch to disconnected mode while retaining the mailbox status. See the description of the <i>disconnected</i> variable for more. A list of messages may optionally be given as argument; the respective messages are then read into the cache before the connection is closed, thus `disco&#8217; * makes the entire mailbox available for disconnected use. </p>
 </dd>
<dt><code>imap</code></dt>
<dd> <p> Sends command strings directly to the current IMAP server. S-nail operates always in IMAP `selected state&#8217; on the current mailbox; commands that change this will produce undesirable results and should be avoided. Useful IMAP commands are: </p>
 </dd>
<dl>
<dt><code>create</code></dt>
<dd> <p> Takes the name of an IMAP mailbox as an argument and creates it. </p>
 </dd>
<dt><code>getquotaroot</code></dt>
<dd> <p> (RFC 2087) Takes the name of an IMAP mailbox as an argument and prints the quotas that apply to the mailbox. Not all IMAP servers support this command. </p>
 </dd>
<dt><code>namespace</code></dt>
<dd> <p> (RFC 2342) Takes no arguments and prints the Personal Namespaces, the Other User&#8217;s Namespaces and the Shared Namespaces. Each namespace type is printed in parentheses; if there are multiple namespaces of the same type, inner parentheses separate them. For each namespace a prefix and a hierarchy separator is listed. Not all IMAP servers support this command. </p>
 </dd></dl>
<dt><code>imapcodec</code></dt>
<dd> <p> Perform IMAP path transformations. Supports <code>vput</code> (see Sx Command modifiers ) , and manages the error number <i>!</i> The first argument specifies the operation: <i>e[ncode]</i> normalizes hierarchy delimiters (see <i>imap-delim</i> and converts the strings from the locale <i>ttycharset</i> to the internationalized variant used by IMAP, <i>d[ecode]</i> performs the reverse operation. Encoding will honour the (global) value of <i>imap-delim</i> </p>
 </dd></dl>
<p> The following IMAP-specific internal variables exist: </p>
<dl>
<dt><i>disconnected</i></dt>
<dd> <p> (Boolean) When an IMAP mailbox is selected and this variable is set, no connection to the server is initiated. Instead, data is obtained from the local cache (see <i>imap-cache </i><code>).</code> Mailboxes that are not present in the cache and messages that have not yet entirely been fetched from the server are not available; to fetch all messages in a mailbox at once, the command <code>` copy * /dev/null </code> can be used while still in connected mode. Changes that are made to IMAP mailboxes in disconnected mode are queued and committed later when a connection to that server is made. This procedure is not completely reliable since it cannot be guaranteed that the IMAP unique identifiers (UIDs) on the server still match the ones in the cache at that time. Data is saved to <code>DEAD</code> when this problem occurs. </p>
 </dd>
<dt><i>disconnected-USER [at] HOST</i></dt>
<dd> <p> The specified account is handled as described for the <i>disconnected</i> variable above, but other accounts are not affected. </p>
 </dd>
<dt><i>imap-auth-USER [at] HOST , imap-auth</i></dt>
<dd> <p> Sets the IMAP authentication method. Supported are the default `login&#8217; , [v15-compat] `oauthbearer&#8217; (see Sx FAQ entry Sx But, how about XOAUTH2 / OAUTHBEARER? ) , [v15-compat] `external&#8217; and `externanon&#8217; (for TLS secured connections which pass a client certificate via <i>tls-config-pairs )</i> as well as the [Option]al `cram-md5&#8217; and `gssapi&#8217; All methods need a <i>user</i> and a <i>password</i> except `gssapi&#8217; and `external&#8217; , which only need the former. `externanon&#8217; solely builds upon the credentials passed via a client certificate, and is usually the way to go since tested servers do not actually follow RFC 4422, and fail if additional credentials are actually passed. </p>
 </dd>
<dt><i>imap-cache</i></dt>
<dd> <p> Enables caching of IMAP mailboxes. The value of this variable must point to a directory that is either existent or can be created by S-nail. All contents of the cache can be deleted by S-nail at any time; it is not safe to make assumptions about them. </p>
 </dd>
<dt><i>imap-delim-USER [at] HOST , imap-delim-HOST , imap-delim</i></dt>
<dd> <p> The hierarchy separator used by the IMAP server. Whenever an IMAP path is specified it will undergo normalization. One of the normalization steps is the squeezing and adjustment of hierarchy separators. If this variable is set, any occurrence of any character of the given value that exists in the path will be replaced by the first member of the value; an empty value will cause the default to be used, it is `/.&#8216; If not set, we will reuse the first hierarchy separator character that is discovered in a user-given mailbox name. </p>
 </dd>
<dt><i>imap-keepalive-USER [at] HOST , imap-keepalive-HOST , imap-keepalive</i></dt>
<dd> <p> IMAP servers may close the connection after a period of inactivity; the standard requires this to be at least 30 minutes, but practical experience may vary. Setting this variable to a numeric `value&#8217; greater than 0 causes a `NOOP&#8217; command to be sent each `value&#8217; seconds if no other operation is performed. </p>
 </dd>
<dt><i>imap-list-depth</i></dt>
<dd> <p> When retrieving the list of folders on an IMAP server, the <code>folders</code> command stops after it has reached a certain depth to avoid possible infinite loops. The value of this variable sets the maximum depth allowed. The default is 2. If the folder separator on the current IMAP server is a slash `/&#8216;, this variable has no effect and the <code>folders</code> command does not descend to subfolders. </p>
 </dd>
<dt><i>imap-use-starttls-USER [at] HOST , imap-use-starttls-HOST , imap-use-starttls</i></dt>
<dd> <p> Causes S-nail to issue a `STARTTLS&#8217; command to make an unencrypted IMAP session TLS encrypted. This functionality is not supported by all servers, and is not used if the session is already encrypted by the IMAPS method. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bogofilter/">bogofilter</a>(1), <a href="/docs/linux/man/1-gpg/">gpg</a>(1), <a href="/docs/linux/man/1-more/">more</a>(1), <a href="/docs/linux/man/1-newaliases/">newaliases</a>(1), openssl(1), <a href="/docs/linux/man/1-sendmail/">sendmail</a>(1), <a href="/docs/linux/man/1-sh/">sh</a>(1), <a href="/docs/linux/man/1-spamassassin/">spamassassin</a>(1), <a href="/docs/linux/man/3-iconv/">iconv</a>(3), <a href="/docs/linux/man/3-setlocale/">setlocale</a>(3), <a href="/docs/linux/man/5-aliases/">aliases</a>(5), <a href="/docs/linux/man/5-termcap/">termcap</a>(5), <a href="/docs/linux/man/5-terminfo/">terminfo</a>(5), <a href="/docs/linux/man/7-locale/">locale</a>(7), <a href="/docs/linux/man/7-mailaddr/">mailaddr</a>(7), re_format7 (or&nbsp; <a href="/docs/linux/man/7-regex/">regex</a>(7)) mailwrapper(8), sendmail(8)  </p>
<h2>HISTORY</h2>
<p> M. Douglas McIlroy writes in his article ``A Research UNIX Reader: Annotated Excerpts&#8217;&#8216; from the Programmer&#8217;s Manual, 1971-1986 that a <a href="/docs/linux/man/1-mail/">mail</a>(1) command already appeared in First Edition UNIX in 1971: </p>
<blockquote><p> Electronic mail was there from the start. Never satisfied with its exact behavior, everybody touched it at one time or another: to assure the safety of simultaneous access, to improve privacy, to survive crashes, to exploit uucp, to screen out foreign freeloaders, or whatever. Not until v7 did the interface change (Thompson). Later, as mail became global in its reach, Dave Presotto took charge and brought order to communications with a grab-bag of external networks (v8). </p>
</blockquote>
<p> BSD Mail, in large parts compatible with UNIX mail, was written in 1978 by Kurt Shoens and developed as part of the BSD UNIX distribution until 1995. This manual page is derived from ``The Mail Reference Manual&#8217;&#8216; that Kurt Shoens wrote for Mail 1.3, included in 3BSD in 1980. The common UNIX and BSD denominator became standardized as <a href="/docs/linux/man/1-mailx/">mailx</a>(1) in the X/Open Portability Guide Issue 2 (January 1987). After the rise of Open Source BSD variants Mail saw continuous development in the individual code forks, noticeably by Christos Zoulas in Net BSD Based upon this Nail, later Heirloom Mailx, was developed by Gunnar Ritter in the years 2000 until 2008. Since 2012 S-nail is maintained by Steffen Nurpmeso. </p>
<p> Electronic mail exchange in general is a concept even older. The earliest well documented electronic mail system was part of the Compatible Time Sharing System (CTSS) at MIT, its MAIL command had been proposed in a staff planning memo at the end of 1964 and was implemented in mid-1965 when Tom Van Vleck and Noel Morris wrote the necessary code. Similar communication programs were built for other timesharing systems. One of the most ambitious and influential was Murray Turoff&#8217;s EMISARI. Created in 1971 for the United States Office of Emergency Preparedness, EMISARI combined private electronic messages with a chat system, public postings, voting, and a user directory. </p>
<p> During the 1960s it was common to connect a large number of terminals to a single, central computer. Connecting two computers together was relatively unusual. This began to change with the development of the ARPANET, the ancestor of today&#8217;s Internet. In 1971 Ray Tomlinson adapted the SNDMSG program, originally developed for the University of California at Berkeley timesharing system, to give it the ability to transmit a message across the network into the mailbox of a user on a different computer. For the first time it was necessary to specify the recipient&#8217;s computer as well as an account name. Tomlinson decided that the underused commercial at `@&#8216; would work to separate the two. </p>
<p> Sending a message across the network was originally treated as a special instance of transmitting a file, and so a MAIL command was included in RFC 385 on file transfer in 1972. Because it was not always clear when or where a message had come from, RFC 561 in 1973 aimed to formalize electronic mail headers, including ``from&#8217;&#8216; ``date&#8217;&#8216; and ``subject&#8217;&#8216; In 1975 RFC 680 described fields to help with the transmission of messages to multiple users, including ``to&#8217;&#8216; ``cc&#8217;&#8216; and ``bcc&#8217;&#8216; In 1977 these features and others went from best practices to a binding standard in RFC 733. Queen Elizabeth II of England became the first head of state to send electronic mail on March 26 1976 while ceremonially opening a building in the British Royal Signals and Radar Establishment (RSRE) in Malvern.  </p>
<h2>AUTHORS</h2>
<p> An -nosplit An Kurt Shoens , An Edward Wang , An Keith Bostic , An Christos Zoulas , An Gunnar Ritter . S-nail is developed by An Steffen Nurpmeso Aq s-mailx [at] lists.sdaoden.eu .  </p>
<h2>CAVEATS</h2>
<p> [v15 behaviour may differ] Interrupting an operation via <code>SIGINT</code> aka `control-C&#8217; from anywhere else but a command prompt is very problematic and likely to leave the program in an undefined state: many library functions cannot deal with the Fn siglongjmp 3 that this software (still) performs; even though efforts have been taken to address this, no sooner but in v15 it will have been worked out: interruptions have not been disabled in order to allow forceful breakage of hanging network connections, for example (all this is unrelated to <i>ignore )</i> </p>
<p> The SMTP and POP3 protocol support of S-nail is very basic. Also, if it fails to contact its upstream SMTP server, it will not make further attempts to transfer the message at a later time (setting <i>save</i> and <i>sendwait</i> may be useful). If this is a concern, it might be better to set up a local SMTP server that is capable of message queuing.  </p>
<h2>BUGS</h2>
<p> When a network-based mailbox is open, directly changing to another network-based mailbox of a different protocol (i.e., from POP3 to IMAP or vice versa) will cause a ``deadlock&#8217;&#8216; </p>
<p> After deleting some message of a POP3 mailbox the header summary falsely claims that there are no messages to display, one needs to perform a scroll or dot movement to restore proper state. </p>
<p> In `thread&#8217; Ns ed <code>sort</code> mode a power user may encounter crashes very occasionally (this is may and very). </p>
<p> Please report bugs to the <i>contact-mail</i> address, for example from within s-nail: `?&#8216; Ns Ic eval Ns Ic mail Ns $contact-mail . Including the <i>verbose</i> output of the command <code>version</code> may be helpful: </p>
<blockquote><pre><code>? wysh set escape=! verbose; vput version xy; unset verbose;\
  eval mail $contact-mail
Bug subject
!I xy
!.
</code></pre>
</blockquote>
<p> Information on the web at `$&#8216; s-nail -X &#8216;echo Ns $ Ns Va contact-web Ns ; x&#8217; . </p>
