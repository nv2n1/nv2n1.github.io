---
title: "bloom(1)"
name: "bloom"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bloom/"
description: "bloom – bloom Documentation"
---

<h2>NAME</h2>
<p> bloom &#8211; bloom Documentation</p>
<h2>WHAT IS BLOOM?</h2>
<p> Bloom is a release automation tool, designed to make generating platform specific release artifacts from source projects easier. Bloom is designed to work best with <i>catkin</i> projects, but can also accommodate other types of projects.</p>
<h2>HOW DOES IT WORK?</h2>
<p> Bloom works by importing your upstream source tree into a git repository, where it is manipulated and used to generate build artifacts for different platforms like Debian or Fedora. </p>
<p> First bloom gathers information about your source repository and creates an archive for the version you want to release. Then the archive is imported into the release repository, and the source tree is run through a release track where it is tagged, can be patched, and has platform specific artifacts generated for it. </p>
<p> The individual stages of these release tracks are tagged with git and those tags are used by build infrastructure and deployment systems.</p>
<h2>WHAT CAN I RELEASE WITH BLOOM?</h2>
<p> Bloom supports releasing arbitrary software packages, but is optimized for use with <i>catkin</i> projects. </p>
<p> <code>NOTE:</code> For <i>dry</i> ROS stacks, you should use the legacy <i>ros-release</i> system.</p>
<h2>HOW DO I INSTALL BLOOM?</h2>
<p> On Ubuntu the recommended method is to use apt: </p>
<pre>
$ sudo apt-get install python-bloom
</pre>
<p> On other systems you can install bloom via pypi: </p>
<pre>
$ sudo pip install -U bloom
</pre>
<p> Note: pip will not notify you of updates, but bloom will notify you when you are using a version of bloom that is not the latest released.</p>
<h2>HOW DO I RELEASE SOMETHING WITH BLOOM?</h2>
<p> Please refer to the documentation and tutorials on the <i>bloom</i> ROS wiki page.</p>
<h2>AUTHOR</h2>
<p> William Woodall</p>
<h2>COPYRIGHT</h2>
<p> 2014, Open Source Robotics Foundation </p>
<h2>Index</h2>
