---
title: "mh-format(5)"
name: "mh-format"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mh-format/"
description: "mh-format – format file for nmh message system"
---

<p>mh-format &#8211; format file for nmh message system</p>
<h2>Description</h2>
<p>Several <code>nmh</code> commands utilize either a <i>format</i> string or a <i>format</i> file during their execution. For example, <code>scan</code> uses a format string which directs it how to generate the scan listing for each message; <code>repl</code> uses a format file which directs it how to generate the reply to a message, and so on. </p>
<p> There are a few alternate scan listing formats available in <i>nmh/etc/scan.time</i>, <i>nmh/etc/scan.size</i>, and <i>nmh/etc/scan.timely</i>. Look in <i>nmh/etc</i> for other <code>scan</code> and <code>repl</code> format files which may have been written at your site. </p>
<p> It suffices to have your local <code>nmh</code> expert actually write new format commands or modify existing ones. This manual section explains how to do that. Note: familiarity with the C <code>printf</code> routine is assumed. </p>
<p> A format string consists of ordinary text, and special multi-character escape sequences which begin with `%&#8217;. When specifying a format string, the usual C backslash characters are honored: `&#8217;, `&#8217;, `
&#8217;, `&#8217;, and `	&#8217;. Continuation lines in format files end with `\&#8217; followed by the newline character. A literal `%&#8217; can be inserted into a format file by using the sequence `%%&#8217;.</p>
<h3>Syntax</h3>
<p>Format strings are built around <i>escape sequences</i>. There are three types of escape sequences: header <i>components</i>, built-in <i>functions</i>, and flow <i>control</i>. Comments may be inserted in most places where a function argument is not expected. A comment begins with `%;&#8217; and ends with a (non-escaped) newline. </p>
<p> A <i>component</i> escape is specified as `%{<i>component</i>}&#8217;, and exists for each header found in the message being processed. For example `%{<i>date</i>}&#8217; refers to the &#8220;Date:&#8221; field of the appropriate message. All component escapes have a string value. Normally, component values are compressed by converting any control characters (tab and newline included) to spaces, then eliding any leading or multiple spaces. However, commands may give different interpretations to some component escapes; be sure to refer to each command&#8217;s manual entry for complete details. Some commands (such as <code>ap</code> and <code>mhl</code>) use a special component `%{<i>text</i>}&#8217; to refer to the text being processed; see their respective man pages for details and examples. </p>
<p> A <i>function</i> escape is specified as `%(<i>function</i>)&#8217;. All functions are built-in, and most have a string or numeric value. A function escape may have an <i>argument</i>. The argument follows the function escape: separating whitespace is discarded: `%(<i>function</i> <i>argument</i>)&#8217;. </p>
<p> In addition to literal numbers or strings, the argument to a function escape can be another function, a component, or a control escape. When the argument is a function or a component, they are listed without a leading `%&#8217;. When control escapes are used as function arguments, they written as normally, with a leading `%&#8217;;</p>
<h3>Control escapes</h3>
<p>A <i>control</i> escape is one of: `%&lt;&#8216;, `%?&#8217;, `%|&#8217;, or `%&gt;&#8217;. These are combined into the conditional execution construct: </p>
<dl>
<dd>
<pre>%&lt; <i>condition</i> <i>format-text</i>
%? <i>condition</i> <i>format-text</i>
 ...
%| <i>format-text</i>
%&gt;</pre>
</dl>
<p> Extra white space is shown here only for clarity. These constructs may be nested without ambiguity. They form a general <code>if-elseif-else-endif</code> block where only one of the format-texts is interpreted. In other words, `%&lt;&#8216; is like the &quot;if&quot;, `%?&#8217; is like the &quot;elseif&quot;, `%|&#8217; is like &quot;else&quot;, and `%&gt;&#8217; is like &quot;endif&quot;. </p>
<p> A `%&lt;&#8216; or `%?&#8217; control escape causes its condition to be evaluated. This condition is a <i>component</i> or <i>function</i>. For integer valued functions or components, the condition is true if the function return or component value is non-zero, and false if zero. For string valued functions or components, the condition is true if the function return or component value is a non-empty string, and false for an empty string. </p>
<p> The `%?&#8217; control escape is optional, and may there may be more than one `%?&#8217; control escape in a conditional block. The `%|&#8217; control escape is also optional, but may be included at most once.</p>
<h3>Function escapes</h3>
<p>Functions expecting an argument generally require an argument of a particular type. In addition to the number and string types, these include: </p>
<dl>
<dd>
<pre><i>Argument DescriptionExample Syntax</i>
literal A literal number %(<i>func</i> 1234)
 or string %(<i>func</i> text string)
comp Any component %(<i>func</i>{<i>in-reply-to</i>})
date A date component %(<i>func</i>{<i>date</i>})
addr An address component %(<i>func</i>{<i>from</i>})
expr Nothing %(<i>func</i>)
 or a subexpression %(<i>func</i>(<i>func2</i>))
 or control escape %(<i>func</i> %&lt;{<i>reply-to</i>}%|%{<i>from</i>}%&gt;)</pre>
</dl>
<p> The types <i>date</i> and <i>addr</i> have the same syntax as <i>comp</i>, but require that the header component be a date string, or address string, respectively. </p>
<p> Most arguments not of type <i>expr</i> are required. When escapes are nested (via expr arguments), evaluation is done from inner-most to outer-most. As noted above, for the expr argument type, functions and components are written without a leading `%&#8217;. Control escape arguments must use a leading `%&#8217;, preceded by a space. </p>
<p> For example, </p>
<dl>
<dd>
<pre>%&lt;(mymbox{from}) To: %{to}%&gt;</pre>
</dl>
<p> writes the value of the header component &#8220;From:&#8221; to the internal register named str; then (<i>mymbox</i>) reads str and writes its result to the internal register named <i>num</i>; then the control escape evaluates <i>num</i>. If <i>num</i> is non-zero, the string &#8220;To:&#8221; is printed followed by the value of the header component &#8220;To:&#8221;.</p>
<h3>Evaluation</h3>
<p>The evaluation of format strings is performed by a small virtual machine. The machine is capable of evaluating nested expressions as described above, and in addition has an integer register <i>num</i>, and a text string register <i>str</i>. When a function escape that accepts an optional argument is processed, and the argument is not present, the current value of either <i>num</i> or <i>str</i> is used as the argument: which register is used depends on the function, as listed below. </p>
<p> Component escapes write the value of their message header in <i>str</i>. Function escapes write their return value in <i>num</i> for functions returning integer or boolean values, and in <i>str</i> for functions returning string values. (The boolean type is a subset of integers with usual values 0=false and 1=true.) Control escapes return a boolean value, setting <i>num</i> to 1 if the last explicit condition evaluated by a `%&lt;&#8216; or `%?&#8217; control succeeded, and 0 otherwise. </p>
<p> All component escapes, and those function escapes which return an integer or string value, evaluate to their value as well as setting <i>str</i> or <i>num</i>. Outermost escape expressions in these forms will print their value, but outermost escapes which return a boolean value do not result in printed output.</p>
<h3>Functions</h3>
<p>The function escapes may be roughly grouped into a few categories. </p>
<dl>
<dd>
<pre><i>Function Argument Result Description</i>
msg integer message number
cur integer message is current (0 or 1)
unseen integer message is unseen (0 or 1)
size integer size of message
strlen integer length of <i>str</i>
width integer column width of terminal
charleft integer bytes left in output buffer
timenow integer seconds since the UNIX epoch
me string the user's mailbox (username)
myhost string the user's local hostname
myname string the user's name
localmbox string the complete local mailbox
eq literal boolean <i>num</i> == <i>arg</i>
ne literal boolean <i>num</i> != <i>arg</i>
gt literal boolean <i>num</i> &gt; <i>arg</i>
match literal boolean <i>str</i> contains <i>arg</i>
amatch literal boolean <i>str</i> starts with <i>arg</i>
plus literal integer <i>arg</i> plus <i>num</i>
minus literal integer <i>arg</i> minus <i>num</i>
divide literal integer <i>num</i> divided by <i>arg</i>
modulo literal integer <i>num</i> modulo <i>arg</i>
num literal integer Set <i>num</i> to <i>arg</i>.
num integer Set <i>num</i> to zero.
lit literal string Set <i>str</i> to <i>arg</i>.
lit string Clear <i>str</i>.
getenv literal string Set <i>str</i> to environment value of <i>arg</i>
profile literal string Set <i>str</i> to profile component <i>arg</i> 
 value
nonzero expr boolean <i>num</i> is non-zero
zero expr boolean <i>num</i> is zero
null expr boolean <i>str</i> is empty
nonnull expr boolean <i>str</i> is non-empty
void expr Set <i>str</i> or <i>num</i>
comp comp string Set <i>str</i> to component text
compval comp integer Set <i>num</i> to ``<code>atoi</code>(<i>comp</i>)''
decode expr string decode <i>str</i> as RFC 2047 (MIME-encoded) 
 component
unquote expr string remove RFC 2822 quotes from <i>str</i>
trim expr trim trailing whitespace from <i>str</i>
putstr expr print <i>str</i>
putstrf expr print <i>str</i> in a fixed width
putnum expr print <i>num</i>
putnumf expr print <i>num</i> in a fixed width
putlit expr print <i>str</i> without space compression
zputlit expr print <i>str</i> without space compression;
 <i>str</i> must occupy no width on display
bold string set terminal bold mode
underline string set terminal underlined mode
standout string set terminal standout mode
resetterm string reset all terminal attributes
hascolor boolean terminal supports color
fgcolor literal string set terminal foreground color
bgcolor literal string set terminal background color
formataddr expr append <i>arg</i> to <i>str</i> as a
 (comma separated) address list
concataddr expr append <i>arg</i> to <i>str</i> as a
 (comma separated) address list,
 including duplicates,
 see Special Handling
putaddr literal print <i>str</i> address list with
 <i>arg</i> as optional label;
 get line width from <i>num</i></pre>
</dl>
<p> The (<i>me</i>) function returns the username of the current user. The (<i>myhost</i>) function returns the <code>localname</code> entry in <i>mts.conf</i>, or the local hostname if <code>localname</code> is not configured. The (<i>myname</i>) function will return the value of the <code>SIGNATURE</code> environment variable if set, otherwise will return the passwd GECOS field (truncated at the first comma if it contains one) for the current user. The (<i>localmbox</i>) function will return the complete form of the local mailbox, suitable for use in a &#8220;From&#8221; header. It will return the &#8220;<i>Local-Mailbox</i>&#8221; profile entry if it is set; if it is not, it will be equivalent to: </p>
<dl>
<dd>
<pre>%(myname) &lt;%(me)@%(myhost)&gt;</pre>
</dl>
<p> The following functions require a date component as an argument: </p>
<dl>
<dd>
<pre><i>Function Argument Return Description</i>
sec date integer seconds of the minute
min date integer minutes of the hour
hour date integer hours of the day (0-23)
wday date integer day of the week (Sun=0)
day date string day of the week (abbrev.)
weekday date string day of the week
sday date integer day of the week known?
 (1=explicit,0=implicit,-1=unknown)
mday date integer day of the month
yday date integer day of the year
mon date integer month of the year
month date string month of the year (abbrev.)
lmonth date string month of the year
year date integer year (may be &gt; 100)
zone date integer timezone in hours
tzone date string timezone string
szone date integer timezone explicit?
 (1=explicit,0=implicit,-1=unknown)
date2local date coerce date to local timezone
date2gmt date coerce date to GMT
dst date integer daylight savings in effect? (0 or 1)
clock date integer seconds since the UNIX epoch
rclock date integer seconds prior to current time
tws date string official RFC 822 rendering
pretty date string user-friendly rendering
nodate date integer returns 1 if date is invalid</pre>
</dl>
<p> These functions require an address component as an argument. The return value of functions noted with `*&#8217; is computed from the first address present in the header component. </p>
<dl>
<dd>
<pre><i>Function Argument Return Description</i>
proper addr string official RFC 822 rendering
friendly addr string user-friendly rendering
addr addr string mbox [at] host or host!mbox rendering*
pers addr string the personal name*
note addr string commentary text*
mbox addr string the local mailbox*
mymbox addr integer List has the user's address? (0 or 1)
host addr string the host domain*
nohost addr integer no host was present (0 or 1)*
type addr integer host type* (0=local,1=network,
 -1=uucp,2=unknown)
path addr string any leading host route*
ingrp addr integer address was inside a group (0 or 1)*
gname addr string name of group*</pre>
</dl>
<p> (A clarification on (<i>mymbox</i>{<i>comp</i>}) is in order. This function checks each of the addresses in the header component &#8220;<i>comp</i>&#8221; against the user&#8217;s mailbox name and any &#8220;<i>Alternate-Mailboxes</i>&#8221;. It returns true if any address matches, however, it also returns true if the &#8220;<i>comp</i>&#8221; header is not present in the message. If needed, the (<i>null</i>) function can be used to explicitly test for this case.)</p>
<h3>Formatting</h3>
<p>When a function or component escape is interpreted and the result will be immediately printed, an optional field width can be specified to print the field in exactly a given number of characters. For example, a numeric escape like %4(<i>size</i>) will print at most 4 digits of the message size; overflow will be indicated by a `?&#8217; in the first position (like `?234&#8242;). A string escape like %4(<i>me</i>) will print the first 4 characters and truncate at the end. Short fields are padded at the right with the fill character (normally, a blank). If the field width argument begins with a leading zero, then the fill character is set to a zero. </p>
<p> The functions (<i>putnumf</i>) and (<i>putstrf</i>) print their result in exactly the number of characters specified by their leading field width argument. For example, %06(<i>putnumf</i>(<i>size</i>)) will print the message size in a field six characters wide filled with leading zeros; %14(<i>putstrf</i>{<i>from</i>}) will print the &#8220;From:&#8221; header component in fourteen characters with trailing spaces added as needed. For <i>putstrf</i>, using a negative value for the field width causes right-justification of the string within the field, with padding on the left up to the field width. The functions (<i>putnum</i>) and (<i>putstr</i>) are somewhat special: they print their result in the minimum number of characters required, and ignore any leading field width argument. The (<i>putlit</i>) function outputs the exact contents of the str register without any changes such as duplicate space removal or control character conversion. The (<i>zputlit</i>) function similarly outputs the exact contents of the str register, but requires that those contents not occupy any output width. It can therefore be used for outputting terminal escape sequences. </p>
<p> There are a limited number of function escapes to output terminal escape sequences. These sequences are retrieved from the <i><a href="/docs/linux/man/5-terminfo/">terminfo</a></i>(5) database according to the current terminal setting. The (<i>bold</i>), (<i>underline</i>), and (<i>standout</i>) escapes set bold mode, underline mode, and standout mode respectively. </p>
<p> (<i>hascolor</i>) can be used to determine if the current terminal supports color. (<i>fgcolor</i>) and (<i>bgcolor</i>) set the foreground and background colors respectively. Both of these escapes take one literal argument, the color name, which can be one of: black, red, green, yellow, blue, magenta, cyan, white. (<i>resetterm</i>) resets all terminal attributes back to their default setting. </p>
<p> All of these terminal escape should be used in conjunction with (<i>zputlit</i>) (preferred) or (<i>putlit</i>), as the normal (<i>putstr</i>) function will strip out control characters. </p>
<p> The available output width is kept in an internal register; any output past this width will be truncated. The one exception to this is (<i>zputlit</i>) functions will still be executed in case a terminal reset code is being placed at the end of the line.</p>
<h3>Special Handling</h3>
<p>A few functions have different behavior depending on what command they are being invoked from. </p>
<p> In <code>repl</code> the (<i>formataddr</i>) function stores all email addresses encountered into an internal cache and will use this cache to suppress duplicate addresses. If you need to create an address list that includes previously-seen addresses you may use the (<i>concataddr</i>) function, which is identical to (<i>formataddr</i>) in all other respects. Note that (<i>concataddr</i>) will NOT add addresses to the duplicate-suppression cache.</p>
<h3>Other Hints and Tips</h3>
<p>Sometimes to format function writers it is confusing as to why output is duplicated. The general rule to remember is simple: If a function or component escape is used where it starts with a %, then it will generate text in the output file. Otherwise, it will not. </p>
<p> A good example is a simple attempt to generate a To: header based on the From: and Reply-To: headers: </p>
<dl>
<dd>
<pre>%(formataddr %&lt;{reply-to}%|%{from})%(putaddr To: )</pre>
</dl>
<p> Unfortuantely if the Reply-to: header is NOT present, the output line that is generated will be something like: </p>
<dl>
<dd>
<pre>My From User &lt;from [at] example.com&gt;To: My From User &lt;from [at] example.com&gt;</pre>
</dl>
<p> What went wrong? When performing the test for the <code>if</code> clause (%&lt;), the component is not output because it is considered an argument to the <code>if</code> statement (hence the rule about the lack of % applies). But the component escape in our <code>else</code> statement (everything after the `%|&#8217;) is NOT an argument to anything; the syntax is that it is written with a %, and thus the value of that component is output. This also has the side effect of setting the <i>str</i> register, which is later picked up by the (<i>formataddr</i>) function and then output by (<i>putaddr</i>). This format string has another bug as well; there should always be a valid width value in the <i>num</i> register when (<i>putaddr</i>) is called, otherwise bad formatting can take place. </p>
<p> The solution is to use the (<i>void</i>) function; this will prevent the function or component from outputting any text. With this in place (and using (<i>width</i>) to set the <i>num</i> register for the width, a better implementation would look like: </p>
<dl>
<dd>
<pre>%(formataddr %&lt;{reply-to}%|%(void{from})%(void(width))%(putaddr To: )</pre>
</dl>
<p> It should be noted here that the side-effects of functions and component escapes still are in force: as a result each component test in the <code>if-elseif-else-endif</code> clause sets the <i>str</i> register. </p>
<p> As an additional note, the (<i>formataddr</i>) and (<i>concataddr</i>) functions have special behavior when it comes to the <i>str</i> register. The starting point of the register is saved and is used to build up entries in the address list. </p>
<p> You will find the <code>fmttest</code> utility invaluable when debugging problems with format strings.</p>
<h3>Examples</h3>
<p>With all this in mind, here&#8217;s the default format string for <code>scan</code>. It&#8217;s been divided into several pieces for readability. The first part is: </p>
<dl>
<dd>
<pre>%4(msg)%&lt;(cur)+%| %&gt;%&lt;{replied}-%?{encrypted}E%| %&gt;</pre>
</dl>
<p> which says that the message number should be printed in four digits. If the message is the current message then a `+&#8217; else a space should be printed; if a &#8220;Replied:&#8221; field is present then a `-&#8216; else if an &#8220;Encrypted:&#8221; field is present then an `E&#8217; otherwise a space should be printed. Next: </p>
<dl>
<dd>
<pre>%02(mon{date})/%02(mday{date})</pre>
</dl>
<p> the month and date are printed in two digits (zero filled) separated by a slash. Next, </p>
<dl>
<dd>
<pre>%&lt;{date} %|*%&gt;</pre>
</dl>
<p> If a &#8220;Date:&#8221; field was present, then a space is printed, otherwise a `*&#8217;. Next, </p>
<dl>
<dd>
<pre>%&lt;(mymbox{from})%&lt;{to}To:%14(decode(friendly{to}))%&gt;%&gt;</pre>
</dl>
<p> if the message is from me, and there is a &#8220;To:&#8221; header, print &#8220;To:&#8221; followed by a &#8220;user-friendly&#8221; rendering of the first address in the &#8220;To:&#8221; field; any MIME-encoded characters are decoded into the actual characters. Continuing, </p>
<dl>
<dd>
<pre>%&lt;(zero)%17(decode(friendly{from}))%&gt;</pre>
</dl>
<p> if either of the above two tests failed, then the &#8220;From:&#8221; address is printed in a mime-decoded, &#8220;user-friendly&#8221; format. And finally, </p>
<dl>
<dd>
<pre>%(decode{subject})%&lt;{body}&lt;&lt;%{body}&gt;&gt;%&gt;</pre>
</dl>
<p> the mime-decoded subject and initial body (if any) are printed. </p>
<p> For a more complicated example, next consider a possible <i>replcomps</i> format file. </p>
<dl>
<dd>
<pre>%(lit)%(formataddr %&lt;{reply-to}</pre>
</dl>
<p> This clears <i>str</i> and formats the &#8220;Reply-To:&#8221; header if present. If not present, the else-if clause is executed. </p>
<dl>
<dd>
<pre>%?{from}%?{sender}%?{return-path}%&gt;)\</pre>
</dl>
<p> This formats the &#8220;From:&#8221;, &#8220;Sender:&#8221; and &#8220;Return-Path:&#8221; headers, stopping as soon as one of them is present. Next: </p>
<dl>
<dd>
<pre>%&lt;(nonnull)%(void(width))%(putaddr To: )
%&gt;\</pre>
</dl>
<p> If the <i>formataddr</i> result is non-null, it is printed as an address (with line folding if needed) in a field <i>width</i> wide with a leading label of &#8220;To:&#8221;. </p>
<dl>
<dd>
<pre>%(lit)%(formataddr{to})%(formataddr{cc})%(formataddr(me))\</pre>
</dl>
<p> <i>str</i> is cleared, and the &#8220;To:&#8221; and &#8220;Cc:&#8221; headers, along with the user&#8217;s address (depending on what was specified with the &#8220;-cc&#8221; switch to <i>repl</i>) are formatted. </p>
<dl>
<dd>
<pre>%&lt;(nonnull)%(void(width))%(putaddr cc: )
%&gt;\</pre>
</dl>
<p> If the result is non-null, it is printed as above with a leading label of &#8220;cc:&#8221;. </p>
<dl>
<dd>
<pre>%&lt;{fcc}Fcc: %{fcc}
%&gt;\</pre>
</dl>
<p> If a <code>-fcc</code> <i>folder</i> switch was given to <code>repl</code> (see <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1) for more details about %{<i>fcc</i>}), an &#8220;Fcc:&#8221; header is output. </p>
<dl>
<dd>
<pre>%&lt;{subject}Subject: Re: %{subject}
%&gt;\</pre>
</dl>
<p> If a subject component was present, a suitable reply subject is output. </p>
<dl>
<dd>
<pre>%&lt;{message-id}In-Reply-To: %{message-id}
%&gt;\
%&lt;{message-id}References: %&lt;{references} %{references}%&gt;\
%{message-id}
%&gt;
--------</pre>
</dl>
<p> If a message-id component was present, an &#8220;In-Reply-To:&#8221; header is output including the message-id, followed by a &#8220;References:&#8221; header with references, if present, and the message-id. As with all plain-text, the row of dashes are output as-is. </p>
<p> This last part is a good example for a little more elaboration. Here&#8217;s that part again in pseudo-code: </p>
<dl>
<dd>
<pre>if (comp_exists(message-id)) then
 print (``In-reply-to: '')
 print (message-id.value)
 print (``
'')
endif
if (comp_exists(message-id)) then
 print (``References: '')
 if (comp_exists(references)) then
 print(references.value);
 endif
 print (message-id.value)
 print (``
'')
endif</pre>
</dl>
<p> One more example: Currently, <code>nmh</code> supports very large message numbers, and it is not uncommon for a folder to have far more than 10000 messages. Nontheless (as noted above) the various scan format strings are inherited from older MH versions, and are generally hard-coded to 4 digits of message number before formatting problems start to occur. The nmh format strings can be modified to behave more sensibly with larger message numbers: </p>
<dl>
<dd>
<pre>%(void(msg))%&lt;(gt 9999)%(msg)%|%4(msg)%&gt;</pre>
</dl>
<p> The current message number is placed in <i>num</i>. (Note that (<i>msg</i>) is an int function, not a component.) The (<i>gt</i>) conditional is used to test whether the message number has 5 or more digits. If so, it is printed at full width, otherwise at 4 digits.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-scan/">scan</a></i>(1), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1), <i><a href="/docs/linux/man/1-fmttest/">fmttest</a></i>(1),</p>
<h2>Context</h2>
<p>None</p>
