---
title: "acheck-rules(5)"
name: "acheck-rules"
section: "5"
letter: "a"
url: "/docs/linux/man/5-acheck-rules/"
description: "set.rules – Rules set for acheck"
---

<p>set.rules &#8211; Rules set for acheck</p>
<h2>Description</h2>
<p>Rules set files contain rules to be check by acheck. </p>
<p> Lines beginning with a number sign (`<code>#</code>&#8216;) and empty lines will be ignored. Spaces at the beginning and the end of a line will also be ignored as well as tabulators. If you need spaces at the end or the beginning of a value you can use apostrophes (`<code>&quot;</code>&#8216;). A comment starts with the number sign, there can be any number of spaces and/or tab stops in front of the #. Long lines can be broken into multiple lines ending with a backslash (`<code>\</code>&#8216;). Some possible examples: </p>
<pre> # this line is ignored
 field value
 field value # this is a comment
 field &quot;value ending with space &quot;
 field value\
 continuing on the next line</pre>
<p>You have to escape number signs with a backslash to use it in a value and use apostrophes if a value ends with a backslash. </p>
<p> Rule sets are made of lists of rules. Theses lists can be repeated a number of times, until or while a condition happens. </p>
<p> A rule detects an error if the corresponding test succeeds and none of its validation tests does. Each rule can then produce some fixes, a warning or an error, and provide hints to help the operator to correct the error. </p>
<p> Parts of the text can be set as comments and so no rule and no spell check will be performed on them.</p>
<h2>Rule File Syntax</h2>
<h2>Syntax Rules</h2>
<h2>list</h2>
<p>A list starts at a `<i>list</i>&#8216; statement, and stops at the first `<i>end_list</i>&#8216; or at the end of the file. </p>
<p> Mandatory fields:</p>
<dl>
<dt><i>type</i> type</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>until</i>, perform the list until the current line matches `<i>test</i>&#8216;</p>
<dd>
<dt><i>while</i>, perform the lint while the current line matches `<i>test</i>&#8216;</p>
<dd>
<dt><i>loop</i>, perform the list `<i>test</i>&#8216; times</p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><i>test</i> regex / number</p>
<dd>A regex for `<i>until</i>&#8216; and `<i>while</i>&#8216; lists. The number of times the list must be performed for `<i>loop</i>&#8216;, or `<i>0</i>&#8216; for infinite loop.</dl>
<p> Optional fields:</p>
<dl>
<dt><i>name</i> name</p>
<dd>Use this to give the list a name.</p>
<dt><i>spell</i> yes / no</p>
<dd>Set it to `<i>yes</i>&#8216; (default) or `<i>no</i>&#8216;, if you want or don&#8217;t want spelling to be checked in the lines matching this list. This value will be inherited by the nested lists.</dl>
<p> Sub-rules:</p>
<dl>
<dt><i>list</i> [name]</p>
<dd>
<dt><i>rule</i> [name]</p>
<dd>
<dt><i>comment</i> [name]</p>
<dd>Followed by the name of the sub-rule or its definition for an anonymous sub-rule.</dl>
<h2>rule</h2>
<p>A rule starts at a `<i>rule</i>&#8216; statement, and stops at the first `<i>end_rule</i>&#8216; or at the beginning of a comment or a list. </p>
<p> Mandatory fields:</p>
<dl>
<dt><i>type</i> type</p>
<dd>
<dl>
<dd>
<dl>
<dt><i>fix</i>, rule provides fixes and hints thought a menu</p>
<dd>
<dt><i>autofix</i>, rule fixes the mistake with no interaction</p>
<dd>
<dt><i>warning</i>, rule issues a warning</p>
<dd>
<dt><i>error</i>, rule issues an error</p>
<dd>
<dt><i>nop</i>, special rule that do nothing, no other field is required</p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><i>regex</i> regex</p>
<dd>The regex to be match to found this error. Patterns can be captures and then used in the `<i>fix</i>&#8216; expression.</p>
<dt><i>fix</i> expr</p>
<dd>Provides a correction for the rule, this field can be repeated to provides more than one choice. Only the first one will be used for `<i>autofix</i>&#8216; rules. `<i>warning</i>&#8216; and `<i>error</i>&#8216; do not provides fixes. The captured patterns can be used here with variables `<i></i>$1<i></i>&#8216;, `<i></i>$2<i></i>&#8216;, and so on.</p>
<dt><i>hint</i> text</p>
<dd>Provides some explanations, this will be used as reviewer comments in review mode.</dl>
<p> Optional fields:</p>
<dl>
<dt><i>name</i> name</p>
<dd>Use this to give the rule a name.</p>
<dt><i>valid</i> [name]</p>
<dd>Provides a validation test, it can be named or anonymous. For anonymous validation, the test definition must follow. This field can be repeated more than once, if any of the validation test succeed, the rule does not apply.</dl>
<h2>valid</h2>
<p>A validation test starts at a `<i>valid</i>&#8216; statement, and stops at the first `<i>end_valid</i>&#8216; or at the beginning of a rule, a comment, a list or another validation test. </p>
<p> Mandatory field:</p>
<dl>
<dt><i>pre</i> regex</p>
<dd>
<dt><i>in</i> regex&gt;</p>
<dd>
<dt><i>post</i> regex</p>
<dd>Try the regex before, in or after the match of the regex rule. At least one of these test must be provided. If all tests are successful, the rule won&#8217;t apply.</dl>
<p> Optional field:</p>
<dl>
<dt><i>name</i> name</p>
<dd>Use this to give the validation test a name.</dl>
<h2>comment</h2>
<p>A comment starts at a `<i>comment</i>&#8216; statement, and stops at the first `<i>end_comment</i>&#8216; or at the beginning of a rule, a comment or a list. </p>
<p> Comments are just skipped, no other rule and no spelling are performed on them. </p>
<p> Mandatory field:</p>
<dl>
<dt><i>skip</i> regex</p>
<dd>A regex matching the text of the comment. Do not use `<i>start</i>&#8216; and `<i>stop</i>&#8216; with this.</p>
<dt><i>start</i> regex</p>
<dd>
<dt><i>stop</i> regex</p>
<dd>Regexs defining the beginning and the end of the comment, all the text between will be considered as comment. Do not use `<i>skip</i>&#8216; with this.</dl>
<p> Optional fields:</p>
<dl>
<dt><i>name</i> name</p>
<dd>Use this to give the comment a name.</p>
<dt><i>start_offset</i></p>
<dd>
<dt><i>stop_offset</i></p>
<dd>Defines where the comment really starts or end. Values are `<i>s</i>&#8216; for the place the match starts, `<i>s+&lt;n&gt;</i>&#8216; for <i>n</i> characters after the match starts, `<i>e</i>&#8216; for the place the match ends, or `<i>e-&lt;n&gt;</i>&#8216; for <i>n</i> characters before the match ends. Defaults are `<i>s</i>&#8216; for `<i>start</i>&#8216; matches and `<i>e</i>&#8216; for `<i>stop</i>&#8216; matches.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-acheck/">acheck</a></i>(1), <i><a href="/docs/linux/man/5-acheck/">acheck</a></i>(5)</p>
<h2>Author</h2>
<p>Nicolas Bertolissio &lt;nico.bertol [at] free.fr&gt;</p>
