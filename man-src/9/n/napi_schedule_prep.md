---
title: "napi_schedule_prep(9)"
name: "napi_schedule_prep"
section: "9"
letter: "n"
url: "/docs/linux/man/9-napi_schedule_prep/"
description: "napi_schedule_prep – check if NAPI can be scheduled"
---

<p>napi_schedule_prep &#8211; check if NAPI can be scheduled</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool napi_schedule_prep(struct napi_struct&nbsp;<wbr>*&nbsp;<wbr></code><i>n</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>n</i></p>
<dl>
<dd>
<dd>NAPI context</dl>
<h2>Description</h2>
<p>Test if NAPI routine is already running, and if not mark it as running. This is used as a condition variable to insure only one NAPI poll instance runs. We also make sure there is no pending NAPI disable.</p>
<h2>Copyright</h2>
