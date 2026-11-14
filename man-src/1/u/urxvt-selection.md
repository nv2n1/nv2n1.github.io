---
title: "urxvt-selection(1)"
name: "urxvt-selection"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-selection/"
---

<h2 class="name">NAME</h2>
 

 selection - more intelligent selection (enabled by default) 

<h2>DESCRIPTION</h2>

 This extension tries to be more intelligent when the user extends selections (double-click and further clicks). Right now, it tries to select words, urls and complete shell-quoted arguments, which is very convenient, too, if your <i>ls</i> supports <tt>&quot;--quoting-style=shell&quot;</tt>. 

 A double-click usually selects the word under the cursor, further clicks will enlarge the selection. 

 The selection works by trying to match a number of regexes and displaying them in increasing order of length. You can add your own regexes by specifying resources of the form: 

 <pre>
   URxvt.selection.pattern-0: perl-regex
   URxvt.selection.pattern-1: perl-regex
   ...
</pre> 

 The index number (0, 1...) must not have any holes, and each regex must contain at least one pair of capturing parentheses, which will be used for the match. For example, the following adds a regex that matches everything between two vertical bars: 

 <pre>
   URxvt.selection.pattern-0: \\|([^|]+)\\|
</pre> 

 Another example: Programs I use often output ``absolute path: '' at the beginning of a line when they process multiple files. The following pattern matches the filename (note, there is a single space at the very end): 

 <pre>
   URxvt.selection.pattern-0: ^(/[^:]+):\
</pre> 

 You can look at the source of the selection extension to see more interesting uses, such as parsing a line from beginning to end. 

 This extension also offers the following actions:
<dl>
<dt>rot13
<dd> Rot-13 the selection when activated. 

 Example: 

 <pre>
   URxvt.keysym.C-M-r: selection:rot13
</pre> 

</dl>

<h2>Index</h2>


