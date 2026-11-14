---
title: "copr-cli(1)"
name: "copr-cli"
section: "1"
letter: "c"
url: "/docs/linux/man/1-copr-cli/"
---

<h2 class="name">NAME</h2>
 

 copr-cli - command line interface for the Copr service 

<h2>SYNOPSIS</h2>

 

 copr-cli [-h] [--version] [--config CONFIG] {list,create,build} ...

<h2>DESCRIPTION</h2>

 

 This command allows you to interact with the Copr service from the command line. 

 You need to generate an API key first (see the API KEY section below).

<h2>OPTIONS</h2>

 

 -h, --help
<dl>
<dt>
<dd> show this help message and exit</dl>
 

 --version
<dl>
<dt>
<dd> show the program's version number and exit</dl>
 

 --config
<dl>
<dt>
<dd> path to an alternative configuration file (default is ~/.config/copr).</dl>

<h2>ACTION LIST</h2>

 

 list [username|@groupname]
<dl>
<dt>
<dd> List all the projects of the provided username. If no username is provided, then your projects are listed.</dl>
 

 create
<dl>
<dt>
<dd> Create a new project.</dl>
 

 delete
<dl>
<dt>
<dd> Delete an entire project.</dl>
 

 build
<dl>
<dt>
<dd> Build packages for a specified project.</dl>
 

 status
<dl>
<dt>
<dd> Get the status of the build.</dl>
 

 cancel
<dl>
<dt>
<dd> Cancel a build of given id.</dl>
 

 download-build
<dl>
<dt>
<dd> Download a build to local directory.</dl>
 

 modify
<dl>
<dt>
<dd> Modify existing copr</dl>
 

 add-package-*
<dl>
<dt>
<dd> Add a new package of the specified source type (e.g. add-package-tito)</dl>
 

 edit-package-*
<dl>
<dt>
<dd> Edit source definition and type of an existing package (e.g. edit-package-tito)</dl>
 

 list-packages
<dl>
<dt>
<dd> List all packages from a copr in json format</dl>
 

 list-package-names
<dl>
<dt>
<dd> Output just the package names from the given copr</dl>
 

 get-package
<dl>
<dt>
<dd> Display details of a single package in json format</dl>
 

 delete-package
<dl>
<dt>
<dd> Remove package from a copr and all its builds as well</dl>
 

 reset-package
<dl>
<dt>
<dd> Clear source definition of a package and its source type</dl>
 

 build-package
<dl>
<dt>
<dd> Build package from its source definition</dl>
 

 mock-config
<dl>
<dt>
<dd> Get the mock profile (similar to koji mock-config)</dl>

<h2>PROJECT ACTIONS</h2>

<h3>copr-cli create [options]</h3>

 

 usage: copr-cli create [-h] --chroot CHROOTS [--repo REPOS] [--initial-pkgs PKGS] [--description DESCRIPTION] [--instructions INSTRUCTIONS] [--disable_createrepo DISABLE_CREATEREPO] [--enable-net {on,off}] [--unlisted-on-hp {on,off}] [--persistent] [--auto-prune {on,off}] name 

 --chroot
<dl>
<dt>
<dd> Chroot to use for this project. Can be specified multiple times, but at least one must be present.</dl>
 

 --repo
<dl>
<dt>
<dd> Repository to add to this project. Can be specified multiple times.</dl>
 

 --initial-pkgs
<dl>
<dt>
<dd> List of packages to build in this new project. Can be specified multiple times.</dl>
 

 --description
<dl>
<dt>
<dd> Description of the project.</dl>
 

 --instructions
<dl>
<dt>
<dd> Instructions for the project.</dl>
 

 --disable_createrepo
<dl>
<dt>
<dd> Disables automatic repository metadata generation. Accepted values for DISABLE_CREATEREPO: true/false.</dl>
 

 --enable-net
<dl>
<dt>
<dd> If net should be enabled for builds in this project.</dl>
 

 --unlisted-on-hp
<dl>
<dt>
<dd> This project will not be listed on COPR home page.</dl>
 

 --persistent
<dl>
<dt>
<dd> Project and its builds will be undeletable. This option can only be specified by a COPR admin.</dl>
 

 --auto-prune
<dl>
<dt>
<dd> If backend auto-prunning script should be run for this project. This option can only be specified by a COPR admin.</dl>
 

 name
<dl>
<dt>
<dd> Can be just name of the project or in form username/projectname or @groupname/projectname.</dl>

<h3>copr-cli modify [options]</h3>

 

 usage: copr-cli modify [-h] [--repo REPOS] [--description DESCRIPTION] [--instructions INSTRUCTIONS] [--disable_createrepo DISABLE_CREATEREPO] [--enable-net {on,off}] [--unlisted-on-hp {on,off}] [--auto-prune {on,off}] name 

 Alters only specified project property. 

 --repo
<dl>
<dt>
<dd> Repository to add to this project. Can be specified multiple times.</dl>
 

 --description
<dl>
<dt>
<dd> Description of the project.</dl>
 

 --instructions
<dl>
<dt>
<dd> Instructions for the project.</dl>
 

 --disable_createrepo
<dl>
<dt>
<dd> Disables automatic repository metadata generation. Accepted values for DISABLE_CREATEREPO: true/false.</dl>
 

 --enable-net
<dl>
<dt>
<dd> If net should be enabled for builds in this project.</dl>
 

 --unlisted-on-hp
<dl>
<dt>
<dd> This project will not be listed on COPR home page.</dl>
 

 --auto-prune
<dl>
<dt>
<dd> If backend auto-prunning script should be run for this project. This option can only be specified by a COPR admin.</dl>
 

 name
<dl>
<dt>
<dd> Can be just name of the project or in form username/projectname or @groupname/projectname.</dl>

<h2>BUILD ACTIONS</h2>

<h3>copr-cli build [options]</h3>

 

 usage: copr-cli build [-h] [-r, --chroot CHROOTS] [--memory MEMORY] [--timeout TIMEOUT] [--nowait] [--background] project PKG [PKG ...] 

 -r, --chroot
<dl>
<dt>
<dd> If you don't need this build for all the project's chroots. You can use it several times for each chroot you need.</dl>
 

 --memory
<dl>
<dt>
<dd> Override memory for this build. This is actually not used and it have no effect.</dl>
 

 --timeout
<dl>
<dt>
<dd> Override timeout for this build. This is actually not used and it have no effect.</dl>
 

 --nowait
<dl>
<dt>
<dd> Don't wait for build completion.</dl>
 

 --background
<dl>
<dt>
<dd> Run the build at a lower priority.</dl>
 

 project
<dl>
<dt>
<dd> The project build the package in. This can be a simple name of some of your projects. Alternatively, you can specify it as username/project or @groupname/project. This way you can build into the project of another user or group, provided you have the permissions to do so.</dl>
 

 PKG
<dl>
<dt>
<dd> This can be either file on your local workstation or URL of the package to build. When URL is used, then the package must be placed on a public web or ftp server. Note that you cannot combine local file paths and URLs in one command line and local-file builds are limited to the first specified PKG. This limitation comes from the COPR API.</dl>

<h3>copr-cli buildpypi [options]</h3>

 

 usage: copr buildpypi [-h] [-r, --chroot CHROOTS] [--memory MEMORY] [--timeout TIMEOUT] [--nowait] [--background] [--pythonversions [VERSION [VERSION ...]]] [--packageversion PYPIVERSION] --packagename PYPINAME project 

 --pythonversions [VERSION [VERSION ...]]
<dl>
<dt>
<dd> For what Python versions to build (by default: 3 2)</dl>
 

 --packageversion PYPIVERSION
<dl>
<dt>
<dd> Version of the PyPI package to be built (by default latest)</dl>
 

 --packagename PYPINAME
<dl>
<dt>
<dd> Name of the PyPI package to be built, required.</dl>
 

 For the rest of the arguments, see copr-cli build command above.

<h3>copr-cli buildtito [options]</h3>

 

 usage: copr buildtito [-h] [--memory MEMORY] [--timeout TIMEOUT] [--nowait] [--background] [-r CHROOTS] [--git-url URL] [--git-dir DIRECTORY] [--git-branch BRANCH] [--test] project 

 --git-url URL
<dl>
<dt>
<dd> Url to a project managed by Tito, required.</dl>
 

 --git-dir DIRECTORY
<dl>
<dt>
<dd> Relative path from Git root to directory containing .spec file.</dl>
 

 --git-branch BRANCH
<dl>
<dt>
<dd> Checokut specific branch on the repository.</dl>
 

 --test
<dl>
<dt>
<dd> To build from the last commit instead of the last release tag.</dl>
 

 For the rest of the arguments, see copr-cli build command above.

<h3>copr-cli buildmock [options]</h3>

 

 usage: copr buildmock [-h] [--memory MEMORY] [--timeout TIMEOUT] [--nowait] [--background] [-r CHROOTS] [--scm-type TYPE] [--scm-url URL] [--scm-branch BRANCH] [--spec FILE] project 

 --scm-type TYPE
<dl>
<dt>
<dd> Specify versioning tool, default is <i>git</i>.</dl>
 

 --scm-url URL
<dl>
<dt>
<dd> Url to a project versioned by Git or SVN, required.</dl>
 

 --scm-branch BRANCH
<dl>
<dt>
<dd> Checokut specific branch on the repository.</dl>
 

 --spec FILE
<dl>
<dt>
<dd> Relative path from SCM root to .spec file, required.</dl>
 

 For the rest of the arguments, see copr-cli build command above.

<h3>copr-cli buildfedpkg [options]</h3>

 

 usage: copr buildfedpkg [-h] [--memory MEMORY] [--timeout TIMEOUT] [--nowait] [--background] [-r CHROOTS] [--clone-url URL] [--branch BRANCH] project 

 --clone-url URL
<dl>
<dt>
<dd> Specify clone url to the dist-git project on pkgs.fedoraproject.org.</dl>
 

 --branch BRANCH
<dl>
<dt>
<dd> Specify branch in the dist-git project to be be built from.</dl>
 

 For the rest of the arguments, see copr-cli build command above.

<h3>copr-cli download-build [options]</h3>

 

 usage: copr-cli download-build [-h] [-d, --dest DESTINATION] [-r, --chroot CHROOT] build_id 

 build_id
<dl>
<dt>
<dd> Download built packages for build identified by build_id.</dl>
 

 -d, --dest, -r, --chroot
<dl>
<dt>
<dd> Fetch only selected chroots. Can be specified multiple times.\</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> <pre>
copr-cli build myproject some.src.rpm
copr-cli build someone_else/project some.src.rpm
copr-cli build -r fedora-24-x86_64 -r fedora-24-i386 &quot;@somegroup/project&quot; some.src.rpm
</pre></dl>

<h2>CHROOT ACTIONS</h2>

<h3>copr-cli edit-chroot [options] coprchroot</h3>

 

 usage: copr edit-chroot [-h] [--upload-comps FILEPATH | --delete-comps] [--packages PACKAGES] [--repos REPOS] coprchroot 

 Edit the specified coprchroot. 

 coprchroot
<dl>
<dt>
<dd> Path to a project chroot as owner/project/chroot or project/chroot</dl>
 

 --upload-comps FILEPATH
<dl>
<dt>
<dd> Filepath to the comps.xml file to be uploaded</dl>
 

 --delete-comps
<dl>
<dt>
<dd> Deletes already existing comps.xml for the chroot</dl>
 

 --packages PACKAGES
<dl>
<dt>
<dd> space separated string of package names to be added to buildroot (e.g. &quot;gcc ghc&quot;)</dl>
 

 --repos REPOS
<dl>
<dt>
<dd> space separated string of additional repo urls for chroot (e.g. &quot;<a rel="nofollow" HREF="http://foo">http://foo</a> <a rel="nofollow" HREF="http://bar">http://bar</a>&quot;)</dl>

<h3>copr-cli get-chroot coprchroot</h3>

 

 usage: copr get-chroot [-h] coprchroot 

 Print info of the given chroot. 

 coprchroot
<dl>
<dt>
<dd> Path to a project chroot as owner/project/chroot or project/chroot</dl>

<h2>PACKAGE ACTIONS</h2>

<h3>copr-cli add-package-tito [options]</h3>

 

 usage: copr add-package-tito [-h] --git-url URL [--git-dir DIRECTORY] [--git-branch BRANCH] [--test {on,off}] --name PKGNAME [--webhook-rebuild {on,off}] project 

 Add package of <i>Tito</i> source type. 

 --git-url URL
<dl>
<dt>
<dd> URL to a project managed by Tito</dl>
 

 --git-dir DIRECTORY
<dl>
<dt>
<dd> Relative path from Git root to directory containing .spec file</dl>
 

 --git-branch BRANCH
<dl>
<dt>
<dd> Git branch that you want to build from</dl>
 

 --test {on,off}
<dl>
<dt>
<dd> Build the last commit instead of the last release tag</dl>
 

 --name PKGNAME
<dl>
<dt>
<dd> Name of the package to be edited or created</dl>
 

 --webhook-rebuild {on,off}
<dl>
<dt>
<dd> Enable auto-rebuilding.</dl>

<h3>copr-cli edit-package-tito [options]</h3>

 

 usage: copr edit-package-tito [-h] --git-url URL [--git-dir DIRECTORY] [--git-branch BRANCH] [--test {on,off}] --name PKGNAME [--webhook-rebuild {on,off}] project 

 Edit source definition and type of an existing package. Options are shared with add-package-tito.

<h3>copr-cli add-package-pypi [options]</h3>

 

 usage: copr add-package-pypi [-h] [--pythonversions [VERSION [VERSION ...]]] [--packageversion PYPIVERSION] --packagename PYPINAME --name PKGNAME [--webhook-rebuild {on,off}] project 

 Add package of <i>PyPI</i> source type. 

 --pythonversions [VERSION [VERSION ...]]
<dl>
<dt>
<dd> For what Python versions to build (by default: 3 2)</dl>
 

 --packageversion PYPIVERSION
<dl>
<dt>
<dd> Version of the PyPI package to be built (by default latest)</dl>
 

 --packagename PYPINAME
<dl>
<dt>
<dd> Name of the PyPI package to be built, required</dl>
 

 --name PKGNAME
<dl>
<dt>
<dd> Name of the package to be edited or created</dl>
 

 --webhook-rebuild {on,off}
<dl>
<dt>
<dd> Enable auto-rebuilding</dl>

<h3>copr-cli edit-package-pypi [options]</h3>

 

 usage: copr edit-package-pypi [-h] [--pythonversions [VERSION [VERSION ...]]] [--packageversion PYPIVERSION] --packagename PYPINAME --name PKGNAME [--webhook-rebuild {on,off}] project 

 Edit source definition and type of an existing package. Options are shared with add-package-pypi.

<h3>copr-cli add-package-mockscm [options]</h3>

 

 usage: copr add-package-mockscm [-h] [--scm-type TYPE] [--scm-url URL] [--scm-branch BRANCH] [--spec FILE] --name PKGNAME [--webhook-rebuild {on,off}] project 

 Add package of <i>MockSCM</i> source type. 

 --scm-type TYPE
<dl>
<dt>
<dd> Specify versioning tool, default is <i>git</i></dl>
 

 --scm-url URL
<dl>
<dt>
<dd> Url to a project versioned by Git or SVN, required</dl>
 

 --scm-branch BRANCH
<dl>
<dt>
<dd> Branch in the target repository to build from</dl>
 

 --spec FILE
<dl>
<dt>
<dd> Relative path from SCM root to .spec file, required</dl>
 

 --name PKGNAME
<dl>
<dt>
<dd> Name of the package to be edited or created</dl>
 

 --webhook-rebuild {on,off}
<dl>
<dt>
<dd> Enable auto-rebuilding</dl>

<h3>copr-cli edit-package-mockscm [options]</h3>

 

 usage: copr edit-package-mockscm [-h] [--scm-type TYPE] [--scm-url URL] [--scm-branch BRANCH] [--spec FILE] --name PKGNAME [--webhook-rebuild {on,off}] project 

 Edit source definition and type of an existing package. Options are shared with add-package-mockscm.

<h3>copr-cli add-package-rubygems [options]</h3>

 

 usage: copr add-package-rubygems [-h] [--gem GEM] --name PKGNAME [--webhook-rebuild {on,off}] project 

 Add package of <i>RubyGems</i> source type. 

 --gem GEM
<dl>
<dt>
<dd> Specify gem name</dl>
 

 --name PKGNAME
<dl>
<dt>
<dd> Name of the package to be edited or created</dl>
 

 --webhook-rebuild {on,off}
<dl>
<dt>
<dd> Enable auto-rebuilding</dl>

<h3>copr-cli edit-package-rubygems [options]</h3>

 

 usage: copr edit-package-rubygems [-h] [--gem GEM] --name PKGNAME [--webhook-rebuild {on,off}] project 

 Edit source definition and type of an existing package. Options are shared with add-package-rubygems.

<h3>copr-cli list-packages [options]</h3>

 

 usage: copr list-packages [-h] [--with-latest-build] [--with-latest-succeeded-build] [--with-all-builds] project 

 Lists all packages in the given project in json format. 

 --with-latest-build
<dl>
<dt>
<dd> Also display data related to the latest build for each package.</dl>
 

 --with-latest-succeeded-build
<dl>
<dt>
<dd> Also display data related to the latest succeeded build for each package.</dl>
 

 --with-all-builds
<dl>
<dt>
<dd> Also display data related to the builds for each package.</dl>

<h3>copr-cli list-package-names [options]</h3>

 

 usage: copr list-package-names [-h] project 

 Only list package names in the given project line by line.

<h3>copr-cli get-package [options]</h3>

 

 usage: copr get-package [-h] --name PKGNAME [--with-latest-build] [--with-latest-succeeded-build] [--with-all-builds] project 

 Similar to list-packages but returns just a single package directly as json structure (not wrapped in a list).

<h3>copr-cli delete-package [options]</h3>

 

 usage: copr delete-package [-h] --name PKGNAME project 

 Deletes package and all its builds from the given project.

<h3>copr-cli reset-package [options]</h3>

 

 usage: copr reset-package [-h] --name PKGNAME project 

 Clears default source of a package and its source type (all the package settings are lost after invoking this!).

<h3>copr-cli build-package [options]</h3>

 

 usage: copr build-package [-h] [--memory MEMORY] [--timeout TIMEOUT] [--nowait] [-r CHROOTS] --name PKGNAME project 

 Creates a new build of the given package from its source definition. 

 --name PKGNAME
<dl>
<dt>
<dd> Name of a package to be built</dl>
 

 For the rest of the arguments, see copr-cli build command above.

<h3>copr-cli mock-config [options]</h3>

 

 usage: copr mock-config [-h] project chroot 

 Get the mock profile (similar to koji mock-config), print it to standard output. The configuration can be slightly different from the real mock configuration used by Copr Builders, but should be similar enough for basic debugging (e.g. by mock --shell).

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> <pre>
copr-cli add-package-tito myproject --name pkgname --git-url <a rel="nofollow" HREF="http://github.com/clime/example.git">http://github.com/clime/example.git</a> --test on
</pre></dl>
 

<dl>
<dt>
<dd> <pre>
copr-cli get-package myproject --name pkgname
</pre></dl>
 

<dl>
<dt>
<dd> <pre>
copr-cli build-package myproject --name pkgname --nowait --timeout 10000 -r fedora-23-x86_64
</pre></dl>
 

<dl>
<dt>
<dd> <pre>
copr-cli delete-package myproject --name pkgname
</pre></dl>
 

<dl>
<dt>
<dd> <pre>
copr-cli mock-config myproject fedora-rawhide-x86_64
</pre></dl>

<h2>EXIT STATUS</h2>

 

 Normally, the exit code is 0 when everything goes well. But if not, we could get: 1 - Bad request like wrong project name, insufficient rights etc. Also might happen when user interrupts the operation when they shouldn't. 2 - Wrong arguments given. 3 - Bad or no configuration. 4 - Build fails when Cli is waiting for the result. 5 - Communication error between Cli and server. This issue probably means bug and should be reported.

<h2>API KEY</h2>

 

 Visit the page <a rel="nofollow" HREF="https://copr.fedoraproject.org/api/">https://copr.fedoraproject.org/api/</a> to obtain an API token. This token must be saved in the file ~/.config/copr in the following format: 

<dl>
<dt>
<dd> <pre>
[copr-cli]
username = msuchy
login = Y57wcg==##fkfaxbkjhuoiebfafadl
token = vbfseelqdebzedukgombekmuvbkqwo
copr_url = <a rel="nofollow" HREF="https://copr.fedoraproject.org">https://copr.fedoraproject.org</a>
</pre></dl>
 

 Be aware that API tokens have an expiration date. The expiration date for your token is listed on the /api page.

<h2>USING DIFFERENT COPR INSTANCE</h2>

 

 If you plan to run copr client against non-default Copr instance, the API token is available on the <a rel="nofollow" HREF="http://YOUR.COPR.URL/api/">http://YOUR.COPR.URL/api/</a> page. You can either replace your default ~/.config/copr configuration file, or rather use alternative file with a shell alias 

<dl>
<dt>
<dd> <pre>
alias your_copr='copr --config ~/.config/your-copr'
</pre></dl>
 

 inserted into your profile.

<h2>AUTHORS</h2>

 

 Miroslav Suchý &lt;msuchy [at] redhat.com&gt;, clime &lt;clime [at] redhat.com&gt; 

<h2>Index</h2>


