---
title: "applydeltarpm(8)"
name: "applydeltarpm"
section: "8"
letter: "a"
url: "/docs/linux/man/8-applydeltarpm/"
description: "applydeltarpm – reconstruct an rpm from a deltarpm"
---

<p>applydeltarpm &#8211; reconstruct an rpm from a deltarpm </p>
<h2>Synopsis</h2>
<p><code>applydeltarpm</code> [<code>-v</code>] [<code>-p</code>] [<code>-r</code> <i>oldrpm</i>] <i>deltarpm</i> <i>newrpm</i><br />
 <code>applydeltarpm</code> <code>-c</code>|<code>-C</code> <i>deltarpm</i><br />
 <code>applydeltarpm</code> [<code>-c</code>|<code>-C</code>] <code>-s</code> <i>sequence</i><br />
 <code>applydeltarpm</code> <code>-i</code> <i>deltarpm</i> </p>
<h2>Description</h2>
<p>applydeltarpm applies a binary delta to either an old rpm or to on-disk data to re-create a new rpm. The old rpm can be specified with the <code>-r</code> option, if no rpm name is provided on-disk data is used. You can use <code>-p</code> to make applydeltarpm print the percentage of completion, or <code>-v</code> to make it more verbose about its operation. The second an third form can be used to check if the reconstruction is possible. It may fail if the on-disk data got changed (deltarpms are created in a way that config file changes do not matter) or the deltarpm does not match the rpm the delta was generated with. The <code>-c</code> option selects full (i.e. slow) on-disk checking, whereas <code>-C</code> only checks if the filesizes have not changed. Instead of a full deltarpm a sequence id can be given with the <code>-s</code> <i>sequence</i> option. Such an id contains all the information that is needed to do reconstruction checking. Finally information about a deltarpm can be printed with the <code>-i</code> option. </p>
<h2>Memory Considerations</h2>
<p>applydeltarpm was written to work on systems with limited memory. It uses a paging algorithm to keep the size of in-core data low and not bring the system in an out-of-memory situation.</p>
<h2>Exit Status</h2>
<p>applydeltarpm returns 0 if the rpm could be recreated or the checking succeeded, it returns 1 and prints an error message to stderr if something failed.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-makedeltarpm/">makedeltarpm</a></code>(8), <code><a href="/docs/linux/man/8-rpm/">rpm</a></code>(8) </p>
<h2>Author</h2>
<p>Michael Schroeder &lt;mls [at] suse.de&gt;</p>
