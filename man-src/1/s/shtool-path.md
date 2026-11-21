---

title: "shtool-path(1)"
name: "shtool-path"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-path/"
description: "shtool path – GNU shtool command dealing with shell path variables"
---

<p> <code>shtool path</code> [<code>-s</code>|<code>&#8211;suppress</code>] [<code>-r</code>|<code>&#8211;reverse</code>] [<code>-d</code>|<code>&#8211;dirname</code>] [<code>-b</code>|<code>&#8211;basename</code>] [<code>-m</code>|<code>&#8211;magic</code>] [<code>-p</code>|<code>&#8211;path</code> <i>path</i>] <i>str</i> [<i>str</i> &#8230;]</p>
<p> This command deals with shell <tt>$PATH</tt> variables. It can find a program through one or more filenames given by one or more <i>str</i> arguments. It prints the absolute filesystem path to the program displayed on <tt>&quot;stdout&quot;</tt> plus an exit code of 0 if it was really found.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-s</code>, <code>&#8211;suppress</code></dt>
<dd> Supress output. Useful to only test whether a program exists with the help of the return code.</dd>
<dt><code>-r</code>, <code>&#8211;reverse</code></dt>
<dd> Transform a forward path to a subdirectory into a reverse path.</dd>
<dt><code>-d</code>, <code>&#8211;dirname</code></dt>
<dd> Output the directory name of <i>str</i>.</dd>
<dt><code>-b</code>, <code>&#8211;basename</code></dt>
<dd> Output the base name of <i>str</i>.</dd>
<dt><code>-m</code>, <code>&#8211;magic</code></dt>
<dd> Enable advanced magic search for &quot;<tt>&quot;perl&quot;</tt>&#8220; and &#8221;<tt>&quot;cpp&quot;</tt>&quot;.</dd>
<dt><code>-p</code>, <code>&#8211;path</code> <i>path</i></dt>
<dd> Search in <i>path</i>. Default is to search in <tt>$PATH</tt>.</dd></dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 awk=`shtool path -p &quot;${PATH}:.&quot; gawk nawk awk`
 perl=`shtool path -m perl`
 cpp=`shtool path -m cpp`
 revpath=`shtool path -r path/to/subdir`
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>path</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for <code>Apache</code>. It was later taken over into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-which/">which</a></i>(1). </p>
