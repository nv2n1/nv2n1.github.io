---
title: "fcstrcopyfilename(3)"
name: "fcstrcopyfilename"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrcopyfilename/"
description: "FcStrCopyFilename – create a complete path from a filename"
---

<p>FcStrCopyFilename &#8211; create a complete path from a filename </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcStrCopyFilename (const FcChar8 *</code><i>s</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcStrCopyFilename</code> constructs an absolute pathname from <i>s</i>. It converts any leading &#8216;~&#8217; characters in to the value of the HOME environment variable, and any relative paths are converted to absolute paths using the current working directory. Sequences of &#8216;/&#8217; characters are converted to a single &#8216;/&#8217;, and names containing the current directory &#8216;.&#8217; or parent directory &#8216;..&#8217; are correctly reconstructed. Returns NULL if &#8216;~&#8217; is the leading character and HOME is unset or disabled (see <code>FcConfigEnableHome</code>).</p>
