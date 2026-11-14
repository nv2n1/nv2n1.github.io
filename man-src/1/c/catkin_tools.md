---
title: "catkin_tools(1)"
name: "catkin_tools"
section: "1"
letter: "c"
url: "/docs/linux/man/1-catkin_tools/"
description: "catkin_tools – catkin_tools Documentation"
---

<h2>NAME</h2>
<p> catkin_tools &#8211; catkin_tools Documentation</p>
<h2>INSTALLING CATKIN_TOOLS</h2>
<p> You can install the <code>catkin_tools</code> package as a binary through a package manager like <code>pip</code> or <code>apt-get</code>, or from source. </p>
<p> <code>NOTE:</code> This project is still in beta and has not been released yet, please install from source. In particular, interface and behaviour are still subject to incompatible changes. If you rely on a stable environment, please use <code>catkin_make</code> instead of this tool.</p>
<h3>Installing on Ubuntu with apt-get</h3>
<p> First you must have the ROS repositories which contain the <code>.deb</code> for <code>catkin_tools</code>: </p>
<pre>
$ sudo sh -c 'echo &quot;deb <a rel="nofollow" href="http://packages.ros.org/ros/ubuntu">http://packages.ros.org/ros/ubuntu</a> `lsb_release -sc` main&quot; &gt; /etc/apt/sources.list.d/ros-latest.list'
$ wget <a rel="nofollow" href="http://packages.ros.org/ros.key">http://packages.ros.org/ros.key</a> -O - | sudo apt-key add -
</pre>
<p> Once you have added that repository, run these commands to install <code>catkin_tools</code>: </p>
<pre>
$ sudo apt-get update
$ sudo apt-get install python-catkin-tools
</pre>
<h3>Installing on other platforms with pip</h3>
<p> Simply install it with <code>pip</code>: </p>
<pre>
$ sudo pip install -U catkin_tools
</pre>
<h3>Installing from source</h3>
<p> First clone the source for <code>catkin_tools</code>: </p>
<pre>
$ git clone <a rel="nofollow" href="https://github.com/catkin/catkin_tools.git">https://github.com/catkin/catkin_tools.git</a>
$ cd catkin_tools
</pre>
<p> Then install with the <code>setup.py</code> file: </p>
<pre>
$ python setup.py install
</pre>
<p> Note: Depending on your environment/machine, you may need to use <code>sudo</code> with this command.</p>
<h3>Developing</h3>
<p> Listed here are some useful tips for developing against <code>catkin_tools</code>.</p>
<h3>Install <code>catkin_tools</code> for developing</h3>
<p> To setup <code>catkin_tools</code> for fast iteration during development, use the <code>develop</code> verb to <code>setup.py</code>: </p>
<pre>
$ python setup.py develop
</pre>
<p> Now the commands, like <code>catkin</code>, will be in the system path and the local source files located in the <code>catkin_tools</code> folder will be on the <code>PYTHONPATH</code>. When you are done with your development, undo this by running this command: </p>
<pre>
$ python setup.py develop -u
</pre>
<h2>QUICKSTART</h2>
<p> This chapter gives a high-level overview of how to use <code>catkin_tools</code> and the <code>catkin</code> command. This shows how to use the different command verbs to create and manipulate a workspace. For a more in-depth explanation of the mechanics of catkin workspaces, see <code>Workspace Mechanics</code>, and for thorogh usage details see the individual verb documentation.</p>
<h3>TL;DR</h3>
<p> The following is an example workflow and sequence of commands using default settings: </p>
<pre><code>
$ mkdir - p / tmp / path / to / my_catkin_ws / src #Make a new workspace and source space $ cd / tmp / path / to / my_catkin_ws #Navigate to the workspace root $ catkin init #Initialize it with a hidden marker file $ cd / tmp / path / to / my_catkin_ws / src #Navigate to the source space $ catkin create pkg pkg_a #Populate the source space with packages... $ catkin create pkg pkg_b $ catkin create pkg pkg_c-- catkin - deps pkg_a $ catkin create pkg pkg_d-- catkin - deps pkg_a pkg_b $ catkin build #Build all packages in the workspace $ source../ devel / setup.bash #Load the workspace's environment $ catkin clean-- all #Clean the build products $ catkin build pkg_d #Build `pkg_d` and its deps $ cd / tmp / path / to / my_catkin_ws / src / pkg_c #Navigate to `pkg_c`'s source directory $ catkin build-- this #Build `pkg_c` and its deps $ catkin build-- this --no - deps #Rebuild only `pkg_c`
</code></pre>
<h3>Initializing a New Workspace</h3>
<p> While initialization of a workspace can be done automatically with <code>catkin build</code>, it&#8217;s good practice to initialize a catkin workspace explicitly. This is done by simply creating a new workspace with an empty <code>source space</code> (named <code>src</code> by default) and calling <code>catkin init</code> from the workspace root: </p>
<p>$ mkdir &#8211; p / tmp / path / to / my_catkin_ws / src $ cd / tmp / path / to / my_catkin_ws $ catkin init&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None Workspace : / tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel Install Space : [missing] / tmp / path / to / my_catkin_ws / install DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<p> Now the directory <code>/tmp/path/to/my_catkin_ws</code> has been initialized and <code>catkin init</code> has printed the standard configuration summary to the console with the default values. This summary describes the layout of the workspace as well as other important settings which influence build and execution behavior. </p>
<p> Once a workspace has been initialized, the configuration summary can be displayed by calling <code>catkin config</code> without arguments from anywhere under the root of the workspace. Doing so will not modify your workspace. The <code>catkin</code> command is context-sensitive, so it will determine which workspace contains the current working directory. </p>
<p> An important property which deserves attention is the summary value labeled <code>Extending</code>. This describes other collections of libraries and packages which will be visible to your workspace. This is process called &quot;workspace chaining.&quot; The value can be come from a few different sources, and can be classified in one of the three following ways:</p>
<dl>
<dt>&bull;</p>
<dd> No chaining</p>
<dt>&bull;</p>
<dd> Implicit chaining via <code>CMAKE_PREFIX_PATH</code> environment or cache variable</p>
<dt>&bull;</p>
<dd> Explicit chaining via <code>catkin config &#8211;extend</code> </p>
<p> For more information on the configuration summary and workspace chaining, see <code>Configuration Summary</code>. For information on manipulating these options, see <code>the config verb</code>. </p>
<p> <code>NOTE:</code> Calling <code>catkin init</code> &quot;marks&quot; a directory path by creating a hidden directory called <code>.catkin_tools</code>. This hidden directory is used to designate the parent as the root of a Catkin workspace as well as store persistent information about the workspace configuration.</dl>
<h3>Adding Packages to the Workspace</h3>
<p> In order to build software with Catkin, it needs to be added to the workspace&#8217;s <code>source space</code>. You can either download some existing packages, or create one or more empty ones. As shown above, the default path for a Catkin <code>source space</code> is <i>./src</i> relative to the workspace root. A standard Catkin package is simply a directory with a <code>CMakeLists.txt</code> file and a <code>package.xml</code> file. For more information on Catkin packages see <code>workspace mechanics</code>. The shell interaction below shows the creation of three trivial packages: <code>pkg_a</code>, <code>pkg_b</code>, and <code>another_one</code>: </p>
<pre>
$ cd /tmp/path/to/my_catkin_ws/src
$ catkin_create_pkg pkg_a
Created file pkg_a/CMakeLists.txt
Created file pkg_a/package.xml
Successfully created files in /tmp/path/to/my_catkin_ws/src/pkg_a. Please adjust the values in package.xml.
$ catkin_create_pkg pkg_b
Created file pkg_b/CMakeLists.txt
Created file pkg_b/package.xml
Successfully created files in /tmp/path/to/my_catkin_ws/src/pkg_b. Please adjust the values in package.xml.
$ catkin_create_pkg another_one
Created file another_one/CMakeLists.txt
Created file another_one/package.xml
Successfully created files in /tmp/path/to/my_catkin_ws/src/another_one. Please adjust the values in package.xml.
</pre>
<p> After these operations, your workspace&#8217;s local directory structure would look like the followng (to two levels deep): </p>
<pre>
$ cd /tmp/path/to/my_catkin_ws
$ tree -aL 2
.
├── .catkin_tools
│&nbsp;<wbr>&nbsp;<wbr> └── README
└── src
    ├── another_one
    ├── pkg_a
    └── pkg_b
</pre>
<p> Now that there are some packages in the workspace, Catkin has something to build. </p>
<p> <code>NOTE:</code> Catkin utilizes an &quot;out-of-source&quot; and &quot;aggregated&quot; build pattern. This means that not only will temporary or final build products never be placed in a package&#8217;s source directory (or anywhere in the <code>source space</code> for that matter), but also all build directories are aggregated in the <code>build space</code> and all final build products (executables, libraries, etc.) will be put in the <code>devel space</code>.</p>
<h3>Building the Workspace</h3>
<p> Since the catkin workspace has already been initialized, you can call <code>catkin build</code> from any directory contained within it. If it had not been initialized, then <code>catkin build</code> would need to be called from the workspace root. Based on the default configuration, it will locate the packages in the <code>source space</code> and build each of them. </p>
<p>$ catkin build&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None<br />
                                                                                                                                            Workspace : /<br />
                                                                                                                                                        tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel Install Space : [missing] / tmp / path / to / my_catkin_ws / install DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Found &#8216;3&#8217; packages in 0.0 seconds.Starting ==<br />
    &gt; another_one<br />
            Starting ==<br />
    &gt; pkg_a<br />
            Starting ==<br />
    &gt; pkg_b<br />
            Finished &lt;= = pkg_b[2.0 seconds] Finished &lt;= = another_one[2.0 seconds] Finished &lt;= = pkg_a[3.4 seconds]<br />
                                                                                                       [build] Finished.<br />
                                                                                                           [build] Runtime : 3.4 seconds</p>
<p> Calling <code>catkin build</code> will generate <code>build</code> and <code>devel</code> directories (as described in the config summary above) and result in a directory structure like the following (to one level deep): </p>
<pre>
$ cd /tmp/path/to/my_catkin_ws
$ tree -aL 1
.
├── build
├── .catkin_tools
├── devel
└── src
</pre>
<p> Intermediate build products (CMake cache files, Makefiles, object files, etc.) are generated in the <code>build</code> directory, or <code>build space</code> and final build products (libraries, executables, config files) are generated in the <code>devel</code> directory, or <code>devel space</code>. For more information on building and customizing the build configuration see the <code>build verb</code> and <code>config verb</code> documentation.</p>
<h3>Loading the Workspace Environment</h3>
<p> In order to properly &quot;use&quot; the products of the workspace, it&#8217;s environment needs to be loaded. Among other environment variables, sourcing a Catkin setup file modifies the <code>CMAKE_PREFIX_PATH</code> environment variable, which will affect workspace chaining as described in the earlier section. </p>
<p> Setup files are located in one of the <code>result spaces</code> generated by your workspace. Both the <code>devel space</code> or the <code>install space</code> are valid <code>result spaces</code>. In the default build configuration, only the <code>devel space</code> is generated. You can load the environment for your respective shell like so: </p>
<pre>
$ source /tmp/path/to/my_catkin_ws/devel/setup.bash
</pre>
<p> At this point you should be able to use products built by any of the packages in your workspace. </p>
<p> <code>NOTE:</code> Any time the member packages change in your workspace, you will need to re-run the source command. </p>
<p> Loading the environment from a Catkin workspace can set <code>arbitrarily many</code> environment variables, depending on which &quot;environment hooks&quot; the member packages define. As such, it&#8217;s important to know which workspace environment is loaded in a given shell. </p>
<p> It&#8217;s not unreasonable to automatically source a given setup file in each shell for convenience, but if you do so, it&#8217;s good practice to pay attention to the <code>Extending</code> value in the Catkin config summary. Any Catkin setup file will modify the <code>CMAKE_PREFIX_PATH</code> environment variable, and the config summary should catch common inconsistencies in the environment.</p>
<h3>Cleaning Workspace Products</h3>
<p> Instead of using dangerous commands like <code>rm -rf build devel</code> in your workspace when cleaning build products, you can use the <code>catkin clean &#8211;all</code> command. Just like the other verbs, <code>catkin clean</code> is context-aware, so it only needs to be called from a directory under the workspace root. </p>
<p> In order to clean the <code>build space</code> and <code>devel space</code> for the workspace, you can use any following command: </p>
<pre>
$ catkin clean --build --devel
Removing buildspace: /tmp/path/to/my_catkin_ws/build
Removing develspace: /tmp/path/to/my_catkin_ws/devel
</pre>
<p> For more information on less aggressive cleaning options see the <code>clean verb</code> documentation.</p>
<h2>WORKSPACE MECHANICS</h2>
<p> This chapter defines how Catkin workspaces are organized and used, as well as some standardized nomenclature for describing elements of a Catkin workspace. Unlike integrated development environments (IDEs) which normally only manage single projects, the purpose of Catkin is to enable the simultaneous compilation of numerous independently-authored projects. As such, these projects need to be organized in a &quot;workspace&quot; which contains both the source and build products for a collection of &quot;packages.&quot;</p>
<h3>Anatomy of a Catkin Workspace</h3>
<p> A standard catkin workspace, as defined by <i>REP-0128</i>, is a folder with a prescribed set &quot;spaces&quot;, each of which is normally a folder within the workspace:</p>
<dl>
<dt>&bull;</p>
<dd> <code>source space</code> &#8212; default: <code>./src</code></p>
<dt>&bull;</p>
<dd> <code>build space</code> &#8212; default: <code>./build</code></p>
<dt>&bull;</p>
<dd> <code>devel space</code> &#8212; default: <code>./devel</code></p>
<dt>&bull;</p>
<dd> <code>install space</code> &#8212; default: <code>./install</code> </p>
<p> Though there are standard conventions for the layout and names of the workspace&#8217;s various spaces, they can be renamed for a given build using the <code>catkin config</code> verb.</dl>
<h3>source space</h3>
<p> The <code>source space</code> is where the code for your packages resides and normally is in the folder <code>/path/to/workspace/src</code>. The build command considers <code>source space</code> to be read-only, in that during a build no files or folders should be created or modified in that folder. Therefore catkin workspaces are said to be built &quot;out of source&quot;, which simply means that the folder in which you build your code is not under or part of the folder with contains the source code.</p>
<h3>build space</h3>
<p> Temporary build files are put into the <code>build space</code>, which by default is in the <code>/path/to/workspace/build</code> folder. The <code>build space</code> is the working directory in which commands like <code>cmake</code> and <code>make</code> are run.</p>
<h3>devel space</h3>
<p> Generated files, like executables, libraries, pkg-config files, CMake config files, or message code, are placed in the <code>devel space</code>. By convention the <code>devel space</code> is located as a peer to the <code>source space</code> and <code>build space</code> in the <code>/path/to/workspace/devel</code> folder. The layout of the <code>devel space</code> is intended to mimic the root of an <i>FHS filesystem</i>, with folders like <code>include</code>, <code>lib</code>, <code>bin</code>, and <code>share</code>. Running code is possible from <code>devel space</code> because references to the <code>source space</code> are created.</p>
<h3>install space</h3>
<p> Finally, if the packages in the workspace are setup for installing, the <code>&#8211;install</code> option can be invoked to install the packages to the <code>CMAKE_INSTALL_PREFIX</code>, which in <i>REP-0128</i> terms is the <code>install space</code>. The <code>install space</code>, like the <code>devel space</code>, has an FHS layout along with some generated setup files. The <code>install space</code> is set to <code>/path/to/workspace/install</code> by changing the <code>CMAKE_INSTALL_PREFIX</code> by default. This is done to prevent users from accidentally trying to install to the normal <code>CMAKE_INSTALL_PREFIX</code> path, <code>/usr/local</code>. Unlike the <code>devel space</code>, the <code>install space</code> is completely standalone and does not require the <code>source space</code> or <code>build space</code> to function, and is suitable for packaging.</p>
<h3>Additional Workspace Directories with <code>catkin_tools</code></h3>
<h3>Hidden Marker / Config Directory</h3>
<p> In addition to the standard workspace structure, <code>catkin_tools</code> also adds a marker directory called <code>.catkin_tools</code> at the root of the workspace. This directory both acts as a marker for the root of the workspace and contains persistent configuration information. </p>
<p> This directory contains subdirectories representing different configuration profiles, and inside of each profile directory are YAML files which contain verb-specific metadata. It additionally contains a file which lists the name of the active configuration profile if it is different than <code>default</code>.</p>
<h3>Build Log Directory</h3>
<p> Another addition is the <code>build_logs</code> directory which is generated in the <code>build space</code> and contains individual build logs for each package.</p>
<h3>Environment Setup Files</h3>
<p> In addition to the FHS folders, some setup scripts are generated in the <code>devel space</code>, e.g. <code>setup.bash</code> or <code>setup.zsh</code>. These setup scripts are intended to make it easier to use the resulting <code>devel space</code> for building on top of the packages that were just built or for running programs built by those packages. The setup script can be used like this in <code>bash</code>: </p>
<pre>
$ source /path/to/workspace/devel/setup.bash
</pre>
<p> Or like this in <code>zsh</code>: </p>
<pre>
% source /path/to/workspace/devel/setup.zsh
</pre>
<p> Sourcing these setup scripts adds this workspace and any &quot;underlaid&quot; workspaces to your environment, prefixing the <code>CMAKE_PREFIX_PATH</code>, <code>PKG_CONFIG_PATH</code>, <code>PATH</code>, <code>LD_LIBRARY_PATH</code>, <code>CPATH</code>, and <code>PYTHONPATH</code> with local workspace folders. </p>
<p> The setup scripts will also execute any shell hooks exported by packages in the workspace, which is how <code>roslib</code>, for example, sets the <code>ROS_PACKAGE_PATH</code> environment variable. </p>
<p> <code>NOTE:</code> Like the <code>devel space</code>, the <code>install space</code> includes <code>setup.*</code> and related files at the top of the file hierarchy. This is not suitable for some packaging systems, so this can be disabled by passing the <code>-DCATKIN_BUILD_BINARY_PACKAGE=&quot;1&quot;</code> option to <code>cmake</code> using the <code>&#8211;cmake-args</code> option for this verb. Though this will suppress the installation of the setup files, you will loose the functionality provided by them, namely extending the environment and executing environment hooks.</p>
<h3>Workspace Packages and Dependencies</h3>
<p> A workspace&#8217;s packages consist of any packages found in the <code>source space</code>. A package is any folder which contains a <code>package.xml</code> as defined in <i>REP-0127</i>. </p>
<p> The <code>catkin build</code> command determines the order in which packages are built based on the <code>depend</code>, <code>build_depend</code>, <code>run_depend</code>, and <code>build_type</code> tags in a package&#8217;s <code>package.xml</code> file.</p>
<dl>
<dt>&bull;</p>
<dd> The <code>*_depend</code> tags are used to determine the topological build order of the packages.</p>
<dt>&bull;</p>
<dd> The <code>build_type</code> tag is used to determine which build work flow to use on the package. </p>
<p> Packages without an explicitly defined <code>build_type</code> tag are assumed to be catkin packages, but plain CMake packages can be built by adding a <code>package.xml</code> file to the root of their source tree with the <code>build_type</code> flag set to <code>cmake</code> and appropriate <code>build_depend</code> and <code>run_depend</code> tags set, as described in <i>REP-0136</i>. This has been done in the past for building packages like <code>opencv</code>, <code>pcl</code>, and <code>flann</code>.</dl>
<h3>Understanding the Build Process</h3>
<h3>Legacy Catkin Workflow</h3>
<p> The core Catkin meta-buildsystem was originally designed in order to efficiently build numerous inter-dependent, but separately developed, CMake projects. This was developed by the Robot Operating System (ROS) community, originally as a successor to the standard meta-buildtool <code>rosbuild</code>. The ROS community&#8217;s distributed development model with many modular projects and the need for building distributable binary packages motivated the design of a system which efficiently merged numerous disparate projects so that they utilize a single target dependency tree and build space. </p>
<p> To facilitate this &quot;merged&quot; build process, a workspace&#8217;s <code>source space</code> would contain boiler-plate &quot;top-level&quot; <code>CMakeLists.txt</code> which automatically added all of the Catkin CMake projects below it to the single large CMake project. </p>
<p> Then the user would build this collection of projects like a single unified CMake project with a workflow similar to the standard CMake out-of-source build workflow. They would all be configured with one invocation of <code>cmake</code> and subsequently targets would be built with one or more invocations of <code>make</code>: </p>
<pre>
$ mkdir build
$ cd build
$ cmake ../src
$ make
</pre>
<p> In order to help automate the merged build process, Catkin was distributed with a command-line tool called <code>catkin_make</code>. This command automated the above CMake work flow while setting some variables according to standard conventions. These defaults would result in the execution of the following commands: </p>
<pre>
$ mkdir build
$ cd build
$ cmake ../src -DCATKIN_DEVEL_SPACE=../devel -DCMAKE_INSTALL_PREFIX=../install
$ make -j&lt;number of cores&gt; -l&lt;number of cores&gt; [optional target, e.g. install]
</pre>
<p> An advantage of this approach is that the total configuration would be smaller than configuring each package individually and that the Make targets can be parallelized even amongst dependent packages. </p>
<p> In practice, however, it also means that in large workspaces, modification of the CMakeLists.txt of one package would necessitate the reconfiguration of all packages in the entire workspace. </p>
<p> A critical flaw of this approach, however, is that there is no fault isolation. An error in a leaf package (package with no dependencies) will prevent all packages from configuring. Packages might have colliding target names. The merged build process can even cause CMake errors to go undetected if one package defines variables needed by another one, and can depend on the order in which independent packages are built. Since packages are merged into a single CMake invocation, this approach also requires developers to specify explicit dependencies on some targets inside of their dependencies. </p>
<p> Another disadvantage of the merged build process is that it can only work on a homogeneous workspace consisting only of Catkin CMake packages. Other types of packages like plain CMake packages and autotools packages cannot be integrated into a single configuration and a single build step.</p>
<h3>Isolated Catkin Workflow</h3>
<p> The numerous drawbacks of the merged build process and the <code>catkin_make</code> tool motivated the development of the <code>catkin_make_isolated</code> tool. In contrast to <code>catkin_make</code>, the <code>catkin_make_isolated</code> command uses an isolated build process, wherein each package is independently configured, built, and loaded into the environment. </p>
<p> This way, each package is built in isolation and the next packages are built on the atomic result of the current one. This resolves the issues with target collisions, target dependency management, and other undesirable cross-talk between projects. This also allows for the homogeneous automation of other buildtools like the plain CMake or autotools. </p>
<p> The isolated workflow also enabled the following features:</p>
<dl>
<dt>&bull;</p>
<dd> Allowing building of <i>part</i> of a workspace</p>
<dt>&bull;</p>
<dd> Building Catkin and non-Catkin projects into a single <code>devel space</code></p>
<dt>&bull;</p>
<dd> Building packages without re-configuring or re-building their dependencies</p>
<dt>&bull;</p>
<dd> Removing the requirement that all packages in the workspace are free of CMake errors before any packages can be built </p>
<p> There are, however, still some problems with <code>catkin_make_isolated</code>. First, it is dramatically slower than <code>catkin_make</code> since it cannot parallelize the building of targets or even packages which do not depend on each other. It also lacks robustness to changes in the list of packages in the workspace. Since it is a &quot;released&quot; tool, it also has strict API stability requirements.</dl>
<h3>Parallel Isolated Catkin Workflow and <code>catkin build</code></h3>
<p> The limitations of <code>catkin_make_isolated</code> and the need for additional high-level build tools lead to the development of a parallel version of catkin make isolated, or <code>pcmi</code>, as part of <i>Project Tango</i>. <code>pcmi</code> later became the <code>build</code> verb of the <code>catkin</code> command included in this project. </p>
<p> As such, the principle behavior of the <code>build</code> verb is to build each package in isolation and in topological order while parallelizing the building of packages which do not depend on each other. </p>
<p> Other functional improvements over <code>catkin_make</code> and <code>catkin_make_isolated</code> include the following:</p>
<dl>
<dt>&bull;</p>
<dd> The use of sub-command &quot;verbs&quot; for better organization of build options and build-related functions</p>
<dt>&bull;</p>
<dd> Robustly adapting a build when packages are added to or removed from the <code>source space</code></p>
<dt>&bull;</p>
<dd> Context-aware building of a given package based on the working directory</p>
<dt>&bull;</p>
<dd> Utilization of persistent build metadata which catches common errors</p>
<dt>&bull;</p>
<dd> Support for different build &quot;profiles&quot; in a single workspace</p>
<dt>&bull;</p>
<dd> Explicit control of workspace chaining</p>
<dt>&bull;</p>
<dd> Additional error-checking for common environment configuration errors</p>
<dt>&bull;</p>
<dd> Numerous other command-line user-interface improvements</dl>
<h3>Workspace Chaining and the Importance of CMAKE_PREFIX_PATH</h3>
<p> Above, it&#8217;s mentioned that the Catkin setup files export numerous environment variables, including <code>CMAKE_PREFIX_PATH</code>. Since CMake 2.6.0, the <code>CMAKE_PREFIX_PATH</code> is used when searching for include files, binaries, or libraries using the <code>FIND_PACKAGE()</code>, <code>FIND_PATH()</code>, <code>FIND_PROGRAM()</code>, or <code>FIND_LIBRARY()</code> CMake commands. </p>
<p> As such, this is also the primary way that Catkin &quot;chains&quot; workspaces together. When you build a Catkin workspace for the first time, it will automatically use <code>CMAKE_PREFIX_PATH</code> to find dependencies. After that compilation, the value will be cached internally by each project as well as the Catkin setup files and they will ignore any changes to your <code>CMAKE_PREFIX_PATH</code> environment variable until they are cleaned. </p>
<p> <code>NOTE:</code> Workspace <code>chaining</code> is the act of putting the products of one workspace <code>A</code> in the search scope of another workspace <code>B</code>. When describing the relationship between two such chained workspaces, <code>A</code> and <code>B</code>, it is said that workspace <code>B</code> <code>extends</code> workspace <code>A</code> and workspace <code>A</code> is <code>extended by</code> workspace <code>B</code>. This concept is also sometimes referred to as &quot;overlaying&quot; or &quot;inheriting&quot; a workspace. </p>
<p> Similarly, when you <code>source</code> a Catkin workspace&#8217;s setup file from a workspace&#8217;s <code>devel space</code> or <code>install space</code>, it prepends the path containing that setup file to the <code>CMAKE_PREFIX_PATH</code> environment variable. The next time you initialize a workspace, it will extend the workspace that you previously sourced. </p>
<p> On one hand, this makes it easy and automatic to chain workspaces. At the same time, however, previous tools like <code>catkin_make</code> and <code>catkin_make_isolated</code> had no easy mechanism for either making it obvious which workspace was being extended, nor did they provide features to explicitly extend a given workspace. This means that for users unaware of Catkin&#8217;s use of <code>CMAKE_PREFIX_PATH</code> </p>
<p> Since it&#8217;s not expected that 100% of users will read this section of the documentation, the <code>catkin</code> program adds both configuration consistency checking for the value of <code>CMAKE_PREFIX_PATH</code> and makes it obvious on each invocation which workspace is being extended. Furthermore, the <code>catkin</code> command adds an explicit extension interface to override the value of <code>$CMAKE_PREFIX_PATH</code> with the <code>catkin config &#8211;extend</code> command. </p>
<p> <code>NOTE:</code> While workspaces can be chained together to add search paths, invoking a build in one workspace will not cause products in any other workspace to be built.</p>
<h2>CONFIGURATION SUMMARY</h2>
<h3>Contents of the Config Summary</h3>
<p> Most <code>catkin</code> commands which modify a workspace&#8217;s configuration will display the standard configuration summary, as shown below: </p>
<p>$ cd / tmp / path / to / my_catkin_ws $ catkin config&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None Workspace : / tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel Install Space : [missing] / tmp / path / to / my_catkin_ws / install DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Whitelisted Packages : None Blacklisted Packages : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<p> This summary describes the layout of the workspace as well as other important settings which influence build and execution behavior. Each of these options can be modified either with the <code>config</code> verb&#8217;s options described in the full command-line usage or by changing environment variables. The summary is composed of the following sections:</p>
<h3>Overview Section</h3>
<dl>
<dt>&bull;</p>
<dd> <code>Profile</code> &#8212; The name of this configuration</p>
<dt>&bull;</p>
<dd> <code>Extending</code> &#8212; Describes if your current configuration will extend another Catkin workspace, and through which mechanism it determined the location of the extended workspace:</p>
<dt>&bull;</p>
<dd> <i>No Chaining</i> </p>
<pre>
Extending:                   None
</pre>
<dt>&bull;</p>
<dd> <i>Implicit Chaining</i> &#8212; Derived from the <code>CMAKE_PREFIX_PATH</code> environment or cache variable. </p>
<pre>
Extending:             [env] /opt/ros/hydro
</pre>
<pre>
Extending:          [cached] /opt/ros/hydro
</pre>
<dt>&bull;</p>
<dd> <i>Explicit Chaining</i> &#8212; Specified by <code>catkin config &#8211;extend</code> </p>
<pre>
Extending:        [explicit] /opt/ros/hydro
</pre>
<dt>&bull;</p>
<dd> <code>[* Space]</code> &#8212; Lists the paths to each of the catkin &quot;spaces&quot; and whether or not they exist</p>
<dt>&bull;</p>
<dd> <code>DESTDIR</code> &#8212; An optional prefix to the <code>install space</code> as defined by <i>GNU Standards</i></p>
<dt>&bull;</p>
<dd> <code>Isolate Develspaces</code> &#8212; Builds products (like libraries and binaries) into individual FHS subdirectories in the <code>devel space</code>, instead of a single FHS directory</p>
<dt>&bull;</p>
<dd> <code>Install Packages</code> &#8212; Enable creating and installation into the <code>install space</code></p>
<dt>&bull;</p>
<dd> <code>Isolate Installs</code> &#8212; Installs products into individual FHS subdirectories in the <code>install space</code></p>
<dt>&bull;</p>
<dd> <code>Additional CMake Args</code> &#8212; Arguments to be passed to CMake during the <i>configuration</i> step for all packages to be built.</p>
<dt>&bull;</p>
<dd> <code>Additional Make Args</code> &#8212; Arguments to be passed to Make during the <i>build</i> step for all packages to be built.</p>
<dt>&bull;</p>
<dd> <code>Additional catkin Make Args</code> &#8212; Similar to <code>Additional Make Args</code> but only applies to Catkin packages.</p>
<dt>&bull;</p>
<dd> <code>Package Whitelist</code> &#8212; These are the packages that will be built with a bare call to <code>catkin build</code></p>
<dt>&bull;</p>
<dd> <code>Package Blacklist</code> &#8212; These are the packages that will <i>not</i> be built unless explicitly named</dl>
<h3>Notes Section</h3>
<p> The summary will sometimes contain notes about the workspace or the action that you&#8217;re performing, or simply tell you that the workspace configuration appears valid.</p>
<h3>Warnings Section</h3>
<p> If something is wrong with your configuration such as a missing source space, an additional section will appear at the bottom of the summary with details on what is wrong and how you can fix it.</p>
<h3>Workspace Chaining Mode</h3>
<p> An important property listed in the configuration configuration which deserves attention is the summary value of the <code>Extending</code> property. This affects which other collections of libraries and packages which will be visible to your workspace. This is process called &quot;workspace chaining.&quot; For more details on this see the details about workspace chaining and <code>CMAKE_PREFIX_PATH</code> in <code>Workspace Mechanics</code>. </p>
<p> The information about which workspace to extend can come from a few different sources, and can be classified in one of three ways:</p>
<h3>No Chaining</h3>
<p> This is what is shown in the above example configuration and it implies that there are no other Catkin workspaces which this workspace extends. The user has neither explicitly specified a workspace to extend, and the <code>CMAKE_PREFIX_PATH</code> environment variable is empty: </p>
<pre>
Extending:                   None
</pre>
<h3>Implicit Chaining via <code>CMAKE_PREFIX_PATH</code> Environment or Cache Variable</h3>
<p> In this case, the <code>catkin</code> command is <i>implicitly</i> assuming that you want to build this workspace against resources which have been built into the directories listed in your <code>CMAKE_PREFIX_PATH</code> environment variable. As such, you can control this value simply by changing this environment variable. </p>
<p> For example, ROS users who load their system&#8217;s installed ROS environment by calling something similar to <code>source /opt/ros/hydro/setup.bash</code> will normally see an <code>Extending</code> value such as: </p>
<pre>
Extending:             [env] /opt/ros/hydro
</pre>
<p> If you don&#8217;t want to extend the given workspace, unsetting the <code>CMAKE_PREFIX_PATH</code> environment variable will change it back to none. You can also alternatively </p>
<p> Once you have built your workspace once, this <code>CMAKE_PREFIX_PATH</code> will be cached by the underlying CMake buildsystem. As such, the <code>Extending</code> status will subsequently describe this as the &quot;cached&quot; extension path: </p>
<pre>
Extending:          [cached] /opt/ros/hydro
</pre>
<p> Once the extension mode is cached like this, you must use <code>catkin clean</code> to before changing it to something else.</p>
<h3>Explicit Chaining via <code>catkin config &#8211;extend</code></h3>
<p> This behaves like the above implicit chaining except it means that this workspace is <i>explicitly</i> extending another workspace and the workspaces which the other workspace extends, recursively. This can be set with the <code>catkin config &#8211;extend</code> command. It will override the value of <code>CMAKE_PREFIX_PATH</code> and persist between builds. </p>
<pre>
Extending:        [explicit] /tmp/path/to/other_ws
</pre>
<h2>CHEAT SHEET</h2>
<p> This is a non-exhaustive list of some common and useful invocations of the <code>catkin</code> command. All of the commands which do not explicitly specify a workspace path (with <code>&#8211;workspace</code>) are assumed to be run from within a directory contained by the target workspace. For thorough documentation, please see the chapters on each verb.</p>
<h3>Initializing Workspaces</h3>
<dl>
<dt><code>Initialize a workspace with a default layout (src</code>/<code>build</code>/<code>devel</code>) in the <i>current</i> directory:</p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin init</code></p>
<dt>&bull;</p>
<dd> <code>catkin init &#8211;workspace .</code></p>
<dt>&bull;</p>
<dd> <code>catkin config &#8211;init</code></p>
<dt>&bull;</p>
<dd> <code>mkdir src &amp;&amp; catkin build</code></p>
<dt><code>&#8230; with a default layout in a </code><i>different</i> directory:</p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin init &#8211;workspace /tmp/path/to/my_catkin_ws</code></p>
<dt><code>&#8230; which explicity extends another workspace:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin config &#8211;init &#8211;extend /opt/ros/hydro</code></p>
<dt><code>Initialize a workspace with a source space</code> called <code>other_src</code>:</p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin config &#8211;init &#8211;source-space other_src</code></p>
<dt><code>&#8230; or a workspace with build</code>, <code>devel</code>, and <code>install space</code> ending with the suffix <code>_alternate</code>:</p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin config &#8211;init &#8211;space-suffix _alternate</code></dl>
<h3>Configuring Workspaces</h3>
<dl>
<dt><code>View the current configuration:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin config</code></p>
<dt><code>Setting and un-setting CMake options:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin config &#8211;cmake-args -DENABLE_CORBA=ON -DCORBA_IMPLEMENTATION=OMNIORB</code></p>
<dt>&bull;</p>
<dd> <code>catkin config &#8211;no-cmake-args</code></p>
<dt><code>Toggle installing to the specified install space</code>:</p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin config &#8211;install</code></dl>
<h3>Building Packages</h3>
<dl>
<dt><code>Build all the packages:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build</code></p>
<dt><code>&#8230; one at a time, with additional debug output:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build -p 1</code></p>
<dt><code>&#8230; and force CMake to re-configure for each one:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build &#8211;force-cmake</code></p>
<dt><code>Build a specific package and its dependencies:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build my_package</code></p>
<dt><code>&#8230; or ignore its dependencies:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build my_package &#8211;no-deps</code></p>
<dt><code>Build the package containing the current working directory:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build &#8211;this</code></p>
<dt><code>&#8230; but don&#8217;t rebuild its dependencies:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build &#8211;this &#8211;no-deps</code></p>
<dt><code>Build packages with aditional CMake args:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build &#8211;cmake-args -DCMAKE_BUILD_TYPE=Debug</code></p>
<dt><code>&#8230; and save them to be used for the next build:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build &#8211;save-config &#8211;cmake-args -DCMAKE_BUILD_TYPE=Debug</code></p>
<dt><code>Build all packages in a given directory:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build $(catkin list -u /path/to/folder)</code></p>
<dt><code>&#8230; or in the current folder:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin build $(catkin list -u .)</code></dl>
<h3>Cleaning Build Products</h3>
<dl>
<dt><code>Blow away the build, devel, and install spaces (if they exist):</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin clean -a</code></p>
<dt><code>&#8230; or just the build space</code>:</p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin clean &#8211;build</code></p>
<dt><code>&#8230; or just delete the </code><i>CMakeCache.txt</i> files for each package:</p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin clean &#8211;cmake-cache</code></p>
<dt><code>&#8230; or just delete the build directories for packages which have been disabled or removed:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin clean &#8211;orphans</code></dl>
<h3>Controlling Color Display</h3>
<dl>
<dt><code>Disable colors when building in a shell that doesn&#8217;t support it (like IDEs):</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin &#8211;no-color build</code></p>
<dt><code>&#8230; or enable it for shells that don&#8217;t know they support it:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>catkin &#8211;force-color build</code></dl>
<h3>Profile Cookbook</h3>
<dl>
<dt><code>Create Debug and Release profiles and then build them in independent build and devel spaces:</code></p>
<dd>
<p>catkin config&#8211; profile debug &#8211; x _debug&#8211; cmake &#8211; args &#8211; DCMAKE_BUILD_TYPE = Debug<br />
                                                                                  catkin config&#8211; profile release &#8211;<br />
                                                                              x _release&#8211; cmake &#8211; args &#8211; DCMAKE_BUILD_TYPE = Release<br />
                                                                                  catkin build&#8211; profile debug<br />
                                                                                      catkin build&#8211; profile release</p>
<dt><code>Quickly build a package from scratch to make sure all of its dependencies are satisfied, then clean it:</code></p>
<dd>
<p>catkin config&#8211; profile my_pkg &#8211; x _my_pkg_test<br />
                                     catkin build&#8211; profile my_pkg my_pkg<br />
                                         catkin clean&#8211; profile my_pkg&#8211; all
</dl>
<h3>Manipulating Workspace Chaining</h3>
<dl>
<dt><code>Change from implicit to explicit chaining:</code></p>
<dd>
<pre>
catkin clean -a
catkin config --extend /opt/ros/hydro
</pre>
<dt><code>Change from explicit to implicit chaining:</code></p>
<dd>
<pre>
catkin clean -a
catkin config --no-extend
</pre>
</dl>
<h3>Building With Other Jobservers</h3>
<dl>
<dt><code>Build with distcc</code>:</p>
<dd>
<pre>
CC=&quot;distcc gcc&quot; CXX=&quot;distcc g++&quot; catkin build -p$(distcc -j) -j$(distcc -j) --no-jobserver
</pre>
</dl>
<h2>TROUBLESHOOTING</h2>
<h3>Configuration Summary Warnings</h3>
<p> The <code>catkin</code> tool is capable of detecting some issues or inconsistencies with the build configuration automatically. In these cases, it will often describe the problem as well as how to resolve it. The <code>catkin</code> tool will detect the following issues automatically.</p>
<h3>Missing Workspace Components</h3>
<dl>
<dt>&bull;</p>
<dd> Uninitialized workspace (mising <code>.catkin_tools</code> directory)</p>
<dt>&bull;</p>
<dd> Missing <code>source space</code> as specified by the configuration</dl>
<h3>Inconsistent Environment</h3>
<dl>
<dt>&bull;</p>
<dd> The <code>CMAKE_PREFIX_PATH</code> environment variable is different than the cahced <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd> The explicitly extended workspace path yeilds a different <code>CMAKE_PREFIX_PATH</code> than the cached <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd> The <code>build space</code> or <code>devel space</code> was built with a different tool such as <code>catkin_make</code> or <code>catkin_make_isolated</code></p>
<dt>&bull;</p>
<dd> The <code>build space</code> or <code>devel space</code> was built in a different isolation mode</dl>
<h3>Dependency Resolution</h3>
<h3>Packages Are Being Built Out of Order</h3>
<dl>
<dt>&bull;</p>
<dd> The <code>package.xml</code> dependency tags are most likely incorrect. Note that dependencies are only used to order the packages, and there is no warning if a package can&#8217;t be found.</p>
<dt>&bull;</p>
<dd> Run <code>catkin list &#8211;deps /path/to/ws/src</code> to list the dependencies of each package and look for errors.</dl>
<h2>CATKIN BUILD &#8212; BUILD PACKAGES</h2>
<p> The <code>build</code> verb for the <code>catkin</code> command is used to build one or more packages in a catkin workspace. Like most <code>catkin</code> verbs, the <code>catkin build</code> verb is context-aware. This means that it can be executed from within any directory contained by an <i>initialized</i> workspace. </p>
<p> If a workspace is not yet initialized, <code>catkin build</code> can initialize it, but only if it is called from the workspace root and the default workspace structure is desired. </p>
<p> Workspaces can also be built from arbitrary working directories if the user specifies the path to the workspace with the <code>&#8211;workspace</code> option. </p>
<p> <code>NOTE:</code> To set up the workspace and clone the repositories used in the following examples, you can use <i>rosinstall_generator</i> and <i>wstool</i>. This clones all of the ROS packages necessary for building the introductory ROS tutorials: </p>
<pre>
$ mkdir -p /tmp/path/to/my_catkin_ws/src
$ cd /tmp/path/to/my_catkin_ws
$ catkin init
$ cd /tmp/path/to/my_catkin_ws/src
$ rosinstall_generator --deps ros_tutorials &gt; .rosinstall
$ wstool update
</pre>
<h3>Basic Usage</h3>
<p> Consider a Catkin workspace with a <code>source space</code> populated with the following Catkin packages which have yet to be built: </p>
<pre>
$ pwd
/tmp/path/to/my_catkin_ws
$ ls ./*
./src:
catkin             console_bridge     genlisp            genpy
message_runtime    ros_comm           roscpp_core        std_msgs
common_msgs        gencpp             genmsg             message_generation
ros                ros_tutorials      rospack
</pre>
<h3>Previewing The Build</h3>
<p> Before actually building anything in the workspace, it is useful to preview which packages <code>catkin build</code> will build, and in what order. This can be done with the <code>&#8211;dry-run</code> option: </p>
<p>$ catkin build&#8211; dry &#8211; run&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None Workspace : / tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel Install Space : [missing] / tmp / path / to / my_catkin_ws / install DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Whitelisted Packages : None Blacklisted Packages : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Found &#8217;36&#8217; packages in 0.0 seconds.Packages to be built : -catkin(catkin) &#8211; genmsg(catkin) &#8211; gencpp(catkin) &#8211; genlisp(catkin) &#8211; genpy(catkin) &#8211; console_bridge(cmake) &#8211; cpp_common(catkin) &#8211; message_generation(catkin) &#8211; message_runtime(catkin) &#8211; ros_tutorials(metapackage) &#8211; rosbuild(catkin) &#8211; rosclean(catkin) &#8211; roscpp_traits(catkin) &#8211; rosgraph(catkin) &#8211; roslang(catkin) &#8211; roslaunch(catkin) &#8211; rosmaster(catkin) &#8211; rospack(catkin) &#8211; roslib(catkin) &#8211; rosparam(catkin) &#8211; rospy(catkin) &#8211; rostime(catkin) &#8211; roscpp_serialization(catkin) &#8211; rosunit(catkin) &#8211; rosconsole(catkin) &#8211; rostest(catkin) &#8211; std_msgs(catkin) &#8211; geometry_msgs(catkin) &#8211; rosgraph_msgs(catkin) &#8211; std_srvs(catkin) &#8211; xmlrpcpp(catkin) &#8211; roscpp(catkin) &#8211; roscpp_tutorials(catkin) &#8211; rosout(catkin) &#8211; rospy_tutorials(catkin) &#8211; turtlesim(catkin) Total packages : 36</p>
<p> In addition to the listing the package names and in which order they would be built, it also displays the buildtool type of each package. Among those listed above are:</p>
<dl>
<dt>&bull;</p>
<dd> <code>catkin</code> &#8212; A CMake package which uses Catkin</p>
<dt>&bull;</p>
<dd> <code>cmake</code> &#8212; A &quot;vanilla&quot; CMake package</p>
<dt>&bull;</p>
<dd> <code>metapackage</code> &#8212; A package which contains no build products, but just groups other packages together for distribution</dl>
<h3>Building Specific Packages</h3>
<p> In addition to the usage above, the <code>&#8211;dry-run</code> option will show what the behavior of <code>catkin build</code> will be with various other options. For example, the following will happen when you specify a single package to build: </p>
<pre>
$ catkin build roscpp_tutorials --dry-run
....
Found '36' packages in 0.1 seconds.
Packages to be built:
- catkin               (catkin)
- genmsg               (catkin)
- gencpp               (catkin)
- genlisp              (catkin)
- genpy                (catkin)
- console_bridge       (cmake)
- cpp_common           (catkin)
- message_generation   (catkin)
- message_runtime      (catkin)
- rosbuild             (catkin)
- roscpp_traits        (catkin)
- roslang              (catkin)
- rospack              (catkin)
- roslib               (catkin)
- rostime              (catkin)
- roscpp_serialization (catkin)
- rosunit              (catkin)
- rosconsole           (catkin)
- std_msgs             (catkin)
- rosgraph_msgs        (catkin)
- xmlrpcpp             (catkin)
- roscpp               (catkin)
- roscpp_tutorials     (catkin)
Total packages: 23
</pre>
<p> As shown above, only 23 packages (<code>roscpp_tutorials</code> and its dependencies), of the total 36 packages would be built.</p>
<h3>Skipping Packages</h3>
<p> Suppose you built every package up to <code>roscpp_tutorials</code>, but that package had a build error. After fixing the error, you could run the same build command again, but the <code>build</code> verb provides an option to save time in this situation. If re-started from the beginning, none of the products of the dependencies of <code>roscpp_tutorials</code> would be re-built, but it would still take some time for the underlying byuildsystem to verify that for each package. </p>
<p> Those checks could be skipped, however, by jumping directly to a given package. You could use the <code>&#8211;start-with</code> option to continue the build where you left off after fixing the problem. (The following example uses the <code>&#8211;dry-run</code> option again to preview the behavior): </p>
<p>$ catkin build roscpp_tutorials&#8211; start &#8211; with roscpp_tutorials&#8211; dry &#8211; run&#8230;.Found &#8217;36&#8217; packages in 0.0 seconds.Packages to be built : (skip)catkin(catkin)(skip) genmsg(catkin)(skip) gencpp(catkin)(skip) genlisp(catkin)(skip) genpy(catkin)(skip) console_bridge(cmake)(skip) cpp_common(catkin)(skip) message_generation(catkin)(skip) message_runtime(catkin)(skip) rosbuild(catkin)(skip) roscpp_traits(catkin)(skip) roslang(catkin)(skip) rospack(catkin)(skip) roslib(catkin)(skip) rostime(catkin)(skip) roscpp_serialization(catkin)(skip) rosunit(catkin)(skip) rosconsole(catkin)(skip) std_msgs(catkin)(skip) rosgraph_msgs(catkin)(skip) xmlrpcpp(catkin)(skip) roscpp(catkin)&#8211; &#8212; &#8211;roscpp_tutorials(catkin) Total packages : 23</p>
<p> However, you should be careful when using the <code>&#8211;start-with</code> option, as <code>catkin build</code> will assume that all dependencies leading up to that package have already been successfully built. </p>
<p> If you&#8217;re only interested in building a <i>single</i> package in a workspace, you can also use the <code>&#8211;no-deps</code> option along with a package name. This will skip all of the package&#8217;s dependencies, build the given package, and then exit. </p>
<pre>
$ catkin build roscpp_tutorials --no-deps roscpp_tutorials --dry-run
....
Found '36' packages in 0.0 seconds.
Packages to be built:
- roscpp_tutorials     (catkin)
Total packages: 1
</pre>
<h3>Build Products</h3>
<p> At this point the workspace has not been modified, but once we tell the <code>build</code> verb to actually build the workspace then directories for a <code>build space</code> and a <code>devel space</code> will be created: </p>
<p>$ catkin build<br />
    Creating buildspace directory,<br />
    &#8216;/tmp/path/to/my_catkin_ws/build&#8217; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None<br />
                                                                                                                                                                    Workspace : /<br />
                                                                                                                                                                                tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel Install Space : [missing] / tmp / path / to / my_catkin_ws / install DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Whitelisted Packages : None Blacklisted Packages : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Found &#8217;36&#8217; packages in 0.0 seconds.Starting ==<br />
        &gt; catkin<br />
                Starting ==<br />
        &gt; console_bridge<br />
                Finished &lt;= = catkin[2.4 seconds]&#8230;.<br />
                                  [build] Finished.<br />
                                      [build] Runtime : 3 minutes and<br />
                              54.6 seconds</p>
<p> Since no packages were given as arguments, <code>catkin build</code> built all of the packages in the workspace. </p>
<p> As shown above, after the build finishes, we now have a <code>build space</code> with a folder containing the intermediate build products for each package and a <code>devel space</code> with an FHS layout into which all the final build products have been written. </p>
<pre>
$ ls ./*
./build:
catkin               genlisp              message_runtime      roscpp
rosgraph_msgs        rosout               rostest              turtlesim
build_logs           genmsg               ros_tutorials
roscpp_serialization roslang              rospack              rostime
xmlrpcpp             console_bridge       genpy                rosbuild
roscpp_traits        roslaunch            rosparam             rosunit
cpp_common           geometry_msgs        rosclean
roscpp_tutorials     roslib               rospy                std_msgs
gencpp               message_generation   rosconsole           rosgraph
rosmaster            rospy_tutorials      std_srvs
./devel:
_setup_util.py bin            env.sh         etc            include
lib            setup.bash     setup.sh       setup.zsh      share
./src:
catkin             console_bridge     genlisp            genpy
message_runtime    ros_comm           roscpp_core        std_msgs
common_msgs        gencpp             genmsg             message_generation
ros                ros_tutorials      rospack
</pre>
<p> <code>NOTE:</code> The products of <code>catkin build</code> differ significantly from the behavior of <code>catkin_make</code>, for example, which would have all of the build files and intermediate build products in a combined <code>build space</code> or <code>catkin_make_isolated</code> which would have an isolated FHS directory for each package in the <code>devel space</code>.</p>
<h3>Context-Aware Building</h3>
<p> In addition to building all packages or specified packages with various dependency requirements, <code>catkin build</code> can also determine the package containing the current working directory. This is equivalent to specifying the name of the package on the command line, and is done by passing the <code>&#8211;this</code> option to <code>catkin build</code> like the following: </p>
<pre>
$ cd /tmp/path/to/my_catkin_ws/src/roscpp_tutorials
$ catkin build --this --dry-run
....
Found '36' packages in 0.0 seconds.
Packages to be built:
- roscpp_tutorials     (catkin)
Total packages: 1
</pre>
<h3>Controlling the Number of Build Jobs</h3>
<p> By default <code>catkin build</code> on a computer with <code>N</code> cores will build up to <code>N</code> packages in parallel and will distribute <code>N</code> <code>make</code> jobs among them using an internal jobserver. If your platform doesn&#8217;t support jobserver scheduling, <code>catkin build</code> will pass <code>-jN -lN</code> to <code>make</code> for each package. </p>
<p> You can control the maximum number of packages allowed to build in parallel by using the <code>-p</code> or <code>&#8211;parallel-packages</code> option and you can change the number of <code>make</code> jobs available with the <code>-j</code> or <code>&#8211;jobs</code> option. </p>
<p> By default, these jobs options aren&#8217;t passed to the underlying <code>make</code> command. To disable the jobserver, you can use the <code>&#8211;no-jobserver</code> option, and you can pass flags directly to <code>make</code> with the <code>&#8211;make-args</code> option. </p>
<p> <code>NOTE:</code> Jobs flags (<code>-jN</code> and/or <code>-lN</code>) can be passed directly to <code>make</code> by giving them to <code>catkin build</code>, but other <code>make</code> arguments need to be passed to the <code>&#8211;make-args</code> option.</p>
<h3>Controlling Command-Line Output</h3>
<h3>Status Line</h3>
<p> While running <code>catkin build</code> with default options, you would have seen the &quot;live&quot; status lines similar to the following: </p>
<p>[build &#8211; 5.9][genmsg &#8211; 1.3][message_runtime &#8211; 0.7]&#8230;[4 / 4 Active | 3 / 36 Completed]</p>
<p> This status line stays at the bottom of the screen and displays the continuously-updated progress of the entire build as well as the active build jobs which are still running. It is composed of the following information:</p>
<dl>
<dt>&bull;</p>
<dd> <code>Total Build Time</code> &#8212; The first block on the left, indicates the total elapsed build time in seconds thus far. Above, <code>[build &#8211; 5.9]</code> means that the build has been running for a total of <code>5.9</code> seconds.</p>
<dt>&bull;</p>
<dd> <code>Active Job Status</code> &#8212; The next blocks show the currently active jobs with as name of the package being built and the elapsed time for that job, in seconds. The above block like <code>[genmsg &#8211; 1.3]</code> means that the <code>genmsg</code> package is currently being built, and it has been building for <code>1.3</code> seconds.</p>
<dt>&bull;</p>
<dd> <code>Active and Completed Counts</code> &#8212; The final block, justified to the right, is the number of packages being actively built out of the total allowed parallel jobs (specified with the <code>-p</code> options) as well as the number of completed packages out of the total. Above, the block <code>[4/4 Active | 3/36 Completed]</code> means that there are four out of four jobs active and three of the total 36 packages to be built have been completed. </p>
<p> This status line can be disabled by passing the <code>&#8211;no-status</code> option to <code>catkin build</code>.</dl>
<h3>Package Build Messages</h3>
<p> Normally, unless an error occurs, the output from each package&#8217;s build proces is collected but not printed to the console. All that is printed is a pair of messages designating the start and end of a package&#8217;s build. This is formatted like the following for the <code>genmsg</code> package: </p>
<p>Starting == &gt; genmsg<br />
                    Finished &lt;= = genmsg[2.4 seconds]</p>
<p> However, if you would like to see more of the messages from the underlying buildsystem, you can invoke the <code>-v</code> or <code>&#8211;verbose</code> option. This will print the normal message when a package build starts and finished as well as the output of each build command in a block, once it finishes: </p>
<p>Starting ==&gt; catkin<br />
[catkin]: ==&gt; &#8216;/path/to/my_catkin_ws/build/catkin/build_env.sh /usr/local/bin/cmake /path/to/my_catkin_ws/src/catkin -DCATKIN_DEVEL_PREFIX=/path/to/my_catkin_ws/devel/catkin -DCMAKE_INSTALL_PREFIX=/path/to/my_catkin_ws/install&#8217; in &#8216;/path/to/my_catkin_ws/build/catkin&#8217;<br />
&#8212; The C compiler identification is Clang 5.0.0<br />
&#8212; The CXX compiler identification is Clang 5.0.0<br />
&#8212; Check for working C compiler: /usr/bin/cc<br />
&#8212; Check for working C compiler: /usr/bin/cc &#8212; works<br />
&#8212; Detecting C compiler ABI info<br />
&#8212; Detecting C compiler ABI info &#8211; done<br />
&#8212; Check for working CXX compiler: /usr/bin/c++<br />
&#8212; Check for working CXX compiler: /usr/bin/c++ &#8212; works<br />
&#8212; Detecting CXX compiler ABI info<br />
&#8212; Detecting CXX compiler ABI info &#8211; done<br />
&#8212; Using CATKIN_DEVEL_PREFIX: /path/to/my_catkin_ws/devel/catkin<br />
&#8212; Using CMAKE_PREFIX_PATH: /path/to/my_catkin_ws/install<br />
&#8212; This workspace overlays: /path/to/my_catkin_ws/install<br />
&#8212; Found PythonInterp: /usr/bin/python (found version &#8220;2.7.5&#8221;)<br />
&#8212; Using PYTHON_EXECUTABLE: /usr/bin/python<br />
&#8212; Python version: 2.7<br />
&#8212; Using default Python package layout<br />
&#8212; Found PY_em: /Library/Python/2.7/site-packages/em.pyc<br />
&#8212; Using CATKIN_ENABLE_TESTING: ON<br />
&#8212; Call enable_testing()<br />
&#8212; Using CATKIN_TEST_RESULTS_DIR: /path/to/my_catkin_ws/build/catkin/test_results<br />
&#8212; Found gtest: gtests will be built<br />
&#8212; catkin 0.5.86<br />
&#8212; Configuring done<br />
&#8212; Generating done<br />
&#8212; Build files have been written to: /path/to/my_catkin_ws/build/catkin<br />
[catkin]: &lt;== &#8216;/path/to/my_catkin_ws/build/catkin/build_env.sh /usr/local/bin/cmake /path/to/my_catkin_ws/src/catkin -DCATKIN_DEVEL_PREFIX=/path/to/my_catkin_ws/devel/catkin -DCMAKE_INSTALL_PREFIX=/path/to/my_catkin_ws/install&#8217; finished with return code &#8216;0&#8217;<br />
[catkin]: ==&gt; &#8216;/path/to/my_catkin_ws/build/catkin/build_env.sh /usr/bin/make -j4 -l4&#8217; in &#8216;/path/to/my_catkin_ws/build/catkin&#8217;<br />
[catkin]: &lt;== &#8216;/path/to/my_catkin_ws/build/catkin/build_env.sh /usr/bin/make -j4 -l4&#8217; finished with return code &#8216;0&#8217;<br />
[catkin]: ==&gt; &#8216;/path/to/my_catkin_ws/build/catkin/build_env.sh /usr/bin/make install&#8217; in &#8216;/path/to/my_catkin_ws/build/catkin&#8217;<br />
Install the project&#8230;<br />
&#8212; Install configuration: &#8220;&#8221;<br />
&#8230; truncated for brevity<br />
[catkin]: &lt;== &#8216;/path/to/my_catkin_ws/build/catkin/build_env.sh /usr/bin/make install&#8217; finished with return code &#8216;0&#8217;<br />
Finished &lt;== catkin [ 3.4 seconds ]</p>
<p> <code>NOTE:</code> The printing of these command outputs maybe be interleaved with commands from other package builds if more than one package is being built at the same time. </p>
<p> If you want to see the output from commands streaming to the screen, then you can use the <code>-i</code> or <code>&#8211;interleave</code> option. This option will cause the output from commands to be pushed to the screen immediately, instead of buffering until the command finishes. This ends up being pretty confusing, so when interleaved output is used <code>catkin build</code> prefixes each line with <code>[&lt;package name&gt;]:</code> like this: </p>
<p>[roscpp_traits]: ==&gt; &#8216;/Users/william/my_catkin_ws/build/roscpp_traits/build_env.sh /usr/bin/make cmake_check_build_system&#8217; in &#8216;/Users/william/my_catkin_ws/build/roscpp_traits&#8217;<br />
[ros_tutorials]: &#8212; The CXX compiler identification is Clang 5.0.0<br />
[ros_tutorials]: &#8212; Check for working C compiler: /usr/bin/cc<br />
[roscpp_traits]: ==&gt; &#8216;/Users/william/my_catkin_ws/build/roscpp_traits/build_env.sh /usr/bin/make -j4 -l4&#8217; in &#8216;/Users/william/my_catkin_ws/build/roscpp_traits&#8217;<br />
[rosbuild]: ==&gt; &#8216;/Users/william/my_catkin_ws/build/rosbuild/build_env.sh /usr/bin/make -j4 -l4&#8217; in &#8216;/Users/william/my_catkin_ws/build/rosbuild&#8217;<br />
[rosclean]: &#8212; The C compiler identification is Clang 5.0.0<br />
[ros_tutorials]: &#8212; Check for working C compiler: /usr/bin/cc &#8212; works<br />
[ros_tutorials]: &#8212; Detecting C compiler ABI info<br />
[rosclean]: &#8212; The CXX compiler identification is Clang 5.0.0<br />
[rosclean]: &#8212; Check for working C compiler: /usr/bin/cc</p>
<p> <code>NOTE:</code> When you use <code>-p 1</code> and <code>-v</code> at the same time, <code>-i</code> is implicitly added.</p>
<h3>Running Tests Built in a Workspace</h3>
<p> Running tests for a given package typically is done by invoking a special <code>make</code> target like <code>test</code> or <code>run_tests</code>. catkin packages all define the <code>run_tests</code> target which aggregates all types of tests and runs them together. So in order to get tests to build and run for your packages you need to pass them this additional <code>run_tests</code> or <code>test</code> target as a command line option to <code>make</code>. </p>
<p> To run catkin tests for all catkin packages in the workspace, use the following: </p>
<pre>
$ catkin run_tests
</pre>
<p> Or the longer version: </p>
<pre>
$ catkin build [...] --catkin-make-args run_tests
</pre>
<p> To run a catkin test for a specific catkin package, from a directory within that package: </p>
<pre>
$ catkin run_tests --no-deps --this
</pre>
<p> For non-catkin packages which define a <code>test</code> target, you can do this: </p>
<pre>
$ catkin build [...] --make-args test
</pre>
<p> If you want to run tests for just one package, then you should build that package and this narrow down the build to just that package with the additional make argument: </p>
<p>$ # First build the package<br />
$ catkin build package<br />
&#8230;<br />
$ # Then run its tests<br />
$ catkin build package &#8211;no-deps &#8211;catkin-make-args run_tests<br />
$ # Or for non-catkin packages<br />
$ catkin build package &#8211;no-deps &#8211;make-args test</p>
<p> For catkin packages and the <code>run_tests</code> target, failing tests will not result in an non-zero exit code. So if you want to check for failing tests, use the <code>catkin_test_results</code> command like this: </p>
<pre>
$ catkin_test_results build/&lt;package name&gt;
</pre>
<p> The result code will be non-zero unless all tests passed.</p>
<h3>Building With Warnings</h3>
<p> It can sometimes be useful to compile with additional warnings enabled across your whole catkin workspace. To achieve this, use a command similar to this: </p>
<pre>
$ catkin build -v --cmake-args -DCMAKE_C_FLAGS=&quot;-Wall -W -Wno-unused-parameter&quot;
</pre>
<p> This command passes the <code>-DCMAKE_C_FLAGS=&#8230;</code> arugment to all invocations of <code>cmake</code>.</p>
<h3>Debugging Build Errors</h3>
<p> As mentioned above, by default the output from each build is optimistically hidden to give a clean overview of the workspace build, but when there is a problem with a build a few things happen. </p>
<p> First, the package with a failure prints the failing command&#8217;s output to the screen between some enclosing lines: </p>
<p>[rospack] : == &gt; &#8216;/path/to/my_catkin_ws/build/rospack/build_env.sh /usr/bin/make -j4 -l4&#8217; in &#8216;/path/to/my_catkin_ws/build/rospack&#8217;<br />
                       [66 % ] Built target rospack<br />
                           make[1] : ***[CMakeFiles / rosstackexe.dir / all] Interrupt : 2 make[1] : ***[CMakeFiles / rospackexe.dir / all] Interrupt : 2 make : ***[all] Interrupt : 2<br />
                                                                                                                                                                     [rospack] : &lt;= = &#8216;/path/to/my_catkin_ws/build/rospack/build_env.sh /usr/bin/make -j4 -l4&#8217; failed with return code &#8216;-2&#8217;</p>
<p> And the status line is updated to reflect that that package has run into an issue by placing a <code>!</code> in front of it: </p>
<p>[build &#8211; 1.7][!cpp_common][!rospack][genlisp &#8211; 0.3][1 / 1 Active | 10 / 23 Completed]</p>
<p> Then the <code>catkin build</code> command waits for the rest of the currently still building packages to finish (without starting new package builds) and then summarizes the errors for you: </p>
<p>[build] There were &#8216;2&#8217; errors : Failed to build package &#8216;cpp_common&#8217; because the following command :<br />
#Command run in directory : / path / to / my_catkin_ws / build / cpp_common<br />
    /<br />
    path / to / my_catkin_ws / build / cpp_common / build_env.sh / usr / bin / make &#8211;<br />
    j4 &#8211; l4 Exited with return code : -2 Failed to build package &#8216;rospack&#8217; because the following command :<br />
#Command run in directory : / path / to / my_catkin_ws / build / rospack<br />
    /<br />
    path / to / my_catkin_ws / build / rospack / build_env.sh / usr / bin / make &#8211;<br />
    j4 &#8211; l4 Exited with return code : -2 Build summary : Successful catkin Successful genmsg&#8230; Failed cpp_common Failed rospack Not built roscpp_serialization Not built roscpp&#8230;</p>
<p> Packages marked as <i>Not built</i> were requested, but not yet built because catkin stopped due to failed packages. </p>
<p> To try to build as many requested packages as possible (instead of stopping after the first package failed), you can pass the <code>&#8211;continue-on-failure</code> option. Then the <code>catkin build</code> command will then continue building packages whose dependencies built successfully </p>
<p> If you don&#8217;t want to scroll back up to find the error amongst the other output, you can <code>cat</code> the whole build log out of the <code>build_logs</code> folder in the <code>build space</code>: </p>
<p>$ cat build / build_logs / rospack.log[rospack] : == &gt; &#8216;/path/to/my_catkin_ws/build/rospack/build_env.sh /usr/bin/make cmake_check_build_system&#8217; in &#8216;/path/to/my_catkin_ws/build/rospack&#8217;<br />
                                                             [rospack] : &lt;= = &#8216;/path/to/my_catkin_ws/build/rospack/build_env.sh /usr/bin/make cmake_check_build_system&#8217; finished with return code &#8216;0&#8217;<br />
                                                                                  [rospack] : == &gt; &#8216;/path/to/my_catkin_ws/build/rospack/build_env.sh /usr/bin/make -j4 -l4&#8217; in &#8216;/path/to/my_catkin_ws/build/rospack&#8217;<br />
                                                                                                         [66 % ] Built target rospack<br />
                                                                                                             make[1] : ***[CMakeFiles / rosstackexe.dir / all] Interrupt : 2 make[1] : ***[CMakeFiles / rospackexe.dir / all] Interrupt : 2 make : ***[all] Interrupt : 2<br />
                                                                                                                                                                                                                                                       [rospack] : &lt;= = &#8216;/path/to/my_catkin_ws/build/rospack/build_env.sh /usr/bin/make -j4 -l4&#8217; failed with return code &#8216;-2&#8217;</p>
<h3>Full Command-Line Interface</h3>
<p>usage: catkin build [-h] [&#8211;workspace WORKSPACE] [&#8211;profile PROFILE]<br />
                    [&#8211;dry-run] [&#8211;this] [&#8211;no-deps]<br />
                    [&#8211;start-with PKGNAME | &#8211;start-with-this | &#8211;continue-on-failure]<br />
                    [&#8211;force-cmake] [&#8211;no-install-lock] [&#8211;save-config]<br />
                    [&#8211;parallel-jobs PARALLEL_JOBS]<br />
                    [&#8211;cmake-args ARG [ARG &#8230;] | &#8211;no-cmake-args]<br />
                    [&#8211;make-args ARG [ARG &#8230;] | &#8211;no-make-args]<br />
                    [&#8211;catkin-make-args ARG [ARG &#8230;] | &#8211;no-catkin-make-args]<br />
                    [&#8211;verbose] [&#8211;interleave-output] [&#8211;no-status] [&#8211;no-notify]<br />
                    [PKGNAME [PKGNAME &#8230;]]<br />
Build one or more packages in a catkin workspace. This invokes `CMake`,<br />
`make`, and optionally `make install` for either all or the specified packages<br />
in a catkin workspace. Arguments passed to this verb can temporarily override<br />
persistent options stored in the catkin profile config. If you want to save<br />
these options, use the &#8211;save-config argument. To see the current config, use<br />
the `catkin config` command.<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;workspace WORKSPACE, -w WORKSPACE<br />
                        The path to the catkin_tools workspace or a directory<br />
                        contained within it (default: &#8220;.&#8221;)<br />
  &#8211;profile PROFILE     The name of a config profile to use (default: active<br />
                        profile)<br />
  &#8211;dry-run, -n         List the packages which will be built with the given<br />
                        arguments without building them.<br />
Packages:<br />
  Control which packages get built.<br />
  PKGNAME               Workspace packages to build, package dependencies are<br />
                        built as well unless &#8211;no-deps is used. If no packages<br />
                        are given, then all the packages are built.<br />
  &#8211;this                Build the package containing the current working<br />
                        directory.<br />
  &#8211;no-deps             Only build specified packages, not their dependencies.<br />
  &#8211;start-with PKGNAME  Build a given package and those which depend on it,<br />
                        skipping any before it.<br />
  &#8211;start-with-this     Similar to &#8211;start-with, starting with the package<br />
                        containing the current directory.<br />
  &#8211;continue-on-failure, -c<br />
                        Try to continue building packages whose dependencies<br />
                        built successfully even if some other requested<br />
                        packages fail to build.<br />
Build:<br />
  Control the build behavior.<br />
  &#8211;force-cmake         Runs cmake explicitly for each catkin package.<br />
  &#8211;no-install-lock     Prevents serialization of the install steps, which is<br />
                        on by default to prevent file install collisions<br />
Config:<br />
  Parameters for the underlying buildsystem.<br />
  &#8211;save-config         Save any configuration options in this section for the<br />
                        next build invocation.<br />
  &#8211;parallel-jobs PARALLEL_JOBS, &#8211;parallel PARALLEL_JOBS, -p PARALLEL_JOBS<br />
                        Maximum number of packages which could be built in<br />
                        parallel (default is cpu count)<br />
  &#8211;cmake-args ARG [ARG &#8230;]<br />
                        Arbitrary arguments which are passes to CMake. It<br />
                        collects all of following arguments until a &#8220;&#8211;&#8221; is<br />
                        read.<br />
  &#8211;no-cmake-args       Pass no additional arguments to CMake.<br />
  &#8211;make-args ARG [ARG &#8230;]<br />
                        Arbitrary arguments which are passes to make.It<br />
                        collects all of following arguments until a &#8220;&#8211;&#8221; is<br />
                        read.<br />
  &#8211;no-make-args        Pass no additional arguments to make (does not affect<br />
                        &#8211;catkin-make-args).<br />
  &#8211;catkin-make-args ARG [ARG &#8230;]<br />
                        Arbitrary arguments which are passes to make but only<br />
                        for catkin packages.It collects all of following<br />
                        arguments until a &#8220;&#8211;&#8221; is read.<br />
  &#8211;no-catkin-make-args<br />
                        Pass no additional arguments to make for catkin<br />
                        packages (does not affect &#8211;make-args).<br />
Interface:<br />
  The behavior of the command-line interface.<br />
  &#8211;verbose, -v         Print output from commands in ordered blocks once the<br />
                        command finishes.<br />
  &#8211;interleave-output, -i<br />
                        Prevents ordering of command output when multiple<br />
                        commands are running at the same time.<br />
  &#8211;no-status           Suppresses status line, useful in situations where<br />
                        carriage return is not properly supported.<br />
  &#8211;no-notify           Suppresses system popup notification.</p>
<h2>CATKIN CLEAN &#8212; CLEAN BUILD PRODUCTS</h2>
<p> The <code>clean</code> verb makes it easier and safer to clean various products of a catkin workspace. In addition to removing entire <code>build</code>, <code>devel</code>, and <code>install spaces</code>, it also gives you more fine-grained control over removing just parts of these directories. </p>
<p> The <code>clean</code> verb is context-aware, but in order to work, it must be given the path to an initialized catkin workspace, or called from a path contained in an initialized catkin workspace. This is because the paths to the relevant spaces are contained in a workspace&#8217;s metadata directory.</p>
<h3>Full Command-Line Interface</h3>
<p>usage: catkin clean [-h] [&#8211;workspace WORKSPACE] [&#8211;profile PROFILE] [-a] [-b]<br />
                    [-d] [-i] [-c] [-o]<br />
Deletes various products of the build verb.<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;workspace WORKSPACE, -w WORKSPACE<br />
                        The path to the catkin_tools workspace or a directory<br />
                        contained within it (default: &#8220;.&#8221;)<br />
  &#8211;profile PROFILE     The name of a config profile to use (default: active<br />
                        profile)<br />
Basic:<br />
  Clean workspace subdirectories.<br />
  -a, &#8211;all             Remove all of the *spaces associated with the given or<br />
                        active profile. This will remove everything but the<br />
                        source space and the hidden .catkin_tools directory.<br />
  -b, &#8211;build           Remove the buildspace.<br />
  -d, &#8211;devel           Remove the develspace.<br />
  -i, &#8211;install         Remove the installspace.<br />
Advanced:<br />
  Clean only specific parts of the workspace.<br />
  -c, &#8211;cmake-cache     Clear the CMakeCache for each package, but leave build<br />
                        and devel spaces.<br />
  -o, &#8211;orphans         Remove only build directories whose source packages<br />
                        are no longer enabled or in the source space. This<br />
                        might require &#8211;force-cmake on the next build.</p>
<h2>CATKIN CONFIG &#8212; CONFIGURE A WORKSPACE</h2>
<p> The <code>config</code> verb can be used to both view and mapiulate a workspace&#8217;s configuration options. These options include all of the elements listed in thr configuration summary. </p>
<p> By default, the <code>config</code> verb gets and sets options for a workspace&#8217;s <i>active</i> profile. If no profiles have been specified for a workspace, this is a default profile named <code>default</code>. </p>
<p> <code>NOTE:</code> Calling <code>catkin config</code> on an uninitialied workspace will not automatically initialize it unless it is used with the <code>&#8211;init</code> option.</p>
<h3>Viewing the Configuration Summary</h3>
<p> Once a workspace has been initialized, the configuration summary can be displayed by calling <code>catkin config</code> without arguments from anywhere under the root of the workspace. Doing so will not modify your workspace. The <code>catkin</code> command is context-sensitive, so it will determine which workspace contains the current working directory.</p>
<h3>Appending or Removing List-Type Arguments</h3>
<p> Several configuration options are actually <i>lists</i> of values. Normally for these options, the given values will replace the current values in the configuration. </p>
<p> If you would only like to modify, but not replace the value of a list-type option, you can use the <code>-a</code> / <code>&#8211;append-args</code> and <code>-r</code> / <code>&#8211;remove-args</code> options to append or remove elements from these lists, respectively. </p>
<p> List-type options include:</p>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;cmake-args</code></p>
<dt>&bull;</p>
<dd> <code>&#8211;make-args</code></p>
<dt>&bull;</p>
<dd> <code>&#8211;catkin-make-args</code></p>
<dt>&bull;</p>
<dd> <code>&#8211;whitelist</code></p>
<dt>&bull;</p>
<dd> <code>&#8211;blacklist</code></dl>
<h3>Installing Packages</h3>
<p> Without any additional arguments, packages are not &quot;installed&quot; using the standard CMake <code>install()</code> targets. Addition of the <code>&#8211;install</code> option will configure a workspace so that it creates an <code>install space</code> and write the products of all install targets to that FHS tree. The contents of the <code>install space</code>, which, by default, is located in a directory named <code>install</code> will look like the following: </p>
<pre>
$ ls ./install
_setup_util.py bin            env.sh         etc            include
lib            setup.bash     setup.sh       setup.zsh      share
</pre>
<h3>Explicitly Specifying Workspace Chaining</h3>
<p> Normally, a catkin workspace automatically &quot;extends&quot; the other workspaces that have previously been sourced in your environment. Each time you source a catkin setup file from a result-space (devel-space or install-space), it sets the <code>$CMAKE_PREFIX_PATH</code> in your environment, and this is used to build the next workspace. This is also sometimes referred to as &quot;workspace chaining&quot; and sometimes the extended workspace is referred to as a &quot;parent&quot; workspace. </p>
<p> With <code>catkin config</code>, you can explicitly set the workspace you want to extend, using the <code>&#8211;extend</code> argument. This is equivalent to sourcing a setup file, building, and then reverting to the environment before sourcing the setup file. </p>
<p> Note that in case the desired parent workspace is different from one already being used, using the <code>&#8211;extend</code> argument also necessitates cleaning the setup files from your workspace with <code>catkin clean</code>. </p>
<p> For example, regardless of your current environment variable settings (like <code>$CMAKE_PREFIX_PATH</code>), this will build your workspace against the <code>/opt/ros/hydro</code> install space. </p>
<p> First start with an empty <code>CMAKE_PREFIX_PATH</code> and initialize, build, and source a workspace: </p>
<p>$ echo $CMAKE_PREFIX_PATH<br />
        $ mkdir &#8211;<br />
    p / tmp / path / to / my_catkin_ws / src $ cd / tmp / path / to / my_catkin_ws $ catkin init&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None Workspace : / tmp / path / to / my_catkin_ws&#8230; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;$ cd / tmp / path / to / my_catkin_ws $ catkin create pkg aaa $ catkin create pkg bbb $ catkin create pkg ccc $ catkin build&#8230; $ source devel / setup.bash $ echo $CMAKE_PREFIX_PATH / tmp / path / to / my_catkin_ws / devel $ catkin config&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None Workspace : / tmp / path / to / my_catkin_ws&#8230; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<p> At this point you have a workspace which doesn&#8217;t extend anything. If you realize this after the fact, you can explicitly tell it to extend another workspace. Suppose you wanted to extend a standard ROS system install like <code>/opt/ros/hydro</code>. This can be done with the <code>&#8211;extend</code> option: </p>
<p>$ catkin config&#8211; extend / opt / ros / hydro&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : [explicit] / opt / ros / hydro Workspace : / tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel Install Space : [missing] / tmp / path / to / my_catkin_ws / install DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Whitelisted Packages : None Blacklisted Packages : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;$ catkin clean&#8211; setup &#8211; files<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        $ catkin build&#8230; $ source devel /<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    setup.bash<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        $ echo $CMAKE_PREFIX_PATH /<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    tmp / path / to / my_catkin_ws : / opt / ros / hydro</p>
<h3>Whitelisting and Blacklisting Packages</h3>
<p> Packages can be added to a package <i>whitelist</i> or <i>blacklist</i> in order to change which packages get built. If the <i>whitelist</i> is non-empty, then a call to <code>catkin build</code> with no specific package names will only build the packages on the <i>whitelist</i>. This means that you can still build packages not on the <i>whitelist</i>, but only if they are named explicitly or are dependencies of other whitelisted packages. </p>
<p> To set the whitelist, you can call the following command: </p>
<p> To clear the whitelist, you can use the <code>&#8211;no-whitelist</code> option: </p>
<pre>
catkin config --no-whitelist
</pre>
<p> If the <i>blacklist</i> is non-empty, it will filter the packages to be built in all cases except where a given package is named explicitly. This means that blacklisted packages will not be built even if another package in the workspace depends on them. </p>
<p> <code>NOTE:</code> Blacklisting a package does not remove it&#8217;s build directory or build products, it only pevents it from being rebuilt. </p>
<p> To set the blacklist, you can call the following command: </p>
<p> To clear the blacklist, you can use the <code>&#8211;no-blacklist</code> option: </p>
<pre>
catkin config --no-blacklist
</pre>
<p> Note that you can still build packages on the blacklist and whitelist by passing their names to <code>catkin build</code> explicitly.</p>
<h3>Full Command-Line Interface</h3>
<p>usage: catkin config [-h] [&#8211;workspace WORKSPACE] [&#8211;profile PROFILE]<br />
                     [&#8211;append-args | &#8211;remove-args] [&#8211;init]<br />
                     [&#8211;extend EXTEND_PATH | &#8211;no-extend] [&#8211;mkdirs]<br />
                     [&#8211;whitelist PKG [PKG &#8230;] | &#8211;no-whitelist]<br />
                     [&#8211;blacklist PKG [PKG &#8230;] | &#8211;no-blacklist]<br />
                     [-s SOURCE_SPACE | &#8211;default-source-space]<br />
                     [-b BUILD_SPACE | &#8211;default-build-space]<br />
                     [-d DEVEL_SPACE | &#8211;default-devel-space]<br />
                     [-i INSTALL_SPACE | &#8211;default-install-space]<br />
                     [-x SPACE_SUFFIX] [&#8211;isolate-devel | &#8211;merge-devel]<br />
                     [&#8211;install | &#8211;no-install]<br />
                     [&#8211;isolate-install | &#8211;merge-install]<br />
                     [&#8211;parallel-jobs PARALLEL_JOBS]<br />
                     [&#8211;cmake-args ARG [ARG &#8230;] | &#8211;no-cmake-args]<br />
                     [&#8211;make-args ARG [ARG &#8230;] | &#8211;no-make-args]<br />
                     [&#8211;catkin-make-args ARG [ARG &#8230;] |<br />
                     &#8211;no-catkin-make-args]<br />
This verb is used to configure a catkin workspace&#8217;s configuration and layout.<br />
Calling `catkin config` with no arguments will display the current config and<br />
affect no changes if a config already exists for the current workspace and<br />
profile.<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;workspace WORKSPACE, -w WORKSPACE<br />
                        The path to the catkin_tools workspace or a directory<br />
                        contained within it (default: &#8220;.&#8221;)<br />
  &#8211;profile PROFILE     The name of a config profile to use (default: active<br />
                        profile)<br />
Behavior:<br />
  Options affecting argument handling.<br />
  &#8211;append-args, -a     For list-type arguments, append elements.<br />
  &#8211;remove-args, -r     For list-type arguments, remove elements.<br />
Workspace Context:<br />
  Options affecting the context of the workspace.<br />
  &#8211;init                Initialize a workspace if it does not yet exist.<br />
  &#8211;extend EXTEND_PATH, -e EXTEND_PATH<br />
                        Explicitly extend the result-space of another catkin<br />
                        workspace, overriding the value of $CMAKE_PREFIX_PATH.<br />
  &#8211;no-extend           Un-set the explicit extension of another workspace as<br />
                        set by &#8211;extend.<br />
  &#8211;mkdirs              Create directories required by the configuration (e.g.<br />
                        source space) if they do not already exist.<br />
Package Build Defaults:<br />
  Packages to include or exclude from default build behavior.<br />
  &#8211;whitelist PKG [PKG &#8230;]<br />
                        Set the packages on the whitelist. If the whitelist is<br />
                        non-empty, only the packages on the whitelist are<br />
                        built with a bare call to `catkin build`.<br />
  &#8211;no-whitelist        Clear all packages from the whitelist.<br />
  &#8211;blacklist PKG [PKG &#8230;]<br />
                        Set the packages on the blacklist. Packages on the<br />
                        blacklist are not built with a bare call to `catkin<br />
                        build`.<br />
  &#8211;no-blacklist        Clear all packages from the blacklist.<br />
Spaces:<br />
  Location of parts of the catkin workspace.<br />
  -s SOURCE_SPACE, &#8211;source-space SOURCE_SPACE<br />
                        The path to the source space.<br />
  &#8211;default-source-space<br />
                        Use the default path to the source space (&#8220;src&#8221;)<br />
  -b BUILD_SPACE, &#8211;build-space BUILD_SPACE<br />
                        The path to the build space.<br />
  &#8211;default-build-space<br />
                        Use the default path to the build space (&#8220;build&#8221;)<br />
  -d DEVEL_SPACE, &#8211;devel-space DEVEL_SPACE<br />
                        Sets the target devel space<br />
  &#8211;default-devel-space<br />
                        Sets the default target devel space (&#8220;devel&#8221;)<br />
  -i INSTALL_SPACE, &#8211;install-space INSTALL_SPACE<br />
                        Sets the target install space<br />
  &#8211;default-install-space<br />
                        Sets the default target install space (&#8220;install&#8221;)<br />
  -x SPACE_SUFFIX, &#8211;space-suffix SPACE_SUFFIX<br />
                        Suffix for build, devel, and install space if they are<br />
                        not otherwise explicitly set.<br />
Devel Space:<br />
  Options for configuring the structure of the devel space.<br />
  &#8211;isolate-devel       Build products from each catkin package into isolated<br />
                        devel spaces.<br />
  &#8211;merge-devel         Build products from each catkin package into a single<br />
                        merged devel spaces.<br />
Install Space:<br />
  Options for configuring the structure of the install space.<br />
  &#8211;install             Causes each package to be installed to the install<br />
                        space.<br />
  &#8211;no-install          Disables installing each package into the install<br />
                        space.<br />
  &#8211;isolate-install     Install each catkin package into a separate install<br />
                        space.<br />
  &#8211;merge-install       Install each catkin package into a single merged<br />
                        install space.<br />
Build Options:<br />
  Options for configuring the way packages are built.<br />
  &#8211;parallel-jobs PARALLEL_JOBS, &#8211;parallel PARALLEL_JOBS, -p PARALLEL_JOBS<br />
                        Maximum number of packages which could be built in<br />
                        parallel (default is cpu count)<br />
  &#8211;cmake-args ARG [ARG &#8230;]<br />
                        Arbitrary arguments which are passes to CMake. It must<br />
                        be passed after other arguments since it collects all<br />
                        following options.<br />
  &#8211;no-cmake-args       Pass no additional arguments to CMake.<br />
  &#8211;make-args ARG [ARG &#8230;]<br />
                        Arbitrary arguments which are passes to make.It must<br />
                        be passed after other arguments since it collects all<br />
                        following options.<br />
  &#8211;no-make-args        Pass no additional arguments to make (does not affect<br />
                        &#8211;catkin-make-args).<br />
  &#8211;catkin-make-args ARG [ARG &#8230;]<br />
                        Arbitrary arguments which are passes to make but only<br />
                        for catkin packages.It must be passed after other<br />
                        arguments since it collects all following options.<br />
  &#8211;no-catkin-make-args<br />
                        Pass no additional arguments to make for catkin<br />
                        packages (does not affect &#8211;make-args).</p>
<h2>CATKIN CREATE &#8212; CREATE PACKAGES</h2>
<p> This verb enables you to quickly create workspace elements like boilerplate Catkin packages.</p>
<h3>Full Command-Line Interface</h3>
<p>usage : catkin create[-h]{pkg}&#8230; Creates a catkin workspace<br />
            positional arguments : {pkg} sub &#8211;<br />
                                   command help<br />
                                       pkg Create a catkin package.optional arguments : -h,<br />
    &#8211;help show this help message and exit</p>
<p>usage: catkin create pkg [-h] [&#8211;rosdistro ROSDISTRO] [-v MAJOR.MINOR.PATCH]<br />
                         [-l LICENSE] [-m NAME EMAIL] [-a NAME EMAIL]<br />
                         [-d DESCRIPTION] [&#8211;catkin-deps [DEP [DEP &#8230;]]]<br />
                         [&#8211;system-deps [DEP [DEP &#8230;]]]<br />
                         [&#8211;boost-components [COMP [COMP &#8230;]]]<br />
                         PKGNAME<br />
Create a new Catkin package. Note that while the default options used by this<br />
command are sufficient for prototyping and local usage, it is important that<br />
any publically-available packages have a valid license and a valid maintainer<br />
e-mail address.<br />
positional arguments:<br />
  PKGNAME               The name of the package to create. This name should be<br />
                        completely lower-case with individual words separated<br />
                        by undercores.<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;rosdistro ROSDISTRO<br />
                        The ROS distro (default: environment variable<br />
                        ROS_DISTRO if defined)<br />
Package Metadata:<br />
  -v MAJOR.MINOR.PATCH, &#8211;version MAJOR.MINOR.PATCH<br />
                        Initial package version. (default 0.0.0)<br />
  -l LICENSE, &#8211;license LICENSE<br />
                        The software license under which the code is<br />
                        distributed, such as BSD, MIT, GPLv3, or others.<br />
                        (default: &#8220;TODO&#8221;)<br />
  -m NAME EMAIL, &#8211;maintainer NAME EMAIL<br />
                        A maintainer who is responsible for the package.<br />
                        (default: [username, username [at] todo.todo]) (multiple<br />
                        allowed)<br />
  -a NAME EMAIL, &#8211;author NAME EMAIL<br />
                        An author who contributed to the package. (default: no<br />
                        additional authors) (multiple allowed)<br />
  -d DESCRIPTION, &#8211;description DESCRIPTION<br />
                        Description of the package. (default: empty)<br />
Package Dependencies:<br />
  &#8211;catkin-deps [DEP [DEP &#8230;]], -c [DEP [DEP &#8230;]]<br />
                        The names of one or more Catkin dependencies. These<br />
                        are Catkin-based packages which are either built as<br />
                        source or installed by your system&#8217;s package manager.<br />
  &#8211;system-deps [DEP [DEP &#8230;]], -s [DEP [DEP &#8230;]]<br />
                        The names of one or more system dependencies. These<br />
                        are other packages installed by your operating<br />
                        system&#8217;s package manager.<br />
C++ Options:<br />
  &#8211;boost-components [COMP [COMP &#8230;]]<br />
                        One or more boost components used by the package.</p>
<h2>CATKIN INIT &#8212; INITIALIZE A WORKSPACE</h2>
<p> The <code>init</code> verb is the simplest way to &quot;initialize&quot; a catkin workspace so that it can be automatically detected automatically by other verbs which need to know the location of the workspace root. </p>
<p> This verb does not store any configuration information, but simply creates the hidden <code>.catkin_tools</code> directory in the specified workspace. If you want to initialize a workspace simultaneously with an initial config, see the <code>&#8211;init</code> option for the <code>config</code> verb. </p>
<p> Catkin workspaces can be initialized anywhere. The only constraint is that catkin workspaces cannot contain other catkin workspaces. If you call <code>caktin init</code> and it reports an error saying that the given directory is already contained in a workspace, you can call <code>catkin config</code> to determine the root of that workspace.</p>
<h3>Full Command-Line Interface</h3>
<p>usage: catkin init [-h] [&#8211;workspace WORKSPACE] [&#8211;profile PROFILE] [&#8211;reset]<br />
Initializes a given folder as a catkin workspace<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;workspace WORKSPACE, -w WORKSPACE<br />
                        The path to the catkin_tools workspace or a directory<br />
                        contained within it (default: &#8220;.&#8221;)<br />
  &#8211;reset               Reset (delete) all of the metadata for the given<br />
                        workspace.</p>
<h2>CATKIN LIST &#8212; LIST PACKAGE INFO</h2>
<p> The <code>list</code> verb for the <code>catkin</code> command is used to find and list information about catkin packages. By default, it will list the packages in the workspace containing the current working directoy. It can also be used to list the packages in any other arbitrary directory.</p>
<h3>Checking for Catkin Package Warnings</h3>
<p> In addition to the names of the packages in your workspace, running <code>catkin list</code> will output any warnings about catkin packages in your workspace. To suppress these warnings, you can use the <code>&#8211;quiet</code> option.</p>
<h3>Using Unformatted Output in Shell Scripts</h3>
<p> <code>catkin list &#8211;unformatted</code> is useful for automating shell scripts in UNIX pipe-based programs.</p>
<h3>Full Command-Line Interface</h3>
<p>usage : catkin list[-h][&#8211;deps][&#8211;depends &#8211; on[DEPENDS_ON[DEPENDS_ON&#8230;]]]<br />
                   [folders[folders&#8230;]] Lists catkin packages in the workspace or<br />
        other arbitray folders.positional arguments : folders Folders in which to find packages.(default<br />
                                                                                                 : cwd)<br />
                                                          optional arguments : -h,<br />
    &#8211;help show this help message and exit<br />
    &#8212; deps,<br />
    &#8211;dependencies<br />
        List dependencies of each package.&#8211;depends<br />
        &#8211; on[DEPENDS_ON[DEPENDS_ON&#8230;]] List all packages that depend on supplied argument<br />
          package(s)<br />
              .&#8211;quiet Don&#8217;t print out detected package warnings. &#8211;unformatted,<br />
    -u Print list without punctuation and additional details.</p>
<h2>CATKIN PROFILE &#8212; MANAGE PROFILES</h2>
<p> Many verbs contain a <code>&#8211;profile</code> option, which selects which configuration profile to use, without which it will use the &quot;active&quot; profile. The <code>profile</code> verb enables you to manager the available profiles as well as set the &quot;active&quot; profile when using other verbs. </p>
<p> Even without using the <code>profile</code> verb, any use of the <code>catkin</code> command which changes the workspace is impliclty using a configuration profile called &quot;default&quot;. </p>
<p> The <code>profile</code> verb has several sub-commands for profile management. These include the following:</p>
<dl>
<dt>&bull;</p>
<dd> <code>list</code> &#8212; List the available profiles</p>
<dt>&bull;</p>
<dd> <code>set</code> &#8212; Set the active profile by name.</p>
<dt>&bull;</p>
<dd> <code>add</code> &#8212; Add a new profile by name.</p>
<dt>&bull;</p>
<dd> <code>rename</code> &#8212; Rename a given profile.</p>
<dt>&bull;</p>
<dd> <code>remove</code> &#8212; Remove a profile by name.</dl>
<h3>Creating Profiles Automatically</h3>
<p> After initializing a workspace, you can start querying information about profiles. Until you execute a verb which actually writes a profile configuration, however, there will be no profiles listed: </p>
<pre>
$ mkdir -p /tmp/path/to/my_catkin_ws/src
$ cd /tmp/path/to/my_catkin_ws
$ catkin init
$ catkin profile list
[profile] This workspace has no metadata profiles. Any configuration
settings will automatically by applied to a new profile called `default`.
</pre>
<p> To see these effects, you can run <code>catkin config</code> to write a default configuration to the workspace: </p>
<p>$ cd / tmp / path / to / my_catkin_ws $ catkin config&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : default Extending : None Workspace : / tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel Install Space : [missing] / tmp / path / to / my_catkin_ws / install DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;$ catkin profile list[profile] Available profiles : -default(active)</p>
<p> The <code>profile</code> verb now shows that the profile named &quot;default&quot; is avialable and is active. Calling <code>catkin config</code> with the <code>&#8211;profile</code> argument will automatically create a profile based on the given configuration options: </p>
<p>$ catkin config&#8211; profile alternate &#8211; x _alt&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Profile : alternate Extending : None Workspace : / tmp / path / to / my_catkin_ws Source Space : [exists] / tmp / path / to / my_catkin_ws / src Build Space : [missing] / tmp / path / to / my_catkin_ws / build_alt Devel Space : [missing] / tmp / path / to / my_catkin_ws / devel_alt Install Space : [missing] / tmp / path / to / my_catkin_ws / install_alt DESTDIR : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Isolate Develspaces : False Install Packages : False Isolate Installs : False&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Additional CMake Args : None Additional Make Args : None Additional catkin Make Args : None&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Workspace configuration appears valid.&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;$ catkin profile list[profile] Available profiles : -alternate &#8211; default(active)</p>
<p> Note that while the profile named <code>alternate</code> has been configured, it is still not <i>active</i>, so any calls to catkin-verbs without an explicit <code>&#8211;profile alternate</code> option will still use the profile named <code>default</code>.</p>
<h3>Explicitly Creating Profiles</h3>
<p> Profiles can also be added explicitly with the <code>add</code> command. This profile can be initialized with configuration information from either the default settings or another profile. </p>
<p>$ catkin profile list<br />
        [profile] Available profiles : -alternate &#8211;<br />
                                       default(active)<br />
                                           $ catkin profile add alternate_2&#8211; copy alternate<br />
                                               [profile] Created a new profile named alternate_2 based on profile alternate<br />
                                                   [profile] Available profiles : -alternate<br />
                                                                                  &#8211;<br />
                                                                                  alternate_2<br />
                                                                                  &#8211;<br />
                                                                                  default(active)</p>
<h3>Setting the Active Profile</h3>
<p> The active profile can be easily set with the <code>set</code> sub-command. Suppose a workspace has the following profiles: </p>
<p>$ catkin profile list<br />
        [profile] Available profiles : -alternate &#8211;<br />
                                       alternate_2 &#8211; default(active) $ catkin profile set alternate_2[profile] Activated catkin metadata profile : alternate_2[profile] Available profiles : -alternate<br />
                                                                                                                                                                                             &#8211;<br />
                                                                                                                                                                                             alternate_2(active) &#8211; default</p>
<h3>Renaming and Removing Profiles</h3>
<p> The <code>profile</code> verb can also be used for renaming and removing profiles: </p>
<p>$ catkin profile list<br />
        [profile] Available profiles : -alternate &#8211;<br />
                                       alternate_2(active) &#8211; default $ catkin profile rename alternate_2 alternate2[profile] Renamed profile alternate_2 to alternate2[profile] Available profiles : -alternate<br />
                                                                                                                                                                                                     &#8211;<br />
                                                                                                                                                                                                     alternate2(active) &#8211; default $ catkin profile remove alterate[profile] Removed profile : alternate[profile] Available profiles : -alternate2(active) &#8211; default</p>
<h3>Full Command-Line Interface</h3>
<p>usage: catkin profile [-h] [&#8211;workspace WORKSPACE]<br />
                      {list,set,add,rename,remove} &#8230;<br />
Manage metadata profiles for a catkin workspace<br />
positional arguments:<br />
  {list,set,add,rename,remove}<br />
                        sub-command help<br />
    list                List the available profiles.<br />
    set                 Set the active profile by name.<br />
    add                 Add a new profile by name.<br />
    rename              Rename a given profile.<br />
    remove              Remove a profile by name.<br />
optional arguments:<br />
  -h, &#8211;help            show this help message and exit<br />
  &#8211;workspace WORKSPACE, -w WORKSPACE<br />
                        The path to the catkin workspace. Default: current<br />
                        working directory</p>
<h3><code>catkin profile list</code></h3>
<pre>
usage: catkin profile list [-h]
optional arguments:
  -h, --help  show this help message and exit
</pre>
<h3><code>catkin profile set</code></h3>
<pre>
usage: catkin profile set [-h] name
positional arguments:
  name        The profile to activate.
optional arguments:
  -h, --help  show this help message and exit
</pre>
<h3><code>catkin profile add</code></h3>
<p>usage : catkin profile add[-h][-f][&#8211;copy BASE_PROFILE | &#8211;copy &#8211; active] name<br />
            positional arguments : name The new profile name.optional arguments : -h,<br />
    &#8211;help show this help message and exit &#8211; f, &#8211;force Overwrite an existing profile.&#8211;copy BASE_PROFILE Copy the settings from an existing profile.(default<br />
                                                                                                                                                      : None)&#8211; copy<br />
                                                    &#8211; active Copy the settings from the active profile.</p>
<h3><code>catkin profile rename</code></h3>
<p>usage: catkin profile rename [-h] [-f] current_name new_name<br />
positional arguments:<br />
  current_name  The current name of the profile to be renamed.<br />
  new_name      The new name for the profile.<br />
optional arguments:<br />
  -h, &#8211;help    show this help message and exit<br />
  -f, &#8211;force   Overwrite an existing profile.</p>
<h3><code>catkin profile remove</code></h3>
<p>usage : catkin profile remove[-h][name[name&#8230;]] positional arguments : name One or more profile names to remove.optional arguments : -h, &#8211;help show this help message and exit</p>
<h2>SHELL SUPPORT IN CATKIN COMMAND</h2>
<p> You can use the command <code>catkin &#8211;locate-extra-shell-verbs</code> to locate the shell file for your installation. When you source the resulting file, you can use <code>bash</code>/<code>zsh</code> shell functions which provide added utility. </p>
<pre>
. `catkin --locate-extra-shell-verbs`
</pre>
<p> Provided verbs are:</p>
<dl>
<dt>&bull;</p>
<dd> <code>catkin cd</code> &#8212; Change to package directory in source space.</p>
<dt>&bull;</p>
<dd> <code>catkin source</code> &#8212; Source the develspace or installspace of the containing workspace.</dl>
<h3>Full Command-Line Interface</h3>
<p> Change to package directory in source space with <i>cd</i> verb. </p>
<pre>
usage: catkin cd [ARGS...]
ARGS are any valid catkin locate arguments
</pre>
<p> The <i>source</i> verb sources the develspace or installspace of the containing workspace. </p>
<p>usage : catkin source[-w / path / to / ws] Sources setup.sh in the workspace.optional arguments : -w[/ path / to / ws] Source setup.sh from given workspace.</p>
<h2>VERB ALIASING</h2>
<p> The <code>catkin</code> command allows you to define your own verb &quot;aliases&quot; which expand to more complex expressions including built-in verbs, command-line options, and other verb aliases. These are processed before any other command-line processing takes place, and can be useful for making certain use patterns more convenient.</p>
<h3>The Built-In Aliases</h3>
<p> You can list the available aliases using the <code>&#8211;list-aliases</code> option to the <code>catkin</code> command. Below are the built-in aliases as displayed by this command: </p>
<pre>
$ catkin --list-aliases
b: build
bt: b --this
ls: list
install: config --install
</pre>
<h3>Defining Additional Aliases</h3>
<p> Verb aliases are defined in the <code>verb_aliases</code> subdirectory of the catkin config folder, <code>~/.config/catkin/verb_aliases</code>. Any YAML files in that folder (files with a <code>.yaml</code> extension) will be processed as definition files. </p>
<p> These files are formatted as simple YAML dictionaries which map aliases to expanded expressions, which must be composed of other <code>catkin</code> verbs, options, or aliases: </p>
<pre>
&lt;ALIAS&gt;: &lt;EXPRESSION&gt;
</pre>
<p> For example, aliases which configure a workspace profile so that it ignores the value of the <code>CMAKE_PREFIX_PATH</code> environment variable, and instead <i>extends</i> one or another ROS install spaces could be defined as follows: </p>
<p>#~/.config / catkin / verb_aliases / 10 &#8211; ros &#8211; distro &#8211; aliases.yaml<br />
extend &#8211; sys : config&#8211; profile sys&#8211; extend / opt / ros / hydro &#8211; x _sys extend &#8211; overlay : config&#8211; profile overlay&#8211; extend ~ / ros / hydro / install &#8211; x _overlay</p>
<p> After defining these aliases, one could use them with optional additional options and build a given configuration profile. </p>
<pre>
$ catkin extend-overlay
$ catkin profile set overlay
$ catkin build some_package
</pre>
<p> <code>NOTE:</code> The <code>catkin</code> command will initialize the <code>verb_aliases</code> directory with a file named <code>00-default-aliases.yaml</code> containing the set of built-in aliases. These defaults can be overridden by adding additional definition files, but the default alias file should not be modified since any changes to it will be over-written by invocations of the <code>catkin</code> command.</p>
<h3>Alias Precedence and Overriding Aliases</h3>
<p> Verb alias files in the <code>verb_aliases</code> directory are processed in alphabetical order, so files which start with larger numbers will override files with smaller numbers. In this way you can override the built-in aliases using a file which starts with a number higher than <code>00-</code>. </p>
<p> For example, the <code>bt: build &#8211;this</code> alias exists in the default alias file, <code>00-default-aliases.yaml</code>, but you can create a file to override it with an alternate definition defined in a file named <code>01-my-aliases.yaml</code>. </p>
<pre>
# ~/.config/catkin/verb_aliases/01-my-aliases.yaml
# Override `bt` to build with no deps
bt: build --this --no-deps
</pre>
<p> You can also disable or unset an alias by setting its value to <code>null</code>. For example, the <code>ls: list</code> alias is defined in the default aliases, but you can override it with this entry in a custom file named something like <code>02-unset.yaml</code>: </p>
<pre>
# ~/.config/catkin/verb_aliases/02-unset.yaml
# Disable `ls` alias
ls: null
</pre>
<h3>Recursive Alias Expansion</h3>
<p> Additionally, verb aliases can be recursive, for instance in the <code>bt</code> alias, the <code>b</code> alias expands to <code>build</code> so that <code>b &#8211;this</code> expands to <code>build &#8211;this</code>. The <code>catkin</code> command shows the expansion of aliases when they are invoked so that their behavior is more transparent: </p>
<p>$ catkin bt == &gt; Expanding alias &#8216;bt&#8217; from &#8216;catkin bt&#8217; to &#8216;catkin b &#8211;this&#8217; == &gt; Expanding alias &#8216;b&#8217; from &#8216;catkin b &#8211;this&#8217; to &#8216;catkin build &#8211;this&#8217; &#8230;</p>
<h2>EXTENDING THE CATKIN COMMAND</h2>
<p> The <code>catkin</code> command is setup to be easily extended using the <code>setuptools</code> notion of <code>entry_points</code>, see: <i><a rel="nofollow" href="http://guide.python-distribute.org/creation.html#entry-points">http://guide.python-distribute.org/creation.html#entry-points</a></i> By using the <code>entry_points</code> extensions to the <code>catkin</code> command can be made within the <code>catkin_tools</code> package or an external package. Regardless of what package the <code>entry_point</code> is defined in, it will be defined in the <code>setup.py</code> of that package, and will take this form: </p>
<p>from setuptools import setup<br />
setup(<br />
    &#8230; entry_points = {<br />
        &#8230; &#8216;catkin_tools.commands.catkin.verbs&#8217; : [<br />
#Example from catkin_tools&#8217; setup.py:<br />
#&#8217;list = catkin_tools.verbs.catkin_list:description&#8217;,<br />
            &#8216;my_verb = my_package.some.module:description&#8217;,<br />
        ],<br />
    }, )</p>
<p> This entry in the <code>setup.py</code> places a file in the <code>PYTHONPATH</code> when either the <code>install</code> or the <code>develop</code> verb is given to <code>setup.py</code>. This file relates the key (in this case <code>my_verb</code>) to a module and attribute (in this case <code>my_package.some.module</code> and <code>description</code>). Then the <code>catkin</code> command will use the <code>pkg_resources</code> modules to retrieve these mapping at run time. Any entry for the <code>catkin_tools.commands.catkin.verbs</code> group must point to a <code>description</code> attribute of a module, where the <code>description</code> attribute is a <code>dict</code>. The <code>description</code> <code>dict</code> should take this form (the description from the <code>build</code> verb for example): </p>
<pre>
description = dict(
    verb='build',
    description=&quot;Builds a catkin workspace&quot;,
    main=main,
    prepare_arguments=prepare_arguments,
    argument_preprocessor=argument_preprocessor,
)
</pre>
<p> This <code>dict</code> defines all the information that the <code>catkin</code> command needs to provide and execute your verb. The <code>verb</code> key takes a string which is the verb name (as shown in help and used for invoking the verb). The <code>description</code> key takes a string which is the description which is shown in the <code>catkin -h</code> output. The <code>main</code> key takes a callable (function) which is called when the verb is invoked. The signature of the main callable should be like this: </p>
<pre>
def main(opts):
    # ...
    return 0
</pre>
<p> Where the <code>opts</code> parameter is the <code>Namespace</code> object returns from <code>ArgumentParser.parse_args(&#8230;)</code> and should return an exit code which is passed to <code>sys.exit</code>. </p>
<p> The <code>prepare_arguments</code> key takes a function with this signature: </p>
<pre>
def prepare_arguments(parser):
    add = parser.add_argument
    # What packages to build
    add('packages', nargs='*',
        help='Workspace packages to build, package dependencies are built as well unless --no-deps is used. '
             'If no packages are given, then all the packages are built.')
    add('--no-deps', action='store_true', default=False,
        help='Only build specified packages, not their dependencies.')
    return parser
</pre>
<p> The above example is a snippet from the <code>build</code> verb&#8217;s <code>prepare_arguments</code> function. The purpose of this function is to take a given <code>ArgumentParser</code> object, which was created by the <code>catkin</code> command, and add this verb&#8217;s <code>argparse</code> arguments to it and then return it. </p>
<p> Finally, the <code>argument_preprocessor</code> command is an optional entry in the <code>description</code> <code>dict</code> which has this signature: </p>
<p>def argument_preprocessor(args)<br />
    : &#8220;&#8221;<br />
      &#8220;Processes the arguments for the build verb, before being passed to argparse&#8221;<br />
      &#8220;&#8221;<br />
#CMake / make pass &#8211; through flags collect dashed options.They require special<br />
#handling or argparse will complain about unrecognized options.<br />
      args = sys.argv [1:] if args is None else args<br />
             extract_make_args = extract_cmake_and_make_and_catkin_make_arguments args,<br />
      cmake_args, make_args, catkin_make_args = extract_make_args(args)<br />
#Extract make jobs flags.<br />
                                 jobs_flags = extract_jobs_flags(&#8216; &#8216;.join(args)) if jobs_flags : args = re.sub(jobs_flags, &#8221;, &#8216; &#8216;.join(args)).split() jobs_flags = jobs_flags.split()<br />
                                                                                                                                                                        extras = {<br />
                                     &#8216;cmake_args&#8217; : cmake_args,<br />
                                     &#8216;make_args&#8217; : make_args + (jobs_flags or []),<br />
                                     &#8216;catkin_make_args&#8217; : catkin_make_args,<br />
                                 } return args,<br />
      extras</p>
<p> The above example is the <code>argument_preprocessor</code> function for the <code>build</code> verb. The purpose of the <code>argument_preprocessor</code> callable is to allow the verb to preprocess its own arguments before they are passed to <code>argparse</code>. In the case of the <code>build</code> verb, it is extracting the CMake and Make arguments before having them passed to <code>argparse</code>. The input parameter to this function is the list of arguments which come after the verb, and this function is only called when this verb has been detected as the first positional argument to the <code>catkin</code> command. So, you do not need to worry about making sure the arguments you just got are yours. This function should return a tuple where the first item in the tuple is the potentially modified list of arguments, and the second item is a dictionary of keys and values which should be added as attributes to the <code>opts</code> parameter which is later passed to the <code>main</code> callable. In this way you can take the arguments for your verb, parse them, remove some, add some or whatever, then you can additionally return extra information which needs to get passed around the <code>argparse</code> <code>parse_args</code> function. Most verbs should not need to do this, and in fact the built-in <code>list</code> verb&#8217;s <code>description</code> <code>dict</code> does not include one: </p>
<pre>
description = dict(
    verb='list',
    description=&quot;Lists catkin packages in a given folder&quot;,
    main=main,
    prepare_arguments=prepare_arguments,
)
</pre>
<p> Hopefully, this information will help you get started when you want to extend the <code>catkin</code> command with custom verbs. </p>
<p> This Python package provides command line tools for working with the catkin meta-buildsystem and catkin workspaces. </p>
<p> <code>NOTE:</code> This is the documentation for the <code>catkin</code> command-line tool and <code>not</code> the Catkin package specification documentation. For documentation on writing catkin packages, see: <i><a rel="nofollow" href="http://docs.ros.org/api/catkin/html/">http://docs.ros.org/api/catkin/html/</a></i></p>
<h2>THE CATKIN COMMAND</h2>
<p> The <code>catkin</code> Command-Line Interface (CLI) tool is the single point of entry for most of the functionality provided by this package. All invocations of the <code>catkin</code> CLI tool take this form: </p>
<pre><code>
$ catkin[global options]&lt;verb&gt;[verb arguments and options]
</code></pre>
<p> The different capabilities of the <code>catkin</code> CLI tool are organized into different sub-command &quot;verbs.&quot; This is similar to common command-line tools such as <code>git</code> or <code>apt-get</code>. Verbs include actions such as <code>build</code> which builds a catkin workspace or <code>list</code> which simply lists the catkin packages found in one or more folders. </p>
<p> Additionally, global options can be provided before the verb, options like <code>-d</code> for debug level verbosity or <code>-h</code> for help on the <code>catkin</code> CLI tool itself. Verbs can take arbitrary arguments and options, but they must all come after the verb. For more help on the usage of a particular verb, simply pass the <code>-h</code> or <code>&#8211;help</code> option after the verb.</p>
<h3>Built-in <code>catkin</code> command verbs</h3>
<p> Each of the following verbs is built-in to the <code>catkin</code> command and has its own detailed documentation:</p>
<dl>
<dt>&bull;</p>
<dd> <code>build &#8212; Build packages in a catkin workspace</code></p>
<dt>&bull;</p>
<dd> <code>config &#8212; Configure a catkin workspace&#8217;s layout and settings</code></p>
<dt>&bull;</p>
<dd> <code>clean &#8212; Clean products generated in a catkin workspace</code></p>
<dt>&bull;</p>
<dd> <code>create &#8212; Create structures like Catkin packages</code></p>
<dt>&bull;</p>
<dd> <code>init &#8212; Initialize a catkin workspace</code></p>
<dt>&bull;</p>
<dd> <code>list &#8212; Find and list information about catkin packages in a workspace</code></p>
<dt>&bull;</p>
<dd> <code>profile &#8212; Manage different named configuration profiles</code></dl>
<h3>Shell support in <code>catkin</code> command</h3>
<p> If you are using <code>bash</code> or <code>zsh</code>, then you can source an extra setup file to gain access to some additional verbs. For more information see: <code>advanced/catkin_shell_verbs</code>.</p>
<h3>Extending the <code>catkin</code> command</h3>
<p> If you would like to add a verb to the <code>catkin</code> command without modifying its source, please read <code>development/extending_the_catkin_command</code>.</p>
<h2>AUTHOR</h2>
<p> William Woodall</p>
<h2>COPYRIGHT</h2>
<p> 2014, Open Source Robotics Foundation, Inc. </p>
<h2>Index</h2>
<dt><a href="#lbAI">QUICKSTART</a></p>
<dd>
<dt><a href="#lbAP">WORKSPACE MECHANICS</a></p>
<dd>
<dt><a href="#lbBF">CONFIGURATION SUMMARY</a></p>
<dd>
<dt><a href="#lbBO">CHEAT SHEET</a></p>
<dd>
<dt><a href="#lbBX">TROUBLESHOOTING</a></p>
<dd>
<dt><a href="#lbCD">CATKIN BUILD &#8212; BUILD PACKAGES</a></p>
<dd>
<dt><a href="#lbCS">CATKIN CLEAN &#8212; CLEAN BUILD PRODUCTS</a></p>
<dd>
<dt><a href="#lbCU">CATKIN CONFIG &#8212; CONFIGURE A WORKSPACE</a></p>
<dd>
<dt><a href="#lbDB">CATKIN CREATE &#8212; CREATE PACKAGES</a></p>
<dd>
<dt><a href="#lbDD">CATKIN INIT &#8212; INITIALIZE A WORKSPACE</a></p>
<dd>
<dt><a href="#lbDF">CATKIN LIST &#8212; LIST PACKAGE INFO</a></p>
<dd>
<dt><a href="#lbDJ">CATKIN PROFILE &#8212; MANAGE PROFILES</a></p>
<dd>
<dt><a href="#lbDU">SHELL SUPPORT IN CATKIN COMMAND</a></p>
<dd>
<dt><a href="#lbDW">VERB ALIASING</a></p>
<dd>
<dt><a href="#lbEB">EXTENDING THE CATKIN COMMAND</a></p>
<dd>
<dt><a href="#lbEC">THE CATKIN COMMAND</a></p>
<dd>
<dt><a href="#lbEG">AUTHOR</a></p>
<dd>
<dt><a href="#lbEH">COPYRIGHT</a></p>
<dd></dl>
