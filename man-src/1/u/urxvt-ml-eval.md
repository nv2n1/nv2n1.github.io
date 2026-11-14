---
title: "urxvt-ml-eval(1)"
name: "urxvt-ml-eval"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-ml-eval/"
description: "eval – evaluate arbitrary perl code using actions"
---

<h2 class="name">NAME</h2>
<p> eval &#8211; evaluate arbitrary perl code using actions </p>
<h2>EXAMPLES</h2>
<pre>
  URxvt.keysym.M-c: eval:selection_to_clipboard
  URxvt.keysym.M-v: eval:paste_clipboard
  URxvt.keysym.M-V: eval:paste_primary
  URxvt.keysym.M-Up: eval:scroll_up 1
  URxvt.keysym.M-Down: eval:scroll_down 1
  URxvt.keysym.M-Home: eval:scroll_to_top
  URxvt.keysym.M-End:  eval:scroll_to_bottom
</pre>
<h2>DESCRIPTION</h2>
<p> Add support for evaluating arbitrary perl code using actions in keysym resources. If a keysym <i>action</i> takes the form <tt>&quot;eval:STRING&quot;</tt>, the specified <font SIZE="-1"><code>STRING</code></font> is evaluated as a Perl expression. While the full urxvt <font SIZE="-1">API</font> is available, the following methods are also provided for users&#8217; convenience, as they implement basic actions:</p>
<dl>
<dt>scroll_up $count</p>
<dd>
<dt>scroll_up_pages $count</p>
<dd>
<dt>scroll_down $count</p>
<dd>
<dt>scroll_down_pages $count</p>
<dd> Scroll up or down by <tt>$count</tt> lines or pages.</p>
<dt>scroll_to_top</p>
<dd>
<dt>scroll_to_bottom</p>
<dd> Scroll to the top or bottom of the scrollback.</p>
<dt>selection_to_clipboard</p>
<dd> Copy the selection to the <font SIZE="-1">CLIPBOARD.</font></p>
<dt>paste_primary</p>
<dd>
<dt>paste_clipboard</p>
<dd> Paste the value of the <font SIZE="-1">PRIMARY</font> or <font SIZE="-1">CLIPBOARD</font> selection. </p>
</dl>
<h2>Index</h2>
