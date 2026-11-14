---
title: "auparse_set_escape_mode(3)"
name: "auparse_set_escape_mode"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_set_escape_mode/"
description: "auparse_set_escape_mode – choose escape method"
---

<h2>NAME</h2>
<p> auparse_set_escape_mode &#8211; choose escape method</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> void auparse_set_escape_mode(auparse_state_t *au, auparse_esc_t mode); </p>
<h2>DESCRIPTION</h2>
<p> auparse_set_escape_mode is used to set the escaping method that will be used to output interpretted text. The choices for the mode variable are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>AUPARSE_ESC_RAW</code></p>
<dd> No escaping of any kind is done.</p>
<dt><code>AUPARSE_ESC_TTY</code></p>
<dd> Escape TTY control characters so that they are harmless to display on a terminal. When any control character is found, they are displayed as octal numbers. This is the default mode that the auparse library is initialized with.</p>
<dt><code>AUPARSE_ESC_SHELL</code></p>
<dd> Besides escaping control characters, this will escape some characters that can cause problems when used with shell scripting. Any escaped control characters are displayed as octal numbers. Other escaped characters are proceeded with a backslash. The additional characters it escapes are: &quot; &#8216; ` $ \</p>
<dt><code>AUPARSE_ESC_SHELL_QUOTE</code></p>
<dd> Similar to <i>AUPARSE_ESC_SHELL</i> but expands the character set to include shell operators. Any escaped control characters are displayed as octal numbers. Other escaped characters are proceeded with a backslash. The additional characters it escapes include: ; &#8216; &nbsp;<wbr>&quot; ` # $ &amp; * ? [ ] &lt; &gt; { } \</dl>
</dl>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_interpret_field/">auparse_interpret_field</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
