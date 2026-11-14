---
title: "clipjoin(1)"
name: "clipjoin"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clipjoin/"
---

<h2 class="name">NAME</h2>
 

 clipjoin - Remove superfluous spaces from the clipboard. 

<h2>MOTIVATION</h2>

 Often you'll copy some stuff, like this: 

 <pre>
  &lt;ingy&gt; hey rking, you should use YBFOD: <a rel="nofollow" HREF="http://search.cpan">http://search.cpan</a>
    | .org/~ingy/Acme-YBFOD-0.11/
</pre> 

 Getting that <font SIZE="-1">URL</font> to a browser is tedious. 

 Another <font SIZE="-1">IRC</font> example is longer quotes: 

 <pre>
  &lt;strunk&gt; Objective consideration of contemporary phenomena compels the
      conclusion that success or failure in competitive activities
      exhibits no tendency to be commensurate with enate capacity but
      that a considerable element of the unpredictable must invariably
      be taken into account. I returned, and saw under the sun, that the
      race is not to the swift, nor the battle to the strong, neither
      yet bread to the wise, nor yet riches to men of understanding, nor
      yet favour to men of skill, but time and chance happeneth to them all.
</pre> 

 If you wanted to quote that to someone, you'd have \n's and `` '''s everywhere, unless you ran ``clipjoin'' first. 

 An example from mutt: 

 ,-------------------------------------------. | xterm (X) | +-------------------------------------------+ | <a rel="nofollow" HREF="http://www.thisisalink.com/that/wrapped/ar|">http://www.thisisalink.com/that/wrapped/ar|</a> |+ound/a/line/and/its/a/pain/without/the/joi| |+inclip/script | `-------------------------------------------' 

 Becomes: <a rel="nofollow" HREF="http://www.thisisalink.com/that/wrapped/around/a/line/and/its/a/pain/without/the/clipjoin/script">http://www.thisisalink.com/that/wrapped/around/a/line/and/its/a/pain/without/the/clipjoin/script</a>

<h2>AUTHOR</h2>

 Ryan King &lt;rking [at] panoptic.com&gt;

<h2>COPYRIGHT</h2>

 Copyright (c) 2010. Ryan King. All rights reserved. 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

 See &lt;<a rel="nofollow" HREF="http://www.perl.com/perl/misc/Artistic.html">http://www.perl.com/perl/misc/Artistic.html</a>&gt; 

<h2>Index</h2>


