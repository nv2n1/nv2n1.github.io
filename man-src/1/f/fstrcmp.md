---
title: "fstrcmp(1)"
name: "fstrcmp"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fstrcmp/"
description: "fstrcmp – fuzzy comparison of strings"
---

<h2>NAME</h2>
<p> fstrcmp &#8211; fuzzy comparison of strings</p>
<h2>SYNOPSIS</h2>
<p> <code>fstrcmp</code> [ <code>-p</code> ] <i>first-string</i> <i>second-string</i> </p>
<p> <code>fstrcmp</code> <code>-w</code> <i>first-string</i> <i>second-string</i> </p>
<p> <code>fstrcmp</code> <code>-a</code> <i>first-file</i> <i>second-file</i> </p>
<p> <code>fstrcmp</code> <code>-s</code> <i>needle</i> <i>haystack</i>&#8230; </p>
<p> <code>fstrcmp</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> The fstrcmp command is used to make fuzzy comparisons between strings. The &#8220;edit distance&#8221; between the strings is printed, with 0.0 meaning the strings are utterly un-alike, and 1.0 meaning the strings are identical. </p>
<p> You may need to quote the string to insulate them from the shell.</p>
<h2>OPTIONS</h2>
<p> The fstrcmp command understands the following options:</p>
<dl>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;files-as-bytes</code></p>
<dd> This option is used to compare two files as arrays of bytes. See <a href="/docs/linux/man/3-fmemcmp/">fmemcmp</a>(3) for more information.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;pair</code></p>
<dd> This option is used to compare two strings as arrays of bytes. This is the default. See <a href="/docs/linux/man/3-fstrcmp/">fstrcmp</a>(3) for more information.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;select</code></p>
<dd> This option is used to select the closest <i>needle</i> from the provided <i>haystack</i> alternatives. The most similar (single) choice is printed. If none are particularly similar, nothing is printed. See <a href="/docs/linux/man/3-fstrcmp/">fstrcmp</a>(3) for more information. See below for example.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> This option may be used to print the version of the fstrcmp command, and then exit.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;wide-pair</code></p>
<dd> This option is used to compare two multi-byte character strings. See <a href="/docs/linux/man/3-fstrcoll/">fstrcoll</a>(3) for more information.</dl>
<h2>EXIT STATUS</h2>
<p> The fstrcmp command exits with status 1 on any error. The fstrcmp command only exits with status 0 if there are no errors.</p>
<h2>EXAMPLE</h2>
<p> The <i>fstrcmp &#8211;select</i> option may be used in a shell script to improve error messages.</p>
<dl>
<dt>
<dd>
<pre><code>
case "$action" in
start)
    start
    ;;
stop)
    stop
    ;;
restart)
    stop
    start
    ;;
*)
    echo "$0: action \"$action\" unknown" 1&gt;&amp;2
    guess=`fstrcmp --select "$action" stop start restart`
    if [ "$guess" ]
    then
        echo "$0: did you mean \"$guess\" instead?" 1&gt;&amp;2
    fi
    exit 1
    ;;
esac
</code></pre>
</dl>
<p> Thus, the error message frequently suggests the correct action in the face of simple finger problems on the command line.</p>
<h2>SEE ALSO</h2>
<dl>
<dt><a href="/docs/linux/man/3-fstrcmp/">fstrcmp</a>(3)</p>
<dd> fuzzy comparison of strings</p>
<dt><a href="/docs/linux/man/3-fstrcoll/">fstrcoll</a>(3)</p>
<dd> fuzzy comparison of two multi-byte character strings</p>
<dt><a href="/docs/linux/man/3-fstrcmpi/">fstrcmpi</a>(3)</p>
<dd> fuzzy comparison of strings, integer variation</dl>
<h2>COPYRIGHT</h2>
<p> fstrcmp version 0.7<br />
 Copyright (C) 2009 Peter Miller<br />
 Peter Miller &lt;pmiller [at] opensource.org.au&gt; </p>
<p> The comparison code is derived from the fuzzy comparison functions in GNU Gettext 0.17. The GNU Gettext comparison functions were, in turn, derived from GNU Diff 2.7. </p>
<p> Copyright (C) 1988-2009 Free Software Foundation </p>
<h2>Index</h2>
