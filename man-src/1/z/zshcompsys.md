---
title: "zshcompsys(1)"
name: "zshcompsys"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshcompsys/"
description: "zshcompsys – zsh completion system"
---

<h2 class="name">NAME</h2>
<p> zshcompsys &#8211; zsh completion system </p>
<h2>DESCRIPTION</h2>
<p> This describes the shell code for the `new&#8217; completion system, referred to as <code>compsys</code>. It is written in shell functions based on the features described in <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1). </p>
<p> The features are contextual, sensitive to the point at which completion is started. Many completions are already provided. For this reason, a user can perform a great many tasks without knowing any details beyond how to initialize the system, which is described below in INITIALIZATION. </p>
<p> The context that decides what completion is to be performed may be</p>
<dl>
<dt>
<dd> &bull; an argument or option position: these describe the position on the command line at which completion is requested. For example `first argument to rmdir, the word being completed names a directory&#8217;; </p>
<dt>&bull;</p>
<dd> a special context, denoting an element in the shell&#8217;s syntax. For example `a word in command position&#8217; or `an array subscript&#8217;. </p>
</dl>
<p> A full context specification contains other elements, as we shall describe. </p>
<p> Besides commands names and contexts, the system employs two more concepts, <i>styles</i> and <i>tags</i>. These provide ways for the user to configure the system&#8217;s behaviour. </p>
<p> Tags play a dual role. They serve as a classification system for the matches, typically indicating a class of object that the user may need to distinguish. For example, when completing arguments of the <code>ls</code> command the user may prefer to try <code>files</code> before <code>directories</code>, so both of these are tags. They also appear as the rightmost element in a context specification. </p>
<p> Styles modify various operations of the completion system, such as output formatting, but also what kinds of completers are used (and in what order), or which tags are examined. Styles may accept arguments and are manipulated using the <code>zstyle</code> command described in see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). </p>
<p> In summary, tags describe <i>what</i> the completion objects are, and style <code>how</code> they are to be completed. At various points of execution, the completion system checks what styles and/or tags are defined for the current context, and uses that to modify its behavior. The full description of context handling, which determines how tags and other elements of the context influence the behaviour of styles, is described below in COMPLETION SYSTEM CONFIGURATION. </p>
<p> When a completion is requested, a dispatcher function is called; see the description of <code>_main_complete</code> in the list of control functions below. This dispatcher decides which function should be called to produce the completions, and calls it. The result is passed to one or more <i>completers</i>, functions that implement individual completion strategies: simple completion, error correction, completion with error correction, menu selection, etc. </p>
<p> More generally, the shell functions contained in the completion system are of two types:</p>
<dl>
<dt>
<dd> &bull; those beginning `<code>comp</code>&#8216; are to be called directly; there are only a few of these; </p>
<dt>&bull;</p>
<dd> those beginning `<code>_</code>&#8216; are called by the completion code. The shell functions of this set, which implement completion behaviour and may be bound to keystrokes, are referred to as `widgets&#8217;. These proliferate as new completions are required. </p>
</dl>
<h2>INITIALIZATION</h2>
<p> If the system was installed completely, it should be enough to call the shell function <code>compinit</code> from your initialization file; see the next section. However, the function <code>compinstall</code> can be run by a user to configure various aspects of the completion system. </p>
<p> Usually, <code>compinstall</code> will insert code into <code>.zshrc</code>, although if that is not writable it will save it in another file and tell you that file&#8217;s location. Note that it is up to you to make sure that the lines added to <code>.zshrc</code> are actually run; you may, for example, need to move them to an earlier place in the file if <code>.zshrc</code> usually returns early. So long as you keep them all together (including the comment lines at the start and finish), you can rerun <code>compinstall</code> and it will correctly locate and modify these lines. Note, however, that any code you add to this section by hand is likely to be lost if you rerun <code>compinstall</code>, although lines using the command `<code>zstyle</code>&#8216; should be gracefully handled. </p>
<p> The new code will take effect next time you start the shell, or run <code>.zshrc</code> by hand; there is also an option to make them take effect immediately. However, if <code>compinstall</code> has removed definitions, you will need to restart the shell to see the changes. </p>
<p> To run <code>compinstall</code> you will need to make sure it is in a directory mentioned in your <code>fpath</code> parameter, which should already be the case if zsh was properly configured as long as your startup files do not remove the appropriate directories from <code>fpath</code>. Then it must be autoloaded (`<code>autoload -U compinstall</code>&#8216; is recommended). You can abort the installation any time you are being prompted for information, and your <code>.zshrc</code> will not be altered at all; changes only take place right at the end, where you are specifically asked for confirmation. </p>
<h3>Use of compinit</h3>
<p> This section describes the use of <code>compinit</code> to initialize completion for the current session when called directly; if you have run <code>compinstall</code> it will be called automatically from your <code>.zshrc</code>. </p>
<p> To initialize the system, the function <code>compinit</code> should be in a directory mentioned in the <code>fpath</code> parameter, and should be autoloaded (`<code>autoload -U compinit</code>&#8216; is recommended), and then run simply as `<code>compinit</code>&#8216;. This will define a few utility functions, arrange for all the necessary shell functions to be autoloaded, and will then re-define all widgets that do completion to use the new system. If you use the <code>menu-select</code> widget, which is part of the <code>zsh/complist</code> module, you should make sure that that module is loaded before the call to <code>compinit</code> so that that widget is also re-defined. If completion styles (see below) are set up to perform expansion as well as completion by default, and the TAB key is bound to <code>expand-or-complete</code>, <code>compinit</code> will rebind it to <code>complete-word</code>; this is necessary to use the correct form of expansion. </p>
<p> Should you need to use the original completion commands, you can still bind keys to the old widgets by putting a `<code>.</code>&#8216; in front of the widget name, e.g. `<code>.expand-or-complete</code>&#8216;. </p>
<p> To speed up the running of <code>compinit</code>, it can be made to produce a dumped configuration that will be read in on future invocations; this is the default, but can be turned off by calling <code>compinit</code> with the option <code>-D</code>. The dumped file is <code>.zcompdump</code> in the same directory as the startup files (i.e. <code>$ZDOTDIR</code> or <code>$HOME</code>); alternatively, an explicit file name can be given by `<code>compinit -d</code> <i>dumpfile</i>&#8216;. The next invocation of <code>compinit</code> will read the dumped file instead of performing a full initialization. </p>
<p> If the number of completion files changes, <code>compinit</code> will recognise this and produce a new dump file. However, if the name of a function or the arguments in the first line of a <code>#compdef</code> function (as described below) change, it is easiest to delete the dump file by hand so that <code>compinit</code> will re-create it the next time it is run. The check performed to see if there are new functions can be omitted by giving the option <code>-C</code>. In this case the dump file will only be created if there isn&#8217;t one already. </p>
<p> The dumping is actually done by another function, <code>compdump</code>, but you will only need to run this yourself if you change the configuration (e.g. using <code>compdef</code>) and then want to dump the new one. The name of the old dumped file will be remembered for this purpose. </p>
<p> If the parameter <code>_compdir</code> is set, <code>compinit</code> uses it as a directory where completion functions can be found; this is only necessary if they are not already in the function search path. </p>
<p> For security reasons <code>compinit</code> also checks if the completion system would use files not owned by root or by the current user, or files in directories that are world- or group-writable or that are not owned by root or by the current user. If such files or directories are found, <code>compinit</code> will ask if the completion system should really be used. To avoid these tests and make all files found be used without asking, use the option <code>-u</code>, and to make <code>compinit</code> silently ignore all insecure files and directories use the option <code>-i</code>. This security check is skipped entirely when the <code>-C</code> option is given. </p>
<p> The security check can be retried at any time by running the function <code>compaudit</code>. This is the same check used by <code>compinit</code>, but when it is executed directly any changes to <code>fpath</code> are made local to the function so they do not persist. The directories to be checked may be passed as arguments; if none are given, <code>compaudit</code> uses <code>fpath</code> and <code>_compdir</code> to find completion system directories, adding missing ones to <code>fpath</code> as necessary. To force a check of exactly the directories currently named in <code>fpath</code>, set <code>_compdir</code> to an empty string before calling <code>compaudit</code> or <code>compinit</code>. </p>
<p> The function <code>bashcompinit</code> provides compatibility with bash&#8217;s programmable completion system. When run it will define the functions, <code>compgen</code> and <code>complete</code> which correspond to the bash builtins with the same names. It will then be possible to use completion specifications and functions written for bash. </p>
<h3>Autoloaded files</h3>
<p> The convention for autoloaded functions used in completion is that they start with an underscore; as already mentioned, the <code>fpath/FPATH</code> parameter must contain the directory in which they are stored. If <code>zsh</code> was properly installed on your system, then <code>fpath/FPATH</code> automatically contains the required directories for the standard functions. </p>
<p> For incomplete installations, if <code>compinit</code> does not find enough files beginning with an underscore (fewer than twenty) in the search path, it will try to find more by adding the directory <code>_compdir</code> to the search path. If that directory has a subdirectory named <code>Base</code>, all subdirectories will be added to the path. Furthermore, if the subdirectory <code>Base</code> has a subdirectory named <code>Core</code>, <code>compinit</code> will add all subdirectories of the subdirectories to the path: this allows the functions to be in the same format as in the <code>zsh</code> source distribution. </p>
<p> When <code>compinit</code> is run, it searches all such files accessible via <code>fpath/FPATH</code> and reads the first line of each of them. This line should contain one of the tags described below. Files whose first line does not start with one of these tags are not considered to be part of the completion system and will not be treated specially. </p>
<p> The tags are: </p>
<dl>
<dt>
<dd> <code>#compdef</code> <i>name</i> &#8230; [ <code>&#8211;</code>{<code>p</code>|<code>P</code>} <i>pattern</i> &#8230; [ <code>-N</code> <i>name</i> &#8230; ] ] The file will be made autoloadable and the function defined in it will be called when completing <i>name</i>s, each of which is either the name of a command whose arguments are to be completed or one of a number of special contexts in the form <code>&#8211;</code><i>context</i><code>&#8211;</code> described below.</p>
<dl>
<dt>
<dd>
<p> Each <i>name</i> may also be of the form `<i>cmd</i><code>=</code><i>service</i>&#8216;. When completing the command <i>cmd</i>, the function typically behaves as if the command (or special context) <i>service</i> was being completed instead. This provides a way of altering the behaviour of functions that can perform many different completions. It is implemented by setting the parameter <code>$service</code> when calling the function; the function may choose to interpret this how it wishes, and simpler functions will probably ignore it. </p>
<p> If the <code>#compdef</code> line contains one of the options <code>-p</code> or <code>-P</code>, the words following are taken to be patterns. The function will be called when completion is attempted for a command or context that matches one of the patterns. The options <code>-p</code> and <code>-P</code> are used to specify patterns to be tried before or after other completions respectively. Hence <code>-P</code> may be used to specify default actions. </p>
<p> The option <code>-N</code> is used after a list following <code>-p</code> or <code>-P</code>; it specifies that remaining words no longer define patterns. It is possible to toggle between the three options as many times as necessary.</dl>
<dt><code>#compdef -k</code> <i>style key-sequence</i> &#8230;</p>
<dd> This option creates a widget behaving like the builtin widget <i>style</i> and binds it to the given <i>key-sequence</i>s, if any. The <i>style</i> must be one of the builtin widgets that perform completion, namely <code>complete-word</code>, <code>delete-char-or-list</code>, <code>expand-or-complete</code>, <code>expand-or-complete-prefix</code>, <code>list-choices</code>, <code>menu-complete</code>, <code>menu-expand-or-complete</code>, or <code>reverse-menu-complete</code>. If the <code>zsh/complist</code> module is loaded (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)) the widget <code>menu-select</code> is also available.</p>
<dl>
<dt>
<dd>
<p> When one of the <i>key-sequence</i>s is typed, the function in the file will be invoked to generate the matches. Note that a key will not be re-bound if it already was (that is, was bound to something other than <code>undefined-key</code>). The widget created has the same name as the file and can be bound to any other keys using <code>bindkey</code> as usual.</dl>
<dt><code>#compdef -K</code> <i>widget-name</i> <i>style</i> <i>key-sequence</i> [ <i>name</i> <i>style</i> <i>seq</i> &#8230; ]</p>
<dd> This is similar to <code>-k</code> except that only one <i>key-sequence</i> argument may be given for each <i>widget-name</i> <i>style</i> pair. However, the entire set of three arguments may be repeated with a different set of arguments. Note in particular that the <i>widget-name</i> must be distinct in each set. If it does not begin with `<code>_</code>&#8216; this will be added. The <i>widget-name</i> should not clash with the name of any existing widget: names based on the name of the function are most useful. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>#compdef -K _foo_complete complete-word &quot;^X^C&quot; \ 
  _foo_list list-choices &quot;^X^D&quot;</code>
</pre>
</dl>
<p> (all on one line) defines a widget <code>_foo_complete</code> for completion, bound to `<code>^X^C</code>&#8216;, and a widget <code>_foo_list</code> for listing, bound to `<code>^X^D</code>&#8216;.</dl>
<dt><code>#autoload</code> [ <i>options</i> ]</p>
<dd> Functions with the <code>#autoload</code> tag are marked for autoloading but are not otherwise treated specially. Typically they are to be called from within one of the completion functions. Any <i>options</i> supplied will be passed to the <code>autoload</code> builtin; a typical use is <code>+X</code> to force the function to be loaded immediately. Note that the <code>-U</code> and <code>-z</code> flags are always added implicitly.</dl>
<p> The <code>#</code> is part of the tag name and no white space is allowed after it. The <code>#compdef</code> tags use the <code>compdef</code> function described below; the main difference is that the name of the function is supplied implicitly. </p>
<p> The special contexts for which completion functions can be defined are: </p>
<dl>
<dt>
<dd> <code>-array-value-</code> The right hand side of an array-assignment (`<i>name</i><code>=(</code><i>&#8230;</i><code>)</code>&#8216;)</p>
<dt><code>-brace-parameter-</code></p>
<dd> The name of a parameter expansion within braces (`<code>${</code><i>&#8230;</i><code>}</code>&#8216;)</p>
<dt><code>-assign-parameter-</code></p>
<dd> The name of a parameter in an assignment, i.e. on the left hand side of an `<code>=</code>&#8216;</p>
<dt><code>-command-</code></p>
<dd> A word in command position</p>
<dt><code>-condition-</code></p>
<dd> A word inside a condition (`<code>[[</code><i>&#8230;</i><code>]]</code>&#8216;)</p>
<dt><code>-default-</code></p>
<dd> Any word for which no other completion is defined</p>
<dt><code>-equal-</code></p>
<dd> A word beginning with an equals sign</p>
<dt><code>-first-</code></p>
<dd> This is tried before any other completion function. The function called may set the <code>_compskip</code> parameter to one of various values: <code>all</code>: no further completion is attempted; a string containing the substring <code>patterns</code>: no pattern completion functions will be called; a string containing <code>default</code>: the function for the `<code>-default-</code>&#8216; context will not be called, but functions defined for commands will be.</p>
<dt><code>-math-</code></p>
<dd> Inside mathematical contexts, such as `<code>((</code><i>&#8230;</i><code>))</code>&#8216;</p>
<dt><code>-parameter-</code></p>
<dd> The name of a parameter expansion (`<code>$</code><i>&#8230;</i>&#8216;)</p>
<dt><code>-redirect-</code></p>
<dd> The word after a redirection operator.</p>
<dt><code>-subscript-</code></p>
<dd> The contents of a parameter subscript.</p>
<dt><code>-tilde-</code></p>
<dd> After an initial tilde (`<code>~</code>&#8216;), but before the first slash in the word.</p>
<dt><code>-value-</code></p>
<dd> On the right hand side of an assignment.</dl>
<p> Default implementations are supplied for each of these contexts. In most cases the context <code>&#8211;</code><i>context</i><code>&#8211;</code> is implemented by a corresponding function <code>_</code><i>context</i>, for example the context `<code>-tilde-</code>&#8216; and the function `<code>_tilde</code>&#8216;). </p>
<p> The contexts <code>-redirect-</code> and <code>-value-</code> allow extra context-specific information. (Internally, this is handled by the functions for each context calling the function <code>_dispatch</code>.) The extra information is added separated by commas. </p>
<p> For the <code>-redirect-</code> context, the extra information is in the form `<code>-redirect-,</code><i>op</i><code>,</code><i>command</i>&#8216;, where <i>op</i> is the redirection operator and <i>command</i> is the name of the command on the line. If there is no command on the line yet, the <i>command</i> field will be empty. </p>
<p> For the <code>-value-</code> context, the form is `<code>-value-,</code><i>name</i><code>,</code><i>command</i>&#8216;, where <i>name</i> is the name of the parameter on the left hand side of the assignment. In the case of elements of an associative array, for example `<code>assoc=(key &lt;TAB&gt;</code>&#8216;, <i>name</i> is expanded to `<i>name</i><code>&#8211;</code><i>key</i>&#8216;. In certain special contexts, such as completing after `<code>make CFLAGS=</code>&#8216;, the <i>command</i> part gives the name of the command, here <code>make</code>; otherwise it is empty. </p>
<p> It is not necessary to define fully specific completions as the functions provided will try to generate completions by progressively replacing the elements with `<code>-default-</code>&#8216;. For example, when completing after `<code>foo=&lt;TAB&gt;</code>&#8216;, <code>_value</code> will try the names `<code>-value-,foo,</code>&#8216; (note the empty <i>command</i> part), `<code>-value-,foo,-default-</code>&#8216; and`<code>-value-,-default-,-default-</code>&#8216;, in that order, until it finds a function to handle the context. </p>
<p> As an example: </p>
<dl>
<dt>
<dd>
<pre>
<code>compdef '_files -g &quot;*.log&quot;' '-redirect-,2&gt;,-default-'</code>
</pre>
</dl>
<p> completes files matching `<code>*.log</code>&#8216; after `<code>2&gt; &lt;TAB&gt;</code>&#8216; for any command with no more specific handler defined. </p>
<p> Also: </p>
<dl>
<dt>
<dd>
<pre>
<code>compdef _foo -value-,-default-,-default-</code>
</pre>
</dl>
<p> specifies that <code>_foo</code> provides completions for the values of parameters for which no special function has been defined. This is usually handled by the function <code>_value</code> itself. </p>
<p> The same lookup rules are used when looking up styles (as described below); for example </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:-redirect-,2&gt;,*:*' file-patterns '*.log'</code>
</pre>
</dl>
<p> is another way to make completion after `<code>2&gt; &lt;TAB&gt;</code>&#8216; complete files matching `<code>*.log</code>&#8216;. </p>
<h3>Functions</h3>
<p> The following function is defined by <code>compinit</code> and may be called directly. </p>
<dl>
<dt>
<dd> <code>compdef</code> [ <code>-ane</code> ] <i>function name</i> &#8230; [ <code>&#8211;</code>{<code>p</code>|<code>P</code>} <i>pattern</i> &#8230; [ <code>-N</code> <i>name</i> &#8230;]]</p>
<dt>
<dd> <code>compdef -d</code> <i>name</i> &#8230;</p>
<dt>
<dd> <code>compdef -k</code> [ <code>-an</code> ] <i>function style key-sequence</i> [ <i>key-sequence</i> &#8230; ]</p>
<dt>
<dd> <code>compdef -K</code> [ <code>-an</code> ] <i>function name style key-seq</i> [ <i>name style seq</i> &#8230; ] The first form defines the <i>function</i> to call for completion in the given contexts as described for the <code>#compdef</code> tag above.</p>
<dl>
<dt>
<dd>
<p> Alternatively, all the arguments may have the form `<i>cmd</i><code>=</code><i>service</i>&#8216;. Here <i>service</i> should already have been defined by `<i>cmd1</i><code>=</code><i>service</i>&#8216; lines in <code>#compdef</code> files, as described above. The argument for <i>cmd</i> will be completed in the same way as <i>service</i>. </p>
<p> The <i>function</i> argument may alternatively be a string containing almost any shell code. If the string contains an equal sign, the above will take precedence. The option <code>-e</code> may be used to specify the first argument is to be evaluated as shell code even if it contains an equal sign. The string will be executed using the <code>eval</code> builtin command to generate completions. This provides a way of avoiding having to define a new completion function. For example, to complete files ending in `<code>.h</code>&#8216; as arguments to the command <code>foo</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>compdef '_files -g &quot;*.h&quot;' foo</code>
</pre>
</dl>
<p> The option <code>-n</code> prevents any completions already defined for the command or context from being overwritten. </p>
<p> The option <code>-d</code> deletes any completion defined for the command or contexts listed. </p>
<p> The <i>name</i>s may also contain <code>-p</code>, <code>-P</code> and <code>-N</code> options as described for the <code>#compdef</code> tag. The effect on the argument list is identical, switching between definitions of patterns tried initially, patterns tried finally, and normal commands and contexts. </p>
<p> The parameter <code>$_compskip</code> may be set by any function defined for a pattern context. If it is set to a value containing the substring `<code>patterns</code>&#8216; none of the pattern-functions will be called; if it is set to a value containing the substring `<code>all</code>&#8216;, no other function will be called. Setting <code>$_compskip</code> in this manner is of particular utility when using the <code>-p</code> option, as otherwise the dispatcher will move on to additional functions (likely the default one) after calling the pattern-context one, which can mangle the display of completion possibilities if not handled properly. </p>
<p> The form with <code>-k</code> defines a widget with the same name as the <i>function</i> that will be called for each of the <i>key-sequence</i>s; this is like the <code>#compdef -k</code> tag. The function should generate the completions needed and will otherwise behave like the builtin widget whose name is given as the <i>style</i> argument. The widgets usable for this are: <code>complete-word</code>, <code>delete-char-or-list</code>, <code>expand-or-complete</code>, <code>expand-or-complete-prefix</code>, <code>list-choices</code>, <code>menu-complete</code>, <code>menu-expand-or-complete</code>, and <code>reverse-menu-complete</code>, as well as <code>menu-select</code> if the <code>zsh/complist</code> module is loaded. The option <code>-n</code> prevents the key being bound if it is already to bound to something other than <code>undefined-key</code>. </p>
<p> The form with <code>-K</code> is similar and defines multiple widgets based on the same <i>function</i>, each of which requires the set of three arguments <i>name</i>, <i>style</i> and <i>key-seq</i>uence, where the latter two are as for <code>-k</code> and the first must be a unique widget name beginning with an underscore. </p>
<p> Wherever applicable, the <code>-a</code> option makes the <i>function</i> autoloadable, equivalent to <code>autoload -U </code><i>function</i>.</dl>
</dl>
<p> The function <code>compdef</code> can be used to associate existing completion functions with new commands. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>compdef _pids foo</code>
</pre>
</dl>
<p> uses the function <code>_pids</code> to complete process IDs for the command <code>foo</code>. </p>
<p> Note also the <code>_gnu_generic</code> function described below, which can be used to complete options for commands that understand the `<code>&#8211;</code><code>-help</code>&#8216; option. </p>
<h2>COMPLETION SYSTEM CONFIGURATION</h2>
<p> This section gives a short overview of how the completion system works, and then more detail on how users can configure how and when matches are generated. </p>
<h3>Overview</h3>
<p> When completion is attempted somewhere on the command line the completion system begins building the context. The context represents everything that the shell knows about the meaning of the command line and the significance of the cursor position. This takes account of a number of things including the command word (such as `<code>grep</code>&#8216; or `<code>zsh</code>&#8216;) and options to which the current word may be an argument (such as the `<code>-o</code>&#8216; option to <code>zsh</code> which takes a shell option as an argument). </p>
<p> The context starts out very generic (&quot;we are beginning a completion&quot;) and becomes more specific as more is learned (&quot;the current word is in a position that is usually a command name&quot; or &quot;the current word might be a variable name&quot; and so on). Therefore the context will vary during the same call to the completion system. </p>
<p> This context information is condensed into a string consisting of multiple fields separated by colons, referred to simply as `the context&#8217; in the remainder of the documentation. Note that a user of the completion system rarely needs to compose a context string, unless for example a new function is being written to perform completion for a new command. What a user may need to do is compose a <i>style</i> pattern, which is matched against a context when needed to look up context-sensitive options that configure the completion system. </p>
<p> The next few paragraphs explain how a context is composed within the completion function suite. Following that is discussion of how <i>styles</i> are defined. Styles determine such things as how the matches are generated, similarly to shell options but with much more control. They are defined with the <code>zstyle</code> builtin command (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). </p>
<p> The context string always consists of a fixed set of fields, separated by colons and with a leading colon before the first. Fields which are not yet known are left empty, but the surrounding colons appear anyway. The fields are always in the order <code>:completion:</code><i>function</i><code>:</code><i>completer</i><code>:</code><i>command</i><code>:</code><i>argument</i><code>:</code><i>tag</i>. These have the following meaning: </p>
<dl>
<dt>
<dd> &bull; The literal string <code>completion</code>, saying that this style is used by the completion system. This distinguishes the context from those used by, for example, zle widgets and ZFTP functions. </p>
<dt>&bull;</p>
<dd> The <i>function</i>, if completion is called from a named widget rather than through the normal completion system. Typically this is blank, but it is set by special widgets such as <code>predict-on</code> and the various functions in the <code>Widget</code> directory of the distribution to the name of that function, often in an abbreviated form. </p>
<dt>&bull;</p>
<dd> The <i>completer</i> currently active, the name of the function without the leading underscore and with other underscores converted to hyphens. A `completer&#8217; is in overall control of how completion is to be performed; `<code>complete</code>&#8216; is the simplest, but other completers exist to perform related tasks such as correction, or to modify the behaviour of a later completer. See the section `Control Functions&#8217; below for more information. </p>
<dt>&bull;</p>
<dd> The <i>command</i> or a special <code>&#8211;</code><i>context</i><code>&#8211;</code>, just at it appears following the <code>#compdef</code> tag or the <code>compdef</code> function. Completion functions for commands that have sub-commands usually modify this field to contain the name of the command followed by a minus sign and the sub-command. For example, the completion function for the <code>cvs</code> command sets this field to <code>cvs-add</code> when completing arguments to the <code>add</code> subcommand. </p>
<dt>&bull;</p>
<dd> The <i>argument</i>; this indicates which command line or option argument we are completing. For command arguments this generally takes the form <code>argument-</code><i>n</i>, where <i>n</i> is the number of the argument, and for arguments to options the form <code>option-</code><i>opt</i><code>&#8211;</code><i>n</i> where <i>n</i> is the number of the argument to option <i>opt</i>. However, this is only the case if the command line is parsed with standard UNIX-style options and arguments, so many completions do not set this. </p>
<dt>&bull;</p>
<dd> The <i>tag</i>. As described previously, tags are used to discriminate between the types of matches a completion function can generate in a certain context. Any completion function may use any tag name it likes, but a list of the more common ones is given below. </p>
</dl>
<p> The context is gradually put together as the functions are executed, starting with the main entry point, which adds <code>:completion:</code> and the <i>function</i> element if necessary. The completer then adds the <i>completer</i> element. The contextual completion adds the <i>command</i> and <i>argument</i> options. Finally, the <i>tag</i> is added when the types of completion are known. For example, the context name </p>
<dl>
<dt>
<dd>
<pre>
<code>:completion::complete:dvips:option-o-1:files</code>
</pre>
</dl>
<p> says that normal completion was attempted as the first argument to the option <code>-o</code> of the command <code>dvips</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>dvips -o ...</code>
</pre>
</dl>
<p> and the completion function will generate filenames. </p>
<p> Usually completion will be tried for all possible tags in an order given by the completion function. However, this can be altered by using the <code>tag-order</code> style. Completion is then restricted to the list of given tags in the given order. </p>
<p> The <code>_complete_help</code> bindable command shows all the contexts and tags available for completion at a particular point. This provides an easy way of finding information for <code>tag-order</code> and other styles. It is described in the section `Bindable Commands&#8217; below. </p>
<p> When looking up styles the completion system uses full context names, including the tag. Looking up the value of a style therefore consists of two things: the context, which is matched to the most specific (best fitting) style pattern, and the name of the style itself, which must be matched exactly. The following examples demonstrate that style patterns may be loosely defined for styles that apply broadly, or as tightly defined as desired for styles that apply in narrower circumstances. </p>
<p> For example, many completion functions can generate matches in a simple and a verbose form and use the <code>verbose</code> style to decide which form should be used. To make all such functions use the verbose form, put </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' verbose yes</code>
</pre>
</dl>
<p> in a startup file (probably <code>.zshrc</code>). This gives the <code>verbose</code> style the value <code>yes</code> in every context inside the completion system, unless that context has a more specific definition. It is best to avoid giving the context as `<code>*</code>&#8216; in case the style has some meaning outside the completion system. </p>
<p> Many such general purpose styles can be configured simply by using the <code>compinstall</code> function. </p>
<p> A more specific example of the use of the <code>verbose</code> style is by the completion for the <code>kill</code> builtin. If the style is set, the builtin lists full job texts and process command lines; otherwise it shows the bare job numbers and PIDs. To turn the style off for this use only: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:kill:*:*' verbose no</code>
</pre>
</dl>
<p> For even more control, the style can use one of the tags `<code>jobs</code>&#8216; or `<code>processes</code>&#8216;. To turn off verbose display only for jobs: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:kill:*:jobs' verbose no</code>
</pre>
</dl>
<p> The <code>-e</code> option to <code>zstyle</code> even allows completion function code to appear as the argument to a style; this requires some understanding of the internals of completion functions (see see <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1))). For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle -e ':completion:*' hosts 'reply=($myhosts)'</code>
</pre>
</dl>
<p> This forces the value of the <code>hosts</code> style to be read from the variable <code>myhosts</code> each time a host name is needed; this is useful if the value of <code>myhosts</code> can change dynamically. For another useful example, see the example in the description of the <code>file-list</code> style below. This form can be slow and should be avoided for commonly examined styles such as <code>menu</code> and <code>list-rows-first</code>. </p>
<p> Note that the order in which styles are <i>defined</i> does not matter; the style mechanism uses the most specific possible match for a particular style to determine the set of values. More precisely, strings are preferred over patterns (for example, `<code>:completion::complete:::foo</code>&#8216; is more specific than `<code>:completion::complete:::*&#8217;</code>), and longer patterns are preferred over shorter patterns. </p>
<p> A good rule of thumb is that any completion style pattern that needs to include more than one wildcard (<code>*</code>) and that does not end in a tag name, should include all six colons (<code>:</code>), possibly surrounding additional wildcards. </p>
<p> Style names like those of tags are arbitrary and depend on the completion function. However, the following two sections list some of the most common tags and styles. </p>
<h3>Standard Tags</h3>
<p> Some of the following are only used when looking up particular styles and do not refer to a type of match. </p>
<dl>
<dt>
<dd> <code>accounts</code> used to look up the <code>users-hosts</code> style</p>
<dt><code>all-expansions</code></p>
<dd> used by the <code>_expand</code> completer when adding the single string containing all possible expansions</p>
<dt><code>all-files</code></p>
<dd> for the names of all files (as distinct from a particular subset, see the <code>globbed-files</code> tag).</p>
<dt><code>arguments</code></p>
<dd> for arguments to a command</p>
<dt><code>arrays</code></p>
<dd> for names of array parameters</p>
<dt><code>association-keys</code></p>
<dd> for keys of associative arrays; used when completing inside a subscript to a parameter of this type</p>
<dt><code>bookmarks</code></p>
<dd> when completing bookmarks (e.g. for URLs and the <code>zftp</code> function suite)</p>
<dt><code>builtins</code></p>
<dd> for names of builtin commands</p>
<dt><code>characters</code></p>
<dd> for single characters in arguments of commands such as <code>stty</code>. Also used when completing character classes after an opening bracket</p>
<dt><code>colormapids</code></p>
<dd> for X colormap ids</p>
<dt><code>colors</code></p>
<dd> for color names</p>
<dt><code>commands</code></p>
<dd> for names of external commands. Also used by complex commands such as <code>cvs</code> when completing names subcommands.</p>
<dt><code>contexts</code></p>
<dd> for contexts in arguments to the <code>zstyle</code> builtin command</p>
<dt><code>corrections</code></p>
<dd> used by the <code>_approximate</code> and <code>_correct</code> completers for possible corrections</p>
<dt><code>cursors</code></p>
<dd> for cursor names used by X programs</p>
<dt><code>default</code></p>
<dd> used in some contexts to provide a way of supplying a default when more specific tags are also valid. Note that this tag is used when only the <i>function</i> field of the context name is set</p>
<dt><code>descriptions</code></p>
<dd> used when looking up the value of the <code>format</code> style to generate descriptions for types of matches</p>
<dt><code>devices</code></p>
<dd> for names of device special files</p>
<dt><code>directories</code></p>
<dd> for names of directories &#8212; <code>local-directories</code> is used instead when completing arguments of <code>cd</code> and related builtin commands when the <code>cdpath</code> array is set</p>
<dt><code>directory-stack</code></p>
<dd> for entries in the directory stack</p>
<dt><code>displays</code></p>
<dd> for X display names</p>
<dt><code>domains</code></p>
<dd> for network domains</p>
<dt><code>email-</code><i>plugin</i></p>
<dd> for email addresses from the `<code>_email-</code><i>plugin</i>&#8216; backend of <code>_email_addresses</code></p>
<dt><code>expansions</code></p>
<dd> used by the <code>_expand</code> completer for individual words (as opposed to the complete set of expansions) resulting from the expansion of a word on the command line</p>
<dt><code>extensions</code></p>
<dd> for X server extensions</p>
<dt><code>file-descriptors</code></p>
<dd> for numbers of open file descriptors</p>
<dt><code>files</code></p>
<dd> the generic file-matching tag used by functions completing filenames</p>
<dt><code>fonts</code></p>
<dd> for X font names</p>
<dt><code>fstypes</code></p>
<dd> for file system types (e.g. for the <code>mount</code> command)</p>
<dt><code>functions</code></p>
<dd> names of functions &#8212; normally shell functions, although certain commands may understand other kinds of function</p>
<dt><code>globbed-files</code></p>
<dd> for filenames when the name has been generated by pattern matching</p>
<dt><code>groups</code></p>
<dd> for names of user groups</p>
<dt><code>history-words</code></p>
<dd> for words from the history</p>
<dt><code>hosts</code></p>
<dd> for hostnames</p>
<dt><code>indexes</code></p>
<dd> for array indexes</p>
<dt><code>jobs</code></p>
<dd> for jobs (as listed by the `<code>jobs</code>&#8216; builtin)</p>
<dt><code>interfaces</code></p>
<dd> for network interfaces</p>
<dt><code>keymaps</code></p>
<dd> for names of zsh keymaps</p>
<dt><code>keysyms</code></p>
<dd> for names of X keysyms</p>
<dt><code>libraries</code></p>
<dd> for names of system libraries</p>
<dt><code>limits</code></p>
<dd> for system limits</p>
<dt><code>local-directories</code></p>
<dd> for names of directories that are subdirectories of the current working directory when completing arguments of <code>cd</code> and related builtin commands (compare <code>path-directories</code>) &#8212; when the <code>cdpath</code> array is unset, <code>directories</code> is used instead</p>
<dt><code>manuals</code></p>
<dd> for names of manual pages</p>
<dt><code>mailboxes</code></p>
<dd> for e-mail folders</p>
<dt><code>maps</code></p>
<dd> for map names (e.g. NIS maps)</p>
<dt><code>messages</code></p>
<dd> used to look up the <code>format</code> style for messages</p>
<dt><code>modifiers</code></p>
<dd> for names of X modifiers</p>
<dt><code>modules</code></p>
<dd> for modules (e.g. <code>zsh</code> modules)</p>
<dt><code>my-accounts</code></p>
<dd> used to look up the <code>users-hosts</code> style</p>
<dt><code>named-directories</code></p>
<dd> for named directories (you wouldn&#8217;t have guessed that, would you?)</p>
<dt><code>names</code></p>
<dd> for all kinds of names</p>
<dt><code>newsgroups</code></p>
<dd> for USENET groups</p>
<dt><code>nicknames</code></p>
<dd> for nicknames of NIS maps</p>
<dt><code>options</code></p>
<dd> for command options</p>
<dt><code>original</code></p>
<dd> used by the <code>_approximate</code>, <code>_correct</code> and <code>_expand</code> completers when offering the original string as a match</p>
<dt><code>other-accounts</code></p>
<dd> used to look up the <code>users-hosts</code> style</p>
<dt><code>other-files</code></p>
<dd> for the names of any non-directory files. This is used instead of <code>all-files</code> when the <code>list-dirs-first</code> style is in effect.</p>
<dt><code>packages</code></p>
<dd> for packages (e.g. <code>rpm</code> or installed <code>Debian</code> packages)</p>
<dt><code>parameters</code></p>
<dd> for names of parameters</p>
<dt><code>path-directories</code></p>
<dd> for names of directories found by searching the <code>cdpath</code> array when completing arguments of <code>cd</code> and related builtin commands (compare <code>local-directories</code>)</p>
<dt><code>paths</code></p>
<dd> used to look up the values of the <code>expand</code>, <code>ambiguous</code> and <code>special-dirs</code> styles</p>
<dt><code>pods</code></p>
<dd> for perl pods (documentation files)</p>
<dt><code>ports</code></p>
<dd> for communication ports</p>
<dt><code>prefixes</code></p>
<dd> for prefixes (like those of a URL)</p>
<dt><code>printers</code></p>
<dd> for print queue names</p>
<dt><code>processes</code></p>
<dd> for process identifiers</p>
<dt><code>processes-names</code></p>
<dd> used to look up the <code>command</code> style when generating the names of processes for <code>killall</code></p>
<dt><code>sequences</code></p>
<dd> for sequences (e.g. <code>mh</code> sequences)</p>
<dt><code>sessions</code></p>
<dd> for sessions in the <code>zftp</code> function suite</p>
<dt><code>signals</code></p>
<dd> for signal names</p>
<dt><code>strings</code></p>
<dd> for strings (e.g. the replacement strings for the <code>cd</code> builtin command)</p>
<dt><code>styles</code></p>
<dd> for styles used by the zstyle builtin command</p>
<dt><code>suffixes</code></p>
<dd> for filename extensions</p>
<dt><code>tags</code></p>
<dd> for tags (e.g. <code>rpm</code> tags)</p>
<dt><code>targets</code></p>
<dd> for makefile targets</p>
<dt><code>time-zones</code></p>
<dd> for time zones (e.g. when setting the <code>TZ</code> parameter)</p>
<dt><code>types</code></p>
<dd> for types of whatever (e.g. address types for the <code>xhost</code> command)</p>
<dt><code>urls</code></p>
<dd> used to look up the <code>urls</code> and <code>local</code> styles when completing URLs</p>
<dt><code>users</code></p>
<dd> for usernames</p>
<dt><code>values</code></p>
<dd> for one of a set of values in certain lists</p>
<dt><code>variant</code></p>
<dd> used by <code>_pick_variant</code> to look up the command to run when determining what program is installed for a particular command name.</p>
<dt><code>visuals</code></p>
<dd> for X visuals</p>
<dt><code>warnings</code></p>
<dd> used to look up the <code>format</code> style for warnings</p>
<dt><code>widgets</code></p>
<dd> for zsh widget names</p>
<dt><code>windows</code></p>
<dd> for IDs of X windows</p>
<dt><code>zsh-options</code></p>
<dd> for shell options</dl>
<h3>Standard Styles</h3>
<p> Note that the values of several of these styles represent boolean values. Any of the strings `<code>true</code>&#8216;, `<code>on</code>&#8216;, `<code>yes</code>&#8216;, and `<code>1</code>&#8216; can be used for the value `true&#8217; and any of the strings `<code>false</code>&#8216;, `<code>off</code>&#8216;, `<code>no</code>&#8216;, and `<code>0</code>&#8216; for the value `false&#8217;. The behavior for any other value is undefined except where explicitly mentioned. The default value may be either `true&#8217; or `false&#8217; if the style is not set. </p>
<p> Some of these styles are tested first for every possible tag corresponding to a type of match, and if no style was found, for the <code>default</code> tag. The most notable styles of this type are <code>menu</code>, <code>list-colors</code> and styles controlling completion listing such as <code>list-packed</code> and <code>last-prompt</code>. When tested for the <code>default</code> tag, only the <i>function</i> field of the context will be set so that a style using the <code>default</code> tag will normally be defined along the lines of: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:default' menu ...</code>
</pre>
</dl>
<dl>
<dt>
<dd> <code>accept-exact</code> This is tested for the <code>default</code> tag in addition to the tags valid for the current context. If it is set to `true&#8217; and any of the trial matches is the same as the string on the command line, this match will immediately be accepted (even if it would otherwise be considered ambiguous).</p>
<dl>
<dt>
<dd>
<p> When completing pathnames (where the tag used is `<code>paths</code>&#8216;) this style accepts any number of patterns as the value in addition to the boolean values. Pathnames matching one of these patterns will be accepted immediately even if the command line contains some more partially typed pathname components and these match no file under the directory accepted. </p>
<p> This style is also used by the <code>_expand</code> completer to decide if words beginning with a tilde or parameter expansion should be expanded. For example, if there are parameters <code>foo</code> and <code>foobar</code>, the string `<code>$foo</code>&#8216; will only be expanded if <code>accept-exact</code> is set to `true&#8217;; otherwise the completion system will be allowed to complete <code>$foo</code> to <code>$foobar</code>. If the style is set to `<code>continue</code>&#8216;, <code>_expand</code> will add the expansion as a match and the completion system will also be allowed to continue.</dl>
<dt><code>accept-exact-dirs</code></p>
<dd> This is used by filename completion. Unlike <code>accept-exact</code> it is a boolean. By default, filename completion examines all components of a path to see if there are completions of that component, even if the component matches an existing directory. For example, when completion after <code>/usr/bin/</code>, the function examines possible completions to <code>/usr</code>.</p>
<dl>
<dt>
<dd>
<p> When this style is `true&#8217;, any prefix of a path that matches an existing directory is accepted without any attempt to complete it further. Hence, in the given example, the path <code>/usr/bin/</code> is accepted immediately and completion tried in that directory. </p>
<p> This style is also useful when completing after directories that magically appear when referenced, such as ZFS <code>.zfs</code> directories or NetApp <code>.snapshot</code> directories. When the style is set the shell does not check for the existence of the directory within the parent directory. </p>
<p> If you wish to inhibit this behaviour entirely, set the <code>path-completion</code> style (see below) to `false&#8217;.</dl>
<dt><code>add-space</code></p>
<dd> This style is used by the <code>_expand</code> completer. If it is `true&#8217; (the default), a space will be inserted after all words resulting from the expansion, or a slash in the case of directory names. If the value is `<code>file</code>&#8216;, the completer will only add a space to names of existing files. Either a boolean `true&#8217; or the value `<code>file</code>&#8216; may be combined with `<code>subst</code>&#8216;, in which case the completer will not add a space to words generated from the expansion of a substitution of the form `<code>$(</code><i>&#8230;</i><code>)</code>&#8216; or `<code>${</code><i>&#8230;</i><code>}</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> The <code>_prefix</code> completer uses this style as a simple boolean value to decide if a space should be inserted before the suffix.</dl>
<dt><code>ambiguous</code></p>
<dd> This applies when completing non-final components of filename paths, in other words those with a trailing slash. If it is set, the cursor is left after the first ambiguous component, even if menu completion is in use. The style is always tested with the <code>paths</code> tag.</p>
<dt><code>assign-list</code></p>
<dd> When completing after an equals sign that is being treated as an assignment, the completion system normally completes only one filename. In some cases the value may be a list of filenames separated by colons, as with <code>PATH</code> and similar parameters. This style can be set to a list of patterns matching the names of such parameters.</p>
<dl>
<dt>
<dd>
<p> The default is to complete lists when the word on the line already contains a colon.</dl>
<dt><code>auto-description</code></p>
<dd> If set, this style&#8217;s value will be used as the description for options that are not described by the completion functions, but that have exactly one argument. The sequence `<code>%d</code>&#8216; in the value will be replaced by the description for this argument. Depending on personal preferences, it may be useful to set this style to something like `<code>specify: %d</code>&#8216;. Note that this may not work for some commands.</p>
<dt><code>avoid-completer</code></p>
<dd> This is used by the <code>_all_matches</code> completer to decide if the string consisting of all matches should be added to the list currently being generated. Its value is a list of names of completers. If any of these is the name of the completer that generated the matches in this completion, the string will not be added.</p>
<dl>
<dt>
<dd>
<p> The default value for this style is `<code>_expand _old_list _correct _approximate</code>&#8216;, i.e. it contains the completers for which a string with all matches will almost never be wanted.</dl>
<dt><code>cache-path</code></p>
<dd> This style defines the path where any cache files containing dumped completion data are stored. It defaults to `<code>$ZDOTDIR/.zcompcache</code>&#8216;, or `<code>$HOME/.zcompcache</code>&#8216; if <code>$ZDOTDIR</code> is not defined. The completion cache will not be used unless the <code>use-cache</code> style is set.</p>
<dt><code>cache-policy</code></p>
<dd> This style defines the function that will be used to determine whether a cache needs rebuilding. See the section on the <code>_cache_invalid</code> function below.</p>
<dt><code>call-command</code></p>
<dd> This style is used in the function for commands such as <code>make</code> and <code>ant</code> where calling the command directly to generate matches suffers problems such as being slow or, as in the case of <code>make</code> can potentially cause actions in the makefile to be executed. If it is set to `true&#8217; the command is called to generate matches. The default value of this style is `false&#8217;.</p>
<dt><code>command</code></p>
<dd> In many places, completion functions need to call external commands to generate the list of completions. This style can be used to override the command that is called in some such cases. The elements of the value are joined with spaces to form a command line to execute. The value can also start with a hyphen, in which case the usual command will be added to the end; this is most useful for putting `<code>builtin</code>&#8216; or `<code>command</code>&#8216; in front to make sure the appropriate version of a command is called, for example to avoid calling a shell function with the same name as an external command.</p>
<dl>
<dt>
<dd>
<p> As an example, the completion function for process IDs uses this style with the <code>processes</code> tag to generate the IDs to complete and the list of processes to display (if the <code>verbose</code> style is `true&#8217;). The list produced by the command should look like the output of the <code>ps</code> command. The first line is not displayed, but is searched for the string `<code>PID</code>&#8216; (or `<code>pid</code>&#8216;) to find the position of the process IDs in the following lines. If the line does not contain `<code>PID</code>&#8216;, the first numbers in each of the other lines are taken as the process IDs to complete. </p>
<p> Note that the completion function generally has to call the specified command for each attempt to generate the completion list. Hence care should be taken to specify only commands that take a short time to run, and in particular to avoid any that may never terminate.</dl>
<dt><code>command-path</code></p>
<dd> This is a list of directories to search for commands to complete. The default for this style is the value of the special parameter <code>path</code>.</p>
<dt><code>commands</code></p>
<dd> This is used by the function completing sub-commands for the system initialisation scripts (residing in <code>/etc/init.d</code> or somewhere not too far away from that). Its values give the default commands to complete for those commands for which the completion function isn&#8217;t able to find them out automatically. The default for this style are the two strings `<code>start</code>&#8216; and `<code>stop</code>&#8216;.</p>
<dt><code>complete</code></p>
<dd> This is used by the <code>_expand_alias</code> function when invoked as a bindable command. If set to `true&#8217; and the word on the command line is not the name of an alias, matching alias names will be completed.</p>
<dt><code>complete-options</code></p>
<dd> This is used by the completer for <code>cd</code>, <code>chdir</code> and <code>pushd</code>. For these commands a <code>&#8211;</code> is used to introduce a directory stack entry and completion of these is far more common than completing options. Hence unless the value of this style is `true&#8217; options will not be completed, even after an initial <code>&#8211;</code>. If it is `true&#8217;, options will be completed after an initial <code>&#8211;</code> unless there is a preceding <code>&#8211;</code><code>&#8211;</code> on the command line.</p>
<dt><code>completer</code></p>
<dd> The strings given as the value of this style provide the names of the completer functions to use. The available completer functions are described in the section `Control Functions&#8217; below.</p>
<dl>
<dt>
<dd>
<p> Each string may be either the name of a completer function or a string of the form `<i>function</i><code>:</code><i>name</i>&#8216;. In the first case the <i>completer</i> field of the context will contain the name of the completer without the leading underscore and with all other underscores replaced by hyphens. In the second case the <i>function</i> is the name of the completer to call, but the context will contain the user-defined <i>name</i> in the <i>completer</i> field of the context. If the <i>name</i> starts with a hyphen, the string for the context will be build from the name of the completer function as in the first case with the <i>name</i> appended to it. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' completer _complete _complete:-foo</code>
</pre>
</dl>
<p> Here, completion will call the <code>_complete</code> completer twice, once using `<code>complete</code>&#8216; and once using `<code>complete-foo</code>&#8216; in the <i>completer</i> field of the context. Normally, using the same completer more than once only makes sense when used with the `<i>functions</i><code>:</code><i>name</i>&#8216; form, because otherwise the context name will be the same in all calls to the completer; possible exceptions to this rule are the <code>_ignored</code> and <code>_prefix</code> completers. </p>
<p> The default value for this style is `<code>_complete _ignored</code>&#8216;: only completion will be done, first using the <code>ignored-patterns</code> style and the <code>$fignore</code> array and then without ignoring matches.</dl>
<dt><code>condition</code></p>
<dd> This style is used by the <code>_list</code> completer function to decide if insertion of matches should be delayed unconditionally. The default is `true&#8217;.</p>
<dt><code>delimiters</code></p>
<dd> This style is used when adding a delimiter for use with history modifiers or glob qualifiers that have delimited arguments. It is an array of preferred delimiters to add. Non-special characters are preferred as the completion system may otherwise become confused. The default list is <code>:</code>, <code>+</code>, <code>/</code>, <code>&#8211;</code>, <code>%</code>. The list may be empty to force a delimiter to be typed.</p>
<dt><code>disabled</code></p>
<dd> If this is set to `true&#8217;, the <code>_expand_alias</code> completer and bindable command will try to expand disabled aliases, too. The default is `false&#8217;.</p>
<dt><code>domains</code></p>
<dd> A list of names of network domains for completion. If this is not set, domain names will be taken from the file <code>/etc/resolv.conf</code>.</p>
<dt><code>environ</code></p>
<dd> The environ style is used when completing for `<code>sudo</code>&#8216;. It is set to an array of `<i>VAR</i><code>=</code><i>value</i>&#8216; assignments to be exported into the local environment before the completion for the target command is invoked.</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:sudo::' environ \ 
  PATH=&quot;/sbin:/usr/sbin:$PATH&quot; HOME=&quot;/root&quot;</code>
</pre>
</dl>
<dt><code>expand</code></p>
<dd> This style is used when completing strings consisting of multiple parts, such as path names.</p>
<dl>
<dt>
<dd>
<p> If one of its values is the string `<code>prefix</code>&#8216;, the partially typed word from the line will be expanded as far as possible even if trailing parts cannot be completed. </p>
<p> If one of its values is the string `<code>suffix</code>&#8216;, matching names for components after the first ambiguous one will also be added. This means that the resulting string is the longest unambiguous string possible. However, menu completion can be used to cycle through all matches.</dl>
<dt><code>fake</code></p>
<dd> This style may be set for any completion context. It specifies additional strings that will always be completed in that context. The form of each string is `<i>value</i><code>:</code><i>description</i>&#8216;; the colon and description may be omitted, but any literal colons in <i>value</i> must be quoted with a backslash. Any <i>description</i> provided is shown alongside the value in completion listings.</p>
<dl>
<dt>
<dd>
<p> It is important to use a sufficiently restrictive context when specifying fake strings. Note that the styles <code>fake-files</code> and <code>fake-parameters</code> provide additional features when completing files or parameters.</dl>
<dt><code>fake-always</code></p>
<dd> This works identically to the <code>fake</code> style except that the <code>ignored-patterns</code> style is not applied to it. This makes it possible to override a set of matches completely by setting the ignored patterns to `<code>*</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> The following shows a way of supplementing any tag with arbitrary data, but having it behave for display purposes like a separate tag. In this example we use the features of the <code>tag-order</code> style to divide the <code>named-directories</code> tag into two when performing completion with the standard completer <code>complete</code> for arguments of <code>cd</code>. The tag <code>named-directories-normal</code> behaves as normal, but the tag <code>named-directories-mine</code> contains a fixed set of directories. This has the effect of adding the match group `<code>extra directories</code>&#8216; with the given completions. </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion::complete:cd:*' tag-order \ 
  'named-directories:-mine:extra\ directories
  named-directories:-normal:named\ directories *'
zstyle ':completion::complete:cd:*:named-directories-mine' \ 
  fake-always mydir1 mydir2
zstyle ':completion::complete:cd:*:named-directories-mine' \ 
  ignored-patterns '*'</code>
</pre>
</dl>
</dl>
<dt><code>fake-files</code></p>
<dd> This style is used when completing files and looked up without a tag. Its values are of the form `<i>dir</i><code>:</code><i>names&#8230;</i>&#8216;. This will add the <i>names</i> (strings separated by spaces) as possible matches when completing in the directory <i>dir</i>, even if no such files really exist. The dir may be a pattern; pattern characters or colons in <i>dir</i> should be quoted with a backslash to be treated literally.</p>
<dl>
<dt>
<dd>
<p> This can be useful on systems that support special file systems whose top-level pathnames can not be listed or generated with glob patterns (but see <code>accept-exact-dirs</code> for a more general way of dealing with this problem). It can also be used for directories for which one does not have read permission. </p>
<p> The pattern form can be used to add a certain `magic&#8217; entry to all directories on a particular file system.</dl>
<dt><code>fake-parameters</code></p>
<dd> This is used by the completion function for parameter names. Its values are names of parameters that might not yet be set but should be completed nonetheless. Each name may also be followed by a colon and a string specifying the type of the parameter (like `<code>scalar</code>&#8216;, `<code>array</code>&#8216; or `<code>integer</code>&#8216;). If the type is given, the name will only be completed if parameters of that type are required in the particular context. Names for which no type is specified will always be completed.</p>
<dt><code>file-list</code></p>
<dd> This style controls whether files completed using the standard builtin mechanism are to be listed with a long list similar to <code>ls -l</code>. Note that this feature uses the shell module <code>zsh/stat</code> for file information; this loads the builtin <code>stat</code> which will replace any external <code>stat</code> executable. To avoid this the following code can be included in an initialization file:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zmodload -i zsh/stat
disable stat</code>
</pre>
</dl>
<p> The style may either be set to a `true&#8217; value (or `<code>all</code>&#8216;), or one of the values `<code>insert</code>&#8216; or `<code>list</code>&#8216;, indicating that files are to be listed in long format in all circumstances, or when attempting to insert a file name, or when listing file names without attempting to insert one. </p>
<p> More generally, the value may be an array of any of the above values, optionally followed by <code>=</code><i>num</i>. If <i>num</i> is present it gives the maximum number of matches for which long listing style will be used. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' file-list list=20 insert=10</code>
</pre>
</dl>
<p> specifies that long format will be used when listing up to 20 files or inserting a file with up to 10 matches (assuming a listing is to be shown at all, for example on an ambiguous completion), else short format will be used. </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle -e ':completion:*' file-list \ 
       '(( ${+NUMERIC} )) &amp;&amp; reply=(true)'</code>
</pre>
</dl>
<p> specifies that long format will be used any time a numeric argument is supplied, else short format.</dl>
<dt><code>file-patterns</code></p>
<dd> This is used by the standard function for completing filenames, <code>_files</code>. If the style is unset up to three tags are offered, `<code>globbed-files</code>&#8216;,`<code>directories</code>&#8216; and `<code>all-files</code>&#8216;, depending on the types of files expected by the caller of <code>_files</code>. The first two (`<code>globbed-files</code>&#8216; and `<code>directories</code>&#8216;) are normally offered together to make it easier to complete files in sub-directories.</p>
<dl>
<dt>
<dd>
<p> The <code>file-patterns</code> style provides alternatives to the default tags, which are not used. Its value consists of elements of the form `<i>pattern</i><code>:</code><i>tag</i>&#8216;; each string may contain any number of such specifications separated by spaces. </p>
<p> The <i>pattern</i> is a pattern that is to be used to generate filenames. Any occurrence of the sequence `<code>%p</code>&#8216; is replaced by any pattern(s) passed by the function calling <code>_files</code>. Colons in the pattern must be preceded by a backslash to make them distinguishable from the colon before the <i>tag</i>. If more than one pattern is needed, the patterns can be given inside braces, separated by commas. </p>
<p> The <i>tag</i>s of all strings in the value will be offered by <code>_files</code> and used when looking up other styles. Any <i>tag</i>s in the same word will be offered at the same time and before later words. If no `<code>:</code><i>tag</i>&#8216; is given the `<code>files</code>&#8216; tag will be used. </p>
<p> The <i>tag</i> may also be followed by an optional second colon and a description, which will be used for the `<code>%d</code>&#8216; in the value of the <code>format</code> style (if that is set) instead of the default description supplied by the completion function. If the description given here contains itself a `<code>%d</code>&#8216;, that is replaced with the description supplied by the completion function. </p>
<p> For example, to make the <code>rm</code> command first complete only names of object files and then the names of all files if there is no matching object file: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:rm:*:*' file-patterns \ 
    '*.o:object-files' '%p:all-files'</code>
</pre>
</dl>
<p> To alter the default behaviour of file completion &#8212; offer files matching a pattern and directories on the first attempt, then all files &#8212; to offer only matching files on the first attempt, then directories, and finally all files: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' file-patterns \ 
    '%p:globbed-files' '*(-/):directories' '*:all-files'</code>
</pre>
</dl>
<p> This works even where there is no special pattern: <code>_files</code> matches all files using the pattern `<code>*</code>&#8216; at the first step and stops when it sees this pattern. Note also it will never try a pattern more than once for a single completion attempt. </p>
<p> During the execution of completion functions, the <code>EXTENDED_GLOB</code> option is in effect, so the characters `<code>#</code>&#8216;, `<code>~</code>&#8216; and `<code>^</code>&#8216; have special meanings in the patterns.</dl>
<dt><code>file-sort</code></p>
<dd> The standard filename completion function uses this style without a tag to determine in which order the names should be listed; menu completion will cycle through them in the same order. The possible values are: `<code>size</code>&#8216; to sort by the size of the file; `<code>links</code>&#8216; to sort by the number of links to the file; `<code>modification</code>&#8216; (or `<code>time</code>&#8216; or `<code>date</code>&#8216;) to sort by the last modification time; `<code>access</code>&#8216; to sort by the last access time; and `<code>inode</code>&#8216; (or `<code>change</code>&#8216;) to sort by the last inode change time. If the style is set to any other value, or is unset, files will be sorted alphabetically by name. If the value contains the string `<code>reverse</code>&#8216;, sorting is done in the opposite order. If the value contains the string `<code>follow</code>&#8216;, timestamps are associated with the targets of symbolic links; the default is to use the timestamps of the links themselves.</p>
<dt><code>file-split-chars</code></p>
<dd> A set of characters that will cause <i>all</i> file completions for the given context to be split at the point where any of the characters occurs. A typical use is to set the style to <code>:</code>; then everything up to and including the last <code>:</code> in the string so far is ignored when completing files. As this is quite heavy-handed, it is usually preferable to update completion functions for contexts where this behaviour is useful.</p>
<dt><code>filter</code></p>
<dd> The <code>ldap</code> plugin of email address completion (see <code>_email_addresses</code>) uses this style to specify the attributes to match against when filtering entries. So for example, if the style is set to `<code>sn</code>&#8216;, matching is done against surnames. Standard LDAP filtering is used so normal completion matching is bypassed. If this style is not set, the LDAP plugin is skipped. You may also need to set the <code>command</code> style to specify how to connect to your LDAP server.</p>
<dt><code>force-list</code></p>
<dd> This forces a list of completions to be shown at any point where listing is done, even in cases where the list would usually be suppressed. For example, normally the list is only shown if there are at least two different matches. By setting this style to `<code>always</code>&#8216;, the list will always be shown, even if there is only a single match that will immediately be accepted. The style may also be set to a number. In this case the list will be shown if there are at least that many matches, even if they would all insert the same string.</p>
<dl>
<dt>
<dd>
<p> This style is tested for the default tag as well as for each tag valid for the current completion. Hence the listing can be forced only for certain types of match.</dl>
<dt><code>format</code></p>
<dd> If this is set for the <code>descriptions</code> tag, its value is used as a string to display above matches in completion lists. The sequence `<code>%d</code>&#8216; in this string will be replaced with a short description of what these matches are. This string may also contain the output attribute sequences understood by <code>compadd -X</code> (see <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1)).</p>
<dl>
<dt>
<dd>
<p> The style is tested with each tag valid for the current completion before it is tested for the <code>descriptions</code> tag. Hence different format strings can be defined for different types of match. </p>
<p> Note also that some completer functions define additional `<code>%</code>&#8216;-sequences. These are described for the completer functions that make use of them. </p>
<p> Some completion functions display messages that may be customised by setting this style for the <code>messages</code> tag. Here, the `<code>%d</code>&#8216; is replaced with a message given by the completion function. </p>
<p> Finally, the format string is looked up with the <code>warnings</code> tag, for use when no matches could be generated at all. In this case the `<code>%d</code>&#8216; is replaced with the descriptions for the matches that were expected separated by spaces. The sequence `<code>%D</code>&#8216; is replaced with the same descriptions separated by newlines. </p>
<p> It is possible to use printf-style field width specifiers with `<code>%d</code>&#8216; and similar escape sequences. This is handled by the <code>zformat</code> builtin command from the <code>zsh/zutil</code> module, see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</dl>
<dt><code>glob</code></p>
<dd> This is used by the <code>_expand</code> completer. If it is set to `true&#8217; (the default), globbing will be attempted on the words resulting from a previous substitution (see the <code>substitute</code> style) or else the original string from the line.</p>
<dt><code>global</code></p>
<dd> If this is set to `true&#8217; (the default), the <code>_expand_alias</code> completer and bindable command will try to expand global aliases.</p>
<dt><code>group-name</code></p>
<dd> The completion system can group different types of matches, which appear in separate lists. This style can be used to give the names of groups for particular tags. For example, in command position the completion system generates names of builtin and external commands, names of aliases, shell functions and parameters and reserved words as possible completions. To have the external commands and shell functions listed separately:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:-command-:*:commands' \ 
       group-name commands
zstyle ':completion:*:*:-command-:*:functions' \ 
       group-name functions</code>
</pre>
</dl>
<p> As a consequence, any match with the same tag will be displayed in the same group. </p>
<p> If the name given is the empty string the name of the tag for the matches will be used as the name of the group. So, to have all different types of matches displayed separately, one can just set: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' group-name ''</code>
</pre>
</dl>
<p> All matches for which no group name is defined will be put in a group named <code>-default-</code>.</dl>
<dt><code>group-order</code></p>
<dd> This style is additional to the <code>group-name</code> style to specify the order for display of the groups defined by that style (compare <code>tag-order</code>, which determines which completions appear at all). The groups named are shown in the given order; any other groups are shown in the order defined by the completion function.</p>
<dl>
<dt>
<dd>
<p> For example, to have names of builtin commands, shell functions and external commands appear in that order when completing in command position: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:-command-:*:*' group-order \ 
       builtins functions commands</code>
</pre>
</dl>
</dl>
<dt><code>groups</code></p>
<dd> A list of names of UNIX groups. If this is not set, group names are taken from the YP database or the file `<code>/etc/group</code>&#8216;.</p>
<dt><code>hidden</code></p>
<dd> If this is set to `true&#8217;, matches for the given context will not be listed, although any description for the matches set with the <code>format</code> style will be shown. If it is set to `<code>all</code>&#8216;, not even the description will be displayed.</p>
<dl>
<dt>
<dd>
<p> Note that the matches will still be completed; they are just not shown in the list. To avoid having matches considered as possible completions at all, the <code>tag-order</code> style can be modified as described below.</dl>
<dt><code>hosts</code></p>
<dd> A list of names of hosts that should be completed. If this is not set, hostnames are taken from the file `<code>/etc/hosts</code>&#8216;.</p>
<dt><code>hosts-ports</code></p>
<dd> This style is used by commands that need or accept hostnames and network ports. The strings in the value should be of the form `<i>host</i><code>:</code><i>port</i>&#8216;. Valid ports are determined by the presence of hostnames; multiple ports for the same host may appear.</p>
<dt><code>ignore-line</code></p>
<dd> This is tested for each tag valid for the current completion. If it is set to `true&#8217;, none of the words that are already on the line will be considered as possible completions. If it is set to `<code>current</code>&#8216;, the word the cursor is on will not be considered as a possible completion. The value `<code>current-shown</code>&#8216; is similar but only applies if the list of completions is currently shown on the screen. Finally, if the style is set to `<code>other</code>&#8216;, all words on the line except for the current one will be excluded from the possible completions.</p>
<dl>
<dt>
<dd>
<p> The values `<code>current</code>&#8216; and `<code>current-shown</code>&#8216; are a bit like the opposite of the <code>accept-exact</code> style: only strings with missing characters will be completed. </p>
<p> Note that you almost certainly don&#8217;t want to set this to `true&#8217; or `<code>other</code>&#8216; for a general context such as `<code>:completion:*</code>&#8216;. This is because it would disallow completion of, for example, options multiple times even if the command in question accepts the option more than once.</dl>
<dt><code>ignore-parents</code></p>
<dd> The style is tested without a tag by the function completing pathnames in order to determine whether to ignore the names of directories already mentioned in the current word, or the name of the current working directory. The value must include one or both of the following strings:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>parent</code> The name of any directory whose path is already contained in the word on the line is ignored. For example, when completing after <code>foo/../</code>, the directory <code>foo</code> will not be considered a valid completion.</p>
<dt><code>pwd</code></p>
<dd> The name of the current working directory will not be completed; hence, for example, completion after <code>../</code> will not use the name of the current directory.</dl>
<p> In addition, the value may include one or both of: </p>
<dl>
<dt>
<dd> <code>..</code> Ignore the specified directories only when the word on the line contains the substring `<code>../</code>&#8216;.</p>
<dt><code>directory</code></p>
<dd> Ignore the specified directories only when names of directories are completed, not when completing names of files.</dl>
<p> Excluded values act in a similar fashion to values of the <code>ignored-patterns</code> style, so they can be restored to consideration by the <code>_ignored</code> completer.</dl>
<dt><code>extra-verbose</code></p>
<dd> If set, the completion listing is more verbose at the cost of a probable decrease in completion speed. Completion performance will suffer if this style is set to `true&#8217;.</p>
<dt><code>ignored-patterns</code></p>
<dd> A list of patterns; any trial completion matching one of the patterns will be excluded from consideration. The <code>_ignored</code> completer can appear in the list of completers to restore the ignored matches. This is a more configurable version of the shell parameter <code>$fignore</code>.</p>
<dl>
<dt>
<dd>
<p> Note that the <code>EXTENDED_GLOB</code> option is set during the execution of completion functions, so the characters `<code>#</code>&#8216;, `<code>~</code>&#8216; and `<code>^</code>&#8216; have special meanings in the patterns.</dl>
<dt><code>insert</code></p>
<dd> This style is used by the <code>_all_matches</code> completer to decide whether to insert the list of all matches unconditionally instead of adding the list as another match.</p>
<dt><code>insert-ids</code></p>
<dd> When completing process IDs, for example as arguments to the <code>kill</code> and <code>wait</code> builtins the name of a command may be converted to the appropriate process ID. A problem arises when the process name typed is not unique. By default (or if this style is set explicitly to `<code>menu</code>&#8216;) the name will be converted immediately to a set of possible IDs, and menu completion will be started to cycle through them.</p>
<dl>
<dt>
<dd>
<p> If the value of the style is `<code>single</code>&#8216;, the shell will wait until the user has typed enough to make the command unique before converting the name to an ID; attempts at completion will be unsuccessful until that point. If the value is any other string, menu completion will be started when the string typed by the user is longer than the common prefix to the corresponding IDs.</dl>
<dt><code>insert-tab</code></p>
<dd> If this is set to `true&#8217;, the completion system will insert a TAB character (assuming that was used to start completion) instead of performing completion when there is no non-blank character to the left of the cursor. If it is set to `false&#8217;, completion will be done even there.</p>
<dl>
<dt>
<dd>
<p> The value may also contain the substrings `<code>pending</code>&#8216; or `<code>pending=</code><i>val</i>&#8216;. In this case, the typed character will be inserted instead of starting completion when there is unprocessed input pending. If a <i>val</i> is given, completion will not be done if there are at least that many characters of unprocessed input. This is often useful when pasting characters into a terminal. Note however, that it relies on the <code>$PENDING</code> special parameter from the <code>zsh/zle</code> module being set properly which is not guaranteed on all platforms. </p>
<p> The default value of this style is `true&#8217; except for completion within <code>vared</code> builtin command where it is `false&#8217;.</dl>
<dt><code>insert-unambiguous</code></p>
<dd> This is used by the <code>_match</code> and <code>_approximate</code> completers. These completers are often used with menu completion since the word typed may bear little resemblance to the final completion. However, if this style is `true&#8217;, the completer will start menu completion only if it could find no unambiguous initial string at least as long as the original string typed by the user.</p>
<dl>
<dt>
<dd>
<p> In the case of the <code>_approximate</code> completer, the completer field in the context will already have been set to one of <code>correct-</code><i>num</i> or <code>approximate-</code><i>num</i>, where <i>num</i> is the number of errors that were accepted. </p>
<p> In the case of the <code>_match</code> completer, the style may also be set to the string `<code>pattern</code>&#8216;. Then the pattern on the line is left unchanged if it does not match unambiguously.</dl>
<dt><code>gain-privileges</code></p>
<dd> If set to <code>true</code>, this style enables the use of commands like <code>sudo</code> or <code>doas</code> to gain extra privileges when retrieving information for completion. This is only done when a command such as <code>sudo</code> appears on the command-line. To force the use of, e.g. <code>sudo</code> or to override any prefix that might be added due to <code>gain-privileges</code>, the <code>command</code> style can be used with a value that begins with a hyphen.</p>
<dt><code>keep-prefix</code></p>
<dd> This style is used by the <code>_expand</code> completer. If it is `true&#8217;, the completer will try to keep a prefix containing a tilde or parameter expansion. Hence, for example, the string `<code>~/f*</code>&#8216; would be expanded to `<code>~/foo</code>&#8216; instead of `<code>/home/user/foo</code>&#8216;. If the style is set to `<code>changed</code>&#8216; (the default), the prefix will only be left unchanged if there were other changes between the expanded words and the original word from the command line. Any other value forces the prefix to be expanded unconditionally.</p>
<dl>
<dt>
<dd>
<p> The behaviour of <code>_expand</code> when this style is `true&#8217; is to cause <code>_expand</code> to give up when a single expansion with the restored prefix is the same as the original; hence any remaining completers may be called.</dl>
<dt><code>last-prompt</code></p>
<dd> This is a more flexible form of the <code>ALWAYS_LAST_PROMPT</code> option. If it is `true&#8217;, the completion system will try to return the cursor to the previous command line after displaying a completion list. It is tested for all tags valid for the current completion, then the <code>default</code> tag. The cursor will be moved back to the previous line if this style is `true&#8217; for all types of match. Note that unlike the <code>ALWAYS_LAST_PROMPT</code> option this is independent of the numeric argument.</p>
<dt><code>known-hosts-files</code></p>
<dd> This style should contain a list of files to search for host names and (if the <code>use-ip</code> style is set) IP addresses in a format compatible with ssh <code>known_hosts</code> files. If it is not set, the files <code>/etc/ssh/ssh_known_hosts</code> and <code>~/.ssh/known_hosts</code> are used.</p>
<dt><code>list</code></p>
<dd> This style is used by the <code>_history_complete_word</code> bindable command. If it is set to `true&#8217; it has no effect. If it is set to `false&#8217; matches will not be listed. This overrides the setting of the options controlling listing behaviour, in particular <code>AUTO_LIST</code>. The context always starts with `<code>:completion:history-words</code>&#8216;.</p>
<dt><code>list-colors</code></p>
<dd> If the <code>zsh/complist</code> module is loaded, this style can be used to set color specifications. This mechanism replaces the use of the <code>ZLS_COLORS</code> and <code>ZLS_COLOURS</code> parameters described in the section `The zsh/complist Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1), but the syntax is the same.</p>
<dl>
<dt>
<dd>
<p> If this style is set for the <code>default</code> tag, the strings in the value are taken as specifications that are to be used everywhere. If it is set for other tags, the specifications are used only for matches of the type described by the tag. For this to work best, the <code>group-name</code> style must be set to an empty string. </p>
<p> In addition to setting styles for specific tags, it is also possible to use group names specified explicitly by the <code>group-name</code> tag together with the `<code>(group)</code>&#8216; syntax allowed by the <code>ZLS_COLORS</code> and <code>ZLS_COLOURS</code> parameters and simply using the <code>default</code> tag. </p>
<p> It is possible to use any color specifications already set up for the GNU version of the <code>ls</code> command: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:default' list-colors \ 
       ${(s.:.)LS_COLORS}</code>
</pre>
</dl>
<p> The default colors are the same as for the GNU <code>ls</code> command and can be obtained by setting the style to an empty string (i.e. <code>&#8221;</code>).</dl>
<dt><code>list-dirs-first</code></p>
<dd> This is used by file completion. If set, directories to be completed are listed separately from and before completion for other files, regardless of tag ordering. In addition, the tag <code>other-files</code> is used in place of <code>all-files</code> for the remaining files, to indicate that no directories are presented with that tag.</p>
<dt><code>list-grouped</code></p>
<dd> If this style is `true&#8217; (the default), the completion system will try to make certain completion listings more compact by grouping matches. For example, options for commands that have the same description (shown when the <code>verbose</code> style is set to `true&#8217;) will appear as a single entry. However, menu selection can be used to cycle through all the matches.</p>
<dt><code>list-packed</code></p>
<dd> This is tested for each tag valid in the current context as well as the <code>default</code> tag. If it is set to `true&#8217;, the corresponding matches appear in listings as if the <code>LIST_PACKED</code> option were set. If it is set to `false&#8217;, they are listed normally.</p>
<dt><code>list-prompt</code></p>
<dd> If this style is set for the <code>default</code> tag, completion lists that don&#8217;t fit on the screen can be scrolled (see the description of the <code>zsh/complist</code> module in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). The value, if not the empty string, will be displayed after every screenful and the shell will prompt for a key press; if the style is set to the empty string, a default prompt will be used.</p>
<dl>
<dt>
<dd>
<p> The value may contain the escape sequences: `<code>%l</code>&#8216; or `<code>%L</code>&#8216;, which will be replaced by the number of the last line displayed and the total number of lines; `<code>%m</code>&#8216; or `<code>%M</code>&#8216;, the number of the last match shown and the total number of matches; and `<code>%p</code>&#8216; and `<code>%P</code>&#8216;, `<code>Top</code>&#8216; when at the beginning of the list, `<code>Bottom</code>&#8216; when at the end and the position shown as a percentage of the total length otherwise. In each case the form with the uppercase letter will be replaced by a string of fixed width, padded to the right with spaces, while the lowercase form will be replaced by a variable width string. As in other prompt strings, the escape sequences `<code>%S</code>&#8216;, `<code>%s</code>&#8216;, `<code>%B</code>&#8216;, `<code>%b</code>&#8216;, `<code>%U</code>&#8216;, `<code>%u</code>&#8216; for entering and leaving the display modes standout, bold and underline, and `<code>%F</code>&#8216;, `<code>%f</code>&#8216;, `<code>%K</code>&#8216;, `<code>%k</code>&#8216; for changing the foreground background colour, are also available, as is the form `<code>%{</code>&#8230;<code>%}</code>&#8216; for enclosing escape sequences which display with zero (or, with a numeric argument, some other) width. </p>
<p> After deleting this prompt the variable <code>LISTPROMPT</code> should be unset for the removal to take effect.</dl>
<dt><code>list-rows-first</code></p>
<dd> This style is tested in the same way as the <code>list-packed</code> style and determines whether matches are to be listed in a rows-first fashion as if the <code>LIST_ROWS_FIRST</code> option were set.</p>
<dt><code>list-suffixes</code></p>
<dd> This style is used by the function that completes filenames. If it is `true&#8217;, and completion is attempted on a string containing multiple partially typed pathname components, all ambiguous components will be shown. Otherwise, completion stops at the first ambiguous component.</p>
<dt><code>list-separator</code></p>
<dd> The value of this style is used in completion listing to separate the string to complete from a description when possible (e.g. when completing options). It defaults to `<code>&#8211;</code><code>&#8211;</code>&#8216; (two hyphens).</p>
<dt><code>local</code></p>
<dd> This is for use with functions that complete URLs for which the corresponding files are available directly from the file system. Its value should consist of three strings: a hostname, the path to the default web pages for the server, and the directory name used by a user placing web pages within their home area.</p>
<dl>
<dt>
<dd>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' local toast \ 
    /var/http/public/toast public_html</code>
</pre>
</dl>
<p> Completion after `<code><a rel="nofollow" href="http://toast/stuff/">http://toast/stuff/</a></code>&#8216; will look for files in the directory <code>/var/http/public/toast/stuff</code>, while completion after `<code><a rel="nofollow" href="http://toast/~yousir/">http://toast/~yousir/</a></code>&#8216; will look for files in the directory <code>~yousir/public_html</code>.</dl>
<dt><code>mail-directory</code></p>
<dd> If set, zsh will assume that mailbox files can be found in the directory specified. It defaults to `<code>~/Mail</code>&#8216;.</p>
<dt><code>match-original</code></p>
<dd> This is used by the <code>_match</code> completer. If it is set to <code>only</code>, <code>_match</code> will try to generate matches without inserting a `<code>*</code>&#8216; at the cursor position. If set to any other non-empty value, it will first try to generate matches without inserting the `<code>*</code>&#8216; and if that yields no matches, it will try again with the `<code>*</code>&#8216; inserted. If it is unset or set to the empty string, matching will only be performed with the `<code>*</code>&#8216; inserted.</p>
<dt><code>matcher</code></p>
<dd> This style is tested separately for each tag valid in the current context. Its value is placed before any match specifications given by the <code>matcher-list</code> style so can override them via the use of an <code>x:</code> specification. The value should be in the form described in the section `Completion Matching Control&#8217; in <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1). For examples of this, see the description of the <code>tag-order</code> style.</p>
<dl>
<dt>
<dd>
<p> For notes comparing the use of this and the <code>matcher-list</code> style, see under the description of the <code>tag-order</code> style.</dl>
<dt><code>matcher-list</code></p>
<dd> This style can be set to a list of match specifications that are to be applied everywhere. Match specifications are described in the section `Completion Matching Control&#8217; in <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1). The completion system will try them one after another for each completer selected. For example, to try first simple completion and, if that generates no matches, case-insensitive completion:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
zstyle ':completion:*' matcher - list '' 'm:{a-zA-Z}={A-Za-z}'
</code></pre>
</dl>
<p> By default each specification replaces the previous one; however, if a specification is prefixed with <code>+</code>, it is added to the existing list. Hence it is possible to create increasingly general specifications without repetition: </p>
<dl>
<dt>
<dd>
zstyle &#8216;:completion:*&#8217; matcher &#8211; list \<br />
       &#8221; &#8216;+m:{a-z}={A-Z}&#8217; &#8216;+m:{A-Z}={a-z}&#8217;
</dl>
<p> It is possible to create match specifications valid for particular completers by using the third field of the context. This applies only to completers that override the global matcher-list, which as of this writing includes only <code>_prefix</code> and <code>_ignored</code>. For example, to use the completers <code>_complete</code> and <code>_prefix</code> but allow case-insensitive completion only with <code>_complete</code>: </p>
<dl>
<dt>
<dd>
zstyle &#8216;:completion:*&#8217; completer _complete _prefix<br />
        zstyle &#8216;:completion:*:complete:*:*:*&#8217; matcher &#8211;<br />
    list \<br />
       &#8221; &#8216;m:{a-zA-Z}={A-Za-z}&#8217;
</dl>
<p> User-defined names, as explained for the <code>completer</code> style, are available. This makes it possible to try the same completer more than once with different match specifications each time. For example, to try normal completion without a match specification, then normal completion with case-insensitive matching, then correction, and finally partial-word completion: </p>
<dl>
<dt>
<dd>
zstyle &#8216;:completion:*&#8217; completer \<br />
    _complete _correct _complete : foo<br />
                                       zstyle &#8216;:completion:*:complete:*:*:*&#8217; matcher &#8211;<br />
                                   list \<br />
    &#8221; &#8216;m:{a-zA-Z}={A-Za-z}&#8217; zstyle &#8216;:completion:*:foo:*:*:*&#8217; matcher &#8211;<br />
                                   list \<br />
    &#8216;m:{a-zA-Z}={A-Za-z} r:|[-_./]=* r:|=*&#8217;
</dl>
<p> If the style is unset in any context no match specification is applied. Note also that some completers such as <code>_correct</code> and <code>_approximate</code> do not use the match specifications at all, though these completers will only ever be called once even if the <code>matcher-list</code> contains more than one element. </p>
<p> Where multiple specifications are useful, note that the <i>entire</i> completion is done for each element of <code>matcher-list</code>, which can quickly reduce the shell&#8217;s performance. As a rough rule of thumb, one to three strings will give acceptable performance. On the other hand, putting multiple space-separated values into the same string does not have an appreciable impact on performance. </p>
<p> If there is no current matcher or it is empty, and the option <code>NO_CASE_GLOB</code> is in effect, the matching for files is performed case-insensitively in any case. However, any matcher must explicitly specify case-insensitive matching if that is required. </p>
<p> For notes comparing the use of this and the <code>matcher</code> style, see under the description of the <code>tag-order</code> style.</dl>
<dt><code>max-errors</code></p>
<dd> This is used by the <code>_approximate</code> and <code>_correct</code> completer functions to determine the maximum number of errors to allow. The completer will try to generate completions by first allowing one error, then two errors, and so on, until either a match or matches were found or the maximum number of errors given by this style has been reached.</p>
<dl>
<dt>
<dd>
<p> If the value for this style contains the string `<code>numeric</code>&#8216;, the completer function will take any numeric argument as the maximum number of errors allowed. For example, with </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:approximate:::' max-errors 2 numeric</code>
</pre>
</dl>
<p> two errors are allowed if no numeric argument is given, but with a numeric argument of six (as in `<code>ESC-6 TAB</code>&#8216;), up to six errors are accepted. Hence with a value of `<code>0 numeric</code>&#8216;, no correcting completion will be attempted unless a numeric argument is given. </p>
<p> If the value contains the string `<code>not-numeric</code>&#8216;, the completer will <i>not</i> try to generate corrected completions when given a numeric argument, so in this case the number given should be greater than zero. For example, `<code>2 not-numeric</code>&#8216; specifies that correcting completion with two errors will usually be performed, but if a numeric argument is given, correcting completion will not be performed. </p>
<p> The default value for this style is `<code>2 numeric</code>&#8216;.</dl>
<dt><code>max-matches-width</code></p>
<dd> This style is used to determine the trade off between the width of the display used for matches and the width used for their descriptions when the <code>verbose</code> style is in effect. The value gives the number of display columns to reserve for the matches. The default is half the width of the screen.</p>
<dl>
<dt>
<dd>
<p> This has the most impact when several matches have the same description and so will be grouped together. Increasing the style will allow more matches to be grouped together; decreasing it will allow more of the description to be visible.</dl>
<dt><code>menu</code></p>
<dd> If this is `true&#8217; in the context of any of the tags defined for the current completion menu completion will be used. The value for a specific tag will take precedence over that for the `<code>default</code>&#8216; tag.</p>
<dl>
<dt>
<dd>
<p> If none of the values found in this way is `true&#8217; but at least one is set to `<code>auto</code>&#8216;, the shell behaves as if the <code>AUTO_MENU</code> option is set. </p>
<p> If one of the values is explicitly set to `false&#8217;, menu completion will be explicitly turned off, overriding the <code>MENU_COMPLETE</code> option and other settings. </p>
<p> In the form `<code>yes=</code><i>num</i>&#8216;, where `<code>yes</code>&#8216; may be any of the `true&#8217; values (`<code>yes</code>&#8216;, `<code>true</code>&#8216;, `<code>on</code>&#8216; and `<code>1</code>&#8216;), menu completion will be turned on if there are at least <i>num</i> matches. In the form `<code>yes=long</code>&#8216;, menu completion will be turned on if the list does not fit on the screen. This does not activate menu completion if the widget normally only lists completions, but menu completion can be activated in that case with the value `<code>yes=long-list</code>&#8216; (Typically, the value `<code>select=long-list</code>&#8216; described later is more useful as it provides control over scrolling.) </p>
<p> Similarly, with any of the `false&#8217; values (as in `<code>no=10</code>&#8216;), menu completion will <i>not</i> be used if there are <i>num</i> or more matches. </p>
<p> The value of this widget also controls menu selection, as implemented by the <code>zsh/complist</code> module. The following values may appear either alongside or instead of the values above. </p>
<p> If the value contains the string `<code>select</code>&#8216;, menu selection will be started unconditionally. </p>
<p> In the form `<code>select=</code><i>num</i>&#8216;, menu selection will only be started if there are at least <i>num</i> matches. If the values for more than one tag provide a number, the smallest number is taken. </p>
<p> Menu selection can be turned off explicitly by defining a value containing the string`<code>no-select</code>&#8216;. </p>
<p> It is also possible to start menu selection only if the list of matches does not fit on the screen by using the value `<code>select=long</code>&#8216;. To start menu selection even if the current widget only performs listing, use the value `<code>select=long-list</code>&#8216;. </p>
<p> To turn on menu completion or menu selection when there are a certain number of matches <i>or</i> the list of matches does not fit on the screen, both of `<code>yes=</code>&#8216; and `<code>select=</code>&#8216; may be given twice, once with a number and once with `<code>long</code>&#8216; or `<code>long-list</code>&#8216;. </p>
<p> Finally, it is possible to activate two special modes of menu selection. The word `<code>interactive</code>&#8216; in the value causes interactive mode to be entered immediately when menu selection is started; see the description of the <code>zsh/complist</code> module in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1) for a description of interactive mode. Including the string `<code>search</code>&#8216; does the same for incremental search mode. To select backward incremental search, include the string `<code>search-backward</code>&#8216;.</dl>
<dt><code>muttrc</code></p>
<dd> If set, gives the location of the mutt configuration file. It defaults to `<code>~/.muttrc</code>&#8216;.</p>
<dt><code>numbers</code></p>
<dd> This is used with the <code>jobs</code> tag. If it is `true&#8217;, the shell will complete job numbers instead of the shortest unambiguous prefix of the job command text. If the value is a number, job numbers will only be used if that many words from the job descriptions are required to resolve ambiguities. For example, if the value is `<code>1</code>&#8216;, strings will only be used if all jobs differ in the first word on their command lines.</p>
<dt><code>old-list</code></p>
<dd> This is used by the <code>_oldlist</code> completer. If it is set to `<code>always</code>&#8216;, then standard widgets which perform listing will retain the current list of matches, however they were generated; this can be turned off explicitly with the value `<code>never</code>&#8216;, giving the behaviour without the <code>_oldlist</code> completer. If the style is unset, or any other value, then the existing list of completions is displayed if it is not already; otherwise, the standard completion list is generated; this is the default behaviour of <code>_oldlist</code>. However, if there is an old list and this style contains the name of the completer function that generated the list, then the old list will be used even if it was generated by a widget which does not do listing.</p>
<dl>
<dt>
<dd>
<p> For example, suppose you type <code>^Xc</code> to use the <code>_correct_word</code> widget, which generates a list of corrections for the word under the cursor. Usually, typing <code>^D</code> would generate a standard list of completions for the word on the command line, and show that. With <code>_oldlist</code>, it will instead show the list of corrections already generated. </p>
<p> As another example consider the <code>_match</code> completer: with the <code>insert-unambiguous</code> style set to `true&#8217; it inserts only a common prefix string, if there is any. However, this may remove parts of the original pattern, so that further completion could produce more matches than on the first attempt. By using the <code>_oldlist</code> completer and setting this style to <code>_match</code>, the list of matches generated on the first attempt will be used again.</dl>
<dt><code>old-matches</code></p>
<dd> This is used by the <code>_all_matches</code> completer to decide if an old list of matches should be used if one exists. This is selected by one of the `true&#8217; values or by the string `<code>only</code>&#8216;. If the value is `<code>only</code>&#8216;, <code>_all_matches</code> will only use an old list and won&#8217;t have any effect on the list of matches currently being generated.</p>
<dl>
<dt>
<dd>
<p> If this style is set it is generally unwise to call the <code>_all_matches</code> completer unconditionally. One possible use is for either this style or the <code>completer</code> style to be defined with the <code>-e</code> option to <code>zstyle</code> to make the style conditional.</dl>
<dt><code>old-menu</code></p>
<dd> This is used by the <code>_oldlist</code> completer. It controls how menu completion behaves when a completion has already been inserted and the user types a standard completion key such as <code>TAB</code>. The default behaviour of <code>_oldlist</code> is that menu completion always continues with the existing list of completions. If this style is set to `false&#8217;, however, a new completion is started if the old list was generated by a different completion command; this is the behaviour without the <code>_oldlist</code> completer.</p>
<dl>
<dt>
<dd>
<p> For example, suppose you type <code>^Xc</code> to generate a list of corrections, and menu completion is started in one of the usual ways. Usually, or with this style set to `false&#8217;, typing <code>TAB</code> at this point would start trying to complete the line as it now appears. With <code>_oldlist</code>, it instead continues to cycle through the list of corrections.</dl>
<dt><code>original</code></p>
<dd> This is used by the <code>_approximate</code> and <code>_correct</code> completers to decide if the original string should be added as a possible completion. Normally, this is done only if there are at least two possible corrections, but if this style is set to `true&#8217;, it is always added. Note that the style will be examined with the completer field in the context name set to <code>correct-</code><i>num</i> or <code>approximate-</code><i>num</i>, where <i>num</i> is the number of errors that were accepted.</p>
<dt><code>packageset</code></p>
<dd> This style is used when completing arguments of the Debian `<code>dpkg</code>&#8216; program. It contains an override for the default package set for a given context. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:complete:dpkg:option--status-1:*' \ 
               packageset avail</code>
</pre>
</dl>
<p> causes available packages, rather than only installed packages, to be completed for `<code>dpkg &#8211;</code><code>-status</code>&#8216;.</dl>
<dt><code>path</code></p>
<dd> The function that completes color names uses this style with the <code>colors</code> tag. The value should be the pathname of a file containing color names in the format of an X11 <code>rgb.txt</code> file. If the style is not set but this file is found in one of various standard locations it will be used as the default.</p>
<dt><code>path-completion</code></p>
<dd> This is used by filename completion. By default, filename completion examines all components of a path to see if there are completions of that component. For example, <code>/u/b/z</code> can be completed to <code>/usr/bin/zsh</code>. Explicitly setting this style to `false&#8217; inhibits this behaviour for path components up to the <code>/</code> before the cursor; this overrides the setting of <code>accept-exact-dirs</code>.</p>
<dl>
<dt>
<dd>
<p> Even with the style set to `false&#8217;, it is still possible to complete multiple paths by setting the option <code>COMPLETE_IN_WORD</code> and moving the cursor back to the first component in the path to be completed. For example, <code>/u/b/z</code> can be completed to <code>/usr/bin/zsh</code> if the cursor is after the <code>/u</code>.</dl>
<dt><code>pine-directory</code></p>
<dd> If set, specifies the directory containing PINE mailbox files. There is no default, since recursively searching this directory is inconvenient for anyone who doesn&#8217;t use PINE.</p>
<dt><code>ports</code></p>
<dd> A list of Internet service names (network ports) to complete. If this is not set, service names are taken from the file `<code>/etc/services</code>&#8216;.</p>
<dt><code>prefix-hidden</code></p>
<dd> This is used for certain completions which share a common prefix, for example command options beginning with dashes. If it is `true&#8217;, the prefix will not be shown in the list of matches.</p>
<dl>
<dt>
<dd>
<p> The default value for this style is `false&#8217;.</dl>
<dt><code>prefix-needed</code></p>
<dd> This style is also relevant for matches with a common prefix. If it is set to `true&#8217; this common prefix must be typed by the user to generate the matches.</p>
<dl>
<dt>
<dd>
<p> The style is applicable to the <code>options</code>, <code>signals</code>, <code>jobs</code>, <code>functions</code>, and <code>parameters</code> completion tags. </p>
<p> For command options, this means that the initial `<code>&#8211;</code>&#8216;, `<code>+</code>&#8216;, or `<code>&#8211;</code><code>&#8211;</code>&#8216; must be typed explicitly before option names will be completed. </p>
<p> For signals, an initial `<code>&#8211;</code>&#8216; is required before signal names will be completed. </p>
<p> For jobs, an initial `<code>%</code>&#8216; is required before job names will be completed. </p>
<p> For function and parameter names, an initial `<code>_</code>&#8216; or `<code>.</code>&#8216; is required before function or parameter names starting with those characters will be completed. </p>
<p> The default value for this style is `false&#8217; for <code>function</code> and <code>parameter</code> completions, and `true&#8217; otherwise.</dl>
<dt><code>preserve-prefix</code></p>
<dd> This style is used when completing path names. Its value should be a pattern matching an initial prefix of the word to complete that should be left unchanged under all circumstances. For example, on some Unices an initial `<code>//</code>&#8216; (double slash) has a special meaning; setting this style to the string `<code>//</code>&#8216; will preserve it. As another example, setting this style to `<code>?:/</code>&#8216; under Cygwin would allow completion after `<code>a:/&#8230;</code>&#8216; and so on.</p>
<dt><code>range</code></p>
<dd> This is used by the <code>_history</code> completer and the <code>_history_complete_word</code> bindable command to decide which words should be completed.</p>
<dl>
<dt>
<dd>
<p> If it is a single number, only the last <i>N</i> words from the history will be completed. </p>
<p> If it is a range of the form `<i>max</i><code>:</code><i>slice</i>&#8216;, the last <i>slice</i> words will be completed; then if that yields no matches, the <i>slice</i> words before those will be tried and so on. This process stops either when at least one match has been found, or <i>max</i> words have been tried. </p>
<p> The default is to complete all words from the history at once.</dl>
<dt><code>recursive-files</code></p>
<dd> If this style is set, its value is an array of patterns to be tested against `<code>$PWD/</code>&#8216;: note the trailing slash, which allows directories in the pattern to be delimited unambiguously by including slashes on both sides. If an ordinary file completion fails and the word on the command line does not yet have a directory part to its name, the style is retrieved using the same tag as for the completion just attempted, then the elements tested against <code>$PWD/</code> in turn. If one matches, then the shell reattempts completion by prepending the word on the command line with each directory in the expansion of <code>**/*(/)</code> in turn. Typically the elements of the style will be set to restrict the number of directories beneath the current one to a manageable number, for example `<code>*/.git/*</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' recursive-files '*/zsh/*'</code>
</pre>
</dl>
<p> If the current directory is <code>/home/pws/zsh/Src</code>, then <code>zle_tr</code><i>TAB</i> can be completed to <code>Zle/zle_tricky.c</code>.</dl>
<dt><code>regular</code></p>
<dd> This style is used by the <code>_expand_alias</code> completer and bindable command. If set to `true&#8217; (the default), regular aliases will be expanded but only in command position. If it is set to `false&#8217;, regular aliases will never be expanded. If it is set to `<code>always</code>&#8216;, regular aliases will be expanded even if not in command position.</p>
<dt><code>rehash</code></p>
<dd> If this is set when completing external commands, the internal list (hash) of commands will be updated for each search by issuing the <code>rehash</code> command. There is a speed penalty for this which is only likely to be noticeable when directories in the path have slow file access.</p>
<dt><code>remote-access</code></p>
<dd> If set to `false&#8217;, certain commands will be prevented from making Internet connections to retrieve remote information. This includes the completion for the <code>CVS</code> command.</p>
<dl>
<dt>
<dd>
<p> It is not always possible to know if connections are in fact to a remote site, so some may be prevented unnecessarily.</dl>
<dt><code>remove-all-dups</code></p>
<dd> The <code>_history_complete_word</code> bindable command and the <code>_history</code> completer use this to decide if all duplicate matches should be removed, rather than just consecutive duplicates.</p>
<dt><code>select-prompt</code></p>
<dd> If this is set for the <code>default</code> tag, its value will be displayed during menu selection (see the <code>menu</code> style above) when the completion list does not fit on the screen as a whole. The same escapes as for the <code>list-prompt</code> style are understood, except that the numbers refer to the match or line the mark is on. A default prompt is used when the value is the empty string.</p>
<dt><code>select-scroll</code></p>
<dd> This style is tested for the <code>default</code> tag and determines how a completion list is scrolled during a menu selection (see the <code>menu</code> style above) when the completion list does not fit on the screen as a whole. If the value is `<code>0</code>&#8216; (zero), the list is scrolled by half-screenfuls; if it is a positive integer, the list is scrolled by the given number of lines; if it is a negative number, the list is scrolled by a screenful minus the absolute value of the given number of lines. The default is to scroll by single lines.</p>
<dt><code>separate-sections</code></p>
<dd> This style is used with the <code>manuals</code> tag when completing names of manual pages. If it is `true&#8217;, entries for different sections are added separately using tag names of the form `<code>manual.</code><i>X</i>&#8216;, where <i>X</i> is the section number. When the <code>group-name</code> style is also in effect, pages from different sections will appear separately. This style is also used similarly with the <code>words</code> style when completing words for the dict command. It allows words from different dictionary databases to be added separately. The default for this style is `false&#8217;.</p>
<dt><code>show-ambiguity</code></p>
<dd> If the <code>zsh/complist</code> module is loaded, this style can be used to highlight the first ambiguous character in completion lists. The value is either a color indication such as those supported by the <code>list-colors</code> style or, with a value of `true&#8217;, a default of underlining is selected. The highlighting is only applied if the completion display strings correspond to the actual matches.</p>
<dt><code>show-completer</code></p>
<dd> Tested whenever a new completer is tried. If it is `true&#8217;, the completion system outputs a progress message in the listing area showing what completer is being tried. The message will be overwritten by any output when completions are found and is removed after completion is finished.</p>
<dt><code>single-ignored</code></p>
<dd> This is used by the <code>_ignored</code> completer when there is only one match. If its value is `<code>show</code>&#8216;, the single match will be displayed but not inserted. If the value is `<code>menu</code>&#8216;, then the single match and the original string are both added as matches and menu completion is started, making it easy to select either of them.</p>
<dt><code>sort</code></p>
<dd> This allows the standard ordering of matches to be overridden.</p>
<dl>
<dt>
<dd>
<p> If its value is `<code>true</code>&#8216; or `<code>false</code>&#8216;, sorting is enabled or disabled. Additionally the values associated with the `<code>-o</code>&#8216; option to <code>compadd</code> can also be listed: <code>match</code>, <code>nosort</code>, <code>numeric</code>, <code>reverse</code>. If it is not set for the context, the standard behaviour of the calling widget is used. </p>
<p> The style is tested first against the full context including the tag, and if that fails to produce a value against the context without the tag. </p>
<p> In many cases where a calling widget explicitly selects a particular ordering in lieu of the default, a value of `<code>true</code>&#8216; is not honoured. An example of where this is not the case is for command history where the default of sorting matches chronologically may be overridden by setting the style to `true&#8217;. </p>
<p> In the <code>_expand</code> completer, if it is set to `true&#8217;, the expansions generated will always be sorted. If it is set to `<code>menu</code>&#8216;, then the expansions are only sorted when they are offered as single strings but not in the string containing all possible expansions.</dl>
<dt><code>special-dirs</code></p>
<dd> Normally, the completion code will not produce the directory names `<code>.</code>&#8216; and `<code>..</code>&#8216; as possible completions. If this style is set to `true&#8217;, it will add both `<code>.</code>&#8216; and `<code>..</code>&#8216; as possible completions; if it is set to `<code>..</code>&#8216;, only `<code>..</code>&#8216; will be added.</p>
<dl>
<dt>
<dd>
<p> The following example sets <code>special-dirs</code> to `<code>..</code>&#8216; when the current prefix is empty, is a single `<code>.</code>&#8216;, or consists only of a path beginning with `<code>../</code>&#8216;. Otherwise the value is `false&#8217;. </p>
<dl>
<dt>
<dd>
zstyle &#8211; e &#8216;:completion:*&#8217; special &#8211; dirs \<br />
   &#8216;[[ $PREFIX = (../)#(|.|..) ]] &amp;&amp; reply=(..)&#8217;
</dl>
</dl>
<dt><code>squeeze-slashes</code></p>
<dd> If set to `true&#8217;, sequences of slashes in filename paths (for example in `<code>foo//bar</code>&#8216;) will be treated as a single slash. This is the usual behaviour of UNIX paths. However, by default the file completion function behaves as if there were a `<code>*</code>&#8216; between the slashes.</p>
<dt><code>stop</code></p>
<dd> If set to `true&#8217;, the <code>_history_complete_word</code> bindable command will stop once when reaching the beginning or end of the history. Invoking <code>_history_complete_word</code> will then wrap around to the opposite end of the history. If this style is set to `false&#8217; (the default), <code>_history_complete_word</code> will loop immediately as in a menu completion.</p>
<dt><code>strip-comments</code></p>
<dd> If set to `true&#8217;, this style causes non-essential comment text to be removed from completion matches. Currently it is only used when completing e-mail addresses where it removes any display name from the addresses, cutting them down to plain <i>user [at] host</i> form.</p>
<dt><code>subst-globs-only</code></p>
<dd> This is used by the <code>_expand</code> completer. If it is set to `true&#8217;, the expansion will only be used if it resulted from globbing; hence, if expansions resulted from the use of the <code>substitute</code> style described below, but these were not further changed by globbing, the expansions will be rejected.</p>
<dl>
<dt>
<dd>
<p> The default for this style is `false&#8217;.</dl>
<dt><code>substitute</code></p>
<dd> This boolean style controls whether the <code>_expand</code> completer will first try to expand all substitutions in the string (such as `<code>$(</code><i>&#8230;</i><code>)</code>&#8216; and `<code>${</code><i>&#8230;</i><code>}</code>&#8216;).</p>
<dl>
<dt>
<dd>
<p> The default is `true&#8217;.</dl>
<dt><code>suffix</code></p>
<dd> This is used by the <code>_expand</code> completer if the word starts with a tilde or contains a parameter expansion. If it is set to `true&#8217;, the word will only be expanded if it doesn&#8217;t have a suffix, i.e. if it is something like `<code>~foo</code>&#8216; or `<code>$foo</code>&#8216; rather than `<code>~foo/</code>&#8216; or `<code>$foo/bar</code>&#8216;, unless that suffix itself contains characters eligible for expansion. The default for this style is `true&#8217;.</p>
<dt><code>tag-order</code></p>
<dd> This provides a mechanism for sorting how the tags available in a particular context will be used.</p>
<dl>
<dt>
<dd>
<p> The values for the style are sets of space-separated lists of tags. The tags in each value will be tried at the same time; if no match is found, the next value is used. (See the <code>file-patterns</code> style for an exception to this behavior.) </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:complete:-command-:*:*' tag-order \ 
    'commands functions'</code>
</pre>
</dl>
<p> specifies that completion in command position first offers external commands and shell functions. Remaining tags will be tried if no completions are found. </p>
<p> In addition to tag names, each string in the value may take one of the following forms: </p>
<dl>
<dt>
<dd> <code>&#8211;</code> If any value consists of only a hyphen, then <i>only</i> the tags specified in the other values are generated. Normally all tags not explicitly selected are tried last if the specified tags fail to generate any matches. This means that a single value consisting only of a single hyphen turns off completion.</p>
<dt><code>!</code> <i>tags</i>&#8230;</p>
<dd> A string starting with an exclamation mark specifies names of tags that are <i>not</i> to be used. The effect is the same as if all other possible tags for the context had been listed.</p>
<dt><i>tag</i><code>:</code><i>label</i> &#8230;</p>
<dd> Here, <i>tag</i> is one of the standard tags and <i>label</i> is an arbitrary name. Matches are generated as normal but the name <i>label</i> is used in contexts instead of <i>tag</i>. This is not useful in words starting with <code>!</code>.</p>
<dl>
<dt>
<dd>
<p> If the <i>label</i> starts with a hyphen, the <i>tag</i> is prepended to the <i>label</i> to form the name used for lookup. This can be used to make the completion system try a certain tag more than once, supplying different style settings for each attempt; see below for an example.</dl>
<dt><i>tag</i><code>:</code><i>label</i><code>:</code><i>description</i></p>
<dd> As before, but <code>description</code> will replace the `<code>%d</code>&#8216; in the value of the <code>format</code> style instead of the default description supplied by the completion function. Spaces in the description must be quoted with a backslash. A `<code>%d</code>&#8216; appearing in <i>description</i> is replaced with the description given by the completion function.</dl>
<p> In any of the forms above the tag may be a pattern or several patterns in the form `<code>{</code><i>pat1</i><code>,</code><i>pat2&#8230;</i><code>}</code>&#8216;. In this case all matching tags will be used except for any given explicitly in the same string. </p>
<p> One use of these features is to try one tag more than once, setting other styles differently on each attempt, but still to use all the other tags without having to repeat them all. For example, to make completion of function names in command position ignore all the completion functions starting with an underscore the first time completion is tried: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:-command-:*:*' tag-order \ 
    'functions:-non-comp *' functions
zstyle ':completion:*:functions-non-comp' \ 
    ignored-patterns '_*'</code>
</pre>
</dl>
<p> On the first attempt, all tags will be offered but the <code>functions</code> tag will be replaced by <code>functions-non-comp</code>. The <code>ignored-patterns</code> style is set for this tag to exclude functions starting with an underscore. If there are no matches, the second value of the <code>tag-order</code> style is used which completes functions using the default tag, this time presumably including all function names. </p>
<p> The matches for one tag can be split into different groups. For example: </p>
<dl>
<dt>
<dd>
zstyle &#8216;:completion:*&#8217; tag &#8211; order \<br />
    &#8216;options:-long:long\ options options : -short : short\ options options : -single &#8211;<br />
                                                                             letter : single\ letter\ options&#8217; zstyle &#8216;:completion:*:options-long&#8217; \<br />
     ignored &#8211; patterns &#8216;[-+](|-|[^-]*)&#8217; zstyle &#8216;:completion:*:options-short&#8217; \<br />
     ignored &#8211; patterns &#8216;&#8211;*&#8217; &#8216;[-+]?&#8217; zstyle &#8216;:completion:*:options-single-letter&#8217; \<br />
     ignored &#8211; patterns &#8216;???*&#8217;
</dl>
<p> With the <code>group-names</code> style set, options beginning with `<code>&#8211;</code><code>&#8211;</code>&#8216;, options beginning with a single `<code>&#8211;</code>&#8216; or `<code>+</code>&#8216; but containing multiple characters, and single-letter options will be displayed in separate groups with different descriptions. </p>
<p> Another use of patterns is to try multiple match specifications one after another. The <code>matcher-list</code> style offers something similar, but it is tested very early in the completion system and hence can&#8217;t be set for single commands nor for more specific contexts. Here is how to try normal completion without any match specification and, if that generates no matches, try again with case-insensitive matching, restricting the effect to arguments of the command <code>foo</code>: </p>
<dl>
<dt>
<dd>
zstyle &#8216;:completion:*:*:foo:*:*&#8217; tag &#8211; order &#8216;*&#8217; &#8216;*:-case&#8217; zstyle &#8216;:completion:*-case&#8217; matcher &#8216;m:{a-z}={A-Z}&#8217;
</dl>
<p> First, all the tags offered when completing after <code>foo</code> are tried using the normal tag name. If that generates no matches, the second value of <code>tag-order</code> is used, which tries all tags again except that this time each has <code>-case</code> appended to its name for lookup of styles. Hence this time the value for the <code>matcher</code> style from the second call to <code>zstyle</code> in the example is used to make completion case-insensitive. </p>
<p> It is possible to use the <code>-e</code> option of the <code>zstyle</code> builtin command to specify conditions for the use of particular tags. For example: </p>
<dl>
<dt>
<dd>
zstyle &#8211; e &#8216;*:-command-:*&#8217; tag &#8211; order &#8216; if[[-n $PREFIX$SUFFIX]];<br />
then<br />
    reply = () else reply = (-)<br />
        fi&#8217;
</dl>
<p> Completion in command position will be attempted only if the string typed so far is not empty. This is tested using the <code>PREFIX</code> special parameter; see zshcompwid for a description of parameters which are special inside completion widgets. Setting <code>reply</code> to an empty array provides the default behaviour of trying all tags at once; setting it to an array containing only a hyphen disables the use of all tags and hence of all completions. </p>
<p> If no <code>tag-order</code> style has been defined for a context, the strings `<code>(|*-)argument-* (|*-)option-* values</code>&#8216; and `<code>options</code>&#8216; plus all tags offered by the completion function will be used to provide a sensible default behavior that causes arguments (whether normal command arguments or arguments of options) to be completed before option names for most commands.</dl>
<dt><code>urls</code></p>
<dd> This is used together with the <code>urls</code> tag by functions completing URLs.</p>
<dl>
<dt>
<dd>
<p> If the value consists of more than one string, or if the only string does not name a file or directory, the strings are used as the URLs to complete. </p>
<p> If the value contains only one string which is the name of a normal file the URLs are taken from that file (where the URLs may be separated by white space or newlines). </p>
<p> Finally, if the only string in the value names a directory, the directory hierarchy rooted at this directory gives the completions. The top level directory should be the file access method, such as `<code>http</code>&#8216;, `<code>ftp</code>&#8216;, `<code>bookmark</code>&#8216; and so on. In many cases the next level of directories will be a filename. The directory hierarchy can descend as deep as necessary. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' urls ~/.urls
mkdir -p ~/.urls/ftp/<a href="ftp://ftp.zsh.org">ftp.zsh.org</a>/pub</code>
</pre>
</dl>
<p> allows completion of all the components of the URL <code><a href="ftp://ftp.zsh.org/pub">ftp://ftp.zsh.org/pub</a></code> after suitable commands such as `<code>netscape</code>&#8216; or `<code>lynx</code>&#8216;. Note, however, that access methods and files are completed separately, so if the <code>hosts</code> style is set hosts can be completed without reference to the <code>urls</code> style. </p>
<p> See the description in the function <code>_urls</code> itself for more information (e.g. `<code>more $^fpath/_urls(N)</code>&#8216;).</dl>
<dt><code>use-cache</code></p>
<dd> If this is set, the completion caching layer is activated for any completions which use it (via the <code>_store_cache</code>, <code>_retrieve_cache</code>, and <code>_cache_invalid</code> functions). The directory containing the cache files can be changed with the <code>cache-path</code> style.</p>
<dt><code>use-compctl</code></p>
<dd> If this style is set to a string <i>not</i> equal to <code>false</code>, <code>0</code>, <code>no</code>, and <code>off</code>, the completion system may use any completion specifications defined with the <code>compctl</code> builtin command. If the style is unset, this is done only if the <code>zsh/compctl</code> module is loaded. The string may also contain the substring `<code>first</code>&#8216; to use completions defined with `<code>compctl -T</code>&#8216;, and the substring `<code>default</code>&#8216; to use the completion defined with `<code>compctl -D</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> Note that this is only intended to smooth the transition from <code>compctl</code> to the new completion system and may disappear in the future. </p>
<p> Note also that the definitions from <code>compctl</code> will only be used if there is no specific completion function for the command in question. For example, if there is a function <code>_foo</code> to complete arguments to the command <code>foo</code>, <code>compctl</code> will never be invoked for <code>foo</code>. However, the <code>compctl</code> version will be tried if <code>foo</code> only uses default completion.</dl>
<dt><code>use-ip</code></p>
<dd> By default, the function <code>_hosts</code> that completes host names strips IP addresses from entries read from host databases such as NIS and ssh files. If this style is `true&#8217;, the corresponding IP addresses can be completed as well. This style is not use in any context where the <code>hosts</code> style is set; note also it must be set before the cache of host names is generated (typically the first completion attempt).</p>
<dt><code>users</code></p>
<dd> This may be set to a list of usernames to be completed. If it is not set all usernames will be completed. Note that if it is set only that list of users will be completed; this is because on some systems querying all users can take a prohibitive amount of time.</p>
<dt><code>users-hosts</code></p>
<dd> The values of this style should be of the form `<i>user</i><code>@</code><i>host</i>&#8216; or `<i>user</i><code>:</code><i>host</i>&#8216;. It is used for commands that need pairs of user- and hostnames. These commands will complete usernames from this style (only), and will restrict subsequent hostname completion to hosts paired with that user in one of the values of the style.</p>
<dl>
<dt>
<dd>
<p> It is possible to group values for sets of commands which allow a remote login, such as <code>rlogin</code> and <code>ssh</code>, by using the <code>my-accounts</code> tag. Similarly, values for sets of commands which usually refer to the accounts of other people, such as <code>talk</code> and <code>finger</code>, can be grouped by using the <code>other-accounts</code> tag. More ambivalent commands may use the <code>accounts</code> tag.</dl>
<dt><code>users-hosts-ports</code></p>
<dd> Like <code>users-hosts</code> but used for commands like <code>telnet</code> and containing strings of the form `<i>user</i><code>@</code><i>host</i><code>:</code><i>port</i>&#8216;.</p>
<dt><code>verbose</code></p>
<dd> If set, as it is by default, the completion listing is more verbose. In particular many commands show descriptions for options if this style is `true&#8217;.</p>
<dt><code>word</code></p>
<dd> This is used by the <code>_list</code> completer, which prevents the insertion of completions until a second completion attempt when the line has not changed. The normal way of finding out if the line has changed is to compare its entire contents between the two occasions. If this style is `true&#8217;, the comparison is instead performed only on the current word. Hence if completion is performed on another word with the same contents, completion will not be delayed.</dl>
<h2>CONTROL FUNCTIONS</h2>
<p> The initialization script <code>compinit</code> redefines all the widgets which perform completion to call the supplied widget function <code>_main_complete</code>. This function acts as a wrapper calling the so-called `completer&#8217; functions that generate matches. If <code>_main_complete</code> is called with arguments, these are taken as the names of completer functions to be called in the order given. If no arguments are given, the set of functions to try is taken from the <code>completer</code> style. For example, to use normal completion and correction if that doesn&#8217;t generate any matches: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' completer _complete _correct</code>
</pre>
</dl>
<p> after calling <code>compinit</code>. The default value for this style is `<code>_complete _ignored</code>&#8216;, i.e. normally only ordinary completion is tried, first with the effect of the <code>ignored-patterns</code> style and then without it. The <code>_main_complete</code> function uses the return status of the completer functions to decide if other completers should be called. If the return status is zero, no other completers are tried and the <code>_main_complete</code> function returns. </p>
<p> If the first argument to <code>_main_complete</code> is a single hyphen, the arguments will not be taken as names of completers. Instead, the second argument gives a name to use in the <i>completer</i> field of the context and the other arguments give a command name and arguments to call to generate the matches. </p>
<p> The following completer functions are contained in the distribution, although users may write their own. Note that in contexts the leading underscore is stripped, for example basic completion is performed in the context `<code>:completion::complete:</code><i>&#8230;</i>&#8216;. </p>
<dl>
<dt>
<dd> <code>_all_matches</code> This completer can be used to add a string consisting of all other matches. As it influences later completers it must appear as the first completer in the list. The list of all matches is affected by the <code>avoid-completer</code> and <code>old-matches</code> styles described above.</p>
<dl>
<dt>
<dd>
<p> It may be useful to use the <code>_generic</code> function described below to bind <code>_all_matches</code> to its own keystroke, for example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -C all-matches complete-word _generic
bindkey '^Xa' all-matches
zstyle ':completion:all-matches:*' old-matches only
zstyle ':completion:all-matches::::' completer _all_matches</code>
</pre>
</dl>
<p> Note that this does not generate completions by itself: first use any of the standard ways of generating a list of completions, then use <code>^Xa</code> to show all matches. It is possible instead to add a standard completer to the list and request that the list of all matches should be directly inserted: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:all-matches::::' completer \ 
       _all_matches _complete
zstyle ':completion:all-matches:*' insert true</code>
</pre>
</dl>
<p> In this case the <code>old-matches</code> style should not be set.</dl>
<dt><code>_approximate</code></p>
<dd> This is similar to the basic <code>_complete</code> completer but allows the completions to undergo corrections. The maximum number of errors can be specified by the <code>max-errors</code> style; see the description of approximate matching in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1) for how errors are counted. Normally this completer will only be tried after the normal <code>_complete</code> completer:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' completer _complete _approximate</code>
</pre>
</dl>
<p> This will give correcting completion if and only if normal completion yields no possible completions. When corrected completions are found, the completer will normally start menu completion allowing you to cycle through these strings. </p>
<p> This completer uses the tags <code>corrections</code> and <code>original</code> when generating the possible corrections and the original string. The <code>format</code> style for the former may contain the additional sequences `<code>%e</code>&#8216; and `<code>%o</code>&#8216; which will be replaced by the number of errors accepted to generate the corrections and the original string, respectively. </p>
<p> The completer progressively increases the number of errors allowed up to the limit by the <code>max-errors</code> style, hence if a completion is found with one error, no completions with two errors will be shown, and so on. It modifies the completer name in the context to indicate the number of errors being tried: on the first try the completer field contains `<code>approximate-1</code>&#8216;, on the second try `<code>approximate-2</code>&#8216;, and so on. </p>
<p> When <code>_approximate</code> is called from another function, the number of errors to accept may be passed with the <code>-a</code> option. The argument is in the same format as the <code>max-errors</code> style, all in one string. </p>
<p> Note that this completer (and the <code>_correct</code> completer mentioned below) can be quite expensive to call, especially when a large number of errors are allowed. One way to avoid this is to set up the <code>completer</code> style using the <code>-e</code> option to zstyle so that some completers are only used when completion is attempted a second time on the same string, e.g.: </p>
<dl>
<dt>
<dd>
zstyle &#8211; e &#8216;:completion:*&#8217; completer &#8216; if [[$_last_try != &#8220;$HISTNO$BUFFER$CURSOR&#8221;]];<br />
then<br />
    _last_try = &#8220;$HISTNO$BUFFER$CURSOR&#8221; reply = (_complete _match _prefix) else reply = (_ignored _correct _approximate)<br />
        fi&#8217;
</dl>
<p> This uses the <code>HISTNO</code> parameter and the <code>BUFFER</code> and <code>CURSOR</code> special parameters that are available inside zle and completion widgets to find out if the command line hasn&#8217;t changed since the last time completion was tried. Only then are the <code>_ignored</code>, <code>_correct</code> and <code>_approximate</code> completers called.</dl>
<dt><code>_canonical_paths</code> [ <code>-A</code> <i>var</i> ] [ <code>-N</code> ] [ <code>-MJV12nfX</code> ] <i>tag</i> <i>descr</i> [ <i>paths</i> &#8230; ]</p>
<dd> This completion function completes all paths given to it, and also tries to offer completions which point to the same file as one of the paths given (relative path when an absolute path is given, and vice versa; when <code>..</code>&#8216;s are present in the word to be completed; and some paths got from symlinks).</p>
<dl>
<dt>
<dd>
<p> <code>-A</code>, if specified, takes the paths from the array variable specified. Paths can also be specified on the command line as shown above. <code>-N</code>, if specified, prevents canonicalizing the paths given before using them for completion, in case they are already so. The options <code>-M</code>, <code>-J</code>, <code>-V</code>, <code>-1</code>, <code>-2</code>, <code>-n</code>, <code>-F</code>, <code>-X</code> are passed to <code>compadd</code>. </p>
<p> See <code>_description</code> for a description of <i>tag</i> and <i>descr</i>.</dl>
<dt><code>_cmdambivalent</code></p>
<dd> Completes the remaining positional arguments as an external command. The external command and its arguments are completed as separate arguments (in a manner appropriate for completing <code>/usr/bin/env</code>) if there are two or more remaining positional arguments on the command line, and as a quoted command string (in the manner of <code>system(&#8230;)</code>) otherwise. See also <code>_cmdstring</code> and <code>_precommand</code>.</p>
<dl>
<dt>
<dd>
<p> This function takes no arguments.</dl>
<dt><code>_cmdstring</code></p>
<dd> Completes an external command as a single argument, as for <code>system(&#8230;)</code>.</p>
<dt><code>_complete</code></p>
<dd> This completer generates all possible completions in a context-sensitive manner, i.e. using the settings defined with the <code>compdef</code> function explained above and the current settings of all special parameters. This gives the normal completion behaviour.</p>
<dl>
<dt>
<dd>
<p> To complete arguments of commands, <code>_complete</code> uses the utility function <code>_normal</code>, which is in turn responsible for finding the particular function; it is described below. Various contexts of the form <code>&#8211;</code><i>context</i><code>&#8211;</code> are handled specifically. These are all mentioned above as possible arguments to the <code>#compdef</code> tag. </p>
<p> Before trying to find a function for a specific context, <code>_complete</code> checks if the parameter `<code>compcontext</code>&#8216; is set. Setting `<code>compcontext</code>&#8216; allows the usual completion dispatching to be overridden which is useful in places such as a function that uses <code>vared</code> for input. If it is set to an array, the elements are taken to be the possible matches which will be completed using the tag `<code>values</code>&#8216; and the description `<code>value</code>&#8216;. If it is set to an associative array, the keys are used as the possible completions and the values (if non-empty) are used as descriptions for the matches. If `<code>compcontext</code>&#8216; is set to a string containing colons, it should be of the form `<i>tag</i><code>:</code><i>descr</i><code>:</code><i>action</i>&#8216;. In this case the <i>tag</i> and <i>descr</i> give the tag and description to use and the <i>action</i> indicates what should be completed in one of the forms accepted by the <code>_arguments</code> utility function described below. </p>
<p> Finally, if `<code>compcontext</code>&#8216; is set to a string without colons, the value is taken as the name of the context to use and the function defined for that context will be called. For this purpose, there is a special context named <code>-command-line-</code> that completes whole command lines (commands and their arguments). This is not used by the completion system itself but is nonetheless handled when explicitly called.</dl>
<dt><code>_correct</code></p>
<dd> Generate corrections, but not completions, for the current word; this is similar to <code>_approximate</code> but will not allow any number of extra characters at the cursor as that completer does. The effect is similar to spell-checking. It is based on <code>_approximate</code>, but the completer field in the context name is <code>correct</code>.</p>
<dl>
<dt>
<dd>
<p> For example, with: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:::::' completer \ 
       _complete _correct _approximate
zstyle ':completion:*:correct:::' max-errors 2 not-numeric
zstyle ':completion:*:approximate:::' max-errors 3 numeric</code>
</pre>
</dl>
<p> correction will accept up to two errors. If a numeric argument is given, correction will not be performed, but correcting completion will be, and will accept as many errors as given by the numeric argument. Without a numeric argument, first correction and then correcting completion will be tried, with the first one accepting two errors and the second one accepting three errors. </p>
<p> When <code>_correct</code> is called as a function, the number of errors to accept may be given following the <code>-a</code> option. The argument is in the same form a values to the <code>accept</code> style, all in one string. </p>
<p> This completer function is intended to be used without the <code>_approximate</code> completer or, as in the example, just before it. Using it after the <code>_approximate</code> completer is useless since <code>_approximate</code> will at least generate the corrected strings generated by the <code>_correct</code> completer &#8212; and probably more.</dl>
<dt><code>_expand</code></p>
<dd> This completer function does not really perform completion, but instead checks if the word on the command line is eligible for expansion and, if it is, gives detailed control over how this expansion is done. For this to happen, the completion system needs to be invoked with <code>complete-word</code>, not <code>expand-or-complete</code> (the default binding for <code>TAB</code>), as otherwise the string will be expanded by the shell&#8217;s internal mechanism before the completion system is started. Note also this completer should be called before the <code>_complete</code> completer function.</p>
<dl>
<dt>
<dd>
<p> The tags used when generating expansions are <code>all-expansions</code> for the string containing all possible expansions, <code>expansions</code> when adding the possible expansions as single matches and <code>original</code> when adding the original string from the line. The order in which these strings are generated, if at all, can be controlled by the <code>group-order</code> and <code>tag-order</code> styles, as usual. </p>
<p> The format string for <code>all-expansions</code> and for <code>expansions</code> may contain the sequence `<code>%o</code>&#8216; which will be replaced by the original string from the line. </p>
<p> The kind of expansion to be tried is controlled by the <code>substitute</code>, <code>glob</code> and <code>subst-globs-only</code> styles. </p>
<p> It is also possible to call <code>_expand</code> as a function, in which case the different modes may be selected with options: <code>-s</code> for <code>substitute</code>, <code>-g</code> for <code>glob</code> and <code>-o</code> for <code>subst-globs-only</code>.</dl>
<dt><code>_expand_alias</code></p>
<dd> If the word the cursor is on is an alias, it is expanded and no other completers are called. The types of aliases which are to be expanded can be controlled with the styles <code>regular</code>, <code>global</code> and <code>disabled</code>.</p>
<dl>
<dt>
<dd>
<p> This function is also a bindable command, see the section `Bindable Commands&#8217; below.</dl>
<dt><code>_extensions</code></p>
<dd> If the cursor follows the string `<code>*.</code>&#8216;, filename extensions are completed. The extensions are taken from files in current directory or a directory specified at the beginning of the current word. For exact matches, completion continues to allow other completers such as <code>_expand</code> to expand the pattern. The standard <code>add-space</code> and <code>prefix-hidden</code> styles are observed.</p>
<dt><code>_external_pwds</code></p>
<dd> Completes current directories of other zsh processes belonging to the current user.</p>
<dl>
<dt>
<dd>
<p> This is intended to be used via <code>_generic</code>, bound to a custom key combination. Note that pattern matching is enabled so matching is performed similar to how it works with the <code>_match</code> completer.</dl>
<dt><code>_history</code></p>
<dd> Complete words from the shell&#8217;s command history. This completer can be controlled by the <code>remove-all-dups</code>, and <code>sort</code> styles as for the <code>_history_complete_word</code> bindable command, see the section `Bindable Commands&#8217; below and the section `Completion System Configuration&#8217; above.</p>
<dt><code>_ignored</code></p>
<dd> The <code>ignored-patterns</code> style can be set to a list of patterns which are compared against possible completions; matching ones are removed. With this completer those matches can be reinstated, as if no <code>ignored-patterns</code> style were set. The completer actually generates its own list of matches; which completers are invoked is determined in the same way as for the <code>_prefix</code> completer. The <code>single-ignored</code> style is also available as described above.</p>
<dt><code>_list</code></p>
<dd> This completer allows the insertion of matches to be delayed until completion is attempted a second time without the word on the line being changed. On the first attempt, only the list of matches will be shown. It is affected by the styles <code>condition</code> and <code>word</code>, see the section `Completion System Configuration&#8217; above.</p>
<dt><code>_match</code></p>
<dd> This completer is intended to be used after the <code>_complete</code> completer. It behaves similarly but the string on the command line may be a pattern to match against trial completions. This gives the effect of the <code>GLOB_COMPLETE</code> option.</p>
<dl>
<dt>
<dd>
<p> Normally completion will be performed by taking the pattern from the line, inserting a `<code>*</code>&#8216; at the cursor position and comparing the resulting pattern with the possible completions generated. This can be modified with the <code>match-original</code> style described above. </p>
<p> The generated matches will be offered in a menu completion unless the <code>insert-unambiguous</code> style is set to `true&#8217;; see the description above for other options for this style. </p>
<p> Note that matcher specifications defined globally or used by the completion functions (the styles <code>matcher-list</code> and <code>matcher</code>) will not be used.</dl>
<dt><code>_menu</code></p>
<dd> This completer was written as simple example function to show how menu completion can be enabled in shell code. However, it has the notable effect of disabling menu selection which can be useful with <code>_generic</code> based widgets. It should be used as the first completer in the list. Note that this is independent of the setting of the <code>MENU_COMPLETE</code> option and does not work with the other menu completion widgets such as <code>reverse-menu-complete</code>, or <code>accept-and-menu-complete</code>.</p>
<dt><code>_oldlist</code></p>
<dd> This completer controls how the standard completion widgets behave when there is an existing list of completions which may have been generated by a special completion (i.e. a separately-bound completion command). It allows the ordinary completion keys to continue to use the list of completions thus generated, instead of producing a new list of ordinary contextual completions. It should appear in the list of completers before any of the widgets which generate matches. It uses two styles: <code>old-list</code> and <code>old-menu</code>, see the section `Completion System Configuration&#8217; above.</p>
<dt><code>_precommand</code></p>
<dd> Complete an external command in word-separated arguments, as for <code>exec</code> and <code>/usr/bin/env</code>.</p>
<dt><code>_prefix</code></p>
<dd> This completer can be used to try completion with the suffix (everything after the cursor) ignored. In other words, the suffix will not be considered to be part of the word to complete. The effect is similar to the <code>expand-or-complete-prefix</code> command.</p>
<dl>
<dt>
<dd>
<p> The <code>completer</code> style is used to decide which other completers are to be called to generate matches. If this style is unset, the list of completers set for the current context is used &#8212; except, of course, the <code>_prefix</code> completer itself. Furthermore, if this completer appears more than once in the list of completers only those completers not already tried by the last invocation of <code>_prefix</code> will be called. </p>
<p> For example, consider this global <code>completer</code> style: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' completer \ 
    _complete _prefix _correct _prefix:foo</code>
</pre>
</dl>
<p> Here, the <code>_prefix</code> completer tries normal completion but ignoring the suffix. If that doesn&#8217;t generate any matches, and neither does the call to the <code>_correct</code> completer after it, <code>_prefix</code> will be called a second time and, now only trying correction with the suffix ignored. On the second invocation the completer part of the context appears as `<code>foo</code>&#8216;. </p>
<p> To use <code>_prefix</code> as the last resort and try only normal completion when it is invoked: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' completer _complete ... _prefix
zstyle ':completion::prefix:*' completer _complete</code>
</pre>
</dl>
<p> The <code>add-space</code> style is also respected. If it is set to `true&#8217; then <code>_prefix</code> will insert a space between the matches generated (if any) and the suffix. </p>
<p> Note that this completer is only useful if the <code>COMPLETE_IN_WORD</code> option is set; otherwise, the cursor will be moved to the end of the current word before the completion code is called and hence there will be no suffix.</dl>
<dt><code>_user_expand</code></p>
<dd> This completer behaves similarly to the <code>_expand</code> completer but instead performs expansions defined by users. The styles <code>add-space</code> and <code>sort</code> styles specific to the <code>_expand</code> completer are usable with <code>_user_expand</code> in addition to other styles handled more generally by the completion system. The tag <code>all-expansions</code> is also available.</p>
<dl>
<dt>
<dd>
<p> The expansion depends on the array style <code>user-expand</code> being defined for the current context; remember that the context for completers is less specific than that for contextual completion as the full context has not yet been determined. Elements of the array may have one of the following forms: </p>
<dl>
<dt><code>$</code><i>hash</i></p>
<dd>
<p> <i>hash</i> is the name of an associative array. Note this is not a full parameter expression, merely a <code>$</code>, suitably quoted to prevent immediate expansion, followed by the name of an associative array. If the trial expansion word matches a key in <i>hash</i>, the resulting expansion is the corresponding value.</dl>
<dl>
<dt><i>_func</i></p>
<dd>
<p> <i>_func</i> is the name of a shell function whose name must begin with <code>_</code> but is not otherwise special to the completion system. The function is called with the trial word as an argument. If the word is to be expanded, the function should set the array <code>reply</code> to a list of expansions. Optionally, it can set <code>REPLY</code> to a word that will be used as a description for the set of expansions. The return status of the function is irrelevant.</dl>
</dl>
</dl>
<h2>BINDABLE COMMANDS</h2>
<p> In addition to the context-dependent completions provided, which are expected to work in an intuitively obvious way, there are a few widgets implementing special behaviour which can be bound separately to keys. The following is a list of these and their default bindings. </p>
<dl>
<dt>
<dd> <code>_bash_completions</code> This function is used by two widgets, <code>_bash_complete-word</code> and <code>_bash_list-choices</code>. It exists to provide compatibility with completion bindings in bash. The last character of the binding determines what is completed: `<code>!</code>&#8216;, command names; `<code>$</code>&#8216;, environment variables; `<code>@</code>&#8216;, host names; `<code>/</code>&#8216;, file names; `<code>~</code>&#8216; user names. In bash, the binding preceded by `<code></code>&#8216; gives completion, and preceded by `<code>^X</code>&#8216; lists options. As some of these bindings clash with standard zsh bindings, only `<code>~</code>&#8216; and `<code>^X~</code>&#8216; are bound by default. To add the rest, the following should be added to <code>.zshrc</code> after <code>compinit</code> has been run:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>for key in '!' '$' '@' '/' '~'; do
  bindkey &quot;$key&quot; _bash_complete-word
  bindkey &quot;^X$key&quot; _bash_list-choices
done</code>
</pre>
</dl>
<p> This includes the bindings for `<code>~</code>&#8216; in case they were already bound to something else; the completion code does not override user bindings.</dl>
<dt><code>_correct_filename</code> (<code>^XC</code>)</p>
<dd> Correct the filename path at the cursor position. Allows up to six errors in the name. Can also be called with an argument to correct a filename path, independently of zle; the correction is printed on standard output.</p>
<dt><code>_correct_word</code> (<code>^Xc</code>)</p>
<dd> Performs correction of the current argument using the usual contextual completions as possible choices. This stores the string `<code>correct-word</code>&#8216; in the <i>function</i> field of the context name and then calls the <code>_correct</code> completer.</p>
<dt><code>_expand_alias</code> (<code>^Xa</code>)</p>
<dd> This function can be used as a completer and as a bindable command. It expands the word the cursor is on if it is an alias. The types of alias expanded can be controlled with the styles <code>regular</code>, <code>global</code> and <code>disabled</code>.</p>
<dl>
<dt>
<dd>
<p> When used as a bindable command there is one additional feature that can be selected by setting the <code>complete</code> style to `true&#8217;. In this case, if the word is not the name of an alias, <code>_expand_alias</code> tries to complete the word to a full alias name without expanding it. It leaves the cursor directly after the completed word so that invoking <code>_expand_alias</code> once more will expand the now-complete alias name.</dl>
<dt><code>_expand_word</code> (<code>^Xe</code>)</p>
<dd> Performs expansion on the current word: equivalent to the standard <code>expand-word</code> command, but using the <code>_expand</code> completer. Before calling it, the <i>function</i> field of the context is set to `<code>expand-word</code>&#8216;.</p>
<dt><code>_generic</code></p>
<dd> This function is not defined as a widget and not bound by default. However, it can be used to define a widget and will then store the name of the widget in the <i>function</i> field of the context and call the completion system. This allows custom completion widgets with their own set of style settings to be defined easily. For example, to define a widget that performs normal completion and starts menu selection:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zle -C foo complete-word _generic
bindkey '...' foo
zstyle ':completion:foo:*' menu yes select=1</code>
</pre>
</dl>
<p> Note in particular that the <code>completer</code> style may be set for the context in order to change the set of functions used to generate possible matches. If <code>_generic</code> is called with arguments, those are passed through to <code>_main_complete</code> as the list of completers in place of those defined by the <code>completer</code> style.</dl>
<dt><code>_history_complete_word</code> (<code>/</code>)</p>
<dd> Complete words from the shell&#8217;s command history. This uses the <code>list</code>, <code>remove-all-dups</code>, <code>sort</code>, and <code>stop</code> styles.</p>
<dt><code>_most_recent_file</code> (<code>^Xm</code>)</p>
<dd> Complete the name of the most recently modified file matching the pattern on the command line (which may be blank). If given a numeric argument <i>N</i>, complete the <i>N</i>th most recently modified file. Note the completion, if any, is always unique.</p>
<dt><code>_next_tags</code> (<code>^Xn</code>)</p>
<dd> This command alters the set of matches used to that for the next tag, or set of tags, either as given by the <code>tag-order</code> style or as set by default; these matches would otherwise not be available. Successive invocations of the command cycle through all possible sets of tags.</p>
<dt><code>_read_comp</code> (<code>^X^R</code>)</p>
<dd> Prompt the user for a string, and use that to perform completion on the current word. There are two possibilities for the string. First, it can be a set of words beginning `<code>_</code>&#8216;, for example `<code>_files -/</code>&#8216;, in which case the function with any arguments will be called to generate the completions. Unambiguous parts of the function name will be completed automatically (normal completion is not available at this point) until a space is typed.</p>
<dl>
<dt>
<dd>
<p> Second, any other string will be passed as a set of arguments to <code>compadd</code> and should hence be an expression specifying what should be completed. </p>
<p> A very restricted set of editing commands is available when reading the string: `<code>DEL</code>&#8216; and `<code>^H</code>&#8216; delete the last character; `<code>^U</code>&#8216; deletes the line, and `<code>^C</code>&#8216; and `<code>^G</code>&#8216; abort the function, while `<code>RET</code>&#8216; accepts the completion. Note the string is used verbatim as a command line, so arguments must be quoted in accordance with standard shell rules. </p>
<p> Once a string has been read, the next call to <code>_read_comp</code> will use the existing string instead of reading a new one. To force a new string to be read, call <code>_read_comp</code> with a numeric argument.</dl>
<dt><code>_complete_debug</code> (<code>^X?</code>)</p>
<dd> This widget performs ordinary completion, but captures in a temporary file a trace of the shell commands executed by the completion system. Each completion attempt gets its own file. A command to view each of these files is pushed onto the editor buffer stack.</p>
<dt><code>_complete_help</code> (<code>^Xh</code>)</p>
<dd> This widget displays information about the context names, the tags, and the completion functions used when completing at the current cursor position. If given a numeric argument other than <code>1</code> (as in `<code>ESC-2 ^Xh</code>&#8216;), then the styles used and the contexts for which they are used will be shown, too.</p>
<dl>
<dt>
<dd>
<p> Note that the information about styles may be incomplete; it depends on the information available from the completion functions called, which in turn is determined by the user&#8217;s own styles and other settings.</dl>
<dt><code>_complete_help_generic</code></p>
<dd> Unlike other commands listed here, this must be created as a normal ZLE widget rather than a completion widget (i.e. with <code>zle -N</code>). It is used for generating help with a widget bound to the <code>_generic</code> widget that is described above.</p>
<dl>
<dt>
<dd>
<p> If this widget is created using the name of the function, as it is by default, then when executed it will read a key sequence. This is expected to be bound to a call to a completion function that uses the <code>_generic</code> widget. That widget will be executed, and information provided in the same format that the <code>_complete_help</code> widget displays for contextual completion. </p>
<p> If the widget&#8217;s name contains <code>debug</code>, for example if it is created as `<code>zle -N _complete_debug_generic _complete_help_generic</code>&#8216;, it will read and execute the keystring for a generic widget as before, but then generate debugging information as done by <code>_complete_debug</code> for contextual completion. </p>
<p> If the widget&#8217;s name contains <code>noread</code>, it will not read a keystring but instead arrange that the next use of a generic widget run in the same shell will have the effect as described above. </p>
<p> The widget works by setting the shell parameter <code>ZSH_TRACE_GENERIC_WIDGET</code> which is read by <code>_generic</code>. Unsetting the parameter cancels any pending effect of the <code>noread</code> form. </p>
<p> For example, after executing the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -N _complete_debug_generic _complete_help_generic
bindkey '^x:' _complete_debug_generic</code>
</pre>
</dl>
<p> typing `<code>C-x :</code>&#8216; followed by the key sequence for a generic widget will cause trace output for that widget to be saved to a file.</dl>
<dt><code>_complete_tag</code> (<code>^Xt</code>)</p>
<dd> This widget completes symbol tags created by the <code>etags</code> or <code>ctags</code> programmes (note there is no connection with the completion system&#8217;s tags) stored in a file <code>TAGS</code>, in the format used by <code>etags</code>, or <code>tags</code>, in the format created by <code>ctags</code>. It will look back up the path hierarchy for the first occurrence of either file; if both exist, the file <code>TAGS</code> is preferred. You can specify the full path to a <code>TAGS</code> or <code>tags</code> file by setting the parameter <code>$TAGSFILE</code> or <code>$tagsfile</code> respectively. The corresponding completion tags used are <code>etags</code> and <code>vtags</code>, after emacs and vi respectively.</dl>
<h2>UTILITY FUNCTIONS</h2>
<p> Descriptions follow for utility functions that may be useful when writing completion functions. If functions are installed in subdirectories, most of these reside in the <code>Base</code> subdirectory. Like the example functions for commands in the distribution, the utility functions generating matches all follow the convention of returning status zero if they generated completions and non-zero if no matching completions could be added. </p>
<dl>
<dt>
<dd> <code>_absolute_command_paths</code> This function completes external commands as absolute paths (unlike <code>_command_names -e</code> which completes their basenames). It takes no arguments.</p>
<dt><code>_all_labels</code> [ <code>-x</code> ] [ <code>-12VJ</code> ] <i>tag</i> <i>name</i> <i>descr</i> [ <i>command</i> <i>arg</i> &#8230; ]</p>
<dd> This is a convenient interface to the <code>_next_label</code> function below, implementing the loop shown in the <code>_next_label</code> example. The <i>command</i> and its arguments are called to generate the matches. The options stored in the parameter <i>name</i> will automatically be inserted into the <i>arg</i>s passed to the <i>command</i>. Normally, they are put directly after the <i>command</i>, but if one of the <i>arg</i>s is a single hyphen, they are inserted directly before that. If the hyphen is the last argument, it will be removed from the argument list before the <i>command</i> is called. This allows <code>_all_labels</code> to be used in almost all cases where the matches can be generated by a single call to the <code>compadd</code> builtin command or by a call to one of the utility functions.</p>
<dl>
<dt>
<dd>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>local expl
...
if _requested foo; then
  ...
  _all_labels foo expl '...' compadd ... - $matches
fi</code>
</pre>
</dl>
<p> Will complete the strings from the <code>matches</code> parameter, using <code>compadd</code> with additional options which will take precedence over those generated by <code>_all_labels</code>.</dl>
<dt><code>_alternative</code> [ <code>-O</code> <i>name</i> ] [ <code>-C</code> <i>name</i> ] <i>spec</i> &#8230;</p>
<dd> This function is useful in simple cases where multiple tags are available. Essentially it implements a loop like the one described for the <code>_tags</code> function below.</p>
<dl>
<dt>
<dd>
<p> The tags to use and the action to perform if a tag is requested are described using the <i>spec</i>s which are of the form: `<i>tag</i><code>:</code><i>descr</i><code>:</code><i>action</i>&#8216;. The <i>tag</i>s are offered using <code>_tags</code> and if the tag is requested, the <i>action</i> is executed with the given description <i>descr</i>. The <i>action</i>s are those accepted by the <code>_arguments</code> function (described below), excluding the `<code>-&gt;</code><i>state</i>&#8216; and `<code>=</code><i>&#8230;</i>&#8216; forms. </p>
<p> For example, the <i>action</i> may be a simple function call: </p>
<dl>
<dt>
<dd>
<pre>
<code>_alternative \ 
    'users:user:_users' \ 
    'hosts:host:_hosts'</code>
</pre>
</dl>
<p> offers usernames and hostnames as possible matches, generated by the <code>_users</code> and <code>_hosts</code> functions respectively. </p>
<p> Like <code>_arguments</code>, this function uses <code>_all_labels</code> to execute the actions, which will loop over all sets of tags. Special handling is only required if there is an additional valid tag, for example inside a function called from <code>_alternative</code>. </p>
<p> The option `<code>-O</code> <i>name</i>&#8216; is used in the same way as by the <code>_arguments</code> function. In other words, the elements of the <i>name</i> array will be passed to <code>compadd</code> when executing an action. </p>
<p> Like <code>_tags</code> this function supports the <code>-C</code> option to give a different name for the argument context field.</dl>
<dt>
<dd> <code>_arguments </code>[ <code>-nswWCRS</code> ] [ <code>-A</code> <i>pat</i> ] [ <code>-O</code> <i>name</i> ] [ <code>-M</code> <i>matchspec</i> ]</p>
<dt>
<dd> [ <code>:</code> ] <i>spec</i> &#8230;</p>
<dt>
<dd> <code>_arguments </code>[ <i>opt</i> &#8230; ] <code>&#8211;</code><code>&#8211;</code> [ <code>-l</code> ] [ <code>-i</code> <i>pats</i> ] [ <code>-s</code> <i>pair</i> ]</p>
<dt>
<dd> [ <i>helpspec</i> &#8230;] This function can be used to give a complete specification for completion for a command whose arguments follow standard UNIX option and argument conventions.</p>
<dl>
<dt>
<dd>
<p> <i>Options Overview</i> </p>
<p> Options to <code>_arguments</code> itself must be in separate words, i.e. <code>-s -w</code>, not <code>-sw</code>. The options are followed by <i>spec</i>s that describe options and arguments of the analyzed command. To avoid ambiguity, all options to <code>_arguments</code> itself may be separated from the <i>spec</i> forms by a single colon. </p>
<p> The `<code>&#8211;</code><code>&#8211;</code>&#8216; form is used to intuit <i>spec</i> forms from the help output of the command being analyzed, and is described in detail below. The <i>opts</i> for the `<code>&#8211;</code><code>&#8211;</code>&#8216; form are otherwise the same options as the first form. Note that `<code>-s</code>&#8216; following `<code>&#8211;</code><code>&#8211;</code>&#8216; has a distinct meaning from `<code>-s</code>&#8216; preceding `<code>&#8211;</code><code>&#8211;</code>&#8216;, and both may appear. </p>
<p> The option switches <code>-s</code>, <code>-S</code>, <code>-A</code>, <code>-w</code>, and <code>-W</code> affect how <code>_arguments</code> parses the analyzed command line&#8217;s options. These switches are useful for commands with standard argument parsing. </p>
<p> The options of <code>_arguments</code> have the following meanings: </p>
<dl>
<dt>
<dd> <code>-n</code> With this option, <code>_arguments</code> sets the parameter <code>NORMARG</code> to the position of the first normal argument in the <code>$words</code> array, i.e. the position after the end of the options. If that argument has not been reached, <code>NORMARG</code> is set to <code>-1</code>. The caller should declare `<code>integer NORMARG</code>&#8216; if the <code>-n</code> option is passed; otherwise the parameter is not used.</p>
<dt><code>-s</code></p>
<dd> Enable <i>option stacking</i> for single-letter options, whereby multiple single-letter options may be combined into a single word. For example, the two options `<code>-x</code>&#8216; and `<code>-y</code>&#8216; may be combined into a single word `<code>-xy</code>&#8216;. By default, every word corresponds to a single option name (`<code>-xy</code>&#8216; is a single option named `<code>xy</code>&#8216;).</p>
<dl>
<dt>
<dd>
<p> Options beginning with a single hyphen or plus sign are eligible for stacking; words beginning with two hyphens are not. </p>
<p> Note that <code>-s</code> after <code>&#8211;</code><code>&#8211;</code> has a different meaning, which is documented in the segment entitled `Deriving <i>spec</i> forms from the help output&#8217;.</dl>
<dt><code>-w</code></p>
<dd> In combination with <code>-s</code>, allow option stacking even if one or more of the options take arguments. For example, if <code>-x</code> takes an argument, with no <code>-s</code>, `<code>-xy</code>&#8216; is considered as a single (unhandled) option; with <code>-s</code>, <code>-xy</code> is an option with the argument `<code>y</code>&#8216;; with both <code>-s</code> and <code>-w</code>, <code>-xy</code> is the option <code>-x</code> and the option <code>-y</code> with arguments to <code>-x</code> (and to <code>-y</code>, if it takes arguments) still to come in subsequent words.</p>
<dt><code>-W</code></p>
<dd> This option takes <code>-w</code> a stage further: it is possible to complete single-letter options even after an argument that occurs in the same word. However, it depends on the action performed whether options will really be completed at this point. For more control, use a utility function like <code>_guard</code> as part of the action.</p>
<dt><code>-C</code></p>
<dd> Modify the <code>curcontext</code> parameter for an action of the form `<code>-&gt;</code><i>state</i>&#8216;. This is discussed in detail below.</p>
<dt><code>-R</code></p>
<dd> Return status 300 instead of zero when a <code>$state</code> is to be handled, in the `<code>-&gt;</code><i>string</i>&#8216; syntax.</p>
<dt><code>-S</code></p>
<dd> Do not complete options after a `<code>&#8211;</code><code>&#8211;</code>&#8216; appearing on the line, and ignore the `<code>&#8211;</code><code>&#8211;</code>&#8216;. For example, with <code>-S</code>, in the line</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>foobar -x -- -y</code>
</pre>
</dl>
<p> the `<code>-x</code>&#8216; is considered an option, the `<code>-y</code>&#8216; is considered an argument, and the `<code>&#8211;</code><code>&#8211;</code>&#8216; is considered to be neither.</dl>
<dt><code>-A</code> <i>pat</i></p>
<dd> Do not complete options after the first non-option argument on the line. <i>pat</i> is a pattern matching all strings which are not to be taken as arguments. For example, to make <code>_arguments</code> stop completing options after the first normal argument, but ignoring all strings starting with a hyphen even if they are not described by one of the <i>optspec</i>s, the form is `<code>-A &quot;-*&quot;</code>&#8216;.</p>
<dt><code>-O</code> <i>name</i></p>
<dd> Pass the elements of the array <i>name</i> as arguments to functions called to execute <i>action</i>s. This is discussed in detail below.</p>
<dt><code>-M</code> <i>matchspec</i></p>
<dd> Use the match specification <i>matchspec</i> for completing option names and values. The default <i>matchspec</i> allows partial word completion after `<code>_</code>&#8216; and `<code>&#8211;</code>&#8216;, such as completing `<code>-f-b</code>&#8216; to `<code>-foo-bar</code>&#8216;. The default <i>matchspec</i> is:</p>
<dl>
<dt>
<dd>
<pre>
<code>r:|[_-]=* r:|=*</code>
</pre>
</dl>
</dl>
<p> <i>spec</i>s: overview </p>
<p> Each of the following forms is a <i>spec</i> describing individual sets of options or arguments on the command line being analyzed. </p>
<dl>
<dt>
<dd> <i>n</i><code>:</code><i>message</i><code>:</code><i>action</i></p>
<dt>
<dd> <i>n</i><code>::</code><i>message</i><code>:</code><i>action</i> This describes the <i>n</i>&#8216;th normal argument. The <i>message</i> will be printed above the matches generated and the <i>action</i> indicates what can be completed in this position (see below). If there are two colons before the <i>message</i> the argument is optional. If the <i>message</i> contains only white space, nothing will be printed above the matches unless the action adds an explanation string itself.</p>
<dt>
<dd> <code>:</code><i>message</i><code>:</code><i>action</i></p>
<dt>
<dd> <code>::</code><i>message</i><code>:</code><i>action</i> Similar, but describes the <i>next</i> argument, whatever number that happens to be. If all arguments are specified in this form in the correct order the numbers are unnecessary.</p>
<dt>
<dd> <code>*:</code><i>message</i><code>:</code><i>action</i></p>
<dt>
<dd> <code>*::</code><i>message</i><code>:</code><i>action</i></p>
<dt>
<dd> <code>*:::</code><i>message</i><code>:</code><i>action</i> This describes how arguments (usually non-option arguments, those not beginning with <code>&#8211;</code> or <code>+</code>) are to be completed when neither of the first two forms was provided. Any number of arguments can be completed in this fashion.</p>
<dl>
<dt>
<dd>
<p> With two colons before the <i>message</i>, the <code>words</code> special array and the <code>CURRENT</code> special parameter are modified to refer only to the normal arguments when the <i>action</i> is executed or evaluated. With three colons before the <i>message</i> they are modified to refer only to the normal arguments covered by this description.</dl>
<dt>
<dd> <i>optspec</i></p>
<dt>
<dd> <i>optspec</i><code>:</code><i>&#8230;</i> This describes an option. The colon indicates handling for one or more arguments to the option; if it is not present, the option is assumed to take no arguments.</p>
<dl>
<dt>
<dd>
<p> The following forms are available for the initial <i>optspec</i>, whether or not the option has arguments. </p>
<dl>
<dt>
<dd> <code>*</code><i>optspec</i> Here <i>optspec</i> is one of the remaining forms below. This indicates the following <i>optspec</i> may be repeated. Otherwise if the corresponding option is already present on the command line to the left of the cursor it will not be offered again.</p>
<dt>
<dd> <code>&#8211;</code><i>optname</i></p>
<dt>
<dd> <code>+</code><i>optname</i> In the simplest form the <i>optspec</i> is just the option name beginning with a minus or a plus sign, such as `<code>-foo</code>&#8216;. The first argument for the option (if any) must follow as a <i>separate</i> word directly after the option.</p>
<dl>
<dt>
<dd>
<p> Either of `<code>-+</code><i>optname</i>&#8216; and `<code>+-</code><i>optname</i>&#8216; can be used to specify that <code>&#8211;</code><i>optname</i> and <code>+</code><i>optname</i> are both valid. </p>
<p> In all the remaining forms, the leading `<code>&#8211;</code>&#8216; may be replaced by or paired with `<code>+</code>&#8216; in this way.</dl>
<dt><code>&#8211;</code><i>optname</i><code>&#8211;</code></p>
<dd> The first argument of the option must come directly after the option name <i>in the same word</i>. For example, `<code>-foo-:</code><i>&#8230;</i>&#8216; specifies that the completed option and argument will look like `<code>-foo</code><i>arg</i>&#8216;.</p>
<dt><code>&#8211;</code><i>optname</i><code>+</code></p>
<dd> The first argument may appear immediately after <i>optname</i> in the same word, or may appear as a separate word after the option. For example, `<code>-foo+:</code><i>&#8230;</i>&#8216; specifies that the completed option and argument will look like either `<code>-foo</code><i>arg</i>&#8216; or `<code>-foo</code> <i>arg</i>&#8216;.</p>
<dt><code>&#8211;</code><i>optname</i><code>=</code></p>
<dd> The argument may appear as the next word, or in same word as the option name provided that it is separated from it by an equals sign, for example `<code>-foo=</code><i>arg</i>&#8216; or `<code>-foo</code> <i>arg</i>&#8216;.</p>
<dt><code>&#8211;</code><i>optname</i><code>=-</code></p>
<dd> The argument to the option must appear after an equals sign in the same word, and may not be given in the next argument.</p>
<dt><i>optspec</i><code>[</code><i>explanation</i><code>]</code></p>
<dd> An explanation string may be appended to any of the preceding forms of <i>optspec</i> by enclosing it in brackets, as in `<code>-q[query operation]</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> The <code>verbose</code> style is used to decide whether the explanation strings are displayed with the option in a completion listing. </p>
<p> If no bracketed explanation string is given but the <code>auto-description</code> style is set and only one argument is described for this <i>optspec</i>, the value of the style is displayed, with any appearance of the sequence `<code>%d</code>&#8216; in it replaced by the <i>message</i> of the first <i>optarg</i> that follows the <i>optspec</i>; see below.</dl>
</dl>
<p> It is possible for options with a literal `<code>+</code>&#8216; or `<code>=</code>&#8216; to appear, but that character must be quoted, for example `<code>-\+</code>&#8216;. </p>
<p> Each <i>optarg</i> following an <i>optspec</i> must take one of the following forms: </p>
<dl>
<dt>
<dd> <code>:</code><i>message</i><code>:</code><i>action</i></p>
<dt>
<dd> <code>::</code><i>message</i><code>:</code><i>action</i> An argument to the option; <i>message</i> and <i>action</i> are treated as for ordinary arguments. In the first form, the argument is mandatory, and in the second form it is optional.</p>
<dl>
<dt>
<dd>
<p> This group may be repeated for options which take multiple arguments. In other words, <code>:</code><i>message1</i><code>:</code><i>action1</i><code>:</code><i>message2</i><code>:</code><i>action2</i> specifies that the option takes two arguments.</dl>
<dt>
<dd> <code>:*</code><i>pattern</i><code>:</code><i>message</i><code>:</code><i>action</i></p>
<dt>
<dd> <code>:*</code><i>pattern</i><code>::</code><i>message</i><code>:</code><i>action</i></p>
<dt>
<dd> <code>:*</code><i>pattern</i><code>:::</code><i>message</i><code>:</code><i>action</i> This describes multiple arguments. Only the last <i>optarg</i> for an option taking multiple arguments may be given in this form. If the <i>pattern</i> is empty (i.e. <code>:*:</code>), all the remaining words on the line are to be completed as described by the <i>action</i>; otherwise, all the words up to and including a word matching the <i>pattern</i> are to be completed using the <i>action</i>.</p>
<dl>
<dt>
<dd>
<p> Multiple colons are treated as for the `<code>*:</code><i>&#8230;</i>&#8216; forms for ordinary arguments: when the <i>message</i> is preceded by two colons, the <code>words</code> special array and the <code>CURRENT</code> special parameter are modified during the execution or evaluation of the <i>action</i> to refer only to the words after the option. When preceded by three colons, they are modified to refer only to the words covered by this description.</dl>
</dl>
</dl>
</dl>
<p> Any literal colon in an <i>optname</i>, <i>message</i>, or <i>action</i> must be preceded by a backslash, `<code>\:</code>&#8216;. </p>
<p> Each of the forms above may be preceded by a list in parentheses of option names and argument numbers. If the given option is on the command line, the options and arguments indicated in parentheses will not be offered. For example, `<code>(-two -three 1)-one:</code><i>&#8230;</i>&#8216; completes the option `<code>-one</code>&#8216;; if this appears on the command line, the options <code>-two</code> and <code>-three</code> and the first ordinary argument will not be completed after it. `<code>(-foo):</code><i>&#8230;</i>&#8216; specifies an ordinary argument completion; <code>-foo</code> will not be completed if that argument is already present. </p>
<p> Other items may appear in the list of excluded options to indicate various other items that should not be applied when the current specification is matched: a single star (<code>*</code>) for the rest arguments (i.e. a specification of the form `<code>*:</code><i>&#8230;</i>&#8216;); a colon (<code>:</code>) for all normal (non-option-) arguments; and a hyphen (<code>&#8211;</code>) for all options. For example, if `<code>(*)</code>&#8216; appears before an option and the option appears on the command line, the list of remaining arguments (those shown in the above table beginning with `<code>*:</code>&#8216;) will not be completed. </p>
<p> To aid in reuse of specifications, it is possible to precede any of the forms above with `<code>!</code>&#8216;; then the form will no longer be completed, although if the option or argument appears on the command line they will be skipped as normal. The main use for this is when the arguments are given by an array, and <code>_arguments</code> is called repeatedly for more specific contexts: on the first call `<code>_arguments $global_options</code>&#8216; is used, and on subsequent calls `<code>_arguments !$^global_options</code>&#8216;. </p>
<p> <i>spec</i>s: actions </p>
<p> In each of the forms above the <i>action</i> determines how completions should be generated. Except for the `<code>-&gt;</code><i>string</i>&#8216; form below, the <i>action</i> will be executed by calling the <code>_all_labels</code> function to process all tag labels. No special handling of tags is needed unless a function call introduces a new one. </p>
<p> The functions called to execute <i>action</i>s will be called with the elements of the array named by the `<code>-O</code> <i>name</i>&#8216; option as arguments. This can be used, for example, to pass the same set of options for the <code>compadd</code> builtin to all <i>action</i>s. </p>
<p> The forms for <i>action</i> are as follows. </p>
<dl>
<dt>
<dd> (single unquoted space) This is useful where an argument is required but it is not possible or desirable to generate matches for it. The <i>message</i> will be displayed but no completions listed. Note that even in this case the colon at the end of the <i>message</i> is needed; it may only be omitted when neither a <i>message</i> nor an <i>action</i> is given.</p>
<dt><code>(</code><i>item1</i> <i>item2</i> <i>&#8230;</i><code>)</code></p>
<dd> One of a list of possible matches, for example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>:foo:(foo bar baz</code><code>)</code>
</pre>
</dl>
</dl>
<dt><code>((</code><i>item1</i>\:<i>desc1</i> <i>&#8230;</i>))</p>
<dd> Similar to the above, but with descriptions for each possible match. Note the backslash before the colon. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>:foo:((a\:bar b\:baz</code><code>))</code>
</pre>
</dl>
<p> The matches will be listed together with their descriptions if the <code>description</code> style is set with the <code>values</code> tag in the context.</dl>
<dt><code>-&gt;</code><i>string</i></p>
<dd> In this form, <code>_arguments</code> processes the arguments and options and then returns control to the calling function with parameters set to indicate the state of processing; the calling function then makes its own arrangements for generating completions. For example, functions that implement a state machine can use this type of action.</p>
<dl>
<dt>
<dd>
<p> Where <code>_arguments</code> encounters <i>action</i> in the `<code>-&gt;</code><i>string</i>&#8216; format, it will strip all leading and trailing whitespace from <i>string</i> and set the array <code>state</code> to the set of all <i>string</i>s for which an action is to be performed. The elements of the array <code>state_descr</code> are assigned the corresponding <i>message</i> field from each <i>optarg</i> containing such an <i>action</i>. </p>
<p> By default and in common with all other well behaved completion functions, _arguments returns status zero if it was able to add matches and non-zero otherwise. However, if the <code>-R</code> option is given, <code>_arguments</code> will instead return a status of 300 to indicate that <code>$state</code> is to be handled. </p>
<p> In addition to <code>$state</code> and <code>$state_descr</code>, <code>_arguments</code> also sets the global parameters `<code>context</code>&#8216;, `<code>line</code>&#8216; and `<code>opt_args</code>&#8216; as described below, and does not reset any changes made to the special parameters such as <code>PREFIX</code> and <code>words</code>. This gives the calling function the choice of resetting these parameters or propagating changes in them. </p>
<p> A function calling <code>_arguments</code> with at least one action containing a `<code>-&gt;</code><i>string</i>&#8216; must therefore declare appropriate local parameters: </p>
<dl>
<dt>
<dd>
<pre>
<code>local context state state_descr line
typeset -A opt_args</code>
</pre>
</dl>
<p> to prevent <code>_arguments</code> from altering the global environment.</dl>
<dt><code>{</code><i>eval-string</i><code>}</code></p>
<dd> A string in braces is evaluated as shell code to generate matches. If the <i>eval-string</i> itself does not begin with an opening parenthesis or brace it is split into separate words before execution.</p>
<dt><code>= </code><i>action</i></p>
<dd> If the <i>action</i> starts with `<code>= </code>&#8216; (an equals sign followed by a space), <code>_arguments</code> will insert the contents of the <i>argument</i> field of the current context as the new first element in the <code>words</code> special array and increment the value of the <code>CURRENT</code> special parameter. This has the effect of inserting a dummy word onto the completion command line while not changing the point at which completion is taking place.</p>
<dl>
<dt>
<dd>
<p> This is most useful with one of the specifiers that restrict the words on the command line on which the <i>action</i> is to operate (the two- and three-colon forms above). One particular use is when an <i>action</i> itself causes <code>_arguments</code> on a restricted range; it is necessary to use this trick to insert an appropriate command name into the range for the second call to <code>_arguments</code> to be able to parse the line.</dl>
<dt>
<dd> <i></i>word&#8230;</p>
<dt>
<dd> <i>word&#8230;</i> This covers all forms other than those above. If the <i>action</i> starts with a space, the remaining list of words will be invoked unchanged.</p>
<dl>
<dt>
<dd>
<p> Otherwise it will be invoked with some extra strings placed after the first word; these are to be passed down as options to the <code>compadd</code> builtin. They ensure that the state specified by <code>_arguments</code>, in particular the descriptions of options and arguments, is correctly passed to the completion command. These additional arguments are taken from the array parameter `<code>expl</code>&#8216;; this will be set up before executing the <i>action</i> and hence may be referred to inside it, typically in an expansion of the form `<code>$expl[@]</code>&#8216; which preserves empty elements of the array.</dl>
</dl>
<p> During the performance of the action the array `<code>line</code>&#8216; will be set to the normal arguments from the command line, i.e. the words from the command line after the command name excluding all options and their arguments. Options are stored in the associative array `<code>opt_args</code>&#8216; with option names as keys and their arguments as the values. For options that have more than one argument these are given as one string, separated by colons. All colons and backslashes in the original arguments are preceded with backslashes. </p>
<p> The parameter `<code>context</code>&#8216; is set when returning to the calling function to perform an action of the form `<code>-&gt;</code><i>string</i>&#8216;. It is set to an array of elements corresponding to the elements of <code>$state</code>. Each element is a suitable name for the argument field of the context: either a string of the form `<code>option</code><i>-opt</i><code>&#8211;</code><i>n</i>&#8216; for the <i>n</i>&#8216;th argument of the option <i>-opt</i>, or a string of the form `<code>argument-</code><i>n</i>&#8216; for the <i>n</i>&#8216;th argument. For `rest&#8217; arguments, that is those in the list at the end not handled by position, <i>n</i> is the string `<code>rest</code>&#8216;. For example, when completing the argument of the <code>-o</code> option, the name is `<code>option-o-1</code>&#8216;, while for the second normal (non-option-) argument it is `<code>argument-2</code>&#8216;. </p>
<p> Furthermore, during the evaluation of the <i>action</i> the context name in the <code>curcontext</code> parameter is altered to append the same string that is stored in the <code>context</code> parameter. </p>
<p> The option <code>-C</code> tells <code>_arguments</code> to modify the <code>curcontext</code> parameter for an action of the form `<code>-&gt;</code><i>state</i>&#8216;. This is the standard parameter used to keep track of the current context. Here it (and not the <code>context</code> array) should be made local to the calling function to avoid passing back the modified value and should be initialised to the current value at the start of the function: </p>
<dl>
<dt>
<dd>
<pre>
<code>local curcontext=&quot;$curcontext&quot;</code>
</pre>
</dl>
<p> This is useful where it is not possible for multiple states to be valid together. </p>
<p> <i>Grouping Options</i> </p>
<p> Options can be grouped to simplify exclusion lists. A group is introduced with `<code>+</code>&#8216; followed by a name for the group in the subsequent word. Whole groups can then be referenced in an exclusion list or a group name can be used to disambiguate between two forms of the same option. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>_arguments \ 
    '(group2--x)-a' \ 
  + group1 \ 
    -m \ 
    '(group2)-n' \ 
  + group2 \ 
    -x -y</code>
</pre>
</dl>
<p> If the name of a group is specified in the form `<code>(</code><i>name</i><code>)</code>&#8216; then only one value from that group will ever be completed; more formally, all specifications are mutually exclusive to all other specifications in that group. This is useful for defining options that are aliases for each other. For example: </p>
<dl>
<dt>
<dd>
_arguments \<br />
    &#8211;<br />
    a &#8211; b \<br />
  + &#8216;(operation)&#8217; \ </p>
<p>{<br />
    -c, &#8211;compress<br />
}<br />
&#8216;[compress]&#8217; \ </p>
<p>{<br />
    -d, &#8211;decompress<br />
}<br />
&#8216;[decompress]&#8217; \ </p>
<p>{<br />
    -l, &#8211;list<br />
}<br />
&#8216;[list]&#8217;
</dl>
<p> If an option in a group appears on the command line, it is stored in the associative array `<code>opt_args</code>&#8216; with &#8216;<i>group</i><code>&#8211;</code><i>option</i>&#8216; as a key. In the example above, a key `<code>operation&#8211;c</code>&#8216; is used if the option `<code>-c</code>&#8216; is present on the command line. </p>
<p> <i>Specifying Multiple Sets of Arguments</i> </p>
<p> It is possible to specify multiple sets of options and arguments with the sets separated by single hyphens. This differs from groups in that sets are considered to be mutually exclusive of each other. </p>
<p> Specifications before the first set and from any group are common to all sets. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>_arguments \ 
    -a \ 
  - set1 \ 
    -c \ 
  - set2 \ 
    -d \ 
    ':arg:(x2 y2)'</code>
</pre>
</dl>
<p> This defines two sets. When the command line contains the option `<code>-c</code>&#8216;, the `<code>-d</code>&#8216; option and the argument will not be considered possible completions. When it contains `<code>-d</code>&#8216; or an argument, the option `<code>-c</code>&#8216; will not be considered. However, after `<code>-a</code>&#8216; both sets will still be considered valid. </p>
<p> As for groups, the name of a set may appear in exclusion lists, either alone or preceding a normal option or argument specification. </p>
<p> The completion code has to parse the command line separately for each set. This can be slow so sets should only be used when necessary. A useful alternative is often an option specification with rest-arguments (as in `<code>-foo:*:&#8230;</code>&#8216;); here the option <code>-foo</code> swallows up all remaining arguments as described by the <i>optarg</i> definitions. </p>
<p> <i>Deriving spec</i> forms from the help output </p>
<p> The option `<code>&#8211;</code><code>&#8211;</code>&#8216; allows <code>_arguments</code> to work out the names of long options that support the `<code>&#8211;</code><code>-help</code>&#8216; option which is standard in many GNU commands. The command word is called with the argument `<code>&#8211;</code><code>-help</code>&#8216; and the output examined for option names. Clearly, it can be dangerous to pass this to commands which may not support this option as the behaviour of the command is unspecified. </p>
<p> In addition to options, `<code>_arguments &#8211;</code><code>&#8211;</code>&#8216; will try to deduce the types of arguments available for options when the form `<code>&#8211;</code><code>&#8211;</code><i>opt</i><code>=</code><i>val</i>&#8216; is valid. It is also possible to provide hints by examining the help text of the command and adding <i>helpspec</i> of the form `<i>pattern</i><code>:</code><i>message</i><code>:</code><i>action</i>&#8216;; note that other <code>_arguments</code> <i>spec</i> forms are not used. The <i>pattern</i> is matched against the help text for an option, and if it matches the <i>message</i> and <i>action</i> are used as for other argument specifiers. The special case of `<code>*:</code>&#8216; means both <i>message</i> and <i>action</i> are empty, which has the effect of causing options having no description in the help output to be ordered in listings ahead of options that have a description. </p>
<p> For example: </p>
<dl>
<dt>
<dd>
_arguments&#8211; &#8216;*\*:toggle:(yes no)&#8217; \<br />
              &#8216;*=FILE*:file:_files&#8217; \<br />
              &#8216;*=DIR*:directory:_files -/&#8217; \<br />
              &#8216;*=PATH*:directory:_files -/&#8217;
</dl>
<p> Here, `<code>yes</code>&#8216; and `<code>no</code>&#8216; will be completed as the argument of options whose description ends in a star; file names will be completed for options that contain the substring `<code>=FILE</code>&#8216; in the description; and directories will be completed for options whose description contains `<code>=DIR</code>&#8216; or `<code>=PATH</code>&#8216;. The last three are in fact the default and so need not be given explicitly, although it is possible to override the use of these patterns. A typical help text which uses this feature is: </p>
<dl>
<dt>
<dd>
<pre>
<code>  -C, --directory=DIR          change to directory DIR</code>
</pre>
</dl>
<p> so that the above specifications will cause directories to be completed after `<code>&#8211;</code><code>-directory</code>&#8216;, though not after `<code>-C</code>&#8216;. </p>
<p> Note also that <code>_arguments</code> tries to find out automatically if the argument for an option is optional. This can be specified explicitly by doubling the colon before the <i>message</i>. </p>
<p> If the <i>pattern</i> ends in `<code>(-)</code>&#8216;, this will be removed from the pattern and the <i>action</i> will be used only directly after the `<code>=</code>&#8216;, not in the next word. This is the behaviour of a normal specification defined with the form `<code>=-</code>&#8216;. </p>
<p> By default, the command (with the option `<code>&#8211;help</code>&#8216;) is run after resetting all the locale categories (except for <code>LC_CTYPE</code>) to `<code>C</code>&#8216;. If the localized help output is known to work, the option `<code>-l</code>&#8216; can be specified after the `<code>_arguments &#8211;</code><code>&#8211;</code>&#8216; so that the command is run in the current locale. </p>
<p> The `<code>_arguments &#8211;</code><code>&#8211;</code>&#8216; can be followed by the option `<code>-i</code> <i>patterns</i>&#8216; to give patterns for options which are not to be completed. The patterns can be given as the name of an array parameter or as a literal list in parentheses. For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>_arguments -- -i \ 
    &quot;(--(en|dis)able-FEATURE*)&quot;</code>
</pre>
</dl>
<p> will cause completion to ignore the options `<code>&#8211;</code><code>-enable-FEATURE</code>&#8216; and `<code>&#8211;</code><code>-disable-FEATURE</code>&#8216; (this example is useful with GNU <code>configure</code>). </p>
<p> The `<code>_arguments &#8211;</code><code>&#8211;</code>&#8216; form can also be followed by the option `<code>-s</code> <i>pair</i>&#8216; to describe option aliases. The <i>pair</i> consists of a list of alternating patterns and corresponding replacements, enclosed in parens and quoted so that it forms a single argument word in the <code>_arguments</code> call. </p>
<p> For example, some <code>configure</code>-script help output describes options only as `<code>&#8211;</code><code>-enable-foo</code>&#8216;, but the script also accepts the negated form `<code>&#8211;</code><code>-disable-foo</code>&#8216;. To allow completion of the second form: </p>
<dl>
<dt>
<dd>
<pre>
<code>_arguments -- -s &quot;((#s)--enable- --disable-)&quot;</code>
</pre>
</dl>
<p> <i>Miscellaneous notes</i> </p>
<p> Finally, note that <code>_arguments</code> generally expects to be the primary function handling any completion for which it is used. It may have side effects which change the treatment of any matches added by other functions called after it. To combine <code>_arguments</code> with other functions, those functions should be called either before <code>_arguments</code>, as an <i>action</i> within a <i>spec</i>, or in handlers for `<code>-&gt;</code><i>state</i>&#8216; actions. </p>
<p> Here is a more general example of the use of <code>_arguments</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>_arguments '-l+:left border:' \ 
           '-format:paper size:(letter A4)' \ 
           '*-copy:output file:_files::resolution:(300 600)' \ 
           ':postscript file:_files -g \*.\(ps\|eps\)' \ 
           '*:page number:'</code>
</pre>
</dl>
<p> This describes three options: `<code>-l</code>&#8216;, `<code>-format</code>&#8216;, and `<code>-copy</code>&#8216;. The first takes one argument described as `<i>left border</i>&#8216; for which no completion will be offered because of the empty action. Its argument may come directly after the `<code>-l</code>&#8216; or it may be given as the next word on the line. </p>
<p> The `<code>-format</code>&#8216; option takes one argument in the next word, described as `<i>paper size</i>&#8216; for which only the strings `<code>letter</code>&#8216; and `<code>A4</code>&#8216; will be completed. </p>
<p> The `<code>-copy</code>&#8216; option may appear more than once on the command line and takes two arguments. The first is mandatory and will be completed as a filename. The second is optional (because of the second colon before the description `<i>resolution</i>&#8216;) and will be completed from the strings `<code>300</code>&#8216; and `<code>600</code>&#8216;. </p>
<p> The last two descriptions say what should be completed as arguments. The first describes the first argument as a `<i>postscript file</i>&#8216; and makes files ending in `<code>ps</code>&#8216; or `<code>eps</code>&#8216; be completed. The last description gives all other arguments the description `<i>page numbers</i>&#8216; but does not offer completions.</dl>
<dt><code>_cache_invalid</code> <i>cache_identifier</i></p>
<dd> This function returns status zero if the completions cache corresponding to the given cache identifier needs rebuilding. It determines this by looking up the <code>cache-policy</code> style for the current context. This should provide a function name which is run with the full path to the relevant cache file as the only argument.</p>
<dl>
<dt>
<dd>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>_example_caching_policy () {
    # rebuild if cache is more than a week old
    local -a oldp
    oldp=( &quot;$1&quot;(Nm+7) )
    (( $#oldp ))
}</code>
</pre>
</dl>
</dl>
<dt><code>_call_function</code> <i>return</i> <i>name</i> [ <i>arg</i> &#8230; ]</p>
<dd> If a function <i>name</i> exists, it is called with the arguments <i>arg</i>s. The <i>return</i> argument gives the name of a parameter in which the return status from the function <i>name</i> should be stored; if <i>return</i> is empty or a single hyphen it is ignored.</p>
<dl>
<dt>
<dd>
<p> The return status of <code>_call_function</code> itself is zero if the function <i>name</i> exists and was called and non-zero otherwise.</dl>
<dt><code>_call_program</code> [ <code>-l</code> ] [ <code>-p</code> ] <i>tag</i> <i>string</i> &#8230;</p>
<dd> This function provides a mechanism for the user to override the use of an external command. It looks up the <code>command</code> style with the supplied <i>tag</i>. If the style is set, its value is used as the command to execute. The <i>string</i>s from the call to <code>_call_program</code>, or from the style if set, are concatenated with spaces between them and the resulting string is evaluated. The return status is the return status of the command called.</p>
<dl>
<dt>
<dd>
<p> By default, the command is run in an environment where all the locale categories (except for <code>LC_CTYPE</code>) are reset to `<code>C</code>&#8216; by calling the utility function <code>_comp_locale</code> (see below). If the option `<code>-l</code>&#8216; is given, the command is run with the current locale. </p>
<p> If the option `<code>-p</code>&#8216; is supplied it indicates that the command output is influenced by the permissions it is run with. If the <code>gain-privileges</code> style is set to true, <code>_call_program</code> will make use of commands such as <code>sudo</code>, if present on the command-line, to match the permissions to whatever the final command is likely to run under. When looking up the <code>gain-privileges</code> and <code>command</code> styles, the command component of the zstyle context will end with a slash (`<code>/</code>&#8216;) followed by the command that would be used to gain privileges.</dl>
<dt><code>_combination</code> [ <code>-s</code> <i>pattern</i> ] <i>tag</i> <i>style</i> <i>spec</i> &#8230; <i>field</i> <i>opts</i> &#8230;</p>
<dd> This function is used to complete combinations of values, for example pairs of hostnames and usernames. The <i>style</i> argument gives the style which defines the pairs; it is looked up in a context with the <i>tag</i> specified.</p>
<dl>
<dt>
<dd>
<p> The style name consists of field names separated by hyphens, for example `<code>users-hosts-ports</code>&#8216;. For each field for a value is already known, a <i>spec</i> of the form `<i>field</i><code>=</code><i>pattern</i>&#8216; is given. For example, if the command line so far specifies a user `<code>pws</code>&#8216;, the argument `<code>users=pws</code>&#8216; should appear. </p>
<p> The next argument with no equals sign is taken as the name of the field for which completions should be generated (presumably not one of the <i>field</i>s for which the value is known). </p>
<p> The matches generated will be taken from the value of the style. These should contain the possible values for the combinations in the appropriate order (users, hosts, ports in the example above). The values for the different fields are separated by colons. This can be altered with the option <code>-s</code> to <code>_combination</code> which specifies a pattern. Typically this is a character class, as for example `<code>-s &quot;[:@]&quot;</code>&#8216; in the case of the <code>users-hosts</code> style. Each `<i>field</i><code>=</code><i>pattern</i>&#8216; specification restricts the completions which apply to elements of the style with appropriately matching fields. </p>
<p> If no style with the given name is defined for the given tag, or if none of the strings in style&#8217;s value match, but a function name of the required field preceded by an underscore is defined, that function will be called to generate the matches. For example, if there is no `<code>users-hosts-ports</code>&#8216; or no matching hostname when a host is required, the function `<code>_hosts</code>&#8216; will automatically be called. </p>
<p> If the same name is used for more than one field, in both the `<i>field</i><code>=</code><i>pattern</i>&#8216; and the argument that gives the name of the field to be completed, the number of the field (starting with one) may be given after the fieldname, separated from it by a colon. </p>
<p> All arguments after the required field name are passed to <code>compadd</code> when generating matches from the style value, or to the functions for the fields if they are called.</dl>
<dt><code>_command_names</code> [ <code>-e</code> | <code>&#8211;</code> ]</p>
<dd> This function completes words that are valid at command position: names of aliases, builtins, hashed commands, functions, and so on. With the <code>-e</code> flag, only hashed commands are completed. The <code>&#8211;</code> flag is ignored.</p>
<dt><code>_comp_locale</code></p>
<dd> This function resets all the locale categories other than <code>LC_CTYPE</code> to `<code>C</code>&#8216; so that the output from external commands can be easily analyzed by the completion system. <code>LC_CTYPE</code> retains the current value (taking <code>LC_ALL</code> and <code>LANG</code> into account), ensuring that non-ASCII characters in file names are still handled properly.</p>
<dl>
<dt>
<dd>
<p> This function should normally be run only in a subshell, because the new locale is exported to the environment. Typical usage would be `<code>$(_comp_locale; </code><i>command</i> &#8230;<code>)</code>&#8216;.</dl>
<dt><code>_completers</code> [ <code>-p</code> ]</p>
<dd> This function completes names of completers.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>-p</code> Include the leading underscore (`<code>_</code>&#8216;) in the matches.</dl>
</dl>
<dt>
<dd> <code>_describe </code>[<code>-12JVx</code>] [ <code>-oO</code> | <code>-t</code> <i>tag</i> ] <i>descr</i> <i>name1</i> [ <i>name2</i> ] [ <i>opt</i> &#8230; ]</p>
<dt>
<dd> [ <code>&#8211;</code><code>&#8211;</code> <i>name1</i> [ <i>name2</i> ] [ <i>opt</i> &#8230; ] &#8230; ] This function associates completions with descriptions. Multiple groups separated by <code>&#8211;</code><code>&#8211;</code> can be supplied, potentially with different completion options <i>opt</i>s.</p>
<dl>
<dt>
<dd>
<p> The <i>descr</i> is taken as a string to display above the matches if the <code>format</code> style for the <code>descriptions</code> tag is set. This is followed by one or two names of arrays followed by options to pass to <code>compadd</code>. The array <i>name1</i> contains the possible completions with their descriptions in the form `<i>completion</i><code>:</code><i>description</i>&#8216;. Any literal colons in <i>completion</i> must be quoted with a backslash. If a <i>name2</i> is given, it should have the same number of elements as <i>name1</i>; in this case the corresponding elements are added as possible completions instead of the <i>completion</i> strings from <i>name1</i>. The completion list will retain the descriptions from <i>name1</i>. Finally, a set of completion options can appear. </p>
<p> If the option `<code>-o</code>&#8216; appears before the first argument, the matches added will be treated as names of command options (N.B. not shell options), typically following a `<code>&#8211;</code>&#8216;, `<code>&#8211;</code><code>&#8211;</code>&#8216; or `<code>+</code>&#8216; on the command line. In this case <code>_describe</code> uses the <code>prefix-hidden</code>, <code>prefix-needed</code> and <code>verbose</code> styles to find out if the strings should be added as completions and if the descriptions should be shown. Without the `<code>-o</code>&#8216; option, only the <code>verbose</code> style is used to decide how descriptions are shown. If `<code>-O</code>&#8216; is used instead of `<code>-o</code>&#8216;, command options are completed as above but <code>_describe</code> will not handle the <code>prefix-needed</code> style. </p>
<p> With the <code>-t</code> option a <i>tag</i> can be specified. The default is `<code>values</code>&#8216; or, if the <code>-o</code> option is given, `<code>options</code>&#8216;. </p>
<p> The options <code>-1</code>, <code>-2</code>, <code>-J</code>, <code>-V</code>, <code>-x</code> are passed to <code>_next_label</code>. </p>
<p> If selected by the <code>list-grouped</code> style, strings with the same description will appear together in the list. </p>
<p> <code>_describe</code> uses the <code>_all_labels</code> function to generate the matches, so it does not need to appear inside a loop over tag labels.</dl>
<dt><code>_description</code> [ <code>-x</code> ] [ <code>-12VJ</code> ] <i>tag</i> <i>name</i> <i>descr</i> [ <i>spec</i> &#8230; ]</p>
<dd> This function is not to be confused with the previous one; it is used as a helper function for creating options to <code>compadd</code>. It is buried inside many of the higher level completion functions and so often does not need to be called directly.</p>
<dl>
<dt>
<dd>
<p> The styles listed below are tested in the current context using the given <i>tag</i>. The resulting options for <code>compadd</code> are put into the array named <i>name</i> (this is traditionally `<code>expl</code>&#8216;, but this convention is not enforced). The description for the corresponding set of matches is passed to the function in <i>descr</i>. </p>
<p> The styles tested are: <code>format</code>, <code>hidden</code>, <code>matcher</code>, <code>ignore-line</code>, <code>ignored-patterns</code>, <code>group-name</code> and <code>sort</code>. The <code>format</code> style is first tested for the given <i>tag</i> and then for the <code>descriptions</code> tag if no value was found, while the remainder are only tested for the tag given as the first argument. The function also calls <code>_setup</code> which tests some more styles. </p>
<p> The string returned by the <code>format</code> style (if any) will be modified so that the sequence `<code>%d</code>&#8216; is replaced by the <i>descr</i> given as the third argument without any leading or trailing white space. If, after removing the white space, the <i>descr</i> is the empty string, the format style will not be used and the options put into the <i>name</i> array will not contain an explanation string to be displayed above the matches. </p>
<p> If <code>_description</code> is called with more than three arguments, the additional <i>spec</i>s should be of the form `<i>char</i><code>:</code><i>str</i>&#8216;. These supply escape sequence replacements for the <code>format</code> style: every appearance of `<code>%</code><i>char</i>&#8216; will be replaced by <i>string</i>. </p>
<p> If the <code>-x</code> option is given, the description will be passed to <code>compadd</code> using the <code>-x</code> option instead of the default <code>-X</code>. This means that the description will be displayed even if there are no corresponding matches. </p>
<p> The options placed in the array <i>name</i> take account of the <code>group-name</code> style, so matches are placed in a separate group where necessary. The group normally has its elements sorted (by passing the option <code>-J</code> to <code>compadd</code>), but if an option starting with `<code>-V</code>&#8216;, `<code>-J</code>&#8216;, `<code>-1</code>&#8216;, or `<code>-2</code>&#8216; is passed to <code>_description</code>, that option will be included in the array. Hence it is possible for the completion group to be unsorted by giving the option `<code>-V</code>&#8216;, `<code>-1V</code>&#8216;, or `<code>-2V</code>&#8216;. </p>
<p> In most cases, the function will be used like this: </p>
<dl>
<dt>
<dd>
local expl<br />
        _description files expl file<br />
            compadd &#8220;$expl[@]&#8221; &#8211;<br />
    &#8220;$files[@]&#8221;
</dl>
<p> Note the use of the parameter <code>expl</code>, the hyphen, and the list of matches. Almost all calls to <code>compadd</code> within the completion system use a similar format; this ensures that user-specified styles are correctly passed down to the builtins which implement the internals of completion.</dl>
<dt><code>_dir_list</code> [ <code>-s</code> <i>sep</i> ] [ <code>-S</code> ]</p>
<dd> Complete a list of directory names separated by colons (the same format as <code>$PATH</code>).</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>-s</code> <i>sep</i> Use <i>sep</i> as separator between items. <i>sep</i> defaults to a colon (`<code>:</code>&#8216;).</p>
<dt><code>-S</code></p>
<dd> Add <i>sep</i> instead of slash (`<code>/</code>&#8216;) as an autoremoveable suffix.</dl>
</dl>
<dt><code>_dispatch</code> <i>context string</i> &#8230;</p>
<dd> This sets the current context to <i>context</i> and looks for completion functions to handle this context by hunting through the list of command names or special contexts (as described above for <code>compdef</code>) given as <i>string</i>s. The first completion function to be defined for one of the contexts in the list is used to generate matches. Typically, the last <i>string</i> is <code>-default-</code> to cause the function for default completion to be used as a fallback.</p>
<dl>
<dt>
<dd>
<p> The function sets the parameter <code>$service</code> to the <i>string</i> being tried, and sets the <i>context/command</i> field (the fourth) of the <code>$curcontext</code> parameter to the <i>context</i> given as the first argument.</dl>
<dt><code>_email_addresses</code> [ <code>-c</code> ] [ <code>-n</code> <i>plugin</i> ]</p>
<dd> Complete email addresses. Addresses are provided by plugins.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>-c</code> Complete bare <code>localhost [at] domain.tld</code> addresses, without a name part or a comment. Without this option, RFC822 `<i>Firstname Lastname</i> <code>&lt;</code><i>address</i><code>&gt;</code>&#8216; strings are completed.</p>
<dt><code>-n</code> <i>plugin</i></p>
<dd> Complete aliases from <i>plugin</i>.</dl>
<p> The following plugins are available by default: <code>_email-ldap</code> (see the <code>filter</code> style), <code>_email-local</code> (completes <i>user</i><code>@</code><i>hostname</i> Unix addresses), <code>_email-mail</code> (completes aliases from <code>~/.mailrc</code>), <code>_email-mush</code>, <code>_email-mutt</code>, and <code>_email-pine</code>. </p>
<p> Addresses from the <code>_email-</code><i>foo</i> plugin are added under the tag `<code>email-</code><i>foo</i>&#8216;. </p>
<p> <i>Writing plugins</i> </p>
<p> Plugins are written as separate functions with names starting with `<code>_email-</code>&#8216;. They are invoked with the <code>-c</code> option and <code>compadd</code> options. They should either do their own completion or set the <code>$reply</code> array to a list of `<i>alias</i><code>:</code><i>address</i>&#8216; elements and return <code>300</code>. New plugins will be picked up and run automatically.</dl>
<dt><code>_files</code></p>
<dd> The function <code>_files</code> is a wrapper around <code>_path_files</code>. It supports all of the same functionality, with some enhancements &#8212; notably, it respects the <code>list-dirs-first</code> style, and it allows users to override the behaviour of the <code>-g</code> and <code>-/</code> options with the <code>file-patterns</code> style. <code>_files</code> should therefore be preferred over <code>_path_files</code> in most cases.</p>
<dl>
<dt>
<dd>
<p> This function accepts the full set of options allowed by <code>_path_files</code>, described below.</dl>
<dt><code>_gnu_generic</code></p>
<dd> This function is a simple wrapper around the <code>_arguments</code> function described above. It can be used to determine automatically the long options understood by commands that produce a list when passed the option `<code>&#8211;</code><code>-help</code>&#8216;. It is intended to be used as a top-level completion function in its own right. For example, to enable option completion for the commands <code>foo</code> and <code>bar</code>, use</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>compdef _gnu_generic foo bar</code>
</pre>
</dl>
<p> after the call to <code>compinit</code>. </p>
<p> The completion system as supplied is conservative in its use of this function, since it is important to be sure the command understands the option `<code>&#8211;</code><code>-help</code>&#8216;.</dl>
<dt><code>_guard</code> [ <i>options</i> ] <i>pattern descr</i></p>
<dd> This function displays <i>descr</i> if <i>pattern</i> matches the string to be completed. It is intended to be used in the <i>action</i> for the specifications passed to <code>_arguments</code> and similar functions.</p>
<dl>
<dt>
<dd>
<p> The return status is zero if the message was displayed and the word to complete is not empty, and non-zero otherwise. </p>
<p> The <i>pattern</i> may be preceded by any of the options understood by <code>compadd</code> that are passed down from <code>_description</code>, namely <code>-M</code>, <code>-J</code>, <code>-V</code>, <code>-1</code>, <code>-2</code>, <code>-n</code>, <code>-F</code> and <code>-X</code>. All of these options will be ignored. This fits in conveniently with the argument-passing conventions of actions for <code>_arguments</code>. </p>
<p> As an example, consider a command taking the options <code>-n</code> and <code>-none</code>, where <code>-n</code> must be followed by a numeric value in the same word. By using: </p>
<dl>
<dt>
<dd>
<pre>
<code>_arguments '-n-: :_guard &quot;[0-9]#&quot; &quot;numeric value&quot;' '-none'</code>
</pre>
</dl>
<p> <code>_arguments</code> can be made to both display the message `<code>numeric value</code>&#8216; and complete options after `<code>-n&lt;TAB&gt;</code>&#8216;. If the `<code>-n</code>&#8216; is already followed by one or more digits (the pattern passed to <code>_guard</code>) only the message will be displayed; if the `<code>-n</code>&#8216; is followed by another character, only options are completed.</dl>
<dt>
<dd> <code>_message</code> [ <code>-r12</code> ] [ <code>-VJ</code> <i>group</i> ] <i>descr</i></p>
<dt>
<dd> <code>_message -e</code> [ <i>tag</i> ] <i>descr</i> The <i>descr</i> is used in the same way as the third argument to the <code>_description</code> function, except that the resulting string will always be shown whether or not matches were generated. This is useful for displaying a help message in places where no completions can be generated.</p>
<dl>
<dt>
<dd>
<p> The <code>format</code> style is examined with the <code>messages</code> tag to find a message; the usual tag, <code>descriptions</code>, is used only if the style is not set with the former. </p>
<p> If the <code>-r</code> option is given, no style is used; the <i>descr</i> is taken literally as the string to display. This is most useful when the <i>descr</i> comes from a pre-processed argument list which already contains an expanded description. Note that this option does not disable the `<code>%</code>&#8216;-sequence parsing done by <code>compadd</code>. </p>
<p> The <code>-12VJ</code> options and the <i>group</i> are passed to <code>compadd</code> and hence determine the group the message string is added to. </p>
<p> The second <code>-e</code> form gives a description for completions with the tag <i>tag</i> to be shown even if there are no matches for that tag. This form is called by <code>_arguments</code> in the event that there is no action for an option specification. The tag can be omitted and if so the tag is taken from the parameter <code>$curtag</code>; this is maintained by the completion system and so is usually correct. Note that if there are no matches at the time this function is called, <code>compstate[insert]</code> is cleared, so additional matches generated later are not inserted on the command line.</dl>
<dt><code>_multi_parts</code> [ <code>-i</code> ] <i>sep</i> <i>array</i></p>
<dd> The argument <i>sep</i> is a separator character. The <i>array</i> may be either the name of an array parameter or a literal array in the form `<code>(foo bar</code><code>)</code>&#8216;, a parenthesised list of words separated by whitespace. The possible completions are the strings from the array. However, each chunk delimited by <i>sep</i> will be completed separately. For example, the <code>_tar</code> function uses `<code>_multi_parts</code> <code>/</code> <i>patharray</i>&#8216; to complete partial file paths from the given array of complete file paths.</p>
<dl>
<dt>
<dd>
<p> The <code>-i</code> option causes <code>_multi_parts</code> to insert a unique match even if that requires multiple separators to be inserted. This is not usually the expected behaviour with filenames, but certain other types of completion, for example those with a fixed set of possibilities, may be more suited to this form. </p>
<p> Like other utility functions, this function accepts the `<code>-V</code>&#8216;, `<code>-J</code>&#8216;, `<code>-1</code>&#8216;, `<code>-2</code>&#8216;, `<code>-n</code>&#8216;, `<code>-f</code>&#8216;, `<code>-X</code>&#8216;, `<code>-M</code>&#8216;, `<code>-P</code>&#8216;, `<code>-S</code>&#8216;, `<code>-r</code>&#8216;, `<code>-R</code>&#8216;, and `<code>-q</code>&#8216; options and passes them to the <code>compadd</code> builtin.</dl>
<dt><code>_next_label</code> [ <code>-x</code> ] [ <code>-12VJ</code> ] <i>tag</i> <i>name</i> <i>descr</i> [ <i>option</i> &#8230; ]</p>
<dd> This function is used to implement the loop over different tag labels for a particular tag as described above for the <code>tag-order</code> style. On each call it checks to see if there are any more tag labels; if there is it returns status zero, otherwise non-zero. As this function requires a current tag to be set, it must always follow a call to <code>_tags</code> or <code>_requested</code>.</p>
<dl>
<dt>
<dd>
<p> The <code>-x12VJ</code> options and the first three arguments are passed to the <code>_description</code> function. Where appropriate the <i>tag</i> will be replaced by a tag label in this call. Any description given in the <code>tag-order</code> style is preferred to the <i>descr</i> passed to <code>_next_label</code>. </p>
<p> The <i>option</i>s given after the <i>descr</i> are set in the parameter given by <i>name</i>, and hence are to be passed to <code>compadd</code> or whatever function is called to add the matches. </p>
<p> Here is a typical use of this function for the tag <code>foo</code>. The call to <code>_requested</code> determines if tag <code>foo</code> is required at all; the loop over <code>_next_label</code> handles any labels defined for the tag in the <code>tag-order</code> style. </p>
<dl>
<dt>
<dd>
local expl ret = 1 &#8230; if _requested foo;<br />
then&#8230; while _next_label foo expl &#8216;&#8230;&#8217;;<br />
do<br />
compadd &#8220;$expl[@]&#8221; &#8230; &amp;&amp;ret = 0 done&#8230; fi return ret
</dl>
</dl>
<dt><code>_normal</code> [ <code>-P</code> | <code>-p</code> <i>precommand</i> ]</p>
<dd> This is the standard function called to handle completion outside any special <code>&#8211;</code><i>context</i><code>&#8211;</code>. It is called both to complete the command word and also the arguments for a command. In the second case, <code>_normal</code> looks for a special completion for that command, and if there is none it uses the completion for the <code>-default-</code> context.</p>
<dl>
<dt>
<dd>
<p> A second use is to reexamine the command line specified by the <code>$words</code> array and the <code>$CURRENT</code> parameter after those have been modified. For example, the function <code>_precommand</code>, which completes after precommand specifiers such as <code>nohup</code>, removes the first word from the <code>words</code> array, decrements the <code>CURRENT</code> parameter, then calls `<code>_normal -p $service</code>&#8216;. The effect is that `<code>nohup</code> <i>cmd &#8230;</i>&#8216; is treated in the same way as `<i>cmd &#8230;</i>&#8216;. </p>
<dl>
<dt>
<dd> <code>-P</code> Reset the list of precommands. This option should be used if completing a command line which allows internal commands (e.g. builtins and functions) regardless of prior precommands (e.g. `<code>zsh -c</code>&#8216;).</p>
<dt><code>-p</code> <i>precommand</i></p>
<dd> Append <i>precommand</i> to the list of precommands. This option should be used in nearly all cases in which <code>-P</code> is not applicable.</dl>
<p> If the command name matches one of the patterns given by one of the options <code>-p</code> or <code>-P</code> to <code>compdef</code>, the corresponding completion function is called and then the parameter <code>_compskip</code> is checked. If it is set completion is terminated at that point even if no matches have been found. This is the same effect as in the <code>-first-</code> context.</dl>
<dt><code>_options</code></p>
<dd> This can be used to complete the names of shell options. It provides a matcher specification that ignores a leading `<code>no</code>&#8216;, ignores underscores and allows upper-case letters to match their lower-case counterparts (for example, `<code>glob</code>&#8216;, `<code>noglob</code>&#8216;, `<code>NO_GLOB</code>&#8216; are all completed). Any arguments are propagated to the <code>compadd</code> builtin.</p>
<dt><code>_options_set</code> and <code>_options_unset</code></p>
<dd> These functions complete only set or unset options, with the same matching specification used in the <code>_options</code> function.</p>
<dl>
<dt>
<dd>
<p> Note that you need to uncomment a few lines in the <code>_main_complete</code> function for these functions to work properly. The lines in question are used to store the option settings in effect before the completion widget locally sets the options it needs. Hence these functions are not generally used by the completion system.</dl>
<dt><code>_parameters</code></p>
<dd> This is used to complete the names of shell parameters.</p>
<dl>
<dt>
<dd>
<p> The option `<code>-g</code> <i>pattern</i>&#8216; limits the completion to parameters whose type matches the <i>pattern</i>. The type of a parameter is that shown by `<code>print ${(t)</code><i>param</i><code>}</code>&#8216;, hence judicious use of `<code>*</code>&#8216; in <i>pattern</i> is probably necessary. </p>
<p> All other arguments are passed to the <code>compadd</code> builtin.</dl>
<dt><code>_path_files</code></p>
<dd> This function is used throughout the completion system to complete filenames. It allows completion of partial paths. For example, the string `<code>/u/i/s/sig</code>&#8216; may be completed to `<code>/usr/include/sys/signal.h</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> The options accepted by both <code>_path_files</code> and <code>_files</code> are: </p>
<dl>
<dt>
<dd> <code>-f</code> Complete all filenames. This is the default.</p>
<dt><code>-/</code></p>
<dd> Specifies that only directories should be completed.</p>
<dt><code>-g</code> <i>pattern</i></p>
<dd> Specifies that only files matching the <i>pattern</i> should be completed.</p>
<dt><code>-W</code> <i>paths</i></p>
<dd> Specifies path prefixes that are to be prepended to the string from the command line to generate the filenames but that should not be inserted as completions nor shown in completion listings. Here, <i>paths</i> may be the name of an array parameter, a literal list of paths enclosed in parentheses or an absolute pathname.</p>
<dt><code>-F</code> <i>ignored-files</i></p>
<dd> This behaves as for the corresponding option to the <code>compadd</code> builtin. It gives direct control over which filenames should be ignored. If the option is not present, the <code>ignored-patterns</code> style is used.</dl>
<p> Both <code>_path_files</code> and <code>_files</code> also accept the following options which are passed to <code>compadd</code>: `<code>-J</code>&#8216;, `<code>-V</code>&#8216;, `<code>-1</code>&#8216;, `<code>-2</code>&#8216;, `<code>-n</code>&#8216;, `<code>-X</code>&#8216;, `<code>-M</code>&#8216;, `<code>-P</code>&#8216;, `<code>-S</code>&#8216;, `<code>-q</code>&#8216;, `<code>-r</code>&#8216;, and `<code>-R</code>&#8216;. </p>
<p> Finally, the <code>_path_files</code> function uses the styles <code>expand</code>, <code>ambiguous</code>, <code>special-dirs</code>, <code>list-suffixes</code> and <code>file-sort</code> described above.</dl>
<dt>
<dd> <code>_pick_variant </code>[ <code>-b</code> <i>builtin-label</i> ] [ <code>-c</code> <i>command</i> ] [ <code>-r</code> <i>name</i> ]</p>
<dt>
<dd> <i>label</i><code>=</code><i>pattern</i> &#8230; <i>label</i> [ <i>arg</i> &#8230; ] This function is used to resolve situations where a single command name requires more than one type of handling, either because it has more than one variant or because there is a name clash between two different commands.</p>
<dl>
<dt>
<dd>
<p> The command to run is taken from the first element of the array <code>words</code> unless this is overridden by the option <code>-c</code>. This command is run and its output is compared with a series of patterns. Arguments to be passed to the command can be specified at the end after all the other arguments. The patterns to try in order are given by the arguments <i>label</i><code>=</code><i>pattern</i>; if the output of `<i>command</i> <i>arg</i> &#8230;&#8217; contains <i>pattern</i>, then <i>label</i> is selected as the label for the command variant. If none of the patterns match, the final command label is selected and status 1 is returned. </p>
<p> If the `<code>-b</code> <i>builtin-label</i>&#8216; is given, the command is tested to see if it is provided as a shell builtin, possibly autoloaded; if so, the label <i>builtin-label</i> is selected as the label for the variant. </p>
<p> If the `<code>-r</code> <i>name</i>&#8216; is given, the <i>label</i> picked is stored in the parameter named <i>name</i>. </p>
<p> The results are also cached in the <code>_cmd_variant</code> associative array indexed by the name of the command run.</dl>
<dt><code>_regex_arguments</code> <i>name</i> <i>spec</i> &#8230;</p>
<dd> This function generates a completion function <i>name</i> which matches the specifications <i>spec</i>s, a set of regular expressions as described below. After running <code>_regex_arguments</code>, the function <i>name</i> should be called as a normal completion function. The pattern to be matched is given by the contents of the <code>words</code> array up to the current cursor position joined together with null characters; no quotation is applied.</p>
<dl>
<dt>
<dd>
<p> The arguments are grouped as sets of alternatives separated by `<code>|</code>&#8216;, which are tried one after the other until one matches. Each alternative consists of a one or more specifications which are tried left to right, with each pattern matched being stripped in turn from the command line being tested, until all of the group succeeds or until one fails; in the latter case, the next alternative is tried. This structure can be repeated to arbitrary depth by using parentheses; matching proceeds from inside to outside. </p>
<p> A special procedure is applied if no test succeeds but the remaining command line string contains no null character (implying the remaining word is the one for which completions are to be generated). The completion target is restricted to the remaining word and any <i>action</i>s for the corresponding patterns are executed. In this case, nothing is stripped from the command line string. The order of evaluation of the <i>action</i>s can be determined by the <code>tag-order</code> style; the various formats supported by <code>_alternative</code> can be used in <i>action</i>. The <i>descr</i> is used for setting up the array parameter <code>expl</code>. </p>
<p> Specification arguments take one of following forms, in which metacharacters such as `<code>(</code>&#8216;, `<code>)</code>&#8216;, `<code>#</code>&#8216; and `<code>|</code>&#8216; should be quoted. </p>
<dl>
<dt>
<dd> <code>/</code><i>pattern</i><code>/</code> [<code>%</code><i>lookahead</i><code>%</code>] [<code>&#8211;</code><i>guard</i>] [<code>:</code><i>tag</i><code>:</code><i>descr</i><code>:</code><i>action</i>] This is a single primitive component. The function tests whether the combined pattern `<code>(#b)((#B)</code><i>pattern</i><code>)</code><i>lookahead</i><code>*</code>&#8216; matches the command line string. If so, `<i>guard</i>&#8216; is evaluated and its return status is examined to determine if the test has succeeded. The <i>pattern</i> string `<code>[]</code>&#8216; is guaranteed never to match. The <i>lookahead</i> is not stripped from the command line before the next pattern is examined.</p>
<dl>
<dt>
<dd>
<p> The argument starting with <code>:</code> is used in the same manner as an argument to <code>_alternative</code>. </p>
<p> A component is used as follows: <i>pattern</i> is tested to see if the component already exists on the command line. If it does, any following specifications are examined to find something to complete. If a component is reached but no such pattern exists yet on the command line, the string containing the <i>action</i> is used to generate matches to insert at that point.</dl>
<dt><code>/</code><i>pattern</i><code>/+</code> [<code>%</code><i>lookahead</i><code>%</code>] [<code>&#8211;</code><i>guard</i>] [<code>:</code><i>tag</i><code>:</code><i>descr</i><code>:</code><i>action</i>]</p>
<dd> This is similar to `<code>/</code><i>pattern</i><code>/</code> &#8230;&#8217; but the left part of the command line string (i.e. the part already matched by previous patterns) is also considered part of the completion target.</p>
<dt><code>/</code><i>pattern</i><code>/-</code> [<code>%</code><i>lookahead</i><code>%</code>] [<code>&#8211;</code><i>guard</i>] [<code>:</code><i>tag</i><code>:</code><i>descr</i><code>:</code><i>action</i>]</p>
<dd> This is similar to `<code>/</code><i>pattern</i><code>/</code> &#8230;&#8217; but the <i>action</i>s of the current and previously matched patterns are ignored even if the following `<i>pattern</i>&#8216; matches the empty string.</p>
<dt><code>(</code> <i>spec</i> <code>)</code></p>
<dd> Parentheses may be used to groups <i>spec</i>s; note each parenthesis is a single argument to <code>_regex_arguments</code>.</p>
<dt><i>spec</i> <code>#</code></p>
<dd> This allows any number of repetitions of <i>spec</i>.</p>
<dt><i>spec</i> <i>spec</i></p>
<dd> The two <i>spec</i>s are to be matched one after the other as described above.</p>
<dt><i>spec</i> <code>|</code> <i>spec</i></p>
<dd> Either of the two <i>spec</i>s can be matched.</dl>
<p> The function <code>_regex_words</code> can be used as a helper function to generate matches for a set of alternative words possibly with their own arguments as a command line argument. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
_regex_arguments _tst / $ &#8216;[^
