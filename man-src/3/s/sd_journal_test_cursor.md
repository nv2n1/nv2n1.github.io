---
title: "sd_journal_test_cursor(3)"
name: "sd_journal_test_cursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_test_cursor/"
description: "sd_journal_get_cursor, sd_journal_test_cursor – Get cursor string for or test cursor string against the current journal entry"
---

<p>sd_journal_get_cursor, sd_journal_test_cursor &#8211; Get cursor string for or test cursor string against the current journal entry </p>
<h2>Synopsis</h2>
<pre>
#include &lt;systemd/sd-journal.h&gt;
</pre>
<dl COMPACT>
<dt> <code>int sd_journal_get_cursor(sd_journal&nbsp;<wbr>*</code><i>j</i><code>, char&nbsp;<wbr>**</code><i>cursor</i><code>);</code></p>
<dt> <code>int sd_journal_test_cursor(sd_journal&nbsp;<wbr>*</code><i>j</i><code>, const char&nbsp;<wbr>*</code><i>cursor</i><code>);</code></dl>
<h2>Description</h2>
<p> <code>sd_journal_get_cursor()</code></p>
<dd>returns a cursor string for the current journal entry. A cursor is a serialization of the current journal position formatted as text. The string only contains printable characters and can be passed around in text form. The cursor identifies a journal entry globally and in a stable way and may be used to later seek to it via <code><a href="/docs/linux/man/3-sd_journal_seek_cursor/">sd_journal_seek_cursor</a></code>(3). The cursor string should be considered opaque and not be parsed by clients. Seeking to a cursor position without the specific entry being available locally will seek to the next closest (in terms of time) available entry. The call takes two arguments: a journal context object and a pointer to a string pointer where the cursor string will be placed. The string is allocated via libc <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and should be freed after use with <code><a href="/docs/linux/man/3-free/">free</a></code>(3). </p>
<p> Note that <code>sd_journal_get_cursor()</code> will not work before <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) (or related call) has been called at least once, in order to position the read pointer at a valid entry. </p>
<p> <code>sd_journal_test_cursor()</code> may be used to check whether the current position in the journal matches the specified cursor. This is useful since cursor strings do not uniquely identify an entry: the same entry might be referred to by multiple different cursor strings, and hence string comparing cursors is not possible. Use this call to verify after an invocation of <code><a href="/docs/linux/man/3-sd_journal_seek_cursor/">sd_journal_seek_cursor</a></code>(3) whether the entry being sought to was actually found in the journal or the next closest entry was used instead.</p>
<h2>Return Value</h2>
<p> <code>sd_journal_get_cursor()</code> returns 0 on success or a negative errno-style error code. <code>sd_journal_test_cursor()</code> returns positive if the current entry matches the specified cursor, 0 if it does not match the specified cursor or a negative errno-style error code on failure.</p>
<h2>Notes</h2>
<p> The <code>sd_journal_get_cursor()</code> and <code>sd_journal_test_cursor()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_seek_cursor/">sd_journal_seek_cursor</a></code>(3)</p>
