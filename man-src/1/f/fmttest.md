---
title: "fmttest(1)"
name: "fmttest"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fmttest/"
---

<h2>FMTTEST</h2>
<p> fmttest &#8211; test tool for the <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) language</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fmttest</code> [<code>-form</code> <i>formatfile</i>] [<code>-format</code> <i>formatstring</i>] [<code>-address</code> | <code>-raw</code> | <code>-date</code> | <code>-message</code>] [<code>-file</code> | <code>-nofile</code>] [<code>&#8211;component</code> <i>component-text</i>] [<code>-dupaddrs</code> | <code>-nodupaddrs</code>] [<code>-ccme</code> | <code>-noccme</code>] [<code>-outsize</code> <i>size-in-characters</i>] [<code>-bufsize</code> <i>size-in-bytes</i>] [<code>-width</code> <i>column-width</i>] [<code>-msgnum</code> <i>number</i>] [<code>-msgcur</code> <i>flag</i>] [<code>-msgsize</code> <i>size</i>] [<code>-unseen</code> <i>flag</i>] [<code>-dump</code> | <code>-nodump</code>] [<code>-trace</code> | <code>-notrace</code>] [<i>+folder</i>] [<i>msgs</i> | <i>strings</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Fmttest</code></p>
<dd>is used to test programs written for the <code>nmh</code> format language as specified by <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5). It is also intended to replace the <code>ap</code>, <code>dp</code>, and <code>fmtdump</code> programs. </p>
<h3>FORMAT PROGRAM SELECTION</h3>
<p> The <code>-format</code> <i>string</i> and <code>-form</code> <i>formatfile</i> switches may be used to specify a format string or a format file to read. If given a format string, it must be specified as a single argument to the <code>-format</code> switch. If given a format file name with <code>-form</code>, the file is searched for using the normal <code>nmh</code> rules: absolute pathnames are accessed directly, tilde expansion is done on usernames, and files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked.</p>
<h3>MODE SELECTION AND COMPONENT SPECIFICATION</h3>
<p> <code>Fmttest</code> has four operating modes: address mode, raw mode, date mode, and message mode. These modes are selected by the <code>-address</code>, <code>-raw</code>, <code>-date</code>, and <code>-message</code> switches respectively. </p>
<p> Address mode treats every argument as an email address and processes it with nmh&#8217;s email parser. Each argument is processed with the specified format program with the parsed email address available as a special %{<i>text</i>} component escape, and the output from the program is printed on standard output. If there was an error parsing the email address the error message is stored in the %{<i>error</i>} component escape. If no format program is given on the command line, the following default program is used: </p>
<dl>
<dt>
<dd>
<pre><code>
% &lt;{error} % {error} : % {text} % | % (putstr(proper{text})) %&gt;
</code></pre>
</dl>
<p> In this mode <code>fmttest</code> is equivalent to <i><a href="/docs/linux/man/8-ap/">ap</a></i>(8). </p>
<p> In raw mode, no processing of the specified arguments is done. Each argument is run against the specified format program with the argument text available in the %{<i>text</i>} component. You must specify a format with <code>-form</code> or <code>-format</code> when using raw mode. </p>
<p> Date mode is identical to raw mode, with one exception: if no format is specified, the following format string is used: </p>
<dl>
<dt>
<dd>
% &lt;(nodate{text})error : % {text} % | % (putstr(pretty{text})) %&gt;
</dl>
<p> Date mode is equivalent to <i><a href="/docs/linux/man/8-dp/">dp</a></i>(8). </p>
<p> In message mode the arguments to <code>fmttest</code> are interpreted as an optional folder and messages. <code>Fmttest</code> will read each specified message and make all of the components in the message available to the format program. Also, the appropriate information for the %(<i>msg</i>), %(<i>cur</i>), %(<i>unseen</i>), and %(<i>size</i>) function escapes will be made available for each message. If the <code>-file</code> switch is given, the arguments are interpreted as filenames instead of message numbers, but otherwise the behavior is the same (except that the %(<i>msg</i>), %(<i>cur</i>), and %(<i>unseen</i>) function escapes will not provide any useful information). </p>
<p> The default format used in address mode is the default format used by <code>scan</code>. The following command can replicate the functionality of the <code>repl</code> command. </p>
<dl>
<dt>
<dd>
<pre>
fmttest -nodupaddrs -form replcomps -outsize max [+folder] message
</pre>
</dl>
<p> Regardless of the mode, other components can be provided to the format program by the use of the <code>&#8211;component</code> switch. For example, the following program will test out the use of the &#8220;<code>encrypted</code>&#8221; component: </p>
<dl>
<dt>
<dd>
<pre>
fmttest --encrypted yes -message cur
</pre>
</dl>
<p> In message mode components supplied on the command line will override components from messages.</p>
<h3>ADDITIONAL SWITCHES</h3>
<p> The <code>-dupaddrs</code> and <code>-nodupaddrs</code> switches control whether duplicate addresses are allowed or suppressed by the <code>FORMATADDR</code> instruction, which is used by the `%(<i>formataddr</i>)&#8217; function escape. In normal operation duplicate addresses are only suppressed by <code>repl</code>. </p>
<p> The <code>-ccme</code> and <code>-noccme</code> switches control whether or not to count the user&#8217;s local mailbox as a duplicate address. This replicates the behavior of the <code>-cc</code> <i>me</i> switch to <code>repl</code>, and only applies if <code>-nodupaddrs</code> is in effect. </p>
<p> The <code>-outsize</code> switch controls the maximum number of printable characters that the format engine will produce. Characters marked as non-printing by the format engine with `%(<i>zputlit</i>)&#8217;, characters with zero width, and extra bytes that are part of a multibyte character are not counted against this total. Two special values are supported: &#8220;<i>max</i>&#8221;, which will set the value to the size of the output buffer, and &#8220;<i>width</i>&#8221;, which will set the value to the width of the terminal. In message mode it defaults to the terminal width, otherwise the default is the output buffer size. </p>
<p> The <code>-bufsize</code> switch controls the size of the output buffer. By default it is set to the size of the <code>BUFSIZ</code> C preprocessor symbol, which is system-dependent. </p>
<p> The <code>-width</code> switch controls the column width which is used by the `%(<i>width</i>)&#8217; function escape. By default is set to the terminal width. </p>
<p> The <code>-msgnum</code>, <code>-msgcur</code>, <code>-msgsize</code>, and the <code>-unseen</code> switches all control the values used, respectively, by the following function escapes: `%(<i>num</i>)&#8217;, `%(<i>cur</i>)&#8217;, `%(<i>size</i>)&#8217;, and `%(<i>unseen</i>)&#8217;. If none are supplied these values are taken from the message in message mode; in all other modes the default values are 0.</p>
<h3>COMPILING AND TRACING FORMAT PROGRAMS</h3>
<p> The <code>-dump</code> switch outputs the complete set of format instructions for the specified format program. The <code>-trace</code> switch will output each format instruction as it is being executed, and show the values of the <i>num</i> and <i>str</i> registers if they have changed from the previous instruction. The output buffer is also printed if it has changed from the previous instruction.</p>
<h3>FORMAT INSTRUCTIONS</h3>
<p> It should be noted that there is not a one-to-one correspondence between format escapes and format instructions; many instructions have side effects. Instructions prefixed with &#8220;<i>LV</i>&#8221; generally return a integer into the <i>num</i> (value) register; instructions prefixed with a &#8220;<i>LS</i>&#8221; return a string into the <i>str</i> register. </p>
<p>Instruction  Description<br />
COMP          Output component<br />
COMPF         Formatted output component<br />
LIT           Output literal text<br />
LITF          Formatted literal text output<br />
CHAR          Output single character<br />
NUM           Output the num register<br />
NUMF          Formatted output of the num register<br />
STR           Output the str register<br />
STRF          Formatted output of the str register<br />
STRFW         Not used<br />
PUTADDR       Output address list in str register<br />
STRLIT        Output str, no space compression<br />
STRLITZ       Like STRLIT, but not counted against width<br />
LS_COMP       Write component to str register<br />
LS_LIT        Write literal to str register<br />
LS_GETENV     Write environment var to str register<br />
LS_DECODECOMP Decode RFC 2047 encoded component to str register<br />
LS_DECODE     Decode RFC 2047 encoded string to str register<br />
LS_TRIM       Trim trailing whitespace from str register<br />
LV_COMP       Convert component to integer, store in num register<br />
LV_COMPFLAG   Set num to 1 if TRUE set in component<br />
LV_LIT        Load literal value into num register<br />
LV_DAT        Load value from dat array into num register (see note)<br />
LV_STRLEN     Set num to the length of str<br />
LV_PLUS_L     Add value to num register<br />
LV_MINUS_L    Substract value from num register<br />
LV_DIVIDE_L   Divide num register by value<br />
LV_MODULO_L   num modulo value<br />
LV_CHAR_LEFT  Store remaining number of printable chars in num<br />
LS_MONTH      Write short name of month to str from date component<br />
LS_LMONTH     Write long name of month to str from date component<br />
LS_ZONE       Write time zone offset to str from date component<br />
LS_DAY        Write short name of day of week to str from date component<br />
LS_WEEKDAY    Write long name of day of week to str from date component<br />
LS_822DATE    Write RFC 822 compatible date to str from date component<br />
LS_PRETTY     Write date with &#8220;pretty&#8221; timezone to str<br />
LV_SEC        Write date component seconds to num<br />
LV_MIN        Write date component minutes to num<br />
LV_HOUR       Write date component hour to num<br />
LV_MON        Write date component numeric month to num (start at 1)<br />
LV_YEAR       Write date component year to num<br />
LV_YDAY       Write date component Julian day to num<br />
LV_WDAY       Write date component day of week to num (0 == Sunday)<br />
LV_ZONE       Write date component time zone offset to num<br />
LV_CLOCK      Write date component in Unix epoch time to num<br />
LV_RCLOCK     Write offset of date component from current time to num<br />
LV_DAYF       Write 1 to num if day of week is explicit<br />
LV_DST        Write 1 to num if DST is in effect for date component<br />
LV_ZONEF      Write 1 to num if timezone is explicit<br />
LS_ADDR       Write email address of addr component to str<br />
LS_PERS       Write personal name of addr component to str<br />
LS_MBOX       Write mailbox (username)<br />
of addr component to str<br />
    LS_HOST Write host of addr component to str<br />
        LS_PATH Write host route of addr component to str<br />
            LS_GNAME Write group name of addr component to str<br />
                LS_NOTE Write note portion of addr component to str<br />
                    LS_822ADDR Write &#8220;proper&#8221; RFC 822 version of addr component to str<br />
                        LS_FRIENDLY Write<br />
                        friendly(name or note) of address component to str<br />
    LS_UNQUOTE Remove RFC 2822 quotes from string<br />
    LV_HOSTTYPE Set num to type of host(0 = local, 1 = network)<br />
        LV_INGRPF Set num to 1 if address was inside of group<br />
    LV_NOHOSTF Set num to 1 of no host was present in address component<br />
    LOCALDATE Convert date component to local timezone<br />
    GMTDATE Convert date component to GMT<br />
    PARSEDATE Parse date component<br />
    PARSEADDR Parse address component<br />
    FORMATADDR Add address component to list in str<br />
    CONCATADDR Like FORMATADDR,<br />
    but will not suppress duplicates<br />
    MYMBOX Set num if address component is a local address<br />
    SAVESTR Save str register temporarily<br />
    DONE End program<br />
    NOP No operation<br />
    GOTO Jump to new instruction<br />
    IF_S_NULL Branch if str is NULL<br />
    IF_S Branch if str is not NULL<br />
    IF_V_EQ Branch if num is equal to value<br />
    IF_V_NE Branch if num is not equal to value<br />
    IF_V_GT Branch if num is greater than value<br />
    IF_MATCH Branch if str contains string<br />
    IF_AMATCH Branch if str starts with string<br />
    S_NULL Set num to 1 if str is NULL<br />
    S_NONNULL Set num to 1 if str is not NULL<br />
    V_EQ Set num to 1 if num equals value<br />
    V_NE Set num to 1 if num does not equal value<br />
    V_GT Set num to 1 if num is greater than value<br />
    V_MATCH Set num to 1 if str contains string<br />
    V_AMATCH Set num to 1 if str starts with string</p>
<p> The <code>LV_DAT</code> instruction is a bit special. Callers of the format library pass in an array of integers that are used by certain format escapes. The current list of format escapes and the indexes they use are: </p>
<dl>
<dt>
<dd>
<pre><code>
dat[0] % (num)dat[1] % (cur)dat[2] % (size)dat[3] % (width)dat[4] % (unseen)
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1), <i><a href="/docs/linux/man/8-ap/">ap</a></i>(8), <i><a href="/docs/linux/man/8-dp/">dp</a></i>(8),</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-message</code>'
`<code>-nofile</code>'
`<code>-dupaddrs</code>'
</pre>
<h2>BUGS</h2>
<p> It shouldn&#8217;t require as much code from other programs as it does. </p>
<h2>Index</h2>
