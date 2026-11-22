---

title: "tv_grab_uk_bleb(1)"
name: "tv_grab_uk_bleb"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_uk_bleb/"
description: "tv_grab_uk_bleb – Grab TV listings for the United Kingdom, from bleb.org"
---

<p> tv_grab_uk_bleb &#8211; Grab TV listings for the United Kingdom, from bleb.org </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_uk_bleb &#8211;help </p>
<p> tv_grab_uk_bleb [&#8211;config-file FILE] &#8211;configure [&#8211;gui OPTION] </p>
<p> tv_grab_uk_bleb [&#8211;config-file FILE] [&#8211;output FILE] [&#8211;quiet]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]</p>
<h2>DESCRIPTION</h2>
<p> Output TV and radio listings in XMLTV format for many stations available in Britain. The data comes from the bleb.org web site.</p>
<h2>USAGE</h2>
<p> First you must run <code>tv_grab_uk_bleb &#8211;configure</code> to choose which stations you want to receive. Then running <code>tv_grab_uk_bleb</code> with no arguments will get about a week&lt;39&gt;s listings for the stations you chose. </p>
<p> <code>&#8211;configure</code> Prompt for which stations to download and write the configuration file. </p>
<p> <code>&#8211;gui </code><code>OPTION</code> Use this option to enable a graphical interface to be used. OPTION may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of OPTION are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;config-file </code><code>FILE</code> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_uk_bleb.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;output </code><code>FILE</code> When grabbing, write output to FILE rather than standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days rather than as many as possible. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N. N may be negative. </p>
<p> <code>&#8211;quiet</code> Suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i>xmltv</i>(5), &lt;<a rel="nofollow" href="http://www.bleb.org/">http://www.bleb.org/</a>&gt;</p>
<h2>AUTHOR</h2>
<p> Andy Balaam, axis3x3 [at] users.sourceforge.net </p>
<p> Icon URLs collated by Lawrence, MagicLGH [at] aol.com </p>
<p> Based on tv_grab_nl_wolf by Ed Avis </p>
