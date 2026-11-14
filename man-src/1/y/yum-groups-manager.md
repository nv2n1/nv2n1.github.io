---
title: "yum-groups-manager(1)"
name: "yum-groups-manager"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-groups-manager/"
description: "yum-groups-manager – create and edit yum’s group metadata"
---

<h2>NAME</h2>
<p> yum-groups-manager &#8211; create and edit yum&#8217;s group metadata</p>
<h2>SYNOPSIS</h2>
<p> <code>yum-groups-manager</code> [options] [packages]</p>
<h2>DESCRIPTION</h2>
<p> <code>yum-groups-manager</code> is used to create or edit a group metadata file for a yum repository. This is often much easier than writing/editing the XML by hand. The <code>yum-groups-manager</code> can load an entire file of groups metadata and either create a new group or edit an existing group and then write all of the groups metadata back out.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help message, and then quit.</p>
<dt><code>&#8211;version</code></p>
<dd> Display a version message, and then quit.</p>
<dt><code>-n, &#8211;name</code></p>
<dd> The name to lookup/use for the group. If you specify an existing group id, then the group with that id will have it&#8217;s name changed to this value.</p>
<dt><code>&#8211;id</code></p>
<dd> The id to lookup/use for the group. If you don&#8217;t specify an id, but do specify a name that doesn&#8217;t refer to an existing group, then an id for the group is generated based on the name.</p>
<dt><code>&#8211;description</code></p>
<dd> The description to use for the group.</p>
<dt><code>&#8211;mandatory</code></p>
<dd> Store the package names specified within the mandatory section of the specified group, the default is to use the default section. This overrides the optional argument.</p>
<dt><code>&#8211;optional</code></p>
<dd> Store the package names specified within the optional section of the specified group, the default is to use the default section. This option is overridden by the mandatory argument.</p>
<dt><code>&#8211;dependencies</code></p>
<dd> Also include the names of the direct dependencies for each package specified.</p>
<dt><code>&#8211;not-user-visible</code></p>
<dd> Make the group not visible in yum grouplist.</p>
<dt><code>&#8211;user-visible</code></p>
<dd> Make the group visible in yum grouplist (this is the default).</p>
<dt><code>&#8211;display-order</code></p>
<dd> Change the integer which controls the order groups are presented in, for example in yum grouplist.</p>
<dt><code>&#8211;load</code></p>
<dd> Load the groups metadata information from the specified file, before performing any operations. This option can be specified multiple times.</p>
<dt><code>&#8211;save</code></p>
<dd> Save the result to this file, you can specify the name of a file you are loading from as the data will only be saved when all the operations have been performed. This option can also be specified multiple times.</p>
<dt><code>&#8211;merge</code></p>
<dd> This is the same as loading and saving a file, however the &quot;merge&quot; file is loaded before any others and saved last.</p>
<dt><code>&#8211;print</code></p>
<dd> Also print the result to stdout, if saving or merging.</p>
<dt><code>&#8211;remove</code></p>
<dd> Instead of adding package, remove them. Note that the packages are removed from all sections (default, mandatory and optional).</p>
<dt><code>&#8211;translated-name</code></p>
<dd> This is another name for the group within the locale given. The syntax is lang:text. Eg. en:my-group-name-in-english</p>
<dt><code>&#8211;translated-description</code></p>
<dd> This is another description for the group within the locale given. The syntax is lang:text. Eg. en:my-group-description-in-english. </p>
</dl>
<h2>YUM OPTIONS</h2>
<p> The following options are meant to be the same as those with the same name in yum.</p>
<dl>
<dt><code>-c CONFIG, &#8211;config=CONFIG</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>
<dt><code>&#8211;enablerepo</code></p>
<dd>
<dt><code>&#8211;disablerepo</code></p>
<dd>
<dt><code>&#8211;noplugins</code></p>
<dd>
<dt><code>-C, &#8211;cache</code></p>
<dd>
<dt><code>&#8211;tempcache</code></p>
<dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Create a new group metadata file, with a group called yum containing all the packages that start with yum:</p>
<dd> <code> yum-groups-manager &#8211;name YUM &#8211;save groups.xml &#8216;yum*&#8217;</code></p>
<dt>After the above command, load the groups.xml data, work with the yum group, make the group not user visible, and remove the yum-skip-broken and yum-priorities packages from it:</p>
<dd> <code> yum-groups-manager -n YUM &#8211;merge groups.xml &#8211;remove yum-skip-broken yum-priorities &#8211;not-user-visible</code></p>
<dt>After the above commands, add a description and a translated name to the yum group:</p>
<dd> <code> yum-groups-manager -n YUM &#8211;merge groups.xml &#8211;description &#8216;This is a group with most of the yum packages in it&#8217; &#8211;translated-name &#8216;en:yum packages&#8217;</code></dl>
<h2>FILES</h2>
<p> <code>yum-groups-manager</code> uses the yum libraries for retrieving information and packages. If no configuration file is specified, the default yum configuration will be used. </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
</pre>
<h2>SEE ALSO</h2>
<pre>
<i>yum (8)</i>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
<h2>BUGS</h2>
<pre>
There are a couple of options you can't set, yet. Most notably you cannot put
package names into the conditional section (where they are installed with
groupinstall only if another package is installed).
Other than that, there are no bugs, but should you find any, you should first
consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful
in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org.
To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos
related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs.
</pre>
<h2>Index</h2>
