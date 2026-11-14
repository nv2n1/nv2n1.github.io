---
title: "dumpkeys(1)"
name: "dumpkeys"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dumpkeys/"
description: "dumpkeys – dump keyboard translation tables"
---

<h2 class="name">NAME</h2>
<p> dumpkeys &#8211; dump keyboard translation tables </p>
<h2>SYNOPSIS</h2>
<p> <code>dumpkeys</code> [ <code>-h &#8211;help -i &#8211;short-info -l -s &#8211;long-info</code> <code>-n &#8211;numeric -f &#8211;full-table -1 &#8211;separate-lines</code> <code>-S</code><i>shape</i> <code>&#8211;shape=</code><i>shape</i> <code>-t &#8211;funcs-only -k &#8211;keys-only -d &#8211;compose-only</code> <code>-c</code><i>charset</i> <code>&#8211;charset=</code><i>charset</i> <code>-v &#8211;verbose -V &#8211;version</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>dumpkeys</code> writes, to the standard output, the current contents of the keyboard driver&#8217;s translation tables, in the format specified by <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5). </p>
<p> Using the various options, the format of the output can be controlled and also other information from the kernel and the programs <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1) and <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) can be obtained.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Prints the program&#8217;s version number and a short usage message to the program&#8217;s standard error output and exits.</p>
<dt><code>-i &#8211;short-info</code></p>
<dd> Prints some characteristics of the kernel&#8217;s keyboard driver. The items shown are:</dl>
<dl>
<dt>
<dd> Keycode range supported by the kernel </p>
<dl>
<dt>
<dd> This tells what values can be used after the <code>keycode</code> keyword in keytable files. See <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) for more information and the syntax of these files.</dl>
<p> Number of actions bindable to a key </p>
<dl>
<dt>
<dd> This tells how many different actions a single key can output using various modifier keys. If the value is 16 for example, you can define up to 16 different actions to a key combined with modifiers. When the value is 16, the kernel probably knows about four modifier keys, which you can press in different combinations with the key to access all the bound actions.</dl>
<p> Ranges of action codes supported by the kernel </p>
<dl>
<dt>
<dd> This item contains a list of action code ranges in hexadecimal notation. These are the values that can be used in the right hand side of a key definition, ie. the <i>vv</i>&#8216;s in a line </p>
<dl>
<dt>
<dd> <code>keycode</code> <i>xx</i> = <i>vv vv vv vv</i></dl>
<p> (see <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) for more information about the format of key definition lines). <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1) and <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) support a symbolic notation, which is preferable to the numeric one, as the action codes may vary from kernel to kernel while the symbolic names usually remain the same. However, the list of action code ranges can be used to determine, if the kernel actually supports all the symbols <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) knows, or are there maybe some actions supported by the kernel that have no symbolic name in your <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) program. To see this, you compare the range list with the action symbol list, see option <code>&#8211;long-info</code> below.</dl>
<p> Number of function keys supported by kernel </p>
<dl>
<dt>
<dd> This tells the number of action codes that can be used to output strings of characters. These action codes are traditionally bound to the various function and editing keys of the keyboard and are defined to send standard escape sequences. However, you can redefine these to send common command lines, email addresses or whatever you like. Especially if the number of this item is greater than the number of function and editing keys in your keyboard, you may have some &quot;spare&quot; action codes that you can bind to AltGr-letter combinations, for example, to send some useful strings. See <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) for more details.</dl>
<p> Function strings </p>
<dl>
<dt>
<dd> You can see you current function key definitions with the command </p>
<dl>
<dt>
<dd> <code>dumpkeys &#8211;funcs-only</code></dl>
</dl>
</dl>
<dl>
<dt><code>-l -s &#8211;long-info</code></p>
<dd> This option instructs <code>dumpkeys</code> to print a long information listing. The output is the same as with the <code>&#8211;short-info</code> appended with the list of action symbols supported by <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) and <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1), along with the symbols&#8217; numeric values.</dl>
<dl>
<dt><code>-n &#8211;numeric</code></p>
<dd> This option causes <code>dumpkeys</code> to by-pass the conversion of action code values to symbolic notation and to print the in hexadecimal format instead.</dl>
<dl>
<dt><code>-f &#8211;full-table</code></p>
<dd> This makes <code>dumpkeys</code> skip all the short-hand heuristics (see <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5)) and output the key bindings in the canonical form. First a keymaps line describing the currently defined modifier combinations is printed. Then for each key a row with a column for each modifier combination is printed. For example, if the current keymap in use uses seven modifiers, every row will have seven action code columns. This format can be useful for example to programs that post-process the output of <code>dumpkeys</code>.</dl>
<dl>
<dt><code>-S</code><i>shape</i><i> </i><code>&#8211;shape=</code><i>shape</i></p>
<dd></dl>
<dl>
<dt><code>-t &#8211;funcs-only</code></p>
<dd> When this option is given, <code>dumpkeys</code> prints only the function key string definitions. Normally <code>dumpkeys</code> prints both the key bindings and the string definitions.</dl>
<dl>
<dt><code>-k &#8211;keys-only</code></p>
<dd> When this option is given, <code>dumpkeys</code> prints only the key bindings. Normally <code>dumpkeys</code> prints both the key bindings and the string definitions.</dl>
<dl>
<dt><code>-d &#8211;compose-only</code></p>
<dd> When this option is given, <code>dumpkeys</code> prints only the compose key combinations. This option is available only if your kernel has compose key support.</dl>
<dl>
<dt><code>-c</code><i>charset</i><i> </i><code>&#8211;charset=</code><i>charset</i></p>
<dd> This instructs <code>dumpkeys</code> to interpret character code values according to the specified character set. This affects only the translation of character code values to symbolic names. Valid values for <i>charset</i> currently are <code>iso-8859-X</code>, Where X is a digit in 1-9. If no <i>charset</i> is specified, <code>iso-8859-1</code> is used as a default. This option produces an output line `charset &quot;iso-8859-X&quot;&#8217;, telling loadkeys how to interpret the keymap. (For example, &quot;division&quot; is 0xf7 in iso-8859-1 but 0xba in iso-8859-8.)</dl>
<dl>
<dt><code>-v &#8211;verbose</code></p>
<dd></dl>
<dl>
<dt><code>-V &#8211;version</code></p>
<dd> Prints version number and exits.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/keymaps</i></p>
<dd> The recommended directory for keytable files.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) </p>
<h2>Index</h2>
