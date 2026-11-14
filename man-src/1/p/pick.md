---
title: "pick(1)"
name: "pick"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pick/"
description: "pick – search for messages by content"
---

<h2 class="name">NAME</h2>
<p> pick &#8211; search for messages by content </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pick</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-and</code> &#8230;] [<code>-or</code> &#8230;] [<code>-not</code> &#8230;] [<code>-lbrace</code> &#8230; <code>-rbrace</code>] [<code>&#8211;component</code> <i>pattern</i>] [<code>-cc</code> <i>pattern</i>] [<code>-date</code> <i>pattern</i>] [<code>-from</code> <i>pattern</i>] [<code>-search</code> <i>pattern</i>] [<code>-subject</code> <i>pattern</i>] [<code>-to</code> <i>pattern</i>] [<code>-after</code> <i>date</i>] [<code>-before</code> <i>date</i>] [<code>-datefield</code> <i>field</i>] [<code>-sequence</code> <i>name</i> &#8230;] [<code>-nosequence</code>] [<code>-public</code> | <code>-nopublic</code>] [<code>-zero</code> | <code>-nozero</code>] [<code>-list</code> | <code>-nolist</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<dd>typical usage: </p>
<dl>
<dt>
<dd>
<pre>
scan&nbsp;<wbr>`pick -from jones`
pick -to holloway -sequence select
show&nbsp;<wbr>`pick -before friday`
</pre>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>Pick</code> searches within a folder for messages with the specified contents, and then identifies those messages. Two types of search primitives are available: pattern matching and date constraint operations. </p>
<p> A modified <i><a href="/docs/linux/man/1-grep/">grep</a></i>(1) is used to perform the matching, so the full regular expression (see <i><a href="/docs/linux/man/1-ed/">ed</a></i>(1)) facility is available within <i>pattern</i>. With <code>-search</code>, <i>pattern</i> is used directly, and with the others, the grep pattern constructed is: </p>
<dl>
<dt>
<dd> `component[ 	]*:.*pattern&#8217;</dl>
<p> This means that the pattern specified for a <code>-search</code> will be found everywhere in the message, including the header and the body, while the other pattern matching requests are limited to the single specified component. The expression </p>
<dl>
<dt>
<dd> `&#8211;component pattern&#8217;</dl>
<p> is a shorthand for specifying </p>
<dl>
<dt>
<dd> `-search &#8220;component[ 	]*:.*pattern&#8221;&nbsp;<wbr>&#8216;</dl>
<p> It is used to pick a component which is not one of &#8220;To:&#8221;, &#8220;cc:&#8221;, &#8220;Date:&#8221;, &#8220;From:&#8221;, or &#8220;Subject:&#8221;. An example is &#8220;<code>pick &#8211;reply-to pooh</code>&#8221;. </p>
<p> Pattern matching is performed on a per-line basis. Within the header of the message, each component is treated as one long line, but in the body, each line is separate. Lower-case letters in the search pattern will match either lower or upper case in the message, while upper case will match only upper case. </p>
<p> Note that since the <code>-date</code> switch is a pattern matching operation (as described above), to find messages sent on a certain date the pattern string must match the text of the &#8220;Date:&#8221; field of the message. </p>
<p> Independent of any pattern matching operations requested, the switches <code>-after</code> <i>date</i> or <code>-before</code> <i>date</i> may also be used to introduce date/time constraints on all of the messages. By default, the &#8220;Date:&#8221; field is consulted, but if another date yielding field (such as &#8220;BB-Posted:&#8221; or &#8220;Delivery-Date:&#8221;) should be used, the <code>-datefield</code> <i>field</i> switch may be used. </p>
<p> With <code>-before</code> and <code>-after</code>, <code>pick</code> will actually parse the date fields in each of the messages specified in `msgs&#8217; and compare them to the date/time specified. If <code>-after</code> is given, then only those messages whose &#8220;Date:&#8221; field value is chronologically after the date specified will be considered. The <code>-before</code> switch specifies the complimentary action. </p>
<p> Both the <code>-after</code> and <code>-before</code> switches take legal RFC 822-style date specifications as arguments. <code>Pick</code> will default certain missing fields so that the entire date need not be specified. These fields are (in order of defaulting): timezone, time and timezone, date, date and timezone. All defaults are taken from the current date, time, and timezone. </p>
<p> In addition to RFC 822-style dates, <code>pick</code> will also recognize any of the days of the week (&#8220;sunday&#8221;, &#8220;monday&#8221;, and so on), and the special dates &#8220;today&#8221;, &#8220;yesterday&#8221; (24 hours ago), and &#8220;tomorrow&#8221; (24 hours from now). All days of the week are judged to refer to a day in the past (e.g., telling <i>pick</i> &#8220;saturday&#8221; on a &#8220;tuesday&#8221; means &#8220;last saturday&#8221; not &#8220;this saturday&#8221;). </p>
<p> Finally, in addition to these special specifications, <code>pick</code> will also honor a specification of the form &#8220;-dd&#8221;, which means &#8220;dd days ago&#8221;. </p>
<p> <code>Pick</code> supports complex boolean operations on the searching primitives with the <code>-and</code>, <code>-or</code>, <code>-not</code>, and <code>-lbrace</code> <code>&#8230;</code> <code>-rbrace</code> switches. For example, </p>
<dl>
<dt>
<dd>
<pre>
pick -after yesterday -and
     -lbrace -from freida -or -from fear -rbrace
</pre>
</dl>
<p> identifies messages recently sent by &#8220;frieda&#8221; or &#8220;fear&#8221;. </p>
<p> The matching primitives take precedence over the <code>-not</code> switch, which in turn takes precedence over <code>-and</code> which in turn takes precedence over <code>-or</code>. To override the default precedence, the <code>-lbrace</code> and <code>-rbrace</code> switches are provided, which act just like opening and closing parentheses in logical expressions. </p>
<p> If no search criteria are given, all the messages specified on the command line are selected (this defaults to &#8220;all&#8221;). </p>
<p> Once the search has been performed, if the <code>-list</code> switch is given, the message numbers of the selected messages are written to the standard output separated by newlines. This is <code>extremely</code> useful for quickly generating arguments for other <code>nmh</code> programs by using the &#8220;backquoting&#8221; syntax of the shell. For example, the command </p>
<dl>
<dt>
<dd> scan&nbsp;<wbr>`pick&nbsp;<wbr>+todo -after&nbsp;<wbr>&#8220;31 Mar 83 0123 PST&#8221;`</dl>
<p> says to <code>scan</code> those messages in the indicated folder which meet the appropriate criterion. Note that since <code>pick</code>&#8216;s context changes are written out prior to <code>scan</code>&#8216;s invocation, you need not give the folder argument to <code>scan</code> as well. </p>
<p> The <code>-sequence</code> <i>name</i> switch may be given once for each sequence the user wishes to define. For each sequence named, that sequence will be defined to mean exactly those messages selected by <code>pick</code>. For example, </p>
<dl>
<dt>
<dd> pick -from frated -seq fred</dl>
<p> defines a new message sequence for the current folder called &#8220;fred&#8221; which contains exactly those messages that were selected. </p>
<p> The <code>-nosequence</code> switch will disable all previously named sequences, allowing those established by a profile component to be overridden. </p>
<p> By default, <code>pick</code> will zero a sequence before adding it. This action can be disabled with the <code>-nozero</code> switch, which means that the messages selected by <code>pick</code> will be added to the sequence, if it already exists, and any messages already a part of that sequence will remain so. </p>
<p> The <code>-public</code> and <code>-nopublic</code> switches are used by <code>pick</code> in the same way <code>mark</code> uses them.</p>
<h3>Output when no messages are matched</h3>
<p> If <code>pick</code> is used in a backquoted operation, such as </p>
<dl>
<dt>
<dd> scan&nbsp;<wbr>`pick -from jones`</dl>
<p> and <code>pick</code> selects no messages (e.g., no messages are from &#8220;jones&#8221;), then the shell will still run the outer command (e.g., <code>scan</code>). Since no messages were matched, <code>pick</code> produced no output, and the argument given to the outer command as a result of backquoting <code>pick</code> is empty. In the case of <code>nmh</code> programs, the outer command now acts as if the default `msg&#8217; or `msgs&#8217; should be used (e.g., &#8220;all&#8221; in the case of <code>scan</code>). To prevent this unexpected behavior, if <code>-list</code> was given, and if its standard output is not a tty, then <code>pick</code> outputs the illegal message number &#8220;0&#8221; when it fails. This lets the outer command fail gracefully as well.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mark/">mark</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to all
`<code>-datefield date</code>'
`<code>-zero</code>'
`<code>-list</code>' is the default if no `-sequence', `-nolist' otherwise
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder.</p>
<h2>HISTORY</h2>
<p> In previous versions of <code>MH</code>, the <code>pick</code> command would <code>show</code>, <code>scan</code>, or <code>refile</code> the selected messages. This was rather &#8220;inverted logic&#8221; from the UNIX point of view, so <code>pick</code> was changed to define sequences and output those sequences. Hence, <code>pick</code> can be used to generate the arguments for all other <code>MH</code> commands, instead of giving <code>pick</code> endless switches for invoking those commands itself. </p>
<p> Also, previous versions of <code>pick</code> balked if you didn&#8217;t specify a search string or a date/time constraint. The current version does not, and merely matches the messages you specify. This lets you type something like: </p>
<dl>
<dt>
<dd> show&nbsp;<wbr>`pick last:20 -seq fear`</dl>
<p> instead of typing </p>
<dl>
<dt>
<dd>
<pre>
mark -add -nozero -seq fear last:20
show fear
</pre>
</dl>
<p> Finally, timezones used to be ignored when comparing dates: they aren&#8217;t any more.</p>
<h2>HELPFUL HINTS</h2>
<p> Use &#8220;<code>pick sequence -list</code>&#8221; to enumerate the messages in a sequence (such as for use by a shell script).</p>
<h2>BUGS</h2>
<p> Any occurrence of <code>-datefield</code> must occur prior to the <code>-after</code> or <code>-before</code> switch it applies to. </p>
<p> The pattern syntax &#8220;[l-r]&#8221; is not supported; each letter to be matched must be included within the square brackets. </p>
<h2>Index</h2>
