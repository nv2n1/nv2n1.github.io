---

title: "nitrogen(1)"
name: "nitrogen"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nitrogen/"
description: "nitrogen – X11 background previewer and setter"
---

<h2>NAME</h2>
<p> nitrogen &#8211; X11 background previewer and setter</p>
<p> <code>nitrogen [</code> <i>OPTIONS</i> <code>]</code> <i>DIRECTORY?</i></p>
<p> In normal working mode, provides an interface which displays all pictures in the given DIRECTORY. From this interface, it is possible to set the X11 root pixmap either temporarily or set and store the picture, drawing mode, and X display for restoration later. If no directory is specified, it uses the stored directories in your &quot;library&quot; (as of 1.5). See the Preferences dialog. When the &#8211;restore option is passed, nitrogen sets all backgrounds that it has a configuration for and exits immediatly, for use in an .xinitrc or .xsession file.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;no-recurse</dt>
<dd> Do not recurse into subdirectories of DIRECTORY.</dd>
<dt>&#8211;restore</dt>
<dd> Restores previously saved pictures to the root displays.</dd>
<dt>&#8211;sort=[option]</dt>
<dd> Sorts the background list by the given option. By default, items are sorted as they are found on the filesystem, giving a quasi-newest first sorting order. Valid options are:</dd>
<dl>
<dl>
<dt>alpha</dt>
<dd> Alphabetical order.</dd>
<dt>ralpha</dt>
<dd> Reverse alphabetical order.</dd>
<dt>time</dt>
<dd> Modified time, ascending.</dd>
<dt>rtime</dt>
<dd> Modified time, descending.</dd></dl>
</dl>
<dt>&#8211;help</dt>
<dd> A mystery option which saves the iguanas of Sweden.</dd></dl>
<h2>FILES</h2>
<p> <i>~/.config/nitrogen/</i></p>
<dl>
<dt>
</dt><dd> Holds the configuration for saved backgrounds.</dd></dl>
<h2>BUGS</h2>
<p> There are probably plenty of them. Report all bugs to Dave Foster &lt;daf [at] minuslab.net&gt;.</p>
<h2>AUTHORS</h2>
<p> Dave Foster &lt;daf [at] minuslab.net&gt; Javeed Shaikh &lt;syscrash2k [at] gmail.com&gt;</p>
<h2>AVAILABILITY</h2>
<p> Homepage &#8211; <a rel="nofollow" href="http://projects.l3ib.org/nitrogen/.">http://projects.l3ib.org/nitrogen/.</a> The git repository is at <a href="http://code.l3ib.org/nitrogen.git">http://code.l3ib.org/nitrogen.git</a> </p>
