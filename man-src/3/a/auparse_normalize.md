---
title: "auparse_normalize(3)"
name: "auparse_normalize"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_normalize/"
description: "auparse_normalize – normalize the current event"
---

<h2>NAME</h2>
<p> auparse_normalize &#8211; normalize the current event</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> <code>int auparse_normalize(auparse_state_t *au, normalize_option_t opt);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>auparse_normalize</code> analyzes the current event so that the important information about the event can be accessed through a normalized API which positions to internal field cursor to the exact record and field when asked about specific information. </p>
<p> The auparse_normalize function takes an opt argument to tell it how much information to gather. Legal values are: </p>
<pre>
        NORM_OPT_ALL - gather maximum information
        NORM_OPT_NO_ATTRS - do not gather subject/object attribute information
</pre>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success and 1 on error. </p>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
