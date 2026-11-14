---
title: "stdstudent_t_distributionstudent_t_distribution(3)"
name: "stdstudent_t_distributionstudent_t_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstudent_t_distributionstudent_t_distribution/"
description: "std::student_t_distribution<RealType>::student_t_distribution – std::student_t_distribution<RealType>::student_t_distribution"
---

<p>std::student_t_distribution&lt;RealType&gt;::student_t_distribution &#8211; std::student_t_distribution&lt;RealType&gt;::student_t_distribution</p>
<h2>Synopsis</h2>
<p>student_t_distribution() : <a href="/docs/linux/man/1-student_t_distribution/">student_t_distribution</a><code>(1)</code> {} (1) <i>(since C++11)</i><br />
explicit student_t_distribution( RealType n ); <code>(2)</code> <i>(since C++11)</i><br />
explicit student_t_distribution( const param_type&amp; params ); <code>(3)</code> <i>(since C++11)</i><br />
Constructs a new distribution object. <code>(2)</code> uses n as the distribution parameter. <code>(3)</code> uses params as the distribution parameter. </p>
<h2>Parameters</h2>
<p>n &#8211; the n distribution parameter (degrees of freedom)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
