---
title: "appstreamcli(1)"
name: "appstreamcli"
section: "1"
letter: "a"
url: "/docs/linux/man/1-appstreamcli/"
description: "appstreamcli – Handle AppStream metadata formats and query AppStream data"
---

<h2 class="name">NAME</h2>
<p> appstreamcli &#8211; Handle AppStream metadata formats and query AppStream data </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>appstreamcli</code> [<code>COMMAND</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>appstreamcli</code> command. </p>
<p> <code>appstreamcli</code> is a small helper tool to work with AppStream metadata and access the AppStream component index from the command-line. The AppStream component index contains a list of all available software components for your distribution, matched to their package names. It is generated using AppStream XML or Debian DEP-11 data, which is provided by your distributor. </p>
<p> For more information about the AppStream project and the other components which are part of it, take a look at the AppStream pages at m[blue]<code>Freedesktop.org</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>OPTIONS</h2>
<p> <code>get </code><i>ID</i></p>
<dl>
<dt>
<dd> Get a component from the matadata pool by its identifier.</dl>
<p> <code>s</code>, <code>search </code><i>TERM</i></p>
<dl>
<dt>
<dd> Search the AppStream component pool for a given search term.</dl>
<p> <code>what-provides </code><i>TYPE</i><i>TERM</i></p>
<dl>
<dt>
<dd> Return components which provide a given item. An item type can be specified using the <i>TYPE</i> parameter, a value to search for has to be supplied using the <i>TERM</i> parameter. </p>
<p> Examples: </p>
<p> Get components which handle the &quot;text/xml&quot; mediatype. </p>
<p> <code>appstreamcli</code> what-provides mediatype &quot;text/xml&quot; </p>
<p> Get component which provides the &quot;libfoo.so.2&quot; library. </p>
<p> <code>appstreamcli</code> what-provides lib libfoo.so.2</dl>
<p> <code>refresh</code>, <code>refresh-cache</code></p>
<dl>
<dt>
<dd> Trigger a database refresh, if necessary. In case you want to force the database to be rebuilt, supply the <code>&#8211;force</code> flag. </p>
<p> This command must be executed with root permission.</dl>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Display various information about the installed metadata and the metadata cache.</dl>
<p> <code>os-info</code></p>
<dl>
<dt>
<dd> Show information about the current operating system from the metadata index. This requires the operating system to provide a operating-system component for itself.</dl>
<p> <code>dump </code><i>ID</i></p>
<dl>
<dt>
<dd> Dump the complete XML descriptions of components with the given ID that were found in the metadata pool.</dl>
<p> <code>validate </code><i>FILES</i></p>
<dl>
<dt>
<dd> Validate AppStream XML metadata for compliance with the specification. </p>
<p> Both XML metadata types, upstream and distro XML, are handled. The format type which should be validated is determined automatically. </p>
<p> The <code>&#8211;pedantic</code> flag triggers a more pedantic validation of the file, including minor and style issues in the report.</dl>
<p> <code>validate-tree </code><i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Validate AppStream XML metadata found in a file-tree. </p>
<p> This performs a standard validation of all found metadata, but also checks for additional errors, like the presence of .desktop files and validity of other additional metadata.</dl>
<p> <code>check-license </code><i>LICENSE</i></p>
<dl>
<dt>
<dd> Test a license string or license expression for validity and display details about it. </p>
<p> This will check whether the license string is considered to be valid for AppStream, and return a non-zero exit code if it is not. The command will also display useful information like the canonical ID of a license, whether it is suitable as license for AppStream metadata, and whether the license is considered to be for Free and Open Source software or proprietary software. </p>
<p> AppStream will consider any license as Free and Open Source that is marked as suitable by either the Free Software Foundation (FSF), Open Source Initiative (OSI) or explicit license list of the Debian Free Software Guidelines (DFSG).</dl>
<p> <code>install </code><i>ID</i></p>
<dl>
<dt>
<dd> Install a software component by its ID using the package manager or Flatpak. </p>
<p> This resolves the AppStream component ID to an installation candidate and then calls either the native package manager or Flatpak (if available) to install the component.</dl>
<p> <code>remove </code><i>ID</i></p>
<dl>
<dt>
<dd> Uninstall a software component by its ID using the package manager or Flatpak. </p>
<p> This will uninstall software matching the selected ID using either the native package manager or Flatpak (if available).</dl>
<p> <code>put </code><i>FILE</i></p>
<dl>
<dt>
<dd> Install a metadata file into the right directory on the current machine.</dl>
<p> <code>compare-versions</code>, <code>vercmp </code><i>VER1</i><i>[CMP]</i><i>VER2</i></p>
<dl>
<dt>
<dd> Compare two version numbers. If two version numbers are given as parameters, the versions will be compared and the comparison result will be printed to stdout. </p>
<p> If a version number, a comparison operator and another version number are passed in as parameter, the result of the comparison operation will be printed to stdout, and <code>appstreamcli</code> will exit with a non-zero exit status in case the comparison failed. The comparison operator can be one of the following: </p>
<dl>
<dt>
<dd> &bull; eq &#8211; Equal to</dl>
<dl>
<dt>
<dd> &bull; ne &#8211; Not equal to</dl>
<dl>
<dt>
<dd> &bull; lt &#8211; Less than</dl>
<dl>
<dt>
<dd> &bull; gt &#8211; Greater than</dl>
<dl>
<dt>
<dd> &bull; le &#8211; Less than or equal to</dl>
<dl>
<dt>
<dd> &bull; ge &#8211; Greater than or equal to</dl>
</dl>
<p> <code>new-template </code><i>TYPE</i><i>FILE</i></p>
<dl>
<dt>
<dd> Create a metainfo file template to be used by software projects. The <code>&#8211;from-desktop</code> option can be used to use a .desktop file as template for generating the example file. </p>
<p> The generated files contain example entries which need to be filed in with the actual desired values by the project author. </p>
<p> The first <i>TYPE</i> parameter is the name of an AppStream component type. For a complete list check out m[blue]<code>the documentation</code>m[]<font SIZE="-2">[2]</font> or the help output of <code>appstreamcli</code> for this subcommand.</dl>
<p> <code>make-desktop-file </code><i>MI_FILE</i><i>DESKTOP_FILE</i></p>
<dl>
<dt>
<dd> Create a XDG desktop-entry file from a metainfo file. If the desktop-entry file specified in <i>DESKTOP_FILE</i> already exists, it will get extended with the new information extracted from the metainfo file. Otherwise a new file will be created. </p>
<p> This command will use the first binary mentioned in a provides tag of the component for the Exec= field of the new desktop-entry file. If this is not the desired behavior, the <code>&#8211;exec</code> flag can be used to explicitly define a binary to launch. Other methods of launching the application are currently not supported. </p>
<p> In order to generate a proper desktop-entry, this command assumes that not only the minimally required tags for an AppStream component are set, but also that it has an &lt;icon/&gt; tag of type &quot;stock&quot; to describe the stock icon that should be used as well as a &lt;categories/&gt; tag containing the categories the application should be placed in.</dl>
<p> <code>news-to-metainfo </code><i>NEWS_FILE</i><i>MI_FILE</i><i>[OUT_FILE]</i></p>
<dl>
<dt>
<dd> This command converts a NEWS file as used by many open source projects into the XML used by AppStream. Since NEWS files are free text, a lot of heuristics will be applied to get reasonable results. The converter can also read a YAML version of the AppStream release description and convert it to XML as well. If the metainfo file <i>MI_FILE</i> already exists, it will be augmented with the new release entries, otherwise the release entries will be written without any wrapping component. If <i>[OUT_FILE]</i> is specified, instead of acting on <i>MI_FILE</i> the changed data will be written to the particular file. If any of the output filenames is set to &quot;-&quot;, the output will instead be written to stdout. </p>
<p> The <code>&#8211;format</code> option can be used to enforce reading the input file in a specific format (&quot;text&quot; or &quot;yaml&quot;) in case the format autodetection fails. The <code>&#8211;limit</code> option is used to limit the amount of release entries written (the newest entries will always be first).</dl>
<p> <code>metainfo-to-news </code><i>MI_FILE</i><i>NEWS_FILE</i></p>
<dl>
<dt>
<dd> This command reverses the <code>news-to-metainfo</code> command and writes a NEWS file as text or YAML using the XML contained in a metainfo file. If <i>NEWS_FILE</i> is set to &quot;-&quot;, the resulting data will be written to stdout instead of to a file. </p>
<p> The <code>&#8211;format</code> option can be used to explicitly specify the output format (&quot;yaml&quot; or &quot;text&quot;). If it is not set, <code>appstreamcli</code> will guess which format is most suitable.</dl>
<p> <code>convert </code><i>FILE1</i><i>FILE1</i></p>
<dl>
<dt>
<dd> Converts AppStream XML metadata into its YAML representation and vice versa.</dl>
<p> <code>compose</code></p>
<dl>
<dt>
<dd> Composes an AppStream metadata catalog from a directory tree with metainfo files. This command is only available if the org.freedesktop.appstream.compose component is installed. See <code><a href="/docs/linux/man/1-appstreamcli-compose/">appstreamcli-compose</a></code>(1) for more information.</dl>
<p> <code>&#8211;details</code></p>
<dl>
<dt>
<dd> Print out more information about a found component.</dl>
<p> <code>&#8211;no-color</code></p>
<dl>
<dt>
<dd> Don&#8217;t print colored output.</dl>
<p> <code>&#8211;no-net</code></p>
<dl>
<dt>
<dd> Do not access the network when validating metadata. </p>
<p> The same effect can be achieved by setting the <code>AS_VALIDATE_NONET</code> environment variable before running <code>appstreamcli</code>.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of appstreamcli</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pkcon/">pkcon</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Matthias Klumpp &lt;matthias [at] tenstral.net&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2012-2022 Matthias Klumpp </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Freedesktop.org</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.freedesktop.org/wiki/Distributions/AppStream/">https://www.freedesktop.org/wiki/Distributions/AppStream/</a></dl>
<dt> 2.</p>
<dd> the documentation</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.freedesktop.org/software/appstream/docs/chap-Metadata.html">https://www.freedesktop.org/software/appstream/docs/chap-Metadata.html</a></dl>
</dl>
<h2>Index</h2>
