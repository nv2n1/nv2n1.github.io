---
title: "innwatch-ctl(5)"
name: "innwatch-ctl"
section: "5"
letter: "i"
url: "/docs/linux/man/5-innwatch-ctl/"
---

innwatch.ctl - control Usenet supervision by innwatch

<h2>Description</h2>

The file <i>&lt;pathetc in inn.conf&gt;/innwatch.ctl</i> is used to determine what actions are taken during the periodic supervisions by <i>innwatch</i>. 

 The file consists of a series of lines; blank lines and lines beginning with a number sign (``#'') are ignored. All other lines consist of seven fields, each preceded by a delimiting character, for example: 

 <pre><dl><dt><dd>:label:state:condition:test:limit:command:reason
</dl>
or
<dl><dt><dd>@label [at] state@condition [at] test@limit [at] command@reason
</dl></pre>The delimiter can be any one of several non-alphanumeric characters that does not appear elsewhere in the line; there is no way to quote it to include it in any of the fields. Any of ``!'', ``,'', ``:'', ``@'', ``;'', or ``?'' is a good choice. Each line can have a different delimiter; the first character on each line is the delimiter for that line. White space surrounding delimiters, except before the first, is ignored, and does not form part of the fields; white space within fields is permitted. All delimiters must be present. 

 The first field is a label for this control line. It is used as an internal state indicator and in <i>ctlinnd</i> messages to control the server. If this field is empty, the line number is used. 

 The second field specifies when this control line should be used. It consists of a list of labels and special indicators, separated by whitespace. If the current state matches against any of the labels in this field, this line will be used as described below. The values that may be used are:
<dl><dt>-
<dd>This line matches if the current state is the same as the label on this line, or if the current state is ``run'', the initial state. This is also the default state if this field is empty.
<dt>+
<dd>This line matches if the current state is ``run''.
<dt>*
<dd>This line always matches.
<dt>label
<dd>This line matches if the current state is the specified ``label''.
<dt>-label
<dd>This line matches if the current state is not the specified ``label''.</dl>
 

 The third field specifies a shell command that is invoked if this line matches. Do not use any shell filename expansion characters such as ``*'', ``?'', or ``['' (even quoted, they're not likely to work as intended). If the command succeeds, as indicated by its exit status, it is expected to have printed a single integer to standard output. This gives the value of this control line, to be used below. If the command fails, the line is ignored. The command is executed with its current directory set to the news spool articles directory, <i>&lt;patharticles in inn.conf&gt;</i>. 

 The fourth field specifies the operator to use to test the value returned above. It should be one of the two letter numeric test operators defined in <i><a HREF="/docs/linux/man/1-test/">test</a></i>(1) such as ``eq'', ``lt'' and the like. The leading dash (``-'') should not be included. 

 The fifth field specifies a constant with which to compare the value using the operator just defined. This is done by invoking the command: 

<dl><dd>test value -operator constant</dl>
 

 The line is said to ``succeed'' if it returns true. 

 The sixth field specifies what should be done if the line succeeds, and in some cases if it fails. Any of the following words may be used:
<dl><dt>throttle
<dd>Causes <i>innwatch</i> to throttle the server if this line succeeds. It also sets the state to the value of the line's label. If the line fails, and the state was previously equal to the label on this line (that is, this line had previously succeeded), then a <i>go</i> command will be sent to the server, and <i>innwatch</i> will return to the ``run'' state. The ``throttle'' is only performed if the current state is ``run'' or a state other than the label of this line, regardless of whether the command succeeds.
<dt>pause
<dd>Is identical to ``throttle'' except that the server is paused.
<dt>shutdown
<dd>Sends a ``shutdown'' command to the server. It is for emergency use only.
<dt>flush
<dd>Sends a ``flush'' command to the server.
<dt>go
<dd>Causes <i>innwatch</i> to send a ``go'' command to the server and to set the state to ``run''.
<dt>exit
<dd>Causes <i>innwatch</i> to exit.</dl><dl><dt>skip
<dd>The remainder of the control file is skipped for the current pass.</dl>
 

 The last field specifies the reason that is used in those <i>ctlinnd</i> commands that require one. More strictly, it is part of the reason --- <i>innwatch</i> appends some information to it. In order to enable other sites to recognize the state of the local <i>innd</i> server, this field should usually be set to one of several standard values. Use ``No space'' if the server is rejecting articles because of a lack of filesystem resources. Use ``loadav'' if the server is rejecting articles because of a lack of CPU resources. 

 Once <i>innwatch</i> has taken some action as a consequence of its control line, it skips the rest of the control file for this pass. If the action was to restart the server (that is, issue a ``go'' command), then the next pass will commence almost immediately, so that <i>innwatch</i> can discover any other condition that may mean that the server should be suspended again.

<h2>Examples</h2>

<dl><dd><pre>@@@inndf .@lt [at] 10000@throttle@No space
@@@inndf -i .@lt [at] 1000@throttle@No space (inodes)</pre></dl>
 

 The first line causes the server to be throttled if the free space drops below 10000 units (using whatever units <i><a HREF="/docs/linux/man/8-inndf/">inndf</a></i>(8) uses), and restarted again when free space increases above the threshold. 

 The second line does the same for inodes. 

 The next three lines act as a group and should appear in the following order. It is easier to explain them, however, if they are described from the last up. 

<dl><dd><pre>!load!load hiload!loadavg!lt!5!go!
:hiload:+ load:loadavg:gt:8:throttle:loadav
/load/+/loadavg/ge/6/pause/loadav</pre></dl>
 

 The final line causes the server to be paused if <i>innwatch</i> is in the ``run'' state and the load average rises to, or above, six. The state is set to ``load'' when this happens. The previous line causes the server to be throttled when <i>innwatch</i> is in the ``run'' or ``load'' state, and the load average rises above eight. The state is set to ``hiload'' when this happens. Note that <i>innwatch</i> can switch the server from ``paused'' to ``throttled'' if the load average rises from below six to between six and seven, and then to above eight. The first line causes the server to be sent a ``go'' command if <i>innwatch</i> is in the ``load'' or ``hiload'' state, and the load average drops below five. 

 Note that all three lines assume a mythical command <i>loadavg</i> that is assumed to print the current load average as an integer. In more practical circumstances, a pipe of <i>uptime</i> into <i>awk</i> is more likely to be useful.

<h2>Bugs</h2>

This file must be tailored for each individual site, the sample supplied is truly no more than a sample. The file should be ordered so that the more common problems are tested first. 

 The ``run'' state is not actually identified by the label with that three letter name, and using it will not work as expected. 

 Using an ``unusual'' character for the delimiter such as ``('', ``*'', ``&amp;'', ```'', ``&acute;'', and the like, is likely to lead to obscure and hard to locate bugs.

<h2>History</h2>

Written by &lt;kre [at] munnari.oz.au&gt; for InterNetNews. This is revision 5909, dated 2002-12-03.

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-inn-conf/">inn.conf</a>(5), <a HREF="/docs/linux/man/8-innd/">innd</a>(8), <a HREF="/docs/linux/man/8-inndf/">inndf</a>(8), <a HREF="/docs/linux/man/8-ctlinnd/">ctlinnd</a>(8), <a HREF="/docs/linux/man/8-news-daily/">news.daily</a>(8). 
