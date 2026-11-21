---

title: "glabels(1)"
name: "glabels"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glabels/"
description: "glabels – Label and business card creation program for GNOME"
---

<h2>NAME</h2>
<p> glabels &#8211; Label and business card creation program for GNOME</p>
<p> <code>glabels</code> [OPTIONS] [label-filename&#8230;] </p>
<p> <code>glabels-batch</code> [OPTIONS] [label-filename&#8230;]</p>
<p> <code>glabels</code> is a lightweight program for creating labels and business cards for the GNOME desktop environment. It is designed to work with various laser/ink-jet peel-off label and business card sheets that you&#8217;ll find at most office supply stores. <code>glabels</code> is pre-configured with templates for many of these products. It also provides an interactive template designer for creating new templates according to user specifications. </p>
<p> For full documentation see the <code>gLabels</code> online help. </p>
<p> <code>glabels-batch</code> is a command line utility to print labels previously prepared with <code>glabels.</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Display a summary of available command-line options.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display a short usage summary.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Print program version information.</dd></dl>
<p> <code>Options specific to glabels-batch</code></p>
<dl>
<dt><code>-o</code> <i>filename</i>, <code>&#8211;output</code>=<i>filename</i></dt>
<dd> Set output filename to <i>filename</i>. (default=&quot;output.ps&quot;)</dd>
<dt><code>-s</code> <i>n</i>, <code>&#8211;sheets</code>=<i>n</i></dt>
<dd> Set number of sheets to <i>n</i>. (default=1)</dd>
<dt><code>-c</code> <i>n</i>, <code>&#8211;copies</code>=<i>n</i></dt>
<dd> Set number of copies to <i>n</i>. (default=1)</dd>
<dt><code>-f</code> <i>n</i>, <code>&#8211;first</code>=<i>n</i></dt>
<dd> Set label on first sheet to start printing from to <i>n</i>. (default=1)</dd>
<dt><code>-l</code>, <code>&#8211;outline</code></dt>
<dd> Print outlines around labels. This is useful for testing printer alignment or printing proof sheets.</dd>
<dt><code>-r</code>, <code>&#8211;reverse</code></dt>
<dd> Print mirror image of labels. This is useful for clear labels intended to be seen from the back through glass. </dd>
</dl>
<h2>FILES</h2>
<p> The $HOME/.glabels directory contains all user-defined templates.</p>
<h2>SEE ALSO</h2>
<p> The gLabels homepage at &lt;<a rel="nofollow" href="http://glabels.sourceforge.net/">http://glabels.sourceforge.net/</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Jim Evins &lt;evins [at] snaught.com&gt; </p>
