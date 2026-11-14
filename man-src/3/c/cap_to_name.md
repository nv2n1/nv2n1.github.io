---
title: "cap_to_name(3)"
name: "cap_to_name"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cap_to_name/"
description: "cap_from_text, cap_to_text, cap_to_name, cap_from_name – capability state textual representation translation"
---

<h2>NAME</h2>
<p> cap_from_text, cap_to_text, cap_to_name, cap_from_name &#8211; capability state textual representation translation</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/capability.h&gt;</code> </p>
<p> <code>cap_t cap_from_text(const char *</code><i>buf_p</i><code>);</code> </p>
<p> <code>char *cap_to_text(cap_t </code><i>caps</i><code>, ssize_t *</code><i>length_p</i><code>);</code> </p>
<p> <code>int cap_from_name(const char *</code><i>name</i><code>, cap_value_t *</code><i>cap_p</i><code>);</code> </p>
<p> <code>char *cap_to_name(cap_value_t </code><i>cap</i><code>);</code> </p>
<p> Link with <i>-lcap</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions translate a capability state between an internal representation and a textual one. The internal representation is managed by the capability functions in working storage. The textual representation is a structured, human-readable string suitable for display. </p>
<p> <code>cap_from_text</code>() allocates and initializes a capability state in working storage. It then sets the contents of this newly created capability state to the state represented by a human-readable, nul-terminated character string pointed to by <i>buf_p</i>. It returns a pointer to the newly created capability state. When the capability state in working storage is no longer required, the caller should free any releasable memory by calling <code>cap_free</code>() with <i>cap_t</i> as an argument. The function returns an error if it cannot parse the contents of the string pointed to by <i>buf_p</i> or does not recognize any <i>capability_name</i> or flag character as valid. The function also returns an error if any flag is both set and cleared within a single clause. </p>
<p> <code>cap_to_text</code>() converts the capability state in working storage identified by <i>cap_p</i> into a nul-terminated human-readable string. This function allocates any memory necessary to contain the string, and returns a pointer to the string. If the pointer <i>len_p</i> is not NULL, the function shall also return the full length of the string (not including the nul terminator) in the location pointed to by <i>len_p</i>. The capability state in working storage, identified by <i>cap_p</i>, is completely represented in the character string. When the capability state in working storage is no longer required, the caller should free any releasable memory by calling <code>cap_free</code>() with the returned string pointer as an argument. </p>
<p> <code>cap_from_name</code>() converts a text representation of a capability, such as &quot;cap_chown&quot;, to its numerical representation (<code>CAP_CHOWN=0</code>), writing the decoded value into <i>*cap_p</i>. If <i>cap_p</i> is NULL no result is written, but the return code of the function indicates whether or not the specified capability can be represented by the library. </p>
<p> <code>cap_to_name</code>() converts a capability index value, <i>cap</i>, to a libcap-allocated textual string. This string should be deallocated with <code>cap_free</code>().</p>
<h2>TEXTUAL REPRESENTATION</h2>
<p> A textual representation of capability sets consists of one or more whitespace-separated <i>clauses</i>. Each clause specifies some operations on a capability set; the set starts out with all capabilities lowered, and the meaning of the string is the state of the capability set after all the clauses have been applied in order. </p>
<p> Each clause consists of a list of comma-separated capability names (or the word `<code>all</code>&#8216;), followed by an <i>action-list</i>. An action-list consists of a sequence of <i>operator flag</i> pairs. Legal operators are: `<code>=</code>&#8216;, &#8216;<code>+</code>&#8216;, and `<code>&#8211;</code>&#8216;. Legal flags are: `<code>e</code>&#8216;, `<code>i</code>&#8216;, and `<code>p</code>&#8216;. These flags are case-sensitive and specify the Effective, Inheritable and Permitted sets respectively. </p>
<p> In the capability name lists, all names are case-insensitive. The special name `<code>all</code>&#8216; specifies all capabilities; it is equivalent to a list naming every capability individually. </p>
<p> Unnamed capabilities can also be specified by number. This feature ensures that libcap can support capabilities that were not allocated at the time libcap was compiled. However, generally upgrading libcap will add names for recently allocated capabilities. </p>
<p> The `<code>=</code>&#8216; operator indicates that the listed capabilities are first reset in all three capability sets. The subsequent flags (which are optional when associated with this operator) indicate that the listed capabilities for the corresponding set are to be raised. For example: &quot;all=p&quot; means lower every capability in the Effective and Inheritable sets but raise all of the Permitted capabilities; or, &quot;cap_fowner=ep&quot; means raise the Effective and Permitted override-file-ownership capability, while lowering this Inheritable capability. </p>
<p> In the case that the leading operator is `<code>=</code>&#8216;, and no list of capabilities is provided, the action-list is assumed to refer to `all&#8217; capabilities. For example, the following three clauses are equivalent to each other (and indicate a completely empty capability set): &quot;all=&quot;; &quot;=&quot;; &quot;cap_chown,&lt;every-other-capability&gt;=&quot;. </p>
<p> The operators, `+&#8217; and `-&#8216; both require an explicit preceding capability list and one or more explicit trailing flags. The `+&#8217; operator will raise all of the listed capabilities in the flagged capability sets. The `-&#8216; operator will lower all of the listed capabilities in the flagged capability sets. For example: &quot;all+p&quot; will raise all of the Permitted capabilities; &quot;cap_fowner+p-i&quot; will raise the override-file-ownership capability in the Permitted capability set and lower this Inheritable capability; &quot;cap_fowner+pe-i&quot; and &quot;cap_fowner=+pe&quot; are equivalent.</p>
<h2>RETURN VALUE</h2>
<p> <code>cap_from_text</code>(), <code>cap_to_text</code>() and <code>cap_to_name</code>() return a non-NULL value on success, and NULL on failure. <code>cap_from_name</code>() returns 0 for success, and -1 on failure (unknown capability). </p>
<p> On failure, <i>errno</i> is set to <code>EINVAL</code>, or <code>ENOMEM</code>.</p>
<h2>CONFORMING TO</h2>
<p> <code>cap_from_text</code>() and <code>cap_to_text</code>() are specified by the withdrawn POSIX.1e draft specification. <code>cap_from_name</code>() and <code>cap_to_name</code>() are Linux extensions.</p>
<h2>EXAMPLE</h2>
<p> The example program below demonstrates the use of <code>cap_from_text</code>() and <code>cap_to_text</code>(). The following shell session shows a some example runs: </p>
<pre>
$ ./a.out &quot;cap_chown=p cap_chown+e&quot;
caps_to_text() returned &quot;= cap_chown+ep&quot;
$ ./a.out &quot;all=pe cap_chown-e cap_kill-pe&quot;
caps_to_text() returned &quot;=ep cap_chown-e cap_kill-ep&quot;
</pre>
<p> The source code of the program is as follows: </p>
<pre><code>
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;sys/capability.h&gt;
#define handle_error(msg)   \
    do {                    \
        perror(msg);        \
        exit(EXIT_FAILURE); \
    } while (0)
int main(int argc, char *argv[])
{
    cap_t caps;
    char *txt_caps;
    if (argc != 2) {
        fprintf(stderr, "%s &lt;textual-cap-set&gt;
", argv[0]);
        exit(EXIT_FAILURE);
    }
    caps = cap_from_text(argv[1]);
    if (caps == NULL)
        handle_error("cap_from_text");
    txt_caps = cap_to_text(caps, NULL);
    if (txt_caps == NULL)
        handle_error("cap_to_text");
    printf("caps_to_text() returned \"%s\"
", txt_caps);
    if (cap_free(txt_caps) != 0 || cap_free(caps) != 0)
        handle_error("cap_free");
    exit(EXIT_SUCCESS);
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/3-cap_clear/">cap_clear</a></code>(3), <code><a href="/docs/linux/man/3-cap_compare/">cap_compare</a></code>(3), <code><a href="/docs/linux/man/3-cap_copy_ext/">cap_copy_ext</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Index</h2>
