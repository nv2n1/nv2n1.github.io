---
title: "gstream-set_input_approver(3)"
name: "gstream-set_input_approver"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_input_approver/"
description: "set_input_approver"
---

<h2>NAME</h2>
<p> set_input_approver</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_input_approver(bool (*input_approver)(int));</code></p>
<h2>DESCRIPTION</h2>
<p> The function handed over will be called with every new character inputted and determines whether the character will be accepted by the inputter. If it returns true, the character is accepted and inserted in the input string, if false, the character is thrown away. </p>
<p> A short example: </p>
<pre><code>
bool ia_abc_is_what_we_want(int chr)
{
    if (chr == 'a' || chr == 'b' || chr == 'c')
        return true;
    else
        return false;
}

//...

gs.set_input_approver(ia_abc_is_what_we_want);
gs &gt;&gt; my_string; // the user is only able to input a, b or c
</code></pre>
<p> If you want to declare any variables of the type of the function, the typedef &#8216;input_approver&#8217; in &#8216;gbuf&#8217; makes it easy, e.g. </p>
<pre><code>
gbuf::input_approver tmp_ap;

//...

tmp_ap = gs1.get_input_approver();
gs1.set_input_approver(gs2.get_input_approver());
gs2.set_input_approver(tmp_ap);
</code></pre>
<p> Note that a default input string as entered by set_input_string is not checked by this function. The default approver is </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-save_input_approver/">gstream-save_input_approver</a></code>(3), <code><a href="/docs/linux/man/3-gstream-restore_input_approver/">gstream-restore_input_approver</a></code>(3), <code><a href="/docs/linux/man/3-gstream-get_input_approver/">gstream-get_input_approver</a></code>(3), <code><a href="/docs/linux/man/3-gstream-set_input_string/">gstream-set_input_string</a></code>(3), <code><a href="/docs/linux/man/3-gstream-ia_allow_everything/">gstream-ia_allow_everything</a></code>(3) </p>
<h2>Index</h2>
