---
title: "clipbrowse(1)"
name: "clipbrowse"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clipbrowse/"
---

<h2 class="name">NAME</h2>
 

 clipbrowse - Load a URL from the clipboard into your browser. 

<h2>USAGE</h2>

 # ...copy something # (You might want to do a `clipjoin` if the <font SIZE="-1">URL</font> text is messy) $ clipbrowse 

 Remember that many browsers will usefully load things that don't look like <font SIZE="-1">URL</font>'s. For example Firefox does a Google ``I'm feeling lucky'' with non-URLs. This means you can have any text in your clipboard and `clipbrowse`.

<h2>MOTIVATION</h2>

 It saves a couple of seconds every time you run it. Chrome and Firefox, for examples, automatically create a new tab and loads the page when you invoke it from the command line. Already we've saved a Ctrl+T and a Shift+Insert. When you consider the parallelizing (that your browser will be actively loading the page while you're Alt+Tabbing to it), you've squeaked out a little more. 

 Maybe I'm just a freak, but I like shaving out wasted time like that.

<h2>CONFIGURATION</h2>

 The environment variable <tt>$BROWSER</tt> will override the default launching command. If you have a <tt>%s</tt> in the line, it will be replaced with the url. if not, the url will be appended at the end. 

 The default is `chromium-browser ``%s''` (Debian's Google Chrome) If you still use Firefox, consider: `firefox -remote ``openURL(%s,new-tab)'''`.

<h2>AUTHOR</h2>

 Ryan King &lt;rking [at] panoptic.com&gt; =head1 <font SIZE="-1">COPYRIGHT</font> 

 Copyright (c) 2010. Ryan King. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

 See &lt;<a rel="nofollow" HREF="http://www.perl.com/perl/misc/Artistic.html">http://www.perl.com/perl/misc/Artistic.html</a>&gt; 

<h2>Index</h2>


