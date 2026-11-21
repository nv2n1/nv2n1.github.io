---

title: "pyvenv-3(1)"
name: "pyvenv-3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pyvenv-3/"
description: "pyvenv-3.3 – create virtual python environments"
---

<p> pyvenv-3.3 &#8211; create virtual python environments </p>
<h2>DESCRIPTION</h2>
<p> usage: venv [-h] [&#8211;system-site-packages] [&#8211;symlinks] [&#8211;clear] [&#8211;upgrade]</p>
<dl>
<dt>
</dt><dd> ENV_DIR [ENV_DIR &#8230;]</dd></dl>
<p> Creates virtual Python environments in one or more target directories.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ENV_DIR</dt>
<dd> A directory to create the environment in.</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>&#8211;system-site-packages</code></dt>
<dd> Give the virtual environment access to the system site-packages dir.</dd>
<dt><code>&#8211;symlinks</code></dt>
<dd> Attempt to symlink rather than copy.</dd>
<dt><code>&#8211;clear</code></dt>
<dd> Delete the environment directory if it already exists. If not specified and the directory exists, an error is raised.</dd>
<dt><code>&#8211;upgrade</code></dt>
<dd> Upgrade the environment directory to use this version of Python, assuming Python has been upgraded in-place. </dd>
</dl>
