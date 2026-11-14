---
title: "mhl(1)"
name: "mhl"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhl/"
description: "mhl – produce formatted listings of nmh messages"
---

<h2 class="name">NAME</h2>
<p> mhl &#8211; produce formatted listings of nmh messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/mhl</code> [<code>-bell</code> | <code>-nobell</code>] [<code>-clear</code> | <code>-noclear</code>] [<code>-folder</code> <i>+folder</i>] [<code>-form</code> <i>formfile</i>] [<code>-length</code> <i>lines</i>] [<code>-width</code> <i>columns</i>] [<code>-moreproc</code> <i>program</i>] [<code>-nomoreproc</code>] [<code>-fmtproc</code> <i>program</i>] [<code>-nofmtproc</code>] [<i>files</i> <i>&#8230;</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Mhl</code></p>
<dd>is an <code>nmh</code> command for filtering and/or displaying text messages. It is the default method of displaying text messages for <code>nmh</code> (it is the default <i>showproc</i>). </p>
<p> As with <code>more</code>, each of the messages specified as arguments (or the standard input) will be output. If more than one message file is specified, the user will be prompted prior to each one, and a &lt;RETURN&gt; or &lt;EOT&gt; will begin the output, with &lt;RETURN&gt; clearing the screen (if appropriate), and &lt;EOT&gt; (usually CTRL-D) suppressing the screen clear. An &lt;INTERRUPT&gt; (usually CTRL-C) will abort the current message output, prompting for the next message (if there is one), and a &lt;QUIT&gt; (usually CTRL-\) will terminate the program (without core dump). </p>
<p> The <code>-bell</code> option tells <code>mhl</code> to ring the terminal&#8217;s bell at the end of each page, while the <code>-clear</code> option tells <code>mhl</code> to clear the screen at the end of each page (or output a formfeed after each message). Both of these switches (and their inverse counterparts) take effect only if the profile entry <i>moreproc</i> is defined but empty, and <code>mhl</code> is outputting to a terminal. If the <i>moreproc</i> entry is defined and non-empty, and <code>mhl</code> is outputting to a terminal, then <code>mhl</code> will cause the <i>moreproc</i> to be placed between the terminal and <code>mhl</code> and the switches are ignored. Furthermore, if the <code>-clear</code> switch is used and <i>mhl&#8217;s</i> output is directed to a terminal, then <code>mhl</code> will consult the <code>$TERM</code> and <code>$TERMCAP</code> environment variables to determine the user&#8217;s terminal type in order to find out how to clear the screen. If the <code>-clear</code> switch is used and <code>mhl</code>&#8216;s output is not directed to a terminal (e.g., a pipe or a file), then <code>mhl</code> will send a formfeed after each message. </p>
<p> To override the default <i>moreproc</i> and the profile entry, use the <code>-moreproc</code> <i>program</i> switch. Note that <code>mhl</code> will never start a <i>moreproc</i> if invoked on a hardcopy terminal. </p>
<p> The <code>-length</code> <i>length</i> and <code>-width</code> <i>width</i> switches set the screen length and width, respectively. These default to the values indicated by <code>$TERMCAP</code>, if appropriate, otherwise they default to 40 and 80, respectively. </p>
<p> The default format file used by <code>mhl</code> is called &#8220;<i>mhl.format</i>&#8221;. <code>mhl</code> will first search for this file in the user&#8217;s <code>nmh</code> directory, and will then search in the directory <i>/etc/nmh</i>. This default can be changed by using the <code>-form</code> <i>formatfile</i> switch. </p>
<p> Finally, the <code>-folder</code> <i>+folder</i> switch sets the <code>nmh</code> folder name, which is used for the &#8220;messagename:&#8221; field described below. The environment variable <code>$mhfolder</code> is consulted for the default value, which <code>show</code>, <code>next</code>, and <code>prev</code> initialize appropriately. </p>
<p> <code>Mhl</code> operates in two phases: 1) read and parse the format file, and 2) process each message (file). During phase 1, an internal description of the format is produced as a structured list. In phase 2, this list is walked for each message, outputting message information under the format constraints from the format file. </p>
<p> The format file can contain information controlling screen clearing, screen size, wrap-around control, transparent text, component ordering, and component formatting. Also, a list of components to ignore may be specified, and a couple of &#8220;special&#8221; components are defined to provide added functionality. Message output will be in the order specified by the order in the format file. </p>
<p> Each line of a format file has one of the following forms: </p>
<dl>
<dt>
<dd>
<pre><code>
;
comment
    : cleartext
          variable[, variable...] component : [ variable, ... ]
</code></pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> A line beginning with a `;&#8217; is a comment, and is ignored.</p>
<dt>&bull;</p>
<dd> A line beginning with a `:&#8217; is clear text, and is output exactly as is.</p>
<dt>&bull;</p>
<dd> A line containing only a `:&#8217; produces a blank line in the output.</p>
<dt>&bull;</p>
<dd> A line beginning with &#8220;component:&#8221; defines the format for the specified component,</p>
<dt>&bull;</p>
<dd> Remaining lines define the global environment.</dl>
<p> For example, the line: </p>
<dl>
<dt>
<dd> width=80,length=40,clearscreen,overflowtext=&quot;***&quot;,overflowoffset=5</dl>
<p> defines the screen size to be 80 columns by 40 rows, specifies that the screen should be cleared prior to each page, that the overflow indentation is 5, and that overflow text should be flagged with &#8220;***&#8221;. </p>
<p> Following are all of the current variables and their arguments. If they follow a component, they apply only to that component, otherwise, their affect is global. Since the whole format is parsed before any output processing, the last global switch setting for a variable applies to the whole message if that variable is used in a global context (i.e., bell, clearscreen, width, length). </p>
<dl>
<dt>
<dd>
variable      type       semantics<br />
width          integer    screen width or component width<br />
length         integer    screen length or component length<br />
offset         integer    positions to indent &#8220;component: &#8221;<br />
overflowtext   string     text to use at the beginning of an<br />
                          overflow line<br />
overflowoffset integer    positions to indent overflow lines<br />
compwidth      integer    positions to indent component text<br />
                          after the first line is output<br />
uppercase      flag       output text of this component in all<br />
                          upper case<br />
nouppercase    flag       don&#8217;t uppercase<br />
clearscreen    flag/G     clear the screen prior to each page<br />
noclearscreen  flag/G     don&#8217;t clearscreen<br />
bell           flag/G     ring the bell at the end of each page<br />
nobell         flag/G     don&#8217;t bell<br />
component      string/L   name to use instead of &#8220;component&#8221; for<br />
                          this component<br />
nocomponent    flag       don&#8217;t output &#8220;component: &#8221; for this<br />
                          component<br />
center         flag       center component on line (works for<br />
                          one-line components only)<br />
nocenter       flag       don&#8217;t center<br />
leftadjust     flag       strip off leading whitespace on each<br />
                          line of text<br />
noleftadjust   flag       don&#8217;t leftadjust<br />
compress       flag       change newlines in text to spaces<br />
nocompress     flag       don&#8217;t compress<br />
wrap           flag       Wrap lines that exceed width (default)<br />
nowrap         flag       Do not perform line wrapping<br />
split          flag       don&#8217;t combine multiple fields into<br />
                          a single field<br />
nosplit        flag       combine multiple fields into<br />
                          a single field<br />
newline        flag       print newline at end of components<br />
                          (this is the default)<br />
nonewline      flag       don&#8217;t print newline at end of components<br />
formatfield    string     format string for this component<br />
                          (see below)<br />
decode         flag       decode text as RFC 2047 encoded<br />
                          header field<br />
addrfield      flag       field contains addresses<br />
datefield      flag       field contains dates<br />
format         flag       Run component through formatproc filter<br />
                          (body only)<br />
noformat       flag       Do not run component through<br />
                          formatproc filter (default)<br />
formatarg      string     Argument to format filter
</dl>
<p> To specify the value of integer-valued and string-valued variables, follow their name with an equals-sign and the value. Integer-valued variables are given decimal values, while string-valued variables are given arbitrary text bracketed by double-quotes. If a value is suffixed by &#8220;/G&#8221; or &#8220;/L&#8221;, then its value is useful in a global-only or local-only context (respectively). </p>
<p> A line of the form: </p>
<dl>
<dt>
<dd> ignores=component,&#8230;</dl>
<p> specifies a list of components which are never output. </p>
<p> The component &#8220;MessageName&#8221; (case-insensitive) will output the actual message name (file name) preceded by the folder name if one is specified or found in the environment. The format is identical to that produced by the <code>-header</code> option to <code>show</code>. </p>
<p> The component &#8220;Extras&#8221; will output all of the components of the message which were not matched by explicit components, or included in the ignore list. If this component is not specified, an ignore list is not needed since all non-specified components will be ignored. </p>
<p> If &#8220;nocomponent&#8221; is NOT specified, then the component name will be output as it appears in the format file. </p>
<p> The default format file is: </p>
<dl>
<dt>
<dd>
<pre><code>
;
mhl.format;
; default message filter for `show'
;
:
overflowtext="***",overflowoffset=5
leftadjust,compwidth=9
ignores=msgid,message-id,received,content-type,content-transfer-encoding,content-id
Date:formatfield="%&lt;(nodate{text})%{text}%|%(pretty{text})%&gt;"
To:
cc:
From:decode
Subject:decode
:
extras:nocomponent
:
body:nocomponent,overflowtext=,overflowoffset=0,noleftadjust
</code></pre>
</dl>
<p> The variable &#8220;formatfield&#8221; specifies a format string (see <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5)). The flag variables &#8220;addrfield&#8221; and &#8220;datefield&#8221; (which are mutually exclusive), tell <code>mhl</code> to interpret the escapes in the format string as either addresses or dates, respectively. </p>
<p> By default, <code>mhl</code> does not apply any formatting string to fields containing address or dates (see <i><a href="/docs/linux/man/5-mh-mail/">mh-mail</a></i>(5) for a list of these fields). Note that this results in faster operation since <code>mhl</code> must parse both addresses and dates in order to apply a format string to them. If desired, <code>mhl</code> can be given a default format string for either address or date fields (but not both). To do this, on a global line specify: either the flag addrfield or datefield, along with the appropriate formatfield variable string. </p>
<p> The &#8220;format&#8221; flag specifies that this component will be run through the filter program specified by the <i>formatproc</i> profile entry. This filter program is expected to read data on standard input and output data on standard output. Currently the &#8220;format&#8221; flag is only supported for the &#8220;body&#8221; component. The component name will be prefixed to the output <i>after</i> the filter has been run. The expected use of this is to filter a message body to create more pleasing text to use in a reply message. A suggested filter to use for <i><a href="/docs/linux/man/1-repl/">repl</a>(1)</i> is as follows: </p>
<dl>
<dt>
<dd> body:component=&quot;&gt;&quot;,overflowtext=&quot;&gt;&quot;,overflowoffset=0,format,nowrap</dl>
<p> The <code>-fmtproc</code> and <code>-nofmtproc</code> switches can be used to override the <i>formatproc</i> profile entry. </p>
<p> The <i>formatarg</i> option specifies a string that is used as an argument to the format filter. This string is processed by <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) and all of the message components are available for use. Multiple <i>formatarg</i> options can be used to build up multiple arguments to the format filter.</p>
<h2>FILES</h2>
<pre>
^/etc/nmh/mhl.format~^The message template
^or &lt;mh-dir&gt;/mhl.format~^Rather than the standard template
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^moreproc:~^Program to use as interactive front-end
^formatproc:~^Program to use as a filter for components that
^^have the ``format'' flag set.
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-show/">show</a></i>(1), <i><a href="/docs/linux/man/8-ap/">ap</a></i>(8), <i><a href="/docs/linux/man/8-dp/">dp</a></i>(8)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-bell</code>'
`<code>-noclear</code>'
`<code>-length 40</code>'
`<code>-width 80</code>'
</pre>
<h2>CONTEXT</h2>
<p> None</p>
<h2>BUGS</h2>
<p> There should be some way to pass `bell&#8217; and `clear&#8217; information to the front-end. </p>
<p> The &#8220;nonewline&#8221; option interacts badly with &#8220;compress&#8221; and &#8220;split&#8221;. </p>
<p> The &#8220;format&#8221; option really should work on something other than the body component. </p>
<h2>Index</h2>
