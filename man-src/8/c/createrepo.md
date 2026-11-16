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
<dt><code>-u &#8211;baseurl</code> &lt;url&gt;</dt>
<dd>Optional base URL location for all files.</dd>
<dt><code>-o &#8211;outputdir</code> &lt;url&gt;</dt>
<dd>Optional output directory (useful for read only media).</dd>
<dt><code>-x &#8211;excludes</code> &lt;package&gt;</dt>
<dd>File globs to exclude, can be specified multiple times.</dd>
<dt><code>-i &#8211;pkglist</code> &lt;filename&gt;</dt>
<dd>specify a text file which contains the complete list of files to include in the repository from the set found in the directory. File format is one package per line, no wildcards or globs.</dd>
<dt><code>-n &#8211;includepkg</code></dt>
<dd>specify pkgs to include on the command line. Takes urls as well as local paths.</dd>
<dt><code>-q &#8211;quiet</code></dt>
<dd>Run quietly.</dd>
<dt><code>-g &#8211;groupfile</code> &lt;groupfile&gt;</dt>
<dd>A precreated xml filename to point to for group information.<br />
 See examples section below for further explanation.</dd>
<dt><code>-v &#8211;verbose</code></dt>
<dd>Run verbosely.</dd>
<dt><code>-c &#8211;cachedir</code> &lt;path&gt;</dt>
<dd>Specify a directory to use as a cachedir. This allows createrepo to create a cache of checksums of packages in the repository. In consecutive runs of createrepo over the same repository of files that do not have a complete change out of all packages this decreases the processing time dramatically. </dd>
<dt><code>&#8211;update</code></dt>
<dd>If metadata already exists in the outputdir and an rpm is unchanged (based on file size and mtime) since the metadata was generated, reuse the existing metadata rather than recalculating it. In the case of a large repository with only a few new or modified rpms this can significantly reduce I/O and processing time. </dd>
<dt><code>&#8211;skip-stat</code></dt>
<dd>skip the stat() call on a &#8211;update, assumes if the filename is the same then the file is still the same (only use this if you&#8217;re fairly trusting or gullible). </dd>
<dt><code>-C &#8211;checkts</code></dt>
<dd>Don&#8217;t generate repo metadata, if their timestamps are newer than its rpms. This option decreases the processing time drastically again, if you happen to run it on an unmodified repo, but it is (currently) mutual exclusive with the &#8211;split option. NOTE: This command will not notice when packages have been removed from repo. Use &#8211;update to handle that. </dd>
<dt><code>&#8211;split</code></dt>
<dd>Run in split media mode. Rather than pass a single directory, take a set of directories corresponding to different volumes in a media set. </dd>
<dt><code>-p &#8211;pretty</code></dt>
<dd>Output xml files in pretty format.</dd>
<dt><code>-V &#8211;version</code></dt>
<dd>Output version.</dd>
<dt><code>-h &#8211;help</code></dt>
<dd>Show help menu. </dd>
<dt><code>-d &#8211;database</code></dt>
<dd>Generate sqlite databases for use with yum. This is now the default. </dd>
<dt><code>&#8211;no-database</code></dt>
<dd>Do not generate sqlite databases in the repository. </dd>
<dt><code>-S &#8211;skip-symlinks</code></dt>
<dd>Ignore symlinks of packages</dd>
<dt><code>-s &#8211;checksum</code></dt>
<dd>Choose the checksum type used in repomd.xml and for packages in the metadata. The default is now &quot;sha256&quot; (if python has hashlib). The older default was &quot;sha&quot;, which is actually &quot;sha1&quot;, however explicitly using &quot;sha1&quot; doesn&#8217;t work on older (3.0.x) versions of yum, you need to specify &quot;sha&quot;.</dd>
<dt><code>&#8211;profile</code></dt>
<dd>Output time based profiling information.</dd>
<dt><code>&#8211;changelog-limit</code> CHANGELOG_LIMIT</dt>
<dd>Only import the last N changelog entries, from each rpm, into the metadata</dd>
<dt><code>&#8211;unique-md-filenames</code></dt>
<dd>Include the file&#8217;s checksum in the metadata filename, helps HTTP caching (default) </dd>
<dt><code>&#8211;simple-md-filenames</code></dt>
<dd>Do not include the file&#8217;s checksum in the metadata filename. </dd>
<dt><code>&#8211;distro</code></dt>
<dd>Specify distro tags. Can be specified more than once. Optional syntax specifying a cpeid(<a rel="nofollow" href="http://cpe.mitre.org/)">http://cpe.mitre.org/)</a> &#8211;distro=cpeid,distrotag</dd>
<dt><code>&#8211;content</code></dt>
<dd>Specify keyword/tags about the content of the repository. Can be specified more than once.</dd>
<dt><code>&#8211;repo</code></dt>
<dd>Specify keyword/tags about the repository itself. Can be specified more than once.</dd>
<dt><code>&#8211;revision</code></dt>
<dd>Arbitrary string for a repository revision.</dd>
<dt><code>&#8211;deltas</code></dt>
<dd>Tells createrepo to generate deltarpms and the delta metadata</dd>
<dt><code>&#8211;oldpackagedirs</code> PATH</dt>
<dd>paths to look for older pkgs to delta against. Can be specified multiple times</dd>
<dt><code>&#8211;num-deltas</code> int</dt>
<dd>the number of older versions to make deltas against. Defaults to 1</dd>
<dt><code>&#8211;read-pkgs-list</code> READ_PKGS_LIST</dt>
<dd>output the paths to the pkgs actually read useful with &#8211;update</dd>
<dt><code>&#8211;max-delta-rpm-size</code> MAX_DELTA_RPM_SIZE</dt>
<dd>max size of an rpm that to run deltarpm against (in bytes)</dd>
<dt><code>&#8211;workers</code> WORKERS</dt>
<dd>number of workers to spawn to read rpms</dd>
<dt><code>&#8211;xz</code></dt>
<dd>use xz for repodata compression</dd>
<dd></dd></dl>
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
