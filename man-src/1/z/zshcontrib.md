---
title: "zshcontrib(1)"
name: "zshcontrib"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshcontrib/"
description: "zshcontrib – user contributions to zsh"
---

<h2 class="name">NAME</h2>
<p> zshcontrib &#8211; user contributions to zsh </p>
<h2>DESCRIPTION</h2>
<p> The Zsh source distribution includes a number of items contributed by the user community. These are not inherently a part of the shell, and some may not be available in every zsh installation. The most significant of these are documented here. For documentation on other contributed items such as shell functions, look for comments in the function source files. </p>
<h2>UTILITIES</h2>
<h3>Accessing On-Line Help</h3>
<p> The key sequence <code>ESC h</code> is normally bound by ZLE to execute the <code>run-help</code> widget (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)). This invokes the <code>run-help</code> command with the command word from the current input line as its argument. By default, <code>run-help</code> is an alias for the <code>man</code> command, so this often fails when the command word is a shell builtin or a user-defined function. By redefining the <code>run-help</code> alias, one can improve the on-line help provided by the shell. </p>
<p> The <code>helpfiles</code> utility, found in the <code>Util</code> directory of the distribution, is a Perl program that can be used to process the zsh manual to produce a separate help file for each shell builtin and for many other shell features as well. The autoloadable <code>run-help</code> function, found in <code>Functions/Misc</code>, searches for these helpfiles and performs several other tests to produce the most complete help possible for the command. </p>
<p> Help files are installed by default to a subdirectory of <code>/usr/share/zsh</code> or <code>/usr/local/share/zsh</code>. </p>
<p> To create your own help files with <code>helpfiles</code>, choose or create a directory where the individual command help files will reside. For example, you might choose <code>~/zsh_help</code>. If you unpacked the zsh distribution in your home directory, you would use the commands: </p>
<dl>
<dt>
<dd>
<pre>
<code>mkdir ~/zsh_help
perl ~/zsh-5.8/Util/helpfiles ~/zsh_help</code>
</pre>
</dl>
<p> The <code>HELPDIR</code> parameter tells <code>run-help</code> where to look for the help files. When unset, it uses the default installation path. To use your own set of help files, set this to the appropriate path in one of your startup files: </p>
<dl>
<dt>
<dd>
<pre>
<code>HELPDIR=~/zsh_help</code>
</pre>
</dl>
<p> To use the <code>run-help</code> function, you need to add lines something like the following to your <code>.zshrc</code> or equivalent startup file: </p>
<dl>
<dt>
<dd>
<pre>
<code>unalias run-help
autoload run-help</code>
</pre>
</dl>
<p> Note that in order for `<code>autoload run-help</code>&#8216; to work, the <code>run-help</code> file must be in one of the directories named in your <code>fpath</code> array (see <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1)). This should already be the case if you have a standard zsh installation; if it is not, copy <code>Functions/Misc/run-help</code> to an appropriate directory. </p>
<h3>Recompiling Functions</h3>
<p> If you frequently edit your zsh functions, or periodically update your zsh installation to track the latest developments, you may find that function digests compiled with the <code>zcompile</code> builtin are frequently out of date with respect to the function source files. This is not usually a problem, because zsh always looks for the newest file when loading a function, but it may cause slower shell startup and function loading. Also, if a digest file is explicitly used as an element of <code>fpath</code>, zsh won&#8217;t check whether any of its source files has changed. </p>
<p> The <code>zrecompile</code> autoloadable function, found in <code>Functions/Misc</code>, can be used to keep function digests up to date. </p>
<dl>
<dt>
<dd> <code>zrecompile</code> [ <code>-qt</code> ] [ <i>name</i> &#8230; ]</p>
<dt>
<dd> <code>zrecompile</code> [ <code>-qt</code> ] <code>-p</code> <i>arg</i> &#8230; [ <code>&#8211;</code><code>&#8211;</code> <i>arg</i> &#8230; ] This tries to find <code>*.zwc</code> files and automatically re-compile them if at least one of the original files is newer than the compiled file. This works only if the names stored in the compiled files are full paths or are relative to the directory that contains the <code>.zwc</code> file.</p>
<dl>
<dt>
<dd>
<p> In the first form, each <i>name</i> is the name of a compiled file or a directory containing <code>*.zwc</code> files that should be checked. If no arguments are given, the directories and <code>*.zwc</code> files in <code>fpath</code> are used. </p>
<p> When <code>-t</code> is given, no compilation is performed, but a return status of zero (true) is set if there are files that need to be re-compiled and non-zero (false) otherwise. The <code>-q</code> option quiets the chatty output that describes what <code>zrecompile</code> is doing. </p>
<p> Without the <code>-t</code> option, the return status is zero if all files that needed re-compilation could be compiled and non-zero if compilation for at least one of the files failed. </p>
<p> If the <code>-p</code> option is given, the <i>arg</i>s are interpreted as one or more sets of arguments for <code>zcompile</code>, separated by `<code>&#8211;</code><code>&#8211;</code>&#8216;. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zrecompile -p \ 
           -R ~/.zshrc -- \ 
           -M ~/.zcompdump -- \ 
           ~/zsh/comp.zwc ~/zsh/Completion/*/_*</code>
</pre>
</dl>
<p> This compiles <code>~/.zshrc</code> into <code>~/.zshrc.zwc</code> if that doesn&#8217;t exist or if it is older than <code>~/.zshrc</code>. The compiled file will be marked for reading instead of mapping. The same is done for <code>~/.zcompdump</code> and <code>~/.zcompdump.zwc</code>, but this compiled file is marked for mapping. The last line re-creates the file <code>~/zsh/comp.zwc</code> if any of the files matching the given pattern is newer than it. </p>
<p> Without the <code>-p</code> option, <code>zrecompile</code> does not create function digests that do not already exist, nor does it add new functions to the digest.</dl>
</dl>
<p> The following shell loop is an example of a method for creating function digests for all functions in your <code>fpath</code>, assuming that you have write permission to the directories: </p>
<dl>
<dt>
<dd>
<pre><code>
for ((i = 1; i &lt;= $ #fpath; ++i))
    ;
do
  dir=$fpath[i]
  zwc=${dir:t}.zwc
  if [[ $dir == (.|..) || $dir == (.|..)/* ]]; then
    continue
  fi
  files=($dir/*(N-.))
  if [[ -w $dir:h &amp;&amp; -n $files ]]; then
    files=(${${(M)files%/*/*
}
#/
})
    if ( cd $dir:h &amp;&amp;
         zrecompile -p -U -z $zwc $files );
then
    fpath[i] = $fpath[i].zwc
                   fi
                       fi
                           done
</code></pre>
</dl>
<p> The <code>-U</code> and <code>-z</code> options are appropriate for functions in the default zsh installation <code>fpath</code>; you may need to use different options for your personal function directories. </p>
<p> Once the digests have been created and your <code>fpath</code> modified to refer to them, you can keep them up to date by running <code>zrecompile</code> with no arguments. </p>
<h3>Keyboard Definition</h3>
<p> The large number of possible combinations of keyboards, workstations, terminals, emulators, and window systems makes it impossible for zsh to have built-in key bindings for every situation. The <code>zkbd</code> utility, found in <code>Functions/Misc</code>, can help you quickly create key bindings for your configuration. </p>
<p> Run <code>zkbd</code> either as an autoloaded function, or as a shell script: </p>
<dl>
<dt>
<dd>
<pre>
<code>zsh -f ~/zsh-5.8/Functions/Misc/zkbd</code>
</pre>
</dl>
<p> When you run <code>zkbd</code>, it first asks you to enter your terminal type; if the default it offers is correct, just press return. It then asks you to press a number of different keys to determine characteristics of your keyboard and terminal; <code>zkbd</code> warns you if it finds anything out of the ordinary, such as a Delete key that sends neither <code>^H</code> nor <code>^?</code>. </p>
<p> The keystrokes read by <code>zkbd</code> are recorded as a definition for an associative array named <code>key</code>, written to a file in the subdirectory <code>.zkbd</code> within either your <code>HOME</code> or <code>ZDOTDIR</code> directory. The name of the file is composed from the <code>TERM</code>, <code>VENDOR</code> and <code>OSTYPE</code> parameters, joined by hyphens. </p>
<p> You may read this file into your <code>.zshrc</code> or another startup file with the `<code>source</code>&#8216; or `<code>.</code>&#8216; commands, then reference the <code>key</code> parameter in bindkey commands, like this: </p>
<dl>
<dt>
<dd>
source ${ZDOTDIR : -$HOME} /.zkbd / $TERM &#8211; $VENDOR &#8211; $OSTYPE[[-n ${key[Left]}]] &amp;&amp; bindkey &#8220;${key[Left]}&#8221; backward &#8211; char[[-n ${key[Right]}]] &amp;&amp; bindkey &#8220;${key[Right]}&#8221; forward &#8211; char<br />
#etc.
</dl>
<p> Note that in order for `<code>autoload zkbd</code>&#8216; to work, the <code>zkdb</code> file must be in one of the directories named in your <code>fpath</code> array (see <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1)). This should already be the case if you have a standard zsh installation; if it is not, copy <code>Functions/Misc/zkbd</code> to an appropriate directory. </p>
<h3>Dumping Shell State</h3>
<p> Occasionally you may encounter what appears to be a bug in the shell, particularly if you are using a beta version of zsh or a development release. Usually it is sufficient to send a description of the problem to one of the zsh mailing lists (see <i><a href="/docs/linux/man/1-zsh/">zsh</a></i>(1)), but sometimes one of the zsh developers will need to recreate your environment in order to track the problem down. </p>
<p> The script named <code>reporter</code>, found in the <code>Util</code> directory of the distribution, is provided for this purpose. (It is also possible to <code>autoload reporter</code>, but <code>reporter</code> is not installed in <code>fpath</code> by default.) This script outputs a detailed dump of the shell state, in the form of another script that can be read with `<code>zsh -f</code>&#8216; to recreate that state. </p>
<p> To use <code>reporter</code>, read the script into your shell with the `<code>.</code>&#8216; command and redirect the output into a file: </p>
<dl>
<dt>
<dd>
<pre>
<code>. ~/zsh-5.8/Util/reporter &gt; zsh.report</code>
</pre>
</dl>
<p> You should check the <code>zsh.report</code> file for any sensitive information such as passwords and delete them by hand before sending the script to the developers. Also, as the output can be voluminous, it&#8217;s best to wait for the developers to ask for this information before sending it. </p>
<p> You can also use <code>reporter</code> to dump only a subset of the shell state. This is sometimes useful for creating startup files for the first time. Most of the output from reporter is far more detailed than usually is necessary for a startup file, but the <code>aliases</code>, <code>options</code>, and <code>zstyles</code> states may be useful because they include only changes from the defaults. The <code>bindings</code> state may be useful if you have created any of your own keymaps, because <code>reporter</code> arranges to dump the keymap creation commands as well as the bindings for every keymap. </p>
<p> As is usual with automated tools, if you create a startup file with <code>reporter</code>, you should edit the results to remove unnecessary commands. Note that if you&#8217;re using the new completion system, you should <i>not</i> dump the <code>functions</code> state to your startup files with <code>reporter</code>; use the <code>compdump</code> function instead (see <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1)). </p>
<dl>
<dt>
<dd> <code>reporter</code> [ <i>state</i> &#8230; ] Print to standard output the indicated subset of the current shell state. The <i>state</i> arguments may be one or more of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>all</code></p>
<dd> Output everything listed below.</p>
<dt><code>aliases</code></p>
<dd> Output alias definitions.</p>
<dt><code>bindings</code></p>
<dd> Output ZLE key maps and bindings.</p>
<dt><code>completion</code></p>
<dd> Output old-style <code>compctl</code> commands. New completion is covered by <code>functions</code> and <code>zstyles</code>.</p>
<dt><code>functions</code></p>
<dd> Output autoloads and function definitions.</p>
<dt><code>limits</code></p>
<dd> Output <code>limit</code> commands.</p>
<dt><code>options</code></p>
<dd> Output <code>setopt</code> commands.</p>
<dt><code>styles</code></p>
<dd> Same as <code>zstyles</code>.</p>
<dt><code>variables</code></p>
<dd> Output shell parameter assignments, plus <code>export</code> commands for any environment variables.</p>
<dt><code>zstyles</code></p>
<dd> Output <code>zstyle</code> commands.</dl>
<p> If the <i>state</i> is omitted, <code>all</code> is assumed.</dl>
</dl>
<p> With the exception of `<code>all</code>&#8216;, every <i>state</i> can be abbreviated by any prefix, even a single letter; thus <code>a</code> is the same as <code>aliases</code>, <code>z</code> is the same as <code>zstyles</code>, etc. </p>
<h3>Manipulating Hook Functions</h3>
<dl>
<dt>
<dd> <code>add-zsh-hook</code> [ <code>-L</code> | <code>-dD</code> ] [ <code>-Uzk</code> ] <i>hook</i> <i>function</i> Several functions are special to the shell, as described in the section SPECIAL FUNCTIONS, see <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1), in that they are automatically called at specific points during shell execution. Each has an associated array consisting of names of functions to be called at the same point; these are so-called `hook functions&#8217;. The shell function <code>add-zsh-hook</code> provides a simple way of adding or removing functions from the array.</p>
<dl>
<dt>
<dd>
<p> <i>hook</i> is one of <code>chpwd</code>, <code>periodic</code>, <code>precmd</code>, <code>preexec</code>, <code>zshaddhistory</code>, <code>zshexit</code>, or <code>zsh_directory_name</code>, the special functions in question. Note that <code>zsh_directory_name</code> is called in a different way from the other functions, but may still be manipulated as a hook. </p>
<p> <i>function</i> is name of an ordinary shell function. If no options are given this will be added to the array of functions to be executed in the given context. Functions are invoked in the order they were added. </p>
<p> If the option <code>-L</code> is given, the current values for the hook arrays are listed with <code>typeset</code>. </p>
<p> If the option <code>-d</code> is given, the <i>function</i> is removed from the array of functions to be executed. </p>
<p> If the option <code>-D</code> is given, the <i>function</i> is treated as a pattern and any matching names of functions are removed from the array of functions to be executed. </p>
<p> The options <code>-U</code>, <code>-z</code> and <code>-k</code> are passed as arguments to <code>autoload</code> for <i>function</i>. For functions contributed with zsh, the options <code>-Uz</code> are appropriate.</dl>
<dt><code>add-zle-hook-widget</code> [ <code>-L</code> | <code>-dD</code> ] [ <code>-Uzk</code> ] <i>hook</i> <i>widgetname</i></p>
<dd> Several widget names are special to the line editor, as described in the section Special Widgets, see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1), in that they are automatically called at specific points during editing. Unlike function hooks, these do not use a predefined array of other names to call at the same point; the shell function <code>add-zle-hook-widget</code> maintains a similar array and arranges for the special widget to invoke those additional widgets.</p>
<dl>
<dt>
<dd>
<p> <i>hook</i> is one of <code>isearch-exit</code>, <code>isearch-update</code>, <code>line-pre-redraw</code>, <code>line-init</code>, <code>line-finish</code>, <code>history-line-set</code>, or <code>keymap-select</code>, corresponding to each of the special widgets <code>zle-isearch-exit</code>, etc. The special widget names are also accepted as the <i>hook</i> argument. </p>
<p> <i>widgetname</i> is the name of a ZLE widget. If no options are given this is added to the array of widgets to be invoked in the given hook context. Widgets are invoked in the order they were added, with</p>
<dl>
<dt>
<dd>
<pre>
<code>zle </code><i>widgetname</i><code> -Nw -- &quot;$@&quot;</code>
</pre>
</dl>
<p> Note that this means that the `<code>WIDGET</code>&#8216; special parameter tracks the <i>widgetname</i> when the widget function is called, rather than tracking the name of the corresponding special hook widget. </p>
<p> If the option <code>-d</code> is given, the <i>widgetname</i> is removed from the array of widgets to be executed. </p>
<p> If the option <code>-D</code> is given, the <i>widgetname</i> is treated as a pattern and any matching names of widgets are removed from the array. </p>
<p> If <i>widgetname</i> does not name an existing widget when added to the array, it is assumed that a shell function also named <i>widgetname</i> is meant to provide the implementation of the widget. This name is therefore marked for autoloading, and the options <code>-U</code>, <code>-z</code> and <code>-k</code> are passed as arguments to <code>autoload</code> as with <code>add-zsh-hook</code>. The widget is also created with `<code>zle -N </code><i>widgetname</i>&#8216; to cause the corresponding function to be loaded the first time the hook is called. </p>
<p> The arrays of <i>widgetname</i> are currently maintained in <code>zstyle</code> contexts, one for each <i>hook</i> context, with a style of `<code>widgets</code>&#8216;. If the <code>-L</code> option is given, this set of styles is listed with `<code>zstyle -L</code>&#8216;. This implementation may change, and the special widgets that refer to the styles are created only if <code>add-zle-hook-widget</code> is called to add at least one widget, so if this function is used for any hooks, then all hooks should be managed only via this function.</dl>
</dl>
<h2>REMEMBERING RECENT DIRECTORIES</h2>
<p> The function <code>cdr</code> allows you to change the working directory to a previous working directory from a list maintained automatically. It is similar in concept to the directory stack controlled by the <code>pushd</code>, <code>popd</code> and <code>dirs</code> builtins, but is more configurable, and as it stores all entries in files it is maintained across sessions and (by default) between terminal emulators in the current session. Duplicates are automatically removed, so that the list reflects the single most recent use of each directory. </p>
<p> Note that the <code>pushd</code> directory stack is not actually modified or used by <code>cdr</code> unless you configure it to do so as described in the configuration section below. </p>
<h3>Installation</h3>
<p> The system works by means of a hook function that is called every time the directory changes. To install the system, autoload the required functions and use the <code>add-zsh-hook</code> function described above: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -Uz chpwd_recent_dirs cdr add-zsh-hook
add-zsh-hook chpwd chpwd_recent_dirs</code>
</pre>
</dl>
<p> Now every time you change directly interactively, no matter which command you use, the directory to which you change will be remembered in most-recent-first order. </p>
<h3>Use</h3>
<p> All direct user interaction is via the <code>cdr</code> function. </p>
<p> The argument to cdr is a number <i>N</i> corresponding to the <i>N</i>th most recently changed-to directory. 1 is the immediately preceding directory; the current directory is remembered but is not offered as a destination. Note that if you have multiple windows open 1 may refer to a directory changed to in another window; you can avoid this by having per-terminal files for storing directory as described for the <code>recent-dirs-file</code> style below. </p>
<p> If you set the <code>recent-dirs-default</code> style described below <code>cdr</code> will behave the same as <code>cd</code> if given a non-numeric argument, or more than one argument. The recent directory list is updated just the same however you change directory. </p>
<p> If the argument is omitted, 1 is assumed. This is similar to <code>pushd</code>&#8216;s behaviour of swapping the two most recent directories on the stack. </p>
<p> Completion for the argument to <code>cdr</code> is available if compinit has been run; menu selection is recommended, using: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*:*:cdr:*:*' menu selection</code>
</pre>
</dl>
<p> to allow you to cycle through recent directories; the order is preserved, so the first choice is the most recent directory before the current one. The verbose style is also recommended to ensure the directory is shown; this style is on by default so no action is required unless you have changed it. </p>
<h3>Options</h3>
<p> The behaviour of <code>cdr</code> may be modified by the following options. </p>
<dl>
<dt>
<dd> <code>-l</code> lists the numbers and the corresponding directories in abbreviated form (i.e. with <code>~</code> substitution reapplied), one per line. The directories here are not quoted (this would only be an issue if a directory name contained a newline). This is used by the completion system.</p>
<dt><code>-r</code></p>
<dd> sets the variable <code>reply</code> to the current set of directories. Nothing is printed and the directory is not changed.</p>
<dt><code>-e</code></p>
<dd> allows you to edit the list of directories, one per line. The list can be edited to any extent you like; no sanity checking is performed. Completion is available. No quoting is necessary (except for newlines, where I have in any case no sympathy); directories are in unabbreviated from and contain an absolute path, i.e. they start with <code>/</code>. Usually the first entry should be left as the current directory.</p>
<dt><code>-p &#8216;</code><i>pattern</i><code>&#8216;</code></p>
<dd> Prunes any items in the directory list that match the given extended glob pattern; the pattern needs to be quoted from immediate expansion on the command line. The pattern is matched against each completely expanded file name in the list; the full string must match, so wildcards at the end (e.g. <code>&#8216;*removeme*&#8217;</code>) are needed to remove entries with a given substring.</p>
<dl>
<dt>
<dd>
<p> If output is to a terminal, then the function will print the new list after pruning and prompt for confirmation by the user. This output and confirmation step can be skipped by using <code>-P</code> instead of <code>-p</code>.</dl>
</dl>
<h3>Configuration</h3>
<p> Configuration is by means of the styles mechanism that should be familiar from completion; if not, see the description of the <code>zstyle</code> command in see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). The context for setting styles should be <code>&#8216;:chpwd:*&#8217;</code> in case the meaning of the context is extended in future, for example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':chpwd:*' recent-dirs-max 0</code>
</pre>
</dl>
<p> sets the value of the <code>recent-dirs-max</code> style to 0. In practice the style name is specific enough that a context of &#8216;*&#8217; should be fine. </p>
<p> An exception is <code>recent-dirs-insert</code>, which is used exclusively by the completion system and so has the usual completion system context (<code>&#8216;:completion:*&#8217;</code> if nothing more specific is needed), though again <code>&#8216;*&#8217;</code> should be fine in practice. </p>
<dl>
<dt>
<dd> <code>recent-dirs-default</code> If true, and the command is expecting a recent directory index, and either there is more than one argument or the argument is not an integer, then fall through to &quot;cd&quot;. This allows the lazy to use only one command for directory changing. Completion recognises this, too; see recent-dirs-insert for how to control completion when this option is in use.</p>
<dt><code>recent-dirs-file</code></p>
<dd> The file where the list of directories is saved. The default is <code>${ZDOTDIR:-$HOME}/.chpwd-recent-dirs</code>, i.e. this is in your home directory unless you have set the variable <code>ZDOTDIR</code> to point somewhere else. Directory names are saved in <code>$&#8217;</code><i>&#8230;</i><code>&#8216;</code> quoted form, so each line in the file can be supplied directly to the shell as an argument.</p>
<dl>
<dt>
<dd>
<p> The value of this style may be an array. In this case, the first file in the list will always be used for saving directories while any other files are left untouched. When reading the recent directory list, if there are fewer than the maximum number of entries in the first file, the contents of later files in the array will be appended with duplicates removed from the list shown. The contents of the two files are not sorted together, i.e. all the entries in the first file are shown first. The special value <code>+</code> can appear in the list to indicate the default file should be read at that point. This allows effects like the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':chpwd:*' recent-dirs-file \ 
~/.chpwd-recent-dirs-${TTY##*/} +</code>
</pre>
</dl>
<p> Recent directories are read from a file numbered according to the terminal. If there are insufficient entries the list is supplemented from the default file. </p>
<p> It is possible to use <code>zstyle -e</code> to make the directory configurable at run time: </p>
<dl>
<dt>
<dd>
zstyle &#8211; e &#8216;:chpwd:*&#8217; recent &#8211; dirs &#8211; file pick &#8211; recent &#8211; dirs &#8211; file pick &#8211; recent &#8211; dirs &#8211; file()<br />
{<br />
    if [[ $PWD = ~/text/writing(|/*) ]]; then<br />
    reply=(~/.chpwd-recent-dirs-writing)<br />
  else<br />
    reply=(+)<br />
  fi<br />
}
</dl>
<p> In this example, if the current directory is <code>~/text/writing</code> or a directory under it, then use a special file for saving recent directories, else use the default.</dl>
<dt><code>recent-dirs-insert</code></p>
<dd> Used by completion. If <code>recent-dirs-default</code> is true, then setting this to <code>true</code> causes the actual directory, rather than its index, to be inserted on the command line; this has the same effect as using the corresponding index, but makes the history clearer and the line easier to edit. With this setting, if part of an argument was already typed, normal directory completion rather than recent directory completion is done; this is because recent directory completion is expected to be done by cycling through entries menu fashion.</p>
<dl>
<dt>
<dd>
<p> If the value of the style is <code>always</code>, then only recent directories will be completed; in that case, use the <code>cd</code> command when you want to complete other directories. </p>
<p> If the value is <code>fallback</code>, recent directories will be tried first, then normal directory completion is performed if recent directory completion failed to find a match. </p>
<p> Finally, if the value is <code>both</code> then both sets of completions are presented; the usual tag mechanism can be used to distinguish results, with recent directories tagged as <code>recent-dirs</code>. Note that the recent directories inserted are abbreviated with directory names where appropriate.</dl>
<dt><code>recent-dirs-max</code></p>
<dd> The maximum number of directories to save to the file. If this is zero or negative there is no maximum. The default is 20. Note this includes the current directory, which isn&#8217;t offered, so the highest number of directories you will be offered is one less than the maximum.</p>
<dt><code>recent-dirs-prune</code></p>
<dd> This style is an array determining what directories should (or should not) be added to the recent list. Elements of the array can include:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>parent</code> Prune parents (more accurately, ancestors) from the recent list. If present, changing directly down by any number of directories causes the current directory to be overwritten. For example, changing from ~pws to ~pws/some/other/dir causes ~pws not to be left on the recent directory stack. This only applies to direct changes to descendant directories; earlier directories on the list are not pruned. For example, changing from ~pws/yet/another to ~pws/some/other/dir does not cause ~pws to be pruned.</p>
<dt><code>pattern:</code><i>pattern</i></p>
<dd> Gives a zsh pattern for directories that should not be added to the recent list (if not already there). This element can be repeated to add different patterns. For example, <code>&#8216;pattern:/tmp(|/*)&#8217;</code> stops <code>/tmp</code> or its descendants from being added. The <code>EXTENDED_GLOB</code> option is always turned on for these patterns.</dl>
</dl>
<dt><code>recent-dirs-pushd</code></p>
<dd> If set to true, <code>cdr</code> will use <code>pushd</code> instead of <code>cd</code> to change the directory, so the directory is saved on the directory stack. As the directory stack is completely separate from the list of files saved by the mechanism used in this file there is no obvious reason to do this.</dl>
<h3>Use with dynamic directory naming</h3>
<p> It is possible to refer to recent directories using the dynamic directory name syntax by using the supplied function <code>zsh_directory_name_cdr</code> a hook: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -Uz add-zsh-hook
add-zsh-hook -Uz zsh_directory_name zsh_directory_name_cdr</code>
</pre>
</dl>
<p> When this is done, <code>~[1]</code> will refer to the most recent directory other than $PWD, and so on. Completion after <code>~[</code><i>&#8230;</i> also works. </p>
<h3>Details of directory handling</h3>
<p> This section is for the curious or confused; most users will not need to know this information. </p>
<p> Recent directories are saved to a file immediately and hence are preserved across sessions. Note currently no file locking is applied: the list is updated immediately on interactive commands and nowhere else (unlike history), and it is assumed you are only going to change directory in one window at once. This is not safe on shared accounts, but in any case the system has limited utility when someone else is changing to a different set of directories behind your back. </p>
<p> To make this a little safer, only directory changes instituted from the command line, either directly or indirectly through shell function calls (but not through subshells, evals, traps, completion functions and the like) are saved. Shell functions should use <code>cd -q</code> or <code>pushd -q</code> to avoid side effects if the change to the directory is to be invisible at the command line. See the contents of the function <code>chpwd_recent_dirs</code> for more details. </p>
<h2>ABBREVIATED DYNAMIC REFERENCES TO DIRECTORIES</h2>
<p> The dynamic directory naming system is described in the subsection <i>Dynamic named directories</i> of the section <i>Filename Expansion</i> in <i><a href="/docs/linux/man/1-expn/">expn</a></i>(1). In this, a reference to <code>~[</code><i>&#8230;</i><code>]</code> is expanded by a function found by the hooks mechanism. </p>
<p> The contributed function <code>zsh_directory_name_generic</code> provides a system allowing the user to refer to directories with only a limited amount of new code. It supports all three of the standard interfaces for directory naming: converting from a name to a directory, converting in the reverse direction to find a short name, and completion of names. </p>
<p> The main feature of this function is a path-like syntax, combining abbreviations at multiple levels separated by &quot;:&quot;. As an example, ~[g:p:s] might specify:</p>
<dl>
<dt>
<dd> <code>g</code> The top level directory for your git area. This first component has to match, or the function will return indicating another directory name hook function should be tried.</p>
<dt><code>p</code></p>
<dd> The name of a project within your git area.</p>
<dt><code>s</code></p>
<dd> The source area within that project. This allows you to collapse references to long hierarchies to a very compact form, particularly if the hierarchies are similar across different areas of the disk.</dl>
<p> Name components may be completed: if a description is shown at the top of the list of completions, it includes the path to which previous components expand, while the description for an individual completion shows the path segment it would add. No additional configuration is needed for this as the completion system is aware of the dynamic directory name mechanism. </p>
<h3>Usage</h3>
<p> To use the function, first define a wrapper function for your specific case. We&#8217;ll assume it&#8217;s to be autoloaded. This can have any name but we&#8217;ll refer to it as zdn_mywrapper. This wrapper function will define various variables and then call this function with the same arguments that the wrapper function gets. This configuration is described below. </p>
<p> Then arrange for the wrapper to be run as a zsh_directory_name hook: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -Uz add-zsh-hook zsh_diretory_name_generic zdn_mywrapper
add-zsh-hook -U zsh_directory_name zdn_mywrapper</code>
</pre>
</dl>
<h3>Configuration</h3>
<p> The wrapper function should define a local associative array zdn_top. Alternatively, this can be set with a style called <code>mapping</code>. The context for the style is <code>:zdn:</code><i>wrapper-name</i> where <i>wrapper-name</i> is the function calling zsh_directory_name_generic; for example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle :zdn:zdn_mywrapper: mapping zdn_mywrapper_top</code>
</pre>
</dl>
<p> The keys in this associative array correspond to the first component of the name. The values are matching directories. They may have an optional suffix with a slash followed by a colon and the name of a variable in the same format to give the next component. (The slash before the colon is to disambiguate the case where a colon is needed in the path for a drive. There is otherwise no syntax for escaping this, so path components whose names start with a colon are not supported.) A special component <code>:default:</code> specifies a variable in the form <code>/:</code><i>var</i> (the path section is ignored and so is usually empty) that will be used for the next component if no variable is given for the path. Variables referred to within <code>zdn_top</code> have the same format as <code>zdn_top</code> itself, but contain relative paths. </p>
<p> For example, </p>
<dl>
<dt>
<dd>
<pre>
<code>local -A zdn_top=(
  g   ~/git
  ga  ~/alternate/git
  gs  /scratch/$USER/git/:second2
  :default: /:second1
)</code>
</pre>
</dl>
<p> This specifies the behaviour of a directory referred to as <code>~[g:&#8230;]</code> or <code>~[ga:&#8230;]</code> or <code>~[gs:&#8230;]</code>. Later path components are optional; in that case <code>~[g]</code> expands to <code>~/git</code>, and so on. <code>gs</code> expands to <code>/scratch/$USER/git</code> and uses the associative array <code>second2</code> to match the second component; <code>g</code> and <code>ga</code> use the associative array <code>second1</code> to match the second component. </p>
<p> When expanding a name to a directory, if the first component is not <code>g</code> or <code>ga</code> or <code>gs</code>, it is not an error; the function simply returns 1 so that a later hook function can be tried. However, matching the first component commits the function, so if a later component does not match, an error is printed (though this still does not stop later hooks from being executed). </p>
<p> For components after the first, a relative path is expected, but note that multiple levels may still appear. Here is an example of <code>second1</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>local -A second1=(
  p   myproject
  s   somproject
  os  otherproject/subproject/:third
)</code>
</pre>
</dl>
<p> The path as found from <code>zdn_top</code> is extended with the matching directory, so <code>~[g:p]</code> becomes <code>~/git/myproject</code>. The slash between is added automatically (it&#8217;s not possible to have a later component modify the name of a directory already matched). Only <code>os</code> specifies a variable for a third component, and there&#8217;s no <code>:default:</code>, so it&#8217;s an error to use a name like <code>~[g:p:x]</code> or <code>~[ga:s:y]</code> because there&#8217;s nowhere to look up the <code>x</code> or <code>y</code>. </p>
<p> The associative arrays need to be visible within this function; the generic function therefore uses internal variable names beginning <code>_zdn_</code> in order to avoid clashes. Note that the variable <code>reply</code> needs to be passed back to the shell, so should not be local in the calling function. </p>
<p> The function does not test whether directories assembled by component actually exist; this allows the system to work across automounted file systems. The error from the command trying to use a non-existent directory should be sufficient to indicate the problem. </p>
<h3>Complete example</h3>
<p> Here is a full fictitious but usable autoloadable definition of the example function defined by the code above. So <code>~[gs:p:s]</code> expands to <code>/scratch/$USER/git/myscratchproject/top/srcdir</code> (with <code>$USER</code> also expanded). </p>
<dl>
<dt>
<dd>
<pre>
<code>local -A zdn_top=(
  g   ~/git
  ga  ~/alternate/git
  gs  /scratch/$USER/git/:second2
  :default: /:second1
)
local -A second1=(
  p   myproject
  s   somproject
  os  otherproject/subproject/:third
)
local -A second2=(
  p   myscratchproject
  s   somescratchproject
)
local -A third=(
  s   top/srcdir
  d   top/documentation
)
# autoload not needed if you did this at initialisation...
autoload -Uz zsh_directory_name_generic
zsh_directory_name_generic &quot;$@</code>
</pre>
</dl>
<p> It is also possible to use global associative arrays, suitably named, and set the style for the context of your wrapper function to refer to this. Then your set up code would contain the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>typeset -A zdn_mywrapper_top=(...)
# ... and so on for other associative arrays ...
zstyle ':zdn:zdn_mywrapper:' mapping zdn_mywrapper_top
autoload -Uz add-zsh-hook zsh_directory_name_generic zdn_mywrapper
add-zsh-hook -U zsh_directory_name zdn_mywrapper</code>
</pre>
</dl>
<p> and the function <code>zdn_mywrapper</code> would contain only the following: </p>
<dl>
<dt>
<dd>
<pre>
<code>zsh_directory_name_generic &quot;$@&quot;</code>
</pre>
</dl>
<h2>GATHERING INFORMATION FROM VERSION CONTROL SYSTEMS</h2>
<p> In a lot of cases, it is nice to automatically retrieve information from version control systems (VCSs), such as subversion, CVS or git, to be able to provide it to the user; possibly in the user&#8217;s prompt. So that you can instantly tell which branch you are currently on, for example. </p>
<p> In order to do that, you may use the <code>vcs_info</code> function. </p>
<p> The following VCSs are supported, showing the abbreviated name by which they are referred to within the system:</p>
<dl>
<dt>Bazaar (<code>bzr</code>)</p>
<dd> <code><a rel="nofollow" href="https://bazaar.canonical.com/">https://bazaar.canonical.com/</a></code></p>
<dt>Codeville (<code>cdv</code>)</p>
<dd> <code><a rel="nofollow" href="http://freecode.com/projects/codeville/">http://freecode.com/projects/codeville/</a></code></p>
<dt>Concurrent Versioning System (<code>cvs</code>)</p>
<dd> <code><a rel="nofollow" href="https://www.nongnu.org/cvs/">https://www.nongnu.org/cvs/</a></code></p>
<dt>Darcs (<code>darcs</code>)</p>
<dd> <code><a rel="nofollow" href="http://darcs.net/">http://darcs.net/</a></code></p>
<dt>Fossil (<code>fossil</code>)</p>
<dd> <code><a rel="nofollow" href="https://fossil-scm.org/">https://fossil-scm.org/</a></code></p>
<dt>Git (<code>git</code>)</p>
<dd> <code><a rel="nofollow" href="https://git-scm.com/">https://git-scm.com/</a></code></p>
<dt>GNU arch (<code>tla</code>)</p>
<dd> <code><a rel="nofollow" href="https://www.gnu.org/software/gnu-arch/">https://www.gnu.org/software/gnu-arch/</a></code></p>
<dt>Mercurial (<code>hg</code>)</p>
<dd> <code><a rel="nofollow" href="https://www.mercurial-scm.org/">https://www.mercurial-scm.org/</a></code></p>
<dt>Monotone (<code>mtn</code>)</p>
<dd> <code><a rel="nofollow" href="https://monotone.ca/">https://monotone.ca/</a></code></p>
<dt>Perforce (<code>p4</code>)</p>
<dd> <code><a rel="nofollow" href="https://www.perforce.com/">https://www.perforce.com/</a></code></p>
<dt>Subversion (<code>svn</code>)</p>
<dd> <code><a rel="nofollow" href="https://subversion.apache.org/">https://subversion.apache.org/</a></code></p>
<dt>SVK (<code>svk</code>)</p>
<dd> <code><a rel="nofollow" href="https://svk.bestpractical.com/">https://svk.bestpractical.com/</a></code></dl>
<p> There is also support for the patch management system <code>quilt</code> (<code><a rel="nofollow" href="https://savannah.nongnu.org/projects/quilt">https://savannah.nongnu.org/projects/quilt</a></code>). See <code>Quilt Support</code> below for details. </p>
<p> To load <code>vcs_info</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -Uz vcs_info</code>
</pre>
</dl>
<p> It can be used in any existing prompt, because it does not require any specific <code>$psvar</code> entries to be available. </p>
<h3>Quickstart</h3>
<p> To get this feature working quickly (including colors), you can do the following (assuming, you loaded <code>vcs_info</code> properly &#8211; see above): </p>
<dl>
<dt>
<dd>
zstyle &#8216;:vcs_info:*&#8217; actionformats \<br />
    &#8216;%F{5}(%f%s%F{5})%F{3}-%F{5}[%F{2}%b%F{3}|%F{1}%a%F{5}]%f &#8216; zstyle &#8216;:vcs_info:*&#8217; formats       \<br />
    &#8216;%F{5}(%f%s%F{5})%F{3}-%F{5}[%F{2}%b%F{5}]%f &#8216; zstyle &#8216;:vcs_info:(sv[nk]|bzr):*&#8217; branchformat &#8216;%b%F{1}:%F{3}%r&#8217; precmd(){vcs_info} PS1 = &#8216;%F{5}[%F{2}%n%F{5}] %F{3}%3~ ${vcs_info_msg_0_}%f%# &#8216;
</dl>
<p> Obviously, the last two lines are there for demonstration. You need to call <code>vcs_info</code> from your <code>precmd</code> function. Once that is done you need a <i>single quoted</i> <code>&#8216;${vcs_info_msg_0_}&#8217;</code> in your prompt. </p>
<p> To be able to use <code>&#8216;${vcs_info_msg_0_}&#8217;</code> directly in your prompt like this, you will need to have the <code>PROMPT_SUBST</code> option enabled. </p>
<p> Now call the <code>vcs_info_printsys</code> utility from the command line: </p>
<dl>
<dt>
<dd>
% vcs_info_printsys##list of supported version control backends :##disabled systems are prefixed by a hash sign(#)<br />
                                                                     bzr<br />
                                                                 cdv<br />
                                                                 cvs<br />
                                                                 darcs<br />
                                                                 fossil<br />
                                                                 git<br />
                                                                 hg<br />
                                                                 mtn<br />
                                                                 p4<br />
                                                                 svk<br />
                                                                 svn<br />
                                                                 tla<br />
                                                                 ##flavours(cannot be used in the enable or disable styles; they##are enabled and disabled with their master[git &#8211; svn-&gt;git])##they *can *be used in contexts : &#8216;:vcs_info:git-svn:*&#8217;.git<br />
    &#8211; p4 git &#8211; svn hg &#8211; git hg &#8211; hgsubversion hg &#8211; hgsvn
</dl>
<p> You may not want all of these because there is no point in running the code to detect systems you do not use. So there is a way to disable some backends altogether: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*' disable bzr cdv darcs mtn svk tla</code>
</pre>
</dl>
<p> You may also pick a few from that list and enable only those: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*' enable git cvs svn</code>
</pre>
</dl>
<p> If you rerun <code>vcs_info_printsys</code> after one of these commands, you will see the backends listed in the <code>disable</code> style (or backends not in the <code>enable</code> style &#8211; if you used that) marked as disabled by a hash sign. That means the detection of these systems is skipped <i>completely</i>. No wasted time there. </p>
<h3>Configuration</h3>
<p> The <code>vcs_info</code> feature can be configured via <code>zstyle</code>. </p>
<p> First, the context in which we are working:</p>
<dl>
<dt>
<dd>
<pre>
<code>:vcs_info:</code><i>vcs-string</i>:<i>user-context</i>:<i>repo-root-name</i>
</pre>
</dl>
<dl>
<dt>
<dd> <i>vcs-string</i> is one of: <code>git</code>, <code>git-svn</code>, <code>git-p4</code>, <code>hg</code>, <code>hg-git</code>, <code>hg-hgsubversion</code>, <code>hg-hgsvn</code>, <code>darcs</code>, <code>bzr</code>, <code>cdv</code>, <code>mtn</code>, <code>svn</code>, <code>cvs</code>, <code>svk</code>, <code>tla</code>, <code>p4</code> or <code>fossil</code>. This is followed by `<code>.quilt-</code><i>quilt-mode</i>&#8216; in Quilt mode (see <code>Quilt Support</code> for details) and by `<code>+</code><i>hook-name</i>&#8216; while hooks are active (see <code>Hooks in vcs_info</code> for details).</p>
<dl>
<dt>
<dd>
<p> Currently, hooks in quilt mode don&#8217;t add the `<code>.quilt-</code><i>quilt-mode</i>&#8216; information. This may change in the future.</dl>
<dt><i>user-context</i></p>
<dd> is a freely configurable string, assignable by the user as the first argument to <code>vcs_info</code> (see its description below).</p>
<dt><i>repo-root-name</i></p>
<dd> is the name of a repository in which you want a style to match. So, if you want a setting specific to <code>/usr/src/zsh</code>, with that being a CVS checkout, you can set <i>repo-root-name</i> to <code>zsh</code> to make it so.</dl>
<p> There are three special values for <i>vcs-string</i>: The first is named <code>-init-</code>, that is in effect as long as there was no decision what VCS backend to use. The second is <code>-preinit-</code>; it is used <i>before</i> <code>vcs_info</code> is run, when initializing the data exporting variables. The third special value is <code>formats</code> and is used by the <code>vcs_info_lastmsg</code> for looking up its styles. </p>
<p> The initial value of <i>repo-root-name</i> is <code>-all-</code> and it is replaced with the actual name, as soon as it is known. Only use this part of the context for defining the <code>formats</code>, <code>actionformats</code> or <code>branchformat</code> styles, as it is guaranteed that <i>repo-root-name</i> is set up correctly for these only. For all other styles, just use <code>&#8216;*&#8217;</code> instead. </p>
<p> There are two pre-defined values for <i>user-context</i>:</p>
<dl>
<dt><code>default</code></p>
<dd> the one used if none is specified</p>
<dt><code>command</code></p>
<dd> used by vcs_info_lastmsg to lookup its styles</dl>
<p> You can of course use <code>&#8216;:vcs_info:*&#8217;</code> to match all VCSs in all user-contexts at once. </p>
<p> This is a description of all styles that are looked up. </p>
<dl>
<dt>
<dd> <code>formats</code> A list of formats, used when actionformats is not used (which is most of the time).</p>
<dt><code>actionformats</code></p>
<dd> A list of formats, used if there is a special action going on in your current repository; like an interactive rebase or a merge conflict.</p>
<dt><code>branchformat</code></p>
<dd> Some backends replace <code>%b</code> in the formats and actionformats styles above, not only by a branch name but also by a revision number. This style lets you modify how that string should look.</p>
<dt><code>nvcsformats</code></p>
<dd> These &quot;formats&quot; are set when we didn&#8217;t detect a version control system for the current directory or <code>vcs_info</code> was disabled. This is useful if you want <code>vcs_info</code> to completely take over the generation of your prompt. You would do something like <code>PS1=&#8217;${vcs_info_msg_0_}&#8217;</code> to accomplish that.</p>
<dt><code>hgrevformat</code></p>
<dd> <code>hg</code> uses both a hash and a revision number to reference a specific changeset in a repository. With this style you can format the revision string (see <code>branchformat</code>) to include either or both. It&#8217;s only useful when <code>get-revision</code> is true. Note, the full 40-character revision id is not available (except when using the <code>use-simple</code> option) because executing hg more than once per prompt is too slow; you may customize this behavior using hooks.</p>
<dt><code>max-exports</code></p>
<dd> Defines the maximum number of <code>vcs_info_msg_*_</code> variables <code>vcs_info</code> will set.</p>
<dt><code>enable</code></p>
<dd> A list of backends you want to use. Checked in the <code>-init-</code> context. If this list contains an item called <code>NONE</code> no backend is used at all and <code>vcs_info</code> will do nothing. If this list contains <code>ALL</code>, <code>vcs_info</code> will use all known backends. Only with <code>ALL</code> in <code>enable</code> will the <code>disable</code> style have any effect. <code>ALL</code> and <code>NONE</code> are case insensitive.</p>
<dt><code>disable</code></p>
<dd> A list of VCSs you don&#8217;t want <code>vcs_info</code> to test for repositories (checked in the <code>-init-</code> context, too). Only used if <code>enable</code> contains <code>ALL</code>.</p>
<dt><code>disable-patterns</code></p>
<dd> A list of patterns that are checked against <code>$PWD</code>. If a pattern matches, <code>vcs_info</code> will be disabled. This style is checked in the <code>:vcs_info:-init-:*:-all-</code> context.</p>
<dl>
<dt>
<dd>
<p> Say, <code>~/.zsh</code> is a directory under version control, in which you do not want <code>vcs_info</code> to be active, do:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*' disable-patterns &quot;${(b)HOME}/.zsh(|/*)&quot;</code>
</pre>
</dl>
</dl>
<dt><code>use-quilt</code></p>
<dd> If enabled, the <code>quilt</code> support code is active in `addon&#8217; mode. See <code>Quilt Support</code> for details.</p>
<dt><code>quilt-standalone</code></p>
<dd> If enabled, `standalone&#8217; mode detection is attempted if no VCS is active in a given directory. See <code>Quilt Support</code> for details.</p>
<dt><code>quilt-patch-dir</code></p>
<dd> Overwrite the value of the <code>$QUILT_PATCHES</code> environment variable. See <code>Quilt Support</code> for details.</p>
<dt><code>quiltcommand</code></p>
<dd> When <code>quilt</code> itself is called in quilt support, the value of this style is used as the command name.</p>
<dt><code>check-for-changes</code></p>
<dd> If enabled, this style causes the <code>%c</code> and <code>%u</code> format escapes to show when the working directory has uncommitted changes. The strings displayed by these escapes can be controlled via the <code>stagedstr</code> and <code>unstagedstr</code> styles. The only backends that currently support this option are <code>git</code>, <code>hg</code>, and <code>bzr</code> (the latter two only support unstaged).</p>
<dl>
<dt>
<dd>
<p> For this style to be evaluated with the <code>hg</code> backend, the <code>get-revision</code> style needs to be set and the <code>use-simple</code> style needs to be unset. The latter is the default; the former is not. </p>
<p> With the <code>bzr</code> backend, <i>lightweight checkouts</i> only honor this style if the <code>use-server</code> style is set. </p>
<p> Note, the actions taken if this style is enabled are potentially expensive (read: they may be slow, depending on how big the current repository is). Therefore, it is disabled by default.</dl>
<dt><code>check-for-staged-changes</code></p>
<dd> This style is like <code>check-for-changes</code>, but it never checks the worktree files, only the metadata in the <code>.${vcs}</code> dir. Therefore, this style initializes only the <code>%c</code> escape (with <code>stagedstr</code>) but not the <code>%u</code> escape. This style is faster than <code>check-for-changes</code>.</p>
<dl>
<dt>
<dd>
<p> In the <code>git</code> backend, this style checks for changes in the index. Other backends do not currently implement this style. </p>
<p> This style is disabled by default.</dl>
<dt><code>stagedstr</code></p>
<dd> This string will be used in the <code>%c</code> escape if there are staged changes in the repository.</p>
<dt><code>unstagedstr</code></p>
<dd> This string will be used in the <code>%u</code> escape if there are unstaged changes in the repository.</p>
<dt><code>command</code></p>
<dd> This style causes <code>vcs_info</code> to use the supplied string as the command to use as the VCS&#8217;s binary. Note, that setting this in &#8216;<code>:vcs_info:*</code>&#8216; is not a good idea.</p>
<dl>
<dt>
<dd>
<p> If the value of this style is empty (which is the default), the used binary name is the name of the backend in use (e.g. <code>svn</code> is used in an <code>svn</code> repository). </p>
<p> The <code>repo-root-name</code> part in the context is always the default <code>-all-</code> when this style is looked up. </p>
<p> For example, this style can be used to use binaries from non-default installation directories. Assume, <code>git</code> is installed in /usr/bin but your sysadmin installed a newer version in /usr/local/bin. Instead of changing the order of your <code>$PATH</code> parameter, you can do this:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:git:*:-all-' command /usr/local/bin/git</code>
</pre>
</dl>
</dl>
<dt><code>use-server</code></p>
<dd> This is used by the Perforce backend (<code>p4</code>) to decide if it should contact the Perforce server to find out if a directory is managed by Perforce. This is the only reliable way of doing this, but runs the risk of a delay if the server name cannot be found. If the server (more specifically, the <code>host</code><code>:</code><code>port</code> pair describing the server) cannot be contacted, its name is put into the associative array <code>vcs_info_p4_dead_servers</code> and is not contacted again during the session until it is removed by hand. If you do not set this style, the <code>p4</code> backend is only usable if you have set the environment variable <code>P4CONFIG</code> to a file name and have corresponding files in the root directories of each Perforce client. See comments in the function <code>VCS_INFO_detect_p4</code> for more detail.</p>
<dl>
<dt>
<dd>
<p> The Bazaar backend (<code>bzr</code>) uses this to permit contacting the server about lightweight checkouts, see the <code>check-for-changes</code> style.</dl>
<dt><code>use-simple</code></p>
<dd> If there are two different ways of gathering information, you can select the simpler one by setting this style to true; the default is to use the not-that-simple code, which is potentially a lot slower but might be more accurate in all possible cases. This style is used by the <code>bzr</code> and <code>hg</code> backends. In the case of <code>hg</code> it will invoke the external hexdump program to parse the binary dirstate cache file; this method will not return the local revision number.</p>
<dt><code>get-revision</code></p>
<dd> If set to true, vcs_info goes the extra mile to figure out the revision of a repository&#8217;s work tree (currently for the <code>git</code> and <code>hg</code> backends, where this kind of information is not always vital). For <code>git</code>, the hash value of the currently checked out commit is available via the <code>%i</code> expansion. With <code>hg</code>, the local revision number and the corresponding global hash are available via <code>%i</code>.</p>
<dt><code>get-mq</code></p>
<dd> If set to true, the <code>hg</code> backend will look for a Mercurial Queue (<code>mq</code>) patch directory. Information will be available via the `<code>%m</code>&#8216; replacement.</p>
<dt><code>get-bookmarks</code></p>
<dd> If set to true, the <code>hg</code> backend will try to get a list of current bookmarks. They will be available via the `<code>%m</code>&#8216; replacement.</p>
<dl>
<dt>
<dd>
<p> The default is to generate a comma-separated list of all bookmark names that refer to the currently checked out revision. If a bookmark is active, its name is suffixed an asterisk and placed first in the list.</dl>
<dt><code>use-prompt-escapes</code></p>
<dd> Determines if we assume that the assembled string from <code>vcs_info</code> includes prompt escapes. (Used by <code>vcs_info_lastmsg</code>.)</p>
<dt><code>debug</code></p>
<dd> Enable debugging output to track possible problems. Currently this style is only used by <code>vcs_info</code>&#8216;s hooks system.</p>
<dt><code>hooks</code></p>
<dd> A list style that defines hook-function names. See <code>Hooks in vcs_info</code> below for details.</p>
<dt>
<dd> <code>patch-format</code></p>
<dt>
<dd> <code>nopatch-format</code> This pair of styles format the patch information used by the <code>%m</code> expando in formats and actionformats for the <code>git</code> and <code>hg</code> backends. The value is subject to certain <code>%</code>-expansions described below. The expanded value is made available in the global <code>backend_misc</code> array as <code>${backend_misc[patches]}</code> (also if a <code>set-patch-format</code> hook is used).</p>
<dt><code>get-unapplied</code></p>
<dd> This boolean style controls whether a backend should attempt to gather a list of unapplied patches (for example with Mercurial Queue patches).</p>
<dl>
<dt>
<dd>
<p> Used by the <code>quilt</code> and <code>hg</code> backends.</dl>
</dl>
<p> The default values for these styles in all contexts are: </p>
<dl>
<dt><code>formats</code></p>
<dd> &quot; (%s)-[%b]%u%c-&quot;</p>
<dt><code>actionformats</code></p>
<dd> &quot; (%s)-[%b|%a]%u%c-&quot;</p>
<dt><code>branchformat</code></p>
<dd> &quot;%b:%r&quot; (for bzr, svn, svk and hg)</p>
<dt><code>nvcsformats</code></p>
<dd> &quot;&quot;</p>
<dt><code>hgrevformat</code></p>
<dd> &quot;%r:%h&quot;</p>
<dt><code>max-exports</code></p>
<dd> 2</p>
<dt><code>enable</code></p>
<dd> ALL</p>
<dt><code>disable</code></p>
<dd> (empty list)</p>
<dt><code>disable-patterns</code></p>
<dd> (empty list)</p>
<dt><code>check-for-changes</code></p>
<dd> false</p>
<dt><code>check-for-staged-changes</code></p>
<dd> false</p>
<dt><code>stagedstr</code></p>
<dd> (string: &quot;S&quot;)</p>
<dt><code>unstagedstr</code></p>
<dd> (string: &quot;U&quot;)</p>
<dt><code>command</code></p>
<dd> (empty string)</p>
<dt><code>use-server</code></p>
<dd> false</p>
<dt><code>use-simple</code></p>
<dd> false</p>
<dt><code>get-revision</code></p>
<dd> false</p>
<dt><code>get-mq</code></p>
<dd> true</p>
<dt><code>get-bookmarks</code></p>
<dd> false</p>
<dt><code>use-prompt-escapes</code></p>
<dd> true</p>
<dt><code>debug</code></p>
<dd> false</p>
<dt><code>hooks</code></p>
<dd> (empty list)</p>
<dt><code>use-quilt</code></p>
<dd> false</p>
<dt><code>quilt-standalone</code></p>
<dd> false</p>
<dt><code>quilt-patch-dir</code></p>
<dd> empty &#8211; use <code>$QUILT_PATCHES</code></p>
<dt><code>quiltcommand</code></p>
<dd> quilt</p>
<dt><code>patch-format</code></p>
<dd> <i>backend dependent</i></p>
<dt><code>nopatch-format</code></p>
<dd> <i>backend dependent</i></p>
<dt><code>get-unapplied</code></p>
<dd> false</dl>
<p> In normal <code>formats</code> and <code>actionformats</code> the following replacements are done: </p>
<dl>
<dt><code>%s</code></p>
<dd> The VCS in use (git, hg, svn, etc.).</p>
<dt><code>%b</code></p>
<dd> Information about the current branch.</p>
<dt><code>%a</code></p>
<dd> An identifier that describes the action. Only makes sense in <code>actionformats</code>.</p>
<dt><code>%i</code></p>
<dd> The current revision number or identifier. For <code>hg</code> the <code>hgrevformat</code> style may be used to customize the output.</p>
<dt><code>%c</code></p>
<dd> The string from the <code>stagedstr</code> style if there are staged changes in the repository.</p>
<dt><code>%u</code></p>
<dd> The string from the <code>unstagedstr</code> style if there are unstaged changes in the repository.</p>
<dt><code>%R</code></p>
<dd> The base directory of the repository.</p>
<dt><code>%r</code></p>
<dd> The repository name. If <code>%R</code> is <code>/foo/bar/repoXY</code>, <code>%r</code> is <code>repoXY</code>.</p>
<dt><code>%S</code></p>
<dd> A subdirectory within a repository. If <code>$PWD</code> is <code>/foo/bar/repoXY/beer/tasty</code>, <code>%S</code> is <code>beer/tasty</code>.</p>
<dt>
<dd> <code>%m</code> A &quot;misc&quot; replacement. It is at the discretion of the backend to decide what this replacement expands to.</p>
<dl>
<dt>
<dd>
<p> The <code>hg</code> and <code>git</code> backends use this expando to display patch information. <code>hg</code> sources patch information from the <code>mq</code> extensions; <code>git</code> from in-progress <code>rebase</code> and <code>cherry-pick</code> operations and from the <code>stgit</code> extension. The <code>patch-format</code> and <code>nopatch-format</code> styles control the generated string. The former is used when at least one patch from the patch queue has been applied, and the latter otherwise. </p>
<p> The <code>hg</code> backend displays bookmark information in this expando (in addition to <code>mq</code> information). See the <code>get-mq</code> and <code>get-bookmarks</code> styles. Both of these styles may be enabled at the same time. If both are enabled, both resulting strings will be shown separated by a semicolon (that cannot currently be customized). </p>
<p> The <code>quilt</code> `standalone&#8217; backend sets this expando to the same value as the <code>%Q</code> expando.</dl>
<dt><code>%Q</code></p>
<dd> Quilt series information. When quilt is used (either in `addon&#8217; mode or as a `standalone&#8217; backend), this expando is set to quilt series&#8217; <code>patch-format</code> string. The <code>set-patch-format</code> hook and <code>nopatch-format</code> style are honoured.</p>
<dl>
<dt>
<dd>
<p> See <code>Quilt Support</code> below for details.</dl>
</dl>
<p> In <code>branchformat</code> these replacements are done: </p>
<dl>
<dt><code>%b</code></p>
<dd> The branch name.</p>
<dt><code>%r</code></p>
<dd> The current revision number or the <code>hgrevformat</code> style for <code>hg</code>.</dl>
<p> In <code>hgrevformat</code> these replacements are done: </p>
<dl>
<dt><code>%r</code></p>
<dd> The current local revision number.</p>
<dt><code>%h</code></p>
<dd> The current global revision identifier.</dl>
<p> In <code>patch-format</code> and <code>nopatch-format</code> these replacements are done: </p>
<dl>
<dt><code>%p</code></p>
<dd> The name of the top-most applied patch; may be overridden by the <code>applied-string</code> hook.</p>
<dt><code>%u</code></p>
<dd> The number of unapplied patches; may be overridden by the <code>unapplied-string</code> hook.</p>
<dt><code>%n</code></p>
<dd> The number of applied patches.</p>
<dt><code>%c</code></p>
<dd> The number of unapplied patches.</p>
<dt><code>%a</code></p>
<dd> The number of all patches (<code>%a = %n + %c</code>).</p>
<dt><code>%g</code></p>
<dd> The names of active <code>mq</code> guards (<code>hg</code> backend).</p>
<dt><code>%G</code></p>
<dd> The number of active <code>mq</code> guards (<code>hg</code> backend).</dl>
<p> Not all VCS backends have to support all replacements. For <code>nvcsformats</code> no replacements are performed at all, it is just a string. </p>
<h3>Oddities</h3>
<p> If you want to use the <code>%b</code> (bold off) prompt expansion in <code>formats</code>, which expands <code>%b</code> itself, use <code>%%b</code>. That will cause the <code>vcs_info</code> expansion to replace <code>%%b</code> with <code>%b</code>, so that zsh&#8217;s prompt expansion mechanism can handle it. Similarly, to hand down <code>%b</code> from <code>branchformat</code>, use <code>%%%%b</code>. Sorry for this inconvenience, but it cannot be easily avoided. Luckily we do not clash with a lot of prompt expansions and this only needs to be done for those. </p>
<p> When one of the <code>gen-applied-string</code>, <code>gen-unapplied-string</code>, and <code>set-patch-format</code> hooks is defined, applying <code>%</code>-escaping (`<code>foo=${foo//&#8217;%&#8217;/%%}</code>&#8216;) to the interpolated values for use in the prompt is the responsibility of those hooks (jointly); when neither of those hooks is defined, <code>vcs_info</code> handles escaping by itself. We regret this coupling, but it was required for backwards compatibility. </p>
<h3>Quilt Support</h3>
<p> <code>Quilt</code> is not a version control system, therefore this is not implemented as a backend. It can help keeping track of a series of patches. People use it to keep a set of changes they want to use on top of software packages (which is tightly integrated into the package build process &#8211; the Debian project does this for a large number of packages). Quilt can also help individual developers keep track of their own patches on top of real version control systems. </p>
<p> The <code>vcs_info</code> integration tries to support both ways of using quilt by having two slightly different modes of operation: `addon&#8217; mode and `standalone&#8217; mode). </p>
<p> Quilt integration is off by default; to enable it, set the <code>use-quilt</code> style, and add <code>%Q</code> to your <code>formats</code> or <code>actionformats</code> style:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*' use-quilt true</code>
</pre>
</dl>
<p> Styles looked up from the Quilt support code include `<code>.quilt-</code><i>quilt-mode</i>&#8216; in the <i>vcs-string</i> part of the context, where <i>quilt-mode</i> is either <code>addon</code> or <code>standalone</code>. Example: <code>:vcs_info:git.quilt-addon:default:</code><i>repo-root-name</i>. </p>
<p> For `addon&#8217; mode to become active <code>vcs_info</code> must have already detected a real version control system controlling the directory. If that is the case, a directory that holds quilt&#8217;s patches needs to be found. That directory is configurable via the `<code>QUILT_PATCHES</code>&#8216; environment variable. If that variable exists its value is used, otherwise the value `<code>patches</code>&#8216; is assumed. The value from <code>$QUILT_PATCHES</code> can be overwritten using the `<code>quilt-patches</code>&#8216; style. (Note: you can use <code>vcs_info</code> to keep the value of <code>$QUILT_PATCHES</code> correct all the time via the <code>post-quilt</code> hook). </p>
<p> When the directory in question is found, quilt is assumed to be active. To gather more information, <code>vcs_info</code> looks for a directory called `.pc&#8217;; Quilt uses that directory to track its current state. If this directory does not exist we know that quilt has not done anything to the working directory (read: no patches have been applied yet). </p>
<p> If patches are applied, <code>vcs_info</code> will try to find out which. If you want to know which patches of a series are not yet applied, you need to activate the <code>get-unapplied</code> style in the appropriate context. </p>
<p> <code>vcs_info</code> allows for very detailed control over how the gathered information is presented (see the <code>Configuration</code> and <code>Hooks in vcs_info</code> sections), all of which are documented below. Note there are a number of other patch tracking systems that work on top of a certain version control system (like <code>stgit</code> for <code>git</code>, or <code>mq</code> for <code>hg</code>); the configuration for systems like that are generally configured the same way as the <code>quilt</code> support. </p>
<p> If the <code>quilt</code> support is working in `addon&#8217; mode, the produced string is available as a simple format replacement (<code>%Q</code> to be precise), which can be used in <code>formats</code> and <code>actionformats</code>; see below for details). </p>
<p> If, on the other hand, the support code is working in `standalone&#8217; mode, <code>vcs_info</code> will pretend as if <code>quilt</code> were an actual version control system. That means that the version control system identifier (which otherwise would be something like `svn&#8217; or `cvs&#8217;) will be set to `<code>-quilt-</code>&#8216;. This has implications on the used style context where this identifier is the second element. <code>vcs_info</code> will have filled in a proper value for the &quot;repository&#8217;s&quot; root directory and the string containing the information about quilt&#8217;s state will be available as the `misc&#8217; replacement (and <code>%Q</code> for compatibility with `addon&#8217; mode). </p>
<p> What is left to discuss is how `standalone&#8217; mode is detected. The detection itself is a series of searches for directories. You can have this detection enabled all the time in every directory that is not otherwise under version control. If you know there is only a limited set of trees where you would like <code>vcs_info</code> to try and look for Quilt in `standalone&#8217; mode to minimise the amount of searching on every call to <code>vcs_info</code>, there are a number of ways to do that: </p>
<p> Essentially, `standalone&#8217; mode detection is controlled by a style called `<code>quilt-standalone</code>&#8216;. It is a string style and its value can have different effects. The simplest values are: `<code>always</code>&#8216; to run detection every time <code>vcs_info</code> is run, and `<code>never</code>&#8216; to turn the detection off entirely. </p>
<p> If the value of <code>quilt-standalone</code> is something else, it is interpreted differently. If the value is the name of a scalar variable the value of that variable is checked and that value is used in the same `always&#8217;/`never&#8217; way as described above. </p>
<p> If the value of <code>quilt-standalone</code> is an array, the elements of that array are used as directory names under which you want the detection to be active. </p>
<p> If <code>quilt-standalone</code> is an associative array, the keys are taken as directory names under which you want the detection to be active, but only if the corresponding value is the string `<code>true</code>&#8216;. </p>
<p> Last, but not least, if the value of <code>quilt-standalone</code> is the name of a function, the function is called without arguments and the return value decides whether detection should be active. A `0&#8242; return value is true; a non-zero return value is interpreted as false. </p>
<p> Note, if there is both a function and a variable by the name of <code>quilt-standalone</code>, the function will take precedence. </p>
<h3>Function Descriptions (Public API)</h3>
<dl>
<dt>
<dd> <code>vcs_info</code> [<i>user-context</i>] The main function, that runs all backends and assembles all data into <code>${vcs_info_msg_*_}</code>. This is the function you want to call from <code>precmd</code> if you want to include up-to-date information in your prompt (see <code>Variable Description</code> below). If an argument is given, that string will be used instead of <code>default</code> in the <i>user-context</i> field of the style context.</p>
<dt><code>vcs_info_hookadd</code></p>
<dd> Statically registers a number of functions to a given hook. The hook needs to be given as the first argument; what follows is a list of hook-function names to register to the hook. The `<code>+vi-</code>&#8216; prefix needs to be left out here. See <code>Hooks in vcs_info</code> below for details.</p>
<dt><code>vcs_info_hookdel</code></p>
<dd> Remove hook-functions from a given hook. The hook needs to be given as the first non-option argument; what follows is a list of hook-function names to un-register from the hook. If `<code>-a</code>&#8216; is used as the first argument, <code>all</code> occurrences of the functions are unregistered. Otherwise only the last occurrence is removed (if a function was registered to a hook more than once). The `<code>+vi-</code>&#8216; prefix needs to be left out here. See <code>Hooks in vcs_info</code> below for details.</p>
<dt><code>vcs_info_lastmsg</code></p>
<dd> Outputs the last <code>${vcs_info_msg_*_}</code> value. Takes into account the value of the <code>use-prompt-escapes</code> style in <code>&#8216;:vcs_info:formats:command:-all-&#8216;</code>. It also only prints <code>max-exports</code> values.</p>
<dt><code>vcs_info_printsys</code> [<i>user-context</i>]</p>
<dd> Prints a list of all supported version control systems. Useful to find out possible contexts (and which of them are enabled) or values for the <code>disable</code> style.</p>
<dt><code>vcs_info_setsys</code></p>
<dd> Initializes <code>vcs_info</code>&#8216;s internal list of available backends. With this function, you can add support for new VCSs without restarting the shell.</dl>
<p> All functions named <code>VCS_INFO_*</code> are for internal use only. </p>
<h3>Variable Description</h3>
<dl>
<dt>
<dd> <code>${vcs_info_msg_</code><i>N</i><code>_}</code> (Note the trailing underscore) Where <i>N</i> is an integer, e.g., <code>vcs_info_msg_0_</code>. These variables are the storage for the informational message the last <code>vcs_info</code> call has assembled. These are strongly connected to the <code>formats</code>, <code>actionformats</code> and <code>nvcsformats</code> styles described above. Those styles are lists. The first member of that list gets expanded into <code>${vcs_info_msg_0_}</code>, the second into <code>${vcs_info_msg_1_}</code> and the Nth into <code>${vcs_info_msg_N-1_}</code>. (See the <code>max-exports</code> style above.)</dl>
<p> All variables named <code>VCS_INFO_*</code> are for internal use only. </p>
<h3>Hooks in vcs_info</h3>
<p> Hooks are places in <code>vcs_info</code> where you can run your own code. That code can communicate with the code that called it and through that, change the system&#8217;s behaviour. </p>
<p> For configuration, hooks change the style context:</p>
<dl>
<dt>
<dd>
<pre>
<code>:vcs_info:</code><i>vcs-string</i>+<i>hook-name</i>:<i>user-context</i>:<i>repo-root-name</i>
</pre>
</dl>
<p> To register functions to a hook, you need to list them in the <code>hooks</code> style in the appropriate context. </p>
<p> Example:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*+foo:*' hooks bar baz</code>
</pre>
</dl>
<p> This registers functions to the hook `foo&#8217; for all backends. In order to avoid namespace problems, all registered function names are prepended by a `<code>+vi-</code>&#8216;, so the actual functions called for the `foo&#8217; hook are `<code>+vi-bar</code>&#8216; and `<code>+vi-baz</code>&#8216;. </p>
<p> If you would like to register a function to a hook regardless of the current context, you may use the <code>vcs_info_hookadd</code> function. To remove a function that was added like that, the <code>vcs_info_hookdel</code> function can be used. </p>
<p> If something seems weird, you can enable the `debug&#8217; boolean style in the proper context and the hook-calling code will print what it tried to execute and whether the function in question existed. </p>
<p> When you register more than one function to a hook, all functions are executed one after another until one function returns non-zero or until all functions have been called. Context-sensitive hook functions are executed <code>before</code> statically registered ones (the ones added by <code>vcs_info_hookadd</code>). </p>
<p> You may pass data between functions via an associative array, <code>user_data</code>. For example:</p>
<dl>
<dt>
<dd>
+ vi &#8211; git &#8211; myfirsthook()<br />
{<br />
    user_data[myval] = $myval<br />
}<br />
+ vi &#8211; git &#8211; mysecondhook()<br />
{<br />
#do something with $ { user_data[myval] }<br />
}
</dl>
<p> There are a number of variables that are special in hook contexts: </p>
<dl>
<dt>
<dd> <code>ret</code> The return value that the hooks system will return to the caller. The default is an integer `zero&#8217;. If and how a changed <code>ret</code> value changes the execution of the caller depends on the specific hook. See the hook documentation below for details.</p>
<dt><code>hook_com</code></p>
<dd> An associated array which is used for bidirectional communication from the caller to hook functions. The used keys depend on the specific hook.</p>
<dt><code>context</code></p>
<dd> The active context of the hook. Functions that wish to change this variable should make it local scope first.</p>
<dt><code>vcs</code></p>
<dd> The current VCS after it was detected. The same values as in the enable/disable style are used. Available in all hooks except <code>start-up</code>.</dl>
<p> Finally, the full list of currently available hooks: </p>
<dl>
<dt>
<dd> <code>start-up</code> Called after starting <code>vcs_info</code> but before the VCS in this directory is determined. It can be used to deactivate <code>vcs_info</code> temporarily if necessary. When <code>ret</code> is set to <code>1</code>, <code>vcs_info</code> aborts and does nothing; when set to <code>2</code>, <code>vcs_info</code> sets up everything as if no version control were active and exits.</p>
<dt><code>pre-get-data</code></p>
<dd> Same as <code>start-up</code> but after the VCS was detected.</p>
<dt><code>gen-hg-bookmark-string</code></p>
<dd> Called in the Mercurial backend when a bookmark string is generated; the <code>get-revision</code> and <code>get-bookmarks</code> styles must be true.</p>
<dl>
<dt>
<dd>
<p> This hook gets the names of the Mercurial bookmarks that <code>vcs_info</code> collected from `hg&#8217;. </p>
<p> If a bookmark is active, the key <code>${hook_com[hg-active-bookmark]}</code> is set to its name. The key is otherwise unset. </p>
<p> When setting <code>ret</code> to non-zero, the string in <code>${hook_com[hg-bookmark-string]}</code> will be used in the <code>%m</code> escape in <code>formats</code> and <code>actionformats</code> and will be available in the global <code>backend_misc</code> array as <code>${backend_misc[bookmarks]}</code>.</dl>
<dt><code>gen-applied-string</code></p>
<dd> Called in the <code>git</code> (with <code>stgit</code> or during rebase or merge), and <code>hg</code> (with <code>mq</code>) backends and in <code>quilt</code> support when the <code>applied-string</code> is generated; the <code>use-quilt</code> zstyle must be true for <code>quilt</code> (the <code>mq</code> and <code>stgit</code> backends are active by default).</p>
<dl>
<dt>
<dd>
<p> This hook gets the names of all applied patches which <code>vcs_info</code> collected so far in the opposite order, which means that the first argument is the top-most patch and so forth. </p>
<p> When setting <code>ret</code> to non-zero, the string in <code>${hook_com[applied-string]}</code> will be available as <code>%p</code> in the <code>patch-format</code> and <code>nopatch-format</code> styles. This hook is, in concert with <code>set-patch-format</code>, responsible for <code>%</code>-escaping that value for use in the prompt. (See the <code>Oddities</code> section.)</dl>
<dt><code>gen-unapplied-string</code></p>
<dd> Called in the <code>git</code> (with <code>stgit</code> or during rebase), and <code>hg</code> (with <code>mq</code>) backend and in <code>quilt</code> support when the <code>unapplied-string</code> is generated; the <code>get-unapplied</code> style must be true.</p>
<dl>
<dt>
<dd>
<p> This hook gets the names of all unapplied patches which <code>vcs_info</code> collected so far in order, which means that the first argument is the patch next-in-line to be applied and so forth. </p>
<p> When setting <code>ret</code> to non-zero, the string in <code>${hook_com[unapplied-string]}</code> will be available as <code>%u</code> in the <code>patch-format</code> and <code>nopatch-format</code> styles. This hook is, in concert with <code>set-patch-format</code>, responsible for <code>%</code>-escaping that value for use in the prompt. (See the <code>Oddities</code> section.)</dl>
<dt><code>gen-mqguards-string</code></p>
<dd> Called in the <code>hg</code> backend when <code>guards-string</code> is generated; the <code>get-mq</code> style must be true (default).</p>
<dl>
<dt>
<dd>
<p> This hook gets the names of any active <code>mq</code> guards. </p>
<p> When setting <code>ret</code> to non-zero, the string in <code>${hook_com[guards-string]}</code> will be used in the <code>%g</code> escape in the <code>patch-format</code> and <code>nopatch-format</code> styles.</dl>
<dt><code>no-vcs</code></p>
<dd> This hooks is called when no version control system was detected.</p>
<dl>
<dt>
<dd>
<p> The `<code>hook_com</code>&#8216; parameter is not used.</dl>
<dt><code>post-backend</code></p>
<dd> Called as soon as the backend has finished collecting information.</p>
<dl>
<dt>
<dd>
<p> The `<code>hook_com</code>&#8216; keys available are as for the <code>set-message</code> hook.</dl>
<dt><code>post-quilt</code></p>
<dd> Called after the <code>quilt</code> support is done. The following information is passed as arguments to the hook: 1. the quilt-support mode (`addon&#8217; or `standalone&#8217;); 2. the directory that contains the patch series; 3. the directory that holds quilt&#8217;s status information (the `.pc&#8217; directory) or the string <code>&quot;-nopc-&quot;</code> if that directory wasn&#8217;t found.</p>
<dl>
<dt>
<dd>
<p> The `hook_com&#8217; parameter is not used.</dl>
<dt><code>set-branch-format</code></p>
<dd> Called before `<code>branchformat</code>&#8216; is set. The only argument to the hook is the format that is configured at this point.</p>
<dl>
<dt>
<dd>
<p> The `<code>hook_com</code>&#8216; keys considered are `<code>branch</code>&#8216; and `<code>revision</code>&#8216;. They are set to the values figured out so far by <code>vcs_info</code> and any change will be used directly when the actual replacement is done. </p>
<p> If <code>ret</code> is set to non-zero, the string in <code>${hook_com[branch-replace]}</code> will be used unchanged as the `<code>%b</code>&#8216; replacement in the variables set by <code>vcs_info</code>.</dl>
<dt><code>set-hgrev-format</code></p>
<dd> Called before a `<code>hgrevformat</code>&#8216; is set. The only argument to the hook is the format that is configured at this point.</p>
<dl>
<dt>
<dd>
<p> The `<code>hook_com</code>&#8216; keys considered are `<code>hash</code>&#8216; and `<code>localrev</code>&#8216;. They are set to the values figured out so far by <code>vcs_info</code> and any change will be used directly when the actual replacement is done. </p>
<p> If <code>ret</code> is set to non-zero, the string in <code>${hook_com[rev-replace]}</code> will be used unchanged as the `<code>%i</code>&#8216; replacement in the variables set by <code>vcs_info</code>.</dl>
<dt><code>pre-addon-quilt</code></p>
<dd> This hook is used when <code>vcs_info</code>&#8216;s quilt functionality is active in &quot;addon&quot; mode (quilt used on top of a real version control system). It is activated right before any quilt specific action is taken.</p>
<dl>
<dt>
<dd>
<p> Setting the `<code>ret</code>&#8216; variable in this hook to a non-zero value avoids any quilt specific actions from being run at all.</dl>
<dt><code>set-patch-format</code></p>
<dd> This hook is used to control some of the possible expansions in <code>patch-format</code> and <code>nopatch-format</code> styles with patch queue systems such as quilt, mqueue and the like.</p>
<dl>
<dt>
<dd>
<p> This hook is used in the <code>git</code>, <code>hg</code> and <code>quilt</code> backends. </p>
<p> The hook allows the control of the <code>%p</code> (<code>${hook_com[applied]}</code>) and <code>%u</code> (<code>${hook_com[unapplied]}</code>) expansion in all backends that use the hook. With the mercurial backend, the <code>%g</code> (<code>${hook_com[guards]}</code>) expansion is controllable in addition to that. </p>
<p> If <code>ret</code> is set to non-zero, the string in <code>${hook_com[patch-replace]}</code> will be used unchanged instead of an expanded format from <code>patch-format</code> or <code>nopatch-format</code>. </p>
<p> This hook is, in concert with the <code>gen-applied-string</code> or <code>gen-unapplied-string</code> hooks if they are defined, responsible for <code>%</code>-escaping the final <code>patch-format</code> value for use in the prompt. (See the <code>Oddities</code> section.)</dl>
<dt><code>set-message</code></p>
<dd> Called each time before a `<code>vcs_info_msg_</code><i>N</i><code>_</code>&#8216; message is set. It takes two arguments; the first being the `<i>N</i>&#8216; in the message variable name, the second is the currently configured <code>formats</code> or <code>actionformats</code>.</p>
<dl>
<dt>
<dd>
<p> There are a number of `<code>hook_com</code>&#8216; keys, that are used here: `<code>action</code>&#8216;, `<code>branch</code>&#8216;, `<code>base</code>&#8216;, `<code>base-name</code>&#8216;, `<code>subdir</code>&#8216;, `<code>staged</code>&#8216;, `<code>unstaged</code>&#8216;, `<code>revision</code>&#8216;, `<code>misc</code>&#8216;, `<code>vcs</code>&#8216; and one `<code>miscN</code>&#8216; entry for each backend-specific data field (<code>N</code> starting at zero). They are set to the values figured out so far by <code>vcs_info</code> and any change will be used directly when the actual replacement is done. </p>
<p> Since this hook is triggered multiple times (once for each configured <code>formats</code> or <code>actionformats</code>), each of the `<code>hook_com</code>&#8216; keys mentioned above (except for the <code>miscN</code> entries) has an `<code>_orig</code>&#8216; counterpart, so even if you changed a value to your liking you can still get the original value in the next run. Changing the `<code>_orig</code>&#8216; values is probably not a good idea. </p>
<p> If <code>ret</code> is set to non-zero, the string in <code>${hook_com[message]}</code> will be used unchanged as the message by <code>vcs_info</code>.</dl>
</dl>
<p> If all of this sounds rather confusing, take a look at the <code>Examples</code> section below and also in the <code>Misc/vcs_info-examples</code> file in the Zsh source. They contain some explanatory code. </p>
<h3>Examples</h3>
<p> Don&#8217;t use <code>vcs_info</code> at all (even though it&#8217;s in your prompt):</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*' enable NONE</code>
</pre>
</dl>
<p> Disable the backends for <code>bzr</code> and <code>svk</code>:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*' disable bzr svk</code>
</pre>
</dl>
<p> Disable everything <i>but</i> <code>bzr</code> and <code>svk</code>:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*' enable bzr svk</code>
</pre>
</dl>
<p> Provide a special formats for <code>git</code>:</p>
<dl>
<dt>
<dd>
zstyle &#8216;:vcs_info:git:*&#8217; formats &#8216; GIT, BABY! [%b]&#8217; zstyle &#8216;:vcs_info:git:*&#8217; actionformats &#8216; GIT ACTION! [%b|%a]&#8217;
</dl>
<p> All <code>%x</code> expansion in all sorts of formats (<code>formats</code>, <code>actionformats</code>, <code>branchformat</code>, you name it) are done using the `<code>zformat</code>&#8216; builtin from the `<code>zsh/zutil</code>&#8216; module. That means you can do everything with these <code>%x</code> items what zformat supports. In particular, if you want something that is really long to have a fixed width, like a hash in a mercurial branchformat, you can do this: <code>%12.12i</code>. That&#8217;ll shrink the 40 character hash to its 12 leading characters. The form is actually `<code>%</code><i>min</i><code>.</code><i>max</i><code>x</code>&#8216;. More is possible. See the section `The zsh/zutil Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1) for details. </p>
<p> Use the quicker <code>bzr</code> backend</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:bzr:*' use-simple true</code>
</pre>
</dl>
<p> If you do use <code>use-simple</code>, please report if it does `the-right-thing[tm]&#8217;. </p>
<p> Display the revision number in yellow for <code>bzr</code> and <code>svn</code>:</p>
<dl>
<dt>
<dd>
zstyle &#8216;:vcs_info:(svn|bzr):*&#8217; \<br />
       branchformat &#8216;%b%{&#8216; $<br />
{<br />
    fg[yellow]<br />
}<br />
&#8216;%}:%r&#8217;
</dl>
<p> If you want colors, make sure you enclose the color codes in <code>%{</code><i>&#8230;</i><code>%}</code> if you want to use the string provided by <code>vcs_info</code> in prompts. </p>
<p> Here is how to print the VCS information as a command (not in a prompt):</p>
<dl>
<dt>
<dd>
<pre>
<code>alias vcsi='vcs_info command; vcs_info_lastmsg'</code>
</pre>
</dl>
<p> This way, you can even define different formats for output via <code>vcs_info_lastmsg</code> in the &#8216;<code>:vcs_info:*:command:*</code>&#8216; namespace. </p>
<p> Now as promised, some code that uses hooks: say, you&#8217;d like to replace the string `svn&#8217; by `subversion&#8217; in <code>vcs_info</code>&#8216;s <code>%s</code> <code>formats</code> replacement. </p>
<p> First, we will tell <code>vcs_info</code> to call a function when populating the message variables with the gathered information:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*+set-message:*' hooks svn2subversion</code>
</pre>
</dl>
<p> Nothing happens. Which is reasonable, since we didn&#8217;t define the actual function yet. To see what the hooks subsystem is trying to do, enable the `<code>debug</code>&#8216; style:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*+*:*' debug true</code>
</pre>
</dl>
<p> That should give you an idea what is going on. Specifically, the function that we are looking for is `<code>+vi-svn2subversion</code>&#8216;. Note, the `<code>+vi-</code>&#8216; prefix. So, everything is in order, just as documented. When you are done checking out the debugging output, disable it again:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:*+*:*' debug false</code>
</pre>
</dl>
<p> Now, let&#8217;s define the function:</p>
<dl>
<dt>
<dd>
function + vi &#8211; svn2subversion()<br />
{<br />
    [[${hook_com[vcs_orig]} == svn]] &amp;&amp; hook_com[vcs] = subversion<br />
}
</dl>
<p> Simple enough. And it could have even been simpler, if only we had registered our function in a less generic context. If we do it only in the `<code>svn</code>&#8216; backend&#8217;s context, we don&#8217;t need to test which the active backend is:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:svn+set-message:*' hooks svn2subversion</code>
</pre>
</dl>
<dl>
<dt>
<dd>
function + vi &#8211; svn2subversion()<br />
{<br />
    hook_com[vcs] = subversion<br />
}
</dl>
<p> And finally a little more elaborate example, that uses a hook to create a customised bookmark string for the <code>hg</code> backend. </p>
<p> Again, we start off by registering a function:</p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':vcs_info:hg+gen-hg-bookmark-string:*' hooks hgbookmarks</code>
</pre>
</dl>
<p> And then we define the `<code>+vi-hgbookmarks</code>&#8216; function:</p>
<dl>
<dt>
<dd>
function + vi &#8211; hgbookmarks()<br />
{<br />
#The default is to connect all bookmark names by<br />
#commas.This mixes things up a little.<br />
#Imagine, there&#8217;s one type of bookmarks that is<br />
#special to you.Say, because it&#8217;s *your* work.<br />
#Those bookmarks look always like this : &#8220;sh/*&#8221;<br />
#(because your initials are sh, for example).<br />
#This makes the bookmarks string use only those<br />
#bookmarks.If there&#8217;s more than one, it<br />
#concatenates them using commas.<br />
#The bookmarks returned by `hg&#8217; are available in<br />
#the function&#8217;s positional parameters.<br />
    local s = &#8220;${(Mj:,:)@:#sh/*}&#8221;<br />
#Now, the communication with the code that calls<br />
#the hook functions is done via the hook_com[]<br />
#hash.The key at which the `gen &#8211; hg &#8211; bookmark &#8211; string&#8217;<br />
#hook looks is `hg &#8211; bookmark &#8211; string&#8217;. So:<br />
        hook_com[hg &#8211; bookmark &#8211; string] = $s<br />
#And to signal that we want to use the string we<br />
#just generated, set the special variable `ret&#8217; to<br />
#something other than the default zero:<br />
            ret = 1 return 0<br />
}
</dl>
<p> Some longer examples and code snippets which might be useful are available in the examples file located at Misc/vcs_info-examples in the Zsh source directory. </p>
<p> This concludes our guided tour through zsh&#8217;s <code>vcs_info</code>. </p>
<h2>PROMPT THEMES</h2>
<h3>Installation</h3>
<p> You should make sure all the functions from the <code>Functions/Prompts</code> directory of the source distribution are available; they all begin with the string `<code>prompt_</code>&#8216; except for the special function`<code>promptinit</code>&#8216;. You also need the `<code>colors</code>&#8216; and `<code>add-zsh-hook</code>&#8216; functions from <code>Functions/Misc</code>. All these functions may already be installed on your system; if not, you will need to find them and copy them. The directory should appear as one of the elements of the <code>fpath</code> array (this should already be the case if they were installed), and at least the function <code>promptinit</code> should be autoloaded; it will autoload the rest. Finally, to initialize the use of the system you need to call the <code>promptinit</code> function. The following code in your <code>.zshrc</code> will arrange for this; assume the functions are stored in the directory <code>~/myfns</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>fpath=(~/myfns $fpath)
autoload -U promptinit
promptinit</code>
</pre>
</dl>
<h3>Theme Selection</h3>
<p> Use the <code>prompt</code> command to select your preferred theme. This command may be added to your <code>.zshrc</code> following the call to <code>promptinit</code> in order to start zsh with a theme already selected. </p>
<dl>
<dt>
<dd> <code>prompt</code> [ <code>-c</code> | <code>-l</code> ]</p>
<dt>
<dd> <code>prompt</code> [ <code>-p</code> | <code>-h</code> ] [ <i>theme</i> &#8230; ]</p>
<dt>
<dd> <code>prompt</code> [ <code>-s</code> ] <i>theme</i> [ <i>arg</i> &#8230; ] Set or examine the prompt theme. With no options and a <i>theme</i> argument, the theme with that name is set as the current theme. The available themes are determined at run time; use the <code>-l</code> option to see a list. The special <i>theme</i> `<code>random</code>&#8216; selects at random one of the available themes and sets your prompt to that.</p>
<dl>
<dt>
<dd>
<p> In some cases the <i>theme</i> may be modified by one or more arguments, which should be given after the theme name. See the help for each theme for descriptions of these arguments. </p>
<p> Options are: </p>
<dl>
<dt><code>-c</code></p>
<dd> Show the currently selected theme and its parameters, if any.</p>
<dt><code>-l</code></p>
<dd> List all available prompt themes.</p>
<dt><code>-p</code></p>
<dd> Preview the theme named by <i>theme</i>, or all themes if no <i>theme</i> is given.</p>
<dt><code>-h</code></p>
<dd> Show help for the theme named by <i>theme</i>, or for the <code>prompt</code> function if no <i>theme</i> is given.</p>
<dt><code>-s</code></p>
<dd> Set <i>theme</i> as the current theme and save state.</dl>
</dl>
<dt><code>prompt_</code><i>theme</i><code>_setup</code></p>
<dd> Each available <i>theme</i> has a setup function which is called by the <code>prompt</code> function to install that theme. This function may define other functions as necessary to maintain the prompt, including functions used to preview the prompt or provide help for its use. You should not normally call a theme&#8217;s setup function directly.</dl>
<h3>Utility Themes</h3>
<dl>
<dt>
<dd> <code>prompt off</code> The theme `<code>off</code>&#8216; sets all the prompt variables to minimal values with no special effects.</p>
<dt><code>prompt default</code></p>
<dd> The theme `<code>default</code>&#8216; sets all prompt variables to the same state as if an interactive zsh was started with no initialization files.</p>
<dt><code>prompt restore</code></p>
<dd> The special theme `<code>restore</code>&#8216; erases all theme settings and sets prompt variables to their state before the first time the `<code>prompt</code>&#8216; function was run, provided each theme has properly defined its cleanup (see below).</p>
<dl>
<dt>
<dd>
<p> Note that you can undo `<code>prompt off</code>&#8216; and `<code>prompt default</code>&#8216; with `<code>prompt restore</code>&#8216;, but a second restore does not undo the first.</dl>
</dl>
<h3>Writing Themes</h3>
<p> The first step for adding your own theme is to choose a name for it, and create a file `<code>prompt_</code><i>name</i>_setup&#8217; in a directory in your <code>fpath</code>, such as <code>~/myfns</code> in the example above. The file should at minimum contain assignments for the prompt variables that your theme wishes to modify. By convention, themes use <code>PS1</code>, <code>PS2</code>, <code>RPS1</code>, etc., rather than the longer <code>PROMPT</code> and <code>RPROMPT</code>. </p>
<p> The file is autoloaded as a function in the current shell context, so it may contain any necessary commands to customize your theme, including defining additional functions. To make some complex tasks easier, your setup function may also do any of the following: </p>
<dl>
<dt>
<dd> Assign <code>prompt_opts</code> The array <code>prompt_opts</code> may be assigned any of <code>&quot;bang&quot;</code>, <code>&quot;cr&quot;</code>, <code>&quot;percent&quot;</code>, <code>&quot;sp&quot;</code>, and/or <code>&quot;subst&quot;</code> as values. The corresponding setopts (<code>promptbang</code>, etc.) are turned on, all other prompt-related options are turned off. The <code>prompt_opts</code> array preserves setopts even beyond the scope of <code>localoptions</code>, should your function need that.</p>
<dt>Modify precmd and preexec</p>
<dd> Use of <code>add-zsh-hook</code> is recommended. The <code>precmd</code> and <code>preexec</code> hooks are automatically adjusted if the prompt theme changes or is disabled.</p>
<dt>Declare cleanup</p>
<dd> If your function makes any other changes that should be undone when the theme is disabled, your setup function may call</p>
<dl>
<dt>
<dd>
<pre>
<code>prompt_cleanup </code><i>command</i>
</pre>
</dl>
<p> where <i>command</i> should be suitably quoted. If your theme is ever disabled or replaced by another, <i>command</i> is executed with <code>eval</code>. You may declare more than one such cleanup hook.</p>
<dt>Define preview</p>
<dd> Define or autoload a function <code>prompt_</code><i>name</i>_preview to display a simulated version of your prompt. A simple default previewer is defined by <code>promptinit</code> for themes that do not define their own. This preview function is called by `<code>prompt -p</code>&#8216;.</p>
<dt>Provide help</p>
<dd> Define or autoload a function <code>prompt_</code><i>name</i>_help to display documentation or help text for your theme. This help function is called by `<code>prompt -h</code>&#8216;.</dl>
<h2>ZLE FUNCTIONS</h2>
<h3>Widgets</h3>
<p> These functions all implement user-defined ZLE widgets (see <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)) which can be bound to keystrokes in interactive shells. To use them, your <code>.zshrc</code> should contain lines of the form </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload </code><i>function</i>
zle -N <i>function</i>
</pre>
</dl>
<p> followed by an appropriate <code>bindkey</code> command to associate the function with a key sequence. Suggested bindings are described below. </p>
<dl>
<dt>
<dd> bash-style word functions If you are looking for functions to implement moving over and editing words in the manner of bash, where only alphanumeric characters are considered word characters, you can use the functions described in the next section. The following is sufficient:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>autoload -U select-word-style
select-word-style bash</code>
</pre>
</dl>
</dl>
<dt>
<dd> <code>forward-word-match</code>, <code>backward-word-match</code></p>
<dt>
<dd> <code>kill-word-match</code>, <code>backward-kill-word-match</code></p>
<dt>
<dd> <code>transpose-words-match</code>, <code>capitalize-word-match</code></p>
<dt>
<dd> <code>up-case-word-match</code>, <code>down-case-word-match</code></p>
<dt>
<dd> <code>delete-whole-word-match</code>, <code>select-word-match</code></p>
<dt>
<dd> <code>select-word-style</code>, <code>match-word-context</code>, <code>match-words-by-style</code> The first eight `<code>-match</code>&#8216; functions are drop-in replacements for the builtin widgets without the suffix. By default they behave in a similar way. However, by the use of styles and the function <code>select-word-style</code>, the way words are matched can be altered. <code>select-word-match</code> is intended to be used as a text object in vi mode but with custom word styles. For comparison, the widgets described in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1) under Text Objects use fixed definitions of words, compatible with the <code>vim</code> editor.</p>
<dl>
<dt>
<dd>
<p> The simplest way of configuring the functions is to use <code>select-word-style</code>, which can either be called as a normal function with the appropriate argument, or invoked as a user-defined widget that will prompt for the first character of the word style to be used. The first time it is invoked, the first eight <code>-match</code> functions will automatically replace the builtin versions, so they do not need to be loaded explicitly. </p>
<p> The word styles available are as follows. Only the first character is examined. </p>
<dl>
<dt>
<dd> <code>bash</code> Word characters are alphanumeric characters only.</p>
<dt><code>normal</code></p>
<dd> As in normal shell operation: word characters are alphanumeric characters plus any characters present in the string given by the parameter <code>$WORDCHARS</code>.</p>
<dt><code>shell</code></p>
<dd> Words are complete shell command arguments, possibly including complete quoted strings, or any tokens special to the shell.</p>
<dt><code>whitespace</code></p>
<dd> Words are any set of characters delimited by whitespace.</p>
<dt><code>default</code></p>
<dd> Restore the default settings; this is usually the same as `<code>normal</code>&#8216;.</dl>
<p> All but `<code>default</code>&#8216; can be input as an upper case character, which has the same effect but with subword matching turned on. In this case, words with upper case characters are treated specially: each separate run of upper case characters, or an upper case character followed by any number of other characters, is considered a word. The style <code>subword-range</code> can supply an alternative character range to the default `<code>[:upper:]</code>&#8216;; the value of the style is treated as the contents of a `<code>[</code><i>&#8230;</i><code>]</code>&#8216; pattern (note that the outer brackets should not be supplied, only those surrounding named ranges). </p>
<p> More control can be obtained using the <code>zstyle</code> command, as described in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). Each style is looked up in the context <code>:zle:</code><i>widget</i> where <i>widget</i> is the name of the user-defined widget, not the name of the function implementing it, so in the case of the definitions supplied by <code>select-word-style</code> the appropriate contexts are <code>:zle:forward-word</code>, and so on. The function <code>select-word-style</code> itself always defines styles for the context `<code>:zle:*</code>&#8216; which can be overridden by more specific (longer) patterns as well as explicit contexts. </p>
<p> The style <code>word-style</code> specifies the rules to use. This may have the following values. </p>
<dl>
<dt>
<dd> <code>normal</code> Use the standard shell rules, i.e. alphanumerics and <code>$WORDCHARS</code>, unless overridden by the styles <code>word-chars</code> or <code>word-class</code>.</p>
<dt><code>specified</code></p>
<dd> Similar to <code>normal</code>, but <i>only</i> the specified characters, and not also alphanumerics, are considered word characters.</p>
<dt><code>unspecified</code></p>
<dd> The negation of specified. The given characters are those which will <i>not</i> be considered part of a word.</p>
<dt><code>shell</code></p>
<dd> Words are obtained by using the syntactic rules for generating shell command arguments. In addition, special tokens which are never command arguments such as `<code>()</code>&#8216; are also treated as words.</p>
<dt><code>whitespace</code></p>
<dd> Words are whitespace-delimited strings of characters.</dl>
<p> The first three of those rules usually use <code>$WORDCHARS</code>, but the value in the parameter can be overridden by the style <code>word-chars</code>, which works in exactly the same way as <code>$WORDCHARS</code>. In addition, the style <code>word-class</code> uses character class syntax to group characters and takes precedence over <code>word-chars</code> if both are set. The <code>word-class</code> style does not include the surrounding brackets of the character class; for example, `<code>-:[:alnum:]</code>&#8216; is a valid <code>word-class</code> to include all alphanumerics plus the characters `<code>&#8211;</code>&#8216; and `<code>:</code>&#8216;. Be careful including `<code>]</code>&#8216;, `<code>^</code>&#8216; and `<code>&#8211;</code>&#8216; as these are special inside character classes. </p>
<p> <code>word-style</code> may also have `<code>-subword</code>&#8216; appended to its value to turn on subword matching, as described above. </p>
<p> The style <code>skip-chars</code> is mostly useful for <code>transpose-words</code> and similar functions. If set, it gives a count of characters starting at the cursor position which will not be considered part of the word and are treated as space, regardless of what they actually are. For example, if </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':zle:transpose-words' skip-chars 1</code>
</pre>
</dl>
<p> has been set, and <code>transpose-words-match</code> is called with the cursor on the <i>X</i> of <code>foo</code><i>X</i><code>bar</code>, where <i>X</i> can be any character, then the resulting expression is <code>bar</code><i>X</i><code>foo</code>. </p>
<p> Finer grained control can be obtained by setting the style <code>word-context</code> to an array of pairs of entries. Each pair of entries consists of a <i>pattern</i> and a <i>subcontext</i>. The shell argument the cursor is on is matched against each <i>pattern</i> in turn until one matches; if it does, the context is extended by a colon and the corresponding <i>subcontext</i>. Note that the test is made against the original word on the line, with no stripping of quotes. Special handling is done between words: the current context is examined and if it contains the string <code>between</code> the word is set to a single space; else if it is contains the string <code>back</code>, the word before the cursor is considered, else the word after cursor is considered. Some examples are given below. </p>
<p> The style <code>skip-whitespace-first</code> is only used with the <code>forward-word</code> widget. If it is set to true, then <code>forward-word</code> skips any non-word-characters, followed by any non-word-characters: this is similar to the behaviour of other word-orientated widgets, and also that used by other editors, however it differs from the standard zsh behaviour. When using <code>select-word-style</code> the widget is set in the context <code>:zle:*</code> to <code>true</code> if the word style is <code>bash</code> and <code>false</code> otherwise. It may be overridden by setting it in the more specific context <code>:zle:forward-word*</code>. </p>
<p> It is possible to create widgets with specific behaviour by defining a new widget implemented by the appropriate generic function, then setting a style for the context of the specific widget. For example, the following defines a widget <code>backward-kill-space-word</code> using <code>backward-kill-word-match</code>, the generic widget implementing <code>backward-kill-word</code> behaviour, and ensures that the new widget always implements space-delimited behaviour. </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -N backward-kill-space-word backward-kill-word-match
zstyle :zle:backward-kill-space-word word-style space</code>
</pre>
</dl>
<p> The widget <code>backward-kill-space-word</code> can now be bound to a key. </p>
<p> Here are some further examples of use of the styles, actually taken from the simplified interface in <code>select-word-style</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':zle:*' word-style standard
zstyle ':zle:*' word-chars ''</code>
</pre>
</dl>
<p> Implements bash-style word handling for all widgets, i.e. only alphanumerics are word characters; equivalent to setting the parameter <code>WORDCHARS</code> empty for the given context. </p>
<dl>
<dt>
<dd>
<pre>
<code>style ':zle:*kill*' word-style space</code>
</pre>
</dl>
<p> Uses space-delimited words for widgets with the word `kill&#8217; in the name. Neither of the styles <code>word-chars</code> nor <code>word-class</code> is used in this case. </p>
<p> Here are some examples of use of the <code>word-context</code> style to extend the context. </p>
<dl>
<dt>
<dd>
zstyle &#8216;:zle:*&#8217; word &#8211; context \<br />
       &#8220;*/*&#8221; filename &#8220;[[:space:]]&#8221; whitespace zstyle &#8216;:zle:transpose-words:whitespace&#8217; word &#8211;<br />
    style shell<br />
        zstyle &#8216;:zle:transpose-words:filename&#8217; word &#8211;<br />
    style normal<br />
        zstyle &#8216;:zle:transpose-words:filename&#8217; word &#8211;<br />
    chars &#8221;
</dl>
<p> This provides two different ways of using <code>transpose-words</code> depending on whether the cursor is on whitespace between words or on a filename, here any word containing a <code>/</code>. On whitespace, complete arguments as defined by standard shell rules will be transposed. In a filename, only alphanumerics will be transposed. Elsewhere, words will be transposed using the default style for <code>:zle:transpose-words</code>. </p>
<p> The word matching and all the handling of <code>zstyle</code> settings is actually implemented by the function <code>match-words-by-style</code>. This can be used to create new user-defined widgets. The calling function should set the local parameter <code>curcontext</code> to <code>:zle:</code><i>widget</i>, create the local parameter <code>matched_words</code> and call <code>match-words-by-style</code> with no arguments. On return, <code>matched_words</code> will be set to an array with the elements: (1) the start of the line (2) the word before the cursor (3) any non-word characters between that word and the cursor (4) any non-word character at the cursor position plus any remaining non-word characters before the next word, including all characters specified by the <code>skip-chars</code> style, (5) the word at or following the cursor (6) any non-word characters following that word (7) the remainder of the line. Any of the elements may be an empty string; the calling function should test for this to decide whether it can perform its function. </p>
<p> If the variable <code>matched_words</code> is defined by the caller to <code>match-words-by-style</code> as an associative array (<code>local -A matched_words</code>), then the seven values given above should be retrieved from it as elements named <code>start</code>, <code>word-before-cursor</code>, <code>ws-before-cursor</code>, <code>ws-after-cursor</code>, <code>word-after-cursor</code>, <code>ws-after-word</code>, and <code>end</code>. In addition the element <code>is-word-start</code> is 1 if the cursor is on the start of a word or subword, or on white space before it (the cases can be distinguished by testing the <code>ws-after-cursor</code> element) and 0 otherwise. This form is recommended for future compatibility. </p>
<p> It is possible to pass options with arguments to <code>match-words-by-style</code> to override the use of styles. The options are:</p>
<dl>
<dt><code>-w</code></p>
<dd> <i>word-style</i></p>
<dt><code>-s</code></p>
<dd> <i>skip-chars</i></p>
<dt><code>-c</code></p>
<dd> <i>word-class</i></p>
<dt><code>-C</code></p>
<dd> <i>word-chars</i></p>
<dt><code>-r</code></p>
<dd> <i>subword-range</i></dl>
<p> For example, <code>match-words-by-style -w shell -c 0</code> may be used to extract the command argument around the cursor. </p>
<p> The <code>word-context</code> style is implemented by the function <code>match-word-context</code>. This should not usually need to be called directly.</dl>
<dt><code>bracketed-paste-magic</code></p>
<dd> The <code>bracketed-paste</code> widget (see subsection Miscellaneous in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)) inserts pasted text literally into the editor buffer rather than interpret it as keystrokes. This disables some common usages where the self-insert widget is replaced in order to accomplish some extra processing. An example is the contributed <code>url-quote-magic</code> widget described below.</p>
<dl>
<dt>
<dd>
<p> The <code>bracketed-paste-magic</code> widget is meant to replace <code>bracketed-paste</code> with a wrapper that re-enables these self-insert actions, and other actions as selected by zstyles. Therefore this widget is installed with </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -Uz bracketed-paste-magic
zle -N bracketed-paste bracketed-paste-magic</code>
</pre>
</dl>
<p> Other than enabling some widget processing, <code>bracketed-paste-magic</code> attempts to replicate <code>bracketed-paste</code> as faithfully as possible. </p>
<p> The following zstyles may be set to control processing of pasted text. All are looked up in the context `<code>:bracketed-paste-magic</code>&#8216;. </p>
<dl>
<dt>
<dd> <code>active-widgets</code> A list of patterns matching widget names that should be activated during the paste. All other key sequences are processed as self-insert-unmeta. The default is `<code>self-*</code>&#8216; so any user-defined widgets named with that prefix are active along with the builtin self-insert.</p>
<dl>
<dt>
<dd>
<p> If this style is not set (explicitly deleted) or set to an empty value, no widgets are active and the pasted text is inserted literally. If the value includes `<code>undefined-key</code>&#8216;, any unknown sequences are discarded from the pasted text.</dl>
<dt><code>inactive-keys</code></p>
<dd> The inverse of <code>active-widgets</code>, a list of key sequences that always use <code>self-insert-unmeta</code> even when bound to an active widget. Note that this is a list of literal key sequences, not patterns.</p>
<dt><code>paste-init</code></p>
<dd> A list of function names, called in widget context (but not as widgets). The functions are called in order until one of them returns a non-zero status. The parameter `<code>PASTED</code>&#8216; contains the initial state of the pasted text. All other ZLE parameters such as `<code>BUFFER</code>&#8216; have their normal values and side-effects, and full history is available, so for example <code>paste-init</code> functions may move words from <code>BUFFER</code> into <code>PASTED</code> to make those words visible to the <code>active-widgets</code>.</p>
<dl>
<dt>
<dd>
<p> A non-zero return from a <code>paste-init</code> function does <i>not</i> prevent the paste itself from proceeding. </p>
<p> Loading <code>bracketed-paste-magic</code> defines <code>backward-extend-paste</code>, a helper function for use in <code>paste-init</code>. </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle :bracketed-paste-magic paste-init \ 
       backward-extend-paste</code>
</pre>
</dl>
<p> When a paste would insert into the middle of a word or append text to a word already on the line, <code>backward-extend-paste</code> moves the prefix from <code>LBUFFER</code> into <code>PASTED</code> so that the <code>active-widgets</code> see the full word so far. This may be useful with <code>url-quote-magic</code>.</dl>
<dt><code>paste-finish</code></p>
<dd> Another list of function names called in order until one returns non-zero. These functions are called <i>after</i> the pasted text has been processed by the <code>active-widgets</code>, but <i>before</i> it is inserted into `<code>BUFFER</code>&#8216;. ZLE parameters have their normal values and side-effects.</p>
<dl>
<dt>
<dd>
<p> A non-zero return from a <code>paste-finish</code> function does <i>not</i> prevent the paste itself from proceeding. </p>
<p> Loading <code>bracketed-paste-magic</code> also defines <code>quote-paste</code>, a helper function for use in <code>paste-finish</code>. </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle :bracketed-paste-magic paste-finish \ 
       quote-paste
zstyle :bracketed-paste-magic:finish quote-style \ 
       qqq</code>
</pre>
</dl>
<p> When the pasted text is inserted into <code>BUFFER</code>, it is quoted per the <code>quote-style</code> value. To forcibly turn off the built-in numeric prefix quoting of <code>bracketed-paste</code>, use: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle :bracketed-paste-magic:finish quote-style \ 
       none</code>
</pre>
</dl>
</dl>
</dl>
<p> <i>Important:</i> During <code>active-widgets</code> processing of the paste (after <code>paste-init</code> and before <code>paste-finish</code>), <code>BUFFER</code> starts empty and history is restricted, so cursor motions, etc., may not pass outside of the pasted content. Text assigned to <code>BUFFER</code> by the active widgets is copied back into <code>PASTED</code> before <code>paste-finish</code>.</dl>
<dt><code>copy-earlier-word</code></p>
<dd> This widget works like a combination of <code>insert-last-word</code> and <code>copy-prev-shell-word</code>. Repeated invocations of the widget retrieve earlier words on the relevant history line. With a numeric argument <i>N</i>, insert the <i>N</i>th word from the history line; <i>N</i> may be negative to count from the end of the line.</p>
<dl>
<dt>
<dd>
<p> If <code>insert-last-word</code> has been used to retrieve the last word on a previous history line, repeated invocations will replace that word with earlier words from the same line. </p>
<p> Otherwise, the widget applies to words on the line currently being edited. The <code>widget</code> style can be set to the name of another widget that should be called to retrieve words. This widget must accept the same three arguments as <code>insert-last-word</code>.</dl>
<dt><code>cycle-completion-positions</code></p>
<dd> After inserting an unambiguous string into the command line, the new function based completion system may know about multiple places in this string where characters are missing or differ from at least one of the possible matches. It will then place the cursor on the position it considers to be the most interesting one, i.e. the one where one can disambiguate between as many matches as possible with as little typing as possible.</p>
<dl>
<dt>
<dd>
<p> This widget allows the cursor to be easily moved to the other interesting spots. It can be invoked repeatedly to cycle between all positions reported by the completion system.</dl>
<dt><code>delete-whole-word-match</code></p>
<dd> This is another function which works like the <code>-match</code> functions described immediately above, i.e. using styles to decide the word boundaries. However, it is not a replacement for any existing function.</p>
<dl>
<dt>
<dd>
<p> The basic behaviour is to delete the word around the cursor. There is no numeric argument handling; only the single word around the cursor is considered. If the widget contains the string <code>kill</code>, the removed text will be placed in the cutbuffer for future yanking. This can be obtained by defining <code>kill-whole-word-match</code> as follows: </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -N kill-whole-word-match delete-whole-word-match</code>
</pre>
</dl>
<p> and then binding the widget <code>kill-whole-word-match</code>.</dl>
<dt><code>up-line-or-beginning-search</code>, <code>down-line-or-beginning-search</code></p>
<dd> These widgets are similar to the builtin functions <code>up-line-or-search</code> and <code>down-line-or-search</code>: if in a multiline buffer they move up or down within the buffer, otherwise they search for a history line matching the start of the current line. In this case, however, they search for a line which matches the current line up to the current cursor position, in the manner of <code>history-beginning-search-backward</code> and <code>-forward</code>, rather than the first word on the line.</p>
<dt><code>edit-command-line</code></p>
<dd> Edit the command line using your visual editor, as in <code>ksh</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>bindkey -M vicmd v edit-command-line</code>
</pre>
</dl>
</dl>
<dt><code>expand-absolute-path</code></p>
<dd> Expand the file name under the cursor to an absolute path, resolving symbolic links. Where possible, the initial path segment is turned into a named directory or reference to a user&#8217;s home directory.</p>
<dt><code>history-search-end</code></p>
<dd> This function implements the widgets <code>history-beginning-search-backward-end</code> and <code>history-beginning-search-forward-end</code>. These commands work by first calling the corresponding builtin widget (see `History Control&#8217; in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1)) and then moving the cursor to the end of the line. The original cursor position is remembered and restored before calling the builtin widget a second time, so that the same search is repeated to look farther through the history.</p>
<dl>
<dt>
<dd>
<p> Although you <code>autoload</code> only one function, the commands to use it are slightly different because it implements two widgets. </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -N history-beginning-search-backward-end \ 
       history-search-end
zle -N history-beginning-search-forward-end \ 
       history-search-end
bindkey '^P' history-beginning-search-backward-end
bindkey '^N' history-beginning-search-forward-end</code>
</pre>
</dl>
</dl>
<dt><code>history-beginning-search-menu</code></p>
<dd> This function implements yet another form of history searching. The text before the cursor is used to select lines from the history, as for <code>history-beginning-search-backward</code> except that all matches are shown in a numbered menu. Typing the appropriate digits inserts the full history line. Note that leading zeroes must be typed (they are only shown when necessary for removing ambiguity). The entire history is searched; there is no distinction between forwards and backwards.</p>
<dl>
<dt>
<dd>
<p> With a numeric argument, the search is not anchored to the start of the line; the string typed by the use may appear anywhere in the line in the history. </p>
<p> If the widget name contains `<code>-end</code>&#8216; the cursor is moved to the end of the line inserted. If the widget name contains `<code>-space</code>&#8216; any space in the text typed is treated as a wildcard and can match anything (hence a leading space is equivalent to giving a numeric argument). Both forms can be combined, for example: </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -N history-beginning-search-menu-space-end \ 
       history-beginning-search-menu</code>
</pre>
</dl>
</dl>
<dt><code>history-pattern-search</code></p>
<dd> The function <code>history-pattern-search</code> implements widgets which prompt for a pattern with which to search the history backwards or forwards. The pattern is in the usual zsh format, however the first character may be <code>^</code> to anchor the search to the start of the line, and the last character may be <code>$</code> to anchor the search to the end of the line. If the search was not anchored to the end of the line the cursor is positioned just after the pattern found.</p>
<dl>
<dt>
<dd>
<p> The commands to create bindable widgets are similar to those in the example immediately above: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -U history-pattern-search
zle -N history-pattern-search-backward history-pattern-search
zle -N history-pattern-search-forward history-pattern-search</code>
</pre>
</dl>
</dl>
<dt><code>incarg</code></p>
<dd> Typing the keystrokes for this widget with the cursor placed on or to the left of an integer causes that integer to be incremented by one. With a numeric argument, the number is incremented by the amount of the argument (decremented if the numeric argument is negative). The shell parameter <code>incarg</code> may be set to change the default increment to something other than one.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>bindkey '^X+' incarg</code>
</pre>
</dl>
</dl>
<dt><code>incremental-complete-word</code></p>
<dd> This allows incremental completion of a word. After starting this command, a list of completion choices can be shown after every character you type, which you can delete with <code>^H</code> or <code>DEL</code>. Pressing return accepts the completion so far and returns you to normal editing (that is, the command line is <i>not</i> immediately executed). You can hit <code>TAB</code> to do normal completion, <code>^G</code> to abort back to the state when you started, and <code>^D</code> to list the matches.</p>
<dl>
<dt>
<dd>
<p> This works only with the new function based completion system. </p>
<dl>
<dt>
<dd>
<pre>
<code>bindkey '^Xi' incremental-complete-word</code>
</pre>
</dl>
</dl>
<dt><code>insert-composed-char</code></p>
<dd> This function allows you to compose characters that don&#8217;t appear on the keyboard to be inserted into the command line. The command is followed by two keys corresponding to ASCII characters (there is no prompt). For accented characters, the two keys are a base character followed by a code for the accent, while for other special characters the two characters together form a mnemonic for the character to be inserted. The two-character codes are a subset of those given by RFC 1345 (see for example <code><a rel="nofollow" href="http://www.faqs.org/rfcs/rfc1345.html">http://www.faqs.org/rfcs/rfc1345.html</a></code>).</p>
<dl>
<dt>
<dd>
<p> The function may optionally be followed by up to two characters which replace one or both of the characters read from the keyboard; if both characters are supplied, no input is read. For example, <code>insert-composed-char a:</code> can be used within a widget to insert an a with umlaut into the command line. This has the advantages over use of a literal character that it is more portable. </p>
<p> For best results zsh should have been built with support for multibyte characters (configured with <code>&#8211;enable-multibyte</code>); however, the function works for the limited range of characters available in single-byte character sets such as ISO-8859-1. </p>
<p> The character is converted into the local representation and inserted into the command line at the cursor position. (The conversion is done within the shell, using whatever facilities the C library provides.) With a numeric argument, the character and its code are previewed in the status line </p>
<p> The function may be run outside zle in which case it prints the character (together with a newline) to standard output. Input is still read from keystrokes. </p>
<p> See <code>insert-unicode-char</code> for an alternative way of inserting Unicode characters using their hexadecimal character number. </p>
<p> The set of accented characters is reasonably complete up to Unicode character U+0180, the set of special characters less so. However, it is very sporadic from that point. Adding new characters is easy, however; see the function <code>define-composed-chars</code>. Please send any additions to <code>zsh-workers [at] zsh.org</code>. </p>
<p> The codes for the second character when used to accent the first are as follows. Note that not every character can take every accent.</p>
<dl>
<dt><code>!</code></p>
<dd> Grave.</p>
<dt><code>&#8216;</code></p>
<dd> Acute.</p>
<dt><code>&gt;</code></p>
<dd> Circumflex.</p>
<dt><code>?</code></p>
<dd> Tilde. (This is not <code>~</code> as RFC 1345 does not assume that character is present on the keyboard.)</p>
<dt><code>&#8211;</code></p>
<dd> Macron. (A horizontal bar over the base character.)</p>
<dt><code>(</code></p>
<dd> Breve. (A shallow dish shape over the base character.)</p>
<dt><code>.</code></p>
<dd> Dot above the base character, or in the case of <code>i</code> no dot, or in the case of <code>L</code> and <code>l</code> a centered dot.</p>
<dt><code>:</code></p>
<dd> Diaeresis (Umlaut).</p>
<dt><code>c</code></p>
<dd> Cedilla.</p>
<dt><code>_</code></p>
<dd> Underline, however there are currently no underlined characters.</p>
<dt><code>/</code></p>
<dd> Stroke through the base character.</p>
<dt><code>&quot;</code></p>
<dd> Double acute (only supported on a few letters).</p>
<dt><code>;</code></p>
<dd> Ogonek. (A little forward facing hook at the bottom right of the character.)</p>
<dt><code>&lt;</code></p>
<dd> Caron. (A little v over the letter.)</p>
<dt><code>0</code></p>
<dd> Circle over the base character.</p>
<dt><code>2</code></p>
<dd> Hook over the base character.</p>
<dt><code>9</code></p>
<dd> Horn over the base character.</dl>
<p> The most common characters from the Arabic, Cyrillic, Greek and Hebrew alphabets are available; consult RFC 1345 for the appropriate sequences. In addition, a set of two letter codes not in RFC 1345 are available for the double-width characters corresponding to ASCII characters from <code>!</code> to <code>~</code> (0x21 to 0x7e) by preceding the character with <code>^</code>, for example <code>^A</code> for a double-width <code>A</code>. </p>
<p> The following other two-character sequences are understood. </p>
<dl>
<dt>
<dd> ASCII characters These are already present on most keyboards:</p>
<dt><code>&lt;(</code></p>
<dd> Left square bracket</p>
<dt><code>//</code></p>
<dd> Backslash (solidus)</p>
<dt><code>)&gt;</code></p>
<dd> Right square bracket</p>
<dt><code>(!</code></p>
<dd> Left brace (curly bracket)</p>
<dt><code>!!</code></p>
<dd> Vertical bar (pipe symbol)</p>
<dt><code>!)</code></p>
<dd> Right brace (curly bracket)</p>
<dt><code>&#8216;?</code></p>
<dd> Tilde</p>
<dt>Special letters</p>
<dd> Characters found in various variants of the Latin alphabet:</p>
<dt><code>ss</code></p>
<dd> Eszett (scharfes S)</p>
<dt><code>D-</code>, <code>d-</code></p>
<dd> Eth</p>
<dt><code>TH</code>, <code>th</code></p>
<dd> Thorn</p>
<dt><code>kk</code></p>
<dd> Kra</p>
<dt><code>&#8216;n</code></p>
<dd> &#8216;n</p>
<dt><code>NG</code>, <code>ng</code></p>
<dd> Ng</p>
<dt><code>OI</code>, <code>oi</code></p>
<dd> Oi</p>
<dt><code>yr</code></p>
<dd> yr</p>
<dt><code>ED</code></p>
<dd> ezh</p>
<dt>Currency symbols</p>
<dd>
<dt><code>Ct</code></p>
<dd> Cent</p>
<dt><code>Pd</code></p>
<dd> Pound sterling (also lira and others)</p>
<dt><code>Cu</code></p>
<dd> Currency</p>
<dt><code>Ye</code></p>
<dd> Yen</p>
<dt><code>Eu</code></p>
<dd> Euro (N.B. not in RFC 1345)</p>
<dt>Punctuation characters</p>
<dd> References to &quot;right&quot; quotes indicate the shape (like a 9 rather than 6) rather than their grammatical use. (For example, a &quot;right&quot; low double quote is used to open quotations in German.)</p>
<dt><code>!I</code></p>
<dd> Inverted exclamation mark</p>
<dt><code>BB</code></p>
<dd> Broken vertical bar</p>
<dt><code>SE</code></p>
<dd> Section</p>
<dt><code>Co</code></p>
<dd> Copyright</p>
<dt><code>-a</code></p>
<dd> Spanish feminine ordinal indicator</p>
<dt><code>&lt;&lt;</code></p>
<dd> Left guillemet</p>
<dt><code>&#8211;</code><code>&#8211;</code></p>
<dd> Soft hyphen</p>
<dt><code>Rg</code></p>
<dd> Registered trade mark</p>
<dt><code>PI</code></p>
<dd> Pilcrow (paragraph)</p>
<dt><code>-o</code></p>
<dd> Spanish masculine ordinal indicator</p>
<dt><code>&gt;&gt;</code></p>
<dd> Right guillemet</p>
<dt><code>?I</code></p>
<dd> Inverted question mark</p>
<dt><code>-1</code></p>
<dd> Hyphen</p>
<dt><code>-N</code></p>
<dd> En dash</p>
<dt><code>-M</code></p>
<dd> Em dash</p>
<dt><code>-3</code></p>
<dd> Horizontal bar</p>
<dt><code>:3</code></p>
<dd> Vertical ellipsis</p>
<dt><code>.3</code></p>
<dd> Horizontal midline ellipsis</p>
<dt><code>!2</code></p>
<dd> Double vertical line</p>
<dt><code>=2</code></p>
<dd> Double low line</p>
<dt><code>&#8216;6</code></p>
<dd> Left single quote</p>
<dt><code>&#8216;9</code></p>
<dd> Right single quote</p>
<dt><code>.9</code></p>
<dd> &quot;Right&quot; low quote</p>
<dt><code>9&#8242;</code></p>
<dd> Reversed &quot;right&quot; quote</p>
<dt><code>&quot;6</code></p>
<dd> Left double quote</p>
<dt><code>&quot;9</code></p>
<dd> Right double quote</p>
<dt><code>:9</code></p>
<dd> &quot;Right&quot; low double quote</p>
<dt><code>9&quot;</code></p>
<dd> Reversed &quot;right&quot; double quote</p>
<dt><code>/-</code></p>
<dd> Dagger</p>
<dt><code>/=</code></p>
<dd> Double dagger</p>
<dt>Mathematical symbols</p>
<dd>
<dt><code>DG</code></p>
<dd> Degree</p>
<dt><code>-2</code>, <code>+-</code>, <code>-+</code></p>
<dd> &#8211; sign, +/- sign, -/+ sign</p>
<dt><code>2S</code></p>
<dd> Superscript 2</p>
<dt><code>3S</code></p>
<dd> Superscript 3</p>
<dt><code>1S</code></p>
<dd> Superscript 1</p>
<dt><code>My</code></p>
<dd> Micro</p>
<dt><code>.M</code></p>
<dd> Middle dot</p>
<dt><code>14</code></p>
<dd> Quarter</p>
<dt><code>12</code></p>
<dd> Half</p>
<dt><code>34</code></p>
<dd> Three quarters</p>
<dt><code>*X</code></p>
<dd> Multiplication</p>
<dt><code>-:</code></p>
<dd> Division</p>
<dt><code>%0</code></p>
<dd> Per mille</p>
<dt><code>FA</code>, <code>TE</code>, <code>/0</code></p>
<dd> For all, there exists, empty set</p>
<dt><code>dP</code>, <code>DE</code>, <code>NB</code></p>
<dd> Partial derivative, delta (increment), del (nabla)</p>
<dt><code>(-</code>, <code>-)</code></p>
<dd> Element of, contains</p>
<dt><code>*P</code>, <code>+Z</code></p>
<dd> Product, sum</p>
<dt><code>*-</code>, <code>Ob</code>, <code>Sb</code></p>
<dd> Asterisk, ring, bullet</p>
<dt><code>RT</code>, <code>0(</code>, <code>00</code></p>
<dd> Root sign, proportional to, infinity</p>
<dt>Other symbols</p>
<dd>
<dt><code>cS</code>, <code>cH</code>, <code>cD</code>, <code>cC</code></p>
<dd> Card suits: spades, hearts, diamonds, clubs</p>
<dt><code>Md</code>, <code>M8</code>, <code>M2</code>, <code>Mb</code>, <code>Mx</code>, <code>MX</code></p>
<dd> Musical notation: crotchet (quarter note), quaver (eighth note), semiquavers (sixteenth notes), flag sign, natural sign, sharp sign</p>
<dt><code>Fm</code>, <code>Ml</code></p>
<dd> Female, male</p>
<dt>Accents on their own</p>
<dd>
<dt><code>&#8216;&gt;</code></p>
<dd> Circumflex (same as caret, <code>^</code>)</p>
<dt><code>&#8216;!</code></p>
<dd> Grave (same as backtick, <code>`</code>)</p>
<dt><code>&#8216;,</code></p>
<dd> Cedilla</p>
<dt><code>&#8216;:</code></p>
<dd> Diaeresis (Umlaut)</p>
<dt><code>&#8216;m</code></p>
<dd> Macron</p>
<dt><code>&#8221;</code></p>
<dd> Acute</dl>
</dl>
<dt><code>insert-files</code></p>
<dd> This function allows you type a file pattern, and see the results of the expansion at each step. When you hit return, all expansions are inserted into the command line.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>bindkey '^Xf' insert-files</code>
</pre>
</dl>
</dl>
<dt><code>insert-unicode-char</code></p>
<dd> When first executed, the user inputs a set of hexadecimal digits. This is terminated with another call to <code>insert-unicode-char</code>. The digits are then turned into the corresponding Unicode character. For example, if the widget is bound to <code>^XU</code>, the character sequence `<code>^XU 4 c ^XU</code>&#8216; inserts <code>L</code> (Unicode U+004c).</p>
<dl>
<dt>
<dd>
<p> See <code>insert-composed-char</code> for a way of inserting characters using a two-character mnemonic.</dl>
<dt>
<dd> <code>narrow-to-region </code>[ <code>-p</code> <i>pre</i> ] [ <code>-P</code> <i>post</i> ]</p>
<dt>
<dd> [ <code>-S</code> <i>statepm</i> | <code>-R</code> <i>statepm</i> | [ <code>-l</code> <i>lbufvar</i> ] [ <code>-r</code> <i>rbufvar</i> ] ]</p>
<dt>
<dd> [ <code>-n</code> ] [ <i>start</i> <i>end</i> ]</p>
<dt>
<dd> <code>narrow-to-region-invisible</code> Narrow the editable portion of the buffer to the region between the cursor and the mark, which may be in either order. The region may not be empty.</p>
<dl>
<dt>
<dd>
<p> <code>narrow-to-region</code> may be used as a widget or called as a function from a user-defined widget; by default, the text outside the editable area remains visible. A <code>recursive-edit</code> is performed and the original widening status is then restored. Various options and arguments are available when it is called as a function. </p>
<p> The options <code>-p</code> <i>pretext</i> and <code>-P</code> <i>posttext</i> may be used to replace the text before and after the display for the duration of the function; either or both may be an empty string. </p>
<p> If the option <code>-n</code> is also given, <i>pretext</i> or <i>posttext</i> will only be inserted if there is text before or after the region respectively which will be made invisible. </p>
<p> Two numeric arguments may be given which will be used instead of the cursor and mark positions. </p>
<p> The option <code>-S</code> <i>statepm</i> is used to narrow according to the other options while saving the original state in the parameter with name <i>statepm</i>, while the option <code>-R</code> <i>statepm</i> is used to restore the state from the parameter; note in both cases the <i>name</i> of the parameter is required. In the second case, other options and arguments are irrelevant. When this method is used, no <code>recursive-edit</code> is performed; the calling widget should call this function with the option <code>-S</code>, perform its own editing on the command line or pass control to the user via `<code>zle recursive-edit</code>&#8216;, then call this function with the option <code>-R</code>. The argument <i>statepm</i> must be a suitable name for an ordinary parameter, except that parameters beginning with the prefix <code>_ntr_</code> are reserved for use within <code>narrow-to-region</code>. Typically the parameter will be local to the calling function. </p>
<p> The options <code>-l</code> <i>lbufvar</i> and <code>-r</code> <i>rbufvar</i> may be used to specify parameters where the widget will store the resulting text from the operation. The parameter <i>lbufvar</i> will contain <code>LBUFFER</code> and <i>rbufvar</i> will contain <code>RBUFFER</code>. Neither of these two options may be used with <code>-S</code> or <code>-R</code>. </p>
<p> <code>narrow-to-region-invisible</code> is a simple widget which calls <code>narrow-to-region</code> with arguments which replace any text outside the region with `<code>&#8230;</code>&#8216;. It does not take any arguments. </p>
<p> The display is restored (and the widget returns) upon any zle command which would usually cause the line to be accepted or aborted. Hence an additional such command is required to accept or abort the current line. </p>
<p> The return status of both widgets is zero if the line was accepted, else non-zero. </p>
<p> Here is a trivial example of a widget using this feature.</p>
<dl>
<dt>
<dd>
<pre>
<code>local state
narrow-to-region -p $'Editing restricted region
' \ 
  -P '' -S state
zle recursive-edit
narrow-to-region -R state</code>
</pre>
</dl>
</dl>
<dt><code>predict-on</code></p>
<dd> This set of functions implements predictive typing using history search. After <code>predict-on</code>, typing characters causes the editor to look backward in the history for the first line beginning with what you have typed so far. After <code>predict-off</code>, editing returns to normal for the line found. In fact, you often don&#8217;t even need to use <code>predict-off</code>, because if the line doesn&#8217;t match something in the history, adding a key performs standard completion, and then inserts itself if no completions were found. However, editing in the middle of a line is liable to confuse prediction; see the <code>toggle</code> style below.</p>
<dl>
<dt>
<dd>
<p> With the function based completion system (which is needed for this), you should be able to type <code>TAB</code> at almost any point to advance the cursor to the next &#8220;interesting&#8221; character position (usually the end of the current word, but sometimes somewhere in the middle of the word). And of course as soon as the entire line is what you want, you can accept with return, without needing to move the cursor to the end first. </p>
<p> The first time <code>predict-on</code> is used, it creates several additional widget functions: </p>
<dl>
<dt><code>delete-backward-and-predict</code></p>
<dd> Replaces the <code>backward-delete-char</code> widget. You do not need to bind this yourself.</p>
<dt><code>insert-and-predict</code></p>
<dd> Implements predictive typing by replacing the <code>self-insert</code> widget. You do not need to bind this yourself.</p>
<dt><code>predict-off</code></p>
<dd> Turns off predictive typing.</dl>
<p> Although you <code>autoload</code> only the <code>predict-on</code> function, it is necessary to create a keybinding for <code>predict-off</code> as well. </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -N predict-on
zle -N predict-off
bindkey '^X^Z' predict-on
bindkey '^Z' predict-off</code>
</pre>
</dl>
</dl>
<dt><code>read-from-minibuffer</code></p>
<dd> This is most useful when called as a function from inside a widget, but will work correctly as a widget in its own right. It prompts for a value below the current command line; a value may be input using all of the standard zle operations (and not merely the restricted set available when executing, for example, <code>execute-named-cmd</code>). The value is then returned to the calling function in the parameter <code>$REPLY</code> and the editing buffer restored to its previous state. If the read was aborted by a keyboard break (typically <code>^G</code>), the function returns status 1 and <code>$REPLY</code> is not set.</p>
<dl>
<dt>
<dd>
<p> If one argument is supplied to the function it is taken as a prompt, otherwise `<code>? </code>&#8216; is used. If two arguments are supplied, they are the prompt and the initial value of <code>$LBUFFER</code>, and if a third argument is given it is the initial value of <code>$RBUFFER</code>. This provides a default value and starting cursor placement. Upon return the entire buffer is the value of <code>$REPLY</code>. </p>
<p> One option is available: `<code>-k</code> <i>num</i>&#8216; specifies that <i>num</i> characters are to be read instead of a whole line. The line editor is not invoked recursively in this case, so depending on the terminal settings the input may not be visible, and only the input keys are placed in <code>$REPLY</code>, not the entire buffer. Note that unlike the <code>read</code> builtin <i>num</i> must be given; there is no default. </p>
<p> The name is a slight misnomer, as in fact the shell&#8217;s own minibuffer is not used. Hence it is still possible to call <code>executed-named-cmd</code> and similar functions while reading a value.</dl>
<dt><code>replace-argument</code>, <code>replace-argument-edit</code></p>
<dd> The function <code>replace-argument</code> can be used to replace a command line argument in the current command line or, if the current command line is empty, in the last command line executed (the new command line is not executed). Arguments are as delimited by standard shell syntax,</p>
<dl>
<dt>
<dd>
<p> If a numeric argument is given, that specifies the argument to be replaced. 0 means the command name, as in history expansion. A negative numeric argument counts backward from the last word. </p>
<p> If no numeric argument is given, the current argument is replaced; this is the last argument if the previous history line is being used. </p>
<p> The function prompts for a replacement argument. </p>
<p> If the widget contains the string <code>edit</code>, for example is defined as </p>
<dl>
<dt>
<dd>
<pre>
<code>zle -N replace-argument-edit replace-argument</code>
</pre>
</dl>
<p> then the function presents the current value of the argument for editing, otherwise the editing buffer for the replacement is initially empty.</dl>
<dt>
<dd> <code>replace-string</code>, <code>replace-pattern</code></p>
<dt>
<dd> <code>replace-string-again</code>, <code>replace-pattern-again</code> The function <code>replace-string</code> implements three widgets. If defined under the same name as the function, it prompts for two strings; the first (source) string will be replaced by the second everywhere it occurs in the line editing buffer.</p>
<dl>
<dt>
<dd>
<p> If the widget name contains the word `<code>pattern</code>&#8216;, for example by defining the widget using the command `<code>zle -N replace-pattern replace-string</code>&#8216;, then the matching is performed using zsh patterns. All zsh extended globbing patterns can be used in the source string; note that unlike filename generation the pattern does not need to match an entire word, nor do glob qualifiers have any effect. In addition, the replacement string can contain parameter or command substitutions. Furthermore, a `<code>&amp;</code>&#8216; in the replacement string will be replaced with the matched source string, and a backquoted digit `<code>\</code><i>N</i>&#8216; will be replaced by the <i>N</i>th parenthesised expression matched. The form `<code>\{</code><i>N</i><code>}</code>&#8216; may be used to protect the digit from following digits. </p>
<p> If the widget instead contains the word `<code>regex</code>&#8216; (or `<code>regexp</code>&#8216;), then the matching is performed using regular expressions, respecting the setting of the option <code>RE_MATCH_PCRE</code> (see the description of the function <code>regexp-replace</code> below). The special replacement facilities described above for pattern matching are available. </p>
<p> By default the previous source or replacement string will not be offered for editing. However, this feature can be activated by setting the style <code>edit-previous</code> in the context <code>:zle:</code><i>widget</i> (for example, <code>:zle:replace-string</code>) to <code>true</code>. In addition, a positive numeric argument forces the previous values to be offered, a negative or zero argument forces them not to be. </p>
<p> The function <code>replace-string-again</code> can be used to repeat the previous replacement; no prompting is done. As with <code>replace-string</code>, if the name of the widget contains the word `<code>pattern</code>&#8216; or `<code>regex</code>&#8216;, pattern or regular expression matching is performed, else a literal string replacement. Note that the previous source and replacement text are the same whether pattern, regular expression or string matching is used. </p>
<p> In addition, <code>replace-string</code> shows the previous replacement above the prompt, so long as there was one during the current session; if the source string is empty, that replacement will be repeated without the widget prompting for a replacement string. </p>
<p> For example, starting from the line: </p>
<dl>
<dt>
<dd>
<pre>
<code>print This line contains fan and fond</code>
</pre>
</dl>
<p> and invoking <code>replace-pattern</code> with the source string `<code>f(?)n</code>&#8216; and the replacement string `<code>c\1r</code>&#8216; produces the not very useful line: </p>
<dl>
<dt>
<dd>
<pre>
<code>print This line contains car and cord</code>
</pre>
</dl>
<p> The range of the replacement string can be limited by using the <code>narrow-to-region-invisible</code> widget. One limitation of the current version is that <code>undo</code> will cycle through changes to the replacement and source strings before undoing the replacement itself.</dl>
<dt><code>send-invisible</code></p>
<dd> This is similar to read-from-minibuffer in that it may be called as a function from a widget or as a widget of its own, and interactively reads input from the keyboard. However, the input being typed is concealed and a string of asterisks (`<code>*</code>&#8216;) is shown instead. The value is saved in the parameter <code>$INVISIBLE</code> to which a reference is inserted into the editing buffer at the restored cursor position. If the read was aborted by a keyboard break (typically <code>^G</code>) or another escape from editing such as <code>push-line</code>, <code>$INVISIBLE</code> is set to empty and the original buffer is restored unchanged.</p>
<dl>
<dt>
<dd>
<p> If one argument is supplied to the function it is taken as a prompt, otherwise `<code>Non-echoed text: </code>&#8216; is used (as in emacs). If a second and third argument are supplied they are used to begin and end the reference to <code>$INVISIBLE</code> that is inserted into the buffer. The default is to open with <code>${</code>, then <code>INVISIBLE</code>, and close with <code>}</code>, but many other effects are possible.</dl>
<dt><code>smart-insert-last-word</code></p>
<dd> This function may replace the <code>insert-last-word</code> widget, like so:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zle -N insert-last-word smart-insert-last-word</code>
</pre>
</dl>
<p> With a numeric argument, or when passed command line arguments in a call from another widget, it behaves like <code>insert-last-word</code>, except that words in comments are ignored when <code>INTERACTIVE_COMMENTS</code> is set. </p>
<p> Otherwise, the rightmost &#8220;interesting&#8221; word from the previous command is found and inserted. The default definition of &#8220;interesting&#8221; is that the word contains at least one alphabetic character, slash, or backslash. This definition may be overridden by use of the <code>match</code> style. The context used to look up the style is the widget name, so usually the context is <code>:insert-last-word</code>. However, you can bind this function to different widgets to use different patterns: </p>
<dl>
<dt>
<dd>
zle &#8211; N insert &#8211; last &#8211; assignment smart &#8211; insert &#8211; last &#8211; word zstyle : insert &#8211; last &#8211; assignment match &#8216;[[:alpha:]][][[:alnum:]]#=*&#8217; bindkey &#8216;=&#8217; insert &#8211; last &#8211; assignment
</dl>
<p> If no interesting word is found and the <code>auto-previous</code> style is set to a true value, the search continues upward through the history. When <code>auto-previous</code> is unset or false (the default), the widget must be invoked repeatedly in order to search earlier history lines.</dl>
<dt><code>transpose-lines</code></p>
<dd> Only useful with a multi-line editing buffer; the lines here are lines within the current on-screen buffer, not history lines. The effect is similar to the function of the same name in Emacs.</p>
<dl>
<dt>
<dd>
<p> Transpose the current line with the previous line and move the cursor to the start of the next line. Repeating this (which can be done by providing a positive numeric argument) has the effect of moving the line above the cursor down by a number of lines. </p>
<p> With a negative numeric argument, requires two lines above the cursor. These two lines are transposed and the cursor moved to the start of the previous line. Using a numeric argument less than -1 has the effect of moving the line above the cursor up by minus that number of lines.</dl>
<dt><code>url-quote-magic</code></p>
<dd> This widget replaces the built-in <code>self-insert</code> to make it easier to type URLs as command line arguments. As you type, the input character is analyzed and, if it may need quoting, the current word is checked for a URI scheme. If one is found and the current word is not already in quotes, a backslash is inserted before the input character.</p>
<dl>
<dt>
<dd>
<p> Styles to control quoting behavior: </p>
<dl>
<dt>
<dd> <code>url-metas</code> This style is looked up in the context `<code>:url-quote-magic:</code><i>scheme</i>&#8216; (where <i>scheme</i> is that of the current URL, e.g. &quot;<code>ftp</code>&quot;). The value is a string listing the characters to be treated as globbing metacharacters when appearing in a URL using that scheme. The default is to quote all zsh extended globbing characters, excluding &#8216;<code>&lt;</code>&#8216; and &#8216;<code>&gt;</code>&#8216; but including braces (as in brace expansion). See also <code>url-seps</code>.</p>
<dt><code>url-seps</code></p>
<dd> Like <code>url-metas</code>, but lists characters that should be considered command separators, redirections, history references, etc. The default is to quote the standard set of shell separators, excluding those that overlap with the extended globbing characters, but including &#8216;<code>&lt;</code>&#8216; and &#8216;<code>&gt;</code>&#8216; and the first character of <code>$histchars</code>.</p>
<dt><code>url-globbers</code></p>
<dd> This style is looked up in the context `<code>:url-quote-magic</code>&#8216;. The values form a list of command names that are expected to do their own globbing on the URL string. This implies that they are aliased to use the `<code>noglob</code>&#8216; modifier. When the first word on the line matches one of the values <i>and</i> the URL refers to a local file (see <code>url-local-schema</code>), only the <code>url-seps</code> characters are quoted; the <code>url-metas</code> are left alone, allowing them to affect command-line parsing, completion, etc. The default values are a literal `<code>noglob</code>&#8216; plus (when the <code>zsh/parameter</code> module is available) any commands aliased to the helper function `<code>urlglobber</code>&#8216; or its alias `<code>globurl</code>&#8216;.</p>
<dt><code>url-local-schema</code></p>
<dd> This style is always looked up in the context `<code>:urlglobber</code>&#8216;, even though it is used by both url-quote-magic and urlglobber. The values form a list of URI schema that should be treated as referring to local files by their real local path names, as opposed to files which are specified relative to a web-server-defined document root. The defaults are &quot;<code>ftp</code>&quot; and &quot;<code>file</code>&quot;.</p>
<dt><code>url-other-schema</code></p>
<dd> Like <code>url-local-schema</code>, but lists all other URI schema upon which <code>urlglobber</code> and <code>url-quote-magic</code> should act. If the URI on the command line does not have a scheme appearing either in this list or in <code>url-local-schema</code>, it is not magically quoted. The default values are &quot;<code>http</code>&quot;, &quot;<code>https</code>&quot;, and &quot;<code>ftp</code>&quot;. When a scheme appears both here and in <code>url-local-schema</code>, it is quoted differently depending on whether the command name appears in <code>url-globbers</code>.</dl>
<p> Loading <code>url-quote-magic</code> also defines a helper function `<code>urlglobber</code>&#8216; and aliases `<code>globurl</code>&#8216; to `<code>noglob urlglobber</code>&#8216;. This function takes a local URL apart, attempts to pattern-match the local file portion of the URL path, and then puts the results back into URL format again.</dl>
<dt><code>vi-pipe</code></p>
<dd> This function reads a movement command from the keyboard and then prompts for an external command. The part of the buffer covered by the movement is piped to the external command and then replaced by the command&#8217;s output. If the movement command is bound to vi-pipe, the current line is used.</p>
<dl>
<dt>
<dd>
<p> The function serves as an example for reading a vi movement command from within a user-defined widget.</dl>
<dt><code>which-command</code></p>
<dd> This function is a drop-in replacement for the builtin widget <code>which-command</code>. It has enhanced behaviour, in that it correctly detects whether or not the command word needs to be expanded as an alias; if so, it continues tracing the command word from the expanded alias until it reaches the command that will be executed.</p>
<dl>
<dt>
<dd>
<p> The style <code>whence</code> is available in the context <code>:zle:$WIDGET</code>; this may be set to an array to give the command and options that will be used to investigate the command word found. The default is <code>whence -c</code>.</dl>
<dt><code>zcalc-auto-insert</code></p>
<dd> This function is useful together with the <code>zcalc</code> function described in the section Mathematical Functions. It should be bound to a key representing a binary operator such as `<code>+</code>&#8216;, `<code>&#8211;</code>&#8216;, `<code>*</code>&#8216; or `<code>/</code>&#8216;. When running in zcalc, if the key occurs at the start of the line or immediately following an open parenthesis, the text <code>&quot;ans &quot;</code> is inserted before the representation of the key itself. This allows easy use of the answer from the previous calculation in the current line. The text to be inserted before the symbol typed can be modified by setting the variable <code>ZCALC_AUTO_INSERT_PREFIX</code>.</p>
<dl>
<dt>
<dd>
<p> Hence, for example, typing `<code>+12</code>&#8216; followed by return adds 12 to the previous result. </p>
<p> If zcalc is in RPN mode (<code>-r</code> option) the effect of this binding is automatically suppressed as operators alone on a line are meaningful. </p>
<p> When not in zcalc, the key simply inserts the symbol itself.</dl>
</dl>
<h3>Utility Functions</h3>
<p> These functions are useful in constructing widgets. They should be loaded with `<code>autoload -U</code> <i>function</i>&#8216; and called as indicated from user-defined widgets. </p>
<dl>
<dt>
<dd> <code>split-shell-arguments</code> This function splits the line currently being edited into shell arguments and whitespace. The result is stored in the array <code>reply</code>. The array contains all the parts of the line in order, starting with any whitespace before the first argument, and finishing with any whitespace after the last argument. Hence (so long as the option <code>KSH_ARRAYS</code> is not set) whitespace is given by odd indices in the array and arguments by even indices. Note that no stripping of quotes is done; joining together all the elements of <code>reply</code> in order is guaranteed to produce the original line.</p>
<dl>
<dt>
<dd>
<p> The parameter <code>REPLY</code> is set to the index of the word in <code>reply</code> which contains the character after the cursor, where the first element has index 1. The parameter <code>REPLY2</code> is set to the index of the character under the cursor in that word, where the first character has index 1. </p>
<p> Hence <code>reply</code>, <code>REPLY</code> and <code>REPLY2</code> should all be made local to the enclosing function. </p>
<p> See the function <code>modify-current-argument</code>, described below, for an example of how to call this function.</dl>
<dt><code>modify-current-argument</code> [ <i>expr-using-</i><code>$ARG</code> | <i>func</i> ]</p>
<dd> This function provides a simple method of allowing user-defined widgets to modify the command line argument under the cursor (or immediately to the left of the cursor if the cursor is between arguments).</p>
<dl>
<dt>
<dd>
<p> The argument can be an expression which when evaluated operates on the shell parameter <code>ARG</code>, which will have been set to the command line argument under the cursor. The expression should be suitably quoted to prevent it being evaluated too early. </p>
<p> Alternatively, if the argument does not contain the string <code>ARG</code>, it is assumed to be a shell function, to which the current command line argument is passed as the only argument. The function should set the variable <code>REPLY</code> to the new value for the command line argument. If the function returns non-zero status, so does the calling function. </p>
<p> For example, a user-defined widget containing the following code converts the characters in the argument under the cursor into all upper case: </p>
<dl>
<dt>
<dd>
<pre>
<code>modify-current-argument '${(U)ARG}'</code>
</pre>
</dl>
<p> The following strips any quoting from the current word (whether backslashes or one of the styles of quotes), and replaces it with single quoting throughout: </p>
<dl>
<dt>
<dd>
modify &#8211; current &#8211; argument &#8216;${(qq)${(Q)ARG}}&#8217;
</dl>
<p> The following performs directory expansion on the command line argument and replaces it by the absolute path: </p>
<dl>
<dt>
<dd>
expand &#8211; dir()<br />
{<br />
    REPLY = ${~1} REPLY = $<br />
    {<br />
    REPLY:<br />
        a<br />
    }<br />
}<br />
modify &#8211; current &#8211; argument expand &#8211; dir
</dl>
<p> In practice the function <code>expand-dir</code> would probably not be defined within the widget where <code>modify-current-argument</code> is called.</dl>
</dl>
<h3>Styles</h3>
<p> The behavior of several of the above widgets can be controlled by the use of the <code>zstyle</code> mechanism. In particular, widgets that interact with the completion system pass along their context to any completions that they invoke. </p>
<dl>
<dt>
<dd> <code>break-keys</code> This style is used by the <code>incremental-complete-word</code> widget. Its value should be a pattern, and all keys matching this pattern will cause the widget to stop incremental completion without the key having any further effect. Like all styles used directly by <code>incremental-complete-word</code>, this style is looked up using the context `<code>:incremental</code>&#8216;.</p>
<dt><code>completer</code></p>
<dd> The <code>incremental-complete-word</code> and <code>insert-and-predict</code> widgets set up their top-level context name before calling completion. This allows one to define different sets of completer functions for normal completion and for these widgets. For example, to use completion, approximation and correction for normal completion, completion and correction for incremental completion and only completion for prediction one could use:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':completion:*' completer \ 
        _complete _correct _approximate
zstyle ':completion:incremental:*' completer \ 
        _complete _correct
zstyle ':completion:predict:*' completer \ 
        _complete</code>
</pre>
</dl>
<p> It is a good idea to restrict the completers used in prediction, because they may be automatically invoked as you type. The <code>_list</code> and <code>_menu</code> completers should never be used with prediction. The <code>_approximate</code>, <code>_correct</code>, <code>_expand</code>, and <code>_match</code> completers may be used, but be aware that they may change characters anywhere in the word behind the cursor, so you need to watch carefully that the result is what you intended.</dl>
<dt><code>cursor</code></p>
<dd> The <code>insert-and-predict</code> widget uses this style, in the context `<code>:predict</code>&#8216;, to decide where to place the cursor after completion has been tried. Values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>complete</code> The cursor is left where it was when completion finished, but only if it is after a character equal to the one just inserted by the user. If it is after another character, this value is the same as `<code>key</code>&#8216;.</p>
<dt><code>key</code></p>
<dd> The cursor is left after the <i>n</i>th occurrence of the character just inserted, where <i>n</i> is the number of times that character appeared in the word before completion was attempted. In short, this has the effect of leaving the cursor after the character just typed even if the completion code found out that no other characters need to be inserted at that position.</dl>
<p> Any other value for this style unconditionally leaves the cursor at the position where the completion code left it.</dl>
<dt><code>list</code></p>
<dd> When using the <code>incremental-complete-word</code> widget, this style says if the matches should be listed on every key press (if they fit on the screen). Use the context prefix `<code>:completion:incremental</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> The <code>insert-and-predict</code> widget uses this style to decide if the completion should be shown even if there is only one possible completion. This is done if the value of this style is the string <code>always</code>. In this case the context is `<code>:predict</code>&#8216; (<i>not</i> `<code>:completion:predict</code>&#8216;).</dl>
<dt><code>match</code></p>
<dd> This style is used by <code>smart-insert-last-word</code> to provide a pattern (using full <code>EXTENDED_GLOB</code> syntax) that matches an interesting word. The context is the name of the widget to which <code>smart-insert-last-word</code> is bound (see above). The default behavior of <code>smart-insert-last-word</code> is equivalent to:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
zstyle : insert &#8211; last &#8211; word match &#8216;*[[:alpha:]/\]*&#8217;
</dl>
<p> However, you might want to include words that contain spaces: </p>
<dl>
<dt>
<dd>
zstyle : insert &#8211; last &#8211; word match &#8216;*[[:alpha:][:space:]/\]*&#8217;
</dl>
<p> Or include numbers as long as the word is at least two characters long: </p>
<dl>
<dt>
<dd>
zstyle : insert &#8211; last &#8211; word match &#8216;*([[:digit:]]?|[[:alpha:]/\])*&#8217;
</dl>
<p> The above example causes redirections like &quot;2&gt;&quot; to be included.</dl>
<dt><code>prompt</code></p>
<dd> The <code>incremental-complete-word</code> widget shows the value of this style in the status line during incremental completion. The string value may contain any of the following substrings in the manner of the <code>PS1</code> and other prompt parameters:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>%c</code> Replaced by the name of the completer function that generated the matches (without the leading underscore).</p>
<dt><code>%l</code></p>
<dd> When the <code>list</code> style is set, replaced by `<code>&#8230;</code>&#8216; if the list of matches is too long to fit on the screen and with an empty string otherwise. If the <code>list</code> style is `false&#8217; or not set, `<code>%l</code>&#8216; is always removed.</p>
<dt><code>%n</code></p>
<dd> Replaced by the number of matches generated.</p>
<dt><code>%s</code></p>
<dd> Replaced by `<code>-no match-</code>&#8216;, `<code>-no prefix-</code>&#8216;, or an empty string if there is no completion matching the word on the line, if the matches have no common prefix different from the word on the line, or if there is such a common prefix, respectively.</p>
<dt><code>%u</code></p>
<dd> Replaced by the unambiguous part of all matches, if there is any, and if it is different from the word on the line.</dl>
<p> Like `<code>break-keys</code>&#8216;, this uses the `<code>:incremental</code>&#8216; context.</dl>
<dt><code>stop-keys</code></p>
<dd> This style is used by the <code>incremental-complete-word</code> widget. Its value is treated similarly to the one for the <code>break-keys</code> style (and uses the same context: `<code>:incremental</code>&#8216;). However, in this case all keys matching the pattern given as its value will stop incremental completion and will then execute their usual function.</p>
<dt><code>toggle</code></p>
<dd> This boolean style is used by <code>predict-on</code> and its related widgets in the context `<code>:predict</code>&#8216;. If set to one of the standard `true&#8217; values, predictive typing is automatically toggled off in situations where it is unlikely to be useful, such as when editing a multi-line buffer or after moving into the middle of a line and then deleting a character. The default is to leave prediction turned on until an explicit call to <code>predict-off</code>.</p>
<dt><code>verbose</code></p>
<dd> This boolean style is used by <code>predict-on</code> and its related widgets in the context `<code>:predict</code>&#8216;. If set to one of the standard `true&#8217; values, these widgets display a message below the prompt when the predictive state is toggled. This is most useful in combination with the <code>toggle</code> style. The default does not display these messages.</p>
<dt><code>widget</code></p>
<dd> This style is similar to the <code>command</code> style: For widget functions that use <code>zle</code> to call other widgets, this style can sometimes be used to override the widget which is called. The context for this style is the name of the calling widget (<i>not</i> the name of the calling function, because one function may be bound to multiple widget names).</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle :copy-earlier-word widget smart-insert-last-word</code>
</pre>
</dl>
<p> Check the documentation for the calling widget or function to determine whether the <code>widget</code> style is used.</dl>
</dl>
<h2>EXCEPTION HANDLING</h2>
<p> Two functions are provided to enable zsh to provide exception handling in a form that should be familiar from other languages. </p>
<dl>
<dt>
<dd> <code>throw</code> <i>exception</i> The function <code>throw</code> throws the named <i>exception</i>. The name is an arbitrary string and is only used by the <code>throw</code> and <code>catch</code> functions. An exception is for the most part treated the same as a shell error, i.e. an unhandled exception will cause the shell to abort all processing in a function or script and to return to the top level in an interactive shell.</p>
<dt><code>catch</code> <i>exception-pattern</i></p>
<dd> The function <code>catch</code> returns status zero if an exception was thrown and the pattern <i>exception-pattern</i> matches its name. Otherwise it returns status 1. <i>exception-pattern</i> is a standard shell pattern, respecting the current setting of the <code>EXTENDED_GLOB</code> option. An alias <code>catch</code> is also defined to prevent the argument to the function from matching filenames, so patterns may be used unquoted. Note that as exceptions are not fundamentally different from other shell errors it is possible to catch shell errors by using an empty string as the exception name. The shell variable <code>CAUGHT</code> is set by <code>catch</code> to the name of the exception caught. It is possible to rethrow an exception by calling the <code>throw</code> function again once an exception has been caught.</dl>
<p> The functions are designed to be used together with the <code>always</code> construct described in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). This is important as only this construct provides the required support for exceptions. A typical example is as follows. </p>
<dl>
<dt>
<dd>
{<br />
#&#8221;try&#8221; block<br />
#&#8230; nested code here calls &#8220;throw MyExcept&#8221;<br />
} always<br />
{<br />
#&#8221;always&#8221; block<br />
    if<br />
        catch MyExcept;<br />
    then<br />
        print &#8220;Caught exception MyExcept&#8221; elif catch &#8221;;<br />
    then<br />
        print &#8220;Caught a shell error.  Propagating&#8230;&#8221; throw &#8221; fi<br />
#Other exceptions are not handled but may be caught further<br />
#up the call stack.<br />
}
</dl>
<p> If all exceptions should be caught, the following idiom might be preferable. </p>
<dl>
<dt>
<dd>
{<br />
#&#8230; nested code here throws an exception<br />
} always<br />
{<br />
    if<br />
        catch *;<br />
    then case $CAUGHT in(MyExcept)<br />
        print &#8220;Caught my own exception&#8221;;<br />
    ;<br />
    (*)<br />
        print &#8220;Caught some other exception&#8221;;<br />
    ;<br />
    esac<br />
        fi<br />
}
</dl>
<p> In common with exception handling in other languages, the exception may be thrown by code deeply nested inside the `try&#8217; block. However, note that it must be thrown inside the current shell, not in a subshell forked for a pipeline, parenthesised current-shell construct, or some form of command or process substitution. </p>
<p> The system internally uses the shell variable <code>EXCEPTION</code> to record the name of the exception between throwing and catching. One drawback of this scheme is that if the exception is not handled the variable <code>EXCEPTION</code> remains set and may be incorrectly recognised as the name of an exception if a shell error subsequently occurs. Adding <code>unset EXCEPTION</code> at the start of the outermost layer of any code that uses exception handling will eliminate this problem. </p>
<h2>MIME FUNCTIONS</h2>
<p> Three functions are available to provide handling of files recognised by extension, for example to dispatch a file <code>text.ps</code> when executed as a command to an appropriate viewer. </p>
<dl>
<dt>
<dd> <code>zsh-mime-setup</code> [ <code>-fv</code> ] [ <code>-l</code> [ <i>suffix</i> &#8230; ] ]</p>
<dt>
<dd> <code>zsh-mime-handler</code> [ <code>-l</code> ] <i>command argument</i> &#8230; These two functions use the files <code>~/.mime.types</code> and <code>/etc/mime.types</code>, which associate types and extensions, as well as <code>~/.mailcap</code> and <code>/etc/mailcap</code> files, which associate types and the programs that handle them. These are provided on many systems with the Multimedia Internet Mail Extensions.</p>
<dl>
<dt>
<dd>
<p> To enable the system, the function <code>zsh-mime-setup</code> should be autoloaded and run. This allows files with extensions to be treated as executable; such files be completed by the function completion system. The function <code>zsh-mime-handler</code> should not need to be called by the user. </p>
<p> The system works by setting up suffix aliases with `<code>alias -s</code>&#8216;. Suffix aliases already installed by the user will not be overwritten. </p>
<p> For suffixes defined in lower case, upper case variants will also automatically be handled (e.g. <code>PDF</code> is automatically handled if handling for the suffix <code>pdf</code> is defined), but not vice versa. </p>
<p> Repeated calls to <code>zsh-mime-setup</code> do not override the existing mapping between suffixes and executable files unless the option <code>-f</code> is given. Note, however, that this does not override existing suffix aliases assigned to handlers other than <code>zsh-mime-handler</code>. </p>
<p> Calling <code>zsh-mime-setup</code> with the option <code>-l</code> lists the existing mappings without altering them. Suffixes to list (which may contain pattern characters that should be quoted from immediate interpretation on the command line) may be given as additional arguments, otherwise all suffixes are listed. </p>
<p> Calling <code>zsh-mime-setup</code> with the option <code>-v</code> causes verbose output to be shown during the setup operation. </p>
<p> The system respects the <code>mailcap</code> flags <code>needsterminal</code> and <code>copiousoutput</code>, see <i><a href="/docs/linux/man/4-mailcap/">mailcap</a></i>(4). </p>
<p> The functions use the following styles, which are defined with the <code>zstyle</code> builtin command (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). They should be defined before <code>zsh-mime-setup</code> is run. The contexts used all start with <code>:mime:</code>, with additional components in some cases. It is recommended that a trailing <code>*</code> (suitably quoted) be appended to style patterns in case the system is extended in future. Some examples are given below. </p>
<p> For files that have multiple suffixes, e.g. <code>.pdf.gz</code>, where the context includes the suffix it will be looked up starting with the longest possible suffix until a match for the style is found. For example, if <code>.pdf.gz</code> produces a match for the handler, that will be used; otherwise the handler for <code>.gz</code> will be used. Note that, owing to the way suffix aliases work, it is always required that there be a handler for the shortest possible suffix, so in this example <code>.pdf.gz</code> can only be handled if <code>.gz</code> is also handled (though not necessarily in the same way). Alternatively, if no handling for <code>.gz</code> on its own is needed, simply adding the command </p>
<dl>
<dt>
<dd>
<pre>
<code>alias -s gz=zsh-mime-handler</code>
</pre>
</dl>
<p> to the initialisation code is sufficient; <code>.gz</code> will not be handled on its own, but may be in combination with other suffixes. </p>
<dl>
<dt>
<dd> <code>current-shell</code> If this boolean style is true, the mailcap handler for the context in question is run using the <code>eval</code> builtin instead of by starting a new <code>sh</code> process. This is more efficient, but may not work in the occasional cases where the mailcap handler uses strict POSIX syntax.</p>
<dt><code>disown</code></p>
<dd> If this boolean style is true, mailcap handlers started in the background will be disowned, i.e. not subject to job control within the parent shell. Such handlers nearly always produce their own windows, so the only likely harmful side effect of setting the style is that it becomes harder to kill jobs from within the shell.</p>
<dt><code>execute-as-is</code></p>
<dd> This style gives a list of patterns to be matched against files passed for execution with a handler program. If the file matches the pattern, the entire command line is executed in its current form, with no handler. This is useful for files which might have suffixes but nonetheless be executable in their own right. If the style is not set, the pattern <code>*(*) *(/)</code> is used; hence executable files are executed directly and not passed to a handler, and the option <code>AUTO_CD</code> may be used to change to directories that happen to have MIME suffixes.</p>
<dt><code>execute-never</code></p>
<dd> This style is useful in combination with <code>execute-as-is</code>. It is set to an array of patterns corresponding to full paths to files that should never be treated as executable, even if the file passed to the MIME handler matches <code>execute-as-is</code>. This is useful for file systems that don&#8217;t handle execute permission or that contain executables from another operating system. For example, if <code>/mnt/windows</code> is a Windows mount, then</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':mime:*' execute-never '/mnt/windows/*'</code>
</pre>
</dl>
<p> will ensure that any files found in that area will be executed as MIME types even if they are executable. As this example shows, the complete file name is matched against the pattern, regardless of how the file was passed to the handler. The file is resolved to a full path using the <code>:P</code> modifier described in the subsection Modifiers in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1); this means that symbolic links are resolved where possible, so that links into other file systems behave in the correct fashion.</dl>
<dt><code>file-path</code></p>
<dd> Used if the style <code>find-file-in-path</code> is true for the same context. Set to an array of directories that are used for searching for the file to be handled; the default is the command path given by the special parameter <code>path</code>. The shell option <code>PATH_DIRS</code> is respected; if that is set, the appropriate path will be searched even if the name of the file to be handled as it appears on the command line contains a `<code>/</code>&#8216;. The full context is <code>:mime:.</code><i>suffix</i><code>:</code>, as described for the style <code>handler</code>.</p>
<dt><code>find-file-in-path</code></p>
<dd> If set, allows files whose names do not contain absolute paths to be searched for in the command path or the path specified by the <code>file-path</code> style. If the file is not found in the path, it is looked for locally (whether or not the current directory is in the path); if it is not found locally, the handler will abort unless the <code>handle-nonexistent</code> style is set. Files found in the path are tested as described for the style <code>execute-as-is</code>. The full context is <code>:mime:.</code><i>suffix</i><code>:</code>, as described for the style <code>handler</code>.</p>
<dt><code>flags</code></p>
<dd> Defines flags to go with a handler; the context is as for the <code>handler</code> style, and the format is as for the flags in <code>mailcap</code>.</p>
<dt><code>handle-nonexistent</code></p>
<dd> By default, arguments that don&#8217;t correspond to files are not passed to the MIME handler in order to prevent it from intercepting commands found in the path that happen to have suffixes. This style may be set to an array of extended glob patterns for arguments that will be passed to the handler even if they don&#8217;t exist. If it is not explicitly set it defaults to <code>[[:alpha:]]#:/*</code> which allows URLs to be passed to the MIME handler even though they don&#8217;t exist in that format in the file system. The full context is <code>:mime:.</code><i>suffix</i><code>:</code>, as described for the style <code>handler</code>.</p>
<dt><code>handler</code></p>
<dd> Specifies a handler for a suffix; the suffix is given by the context as <code>:mime:.</code><i>suffix</i><code>:</code>, and the format of the handler is exactly that in <code>mailcap</code>. Note in particular the `<code>.</code>&#8216; and trailing colon to distinguish this use of the context. This overrides any handler specified by the <code>mailcap</code> files. If the handler requires a terminal, the <code>flags</code> style should be set to include the word <code>needsterminal</code>, or if the output is to be displayed through a pager (but not if the handler is itself a pager), it should include <code>copiousoutput</code>.</p>
<dt><code>mailcap</code></p>
<dd> A list of files in the format of <code>~/.mailcap</code> and <code>/etc/mailcap</code> to be read during setup, replacing the default list which consists of those two files. The context is <code>:mime:</code>. A <code>+</code> in the list will be replaced by the default files.</p>
<dt><code>mailcap-priorities</code></p>
<dd> This style is used to resolve multiple mailcap entries for the same MIME type. It consists of an array of the following elements, in descending order of priority; later entries will be used if earlier entries are unable to resolve the entries being compared. If none of the tests resolve the entries, the first entry encountered is retained.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>files</code> The order of files (entries in the <code>mailcap</code> style) read. Earlier files are preferred. (Note this does not resolve entries in the same file.)</p>
<dt><code>priority</code></p>
<dd> The priority flag from the mailcap entry. The priority is an integer from 0 to 9 with the default value being 5.</p>
<dt><code>flags</code></p>
<dd> The test given by the <code>mailcap-prio-flags</code> option is used to resolve entries.</p>
<dt><code>place</code></p>
<dd> Later entries are preferred; as the entries are strictly ordered, this test always succeeds.</dl>
<p> Note that as this style is handled during initialisation, the context is always <code>:mime:</code>, with no discrimination by suffix.</dl>
<dt><code>mailcap-prio-flags</code></p>
<dd> This style is used when the keyword <code>flags</code> is encountered in the list of tests specified by the <code>mailcap-priorities</code> style. It should be set to a list of patterns, each of which is tested against the flags specified in the mailcap entry (in other words, the sets of assignments found with some entries in the mailcap file). Earlier patterns in the list are preferred to later ones, and matched patterns are preferred to unmatched ones.</p>
<dt><code>mime-types</code></p>
<dd> A list of files in the format of <code>~/.mime.types</code> and <code>/etc/mime.types</code> to be read during setup, replacing the default list which consists of those two files. The context is <code>:mime:</code>. A <code>+</code> in the list will be replaced by the default files.</p>
<dt><code>never-background</code></p>
<dd> If this boolean style is set, the handler for the given context is always run in the foreground, even if the flags provided in the mailcap entry suggest it need not be (for example, it doesn&#8217;t require a terminal).</p>
<dt><code>pager</code></p>
<dd> If set, will be used instead of <code>$PAGER</code> or <code>more</code> to handle suffixes where the <code>copiousoutput</code> flag is set. The context is as for <code>handler</code>, i.e. <code>:mime:.</code><i>suffix</i><code>:</code> for handling a file with the given <i>suffix</i>.</dl>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':mime:*' mailcap ~/.mailcap /usr/local/etc/mailcap
zstyle ':mime:.txt:' handler less %s
zstyle ':mime:.txt:' flags needsterminal</code>
</pre>
</dl>
<p> When <code>zsh-mime-setup</code> is subsequently run, it will look for <code>mailcap</code> entries in the two files given. Files of suffix <code>.txt</code> will be handled by running `<code>less</code> <i>file.txt</i>&#8216;. The flag <code>needsterminal</code> is set to show that this program must run attached to a terminal. </p>
<p> As there are several steps to dispatching a command, the following should be checked if attempting to execute a file by extension <code>.</code><i>ext</i> does not have the expected effect. </p>
<p> The command `<code>alias -s</code> <i>ext</i>&#8216; should show `<code>ps=zsh-mime-handler</code>&#8216;. If it shows something else, another suffix alias was already installed and was not overwritten. If it shows nothing, no handler was installed: this is most likely because no handler was found in the <code>.mime.types</code> and <code>mailcap</code> combination for <code>.ext</code> files. In that case, appropriate handling should be added to <code>~/.mime.types</code> and <code>mailcap</code>. </p>
<p> If the extension is handled by <code>zsh-mime-handler</code> but the file is not opened correctly, either the handler defined for the type is incorrect, or the flags associated with it are in appropriate. Running <code>zsh-mime-setup -l</code> will show the handler and, if there are any, the flags. A <code>%s</code> in the handler is replaced by the file (suitably quoted if necessary). Check that the handler program listed lists and can be run in the way shown. Also check that the flags <code>needsterminal</code> or <code>copiousoutput</code> are set if the handler needs to be run under a terminal; the second flag is used if the output should be sent to a pager. An example of a suitable <code>mailcap</code> entry for such a program is: </p>
<dl>
<dt>
<dd>
<pre>
<code>text/html; /usr/bin/lynx '%s'; needsterminal</code>
</pre>
</dl>
<p> Running `<code>zsh-mime-handler -l</code> <i>command line</i>&#8216; prints the command line that would be executed, simplified to remove the effect of any flags, and quoted so that the output can be run as a complete zsh command line. This is used by the completion system to decide how to complete after a file handled by <code>zsh-mime-setup</code>.</dl>
<dt><code>pick-web-browser</code></p>
<dd> This function is separate from the two MIME functions described above and can be assigned directly to a suffix:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>autoload -U pick-web-browser
alias -s html=pick-web-browser</code>
</pre>
</dl>
<p> It is provided as an intelligent front end to dispatch a web browser. It may be run as either a function or a shell script. The status 255 is returned if no browser could be started. </p>
<p> Various styles are available to customize the choice of browsers: </p>
<dl>
<dt>
<dd> <code>browser-style</code> The value of the style is an array giving preferences in decreasing order for the type of browser to use. The values of elements may be</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>running</code> Use a GUI browser that is already running when an X Window display is available. The browsers listed in the <code>x-browsers</code> style are tried in order until one is found; if it is, the file will be displayed in that browser, so the user may need to check whether it has appeared. If no running browser is found, one is not started. Browsers other than Firefox, Opera and Konqueror are assumed to understand the Mozilla syntax for opening a URL remotely.</p>
<dt><code>x</code></p>
<dd> Start a new GUI browser when an X Window display is available. Search for the availability of one of the browsers listed in the <code>x-browsers</code> style and start the first one that is found. No check is made for an already running browser.</p>
<dt><code>tty</code></p>
<dd> Start a terminal-based browser. Search for the availability of one of the browsers listed in the <code>tty-browsers</code> style and start the first one that is found.</dl>
<p> If the style is not set the default <code>running x tty</code> is used.</dl>
<dt><code>x-browsers</code></p>
<dd> An array in decreasing order of preference of browsers to use when running under the X Window System. The array consists of the command name under which to start the browser. They are looked up in the context <code>:mime:</code> (which may be extended in future, so appending `<code>*</code>&#8216; is recommended). For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle ':mime:*' x-browsers opera konqueror firefox</code>
</pre>
</dl>
<p> specifies that <code>pick-web-browser</code> should first look for a running instance of Opera, Konqueror or Firefox, in that order, and if it fails to find any should attempt to start Opera. The default is <code>firefox mozilla netscape opera konqueror</code>.</dl>
<dt><code>tty-browsers</code></p>
<dd> An array similar to <code>x-browsers</code>, except that it gives browsers to use when no X Window display is available. The default is <code>elinks links lynx</code>.</p>
<dt><code>command</code></p>
<dd> If it is set this style is used to pick the command used to open a page for a browser. The context is <code>:mime:browser:new:$browser:</code> to start a new browser or <code>:mime:browser:running:$browser:</code> to open a URL in a browser already running on the current X display, where <code>$browser</code> is the value matched in the <code>x-browsers</code> or <code>tty-browsers</code> style. The escape sequence <code>%b</code> in the style&#8217;s value will be replaced by the browser, while <code>%u</code> will be replaced by the URL. If the style is not set, the default for all new instances is equivalent to <code>%b %u</code> and the defaults for using running browsers are equivalent to the values <code>kfmclient openURL %u</code> for Konqueror, <code>firefox -new-tab %u</code> for Firefox, <code>opera -newpage %u</code> for Opera, and <code>%b -remote &quot;openUrl(%u)&quot;</code> for all others.</dl>
</dl>
</dl>
<h2>MATHEMATICAL FUNCTIONS</h2>
<dl>
<dt>
<dd> <code>zcalc</code> [ <code>-erf</code> ] [ <i>expression</i> &#8230; ] A reasonably powerful calculator based on zsh&#8217;s arithmetic evaluation facility. The syntax is similar to that of formulae in most programming languages; see the section `Arithmetic Evaluation&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1) for details.</p>
<dl>
<dt>
<dd>
<p> Non-programmers should note that, as in many other programming languages, expressions involving only integers (whether constants without a `<code>.</code>&#8216;, variables containing such constants as strings, or variables declared to be integers) are by default evaluated using integer arithmetic, which is not how an ordinary desk calculator operates. To force floating point operation, pass the option <code>-f</code>; see further notes below. </p>
<p> If the file <code>~/.zcalcrc</code> exists it will be sourced inside the function once it is set up and about to process the command line. This can be used, for example, to set shell options; <code>emulate -L zsh</code> and <code>setopt extendedglob</code> are in effect at this point. Any failure to source the file if it exists is treated as fatal. As with other initialisation files, the directory <code>$ZDOTDIR</code> is used instead of <code>$HOME</code> if it is set. </p>
<p> The mathematical library <code>zsh/mathfunc</code> will be loaded if it is available; see the section `The zsh/mathfunc Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). The mathematical functions correspond to the raw system libraries, so trigonometric functions are evaluated using radians, and so on. </p>
<p> Each line typed is evaluated as an expression. The prompt shows a number, which corresponds to a positional parameter where the result of that calculation is stored. For example, the result of the calculation on the line preceded by `<code>4&gt; </code>&#8216; is available as <code>$4</code>. The last value calculated is available as <code>ans</code>. Full command line editing, including the history of previous calculations, is available; the history is saved in the file <code>~/.zcalc_history</code>. To exit, enter a blank line or type `<code>:q</code>&#8216; on its own (`<code>q</code>&#8216; is allowed for historical compatibility). </p>
<p> A line ending with a single backslash is treated in the same fashion as it is in command line editing: the backslash is removed, the function prompts for more input (the prompt is preceded by `<code>&#8230;</code>&#8216; to indicate this), and the lines are combined into one to get the final result. In addition, if the input so far contains more open than close parentheses <code>zcalc</code> will prompt for more input. </p>
<p> If arguments are given to <code>zcalc</code> on start up, they are used to prime the first few positional parameters. A visual indication of this is given when the calculator starts. </p>
<p> The constants <code>PI</code> (3.14159&#8230;) and <code>E</code> (2.71828&#8230;) are provided. Parameter assignment is possible, but note that all parameters will be put into the global namespace unless the <code>:local</code> special command is used. The function creates local variables whose names start with <code>_</code>, so users should avoid doing so. The variables <code>ans</code> (the last answer) and <code>stack</code> (the stack in RPN mode) may be referred to directly; <code>stack</code> is an array but elements of it are numeric. Various other special variables are used locally with their standard meaning, for example <code>compcontext</code>, <code>match</code>, <code>mbegin</code>, <code>mend</code>, <code>psvar</code>. </p>
<p> The output base can be initialised by passing the option `<code>-#</code><i>base</i>&#8216;, for example `<code>zcalc -#16</code>&#8216; (the `<code>#</code>&#8216; may have to be quoted, depending on the globbing options set). </p>
<p> If the option `<code>-e</code>&#8216; is set, the function runs non-interactively: the arguments are treated as expressions to be evaluated as if entered interactively line by line. </p>
<p> If the option `<code>-f</code>&#8216; is set, all numbers are treated as floating point, hence for example the expression `<code>3/4</code>&#8216; evaluates to 0.75 rather than 0. Options must appear in separate words. </p>
<p> If the option `<code>-r</code>&#8216; is set, RPN (Reverse Polish Notation) mode is entered. This has various additional properties:</p>
<dl>
<dt>
<dd> Stack Evaluated values are maintained in a stack; this is contained in an array named <code>stack</code> with the most recent value in <code>${stack[1]}</code>.</p>
<dt>Operators and functions</p>
<dd> If the line entered matches an operator (<code>+</code>, <code>&#8211;</code>, <code>*</code>, <code>/</code>, <code>**</code>, <code>^</code>, <code>|</code> or <code>&amp;</code>) or a function supplied by the <code>zsh/mathfunc</code> library, the bottom element or elements of the stack are popped to use as the argument or arguments. The higher elements of stack (least recent) are used as earlier arguments. The result is then pushed into <code>${stack[1]}</code>.</p>
<dt>Expressions</p>
<dd> Other expressions are evaluated normally, printed, and added to the stack as numeric values. The syntax within expressions on a single line is normal shell arithmetic (not RPN).</p>
<dt>Stack listing</p>
<dd> If an integer follows the option <code>-r</code> with no space, then on every evaluation that many elements of the stack, where available, are printed instead of just the most recent result. Hence, for example, <code>zcalc -r4</code> shows <code>$stack[4]</code> to <code>$stack[1]</code> each time results are printed.</p>
<dt>Duplication: <code>=</code></p>
<dd> The pseudo-operator <code>=</code> causes the most recent element of the stack to be duplicated onto the stack.</p>
<dt><code>pop</code></p>
<dd> The pseudo-function <code>pop</code> causes the most recent element of the stack to be popped. A `<code>&gt;</code>&#8216; on its own has the same effect.</p>
<dt><code>&gt;</code><i>ident</i></p>
<dd> The expression <code>&gt;</code> followed (with no space) by a shell identifier causes the most recent element of the stack to be popped and assigned to the variable with that name. The variable is local to the <code>zcalc</code> function.</p>
<dt><code>&lt;</code><i>ident</i></p>
<dd> The expression <code>&lt;</code> followed (with no space) by a shell identifier causes the value of the variable with that name to be pushed onto the stack. <i>ident</i> may be an integer, in which case the previous result with that number (as shown before the <code>&gt;</code> in the standard <code>zcalc</code> prompt) is put on the stack.</p>
<dt>Exchange: <code>xy</code></p>
<dd> The pseudo-function <code>xy</code> causes the most recent two elements of the stack to be exchanged. `<code>&lt;&gt;</code>&#8216; has the same effect.</dl>
<p> The prompt is configurable via the parameter <code>ZCALCPROMPT</code>, which undergoes standard prompt expansion. The index of the current entry is stored locally in the first element of the array <code>psvar</code>, which can be referred to in <code>ZCALCPROMPT</code> as `<code>%1v</code>&#8216;. The default prompt is `<code>%1v&gt; </code>&#8216;. </p>
<p> The variable <code>ZCALC_ACTIVE</code> is set within the function and can be tested by nested functions; it has the value <code>rpn</code> if RPN mode is active, else 1. </p>
<p> A few special commands are available; these are introduced by a colon. For backward compatibility, the colon may be omitted for certain commands. Completion is available if <code>compinit</code> has been run. </p>
<p> The output precision may be specified within zcalc by special commands familiar from many calculators.</p>
<dl>
<dt>
<dd> <code>:norm</code> The default output format. It corresponds to the printf <code>%g</code> specification. Typically this shows six decimal digits.</p>
<dt><code>:sci</code> <i>digits</i></p>
<dd> Scientific notation, corresponding to the printf <code>%g</code> output format with the precision given by <i>digits</i>. This produces either fixed point or exponential notation depending on the value output.</p>
<dt><code>:fix</code> <i>digits</i></p>
<dd> Fixed point notation, corresponding to the printf <code>%f</code> output format with the precision given by <i>digits</i>.</p>
<dt><code>:eng</code> <i>digits</i></p>
<dd> Exponential notation, corresponding to the printf <code>%E</code> output format with the precision given by <i>digits</i>.</p>
<dt><code>:raw</code></p>
<dd> Raw output: this is the default form of the output from a math evaluation. This may show more precision than the number actually possesses.</dl>
<p> Other special commands:</p>
<dl>
<dt>
<dd> <code>:!</code><i>line&#8230;</i> Execute <i>line&#8230;</i> as a normal shell command line. Note that it is executed in the context of the function, i.e. with local variables. Space is optional after <code>:!</code>.</p>
<dt><code>:local</code> <i>arg</i> &#8230;</p>
<dd> Declare variables local to the function. Other variables may be used, too, but they will be taken from or put into the global scope.</p>
<dt><code>:function</code> <i>name</i> [ <i>body</i> ]</p>
<dd> Define a mathematical function or (with no <i>body</i>) delete it. <code>:function</code> may be abbreviated to <code>:func</code> or simply <code>:f</code>. The <i>name</i> may contain the same characters as a shell function name. The function is defined using <code>zmathfuncdef</code>, see below.</p>
<dl>
<dt>
<dd>
<p> Note that <code>zcalc</code> takes care of all quoting. Hence for example: </p>
<dl>
<dt>
<dd>
<pre>
<code>:f cube $1 * $1 * $1</code>
</pre>
</dl>
<p> defines a function to cube the sole argument. Functions so defined, or indeed any functions defined directly or indirectly using <code>functions -M</code>, are available to execute by typing only the name on the line in RPN mode; this pops the appropriate number of arguments off the stack to pass to the function, i.e. 1 in the case of the example <code>cube</code> function. If there are optional arguments only the mandatory arguments are supplied by this means.</dl>
<dt><code>[#</code><i>base</i><code>]</code></p>
<dd> This is not a special command, rather part of normal arithmetic syntax; however, when this form appears on a line by itself the default output radix is set to <i>base</i>. Use, for example, `<code>[#16]</code>&#8216; to display hexadecimal output preceded by an indication of the base, or `<code>[##16]</code>&#8216; just to display the raw number in the given base. Bases themselves are always specified in decimal. `<code>[#]</code>&#8216; restores the normal output format. Note that setting an output base suppresses floating point output; use `<code>[#]</code>&#8216; to return to normal operation.</p>
<dt><code>$</code><i>var</i></p>
<dd> Print out the value of var literally; does not affect the calculation. To use the value of var, omit the leading `<code>$</code>&#8216;.</dl>
<p> See the comments in the function for a few extra tips.</dl>
<dt>
<dd> <code>min(</code><i>arg</i><code>, &#8230;)</code></p>
<dt>
<dd> <code>max(</code><i>arg</i><code>, &#8230;)</code></p>
<dt>
<dd> <code>sum(</code><i>arg</i><code>, &#8230;)</code></p>
<dt>
<dd> <code>zmathfunc</code> The function <code>zmathfunc</code> defines the three mathematical functions <code>min</code>, <code>max</code>, and <code>sum</code>. The functions <code>min</code> and <code>max</code> take one or more arguments. The function <code>sum</code> takes zero or more arguments. Arguments can be of different types (ints and floats).</p>
<dl>
<dt>
<dd>
<p> Not to be confused with the <code>zsh/mathfunc</code> module, described in the section `The zsh/mathfunc Module&#8217; in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1).</dl>
<dt><code>zmathfuncdef</code> [ <i>mathfunc</i> [ <i>body</i> ] ]</p>
<dd> A convenient front end to <code>functions -M</code>.</p>
<dl>
<dt>
<dd>
<p> With two arguments, define a mathematical function named <i>mathfunc</i> which can be used in any form of arithmetic evaluation. <i>body</i> is a mathematical expression to implement the function. It may contain references to position parameters <code>$1</code>, <code>$2</code>, &#8230; to refer to mandatory parameters and <code>${1:-</code><i>defvalue</i><code>}</code> &#8230; to refer to optional parameters. Note that the forms must be strictly adhered to for the function to calculate the correct number of arguments. The implementation is held in a shell function named <code>zsh_math_func_</code><i>mathfunc</i>; usually the user will not need to refer to the shell function directly. Any existing function of the same name is silently replaced. </p>
<p> With one argument, remove the mathematical function <i>mathfunc</i> as well as the shell function implementation. </p>
<p> With no arguments, list all <i>mathfunc</i> functions in a form suitable for restoring the definition. The functions have not necessarily been defined by <code>zmathfuncdef</code>.</dl>
</dl>
<h2>USER CONFIGURATION FUNCTIONS</h2>
<p> The <code>zsh/newuser</code> module comes with a function to aid in configuring shell options for new users. If the module is installed, this function can also be run by hand. It is available even if the module&#8217;s default behaviour, namely running the function for a new user logging in without startup files, is inhibited. </p>
<dl>
<dt>
<dd> <code>zsh-newuser-install</code> [ <code>-f</code> ] The function presents the user with various options for customizing their initialization scripts. Currently only <code>~/.zshrc</code> is handled. <code>$ZDOTDIR/.zshrc</code> is used instead if the parameter <code>ZDOTDIR</code> is set; this provides a way for the user to configure a file without altering an existing <code>.zshrc</code>.</p>
<dl>
<dt>
<dd>
<p> By default the function exits immediately if it finds any of the files <code>.zshenv</code>, <code>.zprofile</code>, <code>.zshrc</code>, or <code>.zlogin</code> in the appropriate directory. The option <code>-f</code> is required in order to force the function to continue. Note this may happen even if <code>.zshrc</code> itself does not exist. </p>
<p> As currently configured, the function will exit immediately if the user has root privileges; this behaviour cannot be overridden. </p>
<p> Once activated, the function&#8217;s behaviour is supposed to be self-explanatory. Menus are present allowing the user to alter the value of options and parameters. Suggestions for improvements are always welcome. </p>
<p> When the script exits, the user is given the opportunity to save the new file or not; changes are not irreversible until this point. However, the script is careful to restrict changes to the file only to a group marked by the lines `<code># Lines configured by zsh-newuser-install</code>&#8216; and `<code># End of lines configured by zsh-newuser-install</code>&#8216;. In addition, the old version of <code>.zshrc</code> is saved to a file with the suffix <code>.zni</code> appended. </p>
<p> If the function edits an existing <code>.zshrc</code>, it is up to the user to ensure that the changes made will take effect. For example, if control usually returns early from the existing <code>.zshrc</code> the lines will not be executed; or a later initialization file may override options or parameters, and so on. The function itself does not attempt to detect any such conflicts.</dl>
</dl>
<h2>OTHER FUNCTIONS</h2>
<p> There are a large number of helpful functions in the <code>Functions/Misc</code> directory of the zsh distribution. Most are very simple and do not require documentation here, but a few are worthy of special mention. </p>
<h3>Descriptions</h3>
<dl>
<dt>
<dd> <code>colors</code> This function initializes several associative arrays to map color names to (and from) the ANSI standard eight-color terminal codes. These are used by the prompt theme system (see above). You seldom should need to run <code>colors</code> more than once.</p>
<dl>
<dt>
<dd>
<p> The eight base colors are: <code>black</code>, <code>red</code>, <code>green</code>, <code>yellow</code>, <code>blue</code>, <code>magenta</code>, <code>cyan</code>, and <code>white</code>. Each of these has codes for foreground and background. In addition there are seven intensity attributes: <code>bold</code>, <code>faint</code>, <code>standout</code>, <code>underline</code>, <code>blink</code>, <code>reverse</code>, and <code>conceal</code>. Finally, there are seven codes used to negate attributes: <code>none</code> (reset all attributes to the defaults), <code>normal</code> (neither bold nor faint), <code>no-standout</code>, <code>no-underline</code>, <code>no-blink</code>, <code>no-reverse</code>, and <code>no-conceal</code>. </p>
<p> Some terminals do not support all combinations of colors and intensities. </p>
<p> The associative arrays are: </p>
<dl>
<dt>
<dd> <code>color</code></p>
<dt>
<dd> <code>colour</code> Map all the color names to their integer codes, and integer codes to the color names. The eight base names map to the foreground color codes, as do names prefixed with `<code>fg-</code>&#8216;, such as `<code>fg-red</code>&#8216;. Names prefixed with `<code>bg-</code>&#8216;, such as `<code>bg-blue</code>&#8216;, refer to the background codes. The reverse mapping from code to color yields base name for foreground codes and the <code>bg-</code> form for backgrounds.</p>
<dl>
<dt>
<dd>
<p> Although it is a misnomer to call them `colors&#8217;, these arrays also map the other fourteen attributes from names to codes and codes to names.</dl>
<dt>
<dd> <code>fg</code></p>
<dt>
<dd> <code>fg_bold</code></p>
<dt>
<dd> <code>fg_no_bold</code> Map the eight basic color names to ANSI terminal escape sequences that set the corresponding foreground text properties. The <code>fg</code> sequences change the color without changing the eight intensity attributes.</p>
<dt>
<dd> <code>bg</code></p>
<dt>
<dd> <code>bg_bold</code></p>
<dt>
<dd> <code>bg_no_bold</code> Map the eight basic color names to ANSI terminal escape sequences that set the corresponding background properties. The <code>bg</code> sequences change the color without changing the eight intensity attributes.</dl>
<p> In addition, the scalar parameters <code>reset_color</code> and <code>bold_color</code> are set to the ANSI terminal escapes that turn off all attributes and turn on bold intensity, respectively.</dl>
<dt><code>fned</code> [ <code>-x</code> <i>num</i> ] <i>name</i></p>
<dd> Same as <code>zed -f</code>. This function does not appear in the zsh distribution, but can be created by linking <code>zed</code> to the name <code>fned</code> in some directory in your <code>fpath</code>.</p>
<dt><code>is-at-least</code> <i>needed</i> [ <i>present</i> ]</p>
<dd> Perform a greater-than-or-equal-to comparison of two strings having the format of a zsh version number; that is, a string of numbers and text with segments separated by dots or dashes. If the <i>present</i> string is not provided, <code>$ZSH_VERSION</code> is used. Segments are paired left-to-right in the two strings with leading non-number parts ignored. If one string has fewer segments than the other, the missing segments are considered zero.</p>
<dl>
<dt>
<dd>
<p> This is useful in startup files to set options and other state that are not available in all versions of zsh. </p>
<dl>
<dt>
<dd>
<pre>
<code>is-at-least 3.1.6-15 &amp;&amp; setopt NO_GLOBAL_RCS
is-at-least 3.1.0 &amp;&amp; setopt HIST_REDUCE_BLANKS
is-at-least 2.6-17 || print &quot;You can't use is-at-least here.&quot;</code>
</pre>
</dl>
</dl>
<dt><code>nslookup</code> [ <i>arg</i> &#8230; ]</p>
<dd> This wrapper function for the <code>nslookup</code> command requires the <code>zsh/zpty</code> module (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). It behaves exactly like the standard <code>nslookup</code> except that it provides customizable prompts (including a right-side prompt) and completion of nslookup commands, host names, etc. (if you use the function-based completion system). Completion styles may be set with the context prefix `<code>:completion:nslookup</code>&#8216;.</p>
<dl>
<dt>
<dd>
<p> See also the <code>pager</code>, <code>prompt</code> and <code>rprompt</code> styles below.</dl>
<dt><code>regexp-replace</code> <i>var</i> <i>regexp</i> <i>replace</i></p>
<dd> Use regular expressions to perform a global search and replace operation on a variable. POSIX extended regular expressions are used, unless the option <code>RE_MATCH_PCRE</code> has been set, in which case Perl-compatible regular expressions are used (this requires the shell to be linked against the <code>pcre</code> library).</p>
<dl>
<dt>
<dd>
<p> <i>var</i> is the name of the variable containing the string to be matched. The variable will be modified directly by the function. The variables <code>MATCH</code>, <code>MBEGIN</code>, <code>MEND</code>, <code>match</code>, <code>mbegin</code>, <code>mend</code> should be avoided as these are used by the regular expression code. </p>
<p> <i>regexp</i> is the regular expression to match against the string. </p>
<p> <i>replace</i> is the replacement text. This can contain parameter, command and arithmetic expressions which will be replaced: in particular, a reference to <code>$MATCH</code> will be replaced by the text matched by the pattern. </p>
<p> The return status is 0 if at least one match was performed, else 1.</dl>
<dt><code>run-help</code> <i>cmd</i></p>
<dd> This function is designed to be invoked by the <code>run-help</code> ZLE widget, in place of the default alias. See `Accessing On-Line Help&#8217; above for setup instructions.</p>
<dl>
<dt>
<dd>
<p> In the discussion which follows, if <i>cmd</i> is a file system path, it is first reduced to its rightmost component (the file name). </p>
<p> Help is first sought by looking for a file named <i>cmd</i> in the directory named by the <code>HELPDIR</code> parameter. If no file is found, an assistant function, alias, or command named <code>run-help-</code><i>cmd</i> is sought. If found, the assistant is executed with the rest of the current command line (everything after the command name <i>cmd</i>) as its arguments. When neither file nor assistant is found, the external command `<code>man</code> <i>cmd</i>&#8216; is run. </p>
<p> An example assistant for the &quot;ssh&quot; command: </p>
<dl>
<dt>
<dd>
<pre><code>
run - help - ssh()
{
    emulate - LR zsh local - a args
#Delete the "-l username" option
                                 zparseopts -
        D - E - a args l :
#Delete other options, leaving : host command
        args = ($ { @ : # - * }) if [[${#args} - lt 2]];
    then
            man ssh else run -
        help $args[2] fi
}
</code></pre>
</dl>
<p> Several of these assistants are provided in the <code>Functions/Misc</code> directory. These must be autoloaded, or placed as executable scripts in your search path, in order to be found and used by <code>run-help</code>. </p>
<dl>
<dt>
<dd> run-help-git</p>
<dt>
<dd> run-help-ip</p>
<dt>
<dd> run-help-openssl</p>
<dt>
<dd> run-help-p4</p>
<dt>
<dd> run-help-sudo</p>
<dt>
<dd> run-help-svk</p>
<dt>
<dd> <code>run-help-svn</code> Assistant functions for the <code>git</code>, <code>ip</code>, <code>openssl</code>, <code>p4</code>, <code>sudo</code>, <code>svk</code>, and <code>svn</code>, commands.</dl>
</dl>
<dt><code>tetris</code></p>
<dd> Zsh was once accused of not being as complete as Emacs, because it lacked a Tetris game. This function was written to refute this vicious slander.</p>
<dl>
<dt>
<dd>
<p> This function must be used as a ZLE widget: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -U tetris
zle -N tetris
bindkey </code><i>keys</i> tetris
</pre>
</dl>
<p> To start a game, execute the widget by typing the <i>keys</i>. Whatever command line you were editing disappears temporarily, and your keymap is also temporarily replaced by the Tetris control keys. The previous editor state is restored when you quit the game (by pressing `<code>q</code>&#8216;) or when you lose. </p>
<p> If you quit in the middle of a game, the next invocation of the <code>tetris</code> widget will continue where you left off. If you lost, it will start a new game.</dl>
<dt><code>tetriscurses</code></p>
<dd> This is a port of the above to zcurses. The input handling is improved a bit so that moving a block sideways doesn&#8217;t automatically advance a timestep, and the graphics use unicode block graphics.</p>
<dl>
<dt>
<dd>
<p> This version does not save the game state between invocations, and is not invoked as a widget, but rather as: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -U tetriscurses
tetriscurses</code>
</pre>
</dl>
</dl>
<dt><code>zargs</code> [ <i>option</i> &#8230; <code>&#8211;</code><code>&#8211;</code> ] [ <i>input</i> &#8230; ] [ <code>&#8211;</code><code>&#8211;</code> <i>command</i> [ <i>arg</i> &#8230; ] ]</p>
<dd> This function has a similar purpose to GNU xargs. Instead of reading lines of arguments from the standard input, it takes them from the command line. This is useful because zsh, especially with recursive glob operators, often can construct a command line for a shell function that is longer than can be accepted by an external command.</p>
<dl>
<dt>
<dd>
<p> The <i>option</i> list represents options of the <code>zargs</code> command itself, which are the same as those of <code>xargs</code>. The <i>input</i> list is the collection of strings (often file names) that become the arguments of the <code>command</code>, analogous to the standard input of <code>xargs</code>. Finally, the <i>arg</i> list consists of those arguments (usually options) that are passed to the <i>command</i> each time it runs. The <i>arg</i> list precedes the elements from the <code>input</code> list in each run. If no <i>command</i> is provided, then no <i>arg</i> list may be provided, and in that event the default command is `<code>print</code>&#8216; with arguments `<code>-r &#8211;</code><code>&#8211;</code>&#8216;. </p>
<p> For example, to get a long <code>ls</code> listing of all non-hidden plain files in the current directory or its subdirectories: </p>
<dl>
<dt>
<dd>
<pre>
<code>autoload -U zargs
zargs -- **/*(.) -- ls -ld --</code>
</pre>
</dl>
<p> The first and third occurrences of `<code>&#8211;</code><code>&#8211;</code>&#8216; are used to mark the end of options for <code>zargs</code> and <code>ls</code> respectively to guard against filenames starting with `<code>&#8211;</code>&#8216;, while the second is used to separate the list of files from the command to run (`<code>ls -ld &#8212;</code>&#8216;). </p>
<p> The first `<code>&#8211;</code><code>&#8211;</code>&#8216; would also be needed if there was a chance the list might be empty as in: </p>
<dl>
<dt>
<dd>
<pre>
<code>zargs -r -- ./*.back(#qN) -- rm -f</code>
</pre>
</dl>
<p> In the event that the string `<code>&#8211;</code><code>&#8211;</code>&#8216; is or may be an <i>input</i>, the <code>-e</code> option may be used to change the end-of-inputs marker. Note that this does <i>not</i> change the end-of-options marker. For example, to use `<code>..</code>&#8216; as the marker: </p>
<dl>
<dt>
<dd>
<pre>
<code>zargs -e.. -- **/*(.) .. ls -ld --</code>
</pre>
</dl>
<p> This is a good choice in that example because no plain file can be named `<code>..</code>&#8216;, but the best end-marker depends on the circumstances. </p>
<p> The options <code>-i</code>, <code>-I</code>, <code>-l</code>, <code>-L</code>, and <code>-n</code> differ slightly from their usage in <code>xargs</code>. There are no input lines for <code>zargs</code> to count, so <code>-l</code> and <code>-L</code> count through the <i>input</i> list, and <code>-n</code> counts the number of arguments passed to each execution of <i>command</i>, <i>including</i> any <i>arg</i> list. Also, any time <code>-i</code> or <code>-I</code> is used, each <i>input</i> is processed separately as if by `<code>-L</code> <code>1</code>&#8216;. </p>
<p> For details of the other <code>zargs</code> options, see <i><a href="/docs/linux/man/1-xargs/">xargs</a></i>(1) (but note the difference in function between <code>zargs</code> and <code>xargs</code>) or run <code>zargs</code> with the <code>&#8211;</code><code>-help</code> option.</dl>
<dt>
<dd> <code>zed</code> [ <code>-f</code> [ <code>-x</code> <i>num</i> ] ] <i>name</i></p>
<dt>
<dd> <code>zed -b</code> This function uses the ZLE editor to edit a file or function.</p>
<dl>
<dt>
<dd>
<p> Only one <i>name</i> argument is allowed. If the <code>-f</code> option is given, the name is taken to be that of a function; if the function is marked for autoloading, <code>zed</code> searches for it in the <code>fpath</code> and loads it. Note that functions edited this way are installed into the current shell, but <i>not</i> written back to the autoload file. In this case the <code>-x</code> option specifies that leading tabs indenting the function according to syntax should be converted into the given number of spaces; `<code>-x 2</code>&#8216; is consistent with the layout of functions distributed with the shell. </p>
<p> Without <code>-f</code>, <i>name</i> is the path name of the file to edit, which need not exist; it is created on write, if necessary. </p>
<p> While editing, the function sets the main keymap to <code>zed</code> and the vi command keymap to <code>zed-vicmd</code>. These will be copied from the existing <code>main</code> and <code>vicmd</code> keymaps if they do not exist the first time <code>zed</code> is run. They can be used to provide special key bindings used only in zed. </p>
<p> If it creates the keymap, <code>zed</code> rebinds the return key to insert a line break and `<code>^X^W</code>&#8216; to accept the edit in the <code>zed</code> keymap, and binds `<code>ZZ</code>&#8216; to accept the edit in the <code>zed-vicmd</code> keymap. </p>
<p> The bindings alone can be installed by running `<code>zed -b</code>&#8216;. This is suitable for putting into a startup file. Note that, if rerun, this will overwrite the existing <code>zed</code> and <code>zed-vicmd</code> keymaps. </p>
<p> Completion is available, and styles may be set with the context prefix `<code>:completion:zed</code>&#8216;. </p>
<p> A zle widget <code>zed-set-file-name</code> is available. This can be called by name from within zed using `<code>x zed-set-file-name</code>&#8216; (note, however, that because of zed&#8217;s rebindings you will have to type <code>^j</code> at the end instead of the return key), or can be bound to a key in either of the <code>zed</code> or <code>zed-vicmd</code> keymaps after `<code>zed -b</code>&#8216; has been run. When the widget is called, it prompts for a new name for the file being edited. When zed exits the file will be written under that name and the original file will be left alone. The widget has no effect with `<code>zed -f</code>&#8216;. </p>
<p> While <code>zed-set-file-name</code> is running, zed uses the keymap <code>zed-normal-keymap</code>, which is linked from the main keymap in effect at the time zed initialised its bindings. (This is to make the return key operate normally.) The result is that if the main keymap has been changed, the widget won&#8217;t notice. This is not a concern for most users.</dl>
<dt>
<dd> <code>zcp</code> [ <code>-finqQvwW</code> ] <i>srcpat</i> <i>dest</i></p>
<dt>
<dd> <code>zln</code> [ <code>-finqQsvwW</code> ] <i>srcpat</i> <i>dest</i> Same as <code>zmv -C</code> and <code>zmv -L</code>, respectively. These functions do not appear in the zsh distribution, but can be created by linking <code>zmv</code> to the names <code>zcp</code> and <code>zln</code> in some directory in your <code>fpath</code>.</p>
<dt><code>zkbd</code></p>
<dd> See `Keyboard Definition&#8217; above. </p>
<dt>
<dd> <code>zmv</code> [ <code>-finqQsvwW</code> ] [ <code>-C</code> | <code>-L</code> | <code>-M</code> | -{<code>p</code>|<code>P</code>} <i>program</i> ] [ <code>-o</code> <i>optstring</i> ]</p>
<dt>
<dd> <i>srcpat</i> <i>dest</i> Move (usually, rename) files matching the pattern <i>srcpat</i> to corresponding files having names of the form given by <i>dest</i>, where <i>srcpat</i> contains parentheses surrounding patterns which will be replaced in turn by <code>$1</code>, <code>$2</code>, &#8230; in <i>dest</i>. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zmv '(*).lis' '$1.txt'</code>
</pre>
</dl>
<p> renames `<code>foo.lis</code>&#8216; to `<code>foo.txt</code>&#8216;, `<code>my.old.stuff.lis</code>&#8216; to `<code>my.old.stuff.txt</code>&#8216;, and so on. </p>
<p> The pattern is always treated as an <code>EXTENDED_GLOB</code> pattern. Any file whose name is not changed by the substitution is simply ignored. Any error (a substitution resulted in an empty string, two substitutions gave the same result, the destination was an existing regular file and <code>-f</code> was not given) causes the entire function to abort without doing anything. </p>
<p> In addition to pattern replacement, the variable <code>$f</code> can be referrred to in the second (replacement) argument. This makes it possible to use variable substitution to alter the argument; see examples below. </p>
<p> Options: </p>
<dl>
<dt><code>-f</code></p>
<dd> Force overwriting of destination files. Not currently passed down to the <code>mv</code>/<code>cp</code>/<code>ln</code> command due to vagaries of implementations (but you can use <code>-o-f</code> to do that).</p>
<dt><code>-i</code></p>
<dd> Interactive: show each line to be executed and ask the user whether to execute it. `<code>Y</code>&#8216; or `<code>y</code>&#8216; will execute it, anything else will skip it. Note that you just need to type one character.</p>
<dt><code>-n</code></p>
<dd> No execution: print what would happen, but don&#8217;t do it.</p>
<dt><code>-q</code></p>
<dd> Turn bare glob qualifiers off: now assumed by default, so this has no effect.</p>
<dt><code>-Q</code></p>
<dd> Force bare glob qualifiers on. Don&#8217;t turn this on unless you are actually using glob qualifiers in a pattern.</p>
<dt><code>-s</code></p>
<dd> Symbolic, passed down to <code>ln</code>; only works with <code>-L</code>.</p>
<dt><code>-v</code></p>
<dd> Verbose: print each command as it&#8217;s being executed.</p>
<dt><code>-w</code></p>
<dd> Pick out wildcard parts of the pattern, as described above, and implicitly add parentheses for referring to them.</p>
<dt><code>-W</code></p>
<dd> Just like <code>-w</code>, with the addition of turning wildcards in the replacement pattern into sequential <code>${1}</code> .. <code>${N}</code> references.</p>
<dt><code>-C</code></p>
<dd>
<dt><code>-L</code></p>
<dd>
<dt><code>-M</code></p>
<dd> Force <code>cp</code>, <code>ln</code> or <code>mv</code>, respectively, regardless of the name of the function.</p>
<dt><code>-p</code> <i>program</i></p>
<dd> Call <i>program</i> instead of <code>cp</code>, <code>ln</code> or <code>mv</code>. Whatever it does, it should at least understand the form `<i>program</i> <code>&#8211;</code><code>&#8211;</code> <i>oldname</i> <i>newname</i>&#8216; where <i>oldname</i> and <i>newname</i> are filenames generated by <code>zmv</code>. <i>program</i> will be split into words, so might be e.g. the name of an archive tool plus a copy or rename subcommand.</p>
<dt><code>-P</code> <i>program</i></p>
<dd> As <code>-p</code> <i>program</i>, except that <i>program</i> does not accept a following <code>&#8211;</code><code>&#8211;</code> to indicate the end of options. In this case filenames must already be in a sane form for the program in question.</p>
<dt><code>-o</code> <i>optstring</i></p>
<dd> The <i>optstring</i> is split into words and passed down verbatim to the <code>cp</code>, <code>ln</code> or <code>mv</code> command called to perform the work. It should probably begin with a `<code>&#8211;</code>&#8216;.</dl>
<p> Further examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>zmv -v '(* *)' '${1// /_}'</code>
</pre>
</dl>
<p> For any file in the current directory with at least one space in the name, replace every space by an underscore and display the commands executed. </p>
<dl>
<dt>
<dd>
<pre>
<code>zmv -v '* *' '${f// /_}'</code>
</pre>
</dl>
<p> This does exactly the same by referring to the file name stored in <code>$f</code>. </p>
<p> For more complete examples and other implementation details, see the <code>zmv</code> source file, usually located in one of the directories named in your <code>fpath</code>, or in <code>Functions/Misc/zmv</code> in the zsh distribution.</dl>
<dt><code>zrecompile</code></p>
<dd> See `Recompiling Functions&#8217; above.</p>
<dt><code>zstyle+</code> <i>context</i> <i>style</i> <i>value</i> [ <code>+</code> <i>subcontext</i> <i>style</i> <i>value</i> &#8230; ]</p>
<dd> This makes defining styles a bit simpler by using a single `<code>+</code>&#8216; as a special token that allows you to append a context name to the previously used context name. Like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>zstyle+ ':foo:bar' </code><i>style1</i> <i>value1</i> \ 
       +':baz'     <i>style2</i> <i>value2</i> \ 
       +':frob'    <i>style3</i> <i>value3</i>
</pre>
</dl>
<p> This defines <i>style1</i> with <i>value1</i> for the context <code>:foo:bar</code> as usual, but it also defines <i>style2</i> with <i>value2</i> for the context <code>:foo:bar:baz</code> and <i>style3</i> with <i>value3</i> for <code>:foo:bar:frob</code>. Any <i>subcontext</i> may be the empty string to re-use the first context unchanged.</dl>
</dl>
<h3>Styles</h3>
<dl>
<dt>
<dd> <code>insert-tab</code> The <code>zed</code> function <i>sets</i> this style in context `<code>:completion:zed:*</code>&#8216; to turn off completion when <code>TAB</code> is typed at the beginning of a line. You may override this by setting your own value for this context and style.</p>
<dt><code>pager</code></p>
<dd> The <code>nslookup</code> function looks up this style in the context `<code>:nslookup</code>&#8216; to determine the program used to display output that does not fit on a single screen.</p>
<dt>
<dd> <code>prompt</code></p>
<dt>
<dd> <code>rprompt</code> The <code>nslookup</code> function looks up this style in the context `<code>:nslookup</code>&#8216; to set the prompt and the right-side prompt, respectively. The usual expansions for the <code>PS1</code> and <code>RPS1</code> parameters may be used (see EXPANSION OF PROMPT SEQUENCES in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1)). </p>
</dl>
<h2>Index</h2>
