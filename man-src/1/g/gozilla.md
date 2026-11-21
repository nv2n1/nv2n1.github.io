---

title: "gozilla(1)"
name: "gozilla"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gozilla/"
description: "gozilla – force mozilla to display specified source file."
---

<h2>NAME</h2>
<p> gozilla &#8211; force mozilla to display specified source file.</p>
<p> <code>gozilla</code> [-b browser][-p][+no] file<br />
 <code>gozilla</code> [-b browser][-p] -d name </p>
<p> <code>Gozilla</code> force mozilla to display specified source file as a hypertext. <code>Gozilla</code> can be used with other browsers like firefox and epiphany. </p>
<p> In advance of using this command, you must execute <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1) and <code><a href="/docs/linux/man/1-htags/">htags</a></code>(1) at the root directory of the source tree to make tag files. Then you can execute gozilla at anywhere in the source tree. </p>
<p> First form:<br />
 You can specify source file and the line number optionally. </p>
<p> Second form:<br />
 You can specify definition name directly. Definition name must exist in &#8216;GTAGS&#8217; tag file. </p>
<p> Some browsers require you to load it before executing <code>gozilla</code>. Whether or not <code>gozilla</code> waits for exiting of browser depends on browser.</p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>+no</code></dt>
<dd> line number. It must be a line on which function definition or function reference is exist. If you execute <code><a href="/docs/linux/man/1-htags/">htags</a></code>(1) with <code>-l</code> option, you can specify any line.</dd>
<dt><code>-b</code> <i>browser</i></dt>
<dd> browser to use. By default, it is assumed <code>mozilla</code>.</dd>
<dt><code>-d</code> <i>name</i></dt>
<dd> print function.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show help.</dd>
<dt><code>-p</code></dt>
<dd> just print generated target URL.</dd>
<dt><i>file</i></dt>
<dd> path of source file or alias name.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Quiet mode.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Verbose mode.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version number.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>&#8216;HTML/&#8217;</dt>
<dd> hypertext of source tree.</dd>
<dt>&#8216;GTAGS/&#8217;</dt>
<dd> tags file for function definitions.</dd>
<dt>&#8216;$HOME/.gozillarc&#8217;</dt>
<dd> alias file. Please read source code for the detail.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GTAGSROOT</code></dt>
<dd> The directory which is the root of source tree.</dd>
<dt><code>GTAGSDBPATH</code></dt>
<dd> The directory on which gtags database exist. This value is ignored when <code>GTAGSROOT</code> is not defined.</dd>
<dt><code>BROWSER</code></dt>
<dd> browser to use. By default, it is assumed mozilla.</dd></dl>
<h2>EXAMPLES</h2>
<pre>
        $ gtags
        $ htags
        $ global -x main
        main              82 ctags.c          main(argc, argv)
        $ mozilla &amp;
        $ gozilla +82 ctags.c
        $ firefox &amp;
        $ gozilla -b firefox +82 ctags.c
        $ setenv BROWSER 'epiphany --new-tab'
        $ epiphany &amp;
        $ gozilla +82 ctags.c
</pre>
<h2>DIAGNOSTICS</h2>
<p> <code>Gozilla</code> exits with a non 0 value if an error occurred, 0 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-global/">global</a></code>(1), <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1), <code><a href="/docs/linux/man/1-htags/">htags</a></code>(1), <code><a href="/docs/linux/man/1-firefox/">firefox</a></code>(1), <code><a href="/docs/linux/man/1-epiphany/">epiphany</a></code>(1), <code>mozilla</code>(1). </p>
<p> GNU GLOBAL source code tag system<br />
 (<a rel="nofollow" href="http://www.gnu.org/software/global/">http://www.gnu.org/software/global/</a>).</p>
<h2>NOTES</h2>
<p> <code>Gozilla</code> means &#8216;Global for mozilla&#8217;.</p>
<h2>BUGS</h2>
<p> <code>Gozilla</code> can treat not only source file but also normal file, directory, HTML file and even URL, because it is omnivorous.</p>
<h2>AUTHORS</h2>
<p> Tama Communications Corporation.</p>
<h2>HISTORY</h2>
<p> The <code>gozilla</code> command appeared in FreeBSD 2.2.2 but did not installed by default. </p>
