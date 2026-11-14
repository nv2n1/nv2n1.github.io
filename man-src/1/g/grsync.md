---
title: "grsync(1)"
name: "grsync"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grsync/"
description: "GRSYNC – GTK+ frontend for rsync"
---

<h2 class="name">NAME</h2>
<p> GRSYNC &#8211; GTK+ frontend for rsync</p>
<h2>SYNOPSIS</h2>
<p> <code>grsync [-e] [-s] [session_name]</code> </p>
<p> <code>grsync -i session_file_name</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>GRSYNC</code> is a graphical interface using GTK2 for the rsync command line program. It currently supports the most important rsync features and can be used effectively for local directory synchronization. </p>
<h2>OPTIONS</h2>
<p> You can specify a session to load instead of the default one, by typing it as a command line option. The &quot;-e&quot; commandline option automatically executes the session and closes grsync when finished, unless an error has been encountered. You can have grsync stay open anyway using the &quot;-s&quot; option (even if the session run has been successfull). </p>
<p> The alternative syntax, using the &quot;-i&quot; switch, will open the &quot;import session&quot; dialog on the file you specified as argument. </p>
<h2>SEE ALSO</h2>
<p> <code>Website</code> &lt;<a rel="nofollow" href="http://www.opbyte.it/grsync/">http://www.opbyte.it/grsync/</a>&gt; </p>
<h2>AUTHOR</h2>
<p> GRSYNC was written by Piero Orsoni &lt;info [at] opbyte.it&gt;. </p>
<p> This manual page was written by Daniel Baumann &lt;daniel.baumann [at] panthera-systems.net&gt;, for the Debian project (but may be used by others). Updated by Piero Orsoni. </p>
<h2>Index</h2>
