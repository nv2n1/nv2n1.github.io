---
title: "gen_estimator_active(9)"
name: "gen_estimator_active"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gen_estimator_active/"
description: "gen_estimator_active – test if estimator is currently in use"
---

<p>gen_estimator_active &#8211; test if estimator is currently in use</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool gen_estimator_active(const struct gnet_stats_basic_packed&nbsp;<wbr>*&nbsp;<wbr></code><i>bstats</i><code>, const struct gnet_stats_rate_est64&nbsp;<wbr>*&nbsp;<wbr></code><i>rate_est</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>bstats</i></p>
<dl>
<dd>
<dd>basic statistics</dl>
<p> <i>rate_est</i></p>
<dl>
<dd>rate estimator statistics</dl>
<h2>Description</h2>
<p>Returns true if estimator is active, and false if not.</p>
<h2>Copyright</h2>
