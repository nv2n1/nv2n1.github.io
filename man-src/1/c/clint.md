---
title: "clint(1)"
name: "clint"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clint/"
description: "clint – Clint Documentation"
---

<h2>NAME</h2>
<p> clint &#8211; Clint Documentation </p>
<p> Welcome to Clint.</p>
<h2>CONTENTS</h2>
<p> This part of the documentation, which is mostly prose, begins with some background information about Clint, then focuses on step-by-step instructions for using Clint for development.</p>
<h3>Properly Installing Python</h3>
<h3>Mac OS X</h3>
<p> <i>Or, &quot;Installing Python 2.7 via Homebrew&quot;.</i> </p>
<p> One of the reasons everybody loves Python is the interactive shell. It basically allows you to execute Python commands in real time and immediately get results back. Flask itself does not come with an interactive shell, because it does not require any specific setup upfront, just import your application and start playing around.</p>
<h3>Package Manager</h3>
<p> While Snow Leopard comes with a large number of UNIX utilities, those familiar with Linux systems will notice one key component missing: a package manager. Mxcl&#8217;s <i>Homebrew</i> is the answer. </p>
<p> To install Homebrew, simply run: </p>
<pre>
$ ruby -e &quot;$(curl -fsS <a rel="nofollow" href="http://gist.github.com/raw/323731/install_homebrew.rb)">http://gist.github.com/raw/323731/install_homebrew.rb)</a>&quot;
</pre>
<p> It&#8217;s basic commands are <code>update</code>, <code>install</code>, and <code>remove</code>.</p>
<h3>Python Interpreter</h3>
<p> And we can now install Python 2.7: </p>
<pre>
$ brew install python --framework
</pre>
<p> The <code>&#8211;framework</code> option tells Homebrew to compile a Framework-style Python build, rather than a UNIX-style build. The outdated version of Python that Snow Leopard comes packaged with is built as a Framework, so this helps avoid some future module installation bugs. </p>
<p> <i>Don&#8217;t forget to update your environment PATH.</i></p>
<h3>Distribute &amp; Pip</h3>
<p> <i>Distribute</i> is a fantastic drop-in replacement for <i>easy_install</i> and <i>setuptools</i>. It allows you to install and manage python packages from pypi.python.org, amongst a few other sources. It also plays well with <i>virtualenv</i> and user-enviornments. </p>
<p> <code>easy_install</code> is considered by many to be a deprecated system, so we will install it&#8217;s replacement: <code>pip</code>. Pip allows for uninstallation of packages, and is actively maintained, unlike setuptool&#8217;s easy_install. </p>
<p> To install <i>pip</i> and Distribute&#8217;s <i>easy_install</i>: </p>
<p> If you have homebrew: </p>
<pre>
$ brew install pip
</pre>
<p> &#8230;And, if you&#8217;re a mas****st: </p>
<pre>
$ curl -O <a rel="nofollow" href="http://python-distribute.org/distribute_setup.py">http://python-distribute.org/distribute_setup.py</a>
$ python distribute_setup.py
$ easy_install pip
</pre>
<p> To install <code>pip</code>: </p>
<p> Hopefully you&#8217;ll never have to use <code>easy_install</code> again.</p>
<h3>Updating Python</h3>
<p> Homebrew makes it simple. </p>
<pre>
$ brew update
$ brew install --force python
</pre>
<h3>Windows</h3>
<h3>Prerequisites:</h3>
<dl>
<dt>&bull;</p>
<dd> Python2.7 (x86) from Python.org</p>
<dt>&bull;</p>
<dd> Microsoft Visual Studio</dl>
<h3>Step 1: Install Distribute &amp; Pip</h3>
<p> <code>Distribute</code> is a fantastic drop-in replacement for <code>easy_install</code> and <code>setuptools</code>. It allows you to install and manage python packages from PyPi, amongst a few other sources.</p>
<dl>
<dt><code>To install it, run the python script available here:</code></p>
<dd> &lt;<i><a rel="nofollow" href="http://python-distribute.org/distribute_setup.py">http://python-distribute.org/distribute_setup.py</a></i>&gt; </p>
<p> Make sure that <code>`C:\Python27\`</code>, and <code>`C:\Python27\Scripts`</code> are in your PATH. </p>
<p> <code>easy_install</code> is considered by many to be a deprecated system, so we will install it&#8217;s replacement: <code>pip</code>. Pip allows for uninstallation of packages, and is actively maintained, unlike setuptool&#8217;s easy_install. </p>
<p> To install pip, simply run: </p>
<pre>
$ easy_install pip
</pre>
</dl>
<h3>Linux (Ubuntu)</h3>
<h3>Linux (Manual)</h3>
<h3>Useful Tools</h3>
<h3>IPython</h3>
<pre>
$ pip install ipython
</pre>
<h3>BPython</h3>
<pre>
$ pip install bpython
</pre>
<h2>API DOCUMENTATION</h2>
<p> api</p>
<h2>ADDITIONAL NOTES</h2>
<p> Contribution notes and legal information are here for the interested.</p>
<h3>Contribute</h3>
<p> Python-guide is under active development, and contributors are welcome. </p>
<p> If you have a feature request, suggestion, or bug report, please open a new issue on <i>GitHub</i>. To submit patches, please send a pull request on <i>GitHub</i>. Make sure you add yourself to <i>AUTHORS</i>. </p>
<p> If you&#8217;d like to contribute, there&#8217;s plenty to do. Here&#8217;s a short todo list.</p>
<h3>License</h3>
<p> TBD.</p>
<h2>AUTHOR</h2>
<p> Kenneth Reitz</p>
<h2>COPYRIGHT</h2>
<p> 2011, Kenneth Reitz </p>
<h2>Index</h2>
