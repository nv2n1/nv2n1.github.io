---
title: "zshoptions(1)"
name: "zshoptions"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshoptions/"
description: "zshoptions – zsh options"
---

<h2 class="name">NAME</h2>
<p> zshoptions &#8211; zsh options </p>
<h2>SPECIFYING OPTIONS</h2>
<p> Options are primarily referred to by name. These names are case insensitive and underscores are ignored. For example, `<code>allexport</code>&#8216; is equivalent to `<code>A__lleXP_ort</code>&#8216;. </p>
<p> The sense of an option name may be inverted by preceding it with `<code>no</code>&#8216;, so `<code>setopt No_Beep</code>&#8216; is equivalent to `<code>unsetopt beep</code>&#8216;. This inversion can only be done once, so `<code>nonobeep</code>&#8216; is <i>not</i> a synonym for `<code>beep</code>&#8216;. Similarly, `<code>tify</code>&#8216; is not a synonym for `<code>nonotify</code>&#8216; (the inversion of `<code>notify</code>&#8216;). </p>
<p> Some options also have one or more single letter names. There are two sets of single letter options: one used by default, and another used to emulate <code>sh</code>/<code>ksh</code> (used when the <code>SH_OPTION_LETTERS</code> option is set). The single letter options can be used on the shell command line, or with the <code>set</code>, <code>setopt</code> and <code>unsetopt</code> builtins, as normal Unix options preceded by `<code>&#8211;</code>&#8216;. </p>
<p> The sense of the single letter options may be inverted by using `<code>+</code>&#8216; instead of `<code>&#8211;</code>&#8216;. Some of the single letter option names refer to an option being off, in which case the inversion of that name refers to the option being on. For example, `<code>+n</code>&#8216; is the short name of `<code>exec</code>&#8216;, and `<code>-n</code>&#8216; is the short name of its inversion, `<code>noexec</code>&#8216;. </p>
<p> In strings of single letter options supplied to the shell at startup, trailing whitespace will be ignored; for example the string `<code>-f </code>&#8216; will be treated just as `<code>-f</code>&#8216;, but the string `<code>-f i</code>&#8216; is an error. This is because many systems which implement the `<code>#!</code>&#8216; mechanism for calling scripts do not strip trailing whitespace. </p>
<h2>DESCRIPTION OF OPTIONS</h2>
<p> In the following list, options set by default in all emulations are marked &lt;D&gt;; those set by default only in csh, ksh, sh, or zsh emulations are marked &lt;C&gt;, &lt;K&gt;, &lt;S&gt;, &lt;Z&gt; as appropriate. When listing options (by `<code>setopt</code>&#8216;, `<code>unsetopt</code>&#8216;, `<code>set -o</code>&#8216; or `<code>set +o</code>&#8216;), those turned on by default appear in the list prefixed with `<code>no</code>&#8216;. Hence (unless <code>KSH_OPTION_PRINT</code> is set), `<code>setopt</code>&#8216; shows all options whose settings are changed from the default. </p>
<h3>Changing Directories</h3>
<dl>
<dt>
<dd> <code>AUTO_CD</code> (<code>-J</code>) If a command is issued that can&#8217;t be executed as a normal command, and the command is the name of a directory, perform the <code>cd</code> command to that directory. This option is only applicable if the option <code>SHIN_STDIN</code> is set, i.e. if commands are being read from standard input. The option is designed for interactive use; it is recommended that <code>cd</code> be used explicitly in scripts to avoid ambiguity.</p>
<dt><code>AUTO_PUSHD</code> (<code>-N</code>)</p>
<dd> Make <code>cd</code> push the old directory onto the directory stack.</p>
<dt><code>CDABLE_VARS</code> (<code>-T</code>)</p>
<dd> If the argument to a <code>cd</code> command (or an implied <code>cd</code> with the <code>AUTO_CD</code> option set) is not a directory, and does not begin with a slash, try to expand the expression as if it were preceded by a `<code>~</code>&#8216; (see the section `Filename Expansion&#8217;).</p>
<dt><code>CD_SILENT</code></p>
<dd> Never print the working directory after a <code>cd</code> (whether explicit or implied with the <code>AUTO_CD</code> option set). <code>cd</code> normally prints the working directory when the argument given to it was <code>&#8211;</code>, a stack entry, or the name of a directory found under <code>CDPATH</code>. Note that this is distinct from <code>pushd</code>&#8216;s stack-printing behaviour, which is controlled by <code>PUSHD_SILENT</code>. This option overrides the printing-related effects of <code>POSIX_CD</code>.</p>
<dt><code>CHASE_DOTS</code></p>
<dd> When changing to a directory containing a path segment `<code>..</code>&#8216; which would otherwise be treated as canceling the previous segment in the path (in other words, `<code>foo/..</code>&#8216; would be removed from the path, or if `<code>..</code>&#8216; is the first part of the path, the last part of the current working directory would be removed), instead resolve the path to the physical directory. This option is overridden by <code>CHASE_LINKS</code>.</p>
<dl>
<dt>
<dd>
<p> For example, suppose <code>/foo/bar</code> is a link to the directory <code>/alt/rod</code>. Without this option set, `<code>cd /foo/bar/..</code>&#8216; changes to <code>/foo</code>; with it set, it changes to <code>/alt</code>. The same applies if the current directory is <code>/foo/bar</code> and `<code>cd ..</code>&#8216; is used. Note that all other symbolic links in the path will also be resolved.</dl>
<dt><code>CHASE_LINKS</code> (<code>-w</code>)</p>
<dd> Resolve symbolic links to their true values when changing directory. This also has the effect of <code>CHASE_DOTS</code>, i.e. a `<code>..</code>&#8216; path segment will be treated as referring to the physical parent, even if the preceding path segment is a symbolic link.</p>
<dt><code>POSIX_CD</code> &lt;K&gt; &lt;S&gt;</p>
<dd> Modifies the behaviour of <code>cd</code>, <code>chdir</code> and <code>pushd</code> commands to make them more compatible with the POSIX standard. The behaviour with the option unset is described in the documentation for the <code>cd</code> builtin in <i><a href="/docs/linux/man/1-zshbuiltins/">zshbuiltins</a></i>(1). If the option is set, the shell does not test for directories beneath the local directory (`<code>.</code>&#8216;) until after all directories in <code>cdpath</code> have been tested, and the <code>cd</code> and <code>chdir</code> commands do not recognise arguments of the form `{<code>+</code>|<code>&#8211;</code>}<i>n</i>&#8216; as directory stack entries.</p>
<dl>
<dt>
<dd>
<p> Also, if the option is set, the conditions under which the shell prints the new directory after changing to it are modified. It is no longer restricted to interactive shells (although printing of the directory stack with <code>pushd</code> is still limited to interactive shells); and any use of a component of <code>CDPATH</code>, including a `<code>.</code>&#8216; but excluding an empty component that is otherwise treated as `<code>.</code>&#8216;, causes the directory to be printed.</dl>
<dt><code>PUSHD_IGNORE_DUPS</code></p>
<dd> Don&#8217;t push multiple copies of the same directory onto the directory stack.</p>
<dt><code>PUSHD_MINUS</code></p>
<dd> Exchanges the meanings of `<code>+</code>&#8216; and `<code>&#8211;</code>&#8216; when used with a number to specify a directory in the stack.</p>
<dt><code>PUSHD_SILENT</code> (<code>-E</code>)</p>
<dd> Do not print the directory stack after <code>pushd</code> or <code>popd</code>.</p>
<dt><code>PUSHD_TO_HOME</code> (<code>-D</code>)</p>
<dd> Have <code>pushd</code> with no arguments act like `<code>pushd $HOME</code>&#8216;.</dl>
<h3>Completion</h3>
<dl>
<dt>
<dd> <code>ALWAYS_LAST_PROMPT</code> &lt;D&gt; If unset, key functions that list completions try to return to the last prompt if given a numeric argument. If set these functions try to return to the last prompt if given <i>no</i> numeric argument.</p>
<dt><code>ALWAYS_TO_END</code></p>
<dd> If a completion is performed with the cursor within a word, and a full completion is inserted, the cursor is moved to the end of the word. That is, the cursor is moved to the end of the word if either a single match is inserted or menu completion is performed.</p>
<dt><code>AUTO_LIST</code> (<code>-9</code>) &lt;D&gt;</p>
<dd> Automatically list choices on an ambiguous completion.</p>
<dt><code>AUTO_MENU</code> &lt;D&gt;</p>
<dd> Automatically use menu completion after the second consecutive request for completion, for example by pressing the tab key repeatedly. This option is overridden by <code>MENU_COMPLETE</code>.</p>
<dt><code>AUTO_NAME_DIRS</code></p>
<dd> Any parameter that is set to the absolute name of a directory immediately becomes a name for that directory, that will be used by the `<code>%~</code>&#8216; and related prompt sequences, and will be available when completion is performed on a word starting with `<code>~</code>&#8216;. (Otherwise, the parameter must be used in the form `<code>~</code><i>param</i>&#8216; first.)</p>
<dt><code>AUTO_PARAM_KEYS</code> &lt;D&gt;</p>
<dd> If a parameter name was completed and a following character (normally a space) automatically inserted, and the next character typed is one of those that have to come directly after the name (like `<code>}</code>&#8216;, `<code>:</code>&#8216;, etc.), the automatically added character is deleted, so that the character typed comes immediately after the parameter name. Completion in a brace expansion is affected similarly: the added character is a `<code>,</code>&#8216;, which will be removed if `<code>}</code>&#8216; is typed next.</p>
<dt><code>AUTO_PARAM_SLASH</code> &lt;D&gt;</p>
<dd> If a parameter is completed whose content is the name of a directory, then add a trailing slash instead of a space.</p>
<dt><code>AUTO_REMOVE_SLASH</code> &lt;D&gt;</p>
<dd> When the last character resulting from a completion is a slash and the next character typed is a word delimiter, a slash, or a character that ends a command (such as a semicolon or an ampersand), remove the slash.</p>
<dt><code>BASH_AUTO_LIST</code></p>
<dd> On an ambiguous completion, automatically list choices when the completion function is called twice in succession. This takes precedence over <code>AUTO_LIST</code>. The setting of <code>LIST_AMBIGUOUS</code> is respected. If <code>AUTO_MENU</code> is set, the menu behaviour will then start with the third press. Note that this will not work with <code>MENU_COMPLETE</code>, since repeated completion calls immediately cycle through the list in that case.</p>
<dt><code>COMPLETE_ALIASES</code></p>
<dd> Prevents aliases on the command line from being internally substituted before completion is attempted. The effect is to make the alias a distinct command for completion purposes.</p>
<dt><code>COMPLETE_IN_WORD</code></p>
<dd> If unset, the cursor is set to the end of the word if completion is started. Otherwise it stays there and completion is done from both ends.</p>
<dt><code>GLOB_COMPLETE</code></p>
<dd> When the current word has a glob pattern, do not insert all the words resulting from the expansion but generate matches as for completion and cycle through them like <code>MENU_COMPLETE</code>. The matches are generated as if a `<code>*</code>&#8216; was added to the end of the word, or inserted at the cursor when <code>COMPLETE_IN_WORD</code> is set. This actually uses pattern matching, not globbing, so it works not only for files but for any completion, such as options, user names, etc.</p>
<dl>
<dt>
<dd>
<p> Note that when the pattern matcher is used, matching control (for example, case-insensitive or anchored matching) cannot be used. This limitation only applies when the current word contains a pattern; simply turning on the <code>GLOB_COMPLETE</code> option does not have this effect.</dl>
<dt><code>HASH_LIST_ALL</code> &lt;D&gt;</p>
<dd> Whenever a command completion or spelling correction is attempted, make sure the entire command path is hashed first. This makes the first completion slower but avoids false reports of spelling errors.</p>
<dt><code>LIST_AMBIGUOUS</code> &lt;D&gt;</p>
<dd> This option works when <code>AUTO_LIST</code> or <code>BASH_AUTO_LIST</code> is also set. If there is an unambiguous prefix to insert on the command line, that is done without a completion list being displayed; in other words, auto-listing behaviour only takes place when nothing would be inserted. In the case of <code>BASH_AUTO_LIST</code>, this means that the list will be delayed to the third call of the function.</p>
<dt><code>LIST_BEEP</code> &lt;D&gt;</p>
<dd> Beep on an ambiguous completion. More accurately, this forces the completion widgets to return status 1 on an ambiguous completion, which causes the shell to beep if the option <code>BEEP</code> is also set; this may be modified if completion is called from a user-defined widget.</p>
<dt><code>LIST_PACKED</code></p>
<dd> Try to make the completion list smaller (occupying less lines) by printing the matches in columns with different widths.</p>
<dt><code>LIST_ROWS_FIRST</code></p>
<dd> Lay out the matches in completion lists sorted horizontally, that is, the second match is to the right of the first one, not under it as usual.</p>
<dt><code>LIST_TYPES</code> (<code>-X</code>) &lt;D&gt;</p>
<dd> When listing files that are possible completions, show the type of each file with a trailing identifying mark.</p>
<dt><code>MENU_COMPLETE</code> (<code>-Y</code>)</p>
<dd> On an ambiguous completion, instead of listing possibilities or beeping, insert the first match immediately. Then when completion is requested again, remove the first match and insert the second match, etc. When there are no more matches, go back to the first one again. <code>reverse-menu-complete</code> may be used to loop through the list in the other direction. This option overrides <code>AUTO_MENU</code>.</p>
<dt><code>REC_EXACT</code> (<code>-S</code>)</p>
<dd> If the string on the command line exactly matches one of the possible completions, it is accepted, even if there is another completion (i.e. that string with something else added) that also matches.</dl>
<h3>Expansion and Globbing</h3>
<dl>
<dt>
<dd> <code>BAD_PATTERN</code> (<code>+2</code>) &lt;C&gt; &lt;Z&gt; If a pattern for filename generation is badly formed, print an error message. (If this option is unset, the pattern will be left unchanged.)</p>
<dt><code>BARE_GLOB_QUAL</code> &lt;Z&gt;</p>
<dd> In a glob pattern, treat a trailing set of parentheses as a qualifier list, if it contains no `<code>|</code>&#8216;, `<code>(</code>&#8216; or (if special) `<code>~</code>&#8216; characters. See the section `Filename Generation&#8217;.</p>
<dt><code>BRACE_CCL</code></p>
<dd> Expand expressions in braces which would not otherwise undergo brace expansion to a lexically ordered list of all the characters. See the section `Brace Expansion&#8217;.</p>
<dt><code>CASE_GLOB</code> &lt;D&gt;</p>
<dd> Make globbing (filename generation) sensitive to case. Note that other uses of patterns are always sensitive to case. If the option is unset, the presence of any character which is special to filename generation will cause case-insensitive matching. For example, <code>cvs(/)</code> can match the directory <code>CVS</code> owing to the presence of the globbing flag (unless the option <code>BARE_GLOB_QUAL</code> is unset).</p>
<dt><code>CASE_MATCH</code> &lt;D&gt;</p>
<dd> Make regular expressions using the <code>zsh/regex</code> module (including matches with <code>=~</code>) sensitive to case.</p>
<dt><code>CSH_NULL_GLOB</code> &lt;C&gt;</p>
<dd> If a pattern for filename generation has no matches, delete the pattern from the argument list; do not report an error unless all the patterns in a command have no matches. Overrides <code>NOMATCH</code>.</p>
<dt><code>EQUALS</code> &lt;Z&gt;</p>
<dd> Perform <code>=</code> filename expansion. (See the section `Filename Expansion&#8217;.)</p>
<dt><code>EXTENDED_GLOB</code></p>
<dd> Treat the `<code>#</code>&#8216;, `<code>~</code>&#8216; and `<code>^</code>&#8216; characters as part of patterns for filename generation, etc. (An initial unquoted `<code>~</code>&#8216; always produces named directory expansion.)</p>
<dt><code>FORCE_FLOAT</code></p>
<dd> Constants in arithmetic evaluation will be treated as floating point even without the use of a decimal point; the values of integer variables will be converted to floating point when used in arithmetic expressions. Integers in any base will be converted.</p>
<dt><code>GLOB</code> (<code>+F</code>, ksh: <code>+f</code>) &lt;D&gt;</p>
<dd> Perform filename generation (globbing). (See the section `Filename Generation&#8217;.)</p>
<dt><code>GLOB_ASSIGN</code> &lt;C&gt;</p>
<dd> If this option is set, filename generation (globbing) is performed on the right hand side of scalar parameter assignments of the form `<i>name</i><code>=</code><i>pattern</i> (e.g. `<code>foo=*</code>&#8216;). If the result has more than one word the parameter will become an array with those words as arguments. This option is provided for backwards compatibility only: globbing is always performed on the right hand side of array assignments of the form `<i>name</i><code>=(</code><i>value</i><code>)</code>&#8216; (e.g. `<code>foo=(*)</code>&#8216;) and this form is recommended for clarity; with this option set, it is not possible to predict whether the result will be an array or a scalar.</p>
<dt><code>GLOB_DOTS</code> (<code>-4</code>)</p>
<dd> Do not require a leading `<code>.</code>&#8216; in a filename to be matched explicitly.</p>
<dt><code>GLOB_STAR_SHORT</code></p>
<dd> When this option is set and the default zsh-style globbing is in effect, the pattern `<code>**/*</code>&#8216; can be abbreviated to `<code>**</code>&#8216; and the pattern `<code>***/*</code>&#8216; can be abbreviated to <code>***</code>. Hence `<code>**.c</code>&#8216; finds a file ending in <code>.c</code> in any subdirectory, and `<code>***.c</code>&#8216; does the same while also following symbolic links. A <code>/</code> immediately after the `<code>**</code>&#8216; or `<code>***</code>&#8216; forces the pattern to be treated as the unabbreviated form.</p>
<dt><code>GLOB_SUBST</code> &lt;C&gt; &lt;K&gt; &lt;S&gt;</p>
<dd> Treat any characters resulting from parameter expansion as being eligible for filename expansion and filename generation, and any characters resulting from command substitution as being eligible for filename generation. Braces (and commas in between) do not become eligible for expansion.</p>
<dt><code>HIST_SUBST_PATTERN</code></p>
<dd> Substitutions using the <code>:s</code> and <code>:&amp;</code> history modifiers are performed with pattern matching instead of string matching. This occurs wherever history modifiers are valid, including glob qualifiers and parameters. See the section Modifiers in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1).</p>
<dt><code>IGNORE_BRACES</code> (<code>-I</code>) &lt;S&gt;</p>
<dd> Do not perform brace expansion. For historical reasons this also includes the effect of the <code>IGNORE_CLOSE_BRACES</code> option.</p>
<dt><code>IGNORE_CLOSE_BRACES</code></p>
<dd> When neither this option nor <code>IGNORE_BRACES</code> is set, a sole close brace character `<code>}</code>&#8216; is syntactically significant at any point on a command line. This has the effect that no semicolon or newline is necessary before the brace terminating a function or current shell construct. When either option is set, a closing brace is syntactically significant only in command position. Unlike <code>IGNORE_BRACES</code>, this option does not disable brace expansion.</p>
<dl>
<dt>
<dd>
<p> For example, with both options unset a function may be defined in the following fashion: </p>
<dl>
<dt>
<dd>
<pre>
<code>args() { echo $# }</code>
</pre>
</dl>
<p> while if either option is set, this does not work and something equivalent to the following is required: </p>
<dl>
<dt>
<dd>
<pre>
<code>args() { echo $#; }</code>
</pre>
</dl>
</dl>
<dt><code>KSH_GLOB</code> &lt;K&gt;</p>
<dd> In pattern matching, the interpretation of parentheses is affected by a preceding `<code>@</code>&#8216;, `<code>*</code>&#8216;, `<code>+</code>&#8216;, `<code>?</code>&#8216; or `<code>!</code>&#8216;. See the section `Filename Generation&#8217;.</p>
<dt><code>MAGIC_EQUAL_SUBST</code></p>
<dd> All unquoted arguments of the form `<i>anything</i><code>=</code><i>expression</i>&#8216; appearing after the command name have filename expansion (that is, where <i>expression</i> has a leading `<code>~</code>&#8216; or `<code>=</code>&#8216;) performed on <i>expression</i> as if it were a parameter assignment. The argument is not otherwise treated specially; it is passed to the command as a single argument, and not used as an actual parameter assignment. For example, in <code>echo foo=~/bar:~/rod</code>, both occurrences of <code>~</code> would be replaced. Note that this happens anyway with <code>typeset</code> and similar statements.</p>
<dl>
<dt>
<dd>
<p> This option respects the setting of the <code>KSH_TYPESET</code> option. In other words, if both options are in effect, arguments looking like assignments will not undergo word splitting.</dl>
<dt><code>MARK_DIRS</code> (<code>-8</code>, ksh: <code>-X</code>)</p>
<dd> Append a trailing `<code>/</code>&#8216; to all directory names resulting from filename generation (globbing).</p>
<dt><code>MULTIBYTE</code> &lt;D&gt;</p>
<dd> Respect multibyte characters when found in strings. When this option is set, strings are examined using the system library to determine how many bytes form a character, depending on the current locale. This affects the way characters are counted in pattern matching, parameter values and various delimiters.</p>
<dl>
<dt>
<dd>
<p> The option is on by default if the shell was compiled with <code>MULTIBYTE_SUPPORT</code>; otherwise it is off by default and has no effect if turned on. </p>
<p> If the option is off a single byte is always treated as a single character. This setting is designed purely for examining strings known to contain raw bytes or other values that may not be characters in the current locale. It is not necessary to unset the option merely because the character set for the current locale does not contain multibyte characters. </p>
<p> The option does not affect the shell&#8217;s editor, which always uses the locale to determine multibyte characters. This is because the character set displayed by the terminal emulator is independent of shell settings.</dl>
<dt><code>NOMATCH</code> (<code>+3</code>) &lt;C&gt; &lt;Z&gt;</p>
<dd> If a pattern for filename generation has no matches, print an error, instead of leaving it unchanged in the argument list. This also applies to file expansion of an initial `<code>~</code>&#8216; or `<code>=</code>&#8216;.</p>
<dt><code>NULL_GLOB</code> (<code>-G</code>)</p>
<dd> If a pattern for filename generation has no matches, delete the pattern from the argument list instead of reporting an error. Overrides <code>NOMATCH</code>.</p>
<dt><code>NUMERIC_GLOB_SORT</code></p>
<dd> If numeric filenames are matched by a filename generation pattern, sort the filenames numerically rather than lexicographically.</p>
<dt><code>RC_EXPAND_PARAM</code> (<code>-P</code>)</p>
<dd> Array expansions of the form `<i>foo</i><code>${</code><i>xx</i><code>}</code><i>bar</i>&#8216;, where the parameter <i>xx</i> is set to <code>(</code><i>a b c</i><code>)</code>, are substituted with `<i>fooabar foobbar foocbar</i>&#8216; instead of the default `<i>fooa b cbar</i>&#8216;. Note that an empty array will therefore cause all arguments to be removed.</p>
<dt><code>REMATCH_PCRE</code></p>
<dd> If set, regular expression matching with the <code>=~</code> operator will use Perl-Compatible Regular Expressions from the PCRE library. (The <code>zsh/pcre</code> module must be available.) If not set, regular expressions will use the extended regexp syntax provided by the system libraries.</p>
<dt><code>SH_GLOB</code> &lt;K&gt; &lt;S&gt;</p>
<dd> Disables the special meaning of `<code>(</code>&#8216;, `<code>|</code>&#8216;, `<code>)</code>&#8216; and &#8216;<code>&lt;</code>&#8216; for globbing the result of parameter and command substitutions, and in some other places where the shell accepts patterns. If <code>SH_GLOB</code> is set but <code>KSH_GLOB</code> is not, the shell allows the interpretation of subshell expressions enclosed in parentheses in some cases where there is no space before the opening parenthesis, e.g. <code>!(true)</code> is interpreted as if there were a space after the <code>!</code>. This option is set by default if zsh is invoked as <code>sh</code> or <code>ksh</code>.</p>
<dt><code>UNSET</code> (<code>+u</code>, ksh: <code>+u</code>) &lt;K&gt; &lt;S&gt; &lt;Z&gt;</p>
<dd> Treat unset parameters as if they were empty when substituting, and as if they were zero when reading their values in arithmetic expansion and arithmetic commands. Otherwise they are treated as an error.</p>
<dt><code>WARN_CREATE_GLOBAL</code></p>
<dd> Print a warning message when a global parameter is created in a function by an assignment or in math context. This often indicates that a parameter has not been declared local when it should have been. Parameters explicitly declared global from within a function using <code>typeset -g</code> do not cause a warning. Note that there is no warning when a local parameter is assigned to in a nested function, which may also indicate an error.</p>
<dt><code>WARN_NESTED_VAR</code></p>
<dd> Print a warning message when an existing parameter from an enclosing function scope, or global, is set in a function by an assignment or in math context. Assignment to shell special parameters does not cause a warning. This is the companion to <code>WARN_CREATE_GLOBAL</code> as in this case the warning is only printed when a parameter is <i>not</i> created. Where possible, use of <code>typeset -g</code> to set the parameter suppresses the error, but note that this needs to be used every time the parameter is set. To restrict the effect of this option to a single function scope, use `<code>functions -W</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> For example, the following code produces a warning for the assignment inside the function <code>nested</code> as that overrides the value within <code>toplevel</code> </p>
<dl>
<dt>
<dd>
<pre><code>
toplevel(){
    local foo = "in fn" nested} nested(){
    foo = "in nested"} setopt warn_nested_var
    toplevel
</code></pre>
</dl>
</dl>
</dl>
<h3>History</h3>
<dl>
<dt>
<dd> <code>APPEND_HISTORY</code> &lt;D&gt; If this is set, zsh sessions will append their history list to the history file, rather than replace it. Thus, multiple parallel zsh sessions will all have the new entries from their history lists added to the history file, in the order that they exit. The file will still be periodically re-written to trim it when the number of lines grows 20% beyond the value specified by <code>$SAVEHIST</code> (see also the <code>HIST_SAVE_BY_COPY</code> option).</p>
<dt><code>BANG_HIST</code> (<code>+K</code>) &lt;C&gt; &lt;Z&gt;</p>
<dd> Perform textual history expansion, <code>csh</code>-style, treating the character `<code>!</code>&#8216; specially.</p>
<dt><code>EXTENDED_HISTORY</code> &lt;C&gt;</p>
<dd> Save each command&#8217;s beginning timestamp (in seconds since the epoch) and the duration (in seconds) to the history file. The format of this prefixed data is:</p>
<dl>
<dt>
<dd>
<p> `<code>: </code><i>&lt;beginning time&gt;</i><code>:</code><i>&lt;elapsed seconds&gt;</i><code>;</code><i>&lt;command&gt;</i>&#8216;.</dl>
<dt><code>HIST_ALLOW_CLOBBER</code></p>
<dd> Add `<code>|</code>&#8216; to output redirections in the history. This allows history references to clobber files even when <code>CLOBBER</code> is unset.</p>
<dt><code>HIST_BEEP</code> &lt;D&gt;</p>
<dd> Beep in ZLE when a widget attempts to access a history entry which isn&#8217;t there.</p>
<dt><code>HIST_EXPIRE_DUPS_FIRST</code></p>
<dd> If the internal history needs to be trimmed to add the current command line, setting this option will cause the oldest history event that has a duplicate to be lost before losing a unique event from the list. You should be sure to set the value of <code>HISTSIZE</code> to a larger number than <code>SAVEHIST</code> in order to give you some room for the duplicated events, otherwise this option will behave just like <code>HIST_IGNORE_ALL_DUPS</code> once the history fills up with unique events.</p>
<dt><code>HIST_FCNTL_LOCK</code></p>
<dd> When writing out the history file, by default zsh uses ad-hoc file locking to avoid known problems with locking on some operating systems. With this option locking is done by means of the system&#8217;s <code>fcntl</code> call, where this method is available. On recent operating systems this may provide better performance, in particular avoiding history corruption when files are stored on NFS.</p>
<dt><code>HIST_FIND_NO_DUPS</code></p>
<dd> When searching for history entries in the line editor, do not display duplicates of a line previously found, even if the duplicates are not contiguous.</p>
<dt><code>HIST_IGNORE_ALL_DUPS</code></p>
<dd> If a new command line being added to the history list duplicates an older one, the older command is removed from the list (even if it is not the previous event).</p>
<dt><code>HIST_IGNORE_DUPS</code> (<code>-h</code>)</p>
<dd> Do not enter command lines into the history list if they are duplicates of the previous event.</p>
<dt><code>HIST_IGNORE_SPACE</code> (<code>-g</code>)</p>
<dd> Remove command lines from the history list when the first character on the line is a space, or when one of the expanded aliases contains a leading space. Only normal aliases (not global or suffix aliases) have this behaviour. Note that the command lingers in the internal history until the next command is entered before it vanishes, allowing you to briefly reuse or edit the line. If you want to make it vanish right away without entering another command, type a space and press return.</p>
<dt><code>HIST_LEX_WORDS</code></p>
<dd> By default, shell history that is read in from files is split into words on all white space. This means that arguments with quoted whitespace are not correctly handled, with the consequence that references to words in history lines that have been read from a file may be inaccurate. When this option is set, words read in from a history file are divided up in a similar fashion to normal shell command line handling. Although this produces more accurately delimited words, if the size of the history file is large this can be slow. Trial and error is necessary to decide.</p>
<dt><code>HIST_NO_FUNCTIONS</code></p>
<dd> Remove function definitions from the history list. Note that the function lingers in the internal history until the next command is entered before it vanishes, allowing you to briefly reuse or edit the definition.</p>
<dt><code>HIST_NO_STORE</code></p>
<dd> Remove the <code>history</code> (<code>fc -l</code>) command from the history list when invoked. Note that the command lingers in the internal history until the next command is entered before it vanishes, allowing you to briefly reuse or edit the line.</p>
<dt><code>HIST_REDUCE_BLANKS</code></p>
<dd> Remove superfluous blanks from each command line being added to the history list.</p>
<dt><code>HIST_SAVE_BY_COPY</code> &lt;D&gt;</p>
<dd> When the history file is re-written, we normally write out a copy of the file named <code>$HISTFILE.new</code> and then rename it over the old one. However, if this option is unset, we instead truncate the old history file and write out the new version in-place. If one of the history-appending options is enabled, this option only has an effect when the enlarged history file needs to be re-written to trim it down to size. Disable this only if you have special needs, as doing so makes it possible to lose history entries if zsh gets interrupted during the save.</p>
<dl>
<dt>
<dd>
<p> When writing out a copy of the history file, zsh preserves the old file&#8217;s permissions and group information, but will refuse to write out a new file if it would change the history file&#8217;s owner.</dl>
<dt><code>HIST_SAVE_NO_DUPS</code></p>
<dd> When writing out the history file, older commands that duplicate newer ones are omitted.</p>
<dt><code>HIST_VERIFY</code></p>
<dd> Whenever the user enters a line with history expansion, don&#8217;t execute the line directly; instead, perform history expansion and reload the line into the editing buffer.</p>
<dt><code>INC_APPEND_HISTORY</code></p>
<dd> This option works like <code>APPEND_HISTORY</code> except that new history lines are added to the <code>$HISTFILE</code> incrementally (as soon as they are entered), rather than waiting until the shell exits. The file will still be periodically re-written to trim it when the number of lines grows 20% beyond the value specified by <code>$SAVEHIST</code> (see also the <code>HIST_SAVE_BY_COPY</code> option).</p>
<dt><code>INC_APPEND_HISTORY_TIME</code></p>
<dd> This option is a variant of <code>INC_APPEND_HISTORY</code> in which, where possible, the history entry is written out to the file after the command is finished, so that the time taken by the command is recorded correctly in the history file in <code>EXTENDED_HISTORY</code> format. This means that the history entry will not be available immediately from other instances of the shell that are using the same history file.</p>
<dl>
<dt>
<dd>
<p> This option is only useful if <code>INC_APPEND_HISTORY</code> and <code>SHARE_HISTORY</code> are turned off. The three options should be considered mutually exclusive.</dl>
<dt><code>SHARE_HISTORY</code> &lt;K&gt;</p>
<dd>
<dl>
<dt>
<dd>
<p> This option both imports new commands from the history file, and also causes your typed commands to be appended to the history file (the latter is like specifying <code>INC_APPEND_HISTORY</code>, which should be turned off if this option is in effect). The history lines are also output with timestamps ala <code>EXTENDED_HISTORY</code> (which makes it easier to find the spot where we left off reading the file after it gets re-written). </p>
<p> By default, history movement commands visit the imported lines as well as the local lines, but you can toggle this on and off with the set-local-history zle binding. It is also possible to create a zle widget that will make some commands ignore imported commands, and some include them. </p>
<p> If you find that you want more control over when commands get imported, you may wish to turn <code>SHARE_HISTORY</code> off, <code>INC_APPEND_HISTORY</code> or <code>INC_APPEND_HISTORY_TIME</code> (see above) on, and then manually import commands whenever you need them using `<code>fc -RI</code>&#8216;.</dl>
</dl>
<h3>Initialisation</h3>
<dl>
<dt>
<dd> <code>ALL_EXPORT</code> (<code>-a</code>, ksh: <code>-a</code>) All parameters subsequently defined are automatically exported.</p>
<dt><code>GLOBAL_EXPORT</code> &lt;Z&gt;</p>
<dd> If this option is set, passing the <code>-x</code> flag to the builtins <code>declare</code>, <code>float</code>, <code>integer</code>, <code>readonly</code> and <code>typeset</code> (but not <code>local</code>) will also set the <code>-g</code> flag; hence parameters exported to the environment will not be made local to the enclosing function, unless they were already or the flag <code>+g</code> is given explicitly. If the option is unset, exported parameters will be made local in just the same way as any other parameter.</p>
<dl>
<dt>
<dd>
<p> This option is set by default for backward compatibility; it is not recommended that its behaviour be relied upon. Note that the builtin <code>export</code> always sets both the <code>-x</code> and <code>-g</code> flags, and hence its effect extends beyond the scope of the enclosing function; this is the most portable way to achieve this behaviour.</dl>
<dt><code>GLOBAL_RCS</code> (<code>-d</code>) &lt;D&gt;</p>
<dd> If this option is unset, the startup files <code>/etc/zsh/zprofile</code>, <code>/etc/zsh/zshrc</code>, <code>/etc/zsh/zlogin</code> and <code>/etc/zsh/zlogout</code> will not be run. It can be disabled and re-enabled at any time, including inside local startup files (<code>.zshrc</code>, etc.).</p>
<dt><code>RCS</code> (<code>+f</code>) &lt;D&gt;</p>
<dd> After <code>/etc/zsh/zshenv</code> is sourced on startup, source the <code>.zshenv</code>, <code>/etc/zsh/zprofile</code>, <code>.zprofile</code>, <code>/etc/zsh/zshrc</code>, <code>.zshrc</code>, <code>/etc/zsh/zlogin</code>, <code>.zlogin</code>, and <code>.zlogout</code> files, as described in the section `Files&#8217;. If this option is unset, the <code>/etc/zsh/zshenv</code> file is still sourced, but any of the others will not be; it can be set at any time to prevent the remaining startup files after the currently executing one from being sourced.</dl>
<h3>Input/Output</h3>
<dl>
<dt>
<dd> <code>ALIASES</code> &lt;D&gt; Expand aliases.</p>
<dt><code>CLOBBER</code> (<code>+C</code>, ksh: <code>+C</code>) &lt;D&gt;</p>
<dd> Allows `<code>&gt;</code>&#8216; redirection to truncate existing files. Otherwise `<code>&gt;!</code>&#8216; or `<code>&gt;|</code>&#8216; must be used to truncate a file.</p>
<dl>
<dt>
<dd>
<p> If the option is not set, and the option <code>APPEND_CREATE</code> is also not set, `<code>&gt;&gt;!</code>&#8216; or `<code>&gt;&gt;|</code>&#8216; must be used to create a file. If either option is set, `<code>&gt;&gt;</code>&#8216; may be used.</dl>
<dt><code>CORRECT</code> (<code>-0</code>)</p>
<dd> Try to correct the spelling of commands. Note that, when the <code>HASH_LIST_ALL</code> option is not set or when some directories in the path are not readable, this may falsely report spelling errors the first time some commands are used.</p>
<dl>
<dt>
<dd>
<p> The shell variable <code>CORRECT_IGNORE</code> may be set to a pattern to match words that will never be offered as corrections.</dl>
<dt><code>CORRECT_ALL</code> (<code>-O</code>)</p>
<dd> Try to correct the spelling of all arguments in a line.</p>
<dl>
<dt>
<dd>
<p> The shell variable <code>CORRECT_IGNORE_FILE</code> may be set to a pattern to match file names that will never be offered as corrections.</dl>
<dt><code>DVORAK</code></p>
<dd> Use the Dvorak keyboard instead of the standard qwerty keyboard as a basis for examining spelling mistakes for the <code>CORRECT</code> and <code>CORRECT_ALL</code> options and the <code>spell-word</code> editor command.</p>
<dt><code>FLOW_CONTROL</code> &lt;D&gt;</p>
<dd> If this option is unset, output flow control via start/stop characters (usually assigned to ^S/^Q) is disabled in the shell&#8217;s editor.</p>
<dt><code>IGNORE_EOF</code> (<code>-7</code>)</p>
<dd> Do not exit on end-of-file. Require the use of <code>exit</code> or <code>logout</code> instead. However, ten consecutive EOFs will cause the shell to exit anyway, to avoid the shell hanging if its tty goes away.</p>
<dl>
<dt>
<dd>
<p> Also, if this option is set and the Zsh Line Editor is used, widgets implemented by shell functions can be bound to EOF (normally Control-D) without printing the normal warning message. This works only for normal widgets, not for completion widgets.</dl>
<dt><code>INTERACTIVE_COMMENTS</code> (<code>-k</code>) &lt;K&gt; &lt;S&gt;</p>
<dd> Allow comments even in interactive shells.</p>
<dt><code>HASH_CMDS</code> &lt;D&gt;</p>
<dd> Note the location of each command the first time it is executed. Subsequent invocations of the same command will use the saved location, avoiding a path search. If this option is unset, no path hashing is done at all. However, when <code>CORRECT</code> is set, commands whose names do not appear in the functions or aliases hash tables are hashed in order to avoid reporting them as spelling errors.</p>
<dt><code>HASH_DIRS</code> &lt;D&gt;</p>
<dd> Whenever a command name is hashed, hash the directory containing it, as well as all directories that occur earlier in the path. Has no effect if neither <code>HASH_CMDS</code> nor <code>CORRECT</code> is set.</p>
<dt><code>HASH_EXECUTABLES_ONLY</code></p>
<dd> When hashing commands because of <code>HASH_CMDS</code>, check that the file to be hashed is actually an executable. This option is unset by default as if the path contains a large number of commands, or consists of many remote files, the additional tests can take a long time. Trial and error is needed to show if this option is beneficial.</p>
<dt><code>MAIL_WARNING</code> (<code>-U</code>)</p>
<dd> Print a warning message if a mail file has been accessed since the shell last checked.</p>
<dt><code>PATH_DIRS</code> (<code>-Q</code>)</p>
<dd> Perform a path search even on command names with slashes in them. Thus if `<code>/usr/local/bin</code>&#8216; is in the user&#8217;s path, and he or she types `<code>X11/xinit</code>&#8216;, the command `<code>/usr/local/bin/X11/xinit</code>&#8216; will be executed (assuming it exists). Commands explicitly beginning with `<code>/</code>&#8216;, `<code>./</code>&#8216; or `<code>../</code>&#8216; are not subject to the path search. This also applies to the `<code>.</code>&#8216; and <code>source</code> builtins.</p>
<dl>
<dt>
<dd>
<p> Note that subdirectories of the current directory are always searched for executables specified in this form. This takes place before any search indicated by this option, and regardless of whether `<code>.</code>&#8216; or the current directory appear in the command search path.</dl>
<dt><code>PATH_SCRIPT</code> &lt;K&gt; &lt;S&gt;</p>
<dd> If this option is not set, a script passed as the first non-option argument to the shell must contain the name of the file to open. If this option is set, and the script does not specify a directory path, the script is looked for first in the current directory, then in the command path. See the section INVOCATION in <i><a href="/docs/linux/man/1-zsh/">zsh</a></i>(1).</p>
<dt><code>PRINT_EIGHT_BIT</code></p>
<dd> Print eight bit characters literally in completion lists, etc. This option is not necessary if your system correctly returns the printability of eight bit characters (see <i><a href="/docs/linux/man/3-ctype/">ctype</a></i>(3)).</p>
<dt><code>PRINT_EXIT_VALUE</code> (<code>-1</code>)</p>
<dd> Print the exit value of programs with non-zero exit status. This is only available at the command line in interactive shells.</p>
<dt><code>RC_QUOTES</code></p>
<dd> Allow the character sequence `<code>&#8221;</code>&#8216; to signify a single quote within singly quoted strings. Note this does not apply in quoted strings using the format <code>$&#8217;</code><i>&#8230;</i><code>&#8216;</code>, where a backslashed single quote can be used.</p>
<dt><code>RM_STAR_SILENT</code> (<code>-H</code>) &lt;K&gt; &lt;S&gt;</p>
<dd> Do not query the user before executing `<code>rm *</code>&#8216; or `<code>rm path/*</code>&#8216;.</p>
<dt><code>RM_STAR_WAIT</code></p>
<dd> If querying the user before executing `<code>rm *</code>&#8216; or `<code>rm path/*</code>&#8216;, first wait ten seconds and ignore anything typed in that time. This avoids the problem of reflexively answering `yes&#8217; to the query when one didn&#8217;t really mean it. The wait and query can always be avoided by expanding the `<code>*</code>&#8216; in ZLE (with tab).</p>
<dt><code>SHORT_LOOPS</code> &lt;C&gt; &lt;Z&gt;</p>
<dd> Allow the short forms of <code>for</code>, <code>repeat</code>, <code>select</code>, <code>if</code>, and <code>function</code> constructs.</p>
<dt><code>SUN_KEYBOARD_HACK</code> (<code>-L</code>)</p>
<dd> If a line ends with a backquote, and there are an odd number of backquotes on the line, ignore the trailing backquote. This is useful on some keyboards where the return key is too small, and the backquote key lies annoyingly close to it. As an alternative the variable <code>KEYBOARD_HACK</code> lets you choose the character to be removed.</dl>
<h3>Job Control</h3>
<dl>
<dt>
<dd> <code>AUTO_CONTINUE</code> With this option set, stopped jobs that are removed from the job table with the <code>disown</code> builtin command are automatically sent a <code>CONT</code> signal to make them running.</p>
<dt><code>AUTO_RESUME</code> (<code>-W</code>)</p>
<dd> Treat single word simple commands without redirection as candidates for resumption of an existing job.</p>
<dt><code>BG_NICE</code> (<code>-6</code>) &lt;C&gt; &lt;Z&gt;</p>
<dd> Run all background jobs at a lower priority. This option is set by default.</p>
<dt><code>CHECK_JOBS</code> &lt;Z&gt;</p>
<dd> Report the status of background and suspended jobs before exiting a shell with job control; a second attempt to exit the shell will succeed. <code>NO_CHECK_JOBS</code> is best used only in combination with <code>NO_HUP</code>, else such jobs will be killed automatically.</p>
<dl>
<dt>
<dd>
<p> The check is omitted if the commands run from the previous command line included a `<code>jobs</code>&#8216; command, since it is assumed the user is aware that there are background or suspended jobs. A `<code>jobs</code>&#8216; command run from one of the hook functions defined in the section SPECIAL FUNCTIONS in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) is not counted for this purpose.</dl>
<dt><code>CHECK_RUNNING_JOBS</code> &lt;Z&gt;</p>
<dd> Check for both running and suspended jobs when <code>CHECK_JOBS</code> is enabled. When this option is disabled, zsh checks only for suspended jobs, which matches the default behavior of bash.</p>
<dl>
<dt>
<dd>
<p> This option has no effect unless <code>CHECK_JOBS</code> is set.</dl>
<dt><code>HUP</code> &lt;Z&gt;</p>
<dd> Send the <code>HUP</code> signal to running jobs when the shell exits.</p>
<dt><code>LONG_LIST_JOBS</code> (<code>-R</code>)</p>
<dd> Print job notifications in the long format by default.</p>
<dt><code>MONITOR</code> (<code>-m</code>, ksh: <code>-m</code>)</p>
<dd> Allow job control. Set by default in interactive shells.</p>
<dt><code>NOTIFY</code> (<code>-5</code>, ksh: <code>-b</code>) &lt;Z&gt;</p>
<dd> Report the status of background jobs immediately, rather than waiting until just before printing a prompt.</p>
<dt><code>POSIX_JOBS</code> &lt;K&gt; &lt;S&gt;</p>
<dd> This option makes job control more compliant with the POSIX standard.</p>
<dl>
<dt>
<dd>
<p> When the option is not set, the <code>MONITOR</code> option is unset on entry to subshells, so that job control is no longer active. When the option is set, the <code>MONITOR</code> option and job control remain active in the subshell, but note that the subshell has no access to jobs in the parent shell. </p>
<p> When the option is not set, jobs put in the background or foreground with <code>bg</code> or <code>fg</code> are displayed with the same information that would be reported by <code>jobs</code>. When the option is set, only the text is printed. The output from <code>jobs</code> itself is not affected by the option. </p>
<p> When the option is not set, job information from the parent shell is saved for output within a subshell (for example, within a pipeline). When the option is set, the output of <code>jobs</code> is empty until a job is started within the subshell. </p>
<p> In previous versions of the shell, it was necessary to enable <code>POSIX_JOBS</code> in order for the builtin command <code>wait</code> to return the status of background jobs that had already exited. This is no longer the case.</dl>
</dl>
<h3>Prompting</h3>
<dl>
<dt>
<dd> <code>PROMPT_BANG</code> &lt;K&gt; If set, `<code>!</code>&#8216; is treated specially in prompt expansion. See EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</p>
<dt><code>PROMPT_CR</code> (<code>+V</code>) &lt;D&gt;</p>
<dd> Print a carriage return just before printing a prompt in the line editor. This is on by default as multi-line editing is only possible if the editor knows where the start of the line appears.</p>
<dt><code>PROMPT_SP</code> &lt;D&gt;</p>
<dd> Attempt to preserve a partial line (i.e. a line that did not end with a newline) that would otherwise be covered up by the command prompt due to the <code>PROMPT_CR</code> option. This works by outputting some cursor-control characters, including a series of spaces, that should make the terminal wrap to the next line when a partial line is present (note that this is only successful if your terminal has automatic margins, which is typical).</p>
<dl>
<dt>
<dd>
<p> When a partial line is preserved, by default you will see an inverse+bold character at the end of the partial line: a `<code>%</code>&#8216; for a normal user or a `<code>#</code>&#8216; for root. If set, the shell parameter <code>PROMPT_EOL_MARK</code> can be used to customize how the end of partial lines are shown. </p>
<p> NOTE: if the <code>PROMPT_CR</code> option is not set, enabling this option will have no effect. This option is on by default.</dl>
<dt><code>PROMPT_PERCENT</code> &lt;C&gt; &lt;Z&gt;</p>
<dd> If set, `<code>%</code>&#8216; is treated specially in prompt expansion. See EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</p>
<dt><code>PROMPT_SUBST</code> &lt;K&gt; &lt;S&gt;</p>
<dd> If set, <i>parameter expansion</i>, <i>command substitution</i> and <i>arithmetic expansion</i> are performed in prompts. Substitutions within prompts do not affect the command status.</p>
<dt><code>TRANSIENT_RPROMPT</code></p>
<dd> Remove any right prompt from display when accepting a command line. This may be useful with terminals with other cut/paste methods.</dl>
<h3>Scripts and Functions</h3>
<dl>
<dt>
<dd> <code>ALIAS_FUNC_DEF</code> &lt;S&gt; By default, zsh does not allow the definition of functions using the `<i>name</i> <code>()</code>&#8216; syntax if <i>name</i> was expanded as an alias: this causes an error. This is usually the desired behaviour, as otherwise the combination of an alias and a function based on the same definition can easily cause problems.</p>
<dl>
<dt>
<dd>
<p> When this option is set, aliases can be used for defining functions. </p>
<p> For example, consider the following definitions as they might occur in a startup file. </p>
<dl>
<dt>
<dd>
<pre>
<code>alias foo=bar
foo() {
  print This probably does not do what you expect.
}</code>
</pre>
</dl>
<p> Here, <code>foo</code> is expanded as an alias to <code>bar</code> before the <code>()</code> is encountered, so the function defined would be named <code>bar</code>. By default this is instead an error in native mode. Note that quoting any part of the function name, or using the keyword <code>function</code>, avoids the problem, so is recommended when the function name can also be an alias.</dl>
<dt><code>C_BASES</code></p>
<dd> Output hexadecimal numbers in the standard C format, for example `<code>0xFF</code>&#8216; instead of the usual `<code>16#FF</code>&#8216;. If the option <code>OCTAL_ZEROES</code> is also set (it is not by default), octal numbers will be treated similarly and hence appear as `<code>077</code>&#8216; instead of `<code>8#77</code>&#8216;. This option has no effect on the choice of the output base, nor on the output of bases other than hexadecimal and octal. Note that these formats will be understood on input irrespective of the setting of <code>C_BASES</code>.</p>
<dt><code>C_PRECEDENCES</code></p>
<dd> This alters the precedence of arithmetic operators to be more like C and other programming languages; the section ARITHMETIC EVALUATION in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) has an explicit list.</p>
<dt><code>DEBUG_BEFORE_CMD</code> &lt;D&gt;</p>
<dd> Run the <code>DEBUG</code> trap before each command; otherwise it is run after each command. Setting this option mimics the behaviour of ksh 93; with the option unset the behaviour is that of ksh 88.</p>
<dt><code>ERR_EXIT</code> (<code>-e</code>, ksh: <code>-e</code>)</p>
<dd> If a command has a non-zero exit status, execute the <code>ZERR</code> trap, if set, and exit. This is disabled while running initialization scripts.</p>
<dl>
<dt>
<dd>
<p> The behaviour is also disabled inside <code>DEBUG</code> traps. In this case the option is handled specially: it is unset on entry to the trap. If the option <code>DEBUG_BEFORE_CMD</code> is set, as it is by default, and the option <code>ERR_EXIT</code> is found to have been set on exit, then the command for which the <code>DEBUG</code> trap is being executed is skipped. The option is restored after the trap exits. </p>
<p> Non-zero status in a command list containing <code>&amp;&amp;</code> or <code>||</code> is ignored for commands not at the end of the list. Hence </p>
<dl>
<dt>
<dd>
<pre>
<code>false &amp;&amp; true</code>
</pre>
</dl>
<p> does not trigger exit. </p>
<p> Exiting due to <code>ERR_EXIT</code> has certain interactions with asynchronous jobs noted in the section JOBS in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</dl>
<dt><code>ERR_RETURN</code></p>
<dd> If a command has a non-zero exit status, return immediately from the enclosing function. The logic is similar to that for <code>ERR_EXIT</code>, except that an implicit <code>return</code> statement is executed instead of an <code>exit</code>. This will trigger an exit at the outermost level of a non-interactive script.</p>
<dl>
<dt>
<dd>
<p> Normally this option inherits the behaviour of <code>ERR_EXIT</code> that code followed by `<code>&amp;&amp;</code>&#8216; `<code>||</code>&#8216; does not trigger a return. Hence in the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>summit || true</code>
</pre>
</dl>
<p> no return is forced as the combined effect always has a zero return status. </p>
<p> Note. however, that if <code>summit</code> in the above example is itself a function, code inside it is considered separately: it may force a return from <code>summit</code> (assuming the option remains set within <code>summit</code>), but not from the enclosing context. This behaviour is different from <code>ERR_EXIT</code> which is unaffected by function scope.</dl>
<dt><code>EVAL_LINENO</code> &lt;Z&gt;</p>
<dd> If set, line numbers of expressions evaluated using the builtin <code>eval</code> are tracked separately of the enclosing environment. This applies both to the parameter <code>LINENO</code> and the line number output by the prompt escape <code>%i</code>. If the option is set, the prompt escape <code>%N</code> will output the string `<code>(eval)</code>&#8216; instead of the script or function name as an indication. (The two prompt escapes are typically used in the parameter <code>PS4</code> to be output when the option <code>XTRACE</code> is set.) If <code>EVAL_LINENO</code> is unset, the line number of the surrounding script or function is retained during the evaluation.</p>
<dt><code>EXEC</code> (<code>+n</code>, ksh: <code>+n</code>) &lt;D&gt;</p>
<dd> Do execute commands. Without this option, commands are read and checked for syntax errors, but not executed. This option cannot be turned off in an interactive shell, except when `<code>-n</code>&#8216; is supplied to the shell at startup.</p>
<dt><code>FUNCTION_ARGZERO</code> &lt;C&gt; &lt;Z&gt;</p>
<dd> When executing a shell function or sourcing a script, set <code>$0</code> temporarily to the name of the function/script. Note that toggling <code>FUNCTION_ARGZERO</code> from on to off (or off to on) does not change the current value of <code>$0</code>. Only the state upon entry to the function or script has an effect. Compare <code>POSIX_ARGZERO</code>.</p>
<dt><code>LOCAL_LOOPS</code></p>
<dd> When this option is not set, the effect of <code>break</code> and <code>continue</code> commands may propagate outside function scope, affecting loops in calling functions. When the option is set in a calling function, a <code>break</code> or a <code>continue</code> that is not caught within a called function (regardless of the setting of the option within that function) produces a warning and the effect is cancelled.</p>
<dt><code>LOCAL_OPTIONS</code> &lt;K&gt;</p>
<dd> If this option is set at the point of return from a shell function, most options (including this one) which were in force upon entry to the function are restored; options that are not restored are <code>PRIVILEGED</code> and <code>RESTRICTED</code>. Otherwise, only this option, and the <code>LOCAL_LOOPS</code>, <code>XTRACE</code> and <code>PRINT_EXIT_VALUE</code> options are restored. Hence if this is explicitly unset by a shell function the other options in force at the point of return will remain so. A shell function can also guarantee itself a known shell configuration with a formulation like `<code>emulate -L zsh</code>&#8216;; the <code>-L</code> activates <code>LOCAL_OPTIONS</code>.</p>
<dt><code>LOCAL_PATTERNS</code></p>
<dd> If this option is set at the point of return from a shell function, the state of pattern disables, as set with the builtin command `<code>disable -p</code>&#8216;, is restored to what it was when the function was entered. The behaviour of this option is similar to the effect of <code>LOCAL_OPTIONS</code> on options; hence `<code>emulate -L sh</code>&#8216; (or indeed any other emulation with the <code>-L</code> option) activates <code>LOCAL_PATTERNS</code>.</p>
<dt><code>LOCAL_TRAPS</code> &lt;K&gt;</p>
<dd> If this option is set when a signal trap is set inside a function, then the previous status of the trap for that signal will be restored when the function exits. Note that this option must be set <i>prior</i> to altering the trap behaviour in a function; unlike <code>LOCAL_OPTIONS</code>, the value on exit from the function is irrelevant. However, it does not need to be set before any global trap for that to be correctly restored by a function. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
unsetopt localtraps
        trap -
    INT
    fn()
{
    setopt localtraps;
    trap '' INT;
    sleep 3;
}
</code></pre>
</dl>
<p> will restore normal handling of <code>SIGINT</code> after the function exits.</dl>
<dt><code>MULTI_FUNC_DEF</code> &lt;Z&gt;</p>
<dd> Allow definitions of multiple functions at once in the form `<code>fn1 fn2</code><i>&#8230;</i><code>()</code>&#8216;; if the option is not set, this causes a parse error. Definition of multiple functions with the <code>function</code> keyword is always allowed. Multiple function definitions are not often used and can cause obscure errors.</p>
<dt><code>MULTIOS</code> &lt;Z&gt;</p>
<dd> Perform implicit <code>tee</code>s or <code>cat</code>s when multiple redirections are attempted (see the section `Redirection&#8217;).</p>
<dt><code>OCTAL_ZEROES</code> &lt;S&gt;</p>
<dd> Interpret any integer constant beginning with a 0 as octal, per IEEE Std 1003.2-1992 (ISO 9945-2:1993). This is not enabled by default as it causes problems with parsing of, for example, date and time strings with leading zeroes.</p>
<dl>
<dt>
<dd>
<p> Sequences of digits indicating a numeric base such as the `<code>08</code>&#8216; component in `<code>08#77</code>&#8216; are always interpreted as decimal, regardless of leading zeroes.</dl>
<dt><code>PIPE_FAIL</code></p>
<dd> By default, when a pipeline exits the exit status recorded by the shell and returned by the shell variable <code>$?</code> reflects that of the rightmost element of a pipeline. If this option is set, the exit status instead reflects the status of the rightmost element of the pipeline that was non-zero, or zero if all elements exited with zero status.</p>
<dt><code>SOURCE_TRACE</code></p>
<dd> If set, zsh will print an informational message announcing the name of each file it loads. The format of the output is similar to that for the <code>XTRACE</code> option, with the message <code>&lt;sourcetrace&gt;</code>. A file may be loaded by the shell itself when it starts up and shuts down (<code>Startup/Shutdown Files</code>) or by the use of the `<code>source</code>&#8216; and `<code>dot</code>&#8216; builtin commands.</p>
<dt><code>TYPESET_SILENT</code></p>
<dd> If this is unset, executing any of the `<code>typeset</code>&#8216; family of commands with no options and a list of parameters that have no values to be assigned but already exist will display the value of the parameter. If the option is set, they will only be shown when parameters are selected with the `<code>-m</code>&#8216; option. The option `<code>-p</code>&#8216; is available whether or not the option is set.</p>
<dt><code>VERBOSE</code> (<code>-v</code>, ksh: <code>-v</code>)</p>
<dd> Print shell input lines as they are read.</p>
<dt><code>XTRACE</code> (<code>-x</code>, ksh: <code>-x</code>)</p>
<dd> Print commands and their arguments as they are executed. The output is preceded by the value of <code>$PS4</code>, formatted as described in the section EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</dl>
<h3>Shell Emulation</h3>
<dl>
<dt>
<dd> <code>APPEND_CREATE</code> &lt;K&gt; &lt;S&gt; This option only applies when <code>NO_CLOBBER</code> (-<code>C</code>) is in effect.</p>
<dl>
<dt>
<dd>
<p> If this option is not set, the shell will report an error when a append redirection (<code>&gt;&gt;</code>) is used on a file that does not already exists (the traditional zsh behaviour of <code>NO_CLOBBER</code>). If the option is set, no error is reported (POSIX behaviour).</dl>
<dt><code>BASH_REMATCH</code></p>
<dd> When set, matches performed with the <code>=~</code> operator will set the <code>BASH_REMATCH</code> array variable, instead of the default <code>MATCH</code> and <code>match</code> variables. The first element of the <code>BASH_REMATCH</code> array will contain the entire matched text and subsequent elements will contain extracted substrings. This option makes more sense when <code>KSH_ARRAYS</code> is also set, so that the entire matched portion is stored at index 0 and the first substring is at index 1. Without this option, the <code>MATCH</code> variable contains the entire matched text and the <code>match</code> array variable contains substrings.</p>
<dt><code>BSD_ECHO</code> &lt;S&gt;</p>
<dd> Make the <code>echo</code> builtin compatible with the BSD <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1) command. This disables backslashed escape sequences in echo strings unless the <code>-e</code> option is specified.</p>
<dt><code>CONTINUE_ON_ERROR</code></p>
<dd> If a fatal error is encountered (see the section ERRORS in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)), and the code is running in a script, the shell will resume execution at the next statement in the script at the top level, in other words outside all functions or shell constructs such as loops and conditions. This mimics the behaviour of interactive shells, where the shell returns to the line editor to read a new command; it was the normal behaviour in versions of zsh before 5.0.1.</p>
<dt><code>CSH_JUNKIE_HISTORY</code> &lt;C&gt;</p>
<dd> A history reference without an event specifier will always refer to the previous command. Without this option, such a history reference refers to the same event as the previous history reference on the current command line, defaulting to the previous command.</p>
<dt><code>CSH_JUNKIE_LOOPS</code> &lt;C&gt;</p>
<dd> Allow loop bodies to take the form `<i>list</i><code>; end</code>&#8216; instead of `<code>do </code><i>list</i><code>; done</code>&#8216;.</p>
<dt><code>CSH_JUNKIE_QUOTES</code> &lt;C&gt;</p>
<dd> Changes the rules for single- and double-quoted text to match that of <code>csh</code>. These require that embedded newlines be preceded by a backslash; unescaped newlines will cause an error message. In double-quoted strings, it is made impossible to escape `<code>$</code>&#8216;, `<code>`</code>&#8216; or `<code>&quot;</code>&#8216; (and `<code>\</code>&#8216; itself no longer needs escaping). Command substitutions are only expanded once, and cannot be nested.</p>
<dt><code>CSH_NULLCMD</code> &lt;C&gt;</p>
<dd> Do not use the values of <code>NULLCMD</code> and <code>READNULLCMD</code> when running redirections with no command. This make such redirections fail (see the section `Redirection&#8217;).</p>
<dt><code>KSH_ARRAYS</code> &lt;K&gt; &lt;S&gt;</p>
<dd> Emulate <code>ksh</code> array handling as closely as possible. If this option is set, array elements are numbered from zero, an array parameter without subscript refers to the first element instead of the whole array, and braces are required to delimit a subscript (`<code>${path[2]}</code>&#8216; rather than just `<code>$path[2]</code>&#8216;) or to apply modifiers to any parameter (`<code>${PWD:h}</code>&#8216; rather than `<code>$PWD:h</code>&#8216;).</p>
<dt><code>KSH_AUTOLOAD</code> &lt;K&gt; &lt;S&gt;</p>
<dd> Emulate <code>ksh</code> function autoloading. This means that when a function is autoloaded, the corresponding file is merely executed, and must define the function itself. (By default, the function is defined to the contents of the file. However, the most common <code>ksh</code>-style case &#8211; of the file containing only a simple definition of the function &#8211; is always handled in the <code>ksh</code>-compatible manner.)</p>
<dt><code>KSH_OPTION_PRINT</code> &lt;K&gt;</p>
<dd> Alters the way options settings are printed: instead of separate lists of set and unset options, all options are shown, marked `on&#8217; if they are in the non-default state, `off&#8217; otherwise.</p>
<dt><code>KSH_TYPESET</code></p>
<dd> This option is now obsolete: a better appropximation to the behaviour of other shells is obtained with the reserved word interface to <code>declare</code>, <code>export</code>, <code>float</code>, <code>integer</code>, <code>local</code>, <code>readonly</code> and <code>typeset</code>. Note that the option is only applied when the reserved word interface is <i>not</i> in use.</p>
<dl>
<dt>
<dd>
<p> Alters the way arguments to the <code>typeset</code> family of commands, including <code>declare</code>, <code>export</code>, <code>float</code>, <code>integer</code>, <code>local</code> and <code>readonly</code>, are processed. Without this option, zsh will perform normal word splitting after command and parameter expansion in arguments of an assignment; with it, word splitting does not take place in those cases.</dl>
<dt><code>KSH_ZERO_SUBSCRIPT</code></p>
<dd> Treat use of a subscript of value zero in array or string expressions as a reference to the first element, i.e. the element that usually has the subscript 1. Ignored if <code>KSH_ARRAYS</code> is also set.</p>
<dl>
<dt>
<dd>
<p> If neither this option nor <code>KSH_ARRAYS</code> is set, accesses to an element of an array or string with subscript zero return an empty element or string, while attempts to set element zero of an array or string are treated as an error. However, attempts to set an otherwise valid subscript range that includes zero will succeed. For example, if <code>KSH_ZERO_SUBSCRIPT</code> is not set, </p>
<dl>
<dt>
<dd>
<pre>
<code>array[0]=(element)</code>
</pre>
</dl>
<p> is an error, while </p>
<dl>
<dt>
<dd>
<pre>
<code>array[0,1]=(element)</code>
</pre>
</dl>
<p> is not and will replace the first element of the array. </p>
<p> This option is for compatibility with older versions of the shell and is not recommended in new code.</dl>
<dt><code>POSIX_ALIASES</code> &lt;K&gt; &lt;S&gt;</p>
<dd> When this option is set, reserved words are not candidates for alias expansion: it is still possible to declare any of them as an alias, but the alias will never be expanded. Reserved words are described in the section RESERVED WORDS in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1).</p>
<dl>
<dt>
<dd>
<p> Alias expansion takes place while text is being read; hence when this option is set it does not take effect until the end of any function or other piece of shell code parsed as one unit. Note this may cause differences from other shells even when the option is in effect. For example, when running a command with `<code>zsh -c</code>&#8216;, or even `<code>zsh -o posixaliases -c</code>&#8216;, the entire command argument is parsed as one unit, so aliases defined within the argument are not available even in later lines. If in doubt, avoid use of aliases in non-interactive code.</dl>
<dt><code>POSIX_ARGZERO</code></p>
<dd> This option may be used to temporarily disable <code>FUNCTION_ARGZERO</code> and thereby restore the value of <code>$0</code> to the name used to invoke the shell (or as set by the <code>-c</code> command line option). For compatibility with previous versions of the shell, emulations use <code>NO_FUNCTION_ARGZERO</code> instead of <code>POSIX_ARGZERO</code>, which may result in unexpected scoping of <code>$0</code> if the emulation mode is changed inside a function or script. To avoid this, explicitly enable <code>POSIX_ARGZERO</code> in the <code>emulate</code> command:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>emulate sh -o POSIX_ARGZERO</code>
</pre>
</dl>
<p> Note that <code>NO_POSIX_ARGZERO</code> has no effect unless <code>FUNCTION_ARGZERO</code> was already enabled upon entry to the function or script.</dl>
<dt><code>POSIX_BUILTINS</code> &lt;K&gt; &lt;S&gt;</p>
<dd> When this option is set the <code>command</code> builtin can be used to execute shell builtin commands. Parameter assignments specified before shell functions and special builtins are kept after the command completes unless the special builtin is prefixed with the <code>command</code> builtin. Special builtins are <code>.</code>, <code>:</code>, <code>break</code>, <code>continue</code>, <code>declare</code>, <code>eval</code>, <code>exit</code>, <code>export</code>, <code>integer</code>, <code>local</code>, <code>readonly</code>, <code>return</code>, <code>set</code>, <code>shift</code>, <code>source</code>, <code>times</code>, <code>trap</code> and <code>unset</code>.</p>
<dl>
<dt>
<dd>
<p> In addition, various error conditions associated with the above builtins or <code>exec</code> cause a non-interactive shell to exit and an interactive shell to return to its top-level processing. </p>
<p> Furthermore, functions and shell builtins are not executed after an <code>exec</code> prefix; the command to be executed must be an external command found in the path. </p>
<p> Furthermore, the <code>getopts</code> builtin behaves in a POSIX-compatible fashion in that the associated variable <code>OPTIND</code> is not made local to functions. </p>
<p> Moreover, the warning and special exit code from <code>[[ -o </code><i>non_existent_option</i><code> ]]</code> are suppressed.</dl>
<dt><code>POSIX_IDENTIFIERS</code> &lt;K&gt; &lt;S&gt;</p>
<dd> When this option is set, only the ASCII characters <code>a</code> to <code>z</code>, <code>A</code> to <code>Z</code>, <code>0</code> to <code>9</code> and <code>_</code> may be used in identifiers (names of shell parameters and modules).</p>
<dl>
<dt>
<dd>
<p> In addition, setting this option limits the effect of parameter substitution with no braces, so that the expression <code>$#</code> is treated as the parameter <code>$#</code> even if followed by a valid parameter name. When it is unset, zsh allows expressions of the form <code>$#</code><i>name</i> to refer to the length of <code>$</code><i>name</i>, even for special variables, for example in expressions such as <code>$#-</code> and <code>$#*</code>. </p>
<p> Another difference is that with the option set assignment to an unset variable in arithmetic context causes the variable to be created as a scalar rather than a numeric type. So after `<code>unset t; (( t = 3 ))</code>&#8216;. without <code>POSIX_IDENTIFIERS</code> set <code>t</code> has integer type, while with it set it has scalar type. </p>
<p> When the option is unset and multibyte character support is enabled (i.e. it is compiled in and the option <code>MULTIBYTE</code> is set), then additionally any alphanumeric characters in the local character set may be used in identifiers. Note that scripts and functions written with this feature are not portable, and also that both options must be set before the script or function is parsed; setting them during execution is not sufficient as the syntax <i>variable</i><code>=</code><i>value</i> has already been parsed as a command rather than an assignment. </p>
<p> If multibyte character support is not compiled into the shell this option is ignored; all octets with the top bit set may be used in identifiers. This is non-standard but is the traditional zsh behaviour.</dl>
<dt><code>POSIX_STRINGS</code> &lt;K&gt; &lt;S&gt;</p>
<dd> This option affects processing of quoted strings. Currently it only affects the behaviour of null characters, i.e. character 0 in the portable character set corresponding to US ASCII.</p>
<dl>
<dt>
<dd>
<p> When this option is not set, null characters embedded within strings of the form <code>$&#8217;</code><i>&#8230;</i><code>&#8216;</code> are treated as ordinary characters. The entire string is maintained within the shell and output to files where necessary, although owing to restrictions of the library interface the string is truncated at the null character in file names, environment variables, or in arguments to external programs. </p>
<p> When this option is set, the <code>$&#8217;</code><i>&#8230;</i><code>&#8216;</code> expression is truncated at the null character. Note that remaining parts of the same string beyond the termination of the quotes are not truncated. </p>
<p> For example, the command line argument <code>a$&#8217;b
