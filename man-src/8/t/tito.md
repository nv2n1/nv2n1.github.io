---
title: "tito(8)"
name: "tito"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tito/"
description: "tito – manage RPM based projects using git"
---

<p>tito &#8211; manage RPM based projects using git</p>
<h2>Synopsis</h2>
<p>tito init </p>
<p> tito tag [OPTIONS] </p>
<p> tito build &#8211;test &#8211;rpm </p>
<p> tito build [OPTIONS] </p>
<p> tito release [OPTIONS] TARGET </p>
<p> tito report</p>
<h2>Description</h2>
<p>After setting up a directory as a Git repo, use tito to manage the tags and builds. A simple workflow may look like: </p>
<dl>
<dd>1. Save user preferences as described in <a href="/docs/linux/man/5-titorc/">titorc</a>(5)</dl>
<dl>
<dd>2. Initialize a .tito directory</dl>
<dl>
<dd>3. Test </p>
<dl>
<dd>1. Make changes to source</dl>
<dl>
<dd>2. Use git to commit changes</dl>
<dl>
<dd>3. Build: tito build &#8211;rpm &#8211;test</dl>
</dl>
<dl>
<dd>4. Finalize a release </p>
<dl>
<dd>1. Tag: tito tag</dl>
<dl>
<dd>2. Push: git push &amp;&amp; git push $ORIGIN $TAG</dl>
<dl>
<dd>3. Build: tito build [OPTIONS]</dl>
</dl>
<h2>Options</h2>
<h3>tito init</h3>
<p>This will create a top-level metadata directory called &quot;.tito/&quot; and commit it to git. This directory will store tito&#8217;s configuration and package metadata on a per branch basis. It will be filtered out when creating .tar.gz&#8217;s. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Your spec file should list the source as %{name}-%{version}.tar.gz </p>
</dl>
<h3>tito tag [options]</h3>
<p>By default, tito will tag by bumping the rpm version (i.e. we bump the Z in X.Y.Z). If you&#8217;d prefer to bump the package release instead (normally should just be used for changes to the spec file or patches applied within it), you can change the tagger class in .tito/tito.props to ReleaseTagger. This will affect all packages in this git branch; if you&#8217;d prefer to do this on a per-package basis you can do so in a package specific tito.props. </p>
<p> -h, &#8211;help</p>
<dl>
<dd>show this help message and exit</dl>
<p> &#8211;debug</p>
<dl>
<dd>print debug messages (can be also set using DEBUG environment variable)</dl>
<p> &#8211;offline</p>
<dl>
<dd>do not attempt any remote communication (avoid using this please)</dl>
<p> -o <i>OUTPUTDIR</i>, &#8211;output=<i>OUTPUTDIR</i></p>
<dl>
<dd>Write temp files, tarballs, and RPMs to <i>OUTPUTDIR</i>. Create sub-directories as needed by <a href="/docs/linux/man/8-rpmbuild/">rpmbuild</a>(8). (default /tmp/tito)</dl>
<p> &#8211;tag-release</p>
<dl>
<dd>Deprecated, no longer required.</dl>
<p> &#8211;keep-version</p>
<dl>
<dd>Use spec file version/release exactly as specified in spec file to tag package.</dl>
<p> &#8211;use-version=<i>USE_VERSION</i></p>
<dl>
<dd>Update the spec file with the specified version.</dl>
<p> &#8211;use-release=<i>USE_RELEASE</i></p>
<dl>
<dd>Update the spec file with the specified release.</dl>
<p> &#8211;no-auto-changelog</p>
<dl>
<dd>Don&#8217;t automatically create a changelog entry for this tag if none is found</dl>
<p> &#8211;accept-auto-changelog</p>
<dl>
<dd>Automatically accept the generated changelog.</dl>
<p> &#8211;auto-changelog-message=<i>MESSAGE</i></p>
<dl>
<dd>Use <i>MESSAGE</i> as the default changelog message for new packages</dl>
<p> &#8211;changelog=<i>MESSAGE</i></p>
<dl>
<dd>Use <i>MESSAGE</i> as the changelog when tagging, this can be specified every time a package is tagged. Useful when needing to generate custom changelogs. This will override the auto generated changelog.</dl>
<p> -u, &#8211;undo</p>
<dl>
<dd>Undo the most recent (un-pushed) tag.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Tito will create automatic changelog from git commits. Unless you specify one of auto options, tito will open text editor and allow you to edit the text. Editor is by default. This can be changes by environment variable EDITOR. </p>
</dl>
<h3>tito build [options]</h3>
<p>-h, &#8211;help</p>
<dl>
<dd>show this help message and exit</dl>
<p> &#8211;debug</p>
<dl>
<dd>print debug messages (can be also set using DEBUG environment variable)</dl>
<p> &#8211;offline</p>
<dl>
<dd>do not attempt any remote communication. Avoid using this please. See OFFLINE section below.</dl>
<p> -o <i>OUTPUTDIR</i>, &#8211;output=<i>OUTPUTDIR</i></p>
<dl>
<dd>Write temp files, tarballs and RPMs to <i>OUTPUTDIR</i>. (default /tmp/tito)</dl>
<p> &#8211;tgz</p>
<dl>
<dd>Build .tar.gz</dl>
<p> &#8211;srpm</p>
<dl>
<dd>Build srpm</dl>
<p> &#8211;rpm</p>
<dl>
<dd>Build srpm and rpm</dl>
<p> -i, &#8211;install</p>
<dl>
<dd>Install any binary RPMs being built.</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> uses sudo rpm -Uvh &#8211;force </p>
</dl>
<p> &#8211;no-sudo</p>
<dl>
<dd>Don&#8217;t escalate privileges when installing. Use when running this command with required privileges.</dl>
<p> &#8211;dist=<i>DISTTAG</i></p>
<dl>
<dd>Apply <i>DISTTAG</i> to srpm and/or rpm. (e.g., &quot;.el5&quot;)</dl>
<p> &#8211;test</p>
<dl>
<dd>use current branch HEAD instead of latest package tag.</dl>
<p> &#8211;no-cleanup</p>
<dl>
<dd>do not clean up temporary build directories/files</dl>
<p> &#8211;rpmbuild-options=<i>OPTIONS</i></p>
<dl>
<dd>Pass <i>OPTIONS</i> to rpmbuild.</dl>
<p> &#8211;builder=<i>BUILDER</i></p>
<dl>
<dd>Override the normal builder by specifying a full class path or one of the pre-configured shortcuts. Only useful if you need to override the default builder for some purpose, such as testing a build via mock.</dl>
<p> &#8211;arg=<i>BUILDER_ARGS</i></p>
<dl>
<dd>Custom arguments specific to a particular builder. (key=value)</dl>
<p> &#8211;scl=<i>COLLECTION</i></p>
<dl>
<dd>Build package for software collection. This is mostly useful for building src.rpm, because for rpm you want to define this option for specific tag in tito.props</dl>
<p> &#8211;quiet</p>
<dl>
<dd>Suppress output from the build process.</dl>
<p> &#8211;verbose</p>
<dl>
<dd>Expose more output from the build process.</dl>
<h3>tito release [options] TARGETS</h3>
<p>Runs the release targets defined in .tito/releasers.conf. </p>
<p> -h, &#8211;help</p>
<dl>
<dd>show this help message and exit</dl>
<p> &#8211;debug</p>
<dl>
<dd>print debug messages (can be also set using DEBUG environment variable)</dl>
<p> &#8211;offline</p>
<dl>
<dd>do not attempt any remote communication. Avoid using this please. See OFFLINE section below.</dl>
<p> -o <i>OUTPUTDIR</i>, &#8211;output=<i>OUTPUTDIR</i></p>
<dl>
<dd>Write temp files, tarballs and RPMs to <i>OUTPUTDIR</i>. (default /tmp/tito)</dl>
<p> &#8211;tag=<i>PKGTAG</i></p>
<dl>
<dd>build a specific tag instead of the latest version (e.g., spacewalk-java-0.4.0-1)</dl>
<p> &#8211;dry-run</p>
<dl>
<dd>Do not actually commit/push anything during release.</dl>
<p> &#8211;no-build</p>
<dl>
<dd>Do not perform a brew/koji build, only DistGit commit. (only for Koji/DistGit releasers)</dl>
<p> &#8211;all</p>
<dl>
<dd>Run all release targets defined in .tito/releasers.conf.</dl>
<p> &#8211;list</p>
<dl>
<dd>List all release targets defined in .tito/releasers.conf.</dl>
<p> &#8211;all-starting-with=ALL_STARTING_WITH</p>
<dl>
<dd>Run all release targets starting with the given string. (i.e. if you have defined release targets yum-f15 and yum-f14 in releasers.conf, &#8211;all-starting-with=yum will run only these targets, and ignore any others.)</dl>
<p> &#8211;scratch</p>
<dl>
<dd>Perform a scratch build in Koji. Can be specified using environment variable SCRATCH set to 1 as well.</dl>
<p> &#8211;yes</p>
<dl>
<dd>Do not ask to confirm release commits or edit their messages.</dl>
<h3>tito report [options]</h3>
<p>Display a report of all packages with differences between HEAD and their most recent tag, as well as a patch for that diff. Used to determine which packages are in need of a rebuild. </p>
<p> -h, &#8211;help</p>
<dl>
<dd>show this help message and exit</dl>
<p> &#8211;debug</p>
<dl>
<dd>print debug messages (can be also set using DEBUG environment variable)</dl>
<p> &#8211;offline</p>
<dl>
<dd>do not attempt any remote communication. Avoid using this please. See OFFLINE section below.</dl>
<p> -o <i>OUTPUTDIR</i>, &#8211;output=<i>OUTPUTDIR</i></p>
<dl>
<dd>Write temp files, tarballs and RPMs to <i>OUTPUTDIR</i>. (default /tmp/tito)</dl>
<p> &#8211;untagged-diffs</p>
<dl>
<dd>Print out diffs for all packages with changes between their most recent tag and HEAD. Useful for determining which packages are in need of a re-tag.</dl>
<p> &#8211;untagged-commits</p>
<dl>
<dd>Print out the list for all packages with changes between their most recent tag and HEAD. Useful for determining which packages are in need of a re-tag.</dl>
<h2>Offline</h2>
<p>Offline lets you potentially do builds you can&#8217;t reproduce, normally we check that the tag you&#8217;re building exists in the remote repo. If it hasn&#8217;t been pushed, it&#8217;s quite easy to do a build that will result in a checksum that is no longer the same. This is something you should try to avoid.</p>
<h2>Examples</h2>
<p>Build and install a test package from the latest code in current git HEAD</p>
<dl>
<dd>tito build &#8211;rpm &#8211;test -i</dl>
<p> Overriding the default builder to build via mock instead</p>
<dl>
<dd>tito build &#8211;builder mock &#8211;arg mock=fedora-15-x86_64 &#8211;rpm</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-titorc/">titorc</a>(5) <a href="/docs/linux/man/5-releasers-conf/">releasers.conf</a>(5) <a href="/docs/linux/man/5-tito-props/">tito.props</a>(5) </p>
<p> /usr/share/doc/tito-*/README.mkd</p>
<h2>Authors</h2>
<p>Devan Goodwin &lt;dgoodwin [at] rm-rf.ca&gt; </p>
<p> James Bowes &lt;jbowes [at] repl.ca&gt; </p>
<p> Jan Pazdziora </p>
<p> Jesus M Rodriguez &lt;jesusr [at] redhat.com&gt; </p>
<p> Pall Sigurdsson &lt;palli [at] opensource.is&gt; </p>
<p> Miroslav Suchý &lt;msuchy [at] redhat.com&gt; </p>
<p> and: Adam Miller, Alex Wood, Aron Parsons, Brenton Leanhardt, Ivan Nečas, John Eckersberg, Kenny MacDermid, Lukáš Zapletal, Luke Meyer, Marian Csontos, Martin Bačovský, Michael Stead, Mike McCune, mscherer, Paul Morgan, Sean P. Kane, Steve <i>Ashcrow</i> Milner</p>
