---
title: "foomatic-rip(1)"
name: "foomatic-rip"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-rip/"
description: "foomatic-rip – Universal print filter/RIP wrapper"
---

<h2 class="name">NAME</h2>
<p> foomatic-rip &#8211; Universal print filter/RIP wrapper </p>
<h2>SYNOPSIS</h2>
<h3>General Options:</h3>
<p> <code>foomatic-rip</code>&nbsp;<code>[-v]&nbsp;[-q]</code><i>&nbsp;&lt;mode-specific options&gt;</i> </p>
<h3>Spooler-less printing filter:</h3>
<p> <code>foomatic-rip</code>&nbsp;<code>[-P</code><i>&nbsp;&lt;printer&gt;</i><code>&nbsp;</code> | &nbsp;<code>&#8211;ppd</code> &nbsp;<i>&lt;ppdfile&gt;</i> <code>]</code> &nbsp;[<code>-J</code>&nbsp;<i>&lt;jobtitle&gt;</i> ] [<code>-o</code> &nbsp;<i>&lt;option&gt;</i><code>=</code><i>&lt;value&gt;</i> &nbsp;[&#8230;]] &nbsp;<code>[</code><i>&lt;files&gt;</i><code>]</code> </p>
<h3>CUPS filter:</h3>
<p> <code>foomatic-rip</code>&nbsp;<i>&lt;jobid&gt;</i><i>&nbsp;&lt;user&gt;</i><code>&nbsp;</code><i>&lt;jobtitle&gt;</i><i>&nbsp;&lt;numcopies&gt;</i><code>&nbsp;</code><i>&lt;options&gt;</i><i>&nbsp;</i><code>[</code><i>&lt;file&gt;</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> foomatic-rip is a universal print filter which can be used as CUPS filter or stand-alone for spooler-less, direct printing. It has the following features: </p>
<dl>
<dt>&bull;</p>
<dd> It translates PostScript and PDF from standard input or a file to the printer&#8217;s native language on standard output. </p>
<dt>&bull;</p>
<dd> The translation is done with an external renderer, usually Ghostscript (<code><a href="/docs/linux/man/1-gs/">gs</a>(1)</code>). If no translation is needed (PostScript printer) the renderer&#8217;s command line reduces to <code><a href="/docs/linux/man/1-cat/">cat</a>(1)</code>. The way how this translation is done is described in a <code>PPD file</code>. </p>
<dt>&bull;</p>
<dd> Printer capabilities, how to handle user options, and how to build the renderer command line is always described by <code>PPD files</code>, these PPD files usually come from <code>Foomatic</code> or can be the ones supplied by the manufacturers of PostScript printers. The PPD files are the same for both CUPS and direct printing. </p>
<dt>&bull;</p>
<dd> foomatic-rip works with <code>CUPS</code> and for direct printing (<code>without spooler</code>), where the latter is mainly for testing and debugging. The mode is selected by the command line options and environment variables which are supplied to foomatic-rip. </p>
<dt>&bull;</p>
<dd> foomatic-rip does not only apply option settings supplied by the user through the command line of the printing command, but also searches the entire job for embedded option settings (only PostScript jobs). Here not only settings which affect the whole job are taken into account, but also settings in the page headers, which are only valid for the page where they were found, so applications which produce PostScript code with page-specific printer option settings are fully supported. </p>
</dl>
<h2>DIRECT, SPOOLER-LESS PRINTING</h2>
<h3>Options</h3>
<dl>
<dt><code>-v</code></p>
<dd> verbose mode for debugging. <code>WARNING:</code> This will create a file in /tmp that contains the debugging information. This opens a security loophole and should not be used in production. </p>
<dt><code>-q</code></p>
<dd> quiet mode &#8211; minimal information output </p>
<dt><code>-P</code><i>&nbsp;&lt;printer&gt;</i></p>
<dd> <i>&lt;printer&gt;</i> is the configured printer which should be used for this job. </p>
<dt><code>&#8211;ppd</code><i>&nbsp;&lt;ppdfile&gt;</i></p>
<dd> The PPD file <i>&lt;ppdfile&gt;</i> should be applied for processing this job.</p>
<dt><code>-o</code><i>&nbsp;&lt;option&gt;</i><code>=</code><i>&lt;value&gt;</i></p>
<dd> Option settings for this job.</p>
<dt><i>&lt;files&gt;</i></p>
<dd> The file(s) to be printed. </p>
</dl>
<p> <code>foomatic-rip</code> will print from standard input unless at least one file to be printed is specified on the command line. If your printer PPD file is stored as <i>/etc/direct/&lt;printer&gt;.ppd</i> or <i>~/.foomatic/direct/&lt;printer&gt;.ppd</i> you can use it by simply specifying &quot;-P <i>&lt;printer&gt;</i>&quot;. </p>
<p> Put a line </p>
<p> <code>*FoomaticRIPPostPipe: &quot;| </code><i>&lt;command&gt;</i><code>&quot;</code> </p>
<p> into the PPD file, right after <code>*PPD-Adobe: &quot;4.3&quot;</code>, where <i>&lt;command&gt;</i> is a command into which you want to re-direct the output data. Due to the restrictions of PPD files <code>&lt;</code>, <code>&gt;</code>, and <code>&quot;</code> are not allowed in the <i>&lt;command&gt;</i>, replace them as follows: </p>
<pre><code>
Character Replacement-- -- -- -- -- -- -- -- -- -- -
</code></pre>
<p> This way you can print directly to your printer, use </p>
<p> <code>*FoomaticRIPPostPipe: &quot;| cat &amp;gt; /dev/lp0&quot;</code> </p>
<p> or </p>
<p> <code>*FoomaticRIPPostPipe: &quot;| cat &amp;gt; /dev/usb/lp0&quot;</code> </p>
<p> for local parallel or USB printers. To make normal users able to print this way add them to the group <code>lp</code> and make sure that the appropriate printer device file <i>/dev/&#8230;</i> is group-writable for the <code>lp</code> group. </p>
<p> for a TCP/Socket/JetDirect printer with the host name <code>printer</code> listening on port <code>9100</code> you need this: </p>
<p> <code>*FoomaticRIPPostPipe: &quot;| /usr/bin/nc -w 1 printer 9100&quot;</code> </p>
<p> Note the &quot;-w 1&quot; in the &quot;nc&quot; command line, it makes &quot;nc&quot; exiting immediately after the data is transferred to the printer. </p>
<p> <code>*FoomaticRIPPostPipe: &quot;| rlpr -Plp [at] printserver&quot;</code> </p>
<p> directs your jobs to the LPD printer queue <code>lp</code> on the machine named <code>printserver</code>. </p>
<p> See also <a rel="nofollow" href="http://www.openprinting.org/direct-doc.html">http://www.openprinting.org/direct-doc.html</a> </p>
<h2>PRINTING WITH SPOOLER</h2>
<p> See the documentation on the OpenPrinting Web site: <a rel="nofollow" href="http://www.openprinting.org/">http://www.openprinting.org/</a> </p>
<h2>CONFIGURATION FILE</h2>
<p> The file <code>/etc/cups/foomatic-rip.conf</code> or if it is not readable the file <code>/etc/foomatic/filter.conf</code> is read whenever foomatic-rip is executed. It allows one to configure the behavior of foomatic-rip as follows (lines beginning with <code>#</code> are comments and therefore get ignored): </p>
<dl>
<dt><code>debug: 0|1</code></p>
<dd> Turns on (<code>1</code>) or off (<code>0</code>) the debug mode. This is equivalent to supplying the <code>&#8211;debug</code> command line option. Default setting is <code>0</code>. </p>
<dt><code>echo:</code><i>&nbsp;[&lt;path&gt;/]&lt;executable&gt;</i></p>
<dd> Sets the path to an <code><a href="/docs/linux/man/1-echo/">echo</a>(1)</code> executable which supports <code>-n</code>. </p>
<dt><code>gspath:</code><i>&nbsp;[&lt;path&gt;/]&lt;executable&gt;</i></p>
<dd> Sets the path to the Ghostscript (<code><a href="/docs/linux/man/1-gs/">gs</a>(1)</code>) executable. To be used if Ghostscript is at a non-standard location or if an alternative Ghostscript should be used. </p>
<dt><code>execpath:</code><i>&nbsp;&lt;path&gt;[:&lt;path&gt;]&#8230;</i></p>
<dd> Sets the <code>$PATH</code> variable to be used by foomatic-rip. </p>
<dt><code>cupsfilterpath:</code><i>&nbsp;&lt;path&gt;[:&lt;path&gt;]&#8230;</i></p>
<dd> Sets the directories (colon-separated) in which foomatic-rip searches for CUPS filters. </p>
<dt><code>preferred_shell:</code><i>&nbsp;[&lt;path&gt;/]&lt;executable&gt;</i></p>
<dd> Sets the preferred shell to use when executing FoomaticRIPCommandLine and friends. Several PPD files use shell constructs that require a more modern shell like <code>bash</code>, <code>zsh</code>, or <code>ksh</code>. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>/etc/cups/ppd/&lt;printer&gt;.ppd</p>
<dd>
<dt>/etc/direct/&lt;printer&gt;.ppd</p>
<dd>
<p> The PPD files of the currently defined printers </p>
<dt>/etc/cups/foomatic-rip.conf</p>
<dd>
<dt>/etc/foomatic/filter.conf</p>
<dd>
<p> Configuration file for foomatic-rip </p>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>foomatic-rip</code> returns 0 unless something unexpected happens. </p>
<h2>AUTHOR</h2>
<p> Till Kamppeter &lt;<i>till.kamppeter [at] gmail.com</i>&gt; with parts of Manfred Wassmanns&#8217;s &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; man pages for the Foomatic 2.0.x filters. </p>
<h2>BUGS</h2>
<p> None so far. </p>
<p> Please send bug reports to the OpenPrinting bug tracker: </p>
<p> <a rel="nofollow" href="http://bugs.linuxfoundation.org/">http://bugs.linuxfoundation.org/</a> </p>
<p> Use &quot;OpenPrinting&quot; as the product and &quot;cups-filters&quot; as the component. </p>
<h2>Index</h2>
