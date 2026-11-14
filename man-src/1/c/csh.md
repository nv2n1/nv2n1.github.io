---
title: "csh(1)"
name: "csh"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csh/"
description: "csh – a shell (command interpreter) with C-like syntax"
---

<h2 class="name">NAME</h2>
<p> <code>csh</code> &#8211; a shell (command interpreter) with C-like syntax </p>
<h2>SYNOPSIS</h2>
<p> <code>csh</code> [-<code>bcefimnstVvXx </code>[<i>argument &#8230;</i> ] ]<br />
<code>csh</code> [-<code>l</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>csh</code> is a command language interpreter incorporating a history mechanism (see Sx History substitutions ) , job control facilities (see Sx Jobs ) , interactive file name and user name completion (see Sx File name completion ) , and a C-like syntax. It is used both as an interactive login shell and a shell script command processor.</p>
<h3>Argument list processing</h3>
<p> If the first argument (argument 0) to the shell is a dash (`-&#8216; ) then this is a login shell. A login shell also can be specified by invoking the shell with the &#8211;<code>l</code> flag as the only argument. </p>
<p> The rest of the flag arguments are interpreted as follows:</p>
<dl>
<dt><code>-b</code></p>
<dd> This flag forces a &#8220;break&#8221; from option processing, causing any further shell arguments to be treated as non-option arguments. The remaining arguments will not be interpreted as shell options. This may be used to pass options to a shell script without confusion or possible subterfuge. The shell will not run a set-user-ID script without this option.</p>
<dt><code>-c</code></p>
<dd> Commands are read from the (single) following argument which must be present. Any remaining arguments are placed in <i>argv</i></p>
<dt><code>-e</code></p>
<dd> The shell exits if any invoked command terminates abnormally or yields a non-zero exit status.</p>
<dt><code>-f</code></p>
<dd> The shell will start faster, because it will neither search for nor execute commands from the file .cshrc in the invoker&#8217;s home directory. Note: if the environment variable <code>HOME</code> is not set, fast startup is the default.</p>
<dt><code>-i</code></p>
<dd> The shell is interactive and prompts for its top-level input, even if it appears not to be a terminal. Shells are interactive without this option if their inputs and outputs are terminals.</p>
<dt><code>-l</code></p>
<dd> The shell is a login shell (only applicable if &#8211;<code>l</code> is the only flag specified).</p>
<dt><code>-m</code></p>
<dd> Read .cshrc regardless of its owner and group. This option is dangerous and should only be used by <a href="/docs/linux/man/1-su/">su</a>(1).</p>
<dt><code>-n</code></p>
<dd> Commands are parsed, but not executed. This aids in syntactic checking of shell scripts. When used interactively, the shell can be terminated by pressing control-D (end-of-file character), since <code>exit</code> will not work.</p>
<dt><code>-s</code></p>
<dd> Command input is taken from the standard input.</p>
<dt><code>-t</code></p>
<dd> A single line of input is read and executed. A backslash (`\&#8217; ) may be used to escape the newline at the end of this line and continue onto another line.</p>
<dt><code>-V</code></p>
<dd> Causes the <i>verbose</i> variable to be set even before .cshrc is executed.</p>
<dt><code>-v</code></p>
<dd> Causes the <i>verbose</i> variable to be set, with the effect that command input is echoed after history substitution.</p>
<dt><code>-X</code></p>
<dd> Causes the <i>echo</i> variable to be set even before .cshrc is executed.</p>
<dt><code>-x</code></p>
<dd> Causes the <i>echo</i> variable to be set, so that commands are echoed immediately before execution.</dl>
<p> After processing of flag arguments, if arguments remain but none of the &#8211;<code>c</code> &#8211;<code>i</code> &#8211;<code>s</code> or &#8211;<code>t</code> options were given, the first argument is taken as the name of a file of commands to be executed. The shell opens this file, and saves its name for possible resubstitution by `$0&#8242; Since many systems use either the standard version 6 or version 7 shells whose shell scripts are not compatible with this shell, the shell will execute such a &#8220;standard&#8221; shell if the first character of a script is not a hash mark (`#&#8217; ) i.e., if the script does not start with a comment. Remaining arguments initialize the variable <i>argv</i> </p>
<p> An instance of <code>csh</code> begins by executing commands from the file /etc/csh.cshrc and, if this is a login shell, /etc/csh.login It then executes commands from .cshrc in the home directory of the invoker, and, if this is a login shell, the file .login in the same location. It is typical for users on <code>CRT s</code> to put the command <code>stty crt</code> in their .login file, and to also invoke <a href="/docs/linux/man/1-tset/">tset</a>(1) there. </p>
<p> In the normal case, the shell will begin reading commands from the terminal, prompting with `%&#8217; Processing of arguments and the use of the shell to process files containing command scripts will be described later. </p>
<p> The shell repeatedly performs the following actions: a line of command input is read and broken into &#8220;words&#8221; This sequence of words is placed on the command history list and parsed. Finally each command in the current line is executed. </p>
<p> When a login shell terminates it executes commands from the files .logout in the user&#8217;s home directory and /etc/csh.logout</p>
<h3>Lexical structure</h3>
<p> The shell splits input lines into words at blanks and tabs with the following exceptions. The characters `&amp;&#8217; , `|&#8217; , `;&#8217; , `&lt;&#8216; , `&gt;&#8217; , `(&#8216; , and `)&#8217; form separate words. If doubled in `&amp;&amp;&#8217; , `||&#8217; , `&lt;&lt;&#8216; , or `&gt;&gt;&#8217; , these pairs form single words. These parser metacharacters may be made part of other words, or have their special meaning prevented, by preceding them with a backslash (`\&#8217; ) A newline preceded by a `\&#8217; is equivalent to a blank. </p>
<p> Strings enclosed in matched pairs of quotations, `&#8221; , &#8220;&#8217; , or `&#8217; , form parts of a word; metacharacters in these strings, including blanks and tabs, do not form separate words. These quotations have semantics to be described later. Within pairs of `&#8221; or `&#8217; characters, a newline preceded by a `\&#8217; gives a true newline character. </p>
<p> When the shell&#8217;s input is not a terminal, the character `#&#8217; introduces a comment that continues to the end of the input line. This special meaning is prevented when preceded by `\&#8217; and in quotations using &#8220;&#8217; , `&#8221; , and `&#8217;</p>
<h3>Commands</h3>
<p> A simple command is a sequence of words, the first of which specifies the command to be executed. A simple command or a sequence of simple commands separated by `|&#8217; characters forms a pipeline. The output of each command in a pipeline is connected to the input of the next. Sequences of pipelines may be separated by `;&#8217; , and are then executed sequentially. A sequence of pipelines may be executed without immediately waiting for it to terminate by following it with a `&amp;&#8217; </p>
<p> Any of the above may be placed in `(&#8216; `)&#8217; to form a simple command (that may be a component of a pipeline, for example). It is also possible to separate pipelines with `||&#8217; or `&amp;&amp;&#8217; showing, as in the C language, that the second is to be executed only if the first fails or succeeds, respectively. (See <i>Expressions .</i></p>
<h3>Jobs</h3>
<p> The shell associates a <i>job</i> with each pipeline. It keeps a table of current jobs, printed by the <code>jobs</code> command, and assigns them small integer numbers. When a job is started asynchronously with `&amp;&#8217; , the shell prints a line that looks like: </p>
<blockquote><p> [1] 1234 </p></blockquote>
<p> showing that the job which was started asynchronously was job number 1 and had one (top-level) process, whose process ID was 1234. </p>
<p> If you are running a job and wish to do something else you may hit <code>^Z</code> (control-Z), which sends a <code>SIGSTOP</code> signal to the current job. The shell will then normally show that the job has been &#8220;Stopped&#8221; and print another prompt. You can then manipulate the state of this job, putting it in the <i>background</i> with the <code>bg</code> command, or run some other commands and eventually bring the job back into the <i>foreground</i> with the <code>fg</code> command. A <code>^Z</code> takes effect immediately and is like an interrupt in that pending output and unread input are discarded when it is typed. There is another special key <code>^Y</code> that does not generate a <code>SIGSTOP</code> signal until a program attempts to <a href="/docs/linux/man/2-read/">read</a>(2) it. This request can usefully be typed ahead when you have prepared some commands for a job that you wish to stop after it has read them. </p>
<p> A job being run in the background will stop if it tries to read from the terminal. Background jobs are normally allowed to produce output, but this can be disabled by giving the command <code>stty tostop</code> If you set this tty option, then background jobs will stop when they try to produce output like they do when they try to read input. </p>
<p> There are several ways to refer to jobs in the shell. The character `%&#8217; introduces a job name. If you wish to refer to job number 1, you can name it as `%1&#8242; Just naming a job brings it to the foreground; thus <code>%1</code> is a synonym for <code>fg %1</code> bringing job number 1 back into the foreground. Similarly, saying <code>%1</code> resumes job number 1 in the background. Jobs can also be named by prefixes of the string typed in to start them, if these prefixes are unambiguous; thus <code>%ex</code> would normally restart a suspended <a href="/docs/linux/man/1-ex/">ex</a>(1) job, if there were only one suspended job whose name began with the string Qq ex . It is also possible to say <code>%?string</code> which specifies a job whose text contains <i>string</i> if there is only one such job. </p>
<p> The shell maintains a notion of the current and previous jobs. In output about jobs, the current job is marked with a `+&#8217; and the previous job with a `-&#8216; The abbreviation `%+&#8217; refers to the current job and `%-&#8216; refers to the previous job. For close analogy with the syntax of the <code>history</code> mechanism (described below), `%%&#8217; is also a synonym for the current job. </p>
<p> The job control mechanism requires that the <a href="/docs/linux/man/1-stty/">stty</a>(1) option <code>new</code> be set. It is an artifact from a <i>new</i> implementation of the tty driver that allows generation of interrupt characters from the keyboard to tell jobs to stop. See <a href="/docs/linux/man/1-stty/">stty</a>(1) for details on setting options in the new tty driver.</p>
<h3>Status reporting</h3>
<p> The shell learns immediately whenever a process changes state. It normally informs you whenever a job becomes blocked so that no further progress is possible, but only just before it prints a prompt. This is done so that it does not otherwise disturb your work. If, however, you set the shell variable <i>notify</i> the shell will notify you immediately of changes of status in background jobs. There is also a shell command <code>notify</code> that marks a single process so that its status changes will be immediately reported. By default <code>notify</code> marks the current process; simply say <code>notify</code> after starting a background job to mark it. </p>
<p> When you try to leave the shell while jobs are stopped, you will be warned that &#8220;You have stopped jobs&#8221; You may use the <code>jobs</code> command to see what they are. If you try to exit again immediately, the shell will not warn you a second time, and the suspended jobs will be terminated.</p>
<h3>File name completion</h3>
<p> When the file name completion feature is enabled by setting the shell variable <i>filec</i> (see <code>set )</code> <code>csh</code> will interactively complete file names and user names from unique prefixes when they are input from the terminal followed by the escape character (the escape key, or control-[). For example, if the current directory looks like </p>
<blockquote>
<pre>
DSC.OLD  bin      cmd      lib      xmpl.c
DSC.NEW  chaosnet cmtest   mail     xmpl.o
bench    class    dev      mbox     xmpl.out
</pre>
</blockquote>
<p> and the input is </p>
<blockquote><p><tt>% vi ch&lt;escape&gt;</tt></p></blockquote>
<p> <code>csh</code> will complete the prefix &#8220;ch&#8221; to the only matching file name &#8220;chaosnet&#8221; changing the input line to </p>
<blockquote><p><tt>% vi chaosnet</tt></p></blockquote>
<p> However, given </p>
<blockquote><p><tt>% vi D&lt;escape&gt;</tt></p></blockquote>
<p> <code>csh</code> will only expand the input to </p>
<blockquote><p><tt>% vi DSC.</tt></p></blockquote>
<p> and will sound the terminal bell to indicate that the expansion is incomplete, since there are two file names matching the prefix `D&#8217; </p>
<p> If a partial file name is followed by the end-of-file character (usually control-D), then, instead of completing the name, <code>csh</code> will list all file names matching the prefix. For example, the input </p>
<blockquote><p><tt>% vi D&lt;control-D&gt;</tt></p></blockquote>
<p> causes all files beginning with `D&#8217; to be listed: </p>
<blockquote><p><tt>DSC.NEW<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>DSC.OLD</tt></p></blockquote>
<p> while the input line remains unchanged.</p>
<p> The same system of escape and end-of-file can also be used to expand partial user names, if the word to be completed (or listed) begins with the tilde character (`~&#8217; ) For example, typing </p>
<blockquote><p><tt>cd ~ro&lt;escape&gt;</tt></p></blockquote>
<p> may produce the expansion </p>
<blockquote><p><tt>cd ~root</tt></p></blockquote>
<p> The use of the terminal bell to signal errors or multiple matches can be inhibited by setting the variable <i>nobeep</i> </p>
<p> Normally, all files in the particular directory are candidates for name completion. Files with certain suffixes can be excluded from consideration by setting the variable <i>fignore</i> to the list of suffixes to be ignored. Thus, if <i>fignore</i> is set by the command </p>
<blockquote><p><tt>% set fignore = (.o .out)</tt></p></blockquote>
<p> then typing </p>
<blockquote><p><tt>% vi x&lt;escape&gt;</tt></p></blockquote>
<p> would result in the completion to </p>
<blockquote><p><tt>% vi xmpl.c</tt></p></blockquote>
<p> ignoring the files Qq xmpl.o and Qq xmpl.out . However, if the only completion possible requires not ignoring these suffixes, then they are not ignored. In addition, <i>fignore</i> does not affect the listing of file names by control-D. All files are listed regardless of their suffixes.</p>
<h3>Substitutions</h3>
<p> We now describe the various transformations the shell performs on the input in the order in which they occur.</p>
<h3>History substitutions</h3>
<p> History substitutions place words from previous command input as portions of new commands, making it easy to repeat commands, repeat arguments of a previous command in the current command, or fix spelling mistakes in the previous command with little typing and a high degree of confidence. History substitutions begin with the character `!&#8217; and may begin <i>anywhere</i> in the input stream (with the proviso that they do <i>not</i> nest). This `!&#8217; may be preceded by a `\&#8217; to prevent its special meaning; for convenience, a `!&#8217; character is passed unchanged when it is followed by a blank, tab, newline, `=&#8217; or `(&#8216; (History substitutions also occur when an input line begins with `^&#8217; This special abbreviation will be described later.) Any input line that contains history substitution is echoed on the terminal before it is executed as it would have been typed without history substitution. </p>
<p> Commands input from the terminal that consist of one or more words are saved on the history list. The history substitutions reintroduce sequences of words from these saved commands into the input stream. The size of the history list is controlled by the <i>history</i> variable; the previous command is always retained, regardless of the value of the history variable. Commands are numbered sequentially from 1. </p>
<p> For definiteness, consider the following output from the <code>history</code> command: </p>
<blockquote>
<pre>
09  write michael
10  ex write.c
11  cat oldwrite.c
12  diff *write.c
</pre>
</blockquote>
<p> The commands are shown with their event numbers. It is not usually necessary to use event numbers, but the current event number can be made part of the prompt by placing a `!&#8217; in the prompt string. </p>
<p> With the current event 13 we can refer to previous events by event number `!11&#8242; , relatively as in `!-2&#8242; (referring to the same event), by a prefix of a command word as in `!d&#8217; for event 12 or `!wri&#8217; for event 9, or by a string contained in a word in the command as in `!?mic?&#8217; also referring to event 9. These forms, without further change, simply reintroduce the words of the specified events, each separated by a single blank. As a special case, `!!&#8217; refers to the previous command; thus `!!&#8217; alone is a <i>redo</i> </p>
<p> To select words from an event we can follow the event specification by a `:&#8217; and a designator for the desired words. The words of an input line are numbered from 0, the first (usually command) word being 0, the second word (first argument) being 1, etc. The basic word designators are: </p>
<dl>
<dt><code>0</code></p>
<dd> first (command) word</p>
<dt><i>n</i></p>
<dd> <i>n </i><code>&#8216;th</code> argument</p>
<dt><code>^</code></p>
<dd> first argument; i.e., `1&#8242;</p>
<dt><code>$</code></p>
<dd> last argument</p>
<dt><code>%</code></p>
<dd> word matched by (immediately preceding) <code>? </code><i>s </i><code>?</code> search</p>
<dt><i>x-y</i></p>
<dd> range of words</p>
<dt><i>-y</i></p>
<dd> abbreviates `0-y&#8217;</p>
<dt><code>*</code></p>
<dd> abbreviates `^-$&#8217; , or nothing if only 1 word in event</p>
<dt><i>x*</i></p>
<dd> abbreviates `x-$&#8217;</p>
<dt><i>x-</i></p>
<dd> like `x*&#8217; but omitting word `$&#8217;</dl>
<p> The `:&#8217; separating the event specification from the word designator can be omitted if the argument selector begins with a `^&#8217; , `$&#8217; , `*&#8217; , `-&#8216; , or `%&#8217; After the optional word designator, a sequence of modifiers can be placed, each preceded by a `:&#8217; The following modifiers are defined: </p>
<dl>
<dt><code>h</code></p>
<dd> Remove a trailing pathname component, leaving the head.</p>
<dt><code>r</code></p>
<dd> Remove a trailing `.xxx&#8217; component, leaving the root name.</p>
<dt><code>e</code></p>
<dd> Remove all but the extension `.xxx&#8217; part.</p>
<dt><code>s </code><i>/l/r/</i></p>
<dd> Substitute <i>l</i> for <i>r</i></p>
<dt><code>t</code></p>
<dd> Remove all leading pathname components, leaving the tail.</p>
<dt><code>&amp;</code></p>
<dd> Repeat the previous substitution.</p>
<dt><code>g</code></p>
<dd> Apply the change once on each word, prefixing the above; e.g., `g&amp;&#8217;</p>
<dt><code>a</code></p>
<dd> Apply the change as many times as possible on a single word, prefixing the above. It can be used together with `g&#8217; to apply a substitution globally.</p>
<dt><code>p</code></p>
<dd> Print the new command line but do not execute it.</p>
<dt><code>q</code></p>
<dd> Quote the substituted words, preventing further substitutions.</p>
<dt><code>x</code></p>
<dd> Like `q&#8217; , but break into words at blanks, tabs, and newlines.</dl>
<p> Unless preceded by a `g&#8217; the change is applied only to the first modifiable word. With substitutions, it is an error for no word to be applicable. </p>
<p> The left-hand side of substitutions are not regular expressions in the sense of the editors, but instead strings. Any character may be used as the delimiter in place of `/&#8217; ; a `\&#8217; quotes the delimiter into the <i>l </i> and <i>r </i> strings. The character `&amp;&#8217; in the right-hand side is replaced by the text from the left. A `\&#8217; also quotes `&amp;&#8217; A <code>NULL</code> <i>l</i> (`//&#8217; ) uses the previous string either from an <i>l</i> or from a contextual scan string <i>s</i> in `!?&#8217; Ns Ar s Ns \? . The trailing delimiter in the substitution may be omitted if a newline follows immediately as may the trailing `?&#8217; in a contextual scan. </p>
<p> A history reference may be given without an event specification; e.g., `!$&#8217; Here, the reference is to the previous command unless a previous history reference occurred on the same line in which case this form repeats the previous reference. Thus &#8220;!?foo?^ !$&#8221; gives the first and last arguments from the command matching &#8220;?foo?&#8221; </p>
<p> A special abbreviation of a history reference occurs when the first non-blank character of an input line is a `^&#8217; This is equivalent to &#8220;!:s^&#8221; providing a convenient shorthand for substitutions on the text of the previous line. Thus <code>^lb^lib</code> fixes the spelling of &#8220;lib&#8221; in the previous command. Finally, a history substitution may be surrounded with `{&#8216; and `}&#8217; if necessary to insulate it from the characters that follow. Thus, after <code>ls -ld ~paul</code> we might do <code>!{l}a</code> to do <code>ls -ld ~paula</code> while <code>!la</code> would look for a command starting with &#8220;la&#8221;</p>
<h3>Quotations with &#8216; and</h3>
<p> The quotation of strings by `&#8221; and `&#8217; can be used to prevent all or some of the remaining substitutions. Strings enclosed in `&#8221; are prevented from any further interpretation. Strings enclosed in `&#8217; may be expanded as described below. </p>
<p> In both cases the resulting text becomes (all or part of) a single word; only in one special case (see <i>Command Substitution</i> below) does a `&#8217; quoted string yield parts of more than one word; `&#8221; quoted strings never do.</p>
<h3>Alias substitution</h3>
<p> The shell maintains a list of aliases that can be established, displayed and modified by the <code>alias</code> and <code>unalias</code> commands. After a command line is scanned, it is parsed into distinct commands and the first word of each command, left-to-right, is checked to see if it has an alias. If it does, then the text that is the alias for that command is reread with the history mechanism available as though that command were the previous input line. The resulting words replace the command and argument list. If no reference is made to the history list, then the argument list is left unchanged. </p>
<p> Thus if the alias for &#8220;ls&#8221; is &#8220;ls -l&#8221; the command <code>ls /usr</code> would map to <code>ls -l /usr</code> the argument list here being undisturbed. Similarly, if the alias for &#8220;lookup&#8221; was &#8220;grep !^ /etc/passwd&#8221; then <code>lookup bill</code> would map to <code>grep bill /etc/passwd</code> </p>
<p> If an alias is found, the word transformation of the input text is performed and the aliasing process begins again on the reformed input line. Looping is prevented if the first word of the new text is the same as the old by flagging it to prevent further aliasing. Other loops are detected and cause an error. </p>
<p> Note that the mechanism allows aliases to introduce parser metasyntax. Thus, we can <code>alias print &#8216;pr \!* | lpr&#8217;</code> to make a command that <code>pr &#8216;s</code> its arguments to the line printer.</p>
<h3>Variable substitution</h3>
<p> The shell maintains a set of variables, each of which has as value a list of zero or more words. Some of these variables are set by the shell or referred to by it. For instance, the <i>argv</i> variable is an image of the shell&#8217;s argument list, and words of this variable&#8217;s value are referred to in special ways. </p>
<p> The values of variables may be displayed and changed by using the <code>set</code> and <code>unset</code> commands. Of the variables referred to by the shell a number are toggles; the shell does not care what their value is, only whether they are set or not. For instance, the <i>verbose</i> variable is a toggle that causes command input to be echoed. The setting of this variable results from the &#8211;<code>v</code> command-line option. </p>
<p> Other operations treat variables numerically. The <code>@</code> command permits numeric calculations to be performed and the result assigned to a variable. Variable values are, however, always represented as (zero or more) strings. For the purposes of numeric operations, the null string is considered to be zero, and the second and additional words of multiword values are ignored. </p>
<p> After the input line is aliased and parsed, and before each command is executed, variable substitution is performed, keyed by `$&#8217; characters. This expansion can be prevented by preceding the `$&#8217; with a `\&#8217; except within double quotes (`&quot;&#8217;), where it <i>always</i> occurs, and within single quotes (`&#8221;), where it <i>never</i> occurs. Strings quoted by backticks (`) are interpreted later (see Sx Command substitution below), so `$&#8217; substitution does not occur there until later, if at all. A `$&#8217; is passed unchanged if followed by a blank, tab, or end-of-line. </p>
<p> Input/output redirections are recognized before variable expansion, and are variable expanded separately. Otherwise, the command name and entire argument list are expanded together. It is thus possible for the first (command) word (to this point) to generate more than one word, the first of which becomes the command name, and the rest of which become arguments. </p>
<p> Unless enclosed in `&#8217; or given the `:q&#8217; modifier, the results of variable substitution may eventually be command and filename substituted. Within `&#8217; , a variable whose value consists of multiple words expands to (a portion of) a single word, with the words of the variable&#8217;s value separated by blanks. When the `:q&#8217; modifier is applied to a substitution the variable will expand to multiple words with each word separated by a blank and quoted to prevent later command or filename substitution. </p>
<p> The following metasequences are provided for introducing variable values into the shell input. Except as noted, it is an error to reference a variable that is not set. </p>
<dl>
<dt><code>$name</code></p>
<dd>
<dt><code>${name}</code></p>
<dd> Are replaced by the words of the value of variable <i>name</i> each separated by a blank. Braces insulate <i>name</i> from following characters that would otherwise be part of it. Shell variables have names consisting of up to 20 letters and digits starting with a letter. The underscore character is considered a letter. If <i>name</i> is not a shell variable, but is set in the environment, then that value is returned (but `:&#8217; modifiers and the other forms given below are not available here).</p>
<dt><code>$name </code>[selector]</p>
<dd>
<dt><code>${name [ selector ] }</code></p>
<dd> May be used to select only some of the words from the value of <i>name</i> The selector is subjected to `$&#8217; substitution and may consist of a single number or two numbers separated by a `-&#8216; The first word of a variable&#8217;s value is numbered `1&#8242; If the first number of a range is omitted it defaults to `1&#8242; If the last number of a range is omitted it defaults to `$#name&#8217; The selector `*&#8217; selects all words. It is not an error for a range to be empty if the second argument is omitted or in range.</p>
<dt><code>$#name</code></p>
<dd>
<dt><code>${#name}</code></p>
<dd> Gives the number of words in the variable. This is useful for later use in a &#8220;$argv[selector]&#8221;</p>
<dt><code>$0</code></p>
<dd> Substitutes the name of the file from which command input is being read. An error occurs if the name is not known.</p>
<dt><code>$number</code></p>
<dd>
<dt><code>${number}</code></p>
<dd> Equivalent to &#8220;$argv[number]&#8221;</p>
<dt><code>$*</code></p>
<dd> Equivalent to &#8220;$argv[*]&#8221;</dl>
<p> The modifiers `:e&#8217; , `:h&#8217; , `:t&#8217; , `:r&#8217; , `:q&#8217; , and `:x&#8217; may be applied to the substitutions above as may `:gh&#8217; , `:gt&#8217; , and `:gr&#8217; If braces `{&#8216; `}&#8217; appear in the command form then the modifiers must appear within the braces. The current implementation allows only one `:&#8217; modifier on each `$&#8217; expansion. </p>
<p> The following substitutions may not be modified with `:&#8217; modifiers.</p>
<dl>
<dt><code>$?name</code></p>
<dd>
<dt><code>${?name}</code></p>
<dd> Substitutes the string &#8220;1&#8221; if name is set, &#8220;0&#8221; if it is not.</p>
<dt><code>$?0</code></p>
<dd> Substitutes `1&#8242; if the current input filename is known, `0&#8242; if it is not.</p>
<dt><code>$$</code></p>
<dd> Substitute the (decimal) process number of the (parent) shell. Do <i>NOT</i> use this mechanism for generating temporary file names; see <a href="/docs/linux/man/1-mktemp/">mktemp</a>(1) instead.</p>
<dt><code>$!</code></p>
<dd> Substitute the (decimal) process number of the last background process started by this shell.</p>
<dt><code>$&lt;</code></p>
<dd> Substitutes a line from the standard input, with no further interpretation. It can be used to read from the keyboard in a shell script.</dl>
<h3>Command and filename substitution</h3>
<p> The remaining substitutions, command and filename substitution, are applied selectively to the arguments of built-in commands. By selectively, we mean that portions of expressions which are not evaluated are not subjected to these expansions. For commands that are not internal to the shell, the command name is substituted separately from the argument list. This occurs very late, after input-output redirection is performed, and in a child of the main shell.</p>
<h3>Command substitution</h3>
<p> Command substitution is shown by a command enclosed in &#8220;&#8217; The output from such a command is normally broken into separate words at blanks, tabs, and newlines, with null words being discarded; this text then replaces the original string. Within double quotes (`&quot;&#8217;), only newlines force new words; blanks and tabs are preserved. </p>
<p> In any case, the single final newline does not force a new word. Note that it is thus possible for a command substitution to yield only part of a word, even if the command outputs a complete line.</p>
<h3>Filename substitution</h3>
<p> If a word contains any of the characters `*&#8217; , `?&#8217; , `[&#8216; , or `{&#8216; , or begins with the character `~&#8217; , then that word is a candidate for filename substitution, also known as &#8220;globbing&#8221; This word is then regarded as a pattern, and replaced with an alphabetically sorted list of file names that match the pattern. In a list of words specifying filename substitution it is an error for no pattern to match an existing file name, but it is not required for each pattern to match. Only the metacharacters `*&#8217; , `?&#8217; , and `[&#8216; imply pattern matching, the characters `~&#8217; and `{&#8216; being more akin to abbreviations. </p>
<p> In matching filenames, the character `.&#8217; at the beginning of a filename or immediately following a `/&#8217; , as well as the character `/&#8217; must be matched explicitly. The character `*&#8217; matches any string of characters, including the null string. The character `?&#8217; matches any single character. </p>
<p> The sequence &#8220;[&#8230;] &#8221; matches any one of the characters enclosed. Within &#8220;[&#8230;] &#8221; a pair of characters separated by `-&#8216; matches any character lexically between the two (inclusive). Within &#8220;[&#8230;] &#8221; the name of a <i>character class</i> enclosed in `[:&#8217; and `:]&#8217; stands for the list of all characters belonging to that class. Supported character classes:</p>
<dl>
<dt><code>alnum Ta </code>cntrl Ta lower Ta space</p>
<dd>
<dt><code>alpha Ta </code>digit Ta print Ta upper</p>
<dd>
<dt><code>blank Ta </code>graph Ta punct Ta xdigit</p>
<dd></dl>
<p> These match characters using the macros specified in <a href="/docs/linux/man/3-ctype/">ctype</a>(3). A character class may not be used as an endpoint of a range. </p>
<p> The character `~&#8217; at the beginning of a filename refers to home directories. Standing alone, i.e., `~&#8217; , it expands to the invoker&#8217;s home directory as reflected in the value of the variable <i>home</i> When followed by a name consisting of letters, digits, and `-&#8216; characters, the shell searches for a user with that name and substitutes their home directory; thus &#8220;~ken&#8221; might expand to &#8220;/usr/ken&#8221; and &#8220;~ken/chmach&#8221; to &#8220;/usr/ken/chmach&#8221; If the character `~&#8217; is followed by a character other than a letter or `/&#8217; , or does not appear at the beginning of a word, it is left undisturbed. </p>
<p> The metanotation &#8220;a{b,c,d}e&#8221; is a shorthand for &#8220;abe ace ade&#8221; Left to right order is preserved, with results of matches being sorted separately at a low level to preserve this order. This construct may be nested. Thus, &#8220;~source/s1/{oldls,ls}.c&#8221; expands to &#8220;/usr/source/s1/oldls.c /usr/source/s1/ls.c&#8221; without chance of error if the home directory for &#8220;source&#8221; is &#8220;/usr/source&#8221; Similarly &#8220;../{memo,*box}&#8221; might expand to &#8220;../memo ../box ../mbox&#8221; (Note that &#8220;memo&#8221; was not sorted with the results of the match to &#8220;*box .&#8221; As a special case `{&#8216; , `}&#8217; , and `{}&#8217; are passed undisturbed.</p>
<h3>Input/output</h3>
<p> The standard input and the standard output of a command may be redirected with the following syntax: </p>
<dl>
<dt><code>&lt; name</code></p>
<dd> Open file <i>name</i> (which is first variable, command, and filename expanded) as the standard input.</p>
<dt><code>&lt;&lt; word</code></p>
<dd> Read the shell input up to a line that is identical to <i>word</i> <i>word</i> is not subjected to variable, command, or filename substitution, and each input line is compared to <i>word</i> before any substitutions are done on the input line. Unless a quoting `\&#8217; , `&#8217; , `&#8221; or &#8220;&#8217; appears in <i>word</i> variable and command substitution is performed on the intervening lines, allowing `\&#8217; to quote `$&#8217; , `\&#8217; and &#8220;&#8217; Commands that are substituted have all blanks, tabs, and newlines preserved, except for the final newline which is dropped. The resultant text is placed in an anonymous temporary file that is given to the command as its standard input.</p>
<dt><code>&gt; name</code></p>
<dd>
<dt><code>&gt;! name</code></p>
<dd>
<dt><code>&gt;&amp; name</code></p>
<dd>
<dt><code>&gt;&amp;! name</code></p>
<dd> The file <i>name</i> is used as the standard output. If the file does not exist then it is created; if the file exists, it is truncated; its previous contents are lost. </p>
<p> If the variable <i>noclobber</i> is set, then the file must not exist or be a character special file (e.g., a terminal or /dev/null or an error results. This helps prevent accidental destruction of files. Here, the `!&#8217; forms can be used to suppress this check. </p>
<p> The forms involving `&amp;&#8217; route the standard error output into the specified file as well as the standard output. <i>name</i> is expanded in the same way as `&lt;&#8216; input filenames are.</p>
<dt><code>&gt;&gt; name</code></p>
<dd>
<dt><code>&gt;&gt;&amp; name</code></p>
<dd>
<dt><code>&gt;&gt;! name</code></p>
<dd>
<dt><code>&gt;&gt;&amp;! name</code></p>
<dd> Uses file <i>name</i> as the standard output; like `&gt;&#8217; but places output at the end of the file. If the variable <i>noclobber</i> is set, then it is an error for the file not to exist unless one of the `!&#8217; forms is given. Otherwise similar to `&gt;&#8217;</dl>
<p> A command receives the environment in which the shell was invoked as modified by the input-output parameters and the presence of the command in a pipeline. Thus, unlike some previous shells, commands run from a file of shell commands have no access to the text of the commands by default; instead they receive the original standard input of the shell. The `&lt;&lt;&#8216; mechanism should be used to present inline data. This permits shell command scripts to function as components of pipelines and allows the shell to block read its input. Note that the default standard input for a command run detached is <i>not</i> modified to be the empty file /dev/null instead the standard input remains as the original standard input of the shell. If this is a terminal and if the process attempts to read from the terminal, then the process will block and the user will be notified (see Sx Jobs above). </p>
<p> The standard error output may be directed through a pipe with the standard output. Simply use the form `|&amp;&#8217; instead of just `|&#8217;</p>
<h3>Expressions</h3>
<p> Several of the built-in commands (to be described later) take expressions, in which the operators are similar to those of C, with the same precedence, but with the <i>opposite grouping</i> right to left. These expressions appear in the <code>@</code> <code>exit</code> <code>if</code> and <code>while</code> commands. The following operators are available: </p>
<blockquote><p> || &amp;&amp; | ^ &amp; == != =~ !~ &lt;= &gt;= &lt; &gt; &lt;&lt; &gt;&gt; + &#8211; * / % ! ~ ( ) </p></blockquote>
<p> Here the precedence increases to the right, `==&#8217; `!=&#8217; `=~&#8217; and `!~&#8217; , `&lt;=&#8217; `&gt;=&#8217; `&lt;&#8216; and `&gt;&#8217; , `&lt;&lt;&#8216; and `&gt;&gt;&#8217; , `+&#8217; and `-&#8216; , `*&#8217; `/&#8217; and `%&#8217; being, in groups, at the same level. The `==&#8217; `!=&#8217; `=~&#8217; and `!~&#8217; operators compare their arguments as strings; all others operate on numbers. The operators `=~&#8217; and `!~&#8217; are like `!=&#8217; and `==&#8217; except that the right hand side is a <i>pattern</i> (containing, e.g., *&#8217;s, ?&#8217;s, and instances of &#8220;[&#8230;]&#8221; against which the left-hand operand is matched. This reduces the need for use of the <i>switch</i> statement in shell scripts when all that is really needed is pattern matching. </p>
<p> Strings that begin with `0&#8242; are considered octal numbers. Null or missing arguments are considered `0&#8242; The results of all expressions are strings, which represent decimal numbers. It is important to note that no two components of an expression can appear in the same word; except when adjacent to components of expressions that are syntactically significant to the parser Po `&amp;&#8217; , `|&#8217; , `&lt;&#8216; , `&gt;&#8217; , `(&#8216; , and `)&#8217; Pc , they should be surrounded by spaces. </p>
<p> Also available in expressions as primitive operands are command executions enclosed in `{&#8216; and `}&#8217; and file enquiries of the form &#8211;<code>l</code> <i>name</i> where <code>l</code> is one of: </p>
<blockquote>
<pre>
r       read access
w       write access
x       execute access
e       existence
o       ownership
z       zero size
f       plain file
d       directory
</pre>
</blockquote>
<p> The specified name is command and filename expanded and then tested to see if it has the specified relationship to the real user. If the file does not exist or is inaccessible then all enquiries return false, i.e., `0&#8242; Command executions succeed, returning true, i.e., `1&#8242; , if the command exits with status 0, otherwise they fail, returning false, i.e., `0&#8242; If more detailed status information is required then the command should be executed outside an expression and the variable <i>status</i> examined.</p>
<h3>Control flow</h3>
<p> The shell contains several commands that can be used to regulate the flow of control in command files (shell scripts) and (in limited but useful ways) from terminal input. These commands all operate by forcing the shell to reread or skip in its input and, because of the implementation, restrict the placement of some of the commands. </p>
<p> The <code>foreach</code> <code>switch</code> and <code>while</code> statements, as well as the <code>if-then-else</code> form of the <code>if</code> statement require that the major keywords appear in a single simple command on an input line as shown below. </p>
<p> If the shell&#8217;s input is not seekable, the shell buffers up input whenever a loop is being read and performs seeks in this internal buffer to accomplish the rereading implied by the loop. (To the extent that this allows, backward goto&#8217;s will succeed on non-seekable inputs.)</p>
<h3>Built-in commands</h3>
<p> Built-in commands are executed within the shell. If a built-in command occurs as any component of a pipeline except the last then it is executed in a sub-shell. </p>
<dl>
<dt><code>alias</code></p>
<dd>
<dt><code>alias </code><i>name</i></p>
<dd>
<dt><code>alias </code><i>name wordlist</i></p>
<dd> The first form prints all aliases. The second form prints the alias for name. The final form assigns the specified <i>wordlist</i> as the alias of <i>name</i> <i>wordlist</i> is command and filename substituted. <i>name</i> is not allowed to be &#8220;alias&#8221; or &#8220;unalias&#8221; </p>
<dt><code>alloc</code></p>
<dd> Shows the amount of dynamic memory acquired, broken down into used and free memory. With an argument shows the number of free and used blocks in each size category. The categories start at size 8 and double at each step. This command&#8217;s output may vary across system types, since systems other than the <code>VAX</code> may use a different memory allocator. </p>
<dt><code>bg</code></p>
<dd>
<dt><code>bg % </code><i>job &#8230;</i></p>
<dd> Puts the current or specified jobs into the background, continuing them if they were stopped. </p>
<dt><code>break</code></p>
<dd> Causes execution to resume after the <code>end</code> of the nearest enclosing <code>foreach</code> or <code>while</code> The remaining commands on the current line are executed. Multi-level breaks are thus possible by writing them all on one line. </p>
<dt><code>breaksw</code></p>
<dd> Causes a break from a <code>switch</code> resuming after the <code>endsw</code> </p>
<dt><code>case </code><i>label</i></p>
<dd> A label in a <code>switch</code> statement as discussed below. </p>
<dt><code>cd</code></p>
<dd>
<dt><code>cd </code><i>name</i></p>
<dd>
<dt><code>chdir</code></p>
<dd>
<dt><code>chdir </code><i>name</i></p>
<dd> Change the shell&#8217;s working directory to directory <i>name</i> If no argument is given then change to the home directory of the user. If <i>name</i> is not found as a subdirectory of the current directory (and does not begin with `/&#8217; , `./&#8217; or `../&#8217; ) , then each component of the variable <i>cdpath</i> is checked to see if it has a subdirectory <i>name</i> Finally, if all else fails but <i>name</i> is a shell variable whose value begins with `/&#8217; , then this is tried to see if it is a directory. </p>
<dt><code>continue</code></p>
<dd> Continue execution of the nearest enclosing <code>while</code> or <code>foreach</code> The rest of the commands on the current line are executed. </p>
<dt><code>default</code></p>
<dd> Labels the default case in a <code>switch</code> statement. The default should come after all <code>case</code> labels. </p>
<dt><code>dirs</code></p>
<dd> Prints the directory stack; the top of the stack is at the left, the first directory in the stack being the current directory. </p>
<dt><code>echo </code><i>wordlist</i></p>
<dd>
<dt><code>echo -n </code><i>wordlist</i></p>
<dd> The specified words are written to the shell&#8217;s standard output, separated by spaces, and terminated with a newline unless the &#8211;<code>n</code> option is specified. </p>
<dt><code>else</code></p>
<dd>
<dt><code>end</code></p>
<dd>
<dt><code>endif</code></p>
<dd>
<dt><code>endsw</code></p>
<dd> See the description of the <code>foreach</code> <code>if</code> <code>switch</code> and <code>while</code> statements below. </p>
<dt><code>eval </code><i>arg &#8230;</i></p>
<dd> (As in <a href="/docs/linux/man/1-sh/">sh</a>(1).) The arguments are read as input to the shell and the resulting command(s) executed in the context of the current shell. This is usually used to execute commands generated as the result of command or variable substitution, since parsing occurs before these substitutions. See <a href="/docs/linux/man/1-tset/">tset</a>(1) for an example of using <code>eval</code> </p>
<dt><code>exec </code><i>command</i></p>
<dd> The specified command is executed in place of the current shell. </p>
<dt><code>exit</code></p>
<dd>
<dt><code>exit ( </code><i>expr</i></p>
<dd> The shell exits either with the value of the <code>status</code> variable (first form) or with the value of the specified <code>expr</code> (second form). </p>
<dt><code>fg</code></p>
<dd>
<dt><code>fg % </code><i>job &#8230;</i></p>
<dd> Brings the current or specified jobs into the foreground, continuing them if they were stopped. </p>
<dt><code>foreach </code><i>name ( wordlist</i></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>end</code></p>
<dd> The variable <i>name</i> is successively set to each member of <i>wordlist</i> and the sequence of commands between this command and the matching <code>end</code> are executed. (Both <code>foreach</code> and <code>end</code> must appear alone on separate lines.) The built-in command <code>continue</code> may be used to continue the loop prematurely and the built-in command <code>break</code> to terminate it prematurely. When this command is read from the terminal, the loop is read once prompting with `?&#8217; before any statements in the loop are executed. If you make a mistake typing in a loop at the terminal you can rub it out. </p>
<dt><code>glob </code><i>wordlist</i></p>
<dd> Like <code>echo</code> but no `\&#8217; escapes are recognized and words are delimited by <code>NUL</code> characters in the output. Useful for programs that wish to use the shell to filename expand a list of words. </p>
<dt><code>goto </code><i>word</i></p>
<dd> The specified <i>word</i> is filename and command expanded to yield a string of the form `label&#8217; The shell rewinds its input as much as possible and searches for a line of the form &#8220;label:&#8221; possibly preceded by blanks or tabs. Execution continues after the specified line. </p>
<dt><code>hashstat</code></p>
<dd> Print a statistics line showing how effective the internal hash table has been at locating commands (and avoiding <code>exec &#8216;s</code> An <code>exec</code> is attempted for each component of the <i>path</i> where the hash function indicates a possible hit, and in each component that does not begin with a `/&#8217; </p>
<dt><code>history</code></p>
<dd>
<dt><code>history </code><i>n</i></p>
<dd>
<dt><code>history -h </code><i>n</i></p>
<dd>
<dt><code>history -r </code><i>n</i></p>
<dd> Displays the history event list; if <i>n</i> is given, only the <i>n</i> most recent events are printed. The &#8211;<code>h</code> option causes the history list to be printed without leading numbers. This format produces files suitable for sourcing using the &#8211;<code>h</code> option to <code>source</code> The &#8211;<code>r</code> option reverses the order of printout to be most recent first instead of oldest first. </p>
<dt><code>if ( </code><i>expr ) </i><code>command</code></p>
<dd> If the specified expression evaluates to true, then the single <i>command</i> with arguments is executed. Variable substitution on <i>command</i> happens early, at the same time it does for the rest of the <code>if</code> command. <i>command</i> must be a simple command, not a pipeline, a command list, or a parenthesized command list. Input/output redirection occurs even if <i>expr</i> is false, i.e., when command is <i>not</i> executed (this is a bug). </p>
<dt><code>if ( </code><i>expr ) </i><code>then</code></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>else if ( </code><i>expr2 ) </i><code>then</code></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>else</code></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>endif</code></p>
<dd> If the specified <i>expr</i> is true then the commands up to the first <code>else</code> are executed; otherwise if <i>expr2</i> is true then the commands up to the second <code>else</code> are executed, etc. Any number of <code>else-if</code> pairs are possible; only one <code>endif</code> is needed. The <code>else</code> part is likewise optional. (The words <code>else</code> and <code>endif</code> must appear at the beginning of input lines; the <code>if</code> must appear alone on its input line or after an <code>else .</code> </p>
<dt><code>jobs</code></p>
<dd>
<dt><code>jobs -l</code></p>
<dd> Lists the active jobs; the &#8211;<code>l</code> option lists process IDs in addition to the normal information. </p>
<dt><code>kill % </code><i>job</i></p>
<dd>
<dt><code>kill</code></p>
<dd> [-<code>s </code><i>signal_name</i> ] <i>pid</i></p>
<dt><code>kill -sig </code><i>pid &#8230;</i></p>
<dd>
<dt><code>kill -l </code>[exit_status]</p>
<dd> Sends either the <code>SIGTERM</code> (terminate) signal or the specified signal to the specified jobs or processes. Signals are either given by number or by names (as given in Aq Pa signal.h , stripped of the prefix &#8220;SIG )&#8221; The signal names are listed by &#8220;kill -l&#8221; if an <i>exit_status</i> is specified, only the corresponding signal name will be written. There is no default; just saying &#8220;kill&#8221; does not send a signal to the current job. If the signal being sent is <code>SIGTERM</code> (terminate) or <code>SIGHUP</code> (hangup), then the job or process will be sent a <code>SIGCONT</code> (continue) signal as well. </p>
<dt><code>limit</code></p>
<dd>
<dt><code>limit </code><i>resource</i></p>
<dd>
<dt><code>limit </code><i>resource maximum-use</i></p>
<dd>
<dt><code>limit -h</code></p>
<dd>
<dt><code>limit -h </code><i>resource</i></p>
<dd>
<dt><code>limit -h </code><i>resource maximum-use</i></p>
<dd> Limits the consumption by the current process and each process it creates to not individually exceed <i>maximum-use</i> on the specified <i>resource</i> If no <i>maximum-use</i> is given, then the current limit is printed; if no <i>resource</i> is given, then all limitations are given. If the &#8211;<code>h</code> flag is given, the hard limits are used instead of the current limits. The hard limits impose a ceiling on the values of the current limits. Only the superuser may raise the hard limits, but a user may lower or raise the current limits within the legal range. </p>
<p> Resources controllable currently include:</p>
<dl>
<dt><i>cputime</i></p>
<dd> the maximum number of CPU-seconds to be used by each process.</p>
<dt><i>filesize</i></p>
<dd> the largest single file (in bytes) that can be created.</p>
<dt><i>datasize</i></p>
<dd> the maximum growth of the data+stack region via <a href="/docs/linux/man/2-sbrk/">sbrk</a>(2) beyond the end of the program text.</p>
<dt><i>stacksize</i></p>
<dd> the maximum size of the automatically-extended stack region.</p>
<dt><i>coredumpsize</i></p>
<dd> the size of the largest core dump (in bytes) that will be created.</p>
<dt><i>memoryuse</i></p>
<dd> the maximum size (in bytes) to which a process&#8217;s resident set size (RSS) may grow.</p>
<dt><i>memorylocked</i></p>
<dd> The maximum size (in bytes) which a process may lock into memory using the <a href="/docs/linux/man/2-mlock/">mlock</a>(2) function.</p>
<dt><i>maxproc</i></p>
<dd> The maximum number of simultaneous processes for this user ID.</p>
<dt><i>openfiles</i></p>
<dd> The maximum number of simultaneous open files for this user ID.</p>
<dt><i>vmemoryuse</i></p>
<dd> the maximum size (in bytes) to which a process&#8217;s total size may grow.</dl>
<p> The <i>maximum-use</i> may be given as a (floating point or integer) number followed by a scale factor. For all limits other than <i>cputime</i> the default scale is `k&#8217; or &#8220;kilobytes&#8221; (1024 bytes); a scale factor of `m&#8217; or &#8220;megabytes&#8221; may also be used. For <i>cputime</i> the default scale is &#8220;seconds&#8221; a scale factor of `m&#8217; for minutes or `h&#8217; for hours, or a time of the form &#8220;mm:ss&#8221; giving minutes and seconds also may be used. </p>
<p> For both <i>resource</i> names and scale factors, unambiguous prefixes of the names suffice. </p>
<dt><code>login</code></p>
<dd> Terminate a login shell, replacing it with an instance of /usr/bin/login This is one way to log off, included for compatibility with <a href="/docs/linux/man/1-sh/">sh</a>(1). </p>
<dt><code>logout</code></p>
<dd> Terminate a login shell. Especially useful if <i>ignoreeof</i> is set. </p>
<dt><code>nice</code></p>
<dd>
<dt><code>nice </code><i>+number</i></p>
<dd>
<dt><code>nice </code><i>command</i></p>
<dd>
<dt><code>nice </code><i>+number command</i></p>
<dd> The first form sets the scheduling priority for this shell to 4. The second form sets the priority to the given <i>number</i> The final two forms run command at priority 4 and <i>number</i> respectively. The greater the number, the less <code>CPU</code> the process will get. The superuser may specify negative priority by using &#8220;nice -number &#8230;&#8221; <i>command</i> is always executed in a sub-shell, and the restrictions placed on commands in simple <code>if</code> statements apply. </p>
<dt><code>nohup</code></p>
<dd>
<dt><code>nohup </code><i>command</i></p>
<dd> The first form can be used in shell scripts to cause hangups to be ignored for the remainder of the script. The second form causes the specified command to be run with hangups ignored. All processes detached with `&amp;&#8217; are effectively <code>nohup &#8216;ed</code> </p>
<dt><code>notify</code></p>
<dd>
<dt><code>notify % </code><i>job &#8230;</i></p>
<dd> Causes the shell to notify the user asynchronously when the status of the current or specified jobs change; normally notification is presented before a prompt. This is automatic if the shell variable <i>notify</i> is set. </p>
<dt><code>onintr</code></p>
<dd>
<dt><code>onintr &#8211; </code></p>
<dd>
<dt><code>onintr </code><i>label</i></p>
<dd> Control the action of the shell on interrupts. The first form restores the default action of the shell on interrupts, which is to terminate shell scripts or to return to the terminal command input level. The second form <code>onintr &#8211;</code> causes all interrupts to be ignored. The final form causes the shell to execute a <code>goto label</code> when an interrupt is received or a child process terminates because it was interrupted. </p>
<p> In any case, if the shell is running detached and interrupts are being ignored, all forms of <code>onintr</code> have no meaning and interrupts continue to be ignored by the shell and all invoked commands. Finally, <code>onintr</code> statements are ignored in the system startup files where interrupts are disabled (/etc/csh.cshrc , /etc/csh.login ) </p>
<dt><code>popd</code></p>
<dd>
<dt><code>popd </code><i>+n</i></p>
<dd> Pops the directory stack, returning to the new top directory. With an argument &#8220;+ <i>n</i> &#8221; discards the <i>n </i><code>&#8216;th</code> entry in the stack. The members of the directory stack are numbered from the top starting at 0. </p>
<dt><code>pushd</code></p>
<dd>
<dt><code>pushd </code><i>name</i></p>
<dd>
<dt><code>pushd </code><i>+n</i></p>
<dd> With no arguments, <code>pushd</code> exchanges the top two elements of the directory stack. Given a <i>name</i> argument, <code>pushd</code> changes to the new directory (ala <code>cd</code> and pushes the old current working directory (as in <code>cwd</code> onto the directory stack. With a numeric argument, <code>pushd</code> rotates the <i>n </i><code>&#8216;th</code> argument of the directory stack around to be the top element and changes to it. The members of the directory stack are numbered from the top starting at 0. </p>
<dt><code>rehash</code></p>
<dd> Causes the internal hash table of the contents of the directories in the <i>path</i> variable to be recomputed. This is needed if new commands are added to directories in the <code>path</code> while you are logged in. This should only be necessary if you add commands to one of your own directories, or if a systems programmer changes the contents of a system directory. </p>
<dt><code>repeat </code><i>count command</i></p>
<dd> The specified <i>command</i> which is subject to the same restrictions as the <i>command</i> in the one line <code>if</code> statement above, is executed <i>count</i> times. I/O redirections occur exactly once, even if <i>count</i> is 0. </p>
<dt><code>set</code></p>
<dd>
<dt><code>set </code><i>name</i></p>
<dd>
<dt><code>set </code><i>name </i><code>=word</code></p>
<dd>
<dt><code>set </code><i>name[index] </i><code>=word</code></p>
<dd>
<dt><code>set </code><i>name </i><code>=(wordlist)</code></p>
<dd> The first form of the command shows the value of all shell variables. Variables that have other than a single word as their value print as a parenthesized word list. The second form sets <i>name</i> to the null string. The third form sets <i>name</i> to the single <i>word</i> The fourth form sets the <i>index </i><code>&#8216;th</code> component of <i>name</i> to <i>word</i> this component must already exist. The final form sets <i>name</i> to the list of words in <i>wordlist</i> The value is always command and filename expanded. </p>
<p> These arguments may be repeated to set multiple values in a single set command. Note however, that variable expansion happens for all arguments before any setting occurs. </p>
<dt><code>setenv</code></p>
<dd>
<dt><code>setenv </code><i>name</i></p>
<dd>
<dt><code>setenv </code><i>name value</i></p>
<dd> The first form lists all current environment variables. It is equivalent to <a href="/docs/linux/man/1-printenv/">printenv</a>(1). The last form sets the value of environment variable <i>name</i> to be <i>value</i> a single string. The second form sets <i>name</i> to an empty string. The most commonly used environment variables <code>USER</code> <code>TERM</code> and <code>PATH</code> are automatically imported to and exported from the <code>csh</code> variables <i>user</i> <i>term</i> and <i>path</i> there is no need to use <code>setenv</code> for these. </p>
<dt><code>shift</code></p>
<dd>
<dt><code>shift </code><i>variable</i></p>
<dd> The members of <code>argv</code> are shifted to the left, discarding <code>argv Bq </code>1 It is an error for <code>argv</code> not to be set or to have less than one word as value. The second form performs the same function on the specified variable. </p>
<dt><code>source </code><i>name</i></p>
<dd>
<dt><code>source -h </code><i>name</i></p>
<dd> The shell reads commands from <i>name</i> <code>source</code> commands may be nested; if they are nested too deeply the shell may run out of file descriptors. An error in a <code>source</code> at any level terminates all nested <code>source</code> commands. Normally input during <code>source</code> commands is not placed on the history list; the &#8211;<code>h</code> option causes the commands to be placed on the history list without being executed. </p>
<dt><code>stop</code></p>
<dd>
<dt><code>stop % </code><i>job &#8230;</i></p>
<dd> Stops the current or specified jobs that are executing in the background. </p>
<dt><code>suspend</code></p>
<dd> Causes the shell to stop in its tracks, much as if it had been sent a stop signal with <code>^Z</code> This is most often used to stop shells started by <a href="/docs/linux/man/1-su/">su</a>(1). </p>
<dt><code>switch ( </code><i>string</i></p>
<dd>
<dt><code>case </code><i>str1</i></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;breaksw</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;</code></p>
<dd>
<dt><code>default</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;</code></p>
<dd>
<dt><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;breaksw</code></p>
<dd>
<dt><code>endsw</code></p>
<dd> Each case label is successively matched against the specified <i>string</i> which is first command and filename expanded. The file metacharacters `*&#8217; , `?&#8217; and &#8220;[&#8230;]&#8221; may be used in the case labels, which are variable expanded. If none of the labels match before the &#8220;default&#8221; label is found, then the execution begins after the default label. Each case label and the default label must appear at the beginning of a line. The command <code>breaksw</code> causes execution to continue after the <code>endsw</code> Otherwise control may fall through case labels and the default label as in C. If no label matches and there is no default, execution continues after the <code>endsw</code> </p>
<dt><code>time</code></p>
<dd>
<dt><code>time </code><i>command</i></p>
<dd> With no argument, a summary of time used by this shell and its children is printed. If arguments are given the specified simple command is timed and a time summary as described under the <code>time</code> variable is printed. If necessary, an extra shell is created to print the time statistic when the command completes. </p>
<dt><code>umask</code></p>
<dd>
<dt><code>umask </code><i>value</i></p>
<dd> The file creation mask is displayed (first form) or set to the specified value (second form). The mask is given in octal. Common values for the mask are 002 giving all access to the group and read and execute access to others or 022 giving all access except write access for users in the group or others. </p>
<dt><code>unalias </code><i>pattern</i></p>
<dd> All aliases whose names match the specified pattern are discarded. Thus all aliases are removed by <code>unalias *</code> It is not an error for nothing to be <code>unalias ed.</code> </p>
<dt><code>unhash</code></p>
<dd> Use of the internal hash table to speed location of executed programs is disabled. </p>
<dt><code>unlimit</code></p>
<dd>
<dt><code>unlimit </code><i>resource</i></p>
<dd>
<dt><code>unlimit -h</code></p>
<dd>
<dt><code>unlimit -h </code><i>resource</i></p>
<dd> Removes the limitation on <i>resource</i> If no <i>resource</i> is specified, then all <i>resource</i> limitations are removed. If &#8211;<code>h</code> is given, the corresponding hard limits are removed. Only the superuser may do this. </p>
<dt><code>unset </code><i>pattern</i></p>
<dd> All variables whose names match the specified pattern are removed. Thus all variables are removed by <code>unset *</code> this has noticeably distasteful side-effects. It is not an error for nothing to be <code>unset</code> </p>
<dt><code>unsetenv </code><i>pattern</i></p>
<dd> Removes all variables whose names match the specified pattern from the environment. See also the <code>setenv</code> command above and <a href="/docs/linux/man/1-printenv/">printenv</a>(1). </p>
<dt><code>wait</code></p>
<dd> Wait for all background jobs. If the shell is interactive, then an interrupt can disrupt the wait. After the interrupt, the shell prints names and job numbers of all jobs known to be outstanding. </p>
<dt><code>which </code><i>command</i></p>
<dd> Displays the resolved command that will be executed by the shell. </p>
<dt><code>while ( </code><i>expr</i></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>end</code></p>
<dd> While the specified expression evaluates to non-zero, the commands between the <code>while</code> and the matching <code>end</code> are evaluated. <code>break</code> and <code>continue</code> may be used to terminate or continue the loop prematurely. (The <code>while</code> and <code>end</code> must appear alone on their input lines.) Prompting occurs here the first time through the loop as for the <code>foreach</code> statement if the input is a terminal. </p>
<dt><code>% </code><i>job</i></p>
<dd> Brings the specified job into the foreground. </p>
<dt><code>% </code><i>job </i><code>&amp;</code></p>
<dd> Continues the specified job in the background. </p>
<dt><code>@</code></p>
<dd>
<dt><code>@ </code><i>name </i><code>= expr</code></p>
<dd>
<dt><code>@ </code><i>name[index] </i><code>= expr</code></p>
<dd> The first form prints the values of all the shell variables. The second form sets the specified <i>name</i> to the value of <i>expr</i> If the expression contains `&lt;&#8216; , `&gt;&#8217; , `&amp;&#8217; or `|&#8217; then at least this part of the expression must be placed within `(&#8216; `)&#8217; The third form assigns the value of <i>expr</i> to the <i>index </i><code>&#8216;th</code> argument of <i>name</i> Both <i>name</i> and its <i>index </i><code>&#8216;th</code> component must already exist. </p>
<p> The operators `*=&#8217; , `+=&#8217; , etc. are available as in C. The space separating the name from the assignment operator is optional. Spaces are, however, mandatory in separating components of <i>expr</i> which would otherwise be single words. </p>
<p> Special postfix `++&#8217; and `&#8211;&#8216; operators increment and decrement <i>name</i> respectively; i.e., &#8220;@ i++&#8221;</dl>
<h3>Pre-defined and environment variables</h3>
<p> The following variables have special meaning to the shell. Of these, <i>argv</i> <i>cwd</i> <i>home</i> <i>path</i> <i>prompt</i> <i>shell</i> and <i>status</i> are always set by the shell. Except for <i>cwd</i> and <i>status</i> this setting occurs only at initialization; these variables will not then be modified unless done explicitly by the user. </p>
<p> The shell copies the environment variable <code>USER</code> into the variable <i>user</i> <code>TERM</code> into <i>term</i> and <code>HOME</code> into <i>home</i> and copies these back into the environment whenever the normal shell variables are reset. The environment variable <code>PATH</code> is likewise handled; it is not necessary to worry about its setting other than in the file .cshrc as inferior <code>csh</code> processes will import the definition of <i>path</i> from the environment, and re-export it if you then change it.</p>
<dl>
<dt><code>argv</code></p>
<dd> Set to the arguments to the shell, it is from this variable that positional parameters are substituted; i.e., &#8220;$1&#8221; is replaced by &#8220;$argv[1]&#8221; etc.</p>
<dt><code>cdpath</code></p>
<dd> Gives a list of alternate directories searched to find subdirectories in <code>chdir</code> commands.</p>
<dt><code>cwd</code></p>
<dd> The full pathname of the current directory.</p>
<dt><code>echo</code></p>
<dd> Set when the &#8211;<code>x</code> command-line option is given. Causes each command and its arguments to be echoed just before it is executed. For non-built-in commands all expansions occur before echoing. Built-in commands are echoed before command and filename substitution, since these substitutions are then done selectively.</p>
<dt><code>filec</code></p>
<dd> Enable file name completion.</p>
<dt><code>histchars</code></p>
<dd> Can be given a string value to change the characters used in history substitution. The first character of its value is used as the history substitution character, replacing the default character `!&#8217; The second character of its value replaces the character `^&#8217; in quick substitutions.</p>
<dt><code>histfile</code></p>
<dd> Can be set to the pathname where history is going to be saved/restored.</p>
<dt><code>history</code></p>
<dd> Can be given a numeric value to control the size of the history list. Any command that has been referenced in this many events will not be discarded. Too large values of <i>history</i> may run the shell out of memory. The last executed command is always saved on the history list.</p>
<dt><code>home</code></p>
<dd> The home directory of the invoker, initialized from the environment. The filename expansion of &#8220;~ &#8221; refers to this variable.</p>
<dt><code>ignoreeof</code></p>
<dd> If set the shell ignores end-of-file from input devices which are terminals. This prevents shells from accidentally being killed by control-Ds.</p>
<dt><code>mail</code></p>
<dd> The files where the shell checks for mail. This checking is done after each command completion that will result in a prompt, if a specified interval has elapsed. The shell says &#8220;You have new mail.&#8221; if the file exists with an access time not greater than its modify time. </p>
<p> If the first word of the value of <i>mail</i> is numeric it specifies a different mail checking interval, in seconds, than the default, which is 10 minutes. </p>
<p> If multiple mail files are specified, then the shell says &#8220;New mail in <i>name</i> &#8221; when there is mail in the file <i>name</i></p>
<dt><code>noclobber</code></p>
<dd> As described in the section on Sx Input/output , restrictions are placed on output redirection to ensure that files are not accidentally destroyed, and that `&gt;&gt;&#8217; redirections refer to existing files.</p>
<dt><code>noglob</code></p>
<dd> If set, filename expansion is inhibited. This inhibition is most useful in shell scripts that are not dealing with filenames, or after a list of filenames has been obtained and further expansions are not desirable.</p>
<dt><code>nonomatch</code></p>
<dd> If set, it is not an error for a filename expansion to not match any existing files; instead the primitive pattern is returned. It is still an error for the primitive pattern to be malformed; i.e., &#8220;echo&#8221; still gives an error.</p>
<dt><code>notify</code></p>
<dd> If set, the shell notifies asynchronously of job completions; the default is to present job completions just before printing a prompt.</p>
<dt><code>path</code></p>
<dd> Each word of the <i>path</i> variable specifies a directory in which commands are to be sought for execution. A null word specifies the current directory. If there is no <i>path</i> variable then only full path names will execute. The usual search path is &#8220;.&#8221; &#8220;/bin&#8221; &#8220;/usr/bin&#8221; &#8220;/sbin&#8221; and &#8220;/usr/sbin&#8221; but this may vary from system to system. For the superuser the default search path is &#8220;/bin&#8221; &#8220;/usr/bin&#8221; &#8220;/sbin&#8221; and &#8220;/usr/sbin&#8221; A shell that is given neither the &#8211;<code>c</code> nor the &#8211;<code>t</code> option will normally hash the contents of the directories in the <i>path</i> variable after reading <i>.cshrc</i> and each time the <i>path</i> variable is reset. If new commands are added to these directories while the shell is active, it may be necessary to do a <code>rehash</code> or the commands may not be found.</p>
<dt><code>prompt</code></p>
<dd> The string that is printed before each command is read from an interactive terminal input. If a `!&#8217; appears in the string it will be replaced by the current event number unless a preceding `\&#8217; is given. Default is &#8220;%&#8221; or &#8220;#&#8221; for the superuser.</p>
<dt><code>savehist</code></p>
<dd> Is given a numeric value to control the number of entries of the history list that are saved in ~/.history when the user logs out. Any command that has been referenced in this many events will be saved. During start up the shell sources ~/.history into the history list enabling history to be saved across logins. Too large values of <i>savehist</i> will slow down the shell during start up. If <i>savehist</i> is just set, the shell will use the value of <i>history</i></p>
<dt><code>shell</code></p>
<dd> The file in which the shell resides. This variable is used in forking shells to interpret files that have execute bits set, but which are not executable by the system. (See the description of Sx Non-built-in command execution below.) Initialized to the (system-dependent) home of the shell.</p>
<dt><code>status</code></p>
<dd> The status returned by the last command. If it terminated abnormally, then 0200 is added to the status. Built-in commands that fail return exit status 1, all other built-in commands set status to 0.</p>
<dt><code>time</code></p>
<dd> Controls automatic timing of commands. If set, then any command that takes more than this many <code>CPU</code> seconds will cause a line giving user, system, and real times, and a utilization percentage which is the ratio of user plus system times to real time to be printed when it terminates.</p>
<dt><code>verbose</code></p>
<dd> Set by the &#8211;<code>v</code> command-line option, causes the words of each command to be printed after history substitution.</dl>
<h3>Non-built-in command execution</h3>
<p> When a command to be executed is found to not be a built-in command the shell attempts to execute the command via <a href="/docs/linux/man/2-execve/">execve</a>(2). Each word in the variable <i>path</i> names a directory from which the shell will attempt to execute the command. If it is given neither a &#8211;<code>c</code> nor a &#8211;<code>t</code> option, the shell will hash the names in these directories into an internal table so that it will only try an <code>exec</code> in a directory if there is a possibility that the command resides there. This shortcut greatly speeds command location when many directories are present in the search path. If this mechanism has been turned off (via <code>unhash )</code> or if the shell was given a &#8211;<code>c</code> or &#8211;<code>t</code> argument, and in any case for each directory component of <i>path</i> that does not begin with a `/&#8217; , the shell concatenates with the given command name to form a path name of a file which it then attempts to execute. </p>
<p> Parenthesized commands are always executed in a sub-shell. Thus </p>
<blockquote><p><tt>(cd ; pwd) ; pwd</tt></p></blockquote>
<p> prints the <i>home</i> directory; leaving you where you were (printing this after the home directory), while </p>
<blockquote><p><tt>cd ; pwd</tt></p></blockquote>
<p> leaves you in the <i>home</i> directory. Parenthesized commands are most often used to prevent <code>chdir</code> from affecting the current shell. </p>
<p> If the file has execute permissions but is not an executable binary to the system, then it is assumed to be a file containing shell commands and a new shell is spawned to read it. </p>
<p> If there is an alias for <code>shell</code> then the words of the alias will be prepended to the argument list to form the shell command. The first word of the alias should be the full path name of the shell (e.g., &#8220;$shell )&#8221; Note that this is a special, late occurring, case of <code>alias</code> substitution, and only allows words to be prepended to the argument list without change.</p>
<h3>Signal handling</h3>
<p> The shell normally ignores <code>SIGQUIT</code> signals. Jobs running detached (either by <code>&amp;</code> or the <code>bg</code> or <code>%&#8230;</code> commands) are immune to signals generated from the keyboard, including hangups. Other signals have the values which the shell inherited from its parent. The shell&#8217;s handling of interrupts and terminate signals in shell scripts can be controlled by <code>onintr</code> Login shells catch the <code>SIGTERM</code> (terminate) signal; otherwise this signal is passed on to children from the state in the shell&#8217;s parent. Interrupts are not allowed when a login shell is reading the file .logout</p>
<h2>LIMITATIONS</h2>
<p> Word lengths &#8211; Words can be no longer than 1024 characters. The number of arguments to a command that involves filename expansion is limited to 1/6th the number of characters allowed in an argument list. Command substitutions may substitute no more characters than are allowed in an argument list. To detect looping, the shell restricts the number of <code>alias</code> substitutions on a single line to 20.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.cshrc </code></p>
<dd> read at beginning of execution by each shell</p>
<dt><code>~/.login </code></p>
<dd> read by login shell, after .cshrc at login</p>
<dt><code>~/.logout </code></p>
<dd> read by login shell, at logout</p>
<dt><code>/bin/sh </code></p>
<dd> standard shell, for shell scripts not starting with a `#&#8217;</p>
<dt><code>/tmp/sh.* </code></p>
<dd> temporary file for `&lt;&lt;&#8216;</p>
<dt><code>/etc/passwd </code></p>
<dd> source of home directories for &#8220;~name&#8221;</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sh/">sh</a>(1), <a href="/docs/linux/man/2-access/">access</a>(2), <a href="/docs/linux/man/2-execve/">execve</a>(2), <a href="/docs/linux/man/2-fork/">fork</a>(2), <a href="/docs/linux/man/2-pipe/">pipe</a>(2), <a href="/docs/linux/man/2-setrlimit/">setrlimit</a>(2), <a href="/docs/linux/man/2-umask/">umask</a>(2), <a href="/docs/linux/man/2-wait/">wait</a>(2), <a href="/docs/linux/man/3-killpg/">killpg</a>(3), <a href="/docs/linux/man/3-sigvec/">sigvec</a>(3), <a href="/docs/linux/man/4-tty/">tty</a>(4), a.out5, <a href="/docs/linux/man/7-environ/">environ</a>(7), <a href="/docs/linux/man/7-script/">script</a>(7)</p>
<h2>HISTORY</h2>
<p> <code>csh</code> appeared in BSD 3 It was a first implementation of a command language interpreter incorporating a history mechanism (see Sx History substitutions ) , job control facilities (see Sx Jobs ) , interactive file name and user name completion (see Sx File name completion ) , and a C-like syntax. There are now many shells that also have these mechanisms, plus a few more (and maybe some bugs too), which are available through the usenet.</p>
<h2>AUTHORS</h2>
<p> William Joy. Job control and directory stack features first implemented by J.E. Kulp of IIASA, Laxenburg, Austria, with different syntax than that used now. File name completion code written by Ken Greer, HP Labs. Eight-bit implementation Christos S. Zoulas, Cornell University.</p>
<h2>BUGS</h2>
<p> When a command is restarted from a stop, the shell prints the directory it started in if this is different from the current directory; this can be misleading (i.e., wrong) as the job may have changed directories internally. </p>
<p> Shell built-in functions are not stoppable/restartable. Command sequences of the form &#8220;a ; b ; c&#8221; are also not handled gracefully when stopping is attempted. If you suspend `b&#8217; , the shell will immediately execute `c&#8217; This is especially noticeable if this expansion results from an alias. It suffices to place the sequence of commands in ()&#8217;s to force it to a sub-shell; i.e., &#8220;Po a ; b ; c Pc &#8221; </p>
<p> Control over tty output after processes are started is primitive; perhaps this will inspire someone to work on a good virtual terminal interface. In a virtual terminal interface much more interesting things could be done with output control. </p>
<p> Alias substitution is most often used to clumsily simulate shell procedures; shell procedures should be provided instead of aliases. </p>
<p> Commands within loops, prompted for by `?&#8217; , are not placed on the <code>history</code> list. Control structure should be parsed instead of being recognized as built-in commands. This would allow control commands to be placed anywhere, to be combined with `|&#8217; , and to be used with `&amp;&#8217; and `;&#8217; metasyntax. </p>
<p> It should be possible to use the `:&#8217; modifiers on the output of command substitutions. </p>
<p> The way the <i>filec</i> facility is implemented is ugly and expensive. </p>
<h2>Index</h2>
