---
title: "struct_jbd2_journal_handle(9)"
name: "struct_jbd2_journal_handle"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_jbd2_journal_handle/"
description: "struct_jbd2_journal_handle – The handle_s type is the concrete type associated with handle_t."
---

<p>struct_jbd2_journal_handle &#8211; The handle_s type is the concrete type associated with handle_t.</p>
<h2>Synopsis</h2>
<pre><code>struct jbd2_journal_handle {
    union {
        unnamed_union
    };
    int h_buffer_credits;
    int h_ref;
    int h_err;
    unsigned int h_sync : 1;
    unsigned int h_jdata : 1;
    unsigned int h_aborted : 1;
};</code></pre>
<h2>Members</h2>
<p>{unnamed_union}</p>
<dl>
<dd>anonymous</dl>
<p> h_buffer_credits</p>
<dl>
<dd>Number of remaining buffers we are allowed to dirty.</dl>
<p> h_ref</p>
<dl>
<dd>Reference count on this handle</dl>
<p> h_err</p>
<dl>
<dd>Field for caller&#8217;s use to track errors through large fs operations</dl>
<p> h_sync</p>
<dl>
<dd>flag for sync-on-close</dl>
<p> h_jdata</p>
<dl>
<dd>flag to force data journaling</dl>
<p> h_aborted</p>
<dl>
<dd>flag indicating fatal error on handle</dl>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
