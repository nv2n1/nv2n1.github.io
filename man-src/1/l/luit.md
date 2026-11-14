---
title: "luit(1)"
name: "luit"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luit/"
description: "luit – Locale and ISO 2022 support for Unicode terminals"
---

<h2 class="name">NAME</h2>
<p> luit &#8211; Locale and ISO 2022 support for Unicode terminals </p>
<h2>SYNOPSIS</h2>
<p> <code>luit</code> [ <i>options</i> ] [ <code>&#8212;</code> ] [ <i>program</i> [ <i>args</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Luit</code> is a filter that can be run between an arbitrary application and a UTF-8 terminal emulator. It will convert application output from the locale&#8217;s encoding into UTF-8, and convert terminal input from UTF-8 into the locale&#8217;s encoding. </p>
<p> An application may also request switching to a different output encoding using ISO 2022 and ISO 6429 escape sequences. Use of this feature is discouraged: multilingual applications should be modified to directly generate UTF-8 instead. </p>
<p> <code>Luit</code> is usually invoked transparently by the terminal emulator. For information about running <code>luit</code> from the command line, see EXAMPLES below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display some summary help and quit.</p>
<dt><code>-list</code></p>
<dd> List the supported charsets and encodings, then quit.</p>
<dt><code>-V</code></p>
<dd> Print luit&#8217;s version and quit.</p>
<dt><code>-v</code></p>
<dd> Be verbose.</p>
<dt><code>-c</code></p>
<dd> Function as a simple converter from standard input to standard output.</p>
<dt><code>-p</code></p>
<dd> In startup, establish a handshake between parent and child processes. This is needed for some systems, e.g., FreeBSD.</p>
<dt><code>-x</code></p>
<dd> Exit as soon as the child dies. This may cause <code>luit</code> to lose data at the end of the child&#8217;s output.</p>
<dt><code>-argv0</code><i> name</i></p>
<dd> Set the child&#8217;s name (as passed in argv[0]).</p>
<dt><code>-encoding</code><i> encoding</i></p>
<dd> Set up <code>luit</code> to use <i>encoding</i> rather than the current locale&#8217;s encoding.</p>
<dt><code>+oss</code></p>
<dd> Disable interpretation of single shifts in application output.</p>
<dt><code>+ols</code></p>
<dd> Disable interpretation of locking shifts in application output.</p>
<dt><code>+osl</code></p>
<dd> Disable interpretation of character set selection sequences in application output.</p>
<dt><code>+ot</code></p>
<dd> Disable interpretation of all sequences and pass all sequences in application output to the terminal unchanged. This may lead to interesting results.</p>
<dt><code>-k7</code></p>
<dd> Generate seven-bit characters for keyboard input.</p>
<dt><code>+kss</code></p>
<dd> Disable generation of single-shifts for keyboard input.</p>
<dt><code>+kssgr</code></p>
<dd> Use GL codes after a single shift for keyboard input. By default, GR codes are generated after a single shift when generating eight-bit keyboard input.</p>
<dt><code>-kls</code></p>
<dd> Generate locking shifts (SO/SI) for keyboard input.</p>
<dt><code>-gl</code><i> gn</i></p>
<dd> Set the initial assignment of GL. The argument should be one of <code>g0</code>, <code>g1</code>, <code>g2</code> or <code>g3</code>. The default depends on the locale, but is usually <code>g0</code>.</p>
<dt><code>-gr</code><i> gk</i></p>
<dd> Set the initial assignment of GR. The default depends on the locale, and is usually <code>g2</code> except for EUC locales, where it is <code>g1</code>.</p>
<dt><code>-g0</code><i> charset</i></p>
<dd> Set the charset initially selected in G0. The default depends on the locale, but is usually <code>ASCII</code>.</p>
<dt><code>-g1</code><i> charset</i></p>
<dd> Set the charset initially selected in G1. The default depends on the locale.</p>
<dt><code>-g2</code><i> charset</i></p>
<dd> Set the charset initially selected in G2. The default depends on the locale.</p>
<dt><code>-g3</code><i> charset</i></p>
<dd> Set the charset initially selected in G3. The default depends on the locale.</p>
<dt><code>-ilog</code><i> filename</i></p>
<dd> Log into <i>filename</i> all the bytes received from the child.</p>
<dt><code>-olog</code><i> filename</i></p>
<dd> Log into <i>filename</i> all the bytes sent to the terminal emulator.</p>
<dt><code>-alias</code><i> filename</i></p>
<dd> the locale alias file<br />
 (default: /usr/share/X11/locale/locale.alias).</p>
<dt><code>&#8212;</code></p>
<dd> End of options.</dl>
<h2>EXAMPLES</h2>
<p> The most typical use of <code>luit</code> is to adapt an instance of <code>XTerm</code> to the locale&#8217;s encoding. Current versions of <code>XTerm</code> invoke <code>luit</code> automatically when it is needed. If you are using an older release of <code>XTerm</code>, or a different terminal emulator, you may invoke <code>luit</code> manually:</p>
<dl>
<dt>
<dd> $ xterm -u8 -e luit</dl>
<p> If you are running in a UTF-8 locale but need to access a remote machine that doesn&#8217;t support UTF-8, <code>luit</code> can adapt the remote output to your terminal:</p>
<dl>
<dt>
<dd> $ LC_ALL=fr_FR luit ssh legacy-machine</dl>
<p> <code>Luit</code> is also useful with applications that hard-wire an encoding that is different from the one normally used on the system or want to use legacy escape sequences for multilingual output. In particular, versions of <code>Emacs</code> that do not speak UTF-8 well can use <code>luit</code> for multilingual output:</p>
<dl>
<dt>
<dd> $ luit -encoding &#8216;ISO 8859-1&#8217; emacs -nw</dl>
<p> And then, in <code>Emacs</code>,</p>
<dl>
<dt>
<dd> M-x set-terminal-coding-system RET iso-2022-8bit-ss2 RET</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/X11/locale/locale.alias</code></p>
<dd> The file mapping locales to locale encodings.</dl>
<h2>SECURITY</h2>
<p> On systems with SVR4 (&#8220;Unix-98&#8221;) ptys (Linux version 2.2 and later, SVR4), <code>luit</code> should be run as the invoking user. </p>
<p> On systems without SVR4 (&#8220;Unix-98&#8221;) ptys (notably BSD variants), running <code>luit</code> as an ordinary user will leave the tty world-writable; this is a security hole, and luit will generate a warning (but still accept to run). A possible solution is to make <code>luit</code> suid root; <code>luit</code> should drop privileges sufficiently early to make this safe. However, the startup code has not been exhaustively audited, and the author takes no responsibility for any resulting security issues. </p>
<p> <code>Luit</code> will refuse to run if it is installed setuid and cannot safely drop privileges.</p>
<h2>BUGS</h2>
<p> None of this complexity should be necessary. Stateless UTF-8 throughout the system is the way to go. </p>
<p> Charsets with a non-trivial intermediary byte are not yet supported. </p>
<p> Selecting alternate sets of control characters is not supported and will never be.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xterm/">xterm</a>(1), <a href="/docs/linux/man/7-unicode/">unicode</a>(7), <a href="/docs/linux/man/7-utf-8/">utf-8</a>(7), <a href="/docs/linux/man/7-charsets/">charsets</a>(7). </p>
<pre>
<br>
<i>Character Code Structure and Extension Techniques (ISO 2022, ECMA-35)</i>.
<br>
<i>Control Functions for Coded Character Sets (ISO 6429, ECMA-48)</i>.
</pre>
<h2>AUTHOR</h2>
<p> The version of <code>Luit</code> included in this X.Org Foundation release was originally written by Juliusz Chroboczek &lt;jch [at] freedesktop.org&gt; for the XFree86 Project and includes additional contributions from Thomas E. Dickey required for newer releases of <a href="/docs/linux/man/1-xterm/">xterm</a>(1). </p>
<h2>Index</h2>
