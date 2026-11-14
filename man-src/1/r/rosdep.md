---
title: "rosdep(1)"
name: "rosdep"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rosdep/"
description: "rosdep – rosdep command"
---

<h2>NAME</h2>
<p> rosdep &#8211; rosdep command</p>
<h2>SYNOPSIS</h2>
<p> <code>rosdep</code> &lt;<i>command</i>&gt; [<i>options</i>] [<i>args</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>rosdep</code> command helps you install external dependencies in an OS-independent manner. For example, what Debian packages do you need in order to get the OpenGL headers on Ubuntu? How about OS X? Fedora? rosdep can answer this question for your platform and install the necessary package(s). </p>
<p> For more information on rosdep, see <i><a rel="nofollow" href="http://ros.org/wiki/rosdep">http://ros.org/wiki/rosdep</a></i>. </p>
<p> Run &quot;rosdep -h&quot; or &quot;rosdep &lt;command&gt; -h&quot; to access the built-in tool documentation.</p>
<h2>COMMANDS</h2>
<p> <code>check &lt;packages&gt;&#8230;</code> Check if the dependencies of ROS package(s) have been met. </p>
<p> <code>install &lt;packages&gt;&#8230;</code> Install dependencies for specified ROS packages. </p>
<p> <code>db &lt;packages&gt;&#8230;</code> Display the dependency database for package(s). </p>
<p> <code>keys &lt;packages&gt;&#8230;</code> List the rosdep keys that the ROS packages depend on. </p>
<p> <code>what-needs &lt;rosdeps&gt;&#8230;</code> Print a list of packages that declare a rosdep on (at least one of) &lt;rosdeps&gt; </p>
<p> <code>where-defined &lt;rosdeps&gt;&#8230;</code> Print a list of YAML files that declare a rosdep on (at least one of) &lt;rosdeps&gt;</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;os=OS_NAME:OS_VERSION</code> Override OS name and version (colon-separated), e.g. ubuntu:lucid </p>
<p> <code>-i, &#8211;include_duplicates</code> Do not deduplicate </p>
<p> <code>-a, &#8211;all</code> Select all ROS packages. Only valid for commands that take &lt;packages&gt; as arguments. </p>
<p> <code>-h, &#8211;help</code> Show usage information </p>
<p> <code>-v, &#8211;verbose</code> Enable verbose output</p>
<h2>INSTALL OPTIONS</h2>
<p> <code>&#8211;reinstall</code> (re)install all dependencies, even if already installed </p>
<p> <code>-y, &#8211;default-yes</code> Tell the package manager to default to y or fail when installing </p>
<p> <code>-s, &#8211;simulate</code> Simulate install </p>
<p> <code>-r</code> Continue installing despite errors.</p>
<h2>AUTHOR</h2>
<p> Tully Foote, Ken Conley</p>
<h2>COPYRIGHT</h2>
<p> 2011, Willow Garage </p>
<h2>Index</h2>
