---

title: "euca-download-bundle(1)"
name: "euca-download-bundle"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-download-bundle/"
description: "euca-download-bundle – Download a bundled image from the cloud"
---

<h2>NAME</h2>
<p> euca-download-bundle &#8211; Download a bundled image from the cloud</p>
<p> euca-download-bundle [-d DIR] [&#8211;progress | <code>&#8211;no-progress]</code> <code>-b</code></p>
<dl>
<dt>BUCKET[/PREFIX]</dt>
<dd> (<code>-m</code> MANIFEST | <code>-p</code> MANIFEST | <code>&#8211;local-manifest</code> FILE) [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<p> Download a bundled image from the cloud</p>
<h2>DESCRIPTION</h2>
<p> You must run euca-unbundle-image on the bundle you download to obtain the original image.</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-d</code> DIR, <code>&#8211;directory</code> DIR</dt>
<dd> the directory to download the bundle parts to, or &quot;-&quot; to write the bundled image to stdout</dd>
<dt><code>&#8211;progress</code></dt>
<dd> show progress (the default when run interactively)</dd>
<dt><code>&#8211;no-progress</code></dt>
<dd> do not show progress (the default when run noninteractively)</dd>
<dt><code>-b</code> BUCKET[/PREFIX], <code>&#8211;bucket</code> BUCKET[/PREFIX]</dt>
<dd> the bucket that contains the bundle, with an optional path prefix (required)</dd>
<dt><code>-m</code> MANIFEST, <code>&#8211;manifest</code> MANIFEST</dt>
<dd> the manifest&#8217;s complete file name, not including any path that may be specified using <code>-b</code></dd>
<dt><code>-p</code> MANIFEST, <code>&#8211;prefix</code> MANIFEST</dt>
<dd> the portion of the manifest&#8217;s file name that precedes &quot;.manifest.xml&quot;</dd>
<dt><code>&#8211;local-manifest</code> FILE</dt>
<dd> use a manifest on disk and ignore any that appear on the server</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> object storage service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
