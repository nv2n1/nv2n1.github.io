---
title: "wstool(1)"
name: "wstool"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wstool/"
description: "wstool – wstool Documentation"
---

<h2>NAME</h2>
<p> wstool &#8211; wstool Documentation </p>
<p> Using wstool you can update several folders using a variety of SCMs (SVN, Mercurial, git, Bazaar) with just one command. </p>
<p> That way you can more effectively manage source code workspaces. </p>
<p> The wstool package provides a Python API for interacting with a source code workspace as well as a group of command line tools. Rosinstall leverages the <code>vcstools</code> package for source control and stores its state in .rosinstall files.</p>
<h2>WSTOOL: A TOOL FOR MANAGING SOURCE CODE WORKSPACES</h2>
<p> wstool allows manipulation of a set of version-controlled folders as specified in a workspace definition file.</p>
<h3>Contents</h3>
<dl>
<dt>&bull;</dt>
<dd> <i>wstool: A tool for managing source code workspaces</i></dd>
<dt>&bull;</dt>
<dd> <i>Usage</i></dd>
<dt>&bull;</dt>
<dd> <i>init</i></dd>
<dt>&bull;</dt>
<dd> <i>set</i></dd>
<dt>&bull;</dt>
<dd> <i>merge</i></dd>
<dt>&bull;</dt>
<dd> <i>update</i></dd>
<dt>&bull;</dt>
<dd> <i>info</i></dd>
<dt>&bull;</dt>
<dd> <i>status</i></dd>
<dt>&bull;</dt>
<dd> <i>diff</i></dd></dl>
<h3>Usage</h3>
<pre><code>
wstool is a command to manipulate multiple version controlled folders.
Official usage:
  wstool CMD [ARGS] [OPTIONS]
wstool will try to infer install path from context
Type 'wstool help' for usage.
Options:
  help            provide help for commands
  init            set up a directory as workspace
  set             add or changes one entry from your workspace config
  merge           merges your workspace with another config set
  remove (rm)
remove an entry from your workspace config, without deleting files
                                            update(up)
update or check out some of your config elements
              info Overview of some entries
              status(st)
print the change status of files in some SCM controlled entries
diff(di)
print a diff over some SCM controlled entries
</code></pre>
<h3>init</h3>
<p> set up a directory as workspace </p>
<p> wstool init does the following:</p>
<dl>
<dt>1.</dt>
<dd> Reads folder/file/web-uri SOURCE_PATH looking for a rosinstall yaml</dd>
<dt>2.</dt>
<dd> Creates new .rosinstall file at TARGET-PATH configured </dd>
<p> SOURCE_PATH can e.g. be a folder like /opt/ros/electric If PATH is not given, uses current folder. </p>
<p>Usage : wstool init[TARGET_PATH[SOURCE_PATH]] ? Options::<br />
                                                        &#8211; h,<br />
        &#8211;help show this help message and exit&#8211; continue &#8211; on &#8211; error Continue despite checkout errors &#8211; j JOBS,<br />
        &#8211;parallel = JOBS<br />
            How many parallel threads to use for installing</p>
<p> Examples: </p>
<pre>
$ wstool init ~/jade /opt/ros/jade
</pre>
</dl>
<h3>set</h3>
<p> add or changes one entry from your workspace config The command will infer whether you want to add or modify an entry. If you modify, it will only change the details you provide, keeping those you did not provide. if you only provide a uri, will use the basename of it as localname unless such an element already exists. </p>
<p> The command only changes the configuration, to checkout or update the element, run wstool update afterwards. </p>
<p>Usage: wstool set [localname] [SCM-URI]?  [&#8211;(detached|svn|hg|git|bzr)] [&#8211;version=VERSION]]<br />
Options:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;detached            make an entry unmanaged (default for new element)<br />
  -v VERSION, &#8211;version-new=VERSION<br />
                        point SCM to this version<br />
  &#8211;git                 make an entry a git entry<br />
  &#8211;svn                 make an entry a subversion entry<br />
  &#8211;hg                  make an entry a mercurial entry<br />
  &#8211;bzr                 make an entry a bazaar entry<br />
  -y, &#8211;confirm         Do not ask for confirmation<br />
  -u, &#8211;update          update repository after set<br />
  -t WORKSPACE, &#8211;target-workspace=WORKSPACE<br />
                        which workspace to use</p>
<p> Examples: </p>
<pre>
$ wstool set robot_model --hg <a rel="nofollow" href="https://kforge.ros.org/robotmodel/robot_model">https://kforge.ros.org/robotmodel/robot_model</a>
$ wstool set robot_model --version robot_model-1.7.1
$ wstool set robot_model --detached
</pre>
<h3>merge</h3>
<p> The command merges config with given other rosinstall element sets, from files or web uris. </p>
<p> The default workspace will be inferred from context, you can specify one using -t. </p>
<p> By default, when an element in an additional URI has the same local-name as an existing element, the existing element will be replaced. In order to ensure the ordering of elements is as provided in the URI, use the option <code>&#8211;merge-kill-append</code>. </p>
<p>Usage: wstool merge [URI] [OPTIONS]<br />
Options:<br />
  -h, &#8211;help            show this help message and exit<br />
  -a, &#8211;merge-kill-append<br />
                        merge by deleting given entry and appending new one<br />
  -k, &#8211;merge-keep      (default) merge by keeping existing entry and<br />
                        discarding new one<br />
  -r, &#8211;merge-replace   merge by replacing given entry with new one<br />
                        maintaining ordering<br />
  -y, &#8211;confirm-all     do not ask for confirmation unless strictly necessary<br />
  -t WORKSPACE, &#8211;target-workspace=WORKSPACE<br />
                        which workspace to use</p>
<p> Examples: </p>
<pre>
$ wstool merge someother.rosinstall
</pre>
<p> You can use &#8216;-&#8216; to pipe in input, as an example: </p>
<pre>
$ roslocate info robot_mode | wstool merge -
</pre>
<h3>update</h3>
<p> update or check out some of your config elements </p>
<p> This command calls the SCM provider to pull changes from remote to your local filesystem. In case the url has changed, the command will ask whether to delete or backup the folder. </p>
<p>Usage: wstool update [localname]*<br />
Options:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;delete-changed-uris<br />
                        Delete the local copy of a directory before changing<br />
                        uri.<br />
  &#8211;abort-changed-uris  Abort if changed uri detected<br />
  &#8211;continue-on-error   Continue despite checkout errors<br />
  &#8211;backup-changed-uris=BACKUP_CHANGED<br />
                        backup the local copy of a directory before changing<br />
                        uri to this directory.<br />
  -j JOBS, &#8211;parallel=JOBS<br />
                        How many parallel threads to use for installing<br />
  -v, &#8211;verbose         Whether to print out more information<br />
  -t WORKSPACE, &#8211;target-workspace=WORKSPACE<br />
                        which workspace to use</p>
<p> Examples: </p>
<pre>
$ wstool update -t ~/jade
$ wstool update robot_model geometry
</pre>
<h3>info</h3>
<p> Overview of some entries</p>
<dl>
<dt><code>The Status (S) column shows</code></dt>
<dd> x for missing L for uncommited (local) changes V for difference in version and/or remote URI C for difference in local and remote versions </dd>
<p> The &#8216;Version-Spec&#8217; column shows what tag, branch or revision was given in the .rosinstall file. The &#8216;UID&#8217; column shows the unique ID of the current (and specified) version. The &#8216;URI&#8217; column shows the configured URL of the repo. </p>
<p> If status is V, the difference between what was specified and what is real is shown in the respective column. For SVN entries, the url is split up according to standard layout (trunk/tags/branches). The ROS_PACKAGE_PATH follows the order of the table, earlier entries overlay later entries. </p>
<p> When given one localname, just show the data of one element in list form. This also has the generic properties element which is usually empty. </p>
<p> The <code>&#8211;only</code> option accepts keywords: [&#8216;path&#8217;, &#8216;localname&#8217;, &#8216;version&#8217;, &#8216;revision&#8217;, &#8216;cur_revision&#8217;, &#8216;uri&#8217;, &#8216;cur_uri&#8217;, &#8216;scmtype&#8217;] </p>
<p>Usage: wstool info [localname]* [OPTIONS]<br />
Options:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;root                Show workspace root path<br />
  &#8211;data-only           Does not provide explanations<br />
  &#8211;only=ONLY           Shows comma-separated lists of only given comma-<br />
                        separated attribute(s).<br />
  &#8211;yaml                Shows only version of single entry. Intended for<br />
                        scripting.<br />
  &#8211;fetch               When used, retrieves version information from remote<br />
                        (takes longer).<br />
  -u, &#8211;untracked       Also show untracked files as modifications<br />
  -t WORKSPACE, &#8211;target-workspace=WORKSPACE<br />
                        which workspace to use<br />
  -m, &#8211;managed-only    only show managed elements</p>
<p> Examples: </p>
<pre>
$ wstool info -t ~/ros/jade
$ wstool info robot_model
$ wstool info --yaml
$ wstool info --only=path,cur_uri,cur_revision robot_model geometry
</pre>
</dl>
<h3>status</h3>
<p> print the change status of files in some SCM controlled entries. The status columns meanings are as the respective SCM defines them. </p>
<p>Usage : wstool status[localname] *<br />
        Options : -h,<br />
    &#8211;help show this help message and exit&#8211; untracked Also shows untracked files &#8211; t WORKSPACE, &#8211;target &#8211; workspace = WORKSPACE which workspace to use</p>
<h3>diff</h3>
<p> print a diff over some SCM controlled entries </p>
<p>Usage : wstool diff[localname] *<br />
        Options : -h,<br />
    &#8211;help show this help message and exit&#8211; untracked Also shows untracked files &#8211; t WORKSPACE, &#8211;target &#8211; workspace = WORKSPACE which workspace to use</p>
<h2>UBUNTU</h2>
<p> On Ubuntu the recommended way to install rosinstall is to use apt. </p>
<pre>
sudo apt-get install python-wstool
</pre>
<h2>OTHER PLATFORMS</h2>
<p> On other platforms rosinstall is available on pypi and can be installed via <code>pip</code> </p>
<pre>
pip install -U wstool
</pre>
<p> or <code>easy_install</code>: </p>
<pre>
easy_install -U wstool vcstools
</pre>
<h2>ROSINSTALL FILE FORMAT</h2>
<h3>Format</h3>
<p> The rosinstall file format is a yaml document. It is a list of top level dictionaries. Each top level dictionary is expected to have one of the vcs type keys and no other keys. </p>
<p> Inside every top level dictionary there is one required key, <code>local-name</code> this represents the path where to install files. It will support both workspace relative paths as well as absolute paths. </p>
<p> Each of the vcs type keys requires a <code>uri</code> key, and optionally takes a <code>version</code> key.</p>
<h3>Top Level Keys</h3>
<p> The valid keys are <code>svn</code>, <code>hg</code>, <code>git</code>, <code>bzr</code>. </p>
<p> Each key represents a form of version control system to use. These are supported from the vcstools module.</p>
<h3>Example rosinstall syntax:</h3>
<p> Below is an example rosinstall syntax with examples of most of the possible permutations: </p>
<pre><code>
- svn:
{
    local - name : some / local / path2, uri : / some / local / uri
}
- hg:
{
    local - name : some / local / path3, uri : http : // some/uri, version: 123}
                                                      -git:
    {
        local - name : / some / local / aboslute / path, uri : http : // some/uri, version: 123}
                                                                      -bzr:
        {
            local - name : some / local / path4, uri : http: // some/uri, version: 123}
</code></pre>
<p> Things to note are:</p>
<dl>
<dt>&bull;</dt>
<dd> <code>version</code> is optional though recommended.</dd>
<dt>&bull;</dt>
<dd> Absolute or relative paths are valid for <code>local-name</code></dd>
<dt>&bull;</dt>
<dd> <code>uri</code> can be a local file path to a repository.</dd></dl>
<h2>DEVELOPER&#8217;S GUIDE</h2>
<h3>Changelog</h3>
<h3>0.1.12</h3>
<dl>
<dt>&bull;</dt>
<dd> Fix command line arguments of <code>wstool scrape</code>.</dd></dl>
<h3>0.1.11</h3>
<dl>
<dt>&bull;</dt>
<dd> Changed the way <code>.bak</code> files are created when overwriting existing configurations.</dd>
<dt>&bull;</dt>
<dd> Added the Scrape command.</dd>
<dt>&bull;</dt>
<dd> Added default git branch and status to <code>wstool fetch &#8211;info</code>.</dd>
<dt>&bull;</dt>
<dd> Added versioned dependency on vcstools <code>0.1.38</code> to make use of new API features.</dd></dl>
<h3>0.1.10</h3>
<dl>
<dt>&bull;</dt>
<dd> Fix regression which broke the -j option.</dd>
<dt>&bull;</dt>
<dd> Enable pretty printing of the <code>.rosinstall</code> file&#8217;s YAML.</dd></dl>
<h3>0.1.9</h3>
<dl>
<dt>&bull;</dt>
<dd> Fix for zsh completion.</dd>
<dt>&bull;</dt>
<dd> Fixed version dependency on vcstools for debian.</dd></dl>
<h3>0.1.8</h3>
<dl>
<dt>&bull;</dt>
<dd> Fix for installation issue.</dd></dl>
<h3>0.1.7</h3>
<dl>
<dt>&bull;</dt>
<dd> Added installation of generated man pages.</dd>
<dt>&bull;</dt>
<dd> Added installation of shell completion for wstool.</dd>
<dt>&bull;</dt>
<dd> Improved output of wstool info with the new get_current_version_label in vcstools.</dd>
<dt>&bull;</dt>
<dd> Added a foreach command.</dd>
<dt>&bull;</dt>
<dd> Added a <code>&#8211;root</code> option to wstool info.</dd>
<dt>&bull;</dt>
<dd> Enhanced the <code>&#8211;update</code> option for wstool set.</dd>
<dt>&bull;</dt>
<dd> Now uses multiple threads for network operations by default.</dd>
<dt>&bull;</dt>
<dd> Some other minor fixes and improvements and docs.</dd></dl>
<h3>0.1.5</h3>
<dl>
<dt>&bull;</dt>
<dd> Releasing to allow changes for new platform vivid.</dd>
<dt>&bull;</dt>
<dd> Fix svn diff for change in output with svn 1.7.9.</dd>
<dt>&bull;</dt>
<dd> info command shows information about unmanaged paths.</dd></dl>
<h3>0.1.4</h3>
<dl>
<dt>&bull;</dt>
<dd> Fix detection of path conflicts #24 (<i><a rel="nofollow" href="https://github.com/vcstools/wstool/pull/24">https://github.com/vcstools/wstool/pull/24</a></i>).</dd></dl>
<h3>0.0.3</h3>
<dl>
<dt>&bull;</dt>
<dd> not using ROS_WORKSPACE anymore</dd>
<dt>&bull;</dt>
<dd> fix to &quot;wstool cmd &#8211;help&quot;</dd></dl>
<h3>0.0.2</h3>
<dl>
<dt>&bull;</dt>
<dd> fix #2 creating &quot;wstool2 file instaed of &quot;.rosinstall&quot;</dd></dl>
<h3>0.0.1</h3>
<dl>
<dt>&bull;</dt>
<dd> Initial creation based on functions inrosinstall</dd></dl>
<h3>Bug reports and feature requests</h3>
<dl>
<dt>&bull;</dt>
<dd> <i>Submit a bug report</i></dd></dl>
<h3>Developer Setup</h3>
<p> The wstool source can be downloaded using Mercurial: </p>
<pre>
$ git clone <a rel="nofollow" href="https://github.com/vcstools/wstool.git">https://github.com/vcstools/wstool.git</a>
</pre>
<p> You will also need vcstools, which you can either install using pip or download using: </p>
<pre>
$ git clone <a rel="nofollow" href="https://github.com/vcstools/vcstools.git">https://github.com/vcstools/vcstools.git</a>
$ cd vcstools
$ python develop
</pre>
<p> wstool uses <i>setuptools</i>, which you will need to download and install in order to run the packaging. We use setuptools instead of distutils in order to be able use <code>setup()</code> keys like <code>install_requires</code>. </p>
<p> Configure your environment: $ cd wstool $ python develop</p>
<h3>Testing</h3>
<p> Install test dependencies </p>
<pre>
$ pip install nose
$ pip install mock
</pre>
<p> wstool uses <i>Python nose</i> for testing, which is a fairly simple and straightforward test framework. The wstool mainly use <code>unittest</code> to construct test fixtures, but with nose you can also just write a function that starts with the name <code>test</code> and use normal <code>assert</code> statements. </p>
<p> wstool also uses <i>mock</i> to create mocks for testing. </p>
<p> You can run the tests, including coverage, as follows: </p>
<pre>
$ cd wstool
$ make test
</pre>
<h3>Documentation</h3>
<p> Sphinx is used to provide API documentation for wstool. The documents are stored in the <code>doc</code> sub-directory. </p>
<p> You can build the docs as follows: </p>
<pre>
$ cd wstool/doc
$ make html
</pre>
<dl>
<dt>&bull;</dt>
<dd> <i>genindex</i></dd>
<dt>&bull;</dt>
<dd> <i>modindex</i></dd>
<dt>&bull;</dt>
<dd> <i>search</i></dd></dl>
<h2>AUTHOR</h2>
<p> Tully Foote, Thibault Kruse, Ken Conley, Brian Gerkey</p>
<h2>COPYRIGHT</h2>
<p> 2011, Willow Garage </p>
