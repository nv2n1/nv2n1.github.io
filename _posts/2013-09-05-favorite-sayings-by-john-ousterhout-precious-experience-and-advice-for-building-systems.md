---
title: "Measuring System Performance: Lessons from Ousterhout"
date: 2013-09-05 06:32:57 +0000
modified: 2026-04-11 17:41:27 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /favorite-sayings-by-john-ousterhout-precious-experience-and-advice-for-building-systems/
---

John Ousterhout, a professor of computer science at Stanford, maintains a collection of “Favorite Sayings” grounded in decades of building real systems—RAMCloud, Tcl, and extensive work in distributed systems. These aren’t abstract principles. They’re lessons that apply directly to the work of building, debugging, and shipping software at scale.

## Optimize After Measurement, Not Before

The most dangerous instinct in software engineering is premature optimization. Ousterhout is direct about this:

> Most real-world programs run plenty fast enough on today’s machines without any particular attention to performance. The real challenges are getting programs completed quickly, ensuring their quality, and managing the complexity of large applications. Thus the primary design criterion for software should be simplicity, not speed.

The mechanism is clear: optimizing during initial construction adds complexity, delays delivery, and usually doesn’t help. Algorithms with better big-O complexity often carry larger constant factors. They’re slower on realistic problem sizes until you reach the scale where they matter—which you probably won’t reach without measurement telling you so.

The discipline is unforgiving:

> If you try to optimize during initial construction you will add complexity that impacts timely delivery and quality, and probably won’t help performance at all. Don’t worry about performance until the application is running; if it isn’t fast enough, then measure carefully to figure out where the bottlenecks are. They are likely in places you wouldn’t have guessed. Tune only the places where you have measured that there is an issue.

This applies everywhere: kernel tuning, application profiling, database queries, network behavior. Your intuition about where the slowness lives will be wrong. Measure first. Always.

## Intuition Is Pattern-Matching, Not Prophecy

Intuition has real value—it’s distilled experience, the pattern-matching that comes from seeing many similar problems. But it’s also easy to mistake confidence for accuracy:

> Intuition is wonderful once you have acquired knowledge and experience. You get gut-level feelings about the right way to handle situations, and these can save time and effort. However, it’s easy to become overconfident and assume intuition is infallible, which leads to mistakes.

Performance debugging is where this breaks down most visibly. A developer looks at a system under load and thinks: “Obviously the database lock is the bottleneck.” They add connection pooling, implement caching, lock-free data structures. Six weeks of work. Then they measure and discover the actual bottleneck was network latency to an external service, or garbage collection pauses, or disk I/O contention.

The antidote: separate observation from action. Measure. Identify the actual constraint. Then change only what matters.

## You Need Facts Before You Can Build Concepts

Understanding doesn’t come from first principles alone:

> Before you can appreciate or develop a concept you need to observe a large number of facts related to the concept. This has implications both for teaching and for working in unfamiliar areas.

This is why junior engineers struggle when asked to optimize unfamiliar code—they lack the foundation of observed behavior. No metrics. No logs. No understanding of how the system actually behaves under load. It’s also why cargo-cult configuration management fails: teams copy patterns from other deployments without understanding what the metrics actually show, then wonder why the copy doesn’t work in their environment.

Build your foundation in facts first. Logs. Traces. Metrics. Then concepts become actionable.

## Confirm Bugs Are Fixed, Not Just Masked

A specific discipline applies to verification:

> Don’t ever assume that a problem has been fixed until you can identify the exact lines of code that caused it and convince yourself that the particular code really explains the behavior you have seen. Ideally you should create a test case that reliably reproduces the problem, make your fix, and then use that test case to verify that the problem is gone.

This is elementary in principle and routinely violated in practice. A service restart that masks the issue temporarily. A change that seems to help without addressing the root cause. A race condition that disappears in staging but reappears under production load. A memory leak that only surfaces after hours of operation.

The discipline: reproduce reliably first. Fix specifically second. Verify with the reproducer third. Don’t move on until the reproducer passes.

## The Real Timeline: Initial Build Is Only 50% of the Work

Shipping code is not completion:

> When you think you are finished with a software project (coded, tested, documented, and ready for QA or production use) you are really only 50-75% done. If you spent 3 months in initial construction, plan on spending another 4-8 weeks in follow-up work.

This accounts for integration friction, edge cases that only appear under production load, usability problems that only real users discover, scaling issues that only emerge at actual traffic volumes. One way to compress this timeline: ship early with a skeletal but functional version. Real users and real traffic generate feedback while you’re still building, not after you’ve already declared the system “done.”

## Quality Requires Sustained Iteration

No software is built correctly on the first pass:

> No software is ever gotten right the first time. The only way to produce high-quality software is to keep improving and improving it. There are 2 kinds of software in the world: software that starts out crappy and eventually becomes great, and software that starts out crappy and stays that way.

The difference isn’t the initial implementation. It’s sustained investment in measurement, feedback, and refinement. It’s paying attention to what actually happens in production, not assuming your tests caught everything.

## Additional Principles Worth Internalizing

**On intermittent failures:** “The only thing worse than a problem that happens all the time is a problem that doesn’t happen all the time.” Bugs that appear randomly are almost always concurrency issues or environmental sensitivity. They require different debugging tools and more careful reasoning about system state.

**On credibility:** “If you admit that you don’t know the answer, or that you made a mistake, you build credibility. People are more likely to trust you when you say that you do have the answer, because they have seen that you don’t make things up.” This applies directly to incident response and operational work—your team will trust your analysis more if you’ve admitted uncertainty before.

**On system coherence:** “Coherent systems often have advantages of efficiency, which is why humans gravitate towards them. Unfortunately, coherent systems are unstable: if a problem arises it can wipe out the whole system very quickly.” Elegance and fragility often travel together. Sometimes resilience requires accepting some incoherence in your design—redundancy that seems wasteful, circuit breakers that seem crude, rate limiting that seems blunt.

The full collection is worth returning to regularly as you work through your own systems problems.
