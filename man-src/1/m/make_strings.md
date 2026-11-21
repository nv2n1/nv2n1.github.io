---

title: "make_strings(1)"
name: "make_strings"
section: "1"
letter: "m"
url: "/docs/linux/man/1-make_strings/"
description: "make_strings – tool to build lists of localizable strings from Objective-C files"
---

<p> <code>make_strings</code> [<code>&#8211;help</code>] [<code>&#8211;verbose</code>] [<code>&#8211;aggresive-import</code>] [<code>&#8211;aggressive-match</code>] [<code>&#8211;aggressive-remove</code>] [<code>-L</code> <i>languages</i>] <i>files.[hmc&#8230;]</i> </p>
<p> <code>make_strings</code> parses Objective-C files and builds lists of localizable strings. It then creates new <i>.strings</i> files or merges the strings with existing <i>.strings</i> files. It&#8217;s fairly intelligent when matching old and new strings, and produces <i>.strings</i> files that are (supposed to be) easy for a translator to work with. </p>
<p> <code>make_strings</code> accepts the following options: </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Prints a short list of available options.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Prints additional information while processing.</dd>
<dt><code>-L</code><i> languages</i></dt>
<dd> Specify which languages to process. Multuple <code>-L</code> options are accepted, or multiple <i>languages</i> defined in one <code>-L</code> flag.</dd>
<dt><code>&#8211;aggressive-import</code></dt>
<dd> Activates <code>&#8211;aggresive-match</code> and automatically removes &quot;dummy&quot; entries that are added by importing <i>.strings</i> files which were not created by <code>make_strings</code> program. This option is suitable when <code>make_strings</code> is run for the first time and there is an existing <i>.strings</i> file which contains a fairly accurate translation.</dd>
<dt><code>&#8211;aggressive-match</code></dt>
<dd> This option will make <code>make_strings</code> assume that matching keys should have matching translations. This can save lots of work, but it increases the risk of erroneous translation.</dd>
<dt><code>&#8211;aggressive-remove</code></dt>
<dd> Removes obsolete strings/keys. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> make_strings -L &quot;English Swedish Russian&quot; *.[hm] </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gnustep/">GNUstep</a></code>(7). </p>
<h2>AUTHORS</h2>
<p> <code>make_strings</code> was written Alexander Malmberg &lt;alexander [at] malmberg.org&gt;. </p>
<p> This manual page was added by Yavor Doganov &lt;yavor [at] gnu.org&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 Free Software Foundation, Inc. </p>
<p> Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. </p>
