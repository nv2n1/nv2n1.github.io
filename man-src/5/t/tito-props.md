---
title: "tito-props(5)"
name: "tito-props"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tito-props/"
---

tito.props - directives for 

<a HREF="/docs/linux/man/5-tito/">tito</a>(5) how to build package.

<h2>Synopsis</h2>

None

<h2>Description</h2>

Project settings can be stored in files: 

 GITROOT/.tito/tito.props 

 GITROOT/SOME/PACKAGE/tito.props 

 The global .tito/tito.props is generally where settings are defined. For some multi-project git repositories, individual packages can override these settings by placing a tito.props in the project directory. (i.e. same location as it's .spec file)

<h2>Sections</h2>

tito.props can contain several sections:

<h2>Buildconfig</h2>

This section and a couple of it's properties are required. You can use following variables: 

 builder
<dl><dd>The fully qualified Builder class implementation to use. You can either specify builders shipped with <a HREF="/docs/linux/man/5-tito/">tito</a>(5) (see BUILDERS section below), or a custom builder located within the directory your lib_dir option points to. This property is required.</dl>
 

 tagger
<dl><dd>The fully qualified Tagger class implementation to use. You can either specify taggers shipped with <a HREF="/docs/linux/man/5-tito/">tito</a>(5) (see TAGGERS section below), or a custom tagger located within the directory your lib_dir option points to. This property is required.</dl>
 

 lib_dir
<dl><dd>Optional property defining a directory to be added to the Python path when executing tito. Allows you to store custom implementations of Builder, Tagger, and Releaser.</dl>
 

 changelog_format
<dl><dd>This option is used to control the formatting of entries when generating changelog entries. The default value is &quot;%s (%ae)&quot;. See PRETTY FORMATS in <a HREF="/docs/linux/man/1-git-log/">git-log</a>(1) for more information.</dl>
 

 changelog_with_email
<dl><dd>If set to 0, then entries in changelog (subject of commits) are not followed by email of committer. Default is 1. This option is deprecated and provided for backwards-compatibility only. New configurations should consider changelog_format instead.</dl>
 

 changelog_do_not_remove_cherrypick
<dl><dd>If set to 0, it will not remove from cherry picked commits the part &quot;(cherry picked from commit ...)&quot;</dl>
 

 tag_suffix
<dl><dd>An optional specification of a suffix to append to all tags created by tito for this repo. Can be useful for situations where one git repository is inheriting from another, but tags are created in both. The suffix will be an indicator as to which repo the tag originated in. (i.e. tag_suffix = -mysuffix)</dl>
 

 tag_commit_message_format
<dl><dd>This option is used control the text of git commit message that is used when new tag is generated. You can use &quot;%(name)s&quot;, &quot;%(release_type)s&quot; and &quot;%(version)s&quot; placeholders.</dl>

<h2>Koji And Copr</h2>

disttag
<dl><dd>Dist tag variable, which is passed to rpmbuild for packages build in this tag.</dl>
 

 blacklist
<dl><dd>Space separated list of packages, which should not be built in this tag.</dl>
 

 whitelist
<dl><dd>If whitelist is present, only packages listed here can be built in this tag. This also override blacklist.</dl>
 

 scl
<dl><dd>Specify name of Software Collection into which package should be build.</dl>

<h2>Version_Template</h2>

Allows the user to write out a template file containing version and/or release and add it to git during the tagging process. 

 template_file
<dl><dd>Path to a file conforming to a Python string.Template, as described at <a rel="nofollow" HREF="http://docs.python.org/2/library/string.html#template-strings.">http://docs.python.org/2/library/string.html#template-strings.</a> Path is relative to root of the entire git checkout, as this is likely to be stored in the top level .tito directory. The variables $version and $release are available inside the template.</dl>
 

 destination_file
<dl><dd>Specifies a file to write, relative to the directory for the package being tagged.</dl>
 

 Example: 

<dl><dd><pre>[version_template]
destination_file = version.txt
template_file = .tito/templates/version.rb</pre></dl>

<h2>Requirements</h2>

tito
<dl><dd>If tito is older then specified version, it will refuse to continue.</dl>

<h2>Tagconfig</h2>

require_package
<dl><dd>Comma separated list of packages, which needs to be installed prior tagging. If those packages are not installed, tito will refuse to continue.</dl>

<h2>Builders</h2>

tito.builder.Builder
<dl><dd>Basic package builder. It create tar.gz of whole directory and create src.rpm and build rpm using some supported method.</dl>
 

 tito.builder.NoTgzBuilder
<dl><dd>Builder for packages that do not require the creation of tarball. Usually these package have source files checked directly into git.</dl>
 

 tito.builder.UpstreamBuilder
<dl><dd>Builder for packages that are based off an upstream git tag. Commits applied in downstream git become patches applied to the upstream tarball. For example - you are building package foo-1.2-3... Tar.gz file is created from commit, which is tagged by foo-1.2-1 and the diff between release 1 and 3 is put in spec file as Patch0.</dl>
 

 tito.builder.GemBuilder
<dl><dd>Builder for packages that list a .gem as Source0, the .gemspec shares a directory hierarchy with the .spec file and the upstream does not want to check .gem files into their git repository.</dl>
 

 tito.distributionbuilder.DistributionBuilder
<dl><dd>Behave similar as tito.builder.UpstreamBuilder, but patch is created for every release. Therefore package from previous example will end up with tar.gz file created from tag foo-1.2-1 and with Patch0: foo-1.2-1-to-foo-1.2-2.patch Patch1: foo-1.2-1-to-foo-1.2-3.patch</dl>
 

 tito.builder.FetchBuilder
<dl><dd>See doc/builders.mkd.</dl><dl><dd><pre>[builder]
fetch_strategy = tito.builder.fetch.ArgSourceStrategy</pre></dl>
 

 ArgSourceStrategy here could be replaced with a custom strategy if you were to have one in your lib_dir. 

 tito.builder.GitAnnexBuilder
<dl><dd>See doc/builders.mkd.</dl>
 

 Builder for packages with existing tarballs checked in using git-annex, e.g. referencing an external source (web remote). This builder will &quot;unlock&quot; the source files to get the real contents, include them in the SRPM, then restore the automatic git-annex symlinks on completion.

<h2>Taggers</h2>

All taggers which inherit from tito.tagger.VersionTagger (all to this date), will update file GITROOT/.tito/packages/name-of-package and put there one line which consist of version-release of package, space delimiter, path to package directory relative to GITROOT. 

 tito.tagger.VersionTagger
<dl><dd>Standard tagger class, used for tagging packages build from source in git. Release will be tagged by incrementing the package version, and the actual &quot;Release&quot; will be always set to 1.</dl>
 

 tito.tagger.ReleaseTagger
<dl><dd>Keep version and increment release.</dl>
 

 tito.zstreamtagger.zStreamTagger
<dl><dd>It is used for EUS packages.</dl>
 

 tito.rheltagger.RHELTagger
<dl><dd>Tagger which is based on ReleaseTagger and uses Red Hat Enterprise Linux changelog format: 

<dl><dd>&bull; Resolves: #1111 - description</dl><dl><dd>&bull; Related: #1111 - description</dl></dl>

<h2>Releaser</h2>

You can create section with the name same as releaser target and there you can specify this option: 

 remote_git_name
<dl><dd>This is useful for FedoraGitReleaser and DistGitReleaser and will allow you to specify name of remote dist-git branch. 

 For example let say you have in releaser.conf: [git-sat] releaser = tito.release.DistGitReleaser branches = satellite-6.0-rhel-6 

 and then in package directory you can create tito.props with content: [git-sat] remote_git_name = ruby193-rubygem-simple-navigation And it will push package into ruby193-rubygem-simple-navigation dist-git despite the fact that it is in /rubygem-simple-navigation directory. And project name (as taken from spec file) is rubygem-simple-navigation.</dl>

<h2>Example</h2>

<dl><dd><pre>[buildconfig]
builder = tito.builder.Builder
tagger = tito.tagger.VersionTagger</pre></dl><dl><dd><pre>[koji]
autobuild_tags = dist-5E-sw-1.2-candidate dist-f12-sw-1.2-candidate dist-f13-sw-1.2-candidate</pre></dl><dl><dd><pre>[dist-5E-sw-1.2-candidate]
disttag = .el5</pre></dl><dl><dd><pre>[dist-f12-sw-1.2-candidate]
disttag = .fc12
blacklist=jabberd-selinux</pre></dl><dl><dd><pre>[dist-f13-sw-1.2-candidate]
disttag = .fc13
blacklist=jabberd-selinux</pre></dl><dl><dd><pre>[requirements]
tito=0.3.0</pre></dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-tito/">tito</a>(8) <a HREF="/docs/linux/man/5-titorc/">titorc</a>(5)

<h2>Authors</h2>

Devan Goodwin &lt;dgoodwin [at] rm-rf.ca&gt; 

 James Bowes &lt;jbowes [at] repl.ca&gt; 

 Jan Pazdziora 

 Jesus M Rodriguez &lt;jesusr [at] redhat.com&gt; 

 Pall Sigurdsson &lt;palli [at] opensource.is&gt; 

 Miroslav Suchý &lt;msuchy [at] redhat.com&gt; 

 and: Adam Miller, Alex Wood, Aron Parsons, Brenton Leanhardt, Ivan Nečas, John Eckersberg, Kenny MacDermid, Lukáš Zapletal, Luke Meyer, Marian Csontos, Martin Bačovský, Michael Stead, Mike McCune, mscherer, Paul Morgan, Sean P. Kane, Steve <i>Ashcrow</i> Milner
