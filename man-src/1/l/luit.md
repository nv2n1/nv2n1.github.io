---

title: "luit(1)"
name: "luit"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luit/"
description: "luit – Locale and ISO 2022 support for Unicode terminals"
---

<p> <code>luit</code> [ <i>options</i> ] [ <code>&#8212;</code> ] [ <i>program</i> [ <i>args</i> ] ]</p>
<p> <code>Luit</code> is a filter that can be run between an arbitrary application and a UTF-8 terminal emulator. It will convert application output from the locale&#8217;s encoding into UTF-8, and convert terminal input from UTF-8 into the locale&#8217;s encoding. </p>
<p> An application may also request switching to a different output encoding using ISO 2022 and ISO 6429 escape sequences. Use of this feature is discouraged: multilingual applications should be modified to directly generate UTF-8 instead. </p>
<p> <code>Luit</code> is usually invoked transparently by the terminal emulator. For information about running <code>luit</code> from the command line, see EXAMPLES below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display some summary help and quit.</dd>
<dt><code>-list</code></dt>
<dd> List the supported charsets and encodings, then quit.</dd>
<dt><code>-V</code></dt>
<dd> Print luit&#8217;s version and quit.</dd>
<dt><code>-v</code></dt>
<dd> Be verbose.</dd>
<dt><code>-c</code></dt>
<dd> Function as a simple converter from standard input to standard output.</dd>
<dt><code>-p</code></dt>
<dd> In startup, establish a handshake between parent and child processes. This is needed for some systems, e.g., FreeBSD.</dd>
<dt><code>-x</code></dt>
<dd> Exit as soon as the child dies. This may cause <code>luit</code> to lose data at the end of the child&#8217;s output.</dd>
<dt><code>-argv0</code><i> name</i></dt>
<dd> Set the child&#8217;s name (as passed in argv[0]).</dd>
<dt><code>-encoding</code><i> encoding</i></dt>
<dd> Set up <code>luit</code> to use <i>encoding</i> rather than the current locale&#8217;s encoding.</dd>
<dt><code>+oss</code></dt>
<dd> Disable interpretation of single shifts in application output.</dd>
<dt><code>+ols</code></dt>
<dd> Disable interpretation of locking shifts in application output.</dd>
<dt><code>+osl</code></dt>
<dd> Disable interpretation of character set selection sequences in application output.</dd>
<dt><code>+ot</code></dt>
<dd> Disable interpretation of all sequences and pass all sequences in application output to the terminal unchanged. This may lead to interesting results.</dd>
<dt><code>-k7</code></dt>
<dd> Generate seven-bit characters for keyboard input.</dd>
<dt><code>+kss</code></dt>
<dd> Disable generation of single-shifts for keyboard input.</dd>
<dt><code>+kssgr</code></dt>
<dd> Use GL codes after a single shift for keyboard input. By default, GR codes are generated after a single shift when generating eight-bit keyboard input.</dd>
<dt><code>-kls</code></dt>
<dd> Generate locking shifts (SO/SI) for keyboard input.</dd>
<dt><code>-gl</code><i> gn</i></dt>
<dd> Set the initial assignment of GL. The argument should be one of <code>g0</code>, <code>g1</code>, <code>g2</code> or <code>g3</code>. The default depends on the locale, but is usually <code>g0</code>.</dd>
<dt><code>-gr</code><i> gk</i></dt>
<dd> Set the initial assignment of GR. The default depends on the locale, and is usually <code>g2</code> except for EUC locales, where it is <code>g1</code>.</dd>
<dt><code>-g0</code><i> charset</i></dt>
<dd> Set the charset initially selected in G0. The default depends on the locale, but is usually <code>ASCII</code>.</dd>
<dt><code>-g1</code><i> charset</i></dt>
<dd> Set the charset initially selected in G1. The default depends on the locale.</dd>
<dt><code>-g2</code><i> charset</i></dt>
<dd> Set the charset initially selected in G2. The default depends on the locale.</dd>
<dt><code>-g3</code><i> charset</i></dt>
<dd> Set the charset initially selected in G3. The default depends on the locale.</dd>
<dt><code>-ilog</code><i> filename</i></dt>
<dd> Log into <i>filename</i> all the bytes received from the child.</dd>
<dt><code>-olog</code><i> filename</i></dt>
<dd> Log into <i>filename</i> all the bytes sent to the terminal emulator.</dd>
<dt><code>-alias</code><i> filename</i></dt>
<dd> the locale alias file<br />
 (default: /usr/share/X11/locale/locale.alias).</dd>
<dt><code>&#8212;</code></dt>
<dd> End of options.</dd></dl>
<h2>EXAMPLES</h2>
<p> The most typical use of <code>luit</code> is to adapt an instance of <code>XTerm</code> to the locale&#8217;s encoding. Current versions of <code>XTerm</code> invoke <code>luit</code> automatically when it is needed. If you are using an older release of <code>XTerm</code>, or a different terminal emulator, you may invoke <code>luit</code> manually:</p>
<dl>
<dt>
</dt><dd> $ xterm -u8 -e luit</dd></dl>
<p> If you are running in a UTF-8 locale but need to access a remote machine that doesn&#8217;t support UTF-8, <code>luit</code> can adapt the remote output to your terminal:</p>
<dl>
<dt>
</dt><dd> $ LC_ALL=fr_FR luit ssh legacy-machine</dd></dl>
<p> <code>Luit</code> is also useful with applications that hard-wire an encoding that is different from the one normally used on the system or want to use legacy escape sequences for multilingual output. In particular, versions of <code>Emacs</code> that do not speak UTF-8 well can use <code>luit</code> for multilingual output:</p>
<dl>
<dt>
</dt><dd> $ luit -encoding &#8216;ISO 8859-1&#8217; emacs -nw</dd></dl>
<p> And then, in <code>Emacs</code>,</p>
<dl>
<dt>
</dt><dd> M-x set-terminal-coding-system RET iso-2022-8bit-ss2 RET</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/X11/locale/locale.alias</code></dt>
<dd> The file mapping locales to locale encodings.</dd></dl>
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
