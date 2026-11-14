---
title: "apropos(1)"
name: "apropos"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apropos/"
description: "apropos – search the manual page names and descriptions"
---

<h2 class="name">NAME</h2>
<p> apropos &#8211; search the manual page names and descriptions </p>
<h2>SYNOPSIS</h2>
<p> <code>apropos</code> [<code>-dalv?V</code>] [<code>-e</code>|<code>-w</code>|<code>-r</code>] [<code>-s</code> <i>list</i>] [<code>-m</code> <i>system</i>[,&#8230;]] [<code>-M</code> <i>path</i>] [<code>-L</code> <i>locale</i>] [<code>-C</code> <i>file</i>] <i>keyword</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Each manual page has a short description available within it. <code>apropos</code> searches the descriptions for instances of <i>keyword</i>. </p>
<p> <i>keyword</i> is usually a regular expression, as if (<code>-r</code>) was used, or may contain wildcards (<code>-w</code>), or match the exact keyword (<code>-e</code>). Using these options, it may be necessary to quote the <i>keyword</i> or escape (\) the special characters to stop the shell from interpreting them. </p>
<p> The standard matching rules allow matches to be made against the page name and word boundaries in the description. </p>
<p> The database searched by <code>apropos</code> is updated by the <code>mandb</code> program. Depending on your installation, this may be run by a periodic cron job, or may need to be run manually after new manual pages have been installed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print verbose warning messages.</p>
<dt><code>-r</code>, <code>&#8211;regex</code></p>
<dd> Interpret each keyword as a regular expression. This is the default behaviour. Each keyword will be matched against the page names and the descriptions independently. It can match any part of either. The match is not limited to word boundaries.</p>
<dt><code>-w</code>, <code>&#8211;wildcard</code></p>
<dd> Interpret each keyword as a pattern containing shell style wildcards. Each keyword will be matched against the page names and the descriptions independently. If <code>&#8211;exact</code> is also used, a match will only be found if an expanded keyword matches an entire description or page name. Otherwise the keyword is also allowed to match on word boundaries in the description.</p>
<dt><code>-e</code>, <code>&#8211;exact</code></p>
<dd> Each keyword will be exactly matched against the page names and the descriptions.</p>
<dt><code>-a</code>, <code>&#8211;and</code></p>
<dd> Only display items that match all the supplied keywords. The default is to display items that match any keyword.</p>
<dt><code>-l</code>, <code>&#8211;long</code></p>
<dd> Do not trim output to the terminal width. Normally, output will be truncated to the terminal width to avoid ugly results from poorly-written <code>NAME</code> sections.</p>
<dt><code>-s</code> <i>list/</i>, <code>&#8211;sections=</code><i>list/</i>, <code>&#8211;section=</code><i>list</i></p>
<dd> Search only the given manual sections. <i>list</i> is a colon- or comma-separated list of sections. If an entry in <i>list</i> is a simple section, for example &quot;3&quot;, then the displayed list of descriptions will include pages in sections &quot;3&quot;, &quot;3perl&quot;, &quot;3x&quot;, and so on; while if an entry in <i>list</i> has an extension, for example &quot;3perl&quot;, then the list will only include pages in that exact part of the manual section.</p>
<dt><code>-m</code> <i>system</i>[,&#8230;], <code>&#8211;systems=</code><i>system</i>[,&#8230;]</p>
<dd> If this system has access to other operating systems&#8217; manual page descriptions, they can be searched using this option. To search NewOS&#8217;s manual page descriptions, use the option <code>-m</code> <code>NewOS</code>. </p>
<p> The <i>system</i> specified can be a combination of comma-delimited operating system names. To include a search of the native operating system&#8217;s <code>whatis</code> descriptions, include the system name <code>man</code> in the argument string. This option will override the $<code>SYSTEM</code> environment variable.</p>
<dt><code>-M&nbsp;</code><i>path</i>,&nbsp;<code>&#8211;manpath=</code><i>path</i></p>
<dd> Specify an alternate set of colon-delimited manual page hierarchies to search. By default, <code>apropos</code> uses the $<code>MANPATH</code> environment variable, unless it is empty or unset, in which case it will determine an appropriate manpath based on your $<code>PATH</code> environment variable. This option overrides the contents of $<code>MANPATH</code>.</p>
<dt><code>-L&nbsp;</code><i>locale</i>,&nbsp;<code>&#8211;locale=</code><i>locale</i></p>
<dd> <code>apropos</code> will normally determine your current locale by a call to the C function <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) which interrogates various environment variables, possibly including $<code>LC_MESSAGES</code> and $<code>LANG</code>. To temporarily override the determined value, use this option to supply a <i>locale</i> string directly to <code>apropos</code>. Note that it will not take effect until the search for pages actually begins. Output such as the help message will always be displayed in the initially determined locale.</p>
<dt><code>-C&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;config-file=</code><i>file</i></p>
<dd> Use this user configuration file rather than the default of <i>~/.manpath</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Successful program execution.</p>
<dt><code>1</code></p>
<dd> Usage, syntax or configuration file error.</p>
<dt><code>2</code></p>
<dd> Operational error.</p>
<dt><code>16</code></p>
<dd> Nothing was found that matched the criteria specified.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SYSTEM</code></p>
<dd> If $<code>SYSTEM</code> is set, it will have the same effect as if it had been specified as the argument to the <code>-m</code> option.</p>
<dt><code>MANPATH</code></p>
<dd> If $<code>MANPATH</code> is set, its value is interpreted as the colon-delimited manual page hierarchy search path to use. </p>
<p> See the <code>SEARCH PATH</code> section of <code><a href="/docs/linux/man/5-manpath/">manpath</a></code>(5) for the default behaviour and details of how this environment variable is handled.</p>
<dt><code>MANWIDTH</code></p>
<dd> If $<code>MANWIDTH</code> is set, its value is used as the terminal width (see the <code>&#8211;long</code> option). If it is not set, the terminal width will be calculated using the value of $<code>COLUMNS</code>, and <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) if available, or falling back to 80 characters if all else fails.</p>
<dt><code>POSIXLY_CORRECT</code></p>
<dd> If $<code>POSIXLY_CORRECT</code> is set, even to a null value, the default <code>apropos</code> search will be as an extended regex (<code>-r</code>). Nowadays, this is the default behaviour anyway.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/man/index.(bt|db|dir|pag)</i></p>
<dd> A traditional global <i>index</i> database cache.</p>
<dt><i>/var/cache/man/index.(bt|db|dir|pag)</i></p>
<dd> An FHS compliant global <i>index</i> database cache.</p>
<dt><i>/usr/share/man/&#8230;/whatis</i></p>
<dd> A traditional <code>whatis</code> text database.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1), <code><a href="/docs/linux/man/8-mandb/">mandb</a></code>(8)</p>
<h2>AUTHOR</h2>
<pre><code>
Wilf.(G.Wilford[at] ee.surrey.ac.uk).Fabrizio Polacco(fpolacco[at] debian.org).Colin Watson(cjwatson[at] debian.org).
</code></pre>
<h2>BUGS</h2>
<p> <a rel="nofollow" href="https://gitlab.com/cjwatson/man-db/-/issues">https://gitlab.com/cjwatson/man-db/-/issues</a><br />
 <a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=man-db">https://savannah.nongnu.org/bugs/?group=man-db</a> </p>
<h2>Index</h2>
