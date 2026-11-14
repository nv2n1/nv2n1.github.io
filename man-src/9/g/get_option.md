---
title: "get_option(9)"
name: "get_option"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_option/"
---

get_option - Parse integer from an option string

<h2>Synopsis</h2>

<pre><code>int get_option(char **str, int *pint);</code></pre>

<h2>Arguments</h2>

<i>str</i>
<dl><dd><dd>option string</dl>
 

 <i>pint</i>
<dl><dd>(output) integer value parsed from <i>str</i></dl>

<h2>Description</h2>

Read an int from an option string; if available accept a subsequent comma as well. 

 Return values: 0 - no int in string 1 - int found, no subsequent comma 2 - int found including a subsequent comma 3 - hyphen found to denote a range

<h2>Copyright</h2>


