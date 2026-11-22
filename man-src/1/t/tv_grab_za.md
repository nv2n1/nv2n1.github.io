---

title: "tv_grab_za(1)"
name: "tv_grab_za"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_za/"
description: "tv_grab_za – Grab TV listings for South Africa."
---

<p> tv_grab_za &#8211; Grab TV listings for South Africa. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_za &#8211;help </p>
<p> tv_grab_za [&#8211;config-file FILE] &#8211;configure [&#8211;gui OPTION] </p>
<p> tv_grab_za [&#8211;config-file FILE] [&#8211;output FILE] [&#8211;days N] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> [&#8211;quiet] [&#8211;retries N]</p>
<h2>DESCRIPTION</h2>
<p> Output TV listings for DSTV channels available in South Africa. The data comes from <a rel="nofollow" href="http://www.dstv.com">www.dstv.com</a>. The grabber relies on parsing HTML so it might stop working at any time. </p>
<p> First run <code>tv_grab_za &#8211;configure</code> to choose, which channels you want to download. Then running <code>tv_grab_za</code> with no arguments will output listings in XML format to standard output. </p>
<p> <code>&#8211;configure</code> Prompt for which channels, and write the configuration file. </p>
<p> <code>&#8211;config-file </code><code>FILE</code> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_za.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><code>OPTION</code> Use this option to enable a graphical interface to be used. OPTION may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of OPTION are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of XMLTV::ProgressBar. </p>
<p> <code>&#8211;output </code><code>FILE</code> write to FILE rather than standard output. </p>
<p> <code>&#8211;days N</code> grab N days. Can be 1, 7, 14 or 30. Default is 14 </p>
<p> <code>&#8211;quiet</code> suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;retries</code> number of retries before failing channel download. </p>
<p> <code>&#8211;help</code> print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i>xmltv</i>(5).</p>
<h2>AUTHORS Chris Picton &lt;cpicton [at] users.sf.net&gt; Neil Garratt &lt;ngarratt [at] users.sf.net&gt;</h2>
<p> Based on tv_grab_fi by Matti Airas. </p>
<p> Latest version always available at <a rel="nofollow" href="http://xmltv.cvs.sourceforge.net/xmltv/xmltv/grab/za/">http://xmltv.cvs.sourceforge.net/xmltv/xmltv/grab/za/</a></p>
<h2>BUGS</h2>
<p> Does not automatically update itself, when DSTV changes their site </p>
