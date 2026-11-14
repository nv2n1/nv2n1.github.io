---
title: "adime_va_end(3)"
name: "adime_va_end"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_va_end/"
description: "adime_va_list, adime_va_start, adime_va_arg, adime_va_end"
---

<h2>NAME</h2>
<p> adime_va_list, adime_va_start, adime_va_arg, adime_va_end</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>typedef adime_va_list;</code> </p>
<p> <code>void adime_va_start(adime_va_list ap, first_arg);</code> </p>
<p> <code>TYPE adime_va_arg(adime_va_list ap, TYPE);</code> </p>
<p> <code>void adime_va_end(adime_va_list ap);</code></p>
<h2>DESCRIPTION</h2>
<p> Because of weirdnesses in the C language, some things that Adime does with va_lists would not be portable if it used a va_list directly. Instead you always have to use this replacement API, which works exactly like the standard API for va_lists, but is more portable. Also, if you pass an `adime_va_list&#8217; to another function, which reads an argument with `adime_va_arg()&#8217;, then the `adime_va_list&#8217; will have advanced to the same position in the calling function as in the called function. In particular, after calling `adime_vdialogf()&#8217;, the `adime_va_list&#8217; will have advanced to after the last argument used by Adime. </p>
<p> The following example shows how `adime_dialogf()&#8217; is implemented in terms of `adime_vdialogf()&#8217;: </p>
<pre><code>
int adime_dialogf(char *title, int x, int y, int edit_w,
                  char *format, ...)
{
    int ret;
    va_list ap;

    va_start(ap, format);
    ret = adime_vdialogf(title, x, y, edit_w, format, ap);
    va_end(ap);

    return ret;
}
</code></pre>
<p> See documentation for the standard `va_list&#8217;, `va_start()&#8217;, `va_arg()&#8217; and `va_end()&#8217; for more information. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_vdialogf/">adime_vdialogf</a></code>(3), <code><a href="/docs/linux/man/3-adime_dialogf/">adime_dialogf</a></code>(3), <code><a href="/docs/linux/man/3-adime_lowlevel_vdialogf/">adime_lowlevel_vdialogf</a></code>(3) </p>
<h2>Index</h2>
