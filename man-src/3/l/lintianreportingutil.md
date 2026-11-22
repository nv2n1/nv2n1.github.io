---
title: "lintianreportingutil(3)"
name: "lintianreportingutil"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianreportingutil/"
description: "Lintian::Reporting::Util – Lintian utility functions"
---

<p>Lintian::Reporting::Util &#8211; Lintian utility functions </p>
<h2>Synopsis</h2>
<pre> use Lintian::Reporting::Util qw(load_state_cache find_backlog);
 my $cache = load_state_cache('path/to/state-dir');
 my @backlog = find_backlog('2.12', $cache);</pre>
<h2>Description</h2>
<p>This module contains a number of utility subs that are nice to have for the reporting framework, but on their own did not warrant their own module. </p>
<p> Most subs are imported only on request.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>load_state_cache(STATE_DIR)</dt>
<dd>[Reporting tools only] Load the state cache from STATE_DIR.</dd>
<dt>save_state_cache(STATE_DIR, STATE)</dt>
<dd>[Reporting tools only] Save the STATE cache to STATE_DIR.</dd>
<dt>find_backlog(LINTIAN_VERSION, STATE)</dt>
<dd>[Reporting tools only] Given the current lintian version and the harness state, return a list of group ids that are part of the backlog. The list is sorted based on what version of Lintian processed the package. </dd>
<p> Note the result is by design not deterministic to reduce the risk of all large packages being in the same run (e.g. like gcc-5 + gcc-5-cross + gcc-6 + gcc-6-cross).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
</p>