---
title: "tpage(1)"
name: "tpage"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tpage/"
description: "Template::Tools::tpage – Process templates from command line"
---

<h2 class="name">NAME</h2>
<p> Template::Tools::tpage &#8211; Process templates from command line </p>
<h2>USAGE</h2>
<pre><code>
tpage[--define var = value] file(s)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>tpage</code> script is a simple wrapper around the Template Toolkit processor. Files specified by name on the command line are processed in turn by the template processor and the resulting output is sent to <font SIZE="-1">STDOUT</font> and can be redirected accordingly. e.g. </p>
<pre>
    tpage myfile &gt; myfile.out
    tpage header myfile footer &gt; myfile.html
</pre>
<p> If no file names are specified on the command line then <code>tpage</code> will read <font SIZE="-1">STDIN</font> for input. </p>
<p> The <tt>&quot;--define&quot;</tt> option can be used to set the values of template variables. e.g. </p>
<pre>
    tpage --define author=&quot;Andy Wardley&quot; skeleton.pm &gt; MyModule.pm
</pre>
<p> See Template for general information about the Perl Template Toolkit and the template language and features.</p>
<h2>AUTHOR</h2>
<p> Andy Wardley &lt;abw [at] wardley.org&gt; </p>
<p> &lt;<a rel="nofollow" href="http://wardley.org/">http://wardley.org/</a>&gt;</p>
<h2>VERSION</h2>
<p> 2.68, distributed as part of the Template Toolkit version 2.19, released on 27 April 2007.</p>
<h2>COPYRIGHT</h2>
<pre>
  Copyright (C) 1996-2007 Andy Wardley.  All Rights Reserved.
</pre>
<p> This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself.</p>
<h2>SEE ALSO</h2>
<p> ttree </p>
<h2>Index</h2>
