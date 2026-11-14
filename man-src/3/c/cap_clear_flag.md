---
title: "cap_clear_flag(3)"
name: "cap_clear_flag"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cap_clear_flag/"
description: "cap_clear, cap_clear_flag, cap_get_flag, cap_set_flag, cap_compare – capability data object manipulation"
---

<h2>NAME</h2>
<p> cap_clear, cap_clear_flag, cap_get_flag, cap_set_flag, cap_compare &#8211; capability data object manipulation</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/capability.h&gt;
int cap_clear(cap_t cap_p);
int cap_clear_flag(cap_t cap_p, cap_flag_t flag);
int cap_get_flag(cap_t cap_p, cap_value_t cap,
                 cap_flag_t flag, cap_flag_value_t *value_p);
int cap_set_flag(cap_t cap_p, cap_flag_t flag, int ncap,
                 const cap_value_t *caps, cap_flag_value_t value);
int cap_compare(cap_t cap_a, cap_t cap_b);
Link with - lcap.
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions work on a capability state held in working storage. A <i>cap_t</i> holds information about the capabilities in each of the three sets, Permitted, Inheritable, and Effective. Each capability in a set may be clear (disabled, 0) or set (enabled, 1). </p>
<p> These functions work with the following data types:</p>
<dl>
<dt><i>cap_value_t</i></p>
<dd> identifies a capability, such as <code>CAP_CHOWN</code>.</p>
<dt><i>cap_flag_t</i></p>
<dd> identifies one of the three flags associated with a capability (i.e., it identifies one of the three capability sets). Valid values for this type are <code>CAP_EFFECTIVE</code>, <code>CAP_INHERITABLE</code> or <code>CAP_PERMITTED</code>.</p>
<dt><i>cap_flag_value_t</i></p>
<dd> identifies the setting of a particular capability flag (i.e, the value of a capability in a set). Valid values for this type are <code>CAP_CLEAR</code> (0) or <code>CAP_SET</code> (1).</dl>
<p> <code>cap_clear</code>() initializes the capability state in working storage identified by <i>cap_p</i> so that all capability flags are cleared. </p>
<p> <code>cap_clear_flag</code>() clears all of the capabilities of the specified capability flag, <i>flag</i>. </p>
<p> <code>cap_get_flag</code>() obtains the current value of the capability flag, <i>flag</i>, of the capability, <i>cap</i>, from the capability state identified by <i>cap_p</i> and places it in the location pointed to by <i>value_p</i>. </p>
<p> <code>cap_set_flag</code>() sets the flag, <i>flag</i>, of each capability in the array <i>caps</i> in the capability state identified by <i>cap_p</i> to <i>value</i>. The argument, <i>ncap</i>, is used to specify the number of capabilities in the array, <i>caps</i>. </p>
<p> <code>cap_compare</code>() compares two full capability sets and, in the spirit of <code>memcmp</code>(), returns zero if the two capability sets are identical. A positive return value, <code>status</code>, indicates there is a difference between them. The returned value carries further information about which of three sets, <i>cap_flag_t</i> <code>flag</code>, differ. Specifically, the macro <code>CAP_DIFFERS</code> (<i>status</i>, <i>flag</i>) evaluates to non-zero if the returned status differs in its <i>flag</i> components.</p>
<h2>RETURN VALUE</h2>
<p> <code>cap_clear</code>(), <code>cap_clear_flag</code>(), <code>cap_get_flag</code>() <code>cap_set_flag</code>() and <code>cap_compare</code>() return zero on success, and -1 on failure. Other return values for <code>cap_compare</code>() are described above. </p>
<p> On failure, <i>errno</i> is set to <code>EINVAL</code>, indicating that one of the arguments is invalid.</p>
<h2>CONFORMING TO</h2>
<p> These functions are as per the withdrawn POSIX.1e draft specification. <code>cap_clear_flag</code>() and <code>cap_compare</code>() are Linux extensions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libcap/">libcap</a></code>(3), <code><a href="/docs/linux/man/3-cap_copy_ext/">cap_copy_ext</a></code>(3), <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_proc/">cap_get_proc</a></code>(3), <code><a href="/docs/linux/man/3-cap_init/">cap_init</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7) </p>
<h2>Index</h2>
