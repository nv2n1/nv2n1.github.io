---
title: "urxvt256c-ml-selection-autotransform(1)"
name: "urxvt256c-ml-selection-autotransform"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-ml-selection-autotransform/"
---

<h2 class="name">NAME</h2>
 

 selection-autotransform - automatically transform select text 

<h2>DESCRIPTION</h2>

 This selection allows you to do automatic transforms on a selection whenever a selection is made. 

 It works by specifying perl snippets (most useful is a single <tt>&quot;s///&quot;</tt> operator) that modify <tt>$_</tt> as resources: 

 <pre>
   URxvt.selection-autotransform.0: transform
   URxvt.selection-autotransform.1: transform
   ...
</pre> 

 For example, the following will transform selections of the form <tt>&quot;filename:number&quot;</tt>, often seen in compiler messages, into <tt>&quot;vi +$filename $word&quot;</tt>: 

 <pre><code>
URxvt.selection - autotransform .0 : s / ^([^:[:space:]] +)
    : (\\d +)
    :
    ? $ / vi + $2 \\Q$1\\E\\x0d /
</code></pre> 

 And this example matches the same,but replaces it with vi-commands you can paste directly into your (vi :) editor: 

 
   URxvt.selection-autotransform.0: s/^([^:[:space:]]+(\\d+):?$/:e \\Q$1\\E\\x0d:$2\\x0d/
 

 Of course, this can be modified to suit your needs and your editor :) 

 To expand the example above to typical perl error messages (``<font SIZE="-1">XXX</font> at <font SIZE="-1">FILENAME</font> line <font SIZE="-1">YYY.''</font>), you need a slightly more elaborate solution: 

 <pre><code>
   URxvt.selection.pattern-0: ( at .*? line \\d+[,.])
   URxvt.selection-autotransform.0: s/^ at (.*?) line (\\d+)[,.]$/:e \\Q$1\E\\x0d:$2\\x0d/
</code></pre> 

 The first line tells the selection code to treat the unchanging part of every error message as a selection pattern, and the second line transforms the message into vi commands to load the file. 

<h2>Index</h2>


