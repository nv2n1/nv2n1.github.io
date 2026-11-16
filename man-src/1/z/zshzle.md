---
title: "zshzle(1)"
name: "zshzle"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshzle/"
description: "zshzle – zsh command line editor"
---

<h2 class="name">NAME</h2>
<p> zshzle &#8211; zsh command line editor </p>
<h2>DESCRIPTION</h2>
<p> If the <code>ZLE</code> option is set (which it is by default in interactive shells) and the shell input is attached to the terminal, the user is able to edit command lines. </p>
<p> There are two display modes. The first, multiline mode, is the default. It only works if the <code>TERM</code> parameter is set to a valid terminal type that can move the cursor up. The second, single line mode, is used if <code>TERM</code> is invalid or incapable of moving the cursor up, or if the <code>SINGLE_LINE_ZLE</code> option is set. This mode is similar to <code>ksh</code>, and uses no termcap sequences. If <code>TERM</code> is &quot;emacs&quot;, the <code>ZLE</code> option will be unset by default. </p>
<p> The parameters <code>BAUD</code>, <code>COLUMNS</code>, and <code>LINES</code> are also used by the line editor. See <i>Parameters Used By The Shell</i> in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<p> The parameter <code>zle_highlight</code> is also used by the line editor; see <i>Character Highlighting</i> below. Highlighting of special characters and the region between the cursor and the mark (as set with <code>set-mark-command</code> in Emacs mode, or by <code>visual-mode</code> in Vi mode) is enabled by default; consult this reference for more information. Irascible conservatives will wish to know that all highlighting may be disabled by the following setting: </p>
<dl>
<dt>
</dt><dd>
<pre>
<code>zle_highlight=(none)</code>
</pre>
</dd></dl>
<p> In many places, references are made to the <code>numeric argument</code>. This can by default be entered in emacs mode by holding the alt key and typing a number, or pressing escape before each digit, and in vi command mode by typing the number before entering a command. Generally the numeric argument causes the next command entered to be repeated the specified number of times, unless otherwise noted below; this is implemented by the <code>digit-argument</code> widget. See also the <i>Arguments</i> subsection of the <i>Widgets</i> section for some other ways the numeric argument can be modified. </p>
<h2>KEYMAPS</h2>
<p> A keymap in ZLE contains a set of bindings between key sequences and ZLE commands. The empty key sequence cannot be bound. </p>
<p> There can be any number of keymaps at any time, and each keymap has one or more names. If all of a keymap&#8217;s names are deleted, it disappears. <code>bindkey</code> can be used to manipulate keymap names. </p>
<p> Initially, there are eight keymaps: </p>
<dl>
<dt><code>emacs</code></dt>
<dd> EMACS emulation</dd>
<dt><code>viins</code></dt>
<dd> vi emulation &#8211; insert mode</dd>
<dt><code>vicmd</code></dt>
<dd> vi emulation &#8211; command mode</dd>
<dt><code>viopp</code></dt>
<dd> vi emulation &#8211; operator pending</dd>
<dt><code>visual</code></dt>
<dd> vi emulation &#8211; selection active</dd>
<dt><code>isearch</code></dt>
<dd> incremental search mode</dd>
<dt><code>command</code></dt>
<dd> read a command name</dd>
<dt><code>.safe</code></dt>
<dd> fallback keymap</dd></dl>
<p> The `<code>.safe</code>&#8216; keymap is special. It can never be altered, and the name can never be removed. However, it can be linked to other names, which can be removed. In the future other special keymaps may be added; users should avoid using names beginning with `<code>.</code>&#8216; for their own keymaps. </p>
<p> In addition to these names, either `<code>emacs</code>&#8216; or `<code>viins</code>&#8216; is also linked to the name `<code>main</code>&#8216;. If one of the <code>VISUAL</code> or <code>EDITOR</code> environment variables contain the string `<code>vi</code>&#8216; when the shell starts up then it will be `<code>viins</code>&#8216;, otherwise it will be `<code>emacs</code>&#8216;. <code>bindkey</code>&#8216;s <code>-e</code> and <code>-v</code> options provide a convenient way to override this default choice. </p>
<p> When the editor starts up, it will select the `<code>main</code>&#8216; keymap. If that keymap doesn&#8217;t exist, it will use `<code>.safe</code>&#8216; instead. </p>
<p> In the `<code>.safe</code>&#8216; keymap, each single key is bound to <code>self-insert</code>, except for ^J (line feed) and ^M (return) which are bound to <code>accept-line</code>. This is deliberately not pleasant to use; if you are using it, it means you deleted the main keymap, and you should put it back.</p>
<h3>Reading Commands</h3>
<p> When ZLE is reading a command from the terminal, it may read a sequence that is bound to some command and is also a prefix of a longer bound string. In this case ZLE will wait a certain time to see if more characters are typed, and if not (or they don&#8217;t match any longer string) it will execute the binding. This timeout is defined by the <code>KEYTIMEOUT</code> parameter; its default is 0.4 sec. There is no timeout if the prefix string is not itself bound to a command. </p>
<p> The key timeout is also applied when ZLE is reading the bytes from a multibyte character string when it is in the appropriate mode. (This requires that the shell was compiled with multibyte mode enabled; typically also the locale has characters with the UTF-8 encoding, although any multibyte encoding known to the operating system is supported.) If the second or a subsequent byte is not read within the timeout period, the shell acts as if <code>?</code> were typed and resets the input state. </p>
<p> As well as ZLE commands, key sequences can be bound to other strings, by using `<code>bindkey -s</code>&#8216;. When such a sequence is read, the replacement string is pushed back as input, and the command reading process starts again using these fake keystrokes. This input can itself invoke further replacement strings, but in order to detect loops the process will be stopped if there are twenty such replacements without a real command being read. </p>
<p> A key sequence typed by the user can be turned into a command name for use in user-defined widgets with the <code>read-command</code> widget, described in the subsection `Miscellaneous&#8217; of the section `Standard Widgets&#8217; below.</p>
<h3>Local Keymaps</h3>
<p> While for normal editing a single keymap is used exclusively, in many modes a local keymap allows for some keys to be customised. For example, in an incremental search mode, a binding in the <code>isearch</code> keymap will override a binding in the <code>main</code> keymap but all keys that are not overridden can still be used. </p>
<p> If a key sequence is defined in a local keymap, it will hide a key sequence in the global keymap that is a prefix of that sequence. An example of this occurs with the binding of <code>iw</code> in <code>viopp</code> as this hides the binding of <code>i</code> in <code>vicmd</code>. However, a longer sequence in the global keymap that shares the same prefix can still apply so for example the binding of <code>^Xa</code> in the global keymap will be unaffected by the binding of <code>^Xb</code> in the local keymap. </p>
<h2>ZLE BUILTINS</h2>
<p> The ZLE module contains three related builtin commands. The <code>bindkey</code> command manipulates keymaps and key bindings; the <code>vared</code> command invokes ZLE on the value of a shell parameter; and the <code>zle</code> command manipulates editing widgets and allows command line access to ZLE commands from within shell functions. </p>
<dl>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-l</code> [ <code>-L</code> ] [ <i>keymap</i> &#8230; ]</dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-d</code></dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-D</code> <i>keymap</i> &#8230;</dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-A</code> <i>old-keymap new-keymap</i></dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-N</code> <i>new-keymap</i> [ <i>old-keymap</i> ]</dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-m</code></dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-r</code> <i>in-string</i> &#8230;</dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <code>-s</code> <i>in-string out-string</i> &#8230;</dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] <i>in-string command</i> &#8230;</dd>
<dt>
</dt><dd> <code>bindkey</code> [ <i>options</i> ] [ <i>in-string</i> ] <code>bindkey</code>&#8216;s options can be divided into three categories: keymap selection for the current command, operation selection, and others. The keymap selection options are:</dd>
<dl>
<dl>
<dt>
</dt><dd> <code>-e</code> Selects keymap `<code>emacs</code>&#8216; for any operations by the current command, and also links `<code>emacs</code>&#8216; to `<code>main</code>&#8216; so that it is selected by default the next time the editor starts.</dd>
<dt><code>-v</code></dt>
<dd> Selects keymap `<code>viins</code>&#8216; for any operations by the current command, and also links `<code>viins</code>&#8216; to `<code>main</code>&#8216; so that it is selected by default the next time the editor starts.</dd>
<dt><code>-a</code></dt>
<dd> Selects keymap `<code>vicmd</code>&#8216; for any operations by the current command.</dd>
<dt><code>-M</code> <i>keymap</i></dt>
<dd> The <i>keymap</i> specifies a keymap name that is selected for any operations by the current command.</dd></dl>
<p> If a keymap selection is required and none of the options above are used, the `<code>main</code>&#8216; keymap is used. Some operations do not permit a keymap to be selected, namely: </p>
<dl>
<dt>
</dt><dd> <code>-l</code> List all existing keymap names; if any arguments are given, list just those keymaps.</dd>
<dl>
<dt>
</dt><dd>
<p> If the <code>-L</code> option is also used, list in the form of <code>bindkey</code> commands to create or link the keymaps. `<code>bindkey -lL main</code>&#8216; shows which keymap is linked to `<code>main</code>&#8216;, if any, and hence if the standard emacs or vi emulation is in effect. This option does not show the <code>.safe</code> keymap because it cannot be created in that fashion; however, neither is `<code>bindkey -lL .safe</code>&#8216; reported as an error, it simply outputs nothing.</dd></dl>
<dt><code>-d</code></dt>
<dd> Delete all existing keymaps and reset to the default state.</dd>
<dt><code>-D</code> <i>keymap</i> &#8230;</dt>
<dd> Delete the named <i>keymap</i>s.</dd>
<dt><code>-A</code> <i>old-keymap new-keymap</i></dt>
<dd> Make the <i>new-keymap</i> name an alias for <i>old-keymap</i>, so that both names refer to the same keymap. The names have equal standing; if either is deleted, the other remains. If there is already a keymap with the <i>new-keymap</i> name, it is deleted.</dd>
<dt><code>-N</code> <i>new-keymap</i> [ <i>old-keymap</i> ]</dt>
<dd> Create a new keymap, named <i>new-keymap</i>. If a keymap already has that name, it is deleted. If an <i>old-keymap</i> name is given, the new keymap is initialized to be a duplicate of it, otherwise the new keymap will be empty.</dd></dl>
<p> To use a newly created keymap, it should be linked to <code>main</code>. Hence the sequence of commands to create and use a new keymap `<code>mymap</code>&#8216; initialized from the <code>emacs</code> keymap (which remains unchanged) is: </p>
<dl>
<dt>
</dt><dd>
<pre>
<code>bindkey -N mymap emacs
bindkey -A mymap main</code>
</pre>
</dd></dl>
<p> Note that while `<code>bindkey -A</code> <i>newmap</i> <code>main</code>&#8216; will work when <i>newmap</i> is <code>emacs</code> or <code>viins</code>, it will not work for <code>vicmd</code>, as switching from vi insert to command mode becomes impossible. </p>
<p> The following operations act on the `<code>main</code>&#8216; keymap if no keymap selection option was given: </p>
<dl>
<dt>
</dt><dd> <code>-m</code> Add the built-in set of meta-key bindings to the selected keymap. Only keys that are unbound or bound to <code>self-insert</code> are affected.</dd>
<dt><code>-r</code> <i>in-string</i> &#8230;</dt>
<dd> Unbind the specified <i>in-string</i>s in the selected keymap. This is exactly equivalent to binding the strings to <code>undefined-key</code>.</dd>
<dl>
<dt>
</dt><dd>
<p> When <code>-R</code> is also used, interpret the <i>in-string</i>s as ranges. </p>
<p> When <code>-p</code> is also used, the <i>in-string</i>s specify prefixes. Any binding that has the given <i>in-string</i> as a prefix, not including the binding for the <i>in-string</i> itself, if any, will be removed. For example, </p>
</dd><dl>
<dt>
</dt><dd>
<pre>
<code>bindkey -rpM viins '^['</code>
</pre>
</dd></dl>
<p> will remove all bindings in the vi-insert keymap beginning with an escape character (probably cursor keys), but leave the binding for the escape character itself (probably <code>vi-cmd-mode</code>). This is incompatible with the option <code>-R</code>.</dl>
<dt><code>-s</code> <i>in-string out-string</i> &#8230;</dt>
<dd> Bind each <i>in-string</i> to each <i>out-string</i>. When <i>in-string</i> is typed, <i>out-string</i> will be pushed back and treated as input to the line editor. When <code>-R</code> is also used, interpret the <i>in-string</i>s as ranges.</dd>
<dl>
<dt>
</dt><dd>
<p> Note that both <i>in-string</i> and <i>out-string</i> are subject to the same form of interpretation, as described below.</dd></dl>
<dt><i>in-string command</i> &#8230;</dt>
<dd> Bind each <i>in-string</i> to each <i>command</i>. When <code>-R</code> is used, interpret the <i>in-string</i>s as ranges.</dd>
<dt>[ <i>in-string</i> ]</dt>
<dd> List key bindings. If an <i>in-string</i> is specified, the binding of that string in the selected keymap is displayed. Otherwise, all key bindings in the selected keymap are displayed. (As a special case, if the <code>-e</code> or <code>-v</code> option is used alone, the keymap is <i>not</i> displayed &#8211; the implicit linking of keymaps is the only thing that happens.)</dd>
<dl>
<dt>
</dt><dd>
<p> When the option <code>-p</code> is used, the <i>in-string</i> must be present. The listing shows all bindings which have the given key sequence as a prefix, not including any bindings for the key sequence itself. </p>
<p> When the <code>-L</code> option is used, the list is in the form of <code>bindkey</code> commands to create the key bindings.</dd></dl>
</dl>
<p> When the <code>-R</code> option is used as noted above, a valid range consists of two characters, with an optional `<code>&#8211;</code>&#8216; between them. All characters between the two specified, inclusive, are bound as specified. </p>
<p> For either <i>in-string</i> or <i>out-string</i>, the following escape sequences are recognised: </p>
<dl>
<dt><code></code></dt>
<dd> bell character</dd>
<dt><code></code></dt>
<dd> backspace</dd>
<dt><code></code>, <code>\E</code></dt>
<dd> escape</dd>
<dt><code></code></dt>
<dd> form feed</dd>
<dt><code>
</code></dt>
<dd> linefeed (newline)</dd>
<dt><code>
</code></dt>
<dd> carriage return</dd>
<dt><code>	</code></dt>
<dd> horizontal tab</dd>
<dt><code></code></dt>
<dd> vertical tab</dd>
<dt><code>\</code><i>NNN</i></dt>
<dd> character code in octal</dd>
<dt><code>
</dt></dl></dl></dl>
</code>
