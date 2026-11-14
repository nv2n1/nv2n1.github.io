---
title: "coverpg(1)"
name: "coverpg"
section: "1"
letter: "c"
url: "/docs/linux/man/1-coverpg/"
description: "make.coverpg – create a fax coverpg on stdout"
---

<h2 class="name">NAME</h2>
<p> make.coverpg &#8211; create a fax coverpg on stdout </p>
<h2>SYNOPSIS</h2>
<p> make.coverpg [options] &lt;pages&gt; &lt;sender-ID&gt; &lt;sender-NAME&gt; &lt;receiver-ID&gt; &lt;receiver-NAME&gt; &lt;date&gt; &lt;time&gt;</p>
<h2>DESCRIPTION</h2>
<p> <i>make.coverpg </i> is called from <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1) to generate a cover page for the just-processed fax. It has to create a proper G3 file (e.g. via <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1) or <a href="/docs/linux/man/1-hp2hig3/">hp2hig3</a>(1) or <a href="/docs/linux/man/1-ghostscript/">ghostscript</a>(1)) and output that on stdout. If the program doesn&#8217;t exist, or can&#8217;t be executed, the fax simply won&#8217;t get a coverpage (so, if you don&#8217;t want a fax coverpage, do not install it&#8230;) </p>
<p> <i>make.coverpg</i> can put anything it wants on the page, but note that there are certain legal requirements in certain countries about the contents that *have* to be on the cover page, for example, the fax phone number of the sender and the recepient, the number of pages, or similar things. </p>
<p> <i>make.coverpg</i> gets the informations about the fax to be sent from the command line, in the order listed above. </p>
<p> If the environment variable <i>normal_res</i> is set to something non-empty, <i>faxspool</i> requests that <i>make.coverpg</i> creates a cover page in normal resolution (98 lpi). Default is fine resolution (196 lpi). </p>
<p> <code>NO</code> <i>make.coverpg</i> program is installed by default, since everyones needs differ too wildly. </p>
<p> Some sample coverpage programs are provided in the mgetty source tree, in the samples/ subdirectory (coverpg.pbm shows how to do it with &quot;pbmtext|pbm2g3&quot;, coverpg.ps shows how I do it with ghostscript). </p>
<p> In this directory, you can also find two shell scripts (fax and faxmemo) that will take advantage of one more esoteric feature of my coverpage programs: if called with the option &quot;-m &lt;memo-file&gt;&quot;, the sample programs will put a text file &quot;&lt;memo-file&gt;&quot; on the cover page (used for short notes or such). To make use of it, <i>faxspool</i> is called with the option &#8216;-C &quot;make.coverpg -m &lt;memo-file&gt;&quot;&#8217; (the double quotes are needed!). </p>
<h2>OPTIONS</h2>
<dl>
<dt>none</p>
<dd>
</dl>
<h2>Example</h2>
<p> A five-page fax sent from me to my second number could result in a call like this: </p>
<p> make.coverpg 5 &quot;+49-89-3243328&quot; &quot;Gert Doering&quot; &quot;3244814&quot; &quot;myself&quot; &quot;Sep 15 94&quot; &quot;22:10:00&quot; </p>
<h2>FILES</h2>
<dl>
<dt><code>/usr/lib64/mgetty+sendfax/make.coverpg</code></p>
<dd> the program itself </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-faxspool/">faxspool</a>(1), <a href="/docs/linux/man/1-pbm2g3/">pbm2g3</a>(1), <a href="/docs/linux/man/1-ghostscript/">ghostscript</a>(1) </p>
<h2>AUTHORS</h2>
<p> The idea behind <i>make.coverpg</i> is Copyright (C) 1993 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;, the implementation will most likely have yours&#8230; </p>
<h2>Index</h2>
