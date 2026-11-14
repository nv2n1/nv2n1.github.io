---
title: "getsubopt(3)"
name: "getsubopt"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getsubopt/"
description: "getsubopt – parse suboption arguments from a string"
---

<h2 class="name">NAME</h2>
<p> getsubopt &#8211; parse suboption arguments from a string </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;stdlib.h&gt;</code> </p>
<p> <code>int getsubopt(char **optionp</code><i>, char * const *</i><code>tokens</code><i>, char **</i><code>valuep</code><i>);</i> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getsubopt</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;= 500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dl>
<h2>DESCRIPTION</h2>
<p> <code>getsubopt</code>() parses the list of comma-separated suboptions provided in <i>optionp</i>. (Such a suboption list is typically produced when <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) is used to parse a command line; see for example the <i>-o</i> option of <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8).) Each suboption may include an associated value, which is separated from the suboption name by an equal sign. The following is an example of the kind of string that might be passed in <i>optionp</i>: </p>
<p> <code>ro,name=xyz</code> </p>
<p> The <i>tokens</i> argument is a pointer to a NULL-terminated array of pointers to the tokens that <code>getsubopt</code>() will look for in <i>optionp</i>. The tokens should be distinct, null-terminated strings containing at least one character, with no embedded equal signs or commas. </p>
<p> Each call to <code>getsubopt</code>() returns information about the next unprocessed suboption in <i>optionp</i>. The first equal sign in a suboption (if any) is interpreted as a separator between the name and the value of that suboption. The value extends to the next comma, or (for the last suboption) to the end of the string. If the name of the suboption matches a known name from <i>tokens</i>, and a value string was found, <code>getsubopt</code>() sets <i>*valuep</i> to the address of that string. The first comma in <i>optionp</i> is overwritten with a null byte, so <i>*valuep</i> is precisely the &quot;value string&quot; for that suboption. </p>
<p> If the suboption is recognized, but no value string was found, <i>*valuep</i> is set to NULL. </p>
<p> When <code>getsubopt</code>() returns, <i>optionp</i> points to the next suboption, or to the null byte (&#8216;
