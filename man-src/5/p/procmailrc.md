---
title: "procmailrc(5)"
name: "procmailrc"
section: "5"
letter: "p"
url: "/docs/linux/man/5-procmailrc/"
description: "procmailrc – procmail rcfile"
---

<p>procmailrc &#8211; procmail rcfile</p>
<h2>Synopsis</h2>
<p><code>$HOME/.procmailrc</code></p>
<h2>Description</h2>
<p>For a quick start, see <code>NOTES</code> at the end of the <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1) man page. </p>
<p> The rcfile can contain a mixture of environment variable assignments (some of which have special meanings to procmail), and recipes. In their most simple appearance, the recipes are simply one line regular expressions that are searched for in the header of the arriving mail. The first recipe that matches is used to determine where the mail has to go (usually a file). If processing falls off the end of the rcfile, procmail will deliver the mail to <code>$DEFAULT</code>. </p>
<p> There are two kinds of recipes: delivering and non-delivering recipes. If a <i>delivering recipe</i> is found to match, procmail considers the mail (you guessed it) delivered and will <i>cease processing</i> the rcfile after having successfully executed the action line of the recipe. If a <i>non-delivering recipe</i> is found to match, processing of the rcfile will <i>continue</i> after the action line of this recipe has been executed. </p>
<p> Delivering recipes are those that cause header and/or body of the mail to be: written into a file, absorbed by a program or forwarded to a mailaddress. </p>
<p> Non-delivering recipes are: those that cause the output of a program or filter to be captured back by procmail or those that start a nesting block. </p>
<p> You can tell procmail to treat a <i>delivering recipe</i> as if it were a non-delivering recipe by specifying the `c&#8217; flag on such a recipe. This will make procmail generate a <i>carbon copy</i> of the mail by delivering it to this recipe, yet continue processing the rcfile. </p>
<p> By using any number of recipes you can presort your mail extremely straightforward into several mailfolders. Bear in mind though that the mail can arrive concurrently in these mailfolders (if several procmail programs happen to run at the same time, not unlikely if a lot of mail arrives). To make sure this does not result in a mess, proper use of lockfiles is highly recommended. </p>
<p> The environment variable <code>assignments</code> and <code>recipes</code> can be freely intermixed in the rcfile. If any environment variable has a special meaning to procmail, it will be used appropriately the moment it is parsed (i.e., you can change the current directory whenever you want by specifying a new <code>MAILDIR</code>, switch lockfiles by specifying a new <code>LOCKFILE</code>, change the umask at any time, etc., the possibilities are endless :-). </p>
<p> The assignments and substitutions of these environment variables are handled exactly like in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) (that includes all possible quotes and escapes), with the added bonus that blanks around the &#8216;=&#8217; sign are ignored and that, if an environment variable appears without a trailing &#8216;=&#8217;, it will be removed from the environment. Any program in backquotes started by procmail will have the entire mail at its stdin.</p>
<h3>Comments</h3>
<p>A word beginning with # and all the following characters up to a NEWLINE are ignored. This does not apply to condition lines, which cannot be commented.</p>
<h3>Recipes</h3>
<p>A line starting with &#8216;:&#8217; marks the beginning of a recipe. It has the following format: </p>
<pre><dl><dt><dd>:0 [<i>flags</i>] [ : [<i>locallockfile</i>] ]
&lt;zero or more conditions (one per line)&gt;
&lt;exactly one action line&gt;
</dl></pre>
<p>Conditions start with a leading `*&#8217;, everything after that character is passed on to the internal egrep <code>literally</code>, except for leading and trailing whitespace. These regular expressions are <code>completely</code> compatible to the normal <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) extended regular expressions. See also <code>Extended regular expressions</code>. </p>
<p> Conditions are anded; if there are no conditions the result will be true by default. </p>
<p> <i>Flags</i> can be any of the following:<br />
 Tp 0.5i <code>H</code> Egrep the header (default).<br />
 Tp <code>B</code> Egrep the body.<br />
 Tp <code>D</code> Tell the internal egrep to distinguish between upper and lower case (contrary to the default which is to ignore case).<br />
 Tp <code>A</code> This recipe will not be executed unless the conditions on the last preceding recipe (on the current block-nesting level) without the `A&#8217; or `a&#8217; flag matched as well. This allows you to chain actions that depend on a common condition.<br />
 Tp <code>a</code> Has the same meaning as the `A&#8217; flag, with the additional condition that the immediately preceding recipe must have been <i>successfully</i> completed before this recipe is executed.<br />
 Tp <code>E</code> This recipe only executes if the immediately preceding recipe was not executed. Execution of this recipe also disables any immediately following recipes with the &#8216;E&#8217; flag. This allows you to specify `else if&#8217; actions.<br />
 Tp <code>e</code> This recipe only executes if the immediately preceding recipe <i>failed</i> (i.e., the action line was attempted, but resulted in an error).<br />
 Tp <code>h</code> Feed the header to the pipe, file or mail destination (default).<br />
 Tp <code>b</code> Feed the body to the pipe, file or mail destination (default).<br />
 Tp <code>f</code> Consider the pipe as a filter.<br />
 Tp <code>c</code> Generate a <code>carbon copy</code> of this mail. This only makes sense on <i>delivering</i> recipes. The only non-delivering recipe this flag has an effect on is on a nesting block, in order to generate a carbon copy this will <code>clone</code> the running procmail process (lockfiles will not be inherited), whereby the clone will proceed as usual and the parent will jump across the block.<br />
 Tp <code>w</code> Wait for the filter or program to finish and check its exitcode (normally ignored); if the filter is unsuccessful, then the text will not have been filtered.<br />
 Tp <code>W</code> Has the same meaning as the `w&#8217; flag, but will suppress any `Program failure&#8217; message.<br />
 Tp <code>i</code> Ignore any write errors on this recipe (i.e., usually due to an early closed pipe).<br />
 Tp <code>r</code> Raw mode, do not try to ensure the mail ends with an empty line, write it out as is. </p>
<p> There are some special conditions you can use that are not straight regular expressions. To select them, the condition must start with:<br />
 Tp 0.5i <code>!</code> Invert the condition.<br />
 Tp <code>$</code> Evaluate the remainder of this condition according to <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) substitution rules inside double quotes, skip leading whitespace, then reparse it.<br />
 Tp <code>?</code> Use the exitcode of the specified program.<br />
 Tp <code>&lt;</code> Check if the total length of the mail is shorter than the specified (in decimal) number of bytes.<br />
 Tp <code>&gt;</code> Analogous to &#8216;&lt;&#8216;.<br />
 Tp <code>variablename </code><i>??</i> Match the remainder of this condition against the value of this environment variable (which cannot be a pseudo variable). A special case is if variablename is equal to `B&#8217;, `H&#8217;, `HB&#8217; or `BH&#8217;; this merely overrides the default header/body search area defined by the initial flags on this recipe.<br />
 Tp <code>\</code> To quote any of the above at the start of the line.</p>
<h3>Local lockfile</h3>
<p>If you put a second (trailing) &#8216;:&#8217; on the first recipe line, then procmail will use a <i>locallockfile</i> (for this recipe only). You can optionally specify the locallockfile to use; if you don&#8217;t however, procmail will use the destination filename (or the filename following the first &#8216;&gt;&gt;&#8217;) and will append $LOCKEXT to it.</p>
<h3>Recipe action line</h3>
<p>The action line can start with the following characters:<br />
 Tp <code>!</code> Forwards to all the specified mail addresses.<br />
 Tp <code>|</code> Starts the specified program, possibly in $SHELL if any of the characters $SHELLMETAS are spotted. You can optionally prepend this pipe symbol with <i>variable=</i>, which will cause stdout of the program to be captured in the environment <i>variable</i> (procmail will <code>not</code> terminate processing the rcfile at this point). If you specify just this pipe symbol, without any program, then procmail will pipe the mail to stdout.<br />
 Tp <code>{</code> Followed by at least one space, tab or newline will mark the start of a nesting block. Everything up till the next closing brace will depend on the conditions specified for this recipe. Unlimited nesting is permitted. The closing brace exists merely to delimit the block, it will <i>not</i> cause procmail to terminate in any way. If the end of a block is reached processing will continue as usual after the block. On a nesting block, the flags `H&#8217; and `B&#8217; only affect the conditions leading up to the block, the flags `h&#8217; and `b&#8217; have no effect whatsoever. </p>
<p> Anything else will be taken as a mailbox name (either a filename or a directory, absolute or relative to the current directory (see MAILDIR)). If it is a (possibly yet nonexistent) filename, the mail will be appended to it. </p>
<p> If it is a directory, the mail will be delivered to a newly created, guaranteed to be unique file named $MSGPREFIX* in the specified directory. If the mailbox name ends in &quot;/.&quot;, then this directory is presumed to be an MH folder; i.e., procmail will use the next number it finds available. If the mailbox name ends in &quot;/&quot;, then this directory is presumed to be a maildir folder; i.e., procmail will deliver the message to a file in a subdirectory named &quot;tmp&quot; and rename it to be inside a subdirectory named &quot;new&quot;. If the mailbox is specified to be an MH folder or maildir folder, procmail will create the necessary directories if they don&#8217;t exist, rather than treat the mailbox as a non-existent filename. When procmail is delivering to directories, you can specify multiple directories to deliver to (procmail will do so utilising hardlinks).</p>
<h3>Environment variable defaults</h3>
<p>Tp 2.2i <code>LOGNAME, HOME and SHELL</code> Your (the recipient&#8217;s) defaults<br />
 Tp <code>PATH</code> $HOME/bin :/usr/local/bin :/usr/bin :/bin (Except during the processing of an /etc/procmailrc file, when it will be set to `/usr/local/bin :/usr/bin :/bin&#8217;.)<br />
 Tp <code>SHELLMETAS</code> &amp; |&lt;&gt;~;?*[<br />
 Tp <code>SHELLFLAGS</code> -c<br />
 Tp <code>ORGMAIL</code> /var/mail/$LOGNAME<br />
 (Unless <code>-m</code> has been specified, in which case it is unset)<br />
 Tp <code>MAILDIR</code> $HOME<br />
 (Unless the name of the first successfully opened rcfile starts with `./&#8217; or if <code>-m</code> has been specified, in which case it defaults to `.&#8217;)<br />
 Tp <code>DEFAULT</code> $ORGMAIL<br />
 Tp <code>MSGPREFIX</code> msg.<br />
 Tp <code>SENDMAIL</code> /usr/sbin/sendmail<br />
 Tp <code>SENDMAILFLAGS</code> -oi<br />
 Tp <code>HOST</code> The current hostname<br />
 Tp <code>COMSAT</code> no<br />
 (If an rcfile is specified on the command line)<br />
 Tp <code>PROCMAIL_VERSION</code> 3.23pre<br />
 Tp <code>LOCKEXT</code> .lock </p>
<p> Other cleared or preset environment variables are IFS, ENV and PWD. </p>
<p> For security reasons, upon startup procmail will wipe out all environment variables that are suspected of modifying the behavior of the runtime linker.</p>
<h3>Environment</h3>
<p>Before you get lost in the multitude of environment variables, keep in mind that all of them have reasonable defaults.<br />
 Tp 1.2i <code>MAILDIR</code> Current directory while procmail is executing (that means that all paths are relative to $MAILDIR).<br />
 Tp <code>DEFAULT</code> Default <code>mailbox</code> file (if not told otherwise, procmail will dump mail in this mailbox). Procmail will automatically use $DEFAULT$LOCKEXT as lockfile prior to writing to this mailbox. You do not need to set this variable, since it already points to the standard system mailbox.<br />
 Tp <code>LOGFILE</code> This file will also contain any error or diagnostic messages from procmail (normally none :-) or any other programs started by procmail. If this file is not specified, any diagnostics or error messages will be mailed back to the sender. See also <code>LOGABSTRACT</code>.<br />
 Tp <code>VERBOSE</code> You can turn on <i>extended diagnostics</i> by setting this variable to `yes&#8217; or `on&#8217;, to turn it off again set it to `no&#8217; or `off&#8217;.<br />
 Tp <code>LOGABSTRACT</code> Just before procmail exits it logs an abstract of the delivered message in $LOGFILE showing the `From &#8216; and `Subject:&#8217; fields of the header, what folder it finally went to and how long (in bytes) the message was. By setting this variable to `no&#8217;, generation of this abstract is suppressed. If you set it to `all&#8217;, procmail will log an abstract for every successful <i>delivering recipe</i> it processes.<br />
 Tp <code>LOG</code> Anything assigned to this variable will be appended to $LOGFILE.<br />
 Tp <code>ORGMAIL</code> Usually the system mailbox (<code>OR</code>i<code>G</code>inal <code>MAIL</code>box). If, for some obscure reason (like `<code>filesystem full</code>&#8216;) the mail could not be delivered, then this mailbox will be the last resort. If procmail fails to save the mail in here (deep, deep trouble :-), then the mail will bounce back to the sender.<br />
 Tp <code>LOCKFILE</code> Global semaphore file. If this file already exists, procmail will wait until it has gone before proceeding, and will create it itself (cleaning it up when ready, of course). If more than one <i>lockfile</i> are specified, then the previous one will be removed before trying to create the new one. The use of a global lockfile is discouraged, whenever possible use locallockfiles (on a per recipe basis) instead.<br />
 Tp <code>LOCKEXT</code> Default extension that is appended to a destination file to determine what local <i>lockfile</i> to use (only if turned on, on a per-recipe basis).<br />
 Tp <code>LOCKSLEEP</code> Number of seconds procmail will sleep before retrying on a <i>lockfile</i> (if it already existed); if not specified, it defaults to 8 seconds.<br />
 Tp <code>LOCKTIMEOUT</code> Number of seconds that have to have passed since a <i>lockfile</i> was last modified/created before procmail decides that this must be an erroneously leftover lockfile that can be removed by force now. If zero, then no timeout will be used and procmail will wait forever until the lockfile is removed; if not specified, it defaults to 1024 seconds. This variable is useful to prevent indefinite hangups of <code>sendmail</code>/procmail. Procmail is immune to clock skew across machines.<br />
 Tp <code>TIMEOUT</code> Number of seconds that have to have passed before procmail decides that some child it started must be hanging. The offending program will receive a TERMINATE signal from procmail, and processing of the rcfile will continue. If zero, then no timeout will be used and procmail will wait forever until the child has terminated; if not specified, it defaults to 960 seconds.<br />
 Tp <code>MSGPREFIX</code> Filename prefix that is used when delivering to a directory (not used when delivering to a maildir or an MH directory).<br />
 Tp <code>HOST</code> If this is not the <i>hostname</i> of the machine, processing of the current <i>rcfile</i> will immediately cease. If other rcfiles were specified on the command line, processing will continue with the next one. If all rcfiles are exhausted, the program will terminate, but will not generate an error (i.e., to the mailer it will seem that the mail has been delivered).<br />
 Tp <code>UMASK</code> The name says it all (if it doesn&#8217;t, then forget about this one :-). Anything assigned to UMASK is taken as an <code>octal</code> number. If not specified, the umask defaults to 077. If the umask permits o+x, all the mailboxes procmail delivers to directly will receive an o+x mode change. This can be used to check if new mail arrived.<br />
 Tp <code>SHELLMETAS</code> If any of the characters in SHELLMETAS appears in the line specifying a filter or program, the line will be fed to $SHELL instead of being executed directly.<br />
 Tp <code>SHELLFLAGS</code> Any invocation of $SHELL will be like:<br />
 &quot;$SHELL&quot; &quot;$SHELLFLAGS&quot; &quot;$*&quot;;<br />
 Tp <code>SENDMAIL</code> If you&#8217;re not using the <i>forwarding</i> facility don&#8217;t worry about this one. It specifies the program being called to forward any mail.<br />
 It gets invoked as: &quot;$SENDMAIL&quot; $SENDMAILFLAGS &quot;$@&quot;;<br />
 Tp <code>NORESRETRY</code> Number of retries that are to be made if any `<code>process table full</code>&#8216;, `<code>file table full</code>&#8216;, `<code>out of memory</code>&#8216; or `<code>out of swap space</code>&#8216; error should occur. If this number is negative, then procmail will retry indefinitely; if not specified, it defaults to 4 times. The retries occur with a $SUSPEND second interval. The idea behind this is that if, e.g., the <i>swap</i> <i>space</i> has been exhausted or the <i>process</i> <i>table</i> is full, usually several other programs will either detect this as well and abort or crash 8-), thereby freeing valuable <i>resources</i> for procmail.<br />
 Tp <code>SUSPEND</code> Number of seconds that procmail will pause if it has to wait for something that is currently unavailable (memory, fork, etc.); if not specified, it will default to 16 seconds. See also: <code>LOCKSLEEP</code>.<br />
 Tp <code>LINEBUF</code> Length of the internal line buffers, cannot be set smaller than 128. All lines read from the <i>rcfile</i> should not exceed $LINEBUF characters before and after expansion. If not specified, it defaults to 2048. This limit, of course, does <i>not</i> apply to the mail itself, which can have arbitrary line lengths, or could be a binary file for that matter. See also PROCMAIL_OVERFLOW.<br />
 Tp <code>DELIVERED</code> If set to `yes&#8217; procmail will pretend (to the mail agent) the mail has been delivered. If mail cannot be delivered after having met this assignment (set to `yes&#8217;), the mail will be lost (i.e., it will not bounce).<br />
 Tp <code>TRAP</code> When procmail terminates of its own accord and not because it received a signal, it will execute the contents of this variable. A copy of the mail can be read from stdin. Any output produced by this command will be appended to $LOGFILE. Possible uses for TRAP are: removal of temporary files, logging customised abstracts, etc. See also <code>EXITCODE</code> and <code>LOGABSTRACT</code>.<br />
 Tp <code>EXITCODE</code> By default, procmail returns an exitcode of zero (success) if it successfully delivered the message or if the <code>HOST</code> variable was misset and there were no more rcfiles on the command line; otherwise it returns failure. Before doing so, procmail examines the value of this variable. If it is set to a positive numeric value, procmail will instead use that value as its exitcode. If this variable is set but empty and <code>TRAP</code> is set, procmail will set the exitcode to whatever the <code>TRAP</code> program returns. If this variable is not set, procmail will set it shortly before calling up the <code>TRAP</code> program.<br />
 Tp <code>LASTFOLDER</code> This variable is assigned to by procmail whenever it is delivering to a folder or program. It always contains the name of the last file (or program) procmail delivered to. If the last delivery was to several directory folders together then $LASTFOLDER will contain the hardlinked filenames as a space separated list.<br />
 Tp <code>MATCH</code> This variable is assigned to by procmail whenever it is told to extract text from a matching regular expression. It will contain all text matching the regular expression past the `<code>\/</code>&#8216; token.<br />
 Tp <code>SHIFT</code> Assigning a positive value to this variable has the same effect as the `shift&#8217; command in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1). This command is most useful to extract extra arguments passed to procmail when acting as a generic mailfilter.<br />
 Tp <code>INCLUDERC</code> Names an rcfile (relative to the current directory) which will be included here as if it were part of the current rcfile. Nesting is permitted and only limited by systems resources (memory and file descriptors). As no checking is done on the permissions or ownership of the rcfile, users of <code>INCLUDERC</code> should make sure that only trusted users have write access to the included rcfile or the directory it is in. Command line assignments to <code>INCLUDERC</code> have no effect.<br />
 Tp <code>SWITCHRC</code> Names an rcfile (relative to the current directory) to which processing will be switched. If the named rcfile doesn&#8217;t exist or is not a normal file or /dev/null then an error will be logged and processing will continue in the current rcfile. Otherwise, processing of the current rcfile will be aborted and the named rcfile started. Unsetting <code>SWITCHRC</code> aborts processing of the current rcfile as if it had ended at the assignment. As with <code>INCLUDERC</code>, no checking is done on the permissions or ownership of the rcfile and command line assignments have no effect.<br />
 Tp <code>PROCMAIL_VERSION</code> The version number of the running procmail binary.<br />
 Tp <code>PROCMAIL_OVERFLOW</code> This variable will be set to a non-empty value if procmail detects a buffer overflow. See the <code>BUGS</code> section below for other details of operation when overflow occurs.<br />
 Tp <code>COMSAT</code> <code><a href="/docs/linux/man/8-comsat/">Comsat</a></code>(8)/<code><a href="/docs/linux/man/1-biff/">biff</a></code>(1) notification is on by default, it can be turned off by setting this variable to `no&#8217;. Alternatively the biff-service can be customised by setting it to either `service@&#8217;, `@hostname&#8217;, or `service [at] hostname&#8217;. When not specified it defaults to biff [at] localhost.<br />
 Tp <code>DROPPRIVS</code> If set to `yes&#8217; procmail will drop all privileges it might have had (suid or sgid). This is only useful if you want to guarantee that the bottom half of the /etc/procmailrc file is executed on behalf of the recipient.</p>
<h3>Extended regular expressions</h3>
<p>The following tokens are known to both the procmail internal egrep and the standard <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) (beware that some egrep implementations include other non-standard extensions; in particular, the repetition operator <code>{</code> is not supported by procmail&#8217;s egrep):<br />
 Tp 1.0i <code>^</code> Start of a line.<br />
 Tp <code>$</code> End of a line.<br />
 Tp <code>.</code> Any character except a newline.<br />
 Tp <code>a*</code> Any sequence of zero or more a&#8217;s.<br />
 Tp <code>a+</code> Any sequence of one or more a&#8217;s.<br />
 Tp <code>a?</code> Either zero or one a.<br />
 Tp <code>[^-a-d]</code> Any character which is <code>not</code> either a dash, a, b, c, d or newline.<br />
 Tp <code>de|abc</code> Either the sequence `de&#8217; or `abc&#8217;.<br />
 Tp <code>(abc)*</code> Zero or more times the sequence `abc&#8217;.<br />
 Tp <code>\.</code> Matches a single dot; use \ to quote any of the magic characters to get rid of their special meaning. See also $\ variable substitution. </p>
<p> These were only samples, of course, any more complex combination is valid as well. </p>
<p> The following token meanings are special procmail extensions:<br />
 Tp 1.0i <code>^</code> or <code>$</code> Match a newline (for multiline matches).<br />
 Tp <code>^^</code> Anchor the expression at the very start of the search area, or if encountered at the end of the expression, anchor it at the very end of the search area.<br />
 Tp <code>\&lt;</code> or <code>\&gt;</code> Match the character before or after a word. They are merely a shorthand for `[^a-zA-Z0-9_]&#8217;, but can also match newlines. Since they match actual characters, they are only suitable to delimit words, not to delimit inter-word space.<br />
 Tp <code>\/</code> Splits the expression in two parts. Everything matching the right part will be assigned to the MATCH environment variable.</p>
<h2>Examples</h2>
<p>Look in the <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5) man page.</p>
<h2>Caveats</h2>
<p>Continued lines in an action line that specifies a program always have to end in a backslash, even if the underlying shell would not need or want the backslash to indicate continuation. This is due to the two pass parsing process needed (first procmail, then the shell (or not, depending on <code>SHELLMETAS</code>)). </p>
<p> Don&#8217;t put comments on the regular expression condition lines in a recipe, these lines are fed to the internal egrep <i>literally</i> (except for continuation backslashes at the end of a line). </p>
<p> Leading whitespace on continued regular expression condition lines is usually ignored (so that they can be indented), but <code>not</code> on continued condition lines that are evaluated according to the <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) substitution rules inside double quotes. </p>
<p> Watch out for deadlocks when doing unhealthy things like forwarding mail to your own account. Deadlocks can be broken by proper use of <code>LOCKTIMEOUT</code>. </p>
<p> Any default values that procmail has for some environment variables will <code>always</code> override the ones that were already defined. If you really want to override the defaults, you either have to put them in the <code>rcfile</code> or on the command line as arguments. </p>
<p> The /etc/procmailrc file cannot change the PATH setting seen by user rcfiles as the value is reset when procmail finishes the /etc/procmailrc file. While future enhancements are expected in this area, recompiling procmail with the desired value is currently the only correct solution. </p>
<p> Environment variables set <code>inside</code> the shell-interpreted-`|&#8217; action part of a recipe will <code>not</code> retain their value after the recipe has finished since they are set in a subshell of procmail. To make sure the value of an environment variable is retained you have to put the assignment to the variable before the leading `|&#8217; of a recipe, so that it can capture stdout of the program. </p>
<p> If you specify only a `h&#8217; or a `b&#8217; flag on a delivering recipe, and the recipe matches, then, unless the `c&#8217; flag is present as well, the body respectively the header of the mail will be silently lost.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1), <code><a href="/docs/linux/man/5-procmailsc/">procmailsc</a></code>(5), <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/1-mailx/">mailx</a></code>(1), <code><a href="/docs/linux/man/1-uucp/">uucp</a></code>(1), <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/5-regexp/">regexp</a></code>(5), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/1-biff/">biff</a></code>(1), <code><a href="/docs/linux/man/8-comsat/">comsat</a></code>(8), <code><a href="/docs/linux/man/1-lockfile/">lockfile</a></code>(1), <code><a href="/docs/linux/man/1-formail/">formail</a></code>(1)</p>
<h2>Bugs</h2>
<p>The only substitutions of environment variables that can be handled by procmail itself are of the type $name, ${name}, ${name:-text}, ${name:+text}, ${name-text}, ${name+text}, $
ame, $#, $n, $$, $?, $_, $- and $=; whereby $
ame will be substituted by the all-magic-regular-expression-characters-disarmed equivalent of $name, $_ by the name of the current rcfile, $- by $LASTFOLDER and $= will contain the score of the last recipe. Furthermore, the result of $
ame substitution will never be split on whitespace. When the <code>-a</code> or <code>-m</code> options are used, $# will expand to the number of arguments so specified and &quot;$@&quot; (the quotes are required) will expand to the specified arguments. However, &quot;$@&quot; will only be expanded when used in the argument list to a program, and then only one such occurrence will be expanded. </p>
<p> Unquoted variable expansions performed by procmail are always split on space, tab, and newline characters; the IFS variable is not used internally. </p>
<p> Procmail does not support the expansion of `~&#8217;. </p>
<p> A line buffer of length $LINEBUF is used when processing the <i>rcfile</i>, any expansions that don&#8217;t fit within this limit will be truncated and PROCMAIL_OVERFLOW will be set. If the overflowing line is a condition or an action line, then it will be considered failed and procmail will continue processing. If it is a variable assignment or recipe start line then procmail will abort the entire rcfile. </p>
<p> If the global lockfile has a <i>relative</i> path, and the current directory is not the same as when the global lockfile was created, then the global lockfile will not be removed if procmail exits at that point (remedy: use <i>absolute</i> paths to specify global lockfiles). </p>
<p> If an rcfile has a <i>relative</i> path and when the rcfile is first opened <code>MAILDIR</code> contains a relative path, and if at one point procmail is instructed to clone itself and the current directory has changed since the rcfile was opened, then procmail will not be able to clone itself (remedy: use an <i>absolute</i> path to reference the rcfile or make sure MAILDIR contains an absolute path as the rcfile is opened). </p>
<p> A locallockfile on the recipe that marks the start of a non-forking nested block does not work as expected. </p>
<p> When capturing stdout from a recipe into an environment variable, exactly one trailing newline will be stripped. </p>
<p> Some non-optimal and non-obvious regexps set MATCH to an incorrect value. The regexp can be made to work by removing one or more unneeded &#8216;*&#8217;, &#8216;+&#8217;, or &#8216;?&#8217; operator on the left-hand side of the \/ token.</p>
<h2>Miscellaneous</h2>
<p>If the regular expression contains `<code>^TO_</code>&#8216; it will be substituted by `<code>(^((Original-)?(Resent-)?(To |Cc |Bcc) |(X-Envelope |Apparently(-Resent)?)-To) :(.*[^-a-zA-Z0-9_.])?)</code>&#8216;, which should catch all destination specifications containing a specific <i>address</i>. </p>
<p> If the regular expression contains `<code>^TO</code>&#8216; it will be substituted by `<code>(^((Original-)?(Resent-)?(To |Cc |Bcc) |(X-Envelope |Apparently(-Resent)?)-To) :(.*[^a-zA-Z])?)</code>&#8216;, which should catch all destination specifications containing a specific <i>word</i>. </p>
<p> If the regular expression contains `<code>^FROM_DAEMON</code>&#8216; it will be substituted by `<code>(^(Mailing-List : |Precedence :.*(junk |bulk |list) |To : Multiple recipients of |(((Resent-)?(From |Sender) |X-Envelope-From) : |&gt;?From )([^&gt;]*[^(.% [at] a-z0-9])?(Post(ma?(st(e?r)? |n) |office) |(send)?Mail(er)? |daemon |m(mdf |ajordomo) |n?uucp |LIST(SERV |proc) |NETSERV |o(wner |ps) |r(e(quest |sponse) |oot) |b(ounce |bs\.smtp) |echo |mirror |s(erv(ices? |er) |mtp(error)? |ystem) |A(dmin(istrator)? |MMGR |utoanswer))(([^).! :a-z0-9][-_a-z0-9]*)?[%@&gt;	 ][^&lt;)]*(\(.*\).*)?)?$([^&gt;] |$)))</code>&#8216;, which should catch mails coming from most daemons (how&#8217;s that for a regular expression :-). </p>
<p> If the regular expression contains `<code>^FROM_MAILER</code>&#8216; it will be substituted by `<code>(^(((Resent-)?(From |Sender) |X-Envelope-From) : |&gt;?From )([^&gt;]*[^(.% [at] a-z0-9])?(Post(ma(st(er)? |n) |office) |(send)?Mail(er)? |daemon |mmdf |n?uucp |ops |r(esponse |oot) |(bbs\.)?smtp(error)? |s(erv(ices? |er) |ystem) |A(dmin(istrator)? |MMGR))(([^).! :a-z0-9][-_a-z0-9]*)?[%@&gt;	 ][^&lt;)]*(\(.*\).*)?)?$([^&gt;] |$))</code>&#8216; (a stripped down version of `<code>^FROM_DAEMON</code>&#8216;), which should catch mails coming from most mailer-daemons. </p>
<p> When assigning boolean values to variables like VERBOSE, DELIVERED or COMSAT, procmail accepts as true every string starting with: a non-zero value, `on&#8217;, `y&#8217;, `t&#8217; or `e&#8217;. False is every string starting with: a zero value, `off&#8217;, `n&#8217;, `f&#8217; or `d&#8217;. </p>
<p> If the action line of a recipe specifies a program, a sole backslash-newline pair in it on an otherwise empty line will be converted into a newline. </p>
<p> The regular expression engine built into procmail does not support named character classes.</p>
<h2>Notes</h2>
<p>Since unquoted leading whitespace is generally ignored in the rcfile you can indent everything to taste. </p>
<p> The leading `|&#8217; on the action line to specify a program or filter is stripped before checking for $SHELLMETAS. </p>
<p> Files included with the INCLUDERC directive containing only environment variable assignments can be shared with sh. </p>
<p> The current behavior of assignments on the command line to <code>INCLUDERC</code> and <code>SWITCHRC</code> is not guaranteed, has been changed once already, and may be changed again or removed in future releases. </p>
<p> For <i>really</i> complicated processing you can even consider calling <code>procmail</code> recursively. </p>
<p> In the old days, the `:0&#8242; that marks the beginning of a recipe, had to be changed to `:n&#8217;, whereby `n&#8217; denotes the number of conditions that follow.</p>
<h2>Authors</h2>
<p>Stephen R. van den Berg </p>
<pre><dl><dt><dd>&lt;srb [at] cuci.nl&gt;
</dl></pre>
<p>Philip A. Guenther </p>
<pre><dl><dt><dd>&lt;guenther [at] sendmail.com&gt;
</dl></pre>
