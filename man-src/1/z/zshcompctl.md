---
title: "zshcompctl(1)"
name: "zshcompctl"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshcompctl/"
description: "zshcompctl – zsh programmable completion"
---

<h2 class="name">NAME</h2>
<p> zshcompctl &#8211; zsh programmable completion </p>
<h2>DESCRIPTION</h2>
<p> This version of zsh has two ways of performing completion of words on the command line. New users of the shell may prefer to use the newer and more powerful system based on shell functions; this is described in <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1), and the basic shell mechanisms which support it are described in <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1). This manual entry describes the older <code>compctl</code> command. </p>
<dl>
<dt><code>compctl</code> [ <code>-CDT</code> ] <i>options</i> [ <i>command</i> &#8230; ]</p>
<dd>
<dt><code>compctl </code>[ <code>-CDT</code> ] <i>options</i> [ <code>-x</code> <i>pattern</i> <i>options</i> <code>&#8211;</code> &#8230; <code>&#8211;</code><code>&#8211;</code> ]</p>
<dd>
<dt>[ <code>+</code> <i>options</i> [ <code>-x</code> &#8230; <code>&#8211;</code><code>&#8211;</code> ] &#8230; [<code>+</code>] ] [ <i>command</i> &#8230; ]</p>
<dd>
<dt><code>compctl</code> <code>-M</code> <i>match-specs</i> &#8230;</p>
<dd>
<dt><code>compctl</code> <code>-L</code> [ <code>-CDTM</code> ] [ <i>command</i> &#8230; ]</p>
<dd>
<dt><code>compctl</code> <code>+</code> <i>command</i> &#8230;</p>
<dd></dl>
<p> Control the editor&#8217;s completion behavior according to the supplied set of <i>options</i>. Various editing commands, notably <code>expand-or-complete-word</code>, usually bound to tab, will attempt to complete a word typed by the user, while others, notably <code>delete-char-or-list</code>, usually bound to ^D in EMACS editing mode, list the possibilities; <code>compctl</code> controls what those possibilities are. They may for example be filenames (the most common case, and hence the default), shell variables, or words from a user-specified list. </p>
<h2>COMMAND FLAGS</h2>
<p> Completion of the arguments of a command may be different for each command or may use the default. The behavior when completing the command word itself may also be separately specified. These correspond to the following flags and arguments, all of which (except for <code>-L</code>) may be combined with any combination of the <i>options</i> described subsequently in the section `Option Flags&#8217;: </p>
<dl>
<dt>
<dd> <i>command</i> &#8230; controls completion for the named commands, which must be listed last on the command line. If completion is attempted for a command with a pathname containing slashes and no completion definition is found, the search is retried with the last pathname component. If the command starts with a <code>=</code>, completion is tried with the pathname of the command.</p>
<dl>
<dt>
<dd>
<p> Any of the <i>command</i> strings may be patterns of the form normally used for filename generation. These should be quoted to protect them from immediate expansion; for example the command string <code>&#8216;foo*&#8217;</code> arranges for completion of the words of any command beginning with <code>foo</code>. When completion is attempted, all pattern completions are tried in the reverse order of their definition until one matches. By default, completion then proceeds as normal, i.e. the shell will try to generate more matches for the specific command on the command line; this can be overridden by including <code>-tn</code> in the flags for the pattern completion. </p>
<p> Note that aliases are expanded before the command name is determined unless the <code>COMPLETE_ALIASES</code> option is set. Commands may not be combined with the <code>-C</code>, <code>-D</code> or <code>-T</code> flags.</dl>
<dt><code>-C</code></p>
<dd> controls completion when the command word itself is being completed. If no <code>compctl -C</code> command has been issued, the names of any executable command (whether in the path or specific to the shell, such as aliases or functions) are completed.</p>
<dt><code>-D</code></p>
<dd> controls default completion behavior for the arguments of commands not assigned any special behavior. If no <code>compctl -D</code> command has been issued, filenames are completed.</p>
<dt><code>-T</code></p>
<dd> supplies completion flags to be used before any other processing is done, even before processing for <code>compctl</code>s defined for specific commands. This is especially useful when combined with extended completion (the <code>-x</code> flag, see the section `Extended Completion&#8217; below). Using this flag you can define default behavior which will apply to all commands without exception, or you can alter the standard behavior for all commands. For example, if your access to the user database is too slow and/or it contains too many users (so that completion after `<code>~</code>&#8216; is too slow to be usable), you can use</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
compctl - T - x 's[~] C[0,[^/]#]' - k friends - S / -tn
</code></pre>
</dl>
<p> to complete the strings in the array <code>friends</code> after a `<code>~</code>&#8216;. The <code>C[</code><i>&#8230;</i><code>]</code> argument is necessary so that this form of <code>~</code>-completion is not tried after the directory name is finished.</dl>
<dt><code>-L</code></p>
<dd> lists the existing completion behavior in a manner suitable for putting into a start-up script; the existing behavior is not changed. Any combination of the above forms, or the <code>-M</code> flag (which must follow the <code>-L</code> flag), may be specified, otherwise all defined completions are listed. Any other flags supplied are ignored.</p>
<dt><i>no argument</i></p>
<dd> If no argument is given, <code>compctl</code> lists all defined completions in an abbreviated form; with a list of <i>options</i>, all completions with those flags set (not counting extended completion) are listed.</dl>
<p> If the <code>+</code> flag is alone and followed immediately by the <i>command</i> list, the completion behavior for all the commands in the list is reset to the default. In other words, completion will subsequently use the options specified by the <code>-D</code> flag. </p>
<p> The form with <code>-M</code> as the first and only option defines global matching specifications (see zshcompwid). The match specifications given will be used for every completion attempt (only when using <code>compctl</code>, not with the new completion system) and are tried in the order in which they are defined until one generates at least one match. E.g.: </p>
<dl>
<dt>
<dd>
compctl &#8211; M &#8221; &#8216;m:{a-zA-Z}={A-Za-z}&#8217;
</dl>
<p> This will first try completion without any global match specifications (the empty string) and, if that generates no matches, will try case insensitive completion. </p>
<h2>OPTION FLAGS</h2>
<dl>
<dt>[ <code>-fcFBdeaRGovNAIOPZEnbjrzu/12</code> ]</p>
<dd>
<dt>[ <code>-k</code> <i>array</i> ] [ <code>-g</code> <i>globstring</i> ] [ <code>-s</code> <i>subststring</i> ]</p>
<dd>
<dt>[ <code>-K</code> <i>function</i> ]</p>
<dd>
<dt>[ <code>-Q</code> ] [ <code>-P</code> <i>prefix</i> ] [ <code>-S</code> <i>suffix</i> ]</p>
<dd>
<dt>[ <code>-W</code> <i>file-prefix</i> ] [ <code>-H</code> <i>num pattern</i> ]</p>
<dd>
<dt>[ <code>-q</code> ] [ <code>-X</code> <i>explanation</i> ] [ <code>-Y</code> <i>explanation</i> ]</p>
<dd>
<dt>[ <code>-y</code> <i>func-or-var</i> ] [ <code>-l</code> <i>cmd</i> ] [ <code>-h</code> <i>cmd</i> ] [ <code>-U</code> ]</p>
<dd>
<dt>[ <code>-t</code> <i>continue</i> ] [ <code>-J</code> <i>name</i> ] [ <code>-V</code> <i>name</i> ]</p>
<dd>
<dt>[ <code>-M</code> <i>match-spec</i> ]</p>
<dd></dl>
<p> The remaining <i>options</i> specify the type of command arguments to look for during completion. Any combination of these flags may be specified; the result is a sorted list of all the possibilities. The options are as follows. </p>
<h3>Simple Flags</h3>
<p> These produce completion lists made up by the shell itself: </p>
<dl>
<dt>
<dd> <code>-f</code> Filenames and file system paths.</p>
<dt><code>-/</code></p>
<dd> Just file system paths.</p>
<dt><code>-c</code></p>
<dd> Command names, including aliases, shell functions, builtins and reserved words.</p>
<dt><code>-F</code></p>
<dd> Function names.</p>
<dt><code>-B</code></p>
<dd> Names of builtin commands.</p>
<dt><code>-m</code></p>
<dd> Names of external commands.</p>
<dt><code>-w</code></p>
<dd> Reserved words.</p>
<dt><code>-a</code></p>
<dd> Alias names.</p>
<dt><code>-R</code></p>
<dd> Names of regular (non-global) aliases.</p>
<dt><code>-G</code></p>
<dd> Names of global aliases.</p>
<dt><code>-d</code></p>
<dd> This can be combined with <code>-F</code>, <code>-B</code>, <code>-w</code>, <code>-a</code>, <code>-R</code> and <code>-G</code> to get names of disabled functions, builtins, reserved words or aliases.</p>
<dt><code>-e</code></p>
<dd> This option (to show enabled commands) is in effect by default, but may be combined with <code>-d</code>; <code>-de</code> in combination with <code>-F</code>, <code>-B</code>, <code>-w</code>, <code>-a</code>, <code>-R</code> and <code>-G</code> will complete names of functions, builtins, reserved words or aliases whether or not they are disabled.</p>
<dt><code>-o</code></p>
<dd> Names of shell options (see <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1)).</p>
<dt><code>-v</code></p>
<dd> Names of any variable defined in the shell.</p>
<dt><code>-N</code></p>
<dd> Names of scalar (non-array) parameters.</p>
<dt><code>-A</code></p>
<dd> Array names.</p>
<dt><code>-I</code></p>
<dd> Names of integer variables.</p>
<dt><code>-O</code></p>
<dd> Names of read-only variables.</p>
<dt><code>-p</code></p>
<dd> Names of parameters used by the shell (including special parameters).</p>
<dt><code>-Z</code></p>
<dd> Names of shell special parameters.</p>
<dt><code>-E</code></p>
<dd> Names of environment variables.</p>
<dt><code>-n</code></p>
<dd> Named directories.</p>
<dt><code>-b</code></p>
<dd> Key binding names.</p>
<dt><code>-j</code></p>
<dd> Job names: the first word of the job leader&#8217;s command line. This is useful with the <code>kill</code> builtin.</p>
<dt><code>-r</code></p>
<dd> Names of running jobs.</p>
<dt><code>-z</code></p>
<dd> Names of suspended jobs.</p>
<dt><code>-u</code></p>
<dd> User names.</dl>
<h3>Flags with Arguments</h3>
<p> These have user supplied arguments to determine how the list of completions is to be made up: </p>
<dl>
<dt>
<dd> <code>-k</code> <i>array</i> Names taken from the elements of <code>$</code><i>array</i> (note that the `<code>$</code>&#8216; does not appear on the command line). Alternatively, the argument <i>array</i> itself may be a set of space- or comma-separated values in parentheses, in which any delimiter may be escaped with a backslash; in this case the argument should be quoted. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>compctl -k &quot;(cputime filesize datasize stacksize
               coredumpsize resident descriptors)&quot; limit</code>
</pre>
</dl>
</dl>
<dt><code>-g</code> <i>globstring</i></p>
<dd> The <i>globstring</i> is expanded using filename globbing; it should be quoted to protect it from immediate expansion. The resulting filenames are taken as the possible completions. Use `<code>*(/)</code>&#8216; instead of `<code>*/</code>&#8216; for directories. The <code>fignore</code> special parameter is not applied to the resulting files. More than one pattern may be given separated by blanks. (Note that brace expansion is <i>not</i> part of globbing. Use the syntax `<code>(either|or)</code>&#8216; to match alternatives.)</p>
<dt><code>-s</code> <i>subststring</i></p>
<dd> The <i>subststring</i> is split into words and these words are than expanded using all shell expansion mechanisms (see <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1)). The resulting words are taken as possible completions. The <code>fignore</code> special parameter is not applied to the resulting files. Note that <code>-g</code> is faster for filenames.</p>
<dt><code>-K</code> <i>function</i></p>
<dd> Call the given function to get the completions. Unless the name starts with an underscore, the function is passed two arguments: the prefix and the suffix of the word on which completion is to be attempted, in other words those characters before the cursor position, and those from the cursor position onwards. The whole command line can be accessed with the <code>-c</code> and <code>-l</code> flags of the <code>read</code> builtin. The function should set the variable <code>reply</code> to an array containing the completions (one completion per element); note that <code>reply</code> should not be made local to the function. From such a function the command line can be accessed with the <code>-c</code> and <code>-l</code> flags to the <code>read</code> builtin. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
function whoson<br />
{<br />
    reply = (`users`);<br />
}<br />
compctl &#8211; K whoson talk
</dl>
<p> completes only logged-on users after `<code>talk</code>&#8216;. Note that `<code>whoson</code>&#8216; must return an array, so `<code>reply=`users`</code>&#8216; would be incorrect.</dl>
<dt><code>-H</code> <i>num pattern</i></p>
<dd> The possible completions are taken from the last <i>num</i> history lines. Only words matching <i>pattern</i> are taken. If <i>num</i> is zero or negative the whole history is searched and if <i>pattern</i> is the empty string all words are taken (as with `<code>*</code>&#8216;). A typical use is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>compctl -D -f + -H 0 ''</code>
</pre>
</dl>
<p> which forces completion to look back in the history list for a word if no filename matches.</dl>
</dl>
<h3>Control Flags</h3>
<p> These do not directly specify types of name to be completed, but manipulate the options that do: </p>
<dl>
<dt>
<dd> <code>-Q</code> This instructs the shell not to quote any metacharacters in the possible completions. Normally the results of a completion are inserted into the command line with any metacharacters quoted so that they are interpreted as normal characters. This is appropriate for filenames and ordinary strings. However, for special effects, such as inserting a backquoted expression from a completion array (<code>-k</code>) so that the expression will not be evaluated until the complete line is executed, this option must be used.</p>
<dt><code>-P</code> <i>prefix</i></p>
<dd> The <i>prefix</i> is inserted just before the completed string; any initial part already typed will be completed and the whole <i>prefix</i> ignored for completion purposes. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>compctl -j -P &quot;%&quot; kill</code>
</pre>
</dl>
<p> inserts a `%&#8217; after the kill command and then completes job names.</dl>
<dt><code>-S</code> <i>suffix</i></p>
<dd> When a completion is found the <i>suffix</i> is inserted after the completed string. In the case of menu completion the suffix is inserted immediately, but it is still possible to cycle through the list of completions by repeatedly hitting the same key.</p>
<dt><code>-W</code> <i>file-prefix</i></p>
<dd> With directory <i>file-prefix</i>: for command, file, directory and globbing completion (options <code>-c</code>, <code>-f</code>, <code>-/</code>, <code>-g</code>), the file prefix is implicitly added in front of the completion. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>compctl -/ -W ~/Mail maildirs</code>
</pre>
</dl>
<p> completes any subdirectories to any depth beneath the directory <code>~/Mail</code>, although that prefix does not appear on the command line. The <i>file-prefix</i> may also be of the form accepted by the <code>-k</code> flag, i.e. the name of an array or a literal list in parenthesis. In this case all the directories in the list will be searched for possible completions.</dl>
<dt><code>-q</code></p>
<dd> If used with a suffix as specified by the <code>-S</code> option, this causes the suffix to be removed if the next character typed is a blank or does not insert anything or if the suffix consists of only one character and the next character typed is the same character; this the same rule used for the <code>AUTO_REMOVE_SLASH</code> option. The option is most useful for list separators (comma, colon, etc.).</p>
<dt><code>-l</code> <i>cmd</i></p>
<dd> This option restricts the range of command line words that are considered to be arguments. If combined with one of the extended completion patterns `<code>p[</code>&#8230;<code>]</code>&#8216;, `<code>r[</code>&#8230;<code>]</code>&#8216;, or `<code>R[</code>&#8230;<code>]</code>&#8216; (see the section `Extended Completion&#8217; below) the range is restricted to the range of arguments specified in the brackets. Completion is then performed as if these had been given as arguments to the <i>cmd</i> supplied with the option. If the <i>cmd</i> string is empty the first word in the range is instead taken as the command name, and command name completion performed on the first word in the range. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
compctl &#8211; x &#8216;r[-exec,;]&#8217; &#8211; l &#8221; &#8211;find
</dl>
<p> completes arguments between `<code>-exec</code>&#8216; and the following `<code>;</code>&#8216; (or the end of the command line if there is no such string) as if they were a separate command line.</dl>
<dt><code>-h</code> <i>cmd</i></p>
<dd> Normally zsh completes quoted strings as a whole. With this option, completion can be done separately on different parts of such strings. It works like the <code>-l</code> option but makes the completion code work on the parts of the current word that are separated by spaces. These parts are completed as if they were arguments to the given <i>cmd</i>. If <i>cmd</i> is the empty string, the first part is completed as a command name, as with <code>-l</code>.</p>
<dt><code>-U</code></p>
<dd> Use the whole list of possible completions, whether or not they actually match the word on the command line. The word typed so far will be deleted. This is most useful with a function (given by the <code>-K</code> option) which can examine the word components passed to it (or via the <code>read</code> builtin&#8217;s <code>-c</code> and <code>-l</code> flags) and use its own criteria to decide what matches. If there is no completion, the original word is retained. Since the produced possible completions seldom have interesting common prefixes and suffixes, menu completion is started immediately if <code>AUTO_MENU</code> is set and this flag is used.</p>
<dt><code>-y</code> <i>func-or-var</i></p>
<dd> The list provided by <i>func-or-var</i> is displayed instead of the list of completions whenever a listing is required; the actual completions to be inserted are not affected. It can be provided in two ways. Firstly, if <i>func-or-var</i> begins with a <code>$</code> it defines a variable, or if it begins with a left parenthesis a literal array, which contains the list. A variable may have been set by a call to a function using the <code>-K</code> option. Otherwise it contains the name of a function which will be executed to create the list. The function will be passed as an argument list all matching completions, including prefixes and suffixes expanded in full, and should set the array <code>reply</code> to the result. In both cases, the display list will only be retrieved after a complete list of matches has been created.</p>
<dl>
<dt>
<dd>
<p> Note that the returned list does not have to correspond, even in length, to the original set of matches, and may be passed as a scalar instead of an array. No special formatting of characters is performed on the output in this case; in particular, newlines are printed literally and if they appear output in columns is suppressed.</dl>
<dt><code>-X</code> <i>explanation</i></p>
<dd> Print <i>explanation</i> when trying completion on the current set of options. A `<code>%n</code>&#8216; in this string is replaced by the number of matches that were added for this explanation string. The explanation only appears if completion was tried and there was no unique match, or when listing completions. Explanation strings will be listed together with the matches of the group specified together with the <code>-X</code> option (using the <code>-J</code> or <code>-V</code> option). If the same explanation string is given to multiple <code>-X</code> options, the string appears only once (for each group) and the number of matches shown for the `<code>%n</code>&#8216; is the total number of all matches for each of these uses. In any case, the explanation string will only be shown if there was at least one match added for the explanation string.</p>
<dl>
<dt>
<dd>
<p> The sequences <code>%B</code>, <code>%b</code>, <code>%S</code>, <code>%s</code>, <code>%U</code>, and <code>%u</code> specify output attributes (bold, standout, and underline), <code>%F</code>, <code>%f</code>, <code>%K</code>, <code>%k</code> specify foreground and background colours, and <code>%{</code><i>&#8230;</i><code>%}</code> can be used to include literal escape sequences as in prompts.</dl>
<dt><code>-Y</code> <i>explanation</i></p>
<dd> Identical to <code>-X</code>, except that the <i>explanation</i> first undergoes expansion following the usual rules for strings in double quotes. The expansion will be carried out after any functions are called for the <code>-K</code> or <code>-y</code> options, allowing them to set variables.</p>
<dt><code>-t</code> <i>continue</i></p>
<dd> The <i>continue</i>-string contains a character that specifies which set of completion flags should be used next. It is useful:</p>
<dl>
<dt>
<dd>
<p> (i) With <code>-T</code>, or when trying a list of pattern completions, when <code>compctl</code> would usually continue with ordinary processing after finding matches; this can be suppressed with `<code>-tn</code>&#8216;. </p>
<p> (ii) With a list of alternatives separated by <code>+</code>, when <code>compctl</code> would normally stop when one of the alternatives generates matches. It can be forced to consider the next set of completions by adding `<code>-t+</code>&#8216; to the flags of the alternative before the `<code>+</code>&#8216;. </p>
<p> (iii) In an extended completion list (see below), when <code>compctl</code> would normally continue until a set of conditions succeeded, then use only the immediately following flags. With `<code>-t-</code>&#8216;, <code>compctl</code> will continue trying extended completions after the next `<code>&#8211;</code>&#8216;; with `<code>-tx</code>&#8216; it will attempt completion with the default flags, in other words those before the `<code>-x</code>&#8216;.</dl>
<dt><code>-J</code> <i>name</i></p>
<dd> This gives the name of the group the matches should be placed in. Groups are listed and sorted separately; likewise, menu completion will offer the matches in the groups in the order in which the groups were defined. If no group name is explicitly given, the matches are stored in a group named <code>default</code>. The first time a group name is encountered, a group with that name is created. After that all matches with the same group name are stored in that group.</p>
<dl>
<dt>
<dd>
<p> This can be useful with non-exclusive alternative completions. For example, in </p>
<dl>
<dt>
<dd>
<pre>
<code>compctl -f -J files -t+ + -v -J variables foo</code>
</pre>
</dl>
<p> both files and variables are possible completions, as the <code>-t+</code> forces both sets of alternatives before and after the <code>+</code> to be considered at once. Because of the <code>-J</code> options, however, all files are listed before all variables.</dl>
<dt><code>-V</code> <i>name</i></p>
<dd> Like <code>-J</code>, but matches within the group will not be sorted in listings nor in menu completion. These unsorted groups are in a different name space from the sorted ones, so groups defined as <code>-J files</code> and <code>-V files</code> are distinct.</p>
<dt><code>-1</code></p>
<dd> If given together with the <code>-V</code> option, makes only consecutive duplicates in the group be removed. Note that groups with and without this flag are in different name spaces.</p>
<dt><code>-2</code></p>
<dd> If given together with the <code>-J</code> or <code>-V</code> option, makes all duplicates be kept. Again, groups with and without this flag are in different name spaces.</p>
<dt><code>-M</code> <i>match-spec</i></p>
<dd> This defines additional matching control specifications that should be used only when testing words for the list of flags this flag appears in. The format of the <i>match-spec</i> string is described in zshcompwid.</dl>
<h2>ALTERNATIVE COMPLETION</h2>
<dl>
<dt><code>compctl</code> [ <code>-CDT</code> ] <i>options</i> <code>+</code> <i>options</i> [ <code>+</code> &#8230; ] [ <code>+</code> ] <i>command</i> &#8230;</p>
<dd></dl>
<p> The form with `<code>+</code>&#8216; specifies alternative options. Completion is tried with the options before the first `<code>+</code>&#8216;. If this produces no matches completion is tried with the flags after the `<code>+</code>&#8216; and so on. If there are no flags after the last `<code>+</code>&#8216; and a match has not been found up to that point, default completion is tried. If the list of flags contains a <code>-t</code> with a <code>+</code> character, the next list of flags is used even if the current list produced matches. </p>
<p> Additional options are available that restrict completion to some part of the command line; this is referred to as `extended completion&#8217;. </p>
<h2>EXTENDED COMPLETION</h2>
<dl>
<dt><code>compctl </code>[ <code>-CDT</code> ] <i>options</i> <code>-x</code> <i>pattern</i> <i>options</i> <code>&#8211;</code> &#8230; <code>&#8211;</code><code>&#8211;</code></p>
<dd>
<dt>[ <i>command</i> &#8230; ]</p>
<dd>
<dt><code>compctl </code>[ <code>-CDT</code> ] <i>options</i> [ <code>-x</code> <i>pattern</i> <i>options</i> <code>&#8211;</code> &#8230; <code>&#8211;</code><code>&#8211;</code> ]</p>
<dd>
<dt>[ <code>+</code> <i>options</i> [ <code>-x</code> &#8230; <code>&#8211;</code><code>&#8211;</code> ] &#8230; [<code>+</code>] ] [ <i>command</i> &#8230; ]</p>
<dd></dl>
<p> The form with `<code>-x</code>&#8216; specifies extended completion for the commands given; as shown, it may be combined with alternative completion using `<code>+</code>&#8216;. Each <i>pattern</i> is examined in turn; when a match is found, the corresponding <i>options</i>, as described in the section `Option Flags&#8217; above, are used to generate possible completions. If no <i>pattern</i> matches, the <i>options</i> given before the <code>-x</code> are used. </p>
<p> Note that each pattern should be supplied as a single argument and should be quoted to prevent expansion of metacharacters by the shell. </p>
<p> A <i>pattern</i> is built of sub-patterns separated by commas; it matches if at least one of these sub-patterns matches (they are `or&#8217;ed). These sub-patterns are in turn composed of other sub-patterns separated by white spaces which match if all of the sub-patterns match (they are `and&#8217;ed). An element of the sub-patterns is of the form `<i>c</i><code>[</code>&#8230;<code>][</code>&#8230;<code>]</code>&#8216;, where the pairs of brackets may be repeated as often as necessary, and matches if any of the sets of brackets match (an `or&#8217;). The example below makes this clearer. </p>
<p> The elements may be any of the following: </p>
<dl>
<dt>
<dd> <code>s[</code><i>string</i><code>]</code>&#8230; Matches if the current word on the command line starts with one of the strings given in brackets. The <i>string</i> is not removed and is not part of the completion.</p>
<dt><code>S[</code><i>string</i><code>]</code>&#8230;</p>
<dd> Like <code>s[</code><i>string</i><code>]</code> except that the <i>string</i> is part of the completion.</p>
<dt><code>p[</code><i>from</i><code>,</code><i>to</i><code>]</code>&#8230;</p>
<dd> Matches if the number of the current word is between one of the <i>from</i> and <i>to</i> pairs inclusive. The comma and <i>to</i> are optional; <i>to</i> defaults to the same value as <i>from</i>. The numbers may be negative: <code>&#8211;</code><i>n</i> refers to the <i>n</i>&#8216;th last word on the line.</p>
<dt><code>c[</code><i>offset</i><code>,</code><i>string</i><code>]</code>&#8230;</p>
<dd> Matches if the <i>string</i> matches the word offset by <i>offset</i> from the current word position. Usually <i>offset</i> will be negative.</p>
<dt><code>C[</code><i>offset</i><code>,</code><i>pattern</i><code>]</code>&#8230;</p>
<dd> Like <code>c</code> but using pattern matching instead.</p>
<dt><code>w[</code><i>index</i><code>,</code><i>string</i><code>]</code>&#8230;</p>
<dd> Matches if the word in position <i>index</i> is equal to the corresponding <i>string</i>. Note that the word count is made after any alias expansion.</p>
<dt><code>W[</code><i>index</i><code>,</code><i>pattern</i><code>]</code>&#8230;</p>
<dd> Like <code>w</code> but using pattern matching instead.</p>
<dt><code>n[</code><i>index</i><code>,</code><i>string</i><code>]</code>&#8230;</p>
<dd> Matches if the current word contains <i>string</i>. Anything up to and including the <i>index</i>th occurrence of this string will not be considered part of the completion, but the rest will. <i>index</i> may be negative to count from the end: in most cases, <i>index</i> will be 1 or -1. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>compctl -s '`users`' -x 'n[1,@]' -k hosts -- talk</code>
</pre>
</dl>
<p> will usually complete usernames, but if you insert an <code>@</code> after the name, names from the array <i>hosts</i> (assumed to contain hostnames, though you must make the array yourself) will be completed. Other commands such as <code>rcp</code> can be handled similarly.</dl>
<dt><code>N[</code><i>index</i><code>,</code><i>string</i><code>]</code>&#8230;</p>
<dd> Like <code>n</code> except that the string will be taken as a character class. Anything up to and including the <i>index</i>th occurrence of any of the characters in <i>string</i> will not be considered part of the completion.</p>
<dt><code>m[</code><i>min</i><code>,</code><i>max</i><code>]</code>&#8230;</p>
<dd> Matches if the total number of words lies between <i>min</i> and <i>max</i> inclusive.</p>
<dt><code>r[</code><i>str1</i><code>,</code><i>str2</i><code>]</code>&#8230;</p>
<dd> Matches if the cursor is after a word with prefix <i>str1</i>. If there is also a word with prefix <i>str2</i> on the command line after the one matched by <i>str1</i> it matches only if the cursor is before this word. If the comma and <i>str2</i> are omitted, it matches if the cursor is after a word with prefix <i>str1</i>.</p>
<dt><code>R[</code><i>str1</i><code>,</code><i>str2</i><code>]</code>&#8230;</p>
<dd> Like <code>r</code> but using pattern matching instead.</p>
<dt><code>q[</code><i>str</i><code>]</code>&#8230;</p>
<dd> Matches the word currently being completed is in single quotes and the <i>str</i> begins with the letter `s&#8217;, or if completion is done in double quotes and <i>str</i> starts with the letter `d&#8217;, or if completion is done in backticks and <i>str</i> starts with a `b&#8217;.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
compctl &#8211; u &#8211; x &#8216;s[+] c[-1,-f],s[-f+]&#8217; \<br />
  &#8211; g &#8216;~/Mail/*(:t)&#8217; &#8211;<br />
    &#8216;s[-f],c[-1,-f]&#8217; &#8211; f&#8211; mail
</dl>
<p> This is to be interpreted as follows: </p>
<p> If the current command is <code>mail</code>, then </p>
<dl>
<dt>
<dd>
<pre><code>
if ((the current word begins with + and the previous word is - f) or (the current word begins with - f +)), then complete the
non-directory part (the `:t' glob modifier) of files in the directory
~/Mail; else
if the current word begins with -f or the previous word was -f, then
complete any file; else
complete user names.
</code></pre>
</dl>
<h2>Index</h2>
