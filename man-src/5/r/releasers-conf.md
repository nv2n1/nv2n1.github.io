---
title: "releasers-conf(5)"
name: "releasers-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-releasers-conf/"
description: "releasers.conf – Config file defining release targets where builds can be published."
---

<p>releasers.conf &#8211; Config file defining release targets where builds can be published.</p>
<h2>Synopsis</h2>
<p>None</p>
<h2>Description</h2>
<p>Tito allows projects to define their own release targets, which can specify the exact releaser implementation to use (potentially a custom one), and any arguments it may need for a specific type of build.</p>
<h2>Releasers</h2>
<p>Tito includes several releaser implementations that can be used in releasers.conf. Additionally you may define a lib_dir in your tito.props globalconfig section, and place your own custom implementation of a releaser there. </p>
<p> Specify &quot;builder.test = 1&quot; in your releasers.conf target to enable &#8211;test builds. (uses the latest git HEAD rather than the latest tagged package) This can be useful for automating the publishing of a nightly build, which you would not want to continually have to tag. </p>
<p> tito.release.YumRepoReleaser</p>
<dl>
<dd>Releaser which will build your packages, rsync down an existing yum repository, place your packages in it, regenerate the yum repodata, and rsync the yum repository back up. </p>
<p> Requires the &quot;srpm_disttag = .fc21&quot; to specify the disttag on the resulting source RPM. This allows for a correct srpm to upload, and prevents problems with it getting clobbered when building for &quot;newer&quot; disttags. </p>
<p> Specify &quot;filetypes = srpm&quot; if you want to build a source rpm instead of a regular rpm. </p>
<p> Specify &quot;createrepo_command = createrepo -s sha1&quot; if you are building on a recent distro and are working with yum repositories for rhel5. </p>
<p> You can use environment variable RSYNC_USERNAME to override rsync username.</dl>
<p> tito.release.RsyncReleaser</p>
<dl>
<dd>Releaser which will build your packages, and rsync up to a remote repository. </p>
<p> Specify &quot;filetypes = rpm srpm tgz&quot; to choose what type of packages will be uploaded. </p>
<p> You can use environment variable RSYNC_USERNAME to override rsync username. </p>
<p> Specify &quot;scl = COLLECTION&quot; to build into Software Collection. Deprecated, prefer &quot;builder.scl = COLLECTION&quot; instead. </p>
<p> Variable &quot;rsync_args&quot; can specify addiontal argument passed to rsync. Default is &quot;-rlvz&quot;.</dl>
<p> tito.release.FedoraGitReleaser</p>
<dl>
<dd>Releaser which will checkout your project in Fedora git using fedpkg. Sources are then synced to the first branch your releaser lists. After this tito will git merge the first branch into all other listed branches, triggering builds in each. </p>
<p> The <i>required_bz_flags</i> property can be specified to have tito check Red Hat Bugzilla to see if each bug number extracted from the changelog has appropriate flags. If it does not, it will be skipped in the commit message. If no bugs are found with the required tags, a <i>placeholder_bz</i> can be specified (see below), otherwise the release will abort. </p>
<p> The <i>placeholder_bz</i> property can be specified to use if no bugs were found in the changelog with the required flags. </p>
<dl>
<dd>
<pre>[fedora-git]
releaser = tito.release.FedoraGitReleaser
branches = master el5 el6 f14 f15 f16
required_bz_flags = myos-1.1.0+ pm_ack+
placeholder_bz = 100000</pre>
</dl>
<p> If you would like to build (ie &#8211; koji) against a different target than what is default for the FedoraGit/DistGit branch currently being worked on it can be done like the following example. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The formatting of build_targets in the following example is git_branch:koji_build_target and the following custom build targets are just place holders for the example and aren&#8217;t likely to exist in Fedora&#8217;s koji </p>
</dl>
<dl>
<dd>
<pre>[fedora-git-custom-target]
releaser = tito.release.FedoraGitReleaser
branches = master el6 f19
build_targets = master:custom-target el6:el6-custom-target f19:f19-custom-target</pre>
</dl>
</dl>
<p> tito.release.DistGitReleaser</p>
<dl>
<dd>Same as FedoraGitReleaser, but use rhpkg instead of fedpkg.</dl>
<p> tito.release.KojiReleaser</p>
<dl>
<dd>Releaser which create src.rpm and submit them into Koji. Can submit more than one build at once. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This is targeted for private instances of Koji. You can not submit regular build into Fedora Koji using this releaser, because Fedora Koji do not allow builds from src.rpm &#8211; for building into Fedora see FedoraGitReleaser above. </p>
</dl>
<dl>
<dd>
<pre>[koji]
releaser = tito.release.KojiReleaser
autobuild_tags = my-koji-tag-rhel6 my-koji-tag-fedora18</pre>
</dl>
<p> In this example, releaser will create src.rpm according the definition of [my-koji-tag-rhel6] in tito.props. You usually want to set up there at least disttag. See KOJI section in <a href="/docs/linux/man/5-tito-props/">tito.props</a>(5). </p>
<p> If &#8211;scratch option or SCRATCH environment variable is set, package is build as scratch in Koji. </p>
<p> You can specify KOJI_OPTIONS in <a href="/docs/linux/man/5-titorc/">titorc</a>(5) and it is passed to koji command as option. Usually you want to specify at least &#8211;config option. </p>
<p> Variable autobuild_tags is required for KojiReleaser.</dl>
<p> tito.release.KojiGitReleaser</p>
<dl>
<dd>Build into Koji through dist-git. It behaves as KojiReleaser. Only difference is that src.rpm is not passed to Koji. Instead is sent to koji git hash from which Koji should build package. </p>
<p> Note: This feature is not in upstream Koji (although is submited for long time). </p>
<p> Please do not confuse with FedoraGitReleaser. KojiGitReleaser is intended for private instances of Koji. </p>
<p> You need to specify git_url, which specify url of git repository. This url needs to be reachable from Koji.</dl>
<p> tito.release.ObsReleaser</p>
<dl>
<dd>Build into Open Build Service using osc command. </p>
<p> You must specify &quot;project_name&quot; in config. You can optionaly specify &quot;package_name&quot;, but if it is not present name of package directory is used. </p>
<p> This releaser assume that you have ~/.oscrc correctly configured.</dl>
<p> tito.release.CoprReleaser</p>
<dl>
<dd>This releaser submits your src.rpm to Copr. </p>
<dl>
<dd>
<pre>[my-copr]
releaser = tito.release.CoprReleaser
project_name = my-copr-project-name
upload_command = scp %(srpm)s my.web.com:public_html/my_srpm/
remote_location = <a rel="nofollow" href="http://my.web.com/~msuchy/my_srpm/">http://my.web.com/~msuchy/my_srpm/</a>
copr_options = --timeout 600</pre>
</dl>
</dl>
<p> Variables are: </p>
<dl>
<dd>&bull; project_name &#8211; this is name of your project on Copr</dl>
<dl>
<dd>&bull; upload_command &#8211; this command is executed to upload src.rpm to internet. It can be scp, rsync or just cp. It may containt string &quot;%(srpm)s&quot; (even several times), which is substitued by real srpm path. (optional)</dl>
<dl>
<dd>&bull; remote_location &#8211; how can be accessed the location above over www. (optional)</dl>
<dl>
<dd>&bull; copr_options &#8211; space separated options to pass directly to copr-cli build. Defaults to &#8211;nowait. (optional)</dl>
<p> The releaser will publish your src.rpm to remote server and then submit it into Copr via URL. If you rather want to submit the package directly from your computer, just omit &quot;upload_command&quot; and &quot;remote_location&quot; variables. </p>
<p> Project_name behave exactly as &quot;autobuild_tags&quot; in KojiReleaser, and you can define various options for each project name in tito.props (e.g. disttag, whitelist, blacklist, scl). For more information see man page of tito.props. </p>
<p> Note: this releaser assume you have copr-cli correctly configured. See API KEY section in copr-cli man page.</p>
<h2>Example</h2>
<dl>
<dd>
<pre>; Release into fedora-15-x86_64 yum repo
[yum-f15-x86_64]
releaser = tito.release.YumRepoReleaser
srpm_disttag = .fc15
builder = tito.builder.MockBuilder
builder.mock = fedora-15-x86_64
rsync = fedorapeople.org:/srv/repos/dgoodwin/tito/fedora-15/x86_64/ fedorapeople.org:/srv/repos/dgoodwin/tito/fedora-15/x86_64/</pre>
</dl>
<dl>
<dd>
<pre>; Release into el6 yum repository. specify builder.test=1 so that
; we build on latest commit (instead of latest tito tag)
[yum-el6-x86_64]
releaser = tito.release.YumRepoReleaser
srpm_disttag = .el6
builder = tito.builder.MockBuilder
builder.mock = epel-6-x86_64
builder.test = 1
scl = ruby193
rsync = remoteserver.org:/srv/repos/el6/testing/x86_64</pre>
</dl>
<dl>
<dd>
<pre>; Upload into source repository
[yum-fc15-sources]
releaser = tito.release.YumRepoReleaser
srpm_disttag = .fc15
builder = tito.builder.MockBuilder
builder.mock = fedora-15-x86_64
filetypes = srpm
rsync = remoteserver.org:/srv/repos/fedora-15/SRPMS</pre>
</dl>
<dl>
<dd>
<pre>; el5 yum repository. Overloading createrepo_command to make
; el5 compatible repo.
[yum-el5-i386]
releaser = tito.release.YumRepoReleaser
srpm_disttag = .el5
builder = tito.builder.MockBuilder
builder.mock = epel-5-i386
createrepo_command = createrepo -s sha1
rsync = remoteserver.org:/srv/repos/rhel5/i386</pre>
</dl>
<dl>
<dd>
<pre>; rsync tgz file to remote site with custom rsync arguments
[rsync]
releaser = tito.release.RsyncReleaser
srpm_disttag = .fc15
builder = tito.builder.MockBuilder
builder.mock = fedora-15-x86_64
filetypes = tgz
rsync = remoteserver.org:/srv/tarballs/
rsync_args = -rlvzpt</pre>
</dl>
<dl>
<dd>
<pre>; Release using OBS
[obs-project]
releaser=tito.release.ObsReleaser
project_name=home:xsuchy</pre>
</dl>
<dl>
<dd>
<pre>; Upload src.rpm to remote server and then submit it into Copr via URL
[copr-project]
releaser = tito.release.CoprReleaser
project_name = my-copr-project-name another-project
upload_command = cp %(srpm)s /home/msuchy/public_html/my_srpm/
remote_location = <a rel="nofollow" href="http://my.web.com/~msuchy/my_srpm/">http://my.web.com/~msuchy/my_srpm/</a></pre>
</dl>
<dl>
<dd>
<pre>; Submit src.rpm from your computer directly to Copr
[copr-project]
releaser = tito.release.CoprReleaser
project_name = my-copr-project-name another-project</pre>
</dl>
<dl>
<dd>
<pre>; Submit src.rpm from your computer directly to Copr, timeout after 10 minutes
[copr-project]
releaser = tito.release.CoprReleaser
project_name = my-copr-project-name another-project
copr_options = --timeout 600</pre>
</dl>
