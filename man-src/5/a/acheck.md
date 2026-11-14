---
title: "acheck(5)"
name: "acheck"
section: "5"
letter: "a"
url: "/docs/linux/man/5-acheck/"
description: ".acheck – Acheck configuration file"
---

<p>.acheck &#8211; Acheck configuration file</p>
<h2>Description</h2>
<p>This is the configuration file for acheck. If it exists, it must be at the top of your home directory (<i></i>$HOME<i></i>). This file is optional unless you don&#8217;t want to use default values. Lines beginning with a number sign (`<code>#</code>&#8216;) and empty lines will be ignored. Spaces at the beginning and the end of a line will also be ignored as well as tabulators. If you need spaces at the end or the beginning of a value you can use apostrophes (`<code>&quot;</code>&#8216;). An option line starts with it&#8217;s name followed by a value. An equal sign is optional. A comment starts with the number sign, there can be any number of spaces and/or tab stops in front of the #. Some possible examples: </p>
<pre><code># this line is ignored
option   value
option = value                               # this is a comment
option        &quot;value ending with space   &quot;</code></pre>
<p> You have to escape number signs with a backslash (`<code>\</code>&#8216;) to use it in a value. Default values are provided into square brackets, they should be suitable for most installations.</p>
<h2>Spelling</h2>
<p>Define if you want to use ispell for checking spelling and how to use it.</p>
<dl>
<dt><i>check_spelling</i></p>
<dd>use Aspell for spelling if set to `<code>yes</code>&#8216; [yes]</p>
<dt><i>dictionary</i></p>
<dd>Language dictionary to use with Aspell, use default if empty [empty]</p>
<dt><i>word_letters</i></p>
<dd>regular expression to define characters allowed to write a word, pattern matches according locale [\w]</p>
<dt><i>$review_mode</i></p>
<dd>set to `<code>yes</code>&#8216; if you want review comments to be added in the output file after parsed line, otherwise just fix error [no]</dl>
<h2>Colors</h2>
<p>Set text colors for clear presentation. </p>
<p> The recognized colors (all of which should be fairly intuitive) are: <code>clear</code>, <code>reset</code>, <code>dark</code>, <code>bold</code>, <code>underline</code>, <code>underscore</code>, <code>blink</code>, <code>reverse</code>, <code>concealed</code>, <code>black</code>, <code>red</code>, <code>green</code>, <code>yellow</code>, <code>blue</code>, <code>magenta</code>, <code>cyan</code>, <code>white</code>, <code>on_black</code>, <code>on_red</code>, <code>on_green</code>, <code>on_yellow</code>, <code>on_blue</code>, <code>on_magenta</code>, <code>on_cyan</code>, and <code>on_white</code>. Case is not significant. Underline and underscore are equivalent, as are clear and reset, so use whichever is the most intuitive to you. The <i>color</i> alone sets the foreground color, and <i>on_color</i> sets the background color. </p>
<p> Note that not all colors are supported by all terminal types, and some terminals may not support any of these sequences. Dark, blink, and concealed in particular are frequently not implemented.</p>
<dl>
<dt><i>error_color</i></p>
<dd>color used to highlight errors, this should highlight space characters [bold on_red]</p>
<dt><i>fix_color</i></p>
<dd>color used to highlight suggestions, this should highlight space characters [bold on_green]</p>
<dt><i>error_head_color</i></p>
<dd>color used to display the error line header [bold red]</p>
<dt><i>error_color</i></p>
<dd>color used to display the suggestion line header [bold green]</p>
<dt><i>comment_color</i></p>
<dd>color used for comments and hints [cyan]</dl>
<h2>Others</h2>
<dl>
<dt><i>bak_ext</i></p>
<dd>extension for backup files [bak]</p>
<dt><i>comment</i></p>
<dd>comment string for review [&gt;&gt; ]</p>
<dt><i>debug</i></p>
<dd>verbosity level [0]</dl>
<p> Verbosity Levels:</p>
<dl>
<dt><i>0</i> quiet, normal</p>
<dd>only warnings and errors</p>
<dt><i>1</i> debug</p>
<dd>names of subroutines</p>
<dt><i>2</i> debug verbose</p>
<dd>names and arguments of subroutines</p>
<dt><i>3</i> .. <i>5</i> debug very verbose</p>
<dd>output parsing and checking details</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-acheck/">acheck</a></i>(1), <i><a href="/docs/linux/man/5-acheck-rules/">acheck-rules</a></i>(5)</p>
<h2>Author</h2>
<p>Nicolas Bertolissio &lt;bertol [at] debian.org&gt;</p>
