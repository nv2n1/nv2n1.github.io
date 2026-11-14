---
title: "zshroadmap(1)"
name: "zshroadmap"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshroadmap/"
description: "zshroadmap – informal introduction to the zsh manual The Zsh Manual, like the shell itself, is large and often complicated. This section of the manual provides some pointers to areas of the shell t..."
---

<h2 class="name">NAME</h2>
<p> zshroadmap &#8211; informal introduction to the zsh manual The Zsh Manual, like the shell itself, is large and often complicated. This section of the manual provides some pointers to areas of the shell that are likely to be of particular interest to new users, and indicates where in the rest of the manual the documentation is to be found.</p>
<h2>WHEN THE SHELL STARTS</h2>
<p> When it starts, the shell reads commands from various files. These can be created or edited to customize the shell. See the section Startup/Shutdown Files in <i><a href="/docs/linux/man/1-zsh/">zsh</a></i>(1). </p>
<p> If no personal initialization files exist for the current user, a function is run to help you change some of the most common settings. It won&#8217;t appear if your administrator has disabled the <code>zsh/newuser</code> module. The function is designed to be self-explanatory. You can run it by hand with `<code>autoload -Uz zsh-newuser-install; zsh-newuser-install -f</code>&#8216;. See also the section User Configuration Functions in <i><a href="/docs/linux/man/1-zshcontrib/">zshcontrib</a></i>(1). </p>
<h2>INTERACTIVE USE</h2>
<p> Interaction with the shell uses the builtin Zsh Line Editor, ZLE. This is described in detail in <i><a href="/docs/linux/man/1-zshzle/">zshzle</a></i>(1). </p>
<p> The first decision a user must make is whether to use the Emacs or Vi editing mode as the keys for editing are substantially different. Emacs editing mode is probably more natural for beginners and can be selected explicitly with the command <code>bindkey -e</code>. </p>
<p> A history mechanism for retrieving previously typed lines (most simply with the Up or Down arrow keys) is available; note that, unlike other shells, zsh will not save these lines when the shell exits unless you set appropriate variables, and the number of history lines retained by default is quite small (30 lines). See the description of the shell variables (referred to in the documentation as parameters) <code>HISTFILE</code>, <code>HISTSIZE</code> and <code>SAVEHIST</code> in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). Note that it&#8217;s currently only possible to read and write files saving history when the shell is interactive, i.e. it does not work from scripts. </p>
<p> The shell now supports the UTF-8 character set (and also others if supported by the operating system). This is (mostly) handled transparently by the shell, but the degree of support in terminal emulators is variable. There is some discussion of this in the shell FAQ, <code><a rel="nofollow" href="http://www.zsh.org/FAQ/">http://www.zsh.org/FAQ/</a></code>. Note in particular that for combining characters to be handled the option <code>COMBINING_CHARS</code> needs to be set. Because the shell is now more sensitive to the definition of the character set, note that if you are upgrading from an older version of the shell you should ensure that the appropriate variable, either <code>LANG</code> (to affect all aspects of the shell&#8217;s operation) or <code>LC_CTYPE</code> (to affect only the handling of character sets) is set to an appropriate value. This is true even if you are using a single-byte character set including extensions of ASCII such as <code>ISO-8859-1</code> or <code>ISO-8859-15</code>. See the description of <code>LC_CTYPE</code> in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<h3>Completion</h3>
<p> Completion is a feature present in many shells. It allows the user to type only a part (usually the prefix) of a word and have the shell fill in the rest. The completion system in zsh is programmable. For example, the shell can be set to complete email addresses in arguments to the mail command from your <code>~/.abook/addressbook</code>; usernames, hostnames, and even remote paths in arguments to scp, and so on. Anything that can be written in or glued together with zsh can be the source of what the line editor offers as possible completions. </p>
<p> Zsh has two completion systems, an old, so called <code>compctl</code> completion (named after the builtin command that serves as its complete and only user interface), and a new one, referred to as <code>compsys</code>, organized as library of builtin and user-defined functions. The two systems differ in their interface for specifying the completion behavior. The new system is more customizable and is supplied with completions for many commonly used commands; it is therefore to be preferred. </p>
<p> The completion system must be enabled explicitly when the shell starts. For more information see <i><a href="/docs/linux/man/1-zshcompsys/">zshcompsys</a></i>(1). </p>
<h3>Extending the line editor</h3>
<p> Apart from completion, the line editor is highly extensible by means of shell functions. Some useful functions are provided with the shell; they provide facilities such as: </p>
<dl>
<dt>
<dd> <code>insert-composed-char</code> composing characters not found on the keyboard</p>
<dt><code>match-words-by-style</code></p>
<dd> configuring what the line editor considers a word when moving or deleting by word</p>
<dt><code>history-beginning-search-backward-end</code>, etc.</p>
<dd> alternative ways of searching the shell history</p>
<dt><code>replace-string</code>, <code>replace-pattern</code></p>
<dd> functions for replacing strings or patterns globally in the command line</p>
<dt><code>edit-command-line</code></p>
<dd> edit the command line with an external editor.</dl>
<p> See the section `ZLE Functions&#8217; in <i><a href="/docs/linux/man/1-zshcontrib/">zshcontrib</a></i>(1) for descriptions of these. </p>
<h2>OPTIONS</h2>
<p> The shell has a large number of options for changing its behaviour. These cover all aspects of the shell; browsing the full documentation is the only good way to become acquainted with the many possibilities. See <i><a href="/docs/linux/man/1-zshoptions/">zshoptions</a></i>(1). </p>
<h2>PATTERN MATCHING</h2>
<p> The shell has a rich set of patterns which are available for file matching (described in the documentation as `filename generation&#8217; and also known for historical reasons as `globbing&#8217;) and for use when programming. These are described in the section `Filename Generation&#8217; in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1). </p>
<p> Of particular interest are the following patterns that are not commonly supported by other systems of pattern matching: </p>
<dl>
<dt>
<dd> <code>**</code> for matching over multiple directories</p>
<dt><code>|</code></p>
<dd> for matching either of two alternatives</p>
<dt><code>~</code>, <code>^</code></p>
<dd> the ability to exclude patterns from matching when the <code>EXTENDED_GLOB</code> option is set</p>
<dt><code>(</code><i>&#8230;</i><code>)</code></p>
<dd> glob qualifiers, included in parentheses at the end of the pattern, which select files by type (such as directories) or attribute (such as size).</dl>
<h2>GENERAL COMMENTS ON SYNTAX</h2>
<p> Although the syntax of zsh is in ways similar to the Korn shell, and therefore more remotely to the original UNIX shell, the Bourne shell, its default behaviour does not entirely correspond to those shells. General shell syntax is introduced in the section `Shell Grammar&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). </p>
<p> One commonly encountered difference is that variables substituted onto the command line are not split into words. See the description of the shell option <code>SH_WORD_SPLIT</code> in the section `Parameter Expansion&#8217; in <i><a href="/docs/linux/man/1-zshexpn/">zshexpn</a></i>(1). In zsh, you can either explicitly request the splitting (e.g. <code>${=foo}</code>) or use an array when you want a variable to expand to more than one word. See the section `Array Parameters&#8217; in <i><a href="/docs/linux/man/1-zshparam/">zshparam</a></i>(1). </p>
<h2>PROGRAMMING</h2>
<p> The most convenient way of adding enhancements to the shell is typically by writing a shell function and arranging for it to be autoloaded. Functions are described in the section `Functions&#8217; in <i><a href="/docs/linux/man/1-zshmisc/">zshmisc</a></i>(1). Users changing from the C shell and its relatives should notice that aliases are less used in zsh as they don&#8217;t perform argument substitution, only simple text replacement. </p>
<p> A few general functions, other than those for the line editor described above, are provided with the shell and are described in <i><a href="/docs/linux/man/1-zshcontrib/">zshcontrib</a></i>(1). Features include: </p>
<dl>
<dt>
<dd> <code>promptinit</code> a prompt theme system for changing prompts easily, see the section `Prompt Themes&#8217; </p>
<dt><code>zsh-mime-setup</code></p>
<dd> a MIME-handling system which dispatches commands according to the suffix of a file as done by graphical file managers</p>
<dt><code>zcalc</code></p>
<dd> a calculator</p>
<dt><code>zargs</code></p>
<dd> a version of <code>xargs</code> that makes the <code>find</code> command redundant</p>
<dt><code>zmv</code></p>
<dd> a command for renaming files by means of shell patterns. </p>
</dl>
<h2>Index</h2>
