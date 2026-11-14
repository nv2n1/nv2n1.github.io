---
title: "update-gconf-defaults(8)"
name: "update-gconf-defaults"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-gconf-defaults/"
description: "update-gconf-defaults – generate GConf defaults shipped in Debian packages"
---

<p>update-gconf-defaults &#8211; generate GConf defaults shipped in Debian packages</p>
<h2>Synopsis</h2>
<p><code>update-gconf-defaults</code> [options]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>update-gconf-defaults</code> command. </p>
<p> <code>update-gconf-defaults</code> is responsible for generating defaults used by GConf from the files found in <i>/usr/share/gconf/defaults</i>. </p>
<p> The syntax of files in this directory consists in lines containing the key name, some white space, and the key value, which can be an integer, a boolean, a float, a string or a list of strings. Example: </p>
<p> /apps/myprogram/frob_number 42<br />
 /apps/myprogram/do_foo true<br />
 /apps/myprogram/priority 1.25<br />
 /apps/myprogram/name &quot;Gotcha !&quot;<br />
 /apps/myprogram/names [Ha ha!,Let&#8217;s keep serious,Ho ho!] </p>
<p> Files are processed in alphabetical order. Files processed later take precedence over the previous ones if they include the same defaults. Thus, it is recommended to name them <i>NN</i>_<i>package</i> with <i>NN</i> being a 2-digit number and <i>package</i> the package name. It is recommended to set <i>NN</i> as 10 for packages in the Debian archive, 20 for derived distributions, 50 for CDD distributions, and 90 for site-specific packages.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;source</code> <i>source_dir</i></p>
<dd>Specify an alternate source directory where to find the defaults.</p>
<dt><code>&#8211;destination</code> <i>destination_dir</i></p>
<dd>Specify an alternate destination directory where to build the resulting GConf tree.</p>
<dt><code>&#8211;mandatory</code></p>
<dd>Sets source and destination directories appropriate for the mandatory values.</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/gconf/defaults/</i></p>
<dd>The directory from which defaults files are read.</p>
<dt><i>/usr/share/gconf/mandatory/</i></p>
<dd>The directory from which defaults files for mandatory settings are read.</p>
<dt><i>/var/lib/gconf/debian.defaults</i></p>
<dd>The directory where the GConf tree for default settings is generated. It is read by GConf with the default Debian configuration, and it takes precedence over upstream defaults.</p>
<dt><i>/var/lib/gconf/debian.mandatory</i></p>
<dd>The directory where the GConf tree for mandatory settings is generated. It is read by GConf with the default Debian configuration, and it takes precedence over user settings.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dh_gconf/">dh_gconf</a></code>(1),<code><a href="/docs/linux/man/1-gconftool/">gconftool</a></code>(1).</p>
<h2>Author</h2>
<p>Josselin Mouette &lt;joss [at] debian.org&gt;.</p>
