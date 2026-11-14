---
title: "fish_key_reader(1)"
name: "fish_key_reader"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fish_key_reader/"
description: "fish_key_reader — explore what characters keyboard keys send"
---

<h2 class="name">NAME</h2>
<p> <code>fish_key_reader</code> &#8212; explore what characters keyboard keys send </p>
<h3>Synopsis</h3>
<pre><code>
fish_key_reader[-c][-d LEVEL]
</code></pre>
<h3>Description</h3>
<p> fish_key_reader is used to study input received from the terminal and can help with key binds. The program is interactive and works on standard input. Individual characters themselves and their hexadecimal values are displayed. </p>
<p> The tool will output an example bind command matching the character sequence captured. If the character sequence matches a special key name (see bind &#8211;key-names), both bind CHARS &#8230; and bind -k KEYNAME &#8230; usage will be shown. </p>
<p> The following parameters are available: </p>
<dl>
<dt>&bull;</p>
<dd> -c or &#8211;continuous begins a session where multiple key sequences can be inspected. By default the program exits after capturing a single key sequence.</p>
<dt>&bull;</p>
<dd> -d or &#8211;debug-level=DEBUG_LEVEL enables debug output and specifies a verbosity level (like fish -d). Defaults to 0.</dl>
<p> In continuous mode (-c), the delay in milliseconds since the previous character was received is also shown. This information may be useful to determine a preferred fish_escape_delay_ms setting or learn the amount of lag introduced by ssh or tmux. </p>
<p> fish_key_reader intentionally disables handling of many signals. To terminate fish_key_reader in a &#8211;continuous run:</p>
<dl>
<dt>&bull;</p>
<dd> press Ctrl-C twice, or</p>
<dt>&bull;</p>
<dd> press Ctrl-D twice, or</p>
<dt>&bull;</p>
<dd> type exit, or</p>
<dt>&bull;</p>
<dd> type quit</dl>
<h2>Index</h2>
