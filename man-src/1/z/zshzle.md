---
title: "zshzle(1)"
name: "zshzle"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshzle/"
description: "zshzle – zsh command line editor"
---
<h2 class="name">NAME</h2>
<p> zshzle - zsh command line editor </p>
<h2>DESCRIPTION</h2>
<p> If the <code>ZLE</code> option is set (which it is by default in interactive shells) and the shell input is attached to the terminal, the user is able to edit command lines. </p>
<p> There are two display modes. The first, multiline mode, is the default. It only works if the <code>TERM</code> parameter is set to a valid terminal type that can move the cursor up. The second, single line mode, is used if <code>TERM</code> is invalid or incapable of moving the cursor up, or if the <code>SINGLE_LINE_ZLE</code> option is set. This mode is similar to <code>ksh</code>, and uses no termcap sequences. If <code>TERM</code> is &quot;emacs&quot;, the <code>ZLE</code> option will be unset by default. </p>
<p> The parameters <code>BAUD</code>, <code>COLUMNS</code>, and <code>LINES</code> are also used by the line editor. See <i>Parameters Used By The Shell</i> in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<p> The parameter <code>zle_highlight</code> is also used by the line editor; see <i>Character Highlighting</i> below. Highlighting of special characters and the region between the cursor and the mark (as set with <code>set-mark-command</code> in Emacs mode, or by <code>visual-mode</code> in Vi mode) is enabled by default; consult this reference for more information. Irascible conservatives will wish to know that all highlighting may be disabled by the following setting: </p>
<dl>
<dd> <pre><code>
 zle_highlight=(none) 
</code></pre>
 </dd></dl>
<p> In many places, references are made to the <code>numeric argument</code>. This can by default be entered in emacs mode by holding the alt key and typing a number, or pressing escape before each digit, and in vi command mode by typing the number before entering a command. Generally the numeric argument causes the next command entered to be repeated the specified number of times, unless otherwise noted below; this is implemented by the <code>digit-argument</code> widget. See also the <i>Arguments</i> subsection of the <i>Widgets</i> section for some other ways the numeric argument can be modified. </p>
<h2>KEYMAPS</h2>
<p> A keymap in ZLE contains a set of bindings between key sequences and ZLE commands. The empty key sequence cannot be bound. </p>
<p> There can be any number of keymaps at any time, and each keymap has one or more names. If all of a keymap&#8217;s names are deleted, it disappears. <code>bindkey</code> can be used to manipulate keymap names. </p>
<p> Initially, there are eight keymaps: </p>
<dl>
<dt><code>emacs</code></dt>
<dd> <p> EMACS emulation </p>
 </dd>
<dt><code>viins</code></dt>
<dd> <p> vi emulation - insert mode </p>
 </dd>
<dt><code>vicmd</code></dt>
<dd> <p> vi emulation - command mode </p>
 </dd>
<dt><code>viopp</code></dt>
<dd> <p> vi emulation - operator pending </p>
 </dd>
<dt><code>visual</code></dt>
<dd> <p> vi emulation - selection active </p>
 </dd>
<dt><code>isearch</code></dt>
<dd> <p> incremental search mode </p>
 </dd>
<dt><code>command</code></dt>
<dd> <p> read a command name </p>
 </dd>
<dt><code>.safe</code></dt>
<dd> <p> fallback keymap </p>
 </dd></dl>
<p> The `<code>.safe</code>&#8216; keymap is special. It can never be altered, and the name can never be removed. However, it can be linked to other names, which can be removed. In the future other special keymaps may be added; users should avoid using names beginning with `<code>.</code>&#8216; for their own keymaps. </p>
<p> In addition to these names, either `<code>emacs</code>&#8216; or `<code>viins</code>&#8216; is also linked to the name `<code>main</code>&#8216;. If one of the <code>VISUAL</code> or <code>EDITOR</code> environment variables contain the string `<code>vi</code>&#8216; when the shell starts up then it will be `<code>viins</code>&#8216;, otherwise it will be `<code>emacs</code>&#8216;. <code>bindkey</code>&#8216;s <code>-e</code> and <code>-v</code> options provide a convenient way to override this default choice. </p>
<p> When the editor starts up, it will select the `<code>main</code>&#8216; keymap. If that keymap doesn&#8217;t exist, it will use `<code>.safe</code>&#8216; instead. </p>
<p> In the `<code>.safe</code>&#8216; keymap, each single key is bound to <code>self-insert</code>, except for ^J (line feed) and ^M (return) which are bound to <code>accept-line</code>. This is deliberately not pleasant to use; if you are using it, it means you deleted the main keymap, and you should put it back.  </p>
<h3>Reading Commands</h3>
<p> When ZLE is reading a command from the terminal, it may read a sequence that is bound to some command and is also a prefix of a longer bound string. In this case ZLE will wait a certain time to see if more characters are typed, and if not (or they don&#8217;t match any longer string) it will execute the binding. This timeout is defined by the <code>KEYTIMEOUT</code> parameter; its default is 0.4 sec. There is no timeout if the prefix string is not itself bound to a command. </p>
<p> The key timeout is also applied when ZLE is reading the bytes from a multibyte character string when it is in the appropriate mode. (This requires that the shell was compiled with multibyte mode enabled; typically also the locale has characters with the UTF-8 encoding, although any multibyte encoding known to the operating system is supported.) If the second or a subsequent byte is not read within the timeout period, the shell acts as if <code>?</code> were typed and resets the input state. </p>
<p> As well as ZLE commands, key sequences can be bound to other strings, by using `<code>bindkey -s</code>&#8216;. When such a sequence is read, the replacement string is pushed back as input, and the command reading process starts again using these fake keystrokes. This input can itself invoke further replacement strings, but in order to detect loops the process will be stopped if there are twenty such replacements without a real command being read. </p>
<p> A key sequence typed by the user can be turned into a command name for use in user-defined widgets with the <code>read-command</code> widget, described in the subsection `Miscellaneous&#8217; of the section `Standard Widgets&#8217; below.  </p>
<h3>Local Keymaps</h3>
<p> While for normal editing a single keymap is used exclusively, in many modes a local keymap allows for some keys to be customised. For example, in an incremental search mode, a binding in the <code>isearch</code> keymap will override a binding in the <code>main</code> keymap but all keys that are not overridden can still be used. </p>
<p> If a key sequence is defined in a local keymap, it will hide a key sequence in the global keymap that is a prefix of that sequence. An example of this occurs with the binding of <code>iw</code> in <code>viopp</code> as this hides the binding of <code>i</code> in <code>vicmd</code>. However, a longer sequence in the global keymap that shares the same prefix can still apply so for example the binding of <code>^Xa</code> in the global keymap will be unaffected by the binding of <code>^Xb</code> in the local keymap. </p>
<h2>ZLE BUILTINS</h2>
<p> The ZLE module contains three related builtin commands. The <code>bindkey</code> command manipulates keymaps and key bindings; the <code>vared</code> command invokes ZLE on the value of a shell parameter; and the <code>zle</code> command manipulates editing widgets and allows command line access to ZLE commands from within shell functions. </p>
<dl>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-l</code> [ <code>-L</code> ] [ <i>keymap</i> ... ] </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-d</code> </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-D</code> <i>keymap</i> ... </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-A</code> <i>old-keymap new-keymap</i> </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-N</code> <i>new-keymap</i> [ <i>old-keymap</i> ] </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-m</code> </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-r</code> <i>in-string</i> ... </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <code>-s</code> <i>in-string out-string</i> ... </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] <i>in-string command</i> ... </p>
 </dd>
<dd> <p> <code>bindkey</code> [ <i>options</i> ] [ <i>in-string</i> ] <code>bindkey</code>&#8216;s options can be divided into three categories: keymap selection for the current command, operation selection, and others. The keymap selection options are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>-e</code> Selects keymap `<code>emacs</code>&#8216; for any operations by the current command, and also links `<code>emacs</code>&#8216; to `<code>main</code>&#8216; so that it is selected by default the next time the editor starts. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Selects keymap `<code>viins</code>&#8216; for any operations by the current command, and also links `<code>viins</code>&#8216; to `<code>main</code>&#8216; so that it is selected by default the next time the editor starts. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Selects keymap `<code>vicmd</code>&#8216; for any operations by the current command. </p>
 </dd>
<dt><code>-M</code><i>keymap</i></dt>
<dd> <p> The <i>keymap</i> specifies a keymap name that is selected for any operations by the current command. </p>
 </dd></dl>
<p> If a keymap selection is required and none of the options above are used, the `<code>main</code>&#8216; keymap is used. Some operations do not permit a keymap to be selected, namely: </p>
<dl>
<dd> <p> <code>-l</code> List all existing keymap names; if any arguments are given, list just those keymaps. </p>
 </dd>
<dl>
<dd> <p> If the <code>-L</code> option is also used, list in the form of <code>bindkey</code> commands to create or link the keymaps. `<code>bindkey -lL main</code>&#8216; shows which keymap is linked to `<code>main</code>&#8216;, if any, and hence if the standard emacs or vi emulation is in effect. This option does not show the <code>.safe</code> keymap because it cannot be created in that fashion; however, neither is `<code>bindkey -lL .safe</code>&#8216; reported as an error, it simply outputs nothing. </p>
 </dd></dl>
<dt><code>-d</code></dt>
<dd> <p> Delete all existing keymaps and reset to the default state. </p>
 </dd>
<dt><code>-D</code><i>keymap</i> ...</dt>
<dd> <p> Delete the named <i>keymap</i>s. </p>
 </dd>
<dt><code>-A</code><i>old-keymap new-keymap</i></dt>
<dd> <p> Make the <i>new-keymap</i> name an alias for <i>old-keymap</i>, so that both names refer to the same keymap. The names have equal standing; if either is deleted, the other remains. If there is already a keymap with the <i>new-keymap</i> name, it is deleted. </p>
 </dd>
<dt><code>-N</code><i>new-keymap</i> [ <i>old-keymap</i> ]</dt>
<dd> <p> Create a new keymap, named <i>new-keymap</i>. If a keymap already has that name, it is deleted. If an <i>old-keymap</i> name is given, the new keymap is initialized to be a duplicate of it, otherwise the new keymap will be empty. </p>
 </dd></dl>
<p> To use a newly created keymap, it should be linked to <code>main</code>. Hence the sequence of commands to create and use a new keymap `<code>mymap</code>&#8216; initialized from the <code>emacs</code> keymap (which remains unchanged) is: </p>
<dl>
<dd> <pre><code>
 bindkey -N mymap emacs
bindkey -A mymap main 
</code></pre>
 </dd></dl>
<p> Note that while `<code>bindkey -A</code> <i>newmap</i> <code>main</code>&#8216; will work when <i>newmap</i> is <code>emacs</code> or <code>viins</code>, it will not work for <code>vicmd</code>, as switching from vi insert to command mode becomes impossible. </p>
<p> The following operations act on the `<code>main</code>&#8216; keymap if no keymap selection option was given: </p>
<dl>
<dd> <p> <code>-m</code> Add the built-in set of meta-key bindings to the selected keymap. Only keys that are unbound or bound to <code>self-insert</code> are affected. </p>
 </dd>
<dt><code>-r</code><i>in-string</i> ...</dt>
<dd> <p> Unbind the specified <i>in-string</i>s in the selected keymap. This is exactly equivalent to binding the strings to <code>undefined-key</code>. </p>
 </dd>
<dl>
<dd> <p> When <code>-R</code> is also used, interpret the <i>in-string</i>s as ranges. </p>
<p> When <code>-p</code> is also used, the <i>in-string</i>s specify prefixes. Any binding that has the given <i>in-string</i> as a prefix, not including the binding for the <i>in-string</i> itself, if any, will be removed. For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 bindkey -rpM viins '^[' 
</code></pre>
 </dd></dl>
<p> will remove all bindings in the vi-insert keymap beginning with an escape character (probably cursor keys), but leave the binding for the escape character itself (probably <code>vi-cmd-mode</code>). This is incompatible with the option <code>-R</code>. </dl>
 </p>
<dt><code>-s</code><i>in-string out-string</i> ...</dt>
<dd> <p> Bind each <i>in-string</i> to each <i>out-string</i>. When <i>in-string</i> is typed, <i>out-string</i> will be pushed back and treated as input to the line editor. When <code>-R</code> is also used, interpret the <i>in-string</i>s as ranges. </p>
 </dd>
<dl>
<dd> <p> Note that both <i>in-string</i> and <i>out-string</i> are subject to the same form of interpretation, as described below. </p>
 </dd></dl>
<dt><i>in-string command</i> ...</dt>
<dd> <p> Bind each <i>in-string</i> to each <i>command</i>. When <code>-R</code> is used, interpret the <i>in-string</i>s as ranges. </p>
 </dd>
<dt>[ <i>in-string</i> ]</dt>
<dd> <p> List key bindings. If an <i>in-string</i> is specified, the binding of that string in the selected keymap is displayed. Otherwise, all key bindings in the selected keymap are displayed. (As a special case, if the <code>-e</code> or <code>-v</code> option is used alone, the keymap is <i>not</i> displayed - the implicit linking of keymaps is the only thing that happens.) </p>
 </dd>
<dl>
<dd> <p> When the option <code>-p</code> is used, the <i>in-string</i> must be present. The listing shows all bindings which have the given key sequence as a prefix, not including any bindings for the key sequence itself. </p>
<p> When the <code>-L</code> option is used, the list is in the form of <code>bindkey</code> commands to create the key bindings. </p>
 </dd></dl>
</dl>
<p> When the <code>-R</code> option is used as noted above, a valid range consists of two characters, with an optional `<code>-</code>&#8216; between them. All characters between the two specified, inclusive, are bound as specified. </p>
<p> For either <i>in-string</i> or <i>out-string</i>, the following escape sequences are recognised: </p>
<dl>
<dt><code>\a</code></dt>
<dd> <p> bell character </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace </p>
 </dd>
<dt><code>\e</code>, <code>\E</code></dt>
<dd> <p> escape </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> form feed </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> linefeed (newline) </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> carriage return </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> horizontal tab </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> vertical tab </p>
 </dd>
<dt><code>\</code><i>NNN</i></dt>
<dd> <p> character code in octal </p>
 </dd>
<dt><code>\x</code><i>NN</i></dt>
<dd> <p> character code in hexadecimal </p>
 </dd>
<dt><code>\u</code><i>NNNN</i></dt>
<dd> <p> unicode character code in hexadecimal </p>
 </dd>
<dt><code>\U</code><i>NNNNNNNN</i></dt>
<dd> <p> unicode character code in hexadecimal </p>
 </dd>
<dt><code>\M</code>[<code>-</code>]<i>X</i></dt>
<dd> <p> character with meta bit set </p>
 </dd>
<dt><code>\C</code>[<code>-</code>]<i>X</i></dt>
<dd> <p> control character </p>
 </dd>
<dt><code>^</code><i>X</i></dt>
<dd> <p> control character </p>
 </dd></dl>
<p> In all other cases, `<code>\</code>&#8216; escapes the following character. Delete is written as `<code>^?</code>&#8216;. Note that `<code>\M^?</code>&#8216; and `<code>^\M?</code>&#8216; are not the same, and that (unlike emacs), the bindings `<code>\M-</code><i>X</i>&#8216; and `<code>\e</code><i>X</i>&#8216; are entirely distinct, although they are initialized to the same bindings by `<code>bindkey -m</code>&#8216;. </dl>
 </p>
<dd> <p> <code>vared </code>[ <code>-Aacghe</code> ] [ <code>-p</code> <i>prompt</i> ] [ <code>-r</code> <i>rprompt</i> ] </p>
 </dd>
<dd> <p> [ <code>-M</code> <i>main-keymap</i> ] [ <code>-m</code> <i>vicmd-keymap</i> ] </p>
 </dd>
<dd> <p> [ <code>-i</code> <i>init-widget</i> ] [ <code>-f</code> <i>finish-widget</i> ] </p>
 </dd>
<dd> <p> [ <code>-t</code> <i>tty</i> ] <i>name</i> The value of the parameter <i>name</i> is loaded into the edit buffer, and the line editor is invoked. When the editor exits, <i>name</i> is set to the string value returned by the editor. When the <code>-c</code> flag is given, the parameter is created if it doesn&#8217;t already exist. The <code>-a</code> flag may be given with <code>-c</code> to create an array parameter, or the <code>-A</code> flag to create an associative array. If the type of an existing parameter does not match the type to be created, the parameter is unset and recreated. The <code>-g</code> flag may be given to suppress warnings from the <code>WARN_CREATE_GLOBAL</code> and <code>WARN_NESTED_VAR</code> options. </p>
 </dd>
<dl>
<dd> <p> If an array or array slice is being edited, separator characters as defined in <code>$IFS</code> will be shown quoted with a backslash, as will backslashes themselves. Conversely, when the edited text is split into an array, a backslash quotes an immediately following separator character or backslash; no other special handling of backslashes, or any handling of quotes, is performed. </p>
<p> Individual elements of existing array or associative array parameters may be edited by using subscript syntax on <i>name</i>. New elements are created automatically, even without <code>-c</code>. </p>
<p> If the <code>-p</code> flag is given, the following string will be taken as the prompt to display at the left. If the <code>-r</code> flag is given, the following string gives the prompt to display at the right. If the <code>-h</code> flag is specified, the history can be accessed from ZLE. If the <code>-e</code> flag is given, typing <code>^D</code> (Control-D) on an empty line causes <code>vared</code> to exit immediately with a non-zero return value. </p>
<p> The <code>-M</code> option gives a keymap to link to the <code>main</code> keymap during editing, and the <code>-m</code> option gives a keymap to link to the <code>vicmd</code> keymap during editing. For vi-style editing, this allows a pair of keymaps to override <code>viins</code> and <code>vicmd</code>. For emacs-style editing, only <code>-M</code> is normally needed but the <code>-m</code> option may still be used. On exit, the previous keymaps will be restored. </p>
<p> <code>Vared</code> calls the usual `<code>zle-line-init</code>&#8216; and `<code>zle-line-finish</code>&#8216; hooks before and after it takes control. Using the <code>-i</code> and <code>-f</code> options, it is possible to replace these with other custom widgets. </p>
<p> If `<code>-t</code> <i>tty</i>&#8216; is given, <i>tty</i> is the name of a terminal device to be used instead of the default <code>/dev/tty</code>. If <i>tty</i> does not refer to a terminal an error is reported. </p>
 </dd></dl>
<dd> <p> <code>zle</code> </p>
 </dd>
<dd> <p> <code>zle</code> <code>-l</code> [ <code>-L</code> | <code>-a</code> ] [ <i>string</i> ... ] </p>
 </dd>
<dd> <p> <code>zle</code> <code>-D</code> <i>widget</i> ... </p>
 </dd>
<dd> <p> <code>zle</code> <code>-A</code> <i>old-widget</i> <i>new-widget</i> </p>
 </dd>
<dd> <p> <code>zle</code> <code>-N</code> <i>widget</i> [ <i>function</i> ] </p>
 </dd>
<dd> <p> <code>zle</code> <code>-f</code> <i>flag</i> [ <i>flag</i>... ] </p>
 </dd>
<dd> <p> <code>zle</code> <code>-C</code> <i>widget</i> <i>completion-widget</i> <i>function</i> </p>
 </dd>
<dd> <p> <code>zle</code> <code>-R</code> [ <code>-c</code> ] [ <i>display-string</i> ] [ <i>string</i> ... ] </p>
 </dd>
<dd> <p> <code>zle</code> <code>-M</code> <i>string</i> </p>
 </dd>
<dd> <p> <code>zle</code> <code>-U</code> <i>string</i> </p>
 </dd>
<dd> <p> <code>zle</code> <code>-K</code> <i>keymap</i> </p>
 </dd>
<dd> <p> <code>zle</code> <code>-F</code> [ <code>-L</code> | <code>-w</code> ] [ <i>fd</i> [ <i>handler</i> ] ] </p>
 </dd>
<dd> <p> <code>zle</code> <code>-I</code> </p>
 </dd>
<dd> <p> <code>zle</code> <code>-T</code> [ <code>tc</code> <i>function</i> | <code>-r</code> <code>tc</code> | <code>-L</code> ] </p>
 </dd>
<dd> <p> <code>zle</code> <i>widget</i> [ <code>-n</code> <i>num</i> ] [ <code>-Nw</code> ] [ <code>-K</code> <i>keymap</i> ] <i>args</i> ... The <code>zle</code> builtin performs a number of different actions concerning ZLE. </p>
 </dd>
<dl>
<dd> <p> With no options and no arguments, only the return status will be set. It is zero if ZLE is currently active and widgets could be invoked using this builtin command and non-zero otherwise. Note that even if non-zero status is returned, zle may still be active as part of the completion system; this does not allow direct calls to ZLE widgets. </p>
<p> Otherwise, which operation it performs depends on its options: </p>
 </dd>
<dl>
<dd> <p> <code>-l</code> [ <code>-L</code> | <code>-a</code> ] [ <i>string</i> ] List all existing user-defined widgets. If the <code>-L</code> option is used, list in the form of <code>zle</code> commands to create the widgets. </p>
 </dd>
<dl>
<dd> <p> When combined with the <code>-a</code> option, all widget names are listed, including the builtin ones. In this case the <code>-L</code> option is ignored. </p>
<p> If at least one <i>string</i> is given, and <code>-a</code> is present or <code>-L</code> is not used, nothing will be printed. The return status will be zero if all <i>string</i>s are names of existing widgets and non-zero if at least one <i>string</i> is not a name of a defined widget. If <code>-a</code> is also present, all widget names are used for the comparison including builtin widgets, else only user-defined widgets are used. </p>
<p> If at least one <i>string</i> is present and the <code>-L</code> option is used, user-defined widgets matching any <i>string</i> are listed in the form of <code>zle</code> commands to create the widgets. </p>
 </dd></dl>
<dt><code>-D</code><i>widget</i> ...</dt>
<dd> <p> Delete the named <i>widget</i>s. </p>
 </dd>
<dt><code>-A</code><i>old-widget</i><i>new-widget</i></dt>
<dd> <p> Make the <i>new-widget</i> name an alias for <i>old-widget</i>, so that both names refer to the same widget. The names have equal standing; if either is deleted, the other remains. If there is already a widget with the <i>new-widget</i> name, it is deleted. </p>
 </dd>
<dt><code>-N</code><i>widget</i> [ <i>function</i> ]</dt>
<dd> <p> Create a user-defined widget. If there is already a widget with the specified name, it is overwritten. When the new widget is invoked from within the editor, the specified shell <i>function</i> is called. If no function name is specified, it defaults to the same name as the widget. For further information, see the section `Widgets&#8217; below. </p>
 </dd>
<dt><code>-f</code><i>flag</i> [ <i>flag</i>... ]</dt>
<dd> <p> Set various flags on the running widget. Possible values for <i>flag</i> are: </p>
 </dd>
<dl>
<dd> <p> <code>yank</code> for indicating that the widget has yanked text into the buffer. If the widget is wrapping an existing internal widget, no further action is necessary, but if it has inserted the text manually, then it should also take care to set <code>YANK_START</code> and <code>YANK_END</code> correctly. <code>yankbefore</code> does the same but is used when the yanked text appears after the cursor. </p>
<p> <code>kill</code> for indicating that text has been killed into the cutbuffer. When repeatedly invoking a kill widget, text is appended to the cutbuffer instead of replacing it, but when wrapping such widgets, it is necessary to call `<code>zle -f kill</code>&#8216; to retain this effect. </p>
<p> <code>vichange</code> for indicating that the widget represents a vi change that can be repeated as a whole with `<code>vi-repeat-change</code>&#8216;. The flag should be set early in the function before inspecting the value of <code>NUMERIC</code> or invoking other widgets. This has no effect for a widget invoked from insert mode. If insert mode is active when the widget finishes, the change extends until next returning to command mode. </p>
 </dd></dl>
<dt><code>-C</code><i>widget</i><i>completion-widget</i><i>function</i></dt>
<dd> <p> Create a user-defined completion widget named <i>widget</i>. The completion widget will behave like the built-in completion-widget whose name is given as <i>completion-widget</i>. To generate the completions, the shell function <i>function</i> will be called. For further information, see <i><a href="/docs/linux/man/1-zshcompwid/">zshcompwid</a></i>(1). </p>
 </dd>
<dt><code>-R</code> [ <code>-c</code> ] [ <i>display-string</i> ] [ <i>string</i> ... ]</dt>
<dd> <p> Redisplay the command line; this is to be called from within a user-defined widget to allow changes to become visible. If a <i>display-string</i> is given and not empty, this is shown in the status line (immediately below the line being edited). </p>
 </dd>
<dl>
<dd> <p> If the optional <i>string</i>s are given they are listed below the prompt in the same way as completion lists are printed. If no <i>string</i>s are given but the <code>-c</code> option is used such a list is cleared. </p>
<p> Note that this option is only useful for widgets that do not exit immediately after using it because the strings displayed will be erased immediately after return from the widget. </p>
<p> This command can safely be called outside user defined widgets; if zle is active, the display will be refreshed, while if zle is not active, the command has no effect. In this case there will usually be no other arguments. </p>
<p> The status is zero if zle was active, else one. </p>
 </dd></dl>
<dt><code>-M</code><i>string</i></dt>
<dd> <p> As with the <code>-R</code> option, the <i>string</i> will be displayed below the command line; unlike the <code>-R</code> option, the string will not be put into the status line but will instead be printed normally below the prompt. This means that the <i>string</i> will still be displayed after the widget returns (until it is overwritten by subsequent commands). </p>
 </dd>
<dt><code>-U</code><i>string</i></dt>
<dd> <p> This pushes the characters in the <i>string</i> onto the input stack of ZLE. After the widget currently executed finishes ZLE will behave as if the characters in the <i>string</i> were typed by the user. </p>
 </dd>
<dl>
<dd> <p> As ZLE uses a stack, if this option is used repeatedly the last string pushed onto the stack will be processed first. However, the characters in each <i>string</i> will be processed in the order in which they appear in the string. </p>
 </dd></dl>
<dt><code>-K</code><i>keymap</i></dt>
<dd> <p> Selects the keymap named <i>keymap</i>. An error message will be displayed if there is no such keymap. </p>
 </dd>
<dl>
<dd> <p> This keymap selection affects the interpretation of following keystrokes within this invocation of ZLE. Any following invocation (e.g., the next command line) will start as usual with the `<code>main</code>&#8216; keymap selected. </p>
 </dd></dl>
<dt><code>-F</code> [ <code>-L</code> | <code>-w</code> ] [ <i>fd</i> [ <i>handler</i> ] ]</dt>
<dd> <p> Only available if your system supports one of the `poll&#8217; or `select&#8217; system calls; most modern systems do. </p>
 </dd>
<dl>
<dd> <p> Installs <i>handler</i> (the name of a shell function) to handle input from file descriptor <i>fd</i>. Installing a handler for an <i>fd</i> which is already handled causes the existing handler to be replaced. Any number of handlers for any number of readable file descriptors may be installed. Note that zle makes no attempt to check whether this <i>fd</i> is actually readable when installing the handler. The user must make their own arrangements for handling the file descriptor when zle is not active. </p>
<p> When zle is attempting to read data, it will examine both the terminal and the list of handled <i>fd</i>&#8216;s. If data becomes available on a handled <i>fd</i>, zle calls <i>handler</i> with the fd which is ready for reading as the first argument. Under normal circumstances this is the only argument, but if an error was detected, a second argument provides details: `<code>hup</code>&#8216; for a disconnect, `<code>nval</code>&#8216; for a closed or otherwise invalid descriptor, or `<code>err</code>&#8216; for any other condition. Systems that support only the `select&#8217; system call always use `<code>err</code>&#8216;. </p>
<p> If the option <code>-w</code> is also given, the <i>handler</i> is instead a line editor widget, typically a shell function made into a widget using `<code>zle -N</code>&#8216;. In that case <i>handler</i> can use all the facilities of zle to update the current editing line. Note, however, that as handling <i>fd</i> takes place at a low level changes to the display will not automatically appear; the widget should call `<code>zle -R</code>&#8216; to force redisplay. As of this writing, widget handlers only support a single argument and thus are never passed a string for error state, so widgets must be prepared to test the descriptor themselves. </p>
<p> If either type of handler produces output to the terminal, it should call `<code>zle -I</code>&#8216; before doing so (see below). Handlers should not attempt to read from the terminal. </p>
<p> If no <i>handler</i> is given, but an <i>fd</i> is present, any handler for that <i>fd</i> is removed. If there is none, an error message is printed and status 1 is returned. </p>
<p> If no arguments are given, or the <code>-L</code> option is supplied, a list of handlers is printed in a form which can be stored for later execution. </p>
<p> An <i>fd</i> (but not a <i>handler</i>) may optionally be given with the <code>-L</code> option; in this case, the function will list the handler if any, else silently return status 1. </p>
<p> Note that this feature should be used with care. Activity on one of the <i>fd</i>&#8216;s which is not properly handled can cause the terminal to become unusable. Removing an <i>fd</i> handler from within a signal trap may cause unpredictable behavior. </p>
<p> Here is a simple example of using this feature. A connection to a remote TCP port is created using the ztcp command; see the description of the <code>zsh/net/tcp</code> module in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). Then a handler is installed which simply prints out any data which arrives on this connection. Note that `select&#8217; will indicate that the file descriptor needs handling if the remote side has closed the connection; we handle that by testing for a failed read. </p>
 </dd>
<dl>
<dd> <pre><code>
 if ztcp pwspc 2811; then
  tcpfd=$REPLY
  handler() {
    zle -I
    local line
    if ! read -r line &lt;&amp;$1; then
      # select marks this fd if we reach EOF,
      # so handle this specially.
      print &quot;[Read on fd $1 failed, removing.]&quot; &gt;&amp;2
      zle -F $1
      return 1
    fi
    print -r - $line
  }
  zle -F $tcpfd handler
fi 
</code></pre>
 </dd></dl>
</dl>
<dt><code>-I</code></dt>
<dd> <p> Unusually, this option is most useful outside ordinary widget functions, though it may be used within if normal output to the terminal is required. It invalidates the current zle display in preparation for output; typically this will be from a trap function. It has no effect if zle is not active. When a trap exits, the shell checks to see if the display needs restoring, hence the following will print output in such a way as not to disturb the line being edited: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>
 TRAPUSR1() {
  # Invalidate zle display
  [[ -o zle ]] &amp;&amp; zle -I
  # Show output
  print Hello
} 
</code></pre>
 </dd></dl>
<p> In general, the trap function may need to test whether zle is active before using this method (as shown in the example), since the <code>zsh/zle</code> module may not even be loaded; if it is not, the command can be skipped. </p>
<p> It is possible to call `<code>zle -I</code>&#8216; several times before control is returned to the editor; the display will only be invalidated the first time to minimise disruption. </p>
<p> Note that there are normally better ways of manipulating the display from within zle widgets; see, for example, `<code>zle -R</code>&#8216; above. </p>
<p> The returned status is zero if zle was invalidated, even though this may have been by a previous call to `<code>zle -I</code>&#8216; or by a system notification. To test if a zle widget may be called at this point, execute <code>zle</code> with no arguments and examine the return status. </dl>
 </p>
<dt><code>-T</code></dt>
<dd> <p> This is used to add, list or remove internal transformations on the processing performed by the line editor. It is typically used only for debugging or testing and is therefore of little interest to the general user. </p>
 </dd>
<dl>
<dd> <p> `<code>zle -T</code> <i>transformation</i> <i>func</i>&#8216; specifies that the given <i>transformation</i> (see below) is effected by shell function <i>func</i>. </p>
<p> `<code>zle -Tr</code> <i>transformation</i>&#8216; removes the given <i>transformation</i> if it was present (it is not an error if none was). </p>
<p> `<code>zle -TL</code>&#8216; can be used to list all transformations currently in operation. </p>
<p> Currently the only transformation is <code>tc</code>. This is used instead of outputting termcap codes to the terminal. When the transformation is in operation the shell function is passed the termcap code that would be output as its first argument; if the operation required a numeric argument, that is passed as a second argument. The function should set the shell variable <code>REPLY</code> to the transformed termcap code. Typically this is used to produce some simply formatted version of the code and optional argument for debugging or testing. Note that this transformation is not applied to other non-printing characters such as carriage returns and newlines. </p>
 </dd></dl>
<dt><i>widget</i> [ <code>-n</code><i>num</i> ] [ <code>-Nw</code> ] [ <code>-K</code><i>keymap</i> ] <i>args</i> ...</dt>
<dd> <p> Invoke the specified <i>widget</i>. This can only be done when ZLE is active; normally this will be within a user-defined widget. </p>
 </dd>
<dl>
<dd> <p> With the options <code>-n</code> and <code>-N</code>, the current numeric argument will be saved and then restored after the call to <i>widget</i>; `<code>-n</code> <i>num</i>&#8216; sets the numeric argument temporarily to <i>num</i>, while `<code>-N</code>&#8216; sets it to the default, i.e. as if there were none. </p>
<p> With the option <code>-K</code>, <i>keymap</i> will be used as the current keymap during the execution of the widget. The previous keymap will be restored when the widget exits. </p>
<p> Normally, calling a widget in this way does not set the special parameter <code>WIDGET</code> and related parameters, so that the environment appears as if the top-level widget called by the user were still active. With the option <code>-w</code>, <code>WIDGET</code> and related parameters are set to reflect the widget being executed by the <code>zle</code> call. </p>
<p> Any further arguments will be passed to the widget; note that as standard argument handling is performed, any general argument list should be preceded by <code>-</code><code>-</code>. If it is a shell function, these are passed down as positional parameters; for builtin widgets it is up to the widget in question what it does with them. Currently arguments are only handled by the incremental-search commands, the <code>history-search-forward</code> and <code>-backward</code> and the corresponding functions prefixed by <code>vi-</code>, and by <code>universal-argument</code>. No error is flagged if the command does not use the arguments, or only uses some of them. </p>
<p> The return status reflects the success or failure of the operation carried out by the widget, or if it is a user-defined widget the return status of the shell function. </p>
<p> A non-zero return status causes the shell to beep when the widget exits, unless the <code>BEEP</code> options was unset or the widget was called via the <code>zle</code> command. Thus if a user defined widget requires an immediate beep, it should call the <code>beep</code> widget directly. </p>
 </dd></dl>
</dl>
</dl>
</dl>
<h2>WIDGETS</h2>
<p> All actions in the editor are performed by `widgets&#8217;. A widget&#8217;s job is simply to perform some small action. The ZLE commands that key sequences in keymaps are bound to are in fact widgets. Widgets can be user-defined or built in. </p>
<p> The standard widgets built into ZLE are listed in Standard Widgets below. Other built-in widgets can be defined by other modules (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). Each built-in widget has two names: its normal canonical name, and the same name preceded by a `<code>.</code>&#8216;. The `<code>.</code>&#8216; name is special: it can&#8217;t be rebound to a different widget. This makes the widget available even when its usual name has been redefined. </p>
<p> User-defined widgets are defined using `<code>zle -N</code>&#8216;, and implemented as shell functions. When the widget is executed, the corresponding shell function is executed, and can perform editing (or other) actions. It is recommended that user-defined widgets should not have names starting with `<code>.</code>&#8216;.  </p>
<h2>USER-DEFINED WIDGETS</h2>
<p> User-defined widgets, being implemented as shell functions, can execute any normal shell command. They can also run other widgets (whether built-in or user-defined) using the <code>zle</code> builtin command. The standard input of the function is redirected from /dev/null to prevent external commands from unintentionally blocking ZLE by reading from the terminal, but <code>read -k</code> or <code>read -q</code> can be used to read characters. Finally, they can examine and edit the ZLE buffer being edited by reading and setting the special parameters described below. </p>
<p> These special parameters are always available in widget functions, but are not in any way special outside ZLE. If they have some normal value outside ZLE, that value is temporarily inaccessible, but will return when the widget function exits. These special parameters in fact have local scope, like parameters created in a function using <code>local</code>. </p>
<p> Inside completion widgets and traps called while ZLE is active, these parameters are available read-only. </p>
<p> Note that the parameters appear as local to any ZLE widget in which they appear. Hence if it is desired to override them this needs to be done within a nested function: </p>
<dl>
<dd> <pre><code>
 widget-function() {
  # $WIDGET here refers to the special variable
  # that is local inside widget-function
  () {
     # This anonymous nested function allows WIDGET
     # to be used as a local variable. The -h
     # removes the special status of the variable.
     local -h WIDGET
  }
} 
</code></pre>
 </dd></dl>
<dl>
<dd> <p> <code>BUFFER</code> (scalar) The entire contents of the edit buffer. If it is written to, the cursor remains at the same offset, unless that would put it outside the buffer. </p>
 </dd>
<dt><code>BUFFERLINES</code> (integer)</dt>
<dd> <p> The number of screen lines needed for the edit buffer currently displayed on screen (i.e. without any changes to the preceding parameters done after the last redisplay); read-only. </p>
 </dd>
<dt><code>CONTEXT</code> (scalar)</dt>
<dd> <p> The context in which zle was called to read a line; read-only. One of the values: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>start</code> The start of a command line (at prompt <code>PS1</code>). </p>
 </dd>
<dt><code>cont</code></dt>
<dd> <p> A continuation to a command line (at prompt <code>PS2</code>). </p>
 </dd>
<dt><code>select</code></dt>
<dd> <p> In a <code>select</code> loop (at prompt <code>PS3</code>). </p>
 </dd>
<dt><code>vared</code></dt>
<dd> <p> Editing a variable in <code>vared</code>. </p>
 </dd></dl>
</dl>
<dt><code>CURSOR</code> (integer)</dt>
<dd> <p> The offset of the cursor, within the edit buffer. This is in the range 0 to <code>$#BUFFER</code>, and is by definition equal to <code>$#LBUFFER</code>. Attempts to move the cursor outside the buffer will result in the cursor being moved to the appropriate end of the buffer. </p>
 </dd>
<dt><code>CUTBUFFER</code> (scalar)</dt>
<dd> <p> The last item cut using one of the `<code>kill-</code>&#8216; commands; the string which the next yank would insert in the line. Later entries in the kill ring are in the array <code>killring</code>. Note that the command `<code>zle copy-region-as-kill</code> <i>string</i>&#8216; can be used to set the text of the cut buffer from a shell function and cycle the kill ring in the same way as interactively killing text. </p>
 </dd>
<dt><code>HISTNO</code> (integer)</dt>
<dd> <p> The current history number. Setting this has the same effect as moving up or down in the history to the corresponding history line. An attempt to set it is ignored if the line is not stored in the history. Note this is not the same as the parameter <code>HISTCMD</code>, which always gives the number of the history line being added to the main shell&#8217;s history. <code>HISTNO</code> refers to the line being retrieved within zle. </p>
 </dd>
<dd> <p> <code>ISEARCHMATCH_ACTIVE</code> (integer) </p>
 </dd>
<dd> <p> <code>ISEARCHMATCH_START</code> (integer) </p>
 </dd>
<dd> <p> <code>ISEARCHMATCH_END</code> (integer) <code>ISEARCHMATCH_ACTIVE</code> indicates whether a part of the <code>BUFFER</code> is currently matched by an incremental search pattern. <code>ISEARCHMATCH_START</code> and <code>ISEARCHMATCH_END</code> give the location of the matched part and are in the same units as <code>CURSOR</code>. They are only valid for reading when <code>ISEARCHMATCH_ACTIVE</code> is non-zero. </p>
 </dd>
<dl>
<dd> <p> All parameters are read-only. </p>
 </dd></dl>
<dt><code>KEYMAP</code> (scalar)</dt>
<dd> <p> The name of the currently selected keymap; read-only. </p>
 </dd>
<dt><code>KEYS</code> (scalar)</dt>
<dd> <p> The keys typed to invoke this widget, as a literal string; read-only. </p>
 </dd>
<dt><code>KEYS_QUEUED_COUNT</code> (integer)</dt>
<dd> <p> The number of bytes pushed back to the input queue and therefore available for reading immediately before any I/O is done; read-only. See also <code>PENDING</code>; the two values are distinct. </p>
 </dd>
<dt><code>killring</code> (array)</dt>
<dd> <p> The array of previously killed items, with the most recently killed first. This gives the items that would be retrieved by a <code>yank-pop</code> in the same order. Note, however, that the most recently killed item is in <code>$CUTBUFFER</code>; <code>$killring</code> shows the array of previous entries. </p>
 </dd>
<dl>
<dd> <p> The default size for the kill ring is eight, however the length may be changed by normal array operations. Any empty string in the kill ring is ignored by the <code>yank-pop</code> command, hence the size of the array effectively sets the maximum length of the kill ring, while the number of non-zero strings gives the current length, both as seen by the user at the command line. </p>
 </dd></dl>
<dt><code>LASTABORTEDSEARCH</code> (scalar)</dt>
<dd> <p> The last search string used by an interactive search that was aborted by the user (status 3 returned by the search widget). </p>
 </dd>
<dt><code>LASTSEARCH</code> (scalar)</dt>
<dd> <p> The last search string used by an interactive search; read-only. This is set even if the search failed (status 0, 1 or 2 returned by the search widget), but not if it was aborted by the user. </p>
 </dd>
<dt><code>LASTWIDGET</code> (scalar)</dt>
<dd> <p> The name of the last widget that was executed; read-only. </p>
 </dd>
<dt><code>LBUFFER</code> (scalar)</dt>
<dd> <p> The part of the buffer that lies to the left of the cursor position. If it is assigned to, only that part of the buffer is replaced, and the cursor remains between the new <code>$LBUFFER</code> and the old <code>$RBUFFER</code>. </p>
 </dd>
<dt><code>MARK</code> (integer)</dt>
<dd> <p> Like <code>CURSOR</code>, but for the mark. With vi-mode operators that wait for a movement command to select a region of text, setting <code>MARK</code> allows the selection to extend in both directions from the initial cursor position. </p>
 </dd>
<dt><code>NUMERIC</code> (integer)</dt>
<dd> <p> The numeric argument. If no numeric argument was given, this parameter is unset. When this is set inside a widget function, builtin widgets called with the <code>zle</code> builtin command will use the value assigned. If it is unset inside a widget function, builtin widgets called behave as if no numeric argument was given. </p>
 </dd>
<dt><code>PENDING</code> (integer)</dt>
<dd> <p> The number of bytes pending for input, i.e. the number of bytes which have already been typed and can immediately be read. On systems where the shell is not able to get this information, this parameter will always have a value of zero. Read-only. See also <code>KEYS_QUEUED_COUNT</code>; the two values are distinct. </p>
 </dd>
<dt><code>PREBUFFER</code> (scalar)</dt>
<dd> <p> In a multi-line input at the secondary prompt, this read-only parameter contains the contents of the lines before the one the cursor is currently in. </p>
 </dd>
<dt><code>PREDISPLAY</code> (scalar)</dt>
<dd> <p> Text to be displayed before the start of the editable text buffer. This does not have to be a complete line; to display a complete line, a newline must be appended explicitly. The text is reset on each new invocation (but not recursive invocation) of zle. </p>
 </dd>
<dt><code>POSTDISPLAY</code> (scalar)</dt>
<dd> <p> Text to be displayed after the end of the editable text buffer. This does not have to be a complete line; to display a complete line, a newline must be prepended explicitly. The text is reset on each new invocation (but not recursive invocation) of zle. </p>
 </dd>
<dt><code>RBUFFER</code> (scalar)</dt>
<dd> <p> The part of the buffer that lies to the right of the cursor position. If it is assigned to, only that part of the buffer is replaced, and the cursor remains between the old <code>$LBUFFER</code> and the new <code>$RBUFFER</code>. </p>
 </dd>
<dt><code>REGION_ACTIVE</code> (integer)</dt>
<dd> <p> Indicates if the region is currently active. It can be assigned 0 or 1 to deactivate and activate the region respectively. A value of 2 activates the region in line-wise mode with the highlighted text extending for whole lines only; see <i>Character Highlighting</i> below. </p>
 </dd>
<dt><code>region_highlight</code> (array)</dt>
<dd> <p> Each element of this array may be set to a string that describes highlighting for an arbitrary region of the command line that will take effect the next time the command line is redisplayed. Highlighting of the non-editable parts of the command line in <code>PREDISPLAY</code> and <code>POSTDISPLAY</code> are possible, but note that the <code>P</code> flag is needed for character indexing to include <code>PREDISPLAY</code>. </p>
 </dd>
<dl>
<dd> <p> Each string consists of the following parts: </p>
 </dd>
<dl>
<dd> <p> &bull; Optionally, a `<code>P</code>&#8216; to signify that the start and end offset that follow include any string set by the <code>PREDISPLAY</code> special parameter; this is needed if the predisplay string itself is to be highlighted. Whitespace may follow the `<code>P</code>&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A start offset in the same units as <code>CURSOR</code>, terminated by whitespace. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An end offset in the same units as <code>CURSOR</code>, terminated by whitespace. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A highlight specification in the same format as used for contexts in the parameter <code>zle_highlight</code>, see the section `Character Highlighting&#8217; below; for example, <code>standout</code> or <code>fg=red,bold</code> </p>
 </dd></dl>
<p> For example, </p>
<dl>
<dd> <pre><code>
 region_highlight=(&quot;P0 20 bold&quot;) 
</code></pre>
 </dd></dl>
<p> specifies that the first twenty characters of the text including any predisplay string should be highlighted in bold. </p>
<p> Note that the effect of <code>region_highlight</code> is not saved and disappears as soon as the line is accepted. </p>
<p> The final highlighting on the command line depends on both <code>region_highlight</code> and <code>zle_highlight</code>; see the section CHARACTER HIGHLIGHTING below for details. </dl>
 </p>
<dt><code>registers</code> (associative array)</dt>
<dd> <p> The contents of each of the vi register buffers. These are typically set using <code>vi-set-buffer</code> followed by a delete, change or yank command. </p>
 </dd>
<dd> <p> <code>SUFFIX_ACTIVE</code> (integer) </p>
 </dd>
<dd> <p> <code>SUFFIX_START</code> (integer) </p>
 </dd>
<dd> <p> <code>SUFFIX_END</code> (integer) <code>SUFFIX_ACTIVE</code> indicates whether an auto-removable completion suffix is currently active. <code>SUFFIX_START</code> and <code>SUFFIX_END</code> give the location of the suffix and are in the same units as <code>CURSOR</code>. They are only valid for reading when <code>SUFFIX_ACTIVE</code> is non-zero. </p>
 </dd>
<dl>
<dd> <p> All parameters are read-only. </p>
 </dd></dl>
<dt><code>UNDO_CHANGE_NO</code> (integer)</dt>
<dd> <p> A number representing the state of the undo history. The only use of this is passing as an argument to the <code>undo</code> widget in order to undo back to the recorded point. Read-only. </p>
 </dd>
<dt><code>UNDO_LIMIT_NO</code> (integer)</dt>
<dd> <p> A number corresponding to an existing change in the undo history; compare <code>UNDO_CHANGE_NO</code>. If this is set to a value greater than zero, the <code>undo</code> command will not allow the line to be undone beyond the given change number. It is still possible to use `<code>zle undo</code> <i>change</i>&#8216; in a widget to undo beyond that point; in that case, it will not be possible to undo at all until <code>UNDO_LIMIT_NO</code> is reduced. Set to 0 to disable the limit. </p>
 </dd>
<dl>
<dd> <p> A typical use of this variable in a widget function is as follows (note the additional function scope is required): </p>
 </dd>
<dl>
<dd> <pre><code>
 () {
  local UNDO_LIMIT_NO=$UNDO_CHANGE_NO
  # Perform some form of recursive edit.
} 
</code></pre>
 </dd></dl>
</dl>
<dt><code>WIDGET</code> (scalar)</dt>
<dd> <p> The name of the widget currently being executed; read-only. </p>
 </dd>
<dt><code>WIDGETFUNC</code> (scalar)</dt>
<dd> <p> The name of the shell function that implements a widget defined with either <code>zle -N</code> or <code>zle -C</code>. In the former case, this is the second argument to the <code>zle -N</code> command that defined the widget, or the first argument if there was no second argument. In the latter case this is the third argument to the <code>zle -C</code> command that defined the widget. Read-only. </p>
 </dd>
<dt><code>WIDGETSTYLE</code> (scalar)</dt>
<dd> <p> Describes the implementation behind the completion widget currently being executed; the second argument that followed <code>zle -C</code> when the widget was defined. This is the name of a builtin completion widget. For widgets defined with <code>zle -N</code> this is set to the empty string. Read-only. </p>
 </dd>
<dd> <p> <code>YANK_ACTIVE</code> (integer) </p>
 </dd>
<dd> <p> <code>YANK_START</code> (integer) </p>
 </dd>
<dd> <p> <code>YANK_END</code> (integer) <code>YANK_ACTIVE</code> indicates whether text has just been yanked (pasted) into the buffer. <code>YANK_START</code> and <code>YANK_END</code> give the location of the pasted text and are in the same units as <code>CURSOR</code>. They are only valid for reading when <code>YANK_ACTIVE</code> is non-zero. They can also be assigned by widgets that insert text in a yank-like fashion, for example wrappers of <code>bracketed-paste</code>. See also <code>zle -f</code>. </p>
 </dd>
<dl>
<dd> <p> <code>YANK_ACTIVE</code> is read-only. </p>
 </dd></dl>
<dt><code>ZLE_RECURSIVE</code> (integer)</dt>
<dd> <p> Usually zero, but incremented inside any instance of <code>recursive-edit</code>. Hence indicates the current recursion level. </p>
 </dd>
<dl>
<dd> <p> <code>ZLE_RECURSIVE</code> is read-only. </p>
 </dd></dl>
<dt><code>ZLE_STATE</code> (scalar)</dt>
<dd> <p> Contains a set of space-separated words that describe the current <code>zle</code> state. </p>
 </dd>
<dl>
<dd> <p> Currently, the states shown are the insert mode as set by the <code>overwrite-mode</code> or <code>vi-replace</code> widgets and whether history commands will visit imported entries as controlled by the set-local-history widget. The string contains `<code>insert</code>&#8216; if characters to be inserted on the command line move existing characters to the right or `<code>overwrite</code>&#8216; if characters to be inserted overwrite existing characters. It contains `<code>localhistory</code>&#8216; if only local history commands will be visited or `<code>globalhistory</code>&#8216; if imported history commands will also be visited. </p>
<p> The substrings are sorted in alphabetical order so that if you want to test for two specific substrings in a future-proof way, you can do match by doing: </p>
 </dd>
<dl>
<dd> <pre><code>
 if [[ $ZLE_STATE == *globalhistory*insert* ]]; then ...; fi 
</code></pre>
 </dd></dl>
</dl>
</dl>
<h3>Special Widgets</h3>
<p> There are a few user-defined widgets which are special to the shell. If they do not exist, no special action is taken. The environment provided is identical to that for any other editing widget. </p>
<dl>
<dd> <p> <code>zle-isearch-exit</code> Executed at the end of incremental search at the point where the isearch prompt is removed from the display. See <code>zle-isearch-update</code> for an example. </p>
 </dd>
<dt><code>zle-isearch-update</code></dt>
<dd> <p> Executed within incremental search when the display is about to be redrawn. Additional output below the incremental search prompt can be generated by using `<code>zle -M</code>&#8216; within the widget. For example, </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>
 zle-isearch-update() { zle -M &quot;Line $HISTNO&quot;; }
zle -N zle-isearch-update 
</code></pre>
 </dd></dl>
<p> Note the line output by `<code>zle -M</code>&#8216; is not deleted on exit from incremental search. This can be done from a <code>zle-isearch-exit</code> widget: </p>
<dl>
<dd> <pre><code>
 zle-isearch-exit() { zle -M &quot;&quot;; }
zle -N zle-isearch-exit 
</code></pre>
 </dd></dl>
</dl>
<dt><code>zle-line-pre-redraw</code></dt>
<dd> <p> Executed whenever the input line is about to be redrawn, providing an opportunity to update the region_highlight array. </p>
 </dd>
<dt><code>zle-line-init</code></dt>
<dd> <p> Executed every time the line editor is started to read a new line of input. The following example puts the line editor into vi command mode when it starts up. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <pre><code>
 zle-line-init() { zle -K vicmd; }
zle -N zle-line-init 
</code></pre>
 </dd></dl>
<p> (The command inside the function sets the keymap directly; it is equivalent to <code>zle vi-cmd-mode</code>.) </dl>
 </p>
<dt><code>zle-line-finish</code></dt>
<dd> <p> This is similar to <code>zle-line-init</code> but is executed every time the line editor has finished reading a line of input. </p>
 </dd>
<dt><code>zle-history-line-set</code></dt>
<dd> <p> Executed when the history line changes. </p>
 </dd>
<dt><code>zle-keymap-select</code></dt>
<dd> <p> Executed every time the keymap changes, i.e. the special parameter <code>KEYMAP</code> is set to a different value, while the line editor is active. Initialising the keymap when the line editor starts does not cause the widget to be called. </p>
 </dd>
<dl>
<dd> <p> The value <code>$KEYMAP</code> within the function reflects the new keymap. The old keymap is passed as the sole argument. </p>
<p> This can be used for detecting switches between the vi command (<code>vicmd</code>) and insert (usually <code>main</code>) keymaps. </p>
 </dd></dl>
</dl>
<h2>STANDARD WIDGETS</h2>
<p> The following is a list of all the standard widgets, and their default bindings in emacs mode, vi command mode and vi insert mode (the `<code>emacs</code>&#8216;, `<code>vicmd</code>&#8216; and `<code>viins</code>&#8216; keymaps, respectively). </p>
<p> Note that cursor keys are bound to movement keys in all three keymaps; the shell assumes that the cursor keys send the key sequences reported by the terminal-handling library (termcap or terminfo). The key sequences shown in the list are those based on the VT100, common on many modern terminals, but in fact these are not necessarily bound. In the case of the <code>viins</code> keymap, the initial escape character of the sequences serves also to return to the <code>vicmd</code> keymap: whether this happens is determined by the <code>KEYTIMEOUT</code> parameter, see <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1).  </p>
<h3>Movement</h3>
<dl>
<dd> <p> <code>vi-backward-blank-word</code> (unbound) (<code>B</code>) (unbound) Move backward one word, where a word is defined as a series of non-blank characters. </p>
 </dd>
<dt><code>vi-backward-blank-word-end</code> (unbound) (<code>gE</code>) (unbound)</dt>
<dd> <p> Move to the end of the previous word, where a word is defined as a series of non-blank characters. </p>
 </dd>
<dt><code>backward-char</code> (<code>^B ESC-[D</code>) (unbound) (unbound)</dt>
<dd> <p> Move backward one character. </p>
 </dd>
<dt><code>vi-backward-char</code> (unbound) (<code>^H h ^?</code>) (<code>ESC-[D</code>)</dt>
<dd> <p> Move backward one character, without changing lines. </p>
 </dd>
<dt><code>backward-word</code> (<code>ESC-B ESC-b</code>) (unbound) (unbound)</dt>
<dd> <p> Move to the beginning of the previous word. </p>
 </dd>
<dt><code>emacs-backward-word</code></dt>
<dd> <p> Move to the beginning of the previous word. </p>
 </dd>
<dt><code>vi-backward-word</code> (unbound) (<code>b</code>) (unbound)</dt>
<dd> <p> Move to the beginning of the previous word, vi-style. </p>
 </dd>
<dt><code>vi-backward-word-end</code> (unbound) (<code>ge</code>) (unbound)</dt>
<dd> <p> Move to the end of the previous word, vi-style. </p>
 </dd>
<dt><code>beginning-of-line</code> (<code>^A</code>) (unbound) (unbound)</dt>
<dd> <p> Move to the beginning of the line. If already at the beginning of the line, move to the beginning of the previous line, if any. </p>
 </dd>
<dt><code>vi-beginning-of-line</code></dt>
<dd> <p> Move to the beginning of the line, without changing lines. </p>
 </dd>
<dt><code>down-line</code> (unbound) (unbound) (unbound)</dt>
<dd> <p> Move down a line in the buffer. </p>
 </dd>
<dt><code>end-of-line</code> (<code>^E</code>) (unbound) (unbound)</dt>
<dd> <p> Move to the end of the line. If already at the end of the line, move to the end of the next line, if any. </p>
 </dd>
<dt><code>vi-end-of-line</code> (unbound) (<code>$</code>) (unbound)</dt>
<dd> <p> Move to the end of the line. If an argument is given to this command, the cursor will be moved to the end of the line (argument - 1) lines down. </p>
 </dd>
<dt><code>vi-forward-blank-word</code> (unbound) (<code>W</code>) (unbound)</dt>
<dd> <p> Move forward one word, where a word is defined as a series of non-blank characters. </p>
 </dd>
<dt><code>vi-forward-blank-word-end</code> (unbound) (<code>E</code>) (unbound)</dt>
<dd> <p> Move to the end of the current word, or, if at the end of the current word, to the end of the next word, where a word is defined as a series of non-blank characters. </p>
 </dd>
<dt><code>forward-char</code> (<code>^F ESC-[C</code>) (unbound) (unbound)</dt>
<dd> <p> Move forward one character. </p>
 </dd>
<dt><code>vi-forward-char</code> (unbound) (<code>space l</code>) (<code>ESC-[C</code>)</dt>
<dd> <p> Move forward one character. </p>
 </dd>
<dt><code>vi-find-next-char</code> (<code>^X^F</code>) (<code>f</code>) (unbound)</dt>
<dd> <p> Read a character from the keyboard, and move to the next occurrence of it in the line. </p>
 </dd>
<dt><code>vi-find-next-char-skip</code> (unbound) (<code>t</code>) (unbound)</dt>
<dd> <p> Read a character from the keyboard, and move to the position just before the next occurrence of it in the line. </p>
 </dd>
<dt><code>vi-find-prev-char</code> (unbound) (<code>F</code>) (unbound)</dt>
<dd> <p> Read a character from the keyboard, and move to the previous occurrence of it in the line. </p>
 </dd>
<dt><code>vi-find-prev-char-skip</code> (unbound) (<code>T</code>) (unbound)</dt>
<dd> <p> Read a character from the keyboard, and move to the position just after the previous occurrence of it in the line. </p>
 </dd>
<dt><code>vi-first-non-blank</code> (unbound) (<code>^</code>) (unbound)</dt>
<dd> <p> Move to the first non-blank character in the line. </p>
 </dd>
<dt><code>vi-forward-word</code> (unbound) (<code>w</code>) (unbound)</dt>
<dd> <p> Move forward one word, vi-style. </p>
 </dd>
<dt><code>forward-word</code> (<code>ESC-F ESC-f</code>) (unbound) (unbound)</dt>
<dd> <p> Move to the beginning of the next word. The editor&#8217;s idea of a word is specified with the <code>WORDCHARS</code> parameter. </p>
 </dd>
<dt><code>emacs-forward-word</code></dt>
<dd> <p> Move to the end of the next word. </p>
 </dd>
<dt><code>vi-forward-word-end</code> (unbound) (<code>e</code>) (unbound)</dt>
<dd> <p> Move to the end of the next word. </p>
 </dd>
<dt><code>vi-goto-column</code> (<code>ESC-|</code>) (<code>|</code>) (unbound)</dt>
<dd> <p> Move to the column specified by the numeric argument. </p>
 </dd>
<dt><code>vi-goto-mark</code> (unbound) (<code>`</code>) (unbound)</dt>
<dd> <p> Move to the specified mark. </p>
 </dd>
<dt><code>vi-goto-mark-line</code> (unbound) (<code>&#8216;</code>) (unbound)</dt>
<dd> <p> Move to beginning of the line containing the specified mark. </p>
 </dd>
<dt><code>vi-repeat-find</code> (unbound) (<code>;</code>) (unbound)</dt>
<dd> <p> Repeat the last <code>vi-find</code> command. </p>
 </dd>
<dt><code>vi-rev-repeat-find</code> (unbound) (<code>,</code>) (unbound)</dt>
<dd> <p> Repeat the last <code>vi-find</code> command in the opposite direction. </p>
 </dd>
<dt><code>up-line</code> (unbound) (unbound) (unbound)</dt>
<dd> <p> Move up a line in the buffer. </p>
 </dd></dl>
<h3>History Control</h3>
<dl>
<dd> <p> <code>beginning-of-buffer-or-history</code> (<code>ESC-&lt;</code>) (<code>gg</code>) (unbound) Move to the beginning of the buffer, or if already there, move to the first event in the history list. </p>
 </dd>
<dt><code>beginning-of-line-hist</code></dt>
<dd> <p> Move to the beginning of the line. If already at the beginning of the buffer, move to the previous history line. </p>
 </dd>
<dt><code>beginning-of-history</code></dt>
<dd> <p> Move to the first event in the history list. </p>
 </dd>
<dt><code>down-line-or-history</code> (<code>^N ESC-[B</code>) (<code>j</code>) (<code>ESC-[B</code>)</dt>
<dd> <p> Move down a line in the buffer, or if already at the bottom line, move to the next event in the history list. </p>
 </dd>
<dt><code>vi-down-line-or-history</code> (unbound) (<code>+</code>) (unbound)</dt>
<dd> <p> Move down a line in the buffer, or if already at the bottom line, move to the next event in the history list. Then move to the first non-blank character on the line. </p>
 </dd>
<dt><code>down-line-or-search</code></dt>
<dd> <p> Move down a line in the buffer, or if already at the bottom line, search forward in the history for a line beginning with the first word in the buffer. </p>
 </dd>
<dl>
<dd> <p> If called from a function by the <code>zle</code> command with arguments, the first argument is taken as the string for which to search, rather than the first word in the buffer. </p>
 </dd></dl>
<dt><code>down-history</code> (unbound) (<code>^N</code>) (unbound)</dt>
<dd> <p> Move to the next event in the history list. </p>
 </dd>
<dt><code>history-beginning-search-backward</code></dt>
<dd> <p> Search backward in the history for a line beginning with the current line up to the cursor. This leaves the cursor in its original position. </p>
 </dd>
<dt><code>end-of-buffer-or-history</code> (<code>ESC-&gt;</code>) (unbound) (unbound)</dt>
<dd> <p> Move to the end of the buffer, or if already there, move to the last event in the history list. </p>
 </dd>
<dt><code>end-of-line-hist</code></dt>
<dd> <p> Move to the end of the line. If already at the end of the buffer, move to the next history line. </p>
 </dd>
<dt><code>end-of-history</code></dt>
<dd> <p> Move to the last event in the history list. </p>
 </dd>
<dt><code>vi-fetch-history</code> (unbound) (<code>G</code>) (unbound)</dt>
<dd> <p> Fetch the history line specified by the numeric argument. This defaults to the current history line (i.e. the one that isn&#8217;t history yet). </p>
 </dd>
<dt><code>history-incremental-search-backward</code> (<code>^R ^Xr</code>) (unbound) (unbound)</dt>
<dd> <p> Search backward incrementally for a specified string. The search is case-insensitive if the search string does not have uppercase letters and no numeric argument was given. The string may begin with `<code>^</code>&#8216; to anchor the search to the beginning of the line. When called from a user-defined function returns the following statuses: 0, if the search succeeded; 1, if the search failed; 2, if the search term was a bad pattern; 3, if the search was aborted by the <code>send-break</code> command. </p>
 </dd>
<dl>
<dd> <p> A restricted set of editing functions is available in the mini-buffer. Keys are looked up in the special <code>isearch</code> keymap, and if not found there in the main keymap (note that by default the <code>isearch</code> keymap is empty). An interrupt signal, as defined by the stty setting, will stop the search and go back to the original line. An undefined key will have the same effect. Note that the following always perform the same task within incremental searches and cannot be replaced by user defined widgets, nor can the set of functions be extended. The supported functions are: </p>
 </dd>
<dl>
<dd> <p> <code>accept-and-hold</code> </p>
 </dd>
<dd> <p> <code>accept-and-infer-next-history</code> </p>
 </dd>
<dd> <p> <code>accept-line</code> </p>
 </dd>
<dd> <p> <code>accept-line-and-down-history</code> Perform the usual function after exiting incremental search. The command line displayed is executed. </p>
 </dd>
<dd> <p> <code>backward-delete-char</code> </p>
 </dd>
<dd> <p> <code>vi-backward-delete-char</code> Back up one place in the search history. If the search has been repeated this does not immediately erase a character in the minibuffer. </p>
 </dd>
<dt><code>accept-search</code></dt>
<dd> <p> Exit incremental search, retaining the command line but performing no further action. Note that this function is not bound by default and has no effect outside incremental search. </p>
 </dd>
<dd> <p> <code>backward-delete-word</code> </p>
 </dd>
<dd> <p> <code>backward-kill-word</code> </p>
 </dd>
<dd> <p> <code>vi-backward-kill-word</code> Back up one character in the minibuffer; if multiple searches have been performed since the character was inserted the search history is rewound to the point just before the character was entered. Hence this has the effect of repeating <code>backward-delete-char</code>. </p>
 </dd>
<dt><code>clear-screen</code></dt>
<dd> <p> Clear the screen, remaining in incremental search mode. </p>
 </dd>
<dt><code>history-incremental-search-backward</code></dt>
<dd> <p> Find the next occurrence of the contents of the mini-buffer. If the mini-buffer is empty, the most recent previously used search string is reinstated. </p>
 </dd>
<dt><code>history-incremental-search-forward</code></dt>
<dd> <p> Invert the sense of the search. </p>
 </dd>
<dt><code>magic-space</code></dt>
<dd> <p> Inserts a non-magical space. </p>
 </dd>
<dd> <p> <code>quoted-insert</code> </p>
 </dd>
<dd> <p> <code>vi-quoted-insert</code> Quote the character to insert into the minibuffer. </p>
 </dd>
<dt><code>redisplay</code></dt>
<dd> <p> Redisplay the command line, remaining in incremental search mode. </p>
 </dd>
<dt><code>vi-cmd-mode</code></dt>
<dd> <p> Select the `<code>vicmd</code>&#8216; keymap; the `<code>main</code>&#8216; keymap (insert mode) will be selected initially. </p>
 </dd>
<dl>
<dd> <p> In addition, the modifications that were made while in vi insert mode are merged to form a single undo event. </p>
 </dd></dl>
<dd> <p> <code>vi-repeat-search</code> </p>
 </dd>
<dd> <p> <code>vi-rev-repeat-search</code> Repeat the search. The direction of the search is indicated in the mini-buffer. </p>
 </dd></dl>
<p> Any character that is not bound to one of the above functions, or <code>self-insert</code> or <code>self-insert-unmeta</code>, will cause the mode to be exited. The character is then looked up and executed in the keymap in effect at that point. </p>
<p> When called from a widget function by the <code>zle</code> command, the incremental search commands can take a string argument. This will be treated as a string of keys, as for arguments to the <code>bindkey</code> command, and used as initial input for the command. Any characters in the string which are unused by the incremental search will be silently ignored. For example, </p>
<dl>
<dd> <pre><code>
 zle history-incremental-search-backward forceps 
</code></pre>
 </dd></dl>
<p> will search backwards for <code>forceps</code>, leaving the minibuffer containing the string `<code>forceps</code>&#8216;. </dl>
 </p>
<dt><code>history-incremental-search-forward</code> (<code>^S ^Xs</code>) (unbound) (unbound)</dt>
<dd> <p> Search forward incrementally for a specified string. The search is case-insensitive if the search string does not have uppercase letters and no numeric argument was given. The string may begin with `<code>^</code>&#8216; to anchor the search to the beginning of the line. The functions available in the mini-buffer are the same as for <code>history-incremental-search-backward</code>. </p>
 </dd>
<dd> <p> <code>history-incremental-pattern-search-backward</code> </p>
 </dd>
<dd> <p> <code>history-incremental-pattern-search-forward</code> These widgets behave similarly to the corresponding widgets with no <code>-pattern</code>, but the search string typed by the user is treated as a pattern, respecting the current settings of the various options affecting pattern matching. See FILENAME GENERATION in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1) for a description of patterns. If no numeric argument was given lowercase letters in the search string may match uppercase letters in the history. The string may begin with `<code>^</code>&#8216; to anchor the search to the beginning of the line. </p>
 </dd>
<dl>
<dd> <p> The prompt changes to indicate an invalid pattern; this may simply indicate the pattern is not yet complete. </p>
<p> Note that only non-overlapping matches are reported, so an expression with wildcards may return fewer matches on a line than are visible by inspection. </p>
 </dd></dl>
<dt><code>history-search-backward</code> (<code>ESC-P ESC-p</code>) (unbound) (unbound)</dt>
<dd> <p> Search backward in the history for a line beginning with the first word in the buffer. </p>
 </dd>
<dl>
<dd> <p> If called from a function by the <code>zle</code> command with arguments, the first argument is taken as the string for which to search, rather than the first word in the buffer. </p>
 </dd></dl>
<dt><code>vi-history-search-backward</code> (unbound) (<code>/</code>) (unbound)</dt>
<dd> <p> Search backward in the history for a specified string. The string may begin with `<code>^</code>&#8216; to anchor the search to the beginning of the line. </p>
 </dd>
<dl>
<dd> <p> A restricted set of editing functions is available in the mini-buffer. An interrupt signal, as defined by the stty setting, will stop the search. The functions available in the mini-buffer are: <code>accept-line</code>, <code>backward-delete-char</code>, <code>vi-backward-delete-char</code>, <code>backward-kill-word</code>, <code>vi-backward-kill-word</code>, <code>clear-screen</code>, <code>redisplay</code>, <code>quoted-insert</code> and <code>vi-quoted-insert</code>. </p>
<p> <code>vi-cmd-mode</code> is treated the same as accept-line, and <code>magic-space</code> is treated as a space. Any other character that is not bound to self-insert or self-insert-unmeta will beep and be ignored. If the function is called from vi command mode, the bindings of the current insert mode will be used. </p>
<p> If called from a function by the <code>zle</code> command with arguments, the first argument is taken as the string for which to search, rather than the first word in the buffer. </p>
 </dd></dl>
<dt><code>history-search-forward</code> (<code>ESC-N ESC-n</code>) (unbound) (unbound)</dt>
<dd> <p> Search forward in the history for a line beginning with the first word in the buffer. </p>
 </dd>
<dl>
<dd> <p> If called from a function by the <code>zle</code> command with arguments, the first argument is taken as the string for which to search, rather than the first word in the buffer. </p>
 </dd></dl>
<dt><code>vi-history-search-forward</code> (unbound) (<code>?</code>) (unbound)</dt>
<dd> <p> Search forward in the history for a specified string. The string may begin with `<code>^</code>&#8216; to anchor the search to the beginning of the line. The functions available in the mini-buffer are the same as for <code>vi-history-search-backward</code>. Argument handling is also the same as for that command. </p>
 </dd>
<dt><code>infer-next-history</code> (<code>^X^N</code>) (unbound) (unbound)</dt>
<dd> <p> Search in the history list for a line matching the current one and fetch the event following it. </p>
 </dd>
<dt><code>insert-last-word</code> (<code>ESC-_ ESC-.</code>) (unbound) (unbound)</dt>
<dd> <p> Insert the last word from the previous history event at the cursor position. If a positive numeric argument is given, insert that word from the end of the previous history event. If the argument is zero or negative insert that word from the left (zero inserts the previous command word). Repeating this command replaces the word just inserted with the last word from the history event prior to the one just used; numeric arguments can be used in the same way to pick a word from that event. </p>
 </dd>
<dl>
<dd> <p> When called from a shell function invoked from a user-defined widget, the command can take one to three arguments. The first argument specifies a history offset which applies to successive calls to this widget: if it is -1, the default behaviour is used, while if it is 1, successive calls will move forwards through the history. The value 0 can be used to indicate that the history line examined by the previous execution of the command will be reexamined. Note that negative numbers should be preceded by a `<code>-</code><code>-</code>&#8216; argument to avoid confusing them with options. </p>
<p> If two arguments are given, the second specifies the word on the command line in normal array index notation (as a more natural alternative to the numeric argument). Hence 1 is the first word, and -1 (the default) is the last word. </p>
<p> If a third argument is given, its value is ignored, but it is used to signify that the history offset is relative to the current history line, rather than the one remembered after the previous invocations of <code>insert-last-word</code>. </p>
<p> For example, the default behaviour of the command corresponds to </p>
 </dd>
<dl>
<dd> <pre><code>
 zle insert-last-word -- -1 -1 
</code></pre>
 </dd></dl>
<p> while the command </p>
<dl>
<dd> <pre><code>
 zle insert-last-word -- -1 1 - 
</code></pre>
 </dd></dl>
<p> always copies the first word of the line in the history immediately before the line being edited. This has the side effect that later invocations of the widget will be relative to that line. </dl>
 </p>
<dt><code>vi-repeat-search</code> (unbound) (<code>n</code>) (unbound)</dt>
<dd> <p> Repeat the last vi history search. </p>
 </dd>
<dt><code>vi-rev-repeat-search</code> (unbound) (<code>N</code>) (unbound)</dt>
<dd> <p> Repeat the last vi history search, but in reverse. </p>
 </dd>
<dt><code>up-line-or-history</code> (<code>^P ESC-[A</code>) (<code>k</code>) (<code>ESC-[A</code>)</dt>
<dd> <p> Move up a line in the buffer, or if already at the top line, move to the previous event in the history list. </p>
 </dd>
<dt><code>vi-up-line-or-history</code> (unbound) (<code>-</code>) (unbound)</dt>
<dd> <p> Move up a line in the buffer, or if already at the top line, move to the previous event in the history list. Then move to the first non-blank character on the line. </p>
 </dd>
<dt><code>up-line-or-search</code></dt>
<dd> <p> Move up a line in the buffer, or if already at the top line, search backward in the history for a line beginning with the first word in the buffer. </p>
 </dd>
<dl>
<dd> <p> If called from a function by the <code>zle</code> command with arguments, the first argument is taken as the string for which to search, rather than the first word in the buffer. </p>
 </dd></dl>
<dt><code>up-history</code> (unbound) (<code>^P</code>) (unbound)</dt>
<dd> <p> Move to the previous event in the history list. </p>
 </dd>
<dt><code>history-beginning-search-forward</code></dt>
<dd> <p> Search forward in the history for a line beginning with the current line up to the cursor. This leaves the cursor in its original position. </p>
 </dd>
<dt><code>set-local-history</code></dt>
<dd> <p> By default, history movement commands visit the imported lines as well as the local lines. This widget lets you toggle this on and off, or set it with the numeric argument. Zero for both local and imported lines and nonzero for only local lines. </p>
 </dd></dl>
<h3>Modifying Text</h3>
<dl>
<dd> <p> <code>vi-add-eol</code> (unbound) (<code>A</code>) (unbound) Move to the end of the line and enter insert mode. </p>
 </dd>
<dt><code>vi-add-next</code> (unbound) (<code>a</code>) (unbound)</dt>
<dd> <p> Enter insert mode after the current cursor position, without changing lines. </p>
 </dd>
<dt><code>backward-delete-char</code> (<code>^H ^?</code>) (unbound) (unbound)</dt>
<dd> <p> Delete the character behind the cursor. </p>
 </dd>
<dt><code>vi-backward-delete-char</code> (unbound) (<code>X</code>) (<code>^H</code>)</dt>
<dd> <p> Delete the character behind the cursor, without changing lines. If in insert mode, this won&#8217;t delete past the point where insert mode was last entered. </p>
 </dd>
<dt><code>backward-delete-word</code></dt>
<dd> <p> Delete the word behind the cursor. </p>
 </dd>
<dt><code>backward-kill-line</code></dt>
<dd> <p> Kill from the beginning of the line to the cursor position. </p>
 </dd>
<dt><code>backward-kill-word</code> (<code>^W ESC-^H ESC-^?</code>) (unbound) (unbound)</dt>
<dd> <p> Kill the word behind the cursor. </p>
 </dd>
<dt><code>vi-backward-kill-word</code> (unbound) (unbound) (<code>^W</code>)</dt>
<dd> <p> Kill the word behind the cursor, without going past the point where insert mode was last entered. </p>
 </dd>
<dt><code>capitalize-word</code> (<code>ESC-C ESC-c</code>) (unbound) (unbound)</dt>
<dd> <p> Capitalize the current word and move past it. </p>
 </dd>
<dt><code>vi-change</code> (unbound) (<code>c</code>) (unbound)</dt>
<dd> <p> Read a movement command from the keyboard, and kill from the cursor position to the endpoint of the movement. Then enter insert mode. If the command is <code>vi-change</code>, change the current line. </p>
 </dd>
<dl>
<dd> <p> For compatibility with vi, if the command is <code>vi-forward-word</code> or <code>vi-forward-blank-word</code>, the whitespace after the word is not included. If you prefer the more consistent behaviour with the whitespace included use the following key binding: </p>
 </dd>
<dl>
<dd> <pre><code>
 bindkey -a -s cw dwi 
</code></pre>
 </dd></dl>
</dl>
<dt><code>vi-change-eol</code> (unbound) (<code>C</code>) (unbound)</dt>
<dd> <p> Kill to the end of the line and enter insert mode. </p>
 </dd>
<dt><code>vi-change-whole-line</code> (unbound) (<code>S</code>) (unbound)</dt>
<dd> <p> Kill the current line and enter insert mode. </p>
 </dd>
<dt><code>copy-region-as-kill</code> (<code>ESC-W ESC-w</code>) (unbound) (unbound)</dt>
<dd> <p> Copy the area from the cursor to the mark to the kill buffer. </p>
 </dd>
<dl>
<dd> <p> If called from a ZLE widget function in the form `<code>zle copy-region-as-kill</code> <i>string</i>&#8216; then <i>string</i> will be taken as the text to copy to the kill buffer. The cursor, the mark and the text on the command line are not used in this case. </p>
 </dd></dl>
<dt><code>copy-prev-word</code> (<code>ESC-^_</code>) (unbound) (unbound)</dt>
<dd> <p> Duplicate the word to the left of the cursor. </p>
 </dd>
<dt><code>copy-prev-shell-word</code></dt>
<dd> <p> Like <code>copy-prev-word</code>, but the word is found by using shell parsing, whereas <code>copy-prev-word</code> looks for blanks. This makes a difference when the word is quoted and contains spaces. </p>
 </dd>
<dt><code>vi-delete</code> (unbound) (<code>d</code>) (unbound)</dt>
<dd> <p> Read a movement command from the keyboard, and kill from the cursor position to the endpoint of the movement. If the command is <code>vi-delete</code>, kill the current line. </p>
 </dd>
<dt><code>delete-char</code></dt>
<dd> <p> Delete the character under the cursor. </p>
 </dd>
<dt><code>vi-delete-char</code> (unbound) (<code>x</code>) (unbound)</dt>
<dd> <p> Delete the character under the cursor, without going past the end of the line. </p>
 </dd>
<dt><code>delete-word</code></dt>
<dd> <p> Delete the current word. </p>
 </dd>
<dt><code>down-case-word</code> (<code>ESC-L ESC-l</code>) (unbound) (unbound)</dt>
<dd> <p> Convert the current word to all lowercase and move past it. </p>
 </dd>
<dt><code>vi-down-case</code> (unbound) (<code>gu</code>) (unbound)</dt>
<dd> <p> Read a movement command from the keyboard, and convert all characters from the cursor position to the endpoint of the movement to lowercase. If the movement command is <code>vi-down-case</code>, swap the case of all characters on the current line. </p>
 </dd>
<dt><code>kill-word</code> (<code>ESC-D ESC-d</code>) (unbound) (unbound)</dt>
<dd> <p> Kill the current word. </p>
 </dd>
<dt><code>gosmacs-transpose-chars</code></dt>
<dd> <p> Exchange the two characters behind the cursor. </p>
 </dd>
<dt><code>vi-indent</code> (unbound) (<code>&gt;</code>) (unbound)</dt>
<dd> <p> Indent a number of lines. </p>
 </dd>
<dt><code>vi-insert</code> (unbound) (<code>i</code>) (unbound)</dt>
<dd> <p> Enter insert mode. </p>
 </dd>
<dt><code>vi-insert-bol</code> (unbound) (<code>I</code>) (unbound)</dt>
<dd> <p> Move to the first non-blank character on the line and enter insert mode. </p>
 </dd>
<dt><code>vi-join</code> (<code>^X^J</code>) (<code>J</code>) (unbound)</dt>
<dd> <p> Join the current line with the next one. </p>
 </dd>
<dt><code>kill-line</code> (<code>^K</code>) (unbound) (unbound)</dt>
<dd> <p> Kill from the cursor to the end of the line. If already on the end of the line, kill the newline character. </p>
 </dd>
<dt><code>vi-kill-line</code> (unbound) (unbound) (<code>^U</code>)</dt>
<dd> <p> Kill from the cursor back to wherever insert mode was last entered. </p>
 </dd>
<dt><code>vi-kill-eol</code> (unbound) (<code>D</code>) (unbound)</dt>
<dd> <p> Kill from the cursor to the end of the line. </p>
 </dd>
<dt><code>kill-region</code></dt>
<dd> <p> Kill from the cursor to the mark. </p>
 </dd>
<dt><code>kill-buffer</code> (<code>^X^K</code>) (unbound) (unbound)</dt>
<dd> <p> Kill the entire buffer. </p>
 </dd>
<dt><code>kill-whole-line</code> (<code>^U</code>) (unbound) (unbound)</dt>
<dd> <p> Kill the current line. </p>
 </dd>
<dt><code>vi-match-bracket</code> (<code>^X^B</code>) (<code>%</code>) (unbound)</dt>
<dd> <p> Move to the bracket character (one of <code>{}</code>, <code>()</code> or <code>[]</code>) that matches the one under the cursor. If the cursor is not on a bracket character, move forward without going past the end of the line to find one, and then go to the matching bracket. </p>
 </dd>
<dt><code>vi-open-line-above</code> (unbound) (<code>O</code>) (unbound)</dt>
<dd> <p> Open a line above the cursor and enter insert mode. </p>
 </dd>
<dt><code>vi-open-line-below</code> (unbound) (<code>o</code>) (unbound)</dt>
<dd> <p> Open a line below the cursor and enter insert mode. </p>
 </dd>
<dt><code>vi-oper-swap-case</code> (unbound) (<code>g~</code>) (unbound)</dt>
<dd> <p> Read a movement command from the keyboard, and swap the case of all characters from the cursor position to the endpoint of the movement. If the movement command is <code>vi-oper-swap-case</code>, swap the case of all characters on the current line. </p>
 </dd>
<dt><code>overwrite-mode</code> (<code>^X^O</code>) (unbound) (unbound)</dt>
<dd> <p> Toggle between overwrite mode and insert mode. </p>
 </dd>
<dt><code>vi-put-before</code> (unbound) (<code>P</code>) (unbound)</dt>
<dd> <p> Insert the contents of the kill buffer before the cursor. If the kill buffer contains a sequence of lines (as opposed to characters), paste it above the current line. </p>
 </dd>
<dt><code>vi-put-after</code> (unbound) (<code>p</code>) (unbound)</dt>
<dd> <p> Insert the contents of the kill buffer after the cursor. If the kill buffer contains a sequence of lines (as opposed to characters), paste it below the current line. </p>
 </dd>
<dt><code>put-replace-selection</code> (unbound) (unbound) (unbound)</dt>
<dd> <p> Replace the contents of the current region or selection with the contents of the kill buffer. If the kill buffer contains a sequence of lines (as opposed to characters), the current line will be split by the pasted lines. </p>
 </dd>
<dt><code>quoted-insert</code> (<code>^V</code>) (unbound) (unbound)</dt>
<dd> <p> Insert the next character typed into the buffer literally. An interrupt character will not be inserted. </p>
 </dd>
<dt><code>vi-quoted-insert</code> (unbound) (unbound) (<code>^Q ^V</code>)</dt>
<dd> <p> Display a `<code>^</code>&#8216; at the cursor position, and insert the next character typed into the buffer literally. An interrupt character will not be inserted. </p>
 </dd>
<dt><code>quote-line</code> (<code>ESC-&#8216;</code>) (unbound) (unbound)</dt>
<dd> <p> Quote the current line; that is, put a `<code>&#8216;</code>&#8216; character at the beginning and the end, and convert all `<code>&#8216;</code>&#8216; characters to `<code>&#8216;\&#8216;&#8216;</code>&#8216;. </p>
 </dd>
<dt><code>quote-region</code> (<code>ESC-&quot;</code>) (unbound) (unbound)</dt>
<dd> <p> Quote the region from the cursor to the mark. </p>
 </dd>
<dt><code>vi-replace</code> (unbound) (<code>R</code>) (unbound)</dt>
<dd> <p> Enter overwrite mode. </p>
 </dd>
<dt><code>vi-repeat-change</code> (unbound) (<code>.</code>) (unbound)</dt>
<dd> <p> Repeat the last vi mode text modification. If a count was used with the modification, it is remembered. If a count is given to this command, it overrides the remembered count, and is remembered for future uses of this command. The cut buffer specification is similarly remembered. </p>
 </dd>
<dt><code>vi-replace-chars</code> (unbound) (<code>r</code>) (unbound)</dt>
<dd> <p> Replace the character under the cursor with a character read from the keyboard. </p>
 </dd>
<dt><code>self-insert</code> (printable characters) (unbound) (printable characters and some control characters)</dt>
<dd> <p> Insert a character into the buffer at the cursor position. </p>
 </dd>
<dt><code>self-insert-unmeta</code> (<code>ESC-^I ESC-^J ESC-^M</code>) (unbound) (unbound)</dt>
<dd> <p> Insert a character into the buffer after stripping the meta bit and converting ^M to ^J. </p>
 </dd>
<dt><code>vi-substitute</code> (unbound) (<code>s</code>) (unbound)</dt>
<dd> <p> Substitute the next character(s). </p>
 </dd>
<dt><code>vi-swap-case</code> (unbound) (<code>~</code>) (unbound)</dt>
<dd> <p> Swap the case of the character under the cursor and move past it. </p>
 </dd>
<dt><code>transpose-chars</code> (<code>^T</code>) (unbound) (unbound)</dt>
<dd> <p> Exchange the two characters to the left of the cursor if at end of line, else exchange the character under the cursor with the character to the left. </p>
 </dd>
<dt><code>transpose-words</code> (<code>ESC-T ESC-t</code>) (unbound) (unbound)</dt>
<dd> <p> Exchange the current word with the one before it. </p>
 </dd>
<dl>
<dd> <p> With a positive numeric argument <i>N</i>, the word around the cursor, or following it if the cursor is between words, is transposed with the preceding <i>N</i> words. The cursor is put at the end of the resulting group of words. </p>
<p> With a negative numeric argument <i>-N</i>, the effect is the same as using a positive argument <i>N</i> except that the original cursor position is retained, regardless of how the words are rearranged. </p>
 </dd></dl>
<dt><code>vi-unindent</code> (unbound) (<code>&lt;</code>) (unbound)</dt>
<dd> <p> Unindent a number of lines. </p>
 </dd>
<dt><code>vi-up-case</code> (unbound) (<code>gU</code>) (unbound)</dt>
<dd> <p> Read a movement command from the keyboard, and convert all characters from the cursor position to the endpoint of the movement to lowercase. If the movement command is <code>vi-up-case</code>, swap the case of all characters on the current line. </p>
 </dd>
<dt><code>up-case-word</code> (<code>ESC-U ESC-u</code>) (unbound) (unbound)</dt>
<dd> <p> Convert the current word to all caps and move past it. </p>
 </dd>
<dt><code>yank</code> (<code>^Y</code>) (unbound) (unbound)</dt>
<dd> <p> Insert the contents of the kill buffer at the cursor position. </p>
 </dd>
<dt><code>yank-pop</code> (<code>ESC-y</code>) (unbound) (unbound)</dt>
<dd> <p> Remove the text just yanked, rotate the kill-ring (the history of previously killed text) and yank the new top. Only works following <code>yank</code>, <code>vi-put-before</code>, <code>vi-put-after</code> or <code>yank-pop</code>. </p>
 </dd>
<dt><code>vi-yank</code> (unbound) (<code>y</code>) (unbound)</dt>
<dd> <p> Read a movement command from the keyboard, and copy the region from the cursor position to the endpoint of the movement into the kill buffer. If the command is <code>vi-yank</code>, copy the current line. </p>
 </dd>
<dt><code>vi-yank-whole-line</code> (unbound) (<code>Y</code>) (unbound)</dt>
<dd> <p> Copy the current line into the kill buffer. </p>
 </dd>
<dt><code>vi-yank-eol</code></dt>
<dd> <p> Copy the region from the cursor position to the end of the line into the kill buffer. Arguably, this is what Y should do in vi, but it isn&#8217;t what it actually does. </p>
 </dd></dl>
<h3>Arguments</h3>
<dl>
<dd> <p> <code>digit-argument</code> (<code>ESC-0</code>..<code>ESC-9</code>) (<code>1</code>-<code>9</code>) (unbound) Start a new numeric argument, or add to the current one. See also <code>vi-digit-or-beginning-of-line</code>. This only works if bound to a key sequence ending in a decimal digit. </p>
 </dd>
<dl>
<dd> <p> Inside a widget function, a call to this function treats the last key of the key sequence which called the widget as the digit. </p>
 </dd></dl>
<dt><code>neg-argument</code> (<code>ESC-</code><code>-</code>) (unbound) (unbound)</dt>
<dd> <p> Changes the sign of the following argument. </p>
 </dd>
<dt><code>universal-argument</code></dt>
<dd> <p> Multiply the argument of the next command by 4. Alternatively, if this command is followed by an integer (positive or negative), use that as the argument for the next command. Thus digits cannot be repeated using this command. For example, if this command occurs twice, followed immediately by <code>forward-char</code>, move forward sixteen spaces; if instead it is followed by <code>-2</code>, then <code>forward-char</code>, move backward two spaces. </p>
 </dd>
<dl>
<dd> <p> Inside a widget function, if passed an argument, i.e. `<code>zle universal-argument</code> <i>num</i>&#8216;, the numeric argument will be set to <i>num</i>; this is equivalent to `<code>NUMERIC=</code><i>num</i>&#8216;. </p>
 </dd></dl>
<dt><code>argument-base</code></dt>
<dd> <p> Use the existing numeric argument as a numeric base, which must be in the range 2 to 36 inclusive. Subsequent use of <code>digit-argument</code> and <code>universal-argument</code> will input a new numeric argument in the given base. The usual hexadecimal convention is used: the letter <code>a</code> or <code>A</code> corresponds to 10, and so on. Arguments in bases requiring digits from 10 upwards are more conveniently input with <code>universal-argument</code>, since <code>ESC-a</code> etc. are not usually bound to <code>digit-argument</code>. </p>
 </dd>
<dl>
<dd> <p> The function can be used with a command argument inside a user-defined widget. The following code sets the base to 16 and lets the user input a hexadecimal argument until a key out of the digit range is typed: </p>
 </dd>
<dl>
<dd> <pre><code>
 zle argument-base 16
zle universal-argument 
</code></pre>
 </dd></dl>
</dl>
</dl>
<h3>Completion</h3>
<dl>
<dd> <p> <code>accept-and-menu-complete</code> In a menu completion, insert the current completion into the buffer, and advance to the next possible completion. </p>
 </dd>
<dt><code>complete-word</code></dt>
<dd> <p> Attempt completion on the current word. </p>
 </dd>
<dt><code>delete-char-or-list</code> (<code>^D</code>) (unbound) (unbound)</dt>
<dd> <p> Delete the character under the cursor. If the cursor is at the end of the line, list possible completions for the current word. </p>
 </dd>
<dt><code>expand-cmd-path</code></dt>
<dd> <p> Expand the current command to its full pathname. </p>
 </dd>
<dt><code>expand-or-complete</code> (<code>TAB</code>) (unbound) (<code>TAB</code>)</dt>
<dd> <p> Attempt shell expansion on the current word. If that fails, attempt completion. </p>
 </dd>
<dt><code>expand-or-complete-prefix</code></dt>
<dd> <p> Attempt shell expansion on the current word up to cursor. </p>
 </dd>
<dt><code>expand-history</code> (<code>ESC-space ESC-!</code>) (unbound) (unbound)</dt>
<dd> <p> Perform history expansion on the edit buffer. </p>
 </dd>
<dt><code>expand-word</code> (<code>^X*</code>) (unbound) (unbound)</dt>
<dd> <p> Attempt shell expansion on the current word. </p>
 </dd>
<dt><code>list-choices</code> (<code>ESC-^D</code>) (<code>^D =</code>) (<code>^D</code>)</dt>
<dd> <p> List possible completions for the current word. </p>
 </dd>
<dt><code>list-expand</code> (<code>^Xg ^XG</code>) (<code>^G</code>) (<code>^G</code>)</dt>
<dd> <p> List the expansion of the current word. </p>
 </dd>
<dt><code>magic-space</code></dt>
<dd> <p> Perform history expansion and insert a space into the buffer. This is intended to be bound to space. </p>
 </dd>
<dt><code>menu-complete</code></dt>
<dd> <p> Like <code>complete-word</code>, except that menu completion is used. See the <code>MENU_COMPLETE</code> option. </p>
 </dd>
<dt><code>menu-expand-or-complete</code></dt>
<dd> <p> Like <code>expand-or-complete</code>, except that menu completion is used. </p>
 </dd>
<dt><code>reverse-menu-complete</code></dt>
<dd> <p> Perform menu completion, like <code>menu-complete</code>, except that if a menu completion is already in progress, move to the <i>previous</i> completion rather than the next. </p>
 </dd>
<dt><code>end-of-list</code></dt>
<dd> <p> When a previous completion displayed a list below the prompt, this widget can be used to move the prompt below the list. </p>
 </dd></dl>
<h3>Miscellaneous</h3>
<dl>
<dd> <p> <code>accept-and-hold</code> (<code>ESC-A ESC-a</code>) (unbound) (unbound) Push the contents of the buffer on the buffer stack and execute it. </p>
 </dd>
<dt><code>accept-and-infer-next-history</code></dt>
<dd> <p> Execute the contents of the buffer. Then search the history list for a line matching the current one and push the event following onto the buffer stack. </p>
 </dd>
<dt><code>accept-line</code> (<code>^J ^M</code>) (<code>^J ^M</code>) (<code>^J ^M</code>)</dt>
<dd> <p> Finish editing the buffer. Normally this causes the buffer to be executed as a shell command. </p>
 </dd>
<dt><code>accept-line-and-down-history</code> (<code>^O</code>) (unbound) (unbound)</dt>
<dd> <p> Execute the current line, and push the next history event on the buffer stack. </p>
 </dd>
<dt><code>auto-suffix-remove</code></dt>
<dd> <p> If the previous action added a suffix (space, slash, etc.) to the word on the command line, remove it. Otherwise do nothing. Removing the suffix ends any active menu completion or menu selection. </p>
 </dd>
<dl>
<dd> <p> This widget is intended to be called from user-defined widgets to enforce a desired suffix-removal behavior. </p>
 </dd></dl>
<dt><code>auto-suffix-retain</code></dt>
<dd> <p> If the previous action added a suffix (space, slash, etc.) to the word on the command line, force it to be preserved. Otherwise do nothing. Retaining the suffix ends any active menu completion or menu selection. </p>
 </dd>
<dl>
<dd> <p> This widget is intended to be called from user-defined widgets to enforce a desired suffix-preservation behavior. </p>
 </dd></dl>
<dt><code>beep</code></dt>
<dd> <p> Beep, unless the <code>BEEP</code> option is unset. </p>
 </dd>
<dt><code>bracketed-paste</code></dt>
<dd> <p> This widget is invoked when text is pasted to the terminal emulator. It is not intended to be bound to actual keys but instead to the special sequence generated by the terminal emulator when text is pasted. </p>
 </dd>
<dl>
<dd> <p> When invoked interactively, the pasted text is inserted to the buffer and placed in the cutbuffer. If a numeric argument is given, shell quoting will be applied to the pasted text before it is inserted. </p>
<p> When a named buffer is specified with <code>vi-set-buffer</code> (<code>&quot;x</code>), the pasted text is stored in that named buffer but not inserted. </p>
<p> When called from a widget function as `<code>bracketed-paste</code> <i>name</i>`, the pasted text is assigned to the variable <i>name</i> and no other processing is done. </p>
<p> See also the <code>zle_bracketed_paste</code> parameter. </p>
 </dd></dl>
<dt><code>vi-cmd-mode</code> (<code>^X^V</code>) (unbound) (<code>^[</code>)</dt>
<dd> <p> Enter command mode; that is, select the `<code>vicmd</code>&#8216; keymap. Yes, this is bound by default in emacs mode. </p>
 </dd>
<dt><code>vi-caps-lock-panic</code></dt>
<dd> <p> Hang until any lowercase key is pressed. This is for vi users without the mental capacity to keep track of their caps lock key (like the author). </p>
 </dd>
<dt><code>clear-screen</code> (<code>^L ESC-^L</code>) (<code>^L</code>) (<code>^L</code>)</dt>
<dd> <p> Clear the screen and redraw the prompt. </p>
 </dd>
<dt><code>deactivate-region</code></dt>
<dd> <p> Make the current region inactive. This disables vim-style visual selection mode if it is active. </p>
 </dd>
<dt><code>describe-key-briefly</code></dt>
<dd> <p> Reads a key sequence, then prints the function bound to that sequence. </p>
 </dd>
<dt><code>exchange-point-and-mark</code> (<code>^X^X</code>) (unbound) (unbound)</dt>
<dd> <p> Exchange the cursor position (point) with the position of the mark. Unless a negative numeric argument is given, the region between point and mark is activated so that it can be highlighted. If a zero numeric argument is given, the region is activated but point and mark are not swapped. </p>
 </dd>
<dt><code>execute-named-cmd</code> (<code>ESC-x</code>) (<code>:</code>) (unbound)</dt>
<dd> <p> Read the name of an editor command and execute it. Aliasing this widget with `<code>zle -A</code>&#8216; or replacing it with `<code>zle -N</code>&#8216; has no effect when interpreting key bindings, but `<code>zle execute-named-cmd</code>&#8216; will invoke such an alias or replacement. </p>
 </dd>
<dl>
<dd> <p> A restricted set of editing functions is available in the mini-buffer. Keys are looked up in the special <code>command</code> keymap, and if not found there in the main keymap. An interrupt signal, as defined by the stty setting, will abort the function. Note that the following always perform the same task within the <code>executed-named-cmd</code> environment and cannot be replaced by user defined widgets, nor can the set of functions be extended. The allowed functions are: <code>backward-delete-char</code>, <code>vi-backward-delete-char</code>, <code>clear-screen</code>, <code>redisplay</code>, <code>quoted-insert</code>, <code>vi-quoted-insert</code>, <code>backward-kill-word</code>, <code>vi-backward-kill-word</code>, <code>kill-whole-line</code>, <code>vi-kill-line</code>, <code>backward-kill-line</code>, <code>list-choices</code>, <code>delete-char-or-list</code>, <code>complete-word</code>, <code>accept-line</code>, <code>expand-or-complete</code> and <code>expand-or-complete-prefix</code>. </p>
<p> <code>kill-region</code> kills the last word, and vi-cmd-mode is treated the same as accept-line. The space and tab characters, if not bound to one of these functions, will complete the name and then list the possibilities if the <code>AUTO_LIST</code> option is set. Any other character that is not bound to <code>self-insert</code> or <code>self-insert-unmeta</code> will beep and be ignored. The bindings of the current insert mode will be used. </p>
<p> Currently this command may not be redefined or called by name. </p>
 </dd></dl>
<dt><code>execute-last-named-cmd</code> (<code>ESC-z</code>) (unbound) (unbound)</dt>
<dd> <p> Redo the last function executed with <code>execute-named-cmd</code>. </p>
 </dd>
<dl>
<dd> <p> Like <code>execute-named-cmd</code>, this command may not be redefined, but it may be called by name. </p>
 </dd></dl>
<dt><code>get-line</code> (<code>ESC-G ESC-g</code>) (unbound) (unbound)</dt>
<dd> <p> Pop the top line off the buffer stack and insert it at the cursor position. </p>
 </dd>
<dt><code>pound-insert</code> (unbound) (<code>#</code>) (unbound)</dt>
<dd> <p> If there is no # character at the beginning of the buffer, add one to the beginning of each line. If there is one, remove a # from each line that has one. In either case, accept the current line. The <code>INTERACTIVE_COMMENTS</code> option must be set for this to have any usefulness. </p>
 </dd>
<dt><code>vi-pound-insert</code></dt>
<dd> <p> If there is no # character at the beginning of the current line, add one. If there is one, remove it. The <code>INTERACTIVE_COMMENTS</code> option must be set for this to have any usefulness. </p>
 </dd>
<dt><code>push-input</code></dt>
<dd> <p> Push the entire current multiline construct onto the buffer stack and return to the top-level (<code>PS1</code>) prompt. If the current parser construct is only a single line, this is exactly like <code>push-line</code>. Next time the editor starts up or is popped with <code>get-line</code>, the construct will be popped off the top of the buffer stack and loaded into the editing buffer. </p>
 </dd>
<dt><code>push-line</code> (<code>^Q ESC-Q ESC-q</code>) (unbound) (unbound)</dt>
<dd> <p> Push the current buffer onto the buffer stack and clear the buffer. Next time the editor starts up, the buffer will be popped off the top of the buffer stack and loaded into the editing buffer. </p>
 </dd>
<dt><code>push-line-or-edit</code></dt>
<dd> <p> At the top-level (<code>PS1</code>) prompt, equivalent to <code>push-line</code>. At a secondary (<code>PS2</code>) prompt, move the entire current multiline construct into the editor buffer. The latter is equivalent to <code>push-input</code> followed by <code>get-line</code>. </p>
 </dd>
<dt><code>read-command</code></dt>
<dd> <p> Only useful from a user-defined widget. A keystroke is read just as in normal operation, but instead of the command being executed the name of the command that would be executed is stored in the shell parameter <code>REPLY</code>. This can be used as the argument of a future <code>zle</code> command. If the key sequence is not bound, status 1 is returned; typically, however, <code>REPLY</code> is set to <code>undefined-key</code> to indicate a useless key sequence. </p>
 </dd>
<dt><code>recursive-edit</code></dt>
<dd> <p> Only useful from a user-defined widget. At this point in the function, the editor regains control until one of the standard widgets which would normally cause zle to exit (typically an <code>accept-line</code> caused by hitting the return key) is executed. Instead, control returns to the user-defined widget. The status returned is non-zero if the return was caused by an error, but the function still continues executing and hence may tidy up. This makes it safe for the user-defined widget to alter the command line or key bindings temporarily. </p>
 </dd>
<dl>
<dd> <p> The following widget, <code>caps-lock</code>, serves as an example. </p>
 </dd>
<dl>
<dd> <pre><code>
 self-insert-ucase() {
  LBUFFER+=${(U)KEYS[-1]}
}
integer stat
zle -N self-insert self-insert-ucase
zle -A caps-lock save-caps-lock
zle -A accept-line caps-lock
zle recursive-edit
stat=$?
zle -A .self-insert self-insert
zle -A save-caps-lock caps-lock
zle -D save-caps-lock
(( stat )) &amp;&amp; zle send-break
return $stat 
</code></pre>
 </dd></dl>
<p> This causes typed letters to be inserted capitalised until either <code>accept-line</code> (i.e. typically the return key) is typed or the <code>caps-lock</code> widget is invoked again; the later is handled by saving the old definition of <code>caps-lock</code> as <code>save-caps-lock</code> and then rebinding it to invoke <code>accept-line</code>. Note that an error from the recursive edit is detected as a non-zero return status and propagated by using the <code>send-break</code> widget. </dl>
 </p>
<dt><code>redisplay</code> (unbound) (<code>^R</code>) (<code>^R</code>)</dt>
<dd> <p> Redisplays the edit buffer. </p>
 </dd>
<dt><code>reset-prompt</code> (unbound) (unbound) (unbound)</dt>
<dd> <p> Force the prompts on both the left and right of the screen to be re-expanded, then redisplay the edit buffer. This reflects changes both to the prompt variables themselves and changes in the expansion of the values (for example, changes in time or directory, or changes to the value of variables referred to by the prompt). </p>
 </dd>
<dl>
<dd> <p> Otherwise, the prompt is only expanded each time zle starts, and when the display has been interrupted by output from another part of the shell (such as a job notification) which causes the command line to be reprinted. </p>
<p> <code>reset-prompt</code> doesn&#8217;t alter the special parameter <code>LASTWIDGET</code>. </p>
 </dd></dl>
<dt><code>send-break</code> (<code>^G ESC-^G</code>) (unbound) (unbound)</dt>
<dd> <p> Abort the current editor function, e.g. <code>execute-named-command</code>, or the editor itself, e.g. if you are in <code>vared</code>. Otherwise abort the parsing of the current line; in this case the aborted line is available in the shell variable <code>ZLE_LINE_ABORTED</code>. If the editor is aborted from within <code>vared</code>, the variable <code>ZLE_VARED_ABORTED</code> is set. </p>
 </dd>
<dt><code>run-help</code> (<code>ESC-H ESC-h</code>) (unbound) (unbound)</dt>
<dd> <p> Push the buffer onto the buffer stack, and execute the command `<code>run-help</code> <i>cmd</i>&#8216;, where <i>cmd</i> is the current command. <code>run-help</code> is normally aliased to <code>man</code>. </p>
 </dd>
<dt><code>vi-set-buffer</code> (unbound) (<code>&quot;</code>) (unbound)</dt>
<dd> <p> Specify a buffer to be used in the following command. There are 37 buffers that can be specified: the 26 `named&#8217; buffers <code>&quot;a</code> to <code>&quot;z</code>, the `yank&#8217; buffer <code>&quot;0</code>, the nine `queued&#8217; buffers <code>&quot;1</code> to <code>&quot;9</code> and the `black hole&#8217; buffer <code>&quot;_</code>. The named buffers can also be specified as <code>&quot;A</code> to <code>&quot;Z</code>. </p>
 </dd>
<dl>
<dd> <p> When a buffer is specified for a cut, change or yank command, the text concerned replaces the previous contents of the specified buffer. If a named buffer is specified using a capital, the newly cut text is appended to the buffer instead of overwriting it. When using the <code>&quot;_</code> buffer, nothing happens. This can be useful for deleting text without affecting any buffers. </p>
<p> If no buffer is specified for a cut or change command, <code>&quot;1</code> is used, and the contents of <code>&quot;1</code> to <code>&quot;8</code> are each shifted along one buffer; the contents of <code>&quot;9</code> is lost. If no buffer is specified for a yank command, <code>&quot;0</code> is used. Finally, a paste command without a specified buffer will paste the text from the most recent command regardless of any buffer that might have been used with that command. </p>
<p> When called from a widget function by the <code>zle</code> command, the buffer can optionally be specified with an argument. For example, </p>
 </dd>
<dl>
<dd> <pre><code>
 zle vi-set-buffer A 
</code></pre>
 </dd></dl>
</dl>
<dt><code>vi-set-mark</code> (unbound) (<code>m</code>) (unbound)</dt>
<dd> <p> Set the specified mark at the cursor position. </p>
 </dd>
<dt><code>set-mark-command</code> (<code>^@</code>) (unbound) (unbound)</dt>
<dd> <p> Set the mark at the cursor position. If called with a negative numeric argument, do not set the mark but deactivate the region so that it is no longer highlighted (it is still usable for other purposes). Otherwise the region is marked as active. </p>
 </dd>
<dt><code>spell-word</code> (<code>ESC-$ ESC-S ESC-s</code>) (unbound) (unbound)</dt>
<dd> <p> Attempt spelling correction on the current word. </p>
 </dd>
<dt><code>split-undo</code></dt>
<dd> <p> Breaks the undo sequence at the current change. This is useful in vi mode as changes made in insert mode are coalesced on entering command mode. Similarly, <code>undo</code> will normally revert as one all the changes made by a user-defined widget. </p>
 </dd>
<dt><code>undefined-key</code></dt>
<dd> <p> This command is executed when a key sequence that is not bound to any command is typed. By default it beeps. </p>
 </dd>
<dt><code>undo</code> (<code>^_ ^Xu ^X^U</code>) (<code>u</code>) (unbound)</dt>
<dd> <p> Incrementally undo the last text modification. When called from a user-defined widget, takes an optional argument indicating a previous state of the undo history as returned by the <code>UNDO_CHANGE_NO</code> variable; modifications are undone until that state is reached, subject to any limit imposed by the <code>UNDO_LIMIT_NO</code> variable. </p>
 </dd>
<dl>
<dd> <p> Note that when invoked from vi command mode, the full prior change made in insert mode is reverted, the changes having been merged when command mode was selected. </p>
 </dd></dl>
<dt><code>redo</code> (unbound) (<code>^R</code>) (unbound)</dt>
<dd> <p> Incrementally redo undone text modifications. </p>
 </dd>
<dt><code>vi-undo-change</code> (unbound) (unbound) (unbound)</dt>
<dd> <p> Undo the last text modification. If repeated, redo the modification. </p>
 </dd>
<dt><code>visual-mode</code> (unbound) (<code>v</code>) (unbound)</dt>
<dd> <p> Toggle vim-style visual selection mode. If line-wise visual mode is currently enabled then it is changed to being character-wise. If used following an operator, it forces the subsequent movement command to be treated as a character-wise movement. </p>
 </dd>
<dt><code>visual-line-mode</code> (unbound) (<code>V</code>) (unbound)</dt>
<dd> <p> Toggle vim-style line-wise visual selection mode. If character-wise visual mode is currently enabled then it is changed to being line-wise. If used following an operator, it forces the subsequent movement command to be treated as a line-wise movement. </p>
 </dd>
<dt><code>what-cursor-position</code> (<code>^X=</code>) (<code>ga</code>) (unbound)</dt>
<dd> <p> Print the character under the cursor, its code as an octal, decimal and hexadecimal number, the current cursor position within the buffer and the column of the cursor in the current line. </p>
 </dd>
<dt><code>where-is</code></dt>
<dd> <p> Read the name of an editor command and print the listing of key sequences that invoke the specified command. A restricted set of editing functions is available in the mini-buffer. Keys are looked up in the special <code>command</code> keymap, and if not found there in the main keymap. </p>
 </dd>
<dt><code>which-command</code> (<code>ESC-?</code>) (unbound) (unbound)</dt>
<dd> <p> Push the buffer onto the buffer stack, and execute the command `<code>which-command</code> <i>cmd</i>&#8216;. where <i>cmd</i> is the current command. <code>which-command</code> is normally aliased to <code>whence</code>. </p>
 </dd>
<dt><code>vi-digit-or-beginning-of-line</code> (unbound) (<code>0</code>) (unbound)</dt>
<dd> <p> If the last command executed was a digit as part of an argument, continue the argument. Otherwise, execute vi-beginning-of-line. </p>
 </dd></dl>
<h3>Text Objects</h3>
<p> Text objects are commands that can be used to select a block of text according to some criteria. They are a feature of the vim text editor and so are primarily intended for use with vi operators or from visual selection mode. However, they can also be used from vi-insert or emacs mode. Key bindings listed below apply to the <code>viopp</code> and <code>visual</code> keymaps. </p>
<dl>
<dd> <p> <code>select-a-blank-word</code> (<code>aW</code>) Select a word including adjacent blanks, where a word is defined as a series of non-blank characters. With a numeric argument, multiple words will be selected. </p>
 </dd>
<dt><code>select-a-shell-word</code> (<code>aa</code>)</dt>
<dd> <p> Select the current command argument applying the normal rules for quoting. </p>
 </dd>
<dt><code>select-a-word</code> (<code>aw</code>)</dt>
<dd> <p> Select a word including adjacent blanks, using the normal vi-style word definition. With a numeric argument, multiple words will be selected. </p>
 </dd>
<dt><code>select-in-blank-word</code> (<code>iW</code>)</dt>
<dd> <p> Select a word, where a word is defined as a series of non-blank characters. With a numeric argument, multiple words will be selected. </p>
 </dd>
<dt><code>select-in-shell-word</code> (<code>ia</code>)</dt>
<dd> <p> Select the current command argument applying the normal rules for quoting. If the argument begins and ends with matching quote characters, these are not included in the selection. </p>
 </dd>
<dt><code>select-in-word</code> (<code>iw</code>)</dt>
<dd> <p> Select a word, using the normal vi-style word definition. With a numeric argument, multiple words will be selected. </p>
 </dd></dl>
<h2>CHARACTER HIGHLIGHTING</h2>
<p> The line editor has the ability to highlight characters or regions of the line that have a particular significance. This is controlled by the array parameter <code>zle_highlight</code>, if it has been set by the user. </p>
<p> If the parameter contains the single entry <code>none</code> all highlighting is turned off. Note the parameter is still expected to be an array. </p>
<p> Otherwise each entry of the array should consist of a word indicating a context for highlighting, then a colon, then a comma-separated list of the types of highlighting to apply in that context. </p>
<p> The contexts available for highlighting are the following: </p>
<dl>
<dd> <p> <code>default</code> Any text within the command line not affected by any other highlighting. Text outside the editable area of the command line is not affected. </p>
 </dd>
<dt><code>isearch</code></dt>
<dd> <p> When one of the incremental history search widgets is active, the area of the command line matched by the search string or pattern. </p>
 </dd>
<dt><code>region</code></dt>
<dd> <p> The currently selected text. In emacs terminology, this is referred to as the region and is bounded by the cursor (point) and the mark. The region is only highlighted if it is active, which is the case after the mark is modified with <code>set-mark-command</code> or <code>exchange-point-and-mark</code>. Note that whether or not the region is active has no effect on its use within emacs style widgets, it simply determines whether it is highlighted. In vi mode, the region corresponds to selected text in visual mode. </p>
 </dd>
<dt><code>special</code></dt>
<dd> <p> Individual characters that have no direct printable representation but are shown in a special manner by the line editor. These characters are described below. </p>
 </dd>
<dt><code>suffix</code></dt>
<dd> <p> This context is used in completion for characters that are marked as suffixes that will be removed if the completion ends at that point, the most obvious example being a slash (<code>/</code>) after a directory name. Note that suffix removal is configurable; the circumstances under which the suffix will be removed may differ for different completions. </p>
 </dd>
<dt><code>paste</code></dt>
<dd> <p> Following a command to paste text, the characters that were inserted. </p>
 </dd></dl>
<p> When <code>region_highlight</code> is set, the contexts that describe a region -- <code>isearch</code>, <code>region</code>, <code>suffix</code>, and <code>paste</code> -- are applied first, then <code>region_highlight</code> is applied, then the remaining <code>zle_highlight</code> contexts are applied. If a particular character is affected by multiple specifications, the last specification wins. </p>
<p> <code>zle_highlight</code> may contain additional fields for controlling how terminal sequences to change colours are output. Each of the following is followed by a colon and a string in the same form as for key bindings. This will not be necessary for the vast majority of terminals as the defaults shown in parentheses are widely used. </p>
<dl>
<dd> <p> <code>fg_start_code</code> (<code>\e[3</code>) The start of the escape sequence for the foreground colour. This is followed by one to three ASCII digits representing the colour. Only used for palette colors, i.e. not 24-bit colors specified via a color triplet. </p>
 </dd>
<dt><code>fg_default_code</code> (<code>9</code>)</dt>
<dd> <p> The number to use instead of the colour to reset the default foreground colour. </p>
 </dd>
<dt><code>fg_end_code</code> (<code>m</code>)</dt>
<dd> <p> The end of the escape sequence for the foreground colour. </p>
 </dd>
<dt><code>bg_start_code</code> (<code>\e[4</code>)</dt>
<dd> <p> The start of the escape sequence for the background colour. See <code>fg_start_code</code> above. </p>
 </dd>
<dt><code>bg_default_code</code> (<code>9</code>)</dt>
<dd> <p> The number to use instead of the colour to reset the default background colour. </p>
 </dd>
<dt><code>bg_end_code</code> (<code>m</code>)</dt>
<dd> <p> The end of the escape sequence for the background colour. </p>
 </dd></dl>
<p> The available types of highlighting are the following. Note that not all types of highlighting are available on all terminals: </p>
<dl>
<dd> <p> <code>none</code> No highlighting is applied to the given context. It is not useful for this to appear with other types of highlighting; it is used to override a default. </p>
 </dd>
<dt><code>fg=</code><i>colour</i></dt>
<dd> <p> The foreground colour should be set to <i>colour</i>, a decimal integer, the name of one of the eight most widely-supported colours or as a `<code>#</code>&#8216; followed by an RGB triplet in hexadecimal format. </p>
 </dd>
<dl>
<dd> <p> Not all terminals support this and, of those that do, not all provide facilities to test the support, hence the user should decide based on the terminal type. Most terminals support the colours <code>black</code>, <code>red</code>, <code>green</code>, <code>yellow</code>, <code>blue</code>, <code>magenta</code>, <code>cyan</code> and <code>white</code>, which can be set by name. In addition. <code>default</code> may be used to set the terminal&#8217;s default foreground colour. Abbreviations are allowed; <code>b</code> or <code>bl</code> selects black. Some terminals may generate additional colours if the <code>bold</code> attribute is also present. </p>
<p> On recent terminals and on systems with an up-to-date terminal database the number of colours supported may be tested by the command `<code>echotc Co</code>&#8216;; if this succeeds, it indicates a limit on the number of colours which will be enforced by the line editor. The number of colours is in any case limited to 256 (i.e. the range 0 to 255). </p>
<p> Some modern terminal emulators have support for 24-bit true colour (16 million colours). In this case, the hex triplet format can be used. This consists of a `<code>#</code>&#8216; followed by either a three or six digit hexadecimal number describing the red, green and blue components of the colour. Hex triplets can also be used with 88 and 256 colour terminals via the <code>zsh/nearcolor</code> module (see <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1)). </p>
<p> Colour is also known as color. </p>
 </dd></dl>
<dt><code>bg=</code><i>colour</i></dt>
<dd> <p> The background colour should be set to <i>colour</i>. This works similarly to the foreground colour, except the background is not usually affected by the bold attribute. </p>
 </dd>
<dt><code>bold</code></dt>
<dd> <p> The characters in the given context are shown in a bold font. Not all terminals distinguish bold fonts. </p>
 </dd>
<dt><code>standout</code></dt>
<dd> <p> The characters in the given context are shown in the terminal&#8217;s standout mode. The actual effect is specific to the terminal; on many terminals it is inverse video. On some such terminals, where the cursor does not blink it appears with standout mode negated, making it less than clear where the cursor actually is. On such terminals one of the other effects may be preferable for highlighting the region and matched search string. </p>
 </dd>
<dt><code>underline</code></dt>
<dd> <p> The characters in the given context are shown underlined. Some terminals show the foreground in a different colour instead; in this case whitespace will not be highlighted. </p>
 </dd></dl>
<p> The characters described above as `special&#8217; are as follows. The formatting described here is used irrespective of whether the characters are highlighted: </p>
<dl>
<dd> <p> ASCII control characters Control characters in the ASCII range are shown as `<code>^</code>&#8216; followed by the base character. </p>
 </dd>
<dt>Unprintable multibyte characters</dt>
<dd> <p> This item applies to control characters not in the ASCII range, plus other characters as follows. If the <code>MULTIBYTE</code> option is in effect, multibyte characters not in the ASCII character set that are reported as having zero width are treated as combining characters when the option <code>COMBINING_CHARS</code> is on. If the option is off, or if a character appears where a combining character is not valid, the character is treated as unprintable. </p>
 </dd>
<dl>
<dd> <p> Unprintable multibyte characters are shown as a hexadecimal number between angle brackets. The number is the code point of the character in the wide character set; this may or may not be Unicode, depending on the operating system. </p>
 </dd></dl>
<dt>Invalid multibyte characters</dt>
<dd> <p> If the <code>MULTIBYTE</code> option is in effect, any sequence of one or more bytes that does not form a valid character in the current character set is treated as a series of bytes each shown as a special character. This case can be distinguished from other unprintable characters as the bytes are represented as two hexadecimal digits between angle brackets, as distinct from the four or eight digits that are used for unprintable characters that are nonetheless valid in the current character set. </p>
 </dd>
<dl>
<dd> <p> Not all systems support this: for it to work, the system&#8217;s representation of wide characters must be code values from the Universal Character Set, as defined by IS0 10646 (also known as Unicode). </p>
 </dd></dl>
<dt>Wrapped double-width characters</dt>
<dd> <p> When a double-width character appears in the final column of a line, it is instead shown on the next line. The empty space left in the original position is highlighted as a special character. </p>
 </dd></dl>
<p> If <code>zle_highlight</code> is not set or no value applies to a particular context, the defaults applied are equivalent to </p>
<dl>
<dd> <pre><code>
 zle_highlight=(region:standout special:standout
suffix:bold isearch:underline paste:standout) 
</code></pre>
 </dd></dl>
<p> i.e. both the region and special characters are shown in standout mode. </p>
<p> Within widgets, arbitrary regions may be highlighted by setting the special array parameter <code>region_highlight</code>; see above. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">KEYMAPS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAE">Reading Commands</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Local Keymaps</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAG">ZLE BUILTINS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">WIDGETS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">USER-DEFINED WIDGETS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAJ">Special Widgets</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAK">STANDARD WIDGETS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAL">Movement</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">History Control</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">Modifying Text</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">Arguments</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">Completion</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">Miscellaneous</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">Text Objects</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAS">CHARACTER HIGHLIGHTING</a></dt>
<dd>  </dd></dl>
