---
title: "createrepo(8)"
name: "createrepo"
section: "8"
letter: "c"
url: "/docs/linux/man/8-createrepo/"
description: "createrepo – Create repomd (xml-rpm-metadata) repository"
---

<p>createrepo &#8211; Create repomd (xml-rpm-metadata) repository</p>
<h2>Synopsis</h2>
<p><code>createrepo</code> [options] &lt;directory&gt; </p>
<h2>Description</h2>
<p><code>createrepo</code> is a program that creates a repomd (xml-based rpm metadata) repository from a set of rpms. </p>
<h2>Options</h2>
<dl>
<dt><code>-u &#8211;baseurl</code> &lt;url&gt;</p>
<dd>Optional base URL location for all files.</p>
<dt><code>-o &#8211;outputdir</code> &lt;url&gt;</p>
<dd>Optional output directory (useful for read only media).</p>
<dt><code>-x &#8211;excludes</code> &lt;package&gt;</p>
<dd>File globs to exclude, can be specified multiple times.</p>
<dt><code>-i &#8211;pkglist</code> &lt;filename&gt;</p>
<dd>specify a text file which contains the complete list of files to include in the repository from the set found in the directory. File format is one package per line, no wildcards or globs.</p>
<dt><code>-n &#8211;includepkg</code></p>
<dd>specify pkgs to include on the command line. Takes urls as well as local paths.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd>Run quietly.</p>
<dt><code>-g &#8211;groupfile</code> &lt;groupfile&gt;</p>
<dd>A precreated xml filename to point to for group information.<br />
 See examples section below for further explanation.</p>
<dt><code>-v &#8211;verbose</code></p>
<dd>Run verbosely.</p>
<dt><code>-c &#8211;cachedir</code> &lt;path&gt;</p>
<dd>Specify a directory to use as a cachedir. This allows createrepo to create a cache of checksums of packages in the repository. In consecutive runs of createrepo over the same repository of files that do not have a complete change out of all packages this decreases the processing time dramatically. </p>
<dt><code>&#8211;update</code></p>
<dd>If metadata already exists in the outputdir and an rpm is unchanged (based on file size and mtime) since the metadata was generated, reuse the existing metadata rather than recalculating it. In the case of a large repository with only a few new or modified rpms this can significantly reduce I/O and processing time. </p>
<dt><code>&#8211;skip-stat</code></p>
<dd>skip the stat() call on a &#8211;update, assumes if the filename is the same then the file is still the same (only use this if you&#8217;re fairly trusting or gullible). </p>
<dt><code>-C &#8211;checkts</code></p>
<dd>Don&#8217;t generate repo metadata, if their timestamps are newer than its rpms. This option decreases the processing time drastically again, if you happen to run it on an unmodified repo, but it is (currently) mutual exclusive with the &#8211;split option. NOTE: This command will not notice when packages have been removed from repo. Use &#8211;update to handle that. </p>
<dt><code>&#8211;split</code></p>
<dd>Run in split media mode. Rather than pass a single directory, take a set of directories corresponding to different volumes in a media set. </p>
<dt><code>-p &#8211;pretty</code></p>
<dd>Output xml files in pretty format.</p>
<dt><code>-V &#8211;version</code></p>
<dd>Output version.</p>
<dt><code>-h &#8211;help</code></p>
<dd>Show help menu. </p>
<dt><code>-d &#8211;database</code></p>
<dd>Generate sqlite databases for use with yum. This is now the default. </p>
<dt><code>&#8211;no-database</code></p>
<dd>Do not generate sqlite databases in the repository. </p>
<dt><code>-S &#8211;skip-symlinks</code></p>
<dd>Ignore symlinks of packages</p>
<dt><code>-s &#8211;checksum</code></p>
<dd>Choose the checksum type used in repomd.xml and for packages in the metadata. The default is now &quot;sha256&quot; (if python has hashlib). The older default was &quot;sha&quot;, which is actually &quot;sha1&quot;, however explicitly using &quot;sha1&quot; doesn&#8217;t work on older (3.0.x) versions of yum, you need to specify &quot;sha&quot;.</p>
<dt><code>&#8211;profile</code></p>
<dd>Output time based profiling information.</p>
<dt><code>&#8211;changelog-limit</code> CHANGELOG_LIMIT</p>
<dd>Only import the last N changelog entries, from each rpm, into the metadata</p>
<dt><code>&#8211;unique-md-filenames</code></p>
<dd>Include the file&#8217;s checksum in the metadata filename, helps HTTP caching (default) </p>
<dt><code>&#8211;simple-md-filenames</code></p>
<dd>Do not include the file&#8217;s checksum in the metadata filename. </p>
<dt><code>&#8211;distro</code></p>
<dd>Specify distro tags. Can be specified more than once. Optional syntax specifying a cpeid(<a rel="nofollow" href="http://cpe.mitre.org/)">http://cpe.mitre.org/)</a> &#8211;distro=cpeid,distrotag</p>
<dt><code>&#8211;content</code></p>
<dd>Specify keyword/tags about the content of the repository. Can be specified more than once.</p>
<dt><code>&#8211;repo</code></p>
<dd>Specify keyword/tags about the repository itself. Can be specified more than once.</p>
<dt><code>&#8211;revision</code></p>
<dd>Arbitrary string for a repository revision.</p>
<dt><code>&#8211;deltas</code></p>
<dd>Tells createrepo to generate deltarpms and the delta metadata</p>
<dt><code>&#8211;oldpackagedirs</code> PATH</p>
<dd>paths to look for older pkgs to delta against. Can be specified multiple times</p>
<dt><code>&#8211;num-deltas</code> int</p>
<dd>the number of older versions to make deltas against. Defaults to 1</p>
<dt><code>&#8211;read-pkgs-list</code> READ_PKGS_LIST</p>
<dd>output the paths to the pkgs actually read useful with &#8211;update</p>
<dt><code>&#8211;max-delta-rpm-size</code> MAX_DELTA_RPM_SIZE</p>
<dd>max size of an rpm that to run deltarpm against (in bytes)</p>
<dt><code>&#8211;workers</code> WORKERS</p>
<dd>number of workers to spawn to read rpms</p>
<dt><code>&#8211;xz</code></p>
<dd>use xz for repodata compression</p>
<dd></dl>
<h2>Examples</h2>
<p>Here is an example of a repository with a groups file. Note that the groups file should be in the same directory as the rpm packages (i.e. /path/to/rpms/comps.xml).<br />
 <code>createrepo</code> -g comps.xml /path/to/rpms </p>
<h2>Files</h2>
<pre>repodata/filelists.xml.gz
repodata/other.xml.gz
repodata/primary.xml.gz
repodata/repomd.xml </pre>
<h2>See Also</h2>
<p><i>yum (8) yum.conf (5)</i> </p>
<h2>Authors</h2>
<pre>See the Authors file</pre>
<h2>Bugs</h2>
<p>Any bugs which are found should be emailed to the mailing list: rpm-metadata [at] lists.baseurl.org or reported in trac at: <a rel="nofollow" href="http://createrepo.baseurl.org">http://createrepo.baseurl.org</a> </p>
