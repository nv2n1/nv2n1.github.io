---
title: "kwalletcli_getpin(1)"
name: "kwalletcli_getpin"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kwalletcli_getpin/"
description: "kwalletcli_getpin – command line interface to pinentry"
---

<h2>NAME</h2>
<p> <code>kwalletcli_getpin</code> &#8211; command line interface to pinentry</p>
<h2>SYNOPSIS</h2>
<p> [-<code>q</code> ] [-<code>b | m | p </code><i>prompt</i> ] [-<code>E | e </code><i>errortext</i> ]<br />
 [-<code>N </code><i>NoText</i> ] [-<code>t </code><i>desctext</i> ] [-<code>Y </code><i>YesText</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility is a shell wrapper speaking to <code>pinentry</code> using the Assuan protocol. It will ask the user for a passphrase and print it, without any trailing newline, to standard output. There are options for asking a boolean question or displaying a message. </p>
<p> If <code>PINENTRY</code> is not empty but points to a non-existing or failing programme, <code>pinentry</code> is not called. Instead, <a href="/docs/linux/man/1-xmessage/">xmessage</a>(1) is used for boolean queries and messages if <code>DISPLAY</code> is set; otherwise, uses simple terminal I/O on <code>GPG_TTY</code> using <a href="/docs/linux/man/1-stty/">stty</a>(1) to disable echo of terminal input for passphrase queries. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-b</code></p>
<dd> Ask for a confirmation (boolean) instead of a passphrase.</p>
<dt><code>-E</code></p>
<dd> Unset a previously set error text.</p>
<dt><code>-E </code><i>errtxt</i></p>
<dd> Set the error text to <i>errtxt</i> displaying a dialogue box with a red X icon indicating that this is a retry question.</p>
<dt><code>-m</code></p>
<dd> Display a message (one-button query) instead of asking.</p>
<dt><code>-N </code><i>NoText</i></p>
<dd> Use <i>NoText</i> instead of <code>Cancel</code> for the text of the abort button, if any.</p>
<dt><code>-p </code><i>prompt</i></p>
<dd> Set the small descriptive text shown in front of the input field (&#8220;the Prompt&#8221; ) to <i>prompt</i></p>
<dt><code>-q</code></p>
<dd> Be more quiet.</p>
<dt><code>-t </code><i>desctxt</i></p>
<dd> Set the descriptive text (the input challenge) to <i>desctxt</i></p>
<dt><code>-Y </code><i>YesText</i></p>
<dd> Use <i>YesText</i> instead of <code>OK</code> for the text of the confirm button.</dl>
<p> All input and output is assumed to be in UTF-8.</p>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success, 1 if the passphrase input was cancelled by the user, or &gt;1 if an error occurred. Confirmation (boolean) error codes are 0 for Yes, 1 for No, or &gt;1 if an error occurred. Messages return &gt;0 if an error occurred, 0 otherwise. </p>
<p> A summary of the error codes follows:</p>
<dl>
<dt><code>0</code></p>
<dd> Read password successfully. Boolean question returned Yes/OK.</p>
<dt><code>1</code></p>
<dd> Boolean question returned No/Cancel.</p>
<dt><code>2</code></p>
<dd> Wrong command line syntax.</p>
<dt><code>3</code></p>
<dd> The process reading user input unexpectedly terminated or errored out.</p>
<dt><code>4</code></p>
<dd> Unexpected result reading from pinentry.</p>
<dt><code>5</code></p>
<dd> Unable to determine controlling tty, caller must set <code>GPG_TTY</code></p>
<dt><code>6</code></p>
<dd> Caught SIGHUP, SIGINT, SIGQUIT, SIGTRAP, SIGPIPE, or SIGTERM.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> If not set, pass current terminal information to <code>pinentry</code></p>
<dt><code>GPG_TERM</code></p>
<dd> Terminal type of the current tty. Defaults to the value of the environment variable <code>TERM</code> or &#8220;vt100&#8221; if unset.</p>
<dt><code>GPG_TTY</code></p>
<dd> The current terminal, determined by <a href="/docs/linux/man/1-tty/">tty</a>(1) if unset.</p>
<dt><code>LC_CTYPE</code></p>
<dd> Passed to <code>pinentry</code> Default: &#8220;en_US.UTF-8&#8221;</p>
<dt><code>LC_MESSAGES</code></p>
<dd> Passed to <code>pinentry</code> Unset by default.</p>
<dt><code>PINENTRY</code></p>
<dd> The <code>pinentry</code> programme to use. Default: &#8220;pinentry&#8221;</dl>
<h2>SEE ALSO</h2>
<p> gpg-agent1, <a href="/docs/linux/man/1-kwalletcli/">kwalletcli</a>(1), <a href="/docs/linux/man/1-pinentry/">pinentry</a>(1), <a href="/docs/linux/man/1-stty/">stty</a>(1), <a href="/docs/linux/man/1-tset/">tset</a>(1), <a href="/docs/linux/man/1-tty/">tty</a>(1)</p>
<h2>AUTHORS</h2>
<p> was written by An mirabilos Aq m@mirbsd.org mostly for tarent solutions GmbH.</p>
<h2>CAVEATS</h2>
<p> Some newer pinentry features, such as three-button operation or setting the window title, are not supported yet.</p>
<h2>BUGS</h2>
<p> Some <code>pinentry</code> programmes may not support messages correctly and display them as boolean queries instead. </p>
<p> Some implementations display labels with the wrong charset. </p>
<p> Neither of these two problems is an issue in but a bug of the backend implementation. </p>
<h2>Index</h2>
